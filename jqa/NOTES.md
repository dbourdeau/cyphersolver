# JQA at St Petersburg: the despatches are NOT in the Armstrong code; his own code rebuilt, and Ford's
# "not decyphered" passage of No. 88 (25 June 1812) read

Outcome: read in part (22 Sept 2026). No. 88, measured with `measure.py`: 355 of 390 code groups read as sense
(0.910); the nine lines Ford left out 127/133 (0.955), the remainder 228/257 (0.887). 379/390 groups have a value.

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

**Sources of the table** (all merged by `consolidate.py` into `code_table.tsv`, 962 numbers: 391 H, 241 C, 311 M,
19 I; disagreements in `code_conflicts.txt`, hand decisions in `overrides.tsv`):

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
(133 groups). `python render.py gap88.txt` gives every group a value; 127 read as sense. Reading ([ ] = grade I,
{ } = valued but not sense):

> ... and expectation. But the [journ-ey] itself of the Emperor Alexander to Wilna was in [opposition] to the
> Chan-ce-{last}-or and adv-ice, and if his active influence had not been {im-pas-sion-ed} before it, it can scarcely
> fail to have been affected {use} his illness immediately after his arrival [thither], which was undoubtedly an
> apo-ple-ct-ic stroke. Since then he has had a second and a more severe one. In the German Gazettes even his
> death has been announced; but that was a mistake. At all events it is scarcely possible that he should remain much
> longer in the department of foreign affairs.

"He" is Count Rumyantsev (Romanzoff), Chancellor and foreign minister, who had gone to Wilna with Alexander. The
passage reports that the journey to Wilna went against the Chancellor's advice (the key word, 83 'opposition', is
grade I), his apoplectic stroke soon after
arriving, a second and worse one since, a false report of his death in the German papers, and JQA's judgment that he
cannot long stay at the foreign ministry. That fits the known history (a stroke in 1812 that cost him his hearing;
retired 1814). It differs on timing from standard accounts (Britannica, Wikipedia), which tie the stroke to the news
of the Niemen crossing on 24 June: JQA, writing on 25 June before that news could reach St Petersburg, places the
first stroke soon after Rumyantsev reached Wilna and a second before 25 June. Ford printed none of this.

Changes from the 18 Sept reading: syllables then inferred are now attested: *itself* (1081 self, clerk 0185L1),
*apoplectic* (1141 ple C, 1060 ct H clerk 0182, 1404 ic), *stroke* (1586 oke C), *second* (1077 C), *severe*
(1091 sever), *remain much longer* (743 rem C, 162 much H, 888 long H), *mistake* (134 mis H clerk 0182),
*announced* (479 un H), *after* (1520 H), *At all events* (283 event H clerk 0048), *advice* (1575 adv, Ford 0132,
M; 1405 ice, Ford 0036, C), *foreign affairs* (68 C, 1517 H).

## 4. The "remainder of letter ... undecyphered" (Ford 4:358)

