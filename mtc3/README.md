# MysteryTwister challenges: a harder track

Status: in progress. 24 Sept 2026: challenge 115 (Bigram Substitution Part 2) solved, answer ready for Daniel to submit;
180 (Camouflage Part 6) attempted, open; Weakened ElsieFour Parts 1-3 in progress (SAT attack).

George Lasry (24 Sept 2026) suggested it: historical European ciphers are too easy a test for current models, and
MysteryTwister (formerly MysteryTwister C3, now mysterytwister.org, run by the CrypTool project) accepts LLM solutions
and keeps a separate LLM ranking. LLMs have recently solved challenges no human solver had, and a few remain solved
only by humans.

This folder is not a cipher target: it has no `profile.json` and stays out of the paper data (`NOT_TARGETS` in
`docs/_check_writeup.py`). Each challenge worked gets a subfolder `mtc3/<id>-<name>/` with its own NOTES.md.

- `RESEARCH.md`: how the site works, the LLM rules, which challenges LLMs have and have not solved, sources.
- `challenges_l2_l3_x.csv`: all 284 level II, III and X challenges with human and LLM solver counts
  (from the site's public data, 24 Sept 2026).

## Rules that matter here

- An account is needed to submit. **Daniel creates the account and submits**; sessions do not create accounts or
  submit on his behalf. A session prepares the answer and the notes; the submission is his.
- Each submission asks "Did you use an LLM?"; tick it when a model did more than half the work, and give the model
  name. Solves count on the LLM Hall of Fame.
- Levels I-III are checked automatically with a limited number of attempts (15, sometimes 20): do not guess.
  Level X solutions go by email and are checked by hand.

## Shortlist (from RESEARCH.md section 4)

| # | Challenge | Level | Why |
|---|---|---|---|
| 1 | Double Column Transposition Reloaded 1-3 (287-289) | III | Never solved since 2013; Lasry's published double-transposition attack is the starting point |
| 2 | SIGABA Part 6 (359) | III | One human solver; LLMs cleared Parts 3-5 |
| 3 | SIGABA CSP-2900 / CSP-889 (342, 343; II: 207-210) | III/II | Only Jerva and Lasry have solved them; no LLM |
| 4 | ElsieFour Part 1 (292) | III | Four human solvers, no LLM |
| 5 | Double-Column Transposition/Granit 1-3 (126-128) | II | Never solved; follows the LLM Granit solves; short ciphertexts |
| 6 | ASAC Part 4 (111) | II | Never solved |
| 7 | Monoalphabetic Substitution with Camouflage Part 6 (180) | II | Two human solvers; cheap to try |

Level X items with public solutions (Vatican Part 3, Catherine of Aragon) are only useful as declared controls.

## Results

| # | Challenge | Level | Outcome | Folder |
|---|---|---|---|---|
| 115 | Bigram Substitution, Part 2 | II | Solved 24 Sept 2026 (no earlier LLM solve); key verified by re-encryption; answer in `private/` (git-ignored), not yet submitted | `115-bigram2/` |
| 180 | Monoalphabetic Substitution with Camouflage, Part 6 | II | Attempted, open: the search never reaches the true key | `180-camouflage6/` |

Answers to live challenges are kept in each folder's `private/` directory, which is git-ignored: the repository is public,
and publishing an answer would spoil the challenge.
