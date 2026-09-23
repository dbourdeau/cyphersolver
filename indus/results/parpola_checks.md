# Parpola 2005 against the ICIT-derived corpus

Corpus: 2536 objects (2508 South Asian), 11253 sign tokens after splitting fused repeats, 572 sign types.

## C1-C3 General statistics (pp. 36, 45, 49)
- mean signs per object: 4.44; median 4; longest 17 (p. 45: "the longest text is merely 26 signs"; p. 36: "on the average only five signs").
- longest objects: M-314 Mohenjo-daro (SEAL:S) 17 signs in 3 lines; H-1657 Harappa (SEAL:S) 13 signs in 1 lines; M-23 Mohenjo-daro (SEAL:S) 13 signs in 2 lines
- sign types (unsplit glyph ids): 590; occurring once: 198 = 34% (p. 36, Farmer et al.: "between 25 to 50 per cent of the around 400-600 different signs are attested only once").

## C4-C5 The most frequent sign and its doubling (p. 47)
- most frequent sign: 740 with 1267 tokens = 11.3% of all tokens (p. 47: "almost 10%"); next 2 (583), 400 (338).
- adjacent pairs in the corpus: 8639. Expected jar+jar under independent signs: 8639 x p^2 = 110. Observed: 1, at [('sealid 3889', 'Unknown', 'SEAL:C')].
- objects with the jar twice or more: 16; with the order shuffled inside each line the jar+jar pair would appear 4.4 times on average (max 10 in 500 shuffles).
    - H-811 Harappa TAB:B: 491 920 2 176 740 335 740 317
    - M-1792 Mohenjo-daro SEAL:S: 740 952 740 | 240 760 740
    - M-165 Mohenjo-daro SEAL:S: 32 390 741 1 760 740 | 194 740 817
    - M-1796 Mohenjo-daro SEAL:S: 861 455 740 840 32 740
    - M-495 Mohenjo-daro TAB:B: 741 904 740 820 32 17 904 415 100 740
    - M-626 Mohenjo-daro SEAL:S: 692 60 255 435 690 740 692 60 803 740 | 125 374 842
    - M-638 Mohenjo-daro SEAL:S: 590 740 745 235 240 55 482 740
    - M-644 Mohenjo-daro SEAL:S: 370 90 817 2 240 740 17 585 740
    - M-665 Mohenjo-daro SEAL:S: 575 374 2 350 460 798 740 | 637 740 871
    - M-782 Mohenjo-daro SEAL:S: 621 740 1 912 740
    - M-980 Mohenjo-daro SEAL:S: 415 100 740 93 435 61 550 615 615 740
    - M-1202 Mohenjo-daro SEAL:S: 840 257 740 415 100 740 | 790
    - M-1429 Mohenjo-daro TAB:B: 803 3 220 740 809 809 740 90
    - Sktd-2 Surkotada SEAL:S: 740 803 390 60 740
    - sealid 3889 Unknown SEAL:C: 467 550 1 740 740
    - sealid 4221 Dholavira SEAL:S: 590 740 741 234 760 740

## C6 Indus seals found in West Asia: typical or unique sequences? (p. 47)
Model: bigram language model (interpolated with unigram) trained on the 2508 South Asian objects, each home object scored leave-one-out. "order" = bigram bits minus unigram bits: negative when the signs stand in their usual order, positive when common signs stand in unusual order. Percentile = share of home objects scoring lower.

