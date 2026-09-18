# MatteHjelpen 🧮🤖

Template-repo for innleveringsoppgaven i innføringsmodulen i KI for ingeniørstudenter ved HVL.

Dere skal bruke KI-assistert utvikling («vibe coding») til å lage en webapp som løser typiske førsteårsoppgaver i matematikk – og underveis lære hvor språkmodeller er sterke, hvor de er svake, og hva *dere* må kunne for å stole på svaret.

> **Aldri brukt GitHub, VS Code eller Copilot før?** Start i stedet med
> [`STUDENT_START.md`](STUDENT_START.md) – en komplett steg-for-steg-guide fra bunnen av.

> **Oversikt over hele modulen** (timeplan, oppgave, ressurser – for både
> studenter og forelesere): se [`KURSGUIDE.md`](KURSGUIDE.md).

Opplegget er: **forelesning 1 → én uke gruppearbeid → forelesning 2**.
Oppgaven deles ut i første forelesning.

> **Gratisprinsipp:** Hele oppgaven skal kunne løses uten at noen i gruppen
> bruker egne penger. Se `.env.example` for reelle gratis-alternativer.

## Kom i gang

1. **Lag deres egen kopi:** Klikk «Use this template» → «Create a new repository» (én per gruppe).
2. **Åpne i Codespaces (ingenting å installere):** «Code» → «Codespaces» → «Create codespace on main». Python og pakker settes opp automatisk (se `.devcontainer/`). **Vil dere heller kjøre lokalt**: klon repoet og åpne det i VS Code.
3. **Skaff API-tilgang (gratis):** Dette skal kunne gjøres uten å bruke egne
   penger. Anbefalt: lag en nøkkel hos [OpenRouter](https://openrouter.ai/keys)
   og velg en modell merket `:free` (se
   [openrouter.ai/models?max_price=0](https://openrouter.ai/models?max_price=0)).
   Google AI Studio og Groq har også OpenAI-kompatible gratis-tilbud. En
   betalt modell er valgfritt (typisk for sammenligning i Del B) – aldri et krav.
4. **Sett opp miljøet** (kun nødvendig lokalt – Codespaces gjør dette automatisk):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Uansett: `cp .env.example .env` og fyll inn API-nøkkel, modellnavn og base-URL.
5. **Vibe coding:** Åpne `SYSTEMBESKRIVELSE.md` for kravene, og bruk mal-promptene i [`PROMPTS/`](PROMPTS/README.md) til å fylle ut skjelettfilene – én modul om gangen, med Copilot Chat ELLER en annen gratis KI i nettleseren eller en annen kodeagent for VS Code, for eksempel Cline. Kjør `python scripts/selftest.py` underveis for å se fremdrift.
6. **Kjør appen:**
   ```bash
   uvicorn backend.main:app --reload
   ```
   Åpne http://localhost:8000 i nettleseren (Codespaces åpner en «Ports»-fane automatisk).

Gikk Copilot tom for gratis-kvote? Se [`PROMPTS/README.md`](PROMPTS/README.md) for hvordan dere fortsetter med en annen gratis KI-chat i nettleseren – uten å vente på hjelp. Noe krangler? Se [`FEILSOKING.md`](FEILSOKING.md).

## Repo-struktur

```
mattehjelpen/
├── README.md            # Denne filen
├── STUDENT_START.md     # Steg-for-steg for dere som er helt nye i verktøyene
├── FEILSOKING.md        # Vanlige feil og hvordan dere løser dem selv
├── OPPGAVE.md           # Innleveringsoppgaven med vurderingskriterier
├── KURSGUIDE.md         # Timeplan og samlet oversikt over modulen
├── EVALUERING.md        # Sensurrubrikk og sjekkliste
├── GJENNOMGANG.md       # Erfaringsdel til forelesning 2
├── SYSTEMBESKRIVELSE.md # Start-prompten for vibe coding
├── EKSPERIMENT.md       # Mal for eksperimentloggen (Del B)
├── PROMPTS/             # Prompt-maler, én fil per backend-modul
├── foiler/              # Quarto/reveal.js-foiler for foreleserne
├── scripts/
│   └── selftest.py      # Kjør for å se fremdrift: python scripts/selftest.py
├── .github/workflows/
│   └── selvtest.yml     # Kjører selvtesten ved push og pull request
├── .devcontainer/       # Codespaces-oppsett (installerer alt automatisk)
├── requirements.txt
├── .env.example
├── backend/
│   ├── main.py          # FastAPI-app, POST /solve
│   ├── llm_client.py    # API-kall, systemprompt og tool-calling
│   ├── tools.py         # SymPy-verktøy og tool-definisjoner
│   ├── validator.py     # Numerisk kontroll av svar
│   └── formelsamling.py # Innebygd formelsamling med referanser
└── frontend/
    └── index.html       # Enkel frontend med MathJax
```

## Viktig prinsipp

> **Modellen skal resonnere. Verktøyet skal regne.**
>
> En språkmodell predikerer tekst – den regner ikke. All symbolsk og numerisk
> BEREGNING skal gjøres med SymPy via tool-kall. Deres jobb er å designe appen
> slik at den er *etterprøvbar*: stegvis forklaring, formelreferanser og
> numerisk validering. Husk: DERE er ansvarlige for svaret – ikke KI-en.

> **Grenser for prinsippet:** Ikke all matematikk er beregning. Spør dere om
> et bevis (f.eks. «bevis Pythagoras' læresetning») eller en
> begrepsforklaring, finnes det ikke noe SymPy-kall som gir svaret. Da skal
> appen resonnere i tekst og si eksplisitt at svaret IKKE er verifisert av et
> verktøy – ikke late som SymPy sjekket noe den ikke sjekket. Dette er en
> legitim og forventet del av oppgaven, ikke noe dere skal fjerne eller skjule.

## Forvent variasjon – og bruk flere KI-verktøy

Prompt-malene i [`PROMPTS/`](PROMPTS/README.md) gir krav, ikke fasit. Dere
skal selv formulere flere av kravene (merket `[FYLL INN SELV]`) før dere
spør en modell om hjelp – det er en del av det dere øver på. Det er derfor
helt forventet, og ønskelig, at gruppenes apper ser forskjellige ut. Dere
oppfordres også til å fordele arbeidet mellom flere modeller (Copilot,
en API-leverandør som OpenRouter, og gratis KI-chatter i nettleseren) – se
`PROMPTS/README.md` for konkrete forslag.