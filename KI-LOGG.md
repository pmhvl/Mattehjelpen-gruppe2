# KI-bruk-logg

Dokumenterer bruk av KI i arbeidet med MatteHjelpen, slik `OPPGAVE.md` krever
("dokumentér bruken – hvilke modeller, til hva"). Denne økten er ført av
Romina/romazcue. Andre gruppemedlemmer bør legge til egne økter under, med
dato, verktøy/modell og hva som ble gjort.

## Økt: retting av bugs i skjelett-implementasjonen

**Verktøy/modell:** Claude Sonnet 5, via Claude Code (VS Code-utvidelse/CLI).
**Kontekst:** Gruppemedlem hadde allerede skrevet en første implementasjon av
`backend/tools.py`, `llm_client.py`, `validator.py`, `main.py` og
`frontend/index.html` (trolig med hjelp av Copilot, se tidligere commits).
`python scripts/selftest.py` viste 1 feil. Ba KI-en gå gjennom koden og rette
opp det som var galt før arbeidet ble committet og delt med resten av gruppa.

### Hvordan feilene ble funnet
1. Kjørte `scripts/selftest.py --strict` – avdekket 1 direkte feil (manglende
   `validert`-felt i API-responsen).
2. Ba KI-en lese gjennom `tools.py`, `llm_client.py`, `validator.py`,
   `main.py` og `frontend/index.html` manuelt og sammenligne mot kravene i
   `SYSTEMBESKRIVELSE.md` – dette avdekket flere feil selvtesten *ikke*
   fanger opp (selvtesten sjekker format, ikke om innholdet er riktig eller
   ærlig).
3. Testet appen live i nettleseren med ekte oppgaver – avdekket ytterligere
   2 feil som verken selvtesten eller kodegjennomgangen fanget (MathJax som
   ikke rendret matte riktig, og et steg som ble kuttet).
4. Testet med ekte API-kall mot Google Gemini – avdekket at modellnavnet i
   `.env` var utdatert, og senere at gratiskvoten (20 kall/dag) ble brukt opp.

### Endringer per fil

**`backend/tools.py`**
- `solve_ode`: Feilet på gyldig input (f.eks. `y(x).diff(x) + 4*y(x)`) fordi
  `y` var satt opp som en allerede-anvendt SymPy-funksjon i stedet for en
  kallbar funksjon. Rettet slik at både `y'`/`y''`-notasjon og direkte
  SymPy-notasjon støttes.
- `complex_op("polar", ...)`: Brukte `sp.polar_lift()` feil (den returnerer
  ikke `(r, theta)` som koden antok, og krasjet). Rettet til `sp.Abs()` /
  `sp.arg()`.
- La til `matrix_op("løs", ...)` for å løse lineære ligningssystemer `Ax=b`
  – krevd i `SYSTEMBESKRIVELSE.md`, men manglet i implementasjonen.
- La til `complex_op("potens", ...)` og `complex_op("røtter", ...)` – også
  krevd i `SYSTEMBESKRIVELSE.md`, men manglet.
- Oppdaterte `TOOL_DEFINITIONS` (JSON-schema for tool-calling) tilsvarende.

**`backend/llm_client.py`**
- `formler_brukt` var hardkodet til `list(FORMELSAMLING.keys())[:2]` – ga
  alltid de to første formlene i samlingen, uansett hvilken oppgave som ble
  løst. Dette var det mest alvorlige funnet: appen *påsto* å vise brukte
  formler, uten at det stemte. Erstattet med reell sporing: systemprompten
  ber modellen tagge formel-ID-er i teksten (f.eks. `[D1]`), og koden
  plukker ut disse med regex og validerer dem mot `FORMELSAMLING` (ukjente
  ID-er avvises).
- La til strukturert stegformat: modellen bes formatere svaret som
  `Steg 1: ...`, `Steg 2: ...` osv., og koden trekker ut disse til et eget
  `steg`-felt (var tidligere bare `[hele_svaret]` som étt "steg").
- Fjernet det interne kallet til `validate()` – flyttet til `main.py` (se
  under), slik `SYSTEMBESKRIVELSE.md` faktisk beskriver arkitekturen.
