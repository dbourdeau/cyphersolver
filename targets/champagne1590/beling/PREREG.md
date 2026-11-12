# Pre-registration: champagne1590, no. 24 interlinear glosses as a held-out check of Nevers key no. 25

Written 11 Nov 2026 before any transcription file, script or score for no. 24 exists.

## Finding that makes this possible
The two cipher runs of no. 24 (BnF fr. 3623 f. 37r, lines 8 and 22) carry small letters written above some figures by a
contemporary hand [seen on Gallica crops, 11 Nov]. The target's NOTES list glosses only on nos. 25 and 60, so the no. 24
glosses have not been used for anything in the repo: not for the bracketed alphabet, not for matching key no. 25.

## Frozen key
`key/key25.md` = the repo's `targets/champagne1590/texts/key25.md` (Brackx's transcription of fr. 3995 f. 51r) copied
unchanged, sha256 a88a36ac2b18901219c0c76850acc03873861b0928a724cfee091a945c03ed77. `scripts/key25.py` parses its
"Plaintext | Unbarred figures" table into figure → letter (u/v class = u); nulls and barred entries are not letters.
No value is added or changed.

## Held-out material
Every figure in no. 24's two runs that has a legible letter written above it. Order of work:
1. `transcription/n24_figures.tsv`: run, position, figure as seen (glosses ignored; barred or doubtful marked).
2. `transcription/n24_glosses.tsv`: run, position, gloss letter as seen ('' when none or illegible).
3. Hash both into `results/frozen_inputs.sha256` before `scripts/check_n24.py` exists.

## Score
Per-figure: for each glossed figure, 1 if key no. 25 gives the same letter as the gloss (u = v, i = j), else 0
(a figure the key does not cover counts 0). Score = matches / glossed figures.
Null: 200 keys made by permuting key no. 25's letter values over its figures (seed 1590). Pass if score ≥ 0.85 and
score − best shuffled ≥ 0.30. One run. If fewer than 8 figures carry legible glosses, the test is reported as
"too small" whatever it scores.

## Not tested here
The decryption of nos. 24 and 60 as a whole and the barred figures (22, 44, 51, 84) are a reading, checked by eye against
the key sheet, not part of this test.
