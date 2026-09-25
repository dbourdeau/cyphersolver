# MTC3 180: Monoalphabetic Substitution with Camouflage, Part 6 (Veselovsky, 2012)

Status: in progress (25 Sept 2026): all 9 pieces recovered and ordered, the odd sentence identified; awaiting the site's
verdict on the submitted answer (kept in `private/`).

Level II. Solvers: Peter Mustermann (2012), George Lasry (2023); no LLM solve.

## The cipher

- English plaintext, 1522 letters, cut into 9 contiguous pieces. Piece k is written in alphabet k (numbers
  26k..26k+25), the pieces are merged at random with each piece's order kept, and the 234 numbers go through a random
  permutation. The ciphertext is `ciphertext.bin`, one byte per letter; 194 of the 234 symbols occur.
- Answer: the sentence that does not fit the rest of the plaintext, in capitals with spaces.
- The worked example in the material zip (983 letters, key given) confirms it: the pieces are contiguous (lengths 73-145),
  the merge is a uniform random interleave (P(same group as the previous letter) = 0.113), and the key is a random
  permutation. The example plaintext is the History paragraph and the Darwin quotation of Wikipedia's "Camouflage"
  article (revision of 4 May 2012).

## What was tried (all in the session scratchpad; the tools were not kept)

Tested on the worked example and on synthetic ciphertexts of the challenge's size (9 pieces, 1522 letters).

1. Joint annealing over symbol -> (alphabet, letter), quadgram and interpolated 5-gram English models, Metropolis and
   heat-bath moves (every one of the 234 slots scored per step). Never reaches the true key from a random start; final
   states are at chance purity (4-6 of ~22 symbols from any one piece). From the true key with 2% of symbols disturbed
   it often fails to return: the landscape is a golf course, and one misplaced frequent symbol sets off
   compensating moves.
2. Scaling test on synthetics with 2, 3 and 4 alphabets: the annealer finds the key in 2 of 22 runs at 2 alphabets
   (the Part 5 setting) and in 0 of 22 at 3 or 4.
3. Left-to-right beam search (full, and one piece at a time): the true hypothesis falls out within 5-50 positions,
   because nine piece openings with little context leave far too many equally good prefixes.
4. Letter-free statistics: pairwise co-occurrence and the order in which two symbols interleave pick same-piece
   partners at chance (11%); a letter-free Markov-evidence score for a partition prefers spurious partitions over the true one.
5. Robust scoring (context may skip one of the last letters, or treat the letter as an insertion): only a weak gradient
   towards purity.
6. Crib: the 2012 Wikipedia text following the example (Poulton, Thayer, Cott) is ~840 letters, too short for 1522; an
   article-weighted model did not make random starts converge even on the example.
7. Restricting to the 11 commonest letters (oracle-filtered synthetic): the true key scores only slightly above the
   annealer's optimum; too close to the unicity limit.

## Method that works (24 Sept 2026, `src/camograd.cs`)

Grow ONE piece at a time, letter by letter, and score each partial alphabet with a 5-gram model of English in which
all letters not yet chosen are deleted (`BuildLM(k)`: Gutenberg text filtered to the first k letters of the growth
order). A group that is correct for its first k letters then reads as "English restricted to those letters" and scores
well, while mixtures score like noise; this gives the gradient the joint annealer never had.

- Growth order THEANDOISRLCUMWFGYPBVKJXQZ: starting with T, H, E ("THE") separates true pieces from noise several
  stages earlier than the frequency order ETAOIN... (measured on clean synthetics built from prose).
- Beam over stages (100k-150k hypotheses), score = log-likelihood ratio against the restricted unigram model; from
  stage 13 a letter may be absent (rare letters may not occur in a piece).
- Synthetic check (`cs1`, 9 pieces, 1522 letters): the stage-12 top group had 11/12 letters right; hill-climbing then
  recovered the whole piece (22/22 letters) as readable English.
- Real ciphertext: peel the best piece (beam to stage 20), exclude its symbols, repeat (`src/peel3.sh`). A round whose
  best score is low is a mixture of pieces: a larger beam fixed round 2 (score 29 -> 63). Pieces 1-3 read as clean
  English (scores 56, 63, 80).
- `src/assemble.cs`: once pieces are separated, places the leftover rare-letter symbols and polishes each piece with the
  full 26-letter model.

### Last four pieces: joint annealing (25 Sept 2026, `src/jointcore.cs`, `src/jointfull.cs`)

Peeling stalled after five pieces: in the 97-symbol leftover pool no single-piece beam rose above noise (~22), even with
per-letter count bounds, E anchors, other growth orders and a domain model. What worked was solving the leftover pieces
jointly:

1. `jointcore.cs`: the top 48 symbols by count are annealed onto 4 pieces x 11 letters (THEANDOISRL), score = sum of the
   11-letter restricted 5-gram LLRs. Validated first on the ciphertext cut down to recovered groups 1-4 (known answer):
   one piece exact, two nearly, in 40M-step runs. On the real pool two pieces recurred across restarts (28.3, 20.1).
2. The clearer one was finished with CamoGrad's stepwise refine (score 76 at 22 letters) and removed; the joint core on
   the last 3 pieces converged identically in all 32 restarts.
3. `jointfull.cs`: 26-letter joint polish of those 3 pieces (every symbol in a slot or unassigned at NULLC=-3 log10 per
   letter): 166-173 letters each, -0.81 to -0.99 log10 per letter, readable English.
4. `assemble.cs` on all 9 groups placed the last 9 rare symbols: 9 pieces of 166-172 letters (1522 in all), -0.72 to
   -0.99 per letter. The pieces chain end-to-start into one continuous text (every cut falls mid-word and joins).

`diag.cs` scores each assigned symbol's keep-vs-pool LLR and the best placement of each pool symbol; it showed the five
peeled groups were clean (no stolen frequent symbols), which pointed at the search, not the exclusions, as the blocker.

## Result

The plaintext is two song lyrics run together; one piece carries a two-line sentence from a third, unrelated song,
inserted in the middle of a verse. That sentence (69 letters) is the answer. Key, piece order and the answer's position
are in `private/` (git-ignored); the plaintext is not reproduced here because it is copyrighted lyrics.

The plaintext is a sequence of copyrighted song lyrics; it is kept only in the session scratchpad, not in the
repository (and the answer, a single non-lyric sentence, will go in `private/`).

## Remaining gaps

None in the plaintext (all 1522 letters placed and read). Open only: the site's confirmation of the answer.

## Escalation

Done: single-piece growth (5 pieces), then joint core + full polish for the last 4 (see above).
