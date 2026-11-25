# Blind second reading: number runs in the letter dated "London June 24th 1885"

Reader: isolated AI agent (Claude), 26 Nov 2026. No person checked each digit by hand.

## Blindness

- [stated] Only the 39 files in `fenian1885/crops/` were opened. Nothing else in `fenian1885/` was listed, opened or searched (no `freeze/`, `result/`, notes or tables).
- [stated] No web search was made for this letter.
- [stated] No decoding was attempted and no meaning was guessed for any number.

## Method

1. [measured] Viewed all 39 crops one by one (38 PNG, 1 JPG).
2. [derived] Put the crops in reading order from the running text, and numbered the sides: side 1 starts "London June 24th 1885 / My Dear Friend"; side 2 starts "From the notes I gave him"; side 3 starts "We found him a polished gentleman"; side 4 starts "other firms."
3. [measured] Counted lines on each side from the overlapping crops to give side.line locations.
4. [measured] For each number run, cut 3x to 6x enlargements from the crops into `zoom/` (working copies only, made with PIL, LANCZOS) and read the digits from those.
5. [measured] Counted runs and pairs by script: 13 runs, 72 pairs (4+3+3+3+3+9+8+10+2+4+8+9+6 = 72). The doubtful pair in run 13 is counted as one pair.

## Crops

- [measured] 39 files viewed. 39 usable: none was unreadable.
- [measured] 17 crops show at least one number run. 22 show plain text only (all of side 1, the upside-down top note, the struck-out word, and the text-only parts of sides 2 and 3).
- [measured] One file is a low-resolution JPG screenshot of the viewer (sides 2 and 3 side by side). Used only to check line order, not to read digits.

## Limits and doubts

- [derived] Side 4 line numbers from 4.13 on are probable, not certain. No crop shows side 4 lines 12 and 13 together. The join was inferred from a descender and underline at the top of the "I directed his attention" crop, which appear to match "the Genius of the Cause" (line 12). If a line is missing there, runs 7 to 13 move down by that many lines.
- [measured] Run 13 is on the last line of side 4 and the digit bottoms are clipped by the page edge in both crops that show it.
- [measured] Run 4 is cut by the bottom edge of its crop: any punctuation after 79 is not visible.
- [measured] Three pairs carry a doubt on a digit: run 6 pair 6 (70, alt 76/78), run 7 pair 5 (70, alt 76/78), run 13 pair 2 (47, alt 77). The superscript letters in run 7 are read "re" with low confidence.
- [measured] Side 4 ends mid-sentence ("... feasible"). The crops show no later side, so any number runs beyond side 4 are not covered here.
- [stated] Not counted as runs: the time "7.30" and "9" on side 1, and the year "1885" (also seen upside down in the top-note crops).

## Conventions in BLIND2.tsv

- Pairs are separated by a space for reading. In the letter most runs are written run together; spacing in the letter is uneven and is not recorded as a separator.
- `^` marks letters or digits written above the line. ` / ` marks a line break inside a run. `4?7` marks a doubtful pair, with alternatives in the doubts column.

## Check tool

- [stated] No project check tool exists for this transcription. The run and pair counts were done by script (above).
