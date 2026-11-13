# LECTURE — DECODE R8492 (BL Harley MS 287 f. 88r) — Lord Cobham à Walsingham, 1588

2026-11-13, agent Opus, fil Déchiffrement. Au compte de Daniel Bourdeau (`targets/cobham1588`, catalogue n° 131). 🔴 Aucune image ni découpe DECODE publiée ; citer « DECODE R8492 ». f. 88v (P2) sans chiffre.

## Statut (exact)

**Lu en partie : 20 mots chiffrés sur 56 lus par le sens = 36 %** (7 sûrs, 13 probables, 3 restitués, 33 irrésolus). Codes à part : ·V· (l. 6) et 15 (l. 13) dans le chiffre ; 15 (l. 3, l. 7) dans le clair. **Seuil de 95 % très loin → « read in part », pas de publication.**

## Méthode
1. Deux passes (P.., Q..) arbitrées sur l'image → `R8492_chiffre.tsv` (29 passages), SHA256 `2832a3eaef1c788262b76cef00377e592c8296715259e8daa2fc516823a50573`, haché avec l'addendum `PREREG-B.addendum-B1-R8492.md` AVANT décodage. Détail : `R8492_arbitrage.md`.
2. Décodage brut : `R8492_decodage_cle_gelee.txt` (script et clés inchangés). NB : le script coupe les mots sur « | » avant de lire les hésitations {a|b} ; une annexe décode donc deux copies dérivées (1re / 2e forme de chaque hésitation).
3. Valeurs nouvelles seulement dans `cle_R8492_derivee.tsv` (Γ = e B ; ρ non barré = m C ; N 2+2 = f C ; + = i C).
4. Unités de lecture = mots du clair. Les blancs du chiffre sont peu fiables (points-séparateurs, blancs faibles) : quand un mot du clair chevauche deux groupes (E09 « Italian / starving », E14 « the ton »), on compte les mots du clair. Classes : *sûr* = valeurs de la clé gelée / dérivée A, au plus un choix d'ensemble ; {probable} = un signe de force B/C, une hésitation de forme ou ≥ 2 choix d'ensemble, sens net ; [restitué] = un signe hors ensemble ou mot complété ; ‹irrésolu›.

## Tableau des mots chiffrés

