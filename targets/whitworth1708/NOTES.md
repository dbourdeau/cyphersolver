# whitworth1708: Charles Whitworth's despatches from Moscow, September and October 1708 (TNA SP 91/5): a partial table of his numerical code, rebuilt from the office's own decipherment and tested on a bare duplicate

Status: already deciphered at the time and printed in 1886; our part is the table of the code (246 numbers) and its
test, not a first reading.

Contributed by Andrew Beling, with AI agents. Every transcription, test and check here is by AI agents; no person has
read the numbers against the images (see "Remaining gaps"). Catalogue 863 and lead 1151.

Whitworth, the English envoy at Moscow, wrote parts of his despatches to Secretary Boyle in a numerical code and sent
each despatch twice. The copy that arrived first was deciphered in the Secretary of State's office, which wrote the
words above the code groups; the duplicate was filed bare. The Russian Historical Society printed the despatches in
English in 1886 from the deciphered copies. So these letters have been read since 1708. What was missing was the code
itself. We took the office's words above the groups on the two originals of 22 September / 3 October 1708 and built a
table of 246 numbers from them, then tested it once, under a plan written and hashed beforehand, on a different
despatch that survives bare: the duplicate of 1/12 September 1708. Of its 112 code groups 78 are in the table and 69
of those fit the printed text (0.885; pass mark 0.80), against 0.17 for the 99th percentile of 1,000 shuffled tables.
An earlier test, with a table built from the print alone, was void by its own rule and is reported below. With the
table alone the bare duplicate is "decoded, not read": 47 of its 77 coded words come out whole.

This confirms the office's decipherment and gives a reusable part of the code. It is not an independent solution:
every value in the table is drawn from the office's words. Which group carries which part of a word is our alignment,
and one such split (236) is wrong.

## 1. Documents

The National Archives (Kew), SP 91/5, Secretaries of State: State Papers Foreign, Russia. The volume has two
foliations. The catalogue (TNA Discovery, and catalogue 863 here) uses the older pencil numbers; State Papers Online
uses the stamped numbers. For these items the stamped number plus 184 is the old one, plus 186 from stamped f. 112 on.
Each pair below was confirmed on the pages (both numbers are written on them).

| id | Letter | Stamped folio | Old folio (catalogue) | Code | Decipherment on the copy |
|---|---|---|---|---|---|
| 1708-09-22-relation | Whitworth to Boyle, Moscow, 22 Sept / 3 Oct 1708 | f. 90 (original) | f. 274 | 475 groups | the office's, above the groups |
| | the same, duplicate | f. 114 | f. 300 | 473 groups | none |
| 1708-09-22-private | Whitworth to Boyle, "private letter", same date | f. 110 (original) | f. 294 | 357 groups | the office's, above the groups |
| | the same, duplicate | f. 112 | f. 298 | 357 groups | none |
| 1708-09-01 | Whitworth to Boyle, Moscow, 1/12 Sept 1708, duplicate | f. 49 | f. 233 | 112 groups on two pages | none |
| | the same, original (not seen) | f. 42 | f. 226 | "partly in cipher" | presumably the office's |

Catalogue 863's check is to "match SP 91/5/298 with SP 91/5/294". That match is done: old f. 298 (stamped 112) is the bare duplicate
of the private letter whose deciphered original is old f. 294 (stamped 110), and old f. 300 is likewise the bare
duplicate of old f. 274. The duplicate's groups and the original's agree in sequence apart from scattered digits
(`compare/`). The seven other items of catalogue 863, in SP 91/6 (1709), were seen only after this folder was first
offered, on 22-23 November 2026; nothing from them is in this folder (Remaining gaps).

## 2. Sources and images

- The manuscripts were read, by AI agents, from the page images of State Papers Online, 1509-1714 (Gale), under a
  library licence.
  **No image or crop is in this folder**; the licence does not allow it. What is here is our transcription.
- Catalogue records: old f. 226 <https://discovery.nationalarchives.gov.uk/details/r/C6719667>, old f. 274
  <https://discovery.nationalarchives.gov.uk/details/r/C6719686>, old f. 294
  <https://discovery.nationalarchives.gov.uk/details/r/C6719691>, old f. 298
  <https://discovery.nationalarchives.gov.uk/details/r/C6719693>. The records of old ff. 233 and 300 were not looked up
  by id. TNA has not digitised the volume itself.
