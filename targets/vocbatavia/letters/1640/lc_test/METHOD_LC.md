# METHOD: the letter-cipher (LC) words of the Batavia letter of 9 Sep 1640 (inv. 1134 scan 583), tested with an LC key built from the 1643 letter

Written 25 Nov 2026 (UTC in FREEZE_LC.txt) before the decode. Brief's plan was: test shift, Caesar, atbash and keyed alphabets on the 1640 words.
What changed: the 1643 letter (inv. 1141) uses the same kind of letter-cipher words, and its glossed copy (0886, 0890) gives their meaning
(Tartarien, Chinees, natien, Japan, oosten, acht, hoope, groote, tonnen, drie). So the LC key is built from 1643 ONLY (LC_KEY_v1.tsv), and
the 1640 words are the held-out test. The 1134_0617 gloss over the 1640 words is opened only after the score.

## Disclosure
- Before this freeze, while listing the 1643 equations, I had the 1640 LC words in context (blindtest/RESULT.md and T1640) and noticed
  in my head that 'ctld' would give 'Jhon'/'John' under these values; blindtest/RESULT.md had already said the 617 gloss looks like
  "a name, perhaps 'John ...'". So word 1 is NOT blind. No other 1640 word was worked out before the freeze.
- Plain shift / Caesar / atbash: the 1643 equations already exclude them (a->r is +17, e->b is -3 or +23, n->d is -10): no single shift
  or reflection fits. Recorded as tested-and-excluded by the 1643 equations, not run on 1640.

## Test
- Input: the LC words of T1640 (blindtest/frozen/T1640_transcription.txt, md5 9b68d68b..., unchanged), split on spaces and dots:
  ctld, Gmroodt, b, g, tpbk, lrdgenlm, grbk, nad, m, bpbkdbsbd, Zrpmb, qbbm, boode.
- Decode once with LC_KEY_v1 (lower-casing capitals); a letter not in the key -> '?'.
- Score per word: READ if no '?' and score.norm(word) is in the trackB wordlist W (37,386 types) OR in a list of Dutch/English given names
  and place names fixed here: {jan, ian, john, iohn, ioan, pieter, willem, jacob, thomas, london, londen, engelant, engelandt, bantam, batavia,
  amsterdam, suratte, malacca, iapan, japan}. Figure of record: words read / 13. Also letters keyed / all letters.
- Controls: 5,000 random permutations of the 12 key values over the 12 key letters, seeds 20261112 and 7 (count >= real);
  matched control: 5,000 shuffles of the letters of the 1640 LC words (word lengths kept), real key, both seeds.
- Bar: >= 65% AND 0/5,000 in both controls. Expected weakness: the key has only 12 letters, so many 1640 letters will be '?'.
