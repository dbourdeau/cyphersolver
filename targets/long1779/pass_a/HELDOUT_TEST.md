# Held-out test, written before the held-out pages were read (13 Nov 2026)

Key: key_frozen.json (sha256 in key_frozen.sha256), built only from images 11, 13R, 14L, 14R (29 Jul - 22 Aug 1779).
Held-out text: the cipher words of images 15L, 15R, 16L, 16R and 17L (26 Aug - 6 Oct 1779), about the last third of the
1779 cipher. Procedure: transcribe each held-out cipher word as glyph labels first (heldout_glyphs.txt), then decode it with
the frozen key without changing the key. Statistic: share of held-out cipher words (length >= 2) whose decoding is an English
word in the repository lexicon (lang/lexicons/en.json.gz) or a short list of period spellings recorded in the notes.
Null: the same statistic for 200 keys made by shuffling the frozen key's letter values among its glyphs (seed 1779).
Pass: frozen-key share above the 99th percentile of the shuffled shares.
