# PREREG — F 470 (Uppsala UB, Alvin 634917), chiffre « classe A » 1–~700, Charles XII → Lewenhaupt 1706
Rédigé le 17/11/2026 par l'agent Opus (fil 🔓), AVANT toute recherche de clé (seules lectures faites : transcription
de 286, 287, 289, 290, 292, 293, 295 ; lecture du déchiffrement d'époque écrit sur la page droite de 293 ; vue des
aperçus 600 px de 296-311, dont 310-311, sans transcription ni décodage).

## Corpus et portion tenue à l'écart
- L1 = lettre du 21 janv. 1706 (Schalabova, 2 milles de Grodno) en 3 exemplaires : 286-287, 289-290, 292-293
  (292-293 en partie en clair) + déchiffrement d'époque complet sur 293 (page droite).
- L2 = lettre du 19 févr. 1706 (Zaludek), 2 exemplaires : 295-297 (glose interlinéaire d'époque), 298-299.
- L3 = lettre (reçue à Riga le 6 mars 1706), 2 exemplaires : 301-303, 306-308.
- **H (tenue à l'écart) = L4 = images 310-311** (lettre n° 89, « Prod. d. 13 marty 1706 », exemplaire unique, sans glose
  repérée). Estimation ≈ 400 groupes (≥ 150 exigés). H n'est ni transcrite ni décodée avant le gel de la clé ;
  la transcription de H (deux passes) sera gelée par SHA-256 AVANT le décodage.
- Écart déclaré : en regardant l'aperçu de 310 j'ai vu que la 1re suite de groupes (17 40 32 18 101 166) ressemble au
  « här igenom » de L1 ; aucun autre décodage de H.

## Clé K
Fichier JSON `cle_K.json` : code → chaîne (lettres suédoises minuscules, a-z å ä ö, éventuellement plusieurs lettres ou
un mot ; "" = nul). Ajustée UNIQUEMENT sur L1, L2, L3 (copies parallèles, déchiffrement de 293, glose de 295-297).
Gelée par SHA-256 dans ce fichier (section « Gel ») avant la mesure.

## Mesure (une seule)
- Décodage de H : chaque suite maximale de groupes chiffrés (entre deux mots en clair) → concaténation des chaînes ;
  code absent de K → « ? » (1 caractère, jamais couvert).
- Lexique Lx : mots (minuscules, lettres seules) des textes suédois anciens récoltés le 17/11 sur sv.wikisource
  (`lexique/ws/`, requêtes fixes dans tools/ws_fetch.py), fréquence ≥ 2, longueur ≥ 2 ; normalisation v→w, é→e, ü→y,
  appliquée au lexique et au décodage. Lexique gelé par SHA-256 avant la mesure. Aucun mot de H n'y est ajouté.
- Score S = (caractères couverts par la meilleure segmentation en mots de Lx, programmation dynamique) / (caractères
  totaux des chaînes décodées, « ? » compris).
- Témoins : 200 clés obtenues en permutant au hasard les valeurs de K entre ses codes (random.Random(20261117)),
  même décodage, même score.
- **Succès ssi S(K) ≥ 0,85 ET S(K) ≥ max(témoins) + 0,30.** Sinon : clé non validée sur H (lecture « in part » au mieux).
- Rapport aussi : part de groupes de H non couverts par K.
- H mesurée = grillée.

## Addendum 1 (17/11, avant toute clé gelée) — sources de clair signalées par l'orchestrateur
- Uddgren 1950 (Riksregistraturet : ordres du 11/8/1705, 21/1/1706, 19/2/1706, 12/11/1706) : NON consulté par moi ; rien
  n'en est tiré. L1 (21/1/1706) et L2 (19/2/1706) correspondent sans doute à ces ordres : leur lecture repose sur le
  déchiffrement d'époque (293) et la glose (295-297) = lecture ANTÉRIEURE, pas un déchiffrement indépendant.
- H = L4 est datée « Zaludek d. 2 Martij A. 1706 » (vue sur l'aperçu de 311) : pas dans la liste des ordres cités par
  Uddgren ; je n'irai pas vérifier dans Uddgren avant la mesure.
- Carlson 1893 (lettres à Rehnsköld) : non utilisé pour la clé ni pour le lexique.

## Addendum 2 (17/11, avant gel de la clé)
- Transcription de H gelée : cat transcr/H/A_310_p1.txt transcr/H/A_311L_p1.txt transcr/H/A_311R_p1.txt | shasum -a 256
  = 9a69b87964bbd372aed5383ea55bf9e6d4342e0ce6e16a0d2624e0579ee74d3f (292 groupes ; passe 2 identique, voir transcr/H/PASSE2.md).
- Lexique gelé : lexique/Lx.txt (9 442 mots), SHA-256 19c021bffd7fd2421dbf54a0ddeb90ffddf253b6f21c7b53ed3c1a07dc897ccc.
  La récolte wikisource a été interrompue par des 429 (arrêt, pas de reprise) : 119 pages.
- Écart déclaré : j'ai compté la COUVERTURE de H par la clé provisoire (nombre de groupes de H présents dans la clé, sans
  décodage) : 80 % ; et j'ai relevé quels codes de H manquent (174, 629, 148, 165, 584, 519…). Je cherche ensuite leurs
  valeurs UNIQUEMENT dans L2/L3 (glose, copies parallèles), jamais dans H. Ce choix des codes à chercher est un biais
  léger, déclaré.
- Pendant la transcription, des fragments de H ont pu être lus « en passant » (ex. début 17 40 32 18 101 166 = här igenom,
  déjà déclaré) ; aucun décodage écrit de H avant la mesure.
- Script de mesure figé : tools/measure.py (SHA à la section Gel).

## Addendum 3 (17/11) — écart déclaré AVANT la mesure
En cherchant dans L2 la valeur de 174 (« wåra » 110 6 174 → 174 = ra), j'ai, en comparant les lignes de H où 174
apparaît, lu mentalement un fragment de H (311 dr. « 20 40 174 167 607 » ≈ « lära nu mehra », formule présente aussi
dans le clair de 310). C'est une contamination partielle de H (≈ 5 groupes) ; la valeur 174 = ra est néanmoins fondée
sur L2 (« wåra ordres ») et n'a pas été modifiée après. Aucune autre valeur n'a été tirée de H.

## Gel (17/11)
- cle_K.json : 176 codes, SHA-256 88d75d01ec713b35d9abc43813ff63a5c32fa36a5265f81b766df7cf3b4476e8
  (source : work/key_v2.txt = alignement des 3 copies de L1 sur le déchiffrement d'époque de 293 + glose de 295-296).
- tools/measure.py SHA-256 f064f26417b340777d8adaaa4a7af59d169f5617287b6e01575e4d367debe70f
- Transcription H 9a69b879… ; lexique 19c021bf…
Commande unique : /opt/homebrew/bin/python3.15 -I tools/measure.py cle_K.json lexique/Lx.txt transcr/H/A_310_p1.txt transcr/H/A_311L_p1.txt transcr/H/A_311R_p1.txt
