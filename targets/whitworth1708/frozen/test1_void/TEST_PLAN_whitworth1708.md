# Test plan: Whitworth's numerical code, Moscow, 22 September / 3 October 1708

Written by an AI agent (Claude) on 21 November 2026 before any code group was aligned with any plaintext and
before any table existed. No person has checked it. The test is run once.

## What is tested
Whether a table of code values built from ONE despatch, with the help of the printed decipherment, reads the
code groups of the OTHER despatch of the same day. A pass confirms the period decipherment and gives a partial
table; it is not an independent solution of the code.

## Materials (all fixed before the run; hashes in plans/HASHES.txt)
- Building letter: The National Archives SP 91/5/2 f. 114 (old pencil folio 300), duplicate of Whitworth to
  Boyle, Moscow 22 Sept / 3 Oct 1708. 473 code groups in 35 coded stretches ("runs"); 4 groups left open after
  two blind transcriptions and are treated as unknown. Plaintext: Sbornik of the Imperial Russian Historical
  Society vol. 50 (1886), No. 27, pp. 83-88, typed from the page images. File transcriptions/runs_f114.json.
- Held-out letter: SP 91/5/2 f. 112 (old pencil folio 298), duplicate of the private letter of the same date.
  357 code groups in 32 runs; 2 groups open. Plaintext: Sbornik vol. 50, No. 28, pp. 88-92.
  File transcriptions/runs_f112.json.
- A run is a maximal sequence of code groups between words written in clear. Its plaintext is the printed text
  between the same clear words (letters and digits only, lower case). The pairing used only clear words and the
  print, no code value (scripts/build_runs.py; three hand corrections in transcriptions/overrides_f112.tsv).
- The deciphered manuscript partners (old folios 294 and 274) were not available (State Papers Online asked for
  a sign-in), so the print is the only plaintext. Its spelling may differ from the code's; that counts against
  the score and is accepted.

## Procedure (scripts/run_test.py with scripts/wlib.py, unchanged from the hashed copies)
1. Alignment, building letter only. Each run's plaintext is cut into one piece per group so that equal numbers
   get equal pieces (sampler in wlib.Aligner: pieces of 1-16 characters, annealed, then best-path passes), ten
   times with seeds 0-9.
2. Table rule. Tier A: a number seen at least twice whose pieces all agree (one dissent allowed from four
   sightings up). Tier B: a number seen once whose two neighbours in its run are each a run edge or a tier A
   number standing for its tier A value. An entry is kept only if all ten seeds give it the same value.
3. The table is written to test/table_frozen.tsv with its sha256 before the held-out file is opened.
4. Held-out score. For each held-out run the best tiling of its printed plaintext is found in which a group in
   the table either stands for exactly its table value (a hit) or, like a group not in the table, for any 1-16
   characters (no hit). A run that cannot be tiled scores no hits.
   H = hits / held-out groups whose number is in the table ("covered" groups).
5. Control 1: the same score with the table's values dealt out at random among the table's numbers, 1,000
   times (seed 1708). Control 2 (reported only): the true table with every run scored against another run's
   plaintext, every rotation.

## Marks, fixed now
- VOID (the test says nothing) if fewer than 100 held-out groups are covered, or if the 99th percentile of
  control 1 is above 0.50.
- PASS if the test is valid, H >= 0.80, and H exceeds the 99th percentile of control 1 by at least 0.30.
- MISS otherwise. A miss is reported as a miss.
- Reported besides, not marks: coverage (covered / all held-out groups), share of held-out coded letters under
  hits, runs decoded exactly end to end, the same figures on the building letter (in sample), table size by tier.
- A crash before any score is printed is not a run. Once a score is printed nothing is re-run with changed
  settings, transcriptions, pairings or thresholds.

## Dry run that set the method (no Whitworth text involved)
scripts/synth_dry_run.py: an invented code (150 word groups, 246 letter and syllable groups, 30 homophones)
applied to modern English prose, about 500 groups to build and 300 held out, 2% of numbers corrupted. Five
made-up codes (seeds 1, 2, 3, 4, 7): H 0.96 to 1.00, coverage 0.43 to 0.53, table 103 to 144 entries of which
94 to 98% right, control 1 99th percentile 0.20 to 0.27. The marks above were set from this: 0.80 leaves room
for misread digits and for the print's spelling.

## After the test
Only if PASS: a second table by the same rule from both letters together, labelled as fitted on both and not
tested, and a local package. If MISS or VOID: the result and what was learned, no package.
