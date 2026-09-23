# Ford-aligned coded blocks, second batch, Oct 1811 - Mar 1812 (22 Sept 2026)

Files: `codes_ford1812b.txt` -> `ford1812_pairs_b.tsv` (2,276 pairs: 2,023 C, 253 M; 2,367 groups transcribed).
Rebuild the raw alignment with `python align.py codes_ford1812b.txt code_table.tsv`. The pair file was generated from
that output by a small script (a confirmed table value = C; a new value between confirmed neighbours = C; a split
judgement, table conflict or doubtful digit = M). Dropped groups (struck, blotted, unread) and GAP are not listed.
These pairs have not been checked line by line by eye the way `ford1812_pairs.tsv` was, so treat the M rows
and the NEW values in the long blocks (0154R, 0159L/R, 0168R) as leads, not as settled values.

| Frame | Despatch | Ford | Groups |
|---|---|---|---|
| 0154 left + right | No. 71 Trip., 11 Oct 1811, cyphered paragraphs 2 and 3 (paragraph 1 is 0153, already done) | 4:238-239 | ~460 |
| 0158R, 0159 L+R, 0160L | No. 72 Trip., 16 Oct 1811, both cyphered passages | 4:250-253 | ~1,150 |
| 0168 left + right | No. 74, 2 Nov 1811 | 4:270-271 | ~480 |
| 0173 left | No. 75, 9 Nov 1811 (interlinear gloss) | 4:276 | 96 |
| 0186 right, 0187 right | No. 81, 31 Mar 1812 (interlinear gloss) | 4:305-306, 308 | 90 |

Not in cypher: **No. 77** (12 Jan 1812) and **No. 78** (25 Jan 1812). Ford gives no "Cypher" note for either (the
footnote after No. 78's "etc." is a Monroe quotation, not a cypher note), and frames 0176-0181 are clear text.
No. 76 (10 Dec 1811) has no cypher either.

Still not done on reel 3, 1811-1812: No. 70 (Sept 1811, Ford 4:226-229, three cyphered passages), No. 96 (Ford 4:393
ff.), No. 98 (Ford 4:406); the two No. 85 passages on 0197 that Ford prints as not decyphered; 0211.

## No. 85, 0196 left, lines 11-16 (not in Ford: table reading only)

Ford ends the cypher at "the rest of the Russian dominions." The MS block goes on for six lines (the task's "lines
12-23" is this; the line count differs because the top of the block is 10 lines here). Right edge lost in the gutter.

    L11  854 649 1433^ | 668 1075 1123 863 792 249 1184 809 668 289 1375 23? GAP
    L12  1501 1236 1452 1127 999 1385 1461 1576 39 — 790 1384 981 1385 84+ GAP
    L13  1576 1399 209 471 1016 49 646 1124 195 569 1501 1426 820 439 GAP
    L14  335 283 454 897 792 1385 1507 709 1098 565 1576 357 1162 . .
    L15  569 1176 1385 16 692 395 520 182 1384 169(underlined) 90 1259 352 81^ 668
    L16  1523 1176 169 90 611 352 83 .

Reading with the table: "dominions, and se-per[ated?] by so wi-de and ex-ten[sive] a [gu-l-ph?] from the rest of
Sweden — but that for the [loss?] of this pro-vin-ce [49: they?] might perhaps hope to [be] in-[de-m]-ni-fied
event-ual-ly by the ac-quisi-tion of Nor[way] without ... to which the Emperor assured him that he should have no
objection, and against which he should make no opposition." None of 1185, 1508, 570, 1112 occurs.

## Priority numbers

- **1185**: not met in any block of this batch.
- **1508**: not met. ("probable" is written 220 1503 twice, 0168L3 and 0173 l.3; "possible" 1157 586.)
- **570 = tol**, four more times, all C, all in "told":
  0186R "He himself [570 801 = told] me last week" (No. 81); 0154L9 "His present ambassador here [570 801] me that
  what he relied upon" (No. 71); 0158R foot "He [570 / 801] me that he had written to Baron Blome" (No. 72);
  0159L9 "against her. I [570 801] him that a similar course of reasoning" (No. 72). In every case 801 = d follows.
  No. 88's "— it [570] he said" has no 801 after it, so 'tol(d)' would need the d dropped; nothing here supports
  another value for 570.
- **1112**: five more times, all 'pas(s)': 0168L14 "The land [1112 1068 1205^] = pas-sa-ges" (C); 0168R twice
  "passes" (1112+ 271) and "land passages" (1112+ 1524^) (C); 0159L14 "to avoid the [1112+] passage" (C, line end in
  the gutter); 0160L2 "attempting to [1112+] pass next Spring" (C). The + mark goes with the double s.
  **1112 1433 together: not met.**
- **1433 = ion**, three more times, C: 0154L6 con-vi-ct-ion; 0159L5 possess-ion-s; 0160L14 (pro-te)-ct-ion.
- **'impaired'**: the one coded "impaired" found on the reel is No. 83, frame 0190L5, "shew of being unimpaired"
  (Ford 4:315; clerk decode in `clerk_0190_etc.tsv`). Ford's other "impaired"s in 1811-1812 (4:280 No. 76, 4:363
  No. 91) are in plain text, not cypher. On 0190L5 the groups are
  **1477 1424 110? 14?5 520 = un-im-pa-ir-ed**; the third group reads 1102 (table pa, M) and the fourth, blotted,
  fits 1435 (table ir, C). That is the word the No. 88 context wants, and No. 88's 1424 **1112 1433** 520 differs
  from 1424 **1102 1435** 520 by one digit in each of the two middle groups (1/0 in the third place, 3/5 in the last).
  im-pas-sion-ed remains the literal reading of 1112 1433; im-pa-ir-ed is attested for this writer with 1102 1435.
  Worth re-examining the No. 88 frame for 1112 vs 1102 and 1433 vs 1435; the 0190L5 digits themselves need a sharper
  look (blotted).

## Other values bearing on No. 88

- **1405 = ice** twice: 0159R11 "sacrifice it" = 1068 1054 1416 1405 (sa-cri-f-ice), 0160L11 "practice" = 207 1405.
  Supports the reading of gap88 l.3 `1575 1405` as adv-ice.
- 1315 = case (0159L11 "in this case", with ^ = cases) as well as 'because' (0154R).
- 1543 = against (0154R "odds are against them"); 1523 = against as before.
- 16 = Emperor, 1049 = Count, 21 = minister, 806 1438 = Dan-ish, 62 = yesterday, 1522 = again (0158R).
