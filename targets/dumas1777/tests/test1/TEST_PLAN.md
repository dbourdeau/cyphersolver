# Test plan: Dumas numeric cipher, held-out check of a gloss-built key

Material: NARA file unit 464815090 (M332 roll 2), images 0009, 0010, 0013 (training), 0020 (held out).
Transcriptions: `pairs.tsv` (page, line, number, gloss as seen, confidence h/m/l, note).
Gloss "-" = no gloss seen over the number; such pairs are excluded from key building and from scoring.

Hypothesis under test: each number stands for one letter, and the same number always stands for the
same letter (a fixed number -> letter table, e.g. positions in a key text). If this is right, a key built
from pages 0009/0010/0013 should reproduce the contemporary gloss on page 0020 for every 0020 number it covers.

Procedure (script `heldout_test.py`):
1. Build key from all pairs with page != 0020 and gloss != "-": number -> majority gloss
   (ties/conflicts listed). Write `key_frozen.json`; record its sha256 below BEFORE decoding 0020.
2. Decode the 0020 numbers with the frozen key. Score = matches / (0020 pairs whose number is in the key).
   Also report coverage = covered / all scorable 0020 pairs.
3. Null: 200 keys made by shuffling the frozen key's values among its numbers (seed 20261114);
   score each the same way. Report real score, null mean/max, and the empirical p (share of shuffles >= real).
4. Pass criterion stated in advance: real agreement >= 85% with coverage >= 40%, and above the maximum of
   the 200 shuffles. Disagreements are listed and checked on the image (transcription error vs real conflict).

Frozen key sha256: `5e5fc9cc76f77598c6f7f15d56d3c26baa4c4c5dbf33c3929812177dc9fb1abd` (342 numbers; written before 0020 was decoded)