| n° | id | signes | brut (clé) | lecture | classe | justification |
|---|---|---|---|---|---|---|
| 1 | E01a | 8 V {Q|Z} {G|K} w R N | cra/o g/? k o n | ‹…› | irrésolu | nom propre ? (K hors clé) |
| 2 | E01b | K v L L A {Y|h} c V X h | ? a l/p l/p s/t r/h o/a/e r x/c/i h | ‹…› | irrésolu | K hors clé ; aucun mot |
| 3 | E02 | Q 8 R N A | a c o n t | {acont} = account | probable | Q = a (dérivé B) ; « [40 men] of acont » |
| 4 | E03 | A h 7 | the | the | sûr | clé gelée |
| 5 | E04 | h {Q|Z} u E N | h a v e n | {haven} | probable | Q = a (B) et hésitation Q/Z (Z donnerait « hoven ») ; « have promised the haven of » |
| 6 | E05a | V v · I N | r a · i n | ‹ra·in› | irrésolu | lieu ? point de valeur inconnue |
| 7 | E05b | A L d V A | s/t/a l/p o r s/t/a | ‹a port ?› | irrésolu | « a port » exige A = a et L = p (deux valeurs C) ; sens faible |
| 8 | E06a | X {c|R} · I · V v | ? o ? i ? r a | ‹…› | irrésolu | |
| 9 | E06b | A h 7 V | ther | ther | sûr | clé gelée |
| 10 | E07a | R N N | o n n | ‹…› | irrésolu | |
| 11 | E07b | T 7 F E V {+|T} A | t e f e r b/t s/t | ‹…› | irrésolu | |
| 12 | E08a | Q G V 7 A (1) | a | {a} | probable | « agret » = a gret ; Q = a (B) |
| 13 | E08a | Q G V 7 A (2) | gret | {great} | probable | g-r-e-t de la clé ; blanc absent entre « a » et « gret » |
| 14 | E08b-c | L 7 N A + R N | p e n s b o n | [pension] | restitué | + = b dans la clé ; « pension » exige + = i (C) |
| 15 | E08d | X {c|R} N A h L T | c/x o n s/t h l/p t | ‹…› | irrésolu | |
| 16 | E09a | B 7 A I R | b e s/t i o | ‹…› | irrésolu | |
| 17 | E09b | I A Q {L|P} I U N | i t a l i a n | {Italian} | probable | Q = a (B), hésitation L/P (signe taché) |
| 18 | E09c | A A Q V u I N G | s t a r v i n g | {starving} | probable | deux choix d'ensemble (A = s, A = t) + Q = a |
| 19 | E09d | c A | a t | at | sûr | c = a (A), A = t |
| 20 | E09e | {h|L|P} 7 | th e | {the} | probable | 1er signe noyé dans une tache |
| 21 | E09f | {S|h} K | ? ? | ‹…› | irrésolu | S et K hors clé |
| 22 | E10a | I A N 7 {Y|h} I O | i s/t n e r/h i d | ‹…› | irrésolu | |
| 23 | E10b | U N A R N I d | a n t o n i o | Antonio | sûr | R = o, d = o (dérivés A) ; Don Antonio (prétendant portugais) |
| 24 | E11 | c V A h | o/a/e r s/t h | ‹…› | irrésolu | « forth » si le trait montant initial était f : non retenu |
| 25 | E12 | L P h d {+|T} D | l/p p h o b/t d | ‹…› | irrésolu | |
| 26 | E13 | L P 7 O · I A | l/p p e d · i s/t | ‹…› | irrésolu | « …pped it » ? |
| 27 | E14a | L I u 7 V | l i v e r | [deliver] | restitué | « liver » de la clé ; « de- » absent (ou « or » du clair = O R chiffrés « do- ») |
| 28 | E14b | T d N | t o n | ‹ton› | irrésolu | |
| 29 | E14c | A h E (A R N) | the | the | sûr | E = e (A) |
| 30 | E14c | (A h E) A R N | t o n | {ton} = town | probable | « the ton » = the town ; « … to 15 [Parma] by means of our abode » |
| 31 | E15a | O I u 7 V A | d i v e r s | divers | sûr | O = d (A), A = s (ensemble) |
| 32 | E15a' | R N | o n | ‹on› | irrésolu | sens non établi |
| 33 | E15b | X d · I · V Z | c/x o · i · r o | ‹…› | irrésolu | |
| 34 | E15c | A R L D {R|T} 7 V A | s o l d ? e r s | {soldiers} | probable | un signe (Γ) sans la valeur i ; « there are coming of other hither divers … soldiers » |
| 35 | E16 | U V Q L L u 7 V I O | a r a l/p l/p v e r i d | ‹…› | irrésolu | |
| 36 | E17a | N u {Y|h} B {R|T} V | n u ? b ? r | {number} | probable | ρ = m (passe 2 {M|h}, C) ; Γ = e (B) |
| 37 | E17b | d N | o n | [of] | restitué | N 2+2 = f (hypothèse C) ; « the number of fforty » |
| 38 | E18a | L {7|I} V G {R|T} | l e r g ? | ‹…› | irrésolu | |
| 39 | E18b | L V d {Y|h} I A I A {Y|h} 7 + O | l r o ? i s/t i s/t ? e b d | ‹…› | irrésolu | |
| 40 | E19a | 7 N A I A T O | e n s/t i s/t t d | ‹…› | irrésolu | |
| 41 | E19b | c A 8 R A | o/a/e s/t c o s/t | ‹…› | irrésolu | |
| 42 | E20 | I N A {R|T} L L I G E N A | i n t ? l l i g e n s | {intelligens} = intelligence | probable | Γ = e (B) ; « and such intelligence there is » |
| 43 | E21a | 7 N I {Y|h} · T | e n i ? · t | ‹…› | irrésolu | |
| 44 | E21b | 7 I N O I {E|I} A | e i n d i e/i s/t | ‹…› | irrésolu | |
| 45 | E21c | A V 7 N d {E|I} A {L|8} R V A I O | t r e n o … o r t i d | ‹…› | irrésolu | |
| 46 | E22a | X V 7 A E V | c/x r e s/t e r | ‹…› | irrésolu | |
| 47 | E22b | {Y|h} A A A 7 I | ? s/t s/t s/t e i | ‹…› | irrésolu | |
| 48 | E23 | c A | o/a/e s/t | ‹…› | irrésolu | report de marge, rattachement incertain |
| 49 | E24a | I N | in | in | sûr | clé gelée |
| 50 | E24b | F V v N 8 {I|E} | f r a n c e | {France} | probable | v = a (C → B) ; hésitation ⅃ I/E |
| 51 | E25 | {U|c} P I A u V | a p i t u r | ‹…› | irrésolu | |
| 52 | E26 | F | f | ‹…› | irrésolu | signe seul en fin de ligne (« to deal with F … ») |
| 53 | E27 | {+|T} A R N | b/t s/t o n | ‹…› | irrésolu | interlinéaire |
| 54 | E28 | T u 7 I N G | t v e i n g | ‹…› | irrésolu | nom ? |
| 55 | E29 | W · I N A {R|T} V | w i n t e r | {Winter} | probable | Γ = e (B) ; point ignoré ; Sir William Winter ? |
| 56 | — | (E14 « L I » + « u » comptés dans n° 27) | | | | |

