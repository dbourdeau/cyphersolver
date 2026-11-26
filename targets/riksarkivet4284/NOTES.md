# Gustav II Adolf to Axel Oxenstierna, Stockholm, 18 Nov 1627 (last part), Riksarkivet Chifferklaver låda II:114 (DECODE R4284)

Dated from the printed edition (see "The 1888 print"); the dateline page is not in R4284; the day 18 is the editors',
from the register; "bref för 1628" is where it was filed. Until 24 Nov 2026 this target was titled "Latin numerical
cipher letter of 1628".

Status: in progress (26 Oct 2026). **Key matched: DECODE R4325, the horizontal alphabet strip on I25940** (Dolly
Moulekhi, issue #98). The numbers decode into 17th-century Swedish with enciphered Latin phrases; decoded, not read
(a segmented reading exists as a proposal, 105 of 168 words sure; no translation here). The letter is printed with a
decipherment of the time in an 1888 edition, from another copy (Andrew Beling, issue #893). Earlier: attempted, open
(0 of 822 groups).

Split on 14 Oct 2026 from `riksarkivet1628` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 207
bundled 14 Riksarkivet records; they are unrelated ciphers, each now with its own entry: the Bremen letters of 1631
([`targets/riksarkivet1628/`](../riksarkivet1628/NOTES.md), read), R4282 (George Lasry's
[`targets/decode4282/`](../decode4282/NOTES.md)), R4306 (George Lasry's [`targets/sweden4306/`](../sweden4306/NOTES.md)),
Rusdorff 1628 ([`targets/rusdorff1628/`](../rusdorff1628/NOTES.md)) and E 708, 1633
([`targets/oxenstierna1633/`](../oxenstierna1633/NOTES.md)). Each is a different cipher, with its own page. The work
below was done on 21 Sept 2026 in the riksarkivet1628 session and is carried over from its NOTES; the transcription
moved here on 14 Oct 2026.

Work date: 2026-09-21. Catalogue item 207 (class A), still open for this record.

## The document

Riksarkivet, Stockholm, Chifferklaver låda II:114; DECODE R4284 (two PDF images, `IMG_R4284_I25750_P.pdf` and
`I25751`, public record; not committed). DECODE: undated (1600-1699), cleartext language Latin, Non-decrypted. An
archival note at the foot of the first page reads "Legat … till L. Camerarius bref för 1628": filed with the letters
to Ludwig Camerarius, the Palatine (and from 1626 Swedish) agent, for 1628. That is the filing, not the date of the
letter: it is the last part of Gustav II Adolf's letter to Axel Oxenstierna of 18 Nov 1627 (below), in Swedish with
Latin. Comma-separated numbers with Latin words in
clear (*Sequentes etiam*, *pro eo tempore*, *praeter omnia alia*, *et quorum*, *Sed*, *Cum*, *Quo casu*, *Sed etiam
tam pro*). Beside it lies a leaf on which someone tried a *letter* cipher on four phrases: *effusorem sanguinis*,
*pestem patriae*, *praeter naturalem*, *disturbatorem religionis*.

## Transcription

`r4284_transcription.txt` (agent, 21 Sept 2026): 756 numbers and 108 distinct values in the 21 Sept count; about 20
multi-digit readings doubtful (possibly two numbers run together); one line is written twice in the manuscript.
Measured 14 Oct 2026 with `docs/_check_profile.py --measure`: 822 tokens, 170 distinct (the measure counts every
doubtful form as a value of its own).

## Work log

1. (21 Sept 2026) Homophonic Latin annealing (`targets/riksarkivet1628/solve_num.py`, quadgrams from `qg.py`;
   8 restarts x 250k), also over bands of four numbers: Latin-sounding nonsense only.
2. (21 Sept 2026) 70 key records of Chifferklaver låda II (R4259-R4329) fetched; the Siebenbürgen "Schauis" key
   (R4310, a = 9 50 71 86) and the 1632 key whose 30 ends every word (R4296) tested: neither fits.
3. (14 Oct 2026) Split from riksarkivet1628; transcription re-measured. No new attack.

## 26 Oct 2026: key matched by Dolly Moulekhi (issue #98)

**The key.** Dolly Moulekhi (@dollymoulekhi, with AI assistance in Cursor) found that the separate horizontal alphabet
strip on DECODE **R4325** (Chifferklaver låda II:152, image I25940, left page, below the first square grid; not the
grid) decodes this letter. R4325 was among the 70 key records fetched here on 21 Sept 2026 but never tried. Her
transcription of the strip was checked here on the image (26 Oct 2026, PDF rendered at 400 dpi) and agrees in all 104
values: four numbers per letter (a 5 29 55 102, e 9 37 57 104 ...), Y and Z sharing one column (24 50 75 82), *å* 25
53 80 108, *ä* 27 54 79 107, *ö* 26 52 81 106, and 22, 51, 74, 89 unused.

**The decode** (`moulekhi2026/reviewed_literal.txt`, 41 lines; token by token in `reviewed_number_to_letter.txt`):
729 of 754 numbers take a letter; 23 large groups (952, 347, 831 ...) and two doubtful tokens are unresolved, probably
word codes from R4325's lists or joined numbers. It runs as 17th-century Swedish, with Latin enciphered as well as in
clear: *kunna giöra*, *orsak skull negociera*, *giorde ios der med een behageligt tienst och dette kunde skee på
några …*, *media quae longum foret recensere*, *nobis et patriae securum*, *hafwa allaredan så många hamnar inne i
Östersiön*, *det intet rådeligt ähr att öfwerlåta dem*, *sina barn och arfwingar som för sina wenner och förwanter*,
*communicera med eder för denna gången*. So the letter is mostly Swedish, not Latin as catalogued, and concerns
harbours in the Baltic (*Östersiön*). Her transcription review changed some readings of ours (`line_review.json`); the
original export is kept beside it.

**Validation** (`docs/_validate.py`, `validation.tsv`, model sv-modern, unresolved groups, y/z and clear spans unread):
reading -3.123 per letter, random keys -6.458 (z 8.6), a key annealed onto the shuffled ciphertext -3.342 (best
-3.217, z 2.4), annealer power -2.996. **Verdict: underdetermined.** The decode beats every shuffled fit, but not by
3 sd: 754 tokens over 104 symbol values is thin for a letter model, the text mixes Swedish and Latin, and the model is
modern Swedish. The evidence for the match is the archival key itself, applied unchanged, and the running Swedish it
gives.

## The 1888 print (Andrew Beling, issue #893, 22-23 Nov 2026)

Identified by Andrew Beling (@ajbeling) with AI agents, issue #893. The letter is printed in *Rikskansleren Axel
Oxenstiernas skrifter och brefvexling* II:1 (1888), no. 296, pp. 362-367: Gustav II Adolf to Axel Oxenstierna in
Prussia, Stockholm, 18 Nov 1627, signed by Salvius, docketed as presented at Elbing on 12 Dec 1627. The edition says
the letter is almost wholly in cipher and prints it with Lars Grubbe's decipherment of the time, compared with the
register for 1627; the day in the dateline is bracketed "[18]" and comes from the register. R4284 is the part from
p. 366 to the end ("i det närmeste kunna draga endera armeens speser" to "communicera medh eder för denne gången").

R4284 is another copy, not the one printed: it has Latin clear words where the print has Swedish (*nobis et patriae
securum* against "vår och rijckzsens säkerheet"). So the print is a parallel text, not a gloss on this document, and
a word taken from it is probable, not read.

Checked here (integration review of 23 Nov 2026, an AI agent): the Internet Archive OCR text of the 1888 volume, where
no. 296, the date, the signature, the editors' note and the passage were found as he gives them. Not checked: the
print's page images; R4284's images for this; R4325's word lists. Whether R4284 is a draft, a copy for Camerarius or an
enciphered duplicate is not known.

**Ten code values, probable** (source: print only, parallel text; none checked against the key's own word lists):

| group | value from the print's slot |
|---|---|
| 952 | armeens |
| 831 | tollerne |
| 1493 (number doubtful) | stilleståndh |
| 692 (twice) | Polacken / Pollniske: a stem for Polack- or Polen; the word order around 1273 differs from the print |
| 608, 1302 | Ligisterna(s) |
| 706 | Pryssen |
| 487 | assecurera |
| 1273 | konungar |

Open: 347, 1042, 1336, 800, 659. His table gives 579 as Sigismundus and 1400 as porterne, both probable.

**His segmented reading against the print** (Moulekhi's key; no image checked by him; the reading, the marked
decryption and his translation are not in the repository, he holds them). His strict count by the README rule, 23 Nov
2026: 168 cipher words in ten sentences (27, 14, 22, 9, 36, 18, 5, 20, 13, 4), **105 sure (62.5%)**, 63 holes (by
kind 18, 19, 5, 9, 2, 9, 1); every sentence has a hole and sentence 10 has no sure word. The table adds up (checked in
the review). Of 120 sure words with a counterpart in the print, 92 are the same, 23 equivalent and 5 wrong. He claims no
decipherment and agrees the letter is decoded, not read.

## Remaining gaps
- R4284: a segmented reading exists as a proposal (Beling, issue #893): 105 of 168 words sure (62.5%), every sentence with a hole; needs the image check and a translation - blocker: not-attempted; his reading and translation are not in the repository
- 23 large number groups and 2 doubtful tokens - blocker: not-attempted; ten have a probable value from the 1888 print (a parallel text), 347, 1042, 1336, 800 and 659 have none; try R4325's word-code lists on them, and re-read the doubtful multi-digit numbers on the image (some may be two numbers run together). To check on the image: 208 as 108 (å, "åhr"); line 40, 26 as 36 (f, "efterlåta"); line 41, 30 and 104 as 36 and 101 ("fulkombligen"). These three are Beling's guesses from the print, not corrections; "der är" and "hökstaten" have no one-digit explanation

## Escalation
- [x] siblings: all 14 records of catalogue 207 opened; 70 Chifferklaver key records R4259-R4329 fetched
- [ ] clear-pages: not done — the key-test leaf (four phrases over letter-cipher signs) not used
- [x] known-keys: **R4325's alphabet strip fits** (Moulekhi, 25 Oct 2026; checked on the image here); earlier only R4310 and R4296 had been tried
- [x] print: 1888 edition no. 296 found (Beling, #893); a parallel text of another copy, with Lars Grubbe's decipherment of the time
- [x] key-rebuild: blind homophonic annealing on Latin (21 Sept 2026), no result
- [ ] retry: the reading and the large groups are still to do with the key in hand

## Next

Re-read the doubtful multi-digit numbers on the image, the three guesses above first; try R4325's word lists on the
large groups; build the segmented reading and translation here and count it with `docs/_check_reading.py`.
