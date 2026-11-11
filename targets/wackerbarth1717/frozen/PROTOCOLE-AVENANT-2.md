# Avenant 2 au PROTOCOLE (11/11/2026, agent Opus 5.5, fil 🔓) — mesure calibrée, UNE seule exécution
Écrit APRÈS les relevés des scans glosés manquants (§1) et la transcription (non décodée) de 0091–0093, AVANT la construction
de KEY-W1717b / KEY-W1717c, AVANT tout étalonnage, AVANT tout décodage de 0091–0093. Figé par SHA-256
(`PROTOCOLE-AVENANT-2.sha256`). Le PROTOCOLE et l'Avenant 1 restent valables sauf ce qui est remplacé ici.
🔴 Images InC (recherche privée). 🔴 A.-S. Rous (Tartu) travaille sur ce corpus : toute lecture = découverte simultanée, à nommer.

## 0. Ce que je sais au moment d'écrire (déclaration)
- J'ai lu KEY-W1717, MESURE.json (décodages A et B grillés) et les relevés TRAIN, dont le 28/05 (0057–0061) et ses gloses.
  La lettre choisie comme vérité terrain (§2) est donc CONNUE de moi : c'est pourquoi KEY-W1717b est construite par une
  procédure MÉCANIQUE écrite ici (aucune décision manuelle nouvelle), et toute entrée manuelle reprise de KEY-W1717 doit avoir
  un appui hors de la lettre de vérité (liste fermée §3).
- Relevés nouveaux (avenant 2 §1) : T-0075…T-0078 (sous-agent Opus, `T-ENCLOS-A.sha256`), T-0080, T-0253, S2-0296 (moi,
  `AVENANT2-RELEVES.sha256`). R22-0091…0093 transcrits par un sous-agent Opus (`R22.sha256`), non ouverts par moi à part
  l'en-tête et les 15 premières lignes de 0091 (contrôle de format) ; aucun décodage.

## 1. Classement des scans glosés manquants
| scan | date | système | raison |
|---|---|---|---|
| 0075–0078 | 12/06/1717, enclos A allemand | **S1** | nomenclateur commun (177, 103, 110, 168, 700, 1000) ; « procedures » sur 23.60.16 (p r o en S1) ; « officiers » sur 22.63.46.64.39.2.60.51 (o…i.i.e.r.s en S1). Gloses ALLEMANDES lâches (traductions mot à mot, ancrage approximatif : « bologna » sur 17.2.27, « Czar » sur 59 en 0076 L10) → non littérales |
| 0080 | 12/06/1717, Relat. XXI C | **S1** | « deloger les russes de l'Empire » = 53.2.12.16.7.10.27.103.29.60.6.77.2.51.120.10.275 (cohérent S1) |
| 0253 | 20/11/1717 | S2 (K0) supposé | un seul nombre (148 = « le C. Schlick »), date de nov. |
| 0296 | 29/12/1717 | **S2 (K0)** | « perd de plus en plus » = 62.33.70.30.3.63… incompatible avec S1 |
→ TRAIN S1 = 0017, 0057–0062, 0071–0072, 0075–0078, 0080–0081, 0086–0088.

## 2. Test A' — vérité terrain (critère principal)
- **Lettre de vérité V = Vienne 28/05/1717 W→F, scans 0057–0061** (relevés T-0057…T-0061, déjà hachés implicitement par
  leur état actuel : sha256 consignés dans `AVENANT2-VERITE.sha256` au moment du gel). Seule lettre glosée S1 ayant
  ≥ 300 groupes sous glose (≈ 440 groupes sur des lignes glosées).
