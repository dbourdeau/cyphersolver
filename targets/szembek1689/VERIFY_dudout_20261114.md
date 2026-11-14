# szembek1689: independent check of the key (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py targets/szembek1689` reads only `key.tsv` and the token column of `runs.tsv`, and compares each
decoded run with the gloss column. It does not use `decode.py`.

- Tokens: 436 two-digit signs (one doubtful, `12?` in intricavit), 1 struck single digit (`2?`), 2 code groups = 439, the
  count of `ct.txt`.
- With u/v and ae/e taken as equal, 60 of 70 runs give the gloss letter for letter. The 10 others: code groups 203 (glossed
  Literis) and 202 (no gloss), and the eight slips listed in NOTES.md (gerant/gerent, solicitaverant/sollicitaverant,
  Gegenbeio, Gegenbeii, functsm, pricipem, defunct, audi2?et). The doubtful `12?` gives u, so intricavit reads.
- Key correction: none. Every number keeps one letter; the "other letters seen" column of key.tsv (17 e x1, 21 u x1)
  is the gerant and functsm slips.
- Read bar (README): `research/reading_audit/v10_relabel.measure` on `reading.md` gives 0.986 over 778 words, the recorded value.
- Not done: the WBC scans are behind a proof-of-work page; they were not fetched or re-read.
