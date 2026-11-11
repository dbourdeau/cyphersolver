# Eaton to the Secretary of State, Tunis, 25 May 1801: transcription from NARA T303 roll 2

Made 2026-11-10 from the microfilm images only. Nothing under `output/` (other than this folder), `research/`,
any key file, or `sources/raw/rotunda_founders_2026-11-10/` was opened. Nothing is decoded: the files
record what is written on the two manuscripts.

## Where the letter is

RG 59, Despatches from US Consuls in Tunis, vol. 2 part 1, NARA microfilm T303 roll 2. Two copies, on
consecutive frames, each a single page:

| Copy | Frame | Folio no. on page | Description |
|---|---|---|---|
| A | `T303-02-0049.jpg` | 291 | Headed "Duplicate". Clerk's hand, signed "William Eaton". Decipherment interlined in another hand over the code. This is the copy transcribed in full. |
| B | `T303-02-0048.jpg` | 290 | No "Duplicate" heading. Smaller hand that looks the same as its "William Eaton" signature (my judgement from the writing only). Not interlined; one authorial insertion of three groups above the line. |

Frame 0050 (fol. 292) and frame 0051 are the enclosures, Cathcart's circulars of 11 and 15 May 1801,
certified "True copy, May 25, 1801, William Eaton"; they carry no code. No third copy was seen in frames 0040-0069,
all of which were looked at.

Images are in `sources/raw/eaton_1801_2026-11-10/` with `acquisition.json` (url, bytes, sha256). Frame 0040 was
already in `sources/raw/nara_tunis_2026-11-06/` (it is Eaton, Tunis, 13 April 1801, no code).

## Files

- `lines.txt`: one row per manuscript line for both copies, code as written, clear text in braces.
- `spans.tsv`: copy A only. One row per span, in order; every one of the 196 groups is in exactly one row.
  Rows with an empty `groups` field and kind `clear-on-line` are clear words on a coded line, kept so the order
  of the line can be followed.
- `clear_text.txt`: clear text of both copies with `[code: n groups]` placeholders.
- `copy_comparison.tsv`: the 196 groups of A against the 196 of B, in sequence, with the separator each
  copy writes after the group.

## Notation

- `-` short dash between groups; `—` long dash; `.` `:` `;` `,` as written.
- `+`, `++`: one or two small crosses written after the group on the line.
- `^`: a small tick or hooked mark written beneath the last digit of the group.
- `*`: a digit hidden by a blot. `?` after a group: a digit is legible but doubtful; the note gives the alternative.
- In `spans.tsv`, `—` in the `interlinear` column is a dash written above the group in place of a word.
  `placement` is judged by horizontal position only.

## Counts (copy A)

- 196 code groups on 24 lines (L05-L23, L25-L29), in 11 runs: 15, 5, 4, 27, 2, 34, 12, 3, 42, 12, 40.
- 141 distinct groups; 100 occur once.
- 134 groups stand under an interlinear word (or word plus dash), 38 under a dash or dashes only, 24 under nothing.
- `spans.tsv` has 182 rows: 166 carry groups, 16 are clear text on coded lines. 25 of the 166 are marked `ambiguous`.
- Marks: `+` on 218, 112*, 765, 1008 (L28 only; the 1008 of L19 has none); `++` on 490, 38, 155;
  `^` on 972, 1528 (both times), 1436, 806. Copy B has the same marks on the same groups.

## Doubtful digits in copy A

Most are ink blots that also show through as grey patches. Copy B is clean at nearly all of these places.

| Line | As read | Problem | Copy B |
|---|---|---|---|
| L06 | 12** | last two digits blotted | 1208 |
| L08 | 525? | last digit 5 or 6 | 525 |
| L10 | 112*+ | fourth digit blotted | 1127+ |
| L12 | 3*1 | middle digit blotted | 381 |
| L13 | *4 | first digit blotted, 3 or 5 | 54 |
| L20 | 1**3 | middle digits blotted | 1453 |
| L21 | 59* | last digit blotted | 598 |
| L21 | 15*8 | third digit blotted | 1518 |
| L21 | *58 | first digit blotted; a stroke below the blot could be the tail of a 9 | 558 |
| L22 | 1*82 | second digit blotted | 1082 (third digit 8 or 6 in B) |
| L25 | 15*1 | third digit blotted | 1521 |
| L25 | **23 | first two digits blotted | 1523 |
| L26 | 54* | third digit blotted | 545 |
| L26 | 9*3 | middle digit blotted | 933 |
| L26 | 8** | last two digits blotted | 832 |
| L28 | 1683? | second digit 6 or 0 | same doubt in B, and its last digit 3 or 0 |

Lesser points: 218+ (L08) has a filled last digit, 8 rather than 9; 1190 (L06) has a smudged second digit;
490++ (L12) is preceded by a pen flourish that is not a 1 (B has a plain 490++).

Doubtful in copy B only: 1513 (L06, third digit), 890 (L06, middle digit), 276 (L16, third digit 6 or 0),
and five blotted groups on L17-L18 (75*, 9*7, 109*, 7*2, 14**), all clear in A as 753, 957, 1093, 782, 1435.

## Comparison of the two copies

- Same 196 groups in the same order. Where one copy is blotted the other is legible, and they are compatible.
- One real difference: group 153 in sequence, A L23 `530` (clear) against B L19 `550` (clear). The interlinear
  word "temerity" stands over 753-530 in A.
