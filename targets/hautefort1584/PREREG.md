# PREREG v2 — Hautefort 1584, main 1 (fr. 15567 f. 158) — 16/11/2026, gelé AVANT tout regard rapproché sur la portion B
Portion aveugle : celle fixée par CHOIX-PORTION-B.md (sha a76adb8b…) : fr. 15567 f. 159r, premières lignes (ordre du
manuscrit) jusqu'à ≥ 300 signes chiffrés ; complétée par f. 161r si besoin. Glose interlinéaire éventuelle masquée, ses signes exclus.
Transcription : deux passes indépendantes (la seconde sans regarder la première), mêmes codes de formes que A_f158r_pass1.txt ;
arbitrage sur l'image ; tout signe hors inventaire = code nouveau (décodé « ? »). Fichier mesuré : B_f159r_final.txt.
Clé : key_main1_v1.json (gelée ci-dessous par SHA-256) — table de Tomokiyo (cryptiana, « Hautefort's Cipher ») corrigée sur
f. 158r et f. 160r. Aucune modification après gel.
Mesure unique : tools/measure.py (gelé ci-dessous) : décodage ; normalisation (accents ôtés, v→u, j/y→i) ; score = part des
lettres couvertes par une segmentation de programmation dynamique en mots du lexique lexique-fr-cyphersolver.json (fréq ≥ 10) ∪
mots du corpus Henri IV (fréq ≥ 10), mots de ≥ 4 lettres seulement ; « ? » jamais couvert (mesure lexicale). 200 témoins : mêmes signes, valeurs
d'une lettre permutées au hasard (graine 20261116), codes multi-lettres inchangés.
Seuil de réussite (mesure lexicale, seuils fixés avant regard) : score ≥ 0,40 ET score ≥ meilleur témoin + 0,20.
Pourquoi v2 : la v1 (mots ≥ 2 lettres, seuil 0,85/+0,30) a été essayée sur le seul matériau d'apprentissage (f. 158r) :
réel 0,93 mais témoins jusqu'à 0,96 → mesure non discriminante, abandonnée (superseded/). Calibrage v2 sur f. 158r :
réel 0,54, témoins max 0,17, moyenne 0,09. Aucune donnée de la portion B n'a été vue. Une seule exécution ; la portion est ensuite grillée.
Ensuite : lecture par le sens (règle de Daniel, ≥ 95 % des mots sûrs + probables = read).
