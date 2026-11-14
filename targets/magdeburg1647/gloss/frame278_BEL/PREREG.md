# Pre-registration: Osnabrück 1647 (catalogue 1639), held-out key test

Written 11 Nov 2026 before any key file was built or any script run.

## Material
- Key booklet, LASA A 1 Nr. 530, frame 0004 (two pages, symbol | cipher spelling | clear name).
- Transcription file `transcription/booklet_pairs.tsv`, cipher spellings recorded as seen, with fixed glyph rules:
  `2` -> z, `1`/dotless i -> i, the capital-W-like glyph -> m. g/q and c/o kept as seen (no correction from any key).
- Clear names normalised: lower case, ä/ö/ü -> a/o/u, v -> u, j -> i, spaces dropped.

## Key build (training = LEFT page only)
`scripts/build_key.py`: for every left-page pair whose cipher and clear have equal length, count position-wise
cipher-letter -> clear-letter votes; each cipher letter takes its majority value. Output `results/key.json`,
whose sha256 is written to `results/key.sha256` before the test runs.

## Held-out test (RIGHT page only, never used for the key)
`scripts/heldout_test.py`: decrypt each right-page cipher spelling with the frozen key (unknown letters -> `?`).
Score = matched characters (difflib SequenceMatcher matching blocks) / clear characters, pooled over all right-page pairs.
Null: 200 keys made by randomly permuting the frozen key's values over its cipher letters (seed 1647).
Pass if score >= 0.85 AND score - best shuffled >= 0.30. Anything else is reported as a fail, with the number.

One test, run once. Whatever it gives is recorded.
