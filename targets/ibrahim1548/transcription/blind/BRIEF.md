# Blind transcription of three cipher lines

Work only in this folder: `C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\ef13acc1-ef32-438e-88a0-406fb686ecb2\scratchpad\blind\`.
Do not open, search for or read any other file or folder on this machine (not the repository, not other scratch
folders, not other transcriptions of this page). The point of this task is that you work from the images and the key
alone, with no knowledge of what the text says. If you come across a transcription or a Latin text of this page,
stop using it and say so in your report.

## Task
`lines/L08_a.jpg` ... `L10_b.jpg` are 2x crops of three lines (8, 9, 10) of a 16th-century cipher letter in Latin.
Each line is cut in a left part (`_a`) and a right part (`_b`); the two overlap by about 160 px at the original scale
(about 320 px in the crops): the signs in the overlap are the same signs, do not count them twice. Each crop also
shows slivers of the lines above and below; transcribe only the line in the middle.

The key (same family as this cipher) is in `KEY_BRIEF.md` and `k367.txt`. Read both first. Its values may contain
errors; trust the shapes you see.

## Output
Write to `blind_lines_08-10.txt` in this folder, appending each line as soon as it is finished, two lines per cipher line:

```
L08 SIGNS: <label> <label> ...
L08 READ : <value> <value> ...
```

- SIGNS: one token per sign in reading order, a short ASCII label of the shape; the same shape always gets the same
  label (keep a legend in `blind_labels.txt`). Latin-letter words inside the cipher (nulls such as idcirco, atq, spu, cum,
  Dar, Der, Porro, and loose b, d, n, z) are one token each, in quotes.
- READ: the value the key gives that sign: a Latin letter, `[et]`, a code syllable in brackets, `.` for a null,
  `?` when unsure, `a/b` for two candidates. If you choose between candidates because the surrounding Latin makes
  one word more likely, add `^` to that value. Never invent a sign. `~` after a label marks a doubtful shape.
- Doubled letters are single signs (3=cc, 12=tt, 13=ss, ...): write the pair as the sign's value, e.g. `ss`.
- At the end of each line add a `NOTE:` line if something is odd.

Finish with a short reply: lines done, signs per line, how many `?` and `^`.
