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
