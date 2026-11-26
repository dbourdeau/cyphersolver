# Proposal for `targets/idiaquez1577` (catalogue 754, AGS Estado 1410,115), shape plate of 25 Nov 2026

For LcCompany / WAINUT (folder author, PR #510), copy Daniel Bourdeau. Sent with Brice Dudout's agreement.

## Credit

The transcription, the reading, the scripts and the word counts are LcCompany/WAINUT's work (PR #510, credit
lccompany). This proposal starts from their files as they stand on cyphersolver `main` (830c060074) and changes four
signs only. The key is unchanged (`key_frozen.tsv`, hash still matches).

## What was done

A shape plate of 10 places on images 1-2 that the folder's NOTES list as open or close calls, answered by a human
reader (Brice Dudout, 25 Nov 2026). Each question showed one boxed sign next to two real examples of each candidate
shape from the same hand, with no values or words shown. Three hidden controls of known answer (a bare 4 on img2 L09,
a caret over 4 on img2 L15, an 8 on img2 L12) were mixed in: 3 of 3 right. The selection rule and the integration
rule were written and hashed before the plate was built.

## Answers and changes

| place (folder's line) | question | answer | change |
|---|---|---|---|
| L12 agora, L15 algun, L21 negocio, L24 averiguacion, L04 alguno, L25 castigo | 1 or 4 ("upright 1 + crossed stroke") | 1, all six | none: 11 confirmed, as the blind review had it |
| L02 ordinario (mark over 18) | caret or check | check | `18^` -> `18v`: *or*, the repair `{on/or}` goes, verbatim |
| L01, L16 frances(es) (mark over 33+) | caret or check | check, both | `33+%` -> `33+v` |
| L04 fiesbo (numeral) | 8 or 7 | 7 | `8e` -> `7e`: *fiesco*, verbatim |

The mark over 33+ is the case to look at: with check = r the signs give *frarnceses* / *frarnces*, one r too many.
We now count both as guesses (`[?fra=frar]`) rather than holes, since the sign is no longer outside the key; *fran-*
is from the sense only (probable). If you prefer to keep them as holes until the check over 33+ is explained, the
count below loses nothing verbatim.

## Count (your `scripts/reading.py`, unchanged)

- Before: 187 cipher words, 173 verbatim (92.5%), 3 repaired, 3 guesses, 8 holes.
- After: 187 cipher words, 175 verbatim (93.6%), 2 repaired, 4 guesses, 6 holes.
- Word by word: four words change (ordinario repair -> verbatim, Fiesco guess -> verbatim, franceses and frances
  hole -> guess). No other word changes text or class; no verbatim word is lost.
- `check_marks.py` passes (decryption rebuilt, identical); `heldout.py`: 0.980 characters / 0.926 words (was
  0.970 / 0.910), 200 controls at most 0.933 / 0.754. `docs/_check_reading.py` not rerun.
- That *Fiesco* means the Fieschi stays a reading from the sense; only the word is now verbatim.

## Files

Patch against `targets/idiaquez1577` at 830c060074: transcription (4 signs + a dated comment), decryption, marked
text, reading, translation (brackets off *Fiesco*), NOTES (marked places, figures, a "Shape plate" section),
profile (note and guesses), heldout_result. No image is included; the plate used PARES images privately only.

Images 3-6 remain untranscribed; other words with the 1/4 shape and with a check over 33 there can test these answers.
