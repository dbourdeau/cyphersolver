# Letter-cipher (LC) words, 9 Sep 1640 (inv. 1134 scan 583), tested with an LC key from the 1643 letter (25 Nov 2026 UTC)

## Bottom line
- The LC is a simple (monoalphabetic) substitution of letters, with some digits used as extra signs in 1643 [derived]. Not a shift, Caesar or atbash.
- Key LC_KEY_v1: 12 cipher letters valued from the 1643 glosses only (b=e, c=i/j, d=n, e=s, f=p, g=d, k=r, l=h, m=t, r=a, t=o, u=c).
  Frozen 21:16:17 UTC (frozen/FREEZE_LC.txt, md5 a718f1df...), stamped (stamps_01_freeze-lc, sectigo/freetsa 21:16:17-18 GMT).
- 1640 held-out test, figure of record: 5/13 words = 38.46%. FAIL (bar 65%). Letters keyed 43/56 = 76.79%.
- Controls: key shuffles >= 5: 9/5,000 (seed 20261112), 12/5,000 (seed 7); letter shuffles >= 5: 96/5,000 and 118/5,000. Not significant.
- Three of the 5 'reads' are single letters (b->e, g->d, m->t), which the HTR wordlist accepts; so the true signal is 2 words (iohn, daer), and iohn was not blind.

## Per word (first pass; decode / verdict / 617 gloss read afterwards)
| LC word | decode | scorer | 617 interlinear gloss (post hoc, partly legible) |
|---|---|---|---|
| ctld | iohn | READ (not blind: guessed before freeze) | 'John' (agrees) |
| Gmroodt | dta??no | - | letters partly legible ('... a e e o n'?) |
| b | e | READ (single letter) | not legible |
| g | d | READ (single letter) | not legible |
| tpbk | o?er | - | 'over' (agrees; gives p = v) |
| lrdgenlm | hands?ht | - | 'hand...' (first letters agree; rest not legible) |
| grbk | daer | READ | 'daer'? (partly legible) |
| nad | ??n | - | not legible |
| m | t | READ (single letter) | not legible |
| bpbkdbsbd | e?erne?en | - | not legible |
| Zrpmb | ?a?te | - | 'Tauer..' ? (partly legible) |
| qbbm | ?eet | - | not legible |
| boode | e??ns | - | not legible |

## Emendations / post-hoc only (not the figure of record)
- From the 617 gloss: p = v (tpbk = over). With p = v: bpbkdbsbd -> e v e r n e ? e n; Zrpmb -> ? a v t e.
- The 617 copy writes some LC words differently from 583 (e.g. 'w. b.d.p.b.g' and 'q b / g m boocd'); a 617 transcription is owed.

## Verdict
- Second system identified and partly keyed (from 1643); 1640 LC words NOT read on the figure of record (38.46% < 65%, controls not clear).
- What would finish it: a full-resolution read of the 617 letter-by-letter gloss (or a better image), transcribed blind, giving more equations.
