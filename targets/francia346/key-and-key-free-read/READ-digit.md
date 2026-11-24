# Francia 346, the later digit records: a read with our frozen key

> Paths and working labels removed on 13 November 2026; no number and no rule changed.

**A read with our frozen key, found from the ciphertext alone; not yet checked against the published key.** Every number here is real unless it says "twin".

Written on 12 November 2026, from 16:29 (UTC−3). Reviewed before the freeze; final at 17:00.

**Credit.** DECODE, records R5625, R5626, R5635 to R5637, R5640, R5642, R5643, R5645 to R5659. The archive is the Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346. DECODE is the database of historical ciphers of the DECRYPT project. Use is for research only. Nobody may publish or redistribute the DECODE images. This read opened no image.

**The transcription.** It is a machine transcription of the DECODE images, made in my pipeline: a draft, a source check and a reconciliation for each page. Nobody verified it.

## What this is

- **The key:** the earlier key-free work's frozen key (frozen at 01:27 on 12 November), pool "one2", column "shown". 69 of 80 codes show a letter. 11 codes show `·`.
- **The cut:** H6. A lone 6 is a word space. A lone 2 is a null and is dropped. The other digits form 80 pair codes.
- **The parse:** the earlier key-free work's unit model of the cut, rebuilt from its pool "one2" input. It gives the earlier key-free work's saved parse exactly. Here it runs by Viterbi only.
- **No fit.** No start, no EM step and no change of key, cut, role or rule.
- **The pages:** all 35 pages with cipher rows, in 22 records. R5625 has no cipher row.
- **The declaration:** `DECLARE.md`, written at 16:12 before any count on a new page.
- **The display:** `·` marks an escape, a mask or a code that the key hides. `|` marks a cleartext break. `/` marks a page end.

## The numbers (real)

| Record | Cipher pages (gate fails) | Pair tokens | Share shown | Hidden | Escapes | Masks | P5 runs | Odd runs | P5 | One-key reading A | Reading B |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| R5626 | 1 (0) | 723 | 0.923 | 56 | 27 | 189 | 13 | 4 | 0.308 | fits | fits |
| R5635 | 1 (0) | 474 | 0.928 | 34 | 10 | 11 | 18 | 3 | 0.167 | fits | fits |
| R5636 | 2 (0) | 1,280 | 0.920 | 103 | 25 | 37 | 48 | 14 | 0.292 | fits | fits |
| R5637 | 2 (0) | 968 | 0.911 | 86 | 17 | 19 | 54 | 9 | 0.167 | fits | fits |
| R5640 | 1 (0) | 793 | 0.880 | 95 | 5 | 1 | 19 | 4 | 0.211 | fits | fits |
| R5642 | 2 (1) | 768 | 0.855 | 111 | 20 | 14 | 56 | 31 | 0.554 | differs | differs |
| R5643 | 2 (0) | 46 | 0.870 | 6 | 4 | 40 | 1 | 1 | 1.000 | fits | fits |
| R5645 | 1 (0) | 238 | 0.916 | 20 | 5 | 7 | 2 | 0 | 0.000 | differs | differs |
| R5646 | 2 (1) | 990 | 0.923 | 76 | 28 | 18 | 43 | 18 | 0.419 | fits | fits |
| R5647 | 1 (0) | 72 | 0.847 | 11 | 4 | 14 | 0 | – | – | fits | not decided |
| R5648 | 2 (0) | 1,019 | 0.935 | 66 | 22 | 41 | 36 | 10 | 0.278 | fits | fits |
| R5649 | 1 (0) | 443 | 0.948 | 23 | 10 | 5 | 15 | 6 | 0.400 | differs | differs |
| R5650 | 2 (0) | 874 | 0.919 | 71 | 26 | 31 | 24 | 6 | 0.250 | fits | fits |
| R5651 | 2 (0) | 1,208 | 0.922 | 94 | 53 | 107 | 22 | 9 | 0.409 | differs | not decided |
| R5652 | 2 (0) | 699 | 0.920 | 56 | 20 | 10 | 17 | 6 | 0.353 | differs | differs |
| R5653 | 1 (0) | 188 | 0.926 | 14 | 3 | 4 | 11 | 2 | 0.182 | fits | fits |
| R5654 | 1 (0) | 249 | 0.924 | 19 | 4 | 1 | 6 | 3 | 0.500 | differs | fits |
| R5655 | 2 (1) | 645 | 0.927 | 47 | 14 | 97 | 15 | 2 | 0.133 | fits | fits |
| R5656 | 1 (1) | 395 | 0.835 | 65 | 13 | 69 | 34 | 19 | 0.559 | out (gate) | out (gate) |
| R5657 | 2 (2) | 681 | 0.874 | 86 | 37 | 32 | 110 | 64 | 0.582 | out (gate) | out (gate) |
| R5658 | 3 (1) | 116 | 0.922 | 9 | 5 | 58 | 12 | 7 | 0.583 | out (gate) | out (gate) |
| R5659 | 1 (1) | 27 | 0.815 | 5 | 3 | 22 | 4 | 2 | 0.500 | out (gate) | out (gate) |
| **All** | **35 (8)** | **12,896** | **0.911** | **1153** | **355** | **827** | **560** | **220** | **0.393** | | |

- Records that fit (reading A), pooled: share shown 0.918 on 8,072 pair tokens (12 records).

- **Share shown:** 0.911 of 12,896 pair tokens. On each record, it is 0.815 to 0.948.
- **The .80 rule:** on the 12 records that fit, pooled, the share shown is 0.918 of 8,072 pair tokens. This is above .80, so I propose no new fit.
  - That pool holds all pages of those records, with the failed pages 033 and 089.
  - On their pages that pass the gate only, the share is also 0.918 (6,861 of 7,474).
- **Tokens that the key does not show:** 1,153 hidden tokens (the 11 hidden codes), 355 escapes and 827 masks.
- **Pair types outside the key:** 0. The key holds all 80 pair codes of the cut, so this is a check only.
- **Three-digit codes:** the frozen cut has none, by construction. The key-free proxy is the earlier key-free work's P5 (the odd share of the runs between two 6 signs that hold no 2):
  - all 35 pages: 0.393 on 560 runs;
  - the 27 pages that pass the gate: 0.267 on 329 runs;
  - the earlier key-free work, earlier split: 0.258 on 260 runs; the pilot: 0.130;
  - the three pages with the mark of the 8-to-6 misreading (020, 094 and 098) give 0.549 to 0.573;
  - the other pages that fail the gate give 0.500 to 0.714 on 4 to 20 runs, or have no run;
  - so P5 cannot tell three-digit codes from lone digits or misread digits.

## The page gate and the suspect rules (real)

| Page | Digits | Share of 6 | Share of 8 | P5 runs | P5 | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 006_154r_R5626_P5 | 1,573 | 0.055 | 0.099 | 13 | 0.308 | passes |
| 008_205r_R5635_P1 | 1,077 | 0.074 | 0.121 | 18 | 0.167 | passes |
| 011_211r_R5636_P4 | 1,250 | 0.067 | 0.106 | 18 | 0.333 | passes |
| 012_211v_R5636_P3 | 1,586 | 0.074 | 0.118 | 30 | 0.267 | passes |
| 014_213r_R5637_P3 | 1,596 | 0.080 | 0.096 | 41 | 0.146 | passes |
| 015_213v_R5637_P1 | 558 | 0.082 | 0.082 | 13 | 0.231 | passes |
| 017_237v_R5640_P2 | 1,723 | 0.070 | 0.106 | 19 | 0.211 | passes |
| 020_246r_R5642_P6 | 1,530 | 0.114 | 0.040 | 51 | 0.549 | **fails** |
| 021_246v_R5642_P3 | 226 | 0.097 | 0.053 | 5 | 0.600 | passes |
| 024_249r_R5643_P1 | 0 | 0.000 | 0.000 | 0 | – | passes |
| 025_249v_R5643_P3 | 113 | 0.097 | 0.044 | 1 | 1.000 | passes |
| 029_261r_R5645_P2 | 508 | 0.045 | 0.122 | 2 | 0.000 | passes |
| 033_268r_R5646_P3 | 1,260 | 0.066 | 0.081 | 20 | 0.600 | **fails** |
| 034_268v_R5646_P4 | 898 | 0.071 | 0.088 | 23 | 0.261 | passes |
| 038_272r_R5647_P2 | 168 | 0.065 | 0.107 | 0 | – | passes |
| 042_279r_R5648_P3 | 1,306 | 0.080 | 0.094 | 20 | 0.300 | passes |
| 043_279v_R5648_P6 | 943 | 0.074 | 0.102 | 16 | 0.250 | passes |
| 046_281r_R5649_P1 | 955 | 0.066 | 0.103 | 15 | 0.400 | passes |
| 054_288r_R5650_P2 | 1,362 | 0.068 | 0.091 | 12 | 0.250 | passes |
| 055_288v_R5650_P6 | 556 | 0.065 | 0.095 | 12 | 0.250 | passes |
| 062_297r_R5651_P3 | 1,504 | 0.064 | 0.099 | 15 | 0.333 | passes |
| 063_297v_R5651_P8 | 1,127 | 0.065 | 0.077 | 7 | 0.571 | passes |
| 068_303r_R5652_P4 | 1,199 | 0.066 | 0.107 | 13 | 0.231 | passes |
| 069_303v_R5652_P8 | 314 | 0.061 | 0.118 | 4 | 0.750 | passes |
| 076_310r_R5653_P5 | 406 | 0.074 | 0.096 | 11 | 0.182 | passes |
| 082_315r_R5654_P4 | 537 | 0.060 | 0.108 | 6 | 0.500 | passes |
| 088_323r_R5655_P5 | 1,367 | 0.068 | 0.089 | 15 | 0.133 | passes |
| 089_323v_R5655_P6 | 49 | 0.102 | 0.204 | 0 | – | **fails** |
| 094_337r_R5656_P5 | 979 | 0.104 | 0.056 | 34 | 0.559 | **fails** |
| 098_342r_R5657_P4 | 1,501 | 0.146 | 0.029 | 103 | 0.573 | **fails** |
| 099_342v_R5657_P5 | 119 | 0.151 | 0.059 | 7 | 0.714 | **fails** |
| 102_344r_R5658_P1 | 0 | 0.000 | 0.000 | 0 | – | passes |
| 103_344v_R5658_P2 | 0 | 0.000 | 0.000 | 0 | – | passes |
| 104_345r_R5658_P3 | 284 | 0.102 | 0.063 | 12 | 0.583 | **fails** |
| 110_351r_R5659_P7 | 69 | 0.174 | 0.087 | 4 | 0.500 | **fails** |

