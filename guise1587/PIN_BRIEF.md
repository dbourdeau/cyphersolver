# Brief: sign-by-sign relabelling of weak lines of f. 119

Folder `C:\Users\dbour\cypher\guise1587\`. You MUST open (Read tool) the image of every line you work on:
`img/H<NN>.png` if it exists, else run `python zz.py <NN>` then build it (see how H21.png was made: the three
`img/h<NN>_<p>.png` strips stacked). The line to read is the main row of each strip (left, middle, right third).
Lasry's key: `key_top.png`, `key_bot.png`. Sign list and conventions: `AGENT_BRIEF.md`.

For each line NN:
1. Take its current labels from `f119_glyphs.txt`, the decodes from `f119_beam3.txt`, and the draft from
   `f119_reading.txt`.
2. Walk the image sign by sign alongside the labels. Wherever you are sure of a sign's letter (from its shape in
   the key AND the French word it makes), replace the label with a pinned letter `'x` (e.g. `'r`). Fix missing or
   extra signs. Keep nomenclator groups `[..]` as they are unless clearly wrong.
3. Write the corrected glyph line as `NN | <labels>` and, on the next line, `#R NN | <your French reading>` with
   [?] for signs still unread, to your output file, appending as you go.

Rules: every pinned letter must be backed by the image; do not pin to force a smooth sentence. Report at the end:
lines done, and for each line how many signs remain unread.
