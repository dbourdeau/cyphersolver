# Project check of issue #370 (10 Nov 2026)

- `verify.py` was written from the system as described in the issue (5 x 6 table, N x N square, column order and
  row direction per message), without running or copying the contributor's `src/decrypt.py`.
- Run on the contributor's `ciphertext_451.txt` (1,600 digits) and `ciphertext_523.txt` (575 digits), it gives the
  two texts in `decryption_451.txt` and `decryption_523.txt`, identical pair for pair to the `value` column of
  `reading_451.tsv` and `reading_523.tsv` (off-table pairs shown as [nn] in both).
- The `status` columns count 750 of 764 pairs read in Nr 451 and 279 of 288 in Nr 523: 1,029 of 1,052, 97.8%.
- The Russian was read through as sentences here; the contributor's English translation matches it.
- Not done: no image was compared (the NARA catalogue, `catalog.archives.gov`, is refused by this machine's proxy);
  the contributor's control (`src/control.py`, needs `wordfreq`) was not re-run; `docs/_validate.py` has no Russian
  model.
