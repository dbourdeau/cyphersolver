# Log (append-only)

Format: `## [date] kind | subject` then one or two lines.

## [2026-11-07] ingest | first ingest of the project state
Seeded sources S01-S09, entities E01-E07, systems Y01-Y04, tests T01-T12, claims C001-C031, questions Q01-Q08 and the two lexicons from NOTES.md and the session's analyses (`tools/seed_wiki.py`).
Contradictions recorded: C018 (Pillon's Mercadier decomposition) rejected by T11 and withdrawn by Pillon; C013 (Vinoy) downgraded after T06; C015 negates three of Pillon's readings; C019 corrects my earlier ACK/N readings.

## [2026-11-07] loop | engine loop 1
444 proposals, 6 accepted (C100, C101, C102, C103, C104, C105), 0 demoted; coverage 12.5% -> 19.7%.

## [2026-11-07] loop | engine loop 2
430 proposals, 0 accepted (none), 0 demoted; coverage 19.7% -> 19.7%.

## [2026-11-07] loop | engine loop 3
430 proposals, 0 accepted (none), 0 demoted; coverage 19.7% -> 19.7%.

## [2026-11-07] rollback | engine loop 1 acceptances reverted
Loop 1 (gate M=2, margin + null + replicate only) accepted six units: 2207=de, 9904=vous, 3421=et, 5006=la, 5021 2704=le (spelled as l|e) and 4914 7504 7607 6009=insurrection (spelled insu|r|rectio|n). Review found them unsupported: frequent function words chosen by prior and position with almost no contextual evidence, and one nonsense spelling. Reverted: claim pages C100+ removed, lexicons re-seeded. Lesson recorded in T13/C031: acceptance must require context evidence beyond the frequency prior (a context margin), because the null on margin does not control for positions that sit next to a very common word.

## [2026-11-07] loop | engine loop 1
444 proposals, 1 accepted (C100), 0 demoted; coverage 12.5% -> 13.0%.

## [2026-11-07] loop | engine loop 2
441 proposals, 0 accepted (none), 0 demoted; coverage 13.0% -> 13.0%.

## [2026-11-07] loop | engine loop 3
441 proposals, 0 accepted (none), 0 demoted; coverage 13.0% -> 13.0%.

## [2026-11-07] loop | engine loop 4
441 proposals, 0 accepted (none), 0 demoted; coverage 13.0% -> 13.0%.

## [2026-11-07] rollback | engine run 2 acceptance reverted
The corrected gate (context margin >= 3) accepted one unit: 5021 2704 = le, spelled l|e from a single occurrence in an unbracketed run. Unsupported (a two-letter word spelled in two pieces). Reverted. Added two structural rules from the supported claims: spelled units only for beacon-bounded runs (C002; free segmentation gave +0 in T08) and at least 4 letters for a spelled word.

## [2026-11-07] loop | engine loop 1
355 proposals, 0 accepted (none), 0 demoted; coverage 12.5% -> 12.5%.

## [2026-11-07] loop | engine loop 2
355 proposals, 0 accepted (none), 0 demoted; coverage 12.5% -> 12.5%.

## [2026-11-07] loop | engine loop 3
355 proposals, 0 accepted (none), 0 demoted; coverage 12.5% -> 12.5%.

## [2026-11-07] loop | engine loop 1
356 proposals, 2 accepted (C106, C107), 0 demoted; coverage 12.5% -> 13.8%.

## [2026-11-07] loop | engine loop 2
351 proposals, 0 accepted (none), 7 demoted; coverage 13.8% -> 9.9%.

## [2026-11-07] loop | engine loop 3
362 proposals, 2 accepted (C108, C109), 0 demoted; coverage 9.9% -> 12.5%.

## [2026-11-07] loop | engine loop 4
356 proposals, 2 accepted (C110, C111), 8 demoted; coverage 12.5% -> 9.7%.

## [2026-11-07] loop | engine loop 5
357 proposals, 2 accepted (C112, C113), 7 demoted; coverage 9.7% -> 12.5%.

## [2026-11-07] loop | engine loop 6
356 proposals, 2 accepted (C114, C115), 8 demoted; coverage 12.5% -> 9.7%.

## [2026-11-07] rollback | engine run 3 (piece-consistency path) reverted
With the piece-consistency path on, the loop accepted 'picard' for 6816 1216 2112 and re-derived 'mercadier'/'pigeons' with different splits, overwriting supported entries (6129 on -> n, 4001 ge -> geo), then oscillated (7-8 demotions per loop). Causes: about 40 spelled units each tested at a 5% null give ~2 false accepts by chance (multiple comparisons), and the write-back overwrote accepted entries. Reverted to the seeded lexicon; piece path disabled (PIECE_PATH=False); write-back no longer overwrites accepted entries.

## [2026-11-07] loop | Favre engine and second-text test
Favre topic engine (T16): 628 = la before conference (p=0.004), 620/1908/1440 in the armistice cluster, 121/146 around sauf. Second-text overlap (T15): nothing above chance; no cross-validation text in the collection (C038, Q09). Domain language model from Steenackers 1883 in progress (page word counts via HathiTrust OCR).

## [2026-11-07] loop | engine loop 1
356 proposals, 0 accepted (none), 0 demoted; coverage 12.5% -> 12.5%.

## [2026-11-07] loop | engine loop 2
356 proposals, 0 accepted (none), 0 demoted; coverage 12.5% -> 12.5%.

## [2026-11-07] loop | engine loop 3
356 proposals, 0 accepted (none), 0 demoted; coverage 12.5% -> 12.5%.
