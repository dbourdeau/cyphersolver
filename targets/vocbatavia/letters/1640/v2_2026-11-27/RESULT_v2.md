# 1640 postscript, transcription version 2 (27 Nov 2026 UTC)

The checks were done with AI tools and no person checked each record by hand.

## Bottom line
- Two emendations, both in letter-cipher (system B) words; number tokens unchanged. [measured]
- One re-decode of the letter-cipher words with the frozen LC_KEY_v1: 7/16 = 43.75%, still under our 65% line, controls not clear. [measured]
- The figure of record does not change: the v1 first pass, 5/13 = 38.46% (lc_test/RESULT_LC.md). [derived]

## Emendations (every one listed)
| no. | v1 (frozen 25 Nov 2026 20:58:51 UTC, md5 9b68d68b...) | v2 | source |
|---|---|---|---|
| E1 | after "Amsterdam": nothing | letter-cipher words `k bd. p.` | image (NA 1.04.02 inv. 1134 scan 583); blind reader 2 wrote "te Bd. p."; Dan Bourdeau, review of PR #996 |
| E2 | `qbbm` | `qbhm` | image; blind reader 2 "qbhm"; Dan Bourdeau, review of PR #996 |

Letter-cipher words: 13 in v1, 16 in v2. Reader 2's "te" for "k" is not adopted: the reviewer and the image give "k".

## Freeze
- FREEZE_v2.txt (md5 and `date -u` in one command): 2026-11-27 04:23:58 UTC; T1640_transcription_v2.txt md5 77202d0359683d472985ec0412581f79;
  LC_KEY_v1.tsv a718f1df..., run_lc.py dccab8d2..., score.py e04f5aeb... (all three unchanged from the v1 freeze).
- Stamped: stamps/STAMP_LOG.txt (Sectigo 04:23:59Z, FreeTSA 04:24:00Z, OpenTimestamps submitted; manifest sha256 30c6f3b7...).

## Re-decode (run once, run_lc_v2_output.txt, 04:24:09 UTC)
| word | decode | scorer |
|---|---|---|
| ctld | iohn | accepted (not blind, see RESULT_LC) |
| Gmroodt | dta??no | - |
| k | r | accepted (single letter) |
| bd | en | accepted |
| p | ? | - |
| b | e | accepted (single letter) |
| g | d | accepted (single letter) |
| tpbk | o?er | - |
| lrdgenlm | hands?ht | - |
| grbk | daer | accepted |
| nad | ??n | - |
| m | t | accepted (single letter) |
| bpbkdbsbd | e?erne?en | - |
| Zrpmb | ?a?te | - |
| qbhm | ?e?t | - |
| boode | e??ns | - |

- Words accepted 7/16 = 43.75% (the script labels this line "FIGURE OF RECORD"; for v2 it is not). Four of the seven are single letters.
- Per-letter figures change: letters keyed 45/60 = 75.00% (v1 43/56 = 76.79%). Arithmetic: v1 43/56; E1 adds k (1 keyed), bd (2 keyed), p (0 keyed): +3/+4;
  E2 drops one keyed b for an unkeyed h: -1/0; 43+3-1 = 45, 56+4 = 60.
- Controls: key shuffles >= 7: 9/5,000 (seed 20261112), 12/5,000 (seed 7); letter shuffles >= 7: 235/5,000 and 230/5,000. Not significant.
- Number tokens: load_tokens gives 11 tokens for v1 and v2, identical (number_tokens_check.txt), so the number-cipher figure 9/11 = 81.82% is untouched.

## Effect on the house count
None. The house count (scripts/house_count.py) already counted 16 letter-cipher words and treated all of them as holes; qbbm/qbhm and k, bd, p stay holes.
