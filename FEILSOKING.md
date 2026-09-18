# Feilsøking

Sjekk her først – de aller fleste problemer løses uten å spørre noen.

## «Jeg finner ikke Copilot-ikonet / kan ikke logge inn»

- Se etter chat-boble-ikonet i venstre sidepanel i VS Code.
- Blir dere bedt om å logge inn: bruk samme GitHub-konto dere brukte for å lage repoet.
- Fortsatt ingenting: prøv å laste siden på nytt (Codespaces) eller restart VS Code (lokalt).

## `cp: cannot stat '.env.example'`

Dere står i feil mappe. Kjør `pwd` – dere skal stå i rot-mappen av repoet
(der `README.md` ligger), ikke inni `backend/` eller `frontend/`.

## `ModuleNotFoundError: No module named 'fastapi'` (el. lignende)

- Lokalt: har dere aktivert venv? `source .venv/bin/activate`, og deretter
  `pip install -r requirements.txt`.
- Codespaces: dette skal skje automatisk. Kjør `pip install -r requirements.txt` manuelt hvis ikke.

## `401 Unauthorized` fra API-et

- Nøkkelen (`API_KEY` i `.env`) er feil, ufullstendig kopiert, eller utløpt.
  Lag en ny hos leverandøren deres (f.eks. openrouter.ai/keys eller
  platform.openai.com/api-keys) og oppdater `.env`.
- Sjekk også at `API_BASE_URL` faktisk peker på samme leverandør som nøkkelen er laget hos.
- Husk: ingen mellomrom eller anførselstegn rundt verdien i `.env`.

## `429 Too Many Requests` / rate limit / kvote brukt opp

Dette er **forventet** i et kurs med mange grupper som deler gratis-kvoter.
Løsning – fortsett uten å vente på noen:

1. Åpne en KI-chat i nettleseren (ChatGPT, Claude, Gemini, Mistral Le Chat, …).
2. Lim inn prompt-malen fra `PROMPTS/`-mappen der i stedet.
3. Kopier koden tilbake til riktig fil i Codespaces/VS Code.

Se full oppskrift i `PROMPTS/README.md`, avsnittet «Når Copilot går tom for
gratis-kvote».

## `NotImplementedError` når jeg tester `/solve`

Helt forventet før dere har fylt ut modulen. Det betyr at akkurat den
funksjonen ikke er implementert ennå – se `scripts/selftest.py` for hvilken.

## «Port already in use» / uvicorn starter ikke

Noe annet bruker port 8000 allerede (kanskje en gammel `uvicorn`-prosess).

```bash
# Finn og stopp gammel prosess:
lsof -i :8000
kill <PID>
# Eller bruk en annen port:
uvicorn backend.main:app --reload --port 8001
```

## Feilmelding i nettleser-konsollen om CORS

Backend må ha CORS-middleware som tillater kall fra frontend. Sjekk at
`backend/main.py` har `CORSMiddleware` lagt til – se `SYSTEMBESKRIVELSE.md`.

## MathJax viser rå LaTeX-kode i stedet for pen formatering

Sjekk internett-tilkobling (MathJax lastes fra CDN). Blokkerer skolens
nettverk CDN-er, prøv mobildata eller en annen nettverksforbindelse.

## «Appen sier ✅ validert, men jeg tror svaret er feil»

Validering sjekker kun at løsningen er *numerisk konsistent* med problemet
slik SymPy tolket det. Hvis modellen misforstod OPPGAVEN (f.eks. tvetydig
notasjon som `sin^-1`), kan SymPy regne helt riktig på et **feil problem** –
og validering vil da vise ✅ selv om svaret på den *egentlige* oppgaven er
feil. Dette er eksplisitt et av punktene dere skal undersøke i `OPPGAVE.md`
(aha-bryter 4) – ikke en bug dere skal fikse bort, men noe dere skal
observere og skrive om.

## Gruppa er uenige om hvem som gjør hva / hvilken modell som skal brukes

Se `PROMPTS/README.md`, avsnittet «Fordel arbeid mellom flere modeller» for
et konkret forslag til arbeidsdeling.

## Ingenting av dette hjalp

Skriv ned: hva dere gjorde, nøyaktig feilmelding (kopier hele teksten), og
hvilken fil/steg dere var på. Da går feilsøking raskt når dere til slutt spør
noen.
