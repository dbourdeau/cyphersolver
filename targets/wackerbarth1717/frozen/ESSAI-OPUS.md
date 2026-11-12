# ESSAI-OPUS — wackerbarth-flemming-1717 (11/11/2026, agent Opus 5.5, fil 🔓)
🔴 Images InC, recherche privée : aucun extrait d'image publié. 🔴 A.-S. Rous travaille sur ce corpus (découverte simultanée à nommer).

## Verdicts officiels (PROTOCOLE §4 + Avenant 1 ; mesure unique, `MESURE.json` sha256 142e3209…cc67)
| Test | score | max 200 témoins | marge | verdict |
|---|---|---|---|---|
| A — chiffre 0040 vs feuille 0042–0043 (carA / \|F\|) | 0,2036 | 0,0855 | 0,118 | **ÉCHEC** |
| B — Rel. XXII, 360 groupes (couverture lexicale) | 0,9375 | 0,9231 | 0,014 | **ÉCHEC** |
Couverture de la clé : A 97,8 %, B 96,1 % des groupes. Verdicts maintenus tels quels ; A et P sont grillés.

## Méthodes
Clé S1 (`KEY-W1717.tsv`, 82 entrées, gelée sha256 f2b68ad6…207a) construite sur 13 relevés TRAIN (alignement DP
chiffre↔gloses `scripts/align.py` + décisions manuelles justifiées `scripts/build_key.py`). Mesure `scripts/mesure.py`
(sha256 9e692434…3159), exécutée une fois.

## Cause de l'échec : l'instrument, pas la clé (diagnostic POST-HOC, non décisif, `DIAGNOSTIC-POSTHOC.txt`)
- **A** : la feuille 0042–0043 déchiffre toute la fin de la lettre (1 812 lettres) alors que TEST-A a été réduit au seul
  chiffre de 0040 (414 groupes ≈ 424 lettres) par l'Avenant 1. carA / |F| est donc plafonné vers 0,23 : le seuil 0,85
  était inatteignable par construction (biais déclaré « défavorable » mais sous-estimé). Rapporté à |D| : **0,870**
  (max témoins 0,152) ; le décodage reproduit la fin de la feuille (« … pour parvenir à notre but, mais que nous nous
  fermerions … la porte de les obtenir … nous rendrions … plus dificile et plus incertaine y travaillant conjointement
  avec l'Empereur. Je vois encore jour de pouvoir reussir dans le projet à l'egard d'une echange … comté de Hanau … plein
  pouvoir … un projet en forme pour le traité qui est requis »). Le système S1 et la clé sont donc corrects en substance.
- **B** : lexique de 43 518 formes + mots de 2 lettres → une permutation couvre déjà 77 % (max 92 %) : mesure non
  discriminante sur 360 groupes. Même avec mots ≥ 4 lettres : 0,775 contre max 0,735 (moy. 0,497). Le décodage de P se lit
  pourtant à l'œil (« quoique iusqu'ici i'aye dit a votre maiesté … le comte de [Si]nzendorff chancelier … qu'il avoit
  ordre de me parler de la part de … qu'il me prioit de m'y trouver alors chez lui … luy avoit ordonné de me faire savoir
  comme quoi … du nord … avoit pris [la] resolution de venir au … »). Constat non mesuré, sans valeur de validation.

