# Aaron Burr to Theodosia Burr Alston, Baltimore, 31 January, 10 and 18 February [1808]: Vigenère letters filed with GLC01523

Status: read. Key recovered from the ciphertext alone (period-6 Vigenère, numbers 1-26), 5 Nov 2026. 969 of 973
cipher numbers read (99.6%); one rubbed group of four numbers open.

## The documents

Two sheets of number cipher filed with Gilder Lehrman **GLC01523** (Burr to Joseph Alston, July 1804), which the
catalogue counts as that letter's "second and third pages ... in cypher" (catalogue 2049). They are not: the July
1804 letter has its own short cipher on its clear page (`../burr1804/`, a different system), and these sheets are a
separate set of letters of early 1808.

- **img1** = `GLC01523_Page_1.png` (1160x1400), pencil "1523A" at the foot and "See p. 1[?]" at the left. A full
  page in three sections divided by ruled ("black") lines:
  - A, above the first line: written at Baltimore on 10 February. "Below the black line is copy of my last ...".
  - B, between the lines: the copy of the letter of 31 January ("on this blessed thirty first day of January").
  - C, below the second line: "No person must suspect that I mean to visit you in S.C. ...", most likely the end of
    the 31 January copy (key restarts there, as at every section).
- **img2** = `GLC01523_Page_2.png` (1400x1138), three lines at the head of a sheet, docketed in another hand
  "Balt[imore]" and "1808": the letter of 18 February.
- Images: Hamilton Education Program page https://hamilton.gilderlehrman.org/supporting-document/burrs-coded-letter-about-duel-1804
  (`/sites/default/files/2023-10/GLC01523_Page_{1,2}.png`). Images not committed.

Year: the docket says 1808, and the text fits Burr's winter after the Richmond trials: hiding ("Yet at Baltimore
incog."; "let it be believed ... that I am in Philadelphia"), waiting for "money for the long voyage" (he sailed for
England on 7 June 1808), and Theodosia ill at The Oaks. The recipient is Theodosia, not Alston: "the hope of seeing me
keeps you at the Oaks at the hazard of your life", "except by mari" (French *mari*, husband) and the closing
"huzzey" (hussy, a pet name). "Gamp" is Burr himself, as in the journal he kept for her in Europe.

## The cipher

Vigenère over the alphabet numbered a=1 ... z=26, period 6, the key running through the letters (word divisions kept,
spaces do not advance the key), restarting at each section and on img2:

    cipher = plain + shift (mod 26, written 1-26); shifts 6, 18, 22, 7, 24, 8 (a=0: G S W H Y I)

No keyword behind the six shifts was found (all 26 alphabet offsets and the reversed form tried; `decrypt.py`).

## How the key was found

1. Transcribed section A (80 words, 341 numbers). Letter frequencies flat (top number 8.5%), all 26 values used:
   polyalphabetic. Repeats: one 6-number word three times running (26,19,10,19,1,16 = "submit").
2. Index of coincidence by period: 0.0435 overall, 0.0618 at period 6, 0.0583 at 12.
3. Column-by-column chi-square against English letter frequencies at period 6 gave the shifts at once; section A
   read "below the black line is copy of my last by the schooner wolf ...".
4. Transcribed the rest; the same key reads every section from the first key place.
5. `resync.py`: Viterbi over words with the shared English model (`lang` en-modern) to find where the key phase
   slips. Two places: B.06 "be[s]t" (Burr left out the s but moved the key on) and img2 after the rubbed group.
6. Control (`control.py`): Burr's own 18 July 1804 text (Davis), 341 letters, enciphered with 20 random 6-place
   keys; the same solver recovered the key 20/20.

## The reading

Full line-by-line reading: `reading_numbers.txt` (from `python decrypt.py --measure`). In plain prose:

**[Baltimore, 10 February 1808]** (img1, section A)
> Below the black line is copy of my last, by the schooner Wolf, Capt. Jones, to sail about the eighteenth. You will
> hear again. Keep up your spirits. My plans are not changed. Yet at Baltimore incog., the tenth February. Business
> now detains me. We must submit, submit, submit to ten days more of suspense. The promise in [?] my last was rashly
> made. Affairs begin to look up. J'y travaille. What would Gamp not give to know that you are all well.

