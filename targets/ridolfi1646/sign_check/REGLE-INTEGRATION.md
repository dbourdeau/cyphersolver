# REGLE D'INTEGRATION — planche-c06 (D.107, Ridolfi, Rome 8/5/1646)
Écrite et hachée le 11/11/2026 AVANT toute ouverture de la planche par Brice (SHA-256 dans REGLE-INTEGRATION.sha256).
Aucune modification après ouverture ; toute dérogation sera écrite à part, datée, et ne remplacera pas ce fichier.

## Objet
Les 21 mots « restitués » de la lecture publiée (PR cyphersolver #403, classe « read in part », 405/431 = 94,0 %)
reposent chacun sur UN groupe corrigé. La planche fait relire sur l'image, à l'aveugle, la forme du chiffre en cause.

## Ce que contient la planche (19 questions + 2 contrôles, ordre tiré au hasard, graine dans make_planche.py)
| lieu (transcr. v1) | groupe transcrit | chiffre en cause | candidats (transcrit / correction) | mot restitué (ligne LECTURE) | classe si confirmé |
|---|---|---|---|---|---|
| 1.01 pos15 | 74 | dizaine | 7 / 3 | il (1.01) | sûr |
| 1.12 pos11 | 79 | unité | 9 / 3 | quando (1.12) | sûr |
| 1.17 pos2 | 24 | dizaine | 2 / 3 | il (1.16) | sûr |
| 1.17 pos13 | 22/27 | unité | 2 / 7 | atacatto (1.16) | sûr |
| 2.01 pos4 | 66 | unité | 6 / 8 | lontano (1.21) | sûr |
| 2.01 pos12 | 62 | unité | 2 / 1 | miglia (1.21) | sûr |
| 2.04 pos14 | 61 | unité | 1 / 5 | Bologna (2.03) | sûr |
| 2.05 pos11 | 61 | unité | 1 / 8 | Milano (2.03) | sûr |
| 2.13 pos14 | 36 | unité | 6 / 8 | perche (2.13) | sûr |
| 3.08 pos17 | 74 | unité | 4 / 3 | quando (3.08) | sûr |
| 3.12 pos1 | 24 | dizaine | 2 / 3 | al (3.08) | sûr |
| 3.20 pos6 | 243/23 | ce qui suit le 2 | « 43 » / « 3 » | risolutione (3.19) | sûr |
| 4.02 pos2 | 42 | unité | 2 / 1 | loro (4.01) | sûr |
| 4.04 pos2 | 74 | dizaine | 7 / 3 | al (4.02) | sûr |
| 4.04 pos4 | 37 | unité | 7 / 3 | Signor (4.02) | sûr |
| 4.05 pos15 | 74 | dizaine | 7 / 3 | al (4.04) | sûr |
| 4.13 pos7 | 30 | unité | 0 / 6 | mandero (4.11) | sûr |
| 4.19 pos1 | 68/67 | unité | 8 / 7 | termini (4.17) | sûr |
| 5.07 pos9 | 26 | dizaine | 2 / 7 | oferte (5.05) | sûr |

« sûr » = une fois le chiffre remplacé, toutes les syllabes du mot se lisent directement avec la clé validée
(KEY-PROPOSAL.json gelée, fable-c05-validation) sans autre correction ni conjecture. Si, au moment de l'intégration,
un mot s'avère dépendre d'autre chose que de la clé (autre groupe douteux, coupe de mot incertaine), il passe
« probable » et non « sûr ».

Contrôles (réponse connue, mots sûrs) : 2.05 pos15 « 38 » (unité 6 / 8 → 8 attendu, « partito ») ;
1.19 pos10 « 78 » (dizaine 7 / 3 → 7 attendu, « questo »).

## Hors planche (restent restitués, quelle que soit la planche)
- 1.08 « di » (lo stato <di> Milano) : groupe 72 omis. Aucune forme à juger : l'image montre l'espace normal
  entre 78 et 56, sans groupe, rature ni interligne → omission du chiffreur ; la planche ne peut pas le confirmer.
- 5.03 « lunghezza » (47 = z) : question de VALEUR, pas de forme. Les deux chiffres 4 et 7 (chevron) sont nets sur
  l'image ; seul un 2ᵉ emploi de 47 (autre pièce du même chiffre) pourrait le faire passer probable/sûr.

## Règle, question par question
1. Lire le choix exporté par Brice (forme 1 / forme 2 / autre / illisible / je ne sais pas) ; traduire forme 1/2
   en chiffre par cle-PRIVEE.json (seul endroit où figure la correspondance).
2. Si le choix est une forme : le chiffre choisi REMPLACE celui de la transcription v1 à ce lieu (nouvelle
   transcription v2 écrite à part, v1 gelée intacte). On décode le mot avec la clé validée, sans autre changement.
   - la lecture obtenue = le mot restitué → le mot passe de « restitué » à la classe indiquée ci-dessus (sûr, ou
     probable selon la définition) ;
   - le chiffre choisi = celui de la transcription v1 (la correction n'est pas vue sur l'image) → le mot RESTE
     restitué (erreur probable du chiffreur ; noté « image conforme à v1 ») ;
   - autre lecture → le mot reste restitué, noté.
3. Si le choix est « autre », « illisible » ou « je ne sais pas » (Brice indécis) → le mot reste restitué.
   Une remarque de Brice donnant un autre chiffre est consignée mais ne vaut pas confirmation.
4. Contrôles : si les DEUX contrôles reçoivent la réponse attendue, la règle s'applique. Si un contrôle est manqué
   (mauvaise forme, autre, illisible ou je ne sais pas), AUCUNE question n'est intégrée : tous les mots restent
   restitués, on le note et on en parle à Brice avant toute suite.
5. Aucune autre question ni planche de rattrapage avant d'avoir appliqué cette règle et recompté.

## Recompte façon Daniel (après intégration)
- Même script de classes que fable-c05-validation/scripts/decompte.py, sur une copie des LECTURE où les mots
  confirmés perdent leurs chevrons < > ; 431 mots au total, inchangé.
- read_share = (sûrs + probables) / 431, restitués EXCLUS (règle du README de Daniel, précédents delcarretto1576,
  schoenberg1665). Actuellement 405/431 = 94,0 %.
- ≥ 95 % (soit ≥ 410/431, donc au moins 5 confirmations) → la lettre passe « read » : mise à jour de la PR #403
  (classe, read_share, reading_review, note de crédit « relecture aveugle des formes sur image : Brice Dudout »).
- < 95 % → reste « read in part » ; on met à jour seulement le décompte.
- Le résultat (réponses brutes, traduction par la clé, classes avant/après, recompte) est écrit dans
  planche-c06/RESULTAT.md et une entrée HANDOFF.