Frame **0207** (left leaf): 13 lines of code, then clear sentences (Manifestos of both parties expected; Peace with
Turkey signed a third time; "It is not General Kutuzoff but Count Rostopchin who is appointed Governor, civil and
Military, of Moscow"), then 5 more lines. Groups: `rem88.txt` (257 groups, 7 with digits lost in the gutter).
246 valued, 228 read as sense:

> If this proposition has in any form been disclosed to the Russian government, it was certainly neither unreasonable
> nor im[mod(erate)] nor inconsistent with a system rigorously and {…} [de-fen-sive] (underlined), to meet it with a
> proposition for the e-va-{?}-ation of Prussia by the French troops as {…} preliminary to negotiation. But the very
> point upon which the ambassador manifested the most sensibility in speaking of Prince Kurakin's last note was that
> it held out a proposition with which it would be dishonourable in France to [comply]. He {…} it as a demonstration
> that the Emperor Alexander had determined not to ne-{at} — {al} — it {tol} he {1xxx}-id such a proposal as
> France had never thought of making was Russia even after the {…} of {…}.
> [clear text] … an army of reserve is forming there, and it is [55x] {…} the {…} great success on the, on the side of the French should mark the commencement of the war, the Emperor Napoleon will attempt to
> [pene-t-rate] directly to that centre of the em-{…} the {…} the side{s} of the Baltic.

The ambassador is Lauriston, the French ambassador; Kurakin's note is the Russian ambassador's demand at Paris for the
evacuation of Prussia (April 1812), which Napoleon treated as a declaration of war.

## Remaining gaps

- gap88 l.3-4 im-pas-ion-ed (1424 1112 1433 520): valued, but 'impassioned' does not fit 'if his active influence had not been … before it' - blocker: open-codes; 1112 = pas is clerk-attested (0184L22, 0185L1), so either JQA encoded another word or the group is misread; the catchword 1102 (pa) at the page foot suggests im-pa-...
- gap88 l.5 492 'use' where 'by' is wanted - blocker: open-codes; 492 = use/se is attested four times (clerk 0182, 0184; Ford 0066, 0126), so this is probably JQA's slip for 792 (by)
- gap88 l.2 1457 'last' in Chan-ce-?-or - blocker: illegible; the group may be 1452 with the doubling mark (ll)
- gap88 grade-I words (1434 journ, 168 ey, 83 opposition, 1398 thither) - blocker: open-codes; no clerk decode or Ford passage contains these groups in the frames read
- rem88 l.4 the word before 'defensive' (350 289 1403 897: few-ex-table-ly) - blocker: open-codes; 350 few and 1403 table are Ford values that give no sense here ('exclusively'?)
- rem88 l.5 e-va-{1081}-ation and {1508} before 'preliminary' - blocker: illegible; 1081 is clearly self elsewhere, the digit here is blurred (10?1); 1508 bable (Ford M) where 'a pre-' is wanted
- rem88 l.9 1185, l.11 699/1535/570, l.13 1309 888 996 520 1453 416 ('after the … of …', perhaps Poland), l.16 220 586 1416, l.19 927 1540 748 - blocker: open-codes; not in any decoded frame read so far, and the slot gives no usable bracket (`python slots.py`)
- rem88 seven groups with lost digits (142x, 21x, 15xx, 11xx, 1xxx, 55x, 13xx) - blocker: illegible; cut by the microfilm gutter on frame 0207; the duplicate/original of No. 88 was not found on reel 3

## Escalation

- [x] siblings: the clerk's interlinear decodes on frames 0182, 0183R, 0184, 0185, 0190, 0194R, 0198R and 0048 read into `clerk_*.tsv` (22 Sept); more interlinear pages remain on reel 3 (0047, 0056-57, 0211, 0228-0229, 0233, 0247) and reel 2
- [x] clear-pages: the Department's decyphered copies are printed in Ford vol. 4; 39 coded 1811 blocks aligned with Ford (`codes_ford*.txt`, `ford_pairs*.tsv`); decyphered sheets on the film (0011, 0037, 0064, 0067, 0072, 0082, 0092, 0144, 0156, 0166, 0170, 0230) are in the Department's order, not line by line
- [x] known-keys: Armstrong's THE=972 table tested and ruled out (18 Sept); Pinkney's London code not found in print or online
- [x] print: Ford 4:357-358 prints both passages as not decyphered; no other printed reading found
- [x] key-rebuild: table rebuilt from ~2,200 clerk and ~860 Ford-aligned pairs (962 numbers), `consolidate.py` + `overrides.tsv`; alphabetical-slot bracketing done (`slots.py`, `slot_inferences.tsv`, grade I)
- [x] retry: No. 88 groups re-read from zoomed crops of 0206 and 0207 (three digits corrected, one catchword removed)

## Next

- Read the remaining interlinear pages (0047, 0056-57, 0211, 0228-0229, 0233, 0247) and align the 1812 coded blocks
  whose decipherments Ford prints (vol. 4 after p. 300) the same way; the open No. 88 groups (1185, 1309, 996, 927,
  350/1403, 1508, 1112 in context) need one more occurrence each.
- Ford's other gaps: No. 51 (26 May 1811, "[One line and a half of cypher not decyphered]", frame 0085 block 2,
  transcribed in `codes_ford_A.txt`: "I [195] and [760] these [221 …] will be known to the [73] before the final
  dis-so-[894]-tion of the al(l) negotiation with Eng[land]") and No. 55 (22 June 1811, "[one-half line of cipher not
  deciphered]").
- Reel 2 frame 0155 (1810): a long coded passage with no decode on the NARA copy; compare with Ford vol. 3.
