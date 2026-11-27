# PREREG v3 — Hautefort 1584, main 1 — barre standard du programme — 16/11/2026
Gelé AVANT tout regard rapproché sur la portion C (CHOIX-PORTION-C.md, sha 5eeff90b…) : fr. 15567 f. 160v (vue 167, moitié
gauche), lignes entières depuis la première ligne chiffrée jusqu'à ≥ 300 signes. Signes sous glose retirés ; clair exclu.
Transcription : deux passes sur des découpes différentes, la seconde sans consulter la première ; arbitrage sur l'image ;
conventions de A_f158r_pass1.txt / B_f161r_final.txt, avec « 12 » noté comme un seul signe (code vous) ; signe hors inventaire
= code nouveau (« ? »). Fichier mesuré : C_f160v_final.txt.
Clé : key_main1_v3.json = v1 + k = l, S3 = c (appris sur le développement : f. 158r, f. 161r l. 1-14 grillé) ; codes 14, 15,
16, 17, C2, f2 sans valeur (non levés : contextes insuffisants — « 15 17 de » deux fois, « la 15e intelligence »).
Mesure : tools/measure_v3.py — décodage ; signes-codes sans valeur = coupure de mot, hors dénominateur ; normalisation (accents,
ſ→s, v→u, j/y→i) ; score = part des lettres couvertes par une segmentation DP en mots ≥ 4 lettres du lexique
lexique-fr-cyphersolver.json (fréq ≥ 10) ∪ corpus lex/fr-henri4.txt + lex/fr-1520s-diplomatic.txt (fréq ≥ 3), plus une liste
fermée de mots outils (de, le, la, et, en, il, ne, se, ce, ie, que, qui, les, des, par, pas, est… ; ni « a » ni « y »).
200 témoins : mêmes signes, valeurs d'une lettre permutées (graine 20261116).
Barre (inchangée, celle du programme) : score ≥ 0,85 ET score ≥ meilleur témoin + 0,30. Une seule exécution.
Calibrage sur le développement seulement : f. 161r l. 1-14 (deux passes) 0,885 vs témoins max 0,532 (passerait) ;
f. 158r (une passe, bruitée) 0,797 vs 0,502 (échouerait). Versions écartées sur le développement : mots ≥ 3 (témoins 0,60-0,70),
mots ≥ 5 (réel 0,84), sans « a, y » retenu (témoins 0,60 → 0,53).
