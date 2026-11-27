# PREREG — Lettre A Boissiran (AD17 4 J 1524, photos 160923/160935/160941) — 26/11/2026

Rédigé et haché AVANT tout décodage de la lettre. Une seule mesure.

## Objets gelés
- Clé : CLE-GELEE.md, SHA-256 9e059029fb875968c59ecfaa45ca6db4f6252430fcc568c7ab424efcd94d5d4d (table 3 de la feuille de clé, photo 162030).
- Transcription : transcription/TRANSCRIPTION-ARBITREE.txt, SHA-256 250228663369958b769f355cabd91e5df6021c6a4d11b1a9c32959611c18d86a (passes aveugles A et B par deux agents sans la clé, arbitrage par un 3ᵉ agent sans la clé).
- Lexique : besancon-ms1580-1582/ms62-test/LEXIQUE-FR-EARLY.txt (49 486 formes, français ancien et moderne), lu tel quel.

## Hypothèse
H1 : la lettre est chiffrée par la table 3 (clair → chiffre), chaque chiffre valant 2 ou 3 lettres :
0 {a,x} · 1 {d,p} · 2 {f,r} · 3 {b,h} · 4 {m,y} · 5 {e,l} · 6 {c,g,u} · 7 {i,n} · 8 {q,s} · 9 {o,t}.
Points suscrits ignorés. Groupe = suite de chiffres séparée par une espace dans la transcription.

## Portion tenue à part (mesurée une fois, puis grillée)
Lignes p2.23, p2.24, p3.01 à p3.08 (358 chiffres). La ligne de date p3.09 est exclue.
Doute [x/y] : les deux lectures sont admises. Tache « # » : le groupe qui la contient est compté comme échec.

## Mesure (script measure.py, haché avec ce PREREG)
Pour une clé K (10 ensembles de lettres affectés aux 10 chiffres), un groupe est « lu » s'il peut être découpé entièrement en mots du lexique, chaque mot de longueur ≥ 2 ou égal à « a » ou « y », sous au moins une expansion permise par K.
M(K) = groupes lus / groupes de la portion.
Témoins : 200 clés obtenues en permutant au hasard les 10 ensembles de lettres entre les 10 chiffres (graine 20261126, random.Random, shuffle ; une permutation identique à H1 est rejetée et retirée à nouveau).
Critère fixé d'avance : M(H1) ≥ 0,85 ET M(H1) ≥ max(M témoins) + 0,30.
Adaptation déclarée de la règle « accord caractères » : il n'existe pas de clair de référence, d'où un critère de lecture lexicale contre témoins.

## Lecture par le sens (règle de Daniel)
Après la mesure, et une seule fois : le décodage mécanique de toute la lettre (ensembles de candidats) est lu par le sens. Fiche : sûrs, {probables}, [restitués], ‹irrésolus›, chaque cas non sûr justifié. Critère : ≥ 95 % des mots lus par le sens sur une portion ≥ 300 caractères (la portion ci-dessus, puis la lettre entière rapportée à part).
Les découpages de mots et le choix de la lettre dans chaque ensemble sont faits par le sens : c'est inhérent à cette clé (chiffre à valeurs multiples), donc ils relèvent de la lecture, pas de la mesure.

## Écarts connus avant la mesure
- Pendant l'inventaire (avant ce PREREG), deux groupes fréquents ont été reconnus à l'œil avec la clé : « 865 » = que, « 15 » = de. Ils figurent dans la portion. Effet sur la mesure : nul (la mesure est mécanique), mais déclaré.
- Le crib de la lettre C (« a Bordeaux » noté en clair au-dessus de « 0?9215060 ») a été vu à l'inventaire ; il n'est pas dans cette lettre.
- L'arbitre a supprimé une tache en p1.19 qui peut cacher un chiffre (hors portion).
