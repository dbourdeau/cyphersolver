# PREREG — rakoczi-1632 (BSB Clm 10401, n. 139, fol. 491r-492v), écrit le 06/11/2026 (agent Opus 5.5), AVANT toute transcription de 491v-492v

## Antériorité et crédit
Cible **rakoczi1632 de WAINUT** dans le dépôt de Daniel (targets/rakoczi1632, 03/11/2026) : fol. 491r lu en partie
(54/69 mots chiffrés par la clé gelée), clé `key_frozen.tsv` (72 entrées, bâtie sur les gloses de 491r), test tenu à
l'écart sur 12 mots de 491v (90,8 %, borne haute). 491v-492v non faits. Fichiers lus en lecture seule et hachés dans
`wainut/SHA256-lecture-2026-11-06.txt` (key_frozen.tsv = 2b2aa8cb…6fe13). Tout résultat ici s'appuie sur la clé de
WAINUT et doit le créditer en premier.
Note : notre `ligue-1633/APPLICABILITE.txt` (04/11) a déclaré cette clé NON APPLICABLE au n. 206 (autre système,
chiffres collés dans un clair allemand) ; ce n'est pas une mesure de la clé sur son propre texte.

## Ce que j'ai vu au moment d'écrire
- WAINUT : NOTES, key_frozen, heldout_f491v (donc 12 gloses du haut de 491v).
- Scan 1200 (fol. 491v) : bande haute y < 560 à pleine résolution (gloses lisibles).
- Scans 1201 (fol. 492r) et 1202 (fol. 492v) : vignettes 260 px seulement (gloses et chiffres illisibles).

## Partie tenue à l'écart H
**H = tout le chiffre du scan 1202 (fol. 492v)**, toutes lignes, en ordre de lecture. Les nombres à 3 chiffres
(mots de code, ex. 217.11.99, 307) sont transcrits mais exclus de la mesure.
Transcription de H à partir de bandes recadrées par script (`scripts/crop_h.py`) centrées sur les lignes de chiffre,
la bande de glose au-dessus de chaque ligne étant blanchie ; aucune vue de 1202 à résolution lisible sans masque
avant le gel de `H-CHIFFRE.txt`. Si une glose déborde dans une bande, je le note dans `H-CHIFFRE.txt`.

## Clé mesurée K (une seule)
K = `key_frozen.tsv` de WAINUT (valeurs inchangées) **complétée** par nos paires glosées de fol. 491v et 492r
(scans 1200-1201, hors H), par script (`scripts/build_key.py`) :
- paires = mots chiffrés glosés dont le nombre de groupes (hors mots de code) = nombre de lettres de la glose
  normalisée (minuscules, j→i, v→u, u après q supprimé, non-lettres retirées) ; alignement lettre à lettre ;
- groupe absent de key_frozen → valeur = lettre majoritaire (≥ 1 occurrence ; égalité → toutes les lettres à égalité) ;
- groupe présent → valeur gelée gardée ; une 2ᵉ valeur s'ajoute si elle apparaît ≥ 2 fois sur 491v-492r ;
- K gelée (`KEY.tsv`, SHA dans `KEY.sha256`) AVANT toute lecture des gloses de H.

## Mesure (une seule)
Après gel de H-CHIFFRE puis de K, je lis les gloses de H (bandes de glose, `H-GLOSES.txt`, gelé SHA) ; puis
`scripts/measure.py` :
- pour chaque mot chiffré de H surmonté d'une glose lisible (appariement par position), décodage par K (groupe sans
  valeur = « ? », groupe à plusieurs valeurs = ensemble) ; alignement de Levenshtein entre décodage et glose normalisée ;
  correspondances = positions alignées où la lettre de glose ∈ valeur(s) du groupe ;
- car = Σ correspondances / Σ lettres de glose ; couverture C = part des groupes de H ayant une valeur dans K ;
- 200 témoins : permutations des valeurs (ensembles) de K entre les groupes de K présents dans H, graine 1632 ;
  marge = car − max(témoins).
- Seuils habituels : car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.
- Descriptif seulement (non décisif) : même calcul avec key_frozen seule.

## Ensuite
Lecture au sens de 491v-492v au compte de Daniel (mots chiffrés : sûrs / probables / restitués / irrésolus ; seuil
95 % sans restitués), gloses de Camerarius comprises comme source contemporaine. Si exploitable : PR-PREP.md (crédit
WAINUT, statut exact, aucune image MDZ dans la PR : clé et lecture seulement). Aucune PR ouverte.
