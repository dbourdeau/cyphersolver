# Blind transcription brief (neutral labels)

You are transcribing cipher signs from photographs of four letters (Florence, 1492-93). Work only from the files in this folder. Do not open any other file, repository or web page, and do not try to decipher anything.

## Files
- `SHEET.tsv`: the sign inventory. Each sign has a neutral label (S01 ... S67) and a description of its shape. Labels carry no meaning.
- Eight images, two per letter: `<doc>_L.jpg` is the left half of the lines, `<doc>_R.jpg` the right half. The halves OVERLAP by a few words in the middle: transcribe each sign once (join at the overlap).
  - d42 (c. 90r): a postscript of about five lines. Clear Italian words and cipher signs are mixed on the same lines.
  - d49 (c. 104r): one line, the middle one of the three visible, with a run of cipher after some clear words.
  - d81 (c. 177r): one line, the third visible line, almost all cipher.
  - d90 (c. 200r): one line, the middle one of the three visible, with a run of cipher between clear words.

## What to write
For each doc, one file `BLIND_<doc>.tsv` with columns: `doc  line  run  labels  note`.
- One row per cipher RUN (a stretch of signs between clear words or spaces). `line` = line number within the passage (1 = first line containing cipher). `run` = order within the line.
- `labels` = the signs of the run in order, space-separated, e.g. `S12 S03 S40`.
- An unreadable or doubtful sign: write `S12?` (best guess) or `??`.
- A shape not on the sheet: write `NEW1`, `NEW2` ... and describe it in `note`.
- Write clear (plain Italian) words only in `note`, in square brackets, before or after the run they touch, so the run's place in the sentence is kept, e.g. `[before: Hor non cessa] [after: rispode]`. Do not put clear words in `labels`.
- Do not split or join runs by guessing at words: keep the gaps as they appear on the page.

Also write `READER_NOTES.md`: the number of runs and signs per doc, the shapes you found hard to tell apart, and any place where the sheet did not fit.

Finally stop. Do not decode, and do not look for a key.