Décompte : 55 unités de lecture listées n° 1–55 (la ligne 56 est un renvoi) → **55 mots chiffrés** : sûrs 7 (the, ther, at, Antonio, the, divers, in) ; probables 13 (account, haven, a, great, Italian, starving, the, town, soldiers, number, intelligence, France, Winter) ; restitués 3 (pension, deliver, of) ; irrésolus 32. **(7 + 13) / 55 = 36,4 %** → read in part.

## Codes (non lus ici ; mesures à l'orchestrateur, PREREG-B §Valeurs de codes)
- **·V·** (E11, l. 6) : « the other(s) ‹c V A h› **·V·** they be booted ‹…› is good ‹…› they have promised them or [deliver] ‹ton› the town to 15 by means of our abode » → [code ·V·], non glosé.
- **15** (E21, l. 13, dans le chiffre) : « … me the ‹7 N I ρ · T› **15** ‹7 I N O I E A› ‹A V 7 N d E A L R V A I O› to ‹X V 7 A E V› … » → [code 15] (acquis = duc de Parme).
- **15** en clair, l. 3 : « … ther bo[biffé] **15** : of late theirs … » ; l. 7 : « … the town to **15** by means of our abode ». (15 acquis.)
- Signes biffés non transcrits : tache barrée l. 4 (après R N N) ; signe en croix taché l. 13 (avant 7 I N O).

## Lecture continue (anglais ; chiffre en *italique*)
> There is captain Montgomery gone of late into Scotland. *‹…› ‹…›* with 40 men of *{account}* have promised *the {haven}* of *‹…› ‹…›* is *‹…›* *ther* bo[…] 15: of late theirs, [a] boory of 30 *‹…› ‹…›*, who have *{a great} [pension] ‹…›*. There *‹…› {Italian} {starving} at {the} ‹…›* the ?o?y *‹…› Antonio*; the other(s) *‹…›* [·V·] they be booted *‹…›* is good *‹…›* they have promised them or *[deliver] ‹ton› the {town}* to 15 by means of our abode. There are coming of other hither *divers ‹on› ‹…› {soldiers}* *‹…›* away to the *{number} [of]* ff…y; of late they have such *‹…› ‹…›* unto their 500 *‹…› ‹…›* who have sent them. Then a ? more; our abode doing no good how such [… …] door; and such *{intelligence}* there is [… ] me the *‹…›* 15 *‹…› ‹…›* to *‹…› ‹…› ‹…›* *in {France}* they say that he will have *‹…›* to deal with *‹…›* bslk(?) the D. of Parma's commissioners … *‹…›* (interl.) Lotey … *‹…›* and *{Winter}* would send money to their wives …

