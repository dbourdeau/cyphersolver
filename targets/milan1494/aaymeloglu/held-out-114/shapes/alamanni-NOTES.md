# Alamanni shape check - families A (÷-like) and B (tall stem signs)

Shape-only pass. Inputs used: 220v.jpg, 221r.jpg, 221v.jpg, labels.tsv (this directory only). No values, no other files.

## Method
- Line positions calibrated by eye on gridded leaf overviews (`work/lines.py`); lines slope down to the right.
- Every cipher line cut into two ruled strips (2x) and the label sequence walked token by token to get a raw x for each target (`work/targets.py`), then each target re-centred on a ruled 4x context tile (`work/adjust.py`).
- Cut-outs: `A/<id>_<j>.png` (64x60 raw px, 5x LANCZOS), `B/<id>_<j>.png` (52x70 raw px, 6x). Contact sheets `sheets/A_sheet_*.png`, `sheets/B_sheet_*.png` (A/ and B/ hold only the 31 and 34 cut-outs) (contrast-stretched colour, tile names only; B order seeded-shuffled). Doubtful ones re-read at 7-8x in colour + stretched grey (`work/zA.png`, `work/zB1.png` .. `work/zB4.png`).
- Calls are keyed by id|j in `work/write.py`; the `label` column of B.tsv is joined by script afterwards.
- `raw_x` = x of the sign centre in the 1272-px leaf image; approximate raw y is in the note as `[raw_y~N]`.

## Blindness caveat
I read labels.tsv to locate signs, so I knew which B targets carried `5`, `Zd`, `b` before classing them. Classes were assigned from features on the shuffled sheet, but this is not a fully label-blind sort. The scans are low-resolution JPEGs (a dot is 3-5 px), so fine detail is limited.

## Family A - 31 located of 31
| dots | n | dash |
|---|---|---|
| above only | 13 | 10 straight, 2 tilde ("other"), 1 sloping |
| below only | 10 | 9 arched, 1 unbounded convex line ("other", 220v:20.1) |
| above + below | 8 | 4 arched, 3 straight, 1 sloping |
| none / unclear | 0 | |

- Above-only: the mark sits over the RIGHT end of the dash and is often a small slanted tick rather than a round dot. Dash straight (often with the left end hooked down).
- Below-only: one round dot centred under a dash that is always convex-up (arched, ends turned down). Nothing above in any of the 10.
- Above+below: tick over the right end plus a dot under the left/centre.
- By leaf: 220v 9 above / 3 below / 1 both; 221r 4 / 3 / 5; 221v 0 / 4 / 2.
- 220v:20.1 j0: dot below is clear, but the "dash" is a long convex-up line that appears to come out of the preceding clear word's flourish and runs on to the right; dash recorded as other/low.
- Low confidence: 220v:21.4 j2 (faint tick above; "above" likely), 221r:3.4 j0 (above certain, lower mark faint - could be above-only).
- The below-only + arched combination looks like a distinct sign form from the above-only + straight one; above+below is mixed on dash shape.

## Family B - 34 located of 34 (18 `5`, 14 `Zd`, 2 `b`; no `pb` or `Z` tokens exist in labels.tsv)
Feature classes:
- **B1 (12)** - tall right-leaning stem, a leftward kink at about baseline, then a tail running down-left below the line (zigzag / S-curve). No arm, no bowl, no bar. Two have the top turned over in a small hook (221r:1.2 j0, 221v:2.6 j0).
- **B2 (2)** - B1 body plus a long curved bar crossing the upper stem (221r:6.5 j0, 221r:8.2 j4).
- **B3 (18)** - a "5" with a tall ascender: stem comes down to about baseline, turns at a sharp corner into a horizontal arm going RIGHT, and a tail drops down-left from under the arm. On the clean specimens (220v:13.1 j5, 220v:14.1 j3, 221r:2.2 j2, 221r:10.2 j0, 221r:17.1 j2, 221v:4.2 j2) the arm starts at the stem foot with at most a 1-2 px pen-start nib to the left; it does not pass through the stem, and it sits at baseline, not on the ascender. No bowl on either side, no bar across the ascender. Five specimens have a dark ink knot at the stem-arm corner (221r:2.4 j2, 221r:3.4 j4, 221r:17.2 j0, 221r:18.3 j0, 221v:4.6 j0); at this resolution a very small filled loop at the corner cannot be excluded for those five, so all five are marked low.
- **B4 (2)** - short upright stem with a closed bowl at its right foot (b-like), no bar (220v:7.1 j4, 220v:8.1 j2).

Cross-tab against existing labels (joined after the calls): `5` -> B3 16/16; `5{Zd}` -> B3 2/2; `Zd` -> B1 11, B2 2; `Zd{5}` -> B1 1/1; `b` -> B4 2/2.

### Every `5`: (i) d-like crossed, (ii) b-like crossed, or (iii) open with foot to the right?
All 18 are **(iii)**. None shows a bowl left of the stem and none has a clear bar across the ascender. 13 show no closed bowl at the foot; the other 5 have an ink knot at the stem-arm corner (list above) where a tiny filled loop is not excluded - nothing the size of the B4 bowls. 10 of 18 are high confidence, 8 low. Reservations:
- 220v:7.2 j1 - arm is arched (h-like) and joins the next sign; still open, no bar. Low.
- 221v:4.1 j2 - short tick on the left of the upper stem; may be a stray from the line above or a cross-stroke. Lower part is clearly open with an arm. Low on the top.
- 221v:4.6 j0 - the heaviest of the five corner knots. Low.
- 221r:1.3 j3 - ascender broken/faint; arm visible. Low.
- 220v:10.3 j2 - lower part clear; stem overlain by a descender from the line above, top not judged.
The two `5{Zd}` (220v:7.2, 221r:18.3) have the arm (B3); the `Zd{5}` (221v:2.6) has none (B1).

## Not in scope but seen
- 220v:21.4 j5 (label `?`, raw x~1088, y~1520): a d-like sign (filled bowl LEFT of the stem) with a bar crossing the ascender. This is the only d-like crossed form I met; it is not labelled `5`.
- 220v:13.1 j7 `Zo` not included (different label).
- 221v:3.3: the last two tokens (`x c`) are written at the start of line 4, not on line 3. No effect on targets.

## Signs not located
None. For every target the neighbouring signs on its tile agree with the label sequence around it (I checked neighbours, not full per-unit token counts).
