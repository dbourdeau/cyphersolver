# PLAN: solve the Holger Vind letter cipher (unit 260610, image 126 right)

Written by an AI agent (Claude Opus 5.5) on 26 Nov 2026 UTC, after transcribing the cipher lines and before any solving.
Frozen by SHA-256 (recorded in WORKLOG.md). Changes after the freeze go into NOTES.md as labelled deviations.

## Seen before this plan (disclosed)
- The clear text below the cipher and the heading (see transcription header). The heading is the old riddle for AVE.
- Letter counts by eye only: p and q are very frequent, "pq" often ends words. No value was tried for any sign.

## Method
1. Model: simple (monoalphabetic) substitution, one plain letter per cipher sign, Latin (i=j, u=v), word divisions as written.
2. Solver: hill-climbing with random restarts over substitution keys, scored by a letter 4-gram model built from the
   Latin lexicon of the upstream clone (`lang/lexicons/la.json.gz`, read only), words weighted by frequency, with word
   boundaries. Script `scripts/solve.py`, seed fixed.
3. If simple substitution fails the pass mark, next try (labelled as after the plan): homophones (two signs for one letter),
   then the keyword alphabets of the same file (images 133-137, "Danus ..."), then other sheets.

## Pass mark (registered)
- **Held-out test.** A key is built by the solver from lines 1-6 ONLY. Unchanged, it decodes lines 7-12. It passes when at
  least 80% of the held-out cipher words decode to words of the Latin lexicon (any frequency) AND the held-out Latin
  4-gram score per letter is better than all of 1,000 controls in which the key's plain values are shuffled among its signs
  (seed 20261126).
- **Second control.** The full solver, run the same way on 20 random permutations of the cipher letters (word lengths kept),
  must score clearly worse (every permuted run's per-letter score below the true solve's).
- **Read.** The project bar: 95% of cipher words read (a word needing an emended or supplied letter counts as a hole).
  A sign value fixed by hand after the held-out test is counted and listed as post hoc.

## Counts
Cipher words as written (hyphenated words joined), strict: read / holes, by script.
