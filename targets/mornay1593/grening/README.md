# Loménie to Duplessis, 24 Feb 1595 (vol. 6, CVII): letter key and reading

Shawn Grening, 27 Nov 2026, working with Claude (Anthropic). Builds on Andrew Beling's two cribs (`../beling/`,
NOTES.md step 8) and on the repo's transcription `../lomenie1595.txt`, which is used unchanged.

Status: 13 of the 15 passages read exactly, 158 letters; one more (L8) reads "du roy" only with a value for y that
is seen nowhere else, and is marked doubtful; one is read in part (L15). The name figures in the clear text (3, 11, 14, 16, 25, 26, 98, 99) are not read.

## 1. Files

| File | What |
|---|---|
| `key_lomenie1595.tsv` | the letter values, with which are attested and which only inferred |
| `lomenie1595_decryption.txt` | every passage: figures, the letters each figure allows, the reading, exact or not |
| `lomenie1595_reading.md` | the sentences in French with the cipher words restored, and an English translation |
| `scripts/check_reading.py` | writes the decryption file from `../lomenie1595.txt` and the key (standard library) |
| `scripts/test_key.py`, `results/test_key.txt` | two tests of the key and their output (section 5) |
| `images.txt` | the archive.org page images read; none committed |

Run from this folder: `python3 -I scripts/check_reading.py`, and
`python3 -I scripts/test_key.py <path to mmoiresetcorre06morn_djvu.txt> --anneal` (add `--shape` for the second run).

## 2. The system

Each letter is one figure from 1 to 10. Two letters are written together as one group, and a last odd letter stands
alone: d e = 8 10 = 810, e t = 10 9 = 109, b r = 4 4 = 44. So the "x10 word codes" (810, 910, 410, 610) are
not word codes: they are a letter followed by e or o.

The alphabet is folded onto the ten figures in five runs:

| Letters | Figures | |
|---|---|---|
| a b c d e | 2 4 6 8 10 | even, rising |
| f g h i l | 1 3 5 7 9 | odd, rising |
| m n | 1 2 | |
| o p q r s | 10 8 6 4 2 | even, falling |
| t u x y z | 9 7 5 3 1 | odd, falling |

i/j and u/v are one letter each; there is no k or w. Every figure therefore stands for two or three letters
(2 = a, n, s; 10 = e, o; 7 = i, u), and the reader chooses by sense. It is the same idea as the 1593 key Brice Dudout
recovered (a folded alphabet, two letters per group), with ten values in place of twenty-odd.

f, x and z do not occur in any passage. Their values are the ones the pattern gives and are marked "inferred" in
the key file. y occurs at most once (L8), where the print has 8 and the pattern would give 3; see section 4.

## 3. How it was found

1. Andrew Beling's cribs, "du sieur 810 62 110 4" = "du sieur de Camor" and "810 44 109 27 32 10" = "de Bretagne"
   (NOTES.md step 8), were the starting point.
2. "de Camor" has seven letters and 810 62 110 4 has nine digits. Read with 10 as one figure, it has seven figures:
   8 10 6 2 1 10 4. That gives d 8, e 10, c 6, a 2, m 1, o 10, r 4, with e and o sharing a figure.
3. Split the same way, the second crib has eleven figures, 8 10 4 4 10 9 2 7 3 2 10. "de Bretagne" has ten
   letters; with the spelling of the king's letter, "de Bretaigne", it has eleven and fits: b 4, r 4, e 10, t 9, a 2,
   i 7, g 3, n 2, e 10.
4. a 2, b 4, c 6, d 8, e 10 is the alphabet on rising even figures, and g 3, i 7 continue on odd ones. Filling the
   rest by the same rule gave the table above, and the other passages were then read with it.

So the two cribs were used; this is not a ciphertext-only solution.

## 4. Why I think it is right, and where it is weak

