# Scope and reproducibility

All scripts and outputs are confined to this directory. Run `bash run_search.sh` here to reproduce the computation, using the saved corpus and supplied tables. `fetch_sources.py` separately records curl attempts; it does not need to succeed to reproduce this run.

## Inputs and limitations

369 numeric groups, 216 distinct; 132 groups below 100. Comments, graphic-symbol markers, and the illegible nonnumeric marker are excluded. No word boundaries are inferred from asterisks.

WE028 has all 1600 entries. Armstrong THE=972 uses the first `v` for each of 760 entries in the user-supplied JSON. Its historical full size is not established by that partial JSON (largest known index 1687); **1700 is an explicit assumed modulus**, consistent with the usual diplomatic code size. No modulo-760 reinterpretation of the sparse key was made. Direct transformations do not depend on this modulus beyond the permitted number range. Lack of signal with this incomplete key is weak evidence against that code.

Both requested Cryptiana pages failed fresh curl with DNS resolution errors. Web fetches returned HTTP 503. The already-present cached pages were inspected: no direct Weber code-transcription .txt links occur; the one .txt link is an Archive.org historical book. No additional code table was acquired. Consequently the conclusion covers only the two supplied keys, not all Weber codes.

Training corpus: seven downloaded web extracts from Project Gutenberg's *Pride and Prejudice* (1813), 125680 alphabetic characters after removing the later introduction, bracketed illustrations/copyright captions, and chapter headings. Raw excerpt text, source URL/line ranges, and hashes are saved. Federalist was considered but not used. No candidate plaintext or claimed AFIO solution was used for training.

## Language score

A proper add-0.1 smoothed conditional character **bigram** model is trained after lowercasing and stripping everything except a-z. Codebook outputs, including syllables, are concatenated without spaces. Score is mean natural-log likelihood per character, including a unigram probability for the first character. Higher is better. This low-order model measures local English character plausibility, not semantics or grammatical coherence.

Unknown/missing entries decode to five question marks. The unknown character has probability 1e-6; the remaining mass goes to the trained letters. Known-entry coverage is reported separately. No missing group is silently dropped, and partial-key raw scores should not be directly compared with complete-key scores.

## Exhaustive transformation families

Define `wrap_N(z)=1+(z mod N)`, residues 0..N-1. Each family is tested separately; arbitrary compositions of different families are not included.

1. Direct `y=x+k`: every integer k from -1899 through N-1 (all shifts with any possible valid lookup).
2. Modular `y=wrap_N(x-1+k)`: all N shifts.
3. Decimal digit reversal, without zero padding.
4. All 24 permutations of four-digit zero-padded numbers, including the last-two-digit swap and padded reversal.
5. Every one of 10000 independent decimal-position offsets, each digit modulo 10 (no carries).
6. Independent modular shifts for x<100 and x>=100: every N² pair.
7. `y=wrap_N(a*(x-1)+b)`: all gcd(a,N)=1 and all b, including multiplication-only maps and their inverses.
8. Independent direct shifts for the two number classes: every pair that can map at least one member of each class to a valid table index.

Out-of-range results are unknown. Page/row splitting is not tested. There are 9367227 parameter settings for WE028 and 10281027 for Armstrong972, including duplicates across families.

## Controls and verification

C++ mt19937 seed 18080220 generates 200 permutations, preserving the exact ciphertext frequency histogram; the same permutations are used for both keys. Saved shuffle index files eliminate dependence on standard-library shuffle implementations. **Every family search is repeated on every permutation**, retaining its optimum. Code-level controls additionally take the maximum over all eight families. These are search-adjusted controls, not fixed-winner reshuffles.

An exact, order-independent upper bound accelerates search: the internal-token likelihood is fixed; each cross-token transition is bounded by its best possible successor/predecessor character, with start/end correction. Candidates that cannot beat a control's current best are skipped. This is exhaustive optimization with pruning, not a beam or shortlist search. Each decimal/numeric candidate is still examined for the five frequent-group mapping test before any pruning.

`z=(observed optimum - mean shuffled optima)/sample_sd(shuffled optima)`. Empirical one-sided p uses `(1 + number of shuffled scores >= observed)/201`. An exploratory multiple-comparison control takes the largest standardized z across all 16 code/family combinations, applying the identical operation to each shuffle; its p is 0.402985. With only 200 controls, tail resolution is limited; z is descriptive, not an assumption of Gaussian tails.

An independent Python scorer reconstructed and verified all 3216 reported family/control winners. Maximum score disagreement was 9.24e-14. The top candidates remain incoherent and show no convincing signal. This does not prove that no private modification of an existing code was used.
