# Independent CTTS transcription and reading of catalogue 2393 (George Lasry, 25 Nov 2026)

An independent transcription of ASF MAP CXXXVII doc. 666 (cc. 674r-674 bis v) made in CTTS, with the key recovered from
the ciphertext alone and a line-by-line reading. It was made without knowledge of this folder or of Brice Dudout's key
v6; the two were compared only afterwards. Work done with AI agents (Claude) under George Lasry's direction.

## Files

- `transcription/all.txt`: CTTS transcription, one row per manuscript line, tokens separated by `;`. `# N.png` heads each
  image: 0 = c. 674r, 1 = c. 674v, 2 = c. 674 bis r, 3 = c. 674 bis v, 4 = a separate clear letter photographed with the
  set (Alfonsina Orsini, Florence, 6 Sept 1515; not part of doc. 666). `base^upper` = sign with the figure written above
  it; `CLEARn` = a plaintext segment (its text is in `key.txt`); `15`, `20`, `22`, bare `2` and `4` = numbers between points.
- `decryption/all.txt`: the unedited output of the key on that transcription, token by token.
- `edited/edits.txt`: the reading, one row per manuscript line, plaintext and decrypted cipher together, word-divided.
  Square brackets = expanded abbreviations of the plaintext and letters the writer omitted. `.15.` and `.22.` are left as numbers.
- `key.txt`: CTTS key (`label - value`), 127 sign values followed by the 64 plaintext segments.
- `snapshots/`: CTTS graphical key (`key.png`: label, value and sample crops of each sign), `decryption key.png`, `symbols.png`.

## System, as recovered

Base sign with a figure above = consonant + vowel (5 = a, 4 = e, 3 = i, 2 = o, 1 = u); bare signs = single letters;
`#` ligatures = doubled consonants (ll, nn, cc, gg, tt, bb, rr); word signs (F et, D che, a+ per, M non, D^m con, T^m Sua
Maesta, T^o secondo, T sempre, T^2 senza, u tanto, u^o tempo, D^5 come, B^o quanto, F^o effecto, B anchora); numbers
between points (.2. Papa, .4. Re, .20. Svizeri; .15. and .22. not identified); `Lam^o` = full stop; the marks after it
at a block end are nulls. The key was reached from repeats and cribs (`3^3 s^3 x^5 t^2` = di Milano, 9 times;
`w y 8^4 y 3^4 7^4` = intendere) and confirmed by a blind simulated-annealing search without cribs.

## How it was made

1. Signs boxed and labelled in CTTS on all four pages; plaintext segments as `CLEARn`.
2. Key recovered from the ciphertext; six independent runs under different starting hypotheses converged on the same key.
3. Correction pass: every word that did not read was checked against the images (original and a bleed-through-reduced
   copy) and the labels corrected: about 150 changes in all (reclassified signs, merged number groups, a few added or deleted boxes).
4. Reading written line by line.

## Readings that rest on the sentence more than on a clear image

- c. 674r: "volere" for a sign that occurs once (L^5); "etiam essere" (F^m occurs once); place names left as written
  (Luna loco, Gallera, Biagrasa, Aultrec).
- c. 674v: the amount "novecento mila scudi" (the bases are legible, the vowels of "novecento" lie under an ink smear).
- c. 674 bis r: "anchora" (twice), "obligo", "habbia", "quando", "potra temtare".
- c. 674 bis v: "sa[l]vocondocto"; in the clear note "et come sogno", "Cap[itane]o Comp[at]rj".
- .15. and .22. are not identified; Venetiani and lanzichenechi fit the sentences.

Not done: an English translation, and `docs/_check_reading.py` was not run on these files.
