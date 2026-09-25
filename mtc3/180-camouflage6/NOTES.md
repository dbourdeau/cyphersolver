# MTC3 180: Monoalphabetic Substitution with Camouflage, Part 6 (Veselovsky, 2012)

Status: in progress (24 Sept 2026). Breakthrough: pieces are being recovered one at a time (3 of 9 so far); see "Method that works".

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

The plaintext is a sequence of copyrighted song lyrics; it is kept only in the session scratchpad, not in the
repository (and the answer, a single non-lyric sentence, will go in `private/`).

## Remaining gaps

The whole plaintext. The blocker is search, not identifiability: at the true key every model used scores far above
what the annealer finds.

## Escalation

Ideas not yet tried: a solver that builds one piece at a time with a model trained on English with letters deleted
(scoring partial alphabets correctly); population annealing with crossover of whole alphabets; a word-level model.
