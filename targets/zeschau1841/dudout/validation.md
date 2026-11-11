# zeschau1841, R5005: held-out measure of the segmentation (11 Nov 2026)

- Proposer: Fable 5.2, on R5005 without a3 and a7 (2,905 digits); rule and predictions in its report (its section 3).
- Pre-registration written and hashed before a3/a7 were segmented: rule (verbatim), a3/a7 read as two separate streams,
  offsets 0-3 tried at the start of each block (best kept; controls get the same maximum), every group counted.
- Decision fixed in advance: confirmed if in-form share ≥ 0.95 and above the maximum of every control; partial if
  0.80-0.95 and above the controls; refuted otherwise.
- Calibration on the blocks Fable saw (in-sample for the rule): real 0.977-1.000 per block; controls 0.60-0.65, never above 0.72.
- Held-out data: a3 (3 lines, 177 digits) + a7 (12 lines, 682 digits) of `../ct_R5005.txt`
  (SHA-256 6db0807ff5b42f8bcc294409f99ca92f08e748dccb6c293c1a31bd766bc48069). These lines had been glimpsed as raw digits
  on 5 Nov in an earlier, failed probable-word test, but never segmented. Daniel's own annealers saw all of R5005.

| measure | a3 + a7 | controls (mean / max) | prediction | held |
|---|---|---|---|---|
| groups in the forms | 0.983 (291/296), offset 0 in both | digits 0.641/0.703; pairs 0.630/0.700; synthetic pairs 0.601/0.667 | ≥ 0.95, above every max | yes |
| [2579]x groups ending 1/3/4/6/8 | 0.984 (186) | 0.50-0.56 / 0.70 | ≥ 0.95 | yes |
| [3468] pairs with 2nd digit 1/3/4/6/8 | 0.970 (33) | | ≥ 0.90 | yes |
| immediate repetitions | 0 | 3.3 (group order shuffled) | ≤ 1 | yes |
| glossed groups present | 711 ×3, 708 ×3, 746 ×4, 294 ×7, 234 ×0 | | ≥ 3 of 5 | yes |
| tokens of an already-seen type | 0.956 | 0.49-0.55 / 0.62 | ≥ 0.85 | yes |
| `06777818711001` | 1 occurrence (a7), cut 06\|7778\|18\|711\|001x | | as predicted | yes |

Verdict: confirmed (structure). No values were measured. Lengths in a3+a7: 68 × 2, 186 × 3, 41 × 4, 1 × 1 (the last
digit of a7). Our local files: PREREG-SEG-C04.md SHA-256 28118ac78a8cb0eacbe00a9512526058dceed08bf1405b3028d79803d8762816,
measurement output feea13e29e6c2041f07930047abf7a63a8ba13fb18ff812b446f04c7d1c956b3 (available on request).
