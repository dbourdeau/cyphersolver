# JQA at St Petersburg: the despatches are NOT in the Armstrong code; his own code rebuilt, and Ford's
# "not decyphered" passage of No. 88 (25 June 1812) read

Page split, 14 Oct 2026 (one key, one entry): this entry was shown on the combined page `legation.html` with Erving's
24 March 1807 letter, which is in a different code (Pinckney's legation code, the = 1651). The two now have their own
pages: this one is `docs/jqa.html`; Erving's letter, a different cipher with its own page, is `docs/erving1807.html`
(folder `../erving1807/`). `legation.html` is a stub pointing to both.

Status: read in part (24 Oct 2026; kept on 14 Nov 2026, see "Integration check" and "Image check of the seven one-digit groups": remainder 164 of 177 words, 0.927; nine lines 97 of 100, 0.970). The paragraph below is the group count of 22 Sept 2026 (third pass). No. 88, measured with `measure.py`: **380 of 390 code groups read as sense
(0.974)**; the nine lines Ford left out 133/133 (1.000), the remainder 247/257 (0.961). 382/390 groups have a value;
362/390 (0.928) without the grade-I values. Still open: 7 groups cut by the microfilm gutter (needs the original)
and 3 single code groups (1508, 1185, 570).
The second pass (earlier on 22 Sept) stood at 0.910; see section 5.

Same code, another copy (27 Oct 2026, contributed by WAINUT): Anthony Morris's despatches from Spain, 1813-15
(catalogue 650), use this table with its sixteen blocks of 100 in reverse order (Morris 100i + r = JQA 100(15 - i) + r,
each block keeping its inner order); see [`../morris1813`](../morris1813/NOTES.md). Nothing in this folder is changed.

## 1. The premise, checked

- Madison editors on Armstrong's letters (Founders Madison/02-10-02-0369, 02-12-02-0197): code "also used by John
  Quincy Adams at St. Petersburg and by Jacob Lewis at Saint-Domingue; key not found but substantially reconstructed by
  the editors". On JQA to Madison, 7 Jan 1811 (Founders 03-03-02-0121): "a code provided by the State Department to
  John Armstrong in France and to both William Short and Adams" (citing Ford, Writings of JQA 3:328).
- Ford 3:327-28 (Smith's instructions, 1809) says JQA's own cypher was **the London minister's** (Pinkney's), and JQA
  was to *obtain a copy of Armstrong's* at Paris to correspond with him. JQA acknowledges receiving "the copy of General
  Armstrong's cypher" (Ford 3:~370). So JQA held both; the despatches to Washington use the other one.
- NARA M35 reel 3 (naId 188725601): every coded despatch checked uses a code with **the = 1385, of = 1576, that = 1384,
  and = 668, I = 1401**. THE=972 (Armstrong) has the = 972, of = 1354. The 592-entry Armstrong table renders these
  pages as noise (`../armstrong/decode972.py`). Reel 2 frame 0155 (1810) is in the same JQA code. The Founders note on
  the 7 Jan 1811 letter to Madison (a private letter, not a despatch) was not checked against its manuscript (Forbes
  collection, not online).

## 2. JQA's code rebuilt

Frames: NARA M35 reel 3, downloaded by `dl.py` from the catalogue manifest (`objects_M35_03.json` in the main
checkout's `targets/jqa/`; images `img03/`, git-ignored, not in the repo). `strip.py` and `crop.py` cut crops for reading.

**Structure.** A numbered syllabary: syllables, word-parts and common words, about 1,600 numbers; 1-100 mostly whole
words (13 observation, 16 Emperor, 29 United States, 37 together, 44 negotiation, 71 commerce, 78 President). Values
climb alphabetically only inside short runs (1384 that, 1385 the, 1388 then, 1391 there, 1392 these, 1393 they,
1394 think, 1399 this; 1592 on, 1594 one, 1595 ong, 1597 only), then the run breaks, so the alphabetical slot brackets
a value only where the neighbours are in order (`slots.py`). A superscript o after a group adds -s; a mark under a
group changes it (doubled letter, -ed, or a different word: 1107 paper, 1107+ well). A few groups carry two values in
the sources (508 rect and ear; 1570 of and occurr; 1173 when and would).

**Sources of the table** (all merged by `consolidate.py` into `code_table.tsv`, 1,166 numbers after the third pass: 431 H, 393 C, 324 M,
18 I; disagreements in `code_conflicts.txt`, hand decisions in `overrides.tsv`):

| File | What | Pairs |
|---|---|---|
| `pairs_jqa.txt` | clerk's interlinear decode, frames 0206 (No. 88) and 0189 (18 Sept) | ~400 lines, 262 H |
| `clerk_0182.tsv` | No. 80, 29 Feb 1812, interlinear decode, single leaf | 91 H, 19 M |
| `clerk_0184_0185.tsv` | frames 0184 (left, right top) and 0185 (both leaves), 1812, interlinear | 582 H, 518 M |
| `clerk_0190_etc.tsv` | 0190 (both leaves, continues 0189), 0183 right, 0194 right, 0198 right | 614 H, 327 M |
| `clerk_0048.tsv` | 0048 left, top block (1811), interlinear | 9 H, 5 M |
| `ford_pairs.tsv`, `_A`, `_B` | 1811 coded blocks transcribed from the film (`codes_ford*.txt`, 39 blocks: frames 0005, 0010, 0014, 0036, 0063, 0066, 0071, 0084-85, 0090-93, 0103, 0112, 0126, 0132) aligned with the plaintext Ford printed from the Department's decipherments (Writings vol. 4, OCR `ford_writingsofjohnqu04wort.txt`) by `align.py` and checked by eye | 589 C, 270 M |
| `slot_inferences.tsv` | values for No. 88 groups from slot + sense only | 9 I |

Grades: H the clerk's decode over the group; C fixed by Ford's printed plaintext between known neighbours; M the split
or the digit is a judgement; I slot and sense only. Transcription note: in this hand 5 and 6, 7 and 9, 0/6/8 are easily
confused; three No. 88 readings were corrected on 22 Sept from zoomed crops (gap line 1 168 not 158, line 2 1426 not
1425, line 4 302 not 502), and the underlined 1102 at the foot of frame 0206 left is a catchword, not a group.

## 3. No. 88, 25 June 1812 (the day after Napoleon crossed the Niemen): Ford 4:357 "[Nine lines of this paragraph
## not decyphered.]"

Triplicate, M35 reel 3 frame 0206 (the clerk's decode stops exactly where Ford's gap starts). Groups: `gap88.txt`
(133 groups). `python render.py gap88.txt` gives every group a value; 129 read as sense. Reading ([ ] = grade I,
{ } = valued but not sense):

> ... and expectation. But the [journ-ey] itself of the Emperor Alexander to Wilna was in opposition to the
> Chan-ce-ll-or and adv-ice, and if his active influence had not been im-pa-ir-ed before it, it can scarcely
> fail to have been affected by his illness immediately after his arrival [thither], which was undoubtedly an
> apo-ple-ct-ic stroke. Since then he has had a second and a more severe one. In the German Gazettes even his
> death has been announced; but that was a mistake. At all events it is scarcely possible that he should remain much
> longer in the department of foreign affairs.

"He" is Count Rumyantsev (Romanzoff), Chancellor and foreign minister, who had gone to Wilna with Alexander. The
passage reports that the journey to Wilna went against the Chancellor's advice (83 opposition, now grade C from
No. 73), his apoplectic stroke soon after arriving, a second and worse one since, a false report of his death in the
German papers, and JQA's judgment that he cannot long stay at the foreign ministry. That fits the known history (a
stroke in 1812 that cost him his hearing; retired 1814). It differs on timing from standard accounts (Britannica,
Wikipedia), which tie the stroke to the news of the Niemen crossing on 24 June: JQA, writing on 25 June before that
news could reach St Petersburg, places the first stroke soon after Rumyantsev reached Wilna and a second before
25 June. Ford printed none of this. JQA's diary for September 1812 records Romanzoff speaking of two strokes of
apoplexy suffered with the Emperor at Wilna.

