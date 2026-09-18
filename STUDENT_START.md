# Kom i gang – for deg som aldri har brukt GitHub, VS Code eller Copilot før

Denne guiden antar null forkunnskap om verktøyene. Følg stegene i rekkefølge.

## 0. Ord dere trenger å kjenne

| Ord | Betyr |
|-----|-------|
| Repo (repository) | En mappe med kode + historikk, lagret på GitHub |
| Template | En mal-repo dere kan lage egen kopi av med ett klikk |
| Codespaces | Ferdig oppsatt VS Code som kjører i nettleseren – **ingenting å installere** |
| Terminal | Tekstvindu der dere skriver kommandoer |
| Copilot | KI-assistenten bygget inn i VS Code |
| API-nøkkel | En hemmelig nøkkel som gir appen deres tilgang til en språkmodell via API |
| `.env`-fil | Fil med hemmeligheter (API-nøkkel) – skal ALDRI deles eller lastes opp |
| Prompt | Teksten dere gir en språkmodell for å be den gjøre noe |

## 1. Lag deres egen kopi av repoet (1 min)

1. Gå til repo-siden på GitHub → grønn knapp **«Use this template»** → **«Create a new repository»**.
2. Gi det et navn, f.eks. `mattehjelpen-gruppe3`, og trykk **«Create repository»**.

Nå eier dere en egen kopi som dere kan endre fritt – uten å påvirke originalen.

## 2. Åpne det uten å installere noe (anbefalt: Codespaces)

1. På deres nye repo-side: trykk **«Code»** → fanen **«Codespaces»** → **«Create codespace on main»**.
2. Vent ca. 1 minutt. Dere får en full VS Code i nettleseren, med Python og
   pakker installert automatisk (se `.devcontainer/devcontainer.json`).

Kjører dere heller lokalt (eget installert VS Code): klon repoet med `git clone`,
åpne mappen i VS Code, og følg steg 5 under manuelt. Se `FEILSOKING.md` hvis noe krangler.

## 3. Sjekk at Copilot faktisk virker for deg

1. Klikk Copilot-ikonet (chat-boble) i sidepanelet i VS Code.
2. Logg inn med GitHub-kontoen deres hvis dere blir bedt om det.
3. En gratis GitHub-konto gir **Copilot Free**: en begrenset, men reell kvote
   av chat-meldinger per måned – nok til denne oppgaven i de fleste tilfeller.
4. Test: skriv «Hei, virker du?» i Copilot Chat. Får dere svar? Da er dere klare.
5. Går kvoten tom midt i oppgaven: se steg 7 og `PROMPTS/README.md` for hvordan
   dere bruker en annen gratis KI i nettleseren i stedet – helt uten å vente på hjelp.

## 4. Skaff en API-nøkkel (så APPEN kan spørre en modell) – helt gratis

> **Gratisprinsipp:** Denne oppgaven skal kunne gjennomføres uten at noen i
> gruppen bruker egne penger. Bruk en leverandør med reell gratis-tilgang.
> Vil dere frivillig prøve en betalt modell i eksperimentdelen (Del B) er
> det lov, men det skal ALDRI være en forutsetning for å fullføre appen.

Appen bruker et vanlig OpenAI-kompatibelt API – dere kan velge fritt hvilken
leverandør dere vil bruke, så lenge den er gratis å komme i gang med.

1. **Enklest og anbefalt:** lag en nøkkel hos [OpenRouter](https://openrouter.ai/keys)
   og velg en modell merket **`:free`** i navnet (f.eks.
   `deepseek/deepseek-chat-v3.1:free`) – se
   [openrouter.ai/models?max_price=0](https://openrouter.ai/models?max_price=0)
   for gjeldende gratis-modeller.
2. Alternativer med egen gratis-kvote: [Google AI Studio](https://aistudio.google.com/apikey)
   (Gemini) eller [Groq](https://console.groq.com/keys) – begge har
   OpenAI-kompatible endepunkt.
3. Kopier nøkkelen. De fleste leverandører viser den bare **én gang**.

Gratisnivåer endrer seg over tid – sjekk gjeldende vilkår hos leverandøren
før dere velger. Se `.env.example` for eksakte URL-er og modellnavn.

## 5. Sett opp miljøet

I Codespaces er Python-pakkene allerede installert automatisk. Dere må bare:

```bash
cp .env.example .env
```

Åpne `.env` og lim inn nøkkelen bak `API_KEY=`, og fyll inn `MODEL_NAME` og
`API_BASE_URL` iht. kommentarene i filen (avhenger av hvilken leverandør dere valgte i steg 4).

(Lokalt oppsett uten Codespaces: se `README.md` steg 4 for full oppskrift med venv.)

## 6. Se hvor dere starter – kjør selvtesten

```bash
python scripts/selftest.py
```

Dette gir en fremdriftsoversikt over hva som mangler. Det er helt normalt at
alt viser «⏳ ikke implementert ennå» første gang dere kjører den.

## 7. Fyll ut skjelettet med KI-hjelp

Dere skal fylle ut 5 filer i `backend/`. Bruk mal-promptene i `PROMPTS/`-mappen
– én fil per modul. **Les `PROMPTS/README.md` først** – den forklarer:

- Hvordan bruke Copilot Chat i VS Code direkte.
- Hvordan bruke en ANNEN gratis KI i nettleseren (ChatGPT, Claude, Gemini, …)
  hvis dere går tom for Copilot-kvote, eller bare vil sammenligne.
- Hvordan dere fordeler arbeid mellom flere modeller.
- Hva dere MÅ tenke gjennom selv før dere sender en prompt – det er en del av
  det dere blir vurdert på (etterprøvbarhet, forståelige forklaringer).

## 8. Kjør appen og test

```bash
uvicorn backend.main:app --reload
```

I Codespaces: en «Ports»-fane åpner seg automatisk – trykk på lenken til port 8000.
Lokalt: åpne http://localhost:8000.

## 9. Gjenta

Kjør `python scripts/selftest.py` igjen etter hver fil dere fyller ut. Test
appen med ekte oppgaver i frontend, ikke bare selvtesten – selvtesten sjekker
*format*, ikke om matten faktisk er riktig løst.

## Når noe ikke virker

Se `FEILSOKING.md` – dekker de vanligste feilene og hvordan dere løser dem
selv, uten å vente på læreren.