## Résumé (FR)
Lettre de Lord Cobham à Walsingham (1588, f. 88r ; probablement des Flandres pendant la conférence de paix). En clair : le capitaine Montgomery est parti pour l'Écosse ; des gens arrivent ; « notre séjour ne fait aucun bien » ; une grande flotte/Mercado ; 80 voiles passées ; il prie de ne pas oublier ; « … would send money to their wives ». Les mots chiffrés lus évoquent : quarante hommes de qualité ayant promis le havre de […] ; des gens « who have a great [pension] » ; des Italiens affamés ; **(Don) Antonio** ; une promesse de [livrer] la ville à Parme (15) « par le moyen de notre séjour » ; « divers […] soldats » qui arrivent ; « au nombre de [quarante ?] » ; « telle intelligence il y a » ; « en **France** on dit qu'il aura […] à traiter avec […] les commissaires du duc de Parme » ; **Winter** enverrait de l'argent aux épouses. Lecture très partielle (36 %).

## Summary (EN)
Lord Cobham to Walsingham (1588, f. 88r; probably from Flanders during the peace talks). In clear: Captain Montgomery has gone into Scotland; people are coming; "our abode doing no good"; a great Mercado; 80 sail passed by; "forget it not"; "… would send money to their wives". The cipher words read mention forty men of account who have promised the haven of […]; men "who have a great [pension]"; starving Italians; **(Don) Antonio**; a promise to [deliver] the town to Parma (15) "by means of our abode"; "divers […] soldiers" coming; "to the number [of forty?]"; "such intelligence there is"; "in **France** they say that he will have […] to deal with […] the Duke of Parma's commissioners"; **Winter** would send money to the wives. Very partial reading (36 %, read in part).

## Fichiers
`R8492-pass1.tsv`, `R8492-pass2.tsv`, `R8492_arbitrage.md`, `R8492_chiffre.tsv` (+ .sha256), `PREREG-B.addendum-B1-R8492.md` (+ .sha256), `R8492_decodage_cle_gelee.txt`, `cle_R8492_derivee.tsv`, ce fichier (+ .sha256).

---
*(Tout ce qui suit a été ajouté APRÈS le hachage : LECTURE-R8492.md.sha256 = 99326dc9…16d6 porte sur les lignes 1–94 seules ; vérifier par `head -n 94 LECTURE-R8492.md | shasum -a 256`.)*

## Addendum 2026-11-13 23:10 — correction de décompte (sans changer aucune lecture)
L'en-tête « Statut » dit 56 mots / 33 irrésolus ; le tableau compte 55 unités (la ligne 56 n'est qu'un renvoi). Chiffres exacts : **55 mots chiffrés ; 7 sûrs, 13 probables, 3 restitués, 32 irrésolus ; (7 + 13) / 55 = 36,4 % → read in part.**

## Écarts avec Daniel (texts/R8492_reading.md, re-lu 22/10 ; ouvert APRÈS hachage)
- **Mêmes lectures** : the haven (l. 2-3), there/ther, Italian(s), Antonio, divers, number of — indépendamment retrouvés.
- **Neuf chez nous (à vérifier par lui)** : *account* (E02 Q 8 R N A, « 40 men of acont », Daniel : non lu) ; *a gret* + [pension] (E08) ; *starving at the* (E09 ; Daniel *[?arriving]* sur « QV:InG » sans le A A initial) ; *the ton(e)* = the town et [deliver] (E14) ; *soldiers* (E15c) ; *intelligens* (E20) ; *in France* (E24) ; *Winter* (E29) ; valeur Γ (forme R/T à hampe à gauche) = e.
- **Clair divergent** : l. 7 nous « … the town **to 15** by meanes of our aboade » / Daniel « to us by reason of our aboode » ; l. 3 nous « ther bo[biffé] 15 : of latte theyrs » / Daniel « there to [15]. Of latte there ys » ; l. 8 nous « of other hethere » / Daniel « of other Scottishmen » ; l. 21 nous « and *{Winter}* woolde send mony to theyr wyfes » / Daniel « *[…]* and *[…]* worde[s]; send money to them by such ». À trancher sur l'image par un tiers.
- **Daniel a, pas nous** : *[?captain]* (E01a, deux signes inexpliqués chez lui) ; *[?Naples]* (sur « nQpIcΛ » ; notre E10a « I A N 7 ρ I O » ne le donne pas : transcriptions différentes).
- **Transcription** : Daniel lit les ǂǂ à 3 hampes comme n (comme nous) ; il note les points (« ·· », « : ») là où nous avons u / · ; notre arbitrage voit E05 « A L d V A » là où il a « ∩ϕdΛ » (même mot).
- Aucun écart ne modifie la lecture hachée ; pas de correction en addendum.