- The three groups 700-1171-1005 are in the running line in A (end of L13, start of L14) and an insertion
  above the line in B.
- Punctuation differs. B writes a period after 106 groups, a dash after 89, and nothing after one (1421, before clear text).
  A writes a dash after 174, a period after 17, a colon after 2 (890, 134) and nothing after 3 at line ends
  (886, 1369, 663), so the clerk mostly flattened the periods into dashes. Every period or colon A keeps is a
  period in B. `copy_comparison.tsv` gives both separators for each group, so B's periods can be used
  to check the span boundaries that A's interlinear placement leaves ambiguous.

## Ten most frequent groups (copy A, blotted digits filled from copy B)

| Group | Times | Written above it in A |
|---|---|---|
| 663 | 7 | the (L13, L14, L16, L21, L22, L28); the, placed over the dash after it (L20) |
| 1518 | 4 | of him (L08); of (L08); of (L21); — of (L23) |
| 668 | 4 | stratagem, over 668 and 3*1 together (L12); at, placed over the dash after it (L18, L26); at (L28) |
| 1513 | 3 | a (L06, L12, L27) |
| 1521 | 3 | Morad. (L07); — (L16); long stroke over 1564 and 15*1 together (L25) |
| 598 | 3 | nothing (L10); long stroke over 1486 and 59* together (L21); Regencies, over *58 and 598 (L21) |
| 957 | 3 | distinguishable, over 957 1010 1151 (L10); distinguish, over 957 1112 (L20); three short dashes (L28) |
| 800 | 3 | — (L18); —— (L22); —— (L26) |

Ninth and tenth places are a 33-way tie at two occurrences each: 316, 361, 435, 524, 604, 689, 753, 770, 886,
907, 933, 940, 997, 1005, 1104, 1107, 1114, 1144, 1155, 1171, 1190, 1299, 1404, 1453, 1465, 1479, 1486, 1490,
1506, 1523, 1528^, 1543, 1564. Their interlinear words are in `spans.tsv`.

## Method and checks

Full-resolution strips of frame 0049 were cut with `sips` in thirds of the page width at 2x, each holding two
code lines with the words above, overlapping by a line; doubtful groups were re-cut at 4x and 6x. After the
first pass every line was read again from a second set of half-width strips and checked against the rows; that
pass moved several interlinear dashes (the strokes that run on from the tail of a 9 in the line above, at 1144
and 1107 on L19, 1166 on L21 and 1104 on L22) and confirmed the five `^` marks. Frame 0048 was read from 2x strips
with 3x and 6x crops of every group that was doubtful in either copy. `lines.txt`, `spans.tsv` and
`copy_comparison.tsv` are generated from one hand-entered table by a script that fails if the group sequence of
the spans differs from that of the lines or if the two copies differ in count.

Limits: interlinear word readings were not the object and a few are uncertain (professd, sails, send, Let).
Placement was judged by eye on the strips, not measured.

## Other frames, 0002-0100

Frame 0001 does not exist as an image (the server returns an HTML page). Looked at: 0003, 0004, then every
third frame from 0007 to 0037, every frame from 0040 to 0069, then 0070-0075, 0078, 0080, 0081 and every third frame to
0099, and 0100.

**No other page with numerical code was met.** The only coded pages in this range are frames 0048 and 0049.

Dates seen, for orientation:

| Frames | Content |
|---|---|
| 0003-0004 | roll title page; target "Part I, March 6, 1801 - December 20, 1802" |
| 0007-0010 | Eaton, Tunis, 6 March 1801, to John Marshall |
| 0013-0028 | copies of Cathcart's Tripoli letters and circulars, Feb-March 1801 |
| 0031 | last page of an undated memorandum on consular establishments |
| 0034 | Jercovich receipt, Tunis, 15 April 1801, with translation |
| 0037 | verso, show-through of a page dated Tunis, 16 April 1801 |
| 0040-0041 | Eaton, 13 April 1801 |
| 0042-0044 | Eaton no. 36, 28 April 1801, with postscript of 6 May |
| 0045-0047 | extracts of Madison to Eaton, 20 May 1801 and 22 Aug 1802 (filed out of date order) |
| 0048-0049 | **Eaton, 25 May 1801, two copies, coded** |
| 0050-0051 | Cathcart circulars, Tripoli, 11 and 15 May 1801 (enclosures) |
| 0052-0053 | Eaton to Secretary of State, early June 1801 (day not read at survey size) |
| 0054-0056 | Eaton to Rufus King, 23 May 1801, duplicate |
| 0057-0058 | Eaton to O'Brien, 21 May 1801, copy |
| 0059-0061 | Eaton to Rufus King, 27 May 1801, three copies |
| 0062-0063 | Eaton to Rufus King, 1 June 1801, copy |
| 0064-0065 | Eaton to William Smith, 1 June 1801 |
| 0066-0069 | Eaton, 28 June 1801, duplicate |
| 0070-0075 | Eaton, July 1801 (triplicate, and a letter of 17 July with postscript of 18 July) |
| 0080-0081 | Eaton, July 1801 (verso); Eaton to Madison, 19 Aug 1801, copy |
| 0087-0100 | Eaton letters and enclosures, Aug-Sept 1801; the Bey of Tunis to President Adams (French); Eaton to Perkins Magra, 1 Sept 1801 |
