# Innleveringsoppgave: MatteHjelpen

**Gruppeoppgave. Verktøy: VS Code + KI, for eksempel GitHub Copilot.**

**Arbeidsperiode:** Oppgaven deles ut mot slutten av forelesning 1. Hovedarbeidet
gjøres fram mot forelesning 2 *(fyll inn eksakt dato her)*, der erfaringer fra
arbeidet brukes i undervisningen. **Innleveringsfrist:** *(fyll inn eksakt dato
her; fristen kan ligge etter forelesning 2)*. Full timeplan: se `KURSGUIDE.md`.

> **Gratisprinsipp:** Oppgaven skal kunne gjennomføres **uten at noen i
> gruppen bruker egne penger**. Bruk en leverandør med reell gratis-tilgang
> (se `.env.example` for alternativer). En betalt modell er kun et frivillig
> tillegg i eksperimentdelen (Del B) – aldri en forutsetning.

> **KI-bruk:** Dere kan bruke så mye KI dere vil, på alle deler av oppgaven –
> det er hele poenget. Men: **dokumentér bruken** (hvilke modeller, til hva)
> og vær forberedt på å **innestå for og forklare** alt dere leverer. Kan
> dere ikke forklare koden deres, er den ikke ferdig.

Dette dokumentet er utgangspunktet – start her. Alle andre filer i repoet er
verktøy for å løse denne oppgaven, ikke egne oppgaver i seg selv.

## 🗺️ Dokumentkart

| Dokument | Hva det er | Når du trenger det |
|---|---|---|
| [`README.md`](README.md) | Teknisk oversikt og rask oppstart | Første gang du åpner repoet |
| [`STUDENT_START.md`](STUDENT_START.md) | Steg-for-steg fra bunnen av | Du har aldri brukt GitHub/VS Code/Copilot før |
| [`SYSTEMBESKRIVELSE.md`](SYSTEMBESKRIVELSE.md) | Arkitektur og minimumskrav til koden | Før du begynner å kode |
| [`PROMPTS/`](PROMPTS/README.md) | Prompt-maler, én per modul | Når du faktisk skal skrive kode |
| [`scripts/selftest.py`](scripts/selftest.py) | Kjørbar fremdriftssjekk | Etter hver fil, og før innlevering |
| [`FEILSOKING.md`](FEILSOKING.md) | Løs vanlige feil selv | Noe krangler |
| [`EKSPERIMENT.md`](EKSPERIMENT.md) | Mal for eksperimentloggen | Del B |
| [`EVALUERING.md`](EVALUERING.md) | Rubrikken læreren bruker ved sensur | Før innlevering – sjekk selv først |

## Del A: Bygg appen

Dere skal ved hjelp av KI-assistert utvikling («vibe coding») lage en webapp som
løser typiske førsteårsoppgaver i matematikk (derivasjon, integrasjon, lineær
algebra, differensialligninger, komplekse tall – jf. Edwards & Penney:
*Differential Equations & Linear Algebra* og *Thomas' Calculus*).

Appen skal:

1. Ta imot en matteoppgave som tekst.
2. Bruke en språkmodell via API til å løse den – **men** all symbolsk/numerisk
   BEREGNING skal gjøres med et deterministisk verktøy (SymPy), ikke av
   modellen selv. Noen matteoppgaver er ikke beregninger (f.eks. «bevis
   Pythagoras' læresetning», eller andre bevis-/begrepsoppgaver) – da skal
   appen resonnere i tekst, men si ærlig fra at svaret ikke er verifisert av
   et verktøy.
3. Vise **stegvis løsning med forklaring**, ikke bare svaret.
4. Oppgi hvilke formler som er brukt, med formel-ID, navn og bok-/kapittelreferanse
  fra den innebygde formelsamlingen (à la Jarle Johannessen: *Tekniske
  Tabeller*). Knytt formelen til steget der den faktisk brukes.
5. Validere svaret numerisk (f.eks. sette løsningen inn i differensialligningen)
   og vise valideringsresultatet i frontend.

Bruk `SYSTEMBESKRIVELSE.md` som start-prompt. Dere står fritt til å forbedre og
utvide, men kravene over skal oppfylles.

## Del B: Eksperiment (viktigst!)

Test appen med **minst to modeller av ulik kvalitet** på de samme **10
oppgavene** fra mattekurset, både med og uten tools. Det gir minst 40 kjøringer
totalt. Dokumenter i tabellen i `EKSPERIMENT.md`.

Spørsmål dere skal besvare:

- Hvor ofte feiler en billig/gratis modell **uten** tools? Med tools?
- Hva koster 10 oppgaver i tokens/kroner? Hva ville 1000 studenter × 50 oppgaver kostet?
  (Bruk gjerne en gratis modell til selve appen, og regn kostnadsestimatet ut
  fra tokenforbruket uansett – dere trenger ikke betale noe for å svare på
  dette spørsmålet.)
- Hva skjer når modellen **misforstår** oppgaven (f.eks. tvetydig notasjon som
  `sin^-1`)? Legg merke til at SymPy da regner *riktig* på *feil* problem.
- Hva gjør appen deres når valideringen feiler? Er det ærlig design?
- Gi appen en bevisoppgave (f.eks. «bevis Pythagoras' læresetning»). Sier den
  ærlig fra at svaret ikke er verifisert av et verktøy, eller later den som
  SymPy sjekket noe SymPy ikke kan sjekke?

### Aha-brytere dere skal prøve

1. **Skru av tools** (én linje i `llm_client.py`) → kjør de samme 10 oppgavene.
2. **Fjern «forklar hvert steg»** fra systemprompten → appen blir en svart boks.
3. **Bytt modell** i `.env` → mål kvalitet, latens og kostnad.
4. **Gi appen en tvetydig oppgave** → se misforståelsen forplante seg korrekt regnet.
5. **Fremprovoser valideringsfeil** → hvordan håndterer appen det?

## Del C: Refleksjonsnotat (2–3 sider)

- Når er appen et hjelpemiddel og når er den juks? Trekk paralleller til kalkulatoren.
- Hva må *du* kunne for å oppdage at appen tar feil?
- Ville du stolt på den for å dimensjonere en bro? Hvorfor/hvorfor ikke?
- Hva vil det si å være «flink i matte» når slike verktøy finnes?

## Leveranse

Dere leverer **lenke til gruppens GitHub-repo** (ikke zip-fil, ikke kode limt
inn andre steder). Repoet skal på innleveringstidspunktet inneholde:

- [ ] Fungerende app: `python scripts/selftest.py --strict` viser ingen ❌ og
  ingen ⏳.
- [ ] Reell commit-historikk fra alle gruppemedlemmer (`git log`) – ikke ett
      stort commit limt inn til slutt.
- [ ] Utfylt eksperimenttabell og observasjoner i `EKSPERIMENT.md` (Del B).
- [ ] Refleksjonsnotat (Del C) lastet opp som PDF i den samme innleveringen
      (Canvas/Inspera – se emnesiden), 2–3 sider.

Se `EVALUERING.md` for nøyaktig hva læreren ser etter i hver del – bruk den
som en sjekkliste på dere selv før dere leverer.

## Vurdering

| Del | Vekt |
|-----|------|
| A: Fungerende app | 40 % |
| B: Eksperiment og dokumentasjon | 30 % |
| C: Refleksjonsnotat | 30 % |

Detaljert rubrikk med konkrete kjennetegn per karaktersjikt: se `EVALUERING.md`.
