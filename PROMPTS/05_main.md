# Prompt: `backend/main.py` – koble alt sammen

**Fil:** `backend/main.py`

## Krav (fast)

- `POST /solve` tar `{"oppgave": "..."}`.
- Kaller `llm_client.solve_task(oppgave)`, deretter
  `validator.validate(...)` på resultatet.
- Returnerer JSON med **akkurat** disse feltene (frontend forventer dem):
  `svar`, `steg`, `formler_brukt`, `validert`, `tokens_brukt`, `estimert_kostnad`.
- `GET /` serverer `frontend/index.html`.
- CORS åpent for lokal utvikling.
- God feilhåndtering: vis feilmeldinger ærlig i responsen, ikke skjul dem
  eller returner et falskt «vellykket» svar.

## Hva `main.py` bør gjøre, kort fortalt

`main.py` er koblingslaget, ikke stedet der dere løser matte eller bygger
verktøy. Den bør derfor være liten og tydelig:

- lese inn `Oppgave` fra request-body
- kalle `llm_client.solve_task(...)`
- sende resultatet videre til `validator.validate(...)`
- forme én stabil JSON-respons til frontend
- fange feil fra LLM/API/validator og oversette dem til en ærlig respons

Tenk gjerne slik: `llm_client` lager forslaget, `validator` sjekker det, og
`main.py` bestemmer hva brukeren faktisk får se.

## [FYLL INN SELV] – ta stilling til dette FØR dere sender prompten

- Hva skal skje hvis `llm_client.solve_task` kaster en feil (f.eks. API
  nede, ugyldig token, tom kvote)? Skal brukeren se en teknisk feilmelding,
  eller en forenklet én? Bestem og skriv ned:
  `____________________________________________`
- Hvilken HTTP-statuskode skal brukes ved ulike feil (f.eks. 400 for dårlig
  input, 502/503 for at modellen ikke svarer)? Bestem selv:
  `____________________________________________`

## Praktisk hint

Hold `solve(...)` så enkel som mulig. Hvis den blir stor, er det ofte et tegn
på at ansvar er blandet sammen med `llm_client.py` eller `validator.py`.
Det er helt greit at `main.py` bare gjør et par kall, en `try/except`, og
setter sammen JSON-svaret.

## Ferdig prompt å lime inn (etter at dere har fylt inn over)

```
Implementer backend/main.py sitt POST /solve-endepunkt slik at det:
1. Kaller llm_client.solve_task(oppgave.oppgave).
2. Kaller validator.validate(...) med problemet og svaret fra steg 1.
3. Returnerer JSON med feltene: svar, steg, formler_brukt, validert,
   tokens_brukt, estimert_kostnad.
4. Håndterer feil slik: [LIM INN DERES SVAR FRA "FYLL INN SELV" OVER]
5. Har CORS-middleware som tillater alle origins for lokal utvikling.

Behold GET / som returnerer frontend/index.html.
```

## Kvalitetssjekk før du limer inn koden

- [ ] Alle 6 responsfelt er alltid til stede, selv ved feil.
- [ ] En feil i `llm_client` eller `validator` krasjer ikke serveren (500 med
      stack trace til sluttbruker) – den fanges og vises pent.
- [ ] Kjør `python scripts/selftest.py` – API-kontrakt-sjekken bør nå vise et
      reelt svar i stedet for placeholder-teksten.
- [ ] Test faktisk i frontend (`uvicorn backend.main:app --reload`), ikke
      bare selvtesten.
