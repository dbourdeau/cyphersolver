# LJS 51 key rebuild, fork run (27 Nov 2026)

Label for every key here: **provisional: learned from its own alignment on uncorrected segmentation.**

Tool: `rekey.py`, imported read-only (`run_fork.py`). Selection rule (agreed with the coordinating session): fit_check "fits", no by-eye
correction in the record, segmenter sign count on the cipher lines equal to the record's signs_total; plus the tashifi run as control.
Leave-one-line-out is not used as a verdict (short chains cannot cover their alphabet). Control = same procedure on 100 shuffles of the
same plaintext letters; "ctrl" gives mean / max.

| chain | signs | letters | classes | aligned | letter fit | ctrl fit mean / max | rasm purity | ctrl rasm mean / max | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 14v.7 | 778 | 770 | 18 | 0.97 | 0.76 | 0.18 / 0.19 | 0.94 | 0.24 / 0.27 | control reproduced (pilot: 93.6% rasm) |
| 6v.11 | 41 | 39 | 18 | 0.93 | 0.66 | 0.47 / 0.55 | 0.71 | 0.52 / 0.63 | above chance: key provisional |
| 20r.8 | 297 | 293 | 14 | 0.97 | 0.27 | 0.26 / 0.29 | 0.26 | 0.26 / 0.29 | at chance: no key |

Notes:
- 14v.7 reproduces the pilot (rasm purity 0.936 against a control max of 0.27), so the run itself is sound.
- 6v.11 (41 signs): letter fit 0.66 against shuffled mean 0.47, max 0.55: above every shuffle, but a 41-sign chain gives a partial key only.
- 20r.8 (297 signs): letter fit 0.27, inside the shuffle range. The record notes that the sign style changes at f. 21r l.1, so this "chain" is
  probably two (or more) alphabets, or its plaintext order differs from the cipher order. It needs splitting at f. 21r before a key can be tried.

## Skipped chains and why (62)

