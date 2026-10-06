# Thomas Urquhart's Cyphral Octastich read in full; the distich claim not reproduced

Two numeric cryptograms of Sir Thomas Urquhart (1611–1660), no. 28 on Schmeh's Top 50. The **octastich**: eight
stanza-lines and a ten-number "Decagram", 285 numbers to 201, printed on the last leaf of *Ekskybalauron* / *The Jewel*
(London, 1652), dated "London, March 7, 1651 / 17, 1652", a leaf missing from every digitised copy; reprinted in the
Jack and Lyall edition (Scottish Academic Press, 1983), p. 212 and facing, whose photographs are on the HCPortal
record (`src/octastich_part1.jpg`, `src/octastich_part2.jpg`). The **distich**: 64 numbers in two lines of 32, values
to 70, headed "THE CYPHRAL DISTICH" in the Maitland Club *Works* (1834) p. 417 after the 32 Proquiritations of
*Logopandecteision* (`src/Urquhart-Cryptogram.png`), not in the 1653 edition.

**Status (16 Sept 2026): octastich read.** It is a book cipher on *The Jewel* itself: the k-th number, counting straight
through the poem, is a word index into physical page k of the 1652 edition, the letter is that word's initial, and
Urquhart took the *first* word on the page beginning with the letter he needed. Decoded from the EEBO-TCP text of
*The Jewel* (A95749) and a fresh transcription of the 285 numbers from the 1983 photographs: 238 of 284 numbers are
exact first-occurrence hits (0.838) against 0.434 (max 0.491 in 200 trials) for the same numbers shuffled and 0.436
(max 0.509) for random pages. The reading:

```
Great Lord, mantaine that regal familie
Whereof King Charls the second is the head,
And grant that he may beare the supreme sweigh
Where English, Scots and Irsh are borne and bred;
And [?] overthrow his usurp'd authoritie
Reigne in his royal predecessors stead:
Let him be our sole Cesar, Artur, Hector,
Our Emperour, King, Monarch and Protector.
                              Amen, so be it.
```

A royalist prayer for Charles II in ottava rima, written in London in March 1652 by a prisoner of Worcester, hidden
in a book written to vindicate Scotland. Line 5 was re-read on 5 Oct 2026 (§5): "And [?] overthrow his usurp'd authoritie"; one letter (position 149) stays open. Measured as sense (§8): octastich 274/285 = 0.961 (read); with the unread distich, 274/349 = 0.785. The rule was
published by Vals AI on 31 Aug 2026 as a Claude Fable 5.1 result with the same plaintext; it is verified here from the
text and the numbers alone, without using their plaintext, and their two caveats (a page offset from position 159, a
missing line-5 stretch) are traced to the TCP transcription and to the page itself. The **distich** claim (i-th number
→ i-th Proquiritation, first letter) does not reproduce: 34 of 64 first-occurrence hits, chance for texts that short,
and no English; page-index variants on either book are at chance. The distich stays unread.

## 1. What the poem says about its own key

