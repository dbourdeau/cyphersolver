# Pre-registration: sande1660 cipher A, scan m0271 as a held-out test of the key in key.txt

Written 11 Nov 2026 before any transcription file, script or score for m0271 exists.

## Why this test
The letter key of cipher A (`../key.txt`) was recovered by WAINUT from about 45 transcribed lines (m0265, m0266,
m0268, m0269, m0273). m0271 is a full page of cipher (about 38 lines) that no one has transcribed: NOTES.md lists
it under "Remaining gaps" (not-attempted). It was not used to build the key, so it can test it.

## Frozen key and inputs
- `key/key.txt` = the repo's `targets/sande1660/key.txt` at origin/main 4337f026, copied unchanged,
  sha256 f4974639ebc9ab0a9f14854a3047dd30ca710775c54885d83b6f8e19a780d4a0. The script reads its letter table
  (numbers 1-41 → letters, homophones included: 26 numbers). No value is added or changed.
- `key/transcription_build.txt` = the repo's `transcription.txt` (the lines the key was built and checked on),
  sha256 3e9999cada6d2748d4f7cfc29dbc4a850457b9bfcddb0b8212e7dbe0944b067e. Used only to calibrate the threshold.
- `lexicon/pt.json.gz` = the repo's `lang/lexicons/pt.json.gz` (the Portuguese word list `docs/_check_reading.py`
  uses), sha256 a1127215d8f32b180e61e15706ea2cc1b9a54151f05a134d6aaccf7c1f438ccb.

## Held-out material
Every cipher line of m0271 (DigitArq file PT-TT-LMP-0001_m0271.jpg), transcribed from the image as numbers in
`transcription/m0271.txt`, one line of the page per line of the file. The transcriber knows the key table (it is in
the repo), so the transcription is blind only in the sense that no decryption of m0271 is run or written before the
file is hashed. Word gaps on this page are not reliable, so the test does not use them. Signs not read are `?`.
Hash the file into `results/frozen_inputs.sha256` before `scripts/test_m0271.py` exists.

## Score
Decrypt with the frozen key to one unspaced string per line. Numbers of 60 and up (code groups) and `?` break the
string and are not counted. A number below 60 that the key does not cover counts as one letter that cannot be covered.
Normalise both the decrypt and the lexicon the same way: lowercase, accents stripped (ç → c), then c before e/i → s,
ç and z → s, h dropped, j and y → i, v → u, doubled letters made single.
Coverage = share of decrypted letters that fall inside lexicon words of 3 letters or more, in the parse of each line
that covers the most letters (dynamic programming; shorter words are allowed in the parse but cover nothing).

- S_held = coverage of m0271 under the frozen key.
- S_build = coverage of `key/transcription_build.txt` under the same key and the same rule (word gaps ignored there too).
- Null: 200 keys made by permuting the key's 26 letter values over its 26 numbers (random.Random(1660)); S of m0271
  under each.

Pass if S_held ≥ 0.85 × S_build (m0271 reads at least 85% as well as the lines the key was built on) and
S_held − best shuffled ≥ 0.30. One run. If m0271 yields fewer than 600 decrypted letters, the result is reported as
"too small" whatever it scores.

## Not part of the test
The reading of m0271 as sentences, the code groups, and any other page transcribed in this session (m0272 etc.) are
a reading, checked by eye, and are reported separately.
