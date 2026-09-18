# Prompt: `backend/llm_client.py` – LLM-kall og tool-calling-løkke

**Fil:** `backend/llm_client.py`
**Vanskelighetsgrad:** Høy – bruk gjerne en sterk modell (GPT-4o, Claude
Sonnet, Gemini Pro) på denne.

## Krav (fast)

- Les `API_KEY`, `MODEL_NAME`, `API_BASE_URL` fra `.env` (`python-dotenv`).
- Bruk `openai`-biblioteket med `base_url` mot et OpenAI-kompatibelt API
  (f.eks. OpenRouter, OpenAI selv, eller en annen leverandør – se `.env.example`).
- Systemprompten i filen (se docstring) skal beholdes i kjernen – ikke fjern
  kravene der uten å forstå konsekvensen (det er nettopp «aha-bryter 2» i
  `OPPGAVE.md`).
- Implementer tool-calling-løkke: send melding → hvis modellen ber om
  tool-kall, kjør riktig funksjon fra `tools.py`, legg resultatet tilbake i
  samtalen, gjenta til modellen gir endelig svar.
- Tell tokens fra `response.usage` og regn ut estimert kostnad.
- `USE_TOOLS`-bryteren øverst i filen skal fortsatt fungere som av/på-bryter
  (aha-bryter 1 i `OPPGAVE.md` – ikke fjern den).

## Hva `solve_task(...)` faktisk skal være

`solve_task(...)` skal være en liten orkestrator, ikke en matte-motor. Den bør
derfor:

- lese inn konfigurasjon fra `.env`
- sende brukerens oppgave og systemprompten til modellen
- gjøre `FORMELSAMLING` tilgjengelig for modellen, inkludert formel-ID,
  `bruk` og referanse
- la modellen be om verktøy via tool-calling
- kjøre riktige funksjoner i `backend/tools.py`
- sende tool-resultatet tilbake til modellen til den er ferdig
- pakke sluttresultatet som en `dict` som `main.py` kan sende videre som JSON

Det er med andre ord `tools.py` som skal regne, ikke modellen. Modellen skal
forklare og velge riktig verktøy, mens SymPy gjør utregningen.
## Bevisoppgaver og andre ting SymPy ikke kan regne ut

Ikke alle legitime matteoppgaver er beregninger. Spør noen «bevis Pythagoras'
læresetning», finnes det intet SymPy-kall som gir svaret. Da skal appen:

- resonnere i tekst, gjerne støttet på en oppføring i formelsamlingen
- si eksplisitt at svaret IKKE er verifisert av et verktøy
- aldri late som et tool-kall ble brukt når det ikke ble det

## Ikke stol på modellens egen påstand om verktøybruk

En modell kan skrive «jeg har brukt SymPy til å bekrefte dette» uten at noe
tool-kall faktisk skjedde. Logg derfor brukte verktøy fra de faktiske
`tool_calls` dere fanger i løkken (funksjonsnavn + argumenter), ikke fra fri
tekst. Formelvalg er annerledes: modellen kan oppgi formel-ID per steg, men
appen må kontrollere at ID-en finnes i `FORMELSAMLING` og hente navn og
referanse derfra. En gyldig ID viser hvor regelen står; den beviser ikke at
regelen er anvendt riktig eller at et SymPy-kall skjedde.
## [FYLL INN SELV] – ta stilling til dette FØR dere sender prompten

- Systemprompten i skjelettet er et **minimum**. Hva vil DERE legge til for
  at forklaringene skal bli forståelige for DERE (ikke bare fagkorrekte)?
  Eksempel: be modellen unngå unødvendig fagsjargong, eller alltid forklare
  *hvorfor* et steg gjøres, ikke bare *hva* som gjøres. Skriv deres tillegg:
  `____________________________________________`
- Hvor mange tool-calling-runder skal appen maks tillate før den gir opp (for
  å unngå evighetsløkker)? Bestem et tall og begrunn kort:
  `____________________________________________`
- Hvis dere limer svar inn fra en nettleser-KI som ikke gir `response.usage`
  (tokens): hva skal appen vise da? (Forslag: vær ærlige – vis `"ukjent"`
  fremfor å late som dere har et tall. Dette henger sammen med
  ærlighetsprinsippet i `validator.py`.)

## Ferdig prompt å lime inn (etter at dere har fylt inn over)

```
Implementer backend/llm_client.py for en FastAPI-app som bruker et
OpenAI-kompatibelt API (base_url, API-nøkkel og modellnavn fra .env).

Systemprompt (behold denne kjernen, du kan legge til mer):
"Du er en matematikklærer for ingeniørstudenter. Bruk verktøyene (SymPy) til
all beregning når oppgaven lar seg beregne slik – du skal ALDRI late som du
har brukt et verktøy du ikke faktisk kalte. Kan oppgaven ikke beregnes (f.eks.
et bevis eller en begrepsforklaring), resonnerer du i tekst og sier eksplisitt
at svaret IKKE er verifisert av et verktøy. Forklar hvert steg pedagogisk på
norsk, og oppgi nøyaktig hvilke formler/verktøy du faktisk brukte, med
referanse til formelsamlingen. Hvis du er usikker, si det eksplisitt."

Gjør FORMELSAMLING tilgjengelig i systemprompten i et kompakt format med ID,
navn, formel, bruk og referanse. Be modellen knytte hver brukt formel-ID til
det konkrete steget der formelen anvendes. Avvis ukjente formel-ID-er før
responsen returneres.

Tillegg til systemprompten fra oss: [LIM INN DERES SVAR OVER]

Implementer solve_task(oppgave: str) -> dict som:
1. Sender oppgaven + TOOL_DEFINITIONS fra tools.py til modellen (med mindre
  USE_TOOLS er False).
2. Håndterer tool-calling-løkken med en øvre grense (ikke uendelig løkke).
3. Returnerer dict med: svar, steg (liste av strenger), formler_brukt,
  tokens_brukt, estimert_kostnad. (validert settes IKKE her – det gjør
  validator.py, kalt fra main.py.)

Hvis modellen gir et matematisk svar i fri tekst, men dere også vil rendere pen
matte i frontend, kan dere i tillegg ha et felt som `svar_latex` eller en annen
intern representasjon. Det viktigste er at dere skiller mellom:
- tekst for forklaring
- maskinlesbar løsning for validering
- eventuelt LaTeX for pen visning

Les API_KEY, MODEL_NAME, API_BASE_URL fra .env med python-dotenv.
```

## Kvalitetssjekk før du limer inn koden

- [ ] `USE_TOOLS = False` gir fortsatt et (dårligere) svar – ikke en krasj.
- [ ] Tool-calling-løkken har en øvre grense (ikke uendelig løkke).
- [ ] `tokens_brukt`/`estimert_kostnad` er reelle tall, ikke hardkodet 0.
- [ ] Dere har testet med `USE_TOOLS = True` og `False` og faktisk sett
      forskjellen – dette er data til `EKSPERIMENT.md`.
- [ ] Ingen hemmeligheter (token) er hardkodet i filen – kun lest fra `.env`.
- [ ] Verktøyloggen bygges fra faktiske tool-kall, ikke fra modellens egen
  påstand i fri tekst.
- [ ] Formel-ID-er finnes i `FORMELSAMLING` og er knyttet til steget der
  formelen faktisk brukes.
