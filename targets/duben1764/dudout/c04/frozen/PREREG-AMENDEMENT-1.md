# C04 — AMENDEMENT 1 au PREREG (13/11/2026, 21:55 CET) — écrit AVANT tout décodage confronté au clair et avant la transcription du clair

## Fait nouveau
- Image 127-128 (A0073297_00127, _00128 ; SPOF_2 dl/full, téléchargées le 27/10, SHA dans dl/SHA256SUMS) = texte EN CLAIR de la lettre
  chiffrée 121-124L : note d'archiviste « Tillhör brev av den 31/12 1764 », « und[erdånigst?] 28 Jan 765 » ; incipit « Vous verrez avant
  l'arrivée de celle-ci que non seulement j'ai prévenu les ordres du Roi au sujet du Comte Osterman… », fin « …pour m'être rendus à mon retour ».
  Vue à 21:49 (aperçu), APRÈS l'écriture de N_draft.json (21:46:21, SHA 041840dd…) et du PREREG lexical (21:44).
- Daniel (profile.json, NOTES) : « No decipherment; one clear passage on 122R » → 127-128 n'avaient pas été reconnues.
- Ordre : le clair finit par « La suite … l'a bien prouvé depuis … de m'en pouvoir retourner » puis « J'attends de votre amitié … à mon retour »,
  contenu des lignes 122R.01-05 et 122R.09-12 (vu dans le décodage de C). Ordre de lecture du chiffré retenu (structure seulement) :
  121, 122L, 123R, 124L, 122R (122R.05c, passage en clair du chiffré, exclu).

## Conséquence sur le protocole
- La mesure lexicale du PREREG (C → H) est ANNULÉE avant exécution : H a désormais un clair connu (et entrevu sur l'aperçu de 127).
- Nouvelle mesure unique (re-test de la clé passée sur portion NEUVE, permis une fois) :
  * clé = c03/construction/key_c03.json (SHA b7fd19b0…), construite sur 118.00-119L.06 SEULEMENT, mesurée une fois le 12/11 sur
    119L.07-119R.05 ; jamais confrontée à 127-128 ;
  * chiffré = c03/transcr/lecture_121-124L.txt (transcription de Daniel, SHA ff500765…), 1 247 groupes, ordre ci-dessus ;
  * R = clair 127-128, transcrit en deux passes (la seconde sans regarder la première, arbitrage sur l'image), texte final
    (ajouts interlinéaires pris, mots barrés ôtés), normalisé a-z ; transcription gelée par SHA AVANT la mesure ;
  * D = décodage par la clé (valeur inconnue ou nulle → rien) ;
  * M = lettres de R couvertes par les blocs communs D/R de longueur ≥ 4 (difflib.SequenceMatcher, autojunk=False) / len(R)
    (métrique de c03/scripts/measure.py) ;
  * témoins (400, graine 1231) : 200 clés à chaînes permutées entre les mêmes valeurs ; 200 ordres mélangés des groupes ;
  * seuils (ceux de c03, fixés ici) : VALIDÉE si M ≥ 0,35 ET M > max(témoins) ET M − max(témoins) ≥ 0,15.
- Descriptif (pas une porte) : mêmes calculs avec K0 + c03b_ajouts ; et, valeur par valeur, les 15 valeurs de N_draft.json
  (écrites avant la découverte) jugées après alignement sur le clair : confirmée / infirmée / indécidable.
- Après la mesure : clé complétée par alignement 121-124L ↔ 127-128 (clé c04, datée, séparée) ; lecture = celle du clair d'époque,
  le décodage la suit groupe à groupe. Statut attendu : existing decipherment/clear (non inédit), contribution = identification du clair
  + validation de la clé B sur une seconde lettre + clé complétée.
