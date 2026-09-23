# Structure of the Indus texts (ICIT-derived corpus)

## S1 Numeral systems: do short, tiered and long strokes count the same things?

- short strokes (778 tokens before a non-numeral): 240 x69, 390 x52, 156 x40, 220 x35, 235 x34, 803 x29, 900 x29, 233 x22, 405 x17, 798 x17
- tiered strokes (161 tokens before a non-numeral): 220 x21, 390 x20, 585 x20, 740 x18, 840 x17, 575 x12, 405 x5, 255 x3, 407 x3, 151 x3
- long strokes (545 tokens before a non-numeral): 740 x63, 220 x56, 700 x50, 520 x48, 590 x20, 923 x14, 226 x13, 845 x13, 384 x10, 240 x9
- short vs long: Jensen-Shannon divergence of the following signs 0.519 bits; label permutations as large: 0 of 1000.
- values 1, 3, 4, 5 only (both pairs left out): short (352) before 390 x51, 156 x38, 900 x26, 220 x23, 405 x17, 407 x14; long (311) before 520 x48, 700 x41, 740 x14, 923 x14, 845 x13, 240 x9; divergence 0.592 bits, permutations as large 0 of 1000.
- among the 8 commonest nouns after each: short only ['156', '233', '235', '240', '390', '803', '900']; long only ['226', '520', '590', '700', '740', '845', '923']; both ['220'].

## S2 Counted nouns: signs read after a numeral more often than chance

| sign | after a numeral | expected | all occurrences as 2nd of a pair | share | values seen |
|---|---|---|---|---|---|
| 597 | 8 | 1.6 | 8 | 100% | [2] |
| 417 | 8 | 1.6 | 8 | 100% | [2] |
| 48 | 11 | 2.8 | 14 | 79% | [2] |
| 700 | 56 | 14.5 | 72 | 78% | [2, 3, 4, 6] |
| 384 | 12 | 3.2 | 16 | 75% | [1, 2, 3] |
| 585 | 23 | 6.6 | 33 | 70% | [3, 7] |
| 226 | 15 | 4.4 | 22 | 68% | [2, 3] |
| 156 | 50 | 15.9 | 79 | 63% | [1, 2, 3, 4, 5, 8] |
| 803 | 32 | 12.0 | 60 | 53% | [1, 2, 3, 12] |
| 900 | 29 | 12.8 | 64 | 45% | [1, 2, 3, 4, 5] |
| 840 | 27 | 12.2 | 61 | 44% | [2, 3, 6] |
| 140 | 19 | 8.6 | 43 | 44% | [2, 3, 5] |
| 923 | 15 | 6.8 | 34 | 44% | [3] |
| 220 | 112 | 51.6 | 257 | 44% | [1, 2, 3, 4, 6, 7, 12] |
| 575 | 14 | 6.6 | 33 | 42% | [1, 7] |
| 390 | 78 | 38.9 | 194 | 40% | [2, 3, 4, 5, 6, 7, 8] |

## S3 Endings and paradigms (Kober)

- signs that end a line in half or more of their occurrences (>= 30 tokens): 740 (894 of 1267, 71%), 400 (300 of 338, 89%), 520 (202 of 233, 87%), 90 (86 of 109, 79%), 156 (68 of 80, 85%), 151 (60 of 67, 90%), 700 (54 of 81, 67%), 407 (54 of 100, 54%), 527 (41 of 47, 87%), 154 (29 of 37, 78%)
- signs that begin a line in half or more of their occurrences: 817 (128 of 145), 820 (126 of 177), 861 (118 of 169), 3 (86 of 160), 920 (68 of 114), 503 (49 of 66), 692 (44 of 52), 501 (29 of 31), 5 (22 of 39), 416 (21 of 36)
- ending class used: 90 151 154 156 400 407 520 527 700 740 741 742 745. Stems (the line minus up to two final ending signs, at least two signs long) attested with two or more different endings: 58 of 1682 stems.
- endings that alternate on the same stem: 740 x41, 740 400 x23, (none) x16, 740 90 x11, 520 x7, 151 x6, 400 x4, 154 x4, 156 400 x3, 156 x2, 740 151 x2, 407 x2

