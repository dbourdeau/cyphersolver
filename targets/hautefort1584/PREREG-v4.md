# PREREG v4 — Hautefort 1584, main 1 — dernier essai, barre standard — 16/11/2026
Gelé AVANT tout regard rapproché sur la portion D (CHOIX-PORTION-D.md, sha 40348ec1…) : fr. 15567 f. 161v (vue 168, moitié
gauche), lignes entières depuis la première ligne chiffrée jusqu'à ≥ 300 signes ; si < 300 signes chiffrés : arrêt, pas de mesure.
Transcription : deux passes sur des découpes différentes, la seconde sans consulter la première ; arbitrage sur l'image ;
conventions de C_f160v_final.txt, SAUF : **tout ∂ sans trait croisé en tête est noté D, sans décision m/s** (on ne transcrit
plus S) ; ẟ (trait croisé en tête) = 8 ; « 12 » = un seul signe ; signes sous glose retirés ; clair exclu ; signe hors inventaire
= « ? ». Fichier mesuré : D_f161v_final.txt.
Clé : key_main1_v4.json = v3 + D = S = « m|s » (ambigu) + ◊ = y (appris sur C, grillée : n'auoit, Sauoye, moyen).
Codes 14, 15, 16, 17, C2, f2 : sans valeur, coupure de mot hors dénominateur (non levés).
Règle d'arbitrage « ∂ = m|s ambigu, tranché au lexique » (tools/measure_v4.py, mécanique) : chaque D vaut {s, m} ; la
segmentation DP choisit, mot par mot, la lettre qui fait entrer la chaîne dans le lexique (même lexique figé que v3) ; maximum de
lettres couvertes ; à égalité, ordre figé s puis m ; un D hors mot couvert est compté non couvert.
Métrique : identique à v3 (mots ≥ 4 lettres lexique fréq ≥ 10 ∪ corpus fr-henri4 + fr-1520s fréq ≥ 3 + liste fermée de mots
outils sans « a » ni « y » ; normalisation accents, ſ→s, v→u, j/y→i ; score = lettres couvertes / lettres).
Témoins (200, graine 20261116) : permutation des valeurs entre tous les signes à une lettre ET les signes « m|s » — la valeur
ambiguë « m|s » circule donc dans la permutation et le témoin qui la reçoit bénéficie du même arbitrage au lexique.
Barre (inchangée) : score ≥ 0,85 ET score ≥ meilleur témoin + 0,30. Une seule exécution.
Calibrage sur le développement seulement : C f. 160v (grillée, ◊ appris dessus) 0,910 vs 0,553 ; B f. 161r l. 1-14 0,878 vs
0,523 (passeraient) ; f. 158r (une passe bruitée) 0,806 vs 0,487 (échouerait).
