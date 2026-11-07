# Hypothesis-testing process (rebuilt around the wiki)

**Goal.** A validated reading of the inspectors' telegram (Steenackers to Mercadier, 2 Nov 1870; 736 coded groups, 343 distinct, 437 clear words), measured as the share of coded group occurrences with an accepted
reading (`coverage`) and the share of sentences whose coded tokens are all accepted. The repo's read bar is 95% of tokens read as sense; the current state is on the front page of `index.md`.
Second goal: a table of reliable values for the Favre/delegation code (`lexicon_favre.json`) for Pillon.

**Principle.** Knowledge compounds: an accepted reading becomes a hard constraint for the next proposal (it supplies a known neighbour word, a known piece in a spelled run, a fixed point in the alphabetical order).
Everything the engine does is a test with a number; nothing is accepted on plausibility.

## One loop
1. **State** (read the wiki): accepted lexicon entries (status supported/established), constraints from supported claims (alphabetical layout C001, bracket-spelling C002, bias +0.015, sigma 0.02), open questions.
2. **Units**: every undecided coded group is a *word unit*; every maximal run of 2-6 groups is a *spelled unit*. Contexts: for each occurrence, the neighbouring clear word or accepted reading (left and right).
3. **Proposals**: for each unit, the top candidates by position fit + frequency + bigram context summed over all occurrences of the unit's signature; margin = best minus second-best total score (nats).
4. **Test battery** per proposal: T-fit (every piece within 0.02 of its alphabetical position); T-context (margin >= M); T-null (margin above the 95th percentile of margins obtained with *random group values* in the same contexts: controls for contexts that favour any frequent word);
   T-replicate (units with >= 2 occurrences: the top candidate is the same using odd and even occurrences separately).
5. **Gate** (calibrated, see step 8): accept if fit, context, null and (replicate or single occurrence with margin >= 2M) all pass. Accepted -> lexicon (`auto: true`, status supported), a claim page, a log line.
   Rejected with a clear reason (e.g. fit fails) -> a rejected claim page only when the hypothesis was worth recording; otherwise a log line.
6. **Re-validation**: each previously auto-accepted entry is blinded in turn and re-derived; entries the engine can no longer recover are demoted to hypothesis (logged).
7. **Measure**: coverage, number of auto entries, gold-blind accuracy (the gold entries from the wiki, blinded: precision and recall of the gate).
8. **Calibration (before loop 1)**: blind the supported entries, run steps 2-5 on their units and count correct/incorrect accepts; M is the smallest value with no incorrect accept on the gold set. The calibration result is written to a test page.
9. **Stop** after 3 consecutive loops with no new accepted entry and no change in coverage; write the final state and the open questions to the wiki; run lint.

## What the engine cannot do
Set `established`; resolve a name (it proposes strings, a person must be identified from sources); read a spelled word whose pieces are not in the candidate vocabulary; decide beacon semantics (Q03).
Those go to the question pages and, where useful, to Pillon.
