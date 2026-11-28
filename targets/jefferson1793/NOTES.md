# jefferson1793: Jefferson's Code No. 15 (Jefferson and Thomas Pinckney, London, January-April 1793), with Code No. 14 (Thomas Barclay, Cadiz, 27 Dec 1792)

AI agents (Claude Opus 5.5) did all of this work on 27-28 Nov 2026 for Andrew Beling. No person has checked the
transcription, the alignment or the key against the images. A fresh AI agent of ours (Claude Opus 5.5, its own
context, given file paths only) cold-checked the folder on 28 Nov 2026; what it found and what was changed is under
"Cold check" below. Times are EST. The order of plan, key and test rests on local file times, except the freeze,
which carries a FreeTSA timestamp. Code No. 14 was added on 28 Nov 2026 in `code14/` (section "Code No. 14" below);
`profile.json` covers Code No. 15 only.

## Result

**Registered result first.** Key v1, rebuilt by hand from three of Pinckney's letters and their decipherments of the
time, was frozen with the test protocol (SHA-256 manifest stamped by FreeTSA, 28 Nov 2026 04:53:47 GMT) and measured
once on a letter it had not seen: Jefferson's coded sentence of 1 Jan 1793 (72 groups), against the State
Department's clear file copy. **It passed the pre-set bar** (precision >= 0.80 and p <= 0.01): 37 of the 72 groups had
a key value and 33 of those matched (0.892); coverage 33 of 72 (0.458). 1,000 keys made by shuffling v1's values gave
a mean of 4.3 and a best of 11 matches, so p <= 0.001 (the floor for 1,000 shuffles). This shows the key carries the
code's values better than chance; it does not show that every value is right.

What that 33 is made of (from `test/heldout_alignment.tsv`): 24 of the hits are eight common words (to, the, in, of,
and, I, it, be); values marked sure in v1 were right 28 times of 28, unsure ones 5 of 9; by distinct group, 17 of 20.
"troops" (1085 746 911=) gives three hits on one word. Scoring v1 against a fixed hand alignment of the sentence also
gives 33 of 37, so the free alignment in the test did not raise the score. The four misses: 384 twice (key "ire",
text "from") and 393 (key "de", text "their") come from two errors in the training alignment that were visible on the
film before the freeze (below); 1236 (key "ze", text "-e" of desire) was an uncertain split.

**New text: none.** Every passage here already has a decipherment of the time, printed in PTJ 25, and upstream's
`research/founders_emlo/founders_hits.tsv` (lines 27-28, the Founders Online sweep) lists these letters, and Barclay's
of 27 Dec 1792, as read. What is new is the code itself: the PTJ editors say of Codes Nos. 14 and 15 that they "have
been unable to reconstruct significant portions" (note to Pinckney's letter of 20 Jun 1793, PTJ 26). This folder
gives 206 values of Code No. 15 (`key.tsv`), graded, with the test above.

## The documents

| Document (profile id) | Where | Groups | Words from |
|---|---|---|---|
| Jefferson to Thomas Pinckney, Philadelphia, 1 Jan 1793 (`tj_17930101`) | LoC Thomas Jefferson Papers, series 1, mtj1 017 image 0559 | 72 | the clear file copy (DNA RG 59 DCI), PTJ 25 |
| Pinckney to Jefferson, London, 5 Apr 1793 (`tp_17930405`) | NARA M30 roll 2 frames 0077-0078 | 116 | George Taylor Jr.'s interlinear |
| Pinckney to Jefferson, London, 10 Apr 1793 (`tp_17930410`) | M30 roll 2 frame 0083 | 46 | Taylor's interlinear |
| Pinckney to Jefferson, Great Cumberland Place, 27 Apr 1793 (`tp_17930427`) | M30 roll 2 frame 0086 | 144 + about 5 struck | Jefferson's (first sentence) and Taylor's interlinear |

378 legible groups. Pinckney's letters are in William A. Deas's hand. Pinckney had lost his copy of the code in January
1793 and could not read Jefferson's letter of 1 Jan (his letters of 31 Jan and 5 Feb 1793, M30 roll 2 frames 0054-0058).