| stem (reading order) | endings attested (count) |
|---|---|
| 840 32 | 740 x9; 740 400 x1; (none) x1 |
| 413 575 335 711 33 | 700 x8; 740 x1; (none) x1 |
| 255 435 | 156 400 x4; 156 x2; 154 x1 |
| 590 390 | 740 x2; 740 400 x2; 151 x1 |
| 32 220 | (none) x3; 740 90 x1; 740 x1 |
| 16 220 | (none) x2; 520 x2; 520 400 x1 |
| 809 809 | 740 x3; (none) x1; 740 90 x1 |
| 235 240 | 740 90 x2; 740 151 x1; 520 x1 |
| 240 100 | 740 400 x2; 740 151 x1; 740 x1 |
| 510 460 | 156 x1; 740 x1; 520 x1 |
| 861 2 176 | 151 x1; 740 x1; 740 90 x1 |
| 13 840 | 740 x7; 740 400 x1 |
| 605 760 | 740 400 x6; 740 x1 |
| 798 415 220 | 740 400 x5; 520 x1 |
| 3 220 | 740 x5; 520 x1 |
| 491 817 | 740 400 x3; 740 x2 |
| 33 33 | 520 x4; (none) x1 |
| 61 142 | 400 740 x4; 740 x1 |
| 468 806 | 154 x4; 154 400 x1 |
| 5 900 | 740 x4; 740 90 x1 |
| 4 390 | (none) x3; 400 x1 |
| 240 636 | 740 x3; 740 400 x1 |
| 3 140 100 | 740 x3; 740 400 x1 |
| 28 32 | 740 400 x3; 740 x1 |
| 831 892 | 400 x2; (none) x1 |

## S4 Name + formula on the copper tablets

Copper tablets: 149 objects, 49 distinct texts. Sign sequences (2-4 signs) found in 3 or more distinct texts, with what stands before them and the images of those tablets:

- **142 615 615** in 6 texts:
    - 905 32 597  [ 142 615 615 ]   (x6; images {'Othr': 5, '-': 1})
    - 744 760 95 595 1  [ 142 615 615 ]   (x2; images {'Bull1:W': 2})
    - 861 368 1  [ 142 615 615 ] 235 233 222 740  (x1; images {'Othr': 1})
    - 495 460 365 2 4 407 905 32 597  [ 142 615 615 ]   (x1; images {'Othr': 1})
    - 747 717 95 595 1  [ 142 615 615 ]   (x1; images {'Bull1:W': 1})
    - 904 32 597  [ 142 615 615 ]   (x1; images {'Comp': 1})
- **176 740** in 4 texts:
    - 806 233  [ 176 740 ]   (x2; images {'-': 1, 'Othr': 1})
    - 32 220  [ 176 740 ]   (x2; images {'-': 2})
    - 831 233  [ 176 740 ]   (x1; images {'Othr': 1})
    - 806 231  [ 176 740 ]   (x1; images {'Othr': 1})
- **100 740** in 4 texts:
    - 3 421 176  [ 100 740 ] 790  (x3; images {'Goat:8': 3})
    - 3 422 176  [ 100 740 ]   (x2; images {'-': 1, 'Othr': 1})
    - 3 233  [ 100 740 ]   (x1; images {'Comp': 1})
    - 590 405  [ 100 740 ] 790  (x1; images {'Loop': 1})
- **255 435 690 740** in 3 texts:
    - (nothing)  [ 255 435 690 740 ] 900 3 422  (x3; images {'Buff': 1, '-': 2})
    - (nothing)  [ 255 435 690 740 ] 900 1 3 423  (x1; images {'Gaur': 1})
    - (nothing)  [ 255 435 690 740 ] 900 1 3 424  (x1; images {'Buff': 1})
- **435 690 740 900** in 3 texts:
    - 255  [ 435 690 740 900 ] 3 422  (x3; images {'Buff': 1, '-': 2})
    - 255  [ 435 690 740 900 ] 1 3 423  (x1; images {'Gaur': 1})
    - 255  [ 435 690 740 900 ] 1 3 424  (x1; images {'Buff': 1})
- **597 142 615 615** in 3 texts:
    - 905 32  [ 597 142 615 615 ]   (x6; images {'Othr': 5, '-': 1})
    - 495 460 365 2 4 407 905 32  [ 597 142 615 615 ]   (x1; images {'Othr': 1})
    - 904 32  [ 597 142 615 615 ]   (x1; images {'Comp': 1})
- **32 597 142 615** in 3 texts:
    - 905  [ 32 597 142 615 ] 615  (x6; images {'Othr': 5, '-': 1})
    - 495 460 365 2 4 407 905  [ 32 597 142 615 ] 615  (x1; images {'Othr': 1})
    - 904  [ 32 597 142 615 ] 615  (x1; images {'Comp': 1})
- **1 142 615 615** in 3 texts:
    - 744 760 95 595  [ 1 142 615 615 ]   (x2; images {'Bull1:W': 2})
    - 861 368  [ 1 142 615 615 ] 235 233 222 740  (x1; images {'Othr': 1})
    - 747 717 95 595  [ 1 142 615 615 ]   (x1; images {'Bull1:W': 1})
- **33 923 740** in 3 texts:
    - 706  [ 33 923 740 ]   (x7; images {'Elep': 7})
    - 706  [ 33 923 740 ] 1  (x4; images {'Elep': 4})
    - 705  [ 33 923 740 ] 1  (x1; images {'Comp': 1})
- **235 233** in 3 texts:
    - (nothing)  [ 235 233 ] 222 740  (x4; images {'Othr': 2, 'Rhin': 2})
    - 806  [ 235 233 ] 705 33 585 407  (x3; images {'Comp': 2, '-': 1})
    - 861 368 1 142 615 615  [ 235 233 ] 222 740  (x1; images {'Othr': 1})
