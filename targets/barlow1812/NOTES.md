# barlow1812: Joel Barlow to Monroe, 25 September 1812, and to the Duke of Bassano, 25 October 1812: two passages in the Paris legation code read in part with a rebuilt key

Contributed by Andrew Beling, with AI agents. Every reading and check is by AI agents; no person has read the
numbers against the images (see "Remaining gaps").

Two letters of the American minister in Paris carry short passages in the legation's numerical code (the = 1700)
and no decipherment: his despatch to the Secretary of State of 25 September 1812 and the copy of his note of
25 October 1812 to the French foreign minister. No key sheet for this code is known. We rebuilt 623 numbers of it
(and met 21 more inside words we could not divide) from ten other letters in the same code that were deciphered
at the time, and read the two passages with that table: 59 of 64 numbers in the first, 42 of 46 and 44 of 47 in
the two copies of the second. Seven words are completed from the sense and marked, an eighth is marked doubtful
because its number is miswritten, and one number is left unread.

## 1. Documents

| id | Letter | Frames (NARA M34 roll 16) | Code | Decipherment on film |
|---|---|---|---|---|
| 1812-09-25 | Joel Barlow to James Monroe, Paris, 25 Sep 1812 | 0232 right page, 0233 | 64 numbers, one paragraph | none |
| 1812-10-25 | Joel Barlow to the Duke of Bassano, Paris, 25 Oct 1812, copy A | 0240 left (lower half) and right, 0241 | 46 numbers, two sentences | none |
| | the same, copy B | 0246 left (lower half) and right, 0247 left | 47 numbers | none |

Both copies of the note to Bassano were enclosed to Monroe; they stand in the volume beside copies of Bassano's
French letter of 11 October 1812 from Wilna, which the note answers. Parts of the note are in code in both copies;
we take it (an inference) that this was done for the copies sent home and that the note Bassano received was in
clear.

## 2. Sources and images

- NARA RG 59, Despatches from US Ministers to France, vol. 13, microfilm M34 roll 16. Frames are at
  `https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-016/M34-016-NNNN.jpg`, for example
  [0232](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-016/M34-016-0232.jpg),
  [0240](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-016/M34-016-0240.jpg),
  [0246](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-016/M34-016-0246.jpg).
- The ten letters the key rests on are listed in `key.md` with their repositories. Four are outside M34: three at
  the Library of Congress (free images on loc.gov) and one known from a sale photograph of its last page.
- No images are in this folder.

## 3. The system and the key

A code of words and syllables written as numbers from 7 to 1700, among clear words. Common words have their own
number (the 1700, of 631, and 513, to 494, in 1114); other words are spelt from syllables (in/dem/ni/ti/es,
re/fu/sal, ma/i/est/y). I and J are one letter, U and V one letter. Several syllables have more than one number.
In the September letter a comma joins the numbers of one word and a dash separates words.

`key.tsv` has 644 numbers: 623 with a value and a grade that says how the value is known (`key.md`), and 21 seen
only inside a word we could not divide. `key_evidence.tsv` lists every occurrence behind them (2,323 lines). The values are those of decipherers of 1811-1813 and nothing
else. Where one of the two passages uses a number that has no such value, our suggestion is in `proposals.tsv`
(eight of the nine such numbers) and is marked `?` in the decryption and `[?word]` in the reading.

How the table grew:

1. **M34 roll 16 (19 Oct 2026).** All 296 frames of the roll (2 to 297) surveyed. Barlow's despatch of 29 September 1811 (frame 11, 503
   numbers, no decipherment on the page) has a separate decipherment in a State Department hand four frames on
   (15-16); the two were aligned word for word. Five later despatches have a clerk's decipherment between the
   lines. Together: 436 numbers. Applied to the three undeciphered passages they read 78% of the numbers.
2. **Four letters to and from Barlow outside M34 (20 Oct 2026):** Monroe to Barlow, 23 April and 16 June 1812;
   Madison to Barlow, 11 August 1812; Barlow to Madison, 26 September 1812, each deciphered between the lines at
   the time. 655 numbers.
3. **Blind check (21 Nov 2026).** Every source re-read by two AI readers who saw only the images; section 7.
   644 numbers in `key.tsv` (recounted 24 Nov 2026), of which 623 have a value from a decipherer and 21 are seen only
   inside a word. This line read 649 numbers, "the other five" occurring only in the passages read here; nothing in
   the folder gives 649, and the open numbers of the passages are nine, none of them in `key.tsv`.

## 4. Transcription