- 13 passages encode to exactly the printed figures (`lomenie1595_decryption.txt`). Because each figure allows two or
  three letters, a single short word would prove little. The weight is in the long ones and in the context:
  - "de lui promettre telle **ville de seureté de Bretaigne**" (25 letters) against the king's letter of the same
    day, "telle aultre ville de mon pays de Bretaigne, qu'il aura agreable" (CVI, p. 179);
  - "le service **de Vennes**" against "tant pour le regard de Vannes" (CVI, p. 178);
  - "si vous ne m'aviés rien mandé de **l'assamblée de Saumur**" (18 letters), to the governor of Saumur;
  - "les deputés de **Bearn** mesmes pour **la messe**";
  - "et M. **le marquis de Belisle** seront ses serviteurs" (18 letters).
- Weak points:
  - L8, 87 410 8: "du ro" is certain and "du roy" fits ("la necessité des affaires du roy"), but the last figure
    is a clear 8 in the print. Either y = 8, which breaks the pattern, or y = 3 and the 8 is a slip. y occurs
    nowhere else, so the print cannot decide; the manuscript could. The key file carries the printed 8.
  - L15: 100 76 is not read. 100 may be a name figure like the 98 and 99 in the clear text; that is a guess.
  - "en **de Camor**" (L2) reads as letters but I cannot make good sense of the "en".
  - Everything is from the 1824 print.
- No test was pre-registered. The table was built on L1, L2 and L4; the other passages were read afterwards, but
  nothing was frozen before I looked at them. Section 5 has two tests written afterwards.

## 5. Tests, written after the reading (`scripts/test_key.py`, `results/test_key.txt`)

Model: letter trigrams from the vol. 6 OCR text (the same file as `../beling/`, sha256 2049...5574), with the king's
letter CVI, this letter and the table of contents cut out. A key is scored by the best lettering it allows.

- **Held-out passages: the rule beats chance.** The twelve letters the two cribs fix keep their values. The other ten
  are filled by the folded-alphabet rule, or at random in 2,000 null keys. On the passages the cribs do not touch
  (130 figures) the rule scores -2.045 per figure; the null keys have mean -2.282, sd 0.060, best -2.106. The rule
  beats 2,000 of 2,000 (z = 3.9).
- **Without the cribs a search does not find the key.** Twelve annealing runs from random keys, on all passages,
  reach -1.947 to -2.080 (1-4 letters per figure) and -1.985 to -2.087 (2-3 letters per figure). The pattern key
  scores -2.050. Eleven of the first twelve runs and seven of the second twelve score above it, and none agrees
  with it on more than 10 of its 18 attested letters.
- What this means: on 163 figures, with two or three letters to a figure, letter statistics cannot pick the key
  out. In the terms of `docs/_validate.py` the reading is "underdetermined" (that script itself reports "not
  applicable" for a polyphonic key). The reading does not rest on a letter score. It rests on the two cribs, on the
  regular table they lead to, on that table then doing better than chance on the passages it was not built on, and
  on whole phrases that match the king's letter of the same day.

## 6. Not done

- Duplessis's own figures: I split the eleven passages of `../duplessis1597.txt` the same way and looked at the
  letters the key allows. No words, three figures that are a bare 0, and far too many 5s (h or x). The key does not
  fit them, which agrees with NOTES.md step 8 ("probably two systems"). This was a look, not a scored test, and I
  did not try the 1597-99 figures in `../beling/transcription/`.
- I have not seen the manuscript. NOTES.md (Escalation, print) lists where the originals may be: AN 402AP/13 and
  the Mornay papers at Nantes. It would settle y in L8 and the 100 76 of L15.
- The persons are not identified beyond the names as written (Camor, Boisdauphin, Belisle).

## 7. Prior publication

None found: this repo (NOTES.md "1595-98 figures open", checked 27 Nov 2026), Jason Benham's
`quietofwinter/historical-ciphers`, and web searches for the letter with "Camor", "Boisdauphin" and "chiffre". The
1824 editors say they printed bare figures where they had no key (vol. 6 p. 82 n. 1).
