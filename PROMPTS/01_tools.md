# Prompt: `backend/tools.py` – deterministiske SymPy-verktøy

**Fil:** `backend/tools.py`
**Prinsipp:** Modellen skal ALDRI late som den har beregnet noe et verktøy
kunne gjort. All BEREGNING (derivasjon, ligninger, matriser, komplekse tall)
skjer her, med SymPy – bevis og begrepsforklaringer er en annen kategori
(se `PROMPTS/03_llm_client.md`).

## Krav (fast – ikke forhandlingsbart)

Implementer disse funksjonene med SymPy, med **akkurat** disse navnene og
parameterne (llm_client og resten av appen forventer disse signaturene):

- `derive(uttrykk: str, variabel: str = "x") -> dict`
- `integrate(uttrykk: str, variabel: str = "x") -> dict`
- `solve_equation(ligning: str, variabel: str = "x") -> dict`
- `solve_ode(ligning: str) -> dict`
- `matrix_op(operasjon: str, matrise: list) -> dict`
- `complex_op(operasjon: str, tall: str) -> dict`

Hver funksjon returnerer `{"resultat": str, "latex": str}` ved suksess.

Definer også `TOOL_DEFINITIONS`: en liste med JSON-schema (OpenAI
function-calling-format) som beskriver disse 6 verktøyene, til bruk i
`llm_client.py`.

## Hva disse verktøyene ikke dekker

De 6 funksjonene dekker konkrete beregninger. De dekker IKKE bevisoppgaver
(f.eks. «bevis Pythagoras' læresetning») eller begrepsforklaringer – det er
like fullt legitime matteoppgaver, bare ikke noe SymPy kan «regne ut». Dere
står fritt til å utvide `tools.py` med flere funksjoner senere (f.eks.
grenseverdier, serieutvikling) – hold da samme mønster:
`{"resultat": str, "latex": str}`, og oppdater `TOOL_DEFINITIONS` tilsvarende.

## [FYLL INN SELV] – ta stilling til dette FØR dere sender prompten

- Hvilke feilsituasjoner skal funksjonene håndtere eksplisitt? (F.eks. ugyldig
  syntaks, deling på null, matrise med feil dimensjoner.) Skriv egen liste:
  `____________________________________________`
- Skal feil kastes som exceptions, eller returneres som del av dict
  (f.eks. `{"feil": "..."}`)? Bestem selv og vær konsekvent – dette påvirker
  hvordan `main.py` må håndtere det.
- Hvor «smart» skal parsing av matteuttrykk være? (F.eks.: skal `sin^-1(x)`
  tolkes som invers funksjon eller som potens? Dette er et av
  «aha-punktene» i `OPPGAVE.md` – bestem en tolkning og vær eksplisitt om
  den i koden/docstringen.)

## Ferdig prompt å lime inn (etter at dere har fylt inn over)

```
Implementer backend/tools.py i et FastAPI/SymPy-prosjekt. Funksjonene som
skal implementeres er: derive, integrate, solve_equation, solve_ode,
matrix_op, complex_op (se signaturer og docstrings i filen). Bruk sympy.
Returner alltid {"resultat": str, "latex": str} ved suksess.

Feilhåndtering: [LIM INN SVARET DERES FRA "FYLL INN SELV" OVER]

Legg også til TOOL_DEFINITIONS: en liste med JSON-schema for OpenAI
function-calling som beskriver disse 6 funksjonene (navn, beskrivelse,
parametere med typer).

Skriv en kort forklarende docstring per funksjon, på norsk.
```

## Kvalitetssjekk før du limer inn koden

- [ ] Alle 6 funksjonsnavn og parametere er UENDRET fra skjelettet.
- [ ] Ingen `NotImplementedError` igjen.
- [ ] `TOOL_DEFINITIONS` finnes og er en liste.
- [ ] Dere forstår hvordan feil håndteres, og det stemmer med det dere
      bestemte i «FYLL INN SELV» over.
- [ ] Kjør `python scripts/selftest.py` – tools-sjekkene bør nå vise ✅.
