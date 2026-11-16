# LOG.md  renard1549 Vienna original (work of 16 Nov 2026, Claude Fable 5.2 as agent for Malcolm McBratney)

All times UTC. Inputs read-only. Images are an HHStA working scan (GZ 2026-0.947.186): not committed, not published.

1. Checked scan md5 cb6ae0afef714450be9450cbaef1f859 [measured]. Four page images 2024 x 2866, stored upside down; turned 180 degrees for reading.
2. Read Sourvillo's NOTES.md, reading.md, translation.md, key.tsv (upstream/main) and the renard1554 / renard1556 notes. the project rules (CLAUDE.md) were taken from the copy supplied with the task.
3. Prior art (PRIOR_ART.md): CSP Spain IX, Tomokiyo, DECODE, CCFr. Pich-Ponce 2023b was fetched only at step 9, after the key was built.
4. Layout read from crops (RESULTS.md section 1).
5. Cipher transcribed line by line from 2.2x crops, 30 + 28 + 9 = 67 lines, with shape mnemonics, then relabelled S01..S69 (SIGNS.tsv holds shapes, no values). French margin transcribed from 2.4x crops.
6. FREEZE 08:44:45Z, refrozen 08:44:54Z for a label-only fix (one base sign had two labels). No sign or letter changed after that. sha256 in FREEZE.txt.
7. Alignment attempts, all recorded:
   - A1 blind hard-EM, per page, no seed: FAILED (no consistent values; top sign 22 of 92).
   - A2 seed of 7 guesses from the repeated group at 13r.03 (wrong segmentation, 5 of 7 values wrong): FAILED, drifted.
   - A3 one continuous stream, 11-sign seed from the "soubz / souldars" repeats on 13r (4 of the 11 later shown wrong): converged to readable French.
   - A4 seed of 71 values = consonant sign + vowel mark rule read off A3 (this pass was read with the whole text in view, held-out lines included): final alignment, key_renard1549_vienna.tsv, ALIGNMENT.tsv, DECODE_fullkey.txt. In-sample self-decode 0.8168 (not a test).
8. Hold-out (lines 13v.25 to 14r.09, 13 of 67 lines = 19.4%; 263 of 1,513 signs; 371 letters). Key rebuilt from the first 54 lines only; one decode; score = 1 - Levenshtein / max length; no emendation.
   - H1 first pass, seed A4: 0.7377 (edit distance 101). Controls, 5,000 shuffles each: seed 20261112 mean 0.2141 max 0.2791; seed 7 mean 0.2136 max 0.2700; 0 shuffles reach the real score. CAVEAT: seed A4 was written after seeing an alignment of the whole letter, so H1 is not leak-free.
   - H2 seed A3 only (built from page 13r, leak-free): 0.5666 (edit distance 166). Controls max 0.2773 / 0.2797. BELOW the 65% line.
   - H3 post-hoc, training-only bootstrap (holdout_bootstrap.py): 0.6481 (edit distance 133). Controls max 0.2897 / 0.2863. BELOW the 65% line by 0.2 points.
   No further tuning was done. All three are reported.
9. Fetched Pich-Ponce 2023b summary and compared structure (RESULTS.md section 6).
10. Repo catalogue.json (1,344 entries) and research/leads.json (1,116) searched by regex for Renard / Saint-Mauris / PP1 / Granvelle: 45 and 9 matches, read by eye; DECODE searched for "Renard" and "Mauris".
11. Not done: no change to any repo, no commit, no PR, no DECODE edit, nothing sent. No project check tool applies to this folder (`docs/_check_writeup.py` and `_check_profile.py` belong to the Cyphersolver checkout and were not run because nothing was written there).

Errors of mine found on the way: first seed read the repeated group as letter-by-letter "de tendes" (it is syllabic); my margin reading "chaulux prevost" is contradicted by the cipher, which spells "chauvey secretaire" (FR_CLEAR.txt left as frozen, flagged [?] there).
