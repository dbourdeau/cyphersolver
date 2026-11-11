# AVENANT LOT4 au PROTOCOLE P01 — vanhalen-1840 (cat. Bourdeau n° 2423 ; AHN Diversos-Colecciones 195 N.14, PARES 4151130)
Écrit le 11/11/2026 ≈ 14:15-14:30 CET, AVANT tout décodage de H (S7, S8). Agent Opus 5.5 (fil Déchiffrement, validation).
Haché avec la clé et les scripts dans `AVENANT-LOT4.sha256`. Modèle : `ronquillo-1646/fable-c05-validation/PREREG.md` (C05).
`PROTOCOLE.md` (P01, SHA 92cf8f5a…) n'est pas modifié : cet avenant s'y ajoute et le dit là où il s'en écarte.

## État de H au moment de l'avenant
- H = S7 + S8 (P01). Personne ne l'a décodée : ni l'équipe (HANDOFF 09/11), ni Fable (lot 4 : copie d'envoi `transcription-T-envoi-lot4.txt`
  sans S7/S8, SHA 3d74450c…).
- Ce que j'ai lu de H pour écrire cet avenant, et rien d'autre (script de comptage, valeurs non affichées) : S7 = 10 nombres dont 2 « 70 » ;
  S8 = 15 nombres dont 1 « 70 » et 1 variante de forme `nn|nn` (le doute 13/18 de S8 n°4, déjà connu) ; aucune variante `58|5.8` en H.
  Fuite déclarée : le nombre de « 70 » (= a selon la clé). Les deux transcriptions donnent les mêmes longueurs.

## Pourquoi un avenant
Le critère P01 (car ≥ 0,85 ET car ≥ meilleur témoin + 0,30) n'a presque aucune puissance sur 25 nombres : Fable l'a montré
(0/12 pseudo-H avec la clé stricte, 1/12 avec l'étendue, `PUISSANCE-P01.txt`) et la calibration ci-dessous le confirme (**4,3 %** sur
300 pseudo-H). Un « non validé » P01 ne dirait rien de la clé. P01 est quand même exécuté tel quel (`scripts/measure.py`, inchangé) et
son verdict rapporté ; le verdict **décisif** est celui de la règle LOT4 ci-dessous, calibrée d'avance sur T seul.

## 1. Clé gelée : la clé ÉTENDUE
- `KEY.tsv` = copie octet pour octet de `fable-lot4-2026-11-11/KEY-PROPOSAL.tsv` : **SHA-256 d4ee393774c54f82b37cbbc1c13afe0e411d3cc30327bc0511f0988e0758a727**
  (64 valeurs : 24 observées dans T + 40 déduites de la structure, colonne « source »). Nom et place prévus par P01 (« KEY.tsv »).
- Non retenue : `KEY-PROPOSAL-strict.tsv` (24 valeurs, SHA 667fed88…).
- Justification :
  1. Toutes les valeurs de l'extension viennent de T (structure alphabétique 16/16, rangs a=12/24/58/70) ; aucune n'a été tirée de H.
  2. Avec la clé stricte, tout nombre de H absent de T (4, 21, 22, 25, 26, 29-33…) devient « ? », jamais couvert : sur 25 nombres, un
     seul « ? » coûte 4 points de couverture et coupe le modèle de langue. L'extension fait des prédictions falsifiables à la place.
  3. Une valeur extrapolée fausse ne peut que nuire à la clé elle-même (lettre fausse dans son décodage).
  4. L'extension abaisse aussi les témoins « clés mélangées » (on permute 64 valeurs, dont des consonnes rares). Ce degré de liberté
     est neutralisé ici : la calibration est faite avec la même clé, et le témoin « permutation de groupes » ne dépend pas du mélange de valeurs.
- Les nombres que la clé laisse ambigus (10, 23, 35-46, 69, 81-92) restent « ? » (non couverts). Aucune variante de `KEY-VARIANTES.md`
  n'est appliquée.

