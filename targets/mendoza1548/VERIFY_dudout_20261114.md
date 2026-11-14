# mendoza1548: independent decode and read-bar recount (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/mendoza1548` reads only `key_1548.md` (the "value used" column), the two dotted-sign
rules stated in the notes (`ꝺ .` que/da, `e .` lo) and `transcription/d1_transcription.md`; it does not use
`dec1548.py`. 702 tokens, 10 without a value, 178 with two values, as in NOTES. Its decode agrees with
`decryption/d1_decode.txt` on 691 of 692 items; the one difference is format only (`franceses` printed without brackets).

Against the letters of `decryption/d1_reading.md` (edit-distance alignment, best of each token's values):

| values allowed per token | reading letters outside `[ ]` given | inside `[ ]` |
|---|---|---|
| key value used (decode) | 838 / 915 (0.916) | 108 / 170 |
| + the 1548 gloss pairs (`key_pairs_gloss.txt`) | 864 / 915 (0.944) | 110 / 170 |
| + the crib pairs (`key_pairs_crib.txt`) | 896 / 915 (0.979) | 146 / 170 |

So about 51 unbracketed letters (5.6%, 41 places, listed by the script) come neither from the key's value nor from a
1548 gloss, only from the crib pairs aligned with the printed edition: mostly the vowel of a base sign whose mark is not
seen (`V` pu/pa, `ꝗ` da/do, `ÿʃ` vi/ve), as NOTES says ("chosen by context and checked against the edition"). They are
not errors, but they are not bracketed either. No key correction.

## Read bar (README)
The text entry is `state: "read"` with no `read_share`. It was written on 2 Nov 2026, after the 24 Oct v10 pass, so
the word bar was never applied to it; `fraction_read` 0.986 is the share of tokens with a value (692/702), not a share
of words. `research/reading_audit/v10_relabel.measure` on `decryption/d1_reading.md` gives **0.869** (205 words, 31
holes). The reading has 34 supplied words in brackets; `v2_score.holes` leaves the three capitalised ones
(`[Fernés]`, `[Monseñor]`, `[Que]`) as words, so counting all 34 gives 1 - 34/236 = **0.856**. Either way the letter is
under the 0.95 word bar and, by the README rule, *read in part*. The profile is not changed here; the class is left
to the maintainer.

## Not done
The BNE image was not fetched (the brackets were already re-read on it, NOTES step 8). MSS/7919/75 not seen.
