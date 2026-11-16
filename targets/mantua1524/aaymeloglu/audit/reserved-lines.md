# Reserved control lines

Recorded 2026-11-15, before any refinement of the anneal5 key.

**Reserved: f. 68r lines 20, 21, 22, 23** (transcription-68r.tsv rows with line = 20..23; 31 cipher segments, 136 units (corrected count; first written as 34)).

Rules:
- These lines are dropped from every anneal run from anneal6 onward (`RESERVE` set in anneal6.py) and from the context lists (`dec6.py KEY --ctx`, which reads lib6.runs() without the reserved lines) used for value decisions.
- No value in DECISIONS.md may cite a word from these lines as support.
- At the end they are decoded once with the final key, and the share of real period-Italian words is compared with the same count under 200 permuted keys (`permutation_z_key`).

Caveat, stated now: the earlier anneal5 key was fitted on all lines including these, and its decode of the whole page (these lines included) was printed once during orientation, before this reservation was written. So the control is not fully blind: the starting key saw them. Re-anneals from here on do not.

## Scoring, frozen before any reserved-line decode (2026-11-15)

- **Units:** lib6.py DEFAULT_MERGE at the time of the final run (mi, oo, cc, dd, bb, lo, no, pa, la, bo, mo, gr, g1).
- **Word = one cipher segment** (one TSV row of kind=cipher). A segment that holds two words cannot hit; same rule under the null.
- **Lexicon:** word types occurring at least twice in the cipherkit `it` corpus (cleaner 2), normalised j->i, v->u, k->c, y->i, accents stripped, plus every word of the clear text of ff. 298r-v, 68r, 198r (same folding). No word read from any cipher decode is added.
- **Unread:** a segment containing a code sign (BOX, IZ, H, CROSS, C@) or a sign with no value in the final key (for example 8+, seen only on line 22) counts as a miss.
- **Report:** hits over all segments, and hits among segments that decode to 4+ letters (di/in/la/et hit easily by chance).
- **Null:** `cipherkit.controls.permutation_z_key`, score = the hit count above, n = 200, seed 0, nothing held fixed beyond the function's own rule (multi-letter values held).
- The raw decode of the reserved lines is reported first and as is. No image re-reading of lines 20-23 feeds the headline count; any later re-reading is reported separately.

## Outcome and later changes
- Frozen count (key as of the count, solve/controls6_frozen.json): 19 of 31 segments are lexicon words (null 4.8 +- 1.6, z 8.8); 10 of 20 4+-letter segments (null 0.06).
- Post-hoc (after the count): the `bu` merge was added on non-reserved evidence (altra, desideraria). It turns reserved 21.1 MOSTRABRE into MOSTRARE: 20/31, 11/20 (solve/controls6_posthoc.json). Reported separately; the headline stays 19/31.
- Two citations of reserved lines that crept into the working key notes (bo "questa 20", H "gagli-") were removed from key.json and DECISIONS.md; neither value depended on them.
- After the Codex review: transcription corrections at 23/4 and 23/5 give 22/31 and 13/20 (solve/controls6_postreview.json). The review is right that this is a fit-consistency check with leakage, not a held-out test (controls.md section 1).
