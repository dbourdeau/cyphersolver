# Batch 2 — interlined code pages, King despatches (NARA M30)

Output: `batch2_spans.tsv` (tab-separated; columns frame, page, line, span_no, groups, interlinear, placement, note).
Read from full-resolution crops of the local JPEGs only. No key or word list was built, consulted or applied while reading digits; nothing else under `output/` or `research/` was opened apart from the survey rows for these frames and the first 30 rows of the format example.

## Conventions used in the TSV

- `line` counts code-bearing lines per page from the top (lines wholly in clear are skipped; where that matters the physical page line is given in the note).
- `^` = caret-like mark after a group. In these hands the digit 4 is written like a barred "A", and the caret is an unbarred inverted v; where a final glyph could be either, the group has `?` and the note says so.
- `v`, `x` = small v / small x written after or above a group.
- `{...}` = words written in clear on the code line itself, placed in the `groups` cell at the point where they occur.
- `—— (rule only ...)` in the interlinear = the group has only a rule above it, continuing a word from the previous line or page.
- `?` on a group = at least one digit doubtful, alternative in the note. `_` = digit(s) hidden in the binding (`_` alone = whole group hidden, only its period visible).
- A row with several groups and `rule` in the note = word over the first group(s), rule drawn over the rest. A multi-group row with no rule is marked `ambiguous` unless the word plainly spans exactly those groups.
- A few `ambiguous` rows join a labelled group with a following unlabelled group that has nothing above it; the note always says which groups the word actually stands over.

## Per frame

| frame | date / despatch visible | code lines | groups | doubtful groups | notes |
|---|---|---|---|---|---|
| M30-004-0238 | No. 52 (continuation; no date on these pages) | L 22 (incl. catchword) + R 8 (incl. a pencil note) | 287 | 17 | Left page: a dark strip of tape/repair runs down the right edge and covers the last 1-2 groups of most lines; those are the doubtful ones (lines 1, 6, 7, 8, 13, 15, 18, 19, 20, 21). Right page: a faint note `* expected` over three faint groups (847 1284? 800?) is keyed by an asterisk to 699v in line 6; entered as R line 8. |
| M30-004-0247 | No. 55 (Dup.), London 6 Dec 1797 | R 7 | 79 | 2 | Seven code lines, not five. `[of]` in square brackets is squeezed in before "Rastadt". |
| M30-004-0250 | No. 56 (end) | L 6 | 58 | 3 | Line 1 opens with a rule-only group (word begun on the preceding page, not in this batch). |
| M30-005-0017 | undated on this opening (survey: Jan-Feb 1798) | R 13 | 128 | 2 | Clean page. Several lines mix clear text and code; clear words are in braces. |
| M30-005-0052 | No. 70 (Dup.), London 2 Apr 1798 | R 12 | 127 | 12 | The first group of 10 of the 12 lines is wholly or partly lost in the binding (entered as `_`, `_8`, `_9`, `_88`). Interlinear hand is loose; several placements ambiguous. |
| M30-005-0054 | undated on this opening (survey: Apr 1798); "my No. 69" cited in clear | L 22 | 163 | 6 | Show-through. Code and clear text alternate within lines. |
| M30-005-0056 | undated on this opening (survey: Apr 1798, South America) | L 25 + R 10 | 383 | 7 | Heavy show-through. Margin note on the left page: `as` over `493` in a bracket, keyed by a small x on `494` in L line 10 (entered as its own row). `819` ("well") is written at the foot of the left page and repeated as the first group of the right page (both entered). |
| M30-005-0076 | undated on this opening (survey: c. 1-7 Jun 1798) | R 9 | 83 | 2 | Nine code-bearing lines at the foot of the right page, not five. |
| M30-005-0079 | undated on this opening (survey: Jun 1798); "your No. 7" cited in clear | L 13 (two blocks: 7 + 6) | 99 | 16 | Heavy show-through; the last group of five lines runs into the page edge. The clerk drew almost no rules here, so most multi-group rows are `ambiguous`. |
| M30-005-0100 | "Copies." (enclosure; left page, seen in mirror-image show-through, is dated London July 6 1798) | R 26 (incl. one-group line 938 and the catchword 1547) | 222 | 22 | Heavy blots and show-through in lines 1-10. Different, rounder interlinear hand with almost no rules, so many multi-group rows are `ambiguous`. Five groups in line 17 (1410 839 1412 728 916) are struck through with their words left above. Question marks and clear words on the code line are in braces. |

**Totals: 10 frames, 173 code-bearing lines, 1,629 groups in 1,143 rows; 798 rows are a single undoubted group under a clearly placed word (these include word fragments such as `re-`, `-ing`); 89 groups carry `?` or `_`.** Groups are counted without the clear-text words in braces.

