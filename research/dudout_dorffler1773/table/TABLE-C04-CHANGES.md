# TABLE-C04 — changes from TABLE-C03 (feb40aca…), training evidence only (470, 475, 467, 468, 476), 2026-11-12
474 was not opened (no crop, no view) before TABLE-C04.json was frozen.

System (C03): 14-39 and 40-65 = two a…z sets (a b c d e f f g h i k l l m n o p q r s t u w x y z, 20 & 46 = f(f),
26 & 52 = l); 66-145 = 16 consonants × 5 vowels (b c d f g h k l m n p r s t w z × a e i o u); 146-231 words; 255+ names.

| group | C03 | C04 | evidence |
|---|---|---|---|
| 50 | ke | k | system (24→50); gezucket, keine ×2, aufdrückung, untergedrücket (475/468), geklaget (476 R-7) |
| 55 | on | o | system (29→55); mediation (467 R3), obsequio (476 R-7) |
| 57 | sey | q | system (31→57); « quidem » (476 R-3) |
| 69 | — | bo | system; Lubomirski ×2 (476 R-6, R-7), « bo » |
| 71 | — | ca | system; deprecation (476 L-2), kammer- (476 R-4) |
| 72 | — | ce | system; force (476 L-1), process (476 R-1) |
| 79, 89, 96, 141 | — | do, go, ka, za | system only (89 seen once under « original », gi; read as a likely 88/89 misreading: system kept) |
| 37, 63, 52 | — | x, x, l | system only |
| 208 | — | tion | affection, Machinationes, inthronisation, relationis, mediation, Confoederation, Constitution (training), deprecation, conspiration (476) |
| 290 | — | feld | « Feld-herr » 290.311 ×2 (476 L-1, L-5), homophone of 298 |
| 199 | — | oder | 476 L-2 « oder » |
| 224 | — | wolle | 476 R-1 « anfangen wolle » |
| 225 | — | wir | 476 R-7 « wird » (225.17) |
| 186, 198 | ? | removed | value unknown (was decoded as empty) |

Settled without table change (images re-read):
- « Posen » 470 R1 l.2: the group is **119.127.28** = po-se-n; the first 1 is the tall slanted stroke (same as the 1 of
  the 145 just before), under the P of the gloss. 19 = f stands.
- « vermessen » 470 R1 l.4: the image reads **129** (not 209): 129.107.59.127.(2)8 = so-me-s-se-n. Kept as written
  (clerk's slip or a 1/2 confusion of the encipherer); no change to 129 = so, 209 = ver.
- « ein recit » 467 R2 l.7: the image reads **131**.122.73.34 (not 231): kept as written (slip); no change.
- Kept against single 476 readings (training majority or system): 39 = z (Pfaltz ×3, Conferenz, aufgesetzt) though two
  476 readings give s; 90 = gu (Gulden, intrigues) though « Lubomirski » gives ki twice (likely 98 misread as 90);
  100 = lich (Königlichen ×2, deutlich, wirckung, endlich) though « mi » ×2 on 476 (100/108); 164 = ent.

In-sample check on 476 (now TRAINING; not a measure, not a verdict): measure.py gives 0.7641 with TABLE-C04 (0.7354
with TABLE-C03). The remaining loss is mostly our digit misreadings (0/8, 6/8, 5/6, 15/16, 40/48) and gloss reading.
