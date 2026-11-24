# SOLVE_LOG: cpp10a132 (24 Nov 2026, Brisbane)

All runs use TRAIN only (p75r lines 1-3 + p76r lines 1-21: 158 word groups, 709 letters). p76v was not loaded by
solve.py. Language model: `la-letters` from Cyphersolver `lang/` (Latin letters corpus, order 5, with spaces,
`latin` normalisation), loaded from a private copy of `lang/` at /home/claude/keyless/_cs (the shared checkout has
no `lang/` in its working tree; it was read out of git with `git archive HEAD lang`, the checkout was not touched).

| # | attempt | settings | result |
|---|---|---|---|
| 0 | By eye, during transcription | none | System recognised before any run: "qfs" = per, "bnfo" = amen, "tboubn" = santam: each letter replaced by its successor. Recorded in FREEZE_TX.txt as a limit on blindness. Not used as the key of record: the key below comes from runs 3 and 4. |
| 1 | `lm.load('la')` (default Latin model) | Gutenberg corpus fetch | FAILED: Gutenberg HTTP 503. Switched to `la-letters` (GitHub-hosted corpus), which built in 8 s. Sanity: Latin phrase -1.51, gibberish -7.67 per char. |
| 2 | Statistics | letter counts, index of coincidence | 20 different letters; a, j, l, v, w, z absent. IC 0.0783 (Latin about 0.072): monoalphabetic. Top letters f 94, b 73, s 66, k 64. |
| 3 | A. Shift test | every shift 1..n-1 in four alphabets: 23 letters (a-z less j, v, w), 24 (with v), 21 (no k, y), 26 modern; scored with la-letters | Best: shift back by 1, score -2.444 in the 23-, 24- and 26-letter alphabets (they differ only in letters the text does not use; the 23-letter Latin alphabet is taken as the simplest). 21-letter alphabet fails (k and y are used). Next best shift -5.746; worst -8.813. |
| 4 | B. Free substitution, no shift assumed | hill-climb with annealing acceptance, 20 cipher letters into a 21-letter plain set, 6 seeds (20261112, 7, 1, 2, 3, 4) x 8 restarts x 6,000 steps, la-letters | 27 of 48 restarts converge to the same key, score -2.444; the other 21 stall between -3.95 and -5.02 (failures, kept in solve_out.txt). The converged key is identical to the shift-by-one key in all 20 letters, including y>x and x>u. |
| 5 | Key frozen | KEY.tsv, FREEZE_KEY.txt | 20 letters from TRAIN; a, l, z filled by the rule and flagged (none of the three occurs anywhere in the text). S01 and S02 (scribal abbreviation strokes, once each) given no value. |
| 6 | One decode | decode_once.py | DECODE.txt, judge/decode.txt. 1,137 letters decoded: p75r 100 + p76r 609 + p76v 428 = 1,137. |
| 7 | Shuffle control | shuffle.py, 5,000 keys per seed, seeds 20261112 and 7, same model | see shuffle_out.txt: real key beats all 5,000 shuffles on every split, z about 10. |

Emendations: none. The decode is the first pass and the figure of record.
Not tried, because not needed: Italian models (the text decodes as Latin with Italianate spelling).
