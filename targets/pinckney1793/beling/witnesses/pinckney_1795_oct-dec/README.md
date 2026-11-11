# Code 16 extension: new manuscript pages, 10-11 November 2026

Locating and transcription only. No decoding against a key, no word list, nothing under `output/` or `research/` opened other than `research/pinckney1795_xyz_leads_2026-11-10.md`. Web use was limited to curl downloads of public NARA catalogue images. Nothing posted.

Files here: `frame_survey.tsv`, `spans.tsv`, this README. Images and `acquisition.json` are in `sources/raw/code16_extension_2026-11-11/` (33 JPEGs; frames 0020-0021 of M31 roll 7 stay in `sources/raw/pinckney_madrid_1795_2026-11-10/`).

## What was covered

### M31 roll 7 (Spain vol. 6)

The roll was stepped from frame 0020 to the end (0392) in two ways. Frames 0020-0036, 0110-0112, 0131-0135, 0176-0178, 0221 and 0315 were looked at as images. Every other frame was classed from the per-frame OCR text in the local NARA bulk record (NAID 188604008): a frame counts as "no code" when its OCR has no run of 3-4 digit numbers. That test picked up the single 10-group line on frame 0020, so it is sensitive, but it is not the same as seeing the page. `frame_survey.tsv` says which basis applies to each frame.

Code 16 pages found after frame 0019 (all Thomas Pinckney, 1795):

| Frame | Letter | Groups | Form | Status |
|---|---|---|---|---|
| 0020 right, line 19 | San Ildefonso, 1 Oct 1795 | 10 | interlined | transcribed here |
| 0021 left | same letter, continuation | (not counted) | interlined | already transcribed, not redone |
| 0111 left and right | San Lorenzo, 28 Oct 1795 | 134 | interlined | transcribed here |
| 0134 left | "Notes by Mr Pinckney on the Treaty", enclosure in 28 Oct, art. XVIII | 28 | bare groups, decipherment in the margin | transcribed here |
| 0135 left | same enclosure, art. XXII | 13 | bare groups, decipherment in the margin | transcribed here |
| 0177 left, lines 20-22 | Paris, 18 Dec 1795 | 39 | interlined | transcribed here |

Total new: 224 group tokens in 120 rows (112 rows with groups, 8 clear-on-line rows). The 1 October letter is complete with frame 0020 line 19 plus the already-transcribed frame 0021: it is signed on 0021 and docketed on 0022; nothing further.

The 28 October letter begins on frame 0110 (no code on that page) and ends on 0112 (no code). The 18 December letter is 0176-0178; code only on 0177.

Not Code 16: the 1802-03 despatches of Charles Pinckney and John Graham (frames 0220-0226, 0314-0315, 0334-0335, 0346-0354, 0365, 0390). Commonest groups 1651 and 133, with groups above 1600. Frames 0221 and 0315 were viewed and are interlined; the rest are from OCR.

### M30 roll 3

Roll 3 is not Pinckney and Deas. The film target reads "Roll 3, Volume 1, April 19, 1794 - June 1, 1795" and the contents are John Jay's despatches from London (item NAID 188512651, 265 objects). The OCR of all 265 objects shows digit runs on two frames only, both viewed:

- 0160, Jay No. 21 (duplicate), 17 Nov 1794: three interlined code lines, comma-separated groups, one group 1624.
- 0207, Jay No. 26 (duplicate), 10 Dec 1794: two interlined code lines, hyphen-separated.

Both are Jay's own code (325 = the, 955 = and, 362 = to on the interlinear), not Code 16. Nothing was transcribed from roll 3. Downloads used for part (2): 3 of 40 (0160, 0207, and the roll note of roll 4, which is Rufus King, Aug 1796 - Dec 1797).

Thomas Pinckney's London despatches are on M30 roll 2 ("Volume 3", 29 Nov 1791 - 4 May 1797, NAID 188512217), the roll the earlier note says the existing key already cites. From the local OCR, roll 2 frames with runs of 3-4 digit numbers are: 0077, 0078, 0083, 0086 (1793, no 663 in OCR, probably another code); 0103, 0106, 0107, 0135, 0136, 0140, 0148, 0178, 0180, 0183 (1793, 663-heavy); 0196 (Jan 1794, 201 numbers); 0208; 0305 (149 numbers); 0317 (April 1795); 0384 (87 numbers). "Deas" occurs in the OCR of frames 0019, 0101, 0328, 0339, 0430. None of these was downloaded, because the task named roll 3 and I could not check which roll 2 frames the key already uses.

