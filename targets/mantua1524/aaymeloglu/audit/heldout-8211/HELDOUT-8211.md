# Held-out test of the Mantua 1524 key on new ciphertext in Vat. lat. 8211

Written 2026-11-16, before any cipher passage of Vat. lat. 8211 has been transcribed or decoded. Nobody in this work has decoded anything from 8211; the scan agent saw its cipher only as images and wrote no sign sequences.

## Frozen inputs
- **Key:** `key.json` as published in aaymeloglu/unsolved-ciphers `mantua-1524/key.json` (merged in b3a2126) and in the cyphersolver PR #716, sha256 f78de9d123bfb3f384acaa991d5bbaf5d63d4ba1db271c22a05d361a5b98b78e. No value is added or changed for this test. Units and merges as in `solve/lib6.py` DEFAULT_MERGE at that commit.
- **Passages:** chosen before transcription by the scan agent from Calandra's letters in Vat. lat. 8211 (Feb 1524 and after, frames from about 72): the longest cipher runs on legible frames, 2-4 letters, at least 300 cipher signs in total if available. Choice recorded in `heldout8211/PASSAGES.md` with frames and line numbers before transcription starts.
- **Transcription:** by the same transcriber agent as ff. 298, 68r, 198r, with its own sign labels (`signs.md`), from the images only. It has never seen key values, decodes or readings, and will not now. Clear text of each letter is transcribed too (context; it may enter the lexicon below, see there). The transcription is frozen (sha256 appended below) before decoding.

## One measurement
Same rules as `solve/RESERVED.md` (reserved-line scoring), applied to the new passages:
- word = one cipher segment (one TSV row of kind=cipher);
- lexicon = word types occurring at least twice in the cipherkit `it` corpus (same normalisation), plus every word of the clear text of ff. 298r-v, 68r, 198r and of the clear text of the 8211 letters transcribed for this test; no word read from any cipher decode is added;
- a segment containing a code sign or a sign with no value in the frozen key counts as a miss;
- null: `cipherkit.controls.permutation_z_key`, score = lexicon hit count, n = 200, seed 0.

Reported: hits over all segments (headline), hits among segments decoding to 4+ letters, z against the null, and the raw decode as is.

**Bar (set now): the key passes if the hit share over all segments is at least 0.40 and z is at least 5.** For scale only: the fitted reserved lines of 68r gave 0.61 (19/31) at z 8.8, and that figure had leakage. Whatever the result, it is reported.

Secondary, descriptive, after the measurement: a reader may then read the passages as Italian with the key (post hoc, not part of the test); any new value suggested by them is recorded separately and does not alter the headline.

## Frozen transcription
- `heldout8211/transcription-8211.tsv` sha256 da32665a7c611e0d64c44a5df7e60f733acb3000e11e4f3ff9f7a4ecb0bd96be (194 cipher rows, ~1250 signs over 72R 73L 74R 76R 78L 77B 77A; two blind readings merged, they agree exactly on 60 of 205 runs), frozen before decoding. Its check notes are `work/checkpass-8211.md`, `work/diff_8211.md`.

## Resolution of the two readings (set at freeze, before decoding)
The transcription carries both readings (`x{y}?` = reading 1 x / reading 2 y). The headline is `solve/score8211.py` unchanged: its tokenizer (`lib6.signs`) takes reading 1 at every disagreement, and any bracketed span, sign seen only in reading 2, or unreadable `?` becomes a sign with no key value, so the segment is a miss. Two secondary figures, descriptive only, same lexicon, null and bar, by `solve/score8211_alt.py`: (B) reading 2 at every disagreement; (C) only the segments where both readings agree exactly.

## Result (run once, 2026-11-16, after the freeze commit 92b8eca)
**Headline: FAIL.** 59 of 194 segments decode to lexicon words, share 0.304 (bar 0.40); z 5.96 against shuffled keys (null mean 21.8, sd 6.2; bar 5, met). The key fails on share, not on z.
- Segments decoding to 4+ letters: 10 of 57 hit (0.175); null mean 0.09, z 33.5.
- Secondary (B), reading 2 at every disagreement: 64/194, share 0.33, z 5.31.
- Secondary (C), only the 61 segments both readings agree on: 41/61, share 0.67, z 4.98 (just under 5).
- Raw decode in `heldout8211/result.json`. Unbarred decodes that read as Italian include SATISF.A.TA, SCRIUETI, SCRITTEE, METTUANO, FUSSE, CAMPAGNIA, PAGATA, CESA.REA, DIMANDAR, UENETIA, INPAARTANTI.

Reading: the key decodes new text far above chance, but under the pre-set bar it does not show that the key is right across the board. Most misses are segments with a reading disagreement or an unreadable sign (133 of 194 rows carry one); where both readings agree, two thirds of the segments are words. The images (915 px bitonal microfilm, signs ~10 px) are the limiting factor. Anything read further from these passages is post hoc and does not change this result.
