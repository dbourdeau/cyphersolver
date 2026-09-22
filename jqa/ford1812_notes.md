# Ford-aligned coded blocks, Oct 1811 - Sept 1812 (22 Sept 2026)

Files: `codes_ford1812.txt` -> `ford1812_pairs.tsv` (858 pairs: 752 C, 106 M); `codes_ford1812_no95.txt` ->
`ford1812_pairs_no95.tsv` (1068 pairs). Rebuild the raw alignment with
`python align.py codes_ford1812.txt code_table.tsv` (same for `_no95`); the pair files were made from that output and
checked by eye. Grades are hand corrections where the digit or split is doubtful (the note column says why).

| Frame | Despatch | Ford | Groups | Pairs |
|---|---|---|---|---|
| 0153 | No. 71 Trip., 11 Oct 1811 | 4:237 | 129 | 129 |
| 0165 | No. 73, 26 Oct 1811 (decyphered copy 0166) | 4:256 | 76 | 76 |
| 0188 right | No. 83, 28 Apr 1812, first page (continues 0189, clerk-decoded) | 4:314-315 | 334 | 332 |
| 0194 left | No. 84, 9 May 1812 | 4:324-325 | 59 | 59 |
| 0196 left | No. 85 Dup., 27 May 1812, lines 1-11 | 4:338 | 147 | 147 |
| 0199 left | No. 86, 11 June 1812 | 4:351 | 33 | 33 |
| 0214, 0215 | No. 91, 11 July 1812 | 4:362-364 | 96 | 96 |
| 0228, 0229, 0233, 0234L | No. 95, 30 Sept 1812 (clear copy 0230-0232) | 4:389-391 | ~1090 | 1068 |

Frames 0188R, 0194L, 0196L, 0199L, 0214 and 0215 carry a later interlinear plaintext gloss over the groups; it agrees
with Ford except 0199L 1424 (gloss "ex-pressions", Ford "impressions"; No. 95 confirms 1424 = im four times).
Right-hand line ends lost in the gutter (0194L, 0196L, 0215, 0229) were split per line or marked GAP.

Not done: 0196L lines 12-23 and the two No. 85 passages on 0197 that Ford prints as "[two/three lines of cypher not
decyphered]" (4:339); 0211 (coded lines with a gloss; read in `clerk_0210_0211.tsv` by the other session); the 1812 blocks of Nos. 77, 78, 81.

## Bearing on No. 88

- 996 = fri (fri-end, fri-end-ship, 4x C in No. 95). rem88 l.13 `1576 996 520 1453 416` = of Fri-ed-la-nd
  (1453 la, 416 nd as in Fin-la-nd 0196L): **Friedland**. The two groups before it, 1309 888, are still open.
- 1457 with the mark = ll: 0165 `1025 1016 1457+ 908` = Chan-ce-ll-or (Ford "Chancellor"); 0188R and No. 95 write
  the same word 1025 1016 1452(+) 908. gap88 l.2 `1025 1016 1457 908` is Chancellor, not Chan-ce-last-or.
- 83 = opposition, now C (0165: "the opposition in the Council").
- 1424 = im (4x C, No. 95: im-possible, im-mediate, im-pediments, im-pressions No. 86), 1433 = ion (div-is-ion,
  rela-t-ion, domin-ion-s): gap88 `1424 1112 1433 520` stays im-pas-sion-ed; no other reading of 1112 found.
- 492 = use (No. 95 "to use her best endeavours"): supports the reading of gap88 l.5 492 as JQA's slip.
- 1575 = of twice in No. 95 (0228 "arrangement of the differences", 0229 "Secretary of State"), or 1576 misread;
  gap88 l.3 `1575 1405` is read adv-ice on a single M value from 1811.
- 350 = fi (con-fi-dence, 0196L), 1403 = cal (cal-culate, 0194L), 289 = ex (5x): rem88 l.4 `350 289 1403 897`
  gives fi-ex-cal-ly, still no sense.
- 748 = re once (No. 95 "no good re-sult", M). 1309 = lation (0194L re-lation) and wer (0188R an-s-wer), both M.
- 586 = le (Napo-le-ons, 0215), 1416 = if, 570 = tol, 1535 = al/all, 699 = at, 1081 = self: all confirmed.
- Not met in any block read: 1185, 927, 1508, 1112 (apart from the pas already attested), 220, 1540, 888, 1405.
