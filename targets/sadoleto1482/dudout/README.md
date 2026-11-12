Status: in progress (Brice Dudout, 12 Nov 2026: R1101 first page ll. 2-8 collated word by word with 7a, 97.4% of words read by sense; the rest of the letter not yet collated). Next step: collate the rest of page 1 and pages 2-3 the same way.

# sadoleto1482 / dudout: R1101 against its clear copy 7a, first page

This answers part of the NOTES gap "R1101, whole-letter word-by-word collation with 7a — blocker: not-attempted".
The first original page had not been read before (it was only searched by image template in
`emperor_expression_audit.md`).

## Sources
- Original: Vestigia 1284, photographs (103)-(105). Clear copy 7a: Vestigia 1283, photographs (101)-(102). Fetched
  from the `web_url` fields of `../vestigia/v1283.json` and `v1284.json` (open access, no login). The images are not
  in this PR.

## Protocol (files in `protocol/`, kept as frozen, in French)
1. **Blind transcription** of page 1 ll. 1-8 with `../key_working.md` only, before any look at 7a:
   `TRANSCRIPTION-AVEUGLE-R1101-p1.md`, SHA-256 `0cbd4302…bd65`. Line 1 is left out of the test because the 7a
   incipit is printed in the Vestigia record.
2. **Pre-registration** `PREREG-R1101-p1.md` (SHA-256 `8f2472f1…279e`): held-out portion = ll. 2-8, 79 words,
   306 cipher letters, outside every passage aligned so far (final page opening, queen passage, z/ff/K controls).
   Reference 7a span and measure script hashed before the run (`PREREG-R1101-p1.sha256`).
3. **One measure** (`mesure_r1101.py`, output `MESURE-R1101-p1.txt`): word alignment, character agreement against 7a.
4. **Counting** with the 95% rule, before and after the collation (`LECTURE-R1101-p1.md`; English in
   `r1101_p1_reading.md`).

## Results
- Measure: character agreement **0.764**, word agreement 0.608. 500 controls: 250 random keys (max 0.178) and
  250 shuffled 7a word orders (max 0.295); margin 0.469. The pre-registered criterion (≥ 0.85 and ≥ best control
  + 0.30) is **not met** (0.764 < 0.85; the margin part holds): the key is not re-validated by this test. The blind reading is far
  above chance, but a fresh page read blind with this key still misses about a quarter of the letters, mostly on
  look-alike signs and on groups the alphabet does not cover.
- Counts on ll. 2-8:
  - before this work: page not read (0 of 76 words);
  - blind reading alone, judged against 7a: 48 sure + 10 probable of 79 words (73.4%);
  - after the collation: 52 sure, 14 probable, 8 restored, 2 unresolved of 76 words: **97.4% read by sense**,
    86.8% sure or probable.
- Reading and English: `r1101_p1_reading.md`. The passage gives the King's terms: money from the League for the first
  year for half of 10,000 horse and 10,000 foot, then for a third of them for two more years.

## Points for you
- A tall upright with a diagonal stands for **tt** in "attendere" (cf. the ff and ss signs). One instance; not added.
- A g-like sign stands for **c** twice in "dece". Not added.
- The `┴` sign stands where 7a has **cum**, and the looped sign at the head of "conclusione" is **con**: perhaps one
  con/cum sign, separate from "-1" = a. Not settled.
- The royal title is **one group** of 6-7 signs here; it may be your K group (not compared: no I5655 image used).
- The X group reads **Venetiani** again, as in `verified_groups.md`.

What remains: page 1 from l. 9, page 2 outside the queen passage, page 3, and the final page outside its opening.