## 2. Transcription, décodage
- **Passe 1** `transcription.txt` (SHA 66f920a6…) : **décisive**, comme P01 le prévoit. Variante `a|b` : a retenue (S8 n°4 = 13).
- Passe 2 `transcription-p2.txt` (SHA d99dc675…) : décodée et notée pour information seulement (S8 n°4 = 18).
- Décodage : `measure.decode` (P01) ; normalisation a–z ; « 70 » = a (clé), pas de séparateur ; suites concaténées sans espace.

## 3. Mesures (scripts/lot4lib.py)
- **car** = couverture lexicale P01 (`measure.coverage`, même lexique `_shared/cyphersolver/lang/lexicons/es.json.gz`, SHA gz 0c49f0d4…,
  contenu = `lexique-es-cyphersolver.json` envoyé à Fable, e67ece13…), « ? » jamais couvert.
- **lm** = log10-probabilité moyenne par lettre sous un modèle de lettres à 4-grammes (interpolation fixe, poids 1/2/4/8 + plancher
  uniforme), appris sur `PISTES-AUTO/fable-api/lots/lot3/_communs/corpus-es-quijote-extrait-1.9Mo.txt` (SHA 2e086176…), lettres seules ;
  « ? » coupe le contexte. Raison : la couverture lexicale est aveugle à l'ordre (le lexique contient ≈ 900 mots de 2-3 lettres) ;
  le témoin « permutation de groupes » donne déjà une couverture de 0,64 en médiane. Le modèle de langue, lui, sépare l'ordre.
- **Témoins**, calculés sur H dans la même exécution :
  - 200 clés mélangées (valeurs de KEY.tsv permutées entre les nombres, fonction de P01), `random.Random(2423)` ;
  - 200 permutations de groupes (les 25 nombres de H mélangés entre leurs positions, longueurs 10/15 gardées, clé inchangée),
    `random.Random(2424)`.