- The printed text: *Sbornik Imperatorskago Russkago Istoricheskago Obshchestva*, vol. 50 (St Petersburg, 1886),
  English with a Russian translation, from "Public Record Office, Russia, No. 8": No. 22 (1/12 Sept 1708, pp. 44-49),
  No. 27 (22 Sept / 3 Oct, pp. 83-88), No. 28 ("Private letter", pp. 88-92). Internet Archive:
  <https://archive.org/details/sbornikimperatorskogorusskogoistorichesk58>. Typed from the page images by an AI reader,
  once, proofread once (`print/`). No. 22 opens with an ellipsis: it is an extract, and all the coded passages of the
  duplicate fall inside it.

## 3. The system and the key (`key.tsv`)

A numerical code of words, syllables and single letters, written as numbers separated by dots among clear words. The
numbers seen run from 31 to 1503 (368 different numbers in the three letters). The table shows several alphabetical
runs: single letters from 31 (a) to 141 (y), with several numbers to a letter; syllables from 146 (af) to 253 (wo);
a second run of syllables and short words from 264 (an) to 481 (well); then runs of words, 494 (arm) to 597 (writ),
601 (your) to 713 (was), and upwards, with names and titles high in the range (1415 Archangel, 1423 Czar, 1503
tobacco). Common words have more than one number (the: 357, 469; and: 496, 607). No key sheet for this code was looked
for beyond the volume; BL Add MS 37354-60 (Whitworth's papers) were not seen.

`key.tsv` has 246 numbers, exactly as frozen before the test:

- **tier S, 139 numbers**: the number stands alone under one word of the office's decipherment at least once, and
  never alone under a different word. Three numbers with conflicting words above them are left out (211, 239, 497).
- **tier A, 62**: found by aligning the groups of each coded stretch with the office's words for it (the aligner of
  the first test, started from the tier S values), seen at least twice with the same value in all ten runs.
- **tier B, 45**: found the same way but seen once, between two fixed neighbours. The weakest tier.

The reader who typed the originals placed each of the office's words after the groups it stands above, by eye, and is
sometimes a group or two out. That is how one wrong value got in: **236 is "post" in the table and is almost certainly
"st"** (the office's word "post" stands above two groups, 219 and 236; elsewhere 236 is the st of brimstone, Stiles
and assistance). It is left as frozen and marked in the note column. Values that sit out of alphabetical place for
their number (109 and 180 "the", 157 "came", 165 "not", 927 "of") should be treated with the same caution. Three
other values missed on the held-out letter and are marked: 219 (po), 36 (a), 505 (court).

## 4. Validation (`validation.txt`, `frozen/`)

Two tests, each written down with its pass mark and controls and hashed before it was run, each run once.

**First test, 21 November 2026: void.** Before the originals were seen, a table was built from one bare duplicate
(stamped f. 114) and the 1886 print by alignment alone, and tested on the other duplicate of the same day (f. 112).
The plan required 100 covered groups. The table had 49 numbers and covered 87 of 357 groups, of which 84 fitted the
print. By its own rule the test says nothing, and its table was not used (`frozen/test1_void/` keeps the plan, its hashes, the
output and the 49-number table as a record; the inputs that only this test used are not in the folder, so it cannot be
rerun from here).

**Second test, 22 November 2026: pass, on a small sample.** Plan `frozen/plans/TEST_PLAN_2_whitworth1708.md`, hashed
with every input at 21:18 EST; table frozen at 21:21 EST before the held-out file was opened.

| | |
|---|---|
| Held out | all 112 code groups of the duplicate of 1/12 Sept 1708 (stamped f. 49), in 15 stretches |
| In the key | 78 groups (0.70) |
| Fit the 1886 print | **69 of 78: 0.885** (pass mark 0.80) |
| By tier | S 48 of 51; A 16 of 18; B 5 of 9 |
| Shuffled tables, 1,000 | median 0.10, 99th percentile 0.17, highest 0.22 (margin required 0.30; found 0.72) |
| Coded letters under hits | 185 of 328 (0.56) |
| Not in the key | 34 groups, 33 numbers |

The floor for a valid test was 40 covered groups, set in the plan, because the whole letter has 112 groups; the first
test's floor of 100 could not be met on it. A pass here is a statement about 78 groups.

That the plan predates the run rests on the hashes and clock times in these files. There is no public timestamp.
The held-out letter was first opened before the plan: its page images were saved on 21 November 2026 at 09:35 EST, and
its two blind transcriptions were made on 22 November between 21:08 and 21:14 EST (they are among the hashed inputs).
What came after the freeze was the first use of any key value on it.

