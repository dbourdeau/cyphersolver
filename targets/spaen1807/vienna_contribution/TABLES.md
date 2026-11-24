# Tables and witnesses

| Document | Group-by-group ledger | French witness | Result and controls |
|---|---|---|---|
| No. 7, 24 January | [330 positions](january/vienna_groups.tsv) | [Contemporary reading](january/vienna_clear_copy.txt) | [Predictions](january/vienna_predictions.tsv), [controls](january/vienna_controls.tsv), [result](january/vienna_result.json) |
| No. 23, 21 March | [745 positions](march/groups23.tsv), [both fitted segments at each position](march/training_segments.tsv) | [Training transcription](march/train23.txt) | [Candidate audit](march/candidate_audit.tsv), [93-entry frozen table](march/key.tsv) |
| No. 26, 28 March | [355 positions](march/groups26.tsv), [candidate coverage](march/label_coverage26.tsv) | [Sealed transcription of the period copy](references/reference26.txt), [seal](references/REFERENCE_FREEZE.txt) | [Frozen predictions](march/predictions26.tsv), [matches](march/transfer_matches.tsv), [controls](march/transfer_controls.tsv), [result](march/transfer_result.json) |
| No. 21, 14 March | [432 positions](march14/groups21.tsv), [candidate coverage](march14/label_coverage21.tsv) | [Sealed transcription of the period copy](references/heldout21.txt), [seal](references/SEAL21.txt) | [Frozen predictions](march14/predictions21.tsv), [matches](march14/transfer_matches.tsv), [controls](march14/transfer_controls.tsv), [result](march14/transfer_result.json) |

The [reader files](readers) preserve both independent readings and their prose qualifications. The higher-resolution closing line of No. 23 appears at the beginning of each No. 26 reader file, under END23. The machine ledgers retain one row per position, including every hole, with the two readings side by side.

Whole words have the tag W; B, M and E are initial, medial and final fragments. The suffix on a code identifies the observed superscript: ring o, double dots :, cross +, v-mark v, crossed double stroke #. An underscore denotes no visible superscript, a trailing tilde a baseline stroke and a question mark an unresolved slot.

The [cross-letter table](march14/cross_letter_support.tsv) records each marked type with a whole-token prediction in either held letter, all attempt counts including zero, and the cipher ordinals. The [four-group run](march/shared_sequences.tsv) occurs once in No. 23 and twice in No. 26; this was visible before the diagnostic was specified and establishes no reading of the run. [Relabelling controls](march/overlap_controls.tsv)

The later [working-copy appendix](appendix/NOTES_working_copy.md) compares four period annotations with the tested files. Both underlying [first](appendix/vienna_witness_a.txt) and [second](appendix/vienna_witness_b.txt) readings are included.

AI agents did this work; no person has checked it.
