"""Innebygd formelsamling – à la Jarle Johannessen: «Tekniske Tabeller».

Modellen skal referere til formler herfra i sine forklaringer.
Utvid gjerne med formler fra Edwards & Penney og Thomas' Calculus.

Feltet «bruk» hjelper modellen å velge regel. Modellen oppgir formel-ID i
løsningssteget; appen kontrollerer ID-en og henter navn og referanse herfra.

HVORFOR: Sporbarhet. «Hvilken formel brukte du, og hvor står den?» er et
spørsmål enhver ingeniør må kunne svare på.
"""

FORMELSAMLING = {
    # Derivasjon
    "D1": {
        "navn": "Produktregelen",
        "formel": r"(uv)' = u'v + uv'",
        "referanse": "Thomas' Calculus, kap. 3",
        "bruk": "Når et produkt av to funksjoner skal deriveres.",
    },
    "D2": {
        "navn": "Kjerneregelen",
        "formel": r"\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}",
        "referanse": "Thomas' Calculus, kap. 3",
        "bruk": "Når en sammensatt funksjon skal deriveres.",
    },
    "D3": {
        "navn": "Brokregelen (Kvotientregelen)",
        "formel": r"\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}",
        "referanse": "Thomas' Calculus, kap. 3",
        "bruk": "Når en brøk/kvotient av to funksjoner skal deriveres.",
    },
    "D4": {
        "navn": "Potensregelen for derivasjon",
        "formel": r"\frac{d}{dx}(x^n) = n x^{n-1}",
        "referanse": "Thomas' Calculus, kap. 3",
        "bruk": "Når en potensfunksjon skal deriveres.",
    },
    
    # Integrasjon
    "I1": {
        "navn": "Delvis integrasjon",
        "formel": r"\int u\,dv = uv - \int v\,du",
        "referanse": "Thomas' Calculus, kap. 8",
        "bruk": "Når integralet inneholder et produkt som blir enklere etter derivasjon av én faktor.",
    },
    "I2": {
        "navn": "Integrasjon ved substitusjon",
        "formel": r"\int f(g(x))g'(x)\,dx = \int f(u)\,du",
        "referanse": "Thomas' Calculus, kap. 5",
        "bruk": "Når integralet inneholder en sammensatt funksjon ganget med kjernens deriverte.",
    },
    "I3": {
        "navn": "Potensregelen for integrasjon",
        "formel": r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)",
        "referanse": "Thomas' Calculus, kap. 5",
        "bruk": "Når ubestemte integraler av potensfunksjoner skal beregnes.",
    },
    
    # Differensialligninger (ODE)
    "O1": {
        "navn": "Karakteristisk ligning (2. ordens lineær ODE)",
        "formel": r"ar^2 + br + c = 0 \text{ for } ay'' + by' + cy = 0",
        "referanse": "Edwards & Penney, kap. 3",
        "bruk": "Når en homogen lineær differensialligning med konstante koeffisienter skal løses.",
    },
    "O2": {
        "navn": "Integrerende faktor (1. ordens ODE)",
        "formel": r"y' + P(x)y = Q(x) \implies v(x) = e^{\int P(x)dx}",
        "referanse": "Edwards & Penney, kap. 1",
        "bruk": "Når en 1. ordens lineær differensialligning skal løses ved hjelp av integrerende faktor.",
    },
    "O3": {
        "navn": "Separable differensialligninger",
        "formel": r"\frac{dy}{dx} = g(x)h(y) \implies \int \frac{1}{h(y)}dy = \int g(x)dx",
        "referanse": "Edwards & Penney, kap. 1",
        "bruk": "Når variablene i en differensialligning kan skilles på hver sin side av likhetstegnet.",
    },

    # Komplekse tall
    "K1": {
        "navn": "Eulers formel",
        "formel": r"e^{i\theta} = \cos\theta + i\sin\theta",
        "referanse": "Buanes: Komplekse tall",
        "bruk": "Når komplekse tall skal kobles mellom eksponentialform og trigonometrisk form.",
    },
    "K2": {
        "navn": "Modulus og argument (Polarform)",
        "formel": r"z = r(\cos\theta + i\sin\theta) = r e^{i\theta}, \quad r = |z| = \sqrt{a^2+b^2}",
        "referanse": "Buanes: Komplekse tall",
        "bruk": "Når et komplekst tall z = a + ib skal skrives på polar- eller eksponentialform.",
    },

    # Lineær algebra og matriser
    "M1": {
        "navn": "Determinant (2x2)",
        "formel": r"\det\begin{pmatrix}a & b\\ c & d\end{pmatrix} = ad - bc",
        "referanse": "Edwards & Penney, kap. 4",
        "bruk": "Når determinanten til en 2x2-matrise skal beregnes eller inverterbarhet vurderes.",
    },
    "M2": {
        "navn": "Invers matrise (2x2)",
        "formel": r"A^{-1} = \frac{1}{\det(A)}\begin{pmatrix}d & -b\\ -c & a\end{pmatrix}",
        "referanse": "Edwards & Penney, kap. 4",
        "bruk": "Når inversen til en inverterbar 2x2-matrise skal finnes direkte.",
    },
    "M3": {
        "navn": "Egenverdiligning",
        "formel": r"\det(A - \lambda I) = 0",
        "referanse": "Edwards & Penney, kap. 5",
        "bruk": "Når egenverdiene lambda til en kvadratisk matrise A skal beregnes.",
    },
}