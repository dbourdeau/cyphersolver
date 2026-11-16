# Verification plan: is Harford Jones's code book Entick's *New Spelling Dictionary* (1787-1798 setting)?

Written 15 Nov 2026 by an AI agent (independent verifier), before any held-out comparison. All work by AI agents.
Hashed (sha256, `TEST_PLAN.sha256`) before the first held-out comparison. One run per test; misses stay misses.

Claim under test (earlier agent, `output/jones1802_codebook_2026-11-15/NOTES_jones_codebook.md`): Jones's group
`p,n` = printed page p of Entick's *New Spelling Dictionary* (1787-1798 resetting), n-th entry on that page.
Claimed edition for the page test: **1787** (the earlier agent's best). Other editions are run beside it.

Source of code values: their `table_1798.tsv` (from the clear copy /51), copied in
`output/jones1802_codebook_2026-11-15/their_folder/`. `proposals.tsv` (context guesses) is never used in a test.

## What I knew before writing this

- Read: their NOTES, table, proposals; the earlier agent's notes, plan and scripts. Downloaded the 1787 hOCR (with
  line coordinates) and looked at one page (printed 52, CAP-CAR, not a sample page) to see the layout: one leaf =
  one page, two columns, running head "52 CAP CAR", one entry per line, overflow in brackets, rare indented
  continuation lines.
- Noticed from the table alone (no dictionary consulted): many out-of-order values become alphabetical if a
  printed page digit 2 is read as 4 (W words "weight 232", "which 233", "will 235", "with 236" -> 432-436; "very 201"
  -> 401; "by 28,75" -> 48,75; "you 220" -> 440; "ministers 220", "morning 225" -> 240, 245). This is a
  hypothesis about the transcription of Jones's digits; it is tested only as the pre-declared secondary test S1.

## Samples

- **Old 25**: the earlier agent's rule (first 25 two-number groups with an alphabetic word of 5+ letters, each word
  once). Excluded from everything below. `work/sample_old25.tsv`.
- **Fresh sample** (`scripts/samples.py` -> `work/sample_fresh.tsv`, 122 items): every other group in
  `table_1798.tsv` with a word value, one item per group. A group aligned to two words takes the word with the
  higher count; a tie is excluded as ambiguous. Excluded: groups `p,2` (two numbers ending 2; Brice Dudout: not
  fixed values), "15th", "majesty's". Three-number groups (e.g. 177,12,2 had) are kept and tested on `p,n`.
  Excluded list: `work/sample_excluded.tsv` (19 groups). The `p,2` groups are analysed separately, after the tests.
- **Training set** (counting rule only): fresh-sample rows at 0-based indices 0, 8, 16, ..., 112 (15 items):
  1,1 a; 22,33 as; 50,65 can; 129,70 enemies; 156,56 fortunately; 179,7 her; 217,30 last; 232,12 weight;
  236,35 wisest; 260,26 opportunity; 275,12 people; 308,62 reasoning; 330,16 satisfied; 370,15 sufficient;
  382,28 then.
- **Held-out set**: the other 107 fresh items.
- **Image subset of the held-out set**: held-out items in file order, every third one starting with the first
  (36 items). These pages are fetched as images for the 1787 edition and counted by two blind helpers.

## Test 1: page test (on the fresh sample, 122 items, training included since it does not use positions)

