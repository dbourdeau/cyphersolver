# MysteryTwister (MTC3): LLM track and candidate challenges

Research date: 24 September 2026. Web research only: no account, no login, nothing submitted.

The solver counts below come from the site's own public data (no login needed). They are the JSON the site's
pages load, fetched directly:

- challenge list (all 380, with level, author, publication date, solves, file links):
  `https://mysterytwister.org/challenges.data?more=400` (React Router "turbo-stream" format)
- per-challenge solver list, with a per-solve `used_llm` flag:
  `https://mysterytwister.org/challenge-hof?challenge_id=<id>&page=<n>`
- rankings: `https://mysterytwister.org/internal/rankings?board=llm&include_other=false&timeframe=all_time`
- public profiles: `https://mysterytwister.org/internal/public-profile?user_id=<id>`

The full table (284 challenges at levels 2, 3 and X; human and LLM solvers; first LLM solve; solution-public
date) is saved next to this file as `mtc3_challenges_l2_l3_x.csv`.

---

## 1. How the site is organised

- **Domain.** `mysterytwisterc3.org` returns a 301 redirect to `https://mysterytwister.org/`. The site says
  "Powered by the CrypTool project, © 2009-2026". The home page shows 380 challenges and about 14,970 members.
  (https://mysterytwister.org/)
- **Levels.** The About page says level 1 is easy (for example Caesar) and level 3 is hard ("breaking modern
  encryption algorithms such as AES"). It adds: *"Level X challenges are particularly mysterious and deal with
  unsolved cryptographic problems."* (https://mysterytwister.org/about)
- **Counts** from the challenge list: level 1 has 96, level 2 has 188, level 3 has 78, level X has 18; 380 in all.
  (challenges.data)
- **Challenges solved at least once.** The rankings page shows these counts on both boards:
  - Human board: level 1 96/96, level 2 177/188, level 3 37/78, level X 11/18.
  - LLM board, counting only LLM solves: level 1 94/96, level 2 172/188, level 3 35/78, level X 2/18.

  (https://mysterytwister.org/rankings ; `/internal/rankings?board=llm&include_other=false`)
- **Submitting a solution.**
  - Registration is required.
  - Levels 1-3 are checked automatically. *"The solution can be the plaintext, the key, or a secret codeword
    hidden in the plaintext."*
  - Each challenge allows a limited number of attempts: 15 by default, 20 for some (the `attempts_allowed` field).
    *"Once you exhaust all attempts, you cannot submit additional answers."*
  - Level X is not checked automatically: *"you need to contact the MysteryTwister team via email. They will check
    your solution, and with your permission, publish your results."* (https://mysterytwister.org/about)
- **Points.** Level X points are awarded by hand. Levels 1-3 score 10^i·10 / f(d), where d is the number of days
  between publication and the solve. Points decay slowest at level 3. (https://mysterytwister.org/points)
- **Materials are public.** Challenge PDFs and add-on files download without a login. For example
  `/media/challenges/pdf/mtc3-lasry-31-Sigaba-06-en.pdf` returned HTTP 200, 2.2 MB. Each challenge has public and
  "solved" Discord channels. The Discord links need a login, so I did not read them.

## 2. LLM rules and the LLM ranking

Everything below comes from the text of the site's own front-end code (the public JS bundles). No separate rules
page exists. The About page does not mention LLMs or AI.

- **Every submission must declare LLM use.** The submit dialog has a required radio question, *"Did you use an LLM
  to solve this challenge?"*, with the options "No LLM used" and "Used an LLM". Its tooltip reads: *"AI is allowed,
  choose "Used an LLM" if an AI did more than half of the work on your solution."*
  (https://mysterytwister.org/assets/ChallengeCard-CpSSFfPe.js)
- **Model name.** If "Used an LLM" is chosen, an optional free-text field **"Model used"** appears, with the
  placeholder "e.g., Claude Mythos 5". (same file)
- **No prompts or transcripts are asked for.** The form has only the solution field, the LLM yes/no question and
  the model field. I found no field for prompts, transcripts or method, and no rule forbidding any kind of tool
  use. Level X solutions go by email, so the team could ask for more there. I could not verify that.
- **Two Halls of Fame.** The ranking tooltip reads: *"There are two rankings: users whose correct solutions are at
  least 50% LLM-assisted appear in the LLM Hall of Fame, everyone else in the Human Hall of Fame."* The empty-board
  text reads: *"Users move here once at least 50% of their solves are LLM-assisted."* Each board has a toggle,
  "Include LLM solves" or "Include human solves". (https://mysterytwister.org/assets/rankings-C73eL20U.js ;
  https://mysterytwister.org/rankings)
- **Labels on individual solves.** The per-challenge Hall of Fame puts an "LLM" badge on each LLM-flagged solve,
  and the home page's "Recent solves" marks them "LLM solve".
  (https://mysterytwister.org/assets/ChallengeCard-CpSSFfPe.js ; https://mysterytwister.org/)
- **Profiles.** Public profiles carry a `classification` ("llm" or "human") and an `llm_ratio`. For example:
  - luigylemon: joined 24 June 2026, llm_ratio 0.958.
  - Ron Stoner: joined 22 June 2026, llm_ratio 0.954.
  - Apoorv Raj Saxena: joined 28 June 2026, llm_ratio 1.0.
  - chinafish: joined 2018, classified "llm" with llm_ratio 0.062. This does not match the 50% rule and is
    unexplained.

  (`/internal/public-profile?user_id=16532|16526|16538|10424`)
- **The LLM board is new.** Its top players all joined in June 2026. Their first LLM-flagged solves are dated
  22 June 2026 onward. Nearly all LLM-flagged level 3 solves were made between 22 June and 18 September 2026.
  (challenge-hof data)
- **LLM Hall of Fame, top 6 by points (L1/L2/L3/LX solved).** (https://mysterytwister.org/rankings?board=llm)

  | Rank | Player | Points | L1/L2/L3/LX |
  |---|---|---|---|
  | 1 | luigylemon | 563,890 | 94/161/33/0 |
  | 2 | chinafish | 536,039 | 93/171/26/0 |
  | 3 | Apoorv Raj Saxena | 512,332 | 92/149/29/1 |
  | 4 | Ron Stoner | 443,351 | 67/125/26/0 |
  | 5 | Martin Pescador | 414,498 | 91/106/25/0 |
  | 6 | jgamblin | 307,982 | 85/101/14/0 |

  The top human is George Lasry: 517,594 points, 56/117/27/3. (https://mysterytwister.org/rankings)
- **Announcements.** I found no post about the LLM track on CrypTool's news page
  (https://www.cryptool.org/en/posts/), on Cipherbrain, or anywhere else on the web. It seems to be announced only
  on the site and probably on its Discord, which I could not read.

## 3. What LLMs have solved, and what only humans have

Method: every level 2, 3 and X challenge has a solver list, and each solve on it carries its `used_llm` flag.

### Solved only by LLMs, or by an LLM first ("none of us could solve")

These fit George's remark. Level 2 and 3 solves are checked automatically, so the solves are real. The model used
is not public.

| ID | Level | Challenge | Cipher | Solvers |
|---|---|---|---|---|
| 354 | III | The Heavy T52 Sturgeon Challenge — Part 8 (N. Kopal, 2020) | T52D teleprinter cipher; ciphertext and crib, key unknown | **1 solve, LLM only**: luigylemon, 18 Sept 2026. No human in six years. |
| 275 | II | Weakened Granit — Part 2 (J. Drobick, 2015) | simplified GRANIT (GDR double-transposition hand cipher); ciphertext only, first permutation key known | **1 solve, LLM only**: Ron Stoner, 27 June 2026. |
| 276 | II | Weakened Granit — Part 3 (2015) | as above, second key known | **LLM first**: Ron Stoner, 26 June 2026. Then chinafish, marked human, 6 Sept 2026. No human in the eleven years before. |

Sources: https://mysterytwister.org/challenges/level-3/the-heavy-t52-sturgeon-challenge-part-8 ;
`/challenge-hof?challenge_id=354|275|276`

Two more "no human had solved it" cases involve chinafish's ambiguous account:

- **284, A Heavy SZ42 Challenge — Part 14** (level III, Lorenz SZ42, ciphertext only). No one solved it from 2022
  until chinafish (marked human) on 23 July 2026, then luigylemon (LLM) on 11 Sept 2026.
- **112, ASAC Part 5** (level II, strengthened ADFGVX). Only solver: chinafish (marked human), 6 Sept 2026.

chinafish sits on the LLM board and solved about 7 old level II challenges in one batch on 6 Sept 2026. Treat these
two as "probably LLM-assisted, not declared".

### Not real cryptanalysis

- **313, RSA-260** (level III). The first solves were tony and metowolf (LLM) on 3 Sept 2026, then Theofanidis
  (human) on 4 Sept and luigylemon (LLM). Eric Lu published a factor on 3 Sept 2026, and the site set
  `solution_public_at` to 3 Sept 2026. These solves are look-ups.
  (https://www.johndcook.com/blog/2026/09/03/new-rsa-number-factored/)

### Level III challenges an LLM also solved (after humans)

LLM-flagged solves exist on 35 of the 78 level III challenges. They include:

- Handycipher 3-9 and Extended Handycipher 4-6
- Heavy T52 Sturgeon 1-7 and 9
- SIGABA Challenge 3, 4 and 5, and Sigaba Part 2
- ORYX 4b
- Substitution Cipher with Non-Prefix Codes (346). Its only earlier solver was Peter Mustermann in 2013.
- Heavy SZ42 14
- Elliptic Boogaloo 2 and 3, Vinaigrette signature, CMEA 2, RSA with special d, RSA-232/240/250

(`/challenge-hof`; the CSV)

### Level X

The only LLM-flagged level X solve is **376, The Vatican Challenge — Part 4** (George's own challenge; a nunciature
cipher, ASV Segreteria di Stato Portugal, 1535/36). Solvers:

- Thomas (human), 22 Aug 2019
- Apoorv Raj Saxena (LLM), 15 July 2026

Level X is checked by hand, so the team accepted this LLM solution. (`/challenge-hof?challenge_id=376`)

### Solved only by humans (no LLM-flagged solve)

**Level III: 4 challenges**

| ID | Challenge | Human solvers | Cipher / notes |
|---|---|---|---|
| 359 | The SIGABA Challenge — Part 6 (Lasry, 2020) | **1**: Jerva, 2021 | SIGABA, partial known plaintext, no key information. LLMs solved parts 3-5. |
| 342 | SIGABA CSP-2900 — Part 3 (Kopal, 2021) | 2: Jerva, George Lasry | 200-character ciphertext, 100-character partial crib |
| 343 | SIGABA CSP-889 — Part 3 (Kopal, 2021) | 2: George Lasry, Jerva | same |
| 292 | ElsieFour — Part 1 (Rotthaler, 2017) | 4: Jerva, Michael Möller, D3d4lu5, Eugene | LC4 (RC4, Playfair and plaintext-dependent keystream); two messages, same key, partial known plaintext |

**Level X: 10 challenges.** 363, 364, 365, 368, 370, 371, 374, 375, 377 and 380 have human solves only.

- 364 Catherine of Aragon 1509 (Tomokiyo): 2 solvers.
- 368 Double Column Transposition (Schmeh): 2 solvers, Lasry and Gillogly, 2013.
- 380 Unknown Author (1808): 2 solvers.
- 371 Notes of an Italian Soldier: 4 solvers.
- 374 and 375, Vatican 1 and 2: 3 solvers each.
- 377 Vatican 5: 3 solvers, Dropflux, Simon Klee and AndrewEpstein, 14-18 Sept 2026. Solution made public
  16 Sept 2026.
- 363 Beale: 1 solver, Seth Kintigh, 2011, as listed.

Most of these have **public solutions**: 364 in 2022, 368 in 2014, 371 in 2014, 374/375 in 2018, 380 in 2016 and
377 in 2026. That is a contamination risk.

**Level II, human only and at most 2 solvers** (models have not reached these):

- 207-210, SIGABA CSP-2900 and CSP-889 Parts 1-2: Jerva and Lasry only
- 180, Monoalphabetic Substitution with Camouflage — Part 6: Peter Mustermann and Lasry
- 273, Weakened ElsieFour — Part 2: Lasry and chinafish
- 110, ASAC Part 3: Emanuele and chinafish

### Unsolved by anyone (0 solves)

**Level III (39 challenges).** Most are RSA-270 to RSA-2048, AES-65-bit, FHE key recovery and DSA
medium-field. These are compute problems, not cipher-breaking. The classical-style ones are:

- 287/288/289, Double Column Transposition Reloaded 1-3 (A. Wacker, 2013)
- 345, Spirale — Part 4 (hand one-time-pad-style cipher, 485 letters)
- 303/305, ORYX 4d/4c (LFSR stream cipher)

**Level II (8 challenges):**

- 126-128, Double-Column Transposition/Granit 1-3 (Drobick 2015; 70-, 110- and 80-character ciphertexts)
- 111, ASAC Part 4 (the main ASAC challenge)
- 163, Kaskade-S/T Part 4
- 227, Hutton Cipher Part 5
- 231, Lady Liz
- 235, "The Road" Part 3

**Level X (7 challenges):**

- 366 D'Agapeyeff, 367 Dorabella and 369 Kryptos. These are on the project's FAMOUS list, so they are out of the
  paper data.
- 372 Spanish Strip Cipher Part 3. The page now says *"As of July 2026, no new solutions are accepted. We try to
  verify existing submissions."*
- 373, the third ENIGMA M4 message. Its `solution_public_at` is set to 2013-12-31, but it shows 0 solves.
- 378, Vatican Part 3 (1721). Solution public since 2022, but 0 solves recorded.
- 379, Twelve-Year-Old Murder Case (the McCormick notes).

## 4. Shortlist for an LLM attempt

Priorities: (a) no LLM has solved it yet, so a solve would be a first for the LLM board; (b) few solvers or none;
(c) a classical or machine cipher of the kind our tooling handles; (d) checked automatically (levels II and III),
so the outcome is objective; (e) the solution is not published, so contamination is low.

| # | ID | Level | Challenge | Cipher | Solvers | Why |
|---|---|---|---|---|---|---|
| 1 | 287 (then 288, 289) | III | Double Column Transposition Reloaded — Part 1 | double columnar transposition; Part 1 keys come from English sentences | **0 ever** (since 2013) | Nobody has solved it. Lasry's own published DCT attack (Cryptologia 2014; https://www.cryptool.org/en/posts/solving-double-column-challenge/) exists to build on. Parts 2 and 3 get harder: interleaved texts, then German with random keys. A first solve here would be the "LLM beats humans" result. |
| 2 | 359 | III | The SIGABA Challenge — Part 6 (Lasry) | SIGABA, partial known plaintext, no key information | 1 human, 0 LLM | The hardest SIGABA step not yet done. LLM solvers already cleared parts 3-5, so it is within reach. George wrote it and can judge the method. |
| 3 | 342, 343 (ladder 207-210) | III (II) | SIGABA CSP-2900 / CSP-889 — Part 3 (Kopal) | SIGABA variants; 200-character ciphertext, 100-character crib | 2 humans each (Jerva, Lasry), 0 LLM on all six | A graded series of six that only two humans have finished. No LLM has touched it. |
| 4 | 292 (then 273) | III (II) | ElsieFour — Part 1 | LC4; two messages under one key, partial known plaintext | 4 humans, 0 LLM | A modern hand cipher, so there is little training-data leakage. Part 2 of the weakened version is a warm-up with 2 solvers. |
| 5 | 126-128 | II | Double-Column Transposition/Granit 1-3 (Drobick) | GRANIT (GDR spy cipher: substitution checkerboard and two transpositions); Part 1 adds a codebook | **0 ever** | The natural next step after the LLM-only Weakened Granit 2/3 solves. The ciphertexts are very short (70-110 characters), so it may be hard or ambiguous. |
| 6 | 111 | II | ASAC Part 4 | strengthened ADFGVX (three steps, double column transposition) | **0 ever** | The main challenge of a series whose weaker parts LLMs and chinafish have broken. |
| 7 | 180 | II | Monoalphabetic Substitution with Camouflage — Part 6 | substitution hidden among nine camouflage alphabets | 2 humans (2012, 2023), 0 LLM | Classical, fits our annealing and language-model tools, and cheap to try. |
| 8 | 345 | III | Spirale — Part 4 | hand one-time-pad-style cipher; 485 letters, four new random keys, ciphertext only | **0 ever** | The earlier parts are solved, so a weakness likely exists. The risk is that it was designed not to be breakable. |
| 9 | 364 / 378 | X | Catherine of Aragon 1509; Vatican Part 3 (1721) | historical nomenclators, our core subject | 2 humans / 0 recorded | Closest to our historical work, but both solutions are public (2022), so contamination is high. Only worth doing as a declared "published solution exists" control, and level X means an email submission. |

Not recommended:

- Level III RSA, AES-65, FHE and DSA challenges: raw compute, not cryptanalysis.
- 379 (McCormick), 373 (third M4 message) and the famous level X ciphers: open research problems, and the famous
  ones fall under the project's FAMOUS exclusion.
- 372 Spanish Strip Part 3: closed to new solutions.

## What I could not verify

- **Model and conversation data.** The site asks for the model name, but no public endpoint exposes it, so I cannot
  say which models solved T52 Part 8 or Granit 2. Whether transcripts or write-ups are requested after an LLM solve
  is not visible. The `writeup_id` field exists on challenges but is null on all of these.
- **Discord.** The Discord channels, where announcements and solver discussion probably live, need a login. I did
  not read them.
- **Other announcements.** I found no public news post, blog entry (Lasry, Schmeh/Cipherbrain, CrypTool) or article
  about the LLM ranking.
- **Challenges pre-dating the 2023 site relaunch.** Some old Hall of Fame data may be incomplete. For example,
  Vatican 3 shows 0 solves although its solution has been public since 2022.
- **The `used_llm` flag is self-declared.** chinafish's human-flagged solves in 2026 are ambiguous: the account is
  on the LLM board, but its `llm_ratio` is 0.062.
- **George's "two or more".** He did not name the problems. The only fully LLM-only solves in the data are 354 and
  275, with 276 solved by an LLM first. That fits his remark, but it is my inference.
- **Related but not MysteryTwister.** Claude Fable 5.1's solve of Urquhart's Cyphral Distich (Sept 2026) is a
  separate story (https://www.vals.ai/blogs/fable-solves-cyphral-distich ;
  https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html).
