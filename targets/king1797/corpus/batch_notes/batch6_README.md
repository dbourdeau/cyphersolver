# Batch 6 of 6: interlined code pages, Rufus King despatches (NARA M30)
Output: `batch6_spans.tsv` (tab-separated; columns `frame, page, line, span_no, groups, interlinear, placement, note`).
Read from full-resolution strips of the images in `sources/raw/king_m30_2026-11-10/` (sips crops only). No key or word list was built, consulted or applied; nothing under `output/` or `research/` was opened except `frame_survey.tsv` (rows for these frames) and the first 30 rows of `interlined_page_spans.tsv` (format only). All 15 frames were transcribed; none remain.
## Conventions
- `line` counts CODE lines per page (manuscript lines holding at least one code group), top to bottom; lines wholly in clear are not numbered.
- Rows whose `groups` field is only `{...}` carry King's clear text standing on or between code lines (abridged where long); they are context, not code.
- `?` after a group = at least one digit doubtful, alternatives in the note. `_` = digit(s) hidden in the binding. `^` caret-like mark after a group, `v` small v-like mark.
- A word with a rule over further groups is one row, with `rule` in the note. `—— (rule only …)` rows are groups that have only a rule above them, continuing a word or phrase from the previous row or line.
- `ambiguous` = the pen does not show unambiguously which group(s) the word belongs to. Where a clerk habitually wrote his words to the LEFT of the groups (006-0252, 006-0287, 006-0292, 008-0060, 008-0061), a whole run is given as one ambiguous row and the note says over which group each word physically stands. These rows should not be used as single-group equations without further work.
- Groups with nothing written above them have an empty interlinear.
- Punctuation on the code line (dashes, colons) is mentioned in notes only.
- The digit 4 is often written open, like a capital A; 7 often with a long tail; these are not flagged.
## Totals
| frame | code lines | groups | single-group interlined rows | multi-group interlined rows | ambiguous rows | doubtful groups (?) | gutter groups (_) |
|---|---|---|---|---|---|---|---|
| M30-006-0192 | 8 | 52 | 24 | 8 | 2 | 2 | 0 |
| M30-006-0199 | 11 | 90 | 45 | 11 | 4 | 1 | 0 |
| M30-006-0207 | 5 | 37 | 24 | 5 | 3 | 7 | 0 |
| M30-006-0252 | 6 | 48 | 15 | 10 | 14 | 1 | 4 |
| M30-006-0287 | 28 | 146 | 45 | 22 | 25 | 18 | 0 |
| M30-006-0292 | 9 | 68 | 20 | 9 | 6 | 6 | 0 |
| M30-007-0034 | 4 | 39 | 30 | 3 | 1 | 0 | 0 |
| M30-007-0157 | 18 | 94 | 62 | 10 | 7 | 6 | 0 |
| M30-008-0024 | 3 | 14 | 6 | 2 | 1 | 0 | 0 |
| M30-008-0060 | 9 | 60 | 25 | 4 | 6 | 1 | 0 |
| M30-008-0061 | 4 | 33 | 16 | 5 | 7 | 1 | 0 |
| M30-008-0071 | 11 | 62 | 23 | 11 | 8 | 2 | 0 |
| M30-008-0072 | 13 | 57 | 21 | 11 | 7 | 0 | 2 |
| M30-008-0177 | 3 | 10 | 2 | 2 | 2 | 0 | 1 |
| M30-008-0178 | 2 | 7 | 3 | 1 | 1 | 0 | 0 |
| **total** | 134 | 817 | 361 | 114 | 94 | 45 | 7 |

Of the single-group interlined rows, those marked `clear` are the safest material; single-group rows marked `ambiguous` have a word that straddles a gap.

## Per frame

### M30-006-0192
- Date / despatch number visible: No. 59, 'London Feb 3d 1800' (right page head)
- Transcribed: 8 code lines, 52 groups (24 single-group interlined rows, 2 ambiguous rows).
- Doubtful digits: R4: 760?; R7: 1031?
- Notes: Right page only (left page blank/show-through). The code is King's own small hand; interlinear in a clerk's hand. In line 6 one group (644) is itself an insertion above the line over a caret.
- Spot check (strips a2, b4): no slips.
- Not done: nothing omitted on this frame.

### M30-006-0199
- Date / despatch number visible: No date on the opening (end of a despatch, signed Rufus King; right page is a 'Copy' of a Grenville note mentioning 5 Jan 1800). Survey: Feb-Mar 1800.
- Transcribed: 11 code lines, 90 groups (45 single-group interlined rows, 4 ambiguous rows).
- Doubtful digits: L3: 1292?
- Notes: Left page, 11 code lines. Clear copyist's hand; several groups carry short bracket-like rules UNDER them (1410, 819) and one small group 804 is squeezed in at a line end.
- Spot check (strips u2L, u4L, u6L, u6R): no slips.
- Not done: nothing omitted on this frame.

