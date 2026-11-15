# Held-out test for the Humphreys "994" code table (written before the test was run)

Written 14 Nov 2026, before the held-out despatch was transcribed group by group and before any table value was applied
to it. Nothing below is changed after the run; anything learned later goes in TEST_RESULT.md.

## Held-out despatch

Humphreys to the Secretary of State (John Marshall), No. 262, Madrid, 24 February 1801: the coded passage beginning
after "In consequence of my enquiry, whether Mr. de Orosco would proceed immediately on his mission to the United
States," (M31 roll 6, frame 0235 and any continuation on the adjacent frames). Chosen because:
- it is a whole despatch whose coded passage is not used in building the table (no pair from frames of No. 262 enters
  `pairs.tsv`; `scripts/pairs.py` is run with `HOLDOUT=M31-006-0235` and any other frame of No. 262);
- it has two references independent of the table: the faint decipherment between the lines on the film, and the
  decoded text printed in F. L. Humphreys, *Life and Times of David Humphreys* (1917), vol. 2, p. 289 ("The part here
  given in Italics is in the original all in cypher"), whose source is presumably that decipherment;
- it is from the same Madrid period (1799-1801) as the two target despatches.

## Procedure

1. Freeze the table: `table_frozen.tsv` built by `scripts/build_table.py` from `pairs.tsv` (held-out frames excluded),
   one value per group (majority value; groups whose occurrences disagree and have no majority are left out). Record its
   sha256 in `table_frozen.sha256` before step 2.
2. Transcribe the held-out code from the image, group by group, twice (second pass from the end), reconcile.
3. Build the reference: align each code group to the element of the clerk's/printed decoded text it stands for
   (word, syllable or letter; STOP/COMMA for punctuation groups), using the printed text and the legible interlining,
   WITHOUT consulting the frozen table. Groups whose reference element cannot be fixed are marked and excluded from the
   denominator (and their number reported).
4. Score = share of reference-aligned held-out groups for which the frozen table gives exactly the reference element
   (case-insensitive; a group absent from the table counts as a miss). Also report coverage (share in table) and
   precision (share correct among groups in the table).
5. Control: 200 shuffled tables, each made by randomly permuting the values of the frozen table among its groups
   (same groups, same multiset of values; seeds 1-200). Score each the same way.

## Pass criteria (both required)

- Score >= 0.55 (at least 55 % of the held-out groups decode to the clerk's element), and precision >= 0.85.
- Score above the maximum of the 200 shuffled scores.

A failure is reported as a failure and kept.
