# deboli1787: Deboli and Gołuchowski, St Petersburg, cipher despatches of 1787 in the "older code" (ZbPop 3, key ZbPop 444)

Status: read in part (Brice Dudout, 6 Nov 2026; partial reading explained: 14 pieces read with the key of the time ZbPop 444, 5755 of 7036 words read by sense = 81.8%, no piece at 95%; the key failed our 0.90 test, 0.837 on a held-out pair).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry **416** (Deboli 1787, AGAD Zbiór
Popielów sygn. 3; the status of 416 already records our sorting of the systems, 5 Nov 2026). Related: targets/deboli1788
(our #169, older code of 1788), deboli1789-1791 (Daniel, code of 1789-91), leads PR #283 and issue #286.

## What this folder is, and is not

A **partial reading explained**, at Brice Dudout's request. Every piece below is "read in part": the share of words read
by sense ranges from 0.70 to 0.91, under Daniel's 95%. The unresolved syllables are left in place as ‹…›. The key is the
key **of the time** (we only transcribed it), and our test of it failed at the threshold we had set (0.90). We publish
because the reading is coherent Polish (or French) prose across thousands of words and the despatches are unprinted.

**Prior decipherment.** The cabinet's clear texts of 1786-87 are in AGAD, Archiwum Królestwa Polskiego 1/11/0/-/269
(Daniel's catalogue 415/416). The readings here were made **blind**: the 269 clears were not opened by the reading agent
(pre-registration hashed 5 Nov 2026, so that they can serve later as a test). From the header index of 269, a clear of the
same date exists for 8 of the 14 pieces (p01, p04, p07 [date doubtful], p15, p23, p30, p37, and g4 [a Polish letter of the
same date, match not checked]): for those the content is probably **existing** and our reading is a blind reading, not a
solution. For **p13, p21, p28, p33, g1, g3** no clear text was found in 269 or elsewhere: for those the reading is new (in part).

## Document

AGAD Warsaw, Zbiór Popielów (zesp. 12), sygn. 3, "Deboli. 1787 (cyfry)", 83 pieces, k. 184 (images on szukajwarchiwach;
not reproduced here: private research only). Antoni Augustyn Deboli, Polish envoy in St Petersburg, to King Stanisław
August; and four letters of Gołuchowski (inserted leaves k. 32-36) to one of the King's ministers. Sorting of all 56
despatches and 4 letters by opening group: older code 444 (signal 2345) = 22 pieces; tables 9933 = 19, 3865 = 14,
12282 = 3; the 1789-91 code (leading 4000) = 3; mostly clear = 3. Only pieces in code 444 are read here; G2 (12282) and
the 9933 / 4000 part of p37 are not.

## Key (`key/zbpop444_v3.tsv`)

AGAD Zbiór Popielów sygn. 444, "Cyfra polska", 8 Mar 1783: a one-part Polish code in shuffled letter blocks, groups
1-1969, signal group 2345, nulls from 1970. Transcribed in full from its 9 scans (1,965 entries, 98% legible), then
re-read on the image only for 21 values (v2) and one notation (v3); no value was changed from the sense of a despatch.
It is **not** the 1789-91 code of targets/deboli1789 (8 = "mi" here, "do" there). Groups with a half mark (136½ = Nas,
157½ = nic, 192½ = nigdzie) are written "136" + "1 over 2" in the despatches.

## Test of the key (`validation.txt`)

Three despatches of 1788 in the older code, ciphers hashed before their clears (ZbPop 428 / 417): 0.874, 0.874 and
**0.837 on the held-out one**, 0.864 overall, against shuffled-key controls at 0.08-0.12 (200 controls still being
computed). Our criterion, fixed in advance: >= 0.90. **Failed** at that threshold, while confirming 444 as the key of
1783-88. Most misses are alignment artefacts and misread digits of the despatches, not key errors.

## Pieces read (`transcription/`, `decryption/`, `reading/`, `translation.md`)

Counted by script on each reading file (certain + probable over words, restored excluded):

| piece | writer | date | opening | words | certain | probable | restored | unresolved | read | clear of the time (AKP 269 index) |
|---|---|---|---|---|---|---|---|---|---|---|
| p01 | Deboli | 29 Dec 1786 (received 9 Jan 1787) | Sire (Polish text) | 430 | 316 | 42 | 0 | 72 | 0.833 | scans 368-370 (not opened) |
| p04 | Deboli | 9 Jan 1787 | Polish | 337 | 216 | 18 | 4 | 99 | 0.703 | scans 387 (not opened) |
| p07 | Deboli | 18 Jan 1787 | Polish | 2229 | 1786 | 25 | 0 | 418 | 0.812 | scans 390-398 (date doubtful) (not opened) |
| p13 | Deboli | 27 Jul 1787 | Polish (JWMPana Dobrodzieia) | 198 | 133 | 14 | 0 | 51 | 0.742 | none found |
| p15 | Deboli | 31 Aug 1787 | Monsieur | 269 | 219 | 8 | 0 | 42 | 0.844 | scans 510 (not opened) |
| p21 | Deboli | 17 Aug 1787 | Polish | 224 | 168 | 3 | 0 | 53 | 0.763 | none found |
| p23 | Deboli | 14 Sep 1787 | Sire | 646 | 489 | 2 | 0 | 155 | 0.760 | scans 525-527 (not opened) |
| p28 | Deboli | 25 Sep 1787 | Sire | 259 | 217 | 3 | 0 | 39 | 0.849 | none found |
| p30 | Deboli | 3 Aug 1787 | Polish | 212 | 147 | 17 | 0 | 48 | 0.774 | scans 483 (not opened) |
| p33 | Deboli | 7 Oct 1787 | Sire | 567 | 491 | 22 | 0 | 54 | 0.905 | none found |
| p37 | Deboli | 16 Oct 1787 (the part in code 444 only) | Sire | 725 | 612 | 43 | 0 | 70 | 0.903 | scans 562-571 (not opened) |
| g1 | Gołuchowski | 13 Feb 1787 | date in French | 145 | 105 | 10 | 0 | 30 | 0.793 | none found |
| g3 | Gołuchowski | 30 Mar 1787 | Polish (JW Mći Dobrodzieju) | 184 | 118 | 10 | 0 | 56 | 0.696 | none found |
| g4 | Gołuchowski | 18 May 1787 | Monsieur | 615 | 482 | 39 | 0 | 94 | 0.847 | scans 455 (a Polish letter of that date; match not checked) (not opened) |
| **all** | | | | **7040** | **5499** | **256** | **4** | **1281** | **0.818** | |

Blind shape plates answered by Brice Dudout (shape only, no value shown) settled single digits: Z3a (p01: 1544 -> 1644,
810 -> 840, 1654 -> 1657), Z3G (g1, g4: 1707 -> 1767, 1557 -> 1657, 1736 -> 1756; 1615 kept). The answers of plate Z3c
(p33: 1910 "ła", 1658 "in" adopted, 360 kept) are not yet applied in reading/p33.md (+1 word at most).
`translation.md` gives English **summaries** of what is read, not full translations.

## Remaining gaps

- 1,281 unresolved words over the 14 pieces (isolated syllables that do not construe) - blocker: open-codes; partly misread digits of the despatches, partly values of 444 that do not fit, and four places where the key itself is torn or rubbed out (1215, 1216, 1398, 1405)
- the key fails our 0.90 test (0.837 on the held-out pair) - blocker: no-key-material; a new test on three 1786 despatches with clears in AKP 269 is pre-registered and not yet run
- digits of the despatches read once, on the scans - blocker: illegible; blind plates were used only where one digit changes the reading
- the 9933, 3865, 12282 and 4000 pieces - blocker: no-key-material; no key of the time found (AGAD 453/454 checked)

Not gaps of this reading (scope): the other pieces in code 444 (39, 45-47, 49-51; 56 is reserved as a control), which are not documents of this folder; the clear parts of each piece; Deboli's ZbPop 2 (1786, catalogue 415); the comparison
with the AKP 269 clears, kept for a later test.

## Escalation

- [x] siblings: ZbPop 2 (1786) and ZbPop 428 (1788) in the same code located; ZbPop 3 sorted piece by piece by opening group
- [x] clear-pages: AKP 269 holds the clears of 1786-87 (header index made); kept unopened for a blind test; ZbPop 417 for Dec 1787 and 1788
- [x] known-keys: ZbPop 444 (this key), 451 ("Chiffre François Nouveau", 1780; not the 9933 table), 445/452 (Kwilecki 1772), 453/454 (key collections 1765-1792): checked; targets/deboli1788 K4 and deboli1789 keys tried on the other systems
- [x] print: the IH PAN edition of Deboli's reports (Zielińska and Danilczyk) stops at 1782; Zielińska 2003 cites AKP 269 for 1786; no edition of 1786-87 found
- [x] key-rebuild: not needed for 444 (key of the time); v2 and v3 re-read on the key image only
- [x] retry: p07 and g3 decoded again with v3; plates Z3a and Z3G applied (v2 files)

## Credits

The key and the despatches are of the time (the King's cabinet). Brice Dudout: sorting of ZbPop 3, transcription of the key
444 and of 14 pieces, test of the key, partial readings and summaries. Daniel Bourdeau: catalogue entries 415/416 and the
deboli1788-1791 work this builds on.