### M30-006-0207
- Date / despatch number visible: No. 65 (Triplicate), 'London, [2d or 3d?] April 1800' as the head reads to me (single digit with a superscript; the survey has 22 Apr); docket on the left page.
- Transcribed: 5 code lines, 37 groups (24 single-group interlined rows, 3 ambiguous rows).
- Doubtful digits: R1: 1209?; R1: 105?; R1: 484?; R2: 11??; R2: 208?; R2: 177?; R4: 356?
- Notes: Right page, 5 code lines. Heavy show-through crosses several groups (line 1-2). On this page the clerk's rules sometimes PRECEDE the word (rule over the first group, word over the last).
- Spot check (strips z2, z5): no slips.
- Not done: nothing omitted on this frame.

### M30-006-0252
- Date / despatch number visible: No. 74, Duplicate, 'London June 6. 1800' (right page head).
- Transcribed: 6 code lines, 48 groups (15 single-group interlined rows, 14 ambiguous rows).
- Doubtful digits: R1: 1813?
- Gutter-cut groups: R1: _016; R4: _379; R5: _410; R6: _41
- Notes: Right page, 6 code lines. Leading digits of the first group of lines 1, 4, 5, 6 are in the gutter. Interlinear words are crowded to the left of their groups, so most multi-word runs are marked ambiguous. One run-together group 1813 (exceeds 1599).
- Spot check (strips s2B, s4B): digits confirmed; noted that the last digit of 411 is a curved stroke.
- Not done: nothing omitted on this frame except groups hidden in the gutter.

### M30-006-0287
- Date / despatch number visible: No date line on the opening (survey: c. 31 Oct 1800).
- Transcribed: 28 code lines, 146 groups (45 single-group interlined rows, 25 ambiguous rows).
- Doubtful digits: L1: 834?; L6: 321?; L6: 868?; L6: 561?; L7: 1093?; L7: 710?; L8: 1???; L11: 273?; L13: 6??; L13: 98?; R1: 147?; R1: 250?; R2: 808?; R2: 15?1; R3: 618?; R4: 1016?; R5: 402?; R7: 1051?
- Notes: Both pages: left 17 code lines, right 11. Worst frame of the batch: strong show-through, and the clerk's words stand left of their groups, often by a whole group. Long runs are therefore given as single ambiguous rows with the physical position of each word in the note. Three groups are only partly legible (L8 '1???', L13 '6??' and '98?').
- Spot check (strips L2a, L2b): no slips.
- Not done: nothing omitted on this frame.

### M30-006-0292
- Date / despatch number visible: No date line on the opening; right page ends '(Signed) Rufus King' (survey: Nov 1800).
- Transcribed: 9 code lines, 68 groups (20 single-group interlined rows, 6 ambiguous rows).
- Doubtful digits: L2: 5181?; L4: 641?; L4: 4091?; L5: 692?; L8: 137?; L8: 15?1
- Notes: Left page, 9 code lines; same clerk and same leftward drift as 006-0287. Two penned strings exceed 1599 and are kept as written with '?': 5181 (line 2) and 4091 (line 4).
- Spot check (strips L2b, L4a): no slips.
- Not done: nothing omitted on this frame.

### M30-007-0034
- Date / despatch number visible: No date line (end of a despatch, signed Rufus King; survey: c. Mar 1801).
- Transcribed: 4 code lines, 39 groups (30 single-group interlined rows, 1 ambiguous rows).
- Doubtful digits: none flagged
- Notes: Left page, 4 code lines, very clear. Three words stand in clear on the code line and were rewritten above by the clerk (Consent, lieu, Decision). Two rules precede their word (985.366.1200 'understood'; 641.379 'article'). A stroke after 709 and after 637 at the gutter may hide a further group.
- Spot check (strips s1a, s2b): no slips.
- Not done: nothing omitted on this frame except groups hidden in the gutter.

### M30-007-0157
- Date / despatch number visible: No date line (end of a despatch, signed Rufus King; survey: Jun 1801).
- Transcribed: 18 code lines, 94 groups (62 single-group interlined rows, 7 ambiguous rows).
- Doubtful digits: L1: 987?; L1: 1204?; L2: 1020?; L2: 13??; L4: 3?_; L7: 1553?
- Notes: Left page 9 code lines, right page 9. Left lines 1-2 are REVERSED (clear words on the line, small code groups written above them in a different hand with A-shaped 4s and hooked loops): digits there are the least certain of the frame, and one cancelled group was not read. Gutter cuts L4 '3?_' and L7 (155x).
- Spot check (strips L6a, R2a): no slips. Slip found later: L7 gutter group first entered as 1552?, changed to 1553? after re-examination (see note in the row; that re-examination happened after reading 644.1553 on 008-0178, so it is not independent).
- Not done: nothing omitted on this frame except the one cancelled group on left line 1 and whatever is hidden in the gutter.

