# Independent held-out scorer: plan (written before running it)

Written by an AI agent (Claude Opus 5.5), 22 Nov 2026, about 21:30 EST, before `scripts/reviewer_heldout.py` was run.

Inputs: the session's frozen training table `tests/table_train_frozen.json` (sha256 8854344a..., checked);
Brackx's groups 569-653 (`../ciphertext.txt`, his digits) (0-based 568-652); the draft text `transcriptions/clear_draft_test_text.txt`, normalised by my own code
(lower case, accents removed, letters a-z only), cut at letter 1928 (the session's boundary; I also report the
boundary implied by the hand alignment).

Scorer (my own code, not the session's): a dynamic programme over (groups used, letters used) that must consume all
85 groups and all held-out letters. A group with a table value either writes exactly its table chunk at that place
(counted as a fit) or 0-15 letters (no fit); a group without a table value writes 0-15 letters. Maximise fits.
Controls: 1,000 shuffled keys (the table's chunks dealt at random among its groups), seed 22112026.

Pass mark (the session's, unchanged): at least 40 predictions, at least 70% of them fit, and fits above the 99th
percentile of the shuffled keys. A second, simpler check: compare each frozen-table prediction with the session's
hand alignment (`key/alignment_by_group.txt`) at the same group.

File names updated on 22 Nov 2026 to those in this folder (the plan was written with the local working names); nothing else changed.
