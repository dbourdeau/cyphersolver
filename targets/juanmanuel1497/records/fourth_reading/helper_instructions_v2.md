# Instructions for a blind transcription helper (round 5)

You transcribe signs from images of a handwritten page. You are not told what the signs mean and you must not try to
find out: copy shapes only.

Your folder contains:
- `signsheet_W_part1.png` (W01-W19), `signsheet_W_part2.png` (W20-W38) and `signsheet_W_part3.png` (W39-W49): 49
  reference rows. Each row shows several
  examples of ONE sign, cut from these same letters; the examples differ a little because they are handwritten.
- `lines/`: one image per manuscript line, named like `A01.png` (the letters give the page, the number the line).

Each line image shows ONE manuscript line cut into three overlapping segments, stacked top to bottom, enlarged 3x. The
line has been straightened, so the line you transcribe runs level through the middle of each segment, at the height of
the red arrows. Signs from the lines above and below also show and must be ignored, as must ink showing through from
the other side of the paper (lighter brown, often mirror-reversed, usually thinner). Green dashed vertical lines mark
the part of each segment you are responsible for: transcribe a sign in a segment only if its centre lies between that
segment's green lines, so that every sign is written exactly once. Read the three segments in order, left to right.

Rules:
1. Write one output line per image, in file-name order: `A01: tok tok tok ...` (tokens separated by single spaces).
2. For each sign, the id of the sheet row it matches (W01-W49). Look closely at small marks: dots (how many, above or
   below), bars, the number of legs, a small o or loop attached, a cross-stroke through a stem.
3. A sign that matches no row: `?(short description of its shape)`, e.g. `?(figure 3 with a tail)`.
4. A damaged, blotted or unreadable sign: `#`.
5. A group of ordinary Latin letters written in the line (for example something that looks like `dal`, `bon`, `def`):
   write the letters you see inside braces, letter by letter exactly as written, e.g. `{dal}`, `{bon}`; do not
   normalise them and never use a W id for them. A letter you cannot make out inside a group: `{d?l}`. If you cannot
   decide between two letters, write the more likely one and add a comment line.
6. A stretch of ordinary handwriting (words in the normal script, not signs): one token `<clear>`.
7. Comment lines start with `!` (e.g. `! A07: third sign could also be W12`). Keep them short.
8. Work only from the files in your folder. Do not open, search or list any other file or folder on the computer, and
   do not use the web. Do not create a file named REPORT.md. Write your result to the output file named in your task,
   in your folder, then reply with a short note (number of lines, anything that troubled you).

## Signs that are easy to confuse (shapes only)

- W01 plain pi (two legs, nothing above); W02 pi with two dots above; W03 pi with a small o joined at its right;
  W04 a T with ONE stem and two dots above. Count the legs, then look above.
- W09 ONE bar with a dot above and a dot below; W10 TWO parallel bars with a dot above.
- W11 plain 7; W12 a 7 with a short crossbar through its stem; W13 a small closed o touching the left of a 7;
  W14 a zigzag, a stroke crossing the top of a slanting stem (like a lightning sign or a 4); W15 an open angle.
- W17 an x with a bar across its top (hourglass); W18 a looped x with a long tail sweeping down to the left.
- W20 a long stem with a small o threaded on it; W21 a plain stem with dots beside it.
- W22 a LARGE C crossed by a slanting stroke, no dot inside; W23 a smaller c with a DOT inside; W24 a large reversed
  hook with a stroke.
- W25 a large D-shape (it opens a passage); W26 a small v or u with a bar across its top. W26 is its own sign: do not
  file it under W01, W11 or W25.
- W28 one bowl, then an f (an UPRIGHT stem with a crossbar); W29 two small hooks, then a long stroke sweeping DOWN TO
  THE LEFT (no upright stem); W30 n followed by t; W31 n followed by a z-like tail; W32 a u- or y-like form + t (one or
  two t's); W33 a 3- or g-like form + t.
- W34 an inverted T standing on a base bar, followed by o or v (one sign); W35 an inverted T alone; W36 an upright
  with a crossbar to its right; W37 a gamma / y shape with a bar at its foot.
- W05 two short uprights on a base bar; W06 an m on a base line; W07 a c joined to a t; W08 a tall beta.
- NEW rows W39-W49 (sheet part 3): W39 an upright with a short arm to the right at its top, followed by a small o
  (one sign; do not split it into W36 + o); W40 an x with a dot on EACH side; W41 an alpha (closed loop) joined to a c
  WITH a bar across the top; W42 the same alpha + c WITHOUT a bar (it can look like two small linked c's or o's; look
  for the bar to choose W41 or W42); W43 a small o standing ALONE (not joined to a 7 as in W13, to a pi as in W03, threaded
  on a stem as in W20, or after an arm as in W39); W44 a p with a cross-stroke on its descender; W45 a plain p; W46 an
  S-shaped stroke; W47 a figure 9 with a long tail; W48 a figure 6 / G shape; W49 a # shape (two bars crossed by two
  strokes).
