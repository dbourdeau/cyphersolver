# PREREG: Entick test on message No. 4 (f.345)

Written 12 Nov 2026 (00:00 EST), before the test is run. One run only.

## What is already known (exploratory, not part of the test)
I checked a handful of pairs from message No. 1 by hand against the 1781 London (Dilly) printing of
John Entick's *New Spelling Dictionary* (Internet Archive `11280377bsb`, BSB copy, OCR + one page image):
32-1 = Being (L col.), 225-4 = Member, 240-12 = New, 364-32 = The (L col.), 364-1 = Them (R col.).
These fit Sherwood's sketch of No. 1 ("A member of the House of New Hampshire"). That is how the
hypothesis was found, so these pairs are not evidence in the test below. Message No. 4 has NOT been
looked up in the dictionary.

## Hypothesis H1
The messages are a page-entry code on Entick's New Spelling Dictionary, in an edition with the same
pagination as IA `11280377bsb`. Each pair is PAGE-ROW; ROW counts printed entries (1 to about 40)
down a column, and either column may be meant.

## Test (confirmatory, on No. 4 only)
1. Predicted words: the dictionary lemmas of the content words in Sherwood's sketch of No. 4, fixed now:
   Wednesday, Last, Sleigh, Men, March (verb), From, Albany*, Towards, Oswego*, Vermont*, Post, Alarm,
   Expect, Force, Destine, Reduction, New, State, Council, Windsor*, Hearing, Saturday, Other, Report,
   Say, Only, Movement, There, Certainly, February.
   (* proper names: Entick has a gazetteer/name list at the back; include them only if the OCR finds
   them as headwords; otherwise drop.)
2. For each lemma, find its printed page in IA `11280377bsb` with `scripts/headword_find.py` (first
   headword hit inside the dictionary body; lemmas not found by OCR are dropped and listed).
3. Cipher pages of No. 4: every first number of a pair in f345.01-f345.10 (numbers 500, 1783 and the
   final day number 16 excluded), parsed by `scripts/parse_pairs.py`.
4. Score = number of lemmas whose Entick page equals some cipher page of No. 4 (page match only;
   rows are not used because the OCR row estimate is rough).
5. Controls: repeat step 4 with every lemma page shifted by k = -20, -10, -5, +5, +10, +20.

## Decision rule (fixed now)
- H1 supported on No. 4 if score >= 8 AND the largest control score <= 3.
- H1 rejected for No. 4 if score <= 3.
- Anything between: inconclusive; reported as such.

## Not allowed after seeing results
No change to the lemma list, the edition, the shifts, or the thresholds. Any later reading of the
messages (choosing L/R column, correcting "blundered" page numbers) is reported separately as
inference [I], not as part of this test.
