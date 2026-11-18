# Blind shape sort, families A (N) and B (Z / 5 / pb / b)

Inputs used: `masked/` crops + `manifest.tsv` + `blocks.md`, and `transcription-frozen.tsv` (to locate signs only). Nothing else was opened. No values were used or looked for. Classes were assigned from the contact sheets with tile names only; `label_in_transcription` was joined by script afterwards and was not tabulated against class.

## Counts and location

- Family A: 90 signs with first label `N` (incl. `N?`). All 90 cut out.
- Family B: 117 signs with first label exactly `Z`, `5`, `pb`, `b` (`Zx` never occurs as a first label). All 117 cut out. The six null tokens `Z°` / `Z°x` are NOT included (different first label); with them the total would be 123.
- Not located: 1 (A `c258v_L17_8`, see below; a cut-out of the place where it should be is saved anyway). All other targets were found by walking each line's tokens against the image; on no line did I lose my place. Only the targets were recorded (x-range each); positions of the non-target tokens were checked by eye while walking and are not saved, so the token-count agreement has no artefact behind it beyond the cut-outs landing on the right kind of sign with x increasing with k.
- The same reader saw the transcription labels while locating the signs (unavoidable), but classes were assigned later from name-only sheets.
- Insecure locations (cut-out exists, but treat as doubtful):
  - A `c258v_L17_8`: only one dash is visible between `o` and `oo`, and it runs into the next sign like that sign's own lead-in stroke. A separate N is not visible.
  - A `c259v_L16_25, _26, _30, _33`: the pale brownish dashes already flagged in the transcription; different colour from the cipher ink.
  - A `c259v_L17_35`: only a faint dot/smudge, no clear dash.
  - A `c259v_L8_31` / B `c259v_L8_32`: adjacent, in a yellow stain; the B stroke is pale yellow-brown, not the usual ink.
  - B `c259v_L3_2`: the boundary-doubt sign of the transcription; messy.
- `raw_x` = approximate x of the sign centre in raw-image pixels (crop x0 + crop_x/3), about +-4 px.
- k = 0-based token index over all non-clear rows of the leaf+line (null rows counted).

Resolution limit: signs are ~20-30 raw px tall, a dot is 1-2 raw px.

Masking limit (measured): painted-out areas are perfectly flat colour (7x7 local std ~0, paper >= 1), so I measured the painted fraction next to every sign. Paint is nearly everywhere: both ABOVE the cipher line (its own gloss) and BELOW it (gloss of the next line). The cipher ink survives as islands that the masker chose to keep. Consequences:
- A: in the strip 3-12 raw px above / below the dash, the EMPTY side is >= 50% painted for 21 of 25 dotless signs (above) and 18 of 25 (below), for 16 of 21 below-only signs (above side) and 26 of 34 above-only signs (below side). So "no dot" on a side almost always means "the masker kept no dot there", not "bare paper shows no dot". Columns `painted_frac_above` / `painted_frac_below` in A.tsv give this per sign. Presence of a dot is reliable; absence is only as reliable as the masking.
- B: 95 of 117 stem tips have >= 50% paint in the 8 raw px above them (`painted_frac_at_tip`). A stem cut flush by paint looks like a T-cap, and a top bar or flag could have been painted away. Only 11 "top = none" signs have mostly paper above the tip. Rectangular dark stubs/notches at stem tips are masking remnants and were not counted as bars unless the bar clearly continues as ink on both sides.
- The `confidence` column is confidence in what the visible ink shows, not confidence that nothing was painted out.

## Family A (dash with dots)

| dots seen | all | high confidence |
|---|---|---|
| above only | 34 | 26 |
| below only | 21 | 18 |
| above and below | 4 | 4 |
| no dot visible | 25 | 16 |
| unclear | 6 | 0 |

So the family is not one uniform ÷: clear above-only, below-only, both, and dotless forms all occur many times.

Things that co-vary (high-confidence items only):
- dot below goes with an ARCHED dash (convex up, like a breve over the dot): 13 of 18. Examples `c258v_L16_11`, `c258v_L20_23`, `c258v_L23_13`, `c259v_L8_13`, `c259v_L10_22`, `c259v_L21_16`.
- dot above goes with a straight or down-right sloping dash: 20 of 26 not arched. Examples `c258v_L14_18`, `c258v_L19_7`, `c259v_L7_19`, `c259v_L11_16`, `c259v_L20_7`. The dot above is very often right of centre and often a slanted tick rather than a round dot (`c259v_L14_16`, `c259v_L18_18`, `c259v_L20_29`).
- above+below: always a straight dash (`c258v_L16_17`, `c258v_L21_11`, `c258v_L23_25`, `c259v_L10_15`).
- no dot: mostly an arched dash / tilde (12 of 16): `c258v_L19_12`, `c259v_L11_23`, `c259v_L12_8`, `c259v_L12_11`, `c259v_L17_33`. A few straight dotless dashes (`c259v_L9_9`, `c259v_L12_16`).
- Caveat on "none" and on one-sided dots: see the masking limit above. A dot could have been painted out on either side, so the dotless group (and the above-only / below-only split) cannot be confirmed from the masked crops; it needs a check on the unmasked image by someone allowed to open it. What the masked crops do establish: dots above and dots below both certainly occur, and the dash shape differs (arched vs straight) in step with where the visible dot is. The arched dotless dashes share the dash shape of the below-dot form.
- Dash length: measured as horizontal ink extent in raw px (`dash_len_raw_px`). It is unimodal, 15-27 px for 76 of 88 measurable signs with a thin tail to 39 px; "long" in A.tsv = >= 28 px (12 signs). Length does not form groups.

