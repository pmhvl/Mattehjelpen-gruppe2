"""FastAPI hovedapplikasjon for MatteHjelpen."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.llm_client import solve_task
from backend.validator import validate

app = FastAPI(title="MatteHjelpen API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    oppgave: str
    use_tools: bool = True

@app.post("/solve")
def solve(req: TaskRequest):
    resultat = solve_task(req.oppgave, req.use_tools)
    verktoy_kall = resultat.pop("_verktoy_kall", None)
    validering = validate(req.oppgave, resultat.get("svar", ""), verktoy_kall)
    resultat["validert"] = validering.get("validert", False)
    resultat["valideringsdetaljer"] = validering.get("detaljer", "")
    return resultat

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")