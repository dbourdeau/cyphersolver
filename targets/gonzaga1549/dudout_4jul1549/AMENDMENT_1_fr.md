# AVENANT C12-1 — borne de fin de la référence (écrit APRÈS gel de T41v-arb, AVANT tout décodage) — 17/11/2026
Constat à l'ouverture du déchiffrement d'époque (c. 43r-44r, autre main) : la portion 41v l. 1-18 commence après le clair
« Si ya no fuessen » (43v : « … luego si ya no fuessen en camino … ») et contient un seul mot en clair interne, [quod] (l. 10)
= « embaxadores » (« … llegada aqui delos dichos embaxadores »). Il n'y a pas de mot en clair après la l. 10 : la borne de fin
ne peut pas être fixée par un mot clair (PREREG §Référence). Règle mécanique fixée ICI, sans décodage :
1. Segment A = l. 1-9 + l. 10 jusqu'à [quod] exclu ; référence A = de « en camino » jusqu'au mot qui précède « embaxadores » inclus.
2. Taux r = lettres de la référence A (normalisée score_c12) / jetons du segment A.
3. Segment B = reste de l. 10 après [quod] + l. 11-18 (n_B jetons) ; référence B = depuis le mot qui suit « embaxadores », longueur
   cible r × n_B lettres, coupée à la frontière de mot la plus proche (égalité → la plus courte).
4. [quod] et « embaxadores » exclus des deux côtés. Abréviations développées : q/q̃ → que, vra → vuestra, embax → embaxadores, etc.
   (comme écrites développées par le scribe), lettres incertaines notées telles quelles.
5. Une seule mesure sur A+B (score_c12.py, graine 704, segments « A »). Fichier jetons = T41v-arb sans les mots en clair entre [].
