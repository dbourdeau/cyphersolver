# What the two numbers of a word code are (post-test, 14 Nov 2026)

Worked out by our AI agent (Andrew Beling, with AI agents) from the 174 codes of `key/word_codes.tsv`;
`structure.py` reproduces every figure (`structure_output.txt`).

## The structure

A word code **a-b** is **row a of column b** of a table of words arranged by first letter:

- **b is the first letter** of the word, counted in a 24-letter alphabet: a1 b2 c3 d4 e5 f6 g7 h8 i/j9 k10 l11 m12
  n13 o14 p15 q16 r17 s18 t19 u20 v21 w22 x23 y24 (I and J together, U and V apart). **165 of the 174 codes** have
  a reading that fits; with the b values shuffled among the codes (2000 draws) the mean is 10 and the best 22.
- **a is the word's place in that letter's list**, 1 to at least 58. Inside a letter the order is **not alphabetical**
  (Spearman's rho between a and the alphabetical order of the word: +0.02, weighted over the letter columns; +0.05
  over all codes). Common short words mostly have low numbers (a 9, and 10, an 11, at 17; to 4, the 5, that 8,
  this 9; which 4, who 5, where 6, with 8), and numerals and rarer words high ones (hundred 58-8, eighth 57-5,
  provision 57-15, six 56-18) [observation, not tested].
- Values shared by a first number mean nothing: 5-19 *the*, 5-22 *who*, 5-6 *from* are row 5 of three letters.
- Same word, two codes: *by* 1-2 and 2-2, *of* 3-14 and 9-14, *intelligence* 47-9 and 49-9, *upon* 4-20 (and 29-30,
  below). Either the table repeats some words or one of each pair is a slip.

This is the layout of a code sheet with 24 columns headed A to Y and numbered rows, not of a book: no page-and-line
reading of a printed book puts the first letter of the word in the line number. Whether the sheet was printed or
written out at headquarters is not known.

## The nine codes that do not fit, and what the structure says about them

| code | reading in our table | what the structure suggests [hypothesis] |
|---|---|---|
| 23-6, 12-4 | *a fortnight* (Clinton, units 44-45) | an f-word and a d-word: "**fourteen days**", rendered "a fortnight" by the decipherer |
| 8-13 | *right* ("I think it right to send") | an n-word in column 13 (perhaps *necessary*); the clear copy paraphrases or the 8 is misread |
| 17-4 | *Officers* ("Some of the Rebel Officers say") | a d-word in column 4 (perhaps *deserters*); 17-4 also occurs inside a spelled group in Clinton's letter |
| 46-8 | *Combined* ("the Combined Forces") | an h-word in column 8; not resolved |
| 22-34 | *waiting* | 34-22 (w, row 34) with the numbers transposed |
| 4-30, 26-30 | *continentals*, *commands* | 4-3 *continental* and 26-3 *command* with a plural sign read as 0 (on fo. 125, B.148 p. 127, the sign after 26-3 is a small raised mark like an s, not a full-size 0; on p. 126 the 0 of 4-30 is only a little smaller: `duplicate_fo125/transcription_fo125.txt`, note of 15 Nov 2026) |
| 29-30 | *upon* (6 Sep; the decodes have *upon*, Carleton's clear duplicate B.148 p. 89 has *in*) | not resolved |

Codes the earlier table left with more than one reading:

- 9-8 *has* / *have*: column 8 (h); 4-8 is *have*, so 9-8 is **has**. The 25 Sep cipher says "has contributed"; the
  clear copies' *have* is the decipherer's.
- 13-14 *in* / *on* / *near*: column 14 (o): **on**. The clear copies' *in* (Clinton) and *near* (25 Sep) are the
  decipherers' words.
- 46-9 *just* / *been*: column 9 (i/j): **just**. Clinton's clear "has been received" renders the cipher's "is just
  received" (33-9 *is*, 46-9 *just*).
- 2-5 *engagement* / *French*: column 5 (e): **engagement**; *French* is 2-6, so the 2-5 for French is a slip.
- 33-9 *is* / *has*: column 9: **is**.
- 22-19 *thence* / *there*, 9-19 *this* / *the*, 11-1 *an* / *any*, 5-22 *who* / *whose* / *whom*: both readings start
  with the same letter; the structure does not decide.
- 5-14 / 8-14 *Orders* (the two cipher copies of 25 Sep differ): both in column 14; not decided.

## Held-out test

Written down before the material was read (`TEST_PLAN.md`, sha256 in `TEST_PLAN.sha256`). **Not run**: the planned
material does not exist in a usable form. B.45 has no transcripts of the later Carleton ciphers (only their decodes,
`../other_copies/OTHER_COPIES.md`), and the late-1781 cipher letters in B.147 (Clinton, p. 382, 12 Nov 1781; Robertson,
p. 406, 31 Oct 1781) are spelled throughout, without word codes. So the structure rests on the 174 known codes; it was
found on the same codes it describes, and the shuffled control measures only how unlikely the fit is by chance.

## Books

`../../key/books_tried.tsv` lists every candidate and why it fails. In short: a page-line reading of any book is
excluded by the first-letter rule, and an alphabetical dictionary (Entick, Bailey, Johnson, Dyche) also by the
non-alphabetical order inside each letter. The pre-written book test (at least 20 of 30 held-out codes on the right
word, against shifted-page controls) was not needed for any candidate, because none passed the first screen. The
word list is a code sheet whose columns are the letters; no copy has been found.
