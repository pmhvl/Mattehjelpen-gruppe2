"""MatteHjelpen – FastAPI-backend.

SKJELETT: Bruk SYSTEMBESKRIVELSE.md som prompt og la en språkmodell hjelpe dere
å fylle ut. Kravene:

- POST /solve tar {"oppgave": "..."} og returnerer JSON med:
  svar, steg (liste), formler_brukt, validert (bool), tokens_brukt, estimert_kostnad
- GET / serverer frontend/index.html
- God feilhåndtering: vis feil ærlig, ikke skjul dem.
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="MatteHjelpen")


class Oppgave(BaseModel):
    oppgave: str


@app.get("/")
async def index():
    return FileResponse("frontend/index.html")


@app.post("/solve")
async def solve(oppgave: Oppgave):
    # TODO: Kall llm_client.solve_task(oppgave.oppgave)
    # TODO: Valider svaret med validator.validate(...)
    # TODO: Returner full respons iht. SYSTEMBESKRIVELSE.md
    return {
        "svar": "Ikke implementert ennå – se SYSTEMBESKRIVELSE.md",
        "steg": [],
        "formler_brukt": [],
        "validert": False,
        "tokens_brukt": 0,
        "estimert_kostnad": 0.0,
    }
