"""Orkestrator for kommunikasjon med LLM og tool-calling."""

import os
import re
import json
from dotenv import load_dotenv
from openai import OpenAI
from backend.tools import (
    derive, integrate, solve_equation, solve_ode, matrix_op, complex_op, TOOL_DEFINITIONS
)
from backend.formelsamling import FORMELSAMLING

load_dotenv()

MAKS_TOOL_RUNDER = 5  # øvre grense for tool-calling-løkken, unngår evighetsløkke

TOOL_MAP = {
    "derive": derive,
    "integrate": integrate,
    "solve_equation": solve_equation,
    "solve_ode": solve_ode,
    "matrix_op": matrix_op,
    "complex_op": complex_op,
}

_FORMELSAMLING_TEKST = "\n".join(
    f"{fid}: {f['navn']} – {f['formel']} – {f['bruk']} (ref: {f['referanse']})"
    for fid, f in FORMELSAMLING.items()
)

SYSTEM_PROMPT = (
    "Du er en matematikklærer for ingeniørstudenter. Bruk verktøyene (SymPy) til all beregning "
    "når oppgaven lar seg beregne slik – du skal ALDRI late som du har brukt et verktøy du ikke "
    "faktisk kalte. Kan oppgaven ikke beregnes (f.eks. et bevis eller en begrepsforklaring), "
    "resonnerer du i tekst og sier eksplisitt at svaret IKKE er verifisert av et verktøy. "
    "Forklar hvert steg pedagogisk på norsk, og oppgi nøyaktig hvilke formler/verktøy du faktisk "
    "brukte. Knytt hver formel-ID til steget der den brukes, og ta med navn og referanse fra "
    "formelsamlingen. Hvis du er usikker, si det eksplisitt.\n\n"
    "Formater alltid svaret slik:\n"
    "- Del løsningen i nummererte steg, hver på egen linje på formen "
    "'Steg 1: <forklaring>', 'Steg 2: <forklaring>', osv.\n"
    "- Når et steg bruker en formel fra formelsamlingen under, referer til formel-ID-en i "
    "hakeparentes rett i steget, f.eks. 'Steg 1: Vi deriverer med produktregelen [D1].' "
    "Bruk KUN ID-er som faktisk finnes i formelsamlingen under.\n\n"
    "Formelsamling (ID: navn – formel – bruk – referanse):\n" + _FORMELSAMLING_TEKST
)

_STEG_MØNSTER = re.compile(r"Steg\s+\d+\s*:\s*", re.IGNORECASE)
_FORMEL_ID_MØNSTER = re.compile(r"\[([A-ZÆØÅ]\d+)\]")


def _ekstraher_steg(svar_tekst: str) -> list:
    """Plukker ut innholdet mellom hver 'Steg N:'-markør (kan strekke seg over flere
    linjer, f.eks. når formelen står i en egen $$-blokk under). Faller tilbake til
    avsnitt eller hele svaret hvis modellen ikke fulgte steg-formatet."""
    deler = _STEG_MØNSTER.split(svar_tekst)
    if len(deler) > 1:
        return [d.strip() for d in deler[1:] if d.strip()]
    avsnitt = [a.strip() for a in svar_tekst.split("\n\n") if a.strip()]
    return avsnitt or ([svar_tekst.strip()] if svar_tekst.strip() else [])


def _ekstraher_formler(svar_tekst: str) -> list:
    """Plukker ut formel-ID-er modellen faktisk refererte til, og avviser ukjente ID-er."""
    sett = []
    for fid in _FORMEL_ID_MØNSTER.findall(svar_tekst):
        if fid in FORMELSAMLING and fid not in sett:
            sett.append(fid)
    return [
        {"id": fid, "navn": FORMELSAMLING[fid]["navn"], "referanse": FORMELSAMLING[fid]["referanse"]}
        for fid in sett
    ]


def solve_task(oppgave: str, use_tools: bool = True) -> dict:
    """Orkestrerer løsning av en matteoppgave ved hjelp av modell og verktøy.

    Merk: 'validert' settes IKKE her – det avgjøres av validator.py, kalt fra main.py,
    slik at valideringen sjekker det deterministiske verktøyresultatet, ikke fri tekst.
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("API_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
    model_name = os.getenv("MODEL_NAME", "gemini-1.5-flash")

    tomt_svar = {
        "svar": "Mangler API-nøkkel i .env-filen.",
        "steg": [],
        "formler_brukt": [],
        "tokens_brukt": 0,
        "estimert_kostnad": 0.0,
        "_verktoy_kall": None,
    }
    if not api_key:
        return tomt_svar

    client = OpenAI(api_key=api_key, base_url=base_url)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": oppgave},
    ]

    tools = TOOL_DEFINITIONS if use_tools else None
    tokens = 0
    siste_verktoy = None

    try:
        svar_tekst = ""
        for _ in range(MAKS_TOOL_RUNDER):
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                tools=tools,
            )
            msg = response.choices[0].message
            tokens += response.usage.total_tokens if response.usage else 0

            if not (use_tools and msg.tool_calls):
                svar_tekst = msg.content or ""
                break

            messages.append(msg)
            for tool_call in msg.tool_calls:
                func_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                tool_res = TOOL_MAP[func_name](**args)
                if "resultat" in tool_res:
                    siste_verktoy = {"navn": func_name, "args": args, "resultat": tool_res["resultat"]}
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(tool_res),
                })
        else:
            svar_tekst = msg.content or "Klarte ikke å fullføre svaret innen maks antall tool-kall."

        return {
            "svar": svar_tekst,
            "steg": _ekstraher_steg(svar_tekst),
            "formler_brukt": _ekstraher_formler(svar_tekst),
            "tokens_brukt": tokens,
            "estimert_kostnad": round(tokens * 0.000001, 6),
            "_verktoy_kall": siste_verktoy,
        }

    except Exception as e:
        return {
            "svar": f"Det oppstod en feil under behandling av oppgaven: {str(e)}",
            "steg": [],
            "formler_brukt": [],
            "tokens_brukt": 0,
            "estimert_kostnad": 0.0,
            "_verktoy_kall": None,
        }
