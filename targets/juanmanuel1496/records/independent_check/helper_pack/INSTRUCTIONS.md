# Sign-by-sign transcription of a cipher manuscript (blind task)

You are transcribing lines of a handwritten 1490s cipher letter into sign IDs. You are NOT asked to decipher
anything, and you are not given any key or values: just say which reference shape each sign is.

## What you have (read only this folder, `helper_pack/`)

- `sheet_1.png`, `sheet_2.png`, `sheet_3.png`: the reference shapes, rows S01 to S46. Each row shows the shape as it
  appears on another letter written in the same cipher (left), and, where one was found, the same shape as it looks in
  the letters you are transcribing (right, smaller and blurrier because those photographs are low resolution).
- `letter_groups_examples.png`: besides the invented signs, the writer sometimes puts a short group in ORDINARY Latin
  letters (like the three examples shown). Write such a group as the letters you see, in square brackets, e.g. `[bnh]`.
- `crops/`: the lines to transcribe, 3x enlargements of the manuscript. File `L2_f6r_l07_a.png` is the left part of a
  line and `L2_f6r_l07_b.png` the right part of the same line. Each crop shows about three lines of writing; transcribe
  ONLY the line marked by the red arrows in the white side margins. The page is thin, so faint mirror-image writing from
  the other side shows through (paler, often reversed): ignore it. Ignore any marginal notes.

## What to write

Write one file, `transcription.txt`, in your own folder (the caller names it), one line per crop part, in this form:

    L2_f6r_l07_a: S10 S27 / S45 S09 ? [dal] S31
    L2_f6r_l07_b: S40 S12 / ...

Tokens, left to right as the signs are written:
- `S01`-`S46`: the sheet row whose shape the sign is.
- `?`: a sign is there but you cannot decide which row it is (damaged, blotted, too unclear, or two rows equally likely).
- `[letters]`: a group written in ordinary letters; put `?` inside for an unclear letter, e.g. `[d?l]`.
- `X:short-description`: a sign that matches no row (e.g. `X:circle-with-cross`).
- `{clear}`: a stretch of ordinary handwriting in plain language (not cipher), e.g. a date at the end.
- `/`: a visible gap between groups of signs (word gap). Optional but helpful.

Rules:
- Be careful with the small marks: dots, bars, short strokes and small circles attached to a sign often decide which row
  it is (compare rows that look alike, e.g. the different 7-like shapes, the pi-like shapes, the =-like shapes).
- If a sign is cut by the edge between part a and part b, transcribe it once, in the part where most of it lies.
- Do not guess from what "should" come next; there is no meaning to use. Use `?` freely when unsure.
- Do every crop in `crops/` (72 files). Do not open any file outside `helper_pack/` and your own output folder; do not
  search the web. Do not write any file named REPORT.md.
- When finished, also say in your hand-back message roughly how confident you are and which rows you found hardest.