im-pa-ir-ed: the groups on the page are 1424 [1102] 1112 1433 520. JQA's catchword at the foot of the left leaf is
1102 (pa, C 9x), the group he meant to begin the next page with, and in No. 83 (0190L5) he writes un-im-pa-ir-ed as
1477 1424 1102 1435 520 (1435 ir, C 3x). The 1112 1433 at the top of the right leaf are his own copying slips
(one digit each) for 1102 1435; read as intended, *impaired* (grade C by the No. 83 parallel).

## 4. The "remainder of letter ... undecyphered" (Ford 4:358)

Frame **0207** (left leaf): 13 lines of code, then clear sentences (Manifestos of both parties expected; Peace with
Turkey signed a third time; "It is not General Kutuzoff but Count Rostopchin who is appointed Governor, civil and
Military, of Moscow"), then 5 more lines. Groups: `rem88.txt` (257 groups, 7 with digits lost in the gutter).
249 valued, 247 read as sense:

> If this proposition has in any form been disclosed to the Russian government, it was certainly neither unreasonable
> nor im-[mod(erate)] nor inconsistent with a system rigorously and [in]-[fl]-ex-[ib]-ly de-fen-sive (underlined), to
> meet it with a proposition for the e-va-cu-ation of Prussia by the French troops as {1508} [pre]-liminary to
> negotiation. But the very point upon which the ambassador manifested the most sensibility in speaking of Prince
> Kurakin's last note was that it held out a proposition with which it would be dishonourable in France to comply. He
> {1185} it as a demonstration that the Emperor Alexander had determined not to [negotiate] at all - it {tol} he
> [sa]-id - such a proposal as France had never thought of making to Russia even after the [bat]-tle of Fri-ed-la-nd.
> [clear text] ... an army of reserve is forming there, and it is [...] probab-le that if great success on the, on the
> side of the French should mark the commencement of the war, the Emperor Napoleon will at-[tem]-p-t to pene-t-rate
> directly to that centre of the em-[pire] than [along] the sho-res of the Baltic.

The ambassador is Lauriston, the French ambassador; Kurakin's note is the Russian ambassador's demand at Paris for the
evacuation of Prussia (April 1812), which Napoleon treated as a declaration of war. "Even after the battle of
Friedland" (June 1807, before Tilsit): France had never proposed evacuating Prussia even when Russia was beaten.

## 5. Third pass (22 Sept 2026): 0.910 -> 0.974

New sources: the clerk's interlinear decodes on 0047, 0048 (rest), 0210-0211 and 0247 (`clerk_0047.tsv`,
`clerk_0048b.tsv`, `clerk_0210_0211.tsv`, `clerk_0247.tsv`, 560 pairs; `clerk_notes_pages2.md`), and coded blocks of
eight 1811-1812 despatches aligned with Ford vol. 4 (`codes_ford1812*.txt`, `ford1812_pairs*.tsv`, 1,926 pairs;
No. 95 against the Department's clear copy on 0230-0232; `ford1812_notes.md`). `consolidate.py` now reads them; the
table has 1,166 numbers (with `ford1812_pairs_b.tsv`: Nos. 71, 72, 74, 75, 81; `ford1812b_notes.md`).

What moved, with evidence:

| No. 88 | was | now | evidence |
|---|---|---|---|
| gap88 l.3-4 `1424 [cw 1102] 1112 1433 520` | {im-pas-sion-ed} | im-pa-ir-ed, *impaired* (C) | catchword 1102 pa; No. 83 un-im-pa-ir-ed = 1477 1424 1102 1435 520 (0190L5): 1112 1433 are JQA's slips for 1102 1435 |
| gap88 l.2 `1025 1016 1457 908` | Chan-ce-{last}-or | Chan-ce-ll-or (C) | No. 73 (0165, Ford 4:256) writes the same four groups, 1457 with the doubling mark = ll |
| gap88 l.5 first group | 492 use | **792** by (H) | re-read on 0206R: an open hook, not this hand's looped 4 |
| rem88 l.4 `142x 350 289 1403 897` | few-ex-table-ly | [in]-[fl]-ex-[ib]-ly, *inflexibly* (I) | slots 1401 I < 1403 < 1404 ic and 347 fit < 350 < 352; 350 has a hook under the 0; the single Ford alignments (few, fi, table, cal) disagree with each other, and the 0194 "1403" (cal-cu-late) has a blotted 4, probably 1003 cal |
| rem88 l.5 | e-va-{1081}-ation | **1061** cu (C): e-va-cu-ation | the blurred digit is a 6 (as in 864, 1576); 1061 cu in Ford 0005 and cal-cu-late (0194); slot 1060 ct < 1061 < 1062 cur |
| rem88 l.11 `426 699 1535+` | ne-{at}-{al} | [negotiate] at all | 1535 with the doubling mark = all; 426 slot 423 need < 426 < 428 nei (I) |
| rem88 l.13 `1309 888 1576 996 520 1453 416` | {...} long of {...}-ed la-nd | [bat]-**588** tle(d) of Fri-ed-la-nd | 996 = fri (C, No. 95 fri-end-ship x2, a fri-end x2); 1453 la, 416 nd (Fin-la-nd); the second group is 588 (the 5 has its top bar), 588 = tled (set-tled, C); 1309 slot 1308 bas < 1309 < 1310 be (I) |
| rem88 l.16 `220 586 1384 1416` | {proper le the if} | probab-le that if | 220 = probab (clerk 0047R19 'it is probab-le that', 0190L6, 0190R26; the lone 0184R11 'proper' is the outlier); the third group is 1384 (4 over 5) |
| rem88 l.18-19 `539 927 1383 1540 1385 1097 748` | em-{927} the {ambass} the side-{res} | em-[pire] than [along] the sho-res of the Baltic | 927 context only (I); 1540 slot 1537 alliance < 1538 ally < 1540 (I); 1383 than and 1097 sho are digits JQA overwrote (5/3, 9->7; M); 748 res (M) |

## Verification 5, 23 Oct 2026

Plain-bar check (English 1812; the gap entry had been listed as French): both No. 88 entries were scored on decryption
files with hyphenated syllables and group tables. Readings written out with words joined and grade-I words marked:
`texts/no88_gap_reading.md` (plain 0.9, explicit 1.0) and `texts/no88_remainder_reading.md` (plain 0.688, explicit
0.812). Both keep read.

## Outside validation and later users of the code (Brice Dudout, 27 Oct 2026)

Brice Dudout (Europe chiffrée) read Crawford's Paris letter of 15 Aug 1813 (catalogue 652) and Everett's Madrid "Notes
of a conversation with Mr Zea" of 25 Sept 1825 (catalogue 638) with this table, frozen before use (SHA-256). His two
held-out checks are the first tests of the table against decodes it was not built from. They are his measurements,
not repeated here:

- Crawford's despatch No. 4, Paris 3 Sept 1813 (M34 roll 17 frames 0031-0032), against its interlinear decipherment
  of the time: 194 of 226 and 224 of 246 values agree (0.858, 0.911); the same table with shuffled values reaches at
  most 0.027 and 0.020 (99th percentile).
- Everett's despatch of 8 Sept 1825 (M31 reel 27 frames 0061-0064), against the Department's decoding printed by
  Manning (doc. 1133): 288 of 304 groups agree (0.947); permuted-value control p99 0.023.

So Crawford in 1813 and Everett in 1825 used this code (Weber's "Monroe Cipher", 1979, as Dudout identifies it). Two values
he supplied that the table lacked are added as overrides: 126 convey (grade I, slot and sense) and 1323 been (grade M,
from the 1813 interlinear decipherments). The values he uses that disagree with the table, or that only one later
writer attests, are kept apart in `overlay_dudout.tsv` and are not in `code_table.tsv`: the date digits of Crawford's
heading (952 = 1, 959 = 8, 954 = 3), 1264 as a full stop, and Everett's 557 thro. (Corrected 5 Nov 2026, issue #203: the heading
groups are 952 959 952 954, not 932 939 932 954, and the key sheet M97 frame 1057 prints 951-960 = 0-9; 580 was is withdrawn: the groups
under "was" are read as 500, the least certain of the corrections, and the groups read as 402, 901 and 1106 are 482, 981 and 1186,
which the table already has.) WAINUT's readings
(crawford1813, ellis1839) reached 1264 = full stop and 1323 = been independently; their other proposals are in the
"Proposed table changes" sections of crawford1813 and everett1825, still not applied. The digits are sound for
Crawford: the legation register (frame 0005, checked here) dates the letter 15 Aug 1813, and "952 959 952 954" can
only be 1813 (the groups 932 939 932 were a misreading of 952 959 952).

## Verification with the surviving code sheet (Brice Dudout, 14 Nov 2026)

Since PR #200 (Andrew Beling, for `../morris1813`) the repository holds a transcription of the State Department code
sheet itself, NARA M97 roll 13 frames 1056 (alphabetical) and 1057 (numerical), the code Weber (1979) prints as WE028:
`../morris1813/beling/key/codebook_M97_13_transcription.csv`, 1,600 entries in the order of this table (the = 1385,
of = 1576). It had not been applied to No. 88. It is used here unchanged; no value is added to it.

**Held-out check.** Before use, the sheet was tested against every grade-H pair of the clerk's interlinear decodes in
`clerk_*.tsv` (the sheet was not built from them). Rule and threshold written and frozen by SHA-256 first (agreement
>= 0.80 and >= best of 200 shuffled keys + 0.30): **1,624 of 1,742 pairs agree, 0.932; shuffled keys at most 0.044
(p99 0.025)**. `we028_measure.py`, `we028_measure.txt`. So JQA's code of 1811-12 is WE028. Of the
table's H and C values, 138 of 823 differ from the sheet (mostly single-occurrence C values; a few are clerk splits
such as 948 rus / Russia).

