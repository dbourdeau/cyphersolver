# Method

## 1. Choosing the item

From Daniel Bourdeau's catalogue of unsolved ciphers we took an item whose images are public,
which needs no visit to the repository, and on which nobody had published a reading.
Item 818 (Fossey's notebook) is one. Prior art: `PRIOR_CHECK.en.md`.

## 2. Images

Fetched from Yale's public IIIF endpoint without an account. All 76 images were first taken at
800px wide to find the pages with cipher; the 38 that carry cipher digits were then taken at
2000px and at full size (longest side about 2,900–3,900px). Two seconds between requests.
No images are kept in this repository.

## 3. Recovering the key

Only the digits 1–9 occur, never 0. Digits sit inside otherwise ordinary English, so they stand
for letters. The plain heading on image 18 and the second cipher line of image 19 are the same
phrase, which fixes seven values; the next two words fix the rest. See `../data/key.tsv`.

## 4. Transcription conventions (the shapes of this hand)

- **The digit 9 and the letter g are written alike.** They cannot be told apart by shape, so the
  reading that makes a word was taken. The 12 places are listed in `../data/g9.tsv`.
- **The letter d and a figure 0 look alike.** The notebook never uses 0 (quantities are spelled
  out). Checked at full resolution, e.g. p.41 "p458d" = pound, p.62 "1882s22d" = anneseed.
- **The digit 1 (= a) and the long s (ſ) are similar.** 1 is a short slanted stroke; the long s is
  tall. They were separated at full resolution, e.g. p.25 "b5ſh26" = bushel.
- **q and g are similar.** Where the word must be quart or quarton, the glyph was compared at full
  resolution with the plain-text "quarton" on the same page (p.60) and transcribed as q.
- **The substitution is not consistent**: words written out in full occur inside cipher lines
  (1,295 words with digits against 242 without). They are left as written.
- Struck-through text is transcribed and counted as cipher. Text hidden under a pasted slip is
  marked `[...]` and not counted.

## 5. How corrections were handled

After the first transcription, every cipher word whose decoding was not a word was given candidate
re-readings by swapping the shapes this hand confuses, keeping only those that produce exactly one
word. **A candidate was accepted only when the full-resolution image showed it.** The results are in
`../data/verified_auto.tsv`: of 35 candidates, 7 forms (10 places) were accepted and the rest were
rejected because the image disagreed — for example the candidate that would turn T91c62 into
"Treacle" was rejected because the image reads T91c62 (a period spelling of treacle).
Differences against the second reader were treated the same way (`../data/verified.tsv`).

## 6. How the share of meaningful symbols is measured

Of the cipher symbols (occurrences of 1–9), the share that falls in words whose decoding is a word
(`../src/ratio.py`). A word is checked against an English dictionary
(/usr/share/dict/words) plus the spellings that occur in the notebook's own plain-text pages
(`../data/plain_vocab.txt`) and a list of period drug and measure names
(`../data/materia.txt`, each with its evidence). Words broken across a line are joined.

## 7. Control

The key (1–9 → a e i o u l m n r) was shuffled 1,000 times and the same share measured
(`../src/control.py`). Against the real key's 93.7% (of words containing digits), the best shuffle
reached 55.5% and none reached the real key.

## 8. Calibration

None is possible: the notebook carries no contemporary decipherment and there is no printed
edition or translation (`PRIOR_CHECK.en.md`). Instead the notebook's own plain-text pages, which use
the same words (bole armery, varges, warter), were used as the standard for spelling.

## 9. Limits

- No human has checked this transcription.
- The spelling is of its period and many words are not in a modern dictionary; the judgement of
  "makes sense" depends on the vocabulary described above.
- Pasted slips cover part of the text on one opening; the hidden lines cannot be read (`OPEN.en.md`).