### M30-008-0024
- Date / despatch number visible: No. 50, 'London Jan. 15. 1802' (right page head).
- Transcribed: 3 code lines, 14 groups (6 single-group interlined rows, 1 ambiguous rows).
- Doubtful digits: none flagged
- Notes: Right page, 3 code lines (two short runs). Grainy film. The name over 1231.865 is carried by a rule over the first three groups of the next line.
- Spot check (strips a1, a3): no slips.
- Not done: nothing omitted on this frame.

### M30-008-0060
- Date / despatch number visible: No. 58, 'London March 13. 1802' (right page head).
- Transcribed: 9 code lines, 60 groups (25 single-group interlined rows, 6 ambiguous rows).
- Doubtful digits: R4: 570?
- Notes: Right page, 9 code lines (incl. the final 1410.255). Two long rules (over 8 groups and over 5 groups) continue phrases written over the preceding line; those rows are 'rule only' and the phrase rows are ambiguous.
- Spot check (strips v1-v3, u1-u2): 570 in line 4 flagged doubtful (alt 510) after comparison at high zoom; otherwise no slips.
- Not done: nothing omitted on this frame.

### M30-008-0061
- Date / despatch number visible: No date (end of No. 58, signed Rufus King).
- Transcribed: 4 code lines, 33 groups (16 single-group interlined rows, 7 ambiguous rows).
- Doubtful digits: L2: 648?
- Notes: Left page, 4 code lines. The clerk's phrase 'this country too may be[lieve] that war is' is shifted left across the line break (line 3 to line 4).
- Spot check (strips z1, z2): no slips.
- Not done: nothing omitted on this frame.

### M30-008-0071
- Date / despatch number visible: No. 62 (Duplicate), 'London Ap. 10. 1802' (right page head).
- Transcribed: 11 code lines, 62 groups (23 single-group interlined rows, 8 ambiguous rows).
- Doubtful digits: R2: 510?; R10: 672?
- Notes: Right page, 11 code lines. Names are spelt over several groups with the word over the first group or two only. Line 2 has 510 where lines 7 and 9 (same name) have 570.
- Spot check (strips z1-z4): 510?/570 difference found and noted; no other slips.
- Not done: nothing omitted on this frame.

### M30-008-0072
- Date / despatch number visible: No date (continuation of No. 62).
- Transcribed: 13 code lines, 57 groups (21 single-group interlined rows, 7 ambiguous rows).
- Doubtful digits: none flagged
- Gutter-cut groups: L3: _; L7: 5__
- Notes: Left page 10 code lines, right page 3. Three name sequences on the left page run into the gutter (L3 '1305 _', L7 '1305 5__', L8 '1231 …'): the hidden groups are NOT supplied.
- Spot check (strips h5-h8): found that on R3 'Mr Merry' stands one group left (over 644-128); row made ambiguous.
- Not done: nothing omitted on this frame except groups hidden in the gutter.

### M30-008-0177
- Date / despatch number visible: No date (continuation of No. 89).
- Transcribed: 3 code lines, 10 groups (2 single-group interlined rows, 2 ambiguous rows).
- Doubtful digits: none flagged
- Gutter-cut groups: L1: _
- Notes: Two runs: left page (line 1 cut by the gutter after 1234, at least one group hidden) and right page.
- Spot check (strips a1, b1, b2): no slips.
- Not done: nothing omitted on this frame except groups hidden in the gutter.

### M30-008-0178
- Date / despatch number visible: No date (end of No. 89, signed Rufus King).
- Transcribed: 2 code lines, 7 groups (3 single-group interlined rows, 1 ambiguous rows).
- Doubtful digits: none flagged
- Notes: Left page, 2 code lines.
- Spot check (strips a1, a2, b1): no slips.
- Not done: nothing omitted on this frame.

## Things a later reader should know
- Repeated sequences were each read from the pen independently; where they differ the difference is left standing (e.g. 008-0071 line 2 `510?` against `570` on lines 7 and 9; 006-0287 `868?`/`561?` against clear 868.561 on 006-0252).
- Two penned strings exceed the stated range 1-1599 (006-0252 `1813?`, 006-0292 `5181?`, `4091?`); they are probably two groups with a lost period, or a group plus a mark, and were not split.
- 007-0157 left page lines 1-2 (reversed interlineation) should be treated as low confidence throughout.
- The 006-0287 / 006-0292 clerk's alignment drifts by up to a full group; the per-word positions in the notes are physical positions, not assignments.
- Scratch strips are in the session scratchpad (`king_b6/`), not in the project.
