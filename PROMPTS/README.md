# Prompt-maler – slik fyller dere ut skjelettet

## Grunnidé

Hver fil i denne mappen er en start-prompt for **én modul** i `backend/`.
Dere kan lime prompten inn i:

- **GitHub Copilot Chat** i VS Code (raskest, integrert i editoren), ELLER
- **En hvilken som helst annen gratis KI-chat i nettleseren** (ChatGPT,
  Claude, Gemini, Mistral Le Chat, …) – kopier svaret tilbake til riktig fil.

Begge veier er like gyldige. Vi oppfordrer dere faktisk til å prøve begge og
sammenligne – det gir relevante erfaringer til eksperimentdelen (Del B i
`OPPGAVE.md`) og for arbeidslivet: å vite når man bytter verktøy, og hvordan
man flytter kode mellom systemer uten å rote det til.

## Hvorfor prompt-maler og ikke ferdig kode?

Vi gir dere **ikke fasit**. Malene beskriver krav (hva koden må klare), ikke
eksakt implementasjon. Det betyr:

- Appen deres vil se annerledes ut enn andre gruppers – **det er meningen**.
- Dere må selv formulere noen krav i prompten (merket `[FYLL INN SELV]`) FØR
  dere sender den. Det tvinger dere til å tenke gjennom hva som faktisk gjør
  svaret til noe dere kan stole på – ikke bare «få noe som kjører».

## Arbeidsflyt per fil

1. Åpne prompt-malen for modulen dere skal jobbe med (f.eks. `01_tools.md`).
2. Fyll ut `[FYLL INN SELV]`-feltene – forklaring følger med i hver mal.
3. Lim hele prompten inn i Copilot Chat ELLER en nettleser-KI.
4. Få kode tilbake. **Før** dere limer den inn i filen:
   - Gå gjennom «Kvalitetssjekk»-lista nederst i malen.
   - Les koden. Forstår dere hva den gjør? Hvis ikke: spør modellen «forklar
     linje for linje» – ikke bare godta den fordi den kjører.
5. Lim koden inn på **riktig sted** (malen sier eksakt hvilken fil og
   funksjon). Fjern `raise NotImplementedError(...)`-linjen samtidig.
6. Kjør `python scripts/selftest.py` for å se om modulen nå består sjekkene.
7. Commit med en forklarende melding, f.eks.
   `git commit -am "Implementer tools.py: derive og integrate"`.

## Fordel arbeid mellom flere modeller (anbefalt)

Ikke bruk kun én modell til alt. Prøv f.eks.:

- En **stor modell** (GPT-4o, Claude Sonnet, Gemini Pro) til
  `llm_client.py` og `validator.py` – disse krever nøye resonnering
  (tool-calling-logikk, numerisk validering).
- En **liten/rask modell** (GPT-4o-mini, Gemini Flash, Haiku) til
  `formelsamling.py` – rett frem datastruktur.
- Skriv ned i `EKSPERIMENT.md` hva som faktisk skjedde – dette ER
  en del av eksperimentet fra Del B.

## Når Copilot går tom for gratis-kvote

1. Åpne en ny fane i nettleseren og gå til en gratis KI-chat, f.eks.
   chat.openai.com, claude.ai, gemini.google.com eller chat.mistral.ai
   (gratisnivåer endrer seg – sjekk hva som er tilgjengelig nå).
2. Lim inn prompt-malen der i stedet for i Copilot Chat.
3. Kopier koden tilbake til riktig fil i Codespaces/VS Code med vanlig
   kopier/lim inn – ingen ekstra verktøy trengs.
4. **Aldri** lim inn `.env`-innhold, token, eller andre hemmeligheter i en
   ekstern chat. Prompt-malene inneholder ingen hemmeligheter – bare krav og
   kode.

## Kvalitetsgrind – før dere sier dere er ferdig med en modul

Uansett hvilken modell som skrev koden, sjekk at:

- [ ] Dere kan forklare hva koden gjør, i egne ord, uten å lese den på nytt.
- [ ] Forklaringene appen gir er noe en medstudent ville forstått – ikke bare
      riktig fagspråk uten sammenheng.
- [ ] Feil håndteres ærlig (appen lyver aldri om at noe er validert når det
      ikke er det).
- [ ] Dere har testet med minst én oppgave dere har regnet ut for hånd selv.

## Filoversikt

| Fil | Modul | Vanskelighetsgrad |
|-----|-------|--------------------|
| `01_tools.md` | `backend/tools.py` | Middels – SymPy-kunnskap hjelper |
| `02_formelsamling.md` | `backend/formelsamling.py` | Lett – god jobb for billig modell |
| `03_llm_client.md` | `backend/llm_client.py` | Vanskelig – krever nøye resonnering |
| `04_validator.md` | `backend/validator.py` | Middels – designvalg om ærlighet |
| `05_main.md` | `backend/main.py` | Middels – kobler alt sammen |

`frontend/index.html` er allerede ferdig i skjelettet. Dere står fritt til å
forbedre den, men det er ikke et krav.
