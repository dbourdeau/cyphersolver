# PREREG-2 — Lettre A Boissiran (AD17 4 J 1524) — 27/11/2026
Accord de Brice (relayé par le coordinateur) pour une 2ᵉ mesure sur portion neuve, après l'échec par conception de la 1ʳᵉ (MESURE-JOURNAL.md). Rédigé et haché AVANT la mesure sur la portion neuve.

## Objets gelés (inchangés)
- Clé : CLE-GELEE.md, SHA-256 9e059029fb875968c59ecfaa45ca6db4f6252430fcc568c7ab424efcd94d5d4d.
- Transcription : transcription/TRANSCRIPTION-ARBITREE.txt, SHA-256 250228663369958b769f355cabd91e5df6021c6a4d11b1a9c32959611c18d86a.
- Lexique : besancon-ms1580-1582/ms62-test/LEXIQUE-FR-EARLY.txt, formes de 4 lettres et plus seulement.

## Portion neuve
Lignes p1.01 à p1.09 (jamais décodées ni lues : la lecture de la 1ʳᵉ étape a porté sur p2.23–p3.09 ; seules p1.01–p1.02 ont été survolées à l'œil pour « receu … monsieur vostre lettre … mortifie … chagrin », déclaré ici comme écart — effet sur la mesure mécanique : nul).

## Métrique (measure2.py, haché avec ce PREREG)
Groupes retenus : groupes de 4 chiffres et plus, sans tache ni rature (un doute [x/y] admet les deux lectures).
Un groupe est « lu » si au moins une de ses expansions sous la clé K est EXACTEMENT une forme du lexique (≥ 4 lettres). Pas de découpage en plusieurs mots (c'est ce qui rendait la 1ʳᵉ métrique non discriminante).
M(K) = groupes lus / groupes retenus.

## Témoins (400)
- 200 clés permutées : les 10 ensembles de H1 répartis au hasard entre les 10 chiffres.
- 200 clés aléatoires de même structure : les 21 lettres de H1 mélangées et redécoupées en ensembles de mêmes tailles (2 ou 3 lettres par chiffre) ; une clé identique à H1 est rejetée.
Graine 20261127 (random.Random).

## Critère fixé d'avance
M(H1) ≥ 0,50 ET M(H1) ≥ max(M des 400 témoins) + 0,30.
Justification du seuil 0,50 (et non 0,85) : clair attendu en orthographe du XVIIIᵉ (receu, vostre, estoit…) absente en partie du lexique, et environ 3 % de chiffres douteux ou mal lus dans la transcription ; seul l'écart aux témoins est décisif.

## Contrôle de puissance (autorisé, sur portion déjà grillée)
Exécuté AVANT le hachage sur p2.23–p3.08 (grillée par la 1ʳᵉ mesure) : 51 groupes ; M(H1) = 0,7255 ; max témoins permutés = 0,2745 ; max aléatoires = 0,2745 ; moyenne des témoins = 0,0894 (MESURE2-burned.json). La métrique discrimine (écart 0,45). Le contrôle n'a pas servi à modifier la clé ni la transcription ; les seuils ont été fixés après ce contrôle, ce qui est déclaré.

## Une seule mesure
`python3 -I measure2.py neuve`, une fois. Portion p1.01–p1.09 grillée ensuite.

## Ensuite (si critère atteint)
Lecture par le sens de la lettre A entière (règle de Daniel : ≥ 95 % des mots sur ≥ 300 caractères ; sûrs / {probables} / [restitués] / ‹irrésolus› comptés à part et justifiés) ; puis lettres B et C (2 passes aveugles + arbitrage) ; vérification de la signature.