**[Copy of the letter of 31 January 1808]** (img1, sections B and C)
> My last letter was written eight days ago. Poor Gamp is still at Baltimore on this blessed thirty-first day of
> January, still hoping and still persisting in all the plans so often written to you. It distresses me to think that
> the hope of seeing me keeps you at the Oaks at the hazard of your life. Indeed my be[s]t endeavors are used and
> shall be used to get to you. If after ten days further delay it be found impracticable, a person shall be sent
> express to you, and for you just four hours work, huzzey.
>
> No person must suspect that I mean to visit you in S.C. Let it be believed, except by mari, that I am in
> Philadelphia.

**[Baltimore, 18 February 1808]** (img2)
> Baltimore, eighteenth Feb. Nothing new. The same hopes and intentions continue. Have [?] patience. {2?,11?,1,23}
> hourly expectation of money for the long voyage, and nothing else detains [?] me.

## Readings with a comment

| place | cipher | reading | note | grade |
|---|---|---|---|---|
| A.06 | 15,16 | in | gives "ix"; the key needs 15,6 (16 for 6: Burr's slip or a misreading) | C |
| A.07 | 18,5 | j'y | French, "j'y travaille" | H |
| B.06 | 10,11,16 | be[s]t | Burr left out the s and moved the key on | H |
| B.07-08 | 15,5,12,2?,25,... | impracticable | 4th number torn after its 2; the key needs 25 | H |
| B.08 | 4,23,2? | for | last number torn after its 2; the key needs 24 | H |
| B.09 | 15,19,8,6,23,21 | huzzey | as written; "hussy", a pet name | C |
| C.02 | 18,23,16,1 | mari | as written; French *mari* (husband, i.e. Joseph Alston), so read | C |
| img2.02 | 16,7,11,1 | have | gives "hase"; the key needs 14 for 11 | C |
| img2.02 | 2?,11?,1,23 | — | unread: middle number rubbed on a fold; the key falls back one place after it | — |
| img2.03 | 26,12,13,9,15,6,15 | detains | gives "deoains"; the key needs 18 for 13 | C |

Measured with `decrypt.py --measure`: 973 cipher numbers, 969 giving sense (99.6%).

## Prior work

- Gilder Lehrman calls the cipher undecoded (catalogue, AMDigital record, Hamilton Education Program page, which
  treats these sheets as part of the 1804 letter).
- Davis, *Memoirs of Aaron Burr* (1837): no letters between October 1807 and June 1808 (Gutenberg #7851 grepped for
  "Wolf", "incog", "hourly expectation", "poor Gamp").
- Kline and Ryan, *Political Correspondence and Public Papers of Aaron Burr* (1983): the table of contents (archive.org
  search-inside, p. 27) goes from 1807 to "1808 Editorial Note: The Road to Exile" (p. 1040), then letters from 19 June
  1808. No January-February 1808 letter printed as a document. The editorial note itself (vol. 2, pp. 1040-1045) was not
  read: it may mention or quote these letters.
- cryptiana: Burr only for the 1806 Entick dictionary code. Not on DECODE.

## Remaining gaps

- img2.02 group {2?,11?,1,23} (four numbers) - blocker: illegible; the middle number is rubbed on a fold in the only image (Hamilton Education Program PNG); the Google Arts & Culture zoom or the original may show it

## Escalation

- [x] siblings: the July 1804 letter on the same file uses a different cipher (`../burr1804/`); no other 1808 Burr cipher letter found
- [n/a] clear-pages: no clear text on these sheets apart from the docket
- [n/a] known-keys: key recovered here; no published Burr-Theodosia Vigenère key found
- [x] print: Davis 1837 grepped; Kline 1983 table of contents read; cryptiana; DECODE harvest
- [x] key-rebuild: complete; phase slips located by Viterbi (`resync.py`)
- [x] retry: the rubbed group tried at all six key phases and with 3 and 4 numbers: no word fits with "hourly" following ("in" would need 17,20)