- 1r.2: fit_check not "fits": "no plaintext available"
- 1v.3: fit_check not "fits": "signs < letters: about 80 signs against 89 letters (ratio ~0.9) and 25 plaintex
- 2r.4: fit_check not "fits": "signs > letters (85 vs 78, ratio 1.09, 7 over; 18 dividers+1 = about 19 groups 
- 2v.3: fit_check not "fits": "signs > letters, nearly fits: 68 signs vs 65 letters (+3); dividers+1 = 18 grou
- 3r.7: segmenter count on the cipher lines (69) does not equal signs_total (80)
- 3v.12: fit_check not "fits": "signs < letters for the whole text: about 48 signs against 92 letters (ratio 0.
- 4r.9: by-eye correction in record
- 4v.4: segmenter count on the cipher lines (42) does not equal signs_total (38)
- 4v.8: fit_check not "fits": "signs > letters: 94 signs (66 on 4v + 28 on 5r) vs 80 letters (ratio 1.18, +14)
- 5r.12: segmenter count on the cipher lines (54) does not equal signs_total (52)
- 6r.11: fit_check not "fits": "signs > letters: 91 signs vs 82 letters (+9, ratio 1.11); dividers+1 = 21 group
- 7r.5: fit_check not "fits": "signs > letters: 51 signs vs 38 letters (ratio 1.34, +13); dividers+1 = 12 grou
- 7r.12: segmenter count on the cipher lines (98) does not equal signs_total (93)
- 7v.12: fit_check not "fits": "signs > letters: about 102 signs vs 85 letters (ratio 1.2, +17); dividers+1 = 2
- 8r.11: fit_check not "fits": "signs > letters: 88 signs vs 76 letters (ratio 1.16, +12); dividers+1 = 20 grou
- 8v.10: fit_check not "fits": "8v rows alone: 75 signs vs 75 letters (equal); with the 9r row: 83 vs 75 (+8, s
- 9r.7: segmenter count on the cipher lines (85) does not equal signs_total (76)
- 9v.3: segmenter count on the cipher lines (84) does not equal signs_total (83)
- 10r.2: fit_check not "fits": "signs > letters: 87 signs vs 77 letters (ratio 1.13, +10); dividers+1 = 18 grou
- 10v.1: fit_check not "fits": "nearly fits: 73 signs vs 77 letters when l.9 is included (-4), 62 for l.7-8 alo
- 10v.13: fit_check not "fits": "signs > letters: about 37 signs vs 34 letters (+3), dividers+1 = 12 groups vs 9
- 11r.5: segmenter count on the cipher lines (36) does not equal signs_total (33)
- 11r.10: fit_check not "fits": "signs > letters: 97 signs vs 84 letters (ratio 1.15, +13); dividers+1 = 25 grou
- 11v.11: fit_check not "fits": "signs < or about letters: 41 signs vs 44 letters (-3); dividers+1 = 15 groups v
- 12r.8: fit_check not "fits": "signs > letters: 98 signs vs 70 letters (ratio 1.4, +28); dividers+1 = 25 group
- 12v.8: segmenter count on the cipher lines (45) does not equal signs_total (40)
- 12v.11: fit_check not "fits": "nearly fits, if the candidate is right: 32 signs vs 36 letters for 13r l.5-6 (-
- 13r.11: fit_check not "fits": "signs > letters (43 vs 40, ratio 1.08); word groups 12 = plaintext words 12: th
- 13v.10: fit_check not "fits": "signs > letters (77 vs 71, ratio 1.08); word groups 22 vs plaintext words 20 (w
- 18r.11: fit_check not "fits": "signs > letters (133 vs 123, ratio 1.08); word groups 34 vs plaintext words 31:
- 19r.7: fit_check not "fits": "signs > letters (163 vs 145, ratio 1.12); word groups 38 vs plaintext words 35 
- 22r.1: fit_check not "fits": "signs > letters (171 vs 165, ratio 1.04, 6 more): close; word groups 34 vs plai
- 22v.9: by-eye correction in record
- 23r.9: fit_check not "fits": "signs > letters (132 vs 123, ratio 1.10); word groups 28 vs plaintext words 30:
- 23v.12: fit_check not "fits": "signs > letters (39 vs 35, ratio 1.08); word groups 11 vs plaintext words 8 (+3
- 24r.7: fit_check not "fits": "signs > letters (86 vs 73, ratio 1.18); word groups 18 = plaintext words 18: th
- 24v.6: by-eye correction in record
- 25r.4: fit_check not "fits": "signs > letters: segmenter 86 vs 81 letters (1.06); by eye 84 (two dotted divid
- 25v.4: fit_check not "fits": "segmenter 81 includes the 4 pieces of the Arabic heading ومن ذلك on l.4 and 2 d
- 26r.1: by-eye correction in record
- 26r.12: fit_check not "fits": "signs > letters: segmenter 88, corrected by eye 83 (the segmenter splits severa
- 26v.11: by-eye correction in record
- 27r.10: by-eye correction in record
- 27v.3: fit_check not "fits": "signs > letters: 77 vs 72 (1.07; 71 without the hamza of حماء); about 20-21 wor
- 28r.2: by-eye correction in record
- 28v.1: by-eye correction in record
- 29r.4: by-eye correction in record
- 29v.2: by-eye correction in record
- 30r.4: fit_check not "fits": "signs > letters, near fit: by eye 112 signs vs 109 letters (1.03), 23 dividers 
- 30v.7: fit_check not "fits": "no plaintext to check. Counts: segmenter 95 signs / 24 dividers; by eye 81 sign
- 31r.2: by-eye correction in record
- 31r.11: fit_check not "fits": "signs > letters, near fit: 59 signs by eye vs 56 letters (1.05); about 13 word 
- 31v.11: by-eye correction in record
- 32v.3: fit_check not "fits": "signs > letters: segmenter 77, by eye 79 counting each numeral of the doubled p
- 33r.4: by-eye correction in record
- 33v.6: by-eye correction in record
- 33v.12: by-eye correction in record
- 34r.8: by-eye correction in record
- 34v.6: fit_check not "fits": "signs > letters, near fit: 84 signs by eye (segmenter 72 on its lines plus page
- 35r.6: fit_check not "fits": "counts by eye: 85 signs counting the 8 '//' strokes as signs, 77 without them, 
- 35v.8: by-eye correction in record
- 36r.11: by-eye correction in record
