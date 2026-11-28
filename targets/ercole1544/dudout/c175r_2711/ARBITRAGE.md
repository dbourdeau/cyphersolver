# Arbitrage c. 175r (Ercole Gonzaga à Ferrante), 27/11

Entrées : passe A et passe B (aveugles, 27/11), transcription W (contributeur WAINUT, 2-3/11 + planche 25/11).
Sorties : `transcription_arb.txt` (F01-F26), `arbitrage_log.tsv` (une ligne par colonne non unanime ou tranchée), zooms dans `zoom/`.
Scripts : `al3.py` (alignement à trois), `dec_arb.py` (décisions colonne par colonne, avec base et remarque), `build.py` (fabrique les sorties), `stats.py` (chiffres), `zl.py`/`zc.py` (zooms).

## Méthode
1. **Correction f/s de A** avant comparaison : là où A note `f` et B `s` (s rond), A a été passé en `s` : F01, F04, F05, F08 (×3), F12, F13. Vérifié à l'image : ce sont bien des s ronds (= signe s, clair f). Trois cas restés `f` chez A et marqués {f|s} chez B (F07 ʃ après r, F12 « regno », F17) ont été regardés au zoom : F07 = ʃ long (f), F12 = signe haut à crochet ({f|t}, voir plus bas), F17 = s rond (s).
2. Alignement A↔B (difflib), puis W projeté sur la séquence A/B : 1 317 colonnes.
3. Chaque ligne vue en bande 3,2x (4 morceaux, repères x tous les 25 px), puis chaque désaccord sur zoom 5-9x (autocontraste). Décision par la **forme** d'abord ; le sens seulement quand la forme ne tranche pas (marqué « sens », alternative gardée).
4. Critères de forme fixés en cours d'arbitrage et appliqués partout :
   - **b / h** : b = grande panse refermée sur la haste ; h = petite panse ouverte qui s'enroule (comparaison F01 x≈355 contre x≈410, F04 x≈675 contre x≈710). Cela tranche la plupart des confusions h/b de B.
   - **g / q / z** : g = boucle inférieure fermée (souvent par un retour fin, pâle) ; q = queue droite ; z = « 9 » dont la queue balaie à gauche sous le signe.
   - **« a d » = un seul « d »** (panse + haste). A et B l'ont parfois coupé en n + y (F07, F09).
   - Forme « d » : y (l) ou d (q) ne se distinguent pas à la forme (note de A) → {d|y} décidé par le sens, 5 cas.
   - « ı + 9 crochu » = S ; « ı + q » = 14 ; « s9 » = 59 ; « b ı » = 61 ; 68 = un seul signe.
5. Recouvrements de bandes : plusieurs signes doublés repérés et retirés (W F07 « b y », W F09 « n d h », W F25 « c r e… », A F07 « y b »).

