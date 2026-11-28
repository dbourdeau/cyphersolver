# Code No. 15: held-out test protocol (written before any key work)

Written by an AI agent (Claude Opus 5.5) for Andrew Beling, Fri 27 Nov 2026, about 23:55 EST, before any value of
Code No. 15 was built. Nobody has checked it. This follows Daniel's proposed rule #1014 (a frozen key measured once on
a passage chosen beforehand).

## Material
- Transcription: `transcription/code15_groups.tsv` (379 groups; agent 1 and an independent helper agent transcribed
  blind from the images and agreed on 371 of 379 groups; the 8 disagreements are kept with the doubtful digit in
  brackets). Documents: A = Jefferson to Pinckney, 1 Jan 1793 (LoC, mtj1 017 image 0559); B, C = Pinckney to
  Jefferson, 5 Apr 1793 (NARA M30 roll 2 frames 0077-0078); D = 10 Apr 1793 (frame 0083); E = 27 Apr 1793 (frame 0086).
- Not reached: the 19 Mar 1793 postscript (code only on the press copy at the South Carolina Historical Society) and
  Morris's extract of 2 Mar 1793 (Duplicate Dispatches, not on M30 roll 2 frames 0050-0099).

## Held-out passage (chosen now)
Document A, Jefferson's coded sentence of 1 Jan 1793, all 72 groups. Crib: the en clair State Department file copy as
printed in PTJ 25 (`plaintext/heldout_crib.txt`). Reason: it is a whole letter, has a clear text independent of
Taylor's decipherments, was enciphered by a different hand (Jefferson, not Deas), and has no gutter losses.
Agent 1 saw the groups of A while transcribing; no value was taken from A, and the key script reads only B-E.

## Key build
`scripts/build_key.py` aligns the groups of B, C, D, E with the decipherments of the time
(`plaintext/training_cribs.tsv`) and writes `key/code15_key_v1.tsv`. It does not open A or its crib.

## Freeze and timestamp
`plan/MANIFEST.txt` lists SHA-256 of this protocol, the key, the transcription, both crib files and the two scripts.
Only the SHA-256 of MANIFEST.txt is sent to the FreeTSA time-stamping service (https://freetsa.org/tsr, RFC 3161),
with `openssl ts -query -data plan/MANIFEST.txt -sha256 -cert`; the .tsq and .tsr are kept in `plan/` and verified with
`openssl ts -verify` against FreeTSA's CA certificate before the single run of `scripts/heldout_test.py`.

## Measure (run once)
`scripts/heldout_test.py` aligns A's 72 groups with the crib, the key fixed. A group's piece of the crib is part of
one word, a whole word, or two whole words. A group with a key value scores 1 if its value equals its piece (a
group written with "=" also matches value + "s"/"es"; with "+" or "x" also value + "ed"/"d"); the alignment that
gives the most matches is taken. Figures: k = matches; n = groups of A that have a key value; precision k/n;
coverage k/72.
Controls: 1,000 keys made by shuffling the values among the key's groups (random seed 1793), each measured the same
way. p = (1 + number of shuffled keys with at least k matches) / 1001.

## Pass bar
Pass if precision >= 0.80 and p <= 0.01. A miss is reported first and does not by itself rule the key out.
No change to the key, the transcription or the script after the timestamp; any later round is labelled as such.
