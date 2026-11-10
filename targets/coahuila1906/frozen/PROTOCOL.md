# Protocole C01 — n° 758 coahuila-1906 (écrit le 2026-10-28 07:36 CET, avant le calcul de validation)

Corpus : 9 copies de télégrammes (M862 roll 342 ff. 0505–0513), transcrites dans working/TRANSCRIPTION.txt.

Observation de départ (lecture manuelle) : code = substitution littérale à homophones, nombres de deux chiffres,
dizaines appariées 1↔9, 3↔7, 4↔8 (même lettre pour n et n±80 / n±40), unité = position dans une rangée.

Apprentissage (seul matériau utilisé pour fixer la clé K1) :
- T36 (Cárdenas → Guajardo, 25/6) : ancre « para 40 76 43 99 73 75 quejas » = evitar.
- T104 (Guajardo → Cárdenas, 19/7).
Clé K1 = toutes les valeurs établies sur T36 + T104 seulement, puis gelée (SHA256 ci-dessous), étendue par la règle d'appariement des dizaines (règle établie aussi sur T36/T104 : o 30/70, c 34/74, r 35/75, a 33/73, d 10/90, t 19/99).

Tenu à l'écart (jamais utilisé pour fixer K1) : T35, T53, T67, T82, T99 (anglais), T124.
Mesure : couverture lexicale = part des lettres déchiffrées des passages chiffrés tenus à l'écart couvertes par une segmentation
en mots du lexique espagnol cyphersolver/lang/lexicons/es.json.gz (mots ≥ 2 lettres + « a », « y », « o »), anglais pour T99 ;
les nombres hors K1 comptent comme non couverts.
Témoins : 1000 clés mélangées (permutation aléatoire des lettres de K1 entre les valeurs, même structure d'homophones).
Critère : clé validée si couverture K1 > max des témoins et > 0,80.
T54 (juge Valdés Llano, valeurs 0x/5x/6x) : hors du système, traité à part.
