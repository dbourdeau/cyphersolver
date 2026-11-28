# Code No. 14 (Thomas Barclay, Cadiz, 27 Dec 1792): held-out test protocol (written before any key work)

Written by an AI agent (Claude Opus 5.5) for Andrew Beling, Sat 28 Nov 2026, about 05:56 EST, before any value of
Code No. 14 was built (beyond the five "Gibraltar" values already recorded in
`output/code15_1793_2026-11-28/CODE14_barclay17921227.md` on 28 Nov about 00:00 EST). Nobody has checked it. It follows
Daniel's proposed rule #1014 (a frozen key measured once on a passage chosen beforehand) and the Code No. 15 protocol.

## Material
- The only Code No. 14 text found (Founders Online search, 28 Nov 05:00-05:45 EST; NARA T186 roll 1 frames 0001-0070):
  Barclay's coded paragraph of 27 Dec 1792, in three copies on T186 roll 1 (Despatches from U.S. Consuls in Cadiz):
  frame 0038 = the receiver's copy (RC, clerk's hand, signed by Barclay; left digits of lines 2-17 lost in the gutter);
  frame 0058 = the duplicate (Dupl, whole lines, copying slips struck and rewritten); frame 0037 = an incomplete copy of
  the first 52 groups (probably the draft "in Barclay's hand" that PTJ 24 lists).
- Transcription: an independent helper agent (Claude Opus 5.5, own context, told not to open project files) read all
  three frames blind (28 Nov about 05:51-05:55 EST): `transcription/helper_blind_transcription.tsv`. Agent 1 reads the
  same frames separately; the working sequence `transcription/code14_groups.tsv` is the RC, with gutter-lost digits
  supplied from the Dupl and the draft, and differences kept.
- Clear text: Taylor's decipherment as printed in PTJ 24 (Founders Online Jefferson/01-24-02-0767):
  `plaintext/taylor_decipherment.txt`.

## Held-out passage (chosen now)
The last 30 groups of the working sequence (positions 133-162 of the 162 groups both readers count), with no key value
taken from them. Reason: there is only one coded text, so a held-out passage has to be cut from it; the end of the
paragraph is chosen because its words ("Gibraltar", "Lisbon", "from", "the Business") also occur in the first part, so
a correct key can be tested at all. Where a correction is written above a group (RC line 14: 1482 above 1452), the
group as corrected is used.
Known before the freeze, and disclosed: the 28 Nov 00:00 note read "Gibraltar" in both places (1072 1482 1509 1022
872); the second "Gibraltar" falls in the held-out part. The key takes that word only from its first occurrence.

## Key build
`scripts/build_key.py` reads a hand alignment of groups 1-132 with Taylor's decipherment
(`key/hand_alignment_training.txt`), checks that its groups equal the working sequence and its pieces spell the
decipherment, and writes `key/code14_key_v1.tsv`. It does not read groups 133-162.

## Freeze and timestamp
`plan/MANIFEST.txt` lists SHA-256 of this protocol, the key, the alignment, the working transcription, the helper's
transcription, the clear text and the scripts. Only the SHA-256 of MANIFEST.txt goes to FreeTSA
(https://freetsa.org/tsr, RFC 3161) with `openssl ts -query -data plan/MANIFEST.txt -sha256 -cert`; the .tsq and .tsr
are kept in `plan/` and verified with `openssl ts -verify` before the single run of `scripts/heldout_test.py`.

## Measure (run once)
`scripts/heldout_test.py` aligns the 30 held-out groups with the end of the clear text: the groups must cover a
stretch of the clear text that ends at its last word and starts at any word boundary. A group's piece is part of one
word, a whole word, or two whole words. A group with a key value scores 1 if its value equals its piece; the
alignment with the most matches is taken. k = matches; n = held-out groups with a key value; precision k/n;
coverage k/30. Controls: 1,000 keys made by shuffling the values among the key's groups (random seed 1792), each
measured the same way; p = (1 + number of shuffled keys with at least k matches) / 1001.

## Pass bar
Pass if precision >= 0.80 and p <= 0.01. With 30 groups the test is small; a pass shows the key is consistent, not
that it is complete. No change to the key, the transcription or the script after the timestamp; any later round is
labelled as such.

## Addendum before the freeze (28 Nov about 06:02 EST)
- Disclosure: while transcribing and aligning, agent 1 saw the held-out groups and noticed likely fits there
  ("1142 ... 1142 271 1170" = "as soon as possible", 230 = from, 798 387 = the Business, 944 545 next to 994 545 for
  Lisbon). No value was taken from groups 133-162, but two training choices were made with that in view: the split of
  "impossible" as 1080 / 271 / 1170 (im-pos-sible, marked unsure) and reading 545 as "s". The test is therefore weaker
  than a blind one; it checks consistency, not discovery.
- Key rule as built: a group whose training pieces disagree keeps its majority value (more than half its attestations),
  else no value (`scripts/build_key.py`). Key v1: 87 groups (35 sure, 45 unsure, 7 conflicting; 4 of the 7 have no value).
- Group 151 is 1492 (duplicate; the receiver's copy has only "?2"); it lies in the held-out part.
