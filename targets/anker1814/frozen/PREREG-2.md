# PREREG-2 — anker-christian-frederik-1811-1814 (RA-EA-5938), écrit le 09/11/2026 vers 02:40 (agent Opus 5.5) AVANT toute construction de la clé 2 et toute transcription de H2

## 0. Déclaration de l'échec de la mesure 1
La mesure 1 (PREREG.md, SHA 39b3abf6…) a donné **ÉCHEC** : car = 0,025 ; témoins max 0,018 ; marge 0,006 (`MESURE.txt`).
La clé KN-06 (fiche au crayon) est une reconstruction partielle, à valeur unique par lettre. H1 (1811 p. 10, colonne droite,
l. 1-8) est grillée comme partie de validation ; elle devient ici une donnée d'APPRENTISSAGE (le PREREG 1 l'interdisait
seulement pour une seconde mesure de KN-06). Ce PREREG-2 ne revient pas sur ce verdict.

## 1. État de connaissance au moment de l'écriture (honnêteté)
- Déjà lus avant ce PREREG : l'édition imprimée n° 32 en entier (session précédente et moi) ; 1811 p. 9 l. 1-3 à 450 dpi
  (gloses d'époque « Alquier kan have ret men kun tildeels / om det havde været eller blevet farligt for / Danmark at … ») ;
  1811 p. 11 moitié haute à 300 dpi (clair d'époque, début de la lettre) ; 1811 p. 10 entière à 150 dpi (vue d'ensemble, signes
  non lus) ; 1814 p. 59 entière à 150 dpi ; SK p. 39-40 (clé de Bergen) à 150 dpi.
- Constat (descriptif) tiré de ces lignes : le chiffre de 1811 est une substitution **homophonique** (ex. a = `+` ou `7` ;
  e = `ꝗ` ou `Z` ; o = `⊙` ou `⊍`), ce qui explique en partie l'échec de KN-06 (une valeur par lettre).
- Le clair imprimé n° 32 est un texte abrégé par l'éditeur (la colonne droite de p. 10 contient « magasiner », « distrikter »…
  absents de l'imprimé) ; le clair d'époque p. 11-13 est complet.

## 2. Apprentissage (clé K2) — partie autorisée
Paires d'époque de la lettre du 31/12/1811 SEULEMENT :
- chiffre 1811 p. 9 (toutes lignes, de haut en bas, autant que nécessaire), avec ses gloses interlinéaires ;
- chiffre 1811 p. 10 colonne DROITE (H1, transcription `H-CHIFFRE.txt` déjà gelée, étiquettes de `SIGNES.md`) ;
- clair d'époque 1811 p. 11-13 et imprimé n° 32, **sauf** le passage qui correspond à H2 (ci-dessous).
Méthode : alignement mot à mot (séparations du manuscrit) entre chiffre étiqueté et clair ; un signe reçoit une valeur
s'il est aligné au moins 2 fois sur la même lettre sans contre-exemple, ou 1 fois si la forme est distincte et la lecture
du mot sûre. Homophones admis ; valeurs multi-lettres (aa, logogrammes) admises. Étiquettes et formes dans `SIGNES-2.md`,
valeurs dans `KEY-2.tsv`. **Gel** : `KEY-2.tsv` + `SIGNES-2.md` hachés (`KEY-2.sha256`) AVANT toute transcription de H2.
Aucune valeur ajoutée ni corrigée ensuite avant la mesure. Signe sans valeur → « ? ».
Je fixe aussi d'avance, dans le même gel, `BERGEN-FORMES.tsv` : liste des formes de l'alphabet SK p. 39-40 (Bergen
22/3/1814), lettres a-z/A-Z et chiffres, avec leur valeur (pour le critère d'applicabilité, § 5).

## 3. Partie tenue à l'écart H2 — EXCLUE STRICTEMENT de l'apprentissage
**H2 = 1811 PDF p. 10, colonne GAUCHE, entière** (jamais utilisée en apprentissage, ni chiffre ni clair correspondant).
**Échantillon mesuré = lignes chiffrées 1 à 10 de la colonne gauche** (comptées du haut, ligne d'en-tête « 1 X. … » = l. 1).
Les lignes 11 et suivantes restent hors apprentissage et hors mesure.
- Transcription signe à signe sur recadrages ≥ 400 dpi avec les étiquettes de `SIGNES-2.md` (forme seulement ; toute forme
  absente → nouvelle étiquette `N1`, `N2`… décrite) ; `|` séparation visible ; ponctuation ; `[?]` illisible. Signes suscrits
  ou interlinéaires (corrections d'époque) ignorés, notés en commentaire.
- **Gel** : `H2-CHIFFRE.txt` + `H2-CHIFFRE.sha256` (avec le SHA du script de mesure) AVANT toute lecture du clair d'époque
  correspondant et avant tout décodage par script.
- Limite connue : l'imprimé n° 32 est déjà lu ; un biais de lecture des formes vers le texte attendu reste possible
  (étiquettes de forme, pas de lettres, pour le limiter). Je le signalerai.

## 4. Mesure (UNE seule)
- Référence R : transcription littérale du clair d'époque 1811 p. 11-13 pour TOUT le texte non utilisé en apprentissage
  (passage situé entre la fin du texte aligné sur p. 9 et le début du texte aligné sur p. 10 col. droite, ou ailleurs s'il le
  faut), faite APRÈS le gel de H2, gelée (`R-CLAIR.txt` + SHA dans `MESURE-2.txt`) AVANT l'exécution du script.
- Route A : car = (lettres égales dans la meilleure correspondance locale Smith-Waterman, +1/−1/−1, entre décodage de
  H2 et R, normalisés : minuscules, å/aa → aa, æ/ø gardés, j→i, w→v, « ? » = joker non concordant) / (nombre de positions
  décodées de H2, « ? » compris). Dénominateur sans ambiguïté : toutes les positions.
- 200 témoins : permutations aléatoires des valeurs de K2 entre les étiquettes de K2 présentes dans H2 (graine 1814) ;
  même calcul ; marge = car − max(témoins).
- Seuils habituels : **car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.**
  Accord en mots et car/lettres connues rapportés, non décisifs. Pas de seconde mesure.

## 5. Critère d'applicabilité à 1814 p. 59 (fixé ici, appliqué seulement si VALIDÉ ou PARTIEL)
Transcription de tous les passages chiffrés de 1814 p. 59 avec les étiquettes de `SIGNES-2.md` (formes nouvelles → `N…`),
gelée (`P59-CHIFFRE.txt` + `.sha256`) AVANT tout décodage. Puis :
- C1811 = part des signes chiffrés (occurrences) dont l'étiquette a une valeur dans K2.
- CBergen = part des occurrences dont la forme figure dans `BERGEN-FORMES.tsv` (jugement de forme fait pendant la
  transcription, colonne dédiée, avant décodage).
- L = part des mots décodés (≥ 3 lettres, sans « ? ») présents dans un lexique bâti par script sur les lettres 1801-1817 de
  l'édition C. J. Anker (danois et français), mêmes normalisations ; les mots du n° 32 et de la lettre éventuellement
  identique à p. 59 n'y sont pas exclus (l'édition ne contient pas p. 59, cf. RESULTAT.md).
- **p. 59 suit l'alphabet de 1811 si C1811 ≥ 0,80 ET C1811 − CBergen ≥ 0,20 ET L ≥ 0,50.**
  p. 59 suit l'alphabet de Bergen si CBergen ≥ 0,80 ET CBergen − C1811 ≥ 0,20 (alors décodage par BERGEN-FORMES, même test L).
  Sinon : indéterminé → aucune lecture.

## 6. Lecture (si applicable)
Lecture au compte de Daniel : sûrs / probables {x} / restitués [x] / irrésolus ‹…› ; seuil 95 % (sûrs+probables, sans
restitués) pour « lu ». Texte en danois de 1814 (orthographe du manuscrit), résumé FR et EN. Puis PR-PREP.md (statut exact,
crédits Riksarkivet/Arkivverket et C. J. Anker ; images seulement si la licence le permet explicitement). Aucune PR, aucun envoi.
