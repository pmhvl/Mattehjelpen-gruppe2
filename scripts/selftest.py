"""Selvtest for MatteHjelpen – kjør etter hver fil dere fyller ut.

    python scripts/selftest.py            # vanlig kjøring underveis
    python scripts/selftest.py --strict   # streng sjekk før innlevering:
                                           # gjenstående ⏳ telles også som ikke bestått

Gir en fremdriftsoversikt: hva virker, hva mangler ennå, hva er faktisk feil.
Dette er IKKE en fasit-sjekker – den sjekker kontrakten (format på svarene),
ikke om matteoppgaven faktisk ble riktig løst. Regn kontroll for hånd innimellom!
"""

import argparse
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Støyende, ufarlig varsel fra fastapi.testclient (httpx/starlette) - ikke noe
# studenter trenger å bry seg om her.
warnings.filterwarnings("ignore", message="Using `httpx`")

OK = "\u2705"
TODO = "\u23f3"
FEIL = "\u274c"

results = []


def check(navn, fn):
    try:
        status, melding = fn()
    except NotImplementedError:
        status, melding = TODO, "Ikke implementert ennå – helt normalt i starten."
    except Exception as e:
        status, melding = FEIL, f"Kastet en feil: {e!r}"
    results.append((navn, status, melding))


def check_formelsamling():
    from backend.formelsamling import FORMELSAMLING

    n = len(FORMELSAMLING)
    for fid, f in FORMELSAMLING.items():
        for felt in ("navn", "formel", "referanse", "bruk"):
            if felt not in f:
                return FEIL, f"Formel '{fid}' mangler felt '{felt}'."
    if n < 10:
        return TODO, f"Kun {n} formler – oppgaven ber om ca. 15 (se PROMPTS/02_formelsamling.md)."
    return OK, f"{n} formler, alle med navn/formel/referanse/bruk."


def check_tool(fn_name, *args, **kwargs):
    def _run():
        from backend import tools

        fn = getattr(tools, fn_name, None)
        if fn is None:
            return FEIL, f"Funksjonen {fn_name} finnes ikke i tools.py."
        resultat = fn(*args, **kwargs)
        if not isinstance(resultat, dict) or "resultat" not in resultat or "latex" not in resultat:
            return FEIL, "Returnerer ikke {'resultat': ..., 'latex': ...}."
        return OK, f"OK – resultat={resultat['resultat']!r}"

    return _run


def check_tool_definitions():
    from backend import tools

    defs = getattr(tools, "TOOL_DEFINITIONS", None)
    if defs is None:
        return TODO, "TOOL_DEFINITIONS er ikke definert ennå."
    if not isinstance(defs, list) or not defs:
        return FEIL, "TOOL_DEFINITIONS bør være en ikke-tom liste."
    return OK, f"{len(defs)} tool-definisjoner funnet."


def check_validator():
    from backend.validator import validate

    resultat = validate("Eq(y(x).diff(x), y(x))", "y(x) = C1*exp(x)")
    if not isinstance(resultat, dict) or "validert" not in resultat:
        return FEIL, "Returnerer ikke {'validert': bool, ...}."
    return OK, f"OK – validert={resultat['validert']!r}"


def check_llm_client():
    from backend import llm_client

    if not hasattr(llm_client, "solve_task"):
        return FEIL, "solve_task mangler i llm_client.py."
    if not callable(llm_client.solve_task):
        return FEIL, "solve_task er ikke en funksjon."
    return OK, "solve_task finnes (kjøres ikke her – krever ekte API-kall/token)."


def check_api_contract():
    from unittest.mock import patch

    from fastapi.testclient import TestClient

    simulert_svar = {
        "svar": "2*x",
        "steg": ["Deriver uttrykket."],
        "formler_brukt": [],
        "tokens_brukt": 0,
        "estimert_kostnad": 0.0,
    }
    simulert_validering = {"validert": True, "detaljer": "Simulert selvtest."}

    with (
        patch("backend.llm_client.solve_task", return_value=simulert_svar),
        patch("backend.validator.validate", return_value=simulert_validering),
    ):
        from backend.main import app

        client = TestClient(app)
        r = client.post("/solve", json={"oppgave": "Deriver x**2"})
    if r.status_code != 200:
        return FEIL, f"POST /solve ga statuskode {r.status_code}."
    data = r.json()
    forventet_felt = {
        "svar",
        "steg",
        "formler_brukt",
        "validert",
        "tokens_brukt",
        "estimert_kostnad",
    }
    mangler = forventet_felt - data.keys()
    if mangler:
        return FEIL, f"Mangler felt i responsen: {sorted(mangler)}"
    if isinstance(data.get("svar"), str) and data["svar"].startswith("Ikke implementert"):
        return TODO, "Endepunktet svarer med riktig format, men bruker fortsatt placeholder-logikk."
    return OK, "POST /solve returnerer riktig format med et reelt svar."


def main():
    parser = argparse.ArgumentParser(description="Selvtest for MatteHjelpen")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Tell gjenstående ⏳ som ikke bestått (bruk før innlevering).",
    )
    args = parser.parse_args()

    print("MatteHjelpen – selvtest")
    print("=" * 40)

    check("Formelsamling (backend/formelsamling.py)", check_formelsamling)
    check("tools.derive", check_tool("derive", "x**2", "x"))
    check("tools.integrate", check_tool("integrate", "x**2", "x"))
    check("tools.solve_equation", check_tool("solve_equation", "x**2 - 4", "x"))
    check("tools.solve_ode", check_tool("solve_ode", "y(x).diff(x) + 4*y(x)"))
    check("tools.matrix_op", check_tool("matrix_op", "determinant", [[1, 2], [3, 4]]))
    check("tools.complex_op", check_tool("complex_op", "polar", "1+1j"))
    check("tools.TOOL_DEFINITIONS", check_tool_definitions)
    check("validator.validate", check_validator)
    check("llm_client.solve_task (finnes)", check_llm_client)
    check("API-kontrakt: POST /solve", check_api_contract)

    print()
    for navn, status, melding in results:
        print(f"{status}  {navn}")
        print(f"     {melding}")

    n_ok = sum(1 for _, s, _ in results if s == OK)
    n_todo = sum(1 for _, s, _ in results if s == TODO)
    n_feil = sum(1 for _, s, _ in results if s == FEIL)

    print()
    print("=" * 40)
    print(f"{n_ok} OK \u00b7 {n_todo} gjenstår \u00b7 {n_feil} feil av {len(results)} sjekker")

    if n_feil:
        print("\nNoe er implementert, men gir feil – se meldingene over.")
    elif n_todo:
        print("\nAlt som er implementert virker som det skal. Fortsett med neste modul!")
    else:
        print("\nAlle sjekker består! Husk å teste med ekte oppgaver i frontend også –")
        print("selvtesten sjekker format, ikke om matten faktisk ble riktig løst.")

    if n_feil or (args.strict and n_todo):
        sys.exit(1)


if __name__ == "__main__":
    main()