Not here: the postscript of 19 Mar 1793 in this code (the receiver's copy, frames 0076-0077, has only Jefferson's
decipherment; the code is on the press copy at the South Carolina Historical Society, Pinckney Family Papers);
Gouverneur Morris's extract of 2 Mar 1793, written "entirely in unidentified code by Deas and decoded interlinearly by
Taylor" (PTJ 25), and the duplicates of 5 and 27 Apr, all in NARA's Duplicate Despatches (RG 59, series NAID 733686,
College Park, 57 bound volumes; not filmed or digitized) and Letterpress Despatches (NAID 731320, same). M30 roll 2 was
looked through at frames 0050-0100 and sampled at 0331-0433: no duplicates are filmed there. The Gouverneur Morris
Papers at the Library of Congress have no digitized items (loc.gov, 28 Nov 2026).

## The code

A numerical code of words, syllables and single letters, values up to about 1,600, in no alphabetical order. Common
words have their own groups (1476 of, 1122 to, 611 the, 1001 in, 354 and, 1248 that, 1376 with, 583 be, 1130 I);
longer words are spelt in syllables (1229 1001 834 dom-in-ion; 1165 1139 834= pro-vis-ion-s; 552 1130 832
reg-i-ment). "=" written after a group adds a plural s (1254= ports, 834= -ions); "+" and "x" seem to mark -ed (932+
formed). Some phrases are one group (41 Great Britain, 34 W. Indies, 47 United States). 1010 and 781 stand where no word
was written over them (a null or a stop). No upstream key shares its values (every key file on origin/main was
searched for eight of its commonest values, 27 Nov 2026). It is not Code No. 16 (targets/pinckney1793) and not Code
No. 14 (Barclay 1792).

`key.tsv` (= `key/code15_key_v3.tsv`), 206 groups: 92 "sure" (marked sure in the alignment and either a whole word or
the same value in two places), 15 "probable" (seen only in the 1 Jan letter, so resting on its clear copy as printed),
97 "unsure" (an uncertain split inside a word, or seen once), 2 "conflict" (956 all/again; 1085 in troops, prospect and
expeditions).

## Method and order of events (local file times unless stamped)

27 Nov 2026:
- 23:36-23:57: images saved (NARA catalog media server, LoC image server).
- About 23:40-23:49: two blind transcriptions (agent 1 and a helper agent in its own context, told not to open project
  files). Both saw the words written over the groups.
- 23:50:01: the cribs written (`plaintext/`).
- 23:50:26: `plan/PROTOCOL_code15_heldout.md` written. Its header says "about 23:55 EST": that is wrong; the file time
  is 23:50:26.
- 23:50:50: an automatic aligner was tried and gave a wrong alignment; it was not used. Its output is kept as
  `key/superseded_auto_alignment_NOT_USED.tsv`. It read the training letters only.
- About 23:51-23:53: the hand alignment of the training letters (`key/hand_alignment_training.txt`) and key v1.
- 23:52:57: one transcription cell corrected (a doubtful-digit note that had been put on two 1501s instead of one).
- 23:53:26: `scripts/heldout_test.py` given a dry-run switch (`CODE15_DRYRUN`, which runs with a one-entry dummy key
  and writes nothing; used once to check the script ran).
- 23:53:33: first FreeTSA stamp, replaced 14 seconds later because the header of the alignment file gave a wrong time.
  The key was the same. Both are kept (`plan/superseded_*`).
- 23:53:47 (28 Nov 04:53:47 GMT): `plan/MANIFEST.txt` stamped by FreeTSA. It lists the protocol, key v1, the alignment,
  the transcription, both cribs and three scripts.
  - `openssl ts -verify -data plan/MANIFEST.txt -in plan/MANIFEST.tsr -CAfile cacert.pem -untrusted tsa.crt` gives OK
    (FreeTSA's https://freetsa.org/files/cacert.pem and tsa.crt; the CA file's SHA-256 is 2151b611…044438, the same as
    downloaded again on 28 Nov).
- 23:53:57: the test run once (`test/`).

Agent 1 had seen the groups of the 1 Jan letter and its clear text (in the PTJ text) while transcribing, before the
hand alignment. No value was taken from that letter, and the key script reads the training letters only. The protocol
cannot exclude that this knowledge shaped some hand splits, and every uncertain split that recurs in that letter was
either a hit or a miss.

28 Nov 2026: key v2 (after the test, 23:55 EST); the cold check (about 00:06-00:17, report 00:16:40); key v3 (alignment 00:17:54, key 00:18:00).

## Cold check (28 Nov 2026) and round 3