The suspect rules (the earlier key-free work) masked these stretches:

| Record | Rule | Page | Row |
| --- | ---: | --- | --- |
| R5643 | 1 | 025_249v_R5643_P3 | C11 |
| R5645 | 1 | 029_261r_R5645_P2 | C11 |
| R5646 | 1 | 033_268r_R5646_P3 | C17 |
| R5647 | 1 | 038_272r_R5647_P2 | C05 |
| R5648 | 1 | 043_279v_R5648_P6 | C10 |
| R5656 | 2 | 094_337r_R5656_P5 | C06 |
| R5658 | 1 | 104_345r_R5658_P3 | C05 |

- **8 pages fail the earlier key-free work's gate.** They are read below, but read them with care.
  - Pages 020, 094 and 098 have a high share of 6 and a low share of 8. This is the pilot's 8-to-6 misreading.
  - Page 033 has P5 0.600 on exactly 20 runs. It passed in the earlier split.
  - Pages 089, 099, 104 and 110 are small, and their share of 6 is above 0.10.
- **So four records have no page that passes with a read digit.**
  - R5656, R5657 and R5659 have no page that passes.
  - R5658's pages 102 and 103 pass, but they hold no read digit. Its page 104 fails.
  - The read of these four records is the least sure.
- Pages 024, 102 and 103 hold cipher rows, but the source reads no sign in them.

## The one-key check (real code counts; twins as the control)

### declared

- Records without tokens: R5658.
- Twin slots with p below 0.05 (twin): test A 1 of 108; test B 7 of 108.

| Record | Tokens | A excess | A p | Twin envelope (A) | Reading A | B excess | B p | Twin envelope (B) | Reading B | Power, a quarter relabelled |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- | ---: |
| R5626 | 823 | +0.067 | 0.061 | +0.040 | fits | +0.063 | 0.072 | +0.075 | fits | 0.98 |
| R5635 | 593 | -0.161 | 1.000 | +0.010 | fits | -0.207 | 1.000 | +0.066 | fits | 0.36 |
| R5636 | 1,531 | -0.067 | 0.992 | +0.012 | fits | -0.081 | 0.996 | +0.044 | fits | 0.66 |
| R5637 | 1,169 | -0.081 | 0.991 | -0.013 | fits | -0.144 | 1.000 | +0.018 | fits | 0.73 |
| R5640 | 925 | -0.004 | 0.566 | +0.001 | fits | -0.035 | 0.817 | +0.034 | fits | 0.74 |
| R5642 | 119 | +0.277 | 0.012 | +0.143 | differs | +0.360 | 0.002 | +0.247 | differs | 0.95 |
| R5643 | 59 | +0.092 | 0.283 | +0.288 | fits | +0.101 | 0.266 | +0.414 | fits | 0.46 |
| R5645 | 262 | +0.229 | 0.006 | +0.055 | differs | +0.219 | 0.001 | +0.108 | differs | 0.99 |
| R5646 | 475 | +0.047 | 0.199 | +0.011 | fits | +0.052 | 0.201 | +0.042 | fits | 0.82 |
| R5647 | 88 | +0.195 | 0.063 | +0.508 | fits | +0.252 | 0.030 | +0.484 | not decided | 0.76 |
| R5648 | 1,205 | +0.025 | 0.246 | +0.018 | fits | -0.007 | 0.584 | +0.023 | fits | 0.91 |
| R5649 | 502 | +0.129 | 0.009 | +0.058 | differs | +0.131 | 0.007 | +0.088 | differs | 1.00 |
| R5650 | 1,018 | +0.038 | 0.165 | +0.038 | fits | +0.022 | 0.295 | +0.052 | fits | 0.93 |
| R5651 | 1,370 | +0.059 | 0.031 | +0.002 | differs | +0.069 | 0.011 | +0.078 | not decided | 0.92 |
| R5652 | 794 | +0.133 | 0.001 | +0.019 | differs | +0.132 | 0.004 | +0.050 | differs | 1.00 |
| R5653 | 215 | +0.028 | 0.372 | +0.091 | fits | +0.035 | 0.346 | +0.093 | fits | 0.74 |
| R5654 | 284 | +0.150 | 0.020 | +0.086 | differs | +0.112 | 0.063 | +0.128 | fits | 0.97 |
| R5655 | 730 | +0.021 | 0.343 | +0.007 | fits | +0.022 | 0.320 | +0.073 | fits | 0.88 |

### all pages

- Records without tokens: none.
- Twin slots with p below 0.05 (twin): test A 4 of 132; test B 7 of 132.

| Record | Tokens | A excess | A p | Twin envelope (A) | Reading A | B excess | B p | Twin envelope (B) | Reading B |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| R5626 | 823 | +0.071 | 0.044 | +0.015 | differs | +0.076 | 0.044 | +0.050 | differs |
| R5635 | 593 | -0.164 | 0.999 | +0.016 | fits | -0.211 | 1.000 | +0.068 | fits |
| R5636 | 1,531 | -0.064 | 0.992 | -0.019 | fits | -0.084 | 0.996 | -0.012 | fits |
| R5637 | 1,169 | -0.081 | 0.992 | +0.021 | fits | -0.156 | 1.000 | +0.012 | fits |
| R5640 | 925 | -0.006 | 0.550 | +0.016 | fits | -0.033 | 0.803 | +0.047 | fits |
| R5642 | 968 | +0.170 | 0.001 | +0.020 | differs | +0.238 | 0.001 | +0.047 | differs |
| R5643 | 59 | +0.095 | 0.269 | +0.509 | fits | +0.088 | 0.312 | +0.662 | fits |
| R5645 | 262 | +0.225 | 0.001 | +0.042 | differs | +0.246 | 0.002 | +0.129 | differs |
| R5646 | 1,135 | +0.085 | 0.007 | -0.028 | differs | +0.108 | 0.002 | -0.010 | differs |
| R5647 | 88 | +0.204 | 0.075 | +0.179 | fits | +0.230 | 0.048 | +0.270 | not decided |
| R5648 | 1,205 | +0.023 | 0.243 | +0.033 | fits | -0.009 | 0.606 | +0.027 | fits |
| R5649 | 502 | +0.128 | 0.006 | +0.061 | differs | +0.149 | 0.007 | +0.051 | differs |
| R5650 | 1,018 | +0.038 | 0.168 | +0.066 | fits | +0.040 | 0.174 | +0.066 | fits |
| R5651 | 1,370 | +0.057 | 0.036 | +0.081 | not decided | +0.086 | 0.008 | +0.109 | not decided |
| R5652 | 794 | +0.128 | 0.002 | +0.054 | differs | +0.153 | 0.001 | +0.094 | differs |
| R5653 | 215 | +0.034 | 0.347 | +0.020 | fits | +0.048 | 0.299 | +0.074 | fits |
| R5654 | 284 | +0.151 | 0.013 | +0.080 | differs | +0.115 | 0.064 | +0.105 | fits |
| R5655 | 757 | +0.029 | 0.260 | +0.015 | fits | +0.043 | 0.173 | +0.017 | fits |
| R5656 | 508 | -0.070 | 0.895 | +0.022 | fits | -0.128 | 0.989 | +0.070 | fits |
| R5657 | 902 | -0.088 | 0.981 | +0.020 | fits | -0.150 | 1.000 | +0.108 | fits |
| R5658 | 158 | -0.283 | 0.999 | +0.084 | fits | -0.442 | 1.000 | +0.135 | fits |
| R5659 | 39 | -0.301 | 0.922 | +0.222 | fits | -0.317 | 0.941 | +0.279 | fits |

### old split

- Records without tokens: none.
- Twin slots with p below 0.05 (twin): test A 2 of 84; test B 5 of 84.

| Record | Tokens | A excess | A p | Twin envelope (A) | Reading A | B excess | B p | Twin envelope (B) | Reading B |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| R5626 | 818 | +0.056 | 0.085 | +0.008 | fits | +0.071 | 0.056 | +0.029 | fits |
| R5635 | 551 | -0.148 | 0.997 | +0.079 | fits | -0.201 | 1.000 | +0.098 | fits |
| R5636 | 1,530 | -0.069 | 0.990 | +0.019 | fits | -0.076 | 0.997 | +0.023 | fits |
| R5637 | 1,123 | -0.099 | 0.996 | +0.023 | fits | -0.171 | 1.000 | +0.040 | fits |
| R5640 | 925 | -0.006 | 0.569 | +0.015 | fits | -0.023 | 0.695 | +0.025 | fits |
| R5642 | 119 | +0.280 | 0.008 | +0.069 | differs | +0.369 | 0.002 | +0.146 | differs |
| R5643 | 59 | +0.096 | 0.282 | +0.564 | fits | +0.103 | 0.272 | +0.632 | fits |
| R5645 | 244 | +0.191 | 0.008 | +0.032 | differs | +0.214 | 0.003 | +0.088 | differs |
| R5646 | 1,103 | +0.074 | 0.017 | +0.043 | differs | +0.108 | 0.003 | +0.033 | differs |
| R5647 | 87 | +0.207 | 0.061 | +0.149 | fits | +0.250 | 0.037 | +0.135 | differs |
| R5648 | 1,188 | -0.001 | 0.521 | -0.014 | fits | -0.024 | 0.756 | -0.010 | fits |
| R5649 | 500 | +0.127 | 0.010 | +0.062 | differs | +0.157 | 0.007 | +0.075 | differs |
| R5650 | 996 | +0.070 | 0.033 | +0.022 | differs | +0.084 | 0.018 | +0.023 | differs |
| R5651 | 722 | +0.111 | 0.011 | +0.081 | differs | +0.149 | 0.001 | +0.083 | differs |

### What the check says

- **Declared set (the pages that pass the gate): 18 records.**
  - 12 fit the pilot's code counts: R5626, R5635, R5636, R5637, R5640, R5643, R5646, R5647, R5648, R5650, R5653 and R5655.
  - 6 differ: R5642, R5645, R5649, R5651, R5652 and R5654.
  - R5656, R5657, R5658 and R5659 are out, because no page of theirs passes the gate with tokens.
