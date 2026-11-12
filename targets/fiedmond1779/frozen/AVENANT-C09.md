# Avenant C09 (bilan Fable du 11/11/2026) — mesure unique de K-Guy1780c sur la portion de contrôle

Écrit le 2026-11-11 à 21 h 20 CET (session C11 du dossier), AVANT toute lecture de la portion de contrôle par une clé. Haché avec la clé, les scripts et l'étalonnage dans SHA256-AVENANT-C09.txt avant le lancement de la mesure.

Nom : le bilan des runs Fable du 11/11 [emplacement expurgé] appelle cette étape « avenant (C09) ». Le dossier a déjà un PROTOCOL-C09 (29/10, cryptanalysis/c09/, mesure sur paraphrase, NULLE). Celui-ci ne le remplace pas et n'y touche pas. Fichiers de travail : cryptanalysis/c11-avenant-c09/.

## 1. Clé gelée : K-Guy1780c

- Fichier : cryptanalysis/c11-avenant-c09/K-Guy1780c.tsv, copie à l'octet de fable-lot4-2026-11-11/KEY-PROPOSAL.tsv (sortie du run Fable « guyane1779-fiedmond-f09-f16 », 20261111-131902).
- **SHA-256 ae615f456bdca66965de8e07cf206d64628e93c60c9d94537185c2640dedd57c**, le même que dans fable-lot4-2026-11-11/SHA256-GEL.txt (gel du 11/11, 14 h 07).
- 454 lignes. Toute valeur non vide est employée, sauf le statut « irresolu » (338). Cela compte « sur », « prob », « corrige-paire », « corrige-contexte » et « restitue(-fort/-faible) ». On ne garde que la valeur principale, sans variantes, et sans la règle de bigramme 182.633 que propose l'en-tête. Les hypothèses à une occurrence (HYPOTHESES-1occ.tsv) restent hors clé.
- **Aucune modification de la clé n'est possible** : elle a été produite et gelée avant cet avenant.

## 2. Portion de contrôle

- Elle est fixée par PROTOCOL.md §3 (28/10/2026), précisée en C08/C09 et dans cryptanalysis/c02/ctx.py :
  - **f9 v014g l11–l18** : le P.-S., 8 lignes, 64 groupes ;
  - **f16 v025d l27–l31** : les 5 dernières lignes chiffrées, 54 groupes.
- Total : **118 groupes, 335 chiffres**.
- Transcription reprise telle quelle, gelée le 28/10 : transcription/f09.txt (SHA 4cd4a550…) et transcription/f16.txt (SHA 3b35bf27…), revérifiées ce soir.
- Convention fixée : pour un groupe noté `a?/b`, on lit `a` (lecture la plus probable, PROTOCOL.md §1). Un îlot `«…»` coupe le flot. Les deux morceaux sont mesurés ensemble.

**Contrôle d'intégrité, fait avant cet avenant** (grep des 13 suites de groupes du contrôle et de leurs identifiants de ligne) :
- Paquet envoyé à Fable : l'archive du dossier envoyé, décompressée [emplacement expurgé], 19 fichiers.
- Sorties du run : transcript.json, RAPPORT, LECTURE, read_f09/f16_K1780c, controle_K1780c.
- le dossier des runs Fable en entier [emplacement expurgé], et tout le dossier guyane-1779/.

Résultat :
- Les suites chiffrées ne figurent que dans transcription/f09.txt et f16.txt.
- Les copies d'envoi les remplacent par « # [BLOC RETIRÉ pour l'envoi] » (SHA vérifiés OK).
- Les lectures mécaniques s'arrêtent à v014g l10 et à v025d l26 : read_f09/f16_K1780b (C08) et read_f09/f16_K1780c (Fable).
- transcript.json ne cite que les identifiants de ligne, dans les consignes.

→ La portion n'a **jamais été décodée ni envoyée à Fable**.

**Incident déclaré (même nature que C08c)** : pendant ce contrôle, un `diff` entre f09.txt et sa copie d'envoi a **affiché les groupes chiffrés** des 13 lignes, vers 21 h 05.
- Ces groupes n'ont été ni décodés ni alignés, et rien n'en a été inféré.
- La clé était déjà gelée (14 h 07) et ne peut plus changer.
- Le critère ci-dessous n'utilise que l'apprentissage.

**Limite de taille déclarée** : l'avenant de Brice du 10/11 demande au moins 300 caractères chiffrés ou 150 groupes. La portion fait 335 chiffres mais seulement 118 groupes.
- Elle a été fixée le 28/10, avant cet avenant.
- C'est la seule portion de 1779 encore vierge.
- C'est elle que nomme l'action validée (« mesure unique sur la portion de contrôle intacte (f9 l11-18 et f16 l27-31) »).
- On la mesure donc, et la limite sera rappelée dans le résultat.

