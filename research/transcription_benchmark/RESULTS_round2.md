# Transcription benchmark, round two: 36 correspondences, one blind Fable pass each

Run 19-20 Nov 2026. Scripts: `frame2.py`, `draw2.py`, `prep2.py`, `prompts2.py`, `score2.py`. Scores: `scores2.json`.
Page images and DECODE transcriptions are not committed (`decode_cache/` is git-ignored; tiles in the scratchpad).

## Why a second round
Round one (`RESULTS.md`, `RESULTS_fable.md`) had 10 documents from 5 correspondences. The between-document spread
(SD 4.8 points) dominated the uncertainty, so the sample-size projection asked for about 40-60 documents from separate
correspondences.

## Sample
- Frame: DECODE records with a manual ciphertext transcription ([transc]), page images, a numerical and/or alphabetic
  symbol set (no graphic signs, whose labels are transcriber-specific), at most 4 pages. Strata: letter if the symbol set
  includes Alphabet, else digit.
- Draw: one record per target folder already on disk, then a seeded random walk (seed 20261120) through DECODE's 3,692
  ciphertext records, one record per correspondence. 3,252 candidates checked; 3,052 had no transcription or images.
- Dedupe (v2): v1 took a correspondence to be the exact DECODE author string, which let one person in under several
  spellings (Pallotto x4, Papai x3, Rakoczi, Alessandrino, Ronquillo, Balbases/Carpio and Ferdinand x2). v2 keys on a
  person or series (alias table `PERSONS` in `draw2.py`), keeps the first record, and refills the digit stratum from the
  candidates v1 passed over as "quota full", in their shuffled order. v1 is kept in `frame2/sample2_v1.json`.
- Result: **36 documents, 36 persons or series; 30 digit, 6 letter; 67,137 reference signs; 87 pages.** The letter
  stratum could not be refilled (DECODE has no further eligible letter records from new correspondences), so letter
  figures are indicative only. 9 records come from targets on disk, 27 straight from DECODE. 3 documents (R7, R72, R1890)
  were also in round one.

## Protocol
- Page order from the reference's own image list where it gives one (20 of 36 fully), else DECODE page number.
  Rotation set by eye for 10 sideways documents (crop tested at 90 and 270 degrees; `frame2/rotations2.json`).
- Tiles as round one: bands of 1,000 px, 90 px overlap, max 2,000 px wide (292 tiles).
- One blind pass per document, Fable 5.2 (`claude-fable-5-2`), 10 batches of up to ~38 tiles, at most two at once.
  Same rules as round one; one generic description per stratum, so no prompt carries reference content
  (`prompts2.py`). Each agent saw only its instruction file and the tiles.
- Deviation: the batch-5 agent (R847, R923, R928, R956) enlarged crops of its own tiles with a script. Still blind (tiles
  only), but more effort than the others; reported separately below.
- Scoring as round one: edit distance between sign streams, separators and clear text ignored, '?' always an error.
  Digit stratum digits only; letter stratum digits and letters. DECODE's mark codes over digits ('^' + one character,
  e.g. 3^1, 7^~) are removed in the digit stratum; in the letter stratum '^' introduces a real superscript number and is
  kept.
- Two figures per document. **Strict**: one alignment of the whole stream. **Order-tolerant**: the pass cut into blocks of
  10 lines, each fitted to its best place in the reference, unmatched reference signs counted as deletions. The second
  forgives only block order (two-page spreads transcribed right half first, pages out of order); on documents with no
  order difference the two are identical.
- Interval: bootstrap over documents (the sampling unit).

## Results

| | docs | signs | pooled, order-tolerant | 95% CI | median doc | pooled, strict |
|---|---|---|---|---|---|---|
| all | 36 | 67,137 | 9.2% | 6.5-12.5 | 5.4% | 17.4% |
| digit | 30 | 56,132 | 7.7% | 5.0-10.5 | 4.2% | 15.1% |
| letter | 6 | 11,005 | 16.7% | 8.0-39.4 | 31.1% | 28.8% |
| from disk | 9 | 12,448 | 5.1% | 2.5-10.5 | 3.2% | |
| straight from DECODE | 27 | 54,689 | 10.1% | 6.7-13.9 | 7.2% | |
| without batch 5 | 32 | 57,970 | 10.2% | 7.2-13.8 | 6.1% | |
| not in round one | 33 | 63,314 | 9.6% | 6.8-13.2 | 5.4% | |

18 of 36 documents are under 5% and 11 under 2% (order-tolerant).

Per document (order-tolerant; strict in brackets where different):
R7 1.2, R40 18.6, R65 4.2, R72 2.4, R80 0.7, R90 0.4, R94 1.5, R116 16.0, R142 0.5, R201 2.0, R209 1.1, R249 8.3,
R473 11.2 (13.0), R474 14.6 (37.2), R478 22.3, R711 3.8, R729 15.9 (39.3), R795 12.7 (29.3), R822 4.6 (53.9), R847 5.4,
R923 0.5, R928 0.6, R956 3.3, R973 49.4, R982 45.8 (47.2), R997 31.1, R1014 18.3, R1044 3.2, R1046 5.4, R1051 1.7,
R1066 1.7, R1408 14.2, R1890 2.6, R1893 22.2 (26.2), R1894 7.2 (30.0), R1925 6.1.

## Adjusted score: order, reference conventions and sign labels accounted for
`adjust2.py` -> `scores2_adjusted.json`. One rule per effect:
1. **Order:** the order-tolerant score above (blocks of 10 lines fitted to their best place; lower of strict and
   order-tolerant).
