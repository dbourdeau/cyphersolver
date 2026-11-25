# idiaquez1577, images 1-2: four close calls checked on a blind shape plate (proposal)

The target is LcCompany/WAINUT's (PR #510, credit lccompany): transcription, key, reading, scripts and counts are
theirs. This folder records one check on their work and a patch that applies it. None of their files is changed by
this folder. The owners decide whether to take it, change it or decline it.

## How
The plate was built and scored by AI agents (Claude). Brice Dudout (human reviewer) answered it on 25 Nov 2026. It
asked about 10 places on images 1-2 that the folder's NOTES list as open or close calls. Each question showed one boxed
sign next to real examples of each candidate shape from the same hand, with no value or word shown. Three hidden
controls of known answer were mixed in, and all 3 passed. The selection rule and the integration rule were written and
hashed before the plate was built. An amendment tightened four frames after the first build and before any answer.
The PARES images were used privately: no image, crop or derivative is included. AI analysis was not raised with the
archive; the project's method was not presented to it at the time.

## Result
- "1 or 4" (agora, algun, negocio, averiguacion, alguno, castigo): 1 at all six places. 11 is confirmed, and nothing
  changes.
- Mark over 18 in *ordinario* (L02): a check (r), not a caret. The repair `{on/or}` goes, and the word is verbatim.
- Numeral of *fiesbo* (L04): 7, not 8. *Fiesco* is verbatim. That it means the Fieschi is still a reading from the
  sense.
- Mark over 33+ in *franceses* (L01) and *frances* (L16): a check at both places. The signs then give *frar-*, one r
  too many, and *fran-* comes from the sense only.

Count (folder's `scripts/reading.py`, unchanged): 173 -> 175 verbatim of 187 cipher words (92.5% -> 93.6%); repairs
3 -> 2, guesses 3 -> 4, holes 8 -> 6. Four words change, and no verbatim word is lost. `check_marks.py` passes.
`heldout.py` gives 0.980 characters / 0.926 words, against 0.970 / 0.910 before. Under 95%: still read in part.

**Departure from our own rule.** The hashed rule said that with a check, *frar-* stays a hole. The patch counts both
places as guesses (`[?fra=frar]`) instead, since the sign is no longer outside the key. This is the owners' choice. Kept as holes, the count is 175 verbatim, 2 repaired, 2
guesses and 8 holes, so nothing verbatim is lost either way.

## Applying the patch
From the repository root: `git apply -p1 --directory=targets targets/idiaquez1577/dudout/idiaquez1577-planche-2511.patch`.
It was made against 830c060074. `targets/idiaquez1577` has not changed since then, and the patch applies cleanly
to `main` at b81c613843. LcCompany/WAINUT can apply it, or Daniel can apply it on their request. It touches the
transcription (4 signs and a dated comment), the decryption, the marked text, the reading, the translation, NOTES,
profile.json and heldout_result.txt.

## Files
- `PROPOSAL.md`: the proposal, with the table of answers and changes.
- `idiaquez1577-planche-2511.patch`: the patch above.
- `RECOMPTE.md`: the word-by-word recount (in French).
- `sign_check_2511/`: the selection rule and its amendment (in French; the `.sha256` files check), the answers
  (`answers-2511-idiaquez.json`) and their meaning in English (`results.tsv`).
- `SHA256SUMS`: hashes of the files in this folder.

Open: images 3-6 are not transcribed yet. Other words there with the 1/4 shape, or with a check over 33, can test
these answers.

Brice Dudout (with Claude)