A fresh AI agent of ours (Claude Opus 5.5) rebuilt keys v1 and v2 byte-identical, verified the stamp and every hash,
reproduced the test exactly and checked the transcription against the images: no digit misreading found in all of the
1 Jan, 5 Apr (continuation) and 10 Apr groups, nearly all of the others and all bracketed groups. Its main points, and
what was done:

1. Two training-alignment errors were visible on the film before the freeze. On frame 0078 Taylor wrote "sail" over
   988, a dash over 1010, "from" over 384 and "Ireland" over 89; on frame 0086 "what" spans ?36 and 460, a struck
   "their" sits over 393 and "detestation" over 1166 417 799. v1 had them wrong. They are three of the four misses.
   Corrected in v2 and v3.
2. Self-made conflicts. 1210 = "ed" fits both "permited" and "succeed"; 824 is "d" in land, send, island and contraband,
   with 781 a group with no word over it. Corrected in v3.
3. Single-attestation splits marked sure (987 arm, 966 gra, 833 mil ...): v3 marks a value sure only if it is a whole
   word or attested twice.
4. Transcription marks. Two "#" marks were placed differently by the two readers; the cold checker's reading of the
   image settled both (`transcription/code15_groups_v3.tsv`). The readers differ at about 11 places (8 digits, 3 marks),
   not 8.
5. Wording in the first notes: p should read <= 0.001; one gutter group claimed as a key fit (E 9.2, 488) is not one.

The other points are folded into this file. Key v3 has not been tested again: no fresh text in this code is online.

## Code No. 14 (Thomas Barclay, Cadiz, 27 Dec 1792): `code14/`

AI agents (Claude Opus 5.5), 28 Nov 2026 about 05:00-06:17 EST; one AI cold check; no person has checked the
transcription, the alignment or the key.

**What it is.** The PTJ editors (vol. 26, note to Pinckney, 20 Jun 1793) give the name Code No. 14 to "the cipher used
for the first time" in Barclay's letter of 27 Dec 1792. Barclay calls it "the Cypher I received from London" (PTJ
24:791). It is probably the cipher Jefferson sent on 1 Jun 1792 with his Algiers instructions to John Paul Jones ("You
will recieve herewith a cypher", PTJ 24:3-10; the enclosure is not found), which Pinckney carried to London and which
reached Barclay after Jones's death; that is our inference from these letters, not a statement in them. The only text
in it we found is Barclay's paragraph (Founders Online searches, 28 Nov; Humphreys's coded sentence of 29 May 1793 is
in Code No. 8). A code of words, syllables and letters, values 1 to about 1,600, not the Code No. 15 table (1562 is
"be" here and "no" there).

