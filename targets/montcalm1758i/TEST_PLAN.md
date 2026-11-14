# Test plan for Phase 2 (written before any comparison)

Written 13 November 2026, before opening any file of codes I, B or W, the 1758 letter, or any Montcalm or Vaudreuil target. The frozen table is `table_e001295272.tsv` (sha256 in `FREEZE.txt`).

## Normalisation
Both sides are lower-cased, accents removed, and spaces, apostrophes and punctuation dropped before comparison (so "Isle Royale" = "isleroyale", "qu'il" = "quil").

## Cells compared
A code number N is compared when it is in 21-700 (cells 1-20 are cut off on the image) and the other code gives a value for N. Illegible cells are never compared.

## Classes of result for each compared cell (first that applies)
1. **Exact**: normalised table reading = normalised code value.
2. **Alternative**: the code value equals one of the alternatives listed for a doubtful cell. Reported separately; not counted as exact.
3. **Merged cell**: one side is a whole word of the other side's multi-word entry (for example "royale" against "Isle Royale"), or one side is the other with a final s, e or x added or removed.
4. **Near**: edit distance 1 when the shorter value has 3 to 6 letters, or at most 2 when it has 7 or more. One- and two-letter values cannot be near.
5. **Conflict**: everything else.

Headline number = exact. Lenient number = exact + alternative + merged + near.

## Control
200 shuffled tables: the 680 legible-row readings (cells 21-700, alternatives travelling with their reading) are randomly permuted over the cell numbers (Python `random.Random(1758 + k)`, k = 0..199), and the exact and lenient counts recomputed for each. Report the real count, the shuffled mean and maximum, and an empirical p = (number of shuffles at or above the real count + 1) / 201.

## Decision rule (fixed now)
The sheet is called **code I** if the exact count is at least half of the cells compared and above every one of the 200 shuffles. If exact agreement is above every shuffle but under half, it is called "related to code I (an edition or a neighbouring table)", and the conflicts are listed. Otherwise it is "not code I". The same rule is applied to codes B and W.

## The November 1758 letter (112 groups)
The table is applied group by group. Groups over 700 or in 1-20 stay unread. If a reading of the letter exists in our files (from any code), each group's table value is compared to that reading using the same five classes, with the same 200-shuffle control. Separately, the decoded string is reported as text and judged by eye for French sense; that judgement is not scored. The per-character French score that failed its positive control on sheet e001295276 is not reused.