- `transcription_1812-09-25.txt`: the whole letter, 44 manuscript lines. `transcription_1812-10-25_A.txt`: the
  whole note in copy A, 60 lines. `transcription_1812-10-25_B.txt`: the seven lines of copy B that carry code;
  `collation_copyB.md` lists every difference between the copies. A star after a line label marks a line with
  code numbers.
- The code numbers were read four times by AI readers: in October 2026, by two blind readers on 21 November 2026,
  and by the transcriber of the full text the same day. All four agree on 56 of the 64 numbers of the September
  letter. Each transcription header lists the numbers on which a reading differs, with what the frame shows.
- Three places need saying here. In the September letter the copyist wrote 1553 where the word needs 1353
  (exp/ect/ed), a 1700 that looks like 1780, and an 831 whose 3 has a closed top. The same closed 3 stands in
  631 and 933 in his copy of the Wilna letter (frame 250), and frame 11 has another 1700 written like 1766. We
  give the numbers the words need and say so in the header.
- The clear text was read once. No person has checked any of it.

## 5. Decryption

`decryption_*.txt` give every coded line number by number, `number=value/grade`, straight from `key.tsv` with no
repair. `python decode.py` re-derives the three files from the transcriptions and compares (result: ok, 64 + 46 +
47 numbers).

| Letter | Numbers | With a value in the key | Without |
|---|---|---|---|
| 25 Sep 1812 | 64 | 59 | 815 (twice), 1567, 1404, 163 |
| Bassano, copy A | 46 | 42 | 624, 706, 103, 531 |
| Bassano, copy B | 47 | 44 | 624, 706, 537 |

## 6. Readings

`reading_1812-09-25.md` and `reading_1812-10-25.md` give each letter whole, as sentences, with the coded words in
italics. Read share, counted over the coded words only, a word being read when the key alone gives all of it:
25 of 34 (0.735) in the September letter and 22 of 26 (0.846) in the note, 47 of 60 together (0.783). The 13
holes are the eight words with a value supplied from the sense (`[?word]`), the word with an unread number
(`[163]th`) and the four words with a letter supplied inside them (`{+s}poliations`, `{+exp}ected`, `mod{+e}`,
`wel{+l}`). `profile.json` carries the same counts (`fraction_read`, and `cipher_words` and `holes` for each
text). The repository's sentence check (`docs/_check_reading.py`) is a different measure, the share of sentences
without a hole: 0.812 and 0.877. Both letters are marked "read in part".

### Notes on the coded words, 25 September 1812

- **indemnities, indemnity** (232R11, 23301): 1114 703 815 1156 and 1114 703 815. In, dem and es are in the key;
  815 is not. "nity" gives indemnity exactly and indemnity-es for the plural, which is how the decipherer of
  Monroe's letter of 16 June 1812 wrote it out (in/dem/ni/ty/es). The other letters spell the word 1114 703
  1169 133.
- **spoliations** (232R12): 761 1646 325 761, s/poli/ation/s. The first 761 is blotted and overwritten; only its last digit, 1, is clear. 1646 is "poli" in "police" (Barlow to Madison, 26 September 1812).
- **making progress** (232R13): 1511 1567 1115 and 574 1404 761. Ma, ing, pro and s are in the key; 1567 (added
  above the line) and 1404 are not. "k" and "gres" are our proposals.
- **the [163]th June** (232R16): 163 1699 1126. 1699 is "th" and 1126 is "June"; 163 has no value. In his private
  letter to Madison of the next day Barlow twice refers to the same note with the pair 939 1126, which Madison
  deciphered once as "11th June" and once as "fifth June". We leave the day unread.
- **expected** (232R14): the first number is written like 1553; 1353 659 950 is exp/ect/ed in Thomas Barlow's
  duplicate of 1813.
- **confidence** (232R17): 831 1387 410, as in Barlow's despatch of 29 September 1811; the 3 of 831 has a closed
  top and can be taken for a 9.
- **[?the] United States** (232R19): the number is written like 1780; "the" is 1700, and frame 11 has another
  1700 written like 1766. Because it is a whole word, nothing beside it can confirm the digit, and the reading
  marks it as a proposal.
- **mode** (23301): 1217 750; the 750 is blotted.

- **{+s}poliations, {+exp}ected, mod{+e}:** the three numbers that are blotted or miswritten on the film (761, 1353,
  750) and are read from the word they stand in; each is inside a word whose other numbers are read from the key.
  Each of the three words counts as a hole: the key is rebuilt, not a surviving key of the time, so the
  repository's rule for a one-digit slip does not apply.

