# German Foreign Office → Legation Stockholm, numeric-code telegrams, 2 and 22–27 July 1918 (catalogue 654)

Status: attempted, open. Not deciphered. Nine full copies and one truncated copy, in at least four separate numeric
systems, with no key anywhere we could reach. What the work added: a checked transcription, the telegrams' own running
numbers and a corrected date for the first batch. Catalogue 656, the Ludendorff telegram and the five-figure
legation telegrams from the same batches, has its own folder: `targets/ludendorff1918/`.

## The documents

NARA RG 59, Decimal File 763.72, microfilm M367. The US Legation in Stockholm obtained copies of German telegrams
addressed to the German Legation, sent them home in three despatches, and re-cabled them from Christiania, because
Stockholm's own cable was not safe. Stockholm's covering telegrams call them "authentic" and the dates "uncertain".

| Telegram | Header | Signed | Groups | Frame | Cable copy |
|---|---|---|---|---|---|
| w765 | 288/4/284, 27 July 1:07 | Hintze | 284 | roll 141 ff. 1265–66 | roll 108 ff. 0747–53 |
| w752 | 124/4/120, 26th 10:43 | none | 73 of 120 | roll 141 f. 1259 | roll 108 ff. 0700–01 |
| w763 | 194/4/190, 27 July 1:07 | Hintze | 190 | roll 141 f. 1256 | roll 108 ff. 0691–95 |
| w749 | 45/4/41, 26th 10:43 | auswaertig | 41 | roll 141 f. 1261 | roll 108 ff. 0723–24 |
| w746 | 74/4/70, 26th 10:43 | auswaertig | 70 | roll 141 f. 1263 | roll 108 ff. 0726–27 |
| w735 | 28/4/24, 26th 9:07 | Bussche | 24 | roll 141 f. 1262 | roll 108 f. 0725 |
| w643 | 153-4-149, 22nd 11:45 | auswaertig | 142 legible | roll 122 f. 0155 | none found |
| w2635 | 50/4/46, 2nd 6:30 | Stumm | 46 | roll 114 f. 0416 | roll 108 ff. 0512–13 |
| w512 | 32, 2nd 1:30 | auswaertig | 28 | roll 114 f. 0417 | roll 108 ff. 0513–14 |
| w513 | 44, 2nd 2:00 | auswaertig | 40 | roll 114 f. 0418 | roll 108 ff. 0514–15 |

Frame 0154 of roll 122 is Stockholm's covering despatch 1475. The header counts confirm the transcription: w763, w749,
w735, w2635, w512 and w513 come to exactly the stated number of groups, w765 does once 39520892 is split into two
groups, and w746 does once two typed lines repeated by the American typist are dropped. w752 stops at 73 of 120 in
both copies, so the Legation's source was already short. w643 is 3 to 7 groups short (four groups are struck through
on the frame, and it has no cable copy to check).

`transcription.txt` has every group. A trailing `?` marks figures that stay doubtful; 3, 5, 6 and 8 run together in
this typeface. The check against NARA's OCR of the frames and of the cable copies is `work/triple.py`.

## What the headers say

Mendelsohn 1937 (below) explains the opening three-figure groups: the Foreign Office numbered and dated telegrams from
a separate small code, the Dreinummerheft, whatever code the body used. He prints only part of it, but his examples
give the rule for the numbers. Take Nr. 1 = 416, 2 = 723, 3 = 130, 4 = 547, 7 = 878, 8 = 285, 9 = 692, 11 = 424,
12 = 731, 14 = 555, 16 = 379, 26 = 387, 376 = 333. Going up one number works figure by figure, with no carrying: the
first figure follows a fixed order (0 4 7 1 5 9 3 8 2 6), the second goes up 1 and the third down 3. Going up ten moves
the second up 1 and the third down 2, and going up a hundred moves the third up 2. That formula reproduces all his
examples, including 376 = 333, and it gives consecutive steps such as 149, 556, 963.

Numbers above 499 take two groups. Mendelsohn p. 29 prints three message heads: "285 937" = Nr. 8 + 80, "692 169" = Nr. 9 +
33, "555 851" = Nr. 14 + 82, that is 880, 933, 1482. The second group is a second table with the same figure-by-figure
steps, in which the third figure goes up 2 for ten (not down 2). His page 5 extract shows that half of the book mixing dates
and further numbers (76, 85, 48, 66, 97, 57).

