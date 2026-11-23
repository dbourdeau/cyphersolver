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
   649 numbers, of which 623 have a value from a decipherer and 21 a word; the other five occur only in the
   passages read here.

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
italics. Read share (words read over words plus holes, a supplied word counting as a hole): 0.978 and 0.994 for
the whole letters; 0.824 and 0.885 over the coded words alone (34 and 26 words). The repository's sentence check
(`docs/_check_reading.py`) is a different measure, the share of sentences without a hole: 0.812 and 0.877. Both letters are marked "read in
part": the profile counts over the coded words (0.85 together, 51 of 60), as lee1813 does.

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
  from Thomas Barlow's letter of 1813.
- In copy A the last two numbers of 24106 are unclear (the first written like 714, the second a 5 and a blot);
  copy B has 314 54, "as France".

### Our own review of the readings (21 November 2026)

An AI agent of ours that had made none of the readings reviewed both letters by the repository's rule. It first read
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

- 815 (twice), 1567 and 1404 in the September letter; 624, 706 and 103 in the note to Bassano - blocker: open-codes; no decipherer of the time gives them a value and they occur nowhere else in the ten key letters; each has a value from the sense in `proposals.tsv`, marked [?] in the readings.
- 163, the day in "my note of the [163]th June" - blocker: open-codes; no value and none proposed; Madison's decipherment of the sister letter gives the day once as 11th and once as fifth.
- 531 (copy A) or 537 (copy B) in "regard" - blocker: open-codes; the two copies differ in this one number and neither has a value.
- The blotted group after 745 in the September letter (232R12) - blocker: illegible; overwritten, only the last digit is clear; read 761 ("s") from the word.

Not gaps in the text, but limits of the checking: every reading of the numbers so far is by AI agents (four
readings of each number in these letters, six with the verifier and the reviewer; three of each in the key's
sources), and so is our own review of the readings; no person has read the numbers or the readings against the images. Frames 291 and 293 of the key's
sources are poor film; values that rest on them alone are graded L. The note as Bassano received it (Archives du
ministère des Affaires étrangères, Correspondance politique, États-Unis, vol. 69 f. 350, not digitised) would
test the whole reading of the second letter; Eustis to Barlow, 25 September 1812 (catalogue 770), and the
Princeton copy of Monroe to Barlow, 16 June 1812 (lead 1279), would add occurrences.

## Escalation

- [x] siblings: all 296 frames of M34 roll 16 opened; coded text only on frames 11, 232-233, 240-247, 249-250 and 291-295, all used; four more letters in the code found outside the roll (Library of Congress and a sale photograph)
- [x] clear-pages: frames 15-16 are the State Department's decipherment of frame 11 (used for the key); no clear copy or decipherment of either letter read here is on the roll; the two copies of the note to Bassano compared with each other
- [x] known-keys: no key sheet for this code is known; it is not the JQA code that Crawford used from Paris in 1813 (there the = 1385 and of = 1576; here the = 1700 and of = 631)
- [x] print: section 8 (American State Papers, Wait, Todd, the Monroe and Madison editions, Brant 1958, Weber 1979; exact-phrase searches of Founders Online, Internet Archive, HathiTrust and Google Books); four later books not read page by page
- [x] key-rebuild: 623 values rebuilt from ten letters deciphered at the time; every source read again by two AI readers and 56 misread numbers corrected (section 7)
- [x] retry: the nine open numbers looked for in all ten key letters after the corrections: none occurs there; "justice" recovered from copy B's different spelling

## Files

`profile.json`, `NOTES.md`, `key.tsv`, `key.md`, `key_evidence.tsv`, `proposals.tsv`, `decode.py`,
`transcription_1812-09-25.txt`, `transcription_1812-10-25_A.txt`, `transcription_1812-10-25_B.txt`,
`collation_copyB.md`, `decryption_1812-09-25.txt`, `decryption_1812-10-25_A.txt`, `decryption_1812-10-25_B.txt`,
`reading_1812-09-25.md`, `reading_1812-10-25.md`.
