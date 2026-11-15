# The test on No. 35

- `TEST_PLAN.md`: written by the reader (an AI agent) on 15 November 2026 before any score on No. 35 was computed, as it
  stood when hashed (`../key/FREEZE.txt`). It records what the reader had already seen.
- `RESULT.json`: the one run. `python scripts/run_test.py --check` from the target folder repeats it from
  `key/table_frozen.json` and `transcriptions/n35_office_copy.tsv` and prints whether the result is identical (it is;
  the script differs from the hashed one only in file paths). The script counts 55 words, not 54, because it splits
  "Mons.r" in two; this changes no score.

| Test | Mark set beforehand | Result |
|---|---|---|
| A. Table's words for No. 35's numbers matched in order against the clerk's words | at least 60% of covered numbers, and above all 200 shuffled tables | passed: 16 covered, 11 matched (69%); shuffled mean 3.58, highest 6 |
| B. Table's word against the words directly over the number | 60% if word over number; expected to fail | failed as expected: 13 covered, 0 matched |
| C. Firm entries among the last 15 numbers matched in the last 15 words | at least 2 | **missed**: 2 covered, 1 matched |

The 11 matches of test A, in order: to, any, I, that, (Florida) Blanca, will, Packet, boat(s), that, Consul, there. The
five firm entries that did not match: 717 "the", 672 "and", 423 "of", 1178 "should", 1152 "if".

## The second agent's check (15 November 2026)

- Re-ran the test from the reader's frozen files: identical result.
- The table was built without No. 35 (the loader reads the fifteen files only), and the shuffled tables keep the same
  words on the same set of numbers, so they have the same share of common words: the comparison is fair. Eleven in order
  cannot arise from the method alone; six of the eleven are content words in the right order.
- Test C had two numbers to work with and could hardly pass; its miss stands as a miss.
- Calibration on the fifteen despatches, each left out in turn (the reader's saved alignment): 706 covered, 559 matched
  in order (79%). Split by kind of word: content words 119 of 171 (70%; shuffled 6.5%), function words 440 of 535
  (82%; shuffled 39.5%). Rebuilding the alignment without the despatch (three tried: No. 5, Private, No. 8 of 16 Feb):
  9 of 12, 23 of 29, 71 of 81.
- Rebuilding the table in this folder (`python scripts/build_table.py`, about three minutes, writes `crib_table.json`
  in the working directory) gives the same best alignment, but one of its sixteen runs differs from the frozen record
  (cause not found; the same with Python 3.9 and 3.12). Six entries change grade (33 and 721 weak to firm; 761, 2135,
  3605 and 3709 firm to weak) because their stability sits at the 0.70 line. With the rebuilt table the test gives
  A 10 of 15 (67%; shuffled highest 6), B 0 of 12, C 1 of 2: the same outcome on each. The frozen table is the one
  that was hashed before the run and is the one recorded here.
