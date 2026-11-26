# Test plan: is the Paris draft of 25 messidor an V the plaintext of the 653 code groups?

Written by an AI agent (Claude) on 21 Nov 2026, between about 01:10 and 01:32 EST, **before** either transcription of
the draft was opened by the agent that wrote this plan and runs the tests. At the time of writing that agent had seen:
the ciphertext (Michael Brackx's transcription, upstream `targets/delacroix1797/ciphertext.txt`, sha256 663e0a42...),
the upstream notes on its repeats, and the two-line description of the draft in
`output/loc_clear_online_2026-11-21/NOTES_french.md` (Adams's speech, despatch of 29 prairial, Rozier and Mozard,
cipher to be used, Adet's arrival and audience). It had not seen the draft's wording. The two readers' hand-back
messages (line counts, hard spots such as "[facilité?]", "[m'ont?]", "Boston", "29 prairial") had been seen.

The method was developed and calibrated on synthetic letters only (French passages from Turner 1904 enciphered with a
made-up code of the real size). Calibration files: `work/calibration_synthetic.*`, `work/robust_exp*.py`.

## Inputs, fixed before the run

- **Code groups:** Brackx's 653 groups exactly as upstream, no digit changed. His doubtful digits are looked at only
  after the tests, and any change is reported separately.
- **Candidate plaintext:** the merged transcription of ff. 41r-42r, letter body only: from the first word after the
  address lines to the last word before "Salut et fraternité" (the National Archives copy has the heading and the
  close in clear). Rules for the merged test text, applied before any alignment is looked at:
  1. final intended text: struck-out words left out, insertions put in (including the lines added at the foot of 41v);
  2. where the two readers differ, I look at the image and choose; every such choice is listed; if I cannot decide,
     reader A's reading goes into the test text and the place is marked disputed;
  3. abbreviations written out where the expansion is not in doubt (listed); figures written as French words;
  4. lower case, accents and punctuation removed, apostrophes split words (`align_em.normalise`).
- **Split for the held-out test:** training part = the groups on frames 244 right and 245 left (the first 47 lines
  of the transcription, 568 groups); held-out part = frame 245 right (the last 7 lines, 85 groups). (A first design
  that trained on frame 244 right alone was dropped after a dry run on a synthetic letter: 277 groups are too few for
  the alignment to form, and its scoring rule let shuffled keys score 0.96. Both faults were found and mended on
  synthetic data, before the draft was opened.)

## Test 1: length (necessary, not sufficient)

Letters of the test text divided by 653. Pass if between 2.0 and 6.0 letters per group (and 1.0 to 2.5 groups per
word). The synthetic code ran at 2.4 to 2.6; period French codes with many whole-word entries run higher.

## Test 2a: repeated group sequences against repeated strings (simple, sturdy)

- Take every pair of places where the same sequence of **three or more** groups occurs twice (exact repeats, maximal,
  no homophone guessing). A sequence of n groups starting at group i is expected near letter (i + n/2) × N / 653.
- A pair is **supported** if the test text has one identical string of at least 2n letters (spaces ignored) whose two
  occurrences lie within 6% of the text length of the two expected places.
- Statistic R = supported pairs / all pairs.
- Controls: 100 copies of the test text with its sentences in shuffled order (if fewer than 8 sentences, blocks of 12
  words), and 100 passages of the same letter count from Turner 1904.
- **Pass:** R is at least 0.60 and higher than all 200 controls.

## Test 2b: full alignment (strong when it works; can fail if the draft differs much from the sent text)

- `scripts/align_em.py`: each group emits nothing, or 1 to 15 letters inside one word, or one to three whole words;
  a whole word may be left uncoded at a fixed cost; a group is explained only by what its *other* occurrences are
  aligned to (leave-one-out), never by itself. Thirty rounds from a start that knows only the mean chunk length.
  Eight fixed start settings (`CONF` in `scripts/run_tests.py`); the score of a text is the best of the eight.
- Statistic S: among tokens of groups that occur at least twice, the share whose chunk is shared with at least one
  other token of the same group.
- Calibration on synthetic letters (best of the eight settings): exact text 0.92 to 0.97 (5 of 5); 2% and 5% of words
  changed 0.85 to 0.96 (10 of 10); 10% changed: 2 of 5 above 0.8, 3 of 5 at 0.18 to 0.25; shuffled controls 0.14 to
  0.20.
- Controls: 40 sentence-shuffled copies of the test text and 40 Turner passages of the same letter count, each
  scored the same way (best of eight).
- **Pass:** S is at least 0.50 and higher than all 80 controls.

## Verdict rule for "the draft is the plaintext"

- **Pass:** Test 1 passes and Test 2b passes (2a is then reported beside it).
- **Miss:** Test 2a and Test 2b both fail. The draft is then not shown to be the plaintext; no table is built.
- **Not settled:** 2a passes and 2b fails. Then the draft is related but the automatic alignment did not hold. Any
  alignment by hand from the repeats is labelled as made after the test, and only Test 3 can then earn a table.

## Test 3: held-out prediction (decides whether a code table is earned)

- From the best full alignment, only one number is carried over: the letter position where the training part ends.
- The alignment is re-fitted on the training part alone (best of the eight settings by S). Table = every group whose
  chunk is shared by at least two of its training tokens, with that chunk. The table file is frozen (sha256 recorded
  before scoring).
- Scoring on the held-out part (`scripts/heldout.py`): the held-out groups are placed on the rest of the text in
  order so that as many letters as possible are covered by table chunks standing at their place; groups not in the
  table, and table groups that do not fit, may take 0 to 15 letters. Reported: the share of the held-out letters so
  covered, and the share of table groups that fit.
- Control: 200 shuffled keys (the same chunks dealt out at random among the table's groups), scored the same way.
- Dry run on a synthetic letter with 3% of words changed: 42 of 42 table groups fit, 33% of letters covered, shuffled
  keys 10% on average and 14% at the 99th percentile.
- **Pass:** at least 40 held-out tokens have a table value; at least 70% of them fit; and the share of letters
  covered is above the 99th percentile of the shuffled keys and at least twice their mean.

## Numbers and proper names (reported, not scored)

After the alignment, list each proper name and each number of the draft with the groups aligned to it. Expectation
stated now: a name that occurs more than once takes the same groups each time, apart from neighbouring-number
variants (the upstream notes infer homophones in small blocks: 971-973, 265-269, 81-83 ...); and the seven
occurrences of `705 806 711|400 405` fall on one and the same word.

## What will be reported whatever happens

Every statistic with its control range; the verdict by the rule above; a miss as a miss. Nothing is posted.
