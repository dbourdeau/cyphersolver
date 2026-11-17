# PREREG v2 — F 470 (UUB, Alvin 634917), chiffre « classe A », mesure sur L3
Rédigé le 17/11/2026 par l'agent Opus (fil 🔓, session v2). L4 (310-311) est GRILLÉE (mesure v1 échouée, PREREG.md).

## 1. Portion tenue à l'écart H2 = L3 — gel de la transcription (fait AVANT toute retouche de clé et tout décodage de L3)
- L3 = lettre « Saludek d. 21 Febr. 1706 » (n° 87, « Riga prod. d. 6 marty 1706 »), 2 exemplaires : A = 301-303, B = 306-308.
- Constat : B porte les MÊMES groupes que A (copie recopiée, non rechiffrée). B a donc servi de 2e lecture indépendante ;
  781 groupes de part et d'autre, 5 écarts arbitrés sur TIFF (transcr/L3/ARBITRAGE.md), dont 3 variantes réelles entre copies.
- **H2 = copie A (301-303), 781 groupes** (≥ 150 exigés). Fichiers gelés :
  cat transcr/L3/A_301.txt transcr/L3/A_302L.txt transcr/L3/A_302R.txt transcr/L3/A_303L.txt transcr/L3/A_303R.txt | shasum -a 256
  = fd85444f1341a4885d145ad56c9c943a157dec91829465b9625cf26e7ee9d859
  Copie B (contrôle, non mesurée) : cat transcr/L3/B_306.txt transcr/L3/B_307L.txt transcr/L3/B_307R.txt transcr/L3/B_308.txt | shasum -a 256
  = d801716f6a24869b986c37cbe38b75ee75a688738121c9c5128bed45985e5c68
- Écarts déclarés pendant la transcription (aucun décodage écrit, aucune lecture suivie) :
  (a) je connais par cœur une partie de la clé K (codes-mots fréquents : 605 med, 619 och, 663 som, 669 til, 678 wår, 516 Eder,
  542 för, 433 af…) et les ai reconnus en passant, sans assembler de phrase ;
  (b) le clair intercalé du document (en tête « … skrifwelser af den 24 Nov., 7 Decemb. och 13. samt 26 Januarij » ; au
  milieu « Grodno ofwanbemelte Eder påberopade skrifwelser widkommer, så hafwa Wij » ; fin « Och Wij befalle Eder Gud… »)
  a été lu : il fait partie du document (non chiffré) et donne le sujet général (réponse aux lettres de Lewenhaupt ; Grodno).
- Interdits jusqu'à la mesure : décoder L3 (même partiellement), ajuster une valeur de clé en regardant L3, ajouter au
  lexique/corpus un mot tiré de L3. Les codes de L3 absents de la clé ne seront PAS recherchés (pas de liste « codes à trouver »
  tirée de L3, contrairement à la v1).

