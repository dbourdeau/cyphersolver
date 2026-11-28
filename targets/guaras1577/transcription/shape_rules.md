# Shape check of the statistical sign groups, SP 70/143 f. 93 (Guaras, 15 Feb 1577)

Written 28 Nov 2026 by the AI agent that did the shape comparison. No decoding was done, no values were used, and
no key or edition was opened. Sources: `work_A/s/` line strips, the two page images, `transcription_final.txt`,
`shape_groups_training.tsv`. All crops and working files are in `work_D/`.

## Method

- The two halves of each line strip were joined into one image, with the 120-pixel overlap removed
  (`work_D/full/PnLnn.png`). Ink blobs were boxed and numbered (`work_D/ruler/PnLnn_cc.png`). Each listed instance was
  then found by hand: I counted along the line against the transcription, using the context column.
- Training crops: `work_D/crops/<group>_<line>_<index>.png`. Contact sheets, one row of crops per group:
  `work_D/sheet_<sign>.png`, `work_D/wide_uy1.png` / `wide_uy2.png`, `big_T1.png` / `big_T2.png`, `cmp_T1_right.png` /
  `cmp_T2_right.png`, `big_t1_small.png` / `big_t2_small.png`, `cmp_Z-1.png` / `cmp_Z-2.png` / `cmp_Z-3.png`.
- Token index = the position in the line with `W1` written as `uy T`, `W2` as `uy P`, `u y` as `uy`, and `|` left out.
  All 136 rows of the tsv matched this count and their context strings.
- One listed instance could not be cropped: P1L11 index 55 (t-2). It lies at the right edge, past the end of the strip.

## uy: one consistent rule found (used for part 2)

**Rule.** Count the short minims written before the long descending stroke.
- **uy-1 (left as `uy`, W1, W2):** three short minims, then the long stroke. The sign looks like `uu` plus a descender.
- **uy-2 (new name `uy2`):** only two short minims (a plain `u`), then the long stroke. The sign looks like `u` plus a
  descender.

The height of the long stroke, any loop at its top, and the crossbar belong to the following T or P. They do not
separate the groups.

**Counts from part 1:** uy-1: 14 of 15 fit (misfit P2L13 index 2, which shows two minims). uy-2: 13 of 15 fit
(misfits P1L06 index 7 and P1L21 index 31, which both show three minims). In all, 27 of 30 fit (90%).

**Crops that show it:** `work_D/rule_uy.png` (top row uy-1, middle row uy-2, bottom row the three misfits). Also
`work_D/big1.png` to `big5.png`.

**Part 2.** I cropped all 207 `uy` occurrences in the 47 lines (`work_D/crops_all/uy_<line>_<index>.png`; sheets
`work_D/all_uy_00.png` to `_08.png`). I classified each by the rule, crop by crop, without the group list
(`work_D/class_uy.tsv`). 30 of these are the training instances, which I had already seen. Results:
- three minims, left unchanged: 111
- two minims, relabelled `uy2`: 93
- unreadable, marked `uy?`: 3 (P1L07 index 50, which runs off the right edge of the strip; P1L10 index 0, cut by the
  left edge of the strip; P2L14 index 14, where the first stroke may be a minim or part of the `?` sign before it, so
  the minim count is unclear)

Page totals: f. 93r (P1) 77 unchanged / 62 `uy2` / 2 `uy?`. f. 93v (P2) 34 unchanged / 31 `uy2` / 1 `uy?`.

The relabelled `uy2` occurrences break down as 21 `uy2 T` (from W1), 48 `uy2 P` (from W2) and 24 standing alone.

Because of the downhill slant on f. 93r, the ends of P1L31 and P1L32 were read from the strip of the next line, where
those words appear. These are P1L31 indexes 42, 44 and 50, and P1L32 indexes 35 to 48.

**Per line: unchanged / `uy2` / `uy?`**

| line | unchanged | uy2 | uy? |
|---|---|---|---|
| P1L01 | 2 | 1 | 0 |
| P1L02 | 2 | 4 | 0 |
| P1L03 | 4 | 1 | 0 |
| P1L04 | 1 | 2 | 0 |
| P1L05 | 2 | 3 | 0 |
| P1L06 | 2 | 3 | 0 |
| P1L07 | 3 | 1 | 1 |
| P1L08 | 2 | 1 | 0 |
| P1L09 | 4 | 2 | 0 |
| P1L10 | 1 | 2 | 1 |
| P1L11 | 2 | 0 | 0 |
| P1L12 | 4 | 2 | 0 |
| P1L13 | 4 | 3 | 0 |
| P1L14 | 2 | 3 | 0 |
| P1L15 | 3 | 1 | 0 |
| P1L16 | 1 | 2 | 0 |
| P1L17 | 2 | 0 | 0 |
| P1L18 | 1 | 0 | 0 |
| P1L19 | 1 | 0 | 0 |
| P1L20 | 1 | 3 | 0 |
| P1L21 | 3 | 0 | 0 |
| P1L22 | 5 | 2 | 0 |
| P1L23 | 3 | 0 | 0 |
| P1L24 | 1 | 3 | 0 |
| P1L25 | 1 | 2 | 0 |
| P1L26 | 2 | 3 | 0 |
| P1L27 | 2 | 3 | 0 |
| P1L28 | 3 | 0 | 0 |
| P1L29 | 1 | 2 | 0 |
| P1L30 | 5 | 1 | 0 |
| P1L31 | 0 | 6 | 0 |
| P1L32 | 4 | 3 | 0 |
| P1L33 | 3 | 3 | 0 |
| P2L01 | 2 | 3 | 0 |
| P2L02 | 3 | 2 | 0 |
| P2L03 | 1 | 3 | 0 |
| P2L04 | 3 | 2 | 0 |
| P2L05 | 1 | 3 | 0 |
| P2L06 | 4 | 1 | 0 |
| P2L07 | 1 | 6 | 0 |
| P2L08 | 3 | 3 | 0 |
| P2L09 | 2 | 0 | 0 |
| P2L10 | 4 | 0 | 0 |
| P2L11 | 2 | 3 | 0 |
| P2L12 | 4 | 4 | 0 |
| P2L13 | 3 | 1 | 0 |
| P2L14 | 1 | 0 | 1 |

