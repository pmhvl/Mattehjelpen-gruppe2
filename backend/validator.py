"""Numerisk validering av løsninger.

Sjekker om det FAKTISKE SymPy-verktøyresultatet stemmer med originaloppgaven,
ved å evaluere numerisk i tilfeldige testpunkter (SymPy subs/evalf).

VIKTIG: Vi validerer aldri modellens frie forklaringstekst direkte – naturlig
språk kan ikke sympifiseres pålitelig. Vi validerer verktøykallet (funksjon +
argumenter + resultat) som faktisk ble kjørt i tools.py. Ble ingen verktøy
brukt (f.eks. en bevisoppgave), sier vi ærlig fra at ingenting er verifisert.
"""

import re
import random
import sympy as sp


def _tilfeldige_punkter(n=3, lav=1.0, høy=10.0):
    return [round(random.uniform(lav, høy), 4) for _ in range(n)]


def _identitet_er_null(uttrykk, variabel, punkter, toleranse=1e-6):
    for p in punkter:
        try:
            verdi = complex(sp.N(uttrykk.subs(variabel, p)))
        except Exception:
            return False
        if abs(verdi) >= toleranse:
            return False
    return True


def _valider_derive(args, resultat_str, x, punkter):
    uttrykk = sp.sympify(args["uttrykk"])
    res = sp.sympify(resultat_str)
    ok = _identitet_er_null(sp.diff(uttrykk, x) - res, x, punkter)
    return ok, f"Sjekket at d/dx({args['uttrykk']}) == {resultat_str} i x = {punkter}."


def _valider_integrate(args, resultat_str, x, punkter):
    uttrykk = sp.sympify(args["uttrykk"])
    res = sp.sympify(resultat_str)
    ok = _identitet_er_null(sp.diff(res, x) - uttrykk, x, punkter)
    return ok, f"Sjekket at d/dx({resultat_str}) == {args['uttrykk']} i x = {punkter} (analysens fundamentalteorem)."


def _valider_solve_equation(args, resultat_str, x, punkter):
    ligning = args["ligning"]
    venstre, høyre = ligning.split("=") if "=" in ligning else (ligning, "0")
    uttrykk = sp.sympify(venstre) - sp.sympify(høyre)
    røtter = sp.sympify(resultat_str)
    røtter = list(røtter) if isinstance(røtter, (list, tuple)) else [røtter]
    if not røtter:
        return False, f"Ingen løsning å validere for {ligning}."
    avvik = [abs(complex(sp.N(uttrykk.subs(x, r)))) for r in røtter]
    ok = all(a < 1e-6 for a in avvik)
    return ok, f"Satte løsningen(e) {resultat_str} inn i {ligning}. Avvik: {[round(a, 8) for a in avvik]}."


def _valider_solve_ode(args, resultat_str, x, punkter):
    y = sp.Function("y")
    løsning_str = resultat_str.split("=")[-1] if "=" in resultat_str else resultat_str
    løsning = sp.sympify(løsning_str)

    eq_str = args["ligning"].replace("y''", "y(x).diff(x, 2)").replace("y'", "y(x).diff(x)")
    eq_str = re.sub(r"\by\b(?!\()", "y(x)", eq_str)
    namespace = {"sp": sp, "x": x, "y": y}
    venstre, høyre = eq_str.split("=") if "=" in eq_str else (eq_str, "0")
    uttrykk = eval(venstre, namespace) - eval(høyre, namespace)
    uttrykk = uttrykk.subs(y(x), løsning).doit()

    ok = _identitet_er_null(uttrykk, x, punkter)
    return ok, f"Satte løsningen inn i differensialligningen '{args['ligning']}' og sjekket at den blir ~0 i x = {punkter}."


def _valider_matrix_op(args, resultat_str, x, punkter):
    if args.get("operasjon") != "løs":
        return False, f"Matriseoperasjonen '{args.get('operasjon')}' har ingen numerisk valideringsregel ennå – ikke bekreftet."
    A = sp.Matrix(args["matrise"])
    b = sp.Matrix(args["vektor"])
    løsning = sp.sympify(resultat_str, locals={"Matrix": sp.Matrix})
    avvik = [abs(complex(sp.N(v))) for v in (A * løsning - b)]
    ok = all(a < 1e-6 for a in avvik)
    return ok, f"Satte løsningen inn i Ax=b. Avvik: {[round(a, 8) for a in avvik]}."


_VALIDATORER = {
    "derive": _valider_derive,
    "integrate": _valider_integrate,
    "solve_equation": _valider_solve_equation,
    "solve_ode": _valider_solve_ode,
    "matrix_op": _valider_matrix_op,
}


def validate(oppgave: str, svar: str, verktoy_kall: dict = None) -> dict:
    """Validerer numerisk ut fra det faktiske verktøykallet, ikke fri tekst.

    `verktoy_kall`: {"navn": tool-funksjonsnavn, "args": {...}, "resultat": str} for
    det siste tool-kallet solve_task gjorde, eller None hvis ingen verktøy ble brukt.
    """
    if not verktoy_kall or "resultat" not in verktoy_kall:
        return {
            "validert": False,
            "detaljer": (
                "Ingen verktøyberegning å validere numerisk (f.eks. en bevis-/begrepsoppgave, "
                "eller ingen tool-kall ble gjort). Svaret er IKKE bekreftet av et verktøy."
            ),
        }

    navn = verktoy_kall["navn"]
    args = verktoy_kall.get("args", {})
    resultat_str = verktoy_kall["resultat"]
    valideringsfunksjon = _VALIDATORER.get(navn)

    if valideringsfunksjon is None:
        return {
            "validert": False,
            "detaljer": f"Verktøyet '{navn}' har ingen numerisk valideringsregel ennå – ikke bekreftet.",
        }

    try:
        x = sp.Symbol(args.get("variabel", "x"))
        punkter = _tilfeldige_punkter()
        ok, detalj = valideringsfunksjon(args, resultat_str, x, punkter)
        return {"validert": bool(ok), "detaljer": detalj}
    except Exception as e:
        return {
            "validert": False,
            "detaljer": f"Kunne ikke validere numerisk automatisk: {str(e)}",
        }
