# PREREG-P03bis — AMENDEMENT 1 — 09/11/2026 ≈ 02:45 CET — AVANT toute transcription de 342
Constat (sur 340/341 seulement, aucun regard nouveau sur 342/343) : la calibration de PREREG-P03bis (e3532387…), par substitution
aléatoire UNIFORME de lettres, est dégénérée : N_V = −0,75 et N_P = −3,12, tous deux SOUS le meilleur témoin (N = 0) ; avec eux
n'importe quelle clé mélangée serait « validée ». Ce bruit détruit les n-grammes bien plus que les vraies erreurs de lecture
(340 décodé à 0,715 donne N = 1,11). Résultat conservé : mesure/CALIB_P03bis_v1_DEGENEREE.json.

## Seul changement : le modèle de dégradation de la calibration (tout le reste de P03bis inchangé)
- R2 (341 normalisé) découpé en unités « consonnes + voyelle » (regex [^aeiou]*[aeiou] | reste) = un signe chiffré.
- Erreur de lecture d'un signe simulée par unité : avec probabilité p, la partie consonne est remplacée par une valeur consonne
  tirée uniformément parmi les valeurs de « base » de CLE_v3 (signe mal lu) ; indépendamment, avec probabilité p, la voyelle est
  remplacée par une voyelle tirée uniformément (exposant mal lu).
- Pour chaque cible a ∈ {0,85 ; 0,6412}, p est choisi (recherche par pas de 0,005) pour que l'accord en caractères moyen
  (1 − Levenshtein/longueur, 50 tirages, graine 7) avec R2 soit le plus proche de a ; N(a) = moyenne des N de ces 50 tirages.
- Garde-fou ajouté : si N_P ≤ 0 ou N_V ≤ N_P, la calibration est déclarée invalide et AUCUNE mesure n'est faite.
- Seuils inchangés dans leur forme : VALIDÉE N ≥ N_V ; PARTIEL N_P ≤ N < N_V ; NON VALIDÉE N < N_P.
