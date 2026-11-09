# PREREG — batavia-raad-1801 (NA 2.01.27.02 inv. 209, Smissaert → Prediger, 20 nov. 1800)
Écrit le 09/11/2026 (agent Opus 5.5, fil Déchiffrement), APRÈS transcription et hachage du chiffre
(`TRANSCR-chiffre-0002R.txt`, SHA-256 0614059ad5233e66468112366229aeafb88919534e39d3714ad3d5b9777bc1fa)
et AVANT toute lecture du clair (scans 0001, 0002 gauche, 0004, 0005 : vus seulement en vignette 400 px, illisible).

## Ce que je sais au moment d'écrire
- Le chiffré est un texte néerlandais **partiellement chiffré** : passages en clair intercalés (« maar evenwel, zoo wij
  hopen, eerlang », « is de Asiatische Raad », « waardoor, indien deselve »…).
- Unité chiffrée = colonne de 2 chiffres (haut 1-7, bas 1-4) → au plus 28 valeurs : substitution simple de lettres
  probable (grille 7×4). 61 est de loin le plus fréquent (≈ e ?). Aucune hypothèse de valeur n'est fixée ici.
- Scan 0003 = verso blanc (transparence de 0002) : **aucun autre chiffré dans le lot** ; l'étape « chiffre sans clair »
  est donc vide pour Batavia (sauf comparaison avec Janssens 1811, voir plus bas).

## Paires
- **H (tenue à l'écart, désignée d'avance) = lignes L13-L14** (tout le chiffré entre « dat Gij zen » et
  « tot deszelfs vertrek »), gelées dans `H-CHIFFRE.txt` (SHA-256 dans `H-CHIFFRE.sha256`).
- **A (apprentissage)** = lignes L01-L12, alignées sur le clair de la minute (0001 / 0002 gauche / 0004), lu
  progressivement et **arrêté au mot « zen »** ; le clair correspondant à H n'est ouvert qu'après gel de la clé.

## Clé mesurée (UNE), gelée avant ouverture du clair de H
- **K** : pour chaque valeur HB vue dans A, lettre majoritaire de l'alignement ; valeur absente de A → sans lettre.
  Gelée dans `KEY.tsv` + `KEY.sha256`.

## Clair de référence de H
- Le texte de la minute claire qui suit « dat Gij » jusqu'au mot qui précède « tot » ; bornes notées dans `H-CLAIR.txt`
  + SHA avant la mesure. Si la minute diffère (rédaction remaniée), on prend quand même ce passage, sans retouche.

## Mesure (une passe, `measure.py`)
- Normalisation : minuscules ; ij→y, ÿ→y, é/è→e ; non-lettres retirées ; décodage = concaténation des lettres de K pour
  les groupes de H ([x], ?3 et valeurs sans lettre → rien).
- car = Σ blocs `difflib.SequenceMatcher(None, décodage, référence, autojunk=False)` / lettres de la référence.
- couverture = part des groupes de H ayant une lettre dans K.
- 200 témoins : permutations des lettres de K entre ses valeurs (graine 1801) ; marge = car − max(témoins).
- **Seuils : car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.**
- H est ensuite grillé.

## Ensuite
- Lecture complète au compte de Daniel (sûrs / probables {x} / restitués [x] / irrésolus ‹…›), résumés FR + EN.
- Lien avec Janssens 1811 : comparer la *forme* du système (substitution de lettres vs code numérique) et, si les deux
  sont des substitutions, appliquer K au chiffre Janssens — test descriptif, non décisif, fait APRÈS la mesure.
- Images NA : licence à relever sur la notice (CC0 attendu), noter dans PR-PREP.md.
