# Addendum to the verification plan: blind E/F tick check (written before the run, 15 Nov 2026)

Why: on the run of `TEST_PLAN_verify.md` both blind helpers read E at all 14 E/F-like letters (no F at all); the key
needs F at six of them (cipher letters 12, 16, 34, 64, 76, 81) and E at eight (6, 21, 60, 68, 75, 79, 96, 107).
On my own crops (`mine/sheet_E_ok.jpg`, `mine/sheet_E_needF.jpg`, `mine/g_emeo.jpg`) the clerk's E seemed to carry a
separate short tick at the lower right of the base, which the six "F" letters lacked. I saw this AFTER knowing the
key, so it is tested blind:

- 14 tiles, one letter each, shuffled (`tiles.py`, `random.Random(7)`), named T01-T14 in `tickcheck/`; the mapping
  is in `tick_key.tsv` (sha256 3c706c04...40e7), not given to the helper.
- A new Opus helper, told nothing about keys, plaintext, which letters are expected, or my observation, classifies
  each tile: separate lower-right tick or stroke present / absent / unclear; and its first-choice letter E or F.
- Prediction from the key: tick present on the 8 E letters, absent on the 6 F letters.
- Mark: at least 12 of 14 tiles classified as predicted (unclear counts as a miss) supports the six E-to-F
  corrections as readings of the strokes; fewer is a miss and the six stay "not settled on the image".
