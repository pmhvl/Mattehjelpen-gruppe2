# Foiler – interaktive forelesninger i Quarto

Forelesningsfoiler (reveal.js) for KI-innføringsmodulen, samlet i to
forelesninger à 2 timer med interaktive språkmodelldemoer.

- **Forelesning 1:** delen «Før oppgaven». Oppgaven deles ut mot slutten.
- **Forelesning 2:** delen «Erfaringer og veien videre», én uke senere. Start gjerne
  med erfaringsgjennomgangen i `GJENNOMGANG.md`.

## Kjør/bygg

```bash
# Installer Quarto: https://quarto.org/docs/get-started/
cd foiler
quarto preview forelesning_kort.qmd
quarto render forelesning_kort.qmd  # bygger self-contained HTML
```

HTML-filen er self-contained og kan deles/vises uten server.

## Interaktive gadgets i foilene

- **Live LLM-kall**: Foilene har innebygde paneler som kaller en språkmodell
  direkte fra nettleseren (via fetch). Lim inn en API-nøkkel i feltet på
  «koble til»-foilen i forelesning 1 (lagres kun i minnet, aldri på disk):
  - **OpenAI**-nøkkel (`sk-...`) fra platform.openai.com, eller
  - **OpenRouter**-nøkkel (`sk-or-...`) fra openrouter.ai – ett API, mange modeller.
  Bruk en nøkkel med lav kostnadsgrense, og slett den etter forelesningen.
- **Matte-rendering**: Modellsvar typesettes med MathJax – be gjerne modellen
  bruke LaTeX med `\( \)`-avgrensere (demo-promptene gjør dette allerede).
- **Modellduell**: Sammenlign to modeller side om side på samme matteoppgave.
- **Poll-foiler**: Enkle håndsopprekning/diskusjonsfoiler (bruk gjerne Mentimeter
  i tillegg om ønskelig).
- **Bilder**: Historiske bilder i `img/` er hentet fra Wikimedia Commons
  (offentlig eiendom) og bakes inn i HTML-filen ved rendring.
- Talenotater: trykk `S` i presentasjonen for speaker view.

> **NB:** Live-demoene krever nett og en API-nøkkel. Ha en skjermopptak-backup
> i tilfelle wifi/rate limits svikter – det er forresten også et poeng i kurset 😉

Ferdigrendret HTML deles manuelt ved behov.