## 3. Critère et seuil (étalonnés AVANT, sur l'apprentissage seulement)

Il n'existe aucun clair d'époque de la portion. Le critère caractères ≥ 0,85 et témoins + 0,30 (consigne du 30/10) suppose une référence et ne peut donc pas s'appliquer. On prend la mesure prévue au protocole sous forme automatique et non circulaire : la **lecture lexicale stricte S**.

**Définition de S** (cryptanalysis/c11-avenant-c09/common.py, fonction `S`) :
- On décode avec la clé, on concatène les valeurs et on coupe le flot aux îlots en clair et aux groupes sans valeur.
- On segmente ce flot en mots du lexique, avec une couverture maximale (programmation dynamique, mots de 2 à 22 lettres).
- Le lexique réunit :
  - le lexique français de cyphersolver (SHA cdf81c86…), normalisé j→i, v→u, y→i, sans accents ;
  - les mots des clairs d'apprentissage : f102_clair, c1780_dechiffrement, c09 La Serre ×2.
- S est la part des **groupes** dont toutes les lettres tombent dans un mot qui s'étend sur au moins 2 groupes ou compte au moins 5 lettres.
- Les groupes sans valeur comptent au dénominateur.

**Témoins** : 200 + 200, graine 20261111.
- **200 clés permutées** : les valeurs de K-c redistribuées au hasard sur ses groupes.
- **200 clés mélangées** : la même redistribution, mais seulement à l'intérieur de chaque classe de longueur de valeur. Ces témoins gardent le nombre de lettres de chaque groupe et sont plus durs.

**Étalonnage**, sur les copies d'envoi f09/f16, qui ne contiennent physiquement pas la portion : cryptanalysis/c11-avenant-c09/calibrate_result.txt.
- 54 fenêtres d'au moins 118 groupes.
- K-Guy1780b, qui n'a jamais été ajustée sur f9/f16, sert de modèle d'une bonne clé appliquée à un texte neuf :
  - S de K-b : min 0,602, **q10 0,656**, médiane 0,718 ;
  - max des témoins : médiane 0,639 ;
  - K-b dépasse tous ses témoins dans 52 fenêtres sur 54.
- L'écart à +0,30 n'est jamais atteint (0/54 fenêtres, même à +0,15 : 1/54). Une marge fixe n'est donc pas tenable à cette taille, d'où le critère par rang.
- Puissance de la règle ci-dessous : avec K-b, 48 fenêtres sur 54 passent (≈ 89 %) ; avec K-c, en échantillon et donc optimiste, 53 sur 54.

**Règle de décision (unique, décisive)**. La mesure **PASSE** si et seulement si les deux conditions sont remplies :
1. **S(K-c) > le maximum des 400 témoins** (rang 1/401, p < 0,0025 sous l'hypothèse « clé fausse ») ;
2. **S(K-c) ≥ θ = 0,656** (q10 de K-b hors échantillon).

Sinon, elle **ÉCHOUE**, et le dossier est clos sur K-Guy1780c.

Rapportés mais non décisifs :
- le score de langue (5-grammes de caractères, log10 par lettre ; étalonnage calibrate2_result.txt, où K-b bat ses 400 témoins dans 38 fenêtres sur 54 seulement) ;
- S et LM de K-Guy1780b sur la même portion.

**Une seule exécution** (measure.py refuse de tourner si measure_result.txt existe) : pas de seconde chance, aucun réglage après coup, portion grillée ensuite.

## 4. Après la mesure

- **Si elle passe** : lecture de la portion et des deux lettres selon la règle de Daniel. On compte les mots sûrs, les probables {x}, les restitués [x] et les irrésolus ‹…›. Une restitution ne contredit jamais des lettres sûres ; un mot restitué ne compte jamais comme sûr. Publication envisageable seulement si sûrs + probables ≥ 95 % ; sinon, au mieux une lecture partielle expliquée, sur décision de Brice.
- **Si elle échoue** : dossier clos sur cette clé ; rien publié.
- **Dans les deux cas** : pas de PR, pas de mail, aucune image publiée sans décision de Brice.

## 5. Ce que la mesure prouve, et ce qu'elle ne prouve pas

- Si elle passe, K-c lit un texte neuf du même code nettement mieux que ses 400 témoins, à un niveau au moins égal à celui d'une bonne clé hors échantillon.
- Elle ne contrôle pas chaque valeur restituée : il n'y a pas de clair de référence.
