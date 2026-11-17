# Addition of 14 Nov 2026: Tobias Lear's coded passages of 8 November and 31 December 1807

Andrew Beling, with AI agents. This folder adds to the bundle; elsewhere in it only a pointer in `../README.md` and the new lines of `../SHA256SUMS.txt` change; `../round_2026-11-11/code16_key_v5.tsv`
is used as it stands (sha256 17e3a2ef...773a, checked by the decode script). The scripts run from `targets/pinckney1793`.
The images are local to the contributor and are not committed.

## The letters (National Archives microfilm M23, Despatches from US Consuls in Algiers, Record Group 59)

| Passage | Letter | Copy 1 (roll 9) | Copy 2 (roll 10) | Groups |
|---|---|---|---|---|
| P1 | 8 Nov 1807 | frame 0182, left page | frame 0072, left page (a clerk's copy) | 28 |
| P2-P6 | 31 Dec 1807 | frames 0190, 0192, 0193, 0194 right, 0197 right ("Triplicate") | frames 0077 right, 0079, 0080 left, 0082 left ("(Copy)") | 21, 24, 64, 60, 66 |
| P7, postscript | 31 Dec 1807 | frame 0199 | frame 0082 right | 18 |

The Madison Papers' online Early Access texts print both letters with the code groups as numbers, not decoded
(Founders Online, Madison 99-01-02-2308 and 99-01-02-2490; their numbers are in `transcriptions/founders_early_access_numbers.txt`).
They follow copy 2.

## Transcriptions (`transcriptions/`)

- `copy1_roll09_reader1_forward.txt`, `copy2_roll10_reader1_from_end.txt`: the first reader, forward on copy 1 and from the
  last passage back on copy 2 (labels G, A-F there = P1-P7 here).
- `copy1_and_2_reader2_blind.txt`: a second reader, blind (before opening the first reader's files), on copy 1, with every doubtful
  group and P2-P7 checked on copy 2.
- `reconciled.txt`: the text used. The two copies differ in two places only: P4 group 3 (980 or 986 in copy 1; 980 plainly in
  copy 2, kept) and a 663 before 374 near the end of P6 in copy 2 only (kept: "on the first favorable"). 281 groups, 280 in copy 1.
- **The small "3" is not a group.** Both copies have a small 3-shaped mark under 972 and under 606 in P6: Code No. 16's caret,
  which doubles the last letter (972 al, 972^ all, as with Eaton's caret). Founders prints one such mark as a group "3." between
  856 and 356. Group 3 is "greatbritain" in key v5, so decoding the printed "3" would put Great Britain into a sentence where
  Lear did not write it.

## Decode (`scripts/decode_lear1807.py` writes `decode_v5.tsv`, `../../ct/lear_1807*.txt`, `../../texts/lear_1807*_decryption.txt`)

- Key v5 as it stands: **222 of 281 groups have a value (0.790)**; per passage 23/28, 14/21, 20/24, 53/64, 47/60, 52/66, 13/18.
- `local_values.tsv`: seven groups the key lacks whose value is fixed by evidence outside it, used only in these readings and
  entered in no key: from the pencil decipherment of the postscript (below) 894 only, 1455 cu, 573 rity, 742 can, 1333 na; fixed
  by recurrence 374 first (three places) and 988 tri (Tri-poli; tri-ou-m-[ph], "triumph"). With them 233 of 281 groups have a value; 48 have
  none.
- Readings: `../../texts/lear_18071108_reading.txt`, `../../texts/lear_18071231_reading.txt`. Plain words are key values;
  word° contains a local value; [?word:n] is a guess for group n; [n] is a group with no value and no guess. read_share 0.792
  and 0.777: read in part.

## Control (`scripts/control_char5.py`, results in `control/`)

The first reader's control (share of decoded letters covered by words of an OCR word list: 0.950 against a maximum of 0.947 of
200 shuffled tables) is withdrawn. It measured how word-like each table value is on its own (77% of the values are entries of that
list), a property every shuffle keeps, so it could not have failed.

The control used is the second reader's: a character 5-gram model of English (the repository's `en-gutenberg` corpus) scored over
the letters of each run of decoded values, joined across group boundaries, so it rewards neighbouring values only when they make
English together. Seed 1807, 200 shuffles. Rerun here on 14 Nov 2026 with the same figures:

| Table | Mean log10 P per letter |
|---|---|
| Key v5 as it stands | **-0.856** |
| 200 tables, values of the 123 occurring groups reshuffled among them: mean / maximum | -1.037 / -0.950 (real table rank 1 of 201, 5.9 standard deviations above the mean) |
| 200 tables, whole 549-row table reshuffled: mean / maximum | -1.030 / -0.907 (rank 1 of 201, 4.4 standard deviations) |
| Lear's own clear sentences from these despatches | -0.722 |

The default run uses the second reader's transcription (280 groups) and reproduces its numbers exactly; `control_char5.py
reconciled` on the 281-group text gives -0.855, 5.8 and 4.4 standard deviations. Neither control was declared before the
passages had been seen in print, and this one was designed after the first reader's decode was known. None of the 281 groups
went into key v5, so the table meets these passages for the first time. The S1 and S2 values of the key (the only element of
Weber's word list that fits) are weak single fits.

## The postscript: a check on the table from 1808

Lear repeated the postscript in his letter of [4] January 1808 (M23 roll 10 frame 0008, right page: "P.S. I must repeat that
663.894 ... 456.1415. especially 394."). There another hand wrote between the lines in pencil "the only real security we can have
in this Sea is a naval force", and "now" over 394. All 13 key values in the postscript agree with that pencil reading (the, re, al,
se, we, have, in, this, sea, is, a, val, force), and 394 = now agrees with the key's grade B value. The pencil supplies the five
local values above.

## Corrections made by the second reader (applied)

- P1: 594 is followed by 924 = t, so the verb ends in t: [?hur]t, not "injure".
- P6: no-[208]-b-t spells "no doubt"; "nothing but" would need 208 = thing and a missing u.
- P6: 606 is not in key v5; "call" is a guess.
- P4: 1176 = cy is grade A, so "[depred]ation can" does not fit; the likelier reading is [?pi][?ra]cy can (705, 956), setting
  aside the key's S1 value 956 = ration here.
- P2: "ten thousand ...s" is key values; "dollars" and "presents" are guesses.
- P4: Tri (988) and first (374) are fixed by their other occurrences; "follow" (1422 715) and "struggle" (1108) are guesses.
- P3: the nation "at present not wel(l) ...ed toward us" is Britain by context only (the same despatch blames English reports in
  clear text; P1 names the English consul in key values); "urged" and "disposed" are partly guessed; the subject is "they" (the
  Algerines), not the Dey.
- 441 is a guess "among" in both its places (709 is already "with").

## Lear, 9 March 1808 (`lear_18080309/`, preliminary)

A further coded passage, Lear to Madison, 9 March 1808, "Duplicate" (M23 roll 10 frame 0014, left page), 113 groups with one
interlined group, on one stained copy. Read twice: forward by the first reader and from the end, blind, by a third reader
(14 Nov 2026); they agree on 106 of 113 groups (`reconciled.txt` keeps both readings where they differ). Decoded with key v5:
81 of 113 groups have a value (0.717), leaving the doubtful groups without one (`decode_v5_preliminary.txt`). It is not read and
not counted. Fragments in key values: "... thousand [1026] in present-s to the [214] men ..."; "I shal not be at [867] until we
have a force in this sea to [474 = ard] our [677]".

## Who read these before

- P7: deciphered at the time (the pencil on frame 0008; hand not identified).
- P1-P6: no decipherment on the film (roll 9 frames 0176-0199; roll 10 frames 0005-0016, 0042-0044, 0054-0056, 0070-0084; text
  layer of rolls 8-11 searched for "decypher", "explication", "cypher"). Not found in Naval Documents Related to the United States
  Wars with the Barbary Powers vol. 6 (which prints Lear's circular of 16-17 Dec 1807, p. 583), American State Papers, Foreign
  Relations vol. 3 (pp. 32-33 print only that circular), or Irwin, Diplomatic Relations of the United States with the Barbary
  Powers (1931), pp. 168-169. Brighton's biography of Lear was not searchable and was not checked. The Madison Papers editors
  read Lear's 1813 letter with a key from the Lear family papers, so their volume for late 1807 may print a decoding; their printed
  Secretary of State Series has reached vol. 14, 1 April-30 September 1807 (University of Virginia Press series page,
  https://upress.virginia.edu/series/PJM, seen 14 Nov 2026). This is the first reading known to us.
