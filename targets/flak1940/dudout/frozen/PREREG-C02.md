# PREREG C02 — luftgau-1940, Funkspruch 863–867 (4.6.1940) — figé AVANT toute lecture du chiffré de la partie 4

Date : 2026-11-11 (agent Opus, séance C02). Rien de la partie 4 n'a servi à trouver les clés.

## Clés proposées (numéros de clé par colonne, comme sur une carte)
- K1 (19, appliquée en premier au clair) : 9 14 17 1 12 6 18 3 16 10 4 8 19 13 7 2 11 15 5
- K2 (22, appliquée ensuite) : 19 22 9 17 1 12 7 16 21 13 10 20 4 18 2 15 6 3 8 11 5 14
- Déchiffrement : PT = undo(undo(CT, K2), K1) (dt.py), 1er groupe de chaque partie retiré (indicatif).
- Trouvées sur les parties 1 et 2 seulement (kpw.c, clair approché tiré du FS 862), confirmées par la lecture des parties 3 et 5 (dechiffre_P1235.txt).

## Mesure (une seule, measure_p4.py, figé ici par SHA-256)
- Chiffré : ligne P4 de working/T863-867.txt (transcription C01 du 28/10, non modifiée), 1er groupe retiré.
- Témoins : 200 paires de clés aléatoires (19, 22) appliquées au chiffré P4 + 200 permutations aléatoires du chiffré P4 déchiffrées avec les clés figées (graine 20261111) = 400 témoins.
- Scores : (a) quadrammes allemands, log10 moyen par lettre (qg.bin, corpus Gutenberg normalisé) ; (b) accord = 1 − distance d'édition / longueur, contre le clair PRÉDIT figé dans measure_p4.py (lignes Horb–Marbach et Ichenheim–Hornberg du FS 862, conventions des parties 1–3).
- Critère (fixé avant) : VALIDE si quadrammes ≥ meilleur témoin + 0,5 ET accord ≥ 0,85 ET accord ≥ meilleur témoin + 0,30. Sinon NON VALIDE, sans retouche des clés ni du critère.

## Écart à signaler
- Le 11/11, une commande d'inspection de sources/frames.json a affiché l'OCR NARA brut de la vue 866 (≈ 110 premiers caractères de la partie 4). Pas analysé, pas utilisé (les clés viennent des parties 1–2) ; signalé par honnêteté.
