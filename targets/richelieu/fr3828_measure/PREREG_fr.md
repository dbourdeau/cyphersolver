# PREREG — Richelieu → Rancé (et à la reine), 1629 : lecture des chiffres imprimés par Avenel avec la clé de Daniel

Rédigé et gelé le 19/11/2026 (fil 🔓), **avant tout décodage** des neuf lettres. Aucune suite de nombres de ces lettres n'a été passée dans la clé avant le gel. (Limite honnête : les gloses d'Avenel ont été lues pendant la transcription, puisqu'elles sont imprimées sur les mêmes pages.)

## 1. Matériel gelé

| Objet | Fichier | sha256 |
|---|---|---|
| Transcription arbitrée (passe V, confirmée contre OCR A et B) | `transcription/avenel_figures_V.txt` | `4e13e311b150a80f1cb6313a7c34a182567ccb9625bd43cbd3dbcb4d193bd357` |
| Arbitrage | `transcription/ARBITRAGE.md` | `de32b17bc587bafa52c0ff3e2f27252a7c300ffc9881e30d7b87ea1ca8fa3cff` |
| Clé de Daniel, `targets/richelieu/texts/key.md` @ `9736c436ed190b3162bcc335e4a50dd72ad4fea3` | `cle-daniel/key.md` | `53f6339edaa443fe0774732df1c00ab2d50004d623c4963aa6a36261a3757fb0` |
| Clé de Daniel, `targets/richelieu/final.py` (KEY, NOMEN) même commit | `cle-daniel/final.py` | `ef2ea68928fc8bb463bbfe85fb2d065ac69a48a4b13e5332ee4398e537a0a7c8` |
| Outil de mesure (écrit avant la mesure, non exécuté sur le décodage) | `outils/measure.py` | `eb549a917a9349c24556993224e923f75276218a843c2166f541e199a0ec8f33` |

Dernier commit du dossier `targets/richelieu` de Daniel : `9736c436…` (23/10/2026). `main` lu le 19/11/2026 : `f013a6f4cc36bb27e33f4eab9c705202121920d9`.

## 2. Mesure unique

- **Clé** : celle de Daniel pour fr. 3829 ff. 87, 89, **telle quelle** : 10–28 = c b g p l o r f t a d i n h m s u e q ; 29–33 = a e i o u ; 34–38 = a e i o u ; 39 = *et* ; 40 = *de* ; 42 = *la* ; surligné = lettre doublée. Les codes de nomenclature (≥ 41) **ne sont pas mesurés** : Daniel les a en partie tirés des notes d'Avenel de ce même tome (contamination).
- **Portion de test, tenue à l'écart** : **CLIV** (fr. 3828 n° 18, 30 avril 1629) et **CLV** (fr. 3828 n° 19, 1er mai 1629). Choisies parce qu'aucune n'a servi à Daniel (il cite CXXXV, *ne piquer*, pour 33 = u, et CXCIX/CCV pour 39). Si les suites notées comptent moins de **300 signes**, on ajoute **CLIII** (et rien d'autre). Comptage avant décodage : CLIV 154 + CLV 179 = 333 signes en suites.
- **Référence** : les gloses d'Avenel en note (appel n → note n de la même page).
- **Score** : pour chaque suite de nombres placée avant un appel de note, déchiffrement par la clé, puis distance d'édition contre la meilleure sous-chaîne de la glose normalisée (minuscules, sans accents ni ponctuation, j→i, v→u, y→i). Accord en caractères = 1 − Σ distances / Σ caractères déchiffrés. (La glose peut contenir des mots en clair ou la traduction des codes : on ne pénalise pas ce qu'elle a en plus.)
- **Témoins** : 200 tables mélangées (permutation aléatoire des valeurs des signes 10–38, codes de mots 39/40/42 et doublement conservés ; graine 20261119), même score sur la même portion.
- **Seuil** : accord ≥ **0,85** ET ≥ **meilleur témoin + 0,30**. Une seule exécution de `measure.py`. Jamais rétroactif : CLIV et CLV sont grillées après la mesure.
- Accord en mots : rapporté à titre indicatif, non décisif.

## 3. Règle d'extension de la clé (écrite d'avance)

Sur les **sept autres lettres** (CXIX, CXXXV, CXLVI, CXLVII, CLIII, CLVIII, CLXVII) seulement :

- **E1** Les valeurs des signes 10–38 et des codes de mots 39, 40, 42 **ne changent pas**. Aucune réaffectation.
- **E2** Un code de nomenclature absent de la table de Daniel reçoit une valeur seulement si une note d'Avenel le glose **à cet endroit** et que les suites voisines déchiffrées s'accordent avec la glose. Il est noté « d'après Avenel, lettre X, note n ».
- **E3** Un code de la table de Daniel garde sa valeur. Si une glose d'Avenel le contredit (ex. 59 = « M. de Mantoue » en CLVIII), on le signale et l'on ne tranche pas : la lecture locale vient de la glose, la table n'est pas modifiée.
- **E4** Une suite qui ne donne un mot qu'en corrigeant un nombre imprimé (coquille présumée de l'éditeur ou faute du chiffreur) est lue comme **probable {x}**, avec la correction écrite.
- **E5** Interdiction de toucher la portion de test : rien de ce qui est lu dans CLIV et CLV ne sert à fixer une valeur. Leur lecture, après la mesure, utilise la clé de Daniel plus les seules extensions tirées des sept autres lettres ; un code glosé seulement dans CLIV/CLV est lu d'après la glose locale (lecture d'éditeur), sans entrer dans la clé.

## 4. Comptage selon la règle #728 (cyphersolver, décision du 16/11/2026)

- On compte **les mots chiffrés seulement**, lettre par lettre ; le texte en clair autour n'entre pas dans le compte.
- Unité : un mot du texte rendu par une suite chiffrée (séparation aux espaces et aux apostrophes : *d'elle* = 2 mots) ; un code de nomenclature = **1 mot** (même s'il rend « la reine mère ») ; un code de mot (39, 40, 42) isolé = 1 mot ; un code à l'intérieur d'un mot (ex. 40 dans *bor-de-aux*) ne compte pas à part.
- **Sûr** (lu) : toutes les lettres viennent de la clé sans correction et le mot est du français (graphie d'époque admise) qui fait sens dans la phrase ; ou code de la table de Daniel ; ou code glosé par Avenel à cet endroit (lecture d'éditeur imprimée, comme les groupes « grade M » admis pour jefferson1787 dans #728).
- **Trou** : probable {x} (correction d'un nombre, E4), restitué [x], irrésolu ‹…›, code sans valeur, et le cas « 20 » lu comme nombre (*le 20 mai*) contre la valeur de la clé (d) : probable.
- Seuil « lu » : ≥ 95 % des mots chiffrés ; plancher pour les textes de moins de 40 mots chiffrés : trous ≤ 5 % ou ≤ 2 mots.
- Les nombres en chiffres arabes hors suite (« 2 », « 1 », « 900# ») sont du clair.

## 5. Crédits

D.-L.-M. Avenel, *Lettres, instructions diplomatiques et papiers d'État du cardinal de Richelieu*, t. III (Paris 1858) ; Daniel Bourdeau (cyphersolver) pour la clé de fr. 3829 ; BnF (Archives et manuscrits) pour les cotes fr. 3828, 3835, 3825 ; Internet Archive pour les scans et OCR (`lettresinstructi03richuoft`, `bub_gb_OIQItRIybmIC`).
