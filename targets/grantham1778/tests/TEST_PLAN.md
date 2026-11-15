# Test plan: does a table built from other despatches predict the clerk's decipherment of No. 35?

Written 15 November 2026 by the worker (an AI agent), before any score on No. 35 was computed.
The table was frozen first: `table/crib_table_frozen.tsv` and `.json`, checksums in `table/SHA256SUMS_frozen`.

## What is being tested

- **Table.** Built by `work/build_table.py` from fifteen other Grantham despatches of January to July 1778 in SP 94/205
  (Nos. 2, 3, 5, 6, 7, 8 of 16 February, 8 of 19 February, 11, 16, Private of 10 April, 27, 33, 34, 36, 37), 2,314 code numbers.
  No. 35 was not read by the builder. Only the 263 entries graded "firm" are used (a number matched to the same headword
  at least twice, in at least two thirds of its matches, and stable across alignment runs).
- **Held-out text.** No. 35: 62 code numbers (two blind readings agree on all 62) and the 54 English words the
  Secretary of State's office wrote between the lines.

## What the worker had already seen (limits on blindness)

The worker had read No. 35's numbers and its English, and had printed the list of firm entries, before writing this plan.
While looking at Nos. 35, 36 and 37 side by side the worker formed the view that the English is not written word over
number: in the despatches in Grantham's own large hand the English runs ahead of the numbers, and the last lines of numbers
stand bare because the clerk had finished writing, not because they were left unread. The table itself was built by a script
from the other despatches only. No score for No. 35 has been computed, by hand or by script.

## Tests (one run of `test/run_test.py`, seed 35, 200 shuffles)

**Test A, order-preserving (primary).** Take No. 35's numbers in order; keep those with a firm table entry ("covered");
write down the table's headword for each. Score = length of the longest common subsequence between that list and the 54
words of the decipherment, in order. A match is the same word or the same headword in another form (rule `same()` in
`work/align.py`: equal after dropping 's, or equal stems after dropping -s, -es, -ed, -d, -ing, -ly, or the same first five letters).
Control: the same score for 200 tables in which the firm headwords are shuffled among the same firm numbers.
- **Pass mark: at least 60% of the covered numbers matched, and more than every one of the 200 shuffled tables.**
  (On crib despatches left out one at a time and the table rebuilt without them, the same score was 69% to 79%;
  shuffled tables averaged about 23% and never passed 43%. See `work/loo_true.py`.)
- If fewer than 10 numbers are covered the test is recorded as not decidable.

**Test B, word-over-number (the test as first briefed).** For the 43 numbers with English written directly above them
(`transcriptions/n35_office_copy_reconciled.tsv`, positions agreed by two blind readers), count those whose firm headword
matches one of the words directly above. Same 200 shuffles.
- Pass mark if the English were written word over number: 60% of covered numbers. **Stated expectation: B fails**
  (well under 60%), because the English runs ahead of the numbers.

**Test C, the 19 bare numbers.** Among the last 15 numbers (folio 268 verso, nothing written above), take those with a
firm entry. If the bare lines continue the same sentence, their headwords should be found among the last 15 words of the
decipherment ("... that a Vice Consul or Agent should be appointed to reside there").
- Recorded as "tail carries text" if at least 2 covered tail numbers match words there in order; "not shown" otherwise.
  The first 4 numbers are expected to be nulls (no firm entry matching the opening words "I have no reason").

## How the outcomes will be read

- A passes, B fails: the table is supported and the English is not aligned word over number. The reading of the passage is
  then an alignment of all 62 numbers against the 54 words, and "19 unread groups" was a misreading of the page.
- A and B both pass: the English is word over number and the 19 bare numbers are read from the table alone.
- A fails: the table is not supported; nothing is claimed beyond the transcriptions. A miss is reported as a miss.
