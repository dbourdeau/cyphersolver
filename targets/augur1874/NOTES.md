# Augur's route-cipher telegrams, Department of Texas, January 1874 (Newberry, Ayer MS 3008)

Lead 1536 (Chicago archives sweep, `research/chi_consortium/`, 29 Oct 2026); a fourth telegram found on the facing
page during the attempt.

## The documents

Brig. Gen. Christopher C. Augur, commanding the Department of Texas at San Antonio, kept press-letter-books of his
outgoing letters and telegrams. Box 02 of his papers at the Newberry Library (Ayer MS 3008) holds the 1873-74
book. Four telegrams of January 1874 are copied there in cipher, in the clerk's hand, with no decipherment:

| No. | Date | To | Page / scan | Indicator | Words in grid | Grid |
|---|---|---|---|---|---|---|
| 22 | 9 Jan 1874 | Lt. Gen. Sheridan, Chicago | p. 84, scan 00045-0 | Baltic | 90 | 9 x 10 |
| 29 | 12 Jan 1874 | Sheridan | p. 85, scan 00045-1 | Dresden | 49 | 7 x 7 |
| 30 | 12 Jan 1874 | Maj. G. B. Russell, Austin | p. 85, scan 00045-1 | none | 35 | 7 x 5 |
| 45 | 17 Jan 1874 | Russell | p. 85, scan 00045-1 | none | 70 | 7 x 10 |

Scans: Newberry Digital Collections, assets 2KXJ8ZSFQYFRB (p. 84) and 2KXJ8ZSFQY9EQ (p. 85), 1246 x 2000 px, free.
Newberry Transcribe has volunteer transcriptions; the project's transcriptions (`ct_*.txt`) were checked against the
scans and correct them in places: 29 "table" (not "take"), "Nueces" (not "Neces"), telegram number 29 (not 8529);
22 "I. Davis" (not "J. Davis"), "to" (not "ta"), "late" (not "last"), "united and government" (not "with").
Word counts measured with `docs/_check_profile.py --measure` (indicator included): 91, 50, 35, 70.

Telegram 22 ends with a clear postscript, "Am I correct, please reply." The other cipher pages of the Augur papers
were looked for by scoring all 842 transcribed Augur pages with a word-bigram model: only pp. 84-85 hold cipher.

## The key letter (method)

Benjamin H. Grierson papers (Ayer MS 3039, box 3 f. 153, 3 pages, Newberry Transcribe): Lt. L. V. Caziare,
Headquarters Fifth Military District, Austin, to Gen. Gordon, Fort Concho, 18 Feb 1869, "Your plan of setting up
cypher is not correct". It works one example through: the message is written in lines of 4 to 9 words, arbitraries
from the key replace words and phrases, the last cell is filled, an indicator word ("Pleasure") names a route table,
and the columns are taken in the table's order, up or down, with a check word after each column. The key tables
themselves are not in the folder. Augur's telegrams use the same family without check words.

## How the telegrams were deciphered (29 Oct 2026)

1. Letter-level LM (`lang` en-modern) over column orders: failed even on the 1869 worked example.
2. A word-bigram model built from `lang/corpora/en-gutenberg.txt` (`work/wlm.py`), with a DP over column orders and
   directions (`work/tdp.py`), recovered the 1869 example's structure (5 columns with check words).
3. Telegram 45, 70 words: with the cipher words written in rows of 7, the columns read as English phrases
   ("It seems to me if governor Davis yields to force", "without armed collision it is all that can be Expected").
   The DP put them in the order 1 down, 7 up, 4 down, 6 up, 2 down, 5 up, 3 down; the last column ends in three
   Texas place names (fillers).
4. Telegram 30 with the same route reads at once (I am informed through General Sheridan ...), one filler.
5. Telegram 22 (found on the facing page by the bigram scan): "Baltic" is an indicator outside the grid; 9 columns,
   all read down in the order 2, 4, 6, 8, 9, 7, 5, 3, 1.
6. Telegram 29: "Dresden" is an indicator and "I. I." two words, giving 7 x 7; route 1 down, 7 up, 6 up, 2 down,
   5 up, 4 down, 3 down; three fillers. Seven words are arbitraries.

`route.py` holds the four routes and prints the reading; `reading.md` is the punctuated text.

## Result

Telegrams 22, 30 and 45 are fully deciphered. Telegram 29 is deciphered except seven code words. Of 244 grid words,
237 have a reading (7 of them fillers); 7 arbitraries are open: 97%.

The telegrams cover the Davis-Coke crisis in Austin: Augur reports the Supreme Court ruling and Davis's request for
troops and declines to act without the President (9 Jan); forwards a dispatch from Davis warning that unauthorized persons may try to take the state buildings, sent on through Augur apparently because
Davis had no cypher (12 Jan); tells Russell the President has no instructions (12 Jan); and on
17 Jan tells Russell he need not recognize either governor and may come back unless his stay is needed.

## Remaining gaps
- telegram 29, arbitraries nun, scatter, faint, table, novel, fussy, self - blocker: no-key-material; the Department of Texas list of arbitraries is not in the Augur or Grierson papers, and each word occurs once

## Escalation
- [x] siblings: all 842 transcribed Augur pages scored for cipher; only pp. 84-85 hold cipher telegrams
- [x] clear-pages: no decipherment on pp. 84-85 or the neighbouring pages 80-89
- [x] known-keys: the 1869 Fifth Military District example (Grierson papers) gives the method but different arbitraries; none of its words recur here
- [x] print: web search for the telegrams' wording (29 Oct 2026) found nothing; the Attorney General's 17 Jan reply to Davis is in the press, not Augur's traffic
- [x] key-rebuild: the routes are recovered; the open words are code words, not route errors
- [n/a] retry: each open word occurs once; nothing to regrade without the arbitraries list (Sheridan's received copies, Division of the Missouri records at NARA RG 393, are the place to look)

## Prior work

No published decipherment found (web searches 29 Oct 2026; no hit in the repository, DECODE or Cryptoole by
`known.py`). The telegrams were deciphered at Sheridan's headquarters at the time; those copies were not looked for.

## Dudout corrections, 29 Oct 2026
- For the seven open arbitraries of telegram 29: Davis's dispatch to Grant of 12 Jan 1874 (forwarded by Augur) is probably printed in The Papers of Ulysses S. Grant vol. 25 (1874), a crib for scatter / faint / table / novel / fussy. Not checked (the Mississippi State PDF refused a script).
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
