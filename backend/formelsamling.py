"""Innebygd formelsamling – à la Jarle Johannessen: «Tekniske Tabeller».

Modellen skal referere til formler herfra i sine forklaringer.
Utvid gjerne med formler fra Edwards & Penney og Thomas' Calculus.

Feltet «bruk» hjelper modellen å velge regel. Modellen oppgir formel-ID i
løsningssteget; appen kontrollerer ID-en og henter navn og referanse herfra.

HVORFOR: Sporbarhet. «Hvilken formel brukte du, og hvor står den?» er et
spørsmål enhver ingeniør må kunne svare på.
"""

FORMELSAMLING = {
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
    "I1": {
        "navn": "Delvis integrasjon",
        "formel": r"\int u\,dv = uv - \int v\,du",
        "referanse": "Thomas' Calculus, kap. 8",
        "bruk": "Når integralet inneholder et produkt som blir enklere etter derivasjon av én faktor.",
    },
    "O1": {
        "navn": "Karakteristisk ligning (2. ordens lineær ODE)",
        "formel": r"ar^2 + br + c = 0 \text{ for } ay'' + by' + cy = 0",
        "referanse": "Edwards & Penney, kap. 3",
        "bruk": "Når en homogen lineær differensialligning med konstante koeffisienter skal løses.",
    },
    "K1": {
        "navn": "Eulers formel",
        "formel": r"e^{i\theta} = \cos\theta + i\sin\theta",
        "referanse": "Buanes: Komplekse tall",
        "bruk": "Når komplekse tall skal kobles mellom eksponentialform og trigonometrisk form.",
    },
    "M1": {
        "navn": "Determinant (2x2)",
        "formel": r"\det\begin{pmatrix}a & b\\ c & d\end{pmatrix} = ad - bc",
        "referanse": "Edwards & Penney, kap. 4",
        "bruk": "Når determinanten til en 2x2-matrise skal beregnes eller inverterbarhet vurderes.",
    },
    # TODO: Utvid til ~15 formler. Dekk derivasjon, integrasjon, ODE,
    # lineær algebra og komplekse tall.
}
