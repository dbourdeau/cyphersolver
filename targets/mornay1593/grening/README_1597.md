# Duplessis to Cargroy, 19 Jan 1597 (vol. 7, LXVI): letter key and reading

Shawn Grening, 28 Nov 2026, working with Claude (Anthropic). Uses the repo's transcription `../duplessis1597.txt`
(runs C1-C8) unchanged; I compared its figures with the page images of pp. 124-126 and they agree. Follows the
Loménie 1595 reading in this folder (`README.md`).

Status: 6 of the 8 passages read exactly, 132 of 155 figures. C1 reads in part ("du [?parti] [?contraire]"). C5 is
not read. The three runs of the next letter (LXVII, to his wife, W1-W3) are another system and are not read.

## 1. Files

| File | What |
|---|---|
| `key_duplessis1597.tsv` | the letter values, with which are attested and which only inferred |
| `duplessis1597_decryption.txt` | every passage: figures, the letters each figure allows, the reading, exact or not |
| `duplessis1597_reading.md` | the sentences in French with the cipher words restored, and an English translation |
| `scripts/check_reading_1597.py` | writes the decryption file from `../duplessis1597.txt` and the key (standard library) |
| `scripts/test_key_1597.py`, `results/test_key_1597.txt` | three tests of the key and their output (section 4) |

Run from this folder: `python3 -I scripts/check_reading_1597.py`, and
`python3 -I scripts/test_key_1597.py <path to mmoiresetcorre06morn_djvu.txt> --anneal` (add `--shape` for the second run).

## 2. The system

The same method as Loménie's letter of 1595: one figure 1-10 per letter, two letters written together as a group
(u n = 5 8 = 58, p r = 10 2 = 102). The table is a different one. It is the alphabet in order, ten letters to a
round, starting at a = 7:

| Figure | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Letters | e q | f r | g s | h t | i u | l x | a m y | b n z | c o | d p |

i/j and u/v are one letter each; there is no k or w. f, h, x, y and z do not occur in a passage that reads and are
inferred from their place in the alphabet. Where the words have an odd number of letters the clerk filled the
last pair with e, so the last group is 11 (C2, C3, C6).

Loménie's folded table gives no words on these figures (`README.md` section 6), and neither do its ten shifts
(checked 28 Nov 2026 with the same letter model). Duplessis's letter to his wife of the same days (W1-W3: 40, 80, 132, printed letters) is a third system.

## 3. How it was found

After the Loménie key, the guess was that Duplessis's own figures of January 1597 use the same method with another
table. The plainest table is the alphabet in order, which leaves ten keys, one for each figure a can take. An AI
agent run tried them and a = 7 gave words; I have no log of that run, so I repeated the ten-way test (section 4,
test 0). No crib was used: the names came out of the key. The transcription is the repo's (25 Oct 2026), made
before any key existed.

## 4. Tests, written after the reading (`scripts/test_key_1597.py`, `results/test_key_1597.txt`)

Not pre-registered. Model: letter trigrams from the vol. 6 OCR text (the same file as `../beling/`, sha256
2049...5574), with CVI, CVII and the table of contents cut out. Vol. 7, which names both men in clear, is not in
the model. A key is scored by the best lettering it allows.

- **Ten rotations.** On all eight passages (155 figures), a = 7 scores -2.222 per figure. The other nine score
  between -2.753 and -3.128.
- **Held-out passages.** With the twelve letters of the two names (C6, C8) fixed, the alphabetical rule beats
  2,000 of 2,000 random fillings of the other ten letters on C2, C3, C4 and C7 (110 figures): -2.224 against a
  null mean of -2.678, sd 0.208, best -2.238; z = 2.2.
- **No cribs, free search.** Twelve annealing runs from random keys reach -2.188 to -2.338 (1-4 letters per
  figure) and -2.205 to -2.430 (2-3 letters). The key scores -2.222. Five of the 24 runs score a little above it;
  one of those agrees with it on 11 of 17 attested letters, the others on at most 4.
- What this means: as with Loménie's letter, a letter model alone does not single the key out among all possible
  tables. Within the ten tables of the hypothesis it does, by a wide margin. The reading rests on that, on the
  held-out result, and on the sense: two men named in clear elsewhere in the volume, and phrases that fit their
  sentences ("vous doibt mener un prisonnier de qualité pour estre conduict ici", "pour n'attirer ruine sur sa
  maison").
- `docs/_validate.py` does not apply (polyphonic key).

## 5. Weak points and what is not done

- C1: the print has 119 where "parti" wants a 5, and "contrai" has no ending. Two words doubtful.
- C5 (eight figures) is not read.
- f, h, x, y, z are inferred.
- Everything is from the 1824 print; I have not seen the manuscript.
- Not tried: Duplessis's figures to his wife of Sep 1597-Apr 1598 and of 1599 (`../beling/transcription/`).
- Courbejoliere and Montbarot are not identified beyond their names.

## 6. Prior publication

None found (28 Nov 2026): this repo's issues and pull requests (NOTES.md has the Jan 1597 figures unread),
`quietofwinter/historical-ciphers`, `pangoleen/cipher-readings`, Europe chiffrée (which mentions these figures
only as a negative test of the 1593 key), the Cryptiana index, and a web search. DECODE was not reached.
