"""LLM-klient for MatteHjelpen.

SKJELETT – TODO:
- Les API_KEY, MODEL_NAME og API_BASE_URL fra .env (python-dotenv).
- Bruk openai-biblioteket med base_url mot et OpenAI-kompatibelt API
  (f.eks. OpenRouter, OpenAI selv, eller en annen leverandør).
- SYSTEMPROMPT (viktig – ikke fjern kravene uten å forstå konsekvensen!):

  "Du er en matematikklærer for ingeniørstudenter. Bruk verktøyene (SymPy)
  til all beregning når oppgaven lar seg beregne slik – du skal ALDRI late
  som du har brukt et verktøy du ikke faktisk kalte. Kan oppgaven ikke
  beregnes (f.eks. et bevis eller en begrepsforklaring), resonnerer du i
  tekst og sier eksplisitt at svaret IKKE er verifisert av et verktøy.
  Forklar hvert steg pedagogisk på norsk, og oppgi nøyaktig hvilke
  formler/verktøy du faktisk brukte. Knytt hver formel-ID til steget der den
  brukes, og ta med navn og referanse fra formelsamlingen.
  Hvis du er usikker, si det eksplisitt."

  MERK: «all beregning gjøres via verktøy» gjelder ting SymPy faktisk kan
  regne (derivasjon, ligninger, matriser, ...) – ikke bevis eller
  begrepsforklaringer. Det er legitime matteoppgaver appen skal svare
  ærlig på, uten å late som SymPy validerte noe den ikke kan validere.

- ANTI-HALLUSINASJON: Ikke stol på at modellen forteller sant om egen
  verktøybruk. Bygg verktøyloggen fra faktiske tool_calls. Modellen kan
  foreslå formel-ID per steg, men ID-en må finnes i formelsamlingen; hent
  navn og referanse derfra i stedet for å stole på fri tekst.

- FORMELSAMLING: Send oppføringene fra formelsamling.py til modellen i et
  kompakt format med ID, navn, formel, bruk og referanse. Kontroller at alle
  returnerte formel-ID-er finnes i FORMELSAMLING. Formelreferanser forklarer
  metoden; de beviser ikke at et SymPy-verktøy faktisk ble kalt.

- Implementer tool-calling-løkke:
  1) Send oppgaven + tool-definisjoner fra tools.py
  2) Hvis modellen ber om tool-kall: kjør funksjonen, legg resultatet i samtalen
  3) Gjenta til modellen gir endelig svar
- Tell tokens (response.usage) og estimer kostnad.

EKSPERIMENT-BRYTER: Sett USE_TOOLS = False og se hva som skjer med en billig
modell. Dokumenter i EKSPERIMENT.md!
"""

USE_TOOLS = True  # <-- Aha-bryter nr. 1


def solve_task(oppgave: str) -> dict:
    """Løs en matteoppgave via LLM + tools. Returner dict iht. SYSTEMBESKRIVELSE.md."""
    raise NotImplementedError("Vibe code me! Se SYSTEMBESKRIVELSE.md")
