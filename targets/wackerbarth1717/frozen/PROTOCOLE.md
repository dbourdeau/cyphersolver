# PROTOCOLE — wackerbarth-flemming-1717 (HStA Dresden, 10026 Geheimes Kabinett, Loc. 00713/01)
Écrit le 11/11/2026 (agent Opus 5.5, fil 🔓 Déchiffrement), AVANT la construction de la clé, AVANT la transcription
des portions de test, AVANT tout décodage hors des paires glosées. Figé par SHA-256 (`PROTOCOLE.sha256`).
🔴 Images InC : recherche privée seulement ; aucune image ni dérivé publié. [one storage location removed for publication]
🔴 A.-S. Rous (SBG Sachsen) travaille sur ce corpus : toute lecture est une découverte simultanée, à nommer.

## 0. Ce que j'ai vu au moment d'écrire
- Vignettes basse résolution (1000–1400 px) de 0040, 0057, 0058, 0089 : 0040 = fin du chiffre du 24/04 (f. 31v–32 ;
  une parenthèse ouvrante « ( » au milieu de la p. de droite, peut-être le début du passage déchiffré sur la feuille) ;
  0089 = début de la Relation XXII (« Sire », chiffre mêlé de clair : « selon toute apparence la Cour Imperiale … »).
  Aucun nombre de 0037–0040 ni de 0089–0099 n'a été lu ou noté.
- **Feuille 0042–0043 : NON vue** (une vignette a été générée par erreur de lot, elle n'a pas été ouverte). Seul
  connu : l'extrait de l'inventaire (« …vues du Roy de Suède sur la Pologne… descente du côté de Danzig… Comte de Hanau »,
  fin « Voila ce que pour le present… »).
- Paires (apprentissage) déjà regardées : 0058 (p. de droite, l. 6–14) et 0057 (p. de gauche, bas). Constats : gloses
  d'époque en phrases continues qui ne suivent pas les coupures de lignes du chiffre ; substitution surtout lettre à
  lettre, homophone (ex. « lors avoit » = 44.33.29.57.50.5.33.9.28 ; o = 33, i = 9, t = 28/52, e = 2/10) ; nombres à
  3 chiffres = nomenclateur ou polygrammes (177 = le Czar ; 102 peut-être « ss » ; 120 ?) ; mots clairs intercalés
  dans le chiffre (« et 177. par rapport ») ; nombres biffés et corrigés en exposant (« 78 » sur 74).
- Clés de comparaison : K0 (Dresde 0080, alphabet a 20–22 … consécutif), KEY1 (même famille, décalée −5), clé
  Wackerbarth 1703 (homophone 2 chiffres a 65/67/90 …). Aucune n'est utilisée pour remplir la clé (comparaison seule).

## 1. Segments
- **TRAIN** = les 24 scans glosés : 0017, 0057–0062, 0071–0072, 0075–0078, 0080–0081, 0086–0088, 0234, 0253–0254,
  0275, 0285, 0296. Paires = groupes chiffrés ↔ glose d'époque. Seul matériau de la clé.
- **TEST-A (vérité terrain)** = tout le chiffre de la lettre du 24/04/1717 (fichiers 0037–0040, ordre de lecture),
  transcrit par un sous-agent Opus dans `releves/A-CHIFFRE-0037-0040.txt` ; référence = feuille de déchiffrement
  d'époque 0042–0043 transcrite par le même sous-agent dans `releves/A-FEUILLE-0042-0043.txt`. Les deux fichiers sont
  hachés (`releves/A.sha256`) dès leur écriture ; **je n'ouvre pas la feuille avant la mesure** (le sous-agent ne
  doit pas en citer le contenu dans son rapport).
- **TEST-B (mesure linguistique)** = **P = les 360 premiers groupes chiffrés de la Relation XXII** (copie au Roi,
  Vienne 14–16/06/1717), à partir du premier nombre de 0089, dans l'ordre de lecture (page de gauche puis de droite,
  ligne à ligne), en sautant les mots clairs intercalés et les nombres biffés (un nombre corrigé compte pour sa valeur
  corrigée). Transcrit par un sous-agent Opus dans `releves/B-REL22.txt` (il peut transcrire au-delà de 360 ; seuls
  les 360 premiers comptent), haché (`releves/B.sha256`) avant tout décodage. P ne sert jamais à la clé.

## 2. Clé
- `KEY-W1717.tsv` (nombre, valeur, nb d'occurrences alignées, sûreté sûr/probable/inféré), construite **sur TRAIN seul** :
  alignement manuel ou assisté des groupes sur les gloses ; valeur = valeur majoritaire de l'alignement (égalité →
  la plus fréquente dans l'ensemble des paires, sinon première vue). Valeur = lettre, polygramme ou mot/nom.
- Inférence structurelle (ex. place d'un homophone dans une table régulière) permise seulement si elle est écrite et
  marquée « inféré » dans la clé AVANT le gel. Aucun apport de K0 / KEY1 / clé 1703.
- Nombre absent de la clé → « # » (non décodé). Gelée par SHA-256 (`KEY-W1717.sha256`) AVANT la mesure.

## 3. Normalisation (A et B)
Minuscules ; accents retirés ; j→i ; v→u ; non-lettres retirées ; valeurs de nomenclateur développées en toutes lettres
(crochets retirés) ; « # » conservé comme caractère non-lettre compté dans la longueur décodée.

## 4. Mesure unique (`scripts/mesure.py`, une seule exécution, sortie `MESURE.json`)
- **A** : D = décodage de TEST-A ; F = texte de la feuille sans le titre et sans ce qui suit « Voila ce que pour le
  present » (clair de la lettre recopié). **carA = Σ des blocs communs de taille ≥ 3 (difflib.SequenceMatcher(None, F, D,
  autojunk=False).get_matching_blocks()) / |F|.** Accord en mots rapporté, non décisif.
- **B** : D = décodage de P. **scoreB = part des caractères de D couverts par une segmentation en mots du lexique**
  (programmation dynamique, maximum de lettres couvertes, mots de longueur ≥ 2) / |D| (les « # » comptent au
  dénominateur). Lexique = `lexique-fr-cyphersolver.json` (PISTES-AUTO/fable-api/lots/lot2/_communs/, sha256
  cdf81c86…ce2ea) ∪ mots des gloses de TRAIN (fichier `LEXIQUE-AJOUT-TRAIN.txt`, gelé avec la clé).
- **Témoins** : 200 permutations aléatoires des valeurs de la clé entre ses nombres (graine 1717), mêmes calculs.
  marge = score − max(témoins).
- **Seuils (point 9 + avenant 10)** : score ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.
  A valide la clé sur le système W→F (vérité terrain) ; B décide si la Relation XXII (adressée au Roi, peut-être une
  autre table) peut être lue avec cette clé. Les deux résultats sont rapportés tels quels.
- Après la mesure, TEST-A et P sont grillés : aucune nouvelle mesure sur eux.

## 5. Après la mesure
- Si B VALIDÉ : lecture par le sens de la Relation XXII (et du 24/04 si A VALIDÉ), règle de Daniel : sûrs / probables {x} /
  restitués [x] / irrésolus ‹…›, une fiche par lettre (`LECTURE-*.md`), restitution jamais contraire aux lettres sûres,
  orthographe du chiffre gardée. Publication seulement si ≥ 95 % lus par le sens ET accord de Brice — pas dans cette séance.
- Si ÉCHEC : `ESSAI-OPUS.md` (méthodes, scores, cause).
- Écarts au protocole : notés dans HANDOFF.md, jamais corrigés en silence.
