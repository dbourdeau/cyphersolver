# Pre-registration, round 2: the Rohan key on Mme de Rohan's later letters, and the four inferred values

Written 11 Nov 2026, after an OCR survey of vols. 9-12 and before any page image of vols. 9-12 is read, before any
round-2 transcription file or script exists, and before any decryption of the new material is printed or scored.

## Disclosure: what was seen before this file
The archive.org OCR (`_djvu.txt`) of vols. 9-12 (both scans of 9-11) was searched for figures and the hits were read
in the OCR, with their clear context, to find the letters. So the agent has seen, in garbled OCR:
- vol. 9, CLXIX (Mme de Rohan to Duplessis, 1599), "pour M. de 121. 17^. 38. 143." It noticed that the 1594 key
  gives 121 = la, 174 = vi, 143 = ne, so that 38 is the open sign there ("la vi ? ne").
- vol. 11, four letters of Mme de Rohan to Duplessis, Nov 1611 - Mar 1612 (CXCII, CXCVII, the 3 Dec 1611 letter on
  p. 358, CCXXXII) with runs such as "153 148 165 42 158 54" and "123 57 50 150 164 4? 9? 59" and many single small
  figures used as names (77, 26, 39, 81, 28, 29, 11, 110, 105). It noticed that 153 148 165 42 158 54 gives
  "que pe so l re r" under the 1594 key, which is not French. No other value was looked up; no score was computed.
- vol. 11, CCXLII (unsigned, to Duplessis, Paris 25 Jul 1612): "16 75 90 28", "77 12 90", "16 75". Writer unknown.
- vols. 8-9, Duplessis to his wife 1598-99: the name code "81 63" (vol. 8, about twelve places) and "153 63"
  (vol. 9), "88 32 ? 70", "? 9 64 18", "58 166 32 19", single 33. These are the 1595-98 system, not the Rohan one.
No search found a printed key, a deciphered copy or a clear text of any of these passages (see README round 2).

## Frozen key
`key/rohan1594_key.tsv`, unchanged since round 1 (sha256 in `results/frozen_inputs.sha256`, re-hashed in
`results/frozen_inputs_round2.sha256`). The four values inferred in round 1 (`results/rohan1597_reading.md`) are
672 = roy, 134 = lo, 38 = g, 160 = ro; they are held in the test script as a fixed list, not added to the key file.

## Material
`transcription/v9v12_figures.tsv` (figures only) and `transcription/v9v12_context.tsv` (clear words), read from the
page images. Every passage gets a writer field. The Rohan material is every passage with writer = Rohan. Both files
are hashed into `results/frozen_inputs_round2.sha256` before `scripts/test_round2.py` exists.

## Test 3 (primary): the unchanged 1594 key on the new Rohan figures
Same scoring as Addendum 1 of PREREG.md, nothing changed except the seed:
- Coverage = groups with a value in the 1594 key / all Rohan groups (single figures in the clear included).
- Language: letter-trigram model from vol. 6 OCR (the same file and sha256 as round 1), only letter and syllable values
  scored, pieces cut at unvalued groups and at word or name values; null = 200 keys made by permuting the key's values
  over its own figures, `random.Random(2026)`. Language sign if the key beats at least 190 of 200.
- Verdict: fits if coverage >= 0.50 and a language sign; does not fit if coverage < 0.30 or no language sign; otherwise
  inconclusive; "too small" if fewer than 20 groups are covered or fewer than 30 letters are scored.
- Reported alongside, not changing the verdict: the same scores for the 1611-12 passages alone and for runs of two or
  more groups alone.

## Test 4: the four inferred values
On the same material, the 1594 key plus the four values (the "extended key") against 200 controls in which the four
added figures get four values drawn at random (with replacement) from the key's own letter and syllable values,
`random.Random(2027)`. Score: the language score of Test 3. Supported if the extended key beats at least 190 of the 200.
Not testable if none of 672, 134, 38, 160 occurs in a scored run of the new material. Each occurrence is also listed
with the piece it gives, for the reader.

## Extras (reported, no verdict)
- The folded 1593 key and the Rohan key on the new 1598-99 Duplessis passages (as round 1, part B).
- The 1612 unsigned letter: the Rohan key, the same two scores, labelled extra.

## The 1595-98 Duplessis/Lomenie system
No key exists to test. If a clear copy of any passage turns up, a key will be built from that copy only and an Addendum
to this file will name the held-out passages and the score before the test is run. Anything else done on this system
(ranges, repeats, positions) is exploratory and labelled so.

## One run
`scripts/test_round2.py` is run once after the hashes are written; a second run in CHECKS.txt must give identical
output. Anything done after the run is exploratory.
