# INTEGRATION-2511b — planche aveugle stmauris1548-2511b (68-stmauris-b), réponses de Brice — 25/11/2026, Claude Opus 5.5 (fil 🔓)

**Résultat : les 3 contrôles sont réussis, la planche est intégrée selon la règle hachée.** Ce n'est pas une mesure :
O5 reste FAIL et aucun verdict ne change.

## 1. Vérifications
- REGLE-SELECTION.md 1fe966ee7eb314ddef934946c30eea6487fa26f2c9c389bf69f25f7379286ddf = REGLE-SELECTION.sha256 ✔ (hachée 20:25:36,
  avant toute vignette ; avenant AVENANT-1.md 2b3c071a… pour le remplacement des exemples N4 rond, fait avant l'envoi).
- reponses/reponses-stmauris1548-2511b.json 2210b6b6d6e744a071c5fe392008e04c6ecf0438599ba67a5565d7b35dcf5588 = attendu ✔ ; aucune remarque dans le JSON.
- work/SHA256SUMS (planche.html ac2daca3…, cle-PRIVEE.json 7697ebc5…, scripts) : tous OK.
- Remarque de Brice dans le chat (reponses/REMARQUE-CHAT.txt) : « Attention les formes o et V fermes sont vraiment très proches
  voire mélangées ».

## 2. Contrôles cachés
| q | code | attendu | choix | |
|---|---|---|---|---|
| q12 | K1 `x` (6v L26 r5) | forme 2 | forme 2 | ✔ |
| q10 | K2 `d` (6v L18 r17) | forme 3 | forme 3 | ✔ |
| q03 | K3 `O` (6v L05 r11) | forme 1 | forme 1 | ✔ |

## 3. La remarque « o et V fermés »
Elle porte sur le **groupe N** : l'option « N4 anneau rond » (« o ») contre l'option « N4 boucle en v / D » (« V fermé »).
Ces deux options étaient déjà signalées comme proches dans AVENANT-1 (réserve 2). **Elles mènent à la même valeur** (`N4` = m
dans les deux cas). Selon la consigne, la valeur est donc retenue et la distinction rond / v n'est **pas tranchée** (elle ne sert
que pour la liste des formes).
Elle ne touche pas le groupe V : `vt` / « ox » / `x` / `xo` ne comportent ni o seul ni V fermé, et les 4 réponses sont `vt`.
Elle ne remet en cause **aucun contrôle** : K2 (`d`, longue hampe) a été reconnu ; K1 `x` et K3 `O` ne sont pas concernés.

## 4. Décisions (règle hachée seule)
| groupe | cibles | réponses | règle | décision |
|---|---|---|---|---|
| V (vt / ox) | V1 7r L06 r10, V2 8r L02 r15, V3 7v L17 r11, V4 6v L23 r5 | 4/4 `vt` | ≥ 3/4 `vt` | les 45 jetons restent `vt` (s), **confirmés avec planche** ; la variante « ox » de `vt` est établie |
| N (boucle à amorce) | N1 7r L24 r9, N2 7r L16 r2, N3 6v L15 r4, N4c 7v L09 r6 | 4/4 `N4` v/D | ≥ 3/4 `N4` | les **22 jetons tA-t1/tB-t2 deviennent `N4` → m** (clé) ; la variante est établie ; rond / v non tranché (§3) |
| P (« Piemont ») | P1 6v L15 r2 | `w` | `w` → reste o | « poe?ont » → « poemont » (r4 = N4 = m) : le mot reste **irrésolu** ; graphie ou faute du chiffreur ; « Piemont » par le sens seulement |

Aucune valeur de la clé de WAINUT n'est modifiée ; seuls des noms de formes changent.

## 5. Recompte de la lecture O5 (lecture seulement)
Outil : `recompte_planches_b.py` (7ac49f01…). Il applique les deux planches : ∞ = `w` = o (2511) et tA-t1/tB-t2 = `N4` = m (2511b).
Règles du recompte d'INTEGRATION-2511 §6. Sorties :
- `recompte-planches-2511-2511b.json` (81bd7f95…) ;
- `LECTURE-L1-avec-planches-2511-2511b.txt` (6894c990…) et `LECTURE-L2-…` (d7ab414f…) ;
- `DECODE-O5-avec-planches.txt` (13cad182…) ;
- `transcription_1548-03-12_Q_avec-planches.txt` (c1946bcf…).

| | sûrs | probables | restitués | irrésolus | lus | restitués |
|---|---|---|---|---|---|---|
| L1 O5 | 193 | 95 | 35 | 57 | 0,850 | 0,092 |
| L1 + 2511 | 255 | 52 | 15 | 58 | 0,847 | 0,040 |
| **L1 + 2511 + 2511b** | **266** | 44 | 13 | 57 | **0,850** | **0,034** |
| L2 O5 | 201 | 93 | 29 | 68 | 0,826 | 0,074 |
| L2 + 2511 | 261 | 50 | 11 | 69 | 0,824 | 0,028 |
| **L2 + 2511 + 2511b** | **271** | 41 | 10 | 69 | **0,824** | **0,026** |

- Les « ? » du décodage passent de 215 à **98** (117 jetons renommés : 95 ∞ et 22 boucles à amorce).
- Toutes les majuscules M posées par les lecteurs sur les boucles à amorce sont confirmées par la clé ; il n'y a **aucun conflit
  nouveau**. Exemples : « compte » (6v L02) et « Piedmont » (6v L21) deviennent sûrs.
- Le seul conflit reste [pIeMont] (∞ à la place du i), déjà traité dans INTEGRATION-2511. Aucun mot sûr n'est cassé.
- La part lue ne monte pas (0,850 / 0,824) : les planches rendent la lecture **plus sûre**, pas plus étendue. Les 98 « ? »
  restants sont surtout `n` (27), tA-t8/tB-t7 (23) et des formes rares.
- Information hors protocole : ce n'est pas une mesure. Aucun verdict ne change et cc. 5r-8r restent grillées.