### Notes on the coded words, 25 October 1812

- **little or nothing** (240R28-29): 624 23 408 1115. Or, noth and ing are in the key; 624 is not.
- **imperial treasury** (240R29-30): 1039 1627 1014 1132, im/per/ia/l; 1171 314 1470 152, tre/as/ur/y. Copy B has
  1171 314 152 (tre/as/y), without 1470.
- **determined** (24102): 706 1059 1427 950. Er, min and ed are in the key; 706 is not.
- **refusal of justice** (24103): copy A has 788 1357 861 then 1536 1471 103 410, re/fu/sal i/us/[103]/ce, with no
  "of"; copy B has 788 1357 861 631 1536 1650 284 1017, re/fu/sal of i/u/st/ice. Copy B spells "justice" entirely
  with known values (I and J are one letter in the code), so the word is read; in copy A 103 has no value and
  must stand for "ti".
- **Imperial Majesty** (24104): copy A 1039 1627 1132 (im/per/l, without 1014); copy B has the 1014. Majesty is
  1511 1536 1157 152, ma/i/est/y.
- **in regard** (24106): 1114 841 then 531 in copy A and 537 in copy B. Reg is in the key; neither 531 nor 537
  is. One of the two copies has miscopied the number; we cannot say which.
- **well** (24106): 896, written 89 with a raised 6 and a small sign beneath it in both copies; the key has "wel"
  from Thomas Barlow's letter of 1813. The second l is supplied (`wel{+l}`), so the word counts as a hole.
- In copy A the last two numbers of 24106 are unclear (the first written like 714, the second a 5 and a blot);
  copy B has 314 54, "as France".

### Our own review of the readings (21 November 2026)

An AI agent of ours (model `claude-opus-5-5`) that had made none of the readings reviewed both letters by the repository's rule. It first read
all 157 code numbers from the frames by their shape, before opening any file of this folder, and agreed with 153
(the four others: the blotted group of 232R12, the 1700 written like 1780, and two numbers already marked
doubtful in the Bassano copies). It read more than 50 lines of the clear text against the frames and found no
wrong word. It then read the decryptions as sentences and graded both documents **A** (coherent, scattered
holes). It asked for four changes, all made after its review: *[?the]* marked before "United States"; the "s"
of "spoliations" marked; "treasury" said to follow copy A; "commercial treaty" in the summary changed to "the
treaty". This is the contributor's own check by a model, not a person's reading and not the reviewer's: no
`reading_review` is recorded in `profile.json`, which is left to the repository's reviewer.

## 7. The blind check of the key's sources (21 November 2026)

The table had been built from one AI reading of each source. Before using it here, each source was read again by
two AI readers who were given only the images, in a folder holding nothing else, and told to open no other file.
The pass marks were written down first: each reader to agree with the first transcription on at least 95% of the
numbers, and at least 98% of the numbers to be matched by one reader or the other. Every number on which both
readers differed from the first transcription was then looked at again on the image.

The order of plan and readings rests on our own local records (session log and file times), which are not
public. The plan for Monroe to Barlow, 16 June 1812, was written at 01:37 Eastern on 21 Nov 2026, a minute after
its two readers were started and before either handed in (01:41 and 01:42) or the comparison was run (01:43).
The plan for the other thirteen rows was written at 02:15, before their readers were started.

| Source | Numbers | Reader A | Reader B | Either | Misread in the first transcription |
|---|---|---|---|---|---|
| Monroe to Barlow, 16 Jun 1812 | 501 | 98.2% | 98.2% | 98.2% | 4 |
| Madison to Barlow, 11 Aug 1812 | 435 | 96.1% | 95.9% | 96.1% (miss) | 16 |
| Barlow to Madison, 26 Sep 1812 | 932 | 96.4% | 96.1% | 96.4% (miss) | 32 |
| Barlow, 29 Sep 1811 (frame 11) | 501 | 99.0% | 98.6% | 99.6% | 2 |
| Despatch 19 (frame 242) | 97 | 99.0% | 97.9% | 100% | 0 |
| Despatch 20 (frame 244) | 22 | 90.9% (miss) | 95.5% | 95.5% (miss) | 0 |
| Wilna, 23 Nov 1812 (frames 249-250) | 91 | 95.6% | 96.7% | 96.7% (miss) | 0 |
| Thomas Barlow, 10 Feb 1813 (frame 291) | 101 | 89.1% (miss) | 86.1% (miss) | 91.1% (miss) | 0 |
| the same (frames 292-293) | 116 | 94.0% (miss) | 92.2% (miss) | 95.7% (miss) | 0 |
| Thomas Barlow duplicate (frame 295) | 205 | 97.6% | 98.0% | 99.0% | 1 |
| Monroe to Barlow, 23 Apr 1812 (sale photograph) | 142 | 99.3% | 99.3% | 99.3% | 1 |
| **This folder:** 25 Sep 1812 (frames 232-233) | 61 of 64 (the three groups above the line or blotted were bracketed in the first transcription and compared by hand) | 93.4% (miss) | 91.8% (miss) | 93.4% (miss) | 0 |
| Bassano, copy A | 46 | 95.7% | 95.7% | 95.7% (miss) | 0 |
| Bassano, copy B | 47 | 95.7% | 95.7% | 95.7% (miss) | 0 |