`transcription_final_v2.txt` is `transcription_final.txt` with only these changes:
- a two-minim `W1` / `W2` became `uy2 T` / `uy2 P`, keeping any `~`;
- a two-minim `u y` became `uy2`;
- the three unreadable ones became `uy?` (all three are standalone `u y`).

Turning `uy2` and `uy?` back into the original tokens gives the original file exactly. SHA-256 of v2:
`b17ba320df7ef9f3ab358984bb53798de730e92714720790f98655f90c40a5b1`.

The two `u~ y` in P1L24 and P1L29 are not counted as `uy` in the tsv's tokenization. They were left unchanged.

**Limits.** At this resolution, a third minim joined tightly to the next one can look like two minims. I expect a few
percent of the full-text labels to be wrong, about the same as the 3 misfits in 30 training instances.

## t: a clear tendency, below the 80% threshold (not relabelled)

**Difference seen.** In t-1, the horizontal stroke comes in from the left and stops at the short upright: it joins but
does not cross. In t-2, the horizontal often runs through the upright and out to the right, making a true cross (+).

**Counts from part 1:**
- t-1: 15 of 15 fit (bar stops at the upright).
- t-2: 8 of 15 fit (bar crosses). 5 show the bar stopping (P1L04 index 6, P1L12 index 14, P1L19 index 9, P1L19
  index 45, P1L28 index 38). 1 is unreadable (P1L33 index 38). 1 is off the strip (P1L11 index 55).
- In all, 23 of 30 (77%), or 23 of 28 among those that could be judged.

So the rule describes t-1 well but splits t-2. No other feature separated the five t-2 misfits: not the height of
the upright, its slant, or the left-hand sign the bar comes from. **Not applied to the transcription.**

Crops: `work_D/rule_t.png` (top row t-1, middle row t-2, bottom row the t-2 misfits), `big_t1_small.png`,
`big_t2_small.png`.

For information only, I also sorted all 187 `t` occurrences with the same rule: 106 stop, 70 cross, 11 unreadable
(`work_D/class_t.tsv`, crops `work_D/crops_all/t_*.png`). This sort is **not** in v2.

## T: no consistent difference

Both groups show the same sign. A tall upright on the left is joined by a crossbar to a short upright on the right,
and the left upright descends below the line.

The only variable feature is whether the crossbar runs on past the short right upright:
- T-1: 13 of 15 do not run past (P1L17 index 3 and P1L02 index 20 do).
- T-2: 7 of 15 run past (P1L05 index 11, P1L06 index 45, P1L07 index 8, P1L26 index 4, P2L08 index 20, P2L11 index
  11, P2L11 index 38); 6 do not; 2 are blurred (P1L20 index 45, P1L21 index 36).
- In all, about 20 of 30 (67%).

Spacing, height, slant and the loop of the left upright look the same in both groups.

Crops: `work_D/big_T1.png`, `big_T2.png`, `cmp_T1_right.png`, `cmp_T2_right.png`.

## Z: Z-1 differs from Z-2 and Z-3; Z-2 and Z-3 do not differ (not relabelled)

- **Z-1:** a large 3-shaped sign whose lower bow sweeps round to the right and ends in a tail running right or up to
  the right. 10 of 11 fit (P1L33 index 1 has its tail going down to the left).
- **Z-2:** a small hooked head, then a straight stroke running diagonally down to the lower left, often ending in a
  blob or curl. A crossbar often touches it, which is usually the bar of the following t or P. 10 of 10 fit this
  shape.
- **Z-3:** the same shape as Z-2 in 8 of 10. P1L07 index 11 and P2L10 index 44 have the Z-1 right-sweeping or round
  lower bow.

No feature that I could see separates Z-2 from Z-3. I checked head size, tail length, the blob at the end of the
tail, and the crossbar.

Merging Z-2 and Z-3, a two-way rule (lower stroke sweeps right versus runs down to the left) fits 28 of 31 (90%). The
three-way grouping, however, is sorted correctly for at most about 20 of 31 (65%). Since it does not reproduce the
listed grouping, **I did not apply it**. Say if a two-way `Z` / `Z2` relabelling is wanted.

Crops: `work_D/cmp_Z-1.png`, `cmp_Z-2.png`, `cmp_Z-3.png`, `sheet_Z.png`.

## b: only one group was listed

The tsv lists 15 instances of b, all in group b-1, so there is no second group to compare. The 15 crops look alike: a
tall stem with a closed round bowl, often with a joining stroke out to the right into the next sign. Not relabelled.

Crops: `work_D/sheet_b.png`.
