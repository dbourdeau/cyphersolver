# K5.7, rounds 5–8

All letter positions below are interior positions unless marked “full.” The analyses use the existing transcription. Doubtful, missing, and unidentified letters supply no positive matches. The layout comparisons try all 23 single interior omissions from row 2. These omissions are hypotheses for aligning rows of unequal length. The source data remain intact.

## 5. Is there evidence of copying beyond the shared opening?

Starting at interior position 12 of rows 2 and 4 excludes both the known opening and the reversed triplet. Five statistics compare the remaining tails. The reference distribution comes from 5,000 independent shuffles of the secure letters within each tail, preserving the inventory and the positions of the doubtful cells. The fraction is how often the simulated score equalled or exceeded the manuscript score.

| Statistic | Observed | Reference fraction |
|---|---:|---:|
| Longest contiguous forward match | 1 | 5000/5000 |
| Longest contiguous reverse match | 2 | 409/5000 |
| Longest ordered forward subsequence | 1 | 5000/5000 |
| Longest ordered reverse subsequence | 3 | 826/5000 |
| Distinct adjacent pairs shared in either orientation | 1 | 813/5000 |

The contiguous pair is shin–ayin read in opposite directions. The longer reversed subsequence is kaph–shin–ayin, allowing a gap. Both had already been noticed. Their frequencies under shuffling calibrate the amount of evidence in these short tails. The tests share letters and were conducted after seeing the reversal.

## 6. Can a learned substitution transfer from one row pair to the other?

For each layout and omission, allow each source letter its own output, even if two inputs map to the same output. Minimize training disagreements on rows 2→4. Use only predictions on securely read cells in rows 1→3 on which every best-fitting omission gives the same unique majority output.

| Layout | Minimum training disagreements | Equally best omissions | Successful odd-pair predictions / eligible |
|---|---:|---:|---:|
| Same positions | 0 | 13 | 0/7 |
| Reverse positions | 1 | 6 | 0/0 |
| Swap neighboring positions | 0 | 1 | 1/7 |
| Exchange the two halves | 0 | 2 | 0/2 |
| Map successive positions alternately to opposite ends | 0 | 15 | 1/4 |

For the same-position layout, all omissions of interior positions 11 through 23 allow an exact fit to secure even-row pairs. All predict waw at odd-row target positions 1 and 3. Row 3 reads kaph and bet there. The contradiction can be checked without fitting anything: row 1 has waw at both positions. A fixed same-position substitution from row 1 to row 3 cannot send that one letter to two different outputs. The seven failed predictions reuse some letters and are not seven independent trials.

## 7. Do marks encode numerical relations?

Use zero-based Hebrew alphabet ranks modulo 22, secure upper readings, and clear lower labels. Fit one value per lower shape. For a withheld prediction, require at least two different training rows and unanimity among their observations of that shape. The folds are row 1, row 3, and both even rows together. Forward and backward steps compare the adjacent letter to the current one. The mirror test adds the ranks of the current and next letters. The column offset subtracts the next column index from the next letter rank. The skip-one test compares the letter two positions ahead to the current one.

| Mark interpretation | Eligible observed cells before withholding | Mark classes giving conflicting values | Successful withheld / eligible |
|---|---:|---|---:|
| Forward step | 15 | bend, ring, two dots | 0/1 |
| Backward step | 13 | bend, ring, two dots | 0/0 |
| Mirror sum | 15 | bend, ring, two dots | 0/0 |
| Next-column offset | 19 | angle, bend, ring, two dots | 0/0 |
| Skip-one step | 15 | bend, ring, two dots | 0/0 |

These are tests of the current visual classifications. A more detailed sign inventory or changed mark-to-letter registration could alter the result. Offsets use the literal row positions, including the longer second row.

## 8. Does row spacing locate the extra position?

Normalize horizontal coordinates to the two endpoints of each row. Omit one interior position in row 2 and compare the remaining 26 positions with complete rows 3 and 4. The coordinates come from the earlier lower-mark crop centers, an approximate proxy for scribal spacing. The methods share these measurements.

| Alignment criterion | Preferred row 2 **full** position to omit |
|---|---|
| Absolute distance to row 3 | 6 |
| Absolute distance to row 4 | 11 |
| Squared distance to the mean reference row | 7 |
| Largest distance to the mean reference row | 6–11 tied |
| Absolute differences in consecutive gaps from the mean reference | 10 |

All optima fall within the opening section where upper signs already correspond across the two even rows. The preferred position changes with the reference row and loss function. These measurements give no defensible deletion from the transcription.

[Runnable searches](rounds_5_8.py) · [Upper readings](check.py) · [Lower-mark measurements](lower-register.tsv)
