# Test plan: verification of the key RALLY TO THE FRONT on vol. 11 fr. 0046, lower left (11 April 1865, Surget to Maury)

Written 15 Nov 2026 by the verifier (Claude, Opus) BEFORE any decryption of the helpers' texts and before opening the
key-search folder beyond its file list. The verifier knows the claimed key and plaintext from the brief, so is not
blind; the two transcriptions below are blind (helpers told nothing about key or plaintext). One run.

## Inputs (frozen by the helpers; hashes copied into `FROZEN_inputs.sha256` here)
- Helper A: `helperA/transcription.tsv` sha256 070b1296...9bca, frozen 15:41:21 UTC.
- Helper B: `helperB/transcription.tsv` sha256 d25f5bf7...5593, frozen 15:39:27 UTC.
- Only the column `first` (first-choice letter) is decrypted. The column `alts` is used only in the letter-change count.

## Rule
Ordinary Vigenère, plain = cipher - key (mod 26), key RALLYTOTHEFRONT (15 letters), key letter 1 applied to the
first cipher letter, advancing by one for every cipher letter only (clear words and dashes do not advance it).

## Groups
Both helpers counted 22 dash-separated groups and noted that three line-end joins (no dash either side) could be
splits, giving 25. The brief's pass mark is stated on 25 groups. Two counts are therefore made, both decided in advance:
- G22: the helpers' own 22 groups.
- G25: the same with the three line-end joins split where each helper put the line break (its notes).
A group "is an English word exactly" if its decryption, lower-cased, is a line of `/usr/share/dict/words`
(Webster's Second, 235,976 entries; it contains single letters). No two-word groups, no fuzzy matching.

## Pass mark (written now)
PASS only if all of:
1. G25: at least 17 of 25 groups are words, on helper A's text AND on helper B's text (the brief's mark);
2. G22: at least 15 of 22 groups are words (the same share, 68%), on both texts;
3. every control below scores lower than BOTH helpers' scores, on each count (G25 and G22) separately.
A miss on any of these is reported as a miss.

## Controls
- 400 random 15-letter English-like keys: words drawn uniformly from `/usr/share/dict/words` (alphabetic, length
  2 to 8), concatenated and cut at 15 letters; Python `random.Random(20261115)`; the same 400 keys for both helpers;
  key start at the first cipher letter (same rule).
- The four known keys COMPLETEVICTORY, COMERETRIBUTION, MANCHESTERBLUFF, OURNAVYOURPRIDE at every starting offset
  (15, 15, 15, 14 offsets: 59 controls), stricter than the stated rule alone; the offset-0 scores are also listed.

## Letter changes
Claimed plaintext (from the brief, 107 letters):
EXACTLYHOWLONGYOUWILLHOLDTHECITY RUNNINGOFTHETRAINSDEPENDS HOLDONUNTILNINEOCLOCKTOMORROW ADDITIONALTRAINSTHERE.
For each helper: list every cipher position where the first-choice decryption differs from it; for each, the cipher
letter the claimed plaintext needs, and whether that letter is in the helper's `alts` for that position (yes / no).
Report counts: total changes; changes covered by the helper's alternatives; changes not covered.

## Output
`results_verify.json` and `results_verify.txt` from `run_verify.py`; this plan's sha256 recorded in
`FROZEN_inputs.sha256` before the run.
