# KI for ingeniører – modulguide

*Innføringsmodul i ING100 – Ingeniørfaglig innføringsemne, Høgskulen på Vestlandet*

Denne guiden gir en samlet oversikt over KI-modulen i
[ING100](https://www.hvl.no/studier/studieprogram/emne/ING100) – for
studenter som vil vite hva som skjer når, og for forelesere som skal
undervise modulen. Alt materiell ligger i template-repoet
[sdy087/mattehjelpen](https://github.com/sdy087/mattehjelpen).

## Idéen bak modulen

Studentene skal ikke bare *høre om* KI – de skal **bygge, eksperimentere og
vurdere selvstendig**. Gjennom KI-assistert utvikling («vibe coding») lager hver 
gruppe *MatteHjelpen*: en webapp som løser førsteårsoppgaver i matematikk ved
å kombinere en språkmodell med deterministisk regning (SymPy) og numerisk
validering. Underveis erfarer de hvor språkmodeller er sterke,
hvor de feiler, og hva som skal til for å kunne *stole på* et svar og *ta ansvar* for noe KI har bygget.

Etter modulen skal studentene kunne:

- bruke KI-verktøy produktivt i utviklingsarbeid, med bevisste egne valg,
- vurdere KI-svar kritisk: sporbarhet, validering, og ærlighet når
  validering ikke er mulig,
- gjøre rede for kostnad/ressursbruk (tokens, ekstrapolering til reell skala),
- plassere KI i en etisk og regulatorisk ramme (EU AI Act, GDPR, opphavsrett,
  akademisk redelighet).

## Gratisprinsipp

Alle leverandører nevnt i `.env.example` (OpenRouter-modeller merket `:free`, Google AI Studio, Groq) har reell gratis-tilgang uten kredittkort. Grupper står fritt til å bruke kreditter/betalte modeller *frivillig*, typisk for å sammenligne kvalitet i eksperimentdelen (Del B) – men det skal aldri være en forutsetning for å fullføre Del A, og forelesere skal aldri legge opp til eller forvente at studenter betaler noe. Gratisnivåer hos leverandører endrer seg over tid – sjekk gjeldende vilkår ved kursstart.

## Opplegg og timeplan

Modulen består av to dobbeltforelesninger med én uke mellom. Første
forelesning gir det faglige grunnlaget og deler ut oppgaven. I uken mellom
arbeider gruppene selvstendig. Andre forelesning tar utgangspunkt i det
studentene faktisk erfarte og løfter diskusjonen mot kontroll, ansvar og
videre utvikling av KI.

| Tidspunkt | Aktivitet | Innhold |
|-----------|-----------|---------|
| Start | Forelesning 1: før oppgaven (2 t) | KI-historie, hvordan språkmodeller virker, live-demoer, verktøybruk og introduksjon til MatteHjelpen. **Oppgaven deles ut mot slutten.** |
| Uken mellom | Selvstendig gruppearbeid | Gruppene bygger appen, kjører eksperimentet og arbeider med refleksjonsnotatet. Målet er å ha nok erfaringer til forelesning 2. |
| Etter én uke | Forelesning 2: erfaringer med oppgaven (2 t) | Felles erfaringsgjennomgang, kontroll og ansvar, bro-parallellen, regelverk, agenter og veien videre. |
| Etter forelesning 2 | Ferdigstilling ved behov | Gruppene kan forbedre arbeidet fram mot innleveringsfristen: *(sett dato)*. |

## Innleveringsoppgaven (gruppearbeid)

Full beskrivelse med vurderingskriterier:
[OPPGAVE.md](https://github.com/sdy087/mattehjelpen/blob/main/OPPGAVE.md).
Tre deler:

- **Del A – Bygg appen (40 %).** Fyll ut fem skjelettfiler i `backend/` med
  KI-hjelp, styrt av mal-promptene i `PROMPTS/`. Kravene: all regning i
  SymPy-tools (ikke i modellens tekst), stegvise forklaringer,
  formelreferanser med formel-ID og bok/kapittel, numerisk validering,
  kostnadsestimat.
  `scripts/selftest.py` viser fremdrift hele veien.
- **Del B – Eksperimentér (30 %).** De samme 10 matteoppgavene testes med
  minst to modeller, med og uten tools (minst 40 kjøringer), dokumentert i
  [EKSPERIMENT.md](https://github.com/sdy087/mattehjelpen/blob/main/EKSPERIMENT.md).
  Inkluderer «aha-bryterne»: skru av tools, fjern stegvis forklaring, bytt
  modell, gi tvetydig input, fremprovoser valideringsfeil.
- **Del C – Reflektér (30 %).** Notat på 2–3 sider: kalkulator-analogien, hva
  som kreves for å oppdage feil, tillit («ville du dimensjonert en bro med
  dette?»), og hva «flink i matte» betyr nå.

Sensur skjer mot rubrikken i
[EVALUERING.md](https://github.com/sdy087/mattehjelpen/blob/main/EVALUERING.md)
– studentene ser nøyaktig samme rubrikk som sensor bruker.

## Ressursene i repoet

| Ressurs | For hvem | Hva |
|---------|----------|-----|
| [STUDENT_START.md](https://github.com/sdy087/mattehjelpen/blob/main/STUDENT_START.md) | Studenter | Steg-for-steg fra null forkunnskap (GitHub, Codespaces, Copilot, API-nøkkel) |
| [OPPGAVE.md](https://github.com/sdy087/mattehjelpen/blob/main/OPPGAVE.md) | Alle | Oppgaven med krav og vurdering |
| [SYSTEMBESKRIVELSE.md](https://github.com/sdy087/mattehjelpen/blob/main/SYSTEMBESKRIVELSE.md) | Studenter | Arkitekturkrav – «start-prompten» for vibe coding |
| [PROMPTS/](https://github.com/sdy087/mattehjelpen/blob/main/PROMPTS/README.md) | Studenter | Mal-prompter per modul, med obligatoriske egne valg og kvalitetssjekkliste |
| [EKSPERIMENT.md](https://github.com/sdy087/mattehjelpen/blob/main/EKSPERIMENT.md) | Studenter | Loggmal for Del B |
| [FEILSOKING.md](https://github.com/sdy087/mattehjelpen/blob/main/FEILSOKING.md) | Studenter | Vanlige feil, løses uten å vente på lærer |
| [EVALUERING.md](https://github.com/sdy087/mattehjelpen/blob/main/EVALUERING.md) | Forelesere + studenter | Sensur-rubrikk, kan KI-assisteres per gruppe |
| [foiler/](https://github.com/sdy087/mattehjelpen/blob/main/foiler/README.md) | Forelesere | Quarto/reveal.js-foiler for to forelesninger, med live LLM-demoer |
| [GJENNOMGANG.md](https://github.com/sdy087/mattehjelpen/blob/main/GJENNOMGANG.md) | Forelesere | Disposisjon for erfaringsdelen i forelesning 2 |
| `scripts/selftest.py` | Studenter | Fremdriftssjekk av format/kontrakt (ikke matematisk fasit) |
| `backend/` + `frontend/` | Studenter | Skjelettkoden som skal fylles ut (frontend er ferdig) |

## For deg som skal undervise modulen

- **Foilene:** `foiler/forelesning_kort.qmd`, bygges med `quarto render` (se
  `foiler/README.md`). Første del brukes før oppgaven og andre del i
  forelesning 2. Live-demoene i forelesning 1 trenger en API-nøkkel
  (OpenAI/OpenRouter) som limes inn i nettleseren under forelesningen – ha en
  klar, og ha skjermbilder i bakhånd ved nettverkstrøbbel.
- **API-tilgang:** Opplegget er leverandøruavhengig – alt som er
  OpenAI-kompatibelt virker (`API_KEY`, `MODEL_NAME`, `API_BASE_URL` i
  `.env`). Vis studentene gratis-alternativene i `.env.example`
  (OpenRouter `:free`-modeller, Google AI Studio, Groq) – ingen skal
  trenge å betale for å fullføre oppgaven.
- **Forelesning 2:** Start med gruppenes egne `EKSPERIMENT.md`-funn. Særlig
  aha-bryterne gir godt diskusjonsstoff før resten av etter-oppgave-delen. Se
  [`GJENNOMGANG.md`](https://github.com/sdy087/mattehjelpen/blob/main/GJENNOMGANG.md).
- **Sensur:** Følg oppskriften øverst i `EVALUERING.md` (KI-assistert
  rubrikk-utfylling per gruppe, `selftest.py --strict` + commit-historikk).
