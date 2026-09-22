# Brief: refine the reading of f. 119 to word level

Folder `C:\Users\dbour\cypher\guise1587\`. Letter to Mercœur, 27 May 1587, homophonic cipher with Lasry's key
(`GL_BnFfr15564.png`, enlarged in `key_top.png` / `key_bot.png`).

Inputs for each manuscript line NN:
- `img/yNN.png`: the line shown as three stacked thirds (left, middle, right). The line to read is the one marked
  by the red tick at the left edge of each strip (the row just above the tick); other rows are neighbours.
- `f119_glyphs.txt`: my sign-label transcription of that line.
- `f119_beam.txt`: a machine decode (beam search over key candidates, French LM). Mostly right; errors come from
  signs I labelled wrongly or merged (loop = A or S; C-shapes = L, R, F; slash = A, C, P; 6 = E, R, M; h = I, N, O).
- `f119_reading.txt`: my word-level draft, with […] gaps.
- `f142_reading.txt`: the sibling letter, already read, for vocabulary and style.

Task: for each of your lines, look at the image sign by sign, compare with the beam decode, and produce the best
word-level French reading. Fix the letters where the image or the key shows a different sign. Mark anything you
cannot read as [?] and anything doubtful as [word?]. Do not make up smooth text: every word must be backed by the
signs. Nomenclator groups (ff-ligatures) in UPPER case; digit groups (21, 43, 71, N, &) are names: leave as [21] etc.

Output: append to your output file as you go, one line per manuscript line:
`NN | reading | n_signs_total | n_signs_unread_or_doubtful`
(count signs from f119_glyphs.txt for that line; unread = signs inside [?] or [..?]).
Final report: the full reading of your lines, the totals, and any sign values that contradict the key.