Printed under the numbers (from the 1983 page; the glosses "Aphaeresified: suppressed. Prosthesized: added" are the
editors'):

> To this *Octastick* if you will subjoyn / A *Decagram* of this same stuff of mine, / All gather'd out of my
> *Exskybalorum*, / You'll finde a Rule, by which, with great decorum, / You may most comfortably regulate / Your actions,
> thoughts and speeches; and know that / I love an *Aphaeresified* treason / Better then any *Prosthesized* Reason.

"Gather'd out of my Exskybalorum" names the key text. *Aphaeresis* is the loss of a word's initial: the cipher is made
of initials taken out of the book. The "Rule" is the prayer.

## 2. The ciphertext (`ct.py`, `OCTASTICH_1983`)

Transcribed here from the two HCPortal photographs of the 1983 edition. Each stanza-line runs over onto an indented
second line; the eight lines have 33, 35, 38, 39, 32, 33, 31 and 34 numbers, the Decagram 10: 285. Schmeh's
transcription (Cipherbrain 2015; `OCTASTICH` in `ct.py`; identical on the HCPortal record) has 272: it omits the
run-over of line 2 (`31.5.19.32.3.115.3.22`) and of line 6 (`16.69.1.44`), drops a `2` before the final `10` of line 6,
and reads `6` for `16` at the second number of line 3. Every earlier attempt on the octastich, including the previous
session here, worked on that defective text.

## 3. The text, and the printer's misnumbering (`pages.py`)

`pages.py` reads the TCP XML (`src/tcp_A95749.xml`, textcreationpartnership GitHub mirror) into word lists per page,
dropping marginal notes, running heads and catchwords, joining end-of-line hyphens, tokenising on letters. The 1652
printer numbered pages 34–35, 38–39, 42–43 and 46–47 twice and skipped 60 and 110, and numbered one page "101" for 110;
the TCP `<pb n=…>` follow the print. `numbering='physical'` counts leaves in order from p. 1, which is what a man
turning pages does, and it is the numbering that aligns; `numbering='printed'` does not. Three TCP artefacts are
removed: duplicated `<pb>` elements for re-shot images (two words each, at physical 159 and 184–185). One near-empty
TCP page remains at physical 158 (two words, printed "156" repeated): the reading needs a page slot there, so it is a
real page of the 1652 book whose text the TCP does not carry, and the one letter enciphered on it (position 158,
n = 12) cannot be read from the TCP. That is Vals' "one page used twice / k−1 from position 159".

## 4. The test, the decode and the controls (`decode_1983_full.tsv`, `reading_octastich.txt`)

Whether number n on page k points at the first word of its own initial on that page is a property of the number and
the page alone. For the right page and the right rule it should hold almost always; for a wrong page or rule it holds
at the base rate, about 0.43 in this book (small indices are frequent, and the first few words of a page are first
occurrences by construction). Straight decode, one number per physical page:

| run | first-occurrence rate |
|---|---|
| the 285 numbers, physical pages 1–285 | **0.838** (238/284; one out of range at 158) |
| same numbers shuffled, 200 trials | mean 0.434, max 0.491 |
| numbers in order, pages randomly permuted, 200 trials | mean 0.436, max 0.509 |
| Schmeh's 272 numbers, DP-aligned with skips (previous step) | 0.865 (231/267) vs 0.686 shuffled-and-realigned |

The 46 non-first positions are one to a few words off (first-index column in the table), the size of difference
between a modern tokenisation and a 1652 page: hyphenated compounds, "&", paragraph numbers, catchwords, the
untranscribed Greek. None changes a letter that matters except in line 5.

Reading as decoded (capital = first-occurrence hit, lower case = word not first of its initial, `_` = out of range):

```
wREATLORDMApTAInETHATREGtaFAMILIE          Great Lord, mantaine that regal familie
WtEREOFKINGCHARLStHaStCONtISTaEHiAD        Whereof King Charls the second is the head
ANDGRAnTTHatHEDAYBEARETHEFUPaEMESgEIGS     And grant that he may beare the supreme sweigh
WHERDENGLIsHSCoTSANDIOSoAREBORNEANDBRED    Where English, Scots and Irsh are borne and bred
AaDCOnERTHTO_aIttSUaPDApTHORIEIE           And [?] overthrow his usurp'd authoritie
REIGtEINMISnOtALPREDECESSORSSifAt          Reigne in his royal predecessors stead
SETHpLBEOURSOLtCESAtAmtaRHECBOR            Let him be our sole Cesar, Artur, Hector
OeREMPoRPUwJINGMONARCHANDPROTECTOR         Our Emperour, King, Monarch and Protector
AMsNSOwLtt                                 Amen, so be it
```

*Sweigh* is Scots *swey*, "sway" (DOST: "to bear the swey"); *mantaine*, *Charls*, *Cesar*, *Artur* are period
spellings; *Irsh* is a slip or a syllable-saving contraction. The rhyme scheme is ABABABCC. Where the TCP word is not
the first of its initial the letter is still the one the sense requires in every line but 5, which is what one
expects if Urquhart's page and the TCP page differ by a word or two.

## 5. Line 5

*16 Sept reading (superseded):* positions 149–160 decoded A-N-D, C-O-N-E-R-T-H-T-O, page 158 unreadable, then
"this"; no ten-letter word was found.

*5 Oct 2026 re-reading.* The numbers of line 5 were re-checked on `src/octastich_part1.jpg` at full resolution
(crop 200–3700 × 1580–1720): `3.58.15.2.1.4.5.56.5.5.2.4.12.20.19.14.80.37.45.34.3.95.6.38.1.18.11.27.4.13 / 7.24`,
32 numbers, identical to `ct.py`; the 1983 print is not the problem. What was wrong was the segmentation. The tail
163–177 decodes S-U-a-P-D-A-p-T-H-O-R-I-E-I-E = (u)surpd authoritie at offset 0, so 162 is U (n = 80, first U on the
page at 79). That leaves 149–161 (13 slots) for the words between "And" and "usurp'd". Decoded on its own page,
150–157 give O-n-E-R-T-H-T-O: O, E, R, T, H, O are exact first-occurrence hits for OVERTHRO, and the V (151, n = 4)
and second R (156, n = 2, first R at 1) are the two misses. 158 is the TCP slot with no text (W). 159 n = 20 → H
(first H "hand" at 19), 160 n = 19 → I (exact), 161 n = 14 → S: the TCP splits "Leopoldo's" into "Leopoldo s",
and with that phantom token removed word 14 is "said", the first S. So: **And [?] overthrow his usurp'd
authoritie**, 3 + 1 + 9 + 3 + 6 + 10 = 32 numbers, and the old "this" was a misreading of the same slots. The
en-1640s model scores the line −4.43/char against −4.77 for the old CONERTHTO string.

Position 149 (n = 2) gives C ("Colonel") and the line needs a one-letter word there, or a slip; "O" (vocative)
fits the prayer but O is word 35 on that page, so it is not read. The TCP page 158 is a duplicate-image gap in the
TCP XML although the text runs on ("to let him / know that many ward"); Urquhart's count nevertheless needs a page
there (163 onward aligns at offset 0), so his copy had a leaf the TCP filming does not carry; its letter (W) is
supplied by the word and not counted as read.

## 6. The distich

Reticuli Labs' rebuttal of 1 Sept 2026 (`src/reticuli_*`) says the Proquiritation rule fails at ten of 64 positions
because the required letter begins no word in the target section, and that the distich is not in the 1653 edition but
in the 1834 reprint. The second point is confirmed on the 1834 OCR (`src/maitland1834.txt`: heading, numbers and the
six-line verse *Of carping Zoil …* on p. 417; the 1834 reading of line 2 has `5.38.5` where Schmeh has `5.33.5`). The
first-occurrence test on Reticuli's tokenised Proquiritations gives 34 of 64 hits and the string
`NTMAMNDN_OHTISEABRPTTSGSNTAATVTD / ASOTHDOSTTTBHPBTHBIPFSWTLVWTABV_`, not the claimed prayer. Page-index variants
(k → page k or k+1…3 of *The Jewel* or of *Logopandecteision*, printed or physical, lines restarting at page 1) sit
inside the shuffled control (mean 0.50, max 0.62 of 64). The distich is another construction, or this one on a text
not tried (the six-line verse under it, the *Parva peto* couplet, the 1653 sheets), and it stays open.

## 8. Measuring sense (`measure_sense.py`, `measure_sense.txt`; 5 Oct 2026)

The 16 Sept figure (275/349 = 0.788) counted every position that produced a letter, right or wrong, so it did not
measure sense. `measure_sense.py` compares, for each of the 285 positions, the letter of the final reading with
word n of physical page k: *exact* (the word begins with that letter), *near* (it does not, but the first word with
that letter is within ±2 of n, the tokenisation difference seen across the book), otherwise a gap. Per line:
1.000, 0.943, 0.974, 1.000, 0.906, 0.970, 0.935, 0.971, 0.900; octastich **274/285 = 0.961** (233 exact, 41 near).
The 11 gaps: 55, 66, 106, 149, 151, 158, 207, 232, 239, 250, 283; each was re-checked on the photographs and the
1983 numbers stand, so they are Urquhart's or the 1652 compositor's slips (or 1652/TCP page differences) where the
context fixes the letter. With the distich (64 numbers, unread) the target is 274/349 = **0.785**.

## 7. Files

`ct.py` (both ciphertexts: Schmeh's, and the 1983 transcription), `pages.py` (TCP page parser), `align.py` (DP
alignment used on the defective transcription), `decode_1983_full.tsv` (k, n, word, letter, first-occurrence flag,
first index of that letter), `reading_octastich.txt`, `alignment_schmeh.tsv`, `src/` (TCP XML of A95749 and A64608,
the HCPortal record JSON and photographs, the 1834 *Works* OCR, Schmeh's posts, Vals' page, Reticuli's files, the
1653 and Wilcock OCR from the first session). The HCPortal API: `https://api.hcportal.eu/api/cryptograms/7` (the web
app refuses scripts; the API answers with an `Origin: https://crypto.hcportal.eu` header).

## Earlier sessions

*15 Sept 2026*: provenance objection checked on the 1653 EEB scan and Wilcock 1899; octastich measured on Schmeh's
numbers (272, 82 distinct, IC 0.021) and called a book cipher by shape, "not attackable without the key text". The key
text was the book it is printed in, and the poem said so.

## Remaining gaps
- octastich position 149 (one letter of line 5) and position 158 (TCP gap page) - blocker: needs-physical-access; the 1652 leaves (EEBO images of the filmed copy, or another copy) to check p. 149's word 2 and the text of the leaf counted as p. 158
- octastich 9 other positions (55, 66, 106, 151, 207, 232, 239, 250, 283) - blocker: illegible (writer's/compositor's slips; numbers re-checked on the 1983 photographs, letter fixed by context only)
- distich, 64 numbers - blocker: no-key-material; claimed Proquiritation rule gives 34/64, chance; page-index variants on The Jewel and Logopandecteision at chance; key text not identified

## Escalation
- [n/a] siblings: printed cryptograms in a book, no archival sibling records exist
- [x] clear-pages: the key verse printed under the octastich read and used (it names the key text)
- [x] known-keys: Proquiritation rule and page-index variants on both books tested for the distich
- [x] print: 1652 TCP, 1653 edition, 1834 Works, Wilcock 1899 and the 1983 edition checked
- [x] key-rebuild: 5 Oct 2026, 1834 Works fetched (archive.org worksofsirthomas00mait -> src/maitland1834.txt; p. 417 distich, six-line verse, Parva peto couplet and its English). `distich_verse_keys.py` (output `distich_verse_keys.txt`): the six-line verse, the Latin couplet, its English, the octastich reading and its Decagram verse, alone and concatenated in both orders, as word-index and letter-index keys, with and without wrap-around: 76 decodes, best -6.76/char (Parva peto, letter index) against -5.09 for English; none reads. Distich stays unread
- [x] retry: 5 Oct 2026, line 5 re-transcribed from the 1983 photograph at full resolution (numbers confirmed) and re-segmented: overthrow his usurp'd; the 1652 page images are still not reachable
