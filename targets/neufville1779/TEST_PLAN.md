# Test plan, written before running (13 Nov 2026)

Key K1: majority unit per number from key_source_pairs_pp600-603_609.tsv only (de Neufville's 29 April 1779 draft pp. 600-603 and the undated draft p. 609). No pair from p. 599 or pp. 604-606 is in K1. K1 is frozen by sha256 (key_K1.json) before scoring.

T1 (independent letter). Decode every unstruck group of pp. 604-605 that K1 covers and whose unit in the writer's own draft (p. 599) is known. Score = share of covered groups where the K1 unit equals the draft unit after normalising (lower case, accents and apostrophes dropped, doubled letters collapsed). Baseline: 200 keys made by shuffling K1's units over K1's numbers (seed 1779); report the mean, maximum and the share of shuffles that reach the real score. Pass: real score >= 0.80 and no shuffle reaches it.

T2 (held-out pairs, as the brief asks). The glossed pairs are on p. 599 (numbers with syllables written under them), not p. 606 as the sweep thought. Take the p. 599 lower-block pairs (truth file rows 605.3-605.12). Hold out ten pairs (seed 1779) whose number occurs elsewhere in K1 or in the other p. 599 pairs; train on K1 plus the remaining pairs; predict the ten. Pass: >= 8 of 10, and the real count above every one of 200 shuffled-key counts.

A failed test is kept and reported.

# Round 2 test plan, written before running (13-14 Nov 2026)

Key K2 = K1 pairs + all p. 599 draft pairs (truth file, '?' excluded) + key_additions_round2.tsv; majority unit per number.
The whole p. 608 draft ("6 May d'Arras") is held out: none of its pairs is in K2. K2 frozen as key_K2.json (sha256) before
scoring. Predict the unit of every p. 608 number (heldout_p608_truth.tsv) that K2 covers; score with the same normalisation
as round 1; 200 shuffles of K2's units over its numbers (seed 1780). Pass: >= 80% of covered groups and no shuffle reaches it.
K1 stays as frozen in round 1 (key_K1.json, sha256 dc04ab46...).

# Round 4 test plan, written before running (14 Nov 2026, follow-up to pull request #587)

New evidence: transcriptions/glossed_pp516-548.tsv (every code group of Baudouin's letters pp.516-548 with de Neufville's gloss;
only rows with status G enter a key) and key/p608_truth_complete.tsv (all groups on p.608; '?' rows excluded). They replace
key/key_pairs_classB_glosses.tsv for pp.516-548 and key/heldout_p608_truth.tsv as key sources; the p.579 rows of the old
gloss file are kept.

T4 (held-out letter). Hold out every glossed (G) group of the letter of 10 April 1779, pp.529-531. The letter was fixed as
the hold-out by page before any key was built or scored; the transcriber had read its glosses while transcribing, which
cannot be undone. Key K4 = majority unit per number from all sources except pp.529-531; frozen as key/key_K4.json (sha256
printed and recorded in key/FREEZE.txt) before scoring. Score = held-out groups whose number K4 covers and whose K4 unit
equals the gloss unit, same normalisation as rounds 1-2. Baseline: 200 keys made by shuffling K4's units over K4's numbers
(seed 1781). Pass: >= 80% of covered groups and no shuffle reaches the real count. Run once; the result is kept whatever it is.

Then the full key K5 (all sources, pp.529-531 included) is built and frozen as key/key_full_r4.json before the bare passages
(B573, B491, B492, B527) and the p.608 groups are decoded with it.

Re-score, not a new test: K2 (frozen in round 2) is also scored against key/p608_truth_complete.tsv, to show what T3 gives
on the whole page.

# Round 5 test plan, written before running (14 Nov 2026, second pass)

New evidence: the survey of pp.487-515 and 549-590 (transcriptions/survey_pp487-515_549-590.tsv) found glossed code on one page
only, p.579, already partly used. Its groups are in transcriptions/glossed_p579.tsv, a separate file.

Frozen key: key/key_full_r4.json as committed in 6ce11d9e0; its sha256 must equal 146207b0...f460 (key/FREEZE.txt), and the
script stops if it does not. The key is not rebuilt for the test.

T5 (held-out pairs for the current key). Held-out set: the rows of glossed_p579.tsv with status G and prior = no (pairs never
used to build key_full_r4; 537 and 326 from p.579 were in it and are left out; 473 is D and left out). Score = held-out groups
whose number key_full_r4 covers and whose unit equals the gloss unit, same normalisation as rounds 1-4. Baseline: 200 keys made
by shuffling key_full_r4's units over its numbers (seed 1782); report mean, maximum and the share that reach the real count.
No pass bar: the set is five groups, too small for one; the result is reported whatever it is, and run once.

Then K6 = the round 4 sources plus the G rows of glossed_p579.tsv with prior = no (majority per number, as before), frozen as
key/key_full_r5.json, and the bare passages B573, B491, B492 and B527 are decoded again with it. Any number whose value differs
between key_full_r4 and key_full_r5 is listed. A value given by context only is a guess and is not counted as read.

Post-run note, 15 Nov 2026 (the plan above is left as written). The held-out set was wrong: two of the five pairs, 68 l' and
428 les, were already in key_full_r4 through key/key_additions_round2.tsv (round 2, page 579), which scripts/test_round4.py
reads with no page filter; glossed_p579.tsv had marked them prior = no. Counting only the pairs new to the key (499, 202, 226),
T5 predicts 2 of 3 (226 missed). Three pairs are too few to carry weight either way. Re-run on the corrected files:
results/test_round5_output_rerun_2026-11-15.txt.
