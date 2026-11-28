# Règle de sélection — planche aveugle « Lee, Paris, février 1813 » lee1813-2511, 25/11/2026

Écrite et hachée (REGLE-SELECTION.sha256) AVANT les vignettes de la page ; les cadres ont été vérifiés sur une
planche-contact (scratchpad) avant le hachage. Lieux choisis d'après les fichiers texte du dépôt de Daniel,
targets/lee1813/ (transcription_*.txt, decryption_*.txt, error_accounts.txt régénéré par errors.py, profile.json
gaps, NOTES.md §6). Lieu = stretch + rang du nombre (n1 = 1er nombre du stretch, « : » et « | » exclus).

Pièce : William Lee à James Monroe, Paris, 2 et 6 février 1813, NARA RG 59, microfilm T164 bobine 3, cadres
0106-0110 (catalogue NARA, NAID 211586337, domaine public), JPEG pleine résolution
catalog.archives.gov/medialz/.../T164-03-<cadre>.jpg, copiés sur SPOF_2 planches-pistes-2511/lee1813/images/.
Chiffre WINCHESTER (nombres 1-25). Écriture de Lee pour le 6 fév. (cadres 0108-0110) ; main d'un copiste pour le
2 fév. (« Copy of Dispatch C », cadres 0106-0107) : les exemples d'une question viennent toujours de la même main
que la cible. Le crayon du commis de 1813 (lettres de clé et clair) est visible sur les pages 1-3 du 6 fév. : les
vignettes sont serrées sur la ligne des nombres ; aucune glose, libellés « forme 1… ».

## Pourquoi ces questions
Les trous du 6 fév. qui dépendent d'une FORME sont de deux sortes : (a) un nombre lu 16 là où la clé demande 10, 13
pour 18, 17 pour 7 (paires sosies de errors.py) ; (b) les points entre chiffres, irréguliers chez Lee, dont dépendent
les propositions du profil (F6-01/02 « I established … a cipher, a copy », F6-47 « but on », 2 fév. J « indemnities
through »). On demande à quoi ressemble le nombre ou le groupe encadré. Une réponse « comme transcrit » laisse tout
en l'état ; « aucune / autre forme », « illisible », « impossible à distinguer » = rien ne change.

## Jeux d'options (exemples : lieux sûrs, stretches lus sans trou à cet endroit, jamais un lieu de question)
- D16 (Lee) = { `10` : F6-33 n9 (0109), F6-21 n30 (0109) ; `16` : F6-21 n27 (0109), F6-21 n32 (0109) }
- D17 (Lee) = { `1` : F6-21 n9, F6-38 n4 ; `7` : F6-21 n23, F6-38 n5 ; `17` : F6-21 n31, F6-25 n22 } (tous 0109)
- D13 (Lee) = { `13` : F6-69 n4, F6-69 n30 ; `18` : F6-69 n8, F6-69 n21 } (tous 0110)
- P12 (Lee) = { `12` un nombre : F6-01 n2, F6-03 n3 ; `1·2` deux nombres : F6-05 n33-34, F6-06 n9-10 } (0108)
- P11 (Lee) = { `11` un nombre : F6-04 n11 (0108), F6-32 n7 (0109) ; `1·1` deux nombres : F6-04 n6-7 (0108),
  F6-32 n8-9 (0109) }
- P23 (Lee) = { `23` un nombre : F6-46 n30, F6-38 n1 (0109) ; `2·3` deux nombres : F6-22 n19-20 (0109),
  F6-52 n16-17 (0110) }
- PJ (copiste, 2 fév.) = { `17` un nombre : AE n1, AJ n3 (0107) ; `1 7` deux nombres : Y n25-26 (0107, sans point),
  AJ n6-7 (0107, « 1:7 ») }
Deux formes d'un même code ne sont jamais dans une même question (chaque option = un nombre ou un groupe différent).

## Cibles (10) — transcrit → ce que demande la lecture → effet
| id | lieu (cadre) | jeu | transcrit | côté « mot » | effet si le côté « mot » est choisi |
|---|---|---|---|---|---|
| T01 | F6-01 n29-30 (0108) | P12 | 1·2 | 12 | appuie « I established » (§ F6-01) ; 0 mot au compte |
| T02 | F6-02 n5 (0108) | P11 | 11 | 1·1 | appuie « a [c]ipher, a copy » (§ F6-02) ; 0 mot au compte |
| T21 | F6-21 n20 (0109) | D16 | 16 | 10 | exh[a]usted → exhausted (+1) |
| T25 | F6-25 n26 (0109) | D16 | 16 | 10 | Swartzenb[o]urg → lu (+1) |
| T35 | F6-35 n11 (0109) | D16 | 16 | 10 | o[f] → of (+1) |
| T37 | F6-37 n7 (0109) | D17 | 17 | 7 | Vicero[y] → Viceroy (+1) |
| T47 | F6-47 n18-19 (0109) | P23 | 2·3 | 23 | [?but on] → but on (+2) |
| T65 | F6-65 n9 (0110) | D17 | 1 | 1 | « 1 » confirme « Dalberg » (seul désaccord de la 2ᵉ lecture aveugle) ; « 17 » l'affaiblit (à signaler) |
| T69 | F6-69 n13 (0110) | D13 | 13 | 18 | mad[e] → made (+1) |
| TJ | 2 fév. J n6 (0106) | PJ | 17 | 1 7 | indem[ni]ties → indemnities (+1, 2 fév.) ; « through » reste § |

## Contrôles cachés (3), réponse connue, jamais exemples ni cibles
- K1 (D16) : `10`, F6-35 n20 (0109), « army » sûr.
- K2 (D13) : `13`, F6-69 n16 (0110), « Russia » sûr.
- K3 (D17) : `17`, F6-52 n20 (0110), « departments » sûr.
Un contrôle raté → rien n'est intégré ; on en parle avec Brice (sauf défaut de construction démontré, consigné).

## Gain possible
6 fév. (mesure du dépôt, lecture entière, 799 mots, 60 trous, 0,929) : au plus +7 mots (T21, T25, T35, T37, T69,
T47 ×2) → ≈ 0,938 ; part chiffrée seule 236/293 = 0,805 → 243/293 = 0,829. Le seuil de 95 % n'est PAS atteignable par
cette planche : la plupart des trous restants sont des fautes de Lee (« other wrong figure », 52 cas, et sauts de clé)
qu'aucune forme ne règle. 2 fév. : +1 mot (J) au plus. T01, T02, T65 : consolidation (propositions § et désaccord de la
seconde lecture), sans mot au compte. Les réponses s'appliquent à la transcription (nombres) ; re-décodage
(decode.py, errors.py) et recompte avant toute PR.
