# Blind re-reading K1 of the held-out portion (image 031), 11 Nov 2026

One blind sheet of sign shapes, answered by Brice Dudout on 11 Nov 2026 (export 17:08 UTC), integrated once by a Claude Opus 5.5
agent at 18:14 CET. It bears only on image 031 (both pages), read at full resolution after the single measurement of the key.
No image, crop or thumbnail of the sheet is reproduced here.

## Rules, written and hashed before the sheet was built

`PREREG-PLANCHE-K1.md`, SHA-256 **ecdd74a70fa8eb58a0e4b7b83a39202a6e1092202956a34efdd0750cd148a505** (re-checked at integration).
- One question = one doubtful sign of image 031 (or its immediate neighbour), boxed on its line; the options are 2 to 4 reference
  shapes cut from certain words of the same leaf, plus "none / illegible" and a free remark. No value, gloss or letter is shown.
  Order of questions and options drawn at random, seed 2525111.
- Two control questions on certain signs (the second b of "Stabben"; the e of "Hjørne"). If either control fails, nothing is
  integrated and a different sheet is made later.
- Integration, applied once and mechanically:
  1. shape chosen = class of our reading: the word keeps our reading; if it was probable and this sign was its only doubt, it
     becomes certain;
  2. shape chosen differs: the word becomes unresolved, unless the letter of the chosen shape gives a Danish word attested in the
     Gutenberg word list (frequency >= 2) or a declared 19th-century spelling (t/f, o/ø, i/j, e/æ, aa/å): then it is probable
     with the new reading;
  3. "none / illegible" or no answer: a probable word becomes unresolved, a certain word stays certain;
  4. the share read is recomputed and recorded as it comes out, even under 95%;
  5. no second sheet on the same signs to recover a result.

## Sheet and answers

- Sheet `planche_kloge_K1.html`, SHA-256 76fdabe2dc34caee2471cd00bdfde2ef49e3c7398d94278db97feec05330e3ba (28 questions = 26 points
  + 2 controls; shapes only, images embedded, no external resource; tested under jsdom before it was sent). Builder `build.py`
  dab19930f6b28e025b2279f4da0b66793ae033ec03151774b438d47fb012b3c8. The private map question -> sign -> reading
  (1a1aaae9342d397bf5b6cd97a455a0bfec9e1d1d5f1efcec1d77a7ba676656f2) was never loaded by the page.
- Answers `reponses-brice-2026-11-11.json`, SHA-256 **bdefcb9359da707fa87f4071cab58dbd64066cb058e7ebffd78d6c0b88518a28**
  (equal to the value in its .sha256 file, checked before integration).
- **Controls 2/2**: q26 (b of "Stabben") answered b; q22 (e of "Hjørne") answered e. The sheet is integrated.

## Two results

- **A, the hashed rule as written** (clauses 1-3; the answer is the shape ticked; remarks ignored): held-out portion
  133/37/1/8 of 179 words = **94.97%** (95.5% with the restored word).
- **B, retained at Brice Dudout's request, a declared deviation from the rule**: where Brice wrote a remark ("shape 1 with a dot
  above", "shape 2 without the dot", "the two dots on the side are missing, the shape should be wider"), the remark is turned
  into a sign of the key table, then into a letter, before clauses 1-3 are applied. Held-out portion 133/36/1/9 of 179 words =
  **94.41%**. B is the figure we declare; A is given beside it.
Both are under 95%: the held-out portion is **read in part**. Clause 5 applied: no second sheet on these signs.

| q | place (031) | word (our reading) | shape answered / remark | effect A / B |
|---|---|---|---|---|
| q01 | right l. 23 | [karlegravet] a | shape 1 (a) / "with a dot above" | already unresolved; B would give "kerlegravet", not a word: unresolved |
| q02 | right l. 20 | Kirkegaard: k | shape 2 (dotted stroke, s) / "without the dot" | k not chosen; "Sirkegaard" not a word: certain -> **unresolved** (A and B) |
| q03-q05, q07 | right l. 17, 24-25 | ligger, Solens, foretages | as read | confirmed |
| q06, q10 | right l. 22 | øver ste: ø, e | as read | confirmed; stays probable (wrong word space) |
| q08, q11, q12 | left l. 5 | Kabbe: b, b, e | as read | confirmed (see q15) |
| q09 | right l. 22 | nord: o | as read | only doubt removed: probable -> **certain** |
| q13 | right l. 20 | Aand: a | as read | stays probable (one chevron for "Aa") |
| q14, q16 | right l. 24 | [søn]: s, ø | as read | signs confirmed, word still unresolved by sense |
| q15 | left l. 5 | Kabbe: a | shape 1 (a) / "with 2 dots" | A: stays probable. B: the key has no chevron with two dots; either the dots of the k before it fell in this box (a stays a) or the chevron is dotted (e: "Sebbe", "Kebbe", not words): probable -> **unresolved** in B |
| q17, q19-q21, q23, q25 | right l. 16-17, 25 | Solens, høire, Saugspaaner, som | as read | confirmed |
| q18 | right l. 23 | [karlegravet] a | as read | still unresolved |
| q22, q26 | right | Hjørne e, Stabben b | as read | **controls passed** |
| q24 | right l. 20 | en: e | as read | only doubt removed: probable -> **certain** |
| q27 | left l. 7-8 | Jomfru: o | as read | confirmed (see q28) |
| q28 | left l. 7-8 | Jomfru: capital J (stroke-and-dot + hook) | shape 2 (stroke + 2 dots, h) / "the 2 dots on the side are missing, the shape should be wider" | J not chosen; "Hjomfru" / "Somfru" not words: probable -> **unresolved** (A and B) |

"Jomfru" (031 left l. 7-8) was counted probable before the sheet: the full-resolution re-reading of 031 left gives only a page
total, with no class per word, so this is our assumption; the share read does not depend on it (the word ends unresolved either
way).

## Counts of the held-out portion (restored and unresolved words are holes)

| state | 030 | 031 left | 031 right | held-out portion | read |
|---|---|---|---|---|---|
| after the measurement, before the sheet (re-reading after the measurement, not blind) | 47/15/1/3 | 38/13/0/1 | 47/12/0/2 | 132/40/1/6 of 179 | 96.1% |
| A, rule as written | 47/15/1/3 | 38/12/0/2 | 48/10/0/3 | 133/37/1/8 of 179 | 94.97% |
| **B, retained (declared deviation)** | 47/15/1/3 | 38/11/0/3 | 48/10/0/3 | **133/36/1/9 of 179** | **94.41%** |
| first reading by sense, right after the measurement | | | | 95/62/2/24 of 183 | 85.8% |

The sheet took the held-out portion down by 1.7 points (96.1% -> 94.41%).

## Defect of the sheet: frames too tight

Three of the five losses (q02, q15, q28) come from the segmentation, not from the reading: the floating dots of a sign (the two
dots of k, or of the capital J) fell into the frame of the neighbouring sign, or outside the frame. Brice's remarks describe exactly
what each frame contained. This hand shifts the two dots of k to the right, onto the next sign (q01, q15 confirm it). A later sheet,
on other signs, must widen its frames to take in the floating dots.

## Next sheet (not yet answered)

A second blind sheet, K2, on the full-resolution reading of the rest of the book (36 points drawn from the doubts of the working
fiches + 2 controls), was pre-registered before it was built: `PREREG-PLANCHE-K2.md`, SHA-256
c0bc50a7a4758f0806282c7a2a71160eb6271de3e79ac24b82148d51ddf43488, seed 2525222. It has not been answered; nothing of it is
integrated here, and the whole-book figure (95.2%) is therefore not blind.