| object | site | type | signs (reading order) | bits/sign | pct | order | pct |
|---|---|---|---|---|---|---|---|
| sealid 160 | Hajar | TAB:I | 117 615 615 | 6.83 | 88 | -0.42 | 78 |
| sealid 1971 | Kish | SEAL:S | 416 840 60 3 220 590 390 740 | 4.54 | 51 | -1.39 | 51 |
| sealid 2153 | Luristan | SEAL:C | 91 840 413 831 | 7.82 | 95 | +0.01 | 87 |
| sealid 3863 | Qala'at al-Bahrain | SEAL:C | 160 90 55 60 190 | 7.54 | 93 | -0.22 | 82 |
| sealid 3865 | Ra's al-Junayz | POT:T:g | 4 405 | 4.48 | 50 | -1.40 | 50 |
| sealid 3882 | Susa | SEAL:CY | 924 1 319 31 55 2 150 416 | 8.90 | 98 | +0.68 | 96 |
| sealid 3884 | Tell Umma | TAG:L | 127 705 2 4 390 | 6.16 | 80 | -0.64 | 74 |
| sealid 3889 | Unknown | SEAL:C | 467 550 1 740 740 | 5.89 | 76 | +0.13 | 89 |
| sealid 3897 | Ur | SEAL:C | 528 220 924 340 93 | 10.26 | 100 | +0.69 | 96 |
| sealid 3898 | Ur | SEAL:C | 415 803 1 328 4 2 | 8.11 | 96 | +1.04 | 98 |
| sealid 4173 | Salut | SEAL:S | 595 278 2 4 392 | 8.67 | 98 | +0.60 | 95 |
| sealid 5227 | Karzakan | SEAL:C | 91 31 455 220 | 6.41 | 84 | -0.34 | 80 |
| sealid 5228 | Karzakan | SEAL:C | 91 32 1 33 | 6.43 | 84 | +0.25 | 90 |
| sealid 5229 | Saar | SEAL:C | 55 220 91 1 93 31 | 7.71 | 94 | +0.42 | 93 |

- other (3): median percentile, bits/sign 80, order 74
- square (2): median percentile, bits/sign 98, order 95
- round/cylinder (9): median percentile, bits/sign 94, order 90

## C7 Share of the fish signs (p. 52)
- fish series (219 220 221 222 224 226 228 229 230 231 232 233 234 235 236 240 241 242 243 244): 695 of 7165 tokens on seals = 9.7% ("almost every tenth sign"); plain fish 220: 296; roof-fish 235: 186.

## C8 Numeral + fish (p. 54)
- numerals read immediately before the plain fish, by value: 1: 5, 2: 62, 3: 19, 4: 6, 6: 9, 7: 1, 12: 8
- whole inscriptions that are numeral + plain fish: B-3 Banawali SEAL:S (4 strokes); 151 Farmana SEAL:S (2 strokes); H-1086 Harappa POT:T:s (6 strokes); H-1028 Harappa SEAL:S (6 strokes); H-1737 Harappa POT:T:s (3 strokes); H-1736 Harappa POT:T:s (3 strokes); H-9 Harappa SEAL:S (7 strokes); H-1084 Harappa POT:T:s (2 strokes)
- signs most often read right after a numeral: 220 (110), 740 (84), 240 (77), 390 (72), 520 (51), 156 (48), 32 (47), 700 (47), 235 (37), 3 (32), 803 (32), 590 (31)

## C9-C13 Fig, crab and their combinations (pp. 55-59)
- fig 772 773 776 783 784 785 786: 28 tokens
- fig+crab ligature 777 778 782: 7 tokens
- crab 794 798: 110 tokens
- signs read right after the fig: {'740': 19, '4': 3, '32': 1, '895': 1, '220': 1, '530': 1, '233': 1}
    - fig+crab on L-11 Lothal SEAL:S: 817 2 778 255 435 705 590
    - fig+crab on M-603 Mohenjo-daro TAB:C: 777
    - fig+crab on M-604 Mohenjo-daro TAB:C: 777
    - fig+crab on M-1555 Mohenjo-daro TAB:C: 777
    - fig+crab on M-1556 Mohenjo-daro TAB:C: 777
    - fig+crab on M-1557 Mohenjo-daro TAB:C: 777
    - fig+crab on M-1558 Mohenjo-daro TAB:C: 777
