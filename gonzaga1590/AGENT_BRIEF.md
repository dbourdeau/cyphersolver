# Transcription brief: Mantua → Nevers, 17 Sept 1590 (BnF fr. 3979 f. 92–93)

Folder: `C:\Users\dbour\cypher\.worktrees\gonzaga1590\gonzaga1590`. Images in `img/` (do not commit them).

The letter is Italian clear text with passages in figures, written as unseparated runs of digits.
The key has been found (BnF fr. 3995 f. 64, "Per Cavare 1590"). Every figure is **two digits**, read in pairs
straight across line breaks:

- 11–40 are letters: 11 m 12 f 13 a 14 h 15 e 16 n 17 p 18 g 19 b 20 z 21 d 22 a 23 t 24 u 25 o 28 u 30 l 31 r
  32 t/i 33 c 34 t/i 35 o 36 c/e 37 i 38 a 39 o 40 s. (26 Inglesi, 27 Venetia, 29 Consiglio are words.)
- 41–99 are words and names, e.g. 72 Regno di, 84 Francia, 96 Spagnoli, 97 Roma, 81 Spagna, 80 Francesi.
- Occasional signs (⊖, ⊕, crossed bars, □ etc.) stand for words; write them as `{sign-description}`.

Handwriting traps: **3** is written like ʒ with a descender and looks like **9**; **8** is written as a looped ø/∞
and looks like **0**; the 6 looks like a b with a tall ascender. A tens digit is only ever 1–4, so if you get a pair
starting 5–9 you have misread or lost phase.

Tools:
- `python crop3.py img/<file> <TAG> <y1,y2,...> <x0> <x1> <n>` writes 3× contrast crops `<TAG><line><piece>.png` to
  the current dir (run it with cwd = a scratch dir, e.g. `%TEMP%\r4176`; pass the absolute image path). The y values are the centre
  of each cipher line in original pixels; n pieces across (7 works well).
- `PYTHONUTF8=1 python beam.py <file>`: file of lines `tag | digits`; prints the LM-best decryption, allowing 3↔9, 0↔8
  look-alike fixes. Use it to check a line; if a stretch decodes to nonsense, re-look at the image there.

Work: transcribe **every** cipher passage in your assigned images, in reading order, digit by digit, noting the clear
words before and after each passage. Append results to your output file as you go (one line per manuscript line):
`p<page>l<n> | digits`, then after each passage a line `# decode: <beam output, cleaned by you into words>`.
Mark uncertain digits with `?` after them only in a separate `# note:` line (keep the digit line pure digits and {signs}).
Do not guess plaintext into the digits: transcribe what is written.

Report back: the output file path, number of cipher lines done, and your cleaned reading of each passage.
