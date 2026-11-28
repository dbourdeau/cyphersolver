# PREREG-1 — villeneuve-1737 (cat. 538) — frozen key K1 and the single measure
Date: 2026-11-23, written BEFORE the held-out measure and BEFORE any decoding of the targets T1/T2.
Follows PREREG-0-portions.md (SHA-256 06678b1b1d481b22e8971a21feedc5f74f1666d7f65f75fdc87150c9f7520e70, 2026-11-20).

## Inputs (frozen)
- Cipher transcription: two blind passes (A, B; Opus sub-agents, no key) + blind arbiter (Opus, 62 items) -> transcr/merged_cipher.json.
- Gloss (period interlinear decipherment) transcription: careful re-reading (Opus sub-agent, no key) -> transcr/gloss_careful.txt.
- Key K1 = key/KEY-K1-frozen.txt (218 codes; value '-' = null). Built ONLY from TRAIN (frames 0197, 0198, 0199, 0230, 0231): coordinate-ascent fit of code values to the gloss (edit distance, 3-line chunks) + hard-EM majority + manual curation of values from repeated words on TRAIN only. The held-out glosses (0200-0202) were never used.
- In-sample diagnostic on TRAIN (same measure, page passages): 0.858 (not a validation).

## Measure (the only one; held-out burnt after it)
- Portion: held-out = frames 0200 L+R, 0201 L+R, 0202 L (prereg/heldout.pas, exported by scripts/export.py ... page).
- Program: scripts/measure.c (compiled as-is). Score = 1 - edit distance / number of gloss letters, page-level concatenation; normalisation lowercase a-z, accents stripped, j->i, v->u (as PREREG-0). Lacunae: a gutter loss ([G]) in the cipher absorbs 0-15 gloss letters at no cost; a ‹…› lacuna in the gloss absorbs 0-10 decoded letters at no cost; a code absent from K1 decodes to '*' (always wrong).
- Controls: 200 keys = K1 values shuffled among K1 codes (Fisher-Yates, LCG seed 17371802).
- Criterion (from PREREG-0): PASS iff score >= 0.85 AND score >= best control + 0.30. Held-out < 300 cipher groups = non mesurable (it has 2+ groups on the first page alone; total printed by the program).
- Word agreement: not computed (not decisive).

## After the measure
- Whatever the result, K1 is not changed for the measure. A key K2 = K1 + values read from the (then burnt) held-out glosses may be built for READING the targets; it is frozen by SHA-256 before the targets are decoded and is reported as not separately validated.
