# Lear to Madison, [January 1813]: independent re-transcription (10 Nov 2026)

Library of Congress, James Monroe Papers, reel 5 (mss33217.005), images 981-983.
Numerals and interlinear decipherment were read from the images alone. No key was used,
and the 6 November transcription was not opened until these files were saved (see
`diff_vs_6nov.tsv` for the later comparison).

## Images used

Stored in `sources/raw/lear1813_retranscription_2026-11-10/` with `acquisition.json` (url, bytes, sha256).

| image | pixels | file read | source |
|---|---|---|---|
| 981 | 2428 x 2933 | `r5_0981_master.tif` | https://tile.loc.gov/storage-services/master/mss/mss33217/005/0900/0981.tif |
| 982 | 4590 x 2946 | `r5_0982_master.tif` | https://tile.loc.gov/storage-services/master/mss/mss33217/005/0900/0982.tif |
| 983 | 2934 x 2327 | `r5_0983_master.tif` | https://tile.loc.gov/storage-services/master/mss/mss33217/005/0900/0983.tif |

The IIIF `pct:100` JPEGs were fetched too; they are byte-identical to the 6 Nov audit copies and
have the same pixel size as the masters. No larger rendition exists (IIIF `info.json` reports the
same dimensions). The masters are 8-bit greyscale microfilm scans, lossless, so they were used.

Reading method: `sips` crops only. Each line was read at 190-200 % in two independent sets of
strips with different cut points (thirds of the page width), then every doubtful digit and about
forty further groups were re-cropped at 270-600 %.

## Counts

| page | manuscript lines | code groups |
|---|---|---|
| 981 | 25 (+ catchword 478) | 299 |
| 982 | 5 | 55 |
| 983 | 0 | 0 |
| total | 30 | 354 |

The catchword 478 at the foot of 981 is the first group of 982 and is counted once.
`lear1813_spans.tsv` has 303 rows: every group sits in exactly one row, in manuscript order;
words written in clear on the line have their own rows (`clear-on-line`, groups empty).

983 has no code. It carries, in another hand at the head of the outer leaf:
"This Paper came under a Blank Cover. Mr Lears Cyp[her, blotted] was used to read it."
and a vertical docket; 982's blank right half shows the same docket in show-through.

## Doubtful digits

`?` after a group marks a doubtful digit. First reading is what the pen most probably wrote.

| line | reading | alternative | why |
|---|---|---|---|
| 981-L1 | 616? | - | first digit under an ink blot and show-through from 982; 616 by outline |
| 981-L2 | 856? | 850 | last digit run into by the d of the gloss "and" |
| 981-L2 | 730? | 736 | last digit a small closed loop, gloss strokes above it |
| 981-L3 | 1097? | not recoverable from the ink alone | whole group overwritten by the gloss "they" and blotted; outline agrees with 1097 (L19, same gloss) |
| 981-L3 | 1481? | 1421 | third digit tangled with the gloss; looped form favours 8 |
| 981-L3 | 1396? | 1296 | second digit has an oversized looped head that fits neither this writer's 2 nor his 3 cleanly (the `?` was added after the comparison, see below) |
| 981-L3 | 1159? | 1150, 1156 | last digit crossed by the p of "exposition"; loop with a descender |
| 981-L8 | 1515? | 1505, 1565 | third digit hidden by a blot where the t of "their" (line below) rises; a single upright stroke |
| 981-L12 | 1455? | 1155 | second digit is a blot wider at lower left, as a filled 4 would be |
| 981-L13 | 17? | 77 | first stroke has no head, unlike this writer's 7 |
| 981-L16 | 1580? | 1586 | last digit filled with ink |
| 981-L16 | 1058? | 1038, 1068 | third digit a blot with a 5-like flag |
| 981-L16 | 838? | 858 | middle digit crossed by the t of "unacquainted" |
| 981-L19 | 1513? | 1573 | the flag of the 5 touches the head of the third digit; L10 has the same group, clearer, under the same gloss "a" |
| 981-L22 | 435? | 485 | middle digit heavily inked |
| 982-L3 | 1346? | 1316 | group smeared together with its gloss |
| 982-L4 | 1160? | 1166, 1100 | last two digits filled; show-through hatching across the group |

Readings that look odd but are not doubtful to the eye:
- 981-L2 `1490`: the last digit is this writer's open 0 (an "a" shape), not 2.
- 981-L14 `1512 1251 1512`: the pen wrote 1512 twice (final digit a clear 2 both times), although
  the gloss is "unfounded".
- 981-L24 `1401`: second digit open-topped, a 4; 1201 would need this writer's round-headed 2.
- 981-L10 `1513` against 981-L23 `1573`: the 7 of 1573 has its own waved head; the third digit of
  1513 is a bare stroke with a small flag.
- 982-L5 `8`: a single digit standing alone between points.
- 982-L1 and L2 `1505` are written with a bar over the middle digits. On 981 the same group
  carries a colon (L4), a dot (L18) and a dash (L24) in the interline.