## Conséquence
Pas de fiche LECTURE (le protocole l'exige VALIDÉ) ; rien n'est publiable. Proposition pour une séance suivante
(nouvel avenant, à faire valider) : portion neuve de la Relation XXII (groupes 361–720, ou 0091–0099) + test vérité
terrain sur une autre lettre glosée en entier non utilisée en TRAIN ; mesure A normalisée par |D| ; mesure B par
n-grammes ou lexique ≥ 4 avec seuil sur la moyenne des témoins ; témoins par permutation inchangés.

## Avenant 2 (11/11/2026, 2ᵉ séance, agent Opus 5.5) — mesure unique 2 : A' ÉCHEC, B' VALIDÉ → pas de lecture
Fichiers : PROTOCOLE-AVENANT-2.md (sha256 20131357…e2e1), PROTOCOLE-AVENANT-2BIS.md (191e0bbf…36b2), KEY-W1717b.tsv
(d2e419df…610d), KEY-W1717c.tsv (3322ae87…c49c), ETALONNAGE.json, ETALONNAGE-BIS.json, scripts/mesure2.py (43db6462…6842),
MESURE2.json / MESURE2.txt (hachés dans MESURE2-AVANT.sha256 après l'unique exécution).
| Test | score | témoins (max / moy.) | marge | seuils | verdict |
|---|---|---|---|---|---|
| A' — vérité terrain 28/05 (0057–0061), clé b, mots de glose exacts (195 mots, 709 groupes) | 0,3385 | 0,1282 / 0,0585 | 0,210 | ≥ 0,60 et marge ≥ 0,30 | **ÉCHEC** |
| B' — Rel. XXII portion neuve 0091 (353 groupes), clé c, critère L7 | 0,6453 (z = 11,54) | −0,0971 / −0,3065 (sd 0,083) | gap 0,742 | z ≥ 5,16, gap ≥ 0,314, score ≥ 0,070 | **VALIDÉ** (3/3) |
Règle §5 de l'Avenant 2 : lecture seulement si A' VALIDÉ ou PARTIEL ET B' VALIDÉ → **pas de fiche LECTURE**.

### Cause de l'échec de A' (diagnostic après la mesure, non décisif)
- La clé b est faible : sans le 28/05, il ne reste que 476 groupes français glosés (0017, 0062, 0071–0072, 0080–0081, 0086–0088).
  L'aligneur y donne des valeurs fausses ou absentes sur des nombres fréquents de V : 23 = h (au lieu de p), 44 = i (au lieu de l),
  13/15 m/c, 33 et 34 presque sans appui, nomenclateur 170 / 217 / 292 absent (exclu par la liste fermée, car appuyé sur V seul).
- Les gloses abrègent ce que le chiffre épelle : « S. M. » (sa majesté), « St. » (saint), « Mr. » (monsieur), « Angl. », « Loss ».
  Chaque abréviation fait perdre un ou plusieurs mots exacts, aussi bien à la vraie clé qu'aux témoins.
- Le décodage de V par b est pourtant du français suivi, conforme à la glose : « …notre maitre… le Czar… au prince… c'étoit le
  ministre », « se voyant negligée de ses autres alli[ez] », « lors avoit eu ordres de faire des propositions sur ce sujet et ces
  ordres lui etoient donnés par Votre Excellence ; le Czar feroit avoir à Sa Majesté [la] couronne… héréditaire dans sa succession »,
  « nous aurions grand tort de [l']en détourner nos autres », « Monsieur de Saint-Saphorin s'acquittoit de ses ordres ». Part
  des caractères de glose couverts : 0,544. Constat seulement, sans valeur de validation.
- **Seuil mal calibré** : 0,60 a été fixé sans étalonnage (contrairement à B'). L'exactitude mot à mot punit chaque lettre fausse
  d'une clé réduite de moitié. L'écart à 0,30 de marge (0,21 obtenu) est donc un défaut de seuil autant que de clé.

### B' : le critère corrigé discrimine
- Étalonnage sur l'apprentissage (hors V, clé b) : les candidats prévus L1/L2/L3 restent sous z = 4 (3,50 / 2,75 / 3,50), parce
  que les témoins permutent aussi les longues valeurs du nomenclateur. Avenant 2-bis (avant la mesure) : neutralisation des valeurs
  ≥ 3 lettres → L7 (4-grammes moins unigrammes) z = 10,3 sur l'apprentissage, puis **z = 11,5 sur la portion neuve**.
- La Relation XXII est donc chiffrée en S1 et la clé c la rend en français ; elle n'est pas lue faute de A'.

### Proposition (à faire valider par Brice, nouvel avenant)
Les deux conditions ne mesurent pas la même chose : B' (portion neuve, critère étalonné) établit que la clé c lit la Rel. XXII ;
A' mesurait la capacité de reconstruire la clé sans sa plus grosse lettre, avec un seuil non étalonné. Options :
(1) accepter B' seul comme condition de lecture de la Rel. XXII, la lecture par le sens (règle de Daniel, ≥ 95 %) servant de
contrôle final ; (2) refaire A' avec un seuil étalonné, sur une portion déjà disponible : feuille 0042–0043 grillée ✗ ; il ne reste
pas d'autre vérité terrain glosée ≥ 300 groupes en S1. L'option (1) est la seule réaliste. Relevés prêts pour la lecture :
R22-0091…0093 (≈ 1 035 groupes, sous-agent) + B-REL22 (0089–0090) ; à relever : 0094–0099.
