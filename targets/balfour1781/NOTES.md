# Balfour ↔ Cornwallis cipher letters intercepted by the Americans, 1780-81 (Unsolved Catalogue no. 630)

Lt Col. Nisbet Balfour, commandant at Charleston, wrote to Lord Cornwallis in the field in early March 1781
in the southern British "Common cipher" (Saberton's name). The letters were taken by the Americans and are now
in the Papers of the Continental Congress, with a decipherment written between the lines at the time,
probably by James Lovell. The key (the ring order of the numbers and the setting rule) was rebuilt here from
that interlinear, and the letters were then deciphered from the ciphertext alone and checked against the
interlinear. A second letter of Balfour, to Lt Col. Alexander Stewart (12 Aug 1781), is in a different cipher,
a fixed number table; that table was also rebuilt from its interlinear.

Method: read from existing decipherment (the interlinear is complete); key recovered from adjacent plaintext as
the check. Extent: complete, 99.4-100% of deciphered letters in English, measured.

## The documents

NARA RG 360, Papers of the Continental Congress, item 51 (Intercepted Letters, 1775-81), M247 roll 65,
vol. 1 (naId 475670722, 646 images). Image `https://catalog.archives.gov/medialz/partners/dc-metro/rg-360/M247/pcc_405131_0001/<Fold3 file>.jp2`;
the Fold3 file number of each image is in `digitalObjects[].objectDescription` of
`https://catalog.archives.gov/proxy/records/search?naId=475670722`. Image n = the n-th digital object.

| Item | Images | Pages | Fold3 files | Contents |
|---|---|---|---|---|
| A. Balfour → Cornwallis, Nos. 1-3 (one dispatch on three numbered sheets) | 562-570 | 717-725 | 407629-407653 | wholly in cipher, interlinear decipherment; docket p. 728 (image 571) "Letters dated the ... March 1781 ... in Cypher ... supposed Balfour to Cornwallis" |
| B. Balfour → Cornwallis, about March 1781 | 572-575 | 729-732 | 407660-407668 | wholly in cipher, interlinear; docket "Balfour to Cornwallis, about March 1781" |
| C. Balfour, Charleston, → Lt Col. Alexander Stewart, 12 Aug 1781 | 576-579 | 733-736 | 407671-407682 | clear text with cipher runs, interlinear over most runs; signed N. Balfour |
| D. Cornwallis → Wemyss and Cornwallis → Balfour, 7 Oct 1780; Craig, Wilmington → Cornwallis, 23 July 1781 | 416-419, 552-556; translations 582-584 | 759-761 for the translations | 407130, 407600 | part cipher; numbered phrase translations in the volume. Not transcribed here (see Remaining gaps) |

Dating of A: the Chatham arrived 29 Jan, Monk's Corner raid 2 Feb, Wilmington taken 28 Jan, Craig's letter of
28 Feb, the packet of "the last of February", Arnold's express of 23 Feb, Sumter's attack on the Congarees
19 Feb ("nineteenth ult.", so the letter is of March). B: Rodney's capture of St Eustatius (3 Feb 1781), Eyons
left Arnold at Portsmouth 10 Feb, so also early March 1781.

Not part of this target, found in the same pass: "Sorel to unknown" (image 580, p. 737, number-pair table,
"in cipher with translation"); vol. 2 (naId 475671370) images 188-189, pp. 227-228, "Unknown to unknown, in
cipher"; John Laurens to the President of Congress, 9 Apr 1781 (images 586, 591, an American cipher).

## The system of A and B (the Common cipher)

Saberton (JAR 2019) describes it: a ring of numbers turned against the alphabet; the number standing for A is
the key; numbers from 30 up are fillers. Rebuilt here from the interlinear (`ring.py`):

- 25 letters (i = j), 25 numbers in this cyclic order (`decode.py` RING):
  `5 24 29 1 25 23 22 6 19 9 17 13 16 7 12 8 14 15 26 4 18 21 3 2 11`
  (1-29 without 10, 20, 27, 28). With A set to number x, letter k of the alphabet `abcdefghiklmnopqrstuvwxyz`
  is the number k places after x in the ring. Setting a=19 gives a19 b9 c17 d13 e16 f7 g12 h8 i14 k15 l26 m4
  n18 o21 p3 q2 r11 s5 t24 u29 v1 w25 x23 y22 z6.
- Numbers 30 and over are fillers, mixed into the words.
- Dashes divide the text into groups that are mostly words, often run together.
- **The setting changes inside a letter.** An indicator group is a dash group of fillers holding one real
  number, which becomes the new A: "33 19 37 45 31" opens No. 1 (a=19), "45 36 43 42 9" on p. 718 sets a=9.
  The decipherer put a brace over each. A has 13 indicators in No. 1, 15 in No. 2, 3 in No. 3; B has 4.
  The settings used: 19 23 5 9 13 25 1 22 25 11 4 12 9 | 26 8 13 14 16 6 2 22 18 16 29 5 17 18 14 | 16 11 4 |
  23 18 6 5.
- Nos. 2 and 3 open without an indicator and carry the previous sheet's last setting: the first six numbers
  of No. 2 read "bridge" under No. 1's last setting a=9, completing "their post near Heron's / bridge".
- A lone number between dashes is a numeral in clear: 82, 84, 71, 64 (regiments), 29, 2, 28, 23, 20, 26
  (dates), 18 and 40 (men and horses), 64 (a French 64-gun ship). The one exception is a lone number that
  deciphers to the word "a".
- The encipherer's slip on p. 718 L15: the indicator "47 49 31 25 40" gives a=25, but the decipherer wrote
  "should be 13" under the 25, and a=13 is the setting that reads ("two troops under Colonel Fenwick").

An indicator holding one real number and two fillers can also be a one-letter word padded with fillers;
`decode.py` decides those by scoring the next 40 letters under both readings with `lang` `en-modern`.

## The system of C (Balfour to Stewart, August 1781)

A different cipher: one fixed table, no indicators, fillers from 40 up (most fillers are 57-99). Rebuilt from
the interlinear (`key_from_interlinear.py`, NULL_FROM=40, 21 values with 5-99 votes each):
a31 b12 c22 d32 e13 f23 g33 h14 i24 l15 m25 n35 o16 p26 r17 s27 t37 u18 v28 w38 y29, and from context
k34 (keep, keep, Monk's) and e1 (three readings). Open: 2, 3, 19, 30 (one or two tokens each; 30 reads as
"w" in "will" and as "n" in "present", so it may be a misread). Many numbers in this letter are retouched in
heavy ink.

## Results

`python decode.py` deciphers the transcription with the key above and nothing else, and scores the output:

| Item | Cipher tokens | Illegible | Letters deciphered | In English windows (24 letters, en-modern ≥ -3.3) |
|---|---|---|---|---|
| A No. 1 | 1673 | 3 | 1213 | 100.0% |
| A No. 2 | 1679 | 7 | 1292 | 100.0% |
| A No. 3 | 310 | 0 | 237 | 100.0% |
| B | 1591 | 2 | 1539 | 99.4% |
| C | 1096 | 0 | 850 | 100.0% |

Control: the same measure on the same ciphertext deciphered with a corrupted ring (neighbouring ring numbers
swapped) gives 2.1%, 0.0% and 0.0% for Nos. 1-3. The only flagged span in B is "zprocedst" ("& proceeds t...").

Letter agreement with the interlinear (as transcribed) is 62-82% on pages where the interlinear is legible and
far lower on p. 724, where it is very faint; the differences checked are faint or misread interlinear letters,
not disagreements of the decipherer. One real disagreement: No. 3 has the numeral 18 for the men lost; the
decipherer's small word above it was first read "fifteen" (it is faint and partly struck through and only "-teen" is
sure: see the verification section below).

