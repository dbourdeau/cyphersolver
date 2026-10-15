# A letter to Duke Wilhelm V of Bavaria, 12 June 1583, in a Latin-letter cipher (BayHStA KAA 4591 ff.274–277, DECODE R9424)

Split on 15 Oct 2026 from `targets/kaa4591/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 161
grouped fourteen ciphertexts of the Munich key volume KAA 4591 in at least six systems; this letter is in a cipher of
its own and is **attempted, not solved**. The other letters are different ciphers, each with its own page: System A′
([`targets/kaa4591/`](../kaa4591/NOTES.md)), Łaski's cipher ([`targets/kaa4591b/`](../kaa4591b/NOTES.md)), the Fulda note
([`targets/fulda1576/`](../fulda1576/NOTES.md)), R9367 ([`targets/r9367/`](../r9367/NOTES.md)), R9416
([`targets/r9416/`](../r9416/NOTES.md)) and R9319 ([`targets/r9319/`](../r9319/NOTES.md)). Work 21 Sept 2026 (Claude
Opus 5) as part of kaa4591; `r9424/` moved here unchanged; `signstream.py` added 15 Oct 2026. Catalogue entry 161 stays
open in `catalogue.json` for this record and R9319.

Images: DECODE, login; not public domain, kept untracked; the page shows none.

## The letter

German letter to Duke Wilhelm V, dated 12 June 1583 (the Cologne war). P1 (f.274r) opens in clear; the cipher runs
from line 8, in Latin minuscules with a few invented signs (ε, ∆, ʒ, a 2-like z, '/', a cross-mark), word-separated,
inside clear words ("Zwisch Ho. Fe.", "und Ni. sein"). Contemporary glosses stand over a few single groups on f.275r
(Hildesheim, Würzburg, Eichstätt, Freising). A nomenclator fragment shows on the facing leaf f.273v at the edge of the
photo: names with signs (Cöln = δ?, Wirtemberg = δδ?, Landgraf = φ). P2 (f.274v) is clear German only.
Transcription: `r9424/transcription.txt` (glyph by glyph); 913 cipher signs (`signstream.py` → `r9424/signs.txt`,
29 distinct).

## What was tried

- R9422 (the volume's 1582–83 key; its alphabet is cut off at a/b) does not read as transcribed; R9420 (1531 keys,
  a shift alphabet) and R9421 (tabula recta) checked.
- IoC 0.068, flat over periods 1–8: monoalphabetic, or a code.
- Constrained annealing with de-modern, then de-1500s, with and without '/' and nulls, and in Latin and Italian: no
  text. The glosses sit over single groups, so the cipher is probably partly code groups; with transcription noise and
  too few gloss cribs it does not open.

## Remaining gaps

- R9424, the whole cipher (913 signs) - blocker: no-key-material; R9422 alphabet cut at a/b and does not read as transcribed; R9420 (1531 keys, shift alphabet) and R9421 (tabula recta) checked; IoC 0.068 flat over periods 1–8 = monoalphabetic, yet annealing fails in German (de-1500s, with/without '/' and nulls), Latin and Italian — likely code groups (gloss names sit over single groups) plus transcription noise; gloss cribs too few.

## Escalation

- [x] siblings: R9419-R9423 key records of the volume opened; the f.273v nomenclator fragment noted
- [x] clear-pages: the glosses over names on f.275r used as cribs (too few)
- [x] known-keys: R9420, R9421, R9422 tried; none fits
- [x] print: web search for KAA 4591 ciphers found no edition
- [x] key-rebuild: annealing in German, Latin and Italian, with and without nulls (failed)
- [n/a] retry: no partial key to retry with; next would be a full re-transcription at zoom and the f.273v table read as a key

## Next

Re-transcribe the cipher at full zoom, read the f.273v nomenclator (only its right half is in the photo) and try it
as the key.
