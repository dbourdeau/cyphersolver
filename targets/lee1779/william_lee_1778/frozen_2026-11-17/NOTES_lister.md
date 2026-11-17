# Lister notes

Model: Claude Opus 5.5 (claude-opus-5-5), working alone, no web, no other agents.

How I counted: for each page I made a 1000-px overview of the whole page, then cut the target column into 2-4 overlapping strips with `sips` (crop at full resolution, resized to 1400 px wide, roughly 3x the overview) in crops/. First count: entry by entry on the strips, using the first and last line of each overlap to join them. Second count: on the overview, counting headword lines in fives. Running heads, letter headings, catchwords and indented run-over lines were not counted; turned-up line endings in brackets at the right margin (e.g. "(tend") were not counted and are mentioned in the note column.

Count agreement: all 14 columns agreed on the second count except page 80 col a, where my first pass skipped "Cavalry" (between Cavalierly and Caudle); the recount caught it and the written list includes it (entry 19 = Cavalry).

Columns shorter than count_to: page 115 col b has 38 entries (count_to 41).

Least sure:
- page 415 col a: almost every headword lies in the gutter shadow; headwords restored from visible endings and definitions (Urgently ... Usance). Entry 10 ("oblique case of we", headword hidden, presumably Us) is counted as an entry; if it were a run-over the later numbers would drop by one.
- page 373 col a: lower half has the first letter(s) of each headword hidden in the gutter; line structure was clear, so the count is firm, spellings restored.
- page 177 col a: first letters slightly shaded but readable.

Housekeeping: early on I removed one empty test crop (crops/x.jpg) that my own helper script had just made; no other file was deleted.
