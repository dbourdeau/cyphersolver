# Notation for the blind transcription of SP 70/143 f. 93 (Guaras, London, 15 Feb 1577)

Written 27 Nov 2026 at 23:12 EST (file time), by the AI agent working this lead, before any decoding. The notation describes sign
shapes only; it carries no values.

Images: `strips/P1Lnna.jpg` and `strips/P1Lnnb.jpg` are the left and right halves of line nn of the first page
(f. 93r, 33 cipher lines, below the clear opening); `strips/P2Lnn?.jpg` the same for the second page (f. 93v,
14 cipher lines, above the clear closing). The target line is the one level with the small red tick at the left
edge; neighbouring lines show above and below. The two halves overlap by about 120 source pixels (a few signs):
continue the line from the `a` half into the `b` half without writing the overlap twice.
`strips/P1_overview_numbered.jpg` and `strips/P2_overview_numbered.jpg` show the line numbers. Full page images:
`../../sources/raw/guaras1577_2026-11-28/pages/SP70-143_img00.jpg` (f. 93r is the right-hand page) and `_img01.jpg`
(f. 93v is the left-hand page).

## Tokens (write them separated by single spaces)

- Latin letter shapes as they look: `a b c d g h i m n o r u v x y z` (and any other letter if a sign is plainly that
  letter). Specific choices:
  - `d`: round body with the stem curling back over it to the left (like a Greek delta).
  - `g`: g with a closed lower loop (like an 8 with an open top).
  - `9`: the 9 or q shape with a straight stroke below the line.
  - `b`: b with a tall stem and a closed bowl. `B`: the same b with a horizontal tail or flag running out to the
    right at mid height.
  - `z`: a small 2-like sign sitting on the line.
  - `Z`: a 3-like sign whose lower part runs below the line (like a yogh).
- Tall strokes reaching below the line:
  - `S`: plain tall stroke (long s), no loop, no crossbar.
  - `P`: tall stroke with a loop or flag at the top opening to the right (like a p with a long stem).
  - `T`: tall stroke with a horizontal crossbar (like a dagger or a crossed long s).
- Digits `0`-`9` when a sign is a digit shape inside a cipher group.
- A number written between dots (for example `. 35 .`): write `#35`. Several dotted numbers in a row: `#16 #0 #17`.
- `~` straight after a token that carries a tilde or bar above it (for example `x~`).
- `<` and `>` around a stretch that is underlined in the manuscript.
- `|` for a visible gap between groups of signs.
- `?` for a sign you cannot read; `a/b` for two possible readings, the more likely first.
- Plain (clear) Spanish words in the line: put them in `[[ ]]` as read.

## Output

One line per manuscript line, for example `P1L01: m g c d ...`. After the lines, list any sign shapes that the
notation does not cover, with the line where you saw them.

## Known fault in the strips (noted 27 Nov 2026, 23:28 EST, after both readers reported it)

On f. 93r the lines run downhill to the right by about one line spacing, so the `b` (right) half strips of page 1
mostly show the end of the line above the tick's line. Reader A worked from deskewed crops of the full page instead;
reader B paired `P1Lnna` with `P1L(nn+1)b` and read the end of line 33 from the page image. Page 2 strips are right.