- **The differences are small.** The six show 0.059 to 0.277 bits per token over the null.
  - In the earlier key-free work's report, a full change of key gave 0.86 to 1.00 on the records of the earlier split.
  - In the same report, 5% to 10% token noise gave about 0.05 to 0.13. R5642 (0.277) and R5645 (0.229) lie above that.
  - One key with transcription noise stays possible. These tests do not show it: the control twins carry masks but no misread digits.
  - A second key with a similar frequency profile is not excluded.
- **Reading B** (each record against the other new records) agrees on 15 of 18 records. R5654 fits there. R5647 and R5651 are "not decided".
- **Near the bar:** R5651 differs by 0.059 over an envelope of 0.002. R5626 fits with p 0.061. A small change in the text or in the random draws can move these.
- **Power:** with a quarter of a record's code types changed, test A gives p below 0.05 in 36% (R5635) to 100% of draws. Seven records are under 0.80: R5635, R5636, R5637, R5640, R5643, R5647 and R5653. "Fits" means "not shown to differ".
- **The limits of that power (a reviewer's point):**
  - it counts only p below 0.05, not the twin envelope of the full reading;
  - the change can merge code types, and it can touch the lone 6 and lone 2;
  - so it is one count experiment, not the measured power of the reading rule.
- **A limit of the twin control (a reviewer's point):** the frozen unit model was fitted on text that holds eight of these records in their earlier form. In the twins, the new slots get fresh text that the twin's unit model did not see. So the envelopes match sizes, masks and breaks, but not that overlap.
- **All pages, as a report:** with the gate ignored, the four gate-only records fit (negative excess).
  - R5646 then differs, because its page 033 enters.
  - R5626 then differs with the same tokens: its p moves from 0.061 to 0.044 with other random draws, and its twin envelope changes. So R5626 sits on the bar.
- **The old split, as a report:** with the frozen parse, the earlier split gives the earlier key-free work's reading A exactly. Six differ: R5642, R5645, R5646, R5649, R5650 and R5651.
- **What the newer text changes:** R5646 now fits, because only its page 034 passes the gate. R5650 now fits: p 0.165, where the earlier split gave 0.033. R5652 and R5654 are new records, and both differ.

## How the newer text changes the earlier key-free work's read (records R5626 to R5651)

| Record | Key in the earlier key-free work read | Pair tokens (old / new) | Share shown (old / new) | Old letters matched by alignment |
| --- | --- | --- | --- | ---: |
| R5626 | pool one2 | 716 / 723 | 0.923 / 0.923 | 0.991 (655 of 661) |
| R5635 | pool one2 | 442 / 474 | 0.932 / 0.928 | 0.971 (400 of 412) |
| R5636 | pool one2 | 1,277 / 1,280 | 0.920 / 0.920 | 1.000 (1,175 of 1,175) |
| R5637 | pool one2 | 922 / 968 | 0.918 / 0.911 | 0.988 (836 of 846) |
| R5640 | pool one2 | 793 / 793 | 0.880 / 0.880 | 1.000 (698 of 698) |
| R5642 | pool all (appendix) | 768 / 768 | 0.855 / 0.855 | 1.000 (657 of 657) |
| R5643 | pool one2 | 46 / 46 | 0.870 / 0.870 | 1.000 (40 of 40) |
| R5645 | pool all (appendix) | 219 / 238 | 0.913 / 0.916 | 0.985 (197 of 200) |
| R5646 | pool all (appendix) | 961 / 990 | 0.926 / 0.923 | 0.956 (851 of 890) |
| R5647 | pool one2 | 71 / 72 | 0.859 / 0.847 | 1.000 (61 of 61) |
| R5648 | pool one2 | 998 / 1,019 | 0.934 / 0.935 | 0.985 (918 of 932) |
| R5649 | pool all (appendix) | 441 / 443 | 0.948 / 0.948 | 1.000 (418 of 418) |
| R5650 | pool all (appendix) | 858 / 874 | 0.915 / 0.919 | 0.969 (761 of 785) |
| R5651 | pool all (appendix) | 635 / 1,208 | 0.910 / 0.922 | 0.938 (542 of 578) |

- The old text under the frozen pipeline equals the earlier key-free work's frozen lines on 8 of 8 main records.
- The earlier key-free work's named pieces that still read in the same row: 39 of 39.
- Not in the old row under the pool "one2" key, but in the new row: 055_288v_R5650_P6 C09 "benau".

- **The read stays.** On the same rows, an edit-distance alignment matches 0.938 to 1.000 of the earlier key-free work's decoded letters.
- **Named pieces:** all 39 of the earlier key-free work's named pieces read in the same row of the new text. 38 of them also read in the old text under the "one2" key.
- **The largest changes:** R5651 (0.938), R5646 (0.956) and R5650 (0.969). These pages had the most changed digits.
- **New text:** pages 063 (R5651) and 068 and 069 (R5652) are new to this split. Page 024 has cipher rows but no read sign.
- **The earlier key-free work's appendix records** (R5642, R5645, R5646, R5649, R5650 and R5651) used the pool "all" key there. Here they use the pool "one2" key. The table compares old and new text under the "one2" key only.
- **One gain:** "benau" now reads in 055 C09, where the old text did not show it under the "one2" key.

## Names, places and dates

Each item gives the record, the page and the row. The reading of a name is mine, from the decoded letters only.

| Item | Decoded | Record, page and row |
| --- | --- | --- |
| Benavides (a family name) | "··enauides", "enauides·", "benauides", "nauides", "benuuides", "bena·iides", "benaui·des" | R5637 014 C15; R5640 017 C20; R5645 029 C05; R5646 033 C13; R5650 054 C01, C17 and 055 C09; R5651 062 C02 and 063 C06; R5652 069 C07; R5653 076 C02; R5654 082 C06 |
| Vienna | "iluienna" | R5652 069 C04 |
| Lorraine (Lorena) | "lorenale", "loren···t", "lorena" | R5653 076 C06; R5654 082 C02; R5655 088 C15 |
| The Imperial court (cesarea) | "cesarea" | R5655 088 C08 |
| The Swedes (?) | "sueze·li", "suezeidsle" | R5636 012 C04; R5655 088 C06 |
| The Germans | "tedeso" | R5636 012 C04 |
| The plenipotentiaries | "plenipoten·tiari", "iilplenipotenti / arii" | R5636 012 C11; R5635 008 C18 to C19 |
| Neutrality (?) | "ilneutr····ta" | R5655 088 C05 |
| A suspension (?) | "sosp / enione" | R5655 088 C17 to C18 |
| Precedence | "preced / enza" | R5649 046 C16 to C17 |
| Restitution | "rtsitut·ne", "ilresitut·ne" | R5649 046 C03; R5652 068 C14 |
| The priory | "ilpriorato ilsan·etino", "priorato" | R5636 011 C09; R5637 014 C13 |
| The embassy | "basciata", "lambascian", "l ambasciaria" | R5636 012 C12; R5635 008 C14; R5637 014 C02 |
| The writing (a document) | "scritura" | R5645 029 C05; R5646 033 C13; R5648 042 C08, C13 and 043 C01; R5650 054 C04; R5651 062 C03 |
| A gentleman | "gentiluomo" | R5646 033 C09 |
| A fief | "feudoli" | R5651 063 C10 |
| The brother (or the friar) | "ifrate" | R5652 069 C05 |
| "…lonia", "colon" (perhaps Colonia, Cologne) | "illelonia", "colon" | R5648 043 C09 and 042 C02 |
| "ferare" (perhaps Ferrara, or a verb) | "ferare", "ferarei scriuo" | R5626 006 C03 and C11; R5654 082 C05 |
| "carboniera" (an unknown word, perhaps a name) | "carboniera", "car·toniera", "rbonier" | R5635 008 C16 and C19; R5655 088 C01 |
| 30 November and 3 December | "trentalnouembre eltre·decembre" | R5626 006 C01 |
| The 21st past (?) | "terzalde uentun·ppasat·" | R5635 008 C02 |
| The first of last month (?) | "ilprimo ilpasato" | R5636 011 C01 |
| February | "febraro" | R5636 011 C03 |

## English translation of stretches that read

- The "Decoded" column quotes the decoded text exactly, with its gap marks. `/` joins two rows.
- The "Restored" column is my conjecture. Square brackets mark every letter or word that I add. A `·` stays a gap.
- The "English" column gives the sense of the restored text.
- Most of these stretches come from pages new to this read, or from rows that the newer text changed.

| Record, page and row | Decoded (literal) | Restored (conjecture) | English |
| --- | --- | --- | --- |
| R5635 008 C14 | "oportuna·e·esuasa lambascian" | oportuna … [p]e[r]suasa l'ambascia[ta]… | opportune … persuaded … the embassy |
| R5635 008 C18 to C19 | "ioaratione eimisione iilplenipotenti / arii" | …aratione e [m]isione [de]i plenipotentiarii | …ration and mission of the plenipotentiaries |
| R5646 033 C07 | "sarebe deiderabie" | sareb[b]e de[s]idera[b]i[l]e | it would be desirable |
| R5646 034 C04 | "auona oportunit / a" | [b]uona oportunità | a good opportunity |
| R5646 034 C10 | "ilfara niente" | il farà niente | he will do nothing |
| R5645 029 C02 | "ilsolenitalii·creat·ne" | il[a] solen[n]ità … creat[io]ne | the solemnity … the creation (perhaps an election) |
| R5649 046 C09 | "sua patienzali" | sua patienza | his patience |
| R5649 046 C15 | "pienalfacoltali piace" | piena [la] facoltà … piace | full powers … it pleases |
| R5649 046 C16 to C17 | "ilpunto·ii preced / enza" | il punto [d]i precedenza | the point of precedence |
| R5650 054 C02 | "preparar· llanimo" | preparar[e] l'animo | to prepare the mind |
| R5650 055 C02 to C03 | "itrod / ut·ne elili·uniuersle" | i[n]trodut[io]ne … uniuers[a]le | the introduction … universal |
| R5650 055 C06 | "litentolloro" | l'i[n]tento loro | their aim |
| R5651 062 C02 | "corteli lodlilnauides" | corte … [Be]nauides | the court … Benavides |
| R5651 062 C12 | "cerca·ro i·ogni modoli" | cerca[r]o i[n] ogni modo | they sought in every way |
| R5651 062 C21 | "apartiene alloro" | a[p]partiene a loro | it belongs to them |
| R5651 063 C02 | "ripararebe ililb·l de··g ile obligato" | riparareb[b]e … obligato | it would repair … obliged |
| R5651 063 C04 | "sraorinarii" | s[t]raor[d]inarii | extraordinary (ones) |
| R5651 063 C07 | "dlambe le·partilpiacerebe asai" | d['a]mbe le parti … piacereb[b]e as[s]ai | of both parties … it would please greatly |
| R5651 063 C16 | "ocorendo" | o[c]corendo | if need be |
| R5652 068 C03 | "p·rocurato ilre·nder capace" | p·rocurato [d]i render capace (perhaps "procurato") | tried to make [him] understand |
| R5652 068 C14 | "impoibiitarne ilresitut·ne" | impo[ss]ibi[l]itarne la res[t]itut[io]ne | to make the restitution impossible |
| R5652 068 C18 | "medeime rag·n" | mede[s]ime rag[io]n[i] | the same reasons |
| R5652 069 C06 | "compatendo·cfi lelsciagure" | compatendo … le sciagure | pitying … the misfortunes |
| R5653 076 C06 | "lorenale partorisca" | Lorena … partorisca | Lorraine … may bring forth |
| R5654 082 C02 | "iteso elisguso llacidenti" | i[n]teso … gli acidenti | understood … the events |
| R5654 082 C07 | "ilzeloli acortezali" | il zelo … a[c]cortez[z]a | the zeal … the shrewdness |
| R5654 082 C09 | "abraciera uolenti·eri" | ab[b]rac[c]ierà uolentieri | he will embrace [it] willingly |
| R5655 088 C14 | "facolta·ulco nuoui acident" | facoltà … nuoui acident[i] | the power … new events |
| R5655 088 C15 to C16 | "lorena ihu piulmerito ellode sa / ranoldegni" | Lorena … più merito e lode saran[n]o degni | Lorraine … they will be worthy of more merit and praise |
| R5655 088 C17 to C18 | "sosp / enione" | sospen[s]ione | a suspension |
| R5655 088 C19 | "liscorsooe meco" | [d]iscorso … meco | the discourse … with me |

## How far to trust it

- **The key is the earlier key-free work's.** On twins of its size, the rule's shown values were right on 0.993 to 0.998 of the tokens (twin). That calibration is optimistic: the twins had only letter codes and no misread digits.
- **The public page of the first leaves names limits of this key:** syllable codes, nulls, false pairs and three-digit codes. This read uses the same key and cut, so it has the same limits. I used none of these facts to change a reading.
- **Short words and syllables:** expect wrong "l", "d" and "i" in short stretches, such as "ili", "ll" and "dl" (the earlier key-free work's note).
- **Double letters** are single in the decode ("sarebe", "ocorendo"). This can be the clerk's spelling or a fault of the read.
- **Pages that fail the gate** (020, 033, 089, 094, 098, 099, 104 and 110) read worse. Page 020 is mostly not Italian.
- **The six records that differ** have shares shown like the others (0.855 to 0.948). "Benavides" stands in four of them (R5645, R5651, R5652 and R5654).

## The decoded text, by record, page and row

The rows follow the page and row labels of the transcription. A token sits in the row where it starts.

## R5626

- `006_154r_R5626_P5 C01`: leau·ipe·de trentalnouembre eltre·decembre
- `006_154r_R5626_P5 C02`: sopra·loe···nza·fleia elan··i lid·icliano
- `006_154r_R5626_P5 C03`: ·iii ilfacia·ferare·i·fra·i botrule ·ll·
- `006_154r_R5626_P5 C04`: ia·facolta i·t··atare·elh sonolcapitate ·tr
- `006_154r_R5626_P5 C05`: ohn eunzl···i·ualsogio·irle ·ei·sara··ol·m
- `006_154r_R5626_P5 C06`: preldegnili lodeba·ifmi·eletiuerale i
- `006_154r_R5626_P5 C07`: preimrsoata·uiueza·e prudenzafuseedd·s
- `006_154r_R5626_P5 C08`: poorele anihlie corone·adri·p·d···rale efia
- `006_154r_R5626_P5 C09`: corispondenzalu·e··doi ihganip·re illss·o
- `006_154r_R5626_P5 C10`: erea· mortelio·e···colilognil·tro aciden
- `006_154r_R5626_P5 C11`: te ila··z deec ueniile ferarei scriuo ··lp
- `006_154r_R5626_P5 C12`: artea··nol·biolellfr·elsarai·n·rticipat
- `006_154r_R5626_P5 C13`: o·i·a ilprocedere·i deianlcol fozerelil
- `006_154r_R5626_P5 C14`: f·itaii·gli elloro ··lfifolrapre·ntar
- `006_154r_R5626_P5 C15`: e ilcotesa ···tre cortile pocolprop··r···n
- `006_154r_R5626_P5 C16`: ato··e d·italilc· li·ellalai leuata ··heut
- `006_154r_R5626_P5 C17`: orital·· suoilu ne·u·li·s·onolpartiti e
- `006_154r_R5626_P5 C18`: luol·i do·ue··a··dorono···········································
- `006_154r_R5626_P5 C19`: za·gli·nlcorino··lrihne·ilfa ·irm apareoat
- `006_154r_R5626_P5 C20`: o azif·gs··i oln··uol·m··s···············································
- `006_154r_R5626_P5 C21`: · eis doue sonolgia mei andole ee·dibhlto ill
- `006_154r_R5626_P5 C22`: ·trole u··riilprie···i··························································
- `006_154r_R5626_P5 C23`: a·i

## R5635

- `008_205r_R5635_P1 C01`: tengo nrele·ide·una decid·de··e
- `008_205r_R5635_P1 C02`: i·terzalde uentun·ppasat· i prima h··an
- `008_205r_R5635_P1 C03`: a un·istinnoae·ida· ·illebe lensne i
- `008_205r_R5635_P1 C04`: uantecedenteeliscor· colei le duelet
- `008_205r_R5635_P1 C05`: rade ilsua paternita laldet··dui eili
- `008_205r_R5635_P1 C06`: uorei i·c·
- `008_205r_R5635_P1 C07`: ·e puelpomtap ·ce uulruina iro·nderebel
- `008_205r_R5635_P1 C08`: iutee·i ste·eii·rlg e·ggbteaa·asai
- `008_205r_R5635_P1 C09`: onfr·pue llm iie lapasat·ei
- `008_205r_R5635_P1 C10`: sua ricuperata sae··
- `008_205r_R5635_P1 C11`: ··m··ita i
- `008_205r_R5635_P1 C12`: el ··el
- `008_205r_R5635_P1 C13`: ··no
- `008_205r_R5635_P1 C14`: la·ope oportuna·e·esuasa lambascian
- `008_205r_R5635_P1 C15`: a ·mb ap· glii pria·l ·tasno ili
- `008_205r_R5635_P1 C16`: emezo iap ii·carboniera e·e e searne e
- `008_205r_R5635_P1 C17`: adeso lefeto pense·o ineeo larano i·
- `008_205r_R5635_P1 C18`: ioaratione eimisione iilplenipotenti
- `008_205r_R5635_P1 C19`: arii am· duir i·car·toniera ll pureler
- `008_205r_R5635_P1 C20`: a lan·n·

## R5636

- `011_211r_R5636_P4 C01`: td lo int·soupoa eo eie ilprimo ilpasato
- `011_211r_R5636_P4 C02`: i·caso·i·ea··iie me·ne elun cenno e ilsu
- `011_211r_R5636_P4 C03`: a de····enti·i febraroiienma a io e·a·eli
- `011_211r_R5636_P4 C04`: a·principiol· co·lagiori ii·n·gtrebels
- `011_211r_R5636_P4 C05`: einger isnsl·ai eclusione dluna·buonali
- `011_211r_R5636_P4 C06`: elua eblouar·i·g eicolilii unasp ifc p
- `011_211r_R5636_P4 C07`: otralminuciar ·i·ie iaf itia·e·gcasa·
- `011_211r_R5636_P4 C08`: g do·gli·elgena ·u n ·traiidizgfo··a e
- `011_211r_R5636_P4 C09`: ta ilpriorato ilsan·etino ·iels·s·e··nd
- `011_211r_R5636_P4 C10`: o dauantagio i·gli loh·pmtlo l
- `011_211r_R5636_P4 C11`: etoe···iacere ·
- `011_211r_R5636_P4 C12`: · ··di·la·elisinuato·prudente·eld pro
- `011_211r_R5636_P4 C13`: ···iad·pilaser
- `011_211r_R5636_P4 C14`: olpiede ·pi pareiao·e facii· capita
- `011_211r_R5636_P4 C15`: le i·a·rico·ile·ee
- `011_211r_R5636_P4 C16`: tale·potrebe·dlmrs·sciuto lsnill···
- `011_211r_R5636_P4 C17`: elsara·tempe iluilersene i·buona··g
- `011_211r_R5636_P4 C18`: ·lont·· ihaa
- `011_211r_R5636_P4 C19`: s·ates·i l·medesimoanol elpiaciuta
- `011_211r_R5636_P4 C20`: asai i·eilp·ocuri iantenersi ilefidenzal
- `012_211v_R5636_P3 C01`: / iegan i·animarlo ue· ··o ald·eresi iieid··iius
- `012_211v_R5636_P3 C02`: niltil· la ··ntore iliao mediante una·rocomp··ns
- `012_211v_R5636_P3 C03`: a ipl uolnolimpadnonirsi ··l··unaluli dall re
- `012_211v_R5636_P3 C04`: no·i tengono· li sueze·li a li·it e·li tedeso i
- `012_211v_R5636_P3 C05`: sengono elet·iitata iep iipn eiluegono aber
- `012_211v_R5636_P3 C06`: ito epopoli iptominoo ·emo e·le···i·lole
- `012_211v_R5636_P3 C07`: n··e epdtrapazi·f·i popoli·doue i·trouan
- `012_211v_R5636_P3 C08`: o· icz simano isara ··ocolprofiteuole ·ie
- `012_211v_R5636_P3 C09`: ni·gni similacdisto·uengo ·iie ·eloibis· e
- `012_211v_R5636_P3 C10`: tinente loa i·e lebellanon ·ei isinuo a
- `012_211v_R5636_P3 C11`: orta·e·i necesita delplenipoten·tiari iei
- `012_211v_R5636_P3 C12`: basciata elii·solecitudine ilai replica il
- `012_211v_R5636_P3 C13`: feceaoliei poteua·zi menoi isciare ··sa
- `012_211v_R5636_P3 C14`: presentecn lefu iiiorenai·i sogiun·c··c·
- `012_211v_R5636_P3 C15`: ili·a·sarebe un··ac··moe·elur a·fauore ii
- `012_211v_R5636_P3 C16`: ·n eii·imili agiustaheigrorela er e·tolere
- `012_211v_R5636_P3 C17`: e ternooportuna·ela·zisanza de umimm
- `012_211v_R5636_P3 C18`: otenniari irisposta i·o·a·a·punto·e i
- `012_211v_R5636_P3 C19`: medesimali ·mprees parezl··il·cune uolte u
- `012_211v_R5636_P3 C20`: l·· isciato itender i·e uolerel rispeto i

## R5637

- `014_213r_R5637_P3 C01`: geloiie deca i i·arati· ns ii·esonal· ad ou
- `014_213r_R5637_P3 C02`: ee cia·e l ambasciaria ·eb·fa le··lanol tengo
- `014_213r_R5637_P3 C03`: i·a·f ei·fine i·ei acena·bi·im·lic·luii
- `014_213r_R5637_P3 C04`: i euold tntra·g· au··aliitreto ica i·ullli i
- `014_213r_R5637_P3 C05`: ilec· meso aogeti aortati elc eng·ali ier
- `014_213r_R5637_P3 C06`: ialf ·i·corte i·i sogeti i·traualano e i·s
- `014_213r_R5637_P3 C07`: antaoesa·ei·il·i amdunza ·esleo ·ilco
- `014_213r_R5637_P3 C08`: rte i e ·mpre riputa·a elauanti utieluled
- `014_213r_R5637_P3 C09`: ·eresi icr·i·a·aniera potra·eparlar··lun ·
- `014_213r_R5637_P3 C10`: tra uoltal sara etal· tenendosi su·r·t ·l
- `014_213r_R5637_P3 C11`: ·re·iei prese····a iea potrebono iuitar ili
- `014_213r_R5637_P3 C12`: a·gli desiderano e·i un·certo··odo·impegno
- `014_213r_R5637_P3 C13`: ·i· priorato·ella·parlato·ie dib··era
- `014_213r_R5637_P3 C14`: ··a·gli euien·zlcirca lloferte ilpensioni sop
- `014_213r_R5637_P3 C15`: ra·i·e· ispiace il ··enauides ellabi·i·nela
- `014_213r_R5637_P3 C16`: colta ihigufare oldubito iipo ilrafreegas
- `014_213r_R5637_P3 C17`: · alforsi e· lle uoluto·ilarelnui elcoritr
- `014_213r_R5637_P3 C18`: ·onder a·g ilibo feceroeln·lp·ie·aproc
- `014_213r_R5637_P3 C19`: uri iellfacia aetura·t·poi ·llirocurarebe
- `014_213r_R5637_P3 C20`: ro iai elfacolta circa ·i·ancanza iildil·en
- `015_213v_R5637_P1 C01`: / de ·iiiel ale atoll ailadlhi giallo ·eto·i p
- `015_213v_R5637_P1 C02`: iteualouar·l impegnoiz ail··rltemmo ···ha·
- `015_213v_R5637_P1 C03`: eartico·ire deuo ricerere aie ililtoli··lano
- `015_213v_R5637_P1 C04`: e luomeseeo impegni·oi puri iscorg ··le
- `015_213v_R5637_P1 C05`: i · nelastepac·i oi·u·i puo piacelil·illibi
- `015_213v_R5637_P1 C06`: easa··odicol·ndo ei·labi trouano buon·
- `015_213v_R5637_P1 C07`: ripaego·e· scusar ·andbei tarenza ii·r
- `015_213v_R5637_P1 C08`: isposta

## R5640

- `017_237v_R5640_P2 C01`: ione iiei e·de suoi·sli ogni·comodo ig·
- `017_237v_R5640_P2 C02`: plm·cu·aa·a ldm nel··tri pcntie·ili slitro
- `017_237v_R5640_P2 C03`: ducami·dfml miister· ieee eilprocuaie
- `017_237v_R5640_P2 C04`: lic ideef afine ie·i tronol· ·ellpricid·
- `017_237v_R5640_P2 C05`: df·col pariae·e iscorere·i agic·stano sp
- `017_237v_R5640_P2 C06`: e·lo li·co·ldoue ee·parare·f·iritano l·ani
- `017_237v_R5640_P2 C07`: mile corono ·i rotuaa i·punto icn saral
- `017_237v_R5640_P2 C08`: i·piu ificie·a·pl· dio ahe·uli·alpropoi
- `017_237v_R5640_P2 C09`: to e·so ilagiungere imi uniuers·e·il ·e
- `017_237v_R5640_P2 C10`: ifinite·ificolta e·lunglere ilpotrebono·
- `017_237v_R5640_P2 C11`: ·teraa le·co··nu· i·agiusa·rolli·duelmr
- `017_237v_R5640_P2 C12`: darebe·facie agiustar ll·tri···n i·cap
- `017_237v_R5640_P2 C13`: i·· agiustahe faali duecr e·abracia·
- `017_237v_R5640_P2 C14`: ro·il ·tri ildica puoler·neaun ricordo
- `017_237v_R5640_P2 C15`: particoire·a·e·ipendendoia lhf ie piuliot
- `017_237v_R5640_P2 C16`: o a·lei debr ·lne sono·etiiu ilbasano·flri
- `017_237v_R5640_P2 C17`: mane i·· rimia·il·i·prudenza iee e·i·o··i
- `017_237v_R5640_P2 C18`: ile aica·ne l·acortezalne relo·ome lldna·
- `017_237v_R5640_P2 C19`: c de··ici·iianul uoleua uederli facolta·i ·
- `017_237v_R5640_P2 C20`: enauides· ei·elnellaueuaaf·eai·ei me·ne·llbe
- `017_237v_R5640_P2 C21`: eto partelae·pl· riceunf··ule lei·ii sudia ·ta
- `017_237v_R5640_P2 C22`: e lolpotuoo saesmmnte iilrisposta·iai

## R5642

- `020_246r_R5642_P6 C01`: lollhlos·iscorsolid·edcolanoe ell a·rt·ne·
- `020_246r_R5642_P6 C02`: a h llh·f·as· uolrde b· oleih ·hai·a· d·i·e
- `020_246r_R5642_P6 C03`: ·u s·ueoaiu e·el·bo··af ·fl·ni fi i·faiol·
- `020_246r_R5642_P6 C04`: ubh ell ebidenzi ofli·zn·bl·· ·oimc dl
- `020_246r_R5642_P6 C05`: r·eriu·ndo rhlh era·lo i·till·li o·i lo·
- `020_246r_R5642_P6 C06`: dolilnl· trouerhnolu e odo·i igiu·orl·
- `020_246r_R5642_P6 C07`: nz· mp·alparsitadda ·hrt·i·nle bh go·i
- `020_246r_R5642_P6 C08`: ibosi·zhd ·guli i·e rato re olecitht
- `020_246r_R5642_P6 C09`: o ilnslo· ageelh·r s·inded·adeireh bi
- `020_246r_R5642_P6 C10`: ·o·lgono·a l o e·aeinoloi ala ehesdno·
- `020_246r_R5642_P6 C11`: de·ler·h n··trarr··az eladoresid·arh e
- `020_246r_R5642_P6 C12`: eaiiidh cie··miip ci e·lporeisi· ocorbo
- `020_246r_R5642_P6 C13`: ers ·lei elle ddli sc·doi·clsllnsl· os
- `020_246r_R5642_P6 C14`: ·u·ar ·lbi· rh lelsi re··ai risol·usgue e
- `020_246r_R5642_P6 C15`: uorh i·i ilpreu·h·lp aiig di ntagi·e
- `020_246r_R5642_P6 C16`: ·logi ·sltie·nh aldniesaa·i adezgdnli·
- `020_246r_R5642_P6 C17`: e slsopli·i dl sipr·nap· alilc·e·ul· ag
- `020_246r_R5642_P6 C18`: ·i n·i e·c leloiblhii rlh lco· e·una
- `020_246r_R5642_P6 C19`: li·ilsuieildoos iir ilirle e··ii··ii ic
- `020_246r_R5642_P6 C20`: orerh a·igaicoli··i ·rsrlo·suolleaa hr·
- `021_246v_R5642_P3 C01`: / coteso i·aal· olerii·edhr lba·torit··· od
- `021_246v_R5642_P3 C02`: epa· esor··a· f·lza·u ··f··a·ea··lhs
- `021_246v_R5642_P3 C03`: ll··e·i ··le··bi·i ·i· iu·il·· lpldfis·aa
- `021_246v_R5642_P3 C04`: elecludere |

## R5643

- `024_249r_R5643_P1 C01`: | ·
- `024_249r_R5643_P1 C02`: ·
- `024_249r_R5643_P1 C03`: ·
- `024_249r_R5643_P1 C04`: ·
- `024_249r_R5643_P1 C05`: ·
- `024_249r_R5643_P1 C06`: ·
- `024_249r_R5643_P1 C07`: ·
- `024_249r_R5643_P1 C08`: ·
- `024_249r_R5643_P1 C09`: ·
- `024_249r_R5643_P1 C10`: · | ·
- `024_249r_R5643_P1 C11`: ·
- `024_249r_R5643_P1 C12`: · | ·
- `024_249r_R5643_P1 C13`: ·
- `024_249r_R5643_P1 C14`: ·
- `024_249r_R5643_P1 C15`: ·
- `024_249r_R5643_P1 C16`: ·
- `024_249r_R5643_P1 C17`: ·
- `024_249r_R5643_P1 C18`: ·
- `025_249v_R5643_P3 C01`: / eo lel·faco··s ·
- `025_249v_R5643_P3 C02`: mlcol·
- `025_249v_R5643_P3 C03`: ··oi ·
- `025_249v_R5643_P3 C04`: ·uer·
- `025_249v_R5643_P3 C05`: ·ra·ri·
- `025_249v_R5643_P3 C06`: rfe e·
- `025_249v_R5643_P3 C07`: ·ae·
- `025_249v_R5643_P3 C08`: u· ·
- `025_249v_R5643_P3 C09`: ol·
- `025_249v_R5643_P3 C10`: · |
- `025_249v_R5643_P3 C11`: ·····
- `025_249v_R5643_P3 C12`: abld·
- `025_249v_R5643_P3 C13`: e ·
- `025_249v_R5643_P3 C14`: ·so··

## R5645

- `029_261r_R5645_P2 C01`: le rag·ni··i lang···moso·e ale iteruenirel·
- `029_261r_R5645_P2 C02`: ilsolenitalii·creat·ne ldeee |
- `029_261r_R5645_P2 C03`: circall· a·zlpublici |
- `029_261r_R5645_P2 C04`: ·a e·gna
- `029_261r_R5645_P2 C05`: tali·scritural·sdlbenauidesli iai |
- `029_261r_R5645_P2 C06`: i·lle laeelmlaopa ilcosaldo
- `029_261r_R5645_P2 C07`: uemrisp··ndere | ilris
- `029_261r_R5645_P2 C08`: posa·i·u | ·a eli t
- `029_261r_R5645_P2 C09`: rono·e i·risprsali·d |
- `029_261r_R5645_P2 C10`: elocorso daru·catalii
- `029_261r_R5645_P2 C11`: b ilcredili ·lecisoro·publi···· |

## R5646

- `033_268r_R5646_P3 C01`: · loirpdl·ntore i·flidileliio ritoonoi
- `033_268r_R5646_P3 C02`: ielificolta ieibple·uanoli ecleu ilicure
- `033_268r_R5646_P3 C03`: zal·e·s·iptlfu dioeddelol iiz |
- `033_268r_R5646_P3 C04`: il·nte elpiu band··li·l
- `033_268r_R5646_P3 C05`: ule·liapcli ils·ute·i·cl··ino· eleicolos
- `033_268r_R5646_P3 C06`: o· iciio·ale · iiollaue··aposo iloaa
- `033_268r_R5646_P3 C07`: ri·al· sarebe deiderabie iilriecil····
- `033_268r_R5646_P3 C08`: col·sluolo iltorrna·l·lcl·i potra fori··
- `033_268r_R5646_P3 C09`: spore sdli gentiluomo· anetolllrla ulita
- `033_268r_R5646_P3 C10`: riisacbuiio·elgroso e·ohc alpro··oit
- `033_268r_R5646_P3 C11`: olllmliiaoaa lli modo eill la··ito
- `033_268r_R5646_P3 C12`: lod·ilg·u··a elamolire llanimi loi·sali
- `033_268r_R5646_P3 C13`: lscri·turaleta··lbenauidesli lo liole n
- `033_268r_R5646_P3 C14`: au··r illian ilioario ilesadild·mlpote
- `033_268r_R5646_P3 C15`: ndolollouare elnomia rlioi·eridi··nz···t
- `033_268r_R5646_P3 C16`: radedpre ione · preuego uera·elie·ilfa ··a
- `033_268r_R5646_P3 C17`: nie··t······ |
- `033_268r_R5646_P3 C18`: e·llitere·ldeadlcauar·fuori·iil ieoli·u
- `033_268r_R5646_P3 C19`: i iip·ton re··a· ·fb |
- `034_268v_R5646_P4 C01`: | ilano·belici
- `034_268v_R5646_P4 C02`: medeialulilsato iiii potrebono iid ren
- `034_268v_R5646_P4 C03`: dere idol·la·o·e sur·ilcolc·i· efarme alri
- `034_268v_R5646_P4 C04`: cori ilcarl···ito | auona oportunit
- `034_268v_R5646_P4 C05`: apctrebe sigerir·a eciihilh ·l·seht·a
- `034_268v_R5646_P4 C06`: lsrae· uoler zararelognicosa ele buona i
- `034_268v_R5646_P4 C07`: e etraria ·elbuonelaimeldeed ilrareluo
- `034_268v_R5646_P4 C08`: lteldono riuscite ale |
- `034_268v_R5646_P4 C09`: i·g ili pen·la elpr·egiuici·eafoii ·ici ui
- `034_268v_R5646_P4 C10`: e·nlo aicura ie ilfara niente ··ali··gu·re
- `034_268v_R5646_P4 C11`: e ulde·i lauerebono ancatoaal·seieo·olalh
- `034_268v_R5646_P4 C12`: es·gere anaepfc· eadl |
- `034_268v_R5646_P4 C13`: elillab·i pari·ro ·on
- `034_268v_R5646_P4 C14`: i illmbi·iao·tro·a tolag·r faci·utali pria

## R5647

- `038_272r_R5647_P2 C01`: | · iabre ili iltrece
- `038_272r_R5647_P2 C02`: tralc·l·guore ·nzai·o·lrio·labi·i···n··· ·e
- `038_272r_R5647_P2 C03`: f·n·e·i |
- `038_272r_R5647_P2 C04`: i·glsle·ip s··ailp·or··
- `038_272r_R5647_P2 C05`: ···· |

## R5648

- `042_279r_R5648_P3 C01`: entroie ebuon esorio··sag·na·eliilili un·
- `042_279r_R5648_P3 C02`: ne colon i·fu opcrtuna llutesat·nelilabmmo |
- `042_279r_R5648_P3 C03`: ·n ricordo·ohc alpropoito·ile ilirit···ro lg·
- `042_279r_R5648_P3 C04`: r·ell anih·de adle ·iaiuti ibmlnsnti ilp
- `042_279r_R5648_P3 C05`: otrebono eri·· r··montl··triem iee
- `042_279r_R5648_P3 C06`: ilrisposalfu asa·i·b·g··sfalillir··aola a
- `042_279r_R5648_P3 C07`: uis·ata lop ·oiaali ··lisi lalrag·natoa
- `042_279r_R5648_P3 C08`: tolaopraen scritura etalalbe·g·des·ilt
- `042_279r_R5648_P3 C09`: laueralpoi s··to ··er ···eratoda antole ei
- `042_279r_R5648_P3 C10`: calo ilrom ee r·fio·iilmlio ·lsimo
- `042_279r_R5648_P3 C11`: i·ellauera·fa partelsualsi eha capolei
- `042_279r_R5648_P3 C12`: rompa ilal hlisp·iace·i·cle lod i·iferis
- `042_279r_R5648_P3 C13`: ca·uli erli rispose·lal scritura i·i··
- `042_279r_R5648_P3 C14`: l·gua bilogna pre·ierlsbpra·ili·tlia s
- `042_279r_R5648_P3 C15`: raua gante le ilrompa iif fece·ie·e·a
- `042_279r_R5648_P3 C16`: ire ildoue iltrata depilile uilpuo mierla
- `042_279r_R5648_P3 C17`: no ·i ·ie· |
- `042_279r_R5648_P3 C18`: irome··leleli d
- `042_279r_R5648_P3 C19`: pensarebe·climl ent·e ihl··liaelmodo
- `043_279v_R5648_P6 C01`: / ueruno elentrarebe· ·ilpro·sosa ·ilscritura
- `043_279v_R5648_P6 C02`: | ion aee risposa iia
- `043_279v_R5648_P6 C03`: | ihi ·sl·
- `043_279v_R5648_P6 C04`: i iliare |
- `043_279v_R5648_P6 C05`: i atn·······lie adlerenze deol ispiace ila·e
- `043_279v_R5648_P6 C06`: eliaaa·comunicata subito iceimituraddfi
- `043_279v_R5648_P6 C07`: nbedsmuideslii elibmgml loi·esso iiihg
- `043_279v_R5648_P6 C08`: i·o·negotia ea· iltrouari uiciol·i corte
- `043_279v_R5648_P6 C09`: | lod illelonia |
- `043_279v_R5648_P6 C10`: ···
- `043_279v_R5648_P6 C11`: | ·n·ell cooei
- `043_279v_R5648_P6 C12`: pie·ciuta llate··at·ne ih·· hlfa ia·fio ia·a ·
- `043_279v_R5648_P6 C13`: · ileli lalrisposo·········a· adedata·e |
- `043_279v_R5648_P6 C14`: ispiace i·l iferhta iigu ia ihg·i
- `043_279v_R5648_P6 C15`: itale lano profesatolilemi··i llafari i b |
- `043_279v_R5648_P6 C16`: lol·eduto·g illli h·scriuedeirca ildiianza i
- `043_279v_R5648_P6 C17`: i dlideralldifi iun·emmento ilprezo ion |

## R5649

- `046_281r_R5649_P1 C01`: | if· ileli lebelcolanoe e solicola labi
- `046_281r_R5649_P1 C02`: uolute· etenderli··lirelilallli a·suoi
- `046_281r_R5649_P1 C03`: ··lapartera ilpr·ia·rareli rtsitut·ne
- `046_281r_R5649_P1 C04`: iln supra· il· ieloemute |
- `046_281r_R5649_P1 C05`: fildoaeledilialarii·esdm |
- `046_281r_R5649_P1 C06`: prop·re opurelui labisl·rop
- `046_281r_R5649_P1 C07`: oso pacado·ilirlest genereoi eli |
- `046_281r_R5649_P1 C08`: lilc· |
- `046_281r_R5649_P1 C09`: i unrsld·olii sua patienzali ·ntire |
- `046_281r_R5649_P1 C10`: roli
- `046_281r_R5649_P1 C11`: dele ifeuenis comprende·olle emutelilp
- `046_281r_R5649_P1 C12`: rloibisce sottolcen·aure·oli isce·ri ·nl
- `046_281r_R5649_P1 C13`: tm faralic alledere a·dia boliit··l
- `046_281r_R5649_P1 C14`: laues··lmlacrupo·o posalfariluloluere
- `046_281r_R5649_P1 C15`: end·e·ene pienalfacoltali piace ile iln
- `046_281r_R5649_P1 C16`: uandoh·ellab·l·i··ato ilpunto·ii preced
- `046_281r_R5649_P1 C17`: enza

## R5650

- `054_288r_R5650_P2 C01`: | ilrag·na·eltra lon ilbenauidesleaa·
- `054_288r_R5650_P2 C02`: utielepreparar· llanimoliao·a e·rib
- `054_288r_R5650_P2 C03`: utar·subito ilrisposa·i ·ll era·
- `054_288r_R5650_P2 C04`: ·i scritura i·i·tpmoli cenno·i med
- `054_288r_R5650_P2 C05`: eimood douera·d ··tai e·a··lbe
- `054_288r_R5650_P2 C06`: uc·ricorere aie ileli·facili poib
- `054_288r_R5650_P2 C07`: ieli ell ·teza iilrisposan·li uenglila
- `054_288r_R5650_P2 C08`: rom·oeiafoo imiano aliscute··dlane
- `054_288r_R5650_P2 C09`: giar lelco·it iluano ilano ilan·dlagiu
- `054_288r_R5650_P2 C10`: sando le·mezani ·lpre·ego ··c··l··a··a
- `054_288r_R5650_P2 C11`: i ag·rlscolo ait sopra·aosarticoirel
- `054_288r_R5650_P2 C12`: lo di···la·eli ·at ··hil······li lolsaputo
- `054_288r_R5650_P2 C13`: la··glh·rimio dubito·il·i liio uolnolf
- `054_288r_R5650_P2 C14`: iir ognilcosa·aui·r··e icoile co··i·lio
- `054_288r_R5650_P2 C15`: leei lanol·if···itils· pili ificolta ehd
- `054_288r_R5650_P2 C16`: uiiu it··resati ildl ·lpenso iota··ue
- `054_288r_R5650_P2 C17`: dendo·a i·benaui···es ical···ol·pao····d
- `054_288r_R5650_P2 C18`: ·a irl·tle uolci ·n·el· tratare eloel
- `054_288r_R5650_P2 C19`: mosrili·lun aedpitodl· ·llentrerala
- `054_288r_R5650_P2 C20`: ire ilbisogna fiire·ogni cosa·li·aplfomf·
- `055_288v_R5650_P6 C01`: / ilpotrel·e rispondere ihu liri·cfuarati
- `055_288v_R5650_P6 C02`: e·ilcohnciare·e uno·i ·ruira·oli itrod
- `055_288v_R5650_P6 C03`: ut·ne elili·uniuersle al··aneg· iri ·l
- `055_288v_R5650_P6 C04`: puredipo uorano entrarui rispiol·i rispo
- `055_288v_R5650_P6 C05`: sad·rali ·ll pote·lere eld ilscuoprir
- `055_288v_R5650_P6 C06`: a·faciie llitentolloro ileli lau·era·
- `055_288v_R5650_P6 C07`: ··i entrarui·
- `055_288v_R5650_P6 C08`: | isp·ace ili if
- `055_288v_R5650_P6 C09`: erisca iuli risposad··benauidesi

## R5651

- `062_297r_R5651_P3 C01`: · ele i·eta·pose·r·re ahgli·e···e ··ren·tuno·l
- `062_297r_R5651_P3 C02`: uaoselo li corteli lodlilnauides laueu
- `062_297r_R5651_P3 C03`: mlgia eto·unadialue·scritura ioiisposa
- `062_297r_R5651_P3 C04`: ···i· ··hi elpareli soisfa·c··a··t·····ra···le·
- `062_297r_R5651_P3 C05`: m···au···nzol·ii·dl··· u··e···r·zihi·atarei
- `062_297r_R5651_P3 C06`: to·d·n·zaniltro··a··l· t·····fu·······m···a·eli ·l
- `062_297r_R5651_P3 C07`: portarelianzi i·iiiro lelproposeli le·
- `062_297r_R5651_P3 C08`: rispose ilagiusano·clco·a·ilids·m··eli
- `062_297r_R5651_P3 C09`: fio·ii···le denelar rispo··a·ogniuoltai ie
- `062_297r_R5651_P3 C10`: a·ii····li ripilalbiso·····c····iciarldcapo ·f
- `062_297r_R5651_P3 C11`: ·llauereiic·caro ihe eao·i··treuolte
- `062_297r_R5651_P3 C12`: lolacenato cerca·ro i·ogni modoli·zletiu
- `062_297r_R5651_P3 C13`: areliafli ello isciare icalarele·sma·el
- `062_297r_R5651_P3 C14`: i rispose·tlposono·alnir·t·i egi·unrure
- `062_297r_R5651_P3 C15`: ilci·lacio·i·ebsro·g·co··liafli troua i
- `062_297r_R5651_P3 C16`: pieili ile ·guirebe elaulntura ·li laue·
- `062_297r_R5651_P3 C17`: a rimierlinuouu ele ira·oaneuole i·dole
- `062_297r_R5651_P3 C18`: nz··l·isdlb·me···ides··li·o·e ·sie·no·n····rt
- `062_297r_R5651_P3 C19`: e ll·de·u··a ·e···de loro··l·a···i ····u·····l········e
- `062_297r_R5651_P3 C20`: uison·re de·erahe ·corso·iaad ilpoi toc
- `062_297r_R5651_P3 C21`: alaadlmuouer·g·i apartiene alloro e· i
- `063_297v_R5651_P8 C01`: / eranebti alllpl·mpre·ile parito·iaale
- `063_297v_R5651_P8 C02`: ripararebe ililb·l de··g ile obligato
- `063_297v_R5651_P8 C03`: sohnisrarllore· elle dloanzeluecoe ilia·
- `063_297v_R5651_P8 C04`: f ilsotrarl soihe li·sraorinarii ilpa
- `063_297v_R5651_P8 C05`: reli i·a fo·rolecordoe sol· iha for
- `063_297v_R5651_P8 C06`: a·parli·rlbenauides ilioarat·ne piu
- `063_297v_R5651_P8 C07`: amp·ra dlambe le·partilpiacerebe asai·t
- `063_297v_R5651_P8 C08`: caortarebe iai piulpreso ·lsuo fielal·
- `063_297v_R5651_P8 C09`: u·le bisognalrome ilfio·ieg ilc elnli pr
- `063_297v_R5651_P8 C10`: iende feudoli·f·i eia uilmiono·glc·iu
- `063_297v_R5651_P8 C11`: ·eliadli iluee ·le·ii·ienato·acaa
- `063_297v_R5651_P8 C12`: reli i·comici alrlllntare elparte deedl
- `063_297v_R5651_P8 C13`: ·········orelia·priezione· ien ilresi····isc
- `063_297v_R5651_P8 C14`: ali i·e elpoco·t·sc·taria·nolun··lscol
- `063_297v_R5651_P8 C15`: od·tralreplica eldeuoiai sudlaee iiel
- `063_297v_R5651_P8 C16`: ne ocorendohlirle······roldifi·r·co

## R5652

- `068_303r_R5652_P4 C01`: | c··de uesbiitre i·rmg·na·eli elila·r·
- `068_303r_R5652_P4 C02`: col medeimodille pot·entilrag·nile le·diil
- `068_303r_R5652_P4 C03`: la·p·rocurato ilre·nder capace·i a eiiscia
- `068_303r_R5652_P4 C04`: redlmdduderlilileln·i·lispiace·ino· ··
- `068_303r_R5652_P4 C05`: ania ilel·e | ·nulilidiluol piu
- `068_303r_R5652_P4 C06`: tostolaspiare·dleuentou·ili·i |
- `068_303r_R5652_P4 C07`: i··sl uo·d auerso i·ire i·ria
- `068_303r_R5652_P4 C08`: nendom·n·i ano·depoa··lel·i·ohd ilpeg·re
- `068_303r_R5652_P4 C09`: au | d· elpur peg·idllresil
- `068_303r_R5652_P4 C10`: ilano delmedeih·oli·ilde·plili·saslrli
- `068_303r_R5652_P4 C11`: caci·are eli forza·dsilsono co··piene i·i
- `068_303r_R5652_P4 C12`: ficol·pa ili·eungl·umd· eicoli i isciare·ls
- `068_303r_R5652_P4 C13`: csltempo ilano ii·medeih lels··die duen
- `068_303r_R5652_P4 C14`: u elun dai impoibiitarne ilresitut·ne·
- `068_303r_R5652_P4 C15`: u ili dungo po·lo·fa parerleuoucdl·tr
- `068_303r_R5652_P4 C16`: i·uzsia ile ui anan·
- `068_303r_R5652_P4 C17`: ilspe··ll·tro i elisci ill·
- `068_303r_R5652_P4 C18`: ·are bdblna·es le·medeime rag·n·iht
- `069_303v_R5652_P8 C01`: / | · elseanza ihz
- `069_303v_R5652_P8 C02`: hd cosalenid e·gr
- `069_303v_R5652_P8 C03`: i··u
- `069_303v_R5652_P8 C04`: tcria slsa·eliscorano iluienna |
- `069_303v_R5652_P8 C05`: ·lli lor·na | ifrate·i·o
- `069_303v_R5652_P8 C06`: compatendo·cfi lelsciagure iigdaseza |
- `069_303v_R5652_P8 C07`: ·nsdlbenuuidesli i·a ambi·dco ilresi c
- `069_303v_R5652_P8 C08`: ertasi

## R5653

- `076_310r_R5653_P5 C01`: | · lol·iso i·nso
- `076_310r_R5653_P5 C02`: isd bena·iidescircaln·i iletrar··in
- `076_310r_R5653_P5 C03`: p···tornol· medeimo di elil·ohz ·t
- `076_310r_R5653_P5 C04`: ro ilbaterele una parte ill ·tra elm
- `076_310r_R5653_P5 C05`: otiui acenatil·tce uolte alizi·toli iu
- `076_310r_R5653_P5 C06`: aione·i lorenale partorisca ag·ri iseo
- `076_310r_R5653_P5 C07`: mponi·eltra·le·corone |

## R5654

- `082_315r_R5654_P4 C01`: | lo
- `082_315r_R5654_P4 C02`: iteso elisguso llacidenti·i loren···t
- `082_315r_R5654_P4 C03`: dubito i | ·iloi li ell
- `082_315r_R5654_P4 C04`: a rimorsolie | ildo
- `082_315r_R5654_P4 C05`: ue··i e·ferare·alrouia·a·plisn·pr
- `082_315r_R5654_P4 C06`: omeso i·z·lrgle·aeture a·benaui·des
- `082_315r_R5654_P4 C07`: saraeerap·egna ilzeloli acortezali·
- `082_315r_R5654_P4 C08`: eiiesuader·lsdl |
- `082_315r_R5654_P4 C09`: ipa·nlgia·emga abraciera uolenti·eril
- `082_315r_R5654_P4 C10`: imibl iliaatorna·eto ouderslloo a
- `082_315r_R5654_P4 C11`: id cosal i

## R5655

- `088_323r_R5655_P5 C01`: scri·ro lirn·lli·l·i·alii clm rbonier
- `088_323r_R5655_P5 C02`: ecg ip n ihg corte·ialca·reso ·elloro
- `088_323r_R5655_P5 C03`: ·n·uaioni il· erlparte ·ab iilmosa do
- `088_323r_R5655_P5 C04`: i i·lu···letr······· icl e·era·i icl····e e
- `088_323r_R5655_P5 C05`: moti·uoll·l·gdb·u·ita ilneutr····ta i
- `088_323r_R5655_P5 C06`: la elsuezeidsle·nl a eleaom·ime l
- `088_323r_R5655_P5 C07`: anolei medeih·lloeplicato ildito ·g·e
- `088_323r_R5655_P5 C08`: lalbtrihe taci·utolaad·cesarea ilsu
- `088_323r_R5655_P5 C09`: dio m···············ile soahe ispiaciutol
- `088_323r_R5655_P5 C10`: a ileidendo ogni·oas·cs··s·onta···ri
- `088_323r_R5655_P5 C11`: leno················nal·uonalilfra lelcoron
- `088_323r_R5655_P5 C12`: e e··nldouemo noice·altra·n··ciare ila
- `088_323r_R5655_P5 C13`: neg· ihe santloea ihi piuli esolris
- `088_323r_R5655_P5 C14`: orgonolifacolta·ulco nuoui acident
- `088_323r_R5655_P5 C15`: ili lorena ihu piulmerito ellode sa
- `088_323r_R5655_P5 C16`: ranoldegni lcm ille·mu·i···i·eli for·
- `088_323r_R5655_P5 C17`: col···e·nirela··········illuogo···erzole sosp
- `088_323r_R5655_P5 C18`: enione doi e············· bisogna· ilpotr
- `088_323r_R5655_P5 C19`: ebe·zhd cosa loc laliscorsooe meco
- `088_323r_R5655_P5 C20`: a·nll parireliai·lo rieosciuto ile pa
- `088_323r_R5655_P5 C21`: rte iia resalpur uiuo·i peniero iln
- `089_323v_R5655_P6 C01`: / i ·iz···················galare·ur·i·eli in |

## R5656

- `094_337r_R5656_P5 C01`: i·uoum lidoeaole r· b i·p· rauap
- `094_337r_R5656_P5 C02`: iuadoasei p·dati·i l uoceg eom ·ta
- `094_337r_R5656_P5 C03`: l ·lm ·ong·iaa·suanir···f·doplba
- `094_337r_R5656_P5 C04`: caduta ··rati·r ola··l· inip··giar
- `094_337r_R5656_P5 C05`: ·eita·esmin nt· eid· smigbm · ·d·l
- `094_337r_R5656_P5 C06`: ·······························································
- `094_337r_R5656_P5 C07`: uiua·e iileii ··l·dl·sra ··e·lab
- `094_337r_R5656_P5 C08`: io·potuto spultar·· ecor·ap rale
- `094_337r_R5656_P5 C09`: torolei ·z· re·om·ne··ral
- `094_337r_R5656_P5 C10`: u i sara·poi·coua·dap utolr berio
- `094_337r_R5656_P5 C11`: l· alat·n· ··guita·· sle sia·e i·
- `094_337r_R5656_P5 C12`: l · mraland tdm souitorio··ole·ldop o
- `094_337r_R5656_P5 C13`: lri··uate·ileiu··glu·e li·c
- `094_337r_R5656_P5 C14`: ·oportuna·a par··ta·i·e·la·fdailb
- `094_337r_R5656_P5 C15`: opisarau·i·pensa ipzcol·pll
- `094_337r_R5656_P5 C16`: sll·l· lne ilmzg

## R5657

- `098_342r_R5657_P4 C01`: d· uo ritpouaa due·c··e··dhaotgl zg u
- `098_342r_R5657_P4 C02`: ·ti· pasato ·i· a·ag g ·ic· ete rispoldol
- `098_342r_R5657_P4 C03`: a·pa rt· e·la·du·· i··lilpro·u·i··las
- `098_342r_R5657_P4 C04`: ann rano i·i · ·s· io i·lo lau·ra potu
- `098_342r_R5657_P4 C05`: sglmpim r i··b auad·e·ta··hmmnlis
- `098_342r_R5657_P4 C06`: · ·lilpregm·i·a·ggb·a·bin pololo·ldisfciatel
- `098_342r_R5657_P4 C07`: m p·t·tise e··omo ra·· raar·co·li lalac ria
- `098_342r_R5657_P4 C08`: ·i punti ufle omsc··comiciar llip··u·faci
- `098_342r_R5657_P4 C09`: li·d· pe hl lla coiem·cnis·nh i igr·g·m ·
- `098_342r_R5657_P4 C10`: cose ielpuo e··e o·dul·fl e· ·dub·
- `098_342r_R5657_P4 C11`: iml raci· olr··osal···ai i·impoi·to
- `098_342r_R5657_P4 C12`: il · re·l eiu·nturalib ·agiusa so
- `098_342r_R5657_P4 C13`: cneim· o ed la part·i·m it suilupt to uno
- `098_342r_R5657_P4 C14`: mzi·l·r· i·sra e·· ·pigbdls l l·tri
- `098_342r_R5657_P4 C15`: ·i sono egi· lsi lau·lauhra·eillu so·a·
- `098_342r_R5657_P4 C16`: ni ·t·n· i·d·emc r ·nzacomiion· ls
- `098_342r_R5657_P4 C17`: ·sico lg ·cono·i·i··r iamdio a iuiar
- `098_342r_R5657_P4 C18`: e il itoill pralo i··o ito·c··eb lao coda
- `098_342r_R5657_P4 C19`: a·i th ngono l ll · li i edora irelra
- `098_342r_R5657_P4 C20`: g·l ie in·e · o e·p···po·ono fieri·e poso
- `098_342r_R5657_P4 C21`: aicurarh i·c·llabi··bio adlducuir· ·i·s
- `099_342v_R5657_P5 C01`: / aoib e ··rade tei·
- `099_342v_R5657_P5 C02`: ·i·ild·
- `099_342v_R5657_P5 C03`: col·
- `099_342v_R5657_P5 C04`: o i·i isp·
- `099_342v_R5657_P5 C05`: ·a ·e·
- `099_342v_R5657_P5 C06`: oe don·o ea
- `099_342v_R5657_P5 C07`: suoa·aiar·e · ·a

## R5658

- `102_344r_R5658_P1 C01`: ·
- `102_344r_R5658_P1 C02`: ·
- `102_344r_R5658_P1 C03`: ·
- `102_344r_R5658_P1 C04`: ·
- `102_344r_R5658_P1 C05`: ·
- `102_344r_R5658_P1 C06`: ·
- `102_344r_R5658_P1 C07`: ·
- `102_344r_R5658_P1 C08`: ·
- `102_344r_R5658_P1 C09`: ·
- `102_344r_R5658_P1 C10`: ·
- `102_344r_R5658_P1 C11`: ·
- `102_344r_R5658_P1 C12`: ·
- `102_344r_R5658_P1 C13`: ·
- `102_344r_R5658_P1 C14`: ·
- `102_344r_R5658_P1 C15`: ·
- `102_344r_R5658_P1 C16`: ·
- `102_344r_R5658_P1 C17`: ·
- `102_344r_R5658_P1 C18`: ·
- `102_344r_R5658_P1 C19`: ·
- `102_344r_R5658_P1 C20`: ·
- `102_344r_R5658_P1 C21`: ·
- `102_344r_R5658_P1 C22`: ·
- `102_344r_R5658_P1 C23`: ·
- `103_344v_R5658_P2 C01`: / ·
- `103_344v_R5658_P2 C02`: ·
- `103_344v_R5658_P2 C03`: ·
- `103_344v_R5658_P2 C04`: ·
- `103_344v_R5658_P2 C05`: ·
- `103_344v_R5658_P2 C06`: ·
- `103_344v_R5658_P2 C07`: ·
- `103_344v_R5658_P2 C08`: ·
- `103_344v_R5658_P2 C09`: ·
- `103_344v_R5658_P2 C10`: ·
- `103_344v_R5658_P2 C11`: ·
- `103_344v_R5658_P2 C12`: ·
- `103_344v_R5658_P2 C13`: ·
- `103_344v_R5658_P2 C14`: ·
- `103_344v_R5658_P2 C15`: ·
- `103_344v_R5658_P2 C16`: ·
- `103_344v_R5658_P2 C17`: ·
- `103_344v_R5658_P2 C18`: ·
- `103_344v_R5658_P2 C19`: ·
- `103_344v_R5658_P2 C20`: ·
- `103_344v_R5658_P2 C21`: ·
- `103_344v_R5658_P2 C22`: ·
- `104_345r_R5658_P3 C01`: / esrin·ci·s iuolonta illl l·a·io
- `104_345r_R5658_P3 C02`: sara ·mtre·l iseso i···
- `104_345r_R5658_P3 C03`: adelpite le partiapre so ·o i
- `104_345r_R5658_P3 C04`: apreao lluohni·re sa giusi·mrc·to e
- `104_345r_R5658_P3 C05`: c· h·ba·o· elm prim·· iib·l·l······ |

## R5659

- `110_351r_R5659_P7 C01`: · opo i·c ·ie i uend·z· e··lpa·i·aa sa
- `110_351r_R5659_P7 C02`: ·
- `110_351r_R5659_P7 C03`: ·
- `110_351r_R5659_P7 C04`: ·
- `110_351r_R5659_P7 C05`: ·
- `110_351r_R5659_P7 C06`: ·
- `110_351r_R5659_P7 C07`: ·
- `110_351r_R5659_P7 C08`: ·
- `110_351r_R5659_P7 C09`: ·
- `110_351r_R5659_P7 C10`: ·
- `110_351r_R5659_P7 C11`: ·
- `110_351r_R5659_P7 C12`: ·
- `110_351r_R5659_P7 C13`: ·
- `110_351r_R5659_P7 C14`: ·
- `110_351r_R5659_P7 C15`: ·
- `110_351r_R5659_P7 C16`: ·
- `110_351r_R5659_P7 C17`: ·
- `110_351r_R5659_P7 C18`: ·
- `110_351r_R5659_P7 C19`: ·
- `110_351r_R5659_P7 C20`: ·
- `110_351r_R5659_P7 C21`: ·
- `110_351r_R5659_P7 C22`: ·

## Exposure

- I read the brief, and the plan, the frozen read, the key and the code of the earlier key-free work.
- The brief sent me to the public `francia-346-leaves/README.md`, and I read it.
- That README states results of a check against the published key, as `DECLARE.md` section 7 lists. I used none of them to change a reading.
- So the key is frozen and comes from the ciphertext alone. But the analyst saw those outside facts before writing the text above (a reviewer's point).
- I opened no key file, no grade file, no clear text, no image and nothing in the sealed decode folder.

## Files

- `DECLARE.md`: the declaration.
- The code and the result files of the read stay in local files. They are not in this folder.