Reading each telegram's head that way (`work/tri.py`, and the arithmetic is checked against those three examples):

- **w512, w513, w2635 open 692 157, 692 564, 692 971: Nr. 923, 924, 925.** 692 157 sits two steps from Mendelsohn's own
  692 169 = 933: same first group, ten lower.
- **w765, w752, w763, w749, w746, w735 open 010 018, 017 425, 017 732, 017 149, 017 556, 017 963: Nr. 1010 to 1015**, an
  unbroken run. 017 is Nr. 10 by the formula. w765's 010 is one figure off; we read it as a slip or variant [?].
- **w643 opens 017, a struck group, 119 943.** 119 gives units and tens 88 in the higher half of the second table, so x88 [?].
  The struck group hides the hundreds. Nr. 988 on 22 July would fit the rate, but this one is not certain.

So the six telegrams of 26–27 July are consecutive, across three of the numeric systems (w765, w763 and w735 in A, w749 and
w746 in B, w752 in C). That shows the systems share one numbered series, and that the source of the American copies saw a
consecutive run of the Legation's traffic. The Dreinummerheft is the only part of this traffic with a published key.

**The first batch is about 1–2 July, not 22–27 July.** w2635's head has 961, which Mendelsohn p. 29 gives as "Vom 2 Juli", and
all three telegrams of despatch 1421 carry "2" as their day. The catalogue had taken the whole set as 22–27 July. The numbers
fit: Nr. 925 on 2 July to Nr. 1010 on 26 July is about 3.5 telegrams a day. Also from his tables: 400 = und, in w763's head.
The groups 405, 406, 378 and 437 stand where a date should, but they are not among his printed examples, so they stay unread [?].

The fourth group is probably the code mark, as "Chiffre Nr." is in 13040 (groups 13040–13049): 1219 in four telegrams,
4407, 4416 and 4435 in the other family, a block with a free last figure, as with 13040 and 18470. Not proven [?].

## The systems

Separated by measurement (`work/ovl.py`, `work/addsearch.py`). Nothing here names a code book; these letters are ours.

| | Telegrams | Groups | Shape |
|---|---|---|---|
| A | w765, w763, w735, w2635 | 544 | Mostly four figures, about 15% five figures with any leading figure (0 included), mark 1219. Flat first figure. Same outward form as Bernstorff's 1917 code (`targets/bernstorff1917/`) |
| B | w749, w746, w512, w513 | 179 | Three to five figures up to about 24000, with a few high name-like groups (62308, 89144, 65748). Marks 44xx |
| C | w752 | 73 | Up to 47603, about a third above 31000. 1963 and 1962 recur where a stop would fall [?] |
| D | w643 | 142 | Up to 18187 (31990 once). Pages 133–134, 143 and 181 very dense. Contains 13049 and 13047, in the block 13040 reserves for "Chiffre Nr." |

Repeats inside B are real: "9405 2837" opens w749, w746 and w512; "23456 21890" occurs in w749, w746 and w513. They are
probably a set phrase of address, but there is no way to say which. These are not enough for a ciphertext-only attack on
a code of tens of thousands of groups: 938 groups in four books, the largest with 512 distinct groups.

## What was tried