- copper tablets (TAB:C), 149 objects; the Fig. 4 inscription (read 806 845 61 407 850 900 740) is on 10, the fig+crab sign alone on 6 (Fig. 4: 14 and 7 examples). Tablets sharing the tail 845 (61) 407:
    - 12 x 235 705 33 845 407 321 407
    - 10 x 806 845 61 407 850 900 740
    - 6 x 798 240 845 61 407
    - 3 x 415 220 845 407
    - 1 x 798 240 845 63 407
- crab read immediately before a fish sign: 28 times [('H-423', '798', '240'), ('H-1922', '798', '240'), ('H-1705', '798', '240'), ('H-26', '798', '240'), ('H-44', '798', '235'), ('H-132', '798', '231'), ('H-248', '798', '240'), ('H-659', '798', '240'), ('H-660', '798', '240'), ('M-1972', '798', '235'), ('2481', '798', '240'), ('M-50', '798', '240'), ('M-57', '798', '231'), ('M-121', '798', '233'), ('M-157', '798', '233'), ('M-370', '798', '233'), ('M-567', '798', '240'), ('M-568', '798', '240'), ('M-569', '798', '240'), ('M-629', '798', '240'), ('M-714', '798', '233'), ('M-793', '798', '240'), ('M-815', '798', '233'), ('M-1320', '798', '240'), ('M-1515', '798', '240'), ('M-1516', '798', '240'), ('M-1517', '798', '240'), ('Ns-60', '798', '236')] (p. 58: "three times")
- crab tokens with a fish sign immediately beside them: 48 of 110 (44%); with the signs shuffled inside each line: 28.7 expected, exceeded in 0 of 500 shuffles (p. 57: "usually occurs in the immediate vicinity of the fish signs").

## C14-C15 Eye + eye and water + eye (pp. 60-61)
- eye + eye: 9; [(('809', '809'), 9)]
- water + eye: 3; [(('904', '832'), 3)]
- water + anything: 33; [(('904', '740'), 17), (('904', '158'), 4), (('904', '32'), 3), (('904', '832'), 3), (('904', '31'), 1), (('904', '705'), 1)]
- inscriptions ending water + eye: M-205 (820 1 904 832), M-370 (806 798 233 388 444 740 904 832)

## C16 Sign repetition within one inscription (pp. 36-38)
Share of inscriptions (one line, excluding numerals) with a sign occurring twice, observed vs. the same lengths drawn at random from the corpus sign frequencies (2,000 draws per inscription). A phonetic script roughly follows the random line (p. 36-37, Farmer et al.); a logo-syllabic seal legend need not (Parpola).

| length | inscriptions | observed repeat | random repeat |
|---|---|---|---|
| 2 | 483 | 1.0% | 2.0% |
| 3 | 613 | 5.1% | 6.5% |
| 4 | 537 | 5.2% | 13.8% |
| 5 | 362 | 9.9% | 20.6% |
| 6 | 186 | 17.7% | 29.4% |
| 7 | 93 | 25.8% | 36.2% |
| 8 | 33 | 12.1% | 46.5% |
| 9 | 17 | 29.4% | 52.5% |
| 10+ | 21 | 14.3% | 60.8% |

## C17 Are the proposed compounds real units? (PMI against a within-line shuffle)
| pair (reading order) | observed | expected | PMI (bits) | shuffles >= observed |
|---|---|---|---|---|
| 6 + fish (aru-min, Pleiades) | 9 | 1.0 | 3.13 | 0 / 300 |
| 7 + fish (elu-min, Ursa Major) | 1 | 1.6 | -0.71 | 225 / 300 |
| any numeral + fish | 110 | 51.5 | 1.09 | 0 / 300 |
| any numeral + pot | 47 | 12.6 | 1.90 | 0 / 300 |
| fig + fish (vata-min, north star) | 1 | 0.8 | 0.29 | 151 / 300 |
| crab + fish series (kon-min) | 28 | 10.2 | 1.45 | 0 / 300 |
| eye + eye (kan-kani, overseer) | 9 | 0.1 | 6.54 | 1 / 300 |
| water + eye (nir-k-kanti) | 3 | 0.1 | 4.86 | 0 / 300 |
