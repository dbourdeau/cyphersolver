# Ferdinand the Catholic → Jerónimo de Vich (Rome), Pedrezuela, 26 October 1515 (AHN Estado 8715 N.73)

Split on 14 Oct 2026 from `targets/vich1511/` under the one-key rule (George Lasry, 14 Oct 2026). The letters of
1511-12 to Vich (N.45, N.57, N.60) are in another cipher, the 1511-12 nomenclator, and stay in `targets/vich1511/`
(vich1511.html): a different cipher, with its own page. This entry is N.73 alone.

**Outcome: not solved (attempted).** Transcribed in full; no key found.

PARES: AHN Estado 8715 N.73, id 12751418 (4 images). Images are not committed; they are in the main checkout under
`targets/vich1511/img/n73_*.jpg` and the line strips under `targets/vich1511/lines/` (re-fetch with
`python ../vich1511/pares.py img 12751418 n73`).

## The letter and its cipher

`n73_transcription.txt` (124 lines, 3,177 tokens, 197 distinct) and `n73_freq.txt`. It is a different
system from the 1511-12 key: mostly three-letter code groups (`sin` 151, `sud` 97, `no` 93, `zre` 89, `xed` 68)
with a smaller set of signs (`X` 171, `TH` 170, `PHI` 163, `RH` 151). No deciphered sibling exists for it:
the nearest, N.74 of 1519, is Charles I's and is a third system (its `sex` = papa, `mod` = tiene,
`sin` = de). Its clear text: docket "a 26 de octubre 1515", opening "videlicet iterum", ending
"en Pedrezuela a xxvj de otubre de dxv".

## What was tried (18 Sept 2026)

Annealing against the repo's Spanish 5-gram model (`solve73.py`, `solve73g.py`; they read `../esp318/lm_tabs.pkl`)
with the lowercase groups split into letters, as whole units, and as context breaks around symbol runs. All gave
about -2.7 to -3.5 per character with seeds disagreeing: no solution. Symbol runs are short (median 3), so there is
little for an n-gram model to hold onto; this one needs a crib or a sibling.

The 1511-12 nomenclator (`../vich1511/decode.py`), the N.74 system and the N.79 "Clave de cifra" table were compared:
none fits.

## Remaining gaps
- N.73 (26 Oct 1515, 3,177 tokens) - blocker: no-key-material; different system, no deciphered sibling (N.74 is a third system); annealing with Spanish 5-grams failed

## Escalation
- [x] siblings: the Vich ciphered letters on PARES (8714 N.12, N.26, N.39; 8715 N.41-N.79) sorted; none of the deciphered ones is in this key
- [x] clear-pages: the four images carry only the docket, the clear opening and the dateline
- [x] known-keys: the 1511-12 nomenclator, the N.74 (1519) system and the N.79 table compared; none fits
- [x] print: Terrateig, Política en Italia del Rey Católico (1963) vol. II prints Ferdinand's letters to Vich, but is not online; snippet and web searches (18 Sept, 5 Oct 2026) found no text of this letter
- [n/a] key-rebuild: no key material to extend; ciphertext-only annealing did not converge
- [n/a] retry: there is no partial key to re-run