- The two Library of Congress letters missed because the first transcription was wrong, at about 3.5% of the
  numbers; the readers agreed with each other and with the image. All 56 misread numbers are corrected.
- Frames 291 and 293 are low-resolution film with writing showing through. Numbers there that the readers did
  not both confirm are graded L in the key and carry no value alone.
- Nine of the fourteen rows miss a mark. The short passages in the copyist's hand missed by one to four numbers each, at the places described in
  section 4.
- The check removed ten numbers that had existed only through a misreading and settled six conflicts.
- "Blind" and "independent" here mean AI readers who had not seen the first reading. No person has checked a
  number.
- What the check does not show: that the values are right. A value seen once (290 of the 623) rests on one
  decipherer's word. In the two readings these words lean on such a value: confidence (831), imperial (1014),
  justice in copy B (1017), spoliations (1646); the full stop after "opinion" is 177, known from the 1811
  alignment only.

## 8. Prior work

Print check of 21 November 2026 (by an AI agent; sources reached and not reached are listed below).

- **25 September 1812:** not found in print. American State Papers, Foreign Relations, vol. 3, does not print
  the letter; nor does Wait's *State Papers* (1819), Todd's *Life and Letters of Joel Barlow* (1886) or *The
  Papers of James Monroe*, vol. 6 (which prints Barlow's despatches of 20 October and 23 November 1812). Its
  substance overlaps with the private letter Barlow wrote to Madison the next day, printed with Madison's
  decipherment in *The Papers of James Madison*, Presidential Series 5:354-57. Buel, *Joel Barlow* (2011), cites
  the despatch without quoting it.
- **25 October 1812 to Bassano:** printed only as an extract that stops at "the convention of indemnities",
  before the coded sentences: American State Papers, Foreign Relations 3:604; Wait's *State Papers* 9:218-19;
  Todd pp. 270-71. Irving Brant, "Joel Barlow, Madison's Stubborn Minister", *William and Mary Quarterly* 15
  (1958), pp. 447-48, describes from the French archives the proposal behind the coded clause (reparation to be
  raised by French licences to eighty American merchant vessels, which is why its execution "would really cost
  little or nothing to the imperial treasury") and cites the note as received, Archives du ministère des
  Affaires étrangères, Correspondance politique, États-Unis, vol. 69 f. 350, without quoting it. That is the
  context, not the coded words.
- **The French read part of this code at the time.** Brant (p. 446 and n. 17) reports that Barlow's letter to
  Madison of 26 September 1812 was intercepted and deciphered at the French foreign ministry: a French
  translation with "a few undeciphered numerals" is in Correspondance politique, États-Unis, vol. 68 f. 346.
- Exact-phrase searches of Founders Online, the Internet Archive, HathiTrust and Google Books for seven phrases
  of the two readings found nothing; each search route was first tried with a phrase known to be in print.
- **Not reached:** Brant, *James Madison: Commander in Chief* (1961), Hill, *Napoleon's Troublesome Americans*
  (2005), Egan, *Neither Peace nor War* (1983) and Buel (2011) are on loan-only access; their text was covered by
  the phrase searches but their pages were not read, so a paraphrase in them is not excluded. The French volumes
  68 and 69 are not digitised.
- **On the code itself:** Ralph E. Weber, *United States Diplomatic Codes and Ciphers* (1979), p. 187, gives one
  decoded sentence of Thomas Barlow's letter of 10 February 1813; we know of no published table. The decoded
  texts of the key's sources are printed in Manning, *Diplomatic Correspondence of the United States concerning
  the Independence of the Latin-American Nations*, 2:1372-73 (29 September 1811), *The Papers of James Monroe*
  6:200-201 (16 June 1812) and the Madison edition above; we read the manuscripts, and owe the identification of
  Madison's hand to the Madison editors.
- **This repository** had a note that the code's key could be had from M34 roll 16 frame 11
  (`research/nara_triage_a`), lead 1279 (the Princeton copy of Monroe to Barlow, 16 June 1812, closed as read
  from the letterbook) and catalogue 770 (Eustis to Barlow, 25 September 1812, open). Its duplicate check
  (`known.py`) and a search of `targets/`, `catalogue.json` and `research/` found no entry for either letter
  (main of 22 November 2026).

## 9. Method and tools

Images were read by AI agents (model ids in `profile.json`) in strips at full resolution. The key was built by script from the
transcriptions; the scripts and the full evidence set are in the contributor's project files and can be supplied.
`decode.py` in this folder needs only the standard library.

**Statistical validation, 24 Nov 2026 (at integration of PR #878; an AI agent for the maintainers, not a person).**
`mk_validation.py` writes `validation.tsv` from `decryption_1812-09-25.txt` and `decryption_1812-10-25_A.txt`: 110 numbers,
each with its `key.tsv` value; the 9 with only a proposal or no value are unread, struck-out numbers are left out, and
copy B, which repeats copy A, is not added. `python docs/_validate.py barlow1812 --write` (model en-modern): 101 read
tokens, 68 types, 251 letters; reading -2.064 per letter; random keys of the same structure -2.859 (best -2.603, z 6.4);
a key refitted to the shuffled text -1.901 (best -1.879); the same annealer on the real text -1.827. Verdict:
**underdetermined**. The reading is far better than a random key, but a key fitted freely to shuffled text scores
better than the reading, so on 251 letters the letter model cannot tell this reading from an overfitted one. The
test neither confirms nor contradicts the key; what supports it is the decipherments of the time it was rebuilt from
(section 3) and the blind check of section 7. Recorded in `profile.json` (`outcome.validation` and a solution step; the
script dated them 23 Nov by the machine's clock).

## 10. Escalation steps at the write-up (24 Nov 2026; an AI agent for the maintainers, not a person)

Made before the page was written, to see whether the open numbers could still be had from material that is online.
None of these steps changes a reading or the read count.

- **Other letters in the code.** Founders Online, the Madison and Barlow correspondence from 17 November 1811 to
  26 September 1812: fifteen letters, of which the editors' source notes mark code in two only (Madison to Barlow,
  11 August 1812; Barlow to Madison, 26 September 1812), both already among the ten key letters. (The pages were
  searched for the editors' words "encoded", "decoded", "code", "cypher"; the letters were not each read through.)
  The text-layer triage of the National Archives' RG 59 films (`research/nara_triage_a`, a sample, not a full
  reading) lists no coded frame of 1810-1814 that could be this code outside M34 roll 16: roll 15 frame 0314 (1810)
  is in Armstrong's code (972 = the), M35 roll 3 is J. Q. Adams's, M34 roll 17 is Crawford's of 1813.
- **Cryptiana and DECODE.** S. Tomokiyo, "State Department Code: 1797-1866" (cryptiana.web.fc2.com/code/state.htm,
  read on 24 Nov 2026 through a page-summary tool, not line by line), names a THE=1700 code for Barlow's letter to
  Madison of 26 September 1812 (key not found) and for Thomas Barlow's letter of 10 February 1813, and says the
  French deciphered most of the former. It gives no table and neither letter of this folder. The duplicate search
  (`known.py "Joel Barlow"`) finds no DECODE record.
- **Known tables, number by number.** The code tables held in the repository were set against `key.tsv`: the State
  Department sheet WE028 (`../morris1813/beling/key/codebook_M97_13_transcription.csv`, 576 numbers in common), 419
  rows of WE025 (`../poinsett1813`, `../crawford1814`; 150 in common), Armstrong's code (`../armstrong/key972.js`, 218), Rufus
  King's (`../king1797`, 269) and the table of `../jqa` (434). In none of them does a number have the value it has
  here. Weber's other printed tables are not in the repository and were not tested.
- **The word list is that of the State Department sheet.** 584 of the 623 values are entries of the WE028 sheet, and
  short runs stand in the same order at the same spacing (133 ti, 137 tin, 138 tion here; 560, 564, 565 on the
  sheet). The two codes are numberings of word lists of one family. This code is not that sheet and not a
  reordering of its blocks: the spacing drifts (den to di is 5 numbers here and 10 on the sheet).
- **Test of the open numbers by their place in the list** (`we028_structure_plan.md`, written before the run;
  `we028_structure.py`; `we028_structure.tsv`). Control: each of 571 valued numbers left out and predicted from its
  neighbours. Only 47 could be predicted by the rule (the plan asked for 100), and 43 of them were right (0.915; the
  plan asked for 0.95). **The test did not reach its marks, so no value is taken from it.** The four misses (320
  as/ast, 704 de/demand, 862 army/same, 1047 port/bat) may be errors of the table and not of the order; 862 is the
  conflict already listed in `key.md`. They were not followed up. What the order shows for each open number is
  given as a remark only (grade I, inferred from position, which the read count does not take). By the rule the test
  made no prediction for eight of the nine numbers (the neighbours below and above point to different entries), and
  its one interpolated value, aph for 531, is not the word the sense needs (`we028_structure.tsv`). The remarks:
  - 815: 812 is ning, and the sheet runs ning, ninth, nish, nity, nk (446-450). In the key letters 814 stands in
    "Spanish" and 816 in "think" (`key_evidence.tsv`), which are nish and nk at the sheet's spacing. Counting from
    812, 815 would fall on nity, the proposal from the sense; counting from 818 (no) above, it would fall on fix.
  - 537 and 531: here ar is 535 and are 538; the sheet has ar, an unread entry, arch, ard, are (680-684), so 537
    would be arch counting from 535 and ard counting from 538. 531 stands between ap (530) and appear (532), where
    the rule gives aph, not ard. This does not settle which copy is wrong: the test failed its control, and the
    contributor's note above (in regard) leaves it open.
  - 624: between like (623) and live (625), where the sheet has ling and little. Consistent with little.
  - 1567: between journ (1564) and know (1568), where an entry in k belongs. The sheet breaks off there and gives
    nothing more.
  - 1404: between ge (1403) and great (1405). The sheet's entry before great is gre, which gives pro/gre/s: the
    same word, with the value gre where `proposals.tsv` has gres. Counting from 1403 below it would be ged.
  - 706: the number next after den (705), four numbers before di (710). The sheet has dent, dep, depart, depend,
    der, des, design, det, dev between den and di, so det directly after den is out of the order unless this list
    lacks the entries before it. We see no other word for [706]/er/min/ed, and both copies have 706. The proposal
    stands, with this doubt.
  - 103: between dispose (102) and done (105); the rule gives dist from below and dom from above, not ti. 133 is ti
    in the key, so copy A's 103 may be a slip for 133 (i/us/ti/ce). The word is read from copy B in any case.
  - 163: between yet (156) and the comma (168). The sheet gives nothing.
- **The note of June.** The Madison edition (Presidential Series 5:354-57, n. 5, read on Founders Online) identifies "my note of the fifth
  June" in Barlow's private letter of 26 September as his letter of 5 June 1812 to the Duke of Dalberg, enclosed in
  his despatch to Monroe of 13 July 1812; of "my note of the 11th June" earlier in the same letter it says the note
  has not been found (n. 3). Section 6 above says both places are the pair 939 1126. By its place in the list 939
  stands among the words in fif- (933 fi and 935 ficial here; fi 330, ficial 332, fifteen 336, fifth 337 on the
  sheet), so "11th" may be the decipherer's slip and both places may mean the note of 5 June (a remark from position
  only; `key.md` keeps 939 as an open conflict). If the despatch of 25 September speaks of the same note, [163]th
  would be "5th". Nothing gives 163 a value, and it stays
  unread. The enclosure was not looked for on the roll, and the Library of Congress images of the letter of
  26 September were not opened here.
- **Images.** Frames 0232 and 0241 were fetched from the National Archives Catalog and 163 (232R16), 103 (24103)
  and 531 (24106) looked at enlarged, with no overlay: each is clear and is as transcribed.
- **One key, one target.** Both letters use the same code (1700 the, 631 of, 1114 in and the four numbers of
  "imperial", 1039 1627 1014 1132, stand in both).
  `targets/barlow1807` is not related: it is Sir George Barlow at Fort William in 1807 (catalogue 1245), another
  writer and another cipher.

## Transcription doubts

Every code number that is blotted, or on which one of the AI readings differed. "transcription" below means the
two readings of 21 November 2026 made without sight of the first and, for the note to Bassano, the other copy.
All checks were made by AI agents on enlarged strips of the frames, with no overlay; none by a person.

- 761? (25 Sep, 232R12, first group after 745) - read: 761 "s"; checked: image, decode, transcription; blotted and overwritten, only the final 1 is clear (readers 2461, 261, 2?61, none of which has a value); 761 is taken from the word and marked `{+s}poliations`; open.
- 1511 (25 Sep, 232R13) - read: 1511 "ma"; checked: image, decode, transcription; first digit blotted, three of four readers 1511, one 0511 (511 is "ance"); the same 1511 is clear in "Majesty" in both copies of the note.
- 1404 (25 Sep, 232R13) - read: 1404, no value in the key; checked: image, decode, transcription; third digit blotted (readers 1404, 1444, 1424; 1424 is "mess" and does not fit pro..s; 1444 has no value); the word is marked [?progress]; open.
- 1353? (25 Sep, 232R14) - read: 1353 "exp"; checked: image, decode, transcription; the second digit is formed like the 5 beside it and four of five readers read 1553, which has no value; 1353 659 950 is exp/ect/ed on frame 295; marked `{+exp}ected`.
- 831 (25 Sep, 232R17) - read: 831 "confide"; checked: image, decode, transcription; the middle digit has a closed top and three readers read 891 ("vi"); this copyist's 3 between two digits has that form in 631 and 933 on frame 250; "confide/n/ce".
- 1700? (25 Sep, 232R19) - read: 1700 "the"; checked: image, decode, transcription; written like 1780 (five of six readers), which has no value; frame 11 has another 1700 written like 1766; a whole-word group, so marked [?the] and not counted as read; open.
- 750? (25 Sep, 23301) - read: 750 "e"; checked: image, decode, transcription; blotted (readers 750 or 150; 150 is "x"); "mod/e of"; marked `mod{+e}`.
- 1114 (25 Sep, 23301) - read: 1114 "in"; checked: image, decode, transcription; one reader of four 1119 ("mon"); "in/dem/..." as on 232R11.
- 1357 (25 Oct copy A, 24103) - read: 1357 "fu"; checked: image, decode, transcription; readers 1357, 1367, 1387 (1387 is "n"); copy B has a clear 1357; re/fu/sal as in Madison to Barlow, 11 Aug 1812.
- 103 (25 Oct copy A, 24103) - read: 103, no value in the key; checked: image, decode, transcription; one reader 123 (no value); copy B spells the word differently (1650 284 1017, u/st/ice); open as a value, the word is read from copy B.
- 744 (25 Oct copy A, 24103) - read: 744 "part"; checked: image, decode, transcription; one reader 714 ("disc"); copy B has a clear 744; "on the part of".
- 1132? (25 Oct copy A, 24104) - read: 1132 "l"; checked: image, decode, transcription; written like 1192 (two readers), which has no value; copy B has a clear 1132; "im/per/[ia]/l".
- 1157? (25 Oct copy A, 24104) - read: 1157 "est"; checked: image, decode, transcription; blotted (readers 1157, 1167, 1187, the last two without value); copy B has a clear 1157; "ma/I/est/y".
- 314? (25 Oct copy A, 24106, second 314) - read: 314 "as"; checked: image, decode, transcription; written like 714 (three readers; 714 is "disc"); copy B has a clear 314 in the same place; "as wel as France".
- 54? (25 Oct copy A, 24106) - read: 54 "France"; checked: image, decode, transcription; a 5 and a blotted digit (readers 54, 56, 58; 56 is "between"); copy B has a clear 54.
- 896 (25 Oct, both copies, 24106 and 247L04) - read: 896 "wel"; checked: image, decode, transcription; written 89 with a raised 6 and a small sign beneath it, alike in both copies; "as wel as".
- 531 / 537 (25 Oct, 24106 and 247L04) - read: 531 in copy A, 537 in copy B; checked: image, decode, transcription; each is clear in its own copy and neither has a value; the word is marked [?regard]; open.
- 1650 (25 Oct copy B, 246R31) - read: 1650 "u"; checked: image, decode, transcription; one reader of three 1550 (no value); "I/u/st/ice".
- 1017 (25 Oct copy B, 247L01) - read: 1017 "ice"; checked: image, decode, transcription; one reader of three 1817 (no value); "I/u/st/ice".
- 1114? (25 Oct copy B, 247L03) - read: 1114 "in"; checked: image, decode, transcription; third digit blotted (readers 1104, 1124, 1184, none with a value); copy A has a clear 1114; "in reg..".

## Remaining gaps

One line per open piece (detail in sections 4 and 6):

- 815 (twice), 1567 and 1404 in the September letter; 624, 706 and 103 in the note to Bassano - blocker: no-key-material; no decipherer of the time gives them a value, they occur nowhere else in the ten key letters, no sheet of this code is known, and no other letter in the code with a decipherment is online (section 10); each has a value from the sense in `proposals.tsv`, marked [?] in the readings; by their place in the list five of the seven fit and 706 and 103 are in doubt (section 10).
- 163, the day in "my note of the [163]th June" - blocker: no-key-material; no value and none proposed; the note meant is probably that of 5 June 1812 (section 10), but nothing gives the number a value.
- 531 (copy A) or 537 (copy B) in "regard" - blocker: no-key-material; the two copies differ in this one number and neither has a value from a decipherer; by its place in the list 537 is ard and 531 a copyist's slip (section 10).
- The blotted group after 745 in the September letter (232R12) - blocker: illegible; overwritten, only the last digit is clear; read 761 ("s") from the word.
- 1353 written like 1553 (232R14) and the blotted 750 (23301) - blocker: illegible; miswritten or blotted on the only film of the only copy, and read from the word ({+exp}ected, mod{+e}); each word is counted as a hole.
- "the" before United States, written like 1780 (232R19) - blocker: illegible; a whole-word number, so no neighbour can confirm the digit on the only film; marked [?the].

The thirteenth hole, wel{+l} in the note to Bassano, is not a gap that anything could close: the key gives "wel" for
896, the second l is supplied, and the rule counts a word with a supplied letter as a hole.

Not gaps in the text, but limits of the checking: every reading of the numbers so far is by AI agents (four
readings of each number in these letters, six with the verifier and the reviewer; three of each in the key's
sources), and so is our own review of the readings; no person has read the numbers or the readings against the images. Frames 291 and 293 of the key's
sources are poor film; values that rest on them alone are graded L. The note as Bassano received it (Archives du
ministère des Affaires étrangères, Correspondance politique, États-Unis, vol. 69 f. 350, not digitised) would
test the whole reading of the second letter; Eustis to Barlow, 25 September 1812 (catalogue 770), and the
Princeton copy of Monroe to Barlow, 16 June 1812 (lead 1279), would add occurrences.

## Escalation

- [x] siblings: all 296 frames of M34 roll 16 opened; coded text only on frames 11, 232-233, 240-247, 249-250 and 291-295, all used; four more letters in the code found outside the roll (Library of Congress and a sale photograph); 24 Nov 2026: the fifteen Madison and Barlow letters of 1811-1812 on Founders Online have code in two only, both already used, and the RG 59 triage lists no other frame in this code (section 10)
- [x] clear-pages: frames 15-16 are the State Department's decipherment of frame 11 (used for the key); no clear copy or decipherment of either letter read here is on the roll; the two copies of the note to Bassano compared with each other
- [x] known-keys: no key sheet for this code is known; it is not the JQA code that Crawford used from Paris in 1813 (there the = 1385 and of = 1576; here the = 1700 and of = 631); 24 Nov 2026: the WE028 sheet, the held rows of WE025, Armstrong's code, King's code and the JQA table compared number by number, no number with the same value (section 10); Weber's other printed tables not held and not tested
- [x] print: section 8 (American State Papers, Wait, Todd, the Monroe and Madison editions, Brant 1958, Weber 1979; exact-phrase searches of Founders Online, Internet Archive, HathiTrust and Google Books); four later books not read page by page; 24 Nov 2026: the Madison edition's notes to the letter of 26 Sep 1812 identify the note of 5 June 1812, and Tomokiyo's Cryptiana article on the State Department code names the THE=1700 code with no table (section 10)
- [x] key-rebuild: 623 values rebuilt from ten letters deciphered at the time; every source read again by two AI readers and 56 misread numbers corrected (section 7); 24 Nov 2026: the open numbers tested by their place in the word list of the State Department sheet, the test did not reach its marks and no value is taken from it (section 10)
- [x] retry: the nine open numbers looked for in all ten key letters after the corrections: none occurs there; "justice" recovered from copy B's different spelling; 24 Nov 2026: 163, 103 and 531 looked at again on the frames, each as transcribed

## Files

`profile.json`, `NOTES.md`, `key.tsv`, `key.md`, `key_evidence.tsv`, `proposals.tsv`, `decode.py`,
`transcription_1812-09-25.txt`, `transcription_1812-10-25_A.txt`, `transcription_1812-10-25_B.txt`,
`collation_copyB.md`, `decryption_1812-09-25.txt`, `decryption_1812-10-25_A.txt`, `decryption_1812-10-25_B.txt`,
`reading_1812-09-25.md`, `reading_1812-10-25.md`. Added by the maintainers on 24 Nov 2026: `mk_validation.py`,
`validation.tsv` (section 9); `we028_structure_plan.md`, `we028_structure.py`, `we028_structure.tsv` (section 10).
