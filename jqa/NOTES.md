# JQA at St Petersburg: the despatches are NOT in the Armstrong code; his own code rebuilt, and Ford's
# "not decyphered" passage of No. 88 (25 June 1812) read

Status: read (22 Sept 2026, third pass). No. 88, measured with `measure.py`: **375 of 390 code groups read as sense
(0.962)**; the nine lines Ford left out 129/133 (0.970), the remainder 246/257 (0.957). 382/390 groups have a value;
355/390 (0.910) without the grade-I values. Still open: 7 groups cut by the microfilm gutter (needs the original),
4 groups where JQA's own encoding does not fit the sense (im-pas-sion-ed for 'impaired'), and 4 single code groups.
The second pass (earlier on 22 Sept) stood at 0.910; see section 5.

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
checkout's `jqa/`; images `img03/`, git-ignored, not in the repo). `strip.py` and `crop.py` cut crops for reading.

**Structure.** A numbered syllabary: syllables, word-parts and common words, about 1,600 numbers; 1-100 mostly whole
words (13 observation, 16 Emperor, 29 United States, 37 together, 44 negotiation, 71 commerce, 78 President). Values
climb alphabetically only inside short runs (1384 that, 1385 the, 1388 then, 1391 there, 1392 these, 1393 they,
1394 think, 1399 this; 1592 on, 1594 one, 1595 ong, 1597 only), then the run breaks, so the alphabetical slot brackets
a value only where the neighbours are in order (`slots.py`). A superscript o after a group adds -s; a mark under a
group changes it (doubled letter, -ed, or a different word: 1107 paper, 1107+ well). A few groups carry two values in
the sources (508 rect and ear; 1570 of and occurr; 1173 when and would).

**Sources of the table** (all merged by `consolidate.py` into `code_table.tsv`, 1,070 numbers after the third pass: 431 H, 312 C, 307 M,
20 I; disagreements in `code_conflicts.txt`, hand decisions in `overrides.tsv`):

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
> Chan-ce-ll-or and adv-ice, and if his active influence had not been {im-pas-sion-ed} before it, it can scarcely
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

{im-pas-sion-ed}: 1424 1112 1433 520 are clear on the image and each value is attested (im, pas, ion, ed); the sense
wants *impaired*. Probably JQA's own encoding slip; counted as not read.

## 4. The "remainder of letter ... undecyphered" (Ford 4:358)

