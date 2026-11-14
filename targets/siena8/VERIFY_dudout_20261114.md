# siena8: independent check of the key (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py targets/siena8` reads only `key.json` and `transcripts/no08.tok` (not `decode.py`).

- 4 runs, 166 signs, 23 distinct sign names: the counts of NOTES.md.
- The four decoded runs are identical to the `cipher:` lines of `texts/no08_decryption.txt`; sign 9 has three values
  (u/v/b) and is taken as u there (Biancha is written with 9).
- Key correction: none.
- Read bar (README): `v10_relabel.measure` on `texts/no08_reading.md` gives 1.0 over 41 words, as recorded.
- Not done: the image is DECODE's (R4797) and was not fetched.