- Unités : pour chaque passage (« ## ») de V ayant au moins une glose : G = concaténation normalisée (PROTOCOLE §3) des
  gloses du passage ; D = décodage par KEY-W1717b des nombres non biffés du passage (mots clairs {…} EXCLUS). Une ligne
  G placée au-dessus d'une ligne C entièrement biffée est exclue de G.
- **exactA = mots de G retrouvés exactement / mots de G**. Mots de G = découpage de la glose sur espaces et ponctuation
  (y compris apostrophe), normalisés, longueur ≥ 1. Un mot est « retrouvé exactement » si TOUS ses caractères sont couverts
  par des blocs communs de taille ≥ 3 de difflib.SequenceMatcher(None, G, D, autojunk=False) du passage. Agrégation sur
  tous les passages (somme des mots).
- Rapporté aussi (non décisif) : part des caractères de G couverts (blocs ≥ 3), nombre de groupes de V.
- Témoins : 200 permutations des valeurs de KEY-W1717b entre ses nombres (graine 1717). marge = exactA − max(témoins).
- **Seuils fixés d'avance : exactA ≥ 0,60 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.**
  (0,60 et non 0,85 : clé b privée de la plus grosse lettre glosée et gloses abrégées « S. M. », « Mr. », « Angl. » que le
  chiffre épelle autrement ; fixé sans avoir rien calculé.)

## 3. Clés
- **KEY-W1717b** = `scripts/align.py` (inchangé, 8 itérations) sur TRAIN S1 MOINS V (0057–0061) et MOINS l'enclos A
  (gloses allemandes non littérales, §1) ; règle de `build_key.py` pour les nombres à 1–2 chiffres (majorité ; ≥ 3 votes
  et ≥ 60 % → sûr, sinon probable) ; nombres ≥ 3 chiffres : seulement les entrées manuelles de la liste fermée suivante,
  toutes appuyées hors de V : 77 ss (0071, 0072, 0081, 0087) ; 99 ss (0081) ; 103 les (0088) ; 110 la (0081, 0086) ;
  119 tt (0087) ; 150 [le roy] (0062) ; 154 [votre excellence] (0088) ; 177 [le czar] ; 190 la (0071) ; 193 le (0086) ;
  275 [l'empire] (0071, 0081, 0080) ; 355 [premier] (0017) ; 700 et (0086) ; 100 d, 120 d (≥ 6 cas hors V à vérifier par
  l'aligneur : si l'aligneur ne les vote pas hors V, ils sont omis) ; 377 [ministre] et 168 [l'empereur] (enclos A, gloses
  « ministre » ×4 et « der Käyser » ×2, valeur traduite, marquée inféré) ; nulles 5024, 5043, 5046. Les valeurs manuelles
  de KEY-W1717 appuyées seulement sur V (13, 18, 78, 97, 102, 130, 170, 217, 252, 292) NE sont PAS reprises : 13, 18, 78
  prennent la valeur de l'aligneur hors V s'il en donne une, sinon absents.
- **KEY-W1717c** (pour la lecture et pour B') = même procédure sur TRAIN S1 complet (V compris, enclos A exclu) + toutes les
  entrées manuelles de KEY-W1717 + 377 [ministre] + 168 [l'empereur].
- b et c gelées par SHA-256 (`KEY-W1717bc.sha256`) avant l'étalonnage et avant la mesure. Script `scripts/build_key_bc.py`.

## 4. Critère linguistique L, étalonné sur l'APPRENTISSAGE seulement
- Modèle : 4-grammes de caractères (a–z normalisé PROTOCOLE §3, espace retiré), lissage add-k (k = 0,1) avec repli
  interpolé 4/3/2/1 (poids 0,5/0,3/0,15/0,05), entraîné sur `corpus-fr-henri4-extrait-1.9Mo.txt` +
  `corpus-fr-gutenberg-extrait-1.9Mo.txt` (PISTES-AUTO/fable-api/lots/lot2/_communs/) — français XVIᵉ–XVIIIᵉ, aucun texte
  de ce volume. Candidats :
  L1 = log-vraisemblance moyenne par caractère du décodage (les « # » coupent le contexte et ne sont pas comptés) ;
  L2 = couverture lexicale avec mots ≥ 4 lettres seulement (lexique cyphersolver ∪ LEXIQUE-AJOUT-TRAIN, segmentation DP
  de mesure.py) ;
  L3 = L1 calculé seulement sur les fenêtres sans « # ».
- Étalonnage : ensemble E = tous les nombres non biffés des relevés TRAIN S1 français HORS V (0017, 0062, 0071, 0072,
  0080, 0081, 0086–0088), décodés par KEY-W1717b, contre 200 permutations de b (graine 1717). Pour chaque candidat :
  z_E = (score − moyenne témoins)/écart-type témoins ; gap_E = score − max témoins. **Critère retenu = le candidat de plus
  grand z_E parmi ceux qui ont gap_E > 0 ; il doit avoir z_E ≥ 4**, sinon aucun critère n'est jugé discriminant et B'
  n'est pas mesurée (ÉCHEC d'instrument noté). Sortie `ETALONNAGE.json`, écrite et hachée avant la mesure.
- Portion NEUVE N = tous les nombres du relevé R22-0091.txt (scan 0091, f. 72v–73, ordre de lecture page g puis page d),
  non biffés, corrections prises à leur valeur corrigée, première lecture des « N/M? » ; 353 groupes annoncés (≥ 300). Hors
  des 360 groupes grillés (0089–0090). Décodée par KEY-W1717c.
- **Test B'** : score L*(c, N) contre 200 permutations de c (graine 1717) : z_N, gap_N. **VALIDÉ si z_N ≥ max(4 ; 0,5 × z_E)
  ET gap_N ≥ 0,5 × gap_E ET score ≥ (score_E + moyenne témoins_E)/2** (au moins à mi-chemin du français étalonné) ;
  **PARTIEL** si seule la première condition tient ; sinon ÉCHEC.

## 5. Mesure unique et suites
- `scripts/mesure2.py` exécuté UNE fois → `MESURE2.json` (A' et B'). Aucune nouvelle mesure sur V ni sur N ensuite.
- A' VALIDÉ ou PARTIEL + B' VALIDÉ → lecture par le sens (règle de Daniel : sûrs / probables {x} / restitués [x] /
  irrésolus ‹…›, seuil 95 % sûrs+probables), clé c, Relation XXII d'abord (0089–0099 dans la mesure des relevés
  disponibles), puis autres lettres S1 non glosées ; une fiche `LECTURE-*.md` par lettre + `RESUME-HISTORIQUE.md`.
  La lecture peut corriger des valeurs de c (corrections notées, jamais rétroactives sur la mesure).
  S2/K0 (nov.–déc.) : lecture possible avec K0 si le temps le permet, hors mesure (K0 déjà établie ailleurs).
- A' ÉCHEC ou B' non VALIDÉ → pas de fiche LECTURE ; compléter ESSAI-OPUS.md.
- Rien n'est publié ; pas de PR, pas de mail. Écarts → HANDOFF.md (ajout seulement).