- **222 740** in 3 texts:
    - 235 233  [ 222 740 ]   (x4; images {'Othr': 2, 'Rhin': 2})
    - 861 368 1 142 615 615 235 233  [ 222 740 ]   (x1; images {'Othr': 1})
    - 235 220  [ 222 740 ]   (x1; images {'Othr': 1})
- **705 33** in 3 texts:
    - 235  [ 705 33 ] 845 407 321 407  (x12; images {'Hare': 12})
    - 806 235 233  [ 705 33 ] 585 407  (x3; images {'Comp': 2, '-': 1})
    - (nothing)  [ 705 33 ] 923 740 1  (x1; images {'Comp': 1})

## S4b The formula 845 (61) 407 and what precedes it

- 798 231 233 740 845 407 471 806 154   | before the formula: fish-series or 806 sign | 1 object(s): H-132 SEAL:R 
- 263 365 798 240 233 740 140 845 407   | before the formula: fish-series or 806 sign | 1 object(s): H-659 SEAL:R 
- 806 233 845 407   | before the formula: fish-series or 806 sign | 1 object(s): M-1953 SEAL:R 
- 798 240 845 63 407   | before the formula: fish-series or 806 sign | 1 object(s): 2481 TAB:C Unknown
- 861 2 240 923 101 740 140 845 407   | before the formula: fish-series or 806 sign | 1 object(s): M-7 SEAL:S Bull1:W
- 125 906 2 236 845 407 729 740   | before the formula: fish-series or 806 sign | 1 object(s): M-354 SEAL:R 
- 415 220 845 407   | before the formula: fish-series or 806 sign | 3 object(s): M-507 TAB:C Loop, M-508 TAB:C Loop, M-1456 TAB:C Loop
- 235 705 33 845 407 321 407   | before the formula: fish-series or 806 sign | 12 object(s): M-534 TAB:C Hare, M-535 TAB:C Hare, M-536 TAB:C Hare, M-537 TAB:C Hare
- 798 240 845 61 407   | before the formula: fish-series or 806 sign | 6 object(s): M-567 TAB:C Gaur, M-568 TAB:C Tigr, M-569 TAB:C , M-1515 TAB:C Othr
- 806 845 61 407 850 900 740   | before the formula: fish-series or 806 sign | 10 object(s): M-582 TAB:C Anth, M-583 TAB:C Anth, M-585 TAB:C Anth, M-586 TAB:C Anth

- distinct texts with the formula: 10; the phrase before it holds a fish-series sign or the leaf-in-oval 806 in 10. A random stretch of the same length from the corpus holds one with probability 0.27; binomial p of 10 or more: 1.8e-06.

## S5 Word segmentation by pair cohesion

Rule: cut between two signs unless the pair occurs 3+ times with PMI >= 2 bits (at least four times its chance rate). 2614 lines, 4046 cuts, 1208 distinct units; units of 2+ signs occurring 6+ times: 104.

| unit (reading order) | occurrences |
|---|---|
| 861 2 | 92 |
| 740 400 | 89 |
| 817 2 | 78 |
| 740 90 | 55 |
| 820 2 | 52 |
| 176 740 | 47 |
| 32 220 | 47 |
| 760 740 | 41 |
| 176 740 400 | 37 |
| 3 156 | 35 |
| 590 390 | 34 |
| 840 32 | 29 |
| 501 405 2 240 520 | 29 |
| 503 615 752 740 | 29 |
| 3 390 | 24 |
| 255 435 690 740 | 24 |
| 692 60 | 23 |
| 33 700 | 22 |
| 100 740 | 21 |
| 615 615 | 21 |
| 920 60 741 | 20 |
| 220 520 | 20 |
| 235 240 | 19 |
| 415 100 740 | 19 |
| 415 220 520 | 18 |
| 550 527 | 18 |
| 923 740 | 17 |
| 820 60 | 16 |
| 705 33 | 15 |
| 705 33 520 | 15 |
| 13 840 | 14 |
| 550 60 | 14 |
| 3 220 | 14 |
| 820 1 | 14 |
| 240 520 | 13 |
| 752 740 | 13 |
| 415 220 | 13 |
| 32 226 | 12 |
| 17 575 | 12 |
| 630 740 | 12 |
| 235 705 33 845 407 321 407 | 12 |
| 4 390 | 11 |
| 803 415 220 318 920 255 436 690 590 407 | 11 |
| 233 520 | 11 |
| 17 585 740 | 11 |
| 590 405 | 11 |
| 706 33 520 | 11 |
| 798 415 220 | 11 |
| 817 2 48 740 | 11 |
| 706 33 923 740 | 11 |
| 920 60 | 10 |
| 142 615 615 | 10 |
| 388 740 | 10 |
| 482 740 | 10 |
| 806 845 61 407 850 900 740 | 10 |
| 820 820 | 9 |
| 2 803 | 9 |
| 34 700 | 9 |
| 176 100 740 | 9 |
| 455 220 | 9 |

