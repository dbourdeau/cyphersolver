# The 1782 New York headquarters cipher

One message mixes three kinds of unit:

| unit | how it is written | how it is read |
|---|---|---|
| spelled word | pairs marked with x or underlined, often with the first number written once and dittoed (`x21-1 -6 -7`) | line-letter on the Army List title page: line 1-29, then the letter's place in that line counted from the left (`&` counts; no Q on the page, Q has its own marks) |
| word code | a plain pair (`5-19`) | one word from a table that is not identified: the second number is the word's first letter (a1 b2 c3 d4 e5 f6 g7 h8 i/j9 k10 l11 m12 n13 o14 p15 q16 r17 s18 t19 u20 v21 w22 x23 y24), the first its row in that letter's column (1-58, not alphabetical); 165 of the 174 codes fit (`followup_2026-11-14/structure_test/STRUCTURE.md`, found 14 Nov 2026) |
| clear | words, dates and suffixes written in the clear (`thither`, `6th`, `+eers`) | as written |

## Files

- `key/armylist_titlepage_1778.txt`: the title page as lined in the 1778 edition (Internet Archive `listofgeneralfie00grea`). Lines 1-27 are attested by Haldimand's worked examples (B.147 pp. 402-405); lines 28-29 were inferred from his "1 to 29" and are now used in the 25 Sep 1782 letter (principal, Irwin, plan, new). The file is byte-identical to the copy frozen for the test (`carleton_1782-09-25/preclear/evidence/`).
- `key/word_codes.tsv`: every word code seen in the three letters (174), each reading with its count per letter, a `conflict` mark where the readings differ beyond case, and `status`: frozen before the 25 Sep test (the 100 Clinton codes, 21 of them qualified; 43-19 and 22-19 carry their post-test notes), from the 6 Sep alignment only, or post-clear association from the 25 Sep letter (not tested).
- `carleton_1782-09-25/preclear/evidence/clinton_word_constraints.tsv`: the frozen table exactly as used for the prediction.

## What the code table is not

Books screened against the layout: `key/books_tried.tsv` (every candidate fails; the table is a code sheet in letter columns, not a book).


It is a lookup of observed pairs, not the book. Some codes carry inflected or variant words (who/whose/whom, returned/returning, an/any, Indian/Indians), so the headwords are not proved. Two pairs are more likely copying slips than second meanings (2-5 for French where 2-6 is usual; 23-6 for a where 9-1 is usual). 43-19 is thousand in both letters; the frozen table has hundred because we misread Clinton's clear copy (corrected after the test, `posttest/CORRECTIONS.md`). 22-19 is thence in Clinton's letter and at one place on 25 Sep, but the 25 Sep clear copy has there at the other. The coordinates any candidate word list must fit are listed in `clinton_1782-02-22/DIFFERENCES.md`.
