# Brief: transcribe the cipher of HHStA StAbt Türkei I 7-4-4 f. 29 (copy A, "Dupl. 1548") sign by sign

The page is one letter, 13 lines of cipher, in the Ferdinand-Malvezzi key of 1548 (DECODE R367/R386) as far as we
can tell. Its plaintext should be the Latin exemplar on f. 30, `texts/exemplar_7-4-4_A.txt` (about 560 letters), with
nulls added. Nothing has been transcribed yet. You are the transcriber.

Work in `C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\ef13acc1-ef32-438e-88a0-406fb686ecb2\scratchpad\ib2\targets\ibrahim1548\`.

## Inputs
- `img/lines/Lnn_a.jpg` (left part) and `Lnn_b.jpg` (right part) for each line nn = 01..13, 2x enlargements. The two
  parts overlap by about 160 px at the original scale (x 820-980): the signs in the overlap are the SAME signs; do not
  count them twice. Each crop also shows a sliver of the lines above and below: transcribe only the line in the middle.
- `img/f29.jpg`: the whole page, if you need context.
- The key as far as it is known: `../malvezzi1548/KEY_BRIEF.md` (letters, nulls, code syllables, doubles, calibrated
  readings) and `../malvezzi1548/k367.txt` (the DECODE sign names). Read both first.
- The exemplar: `texts/exemplar_7-4-4_A.txt`. Use it as a crib: the cipher should spell it.

## What to produce, for each line
Two lines, same number of tokens, tokens separated by one space:

```
L03 SIGNS: <label> <label> ...
L03 READ : <value> <value> ...
```

- **SIGNS**: one token per sign, in reading order, left to right. Label what you see in short ASCII (e.g. `hash`,
  `pi`, `P-o`, `circ-stem`, `breve`, `3`, `+`, `taurus`, `Gamma`). Use the sign names of k367.txt where they fit and
  keep one label per shape throughout the page (the same shape always gets the same label; write the label list you
  used in `f29_labels.txt`). Words written in ordinary Latin letters inside the cipher (idcirco, atq, spu, cum,
  Dar, Der, Porro, ...) and loose letters b, d, n, z are nulls: write each as one token in quotes, e.g. `"idcirco"`.
  A full stop the writer put between nulls is a separator, not a sign; ignore it.
- **READ**: the value the key gives that sign, one per token: a Latin letter, `[et]`, `[ki]` for a code syllable,
  `.` for a null token, `?` when you cannot tell. Where a shape has two possible values write both: `u/e`. Where the
  exemplar decides it, take the exemplar's letter and add `*` (`u*`): these are the readings that depend on the
  crib, and we count them separately. Never invent a sign that is not on the page to make the Latin work.
- Mark a sign you cannot see clearly with `~` after its label (`pi~`).

## Rules
- Work from the images, one line at a time, in order. Append each finished line to your output file at once (do not
  keep a batch in your head): if you run out of room the finished lines must already be on disk.
- Do not edit the exemplar or the key files. Do not touch any other file than your output files.
- Be honest about doubt: a `?` costs us less than a wrong letter. At the end of each line add a `NOTE:` line when
  something is odd (damage, a sign not in the key, a line that does not fit the exemplar).
- Time box: if a line takes more than a few attempts, write what you have with `?` and go on.
