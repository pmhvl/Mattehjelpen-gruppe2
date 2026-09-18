# TODO – forbedringer av repoet (for kursansvarlig)

Punkter for å tilpasse repoet til timeplanen i `KURSGUIDE.md`:
forelesning 1, én uke gruppearbeid og forelesning 2.

- [x] **Integrer erfaringsgjennomgangen i forelesning 2.** Se `GJENNOMGANG.md`.
- [x] **Frist-plassholdere i `OPPGAVE.md`** – lagt til, men eksakt dato må
      fortsatt fylles inn av kursansvarlig hvert semester.
- [x] **Fallback i `PROMPTS/02_formelsamling.md`** for grupper uten lærebok
      for hånden.
- [x] **Rydd `httpx`-deprecation-støyen** i `scripts/selftest.py`.
- [x] **Gratisprinsipp håndhevet eksplisitt** i `KURSGUIDE.md`,
      `OPPGAVE.md`, `README.md`, `STUDENT_START.md` og `.env.example` –
      oppgaven skal aldri kreve at studenter betaler noe.

## Gjenstår

- [x] **Del foilene i to forelesninger.** «Før oppgaven» brukes i
      forelesning 1 og «Erfaringer og veien videre» i forelesning 2. Husk å verifisere
      nyhetssaker og lenker markert i talenotatene før forelesning.
- [ ] **Sett eksakt frist-dato** i `OPPGAVE.md` og `KURSGUIDE.md` hvert
      semester (kan ikke automatiseres – avhenger av semesterplan).

Kursguide-PDF til utdeling lages med:

```bash
quarto render KURSGUIDE.md --to typst
```
