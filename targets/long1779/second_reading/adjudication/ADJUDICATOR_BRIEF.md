# Adjudication brief: Enoch Long's cipher journal

Two readers have transcribed the cipher words of each line independently. Where they differ, or where either left a
word unread, you decide what the image shows, sign by sign.

Open only: this brief, `../blind/READER_BRIEF.md` (the sign chart; read its alphabet section), the chart images in
`../chart/`, your packet file, and the crops `../crops/Kxxx.png` named in it. Open nothing else (no other .tsv or .md in
`work/`, nothing outside `work/`, no web). Do not delete any file. You may make enlarged copies of crops in your own
scratchpad.

Each packet item gives two readings, X and Y, as sign strings (a letter per sign; `a/b` = that reader could not choose;
`?` = sign not read), with the word each reader made of them in brackets, if any. X and Y are in random order: neither is
known to be the better reader. `(not read)` or `(nothing read here)` means that reader gave no reading for this word or
saw no word there. The word number is only a rough guide to the word's place in the line; find the word by its signs.
If the two readings clearly describe different words (the item is misaligned), say so and judge each against the word
it describes.

Rules:
1. Judge each sign on the image only. Whether a reading makes good English is NOT evidence that a sign is there. A sign
   is "clear" only if you can see its distinguishing strokes (see the look-alike list in the reader brief) and could
   not take it for its look-alike.
2. If a sign could be either of two letters, write both (`r/s`). If you cannot see it, write `?`.
3. Then, separately, say whether the final signs make an English word that fits the line, and which. If the signs
   allow two words, give both. If no word fits without changing a sign you judged, leave the word empty.
4. Be especially strict on names and on words in private or intimate passages. Do not complete a word from what the
   sentence seems to want.

Write `out_packetN.tsv` (N = your packet number) in this folder, header:

`id	verdict	final_signs	n_signs	n_clear	all_clear	word	alt_word	note`

- `verdict`: `X`, `Y` (that reading is right sign for sign), `neither` (your own final_signs differ from both), `both-wrong-place`
  (misaligned item), or `illegible`.
- `final_signs`: your sign string, space-separated, as in the readings.
- `n_signs`, `n_clear`: number of signs, and how many are individually clear.
- `all_clear`: `yes` only if every sign is clear.
- `word`, `alt_word`: as rule 3.
- `note`: brief reason, especially for any sign you judged differently from both readers.

Every row must have 9 tab-separated fields (keep empty fields). Finish with a short report: items done, how many X, Y,
neither, illegible; crops that were poor.
