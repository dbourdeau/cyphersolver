# Key v7 (PR #699) tested once on fresh glossed leaves of unit 261267 (Brice Dudout, 17 Nov 2026)

Key v7 is Malcolm McBratney's (PR #699, `key_v7.tsv`, md5 d1ee7e3094e1643bfb0f58b39e9d0052, commit e8f0f7e50).
It was used here unchanged. This folder holds one held-out measure of it, and a recount of our reading of image 573.
Work by AI agents (Claude) for Brice Dudout. No image is reproduced: the Rigsarkivet leaves are cited only.

## What was done, in order (times UTC, 17 Nov 2026)

1. **Frozen first (20:41:13, `PREREG.sha256`, `FROZEN_AT.txt`)**: `PREREG.md`, the scoring script `measure_v7.py`,
   the label sheet `SHEET.md` (sign names, no values) and `key/key_v7.tsv` (byte copy of #699's file). Nothing in the
   key was added or changed; our own T2 values that v7 lacks were not added.
2. **Portion.** Glossed relations to the king in unit 261267 that nobody had used for a key, a check or a measure:
   pages 505 left, 505 right, 501 right, then 437 right, 481 left, taken in that order until 300 glossed tokens.
   505 and 501 were the reserves named in our protocol of 11 Nov and never transcribed. The rule stopped at
   **505L + 505R + 501R = 315 tokens**; 437R and 481L were transcribed but never decoded (not burned).
3. **Two blind passes** (`passA_BLIND.tsv`, `passB_BLIND.tsv`): two separate AI sub-agents, each with only the page
   crops and `SHEET.md`, no key, no earlier file, neither seeing the other. On the portion they agree on 310 of 315
   tokens (98.4%; maintainers' count at integration, 27 Nov 2026: this file first said 311, but on 505R line 21 A has
   "MT 269" and B "PM 169", two tokens, so the 4 token rows of the adjudication cover 5 token positions).
4. **Adjudication and freeze** (`ADDENDUM-1.md`, `ADJUDICATION.tsv`, `build_final.py`, `FINAL.tsv`;
   `GEL-FINAL.sha256`, 21:01:30): the 4 token rows (5 token positions) and 4 gloss differences were settled on the image by the coordinating
   agent, who knows key v7 (disclosed), before any decode. Both readers had left many tokens under a long gloss marked
   "no gloss"; the addendum joins every such run to the preceding glossed run of its page, so every token of the three
   pages and every gloss enter the score (an unglossed token can only cost).
5. **One measure** (`MEASURE.json`, per run `MEASURE_segments.tsv`): `python3 -I measure_v7.py key/key_v7.tsv FINAL.tsv`.

## Result

| | score (1 - Levenshtein / max length, a-z) | best of 200 shuffled keys | mean | at or above |
|---|---|---|---|---|
| **FINAL (adjudicated), decisive** | **0.8808** | 0.3241 | 0.2778 | 0 of 200 |
| pass A alone (not decisive) | 0.8637 | 0.3248 | | |
| pass B alone (not decisive) | 0.8719 | 0.3250 | | |

Bar fixed before: score >= 0.85 and >= best control + 0.30. **Passed** (margin +0.557). 57 glossed runs, 315 tokens,
859 predicted letters against 881 glossed letters. Strict count (every token valued, no tier C or '?', decode = gloss
letter for letter): 26 of 57 runs; 8 of 11 one-word runs.

So key v7 reads leaves of the Petkum unit that it never saw, as well as T2 did on its own held-out leaves (0.885).

## What the misses show (from `MEASURE_segments.tsv`; nothing below was changed after the measure)

- **The sign for i.** Both readers wrote the b-like sign as `6` (it looks like a 6; our key T2 called it 6). Key v7 names
  it `B`. The rule frozen in advance gives `6` no value, so every i written with it is a miss (insupportables decodes
  "nsubportables"; seroit "serot"). This costs the score; it does not help it.
- **88 under "l'Euesque de Munster".** On 505 right line 2 the gloss over `100 335 88` reads "et que l'Euesque de
  Munster"; key v6/v7 have 88 = le Roy d'Espagne (561 right, and three glosses in unit 261294). Both readers read 88.
  Either the cipher clerk wrote 88 for another number, or 88 is not the King of Spain everywhere. Not settled; reported.
- **Gloss misread by us, not a key fault.** 505 right line 11: we adjudicated the gloss as "petites emulitez"; the key
  gives "petites civilitez" (317 366 365 MT 184 382 268 365 HB = pe-ti-te-s ci-vi-li-te-z), which is surely the word
  ("civils" is glossed on 437 right too). The frozen file keeps our misreading; the score is lower for it.
- **Numbers with no value in v7, glossed here** (observations only, not added to any key): 53 = S.A.R. (twice),
  94 = Duc (d'York), 262 = inten(tions), 347 = (Reli)gion, 349 in "encore" (185 349 = co-re?). Burned with the portion.
- Code-word rows of v7 met in the portion: 51, 61, 88, 92, 96, 100, 107, 114, 116, 119, 120, 133, 134, 151, 152, 153,
  161, 165, 169, 222, 307, 321, 328, 329, 389.288. 151 (McBratney's single-gloss row, G2) is glossed "francois" on
  505R and "Princesse francoise" on 501R: a second and a third gloss for it. 92 is glossed "l'Angl." there.
  `6` (7 times) and 53, 94, 262, 347, 349 are the tokens with no value. The doubtful rows 181 and 248 and the new rows 164 and 346 do not occur.

## Recount of our image 573 with v7 (`573_recount_v7.md`)

Our reading of 30 Nov 1665, pp. 2-3 (PR #622, `dudout/reading/573.units.tsv`, 238 units) had 220 sure, 13 probable,
5 unresolved. Six probables placed by rank now have a chancery gloss in the folder's keys: 151 françois three times
(v7, McBratney), 163 alliance, 281 maistre, 310 nous (v5, McBratney). Sure words: **226 of 238 = 94.96%**, under 95%,
so the letter stays **read in part**. By the folder's strict rule the six move N to E: S 173, E 49, N 16 (72.69% S, as
before). No transcription was changed; the first reader's frozen files (for example the "15" of 528R.18) are untouched.

18 Nov 2026, blind sign-form check (`573_recount_v7.md`, second section; 3 of 3 controls right): unit 114 is sure
("persuadez"), unit 238 stays probable ("tous", decoded "tols"). Sure words: **227 of 238 = 95.38%**. This is a unit
figure on our units: the class of the 30 Nov 1665 entry stays **read in part** (maintainer, 19 Nov 2026) until a
recount by cipher words is at or above 95% and a reader other than the author has reviewed the reading.

## Files

`PREREG.md`, `PREREG.sha256`, `FROZEN_AT.txt`, `SHEET.md`, `measure_v7.py`, `key/key_v7.tsv`; `passA_BLIND.tsv`,
`passB_BLIND.tsv`; `ADDENDUM-1.md`, `ADJUDICATION.tsv`, `build_final.py`, `FINAL.tsv`, `FINAL_A_only.tsv`,
`FINAL_B_only.tsv`, `GEL-FINAL.sha256`; `MEASURE.json`, `MEASURE_segments.tsv`; `573_recount_v7.md`.
Check the hashes: `shasum -a 256 -c PREREG.sha256`, `head -8 GEL-FINAL.sha256 | shasum -a 256 -c`.
Reproduce: `python3 -I build_final.py passA_BLIND.tsv FINAL.tsv adj` then the measure above (about one minute).
Images: Rigsarkivet, TKUA England A III 52, unit 261267 (epid 19852633), images 505 and 501, fetched from
`api.rigsarkivet.dk/ao/v1/images/<48872547 + image number>`; not reproduced.
