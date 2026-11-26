# eaglepass1917: plan for a one-alphabet solve, written before any solving

Written by an AI agent (Claude Opus 5.5), 23 Nov 2026, Eastern time, before any decipherment of the telegram was attempted in this task. No person has checked it. Its SHA-256 is recorded in `PLAN.sha256` before the first run.

## Item

Mexican embassy, Washington, to J. M. Arredondo, consul at Eagle Pass, 17 April 1917 (AHGE-SRE-AEMEUA leg. 507 exp. 6), pictured in Narváez 2019 p. 339 fig. 10. 246 cipher letters, transcribed twice (T1 = `output/ill_photo_leads_2026-11-23/work/test/T1_telegram.txt`; T2, blind = `.../work/blind/T2_telegram.txt`). They agree except at 12 letters T2 marks uncertain and one K/X (group SFCKY/SFCXY). The earlier Murciélago test with list word 31 (Escultor) missed and stays missed; this is a separate attempt.

Already known before this plan (from the earlier diagnostic): index of coincidence 0.071, flat over periods 1-12.

## Hypothesis and fixed alternatives

- H (main): one-alphabet simple substitution of Spanish, 26 letters, group spacing meaningless (word divisions lost). Spanish written without ñ and accents (ñ -> N, accents dropped) is the normalisation of the language model, so that alternative is built into every run.
- A1: the same, but also allowing that the cipher alphabet is a keyword-mixed alphabet: (a) after the free solve, test whether the recovered plain->cipher or cipher->plain alphabet is a keyword alphabet (a keyword followed by the rest of the alphabet in order), possibly shifted; (b) a direct search over keyword alphabets: keywords = MURCIELAGO plus every corpus word of 5-15 letters seen at least 3 times; alphabet = keyword without repeats + remaining letters in order; both directions (mixed as cipher row, or mixed as plain row), all 26 offsets. Scored with the same model.
- A2: transcription variants: T1 readings (default) and T2's first readings at the 13 doubtful places. Both solved.
- Nothing else. If none of these reads, report the statistics and stop (no transposition, no other Murciélago words, no code-book search).

## Language model (corpus), kept away from the test text

- Corpus C = (1) *Archivo Santander* vol. XIV (Bogotá 1918), Internet Archive OCR text already on disk, `sources/raw/ill_photo_leads_2026-11-23/archivosantander14bogo/archivosantander14bogo_djvu.txt` (letters of 1820s diplomats and officials); plus (2) the Spanish plain texts of Mexican 1906-1917 telegrams and letters read in the DB repo copy (`sources/raw/db_repo_2026-11-22/repo/targets/<t>/decryption*.txt`, `reading*.md`, for t in coahuila1906, delabarra1913, fuentes1914, gonzalez1913, hernandez1911, mccarty1911, mexico1911, murguia1914, nuevaclave1911, rubio1913, limantour1909, dallas1911, carranza1914). This is period Spanish diplomatic and telegraphic prose.
- Held out of C: target carranza1915 (used only for the controls below). Never in C: anything from the Narváez book or its OCR, and the telegram itself.
- Normalisation: lower/upper case folded, accents stripped, ñ -> N, everything not A-Z removed, word spaces removed for the n-gram counts.
- Model: letter 4-gram log probabilities (add-0.5 smoothing over 26^4), score = sum over all 4-grams of the text. A word list (corpus words seen >= 3 times) is kept only for the coverage measure.

## Solver

- Simulated annealing over the 26-letter cipher->plain key, move = swap two plain values; 20,000 steps per restart; temperature from 10 down to 0.2 geometrically; after annealing, a greedy hill-climb over all swaps until no gain. Start key = random permutation from the run's seed.
- Restarts: 40 per text. Seeds: controls 1-40 (shuffles: base seed 100, 200, 300; enciphered: base seed 400, 500, 600; restart seed = base + restart number), real text T1 base 1000, T2 base 2000, held-out (first 170 of T1) base 3000. Every restart's seed and final score is written to `runs/`.

## Controls (run first)

- S1-S3: three random permutations (seeds 11, 12, 13) of the 246 T1 cipher letters. Must FAIL.
- E1-E3: three 246-letter passages of real Spanish (letters 1-246, 247-492, 493-738 of carranza1915's decryption text, normalised as above), each enciphered with a random substitution key (seeds 21, 22, 23). Must SUCCEED.
- Pass marks (fixed now):
  - enciphered control succeeds = best-restart decryption has at least 90% of its 246 letters right;
  - shuffle control fails = its best score is below the lowest best score of E1-E3, and its best decryption shows no Spanish sentence of 5 or more consecutive words.
  - Method validated at this length only if all three E succeed and all three S fail. If not, the result on the real text is reported as "method not validated" whatever it shows.

## Success rule for the telegram

The telegram counts as read only if all hold:
1. The best decryption, divided into words by hand, builds Spanish sentences over at least 90% of the 246 letters (strict count: a word with any supplied or changed letter is a hole).
2. Its score lies above the best shuffled-control score (S1-S3).
3. Held-out check: solving only the first 170 letters gives a key under which letters 171-246 read without changing any value fixed by the first 170 (cipher letters absent from the first 170 are reported as unknown and counted as holes there).
Otherwise: "not read". A miss is reported as a miss.

## Coverage measure (reported, not the pass mark)

Fraction of letters inside words of 3+ letters in a best segmentation by the corpus word list (dynamic programming, maximum covered letters).

## Afterwards

If it reads: Spanish with word divisions and holes, English, the key, strict counts, the 12 uncertain letters (resolved only where key and photograph both support), and the comparison of the alphabet with the book's printed tables (page and figure cited only). If not: monogram and digram profile against Spanish, repeated sequences, and what they suggest; stop.