## Doubtful digits (group as written in the TSV, alternative in its note)

- 004-0238 L: 190? 688? (l.1); 310? (l.6); 1281? 644? (l.7); 411? 644? (l.8); 1039? (l.13); 162? (l.15); 209? 60? (l.18); 574? (l.19); 561? (l.20); 1325? 532? (l.21). R: 1284? 800? (pencil note).
- 004-0247 R: 1160? (l.4); 430? (l.6).
- 004-0250 L: 1119? 572? (l.2); 579? (l.4).
- 005-0017 R: 1123? 1300? (l.5, the Miranda groups; 1300 has its first two digits blotted together).
- 005-0052 R: ten binding-hidden first groups; 437? (l.5); 553? (l.7).
- 005-0054 L: 163? (l.8); 571? (l.13, could be 511); 333? (l.14); 1288? (l.15); 1340? (l.17); 1200? (l.18). Also `370^` at the end of l.20 looks like "3701" (out of range) and is entered as 370 with a caret.
- 005-0056 L: 94? (l.3); 784? (l.19); 353? (l.24). R: 268? 146? (l.1); 1327? (l.5); 1520? (l.9).
- 005-0076 R: 1122? (l.5, underlined); 672? (l.8, in the edge shadow).
- 005-0079 L: 641? 1245? 541? (l.2); 1105? 28? (l.3); 123? (l.4); 383? (l.5); 504? (l.6); 70? (l.8); 461? 716? 685? (l.10); 80? (l.11); 1047? 1170? (l.12); 547? (l.13).

- 005-0100 R: 427? (l.1); 339? 1135? (l.2); 189? 1309? 93_? 593? 710? (l.3; 1028^ and 394^ there are also blotted); 212? (l.4, a blot after it may hide a group); 1537? (l.6); 999? 493? (l.8); 802? 1458? (l.9; 1256 may be two groups 12.56); 1075? 1383? (l.10); 1547? (l.11); 1246? (l.16); 1193? (l.18); 1513? 873? 1412? (l.21).

## Spot checks (strips re-read against the rows after each frame)

- 004-0238: re-read left-page strips for lines 8-10 and 15-17: rows agree. Earlier zoom pass had already downgraded the tape-covered groups to `?`.
- 004-0247: re-read strips for lines 2-5 (left half) and 5-6 (right half): rows agree.
- 004-0250: re-read strips for lines 2-4 (both halves): rows agree; 572 and 579 look firmer on second view but keep their `?`.
- 005-0017: re-read right-half strips for lines 1-4: rows agree.
- 005-0052: gutter crops and 2x zooms of lines 5, 7, 10 re-read: rows agree.
- 005-0054: 3x-5x zooms of ten groups re-read. Slip found and fixed: l.13 first read as 511, the second digit is more likely 7 (now `571?`, alt 511).
- 005-0056: 4x zooms of twelve groups ending in a 4-like glyph. Slips found and fixed: l.2 and l.14 were first read as 894; at 4x the last glyph is an unbarred caret, so both are now `89^` (a true 894 with a barred 4 occurs on the right page, l.5). `189^`, `179^`, `409^`, `1473^`, `768^` confirmed as carets; 1354, 704, 394, 574, 694, 664, 464, 934, 834, 1184, 1134 confirmed as digit 4.
- 005-0076: 3x zooms of lines 5 and 8 re-read: rows agree (33^ confirmed as caret; 1122 kept `?`).
- 005-0079: every line was read twice (strip, then 2x-4x zoom). Slips found and fixed in the second pass: l.3 510 (first read 570), l.5 383? (first read 883), l.10 716? (first read 710).

- 005-0100: lines 1-12 were read from 2x-3x zooms, lines 13-26 from full-resolution strips (digits there are large and clean); 2x zooms of lines 17, 19 and 21 re-read against the rows: agree. Lines 3 and 4 remain the weakest on the page.

A general check for 4/caret confusion was also run on earlier frames (0238, 0247, 0017, 0052, 0054): all sampled 4-final groups there have a barred 4.

## Not done / limits

- All ten frames were transcribed; none remain.
- Rows marked `ambiguous` that join a labelled group to following groups with nothing written above them (frequent in 005-0079 and 005-0100, occasional in 005-0052, 005-0054, 005-0056, 005-0076) are my grouping, not the clerk's: the note on each says exactly which groups the word stands over. If strict "nothing above = empty interlinear" rows are wanted, split those rows on that note.
- 004-0238 left page: the groups under the tape strip were read from enhanced-size crops only; they deserve a second reader.
- 005-0052: the ten binding-hidden first groups cannot be recovered from this image.
- 005-0100 lines 3-4: blots make five groups uncertain and one group may be hidden.
- Words broken across pages (first rows of 004-0238 L, 004-0250 L) depend on frames outside this batch.
