# Test plan: is Harford Jones's 1798-1802 code book a printed book?

Written 15 Nov 2026 by an AI agent, before any comparison with a candidate book. Hashed (sha256) before the first run.
Source of the code values: dbourdeau/cyphersolver `targets/jones1802/` at main 1c81b493 (folder last commit
ebb365ff, 11 Nov 2026), copied to `their_folder/`. Only `table_1798.tsv` (values from the clear copy /51) is used
for the word test; `proposals.tsv` (values guessed from context and page position) is not used, because those
values were chosen partly by alphabet position and would bias the test.

## What the code values already say (read before any candidate was opened)

The 1798 table is not strictly alphabetical: "by" 28,75; "that" 29,3; "of" 29,6; "with" 35,6; "very" 201,68;
"unexpected" 211,52; "you" 220,29; "ministers" 220,50; "morning" 225,23; "use" 227,26; "weight" 232,12; "went"
232,57; "whether" 233,27; "which" 233,52 (x2); "will" 235,51 (beside "me" 235,5 and "measure" 235,32); "wisdom",
"wisest", "with" 236 (x3); "she" 238,67; "separate" 272,62; "should" 321,13; "find" 323,13; "astonished" 373,52;
"peace" 383,20. Some may be alignment slips; the repeated ones (which, with, very, you) are not. A printed dictionary
cannot put "will" on the same page as "me" and "measure". So before testing, the expectation is: an alphabetical
vocabulary (pages, up to about 78 words a page, names after Z) with extra words entered out of order, i.e. a
hand-made or hand-amended code book, possibly built on a printed word list. The tests below check whether the
alphabetical skeleton matches a printed book.

## Jones profile used in test (a) (fixed here)

First page of each letter, from the letter groups in their NOTES. Where their own word values contradict the first
letter code, the stated second code is used, and this is said in the results:
A 1, B 28, C 49 (second code; first code 29,10 is followed by B words on 31-35), D 93, E 123, F 141, G 161,
H 174 (second code 174,7; the other, 147,7, lies inside F), I 187, K 213, L 215, M 228, N 249 (second code 249,48;
first code 229,28 is followed by M words on 230-235), O 256, P 266, R 305, S 327, T 376, U/V 398, Y 439, Z 440.
Total pages: 445 nominal; names on 442-443. 21 letters (J, Q, W, X absent from the profile).

A second, unforced variant (a') with their first codes as printed (C 29, H 147, N 229) is also run and reported,
so the choice above cannot rescue a candidate.

## Test (a): letter-start profile

For each candidate, take the first page on which headwords of each letter begin (from an OCR index; the first
page where at least 3 headwords of that initial occur after the preceding letter's start). Fit one linear map
jones_page = a * cand_page + b by least squares over the 21 letters. Residual = Jones page minus fitted page.
- Pass: at least 18 of 21 letters within 3 pages, and none beyond 8.
- Clear rejection: fewer than 12 of 21 within 3 pages, or any letter beyond 15 pages.
- Between the two: "inconclusive", reported as such.
Also report the raw (unfitted) residual and the candidate's total page count.

## Test (b): word test, only for a candidate that passes (a)

Fixed sample rule: from `table_1798.tsv`, in file order, the first 25 rows with a two-number group (page,word),
whose word value is at least 5 letters long and alphabetic (no "15th"), taking each word once. Misses stay in.
For each: map Jones's page through the fit from (a) to the candidate page, round; look up whether the headword
(or its root form, e.g. "embarrassed" -> "embarrass") is on that page.
- Exact edition (pages match without rescale, a = 1, b = 0 within 1 page): word on the same page for at least 20
  of 25, and where the book has countable entries (two columns), the entry number within 3 of Jones's word number
  for at least 15 of 25.
- Same book, other edition (rescaled): word within 2 pages of the predicted page for at least 20 of 25.
- Below 15 of 25 on either count: rejected.

## Rules

One run per candidate. No re-fitting after seeing word results. Misses are reported as misses. OCR failures of the
candidate index are reported as such, not counted as hits.
