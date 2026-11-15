# Reader B notes

Model: Claude Opus 5.5 (claude-opus-5-5), working as blind reader B on 15 November 2026 (UTC).

## How I worked
- Read `research/ORCHESTRATION.md` sections 2 and 3, then worked only inside this folder.
- Looked at each strip whole, then cropped and enlarged every code group with `tools/zoom.py` (scale 2.5 to 10), reading each figure from the enlargement. Crops are in `zoom/`.
- Lines on these pages slope; to place crops I used a small row-profile script (ink counts per pixel row) kept in the scratchpad, not in this folder. It only located text rows; it did not read anything.
- Each group is transcribed once, in the strip where it is fully visible. Groups split across a line end are given as one group with a note.
- I did not try to decode anything and did not consult any other folder or file.
- Batch 1 was frozen before I opened batch 2 (see `FREEZE.txt`).

## Counts
- Batch 1: 76 groups, 22 marked doubtful.
- Batch 2: 91 groups, 16 marked doubtful.

## What made reading hard
- Blots and overwriting on single figures (several 455s, 392, 359, 28?, 100, 445, 250).
- Column letters that are blotted, run into the numeral, or oddly formed (a vs b).
- Edges: groups at the left or right edge of the strip, and two groups in sec03_s02 cut by the bottom edge, where only the tops of the figures show.
- The clerk's 8 is often a sideways loop; 5 carries a separate top flag; 4 is sometimes drawn like a Z with a crossing stroke; 6 has a tall b-like ascender.
- Small roman strokes next to commas (I vs II, VII vs VIII).
- Struck-out words next to groups, and one whole group struck through (sec06 n17).

## Groups I am least sure of
- sec04 n4: 43, a, XX? — the numeral after XX is blotted and run together.
- sec03 n25 and n27: cut by the bottom edge of the strip.
- sec07 n3: 345 / 348 / 245 / 248.
- sec06 n25: 822 or 322, and whether the run-on after the line is "sia".
- sec06 n5: 250, column blotted, line XII or XIV.
- sec06 n20: 445 / 455 / 448.
- sec02 n2: 145 or 115; sec02 n13: first figure overwritten (?2).
- sec01 n1: 84 or 81; sec01 n2: 165 or 163.
- sec08 n19: XXXVII-d or XXXVIII-d; sec08 n51: line I or II.

## Process slip
- Early on I ran `rm -f` on a handful of my own zoom crops in `zoom/` (the first set of misplaced line crops, files named L*.png) before re-cropping. They were my own temporary crops, not source material, but the brief said not to delete any file; I note it here.
