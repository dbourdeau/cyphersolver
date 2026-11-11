# PREREG-1715 — lettre de Flemming à Wackerbarth, camp devant Stralsund, 20/10/1715 (Loc. 00712/05, scans 0380–0387, ff. 307–314)
Écrit le 11/11/2026 par l'agent Opus 5.5 (fil 🔓), AVANT tout décodage de 0380–0387 et AVANT la construction de la clé gelée.
Haché avec les scripts, les relevés et l'étalonnage (PREREG-1715.sha256). 🔴 Scans InC : recherche privée, aucune image publiée.

## 0. Ce qui a été vu avant ce texte (déclaré)
- Vignette réduite de 0380 (et planche réduite 0380–0387 à 450 px, illisible) vue au début pour repérer les pages ; les nombres de
  0380 étaient visibles sur la vignette ; aucun n'a été décodé.
- Apprentissage 0388–0390 relevé et aligné par moi (TRAIN-0388/0389/0390.txt, TRAIN.sha256 : 9efa5620… / d9d1d131… / effa7b40…).
- Cible 0380–0387 relevée À L'AVEUGLE par deux sous-agents Opus sans accès aux gloses, aux clés ni à 0388–0390
  (CIBLE-*.txt ; CIBLE-A.sha256, CIBLE-B.sha256, CIBLE-0384g.sha256 = 723e30a7…). 1722 + 1693 groupes.
- **Incident** : en vérifiant les hachages, j'ai affiché à l'écran CIBLE-0384-g.txt (la portion de contrôle) alors que je
  connaissais déjà l'alignement d'apprentissage. Rien n'a été décodé ni inféré. La clé est une fonction déterministe
  (scripts/common.py `build_key`) des fichiers TRAIN, hachés dans la même commande AVANT l'affichage ; la méthode n'utilise pas la cible.
- Comparaison faite sur l'apprentissage seul : la clé d'apprentissage 1715 s'accorde avec KEY-W1717d sur 47 des 50 nombres communs
  (désaccords : 77 s/ss, 97 la/m, 187 « roi de Suède » / « le roi de Suède ») → **1715 = même système que S1 de 1717** (homophones
  à 1–2 chiffres + nomenclateur à 3 chiffres : 150 le roi, 164 prince Eugène, 168 l'Empereur, 187 roi de Suède, 306 Vienne, 881 est…).

## 1. Portion de contrôle (désignée avant la transcription de la cible : consigne du sous-agent B)
**Scan 0384, page gauche (f. 310v), toutes les lignes chiffrées : 307 groupes**, lus tels que relevés (CIBLE-0384-g.txt, sha256
723e30a70af84ee19e6fd3d1db00610176b23b684f0ae865249e173c8675f2c3). Convention : `N/M?` → N ; `N?` → N ; `~N~` ignoré ; `N>M` → M ;
mots clairs = coupures du flot.

## 2. Méthode d'apprentissage (0388–0390 seulement)
Paires nombre=valeur tirées des lignes A des TRAIN (alignement sur les gloses d'époque), en excluant tout nombre ou valeur marqué « ? »
ou à lecture alternative ; **vote majoritaire** par nombre (égalité → ordre alphabétique). Résultat : 57 nombres, 934 paires, aucune
contradiction. → **K1715** (scripts/build_key.py écrit KEY-1715.tsv, haché KEY-1715.sha256 avant la mesure). Aucune aide des clés 1717
dans la clé décisive. Variante K1715+d (K1715 complétée par KEY-W1717d pour les nombres absents) : rapportée à l'étalonnage, NON décisive.

## 3. Critère et seuil (étalonnés AVANT, sur l'apprentissage seulement)
S = part des groupes de la portion couverts par un mot du lexique de ≥ 5 lettres ou s'étendant sur ≥ 2 groupes (segmentation par
programmation dynamique ; scripts/common.py `S`, repris de guyane-1779/AVENANT-C09). Lexique = lexique français cyphersolver
(normalisé j→i, v→u, y→i, sans accents) + mots des gloses et du clair de 0388–0390. Groupes sans valeur comptés au dénominateur.
**Témoins** : 200 clés permutées (valeurs de K1715 redistribuées) + 200 clés mélangées (redistribution à l'intérieur des classes de
longueur de valeur), graine 20261111.
**Étalonnage** (scripts/calibrate.py → CALIBRATION.txt) : validation croisée « un scan retenu » (clé apprise sur deux scans, S mesuré
sur des fenêtres de 150 groupes du troisième), 11 fenêtres : S(K) min 0,867, médiane 0,933 ; la clé bat ses 200 témoins dans 11/11
fenêtres ; max des témoins médian 0,767.
**Seuil θ = 0,77** = min hors échantillon (0,867) − 0,10 de marge pour les fautes de relevé d'un autre lecteur et un autre chiffreur.

**Règle (unique, décisive)** : la mesure PASSE si et seulement si (1) S(K1715) > max des 400 témoins (rang 1/401, p < 0,0025) ET
(2) S(K1715) ≥ 0,77. Sinon ÉCHEC : pas de lecture. **Une seule exécution** (scripts/measure.py refuse si MESURE-1715.json existe).

## 4. Après la mesure
Si elle passe : lecture de toute la lettre (0380–0387) avec K1715, complétée explicitement par les valeurs S1/1717 (KEY-W1717d) et le
contexte pour les nombres absents, chaque mot classé sûr / probable {x} / restitué [x] / irrésolu ‹…› ; taux = (sûrs + probables) /
total, règle de Daniel (≥ 95 % pour une publication complète). Une restitution ne compte jamais comme sûre. Pas de PR, pas de mail,
pas de publication : seulement l'avis « publication envisageable ou non ».