## Conventions in spans.tsv

- One row per span; every group is in exactly one row, in manuscript order. `span_no` restarts per frame.
- `?` after a group: a digit is doubtful; the alternatives are in the note. `_`: digits hidden in the gutter (leading or trailing, the note says which). `___`: a whole group unreadable.
- `+` and `++` after a group as written. On frames 0111 and 0177 the double mark is ink-filled and looks like `#`; frame 0135 shows it plainly as two crosses (1403++). `^`: a mark beneath the group (one case, 1650^).
- Clear words on the line inside a coded stretch are rows of kind `clear-on-line`, in braces.
- `placement`: `clear` when the word stands over its group(s); `ambiguous` otherwise.
- Frames 0134 and 0135 are not interlined. Their rows carry the whole passage and the whole marginal decipherment, kind `interlinear`, placement `ambiguous`; the manuscript gives no word-to-group alignment there.

Two things to know before using the interlinear rows:

1. On frame 0111 the binding gutter hides the ends of the left-page lines and the starts of the right-page lines. Affected groups: `1_` (left line 8), `6_` (line 15), `11_` (line 17), `125_` (line 20), `_9++?` (right line 1), `_96` (right line 12), `_6` (right line 14); whole groups may be lost after 663 on left line 9, after 605 on line 13, after 515 on line 14 and before 1116 on right line 13.
2. The clerk often wrote his words compactly and left of the groups they belong to (a word sits over the preceding group, then a dash runs to the line end). Where that happens I assigned words using the groups named in the task brief (663, 1518, 1490, 856, 1513, 753, 1058, 709) as fixed points and marked every such row `ambiguous`, with the physical position in the note. I did not use any key. In a few notes I point to a recurrence inside these same pages (605, 612, 972, 1523) because it bears on where a word boundary falls; those remarks are inferences, not readings.

## Doubtful digits

Frame 0111 is a harsh, high-contrast exposure and loops are ink-filled. Left page: 967 (367), 753 on line 9 (783), 1231 (1251, 1281, 1211), 1515 (1518, 1513), 1126 (1116), 1588 (1388), 460+ (604), 1061 (1060), 359 (369), 85/6 above the struck stretch (possibly one group 856), 662 (642, 602), 616 (619, 614), 1489 (1481, 1480), 668 (608), 1488 (1483), 1442 (1462), 1527 (second digit 5 or 6), 1320 (1380). Right page: `_9++` (394), 194 (104, 124), 1320 (1328, 1323), 1448+ (1428+, 1468+), 694 (698).

Frame 0177: 542 (342), 1490 after 1080 (possibly 194), 1109 (1009, 109). The right half of the last line is in shadow: 541 and 105 are read by sight but may be 1075 and 940; 332, 54, 1523 are tentative; one group is unreadable; the last is 7?5+ (775+, 995+ or 997+).

Frame 0134: 537 (837, 337), 1280 (1260), 1005 (1008), 278 (270). Frame 0135 and frame 0020: no doubtful digits.

Interlinear words not securely read: "pa?minen[t]" (0111 left line 17); the underlined word ending "-ies" in the clerk's remark over 1230+ (line 10); the fragment over `_6` (right line 14); the word over 68_ and the struck word over 54 1523 on frame 0177; the word after "national p" on 0135, cut at the page edge.

## What remains

- A better image of frame 0177 (last line) and of frame 0111 would settle most of the doubtful digits; the NARA JPEG is the only source used.
- M31 roll 7 frames 0037-0109, 0113-0130, 0136-0175, 0179-0219 and the non-code frames after 0220 were classed from OCR only, not viewed.
- M30 roll 2 candidates listed above: not downloaded, not transcribed. They need a check against what the key already cites.
- The Charles Pinckney / Graham code of 1802-03 on M31 roll 7 and Jay's code on M30 roll 3 were identified only as "not Code 16".
