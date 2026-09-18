"""Deterministiske matteverktøy (SymPy) for MatteHjelpen.

PRINSIPP: Modellen resonnerer – verktøyet regner. En språkmodell skal ALDRI
gjøre symbolsk/numerisk regning selv.
"""

import sympy as sp

def derive(uttrykk: str, variabel: str = "x") -> dict:
    """Deriver et uttrykk ved hjelp av SymPy."""
    try:
        var = sp.Symbol(variabel)
        expr = sp.sympify(uttrykk)
        res = sp.diff(expr, var)
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved derivasjon: {str(e)}"}

def integrate(uttrykk: str, variabel: str = "x") -> dict:
    """Integrer et uttrykk ved hjelp av SymPy."""
    try:
        var = sp.Symbol(variabel)
        expr = sp.sympify(uttrykk)
        res = sp.integrate(expr, var)
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved integrasjon: {str(e)}"}

def solve_equation(ligning: str, variabel: str = "x") -> dict:
    """Løs en ligning ved hjelp av SymPy."""
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
    """Løs en differensialligning ved hjelp av SymPy."""
    try:
        x = sp.Symbol('x')
        y = sp.Function('y')(x)
        
        # Erstatt y'' og y' med SymPy-deriverte
        eq_str = ligning.replace("y''", "sp.diff(y, x, 2)").replace("y'", "sp.diff(y, x)")
        if "=" in eq_str:
            v, h = eq_str.split("=")
            eq = sp.Eq(eval(v, {"sp": sp, "x": x, "y": y}), eval(h, {"sp": sp, "x": x, "y": y}))
        else:
            eq = eval(eq_str, {"sp": sp, "x": x, "y": y})
            
        res = sp.dsolve(eq, y)
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved ODE-løsning: {str(e)}"}

def matrix_op(operasjon: str, matrise: list) -> dict:
    """Utfører matriseoperasjoner: determinant, invers, egenverdier."""
    try:
        M = sp.Matrix(matrise)
        if operasjon == "determinant":
            res = M.det()
        elif operasjon == "invers":
            res = M.inv()
        elif operasjon == "egenverdier":
            res = M.eigenvals()
        else:
            return {"error": f"Ukjent matriseoperasjon: {operasjon}"}
        return {"resultat": str(res), "latex": sp.latex(res)}
    except Exception as e:
        return {"error": f"Feil ved matriseoperasjon: {str(e)}"}

def complex_op(operasjon: str, tall: str) -> dict:
    """Utfører operasjoner på komplekse tall."""
    try:
        z = sp.sympify(tall)
        if operasjon == "polar":
            r, theta = sp.polar_lift(z)
            res = f"r = {r}, theta = {theta}"
            latex_res = f"r = {sp.latex(r)}, \\theta = {sp.latex(theta)}"
        elif operasjon == "abs":
            res = sp.Abs(z)
            latex_res = sp.latex(res)
        elif operasjon == "arg":
            res = sp.arg(z)
            latex_res = sp.latex(res)
        else:
            return {"error": f"Ukjent kompleks operasjon: {operasjon}"}
        return {"resultat": str(res), "latex": latex_res}
    except Exception as e:
        return {"error": f"Feil ved kompleks operasjon: {str(e)}"}


# Schema for function calling mot språkmodellen
TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "derive",
            "description": "Deriver et matematisk uttrykk mht en variabel.",
            "parameters": {
                "type": "object",
                "properties": {
                    "uttrykk": {"type": "string", "description": "Uttrykket som skal deriveres, f.eks. 'x**3 + 2*x'"},
                    "variabel": {"type": "string", "description": "Variabelen det skal deriveres med hensyn på, standard er 'x'"}
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
                    "uttrykk": {"type": "string", "description": "Uttrykket som skal integreres, f.eks. 'x**2'"},
                    "variabel": {"type": "string", "description": "Variabelen det skal integreres med hensyn på, standard er 'x'"}
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
                    "ligning": {"type": "string", "description": "Ligningen som skal løses, f.eks. 'x**2 - 4 = 0'"},
                    "variabel": {"type": "string", "description": "Variabelen det skal løses for, standard er 'x'"}
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
                    "ligning": {"type": "string", "description": "ODE-ligningen, f.eks. 'y' + y = 0'"}
                },
                "required": ["ligning"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "matrix_op",
            "description": "Utfør en operasjon på en matrise.",
            "parameters": {
                "type": "object",
                "properties": {
                    "operasjon": {"type": "string", "enum": ["determinant", "invers", "egenverdier"]},
                    "matrise": {
                        "type": "array",
                        "items": {"type": "array", "items": {"type": "number"}},
                        "description": "2D-liste/matrise, f.eks. [[1, 2], [3, 4]]"
                    }
                },
                "required": ["operasjon", "matrise"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "complex_op",
            "description": "Utfør en operasjon på et komplekst tall.",
            "parameters": {
                "type": "object",
                "properties": {
                    "operasjon": {"type": "string", "enum": ["polar", "abs", "arg"]},
                    "tall": {"type": "string", "description": "Komplekst tall som streng, f.eks. '1 + 1*I'"}
                },
                "required": ["operasjon", "tall"]
            }
        }
    }
]