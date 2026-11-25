# WORKLOG tsk2424 (24 Nov 2026, claude-sonnet-5-5)

- Merged the Geniza image sweep and the literature survey branches (COVERAGE.md and research/README.md conflicts: took main's copy, re-ran research/_index.py).
- Read both sweeps for K24.24 / K24.37; PGP pages 33913 and 32699 re-read (live, 24 Nov): descriptions as in the sweeps, entered by Elbaum 2021, no bibliography.
- Images: native tiles of both sides (fetch_images.py). Viewed recto in bands and line strips; verso plain Arabic.
- Tried a by-eye sign-level transcription: connected cursive and cross-line slashes made it unreliable; switched to the automatic stroke-level stream (glyphs.py).
- Line assignment: k-means on slope-corrected y (slope 0.02, k = 10) gave 25-33 glyph components per line; 30 shape clusters; exemplar sheets viewed (size-driven clusters).
- Added lang/ models he-tanakh (lang/build_he_tanakh.py, Sefaria API, 21,800 verses) and ja-from-arabic, norm schemes hebrew and ja in lang/lm.py.
- Attacks and controls: see NOTES.md table. Null result.
- Viewed K24.19 (Bohak family), NS J479 and J277 images for comparison. Zimam chart URLs from the Cambridge blog returned the site home page: chart not obtained.
- Not done: sign-level transcription, K24.23 and the PGP related document, Elbaum's J479 table, Bohak 2010 PDF.

## Second attempt (24 Nov 2026, later session): sign-level transcription
- Merged the first attempt, fetched both CUDL images again (only two images exist for the leaf), deskewed 1.15 degrees, flattened.
- Viewed every line at 2x in windows of 5-8 signs, wrote segments_a.json line by line (seg.py), class sheets (sheet.py), finalize.py -> transcription.txt, signs.tsv, cipher_tokens.txt.
- 228 signs, 42 classes, IC 0.0442; H(next|prev) z -4.1 (first attempt -0.4). Direction right to left from the aligned right line ends.
- Annealing with he-tanakh, ja-from-arabic, ar-mamluk (corpora via CYPHER_CORPUS_ROOTS pointing at the first attempt's worktree; PYTHONUTF8=1): no signal, controls z 4-5.
- Second reading not independent (same reader); lines 1 and 7 re-checked with cuts drawn.