The nine misses, looked at afterwards: four are the print's spelling (warned for war-n-d, engage, Moscovites,
humored); one is word order (the code has "... and persons", the print "persons and effects"); four are the key's or
the reading's (219, 36, 505, 236). An AI checker that had not made the test reran it from the frozen files (same table
byte for byte, same scores), found no path from the held-out letter into the table, and read the nine missed groups
and about 45 others on the images as transcribed (`frozen/test2/VERIFY_test2.md`). Counting only key values of three or
more letters the score is 31 of 36 (0.861) against 0.11 for the shuffled control.

## 5. Texts

- `transcription_1708-09-01.txt`: the duplicate of 1/12 Sept 1708, all six pages, clear words and code groups.
  Two blind AI readings (`frozen/transcriptions/passA_f049.txt`, `passB_f049.txt`) give the same 112 groups.
- `decryption_1708-09-01.txt`: `key.tsv` applied to the 15 coded stretches, unedited, with the 1886 print's words for
  each stretch beside it and labelled as the print's. `python decode.py` rebuilds and checks it.
- `reading_1708-09-01.md`: the coded passages in their clear context, holes marked, and the word count. State
  "decoded, not read": 47 of 77 coded words whole from the key (0.61, an estimate: groups do not map to words one to
  one, and the word list is the print's).
- `interlined_1708-09-22_relation.txt`, `interlined_1708-09-22_private.txt`: the two originals, clear words, code
  groups and the office's words above them. These are the office's decipherment as we read it, the material the key
  was built from. Not prose files.
- `print/`: the three despatches as printed in 1886.
- `compare/`: each original against its duplicate (groups) and against the print (words).

What the despatch of 1/12 September says in its coded passages (from the 1886 print): Whitworth has warned the English
merchants not to give credit, since if the King of Sweden breaks in he cannot see where the Russians would raise
money; their persons and effects will be safe at Archangel; the end of the war may be best observed by the ministers
who follow that king; and on the affront to the Russian ambassador in London he hopes to stop all by recrimination
and not awaken notions of shame by seeming too much concerned.

**The print against the manuscripts.** In the coded passages of the two letters of 22 Sept / 3 Oct the 1886 print and
the office's words agree apart from spelling and, in the relation, five one-word differences (sent / writ, letter /
letters, gentleman / gentlemen, a name, "answer dated" / "answers"); these rest on one AI reading and were not
rechecked. The duplicate of 1/12 Sept has "if he still threatens" in clear where the print has "as he", and a clear
"allways" the print lacks.

## 6. Prior work

- The Secretary of State's office deciphered the received originals in 1708 (the words above the groups on stamped
  ff. 90 and 110; presumably also f. 42).
- The editors of the Sbornik printed the despatches from the deciphered copies in 1886 (above).
- This repository: the UK archives sweep of October 2026 listed the items from the catalogue (lead 1151, catalogue 863,
  not viewed). Andrew Beling's vetting of lead 1151 (14 Nov 2026, with an AI agent) found the Sbornik text and marked
  the 1708 despatches as already in print deciphered.
- No published table of this code was found. Not searched: Hartley's life of Whitworth (2002), the British Library's
  Whitworth papers.

## 7. Method and tools

