# Test written before the scored run (13 Nov 2026)

Key: key.json (sha256 in key.sha256). Applied unchanged to GLC02414.229, .339, .344.

Number of rows per division is not in the key. It is fixed by the word count of each division
(words after the indicator / 6, rounded down), and checked by whether the heading words
(sycamore or Camp Piatt word, July, day, amazon, rye) land in row 1.

Measure ("read share"): undo the route, read the grid row by row, and count the share of adjacent word
pairs that occur as a pair anywhere in the Huntington Eckert telegram ledgers (volunteer transcriptions of
mssEC 15, 19 pp. 1-7 and 25; about 115,000 words of 1862-65 military telegrams). Pairs that contain a
key code word are counted after substituting its meaning; pairs with an unvalued code word count as not attested.

Control: 200 random routes on the same grid (random column order, random up/down for each column, seed 1863),
same measure.

Pass: the real reading's read share must exceed every one of the 200 controls (empirical p < 0.005)
and must be at least 0.30. Calibration on the crib itself (.341) is reported but is not a test.

Disclosure: the three target telegrams were transcribed and looked at before this was written, and the
row counts and the handling of struck words in .229 and .339 were found by trial (see REPORT.md).
The test therefore measures how strongly the frozen route separates from chance; it is not a blind test.
