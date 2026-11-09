# PREREG — thumbshirn-1647 (LATh – StA Altenburg, Schönbergische Sammlung Nr. 85, ThULB IIIF stat_derivate_00025112)
Écrit le 09/11/2026 (agent Opus 5.5, fil Déchiffrement), AVANT tout décodage, avant toute transcription des lettres
chiffrées et avant d'avoir ouvert la moindre fiche de déchiffrement d'époque (0549, 0559, 0571, 0581, 0599, 0605).

## Ce que j'ai vu au moment d'écrire
- Vue 0003 (clé), pleine résolution : transcrite dans `KEY0-0003.tsv` (SHA-256 dans `KEY0-0003.sha256` :
  753ecce795343a239081af2824bae7822cd53b21e974af0c708c2df80a1d9880). 24 lettres → 24 nombres distincts (1 à 52),
  substitution simple sans homophone ; note : chiffres écrits « continuirlich serie », sans coupure de mots.
- REPERAGE.md (fil 🔎) : il cite « propter = 23.28.21.34.20.39 » (0549), la suite de 0583
  « 5.21.15.7.6.34.22.32.11.10.25.36.31 », et des bribes de clair des fiches 0549 (13/11), 0599 (22/12) et 0605 (25/12).
  Rien du contenu de la fiche 0571 (24/12) : seulement « renvois (a)–(i) en latin ».
- Constat déjà possible sans décoder : 21, 23, 28, 34, 20, 39, 11, 25, 36, 31 n'existent pas dans K0. La clé de 0003
  ne couvre donc vraisemblablement pas tout le chiffre de 1647 (autre alphabet, ou homophones ajoutés).
- Notice ThULB du Nr. 85 : correspondance de Thumbshirn et Carpzov avec J. F. von Brand et le duc ; licence CC BY 3.0.

## Paires
- **Apprentissage A** (chiffre et fiches lus librement) : 13/11 (0547, 0548, 0551 ↔ 0549) ; 17/11 (0557 ↔ 0559) ;
  22/12 (0597 ↔ 0599) ; 25/12 (0604, 0607 ↔ 0605).
- **Tenue à l'écart H = la lettre du 24/12/1647** : chiffre 0569, 0573, 0574 ↔ fiche 0571. Choisie parce que c'est la
  plus longue et la seule dont je n'ai lu aucun clair (le 25/12 proposé dans la consigne est déjà en partie cité
  dans REPERAGE.md, donc grillé).
- Ordre : (1) transcription des nombres de H (0569, 0573, 0574 ; 0570 = page en clair, vue seulement pour la suite
  du texte), découpée en passages H(a)…H(i) d'après les renvois rouges, gelée dans `H-CHIFFRE.txt` + SHA-256 ;
  (2) apprentissage sur A ; (3) clé mesurée gelée ; (4) seulement alors, ouverture de 0571, transcription des gloses
  dans `H-GLOSES.txt` + SHA-256 ; (5) mesure.

## Clé mesurée K (une seule)
- Base : K0 = `KEY0-0003.tsv` (SHA ci-dessus).
- Apprentissage : chaque passage chiffré de A est aligné à la main, nombre par nombre, sur le clair de la fiche
  d'époque (orthographe de la fiche) dans `BUILD-PAIRES.tsv` ; segment = lettre (ou vide si nul / non aligné).
- K = pour chaque nombre vu dans A : la valeur majoritaire dans A (égalité → valeur de K0 si elle est parmi les
  ex aequo, sinon la première vue) ; pour un nombre absent de A : sa valeur K0. Aucun apport extérieur.
- K gelée dans `KEY.tsv` + `KEY.sha256` AVANT l'ouverture de 0571.

## Mesure (une seule)
`scripts/measure.py`, après les trois gels :
- normalisation : minuscules, accents retirés, j→i, v→u (w gardé), non-lettres retirées ;
- pour chaque passage glosé H(x) : décodage par K (nombre absent de K = « ? ») ; correspondances = somme des blocs
  `difflib.SequenceMatcher(None, décodage, glose, autojunk=False).get_matching_blocks()` ;
- **car = Σ correspondances / Σ lettres de glose** ; couverture = part des nombres de H ayant une valeur dans K ;
- **200 témoins** : permutations des valeurs de K entre les nombres de K (graine 1647) ; marge = car − max(témoins) ;
- **Seuils habituels (fixés ici) : car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.**
- Accord en mots rapporté, non décisif. À titre descriptif seulement (non décisif) : le même calcul avec K0 seule.
- Limite déclarée d'avance : si les gloses de H font moins de 60 lettres, je le dis ; un passage H(x) sans glose
  correspondante est exclu ; une glose sans chiffre en face est exclue. Le 24/12 mesuré est ensuite grillé.

## Ensuite
- VALIDÉ ou PARTIEL : lire 0583 (avec la bandelette 0581, déchiffrement d'époque d'un passage ⇒ EXISTING pour ce
  passage) et 0837 (P.S. fol. 399, sans déchiffrement repéré) au compte de Daniel (sûrs / probables {x} /
  restitués [x] / irrésolus ‹…›), résumé FR + EN.
- ÉCHEC : pas de lecture présentée comme validée ; noter ce qui manque.
- PR-PREP.md : statut exact, crédits LATh / ThULB ; images seulement si CC BY 3.0 confirmée sur la notice du Nr. 85.