The main source is **C. J. Mendelsohn, *Studies in German Diplomatic Codes Employed during the World War* (War
Department, Register No. 191, 1937)**, written from MI-8's work of 1918–19 and released by NSA in 2014. It is on the
[Internet Archive](https://archive.org/details/41784749082377). It prints the Zimmermann decipherment and other 13040,
5950 and 26040 messages group by group, about 1,500 groups of the 18470 family, and page tables for 12444, 1777 and 2310.
It never mentions Stockholm or any of these marks.

1. **Plain 13040, 18470 and the Bernstorff 1917 code.** Exact hits are at the chance level. A real 13040 text would be
   full of und, die, stop. D looked promising (13049, 13047, 18147 = entziffern in Zimmermann, 15246 = oder), but only
   3 of its 142 groups hit, about what chance gives. Ruled out.
2. **Constant additive, −999 to +999 (the 26040 scheme), on all families.** The best outliers (B +402, 25 hits) come
   from repeated groups and give nonsense in the specimens (koennte, hollaendischen). Ruled out for these sets.
3. **18470 converted to 12444, 1777 and 2310 through Mendelsohn's page tables and block shift.** Hits against a shuffled
   page table: A 16 / 9 / 7 against a control mean of about 10, B 3 / 7 / 5 against 3.5, C 1 / 0 / 0 against 1, D 6 / 6 / 3
   against 3. Chance. Limit: the OCR of the tables keeps only about 125 of 300 pages with no conflict; the pass is only a
   partial test, though a real match should still have shown on those pages.
4. **Slider no. 1 (Mendelsohn p. 98), all 1,000 settings, against 13040 and the Verkehrsbuch groups he prints.** The
   rebuilt slider reproduces his worked example (41259 to 40429 at 718). The best settings produce nonsense
   (18111 to Einverstaendnis). Ruled out for these sets.
5. **Terminal pairs, which survive page renumbering** (`work/terminal.py`, `work/terminal2.py`). A family member should share the
   last-two-figure profile of its family. Nothing beyond chance. A against 13040 first reached 0.864 (control maximum 0.868), then
   z = 1.9 on the 270 clean group-word pairs, across many comparisons: noise. The Bernstorff text, as a control, gave z = -3.1.
6. **The "Dutchman" codes, in part.** Mendelsohn prints only their double-numbered pages. 18470 groups converted through those lists
   for 37000, 29000 and 2500, against shuffled pairs: all inside the control range (best: B on 37000, 12 hits, control mean 7.1, maximum
   17). This covers only a fraction of each code. 20000 could not be parsed from the OCR.
7. **Printed cribs.** Zeman, *Germany and the Revolution in Russia 1915–1918* (1958), has nothing from Berlin to
   Stockholm of these days. FRUS was not checked page by page. No German text of any of these telegrams was found.

Not tested beyond the partial lists in step 6: the "Dutchman" codes 2500, 37000, 29000, 20000; not tested at all: 9700, 5300 (Mendelsohn
describes them, but the full page tables were never printed). C's range would fit a code of that shape, but that is only a range [?].

## Remaining gaps

- All four systems, 938 groups - blocker: no-key-material; no code book or skeleton for marks 1219, 44xx, or for C and D reached online
- w752, the last 47 of 120 groups - blocker: no-key-material; missing from both American copies
- Any MI-8 or Room 40 decode - blocker: needs-physical-access; RG 165 MID 10xxx and RG 457 at NARA, TNA HW 7 for 1918 are not online

## Escalation

- [x] siblings: the Ludendorff and legation telegrams from the same batches split off as `ludendorff1918`; the five-letter telegrams (catalogue 655) stay open; Bernstorff's 1917 code tested
- [x] clear-pages: despatches 1421, 1426, 1475 and Christiania 1214, 1233–37 viewed; no decode or paraphrase filed; the cables were routed "To MID"
- [x] known-keys: 13040, 5950, 26040, 18470, 12444, 1777, 2310 and slider no. 1 tested against all that Mendelsohn prints; none fits
- [x] print: Mendelsohn 1937, Friedman's field-code study, Zeman 1958, web searches; FRUS 1918 not checked page by page
- [n/a] key-rebuild: nothing reads, so there is no foothold; 938 groups in four books give too few repeats to start from
- [n/a] retry: no key to retry with

## What would finish it

An MI-8 worksheet or Room 40 decrypt, or a Foreign Office code book. Politisches Archiv des Auswärtigen Amts, Berlin,
would hold the clear drafts by number and date, which the headers now supply: Nr. 923–925 of 1–2 July and Nr. 1010–1015
of 26–27 July 1918 to Stockholm. Those drafts would be the crib for all four systems. That is the concrete next step and
it needs an archive visit.

## Sources

- NARA RG 59, M367: [roll 141](https://catalog.archives.gov/id/27158076) ff. 1255–1266, [roll 114](https://catalog.archives.gov/id/27133946)
  ff. 0415–0418, [roll 122](https://catalog.archives.gov/id/27140577) ff. 0154–0155, [roll 108](https://catalog.archives.gov/id/27128808)
  (cable copies).
- Mendelsohn 1937 and Friedman, *Field Codes Used by the German Army*: NSA Friedman collection on the Internet Archive.
- Local only, not committed: `images/`, `view/`, `refs/`. The scripts in `work/` read `refs/m.txt`, the Internet Archive
  text with blank lines removed.