All in `frozen/scripts/`, Python standard library only. `merge_passes.py` merges two blind transcriptions;
`build_runs2.py` pairs coded stretches with the print by their clear-word neighbours; `wlib.py` holds the aligner,
the table rule, the score and the controls; `wlib2.py` the reading of the interlined files and the tier S rule;
`run_test2.py` is the test. Before the plan was fixed the rule was tried on the building letters only (table from one
original, scored on the other letter's duplicate; `frozen/test2/dev_*.txt`); those figures chose the rule and are not
results. Models: Claude Fable 5.2 (planning, scripts, write-up) and Claude Opus 5.5 (transcribers, typist, checker).

## Transcription doubts

Duplicate of 1/12 Sept 1708 (stamped f. 49). Two blind readings agree on all 112 groups; the doubts are the groups
either reader gave with a second reading or named as worth a second look.

- 51 (p. 2 l. 2) - read: 51; checked: image, decode, transcription; reader B gave 51|31, reader A 51 alone, a third AI reader 51; the key's "d" gives war-n-d
- 31 (p. 2 l. 3) - read: 31; checked: decode, transcription; reader A gave 31|21, reader B 31 alone; 31 is "a" in br-?-a-? (print: break)
- 563 (p. 2 l. 4) - read: 563; checked: transcription; reader A gave 563|565, reader B 563 alone; the number is not in the key, so the decode cannot settle it
- 679 (p. 2 l. 21) - read: 679; checked: transcription; reader B gave 679|619, reader A 679 alone; not in the key
- 587 (p. 3 l. 22) - read: 587; checked: decode, transcription; reader B gave 587|584, reader A 587 alone; 587 is "their", which the print has here (584 is "then")
- 219 and 990 (p. 2 ll. 3-4) - read: 219, 990; checked: image, transcription; a faint office stamp lies over both; both readers and a third AI reader read them so; 219 (po) does not fit the print here and stays doubtful
- 645, 347, 33, 607, 379 (pp. 2-3) - read: as given; checked: decode, transcription; named by reader A as worth a second look; reader B has the same numbers and each fits the print (have, sh, a, and, all)

The two originals of 22 Sept / 3 Oct 1708 (stamped ff. 90 and 110) were typed once. Their groups were then set
against the two blind readings of the bare duplicates:

- 47 of the 832 groups (28 in the relation, 19 in the private letter) differ from the duplicate's agreed reading, carry a second reading or have no counterpart - read: left unknown; checked: transcription; none was used to build the key (`compare/`, `frozen/transcriptions/adjudication.tsv`)
- 366 (private letter p. 2 l. 1) - read: 366 in the original; checked: transcription; the two readers of the duplicate disagreed (366 and 306) and it had been settled as 306 by eye; the original's 366 with "will" above it shows that was wrong
- the placing of the office's words over the groups - read: by eye; checked: decode; one wrong value is known from it (236), found on the held-out letter and on an image check by a third AI reader

## Remaining gaps

- the 34 groups (33 numbers) of the duplicate of 1/12 Sept 1708 that are not in the key, and with them 30 of its 77 coded words - blocker: open-codes; the original of that despatch (stamped f. 42) should carry the office's words for every one of them, and 19 other 1708 originals in the volume are catalogued "partly in cipher"; none of these was seen
- 236 (post, should be st), and 219, 36 and 505, which missed on the held-out letter - blocker: open-codes; more glossed occurrences would settle them
- the other items of catalogue 863, in SP 91/6: catalogue ff. 9, 99, 144, 210, 213, 222, 225 (1709): the key was not tested on them or extended from them - blocker: not-attempted; seen on State Papers Online on 22-23 November 2026, after this folder was first offered, by AI agents; nothing from them is in this folder. On one AI reading, with the groups counted once: each item is a bare copy of a despatch whose other copy in the same volume carries the office's words above the groups (catalogue f. 213, stamped f. 211, is itself that deciphered copy), and the Sbornik prints the despatches (Nos. 45, 60, 70-71, 81, 83). Correction: this line said the opening of No. 81 (29 July / 9 Aug 1709), which the print replaces with an ellipsis, might be in code and unprinted. It is not: on stamped f. 211 the opening is in clear, and the 21 coded groups carry the office's words, which are the words No. 81 prints (two AI readings of that page)
- no person has read any group or word against the images - blocker: not-attempted; all readings are AI readings, the checks included
- the interlined originals were typed once - blocker: not-attempted; their groups were cross-checked against the duplicates, their words only against the print

## Escalation

- [x] siblings: both despatches of 22 Sept / 3 Oct used for the key (originals and duplicates); the duplicate of 1/12 Sept held out; two other duplicates in the volume (stamped ff. 120, 122) looked at and found to carry no code
- [x] clear-pages: the originals carry the office's decipherment above the groups; the neighbouring leaves were looked at and carry no further code
- [x] known-keys: no key for this code is known to us; none in this repository (known.py on SP 91/5 and SP 91/6 gives only the catalogue row and the lead)
- [x] print: Sbornik vol. 50 (1886) Nos. 22, 27, 28 typed from the page images and compared with the manuscripts
- [x] key-rebuild: 246 numbers from the office's words (tier S) and a seeded alignment (tiers A, B), frozen before the test
- [x] retry: the first test (print alone, one duplicate) was void; the second (office's words, both originals) passed once on a letter no earlier test had touched; nothing was re-run after a score

## Files

- `key.tsv` (246 numbers, with tier and notes), `decode.py`, `stretches_1708-09-01.tsv`
- `transcription_1708-09-01.txt`, `decryption_1708-09-01.txt`, `reading_1708-09-01.md`
- `interlined_1708-09-22_relation.txt`, `interlined_1708-09-22_private.txt`
- `validation.txt`
- `frozen/`: `plans/` (second plan and its hashes), `scripts/`, `transcriptions/` (every input of the second test,
  the two blind readings of f. 49 among them), `test2/` (frozen table, output, result, per-group reading of f. 49 in
  `heldout_reading.tsv`, the method check, the checker's report), `test1_void/` (first plan, hashes, output, its table)
- `print/` (Sbornik Nos. 22, 27, 28), `compare/` (originals against duplicates and print)
