# Judge notes: corsi1513 doc 627, blind decode vs contemporary decipherment

Inputs read (only): `../decode_once.txt` (L1-L5) and `wt_cv/targets/corsi1513/doc627/decipherment_627.txt`.
Rows are tallied against decode lines. Decipherment words that run across a decode line break are counted on the decode line that holds them.

## Rules applied
- One tag per decode unit (a letter, hole `_`, point `.`, `[nn]`, or code unit). Decipherment letters with no decode unit are tagged O.
- Holes and points: H, one per symbol. Where a hole stands for a syllable, the extra reference letters are tagged O (the strict choice).
- Extra decode letters that have no counterpart in the decipherment are tagged X.
- Expansions are compared in full (q[ue]llo = quello, p[er] = per, malignam[en]te). Struck-through `{della}` is left out. Spelling variants count the differing letters: mostro/monstro is an O on n, de/di is an X.
- Code units: `questo Re` given as `.` = H. `firenze` and `fiorentini` given as `mc` = X (a wrong value, not a hole). `65` given as `[63]` = H (unresolved).

## Judgement calls (each moves the score by one or two letters)
- L1 `e` vs `[Il]`: tagged X. `[Il]` is the transcriber's restoration under an ink blot. If the word is really `el`, this becomes M.
- L2 `intendo` vs `Intado[?]` (uncertain reading): tagged X2. If the page reads `intendo`, these become M.
- L2 `coe` after `mc`: 3 spurious letters, tagged X.
- L4 `pl.c__questo` vs `del popolo per quanto`: tagged as del O3, popolo p M, l M, `.` H, o O3, per c X, H2, quanto M4 X2. `popolo` may be a code word, but the decipherment does not mark it as one.
- L4 `_c_` vs `dipoi`: H2 X1 O2.

## Result (`python3 -I judge_count.py judge.tsv ../decode_once.txt`)
Block: M=203 X=25 H=18 O=16. Strict 203/262 = 77.5%. Accuracy on decoded letters 203/228 = 89.0%. The concatenation check passes on all 5 lines.