**No. 88 with the sheet.** Every group of `gap88.txt` and `rem88.txt` decoded with the sheet and compared with
`code_table.tsv`, group by group in `we028_no88.tsv` (status sure / probable / restored / unresolved). Frames 0206 and
0207 re-read on the NARA images where the two disagree.

- Grade-I values the sheet confirms: 143 moderate, 350 fla, 1403 ib (in-fla-ex-ib-ly), 426 negociat, 1309 bat,
  1540 along, 1434 journ, 168 ey.
- Two transcription errors, corrected on the image: rem88 l.10 **262** (st), not 252 (demon-st-ration); l.11 **649**
  (min), not 549 (de-ter-min-ed).
- One-digit slips the sheet and the sense fix (probable): 1864 for 1364 tain (no number above 1600); 669 for 569 to;
  588 for 568 tle (bat-tle; 588 is learn/term); 508 for 518 ect (dir-ect-ly); gap 818 for 518 ect (exp-ect-ation);
  gap 1575 for 1515 adv (adv-ice; 1575 is oe and the image reads 1575); gap 1585 for 1535 al (1585 is ok).
- Gutter groups whose visible digits fit the sheet value: 142x in (1426), 1xxx sa (1068; "10" visible), 13xx temp
  (1374), 15xx ad (1513, am-bas-ad-or), 21x pre/pri; 11xx (pro-po-...) is read from the sense.
- Changed: rem88 l.19 927 is oud on the sheet, not pire; 727 is **rather** (7/9 are confused in this hand), so the line
  reads "to that centre of the em[pire] [rather] than along the shores of the Baltic"; JQA wrote only em (539).
  Gap l.5 1398 is thirty on the sheet (14 thither, 1391 there): the earlier grade-I thither is withdrawn and the word
  is restored as [there].
- Still unresolved: 1508 (acious / account), 1185 (wick; "He considered it", 118, would fit but is not what is
  written), 570 (tol / toe; "it was, he said" would want 500). 55x (gutter) can only be 558 thus among 550-559.

