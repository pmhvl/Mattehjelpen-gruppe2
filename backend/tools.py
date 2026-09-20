"""Deterministiske matteverktøy (SymPy) for MatteHjelpen."""

import re
import sympy as sp

def derive(uttrykk: str, variabel: str = "x") -> dict:
    try:
        var = sp.Symbol(variabel)
        expr = sp.sympify(uttrykk)
        res = sp.diff(expr, var)
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved derivasjon: {str(e)}"}

def integrate(uttrykk: str, variabel: str = "x") -> dict:
    try:
        var = sp.Symbol(variabel)
        expr = sp.sympify(uttrykk)
        res = sp.integrate(expr, var)
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved integrasjon: {str(e)}"}

def solve_equation(ligning: str, variabel: str = "x") -> dict:
    try:
        var = sp.Symbol(variabel)
        if "=" in ligning:
            venstre, høyre = ligning.split("=")
            eq = sp.Eq(sp.sympify(venstre), sp.sympify(høyre))
        else:
            eq = sp.sympify(ligning)
        res = sp.solve(eq, var)
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved ligningsløsning: {str(e)}"}

def solve_ode(ligning: str) -> dict:
    try:
        x = sp.Symbol('x')
        y = sp.Function('y')  # ikke-anvendt funksjon – kallbar som y(x)

        # Støtt både y'/y''-notasjon og direkte SymPy-notasjon (y(x).diff(x, ...)).
        eq_str = ligning.replace("y''", "y(x).diff(x, 2)").replace("y'", "y(x).diff(x)")
        eq_str = re.sub(r"\by\b(?!\()", "y(x)", eq_str)

        namespace = {"sp": sp, "x": x, "y": y}
        if "=" in eq_str:
            venstre, høyre = eq_str.split("=")
            eq = sp.Eq(eval(venstre, namespace), eval(høyre, namespace))
        else:
            eq = eval(eq_str, namespace)

        res = sp.dsolve(eq, y(x))
        return {"resultat": str(res.rhs if hasattr(res, 'rhs') else res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved ODE-løsning: {str(e)}"}

def matrix_op(operasjon: str, matrise: list, vektor: list = None) -> dict:
    try:
        M = sp.Matrix(matrise)
        if operasjon == "determinant":
            res = M.det()
        elif operasjon == "invers":
            res = M.inv()
        elif operasjon == "egenverdier":
            res = M.eigenvals()
        elif operasjon == "løs":
            if vektor is None:
                return {"error": "Operasjonen 'løs' (Ax=b) krever argumentet 'vektor' (b)."}
            res = M.solve(sp.Matrix(vektor))
        else:
            return {"error": f"Ukjent matriseoperasjon: {operasjon}"}
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved matriseoperasjon: {str(e)}"}

def complex_op(operasjon: str, tall: str, n: int = None) -> dict:
    try:
        z = sp.sympify(tall)
        if operasjon == "polar":
            r = sp.Abs(z)
            theta = sp.arg(z)
            res = f"r = {r}, theta = {theta} (z = r*e^(i*theta))"
            latex_res = f"r = {sp.latex(r)}, \\theta = {sp.latex(theta)}"
        elif operasjon == "abs":
            res = str(sp.Abs(z))
            latex_res = sp.latex(sp.Abs(z))
        elif operasjon == "arg":
            res = str(sp.arg(z))
            latex_res = sp.latex(sp.arg(z))
        elif operasjon == "potens":
            if n is None:
                return {"error": "Operasjonen 'potens' krever heltallet 'n'."}
            res_expr = sp.expand_complex(z**n)
            res = str(res_expr)
            latex_res = sp.latex(res_expr)
        elif operasjon == "røtter":
            if n is None:
                return {"error": "Operasjonen 'røtter' krever heltallet 'n' (n-te røtter)."}
            r = sp.Abs(z)
            theta = sp.arg(z)
            røtter = [
                sp.simplify(r ** sp.Rational(1, n) * sp.exp(sp.I * (theta + 2 * sp.pi * k) / n))
                for k in range(n)
            ]
            res = ", ".join(str(rt) for rt in røtter)
            latex_res = ", \\quad ".join(sp.latex(rt) for rt in røtter)
        else:
            return {"error": f"Ukjent operasjon: {operasjon}"}
        return {"resultat": res, "latex": latex_res}
    except Exception as e:
        return {"error": f"Feil ved kompleks operasjon: {str(e)}"}

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "derive",
            "description": "Deriver et matematisk uttrykk mht en variabel.",
            "parameters": {
                "type": "object",
                "properties": {
                    "uttrykk": {"type": "string", "description": "Uttrykket som skal deriveres"},
                    "variabel": {"type": "string", "description": "Variabelen det skal deriveres mht."}
                },
                "required": ["uttrykk"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "integrate",
            "description": "Integrer et matematisk uttrykk mht en variabel.",
            "parameters": {
                "type": "object",
                "properties": {
                    "uttrykk": {"type": "string", "description": "Uttrykket som skal integreres"},
                    "variabel": {"type": "string", "description": "Variabelen det skal integreres mht."}
                },
                "required": ["uttrykk"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "solve_equation",
            "description": "Løs en matematisk ligning.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ligning": {"type": "string", "description": "Ligningen som skal løses"},
                    "variabel": {"type": "string", "description": "Variabelen det skal løses for"}
                },
                "required": ["ligning"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "solve_ode",
            "description": "Løs en ordiner differensialligning (ODE).",
            "parameters": {
                "type": "object",
                "properties": {
                    "ligning": {"type": "string", "description": "ODE-ligningen, f.eks. y' + y = 0"}
                },
                "required": ["ligning"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "matrix_op",
            "description": "Utfør en operasjon på en matrise. Bruk 'løs' for å løse et lineært ligningssystem Ax=b (krever 'vektor').",
            "parameters": {
                "type": "object",
                "properties": {
                    "operasjon": {"type": "string", "enum": ["determinant", "invers", "egenverdier", "løs"]},
                    "matrise": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}},
                    "vektor": {"type": "array", "items": {"type": "number"}, "description": "Høyresiden b i Ax=b. Kun nødvendig for operasjonen 'løs'."}
                },
                "required": ["operasjon", "matrise"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "complex_op",
            "description": "Utfør en operasjon på et komplekst tall: polarform/Eulers formel (polar), modulus (abs), argument (arg), potens (krever n) eller n-te røtter (røtter, krever n).",
            "parameters": {
                "type": "object",
                "properties": {
                    "operasjon": {"type": "string", "enum": ["polar", "abs", "arg", "potens", "røtter"]},
                    "tall": {"type": "string", "description": "Komplekst tall, f.eks. 1 + I"},
                    "n": {"type": "integer", "description": "Eksponent (potens) eller antall røtter (røtter). Påkrevd for disse to operasjonene."}
                },
                "required": ["operasjon", "tall"]
            }
        }
    }
]