# Protocole écrit AVANT calcul — abel-paris-1797 (rédigé 2026-10-28 20:24)

Objet : chiffre des rapports de C. K. Abel (Paris → Stuttgart), HStAS A 16 a Bü 696, 1797.
Nature constatée à la lecture des images (avant tout calcul) : nomenclateur mixte —
groupes numériques 1–99 (≈ lettres, homophones : a = 3/9, n = 70/67, f = 1/7 …),
codes de deux lettres minuscules (cc, cb, hh, gw…) pour des mots, avec exposants de flexion,
quelques groupes à 3 chiffres (125 ?) ; signes « o » (σ, cercle à queue) et « 0 » (cercle).
Les pièces chiffrées portent un déchiffrement interlinéaire d'époque (glose, autre main).

## Données
- Entraînement : Bild 7 et Bild 8 (rapport n° 117, 29 oct. 1797) ; au besoin Bild 29–30 (19 nov.).
- Tenu à l'écart (non regardé de près avant gel de la clé) : Bild 44 (rapport du 13 déc. 1797).
  Bild 50 (24 déc.) = second jeu tenu à l'écart si exploitable.

## Méthode
1. Transcrire jeton par jeton les passages chiffrés d'entraînement, aligner mot à mot sur la glose.
2. Clé = pour chaque jeton numérique, la lettre (ou suite) majoritaire dans l'alignement ;
   pour chaque code alphabétique, le mot glosé. Geler clé + transcription d'entraînement (SHA-256).
3. Transcrire ensuite Bild 44 (jetons seuls, puis glose séparément), geler (SHA).
4. Score : (a) caractères — part des lettres de la glose retrouvées par la clé sur les mots
   entièrement numériques (alignement mot à mot, distance d'édition) ; (b) mots — part des mots
   chiffrés (numériques + codes connus) dont la lecture par la clé = glose (à l'orthographe près :
   i/j/y, ä/ae, ss/ß, c/k confondus).
5. Témoins : 200 clés aléatoires (permutation des valeurs de la clé gelée entre jetons numériques,
   codes permutés entre eux), même score. Succès si clé ≥ 0,85 car. ET ≥ 0,75 mots, et clé > max des 200 témoins.
6. Lecture finale : règle de Daniel (≥ 95 % des mots lus par le sens ; détail sûrs / probables {x} /
   restitués [x] / irrésolus ‹…›).

## Remarque d'antériorité
La glose d'époque donne déjà le clair : l'apport est (i) la clé reconstituée (non numérisée : A 11 Bü 66,
L 6 Bü 1392, A 74 i Bü 24), (ii) le contrôle de la glose, (iii) l'application aux pièces non glosées
éventuelles (Bü 699, 701, 702).

## Avenant (2026-10-28 20:27, après score de Bild 44, AVANT toute transcription de Bild 29–31)
Résultat Bild 44 (10 mots numériques) : car. 0,898 ; mots 0,700 (échecs = 2 jetons jamais vus en entraînement, 42 et p2, + 1 glose douteuse) ;
témoins max 0,224 / 0,100. Bild 50 : 1 mot (9 54 6 15 90 02 → « albert », glose au crayon d'une main tardive « Georgi » ;
le paragraphe suivant, en clair, nomme « Albert » → la glose tardive est fausse).
Bild 29–31 (19 nov.) n'ont PAS servi à l'entraînement : ils deviennent un second jeu tenu à l'écart, scoré avec la MÊME clé gelée
(KEY_FROZEN.json, SHA c81b4985…), mêmes critères. Le résultat final = jeux 44 + 50 + 29–31 réunis.