## How interlinear words were placed

Placement is by horizontal position, measured in the crops.

1. A word is attached to the groups it stands over. A group counts as covered when the word
   overlaps roughly a quarter or more of its width; under about 60 % the row is marked
   `ambiguous` and the note gives the physical extent ("phys: ...").
2. Groups with nothing above them are `none` rows. Where such a group follows a long word and
   is probably its unwritten tail (e.g. 1432 after "exposition"), the row is still `none`, the
   placement is `ambiguous`, and the note says which word precedes.
3. This decipherer often writes a word half a group or more to the right of its group, because
   the previous word overran. Where a word is crowded hard against its predecessor, or a piece
   sits evenly astride two groups, position alone cannot fix its group. In those rows only, a
   repeated gloss elsewhere in this same letter was allowed to decide (for example 1518 = "of"
   on L1 and L19 decides 981-L13), the row is marked `ambiguous`, and the note records the
   physical position. No outside key was used.
4. Detached pieces ("adopt ed", "tend ed", "ter m") that fall in a gap are attached to the group
   that follows, marked `ambiguous`.
5. Small strokes, dots and dashes written above 1160, 1429, 1505 and 1020 are recorded as
   `[tick]`, `[dot]`, `[colon]`, `[dash]`.

Rows where the physical position and the within-letter evidence pull apart, so a reader of the
spans should not lean on them:
- 981-L6: "United States" physically covers 71 and 1107; "resident" stands over 1328-1047.
  The row now gives 1107 to "resident" (rule 3).
- 981-L8: "differ ent parts": each piece sits astride two groups. The rows now read
  638 1255 1435 = "differ ent", 743 = "parts" (rule 3).
- 981-L13: "correspondence" overruns 1518; "of the" is squeezed over 663.
- 981-L20: "circumstances" begins exactly over 972, which elsewhere stands under "al".
- 981-L23: "President" overruns 1167; "before" stands over the join of 1167 and 1160.
- 982-L3: by ink, "British" covers 1346-78, "Minister" 676, "nor" 1153, "Lord" 737, "Wel" 134.
  The rows now put each word one group to the left (rule 3: 134 ends "naming" and follows
  "saying" on 981, and 1400 closes the "Clinton" string). This is the least secure stretch.
- 982-L5: from "attempt" on, each gloss stands about one group to the right
  (attempt over 74-1490, "to" over 8, "communicate" over 1005-1362, "it" past the last group).

Extents were estimated by eye from the crops, to about a digit's width. Borderline cases are
flagged rather than resolved.

## Comparison with the 6 November files (step 3)

`diff_vs_6nov.tsv` has 90 rows. Group counts agree line for line (354 groups in both).

- Numerals: 37 groups differ, plus one place where the 6 Nov ledger and its own numerals file
  disagree (1128 / 1122) and one stray token (a supposed struck "the" on 981-L17). After a
  fresh crop of each spot: 36 resolved for the new reading, 3 undecidable (981-L3 groups 1 and 3,
  981-L8 group 2; all three are blotted and both files mark them doubtful).
- Word-to-group assignment, real conflicts and lines the old ledger did not cover (15 rows):
  9 for the new reading, 3 for the old, 3 undecidable.
- Same groups, finer division of the word (6 rows): recorded as written.
- Trailing groups (28 rows): the old ledger attaches unglossed groups to the word before them;
  the image shows nothing above those groups. Marked undecidable: the attachment is an
  inference, usually a reasonable one, not something the ink shows.
- Notation (2 rows): comma / full stop against the mark actually written.

### Changes made to the step-2 files after the comparison

The step-2 files were saved before the old files were opened
(sha256 then: lines `e222160e...`, spans `81efaba4...`). Four changes were made afterwards:

1. 981-L3 group 3: `1396` became `1396?`. Final look could not settle 3 against 2.
2. 981-L6: `71 1107 = United States; 1328 1047 = resident` became
   `71 = United States; 1107 1328 1047 = resident`. Rule 3 had not been applied here although
   "resident" is crowded against the overrun of "States".
3. 981-L8: `638 = differ; 1255 = ent; 1435 743 = parts` became
   `638 1255 1435 = differ ent; 743 = parts`. Each piece sits astride two groups; 1435 stands
   under "ent(ers)" on L5.
4. 982-L3: `1346? 78 = British; 676 = Minister; 1153 = nor; 737 = Lord; 134 = Wel` became
   `1346? = British; 78 = Minister; 676 = nor; 1153 = Lord; 737 134 = Wel`. By ink alone the
   first version is what stands on the page; the change rests on within-letter evidence only,
   and every row is marked `ambiguous`.

No numeral was changed to agree with the old file.

## Files

- `lear1813_lines.txt`: one manuscript line per row; `{...}` = clear on the line.
- `lear1813_spans.tsv`: `line, span_no, groups, interlinear, kind, placement, note`.
- `diff_vs_6nov.tsv`: comparison with the 6 Nov files, written after the two files above.