For each book: does the word (headword, or its root: -s, -es, -ed, -d, -ing, -ly, -ness, -ation stripped, root of 4+
letters; words of 3 letters or fewer must match a whole headword token) appear as a headword on the predicted page?
Headword = a capitalised token at the start of an OCR line (hOCR line files) or, where only page text is on disk,
a capitalised token anywhere in the page text followed by a comma, accent or part-of-speech mark. The same matcher
is used for every book that has the same kind of text.
- Claimed edition 1787: predicted page = Jones page (no rescale). Also report the best linear fit, for symmetry.
- Other Entick editions 1782-1798 with text on disk or fetched: same, no rescale, and best fit.
- Controls: Entick 1776 and 1781 (Lee indexes), and one or two non-Entick dictionaries of the period (John
  Bentick's *Spelling and Explanatory Dictionary*, 1786, IA, plus one more if quickly had). Each control is
  rescaled linearly, page = a*jones + b, with (a, b) chosen by grid search to MAXIMISE its own on-page hits on this
  same sample (the most favourable rescale possible; overfitted in its favour).
- Pass: 1787 at least 80% on-page (98 of 122) AND at least 20 percentage points above the best control.
- Also reported: within 1 page, within 2 pages.

## Test 2: position test

Counting rules (candidates fixed now; one is chosen on the training set and then frozen):
- R1: n = entry number counting the headword lines of column a top to bottom, then column b continuing.
- R2: as R1 but every printed text line counts (indented continuation lines included).
- R3: column a numbered 1..k, column b numbered from 40 whatever k is.
- R4: as R1 with a constant offset c in -2..+2 (n = index + c), c chosen on training.
Choice: the rule with most training items exact or within 1 on the 1787 image counts; ties go to the lower number.
Frozen rule recorded in the NOTES before any held-out position is read.

Counting sources:
- Primary: page images of the 1787 edition (IA, one page per request), each page counted twice by blind helpers
  (Opus, or Sonnet seeded with two pages I counted and redone if a seed is wrong). Helpers receive only the image
  and are asked to list every line of each column in order, marking headword lines; they are not told any word.
  Disagreements are listed; I resolve each against the image and record it.
- Secondary: machine counts from the IA hOCR line coordinates of each edition (lines assigned to columns by x,
  ordered by y; headword line = starts at the column margin with a capital). Its agreement with the image counts
  on the 1787 image pages is reported first; if agreement (exact entry number) is below 80% the machine results are
  reported as indicative only.

Scoring for each item: "exact" if the n-th entry under the frozen rule is the word (or its root, as in test 1);
"within 1" if the word is at n-1, n or n+1. A word not on page p is a miss.
- Pass: at least 60% within 1 on the held-out set (image subset for 1787 with images; whole held-out set by machine
  for each edition) for some edition, AND a shuffled control below 10%.
- Shuffled control: the held-out groups are given to the words in a fixed derangement (each word gets the group of
  the item 7 places later in file order, cyclic) and scored the same way. Also the analytic chance (3 / entries on
  the page) for words that are on the right page.

## Test 3: edition

Candidate editions on IA, 1782-1798 (identifiers already in `output/arthur_lee_1779_2026-11-14/work/ia_search_entick.json`;
searches only if needed, at most 8): for each with hOCR, the position test by machine on the whole held-out set,
"n of m exact, n of m within 1", plus page test on-page rate. The edition with the most exact hits is named; if two
editions are within 3 exact hits of each other, the edition is "not fixed".

## Secondary test S1 (pre-declared): digit 2/4 confusion

For held-out items that miss on their stated page: replace any single digit 2 in the page number by 4 or any 4 by
2; if the word is the entry at n (within 1) on such a page under the frozen rule, count it as "explained by a 2/4
misreading". Report n of m. This is not used to pass test 1 or 2.

## Rules

Internet Archive only (HathiTrust public-domain images only if essential): one request at a time, 2.5 s apart,
honest User-Agent, stop at the first 403 or 429; at most 250 requests including redirects; at most 8 searches.
Downloads in `sources/raw/jones1802_verify_2026-11-15/` with SHA256SUMS. Python run with -I, never from a download
folder. Nothing pushed, posted or sent.

## Amendment A (15 Nov 2026, 13:05, before any held-out position was looked at)

Original plan hash: a95655aa269b1097e26662af6f709cd42297adcb0792e496007d369f4d7a13c9.
What had been run when this was written: test 1 (page test, complete; result recorded in the NOTES as run), and the
machine counts on the 15 TRAINING items only, for every edition. Those training counts show that the 1787 edition
puts almost no training word at its number (0-3 of 15 under any rule) while the item `..._1795_0` does best
(R2: 4 exact, 5 within 1). Choosing the rule on 1787 images would therefore choose it on noise. Change:
- The image counts (training and held-out image subset) are made on the edition that is best on the training set by
  machine count: **IA `bim_eighteenth-century_enticks-new-spelling-di_entick-john_1795_0`**, not 1787.
- The rule is chosen on the 1795_0 training image counts (same candidates R1-R4, same tie rule) and then frozen.
- Everything else is unchanged: the held-out set, the image subset rule, the pass marks, the shuffled control,
  the machine test of every edition, S1.
