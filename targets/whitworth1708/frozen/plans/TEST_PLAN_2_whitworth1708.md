# Second test plan: Whitworth's numerical code, table from the interlined originals, tested on f. 49

Written by an AI agent (Claude) on 22 November 2026, evening (Eastern), after Andrew's go-ahead relayed as
"Yes, run it". No person has checked it. The test is run once. The first test (21 November, VOID: 87 covered
groups where 100 were required) stands as it is; this is a new test on text no earlier test touched.

## What is tested
Whether a table of code values taken from the Secretary of State's office's own decipherment, written above the
code groups in the two received originals of 22 Sept / 3 Oct 1708, reads the code groups of a different
despatch, three weeks older, that survives bare. A pass confirms the period decipherment and gives a partial
table; it is not an independent solution of the code.

## Materials (fixed before the run; hashes in plans/HASHES_2.txt)
- Building letters: The National Archives SP 91/5/2, stamped f. 90 (old pencil 274; despatch) and stamped f. 110
  (old pencil 294; private letter), both Moscow 22 Sept / 3 Oct 1708, from State Papers Online. Typed once each
  by an AI helper on 21 November with the office's words in brackets after the groups they stand above
  (transcriptions/spo_f090_deciphered.txt, spo_f110_deciphered.txt). These are single readings. Two guards:
  (1) a group of an original counts as read only where the helper gave no alternative and the agreed blind
  double reading of the bare duplicate (ff. 114, 112) has the same number at the same place; all other groups
  are unknown (785 of 832 groups pass: 447 of 475 and 338 of 357); (2) the helper's attachment of words to
  groups, which is sometimes a group or two out, is trusted only in the form stated in step 2.
- Held-out letter: SP 91/5/2 stamped f. 49 (old pencil 233), duplicate of Whitworth to Boyle, Moscow
  1/12 Sept 1708, nothing written above the groups. Two blind transcriptions by AI helpers (Opus) on
  22 November from the State Papers Online images: 112 code groups each, all 112 the same in both
  (transcriptions/passA_f049.txt, passB_f049.txt, merged_f049.tsv). Five groups carry a second reading in one
  pass only; the first reading, on which both agree, is used.
- Plaintext for the held-out letter: Sbornik of the Imperial Russian Historical Society vol. 50 (1886), No. 22,
  pp. 44-49, typed from the Internet Archive page images by an AI helper on 22 November
  (transcriptions/sbornik50_no22_english.txt, 1,340 words). The deciphered original of this despatch (stamped
  f. 42) has not been seen.
- Held-out runs (transcriptions/runs_f049.json, 15 runs, 112 groups): a run is a maximal sequence of code groups
  between words written in clear; its plaintext is the printed text between the same clear words. The pairing
  used only clear words and the print (scripts/build_runs2.py). Five hand settings, each from clear words and
  print alone, are in transcriptions/overrides_f049.tsv: the manuscript's clear "if" stands where the print has
  "as"; the manuscript's clear "allways", which the print lacks, is not placed (the two stretches round it are
  scored as one run); clear "awake" is taken as the print's "awaken"; clear "concernd" as "concerned"; a clear
  "the" that the print lacks is ignored.

## What the planner has already seen of the held-out letter
The page images at small size when the item was saved on 21 November (some numbers are legible there), the two
transcribers' reports, the merge result, and the run listing (clear words and print). No table and no code
value has been applied to any f. 49 group. The planner does know the first test's 49-number table and the
office's glosses, and could not help recognising a few numbers; the "allways" setting above was chosen so that
this knowledge decides nothing.

## Procedure (scripts/run_test2.py with scripts/wlib.py unchanged from the first test and scripts/wlib2.py)
1. Building runs: stretches of groups between clear words in each original, with the office's words above them,
   letters and digits only (68 runs, 2,399 letters).
2. Table rule, three tiers.
   Tier S (straight from the office): a number that stands alone under one word (or one bracketed phrase) at
   least once, and never alone under a different word. Numbers with conflicting single glosses are left out of
   the table altogether.
   Tiers A and B (by alignment, for numbers with no single gloss): the first test's aligner over the building
   runs, started with the tier S values as fixed sightings (weight 2 each), ten seeds 0-9; tier A = a number
   seen at least twice whose pieces all agree (one dissent allowed from four sightings up); tier B = a number
   seen once between two fixed neighbours; kept only if all ten seeds give the same value. No position band.
3. The table is written to test2/table2_frozen.tsv with its sha256 before the held-out file is opened.
4. Held-out score, as in the first test: for each run the best tiling of the printed plaintext in which a group
   in the table either stands for exactly its table value (a hit) or, like a group not in the table, for any
   1-16 characters (no hit). H = hits / held-out groups whose number is in the table ("covered").
5. Control 1: the table's values dealt out at random among the table's numbers, 1,000 times (seed 1708).
   Control 2 (reported only): the true table with every run scored against another run's print, every rotation.

## Marks, fixed now
- VOID if fewer than 40 held-out groups are covered, or if the 99th percentile of control 1 is above 0.50.
- PASS if the test is valid, H >= 0.80, and H exceeds the 99th percentile of control 1 by at least 0.30.
- MISS otherwise. A miss is reported as a miss.
- The floor is 40 here where the first test had 100, because the whole held-out letter has only 112 groups.
  That makes a pass here a statement about a small sample: it is to be reported with the counts, not as a share
  alone.
- Reported besides, not marks: coverage, share of held-out coded letters under hits, runs read end to end,
  per-run readings, the same figures on the building letters (in sample), table size by tier.
- A crash before any score is printed is not a run. Once a score is printed nothing is re-run with changed
  settings, transcriptions, pairings or marks. The script refuses to run if test2/test2_result.json exists.

## Method check that set the rule (building letters only, no f. 49 data)
Table built from ONE interlined original, scored on the OTHER letter's bare duplicate against the 1886 print
(the first test's run files); five seeds; outputs in test2/dev_*.txt.
- First test's aligner alone on the office's text: 37 and 60 entries, coverage 14% and 26%, H 0.96 and 0.96.
- With a position band of 1, 2 or 3 groups round the helper's attachments: no better (37 to 60 entries).
- Tier S alone: 76 and 101 entries, coverage 27% and 31%, H 0.94 and 0.95, control 99th percentile 0.18 and 0.17.
- The rule above (S + seeded A and B, no band): 116 and 157 entries, coverage 37% and 44%, H 0.95 and 0.95,
  control 99th percentile 0.23 and 0.19; tiers A and B alone 92 hits of 96 covered.
These figures were looked at to choose the rule. They are in-family (same day, same writer, and the table's
words are the same office's as the print's source), so they say what to expect, not what the test will show.

## After the test
Whatever the mark: the result goes into NOTES_whitworth1708.md, the register row and INDEX. If PASS: the frozen
table is the earned table; a local package is prepared, nothing is posted. Nothing is posted, sent or pushed in
any case. Licensed images stay out of any package.
