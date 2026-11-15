# Reader A notes

Reader: Claude Opus 5.5 (model id claude-opus-5-5), working as blind reader A on 15 November 2026 (UTC).
Files: `batch1.tsv` (76 groups, 24 marked doubtful), `batch2.tsv` (91 groups, 20 marked doubtful). Both are frozen in `FREEZE.txt`.

## How I worked
- I read only the PNG strips in `batch1/` and `batch2/`, plus sections 2 and 3 of `research/ORCHESTRATION.md`. I opened no other project file and did no decoding.
- For each strip I first looked at the whole strip to find the code groups. Then I zoomed into every group with `tools/zoom.py`, at 3 to 10 times. For a few blots I also made a black-and-white (thresholded) zoom. All zoom images are in `zoom/`.
- Overlaps between strips: I listed each group once, under the first strip where it shows in full.
- Groups split across a line end are listed as one group, with a note.
- I included one struck-through group (batch 2, sec06 n17), marked doubtful and noted as "STRUCK THROUGH". If struck groups should be left out, drop that row.

## What made reading hard
- The lines slope across the page, and in sec03 one line rises steeply, so the reading order there took care. I read sec03 as: ... 392 / 170, 156, 170 / 213 / [cut group] XXVIII / 43 / [cut group] XXIX-d / 348, 218 / 243.
- The bottom of sec03_s02 cuts off a line. Two groups there (sec03 n25 and n27) show only the tops of their figures.
- Left and right edges: in sec02 n15 and sec03 n8, n11, n14 and n18, figures may be lost at the left edge. In sec06 n23 (416, b, X?) strokes may be lost at the right edge.
- This clerk writes 5 as a stroke with a separate top bar. A 5 written this way can look like a 6 with a bar, or like a 3. This affects several 455 readings (batch1 sec05 n23; batch2 sec06 n10 and n20; sec08 n42). A flat-topped 3 can also look like a 5 (batch1 sec01 n2, 163 against 165).
- A 4 with a hook can look like a 1: batch1 sec01 n1 (84 against 81) and sec02 n2 (115 against 145).
- Blots cover whole figures: batch1 sec02 n14 (??2); batch2 sec06 n5 (the column of the interlined group 250, ?, XII), sec08 n23 (28?) and sec08 n30 (100 against 108).
- An arabic line numeral 1 written as a single stroke and a stop could also be a roman I (the 260, b, 1 groups and 80, b, 1). I have given these as "1".

## Groups I am least sure of
1. batch1 sec02 n14: ??2, b, IX-s. The first figures are a wavy blot.
2. batch1 sec03 n25 and n27: only the tops of the figures are visible at the bottom of the strip.
3. batch1 sec04 n3: 359, b, XXXI. It could be 354 or 859.
4. batch2 sec06 n5: 250, ?, XII, interlined. The column is blotted, and the line could be XIV.
5. batch2 sec06 n25: 322, a, VII with "sia" run on. The ending is unclear.
6. batch2 sec07 n3: 348, b, XIII. It could be 248.
7. batch2 sec06 n19: 208, a, XXX. The middle sign is drawn like a V.
8. batch2 sec08 n20: 314, b, XXXVII. It could be XXXVIII.
9. batch1 sec01 n1 (84/81), batch1 sec02 n2 (115/145) and batch1 sec03 n10 (243/248).
