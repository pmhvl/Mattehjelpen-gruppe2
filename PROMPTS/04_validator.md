# Prompt: `backend/validator.py` – numerisk validering

**Fil:** `backend/validator.py`
**Hvorfor:** Etterprøvbarhet er ikke valgfritt for ingeniører. Hvis appen
sier at en løsning stemmer, skal det være fordi dere faktisk sjekket det.

## Krav (fast)

- `validate(problem: str, losning: str) -> {"validert": bool, "detaljer": str}`
- Sett løsningen inn i det originale problemet og evaluer numerisk i (minst)
  3 punkter med SymPy `subs`/`evalf`.
- Vær ærlig: hvis validering ikke er mulig for denne oppgavetypen, **si det**
  i `detaljer` – ikke returner `validert: True` fordi det ser bra ut.

## [FYLL INN SELV] – ta stilling til dette FØR dere sender prompten

- Hva er «nært nok null»/riktig verdi numerisk (toleranse)? Flyttallregning
  er ikke eksakt. Bestem en toleranse (f.eks. `1e-6`) og begrunn kort hvorfor
  akkurat den:
  `____________________________________________`
- Hvilke oppgavetyper klarer dere IKKE å validere med denne metoden (f.eks.
  åpne/ubestemte integraler, symbolske svar uten tallverdi)? List dem opp –
  dette skal appen si ærlig fra om, ikke skjule:
  `____________________________________________`

## Ferdig prompt å lime inn (etter at dere har fylt inn over)

```
Implementer backend/validator.py sin funksjon
validate(problem: str, losning: str) -> dict som:
1. Bruker SymPy til å tolke problem og losning.
2. Setter løsningen inn i problemet og evaluerer numerisk i 3 tilfeldige
   punkter (subs + evalf).
3. Bruker toleranse [TOLERANSE FRA OVER] for å avgjøre om det stemmer.
4. Returnerer {"validert": bool, "detaljer": str} der detaljer forklarer
   HVA som ble sjekket og i hvilke punkter.
5. For oppgavetyper som ikke kan valideres slik (f.eks.
   [LISTEN DERES FRA OVER]): returner validert=False med en ÆRLIG forklaring
   i detaljer om AT og HVORFOR validering ikke var mulig – ikke lat som alt er OK.
```

## Kvalitetssjekk før du limer inn koden

- [ ] `validert` er aldri `True` uten at en faktisk numerisk sjekk ble gjort.
- [ ] Når validering ikke er mulig, sier `detaljer` det eksplisitt (ikke bare
      `"Feil"` uten forklaring).
- [ ] Dere har testet med en løsning dere VET er feil, og sett at
      `validert` faktisk blir `False`.
- [ ] Kjør `python scripts/selftest.py` – validator-sjekken bør nå vise ✅.