## Exposants L^ (règle 3)
Planche de comparaison `zoom/zLcmp2.png` (même échelle, 6x) :
- **F07 (x≈395), F09 (x≈860), F17 (x≈450), F23 (x≈975)** : L suivi d'un **trait court séparé puis d'un o** (« ı o ») → **L^10**. Les quatre sont identiques.
- **F14 (x≈720), F18 (x≈1145), F24 (x≈1250)** : L avec une **boucle seule** accrochée en haut (pas de trait séparé ; F24 a un petit trait *à l'intérieur* de la boucle) → **L^o**.
- **F07 (x≈1115)** : exposant en **« v » ouvert**, pas un o fermé → lu **L^r** (alternative L^o gardée : {L^r|L^o}). C'est B qui avait lu L^r ; A et W L^o.
- **F17 et F23 : A et B lisent L^o, W lit L^10 ; l'image donne L^10** (trait « ı » distinct avant le o, comme F07/F09 où A ou W lisaient déjà L^10). B avait d'ailleurs noté en F09 « L^o précédé d'un petit trait (L^co) » : c'est ce même trait qui fait le 10.

## Chiffres
- Colonnes alignées : 1 317 ; **A = B = W : 1 050**.
- Colonnes en désaccord : 267 (A≠B : 145 ; A=B≠W : 122).
- Convention : `{-|f}` (F13) = signe peut-être absent.
- Bases de décision (294 lignes du journal, y compris quelques colonnes où seules les alternatives différaient) : **forme 191**, majorité+forme 83, **sens 16**, majorité seule 3, forme+sens 1.
- A=B≠W : A=B gardé 102 fois ; 14 décisions contre A=B, toutes sur zoom (ex. F04 h, F18 a, F19 « h a n d », F07 « d » sans n, F17/F23 L^10, F01 z final).
- Transcription arbitrée : **1 263 signes**, dont **30 encore douteux** {x|y} (16 tranchés par le sens, 14 par une forme hésitante) ; aucun « ? ».

## Taux de désaccord contre l'arbitrage (distance d'édition en signes, premiers choix, / 1 263)
| passe | signes | strict | si l'alternative de l'arbitrage est acceptée |
|---|---|---|---|
| A (corrigée f/s) | 1 276 | 107 (8,5 %) | 96 (7,6 %) |
| B | 1 271 | 72 (5,7 %) | 55 (4,4 %) |
| W | 1 245 | 124 (9,8 %) | 114 (9,0 %) |

B est la meilleure passe. Les écarts de A viennent surtout des comptes (signes coupés ou doublés : « a d », « c c », extra n/r) et de q/g ; ceux de W surtout d'omissions et de doublons de recouvrement, et de choix guidés par le sens (h/b, n/a). Une part des écarts de W tient aussi à l'alignement imparfait de lignes très différentes (F01, F08, F09, F25).

## Signes encore douteux méritant une planche de formes
Positions = rang du signe dans `transcription_arb.txt` ; coordonnées approximatives dans 003.jpg (x ; y = centre de ligne). Les 5 {d|y} (F09 x≈700, F16 x≈745, F17 x≈555, F21 x≈235, F25 x≈1160) et F03 {19|S} (même valeur ss) ne sont pas repris : la forme ne peut pas les trancher.

| ligne | pos. | options | x | y | remarque |
|---|---|---|---|---|---|
| F01 | 43 | c / e | 1065 | 247 | c à petite boucle intérieure |
| F01 | 47 | S / 14 | 1160 | 247 | ı + 9 crochu ou ı + q |
| F02 | 28 | g / q | 775 | 303 | queue presque droite, petit crochet |
| F06 | 43 | y / e | 1215 | 517 | panse + point haut : haste pâle ? |
| F07 | 2 | g / f | 225 | 575 | signe surchargé |
| F07 | 3 | x / k | 235 | 575 | croix au-dessus de la surcharge |
| F07 | 40 | L^r / L^o | 1115 | 575 | exposant en v ouvert |
| F07 | 45 | 17 / 27 | 1215 | 575 | premier chiffre en « T » |
| F08 | 16 | 24 / 2+q | 540 | 632 | la planche W du 25/11 a lu « 2 q » |
| F08 | 38 | c / e | 1040 | 632 | c sans boucle, sens « parentado » = e |
| F08 | 48 | b / h | 1235 | 632 | panse petite, fermée ? |
| F09 | 27 | b / h | 720 | 689 | panse fermée ?, sens « qual » = h |
| F11 | 36 | h / r | 1020 | 801 | corps d'h sans haste nette |
| F12 | 12 | e / c | 405 | 858 | sens « del regno » = e |
| F12 | 14 | f / t | 435 | 858 | signe haut à crochet ; sens « regno » = t |
| F13 | 47 | (rien) / f | 1235 | 914 | long trait diagonal entre r et p |
| F18 | 19 | c / e | 605 | 1268 | deux c simples ; sens « pratiche » = e |
| F18 | 28 | n / a | 785 | 1268 | arceau ouvert ; sens « con il » = a |
| F20 | 17 | f / h | 585 | 1384 | trait fin à crochet lié à un arceau |
| F21 | 42 | p / f | 1190 | 1440 | hampe descendante sous panse |
| F22 | 19 | r / e | 530 | 1498 | petit ɾ entre « v » et e |
| F23 | 34 | f / x | 1040 | 1557 | ʃ croisé (surcharge ?) |
| F24 | 7 | z / g | 320 | 1611 | « 9 » avant le 24 pâle |
| F26 | 38 | h / t | 960 | 1669 | haste haute + arceau ; sens « genti » = t |

Doutes de compte (pas de signe dans la transcription, à vérifier sur planche) :
- F08, x≈940, y 632 : tache d'encre accolée au x après « s n e » (B {f|s}) ; non comptée.
- F07, x≈340, y 575 : « q r d » — panse rattachée au d (A et B lisaient n + y) ; un seul signe retenu.
- F22, x≈500-550, y 1498 : quatre signes « c v ɾ e » avant 30 (A c r e r, B c r r e, W c n p r).

## Remarques
- W F03 premier signe : l'image montre une panse à queue droite sans haste → **q** (accord avec la correction de la planche du 25/11).
- F15 : à 8x, « x n e n x » ; A et B comptaient un signe de plus, W un de moins.
- F25 : un seul c dans « b c e r f » (A en compte deux) ; le signe suivant est un ʃ haut (A t).
- Aucune image ni dérivé hors du dossier de travail ; zooms dans `arb/zoom/`.
