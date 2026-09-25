# MTC3 110: ASAC – A Strong(er) ADFGVX Cipher, Part 3 (Fendt, 2016)

Status: no write-up (MTC3 challenge, not a cipher target). Solved 25 Sept 2026, not yet submitted; answer in `private/`.

Level II. Human solvers before this: Emanuele, chinafish; no LLM solve.

## The cipher (from the challenge's own C++ source, `Sourcecode/` in the add-on zip)

1. 10x10 Polybius square: digits 0-9, then space + alphabet (A, I, O, U twice, E four times) repeated until full; rows
   rotated right by password1 letters 11-20 ((letter-'A') mod 10), then columns rotated down by letters 1-10. Each
   character becomes two digits (column, row) and has several homophones.
2. Keystream: a second 10x10 square, every row 0123456789, rotated the same way with password2; read row by row, the
   100 digits are added mod 10 to the step-1 digits (period 100).
3. Part 3: one columnar transposition (Part 4: two).

Our reimplementation (`src/asac.py`) reproduces the worked example of the Part 1 PDF digit for digit (the PDF prints a
`5` of the square as `S`).

## The weakness: rand() is never seeded

`PolybiusSquare::encode` picks the homophone as the first cell of the character at or after `rand() % 100`, and the
program never calls `srand`. Both bundled executables use the MSVC runtime, so every run replays the MSVC LCG from seed 1
(`s = s*214013 + 2531011`, output `(s>>16) & 0x7FFF`). Checked: Part 1 cells match 438/438 (glibc's rand: 194/438), and
Part 2 matches 692/692 with its true key (an equivalent key that gives the same text matches only 427/692).

So for character i the draw r_i is known and its cell lies a little after r_i: the row digit y_i - floor(r_i/10) (mod 10)
is 0-3 in 80% of cases (0.186 log10 of information per row digit against a uniform guess), the column digit almost
nothing. The distance cell - r_i averages 21 cells (`pd.txt`).

## Solution path (all in the session scratchpad; sources copied to `src/`)

1. Parts 1 and 2 as calibration (both already solved by others): Part 1 by annealing the 20 square digits with a
   28-symbol German 5-gram (`lmde/`, built from `lang/corpora/de-gutenberg.txt`); Part 2 in two phases (keystream
   first, by the coincidence count of the aligned cells, which ignores the square; then the square). Both read German
   Wikipedia text (primes; the Emscher).
2. Part 2's key is not reused in Part 3 (no width 20-110 shows the known-key "triple" signal).
3. `asacy.cs`: for each width L, anneal the 15 keystream digits that act on row digits (base sequence v = -row shifts,
   and the 5 odd column shifts); fitness = sum over cipher columns of the best (natural column, start offset) score of
   (digit - floor(r_i/10) - keystream). Synthetic check (L=60): 6/8 restarts converge to the true key (up to rotation).
   Real Part 3: only **L = 22** converges, three restarts to rotations of the same keystream, score 212.8 = 11 row-digit
   columns of 132 rows at their true places.
4. `asac3d.cs`: place the 11 row-digit columns; brute-force the 5 remaining keystream digits (100,000 combinations,
   precomputed tables) with a greedy placement of the 11 column-digit columns scored by the cell-distance distribution;
   rebuild the stream (column offsets come out exactly consistent); anneal the square with the German 5-gram.
5. Result: German Wikipedia text on amateur radio, 1451 characters, **every cell consistent with the replayed rand()
   (1451/1451)**. Answer = words 20-22 run together, in `private/ANSWER.txt`.

Note: the author's rule "transposition key longer than sqrt(2N)" (here 54) was not followed; the key has 22 letters.

## Remaining gaps

None in the plaintext. Open only: the site's confirmation.

## Escalation

Done (see above).
