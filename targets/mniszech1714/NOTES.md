# Józef Mniszech to Jakub Dunin, Dukla, 18 March 1714 (DECODE R7524)

Status: attempted, not solved — 0 of 232 cipher figures deciphered; a separate numerical system, no key found, the solver fails its matched control at this length.

Split on 14 Oct 2026 from `potocka1714` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter was
filed with Barbara Potocka's nine letters to the same recipient; it uses another cipher. Potocka's letters, read with the
alphabet recovered from her Polish postscript, are [`targets/potocka1714/`](../potocka1714/NOTES.md) (a different
cipher, with its own page). The work below was done in the potocka1714 sessions of 23 Sept and 5 Oct 2026 and is
carried over from its NOTES (items 5, 6 and 9 there); the files moved here on 14 Oct 2026.

Work date: 2026-09-23. Catalogue item 280, class C (the catalogue entry has held this letter only since the Potocka letters were read).

## The document

Archiwum Narodowe w Krakowie, Archiwum Sanguszków, ASang_teka_290/6; DECODE R7524
(https://de-crypt.org/decrypt-web/RecordsView/7524), metadata in `R7524.json`. Three images,
`IMG_R7524_I33989_P1/P2/P3.jpg`, git-ignored, in the main checkout's `targets/potocka1714/` (shared source folder, not
moved). Sender on DECODE: "Mniszech J[ózef] - m[arszałek] w[ielki] k[oronny]", Grand Marshal of the Crown; receiver
"Dunin Jakub - regent koronny". The heading on P1 reads *18 marty 1714, w Dukli*; DECODE has 16 March 1714 and
cleartext language Polish. The letter opens with eight lines of clear Polish, then
alternates cipher words with clear Polish and Latin ones (*spraktykowawszy*, *praetextu consilii*, *congressow*,
*generaliter*, *unanimi voto*, *Rempublicam*, *iest plus quam certum*, *correspondencye*, *tractantur*).

## Transcription

- `r7524-cipher.txt` (23 Sept 2026): the 232 figures with the clear anchors, word division lost.
- `R7524-tokens.txt`: the bare 232 figures (written by the old potocka1714 `prepare_reading.py`; now a static file).
- `r7524-words.txt` (5 Oct 2026, re-read at full resolution from P1 and the P3 spread): the writer's word division
  kept, dots inside a word, a gap between words, "=" at a line break joined. 53 cipher words, 232 figures, 77 distinct
  (measured 14 Oct 2026). One-figure words 12, 38, 56, 133; doubled figures 12.19.19.118 and 27.28.28.119.31.125;
  repeated words 22.118.82.36.31.81(.17.68) x4, 36.31.157.31.33.81.15.20 x2 (once with a prefixed 110), 144.76.144 x2.
  The clear word first filed as *[Starosty horodly]* is *spraktykowawszy*.
- **Discrepancy found 14 Oct 2026:** the flat files read 30 at figures 46 and 201 where `r7524-words.txt` reads 36.
  On P1, figure 46 (in 110.109.127.36) has the looped 6 of the other 36s, so the words file is right there; figure 201
  not yet re-checked. The solver runs of 23 Sept used the flat file. Counts (232 / 77) are the same either way.

## Method and work log

1. (23 Sept 2026) Polish quintgram homophonic annealing (`solve_mniszech.py`), a tentative *hetmanow* crib
   (`solve_mniszech_crib.py`), a hypothetical null 33 with ch=130 (`solve_mniszech_null.py`) and a unigram-regularized
   search (`solve_mniszech_regularized.py`): no coherent reading (`r7524-*-result.txt`). The crib values are not
   recovered key material.
2. (23 Sept 2026) Matched control (`solve_control.py`, `control-*.txt`): a synthetic Polish homophonic text of the same
   232-token length and comparable alphabet (75 signs) was recovered to only 49/232 positions (21.1%). The failures on
   the letter are therefore **inconclusive**: the solver is inadequate at this length/alphabet ratio.
3. (23 Sept 2026) Key records in the Sanguszko catalogue: R7515 (a=5/10/15, two series), R7460 and R7461 (graphic signs).
   None fits.
4. (5 Oct 2026) `solve_r7524_words.py`: homophonic annealing scored with word boundaries on pl-modern and on a period
   model built from Pasek's memoirs (Wikisource, 0.65 MB, kept in that session's scratchpad, not in `lang/`) plus
   Gutenberg Polish; with and without the cribs *hetmanow* and 15.20 = *-ie*. No convergence.
5. (5 Oct 2026) `solve_r7524_dict.py`: dictionary-word annealing (49k words, char-model fallback) puts 34-36 of the 53
   words in the dictionary, but every restart gives a different key: underdetermined at 232 figures / 77 signs.
6. (5 Oct 2026) Potocka's own design (base 14-39, homophone = 2x base, `targets/potocka1714/key-potocka.json`) shifted
   -40..40 or scaled x1-x4: fits nothing.
7. (14 Oct 2026) Split from potocka1714; transcription files compared (above). No new attack.

No result is accepted. The figures run 12-157 with 77 distinct values in 232 tokens, and the repeated word shapes
suggest a homophonic letter cipher with word division kept, but that design is not established.

## Prior work

No decipherment found in print or online (searches of 23 Sept 2026 for the correspondents, the shelfmark and cipher
terms). The archive unit 29/637/0/1.3/9477 lists further Dunin correspondence of 1713-1718 without scans. Prior
solution: unknown, not asserted absent.

## Remaining gaps
- R7524, all 232 cipher figures — blocker: no-key-material; 77 signs, word-divided (r7524-words.txt); no matching key or plaintext located; flat, word-boundary and dictionary-word annealing do not converge and the matched control fails at this length; not declared impossible.

## Escalation
- [x] siblings: the nine Potocka letters to Dunin (potocka1714) are another cipher; cached Sanguszko records searched for Mniszech/Dunin; further correspondence catalogued without online scans.
- [x] clear-pages: all three images reviewed; the clear Polish and Latin words are context, not a decipherment.
- [x] known-keys: R7515, R7460, R7461 ruled out; Potocka's alphabet shifted and scaled, no fit.
- [x] print: Polish and French searches for the correspondents, shelfmark and cipher terms; no decipherment.
- [x] key-rebuild: flat, crib, null, regularized, word-boundary, period-model and dictionary-word annealing (23 Sept, 5 Oct 2026); matched control fails.
- [x] retry: re-transcribed at full resolution with word division (5 Oct 2026); the attacks above rerun on it.

## Next

A solver that recovers a 232-token homophonic control (word boundaries, a period Polish model), or more of
Mniszech's cipher correspondence from 1714 (the Grand Marshal's letters in the Sanguszko and other archives).
Re-check figure 201 on the P3 spread before the next attack.
