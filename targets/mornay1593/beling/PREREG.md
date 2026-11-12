# Pre-registration: mornay1593, the folded 1593 key on the 1595-97 figures

Written 11 Nov 2026, before any test script exists and before the vols. 7-8 figures are transcribed.

## Disclosure: one look before this file
Before writing this, a rough count was run of how many of the 1595-97 numeric groups the 1593 key can parse (one key
number, or two key numbers split anywhere). It gave about 74 of 106 (Loménie file) and 60 of 98 (1597 file), counting
the name code N1 and the editor-printed letters loosely. No decryption was printed and no language score was computed.
The thresholds below are the house ones and were not adjusted after that count.

## Frozen key
`key/key_dudout.tsv` = the repo's `targets/mornay1593/key_dudout.tsv` (origin/main 4337f026) copied unchanged,
sha256 ef07fbeeb1343a2c96dd32acab1d6c0dc4a03a015592f558b5b13bef7ffd6349. 19 numbers → letters: a 2, c-m on odd 5-21,
n-u on even 22-8, x 44. Nothing is added or changed. Brice Dudout built it on the 1593 passages only, so the 1595-97
figures were not used to make it.

## Held-out material
A (primary). The repo's transcriptions, copied unchanged into `transcription/repo/`:
- `lomenie1595.txt` (sha256 69f77bb7…): passages L1-L15 and D1. N1 (a single name code) is left out.
- `duplessis1597.txt` (sha256 23062f6d…): passages C1-C8 and W1-W3, numeric groups only; the letters the editors printed
  among the figures (e, v, tr) are left out.

B (secondary, reported separately). Figures in vols. 7-8 not in the repo, transcribed from the archive.org page images
into `transcription/v7v8_figures.tsv` (figures only) with the clear words around them in `transcription/v7v8_context.tsv`.
Both are hashed into `results/frozen_inputs.sha256` before `scripts/test_folded.py` exists.

Control (not a test). The repo's 1593 `ciphertext.txt` (sha256 5874db87…), on which the key was built. The same script
must give the key full coverage and a clear language score there, or the method is broken.

## Parse
A group is read if it is one key number, or two key numbers when split at any point (no part may start with 0), as
in the repo's `apply_dudout.py`. When a group has several readings the whole-number reading is taken, else the
first split from the left.

## Score 1: coverage (the pass/fail test)
S = groups read / numeric groups, over A.
Null: 200 shuffled keys, each the key's 19 letters put on 19 numbers drawn without replacement from 2-44 (the 1593
key's range), `random.Random(1593)`. Pass if S ≥ 0.85 and S − best shuffled ≥ 0.30. One run.

## Score 2: language (stated now, reported whatever it shows)
Letter trigram model, add-0.1 smoothing, built by the script from the OCR text of vol. 6 (archive.org
`mmoiresetcorre06morn_djvu.txt`, sha256 204906c7…, passed as an argument): lowercase, accents stripped, j→i, v→u,
a-z only, no spaces. Each passage's decryption is cut at unread groups; each piece is scored separately; L = mean
log-prob per letter over all pieces. Null: 200 keys made by permuting the key's letters over its own 19 numbers
(`random.Random(1593)`), same parse. Language sign if the key beats at least 190 of the 200.

## Verdict rule
Fits: Score 1 passes and Score 2 shows a language sign. Does not fit: Score 1 fails and no language sign.
Anything else: inconclusive. B gets the same two scores, reported alongside, and does not change the verdict on A.

## Not tested here (exploratory, labelled so)
Variants of the fold (the same key with every number shifted by a constant c, c = 1-100) may be scanned afterwards
for coverage and language score. That is a search over 100 keys, so its best result carries no pass/fail and is
reported only as a lead.

## Addendum 1 (11 Nov 2026, before the vols. 7-8 figures are transcribed and before any script exists)

While locating the vols. 7-8 figures, two of the letters turned out to be **from Madame de Rohan to Madame Duplessis**:
vol. 7 LXXXII (Feb 1597, figures on p. 169) and CXLI (Aug 1597, figures on pp. 306-307). The repo's Rohan 1594 key
(`rohan1594_key.tsv`, built from the decipherment printed in vol. 6 LVI, same writer and recipient) was tried only on
Loménie 1595 and Duplessis 1597, never on Rohan's own later letters. Seen so far: the p. 169 image (two runs,
12 groups); while reading it the agent noticed that 12, 55, 59 and 91 have values in the Rohan key. No decryption or
score was made.

Second test, the Rohan 1594 key on the Rohan 1597 figures:
- Frozen key: `key/rohan1594_key.tsv` = the repo file copied unchanged (sha256 recorded in `results/frozen_inputs.sha256`).
  Only single-letter and syllable values are used for scoring; word and name values (pour, de, le roy, Paris ...) are
  kept in the mechanical output but count as read, not scored by the language model.
- Material: every Rohan 1597 group in `transcription/v7v8_figures.tsv` (passages marked writer = Rohan). Single numbers,
  no splitting (the 1594 system has values above 100).
- Score 1: coverage = groups with a value / groups. Reported; no pass threshold, because the 1594 key holds only the
  78 values one letter happened to use.
- Score 2: the language score of Score 2 above, over the letter and syllable values; null = 200 keys made by permuting
  the key's values over its own figures (`random.Random(1594)`). Language sign if the key beats at least 190 of 200.
- Verdict: fits if coverage ≥ 0.50 and a language sign; does not fit if coverage < 0.30 or no language sign;
  otherwise inconclusive. With fewer than 20 groups covered the test is reported as "too small" whatever it scores.
- The folded 1593 key is applied to these passages too (as part B) and the Rohan key to parts A and B (as a repeat of
  the repo's step 5); both reported, neither changes a verdict above.