**Counts (Daniel's rule, words; texts/no88_remainder_reading.md and texts/no88_gap_reading.md rewritten):** the
remainder 172 of 177 words read as sense (161 sure, 11 probable; 2 restored, 3 unresolved) = **0.972**, up from 0.938,
so **read** (this is the contributor's count and proposal; the strict count and the class kept are in the Integration
check below). Ford's nine lines 98 of 99 = 0.990 (one restored word). Groups: 384 of 390 sure or probable (0.985).

No new value is proposed for the table; `code_table.tsv` is left as it is. The sheet is the better key for this code:
where they differ, `we028_no88.tsv` gives the sheet's value.

## Integration check, 14 Nov 2026 (PR #596)

Brice Dudout's verification above was re-run here before it was merged.

- **Held-out check.** `we028_measure.py` re-run: 1,742 pairs, 0.932, shuffled maximum 0.044, as stated. The script
  counts a pair as agreeing when one value begins with the other; with exact matches only it is 1,528 of 1,742
  (0.877). The 1,742 pairs are 423 distinct codes. That the sheet transcription was made without these decodes is
  Andrew Beling's and the contributor's record. The conclusion stands: JQA's code is the State Department code of the
  M97 sheet (as the morris1813 work had already found from the other side).
- **Decoder.** A decoder written here from the sheet CSV gives the sheet value of each of the 390 rows of
  `we028_no88.tsv` (369 sure, 15 probable, 3 restored, 3 unresolved).
- **Image.** Frame 0207 was fetched from the National Archives Catalog (NAID 188725601) and lines 8-12 and 14-17 of
  the remainder compared with `rem88.txt`: about 95 groups agree, and the two corrections are right, l.10 reads 262
  and l.11 reads 649. `rem88.txt`, `code_table.tsv` (252 *str*, 549 *min*) and `overrides.tsv` still carry the old
  digits: `we028_no88.tsv` is the corrected record until they are brought into line. Frame 0206 was not compared. (Brought into line later the same day, and frame 0206 looked at: next section.)
- **Count and class.** By the strict rule of this project a probable or restored word is a hole. Remainder: 161 sure
  words of 177, **0.910** (the contributor's 0.972 counts the 11 probable words as read). Nine lines: *expectation*,
  *advice* and *Alexander* rest on one-digit slips and *[there]* is restored, 95 of 99, **0.960**; *impaired* is kept
  as read because the catchword 1102 is written on the leaf. The two reading files now mark the probable words
  `{?word}` and the unresolved groups `[n]`. The remainder is under 95%, so the target stays **read in part**; the
  move to "read" proposed in the PR is not applied. The remainder was 0.938 on 24 Oct only because the words on
  gutter-cut groups and digit slips were not marked then.
- What the sheet settles: eight grade-I values confirmed, *thither* and *pire* withdrawn, and the three open groups
  now have sheet values that do not read (1508 *acious*, 1185 *wick*, 570 *tol*), which points to a digit misread or a
  writer's slip in each, not to a missing key value.

## Image check of the seven one-digit groups, and the one-digit rule (14 Nov 2026)

Owner's decision of 14 Nov 2026, now in README Conventions: a code group one digit away from the value the sense
wants counts as read when (1) the key is the surviving key of the period, (2) the correction changes one digit,
(3) the group is part of a word whose other groups are read from the key. The slip is marked in the reading and
listed on the page. A group whose key value gives no sense and has no such correction stays a hole.

The key here is the M97 roll 13 sheet (WE028), a surviving period key, used unchanged: condition 1 holds for all seven.

**Images.** Frames 0206 and 0207 fetched again from the National Archives Catalog (NAID 188725601; the search proxy
`catalog.archives.gov/proxy/records/search?naId_is=188725601` lists the objects, the JPEGs are
`.../medialz/dc-metro/rg-059/603720/M35/M35-03/M35-03-0206.jpg` and `-0207.jpg`; plain HTTPS, no bot check). Each
group enlarged 8 to 12 times. The film is bitonal: a blotted digit cannot always be told.

| Group | Place | Wanted (sheet) | On the image | Single digit | Inside a word read from the key | Verdict |
|---|---|---|---|---|---|---|
| 1864 | rem l.2, 1021 **1864** 897 cer-tain-ly | 1364 tain | 1864: the second digit is a closed two-lobed 8 (the 3s of 399 and 539 on the next line are open); no number above 1600 on the sheet | yes | yes (1021 cer, 897 ly) | Adams's slip; rule applies: **read** |
| 669 | rem l.6, 949 **669** 44 (pre-limina-ry to negotiation) | 569 to | 669: the first two digits have the same shape | yes | **no**, 569 to is a whole word | Adams's slip, but condition 3 fails: **hole** |
| 588 | rem l.13, 1309 **588** bat-tle | 568 tle | 5, then a one-loop digit that may be 6 or 8, then 8 | yes | yes (1309 bat) | digit not told; with 6 it is the sheet's group, with 8 a slip under the rule: **read** either way. rem88.txt keeps 588 |
| 508 | rem l.18, 844 **508** 897 dir-ect-ly | 518 ect | 508, a small raised 0 | yes | yes (844 dir, 897 ly) | Adams's slip; rule applies: **read** |
| 818 | gap l.1, 295 **818** 864 exp-ect-ation | 518 ect | first digit with a closed lower loop, like the 8 of 864 beside it; a blotted 5 is not excluded | yes | yes (295 exp, 864 ation) | a slip under the rule or the sheet's group: **read** either way. gap88.txt keeps 818 |
| 1575 | gap l.3, **1575** 1405 adv-ice | 1515 adv | 1575, the third digit has the bar of a 7 | yes | yes (1405 ice) | Adams's slip; rule applies: **read** |
| 1585 | gap l.1, 16 **1585** / 1549 828 Emperor ..-an-der | 1535 al | the third digit is written over another, 3 or 8 cannot be told; a faint stroke cut by the gutter follows at the line end | not told | the word as written also lacks ex (289; rem l.10 has 1535 289 1549 828) | **hole** |

None of the seven was a misreading here: where the digit can be told the image has the transcribed digit, so the
slips are the writer's (the leaf is Adams's triplicate). The three groups whose sheet value gives no sense (1508,
1185, 570) and the gutter-cut 55x stay holes, as before.

**New on frame 0206.** The left leaf also runs into the gutter. After 908 with the plural mark (gap l.2,
*Chancellor's*) the heavy stroke of a further group is visible at the edge, and the sentence wants a noun ("in
opposition to the Chancellor's ... and advice"). The group is not in `gap88.txt` (133 groups as before); it is counted
as one lost word.

**Recount (words, strict rule plus the one-digit rule).**

- Nine lines: 100 words (99 and the lost word), 97 read, **0.970**. Holes: {?Alexander}, [...], [there]. (95 of 99
  before; *expectation* and *advice* now read.)
- Remainder: 177 words, 164 read, **0.927**. *certainly*, *battle*, *directly* now read. Holes (13): six words on
  gutter-cut groups (inflexibly, preliminary, ambassador, proposition, said, attempt), *to* (669, a whole word),
  *empire* (written em only), [thus], [rather], [1508], [1185], [570].
- The remainder is under 95%: the target stays **read in part**. The remainder holds it back; the six gutter-cut
  words alone would take it to 170 of 177 (0.960).

**Files brought into line with the sheet.** `rem88.txt` l.10 262 and l.11 649; `pairs_jqa.txt` rows 252 str, 549 min
and 1398 thither commented out; `overrides.tsv` rows 252 str and 927 pire commented out; `code_table.tsv` edited by
hand in the same four places (252 Sp M from the remaining sources, 549 and 927 removed, 1398 without "also thither":
1,166 numbers) and `code_conflicts.txt` regenerated. `consolidate.py` was not used to rewrite the table: it breaks
ties between spellings by set order, so a re-run changes seven unrelated rows (13, 403, 730, 1150, 1400, 1484, 1565)
each time. `python measure.py` now gives 379 of 390 groups (rem88 246 of 257: 927 has no value); the 380 of the
22 Sept paragraph above is the figure of that date. `validation.tsv` (the file of the 11 Oct test) is left as it was
tested. The table still carries its rebuilt values for the slip groups (818 pect, 1575 adv, 1585 Alex, 1864 tain,
588 tled, 508 rect): they are the values the 22 Sept reading used, not the sheet's.

Credit: the check with the code sheet and the seven proposed corrections are Brice Dudout's (PR #596); the image
check of the seven groups was done here.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/detail.py` re-applied `code_table.tsv` (the only key file the profile named) to `gap88.txt` and
`rem88.txt` and compared the letters with the two readings in `texts/`: nine lines 15 of 97 words, remainder 18 of 164,
together 33 of 261 words with a letter the table does not give and no bracket. The two texts were then compared by
hand, line by line, with the sheet values of `we028_no88.tsv`. Causes:

- Key file not the key of the reading. Since 14 Nov 2026 the readings follow the State Department code sheet
  (`we028_no88.tsv`, "sheet value"), not the rebuilt table, and the profile still named the table alone. Example:
  rem l.2-3 `428` and `143` are "nei" and "mod" in `code_table.tsv` and "neither" and "moderate" on the sheet; the
  reading prints "neither ... immoderate". Others: 632 media (im-media-te-ly), 1157 possib, 948 Russia, 193 honor,
  728 ration, 1019 cent.
- Clear words in the code lines (scarcely twice, undoubtedly, In the German Gazettes, troops, Prince Kurakin's) are
  written out in `gap88.txt` and `rem88.txt`; the script, which keeps only keyed groups, counts them as supplied.
- Spelling: the reading prints Wilna for will-na, illness for il-ness, meet for met, rigorously for rig-our-ous-ly,
  dishonourable for dis-honor-able, negotiate and negotiation for negociat and negociation, success for suc-ces.
- Marks of the manuscript that the two transcription files do not carry. Section 2 above describes them (a superscript
  o adds -s; a mark under a group doubles a letter, adds -ed or changes the word), and two cases are documented:
  gap l.2 `1457` with the doubling mark = ll and `908` with the plural mark (Chancellor's), rem l.11 `1535` with the
  doubling mark = all. `gap88.txt` and `rem88.txt` hold the bare numbers, so the key gives "chan ce last or" and "al".
- Words printed without a bracket where the groups as transcribed give something else, and no file of this folder says
  why (8): gap l.4 a second "it" ("before it, it can": one 1440 in `gap88.txt`); gap l.9 "events" (283 event) and
  "all" (1535 al); gap l.10 "affairs" (sheet 1517 affair); rem l.1 "disclosed" (674 983 dis-close); rem l.3 "system"
  (399 539 sy-em); rem l.4 "proposition for" (219 1148 1098 981 pro-po-si for); rem l.12 "making to Russia"
  (611 500 948 make was Russia: two words). Some may be marks of the kind above; the film was not looked at for this
  audit, so that is not known.
- Documented but not bracketed in the reading text: "impaired" for 1112 1433 im-pas-ion-ed (section 3 and the note
  under the reading: Adams's slips for 1102 1435).

Changed: `key_we028_no88.tsv` added, one row for each of the 209 different groups of the two texts with the sheet value
copied from `we028_no88.tsv` (source line in the third column; 262 st and 649 min from its "read as" column, the two
groups re-read on the image); each value was compared with `../morris1813/beling/key/codebook_M97_13_transcription.csv`
and equals one of its readings. It is listed in `profile.json` `outcome.key_file` after `code_table.tsv`. Groups written
with a slip keep the sheet value as it stands (818 del, 1575 oe, 1585 ok, 588 learn, 508 ear, 669 ang, 927 oud,
1398 thirty). No reading, decryption or transcription file was changed, and nothing in `code_table.tsv`.

After, with the sheet key alone: nine lines 13 of 96, remainder 16 of 164, together 29 of 260. `detail.py` itself still
prints 33 of 261, because it keeps the key file whose output is nearest the reading, and that is the rebuilt table,
which carries the values the reading wants at the slip groups (818 pect, 1575 adv, 1585 Alex, 1864 tain). What is left
is the clear words, the spellings, the marks and the eight words listed above.

Marked on 16 Nov 2026. `texts/no88_gap_reading.md`: 5 places bracketed, no letter changed: impa[ir]ed, [it] (the
second "it" of l.4), al[l], event[s], affair[s]. `texts/no88_remainder_reading.md`: 5 places: disclose[d], sy[st]em,
proposi[tion] (rem l.4), mak[ing], [to] (before Russia). Left unmarked: Chancellor's and "at all" of rem l.11 (marks
documented above), the spellings, and the clear words. A sentence was added to the comment at the head of each file:
what the new brackets are, that the film was not looked at for them, the spelling convention, and that the Count
section of the file predates the marks. Those Count sections (97 of 100; 164 of 177) and the same figures in the
Status line, the profile and the page were not redone: by the files' own convention a bracketed word is a hole, which
would take the nine lines to 92 of 100 and the remainder to 159 of 177 if none of the ten is a mark on the film.
`v2_score.py` hole rate: nine lines 0.039 before, 0.088 after; remainder 0.079 before, 0.107 after. The page was not
changed: its "Key: code_table.tsv" line is inside the generated texts block.

## No. 85 and No. 74, 21 Nov 2026 (leads 992 and 991; contributed by Andrew Beling, with AI agents)

Done by AI agents on 21 Nov 2026; no person has checked it. Working records: [`beling/no85_no74_2026-11-21/`](beling/no85_no74_2026-11-21/README.md).

**What the film has.** No. 85 (27 May 1812) is on reel 3 as a duplicate: frames 0195 right, 0196 and 0197 left. The clerk's
interlinear words on the code block of 0196 left stop at "Dominions" (854 649 1433, Do-min-ion-s, line 11); the rest of that
line and lines 12-16 are bare (Ford 4:338 ends the passage at "dominions." without a note). On 0197 left two runs of code stand
bare in the clear text: Ford 4:339 "[Here two lines of cypher not decyphered]" and "[here three lines of cypher not
decyphered]". For No. 74 (2 Nov 1811, frame 0168) the clerk wrote a separate sheet (frames 0170-0171) on which three groups are
copied in figures, 387.1431.1101, with a cross and the note "Error in Cypher." (Ford 4:270).

**Transcription.** Two agents copied every group of 0196 left, 0197 left and 0168 (both leaves) and the clerk's sheet, blind to
each other, to any table, to the files of this folder and to print (796 tokens; the same number at 717; doubted by neither at
600). A third agent later read 0197 and the first line of 0168 blind as well. Its blind reading agreed at every group except the last of the two lines, where it first read 528 and on a second look 548; it left 116x, 891/841 and the gutter group open, as the transcribers did. The right leaf of 0168 has 20 lines of code.

**Check before reading (plan written first, one run).** The code sheet (NARA M97 roll 13 frames 1056-1057, Weber WE028;
`../morris1813/beling/key/`), unchanged, against the clerk's own decipherment of these two despatches, number by number, scored
only where both transcribers read the same number without doubt; pass mark 0.85; control, the sheet's values shuffled 1,000 times.
No. 85 (clerk's words over the groups, 112 scored numbers): 0.929 and 0.911 on the two transcriptions, largest control 0.062.
No. 74 (aligned with the clerk's sheet, 367 scored numbers): 0.935 and 0.932, largest control 0.131. Both pass. Of the eight
misses of the first part, five are places where the readers took the clerk's small writing as "ri", "news", "have", "in", "ce"
and the sheet has mi, view, har, ir, re; Ford, who printed from the Department's decipherment, has "armament", "views",
"harbored", "irretrievably", which are the sheet's values, so these are taken as misreadings of the clerk's hand, not faults of
the sheet (the third agent's report records the opposite view). One is a real difference: 350 is fla on the sheet and stands
in con-fi-den-ce.

**The two lines** (`no85_two_lines.txt`, 26 groups; `texts/no85_two_lines_reading.md`): "You will here perceive some uncertainty
how far the neutral intention[s] and expectation[s] of Sweden herself extend." 17 words, 15 read = 0.882: the s of
intention[s] and expectation[s] is supplied from the plural mark, so both are holes (README Conventions, 16 Nov 2026). Read under the
short-text floor (README Conventions, 19 Nov 2026: fewer than 40 cipher words, at most 2 holes): 15 of 17, 2 holes. Not in print; not read here
before.

**The three lines** (`no85_three_lines.txt`, 35 groups, two cut or blotted; `texts/no85_three_lines_reading.md`): "and the
Swedish meaning of it is to be [?expounded] by the hope of being {+in}demnified [?in] Norway [?for] the los[s] of Finland".
23 words, 19 read = 0.826. The holes: los[s] (the sheet gives lose; the s is supplied); 116x with its last figure blotted (pound 1160, or plain 1138); 1626, a number the code
does not have (in, 1426, is one digit away); 9x cut by the gutter (for, 981). 1436 (is) stands where in-dem-ni-fied wants 1426.
With the clear text around it: "If the English Regent's new Proclamation respecting the Orders in Council is to elucidate the
English meaning of neutrality, and the Swedish meaning of it is to be ... by the hope of being indemnified ... Norway ... the
loss of Finland, the roots of that neutrality are not very profound." Not in print; not read here before.

**The six lines after "Dominions"** (`no85_foot.txt`, 75 groups; `texts/no85_foot_reading.md`): a second reading of the lines
first read with the rebuilt table on 22 Sept 2026 (`ford1812b_notes.md`), now with the code sheet. It agrees with that reading,
except that 49 is United States on the sheet where September guessed 'they' and the dots after 'Norway' are line filler, and adds the sheet value of each number that does not fit (1236 ground, 209 pres, 49 United States, 1501 A, 820 delegate, all
five in three independent transcriptions), Sweden (39) for the 49 where the September reading guessed "they", and that the dots
after "Norway" are line filler, not "without". 55 words, 50 read = 0.909 (objection[s], with its s supplied from the plural
mark, is a hole). Three of the five numbers that do not fit (1236, 209, 820) count as read under the one-digit rule; 49 and
1501 are holes.

**No. 74, the three groups "in error".** On the sheet 387 is sue, 1431 into, 1101 P. The line is 199 888 1399 143x 387 1431
1101 948 668 869 ...: how long this [is] sue into P Russia and Austria, that is, "How long this is-sue into P-russia and Austria
will be suffered to remain open is extremely doubtful." No number needs changing. The clerk took "is" for the verb, could make
nothing of "sue into p", and wrote "Russia" where the code has Prussia; thirteen lines further on (left leaf line 14, 668 1101
948) he read the same pair as "Prussia". How firm: **Prussia** is firm (1101 and 948 are read alike by all, and the third agent,
blind to the clerk's sheet, reached it independently). **issue** rests on the clerk's own figures: he had the paper and copied
387, and wrote "is"; on the film two of the three blind readers took the first figure of 387 for an 8 (887, lo), and the last
figure of the group before it is too faint to tell 5 (ir) from 6 (is). In "It is understood" on frame 0196 the clerk likewise
wrote "is" over a group both transcribers read as 1435 (one of them with 1436 as an alternative). `codes_ford1812b.txt` (0168 left line 1) is left as it was.

**Print.** Ford 4:270, 338-339 only, with the gaps. Internet Archive full-text search on three phrases of the surrounding clear
text (21 Nov 2026): copies of Ford's volume and nothing else. Founders Online ("neutrality of Sweden", "suffered to remain
open"): no results. Not seen: Adams's own letterbook copy (Adams Papers microfilm reel 136, Massachusetts Historical Society,
not online), which should have the plain words.

**Counts and weaknesses (recount of 22 Nov 2026).** The counts above follow the rule of 16 Nov 2026: a word with a supplied
or emended letter is a hole. The first count of 21 Nov had taken intention[s], expectation[s], objection[s] and los[s] as read
(17 of 17, 20 of 23, 51 of 55). The two lines, at 15 of 17 with 2 holes, are "read" only under the short-text floor of
19 Nov 2026 (`floor_used` in profile.json); the other two are read in part. Four further weaknesses, stated plainly:
- The test plan was frozen before the run, but its SHA-256 (494b6a49...) was recorded only in our local files; the frozen
  plan and the file of checksums are not in this folder, so the freeze cannot be checked from the repository.
- Two disputed digits were settled partly by sense: 548 against 528 (two lines, last group; *end* makes a word, *ei* does not)
  and 398 against 298 (three lines, *Sw-ed-ish*), each with an enlargement and the third reader also favouring 548 and 398.
- "issue" in No. 74 rests on the clerk's figure 387; on the film two of three blind readers saw 887 (*lo*, no sense).
- Adams's own letterbook copy (Adams Papers microfilm reel 136, Massachusetts Historical Society) was not seen. It should
  carry the plain words and would settle the holes.

## Adams's despatches of 1810 (held-out test, 22 Nov 2026)

Andrew Beling, with AI agents; files in `beling1810/` (README there). Nothing outside that folder changes the table,
the clerk files or the readings of No. 88.

**What.** Adams's despatches Nos. 21-29 of 1810 (NARA M35 reel 2) are in this code, as noted in section 1 for frame
0155. Seven have coded passages. Six can be paired with an independent plaintext: No. 21 with Ford 3:469, and Nos. 23,
24, 25, 27 and 28 with the decipherments made in the Department and filed with them (frames 156-159, 169-172,
178-179, 184). No 1810 material went into `code_table.tsv`, so these 22 passages, 3,083 groups, are a held-out test of
it. No. 29 (19/31 Oct 1810, frames 185R-189L) has no decipherment and is decoded with the key sheet alone.

**In print.** Ford vol. 3 prints Nos. 21, 23 and 24 with their coded passages in clear and in italics (3:469,
3:486-496, 3:503-507), and No. 22, which has no code. The 1980 documentary volume *The United States and Russia: The
Beginning of Relations, 1765-1815* prints No. 27 with both passages (seen only through the Internet Archive's full-text
search of its loan copy). *American State Papers, Foreign Relations* vol. 3 has none of them. Part of No. 25 is in
print: Paul Cernovodeanu, "American Diplomatic Dispatches on the 1806-1812 Russo-Turkish War and on Bessarabia's Rapture," *Revue Roumaine d'Histoire* XXXVII (1998), 1-2, 19-41, p. 29, prints its closing paragraph and the first paragraph of passage G (our research file of 22 Oct 2026,
from a scan read then; not re-opened for this package). The rest of No. 25, and No. 28, were not found in print, and
No. 29 was not found in print or in a contemporary decipherment.

**Plan, written first.** `beling1810/PLAN.md`, hashed before the first run (`PLAN.sha256`, 22:40 EST). The measure is
`align.py`'s own alignment, imported unchanged, with the table alone: the share of valued groups whose table value
falls on the witness letters at that place. The control is 100 tables with the value sets shuffled among the numbers.
The pass mark is pooled agreement >= 0.80 and >= the best shuffled table + 0.30.

**Result: MISS.** Over 3,083 groups:
- 2,843 have a value in the table (coverage 0.922).
- Agreement is **0.730**. The shuffled tables reach best 0.125 and median 0.077.
- The separation from chance is large, but agreement is under the 0.80 that was set, so by the plan this is a miss.

| Despatch | Groups | Agreement | Coverage | Read words, strict |
|---|---|---|---|---|
| No. 21, 16 Aug 1810 | 33 | 0.719 | 0.970 | 14/21 (0.667) |
| No. 23, 5 Sep | 1,014 | 0.721 | 0.927 | 417/829 (0.503) |
| No. 24, 20 Sep | 458 | 0.708 | 0.904 | 164/366 (0.448) |
| No. 25, 30 Sep | 1,266 | 0.739 | 0.920 | 456/845 (0.540) |
| No. 27, 12 Oct | 267 | 0.760 | 0.936 | 117/196 (0.597) |
| No. 28, 10/22 Oct | 45 | 0.690 | 0.933 | 18/74 (0.243) |
| All | 3,083 | 0.730 | 0.922 | 1,186/2,331 (0.509) |

Read words, strict: a word of the witness counts only when every letter comes from a group whose table value the
alignment places there. By that count the table alone reads half the words. The passages are read, but from the period
decipherments, not from this table.

**Why under 0.80: the transcriptions.** Two transcriptions were made for three despatches; the second readings of
Nos. 24 and 29 were made blind by helper agents from the film alone (`beling1810/transcriptions/`). Agreement number
by number:
- No. 21: 33 of 33, counting its alternative readings; not independent: the second reader had seen the first
  sequence in its task text (it says so), and three of its first-choice numbers differ (1259, 1398, 237).
- No. 24: 330 of 461 (0.716).
- No. 29: 878 of 1,169 (0.751).

Most of the differences are 0/6/8, 3/8 and 5/0. Scored on its blind second transcription after the registered run
(post hoc, not part of the pass mark), No. 24 goes from 0.708 to **0.814** agreement and from 164 to 223 of 363 read
words (`heldout_no24_second.txt`). So much of the shortfall is our reading of the film, not the table. Nos. 23 and 25
have one transcription, and Nos. 27 and 28 one made after the witness had been read. No. 28-A is largely washed out.

**No. 29, with the key sheet alone** (`no29_decode.txt`, both transcriptions decoded with
`../morris1813/beling/key/codebook_M97_13_transcription.csv`, unchanged). A model wrote it as sentences from the decode
alone (`no29_reading.md`): 772 coded words, 77 holes (22 inferred, 46 with supplied letters, 9 unread), 695 built from
group values, 0.900. About ten of the group values used come from the rebuilt table where the sheet gives none or another.

It says that French pressure since February 1810 had worked to shut American ships out of Russian ports, or at least to
ban colonial goods. A ban on refined sugar, proposed in April and backed by a French-written memorial, was debated in
the Council and rejected. The Emperor declared his resolution not to exclude American vessels.

This is a model reading, not checked by a person and with no witness: decoded and read in part, not counted in any
share here.

**Two single values met in passing** (alignment output, not checked on the film):
- 570, which the table has as *tol* (H, 11x) and which No. 88 writes where *was* is wanted, aligns with *was* in No. 25-A
  ("but [570] ultimately rejected", frame 167R). It aligns with *tol(d)* in No. 23-D.
- 1185, *wick* on the sheet, spells Sles*wick* in No. 25-D; that confirms the sheet's value, which does not fit No. 88.

Neither changes anything here. The 570 in No. 25 should be looked at on frame 167R (done in the second round below: four new readings give 500 or 510, none 570; 570 not excluded).

### Second round: doubly read groups only (22 Nov 2026, after the miss)

The first test above **missed** and stays as registered. Its own finding was that single transcriptions agree with a
blind second reading at only 0.72-0.75. So a second round was run, labelled as such, scoring only what two blind
readers agree the film says. Its plan and pass mark are in `beling1810/round2/PLAN2.md`, hashed at 23:15 EST before
any second-round score (`PLAN2.sha256`). The pass mark is unchanged: 0.80, and the best of 100 shuffled tables + 0.30.
It was stated in advance that No. 24's post hoc 0.814 is not counted.

**Readings.** Fresh blind transcriptions were made by helper agents (Claude Opus 5.5), from the M35 reel 2 frames only:
no plaintext, no table, no earlier reading, no candidates, and washed-out groups marked rather than guessed
(`beling1810/transcriptions_round2/`; each header gives reader, time and images).
- Nos. 23, 25, 27 and 28 have two each (readers X and Y).
- Nos. 24 and 29 have one more (reader Z). With the blind second readings of round 1, each has two.

A group is scored only where the two readings give the same number; every other group is a hole that is not scored.

**How far the two blind readings agree** (`round2/reader_agreement.txt`):
- No. 23: 920 of 1,020 (0.902).
- No. 24: 438 of 461 (0.950).
- No. 25: 1,200 of 1,270 (0.945).
- No. 27: 218 of 284 (0.768).
- No. 28: 37 of 144 (0.257); passage A on frame 182 is washed out (20 of 117).
- No. 29: 1,083 of 1,168 (0.927).
- No. 21: 33 of 33 as before, but not two independent readings (see round 1); its 32 valued groups are kept in the
  pooled figure as registered and left out in the figure below.

**Result: PASS** (`round2/heldout_round2.txt`, run once). There are 2,718 agreed groups with a value in the table.
Agreement with the witness is **0.853**; the best shuffled table reaches 0.128 (median 0.075). By despatch:
- No. 23: 0.865.
- No. 24: 0.849.
- No. 25: 0.874.
- No. 27: 0.719.
- No. 28: 0.788.
- No. 21: 0.719.

Strict read words, counting every unagreed group as a hole: 1,386 of 2,317 (0.598), against 0.509 in round 1.

Without No. 21, whose two readings are not independent: 2,686 valued groups, agreement 0.854, strict words 1,372 of
2,296 (0.598). The pass does not depend on it.

After the fact, and not part of the registered test, the independent reviewer of 23 Nov 2026 scored each fresh blind
reading alone, without the agreement filter (No. 21 left out). Reading 1 gives 0.816 and reading 2 gives 0.814 with
`heldout_1810.py`; with the reviewer's own scorer they give 0.811 and 0.810. So the fresh readings alone are about
0.81. The filter adds about 0.04, and the round-1 transcriptions were the main problem.

Order of the second round. The last blind reading came back at 23:13 EST. `PLAN2.md` was hashed at 23:15:10, two minutes
later, and the run began at 23:16. The passage mapping in `PLAN2.md` uses the readers' own run labels, so their files
had been opened (for labels, not scores) before the hash. The order rests on local file times only; both commits carry
one git time. `round2/no29_recount.txt` counts 1,169 group positions for No. 29, where `reader_agreement.txt` counts
1,168 (the recount reads the hole tokens of `no29_agreed.txt`); the agreed count, 1,083, is the same in both.

What it means and what it does not:
- The table, rebuilt from 1811-12 alone, gives the witness's letters for about 85% of the 1810 groups that two readers
  read alike. The round-1 shortfall was mostly our transcription.
- The second round was decided on after seeing the first. The readers are all the same model, so their shared
  misreadings pass the agreement filter. The filter keeps the clearer groups.
- The table itself is not changed, and nothing here counts towards the No. 88 figures.

**No. 29 on agreed groups only** (`round2/no29_agreed.txt`, `round2/no29_recount.py`). Of the 781 words of the model
reading (manuscript clear words left out), 582 (0.745) rest wholly on agreed groups whose sheet value the alignment
confirms. The other 199 are holes: 77 were already marked in the reading, and the rest touch a group the readers do not
agree on or a value the sheet does not give. This is stricter than the reading's own count (0.900). It is still a
model reading with no witness, not checked by a person.

**Frame 167R, the 570 of No. 25-A** (`round2/frame167R/NOTE_570.md`, with crops). Neither blind transcriber reads 570:
both have 500. The two crop readers give 500 and 510; one names 570 as its main alternative, since the thin dash above
the middle stroke could be a 7's top bar, though both judge a 7 less likely. The 570 of our first transcription was most
likely our misreading, but the frame does not exclude 570. It gives no clear second example of 570 for *was*, and the
open 570 in No. 88 is unaffected.

## Transcription doubts

For No. 85 (the three files of 21 Nov 2026). The doubts of No. 88 are in the sections on the image checks above.

- 548 (no85_two_lines l.2, last group) - read: 548; checked: image, decode, transcription; one blind reader 528 (ei), one 548; the third reader's second look and an enlargement show the open-topped 4; ext-end
- 1369 (no85_two_lines l.2) - read: 1369; checked: image, decode, transcription; two readers gave 1269 as an alternative (a punctuation sign on the sheet), the third read 1369 without doubt; exp-ect-tation
- 668 (no85_three_lines l.1) - read: 668; checked: image, decode, transcription; at the gutter; one reader gave 608 (mai) as an alternative
- 398 (no85_three_lines l.2) - read: 398; checked: image, decode, transcription; one reader 298 (ext), one 298 or 398, the third 398; the 9 and 8 are fainter; Sw-ed-ish
- 116x (no85_three_lines l.2) - read: not read; checked: image, decode, transcription; last figure blotted (1164 or 1168 to three readers, neither with sense); counted as a hole
- 1436 (no85_three_lines l.3, second time) - read: 1436; checked: image, decode, transcription; clearly written, the sheet's "is" where in-dem-ni-fied wants 1426; one-digit rule
- 1626 (no85_three_lines l.3) - read: 1626; checked: image, decode, transcription; clearly written to three readers; no such number; a hole
- 9x (no85_three_lines l.3, last group) - read: not read; checked: image, decode; cut by the gutter after a 9 and the start of an 8 or 4; the decode has no value for it; a hole
- 891 (no85_three_lines l.4) - read: 891; checked: image, decode, transcription; middle figure blotted (alternatives 89, 841 without sense); lose, for the noun
- 1184, 809, 471, 195, 897, 1507, 1576, 1523 (no85_foot) - read: as given; checked: image, decode, transcription; in each, one of the two blind readers gave an alternative; the other reader, the transcription of 22 Sept 2026 and an enlargement agree with the reading given
- 352 (no85_foot l.5) - read: 352; checked: decode, transcription; alternatives 252 and 362 given by one reader each; the September transcription has 352; not looked at again on an enlargement
- 565 (no85_foot l.4) - read: 565; checked: image, decode, transcription; one reader 585 (lay), one 585 or 565; the September transcription 565; on an enlargement the middle figure is the 6 of 569 in the line above
- 1236, 209, 49, 1501, 820 (no85_foot l.2-3) - read: as written; checked: image (1501, 820), decode, transcription; the same in all three transcriptions; the sheet values give no sense (see the reading)
- 23x, 89x (no85_foot l.1, l.2, last groups) - read: not read; checked: image, decode; cut by the gutter; the decode has no value for them; holes

## Remaining gaps

- rem88 seven groups with lost digits (142x, 21x, 15xx, 11xx, 10xx, 55x, 13xx) - blocker: needs-physical-access; cut by the binding gutter on the microfilm of frame 0207 (every line end); the original and duplicate of No. 88 are not on reel 3, and JQA's letterbook copy (MHS) is not online. Context fixes most of them (in-, pre-, sa-id, tem-p-t) but they are counted unread
- gap88 l.1 1585 (Alexander): third digit overwritten on the film, and the word lacks ex unless the stroke cut by the gutter after it is 289 - blocker: needs-physical-access (14 Nov 2026)
- gap88 l.2 a group cut by the gutter after 908 (Chancellor's ... and advice), not in gap88.txt - blocker: needs-physical-access; frame 0206, left leaf, line end (14 Nov 2026)
- rem88 l.6 669 for 569 to: a one-digit slip on the image, but a whole word, so not covered by the one-digit rule - blocker: needs-physical-access; only the original or the duplicate could show 569 (14 Nov 2026)
- rem88 l.5 1508 before [pre]-liminary - blocker: no-key-material; the M97 sheet gives acious / account, which does not fit 'as a pre-' (14 Nov 2026)
- rem88 l.9 1185 ('He [took?] it as a demonstration') - blocker: no-key-material; the M97 sheet gives wick (14 Nov 2026); the image shows 1185 and a stroke cut by the gutter
- rem88 l.11 570 ('it tol he said'): the M97 sheet gives tol / toe, which does not read; the image shows 570, not 500 (was) - blocker: no-key-material
- no85_three_lines l.2 116x (ex-..-ed: pound 1160 or plain 1138) - blocker: illegible; last figure blotted on frame 0197 (21 Nov 2026)
- no85_three_lines l.3 1626 (indemnified ... Norway): no such number; in (1426) is one digit away but a whole word - blocker: needs-physical-access; only the original or the letterbook copy could show what was meant (21 Nov 2026)
- no85_three_lines l.3 9x (Norway ... the loss): cut by the gutter; for (981) fits - blocker: needs-physical-access (21 Nov 2026)
- no85_foot l.1 23x (exten-), l.2 89x (the lo..), cut by the gutter - blocker: needs-physical-access (21 Nov 2026)
- no85_foot l.3 49 (United States on the sheet, Sweden 39 wanted) and 1501 (A on the sheet, 'be' wanted) - blocker: needs-physical-access; the numbers are clear on the duplicate (21 Nov 2026)

## Escalation

- [x] siblings: clerk interlinear decodes on 0047, 0048, 0182-0185, 0189, 0190, 0194R, 0198R, 0206, 0210-0211, 0247 (`clerk_*.tsv`); 0056-57 are a clear decyphered copy, 0228-0233 No. 95 code only
- [x] clear-pages: Ford vol. 4 decipherments aligned for 39 coded 1811 blocks and 8 despatches of Oct 1811-Sept 1812, No. 95 against the Department's clear copy on 0230-0232 (`ford_pairs*.tsv`, `ford1812_pairs*.tsv`)
- [x] known-keys: Armstrong's THE=972 table tested and ruled out (18 Sept); Pinkney's London code not found in print or online
- [x] print: Ford 4:357-358 prints both passages as not decyphered; no other printed reading found; JQA's diary (Primary Source Cooperative) confirms the two strokes at Wilna
- [x] key-rebuild: table rebuilt to 1,166 numbers (`consolidate.py` + `overrides.tsv`, every override with its reason); alphabetical-slot bracketing (`slots.py`, `slot_inferences.tsv`, grade I)
- [x] retry (14 Nov 2026): the seven one-digit groups looked at on frames 0206 and 0207 enlarged; five read under the one-digit rule, 669 and 1585 stay holes
- [x] siblings (21 Nov 2026): No. 85's two bare passages on 0197 and the six bare lines of 0196 left read with the code sheet after a pre-registered check against the clerk's decipherment of Nos. 85 and 74 (0.911-0.935, controls at most 0.131); the three 'error' groups of No. 74 read as they stand
- [x] retry: No. 88 re-read against the image a third time: 792 (not 492), 1061 (not 1081), 588 (not 888), 1384 (not 1385) corrected; 570 confirmed; 1097 and 1383 read as JQA's own overwritten digits

## Next

- The original or duplicate of No. 88 (not on M35 reel 3) or JQA's letterbook copy at the MHS would restore the seven
  gutter-cut groups of frame 0207 and the one of frame 0206; with them the remainder would pass 95%.
- 1508, 1185 and 570 have sheet values that do not read (14 Nov 2026): a further occurrence would not help, only the
  original, the duplicate or the letterbook copy could show the misread digit or slip. Still unaligned: the 1812
  blocks of Nos. 77, 78, 81 and the remaining lines of No. 85
  (0196L 12-23) are not yet aligned.
- 21 Nov 2026: the remaining lines of No. 85 and its two bare passages on 0197 are now transcribed and read (section above).
  JQA's letterbook copy of No. 85 and No. 74 (Adams Papers reel 136, MHS) would settle the holes and show whether 49, 1501
  and 1626 are the duplicate's slips.
