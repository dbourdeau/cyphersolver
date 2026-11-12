# PROTOCOLE — christianv-1673 (lead Daniel 2528 = 2531), écrit et figé AVANT toute lecture de la portion réservée

Date : 2026-11-11. Auteur : agent Opus (fil 🔓).

## Portion réservée
- Bloc final de l'ordre du 25 mai 1673 : pied de l'image 10 (3 lignes) + image 11 (l. 1-15), soit
  `working/transcr/CIBLE_img10-11.txt` (v0, transcription des groupes seulement) : **197 groupes, 399 signes chiffrés** (≥ 300).
- Aucune paire n'y est connue : pas de glose interlinéaire, la feuille volante (image 9 droite) s'arrête avant (fin = bloc 1, l. C19 « … med hverandre »).
- La transcription des groupes a été faite avant la clé ; elle n'a pas été décodée. Seule fuite à déclarer : en vérifiant la couverture de la clé 1674 v0, la liste
  des TYPES de la cible a été affichée avec leur valeur 1674 (dans l'ordre alphabétique, pas dans l'ordre du texte) ; aucun décodage suivi n'a été fait.

## Clé figée
- `working/KEY-v1.json` = groupes numériques de la clé 1674 (`working/key_1674_v0.json`, valeur majoritaire des gloses interlinéaires,
  images 32-37 et 39-43, relevé `working/pairs/1674_img*.tsv`) + paires de la feuille volante 1673 (`working/key_feuille_1673.tsv`), qui priment ;
  signes = valeurs de la feuille seulement (notation de notre transcription). Groupes absents de la clé : 32, 320, 348, 384, 534, 646, 906 (8 occurrences sur 197).

## Mesure unique (`scripts/mesure.py mesure`)
- Décodage déterministe groupe → valeur ; segments entre mots en clair ; COV = part des lettres décodées couvertes par une segmentation optimale
  en mots du lexique (da.json.gz de cyphersolver, origin/main 0c051c13, + mots des gloses 1674, mots en clair des ordres 1674, texte de la feuille volante),
  mots de ≥ 4 lettres + liste courte (at, og, de, …) ; normalisation w→v, ø/ö→o, æ→e, ck/c/q→k, ff→f, y/j→i, lettres doublées réduites.
- Témoins : 200 clés où les valeurs sont permutées entre groupes de 3 chiffres et, séparément, entre signes/petits nombres ;
  200 mélanges de l'ordre des groupes (graine 20261111).
- Étalonnage fait AVANT, sur le bloc 1 (non réservé ; optimiste car la clé et le lexique contiennent ses paires) : fenêtres de 150 groupes
  COV 0,750-0,875 ; marges sur témoins (50) : +0,088 à +0,24.
- Critères (tous requis) :
  - C0 : ≥ 85 % des groupes de la réserve ont une valeur dans la clé (189/197 = 95,9 %, constaté avant mesure) ;
  - C1 : COV ≥ 0,70 ;
  - C2 : COV ≥ max(200 clés permutées) + 0,06 ;
  - C3 : COV ≥ max(200 mélanges) + 0,06.
- Verdict : C0-C3 tenus → clé VALIDÉE sur la réserve, puis lecture par le sens ; sinon → RÉSULTAT négatif, pas de lecture présentée comme sûre.
- Une seule exécution. Toute correction de transcription faite APRÈS la mesure est consignée (v1) et ne refait pas la mesure.

## Lecture (après la mesure)
- Règle de Daniel : sûrs + probables ≥ 95 % des mots ; restitués et irrésolus = trous. Fiche : `LECTURE-CIBLE.md`.
