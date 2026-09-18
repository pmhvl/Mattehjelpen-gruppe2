"""Deterministiske matteverktøy (SymPy) for MatteHjelpen.

PRINSIPP: Modellen resonnerer – verktøyet regner. En språkmodell skal ALDRI
gjøre symbolsk/numerisk regning selv.

SKJELETT – TODO: Implementer med SymPy. Hver funksjon returnerer
{"resultat": str, "latex": str}. Definer også TOOL_DEFINITIONS (JSON-schema
for function calling) som llm_client.py sender til modellen.
"""


def derive(uttrykk: str, variabel: str = "x") -> dict:
    """Deriver et uttrykk. TODO: sympy.diff"""
    raise NotImplementedError


def integrate(uttrykk: str, variabel: str = "x") -> dict:
    """Integrer et uttrykk. TODO: sympy.integrate"""
    raise NotImplementedError


def solve_equation(ligning: str, variabel: str = "x") -> dict:
    """Løs en ligning. TODO: sympy.solve"""
    raise NotImplementedError


def solve_ode(ligning: str) -> dict:
    """Løs en differensialligning. TODO: sympy.dsolve"""
    raise NotImplementedError


def matrix_op(operasjon: str, matrise: list) -> dict:
    """Matriseoperasjoner: determinant, invers, egenverdier, løs Ax=b."""
    raise NotImplementedError


def complex_op(operasjon: str, tall: str) -> dict:
    """Komplekse tall: polarform, potenser, røtter, Eulers formel."""
    raise NotImplementedError


# TODO: TOOL_DEFINITIONS = [ ... ]  # JSON-schema for function calling
