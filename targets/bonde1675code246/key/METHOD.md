# Draft key of the second code (1-246): how it was built, and what it is not

**Status: draft.** The key agrees with the period gloss at 0.65 (characters), measured on its own training text
(resubstitution). It was never tested on a held-out portion, so this figure is not a validation. It is offered so
that others can improve it; the reading of the letter comes from the period gloss, not from this key.

## Files

- `key.tsv`: number, letter (120 values). `key_draft.json`: the same key as written by the builder.
- `key_start_draft.tsv`: the starting key (an earlier draft from simulated annealing with a Swedish 4-gram model and
  an alignment on the 114 left glosses, 14 Nov 2026), used only as the starting point.
- `../scripts/build_key3.py` (with `../scripts/data.py`): the builder as run, paths changed to this folder.
  `python3 scripts/build_key3.py .` from the target folder rebuilds the same 120 values and prints the figures below.
- `../scripts/decode.py`: the line-by-line decodes in `../decryptions/`.

## Method (fixed in writing before the key was built: protocol/METHODE-CLE.md, protocol/PREREG-CODE246-ADDENDUM-3.md)

1. Training cipher: the pass-3 transcriptions of 113 right lines L01-L18 (390 numbers) and 114 left lines G01-G32
   (588 numbers). The 113 right lines L19-L33 (301 numbers) were set aside before any key was built and were never
   decoded (see NOTES.md).
2. Training clear text T: the period gloss, concatenated: 113 right G01-G20 as read by Fable 5.2 (first option of each
   doubtful letter, unread zones dropped), G21-G33 as read by Opus sub-agents (`../gloss/113R_G19-G33_subagents.tsv`),
   and the gloss of 114 left lines 1-5 (`../transcriptions/114L_G01-G32_pass1.tsv`, column 3). Normalised to lower case,
   w=v, j=i, letters a-z å ä ö only, after expanding the fixed abbreviations of ADDENDUM-3 (Maij:t -> maiestet,
   Kongl: -> kongelig, förbem:~ -> förbenämnde, d. + number -> den, & -> och, Exc: -> excellens). 1,337 letters.
3. Iterate (at most 12 rounds): decode both training sequences with the current key; align each on T (semi-global
   edit distance, ends of T free); for each number take the majority letter it is aligned with (at least two votes, or
   one vote for a number seen once). One class only: letters (no nulls, no code words were found). Converged after
   two rounds.

## Figures (scripts/build_key3.py output)

| metric | all | 113R L01-L18 | 114L G01-G32 |
|---|---|---|---|
| ADDENDUM-3 metric (whole gloss words may be skipped at cost 1) | 0.653 | 0.736 | 0.599 |
| earlier metric (letter edit distance only) | 0.631 | 0.715 | 0.575 |

Our pre-registered floor for a single test on the held-out lines was 0.85. Since even resubstitution stays at 0.65,
the test was not run and the held-out lines were not decoded.

## Why the figure stays low although the decodes follow the gloss word for word

- The gloss abbreviates and does not always follow the cipher (Maij:t against `maiestet`, words in one and not in the
  other: the cipher's `hafver at` and `altsom ste...` near the opening are not in the gloss as read).
- The gloss of G21-G33 and of 114 left was read by sub-agents, often with unread words; the 114 left figure (0.599)
  suffers most.
- The number transcription is not clean: the first two passes agreed on 94% of the numbers of L01-L18; the third pass
  changed 45 numbers and dropped 18 positions.
- The clear date `18/28` at the start of 114 left G32 entered the training sequence as the number 28; one number read
  346 (113R L12) is above the range and is probably a misreading.

## Shape of the key

120 values for 25 letters (homophones): a 10; i, n, t 8; d, l, m, o, r, s 6; e, f, g, v 5; b, c, h 4; k, p, u, ö 3;
å, ä 2; y, z 1. One number per letter, no syllables, no code words, no nulls identified. Number 62 has no value.
Values do not run in alphabetical order. Two examples on the image: `hafver` = 46.38.12.34.70.27 (113 right L01), and the last line of 114 left, `50.77.34.42.22.16.112.55.149` = `Novembris`, which a later pencil hand wrote
letter by letter under the numbers (checked on the images by Daniel Bourdeau, issue #629).