## Family B (tall stem signs)

Classes, defined by ink features only:

| class | definition | n (high/low) | examples |
|---|---|---|---|
| B1 plain hook | slanted tall stem, NO top bar; lower part an open angular hook/zigzag with tail down-left; no arm, or only a tiny notch, to the right | 29 (25/4) | `c258v_L14_0`, `c258v_L20_11`, `c259v_L7_4`, `c259v_L10_29`, `c259v_L19_30`, `c259v_L21_14` |
| B2 hook with arm | as B1 (no top bar) but a distinct horizontal stroke leaves the stem to the right at about baseline height (h/4-like) | 33 (30/3) | `c258v_L16_1`, `c259v_L3_18`, `c259v_L5_3`, `c259v_L5_26`, `c259v_L11_19`, `c259v_L18_22` |
| B3 barred b | CLOSED round bowl at the foot of the stem + a bar at the stem top, either crossing it (stem pokes above) or capping it (T-like) | 24 (16/8) | crossed: `c258v_L14_13`, `c258v_L20_0`, `c259v_L5_13`, `c259v_L7_0`, `c259v_L19_28`; T-cap: `c258v_L17_5`, `c258v_L23_20`, `c259v_L8_17`, `c259v_L15_17` |
| B4 plain b | closed bowl, stem with NO bar | 7 (3/4) | `c258v_L16_26`, `c259v_L6_0`, `c259v_L14_20` |
| B5 crossed d | bowl to the LEFT of a right-leaning stem (d-like), stem crossed by a long bar | 9 (6/3) | `c258v_L15_37`, `c258v_L16_22`, `c258v_L23_18`, `c259v_L7_9`, `c259v_L11_25`, `c259v_L17_29` |
| B6 barred hook | open hook lower part (as B1/B2) + a bar across or on top of the stem | 14 (6/8) | `c259v_L6_20`, `c259v_L9_4`, `c259v_L12_29`, `c259v_L14_18`, `c259v_L14_21`, `c259v_L14_25` |
| B0 other | `c259v_L8_16`: short zigzag under a flat top bar, no ascender | 1 (0/1) | |

How solid the boundaries are:
- Closed bowl (B3/B4/B5) versus open hook (B1/B2/B6) is the clearest split; almost never in doubt.
- B5 versus B3: bowl on the left of the stem and long crossing bar versus bowl at the right foot. Clear. Two low-confidence B5 (`c259v_L17_17`, `c259v_L18_13`) have the bar as a cap at the stem tip in a masking-affected zone, and `c259v_L7_40` is a very tall variant with a foot to the right.
- B1 versus B2 (arm or not) is a real, repeated difference at the extremes, but arm length runs continuously from a notch to a long stroke; a handful (`c259v_L3_28`, `c259v_L12_0`, `c259v_L15_5`) sit near the border. Stem height also varies within both (short forms: `c258v_L19_8`, `c258v_L19_10`, `c259v_L5_9`, `c259v_L14_9`, `c259v_L19_16`) without forming a separate group.
- B6: the six high-confidence ones have a bar that is clearly ink crossing the upper stem. The eight low-confidence ones have a flat dark cap or flag exactly at the masking edge (`c258v_L15_23`, `c259v_L9_8`, `c259v_L10_19`, `c259v_L11_8`, `c259v_L15_12`, `c259v_L16_11`, `c259v_L17_19`, `c259v_L3_2`); these may be B1/B2 with a masking remnant. The same applies in reverse to B1/B2/B4 items noted "flag/masking at tip" (`c259v_L13_34`, `c259v_L17_9`, `c259v_L13_21`, `c259v_L17_24`, `c259v_L20_25`): a real top bar could have been cut.
- B3 crossed versus T-cap: crossed (stem visibly continuing above the bar) is certain in several; T-cap is weaker, because a stem cut flush by paint above the bar looks the same. Recorded in the `top` column, not split into classes.
- B1/B2 "top = none": bar absence is established only where paper shows above the tip (11 signs: `c258v_L15_32`, `c258v_L16_1`, `c258v_L20_11`, `c259v_L5_9`, `c259v_L9_29`, `c259v_L11_29`, `c259v_L12_6`, `c259v_L13_32`, `c259v_L16_27`, `c259v_L16_31`, `c259v_L17_15`); for the rest the stem runs into paint. The stems of B1/B2 are however typically much longer than those of B3/B6 and no bar crosses the visible length.
- B0 `c259v_L8_16` sits at the right edge of crop a (raw x ~628-654) and is cut off at the left edge of crop b, so there is no second view of it.
- B4 is small; only three are clean. B4 could be B3 whose bar was masked only for the low-confidence ones; the three high ones show a clean bare stem.
- Single oddities: `c258v_L15_32` knob/dot on the stem tip; `c259v_L21_12` closed loop at the stem top.

## Files

- `A/`, `B/`: cut-outs `<leaf>_L<line>_<k>.png` (3x crop pixels, ~14 px margin).
- `A_sheet.png` (2x of the cut-outs) and `B_sheet.png` (3x), contact sheets in reading order, full names as labels.
- `A.tsv`, `B.tsv`: per-sign records.
