# zeschau1841, R5005: the cipher is in groups of 2, 3 and 4 digits, not pairs (structure only; Brice Dudout, 11 Nov 2026)

Status: in progress (Next step: check the 15 off-form groups against the DECODE images, then transcribe R5006-R5008 and segment them with the same rule to set probable words on whole groups).

Contributed by Brice Dudout (Europe chiffrée). The rule was proposed by Fable 5.2 (an Anthropic model, run through the API)
working on R5005 **without** blocks a3 and a7; the held-out measure was pre-registered and run by a Claude Opus 5.5 agent.
Transcription: Daniel Bourdeau's `../ct_R5005.txt`, used unchanged. Nothing here is a reading or a key.

## The finding

R5005 is not written in two-digit groups. The length of each group is set by its first digit(s):

| Group starts with | Length | Form |
|---|---|---|
| 0 or 1 (not 00) | 2 | 0x, 1x |
| 3, 4, 6, 8 | 2 | [3468][13468] |
| 2, 5, 7, 9 (not 55, 77) | 3 | [2579] x [13468] |
| 00, 55, 77 | 4 | 00xx, 55xx, 77xx (55xx/77xx end in 1/3/4/6/8) |

Groups are written without separators and run on from one line to the next (a4 runs into a5), so the per-line pair phases
of `../offsets.json` are no longer needed. R5005 gives 1,309 groups of about 190 types; 15 (1.1%) fall outside the forms
and are probably transcription slips (list below). Immediate repetition of a group never occurs, as with a clerk who
alternates homophones. The table thus has roughly 300 cells of 2, 3 and 4 digits, not ordered.

## Held-out check (pre-registered, one run)

Fable saw 2,905 digits (all blocks but a3 and a7). Before a3/a7 were segmented, the rule (verbatim from Fable's script),
the thresholds and the controls were written down and hashed (SHA-256), with a calibration on the blocks Fable had seen.
One measurement on a3 + a7 (859 digits, 296 groups):

| | result | bar |
|---|---|---|
| groups in the forms | **0.983** (a3 60/60, a7 231/236), both blocks starting on a group boundary | ≥ 0.95 |
| digits shuffled within lines (1,000) | mean 0.641, max 0.703 | must beat the max |
| pairs shuffled across the stream (1,000) | mean 0.630, max 0.700 | must beat the max |
| synthetic French homophonic cipher in true pairs (200) | mean 0.601, max 0.667 | must beat the max |

Secondary checks, all held: 3-digit groups ending in 1/3/4/6/8, 0.984 (controls about 0.55; the regex does not use this);
no immediate repetition (shuffled order: 3.3); 95.6% of a3/a7 tokens are of a type already seen elsewhere in R5005
(controls at most 0.62), so the two parts share one closed table; `06777818711001` falls as 06|7778|18|711|001x.
Details and hashes: `validation.md`.

## Glosses on whole groups (proposals, not measured)

Re-aligned on the groups, the erased pencil glosses of a5_03 (`06 711 708 234 294 02`) fall on whole groups:
711 = la, 708 = pre, 746 = que (ends a8_05), 234 = mi (Daniel's "m" + "i" joined), 294 = er (or re / ere; not settled).
The same "711 708 234 294" recurs in a6_03. These are re-alignments of Daniel's readings, not tested values.

## Groups outside the forms (to check on the images)

a2_05 `900 925`; a2_08 `45`; a5_08→a5_09 `62`; a5_09→a5_10 `547`; a6_03 `49`, `45`; a6_10 `7777 89` (the formula
`7778 948 206` with one 7 too many?); a7_07 `65 242`; a7_09 `210 262`; end of a7_11 `1`; a8_05 `85`.

## Files

`segment.py` (the rule; `python3 segment.py ../ct_R5005.txt`), `R5005_groups.txt` (R5005 cut into groups, line by line;
`*` = outside the forms, `>` = runs on into the next line), `validation.md` (pre-registration, controls, hashes).
No image is included.
