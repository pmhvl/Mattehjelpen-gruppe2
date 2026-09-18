# Prompt: `backend/formelsamling.py` – formelsamling med referanser

**Fil:** `backend/formelsamling.py`
**Hvorfor:** Sporbarhet. «Hvilken formel brukte du, og hvor står den?» er et
spørsmål enhver ingeniør må kunne svare på.

## Krav (fast)

Utvid `FORMELSAMLING`-dictet til ca. 15 formler. Hver oppføring skal ha:
`navn`, `formel` (LaTeX), `referanse` og `bruk` (én kort setning om når
formelen er relevant). Dekk minst:
derivasjonsregler, integrasjonsregler, karakteristisk ligning for ODE,
Eulers formel, determinant/egenverdier, delvis integrasjon.

## [FYLL INN SELV] – ta stilling til dette FØR dere sender prompten

- Hvilke formler er faktisk pensum i DERES mattekurs? Ikke bare kopier en
  generisk liste – sjekk emneplan/pensumliste og skriv opp 3–5 formler dere
  vet trengs, med sidetall fra DERES lærebok (Edwards & Penney / Thomas'
  Calculus / Tekniske Tabeller):
  `____________________________________________`

## Valgfri utvidelse: teoremer, ikke bare regneformler

`FORMELSAMLING` kan også inneholde kjente teoremer (f.eks. Pythagoras'
læresetning: `navn`, `formel` som `a^2 + b^2 = c^2`, `referanse` og en kort
`bruk`-tekst), ikke bare regneregler. Da får modellen et konkret holdepunkt å strukturere et
bevis-skjelett rundt når den blir bedt om et bevis – selv en svak modell kan
gjøre en anstendig jobb med riktig teorem servert, i stedet for å måtte
huske det perfekt selv. Dette gjør ikke selve beviset SymPy-verifisert, men
det gjør referansen etterprøvbar: dere kan sjekke om modellen faktisk brukte
riktig teorem riktig.

## Ferdig prompt å lime inn (etter at dere har fylt inn over)

```
Utvid dictet FORMELSAMLING i backend/formelsamling.py til ca. 15 formler.
Behold eksisterende oppføringer og format (id-nøkkel, felt: navn, formel som
LaTeX, referanse og bruk). Dekk: derivasjonsregler (produkt, kjerne, kvotient),
integrasjonsregler (delvis integrasjon, substitusjon), karakteristisk
ligning for 2. ordens lineær ODE, Eulers formel, determinant og egenverdier
for 2x2/3x3-matriser, løsning av lineære likningssystem.

Inkluder også disse spesifikke formlene fra pensum:
[LIM INN LISTEN DERES FRA "FYLL INN SELV" OVER]
```

## Kvalitetssjekk før du limer inn koden

- [ ] Alle oppføringer har `navn`, `formel`, `referanse` – ingen mangler felt.
- [ ] Alle oppføringer har en kort og konkret `bruk`-tekst som hjelper modellen
  å velge formelen og forklare hvorfor den brukes.
- [ ] LaTeX-formlene ser riktige ut (test dem gjerne på https://katex.org/ eller i frontend).
- [ ] Referansene er ekte (bok + kapittel/side) – ikke oppdiktet av modellen.
- [ ] Kjør `python scripts/selftest.py` – formelsamling-sjekken bør nå vise ✅.
