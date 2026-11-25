# WORKLOG tsk2437 (24 Nov 2026, claude-sonnet-5-5)

- Images: native tiles of both sides (../tsk2424/fetch_images.py). Verso is a mirror ink offset of the recto lines.
- Ink map (segment attempt, background median 101 px, threshold 38) located the 8 lines; flattened crops (crop.py), two per line, viewed at 0.9x.
- First-pass shape-class transcription, 166 tokens; second look at lines 1, 6, 7.
- Statistics, annealing attacks and controls with ../tsk2424/analysis.py and attack.py: null result (NOTES.md table).
- Flip test of lines 6 and 7: inconclusive.
- Not done: sign-level transcription, Hebrew-letter candidate sets, raking-light images.

## Second attempt, 24 Nov 2026 (claude-sonnet-5-5): sign-level transcription

- Images: native recto refetched; CUDL has only pages 1r/1v (no other image). Tools: win.py, mkwin.py (windows with pixel ruler), contact.py/montage.py (class sheets), resolve.py (3.2x tiles).
- pass1.txt, pass2.txt (positioned, graded), diff.py, build_final.py -> final.txt, changes_from_pass2.txt, legend.txt, doubts.txt, transcription.txt, cipher_tokens.txt (tok.py, make_legend.py).
- Statistics and annealing re-run (NOTES.md): 209 signs, 36 classes, 98 firm / 72 likely / 39 doubtful; no language signal; direction probably right to left.
- Not done: blind third reading, Hebrew candidate sets per class.