Frame **0207** (left leaf): 13 lines of code, then clear sentences (Manifestos of both parties expected; Peace with
Turkey signed a third time; "It is not General Kutuzoff but Count Rostopchin who is appointed Governor, civil and
Military, of Moscow"), then 5 more lines. Groups: `rem88.txt` (257 groups, 7 with digits lost in the gutter).
249 valued, 246 read as sense:

> If this proposition has in any form been disclosed to the Russian government, it was certainly neither unreasonable
> nor im-[mod(erate)] nor inconsistent with a system rigorously and [in]-[fl]-ex-[ib]-ly de-fen-sive (underlined), to
> meet it with a proposition for the e-va-cu-ation of Prussia by the French troops as {1508} [pre]-liminary to
> negotiation. But the very point upon which the ambassador manifested the most sensibility in speaking of Prince
> Kurakin's last note was that it held out a proposition with which it would be dishonourable in France to comply. He
> {1185} it as a demonstration that the Emperor Alexander had determined not to [negotiate] at all - it {tol} he
> [sa]-id - such a proposal as France had never thought of making to Russia even after the [bat]-tle of Fri-ed-la-nd.
> [clear text] ... an army of reserve is forming there, and it is [...] probab-le that if great success on the, on the
> side of the French should mark the commencement of the war, the Emperor Napoleon will at-[tem]-p-t to pene-t-rate
> directly to that centre of the em-[pire] the [along] the side-{res} of the Baltic.

The ambassador is Lauriston, the French ambassador; Kurakin's note is the Russian ambassador's demand at Paris for the
evacuation of Prussia (April 1812), which Napoleon treated as a declaration of war. "Even after the battle of
Friedland" (June 1807, before Tilsit): France had never proposed evacuating Prussia even when Russia was beaten.

## 5. Third pass (22 Sept 2026): 0.910 -> 0.962

New sources: the clerk's interlinear decodes on 0047, 0048 (rest), 0210-0211 and 0247 (`clerk_0047.tsv`,
`clerk_0048b.tsv`, `clerk_0210_0211.tsv`, `clerk_0247.tsv`, 560 pairs; `clerk_notes_pages2.md`), and coded blocks of
eight 1811-1812 despatches aligned with Ford vol. 4 (`codes_ford1812*.txt`, `ford1812_pairs*.tsv`, 1,926 pairs;
No. 95 against the Department's clear copy on 0230-0232; `ford1812_notes.md`). `consolidate.py` now reads them; the
table has 1,070 numbers.

What moved, with evidence:

| No. 88 | was | now | evidence |
|---|---|---|---|
| gap88 l.2 `1025 1016 1457 908` | Chan-ce-{last}-or | Chan-ce-ll-or (C) | No. 73 (0165, Ford 4:256) writes the same four groups, 1457 with the doubling mark = ll |
| gap88 l.5 first group | 492 use | **792** by (H) | re-read on 0206R: an open hook, not this hand's looped 4 |
| rem88 l.4 `142x 350 289 1403 897` | few-ex-table-ly | [in]-[fl]-ex-[ib]-ly, *inflexibly* (I) | slots 1401 I < 1403 < 1404 ic and 347 fit < 350 < 352; 350 has a hook under the 0; the single Ford alignments (few, fi, table, cal) disagree with each other, and the 0194 "1403" (cal-cu-late) has a blotted 4, probably 1003 cal |
| rem88 l.5 | e-va-{1081}-ation | **1061** cu (C): e-va-cu-ation | the blurred digit is a 6 (as in 864, 1576); 1061 cu in Ford 0005 and cal-cu-late (0194); slot 1060 ct < 1061 < 1062 cur |
| rem88 l.11 `426 699 1535+` | ne-{at}-{al} | [negotiate] at all | 1535 with the doubling mark = all; 426 slot 423 need < 426 < 428 nei (I) |
| rem88 l.13 `1309 888 1576 996 520 1453 416` | {...} long of {...}-ed la-nd | [bat]-**588** tle(d) of Fri-ed-la-nd | 996 = fri (C, No. 95 fri-end-ship x2, a fri-end x2); 1453 la, 416 nd (Fin-la-nd); the second group is 588 (the 5 has its top bar), 588 = tled (set-tled, C); 1309 slot 1308 bas < 1309 < 1310 be (I) |
| rem88 l.16 `220 586 1384 1416` | {proper le the if} | probab-le that if | 220 = probab (clerk 0047R19 'it is probab-le that', 0190L6, 0190R26; the lone 0184R11 'proper' is the outlier); the third group is 1384 (4 over 5) |
| rem88 l.18-19 `539 927 ... 1540` | em-{927} the {ambass} | em-[pire] the [along] | 927 context only (I); 1540 slot 1537 alliance < 1538 ally < 1540 (I) |

## Remaining gaps

- rem88 seven groups with lost digits (142x, 21x, 15xx, 11xx, 10xx, 55x, 13xx) - blocker: needs-physical-access; cut by the binding gutter on the microfilm of frame 0207 (every line end); the original and duplicate of No. 88 are not on reel 3, and JQA's letterbook copy (MHS) is not online. Context fixes most of them (in-, pre-, sa-id, tem-p-t) but they are counted unread
- gap88 l.3-4 im-pas-sion-ed (1424 1112 1433 520) - blocker: open-codes; the four groups are clear and attested, the sense wants 'impaired': JQA's own encoding, not a gap in the table
- rem88 l.5 1508 before [pre]-liminary - blocker: open-codes; 1508 (le/bable, M) does not fit 'as a pre-'; no other occurrence in the decoded pairs
- rem88 l.9 1185 ('He [took?] it as a demonstration') - blocker: open-codes; no occurrence in any decoded frame or Ford block read
- rem88 l.11 570 ('it tol he said'): valued (tol, C) but does not read; the image shows 570, not 500 (was) - blocker: open-codes
- rem88 l.19 748 after 1099 side ('the side-res of the Baltic') - blocker: open-codes; 748 re/res (M); the group before is 1099 (two looped 9s), not 1097 sho

## Escalation

- [x] siblings: clerk interlinear decodes on 0047, 0048, 0182-0185, 0189, 0190, 0194R, 0198R, 0206, 0210-0211, 0247 (`clerk_*.tsv`); 0056-57 are a clear decyphered copy, 0228-0233 No. 95 code only
- [x] clear-pages: Ford vol. 4 decipherments aligned for 39 coded 1811 blocks and 8 despatches of Oct 1811-Sept 1812, No. 95 against the Department's clear copy on 0230-0232 (`ford_pairs*.tsv`, `ford1812_pairs*.tsv`)
- [x] known-keys: Armstrong's THE=972 table tested and ruled out (18 Sept); Pinkney's London code not found in print or online
- [x] print: Ford 4:357-358 prints both passages as not decyphered; no other printed reading found; JQA's diary (Primary Source Cooperative) confirms the two strokes at Wilna
- [x] key-rebuild: table rebuilt to 1,070 numbers (`consolidate.py` + `overrides.tsv`, every override with its reason); alphabetical-slot bracketing (`slots.py`, `slot_inferences.tsv`, grade I)
- [x] retry: No. 88 re-read against the image a third time: 792 (not 492), 1061 (not 1081), 588 (not 888), 1384 (not 1385) corrected; 570 and 1099 confirmed

## Next

- The original or duplicate of No. 88 (not on M35 reel 3) or JQA's letterbook copy at the MHS would restore the seven
  gutter-cut groups; with them the letter would be at about 98%.
- 1185, 1508, 748 each need one more occurrence: the 1812 blocks of Nos. 77, 78, 81 and the remaining lines of No. 85
  (0196L 12-23) are not yet aligned.
