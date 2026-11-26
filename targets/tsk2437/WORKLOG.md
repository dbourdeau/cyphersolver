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

## 25 Nov 2026 (claude-sonnet-5-5): all remaining routes except contacting the PGP editor
- blind3 (pass 1, 218 marks, 57 unmerged labels) read against transcription.txt: inventory unstable (57 vs 36), no consensus run.
- Dash groups of transcription.txt: 31 groups, lengths 1-24, none repeats except the single stems I and ?; dashes do not behave as word breaks.
- Mirror test on crops of L7 (flip): no square-Hebrew forms; signs look like a rapid pseudo-script.
- attack.py --noword (he-tanakh not runnable here: no corpus copy in the worktree; ja-from-arabic): real fwd -2.393 / rev -2.363, nulls -2.488 sd 0.067, z 1.4 / 1.9; control separation only z 3.0: no signal.
- Siblings viewed (K5.7, K24.19, K24.23, K24.24, Misc.10.60, 11.91, 22.218, ENA 3207.17, CUL Or.1080 J277): none shares the K24.37 sign set; no sign table. Box K24 scan (PGP 32670-32708): only K24.19/23/24/37 are cipher leaves.
- Bohak 2010 and Bohak 2011 (charaktêres) not accessed (Anubis check, no PDF found). Not tested: Syriac/Coptic/Samaritan/Ibn Wahshiyya tables (none found).
- Result: no reading, no key, no identification.