- Tool-calling håndterte kun `msg.tool_calls[0]` (ett verktøykall, én runde).
  Bygget om til en løkke (maks 5 runder) som håndterer flere verktøykall per
  runde og fortsetter til modellen gir et endelig svar.

**`backend/validator.py`**
- Kritisk feil: `validate()` ble kalt med modellens frie forklaringstekst
  som input. SymPy klarer ikke å tolke naturlig språk (`sympify()` feiler),
  så `validert` ble så godt som alltid `False` – uavhengig av om svaret
  faktisk var riktig. Bygget om fra bunnen: `validate()` tar nå inn det
  faktiske SymPy-verktøyresultatet (funksjon + argumenter + resultat) fra
  siste tool-kall, og gjør en reell numerisk identitetssjekk i 3 tilfeldige
  punkter (f.eks. sjekker at `d/dx(uttrykk) == resultat` for `derive`, at
  differensialligningen blir ~0 når løsningen settes inn for `solve_ode`,
  osv.). Ingen tool-kall (f.eks. bevisoppgaver) gir ærlig `validert: False`
  med forklaring, ikke en krasjet sympify-feil.

**`backend/main.py`**
- La til eksplisitt kall til `validate()` etter `solve_task()`, og flettet
  `validert`/`valideringsdetaljer` inn i responsen – i tråd med at
  `solve_task()` ikke lenger gjør dette selv.

**`frontend/index.html`**
- Sikkerhet: `svarTekst.innerHTML = data.svar` satte modellens fritekst
  direkte inn som HTML – en XSS-sårbarhet. Byttet til `.innerText`.
- La til visning av `steg`-listen (var ikke rendret i det hele tatt før).
- MathJax rendret ikke matte skrevet med enkle `$...$` (kun `$$...$$` var på
  som standard). La til eksplisitt MathJax-konfigurasjon for `$...$` og
  `\(...\)` før MathJax-scriptet lastes.
- Regex for stegutrekking i `llm_client.py` fanget opprinnelig bare tekst på
  samme linje som "Steg N:" – et steg med formelen på egen linje (vanlig med
  `$$...$$`) ble kuttet. Rettet til å splitte på "Steg N:"-markører i stedet
  for linjeskift.
- Rå modellsvar dupliserte stegvisningen og rotet til siden – lagt i en
  sammenleggbar `<details>`-boks i stedet for å vises fullt ut alltid.
- Feilmeldinger fra backend (f.eks. API-feil) ble tidligere gjemt inni denne
  boksen og usynlige for brukeren – gjort synlige øverst i resultatvisningen.

**`.env`**
- `MODEL_NAME=gemini-1.5-flash` fantes ikke lenger hos Google (404). Byttet
  til `gemini-flash-latest`, som fungerte med gruppas nøkkel.

### Verifisering (ikke bare tatt KI-ens ord for det)
- Kjørte `python scripts/selftest.py --strict` før og etter – gikk fra 1
  feil til 0 feil.
- Testet hver ny/rettet funksjon direkte i et Python-script (matrix "løs",
  complex "potens"/"røtter", validator på riktig og bevisst feil derivert,
  steg-/formel-ekstraksjon) for å bekrefte at de faktisk regner riktig, ikke
  bare at de ikke krasjer.
- Testet hele kjeden med ekte API-kall (ikke mock) mot Gemini, og i
  nettleseren, før arbeidet ble ansett som ferdig.

### Ting å være obs på (til Del B/C)
- Gemini-nøkkelens gratiskvote er kun ~20 kall/dag – for lite til de 40+
  kjøringene Del B krever. Vurder å bruke OpenRouter (`:free`-modeller,
  høyere dagskvote) som den andre modellen.
- `formler_brukt`-fiksen er avhengig av at modellen faktisk følger
  instruksen om å tagge `[ID]` i teksten – ikke alle modeller er like
  lydige på dette. Verdt å teste og kommentere på i `EKSPERIMENT.md`
  (nettopp den typen observasjon Del B ber om).