## 4. Calibration — sur T seul (`scripts/calib_lot4.py` → `scripts/calib_lot4.out`, hachés)
- T = S1-S6 de la passe 2 avec `58|5.8` → 58 (vérifié identique à `fable-lot4-2026-11-11/T-58.txt`), 119 nombres. S2 n°5 laissé à 13
  (pas d'émendation).
- **Pseudo-H** de même forme que H : une fenêtre de 10 nombres + une fenêtre de 15 nombres, prises dans deux suites différentes de T,
  à n'importe quelle position (coupures de mots permises, ce qui est défavorable à la clé) ; 300 tirées parmi 1 869 paires
  (`random.Random(1840)`). Pour chaque pseudo-H : clé, 200 clés mélangées, 200 permutations ; plus 20 + 20 témoins neufs joués
  comme « candidats » pour mesurer les faux positifs.
- **Règle de choix des seuils, écrite dans le script avant son exécution** : c1 = 5ᵉ centile de car de la clé, arrondi en dessous à
  0,05 ; dK et dG = le même quantile q des écarts (lm − max témoins), arrondi en dessous à 0,01, avec q essayé dans l'ordre
  0,20 / 0,15 / 0,10 / 0,05 / 0 ; on retient le premier q (le plus sévère) qui donne puissance ≥ 80 % ET faux positifs ≤ 1 % pour
  chaque type de témoin.
- **Résultats (calib_lot4.out)** :
  - car de la clé : min 0,600, p05 0,760, médiane 0,920 ; témoins : clés mélangées p99 0,72, permutations p99 0,84.
  - écart lm − max(200 clés mélangées) : min −0,032, p10 0,220, médiane 0,343 ; écart lm − max(200 permutations) : min −0,094,
    p10 0,081, médiane 0,189.
  - critère P01 d'origine : puissance 0,043.
  - q = 0,20 → puissance 0,703 ; q = 0,15 → 0,793 ; **q = 0,10 → 0,820 (retenu)** ; q = 0,05 → 0,900 ; q = 0 → 0,940.

### Seuils gelés
- **C1** : car ≥ **0,75**
- **C2** : lm ≥ max(lm des 200 clés mélangées) + **0,22**
- **C3** : lm ≥ max(lm des 200 permutations de groupes) + **0,08**
- **MESURE VALIDÉE si C1 ET C2 ET C3**, sinon NON VALIDÉE.
- Puissance sur T (clé juste, pseudo-H intactes) : **82,0 %**. Faux positifs : **0 / 6 000** témoins clés mélangées, **0 / 6 000**
  permutations (C1 seul laisserait passer 0,6 % des clés mélangées et 13 % des permutations : C3 fait le travail).
- Robustesse (information) : 1 nombre faux dans la pseudo-H → puissance 59 % ; 2 nombres faux → 43 %. Clé stricte, mêmes seuils :
  59 % (100 pseudo-H).
- Limites, dites d'avance : la clé a été construite sur T, donc les pseudo-H sont dans l'échantillon et la puissance est optimiste ;
  une H avec un nombre mal prédit ou une faute de chiffreur (cf. ve[n]ir, cust{o}diar en T) a des chances réelles d'échouer. Un échec
  serait donc peu informatif ; une réussite, elle, est contrôlée (0 faux positif sur 12 000).

## 5. Contrôle de sens (décrit avant ; jugé UNE fois sur la sortie brute)
- **Sens-S7** : le clair dit « …no nos deviera poner personalmente [S6 : en contacto antes de] dicha fecha sobre = [S7] .— Sirvase V.S.
  decirme lo que guste… ». S7 doit donc fournir, en espagnol, le **complément de « sobre »** (groupe nominal : article + nom, nom de
  lieu ou nom commun, éventuellement avec une courte suite) qui **ferme la phrase** : le « .— Sirvase » qui suit ouvre une phrase nouvelle,
  S7 ne doit pas laisser de verbe ou de préposition en suspens.
- **Sens-S8** : le clair dit « …tendremos … de lejos … sobre la = [S8] .— Dios guarde a V.S. … ». S8 doit **commencer par un nom (ou
  adjectif + nom) qui s'accorde avec « la »** (féminin singulier) et **finir la phrase** avant la formule « Dios guarde ».
- Les deux suites doivent se lire en espagnol suivi (graphie d'époque admise : b/v, c/z, y/i, u pour v comme « ueir » en T).
- Relectures permises : au plus **2** sur H en tout, prises dans les classes déjà observées ou déclarées (confusions 3/5, 13/18, 13/3,
  8/3, 1/7 ; un nombre omis), chacune justifiée et notée « restituée » ou « probable » ; au plus **1** « ? » laissé irrésolu.
- **Verdict final** : clé **VALIDÉE (LOT4)** = MESURE VALIDÉE ET Sens-S7 ET Sens-S8. MESURE VALIDÉE mais sens non OK → **« à revoir »**.
  MESURE NON VALIDÉE → clé **PARTIELLE** (elle lit T ; H ne la confirme pas), quel que soit le sens.

## 6. Règles d'exécution
- **Une seule exécution** de `scripts/mesure_lot4.py`. Il vérifie le gel (`AVENANT-LOT4.sha256`), exécute P01 (`measure.py` inchangé,
  avec KEY.tsv, sur la passe 1), puis la règle LOT4, et écrit lui-même sa sortie brute dans `RESULTAT-LOT4-sortie-brute.txt`
  (création exclusive : il refuse de tourner si ce fichier existe).
- Essai à blanc permis AVANT, avec l'option `--dry-T` : il remplace H par S1 (10 premiers nombres) et S2 (15 premiers), ne lit pas H et
  n'écrit rien dans le dossier. Si l'essai révèle une panne, le script est corrigé, re-haché, et la correction déclarée dans le résultat.
- Sortie brute recopiée telle quelle ; `RESULTAT-LOT4.md` donne le verdict selon cet avenant.
- **H est brûlée après** : aucune modification de clé, de seuils, de lexique, de modèle de langue ou de transcription n'est rejouée sur H.
  Les relectures faites ensuite pour la lecture sont déclarées comme telles et n'ont aucun effet sur le verdict.
- Décompte de Daniel sur toute la lettre (S1-S8) si validée : sûrs / probables {x} / restitués [x] / irrésolus ‹…› ; ≥ 95 % = lu.
- Rien publié, aucun mail, aucune PR ni issue ; images PARES privées. Crédit : clé proposée par Fable 5.2 (Anthropic, lot 4), validation Opus.
