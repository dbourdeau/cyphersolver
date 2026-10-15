# Brief: value-blind transcription of cipher lines, Matignon Cipher-3 (BnF fr. 15572, 1586)

You transcribe 16th-century cipher signs **by shape only**. You are not told what any sign means. Do not try to decipher,
and do not guess French words.

## Inputs

1. **Sign chart:** `key/chart_blind.png`.
   - Every known sign sits in a numbered column C01–C23. The rows within a column are variant shapes of the same column.
     Columns are divided by red lines; the two boxed groups at the right of the body are extra variants (box 1 = C12 /
     C18 / C19, box 2 = C19 / W06), as the blue note says.
   - Word signs are W01–W07 (bottom strip, green). Note W05 has two forms (a "p" with a stroke, and a "z" with a hook).
   - Open the chart first and keep it in mind. It is a hand-drawn redrawing, so the manuscript signs are messier.
2. **Line crops:** the folder named in your task. Files are `L<line>_<segment>.jpg`.
   - Segments 0, 1, 2 run left to right, and neighbouring segments overlap by about one or two signs.
   - Some crops may show a fragment of the line above or below at the top or bottom edge: ignore those.

## Rules

- Read only the chart, this brief and your crop folder. Don't open other project files, and don't search the web.
- For each sign, output the chart id whose shape it matches: C01..C23 or W01..W07, **with the row of the matching
  variant**: `C13r1` for the first (top) sign of column C13, `C13r2` for the second, and so on. The row matters: the
  variants of one column are different signs in the manuscript, and we need to keep them apart.
  - If torn between two ids, write `C05r1|C16r2`.
  - If a sign matches nothing on the chart, use `X:<short description>`, e.g. `X:double-barred H`, `X:big script L`,
    `X:S with hook`. Describe the shape, not a letter value.
  - Use `?` if illegible.
- The signs in this hand include Arabic numerals written as a unit (13, 14, 18, 19, 20, 23, 30, 57, 60): a two-digit
  number is ONE sign. Match it to the chart column that shows that number.
- **Small marks matter.** A bar across, a dot, a loop, a tail, a hook, a circle above: say so in an `X:` description when
  a sign is a marked form of a chart sign, e.g. `X:C13 with a bar above`.
- Two dots or a colon after a sign (`..`, `:`) are probably part of the sign or a separate mark: write `X:two dots`.
- Merge overlapping segments: don't repeat a sign that appears at the right edge of one segment and the left edge of
  the next.

## Output

One line per cipher line, with tokens separated by spaces:

    L01: C13 C04 X:big script L C01 C02 ...

Then a short list of the positions you were unsure of. Return only this.
