"""Numerisk validering av løsninger.

HVORFOR: Etterprøvbarhet er ikke valgfritt for ingeniører. Hvis appen sier at
y(x) løser differensialligningen, skal vi SJEKKE det – ved å sette løsningen
inn i originalproblemet og evaluere numerisk i flere punkter.

SKJELETT – TODO:
- validate(problem, losning) -> {"validert": bool, "detaljer": str}
- Bruk SymPy subs/evalf i 3 tilfeldige punkter.
- Vær ærlig: hvis validering ikke er mulig for oppgavetypen, si det –
  ikke lat som alt er OK.
"""


def validate(problem: str, losning: str) -> dict:
    raise NotImplementedError("Vibe code me! Se SYSTEMBESKRIVELSE.md")