The reading is in `reading.md`; the line-by-line decipherment against the cipher and the interlinear is in
`decoded.txt`.

## Independent verification by Brice Dudout (PR #572, 14 Nov 2026)

Brice Dudout (PR #572, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) wrote a second decoder that takes only
the ring and table C from `decode.py` (as literals) and the transcription pages, and decides the indicators by the
dash-group rule alone, with no language model: A 2,742 of 2,742 letters, B 1,539 of 1,539, C 850 of 850 equal to
`decryption_A/B/C.txt`, with the same 31 + 4 settings. Nos. 2 and 3 open on the last setting of the sheet before
(a=9, a=14) without the `START` table, so the carry-over is confirmed. Re-run here: same figures. No key correction.

Read bar. Counted by the README rule on the reading files (`v10_relabel.measure`; every `[?]` and every conjecture
such as `[Hightown?]`, `[Pedee?]`, `[the next?]` is a hole): A 0.988 (668 words, 8 holes), B 0.990 (406, 4),
C 0.970 (226, 7). The profile had 1.0, 0.994 and 1.0, which were the table's letter shares above, not word shares;
`read_share` now carries the measured values. All three stay above 0.95: read.

p. 725, L09 `15 - 18 -` (NARA image 570). Dudout reads the mark over 15 as an *f*, the end of "loss of" (a=16), not
the "4" of the transcription note, and the small struck word over 18 as ending "-teen", first letters unclear
("fifteen" or "eighteen"). Looked at here on the same microfilm scan: the mark over 15 does look like an f, and the
word over 18 is too small and faint to decide. So the one disagreement between cipher and decipherer rests on a faint,
struck word; the cipher's 18 stands.

## Who deciphered it, and prior art

The interlinear is not signed. James Lovell broke the Clinton/Cornwallis cipher in 1781 and sent the key to
Washington and Greene (NSA, *The American Revolution*; Washington to Lovell, 6 Oct 1781, Founders Online).
The hand has not been compared with Lovell's.

Saberton, "Decoding British ciphers used in the South, 1780-81", Journal of the American Revolution,
June 2019, describes the Common cipher and says he found no evidence that the revolutionaries broke any of
these ciphers. These letters show that they did, in March 1781 or soon after. Saberton's The Cornwallis
Papers (2010) has not been checked for A and B (Balfour may have sent duplicates that reached Cornwallis),
nor for the Stewart letter. Not on DECODE.

## Remaining gaps

- C: four table values open (2, 3, 19, 30), five tokens in all: no key material beyond the interlinear,
  which is illegible at those places on pp. 733-734.
- A, B: 12 illegible tokens (edge cut-offs and blots), scattered; one word after "Sumpter's" in No. 2 and one
  after "acted with" in No. 3 not given by the cipher (needs the original; the interlinear has nothing there).
- D (Cornwallis → Wemyss, Cornwallis → Balfour, Craig → Cornwallis) not transcribed: their translations are on
  pp. 759-761, and they are a separate item from the Balfour letters this catalogue entry names. Not attempted.
- Print check: The Cornwallis Papers vols. 3-4 not consulted (no copy online): needs the book.

## Escalation

- Siblings: the key of A was applied to B unchanged and read it; C needed its own table, rebuilt from its
  interlinear. D's translations on pp. 759-761 are the key material for those letters.
- Clear pages: C's clear text is in the transcription (C lines).
- Known keys: Saberton's description of the Common cipher (ring, A-key, fillers from 30) matched exactly.
- Print: The Cornwallis Papers 2010 vols. 3-4 is the place to look for duplicates of A and B.
- Retry: the open values of C need a better image of pp. 733-734 (the NARA scan is from microfilm).

## 2026-10-28: Unsolved Catalogue no. 781 (Cornwallis ↔ Clinton, Friedman folder 796.6)

Catalogue 781 is the Marshall Foundation folder of Friedman's photostats of Cornwallis–Clinton cipher letters
from the Clinton Papers (Clements Library), which Sheldon's guide (2014, p. 284) calls "undeciphered". Checked today:

- No images are online. The folder is at the Marshall Foundation (Lexington, VA); the originals are in the Clinton
  Papers at the Clements Library. The letters in the folder are not identified anywhere online. Getting them needs
  a scan request to either library: an outside blocker.
- "Undeciphered" in Sheldon's guide most likely means Friedman's photostats carry no decipherment, not that the text is unknown.
  The Clinton–Cornwallis dispatches of 1780-81 are in print in clear: Stevens, *The Campaign in Virginia 1781*
  (1888, archive.org `campaigninvirgin01stevrich`), and Saberton, *The Cornwallis Papers* (2010; e.g. Clinton's
  11 July 1781 dispatch in the Common cipher, CP v. 139). Both editors printed from deciphered or duplicate copies.
- System: Saberton (JAR 2019) puts Clinton's July 1781 dispatches in the Common cipher, the ring rebuilt above
  (`decode.py` RING), so once the images are in hand they should decipher with this key directly. Washington's
  secretary also deciphered a paragraph of an intercepted Cornwallis→Clinton letter with a captured alphabet
  (Washington to Lovell, 6 Oct 1781).

Status of 781: attempted, open (blocked: images not online). Next: ask the Marshall Foundation for item 796.6
scans, or ask the Clements Library for the cipher letters in the Clinton Papers, then run `decode.py` on each and
compare with Stevens and Saberton (method would be known key applied, checked against the existing printed text).
