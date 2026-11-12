# C03 — PREREG (système B, « Chiffer n° 2 », cat. Bourdeau 450) — écrit et gelé AVANT la mesure, 2026-11-12

## Matériau (SHA-256 dans SHA256SUMS-PREREG)
- Chiffré du 5 oct. 1764 (images 118 R – 119 R) : transcription de Daniel Bourdeau (targets/duben1764/tx/c1764-10-05.txt,
  cyphersolver origin/main 8a7cc00c7), reprise telle quelle (crochets [del:] ôtés, « ? » et « ' » ôtés).
  Les lignes 119L.07 – 119R.05 ont été relues par nous sur l'image pleine résolution (SPOF_2, dl/full/A0073297_00119.jpg)
  SANS clé : aucune divergence avec Daniel. Pas d'autre retouche.
- Clair d'époque : image 120 (transcription de Daniel p1764-10-05.final.txt, relue sur l'image) = clairs/120_clair.txt.
- Découpage :
  * CONSTRUCTION = 118.00 – 119L.06 (493 groupes) → transcr/build_118-119L06.txt ;
  * TENU À L'ÉCART (H) = 119L.07 – 119R.05 (328 groupes, ≥ 300) → transcr/holdout_119L07-119R05.txt.
    H n'a JAMAIS servi à construire la clé : ni alignement, ni ancre, ni point de passage. (Ses groupes ont été affichés
    une fois dans une liste indexée et relus sur l'image, sans décodage ni alignement.)

## Clé (gelée avant la mesure) : construction/key_c03.json
- Méthode : celle de key_c01 (EM d'alignement ancré, c01/scripts/align_em.py), adaptée (scripts/align_cp.py) :
  bande de ±30 lettres autour de 10 points de passage (construction/cp1.json, tous dans la partie CONSTRUCTION, posés sur
  des répétitions du chiffré : 215.9.549.317 « que j'ai », 155.453 « Votre Majesté », 403.240.709 « dis-po-si-», etc.)
  et 26 valeurs ancrées à la main (construction/anchors_final.json), 12 itérations.
- Constat : nomenclateur syllabique homophone (614 n, 119 r, 354 e, 712 u, 136 de, 410 re, 709 si…), quelques mots entiers
  (453 majesté, 155 votre, 54 interet), 549 = apostrophe (∅), 9 = j. Ce n'est PAS un système à clés changeantes.
- Règle de nettoyage fixée avant la mesure : chaîne de ≥ 5 lettres, non ancrée, vue < 1,5 fois → valeur inconnue (8 valeurs).

## Mesure unique (scripts/measure.py), graine 450
- D = décodage de H par la clé (valeur inconnue → rien).
- R = clair normalisé (a–z) à partir de la position 978 = fin de l'alignement de construction (calculée sur la seule
  CONSTRUCTION) jusqu'à la fin (« curer les secours les plus effectifs… Sire de Votre M. »).
- M = lettres de R couvertes par les blocs communs D/R de longueur ≥ 4 (difflib.SequenceMatcher, autojunk=False) / len(R).
- Témoins (400) : 200 clés à valeurs permutées (mêmes chaînes redistribuées entre les mêmes valeurs) ;
  200 ordres mélangés de H décodés par la vraie clé.
- Seuils (fixés maintenant) : VALIDÉE si M ≥ 0,35 ET M > max(témoins) ET M − max(témoins) ≥ 0,15.
  Sinon : NON VALIDÉE, aucune lecture annoncée, rien poussé.

## Ensuite (seulement si VALIDÉE)
- Lecture des pages sans clair d'époque : 121 (31 déc. 1764 v. st.), 122 L, 122 R, 123 R, 124 L — transcription de Daniel
  c-chiffer2-121-124.txt (1 247 groupes, gelée ici sous transcr/lecture_121-124L.txt), clé key_c03.json inchangée pour le
  décompte. Comptage selon la règle des 95 % de Daniel (mots lus en phrases / mots). Lecture « read » seulement ≥ 95 %.
- Une clé étendue sur 121-124 (si faite) sera datée et séparée ; elle ne change pas le résultat de cette mesure.