2. **Reference conventions (digit stratum):** a letter the reference uses for a digit is read as that digit when it lines
   up with that one digit in the pass in >= 80% of at least 5 aligned occurrences.
3. **Sign labels (letter stratum):** a letter the pass uses for a special sign is renamed to the reference's label on the
   same rule. Signs spelled out as words count as one sign: in the reference ("Infinity", "fire": an unspaced run of
   3+ letters, where the reference spaces its cipher letters) and in the pass (`at`, which the batch-6 agent reported
   using for the crossed d-like sign).

Digits are never renamed, so a misread digit stays an error. Guard against fitting: the blocks are split into two halves
(alternate blocks), each rule is learned on each half separately, and it is applied only if both halves learn it.

Rules that passed: **R478 "i" = 1** (22.3% -> 2.7%) and **R973 "x" = the reference's "Infinity"** (49.4% -> 26.4%,
the reference falling from 555 to 394 signs once "Infinity" counts as one). Learned in one half only, so not applied:
R1014 `at` = "d". No other document has a rule.

| | docs | signs | pooled, adjusted | 95% CI | median doc | docs under 5% |
|---|---|---|---|---|---|---|
| all | 36 | 67,106 | **8.6%** | 5.9-11.7 | 4.6% | 19 |
| digit | 30 | 56,277 | **7.4%** | 4.7-10.2 | 3.8% | 18 |
| letter | 6 | 10,829 | **14.8%** | 7.4-34.6 | 26.4% | 1 |

What remains in the Spanish letters (R982 44.6%, R997 28.7%, R1014 16.3%, R973 26.4%) is not labelling but two digit
shapes of these hands that the pass misreads again and again: 9 read as 4 (43 times in R982, 50 in R997) and 7 read
as 3 (31, 31 and 72 times in R982, R997, R1014), plus o/0 confusions. They are misreadings and stay errors. A bound that
also lets a consistent digit swap be renamed (same both-halves rule) changes little: only R997's 4 -> 9 passes
(28.7% -> 22.7%); 3 -> 7 does not, because the pass also uses 3 for genuine 3s. Pooled with that bound: 8.55%.

## What the high figures are made of
- **Order, not reading.** Strict rates of 30-54% on R474, R729, R795, R822 and R1894 fall to 5-16% once block order is
  forgiven: two-page spreads and pages taken in a different order from the reference.
- **Reference conventions.** R478's reference writes the digit 1 as "i" (`2 3 i` for 231), which digit scoring drops;
  read as 1, the document falls from 22.3% to 2.7% (adjusted score above). The header does not document the
  convention; the adjusted score finds it from the alignment, not by hand. R1893's reference includes a clear-text date line (1793) that the pass skipped.
- **Sign-label conventions in the letter stratum.** The Spanish letters (R973, R982, R997, R1014, 18-49%) mix digits,
  letters and special signs (a crossed d, a crossed q, underlined capitals) whose ASCII labels are the transcriber's own
  choice; the pass chose others (e.g. `at` for the crossed d). R973's pass looked a third shorter than the reference
  because the reference spells a sign as "Infinity" (8 letters for one sign). Accounted for in the adjusted score, the
  labels explain less than they seemed to: the rest is the hands' 9 and 7 read as 4 and 3. R1890 (Ferdinand, letters
  and digits) is 2.6%.
- **Genuinely hard hands.** R40 (smeared, show-through; the agent flagged every line), R116 (three shapes of 4 and an
  "st" ligature), R249 (degraded black-and-white scan), the Hungarian chancery signs (R473, R474).
- So the plain pooled figures are upper bounds on misreading: they also carry order, reference conventions and label
  choice. The adjusted score (8.6% pooled, median 4.6%) removes what the alignment can attribute to those; it still
  counts every disagreement with the DECODE reference, including the reference's own errors (human-to-human
  disagreement: 1.3% pooled over 16 records, see Limits).

## Against round one
- Round one, Fable, 10 documents: 3.3% pooled (2.0% digit-only). Round two, 36 correspondences: 8.6% pooled
  adjusted, median 4.6%; digit stratum 7.4% pooled, median 3.8%.
- The difference is the population: round one's documents were from five correspondences already worked on here, with
  pages ordered by hand; round two is a random draw across DECODE, including scans and hands round one never met.
- Reproducibility: R72, in both rounds under different prompts, scores 2.9% and 2.4%.

## Limits
- One pass per document (round one had three); no vote, no disagreement flag.
- The reference is one DECODE transcriber per document; its errors count against the model. Human-to-human disagreement
  is 1.3% of signs pooled (median 0.9%, 0.1-5.1% by record) over 16 records, five transcriber pairs and 18,508 signs
  (`human_ceiling_wide.json`, from `scan_doubles.py`: 140 of 3,692 records carry two or more text files, 28 by
  differently named transcribers; dropped: 8 whose second file is not the same text, 4 not independent). By pair:
  KaJo/OliNi 0.6% (3 records), Matt F/NiLan 0.8% (8), EHum/KaJo 0.6% (1), Midas/NiLan 2.0% (3, the pilot in
  `human_ceiling.json`), EHum/Midas 5.1% (1). The second transcription usually sits in a decryption file and may have
  been started from the first, so 1.3% may understate independent readers.
- Letter stratum: 6 documents, and label conventions dominate.
- Prompts were generic per stratum; round one's described each document, which may explain part of the gap.