**Copies.** NARA microfilm T186 (Despatches from U.S. Consuls in Cadiz) roll 1: frame 0038, the receiver's copy,
signed, 162 groups on 17 lines, lead digits of lines 2-17 lost in the gutter; frame 0058, the duplicate, whole, with
struck repeats and corrections; frame 0037, the first 50 groups then "990, 944" (perhaps the draft that PTJ lists in
Barclay's hand). The words: George Taylor, Jr.'s decipherment of 1793 (RG 59, Miscellaneous Letters; not on this
film), printed in PTJ 24:791-2. Reading the paragraph with Taylor's decipherment is not an independent solution.

**Transcription.** A helper agent read the three frames blind; agent 1 read 0058 against 0038 after the helper's short
report (which named its doubtful groups). They differ at group 28 only (984 against 98[41]); group 110 is 651 or 657
(cold check: 651); group 135 is 1452 on 0038 with 1482 written above, and unclear on 0058 (1452 or 1482); group 151 is
1492 on 0058 (0038 has "?2"). The cold checker read all of 0038 and found the working sequence
(`code14/transcription/code14_groups.tsv`, frozen) right. Its note at 135 ("Dupl 1482") goes further than the image.

**Freeze and test (rule #1014).** Held out: the last 30 groups (133-162); key from groups 1-132
(`code14/key/code14_key_v1.tsv`, 87 groups: 35 sure, 45 unsure, 7 conflicting). Order of events: protocol first
written about 05:55-05:56 EST (agent's statement; the file was last written at 06:00:10 when its addendum was added,
and the addendum's own label "about 06:02" is wrong); key built 05:59:40; manifest of 10 files stamped by FreeTSA
28 Nov 2026 11:00:21 GMT (06:00:21 EST), `openssl ts -verify` OK with https://freetsa.org/files/cacert.pem (SHA-256
2151b61137ffa86bf664691ba67e7da0b19f98c758e3d228d5d8ebf27e044438) and https://freetsa.org/files/tsa.crt (SHA-256
8bfb0305bb64e2571ca507552ef3245cb1c2fee8728e0ff8689225081ea13467); run once at 06:00:24.
**Registered result: pass, 16 of 18 keyed groups** right (precision 0.889; coverage 16/30; shuffled keys mean 4.1,
best 7 of 1,000; p = 0.001). What the 16 is made of: one (545 = "s" inside "Lisbon", pos 147) rests on a split these
notes reject, and without it the count is 15 of 18 (0.833); five are the repeated "Gibraltar", known before the freeze;
three (pos, sible, and that s) come from training choices made with the held-out part in view, as the protocol's
addendum says; one ("n" of soon) is a coincidence of a split; seven (to, as, as, from, to, the, business) are clean
repeats of whole-word values. The test shows the key is consistent; it is not a blind test.

**What the key rests on.** Only 1509 = l, 1022 = ta and 872 = r are backed group by group by a witness of the time
(Taylor's printed note on the second "Gibraltar": "Gi war l ta r / 107. 1452. 1509 1022. 872."). 1072 = gi rests on the
image (the print has "107"); 1482 = bra is inferred. Every other value is our split of Taylor's prose. "Sure" in the
key means the group certainly lies inside that word, not that the split inside the word is attested.

**What the page adds.** Taylor's "Giwarltar" comes from the clerk's 1452 in the second "Gibraltar", with 1482 written
above it on 0038; the first "Gibraltar" has 1482. The page has 1072 where PTJ prints "107".

**Open.** 545 after "Lisbon" (994 545 and 944 545) is not "s" there; it may be an end sign or a null. 1568 1057 stand
at both "where" and "and". "exert every nerve" (nine groups) and "finish" (716 1344) are not split. New words: none.

## Open points (not findings)

1. **10 Apr 1793, "will be again allotted"** has four groups, 1257 583 956 1198x. Taylor first wrote "will again
   allotted" and added "be" with a caret. 1257 583 is "will be" on 5 Apr, and 956 (with a mark) is "all" there. So the
   code may say "will be allotted", with 956 1198 = al-lotted, and "again" may be Taylor's. Or 956 is "again". The
   editors' "one anomaly" in Taylor's decipherment of this letter may be this. Not settled.
2. **27 Apr 1793, group 460** between "what" and "their", where Taylor struck a word in his interlinear. It is counted
   with "what" in the key. Not settled.
3. **27 Apr 1793**: about five groups struck out by Pinckney after "intoxication of" (PTJ: "Pinckney here canceled
   five codes"), illegible on the film.

## Remaining gaps

- Code No. 14: one known text only, so no blind test is possible; the code table (Jones's copy, or the two ciphers
  Humphreys took from Barclay's papers in Feb 1793) is not found; 45 values rest on an uncertain split.
- None in the text: every passage reads in full from its decipherment of the time.
- In the key: 97 values rest on an uncertain split and 2 conflict. A second held-out test needs fresh text in this code.
  The only known copies are at NARA College Park (Duplicate Despatches: the 5 and 27 Apr duplicates and Morris's extract
  of 2 Mar 1793 with Taylor's decipherment) and at the South Carolina Historical Society (the 19 Mar postscript; a
  further copy of Morris's extract in code).
- Gutter losses: 19 groups on M30 roll 2 lost their leading digits. For 7 of them exactly one key value fits the visible
  digits and the word over them (B 3.1 611 the, B 4.1 244 French, B 6.1 832 -ment, B 7.1 1476 of, D 2.1 832, E 3.1 354
  and, E 7.1 1130 I). These are fits, not readings, and are not entered in the key. The duplicates would settle them.

## Transcription doubts

Two readers each, blind (agent 1 and a helper agent, both Claude Opus 5.5); then checked by the cold checker.
- 119[35] (1 Jan, line 4.7): read 1193 or 1195; checked: image, transcription; the descender is unclear.
- ?[38]5 (10 Apr, 3.1): read 385 or 335 after a lost digit; checked: image, transcription; gutter.
- 14?6 (27 Apr, 1.3): second digit under an ink blot; checked: image, transcription.
- 150[17] (27 Apr, 2.6): read 1501 (agent 1, cold checker) or 1507 (helper); checked: image, decode (1501 = "a"
  elsewhere), transcription.
- [38]22 (27 Apr, 3.14): first digit 3 or 8; checked: image, transcription.
- 8[39]2= (27 Apr, 5.12): read 832 (helper) or 892 (agent 1); checked: image, decode (832 = -ment in three places),
  transcription.
- 4[58]8 (27 Apr, 9.2): read 488 (agent 1) or 458 (helper); checked: image, transcription; ?488 = "are" in line 2 has
  lost its first digit, so the key cannot settle it.
- 11[18]7 (27 Apr, 10.12): 1117 or 1187; checked: image, transcription.
- 112? and 401? (5 Apr, frame 0078): at the right edge of the leaf; a digit may be lost.
- The 1 Jan letter has a faint pencil "I have" over its first groups (not Jefferson's code); left aside.

## Not checked

- Code No. 14: no person has read its images or checked its alignment; Taylor's decipherment sheet of 1793 (RG 59,
  Miscellaneous Letters) and the code table itself were not seen; Pinckney's letters to Barclay (South Carolina
  Historical Society) were not searched.

- No person has read the groups, the alignment or the key against the images.
- The PTJ editors' unpublished partial reconstruction of Code No. 15 (Jefferson Editorial Files) was not seen; this key
  may agree or disagree with it.
- Taylor's own decipherment sheets (RG 59 MLR) were not seen.

## Access and conditions

All images are public scans: NARA catalog (M30 roll 2, RG 59) and the Library of Congress (Thomas Jefferson Papers).
They are not committed; the frame numbers are given above. Code No. 14: NARA microfilm T186 roll 1 frames 0037, 0038,
0058 (public, from catalog.archives.gov). Raw copies with SHA-256 sums were kept locally.

## Files

- `code14/` (Code No. 14): `ct/barclay_17921227.txt` (groups as read, one line per manuscript line); `transcription/`
  (both readings and the frozen working sequence); `plaintext/taylor_decipherment.txt`; `key/` (hand alignment of
  groups 1-132 and key v1); `plan/` (protocol, manifest, FreeTSA query and reply); `test/` (the single run);
  `scripts/` (`build_key.py`, `heldout_test.py`, `code14lib.py`). Run the scripts from `targets/jefferson1793/code14/`
  with `python3 -I scripts/build_key.py` and `python3 -I scripts/heldout_test.py`; their frozen docstrings name the
  local folder they were written in (`output/code14_2026-11-28`), which is not in this repository.
- `ct/<id>.txt`, `texts/<id>_decryption.txt`, `validation.tsv`: built by `scripts/make_texts.py` from
  `transcription/code15_groups_v3.tsv`, `key.tsv` and `key/hand_alignment_v3.txt`. `texts/<id>_reading.txt`: written
  by hand from the decipherments of the time.
- `transcription/`: the two blind transcriptions, the settled table as frozen (`code15_groups.tsv`) and with the marks
  corrected (`code15_groups_v3.tsv`).
- `plan/`: protocol, manifest, FreeTSA query and reply (and the superseded ones). `test/`: the single run.
- `key/`: v1 (frozen; `scripts/build_key.py`), v2 and v3 (after the test; `scripts/build_key_v2.py`,
  `build_key_v3.py`), with their hand alignments. `scripts/heldout_test.py`, `scripts/code15lib.py`.
- The source column of `plaintext/training_cribs.tsv` (frozen) says the words were checked against PTJ 25 on Founders
  Online; the check on 27 Nov was made against the same PTJ text in the Rotunda edition. On 28 Nov Founders Online gave
  the same wording for 1 Jan and 5 Apr 1793.
- `python docs/_validate.py jefferson1793` could not be run on 28 Nov 2026: gutenberg.org answered 503 when the English
  model's corpus was fetched.

## Credits

Code No. 14: the words are George Taylor Jr.'s decipherment of 1793, as printed by the editors of The Papers of Thomas
Jefferson (vol. 24, 1990), who also named the code (vol. 26, 1995).

The words are those of the decipherments of the time, by George Taylor Jr. and Thomas Jefferson at the State
Department, and of the clear file copy of Jefferson's letter, as printed by the editors of The Papers of Thomas
Jefferson (vol. 25, 1992; Founders Online). Transcription, key and test: Andrew Beling (ajbeling), with AI agents.
