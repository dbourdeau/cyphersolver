# Ridolfi 112r / 113r / 113v / 115r - blind shape classification

Shape only. No values were looked up or used; only the files in this directory were read.

## What was done

- Line centres found by ink row-projection on each leaf, then each cipher line cut in four overlapping 4x strips with a raw-x ruler.
- Tokens walked in `labels.tsv` order by eye on every line; raw x recorded for every target sign.
- One 4x LANCZOS cut-out per target in `A/` and `B/`, named `<leaf>_<line.unit>_<j>.png`.
- Shuffled contact sheets with tile names only (`sheet_A_1..4.png`, `sheet_B_1..5.png`). Classes were assigned from these, keyed by tile name, after all sheets had been seen; the `label` column of B.tsv was joined afterwards.
- A second pass on per-class group sheets checked consistency; 18 A tiles and 12 B tiles were re-read at 7x with wider context. Those sheets are in `check/` (`grp_*` = tiles grouped by assigned class, `z*` = zooms).
- `scripts/` holds the locator table (`loc.py`), the tile cutter, the sheet builders and the class files (`clsA.txt`, `clsB.txt`, keyed by tile name; they match the TSVs).
- `raw_x` is an eye-read sign centre from the ruled strips, good to about +/-5 px.

Limits of the blinding: the same reader located and classified, with the label list in hand for locating, and tile names carry the unit id. No label was shown on a tile or sheet, but the reader had seen the labels line by line beforehand. So agreement between label and class (`pb` = B3, `b` = B4) is not independent confirmation. The places where one label splits into several shapes run against that bias and are the stronger result.

## Located

All 108 Family A targets and all 133 Family B targets were located. The label sequence and the images agreed on every line; no unit was lost.

Five targets sit on the leaf line after the one in their id, because the unit wraps (noted per row): 112r:4.13 j5, 112r:9.10 j6, 113v:1.11 j2, 115r:6.12 j4, 115r:10.7 j3. `raw_x` is on the line where the sign is written.

Not in the target set (first label is not N / Z / Zx / 5 / b / pb): `Z°` x6, `Z°x` x1, `NN` x6, `6{pb}` x5, `6{b}` x1.

## Family A (108)

| dots | n | dash straight | sloping | arched | other / unclear |
|---|---|---|---|---|---|
| above | 49 | 38 | 7 | 1 | 3 wavy |
| below | 34 | 9 | 1 | 24 | 0 |
| above+below | 24 | 19 | 2 | 3 | 0 |
| none | 0 | | | | |
| unclear | 1 | | | | 1 cut off by scan edge |

Per leaf (above / below / above+below): 112r 22 / 18 / 12; 113r 14 / 9 / 8 (+1 unclear); 113v 3 / 2 / 1; 115r 10 / 5 / 3.

- Three dot states are real and mostly unambiguous: 101 of 108 are high confidence.
- The dash shape goes with the dots. A below-only sign usually has a convex-up, breve-like dash (24 of 34); above-only and above+below signs almost always have a flat or slightly sloping dash (4 arched of 73). Among below-only signs flat-to-arched is a continuum, so the 9 "straight" there are the flat end of it, not a separate form.
- On 113r the above mark is often a slanted tick right of centre, not a round dot.
- Low confidence (7): 113r:2.15 j2 (cut by scan edge: dot above is visible, below position is not, so dots = unclear), 113r:6.4 j5 (tick far up-right, could be none), 113r:9.2 j0 and 113r:9.10 j1 (brown stains over the sign), 113r:9.10 j4 (above mark very faint), 113v:2.4 j4 (grey smudge below, read as show-through), 115r:9.4 j4 (blob on the dash).

## Family B (133)

| class | n | 112r | 113r | 113v | 115r |
|---|---|---|---|---|---|
| B1 plain hook | 44 | 14 | 19 | 3 | 8 |
| B2 hook with arm | 32 | 17 | 11 | 2 | 2 |
| B3 barred b | 19 | 10 | 5 | 1 | 3 |
| B4 plain b | 10 | 3 | 4 | 1 | 2 |
| B5 crossed d | 14 | 7 | 5 | 0 | 2 |
| B6 barred hook | 13 | 7 | 2 | 1 | 3 |
| B0 | 1 | 1 | 0 | 0 | 0 |

Existing label against shape class (joined after classification):

| label | B1 | B2 | B3 | B4 | B5 | B6 | B0 |
|---|---|---|---|---|---|---|---|
| Z (68) | 44 | 12 | | | | 12 | |
| Zx (1) | | | | | | 1 | |
| 5 (35) | | 20 | | | 14 | | 1 |
| b (10) | | | | 10 | | | |
| pb (19) | | | 19 | | | | |

- `pb` = B3 and `b` = B4 with no exceptions (see the caveat on blinding above).
- Label `5` covers two different shapes: B5 crossed d (14) and B2 hook with arm (20), plus the one B0. B5 and B2 do not look alike.
- Label `Z` covers three shapes: B1 plain hook (44), B2 hook with arm (12) and B6 barred hook (12).
- So B2 (32) is drawn from both labels: 20 `5` + 12 `Z`. The five tokens the transcription already flagged as `Z{5}` / `5{Z}` are all B2 (112r:5.2/0, 17.7/3, 17.9/3, 11.9/0, 12.3/0).
- `Z` tokens that are B2: 112r:5.2/0, 9.5/1, 12.7/0, 14.2/0, 14.5/0, 17.7/3, 17.9/3, 19.6/0; 113r:1.9/0, 2.14/2, 3.2/3, 3.2/6.
- `Z` tokens that are B6: 112r:4.4/6, 5.3/0, 5.9/0, 9.7/0 (`Z{X3}`), 10.10/0, 14.7/2, 18.1/0; 113r:1.4/4, 2.5/0; 113v:2.4/2; 115r:5.7/0, 6.7/4; plus `Zx` 115r:9.4/5.
- B6: none has a baseline arm (no B6+arm). In all 13 the bar crosses the stem near its top with the stem poking above; none is a true T cap. In 112r:14.7/2 and 113v:2.4/2 a stroke to the right at baseline is the next sign.
- B3 and B5: the bar always crosses the stem (stem pokes above), never caps it.
- B4 has three sub-forms (in the note column): b-form with tall straight stem (113r:4.4/0, 112r:7.4/2), 6-form with short curved stem (6 tokens), and stem ending in a closed loop/flag at the top (113v:1.6/5, 115r:6.8/3).
- `top` = `hooked flag` is used only where the stem top turns into a distinct curl or closed loop: 113v:1.9/0 (B1, curl to the right), 113v:1.6/5 and 115r:6.8/3 (B4, closed loop). A stem top that merely bends slightly right stays `no bar` with a note (115r:9.5/0, 115r:12.5/0); 112r:9.10/4 has an ink blob at the top. All these B1 are otherwise plain.
- B0 (1): 112r:5.8/2 (`5{UT,n}`) is f/t-like: a straight stem with a bar crossing it at x-height on both sides, running a little below baseline to a small left foot. No hook or zigzag, no bowl, no top bar. Nearest class would be B2, but it lacks the hook.
- Low confidence (1): 112r:10.6/1 is heavily inked, the arm crosses the stem low down on both sides; B2.

## Odd

- 112r:5 right half and 113r lines slope strongly (up to 30 px across the leaf); tile y follows a linear fit per line and all tiles were checked by eye.
- 113r:2.15 j2 is partly outside the scan (x = 1237 of 1272, grey border covers the right half).