## 2. Clé K2 (ajustée SANS L3) — gel
- Base : cle_K.json v1 (176 codes, 88d75d01…). Modifications et ajouts : work/K2_changes.tsv (48 lignes, source et confiance
  pour chacune). Sources : L1 (3 copies + déchiffrement d'époque de 293), L2 (295-296 + 297 avec leurs gloses d'époque),
  L4 (310-311, grillée pour la mesure, utilisée ici pour l'ajustement par lecture du contexte), structure du nomenclateur
  (blocs de syllabes consonne+voyelle par 5 : c 85-89, d 90-94, f 95-99, k 148-152, l 153-157, m 158-162, n 163-167,
  r 173-177 ; 2e série k 183-187 … w 223-227 ; 2e série de lettres = 1re + 35 ; mots en ordre alphabétique 400-680).
  Aucune valeur n'a été cherchée ni testée sur L3. Remarque : 298-299 (2e copie de L2) porte les mêmes groupes que 295-297
  (vu sur l'aperçu de 298) → aucune information de clé nouvelle, non transcrite.
- **cle_K2.json : 218 codes, SHA-256 faf24a308c1640dc79be7007eebb090b015d1f46df3468b0ee09510c56037424**

## 3. Métrique (gelée) et calibration (faite sur L1/L2/L4, corpus et chaînes aléatoires — jamais sur L3)
- Corpus suédois indépendant de F 470 : Carlson 1893 (lettres autographes de Charles XII, OCR archive.org, bloc <pre>, notes et
  lignes [ ] écartées) + pages sv.wikisource déjà récoltées en v1 (lexique/ws, 119 pages ; gardées si orthographe ancienne
  w ≥ v). Aucune nouvelle requête réseau. Normalisation (tools/corpus.py) ; 1 bloc de 2000 lettres sur 10 tenu à l'écart.
  work/corpus_train.txt 70bb066b46c7684ed79b6b4d33d01437f3d9bb90d7aaa1698b48629da4fbe586 ; work/corpus_heldout.txt a375652320cbc8c00bb9aa16fbcfa9f955c677aa82b23a062d3cfbf7c89e2f99
- Modèle : 5-grammes de lettres, décompte absolu interpolé D = 0,75, alphabet 29 lettres (tools/ngram.py c8d8a4e57e1a0e887fa1c6bc9e3ab2c5dc3334b3feb015727283c923a4629e42).
- Décodage (tools/score2.py 5a7aa3ca0fd315a7631a4edab234b1fd2206e5eed0048662b9f3f6fa8f903b72) : chaque suite de groupes chiffrés (entre mots en clair) → lettres ; un code
  absent de K2 coupe le segment (non compté). L = log2-vraisemblance moyenne par lettre.
- **Score N = (L − U) / (R − U)**, U = log2(1/29) = −4,858 (hasard uniforme), R = −2,456 = moyenne du held-out du corpus
  (work/calib_UR.json 4bc575e81e921465cec0340d181b42845d5ab16d287965029bd13f9fc2826445). Texte authentique ≈ 1 ; hasard uniforme ≈ −2,5.
- Calibration (tools/calib.py, tools/calib_plain.py) :
  · clair authentique de L1 (déchiffrement d'époque, 493 lettres) : N = 0,987 ; avec 2 % de lettres remplacées au hasard 0,83 ;
    5 % → 0,65 (min 0,45) ; 8 % → 0,42 ; 10 % → 0,36 ; 15 % → 0,01. Held-out du corpus : moy 1,00 ; 10 % de bruit → 0,22.
  · chaîne uniforme −2,46 ; held-out mélangé (unigrammes conservés) −1,30.
  · décodages par K2 (textes d'ajustement, donc optimistes) : L1 0,81-0,88 ; L2 0,68 ; L4 0,68 ; 200 clés permutées par texte :
    max 0,19-0,37 (aucune des 1 000 n'atteint 0,37). Décodage de L4 par l'ancienne clé K (non ajustée sur L4) : 0,62.
  · La métrique lexicale (couverture par mots du lexique) est écartée comme critère : même restreinte aux mots ≥ 4 lettres,
    des clés permutées couvrent 39-52 % de L4 (K2 : 57 %) — séparation trop faible (cause de l'échec v1). Rapportée pour info.
- **Seuils fixés AVANT la mesure : succès ssi N(K2, H2) ≥ 0,60 ET N(K2, H2) ≥ max(200 témoins permutés) + 0,30.**
  Justification de 0,60 au lieu de 0,85 : sur cette échelle, 0,85 correspond à un clair authentique de la même chancellerie
  avec ≤ 2 % de lettres fausses, niveau que même les lettres d'ajustement n'atteignent pas toutes (noms propres, mots
  étrangers « Commendo », « brouillera »…). 0,60 ≈ clair authentique avec ~5 % de lettres fausses (moyenne 0,65 ; min 0,45) :
  un décodage qui l'atteint est juste à ~95 % de ses lettres connues ; aucun témoin permuté n'a dépassé 0,37 en calibration.
  La marge + 0,30 au-dessus du meilleur témoin est celle de la consigne.
- Témoins : 200 clés obtenues en permutant les valeurs de K2 entre ses codes (random.Random(20261117)). Informatif, non
  décisif : 200 mélanges de l'ordre des groupes (graine 20261118), part de groupes inconnus, couverture lexicale ≥ 4 lettres
  (lexique v1 Lx.txt, 19c021bf…).
- Script figé : tools/measure2.py c5c74d42764d37044ac4aefe15a30ae94ee316d5cebced5771dc402e9771a227. Essai à blanc du script fait sur L4 (grillée, texte d'ajustement) :
  N = 0,679, témoins max 0,235 (aucune exécution sur L3).
- **Commande unique** (depuis v2/work) :
  /opt/homebrew/bin/python3.15 -I ../tools/measure2.py ../cle_K2.json calib_UR.json ../../lexique/Lx.txt ../transcr/L3/A_301.txt ../transcr/L3/A_302L.txt ../transcr/L3/A_302R.txt ../transcr/L3/A_303L.txt ../transcr/L3/A_303R.txt
- Après la mesure, H2 = L3 est grillée. Le résultat sera écrit dans MESURE-v2.json, quel qu'il soit.
