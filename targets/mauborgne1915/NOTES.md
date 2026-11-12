# mauborgne1915: J. O. Mauborgne's 1915 challenge cipher, Manila, 21 October 1915

Status: read in part (key text and plaintext found by Jacob Houtrouw, 11 Nov 2026; checked here 12 Nov 2026). 89 of 97 words
come out of the key with no correction = 91.8% by the README read bar; 8 words each carry one letter read from the sense.
Key recovered from the ciphertext alone, by the contributor's record. The order of events rests on his word: one issue,
his own timestamps and screenshots, no outside timestamp seen here.

Contributed by Jacob Houtrouw (issue #487, who may be named; he writes as Jake Tschakka), with an AI model working at
his direction. Not in the catalogue (the catalogue's Mauborgne entry 664 is a different cipher, the 1917 one sent to MI-8).
Not on DECODE.

## The document

Cipher dated Manila, 21 October 1915; covering letter 23 October 1915; from 1st Lt J. O. Mauborgne, 8th Infantry, to the
Director, Army Signal School, Fort Leavenworth; posted at the school on 13 December 1915. 499 letters in 100 groups (99
of five, one of four, a printed dash after the last). Mauborgne meant two sealed envelopes, the plaintext to be opened
after three months and the method a month later; neither is known (Altifina's research page). Louis Kruh found the sheet
among Army Signal School papers in the New York Public Library around 1991; when Craig Bauer asked, the library could not
find it. Printed in The Cryptogram (Mar-Apr 1991, p. 7), Cryptologia 17(2) (1993) pp. 172-174, Bauer, *Unsolved!* (2017)
pp. 351-352. **No image of the original is known; none is included here.** The ciphertext in `cipher.txt` is the text of
Futility Closet (14 Mar 2022), which is Kruh's printing, and which Altifina's page reproduces (the two agree on every
letter of the 499, checked here: the Altifina string is the one in `cipher.txt`). SHA-256 of the 499 letters:
b9aa04181dafdc37417abff3dfe18aa8d5511e800b8bdfd22a77b89dd52d6122 (measured here, same as the contributor's).

## The claimed system (`key.txt`, `plaintext.txt`, `decode.py`)

A running key with odd shifts. With A = 0, cipher c = p - (2 * (k mod 13) + 1) mod 26: each plaintext letter is moved
back by an odd number of places chosen by the key letter (A or N: 1, B or O: 3 ... M or Z: 25). Deciphering, p = c + shift.
Because every shift is odd, a cipher letter has the opposite alphabet parity to its plaintext letter.

- Key text: Engineer Field Manual (Professional Papers of the Corps of Engineers No. 29), Part V (Field Fortification),
  paragraphs 1 and 2, p. 357, with "Field fortification" at the head of paragraph 2 replaced by "It" (a contributor choice:
  so altered, the two paragraphs are exactly 499 letters, and that is why the message stops mid-sentence).
- Plaintext: the English text of Article 29 of the Regulations annexed to Hague Convention IV (1907), 499 letters, from "A
  person can only be considered a spy" to "... either for their own army or for". It differs from the treaty text in the
  U.S. treaty series (Bevans) in three ways, per the contributor: "a hostile party" for "the hostile party"; "who having
  penetrated" for "who have penetrated"; pretenses, endeavors, entrusted, dispatches for pretences, endeavours, intrusted,
  despatches. The Yale Avalon Project copy of the 1907 text (checked here) reads "he obtains or endeavours", "the hostile
  party", "who have penetrated", "entrusted", "despatches": it shares "entrusted" and the British spellings with the
  plaintext supplied, but not "a hostile party" or "having".
- `plaintext.txt` keeps the treaty's British spellings (pretences, despatches) as the contributor supplied them; the cipher
  letters give pretenses and dispatches.

## What was checked here (12 Nov 2026)

`decode.py` (run `python3 -I targets/mauborgne1915/decode.py`; standard library only; written here from the rule):

- lengths 499 / 499 / 499, ciphertext hash as above;
- the rule reproduces **489 of 499** letters against `plaintext.txt`; **491** with the American spellings at positions 69
  (S for C) and 457 (I for E);
- the ten misses are at 69, 88, 122, 194, 238, 255, 397, 443, 457, 462 (1-based), as the contributor lists; at four
  (122, 238, 443, 462) no key letter at all can give the printed cipher letter (a parity break);
- **495 of 499 positions have an odd shift** (plain minus cipher); the four exceptions are exactly those four;
- the plaintext shifted one place: 11 of 498 letters; the key shifted one place: 37 of 498;
- **control, 2,000 shuffles of the ciphertext** (seed 20261112): at most 37 exact matches (real 489) and at most 287 odd-shift
  positions (real 495); the first public check by the project (from the Altifina text and Article 29, before the strings
  were sent) gave at most 291;
- adjacent cipher letters of opposite parity: 333 of 498 (chance about 249), the contributor's starting signal.

Key text against the printed manual. The contributor's screenshot (not seen here, the image link was not opened) is of
the fourth (1912) edition in a copy with the 1916 addenda, Google Books GLUmAQAAIAAJ p. 357. Here the **Third (Revised)
Edition, 1909** (archive.org `ad-1117984`, scan of the Defense Technical Information Center copy; printed page 357,
beginning of Part V) was read from its text layer: paragraphs 1 and 2 with "Field fortification" replaced by "It" give
exactly the 499 letters of `key.txt`, no difference. A 1917 printing (archive.org `engineerfieldma02deptgoog`) carries the
same two paragraphs. So the 1909-edition question the contributor left open is settled for the wording; the page number of
the 1912 edition rests on his screenshot.

## Outcome and how it is counted

By the README read bar, counted on the 97 words of the plaintext: 89 come out of the key uncorrected (91.8%), 8 carry one
letter read from the sense (endeavors, operations, Thus, penetrated, of, civilians, the, dispatches: positions 88, 122,
194, 238, 255, 397, 443, 462). The two spelling differences (69, 457) are not holes: the cipher letters give pretenses and
dispatches. 91.8% is under 95%: **read in part**. The contributor's own figure is by letters, 489 of 499 (98.0%), 491 with
the American spellings; counted by letters with those spellings it is 491 of 499 (98.4%). Method (Lasry's categories):
**key recovered from ciphertext-only**, by the contributor's record: the search that found the key text and the plaintext
used the ciphertext's odd-shift signal and a set of candidate texts; no crib, no known plaintext and no existing key of this
item were used, and no one had linked either text to this cipher before. Key: recovered (a book text for every position).

## The contributor's account, by his record only

Found on 11 Nov 2026 by an AI model working at his direction, from a test plan sealed before any decryption code touched
the ciphertext (SHA-256 9e934fd3bb18456766686c67cf99b18d3f3a036311bfec3fec6929179c4c2e92, sealed 15:28:38 UTC by the
session's own clock); the model's own forecast before the run was 2%. Exploratory statistics showed adjacent cipher letters
alternating in parity (333 of 498); a search over 338 candidate tables ranked the real text first of 41, about 20 standard
deviations above the decoys, with planted controls recovered. Sent to Craig Bauer that afternoon and published at
jaketschakka.substack.com ("the adventures of claude and muaddib") at 5:01 PM US Mountain time on 11 Nov 2026 (Substack
dates it 12 Nov); his screenshot of the live post at 5:01 PM MT is his record of the time. The files are hashed and the
hash list is said to be anchored by OpenTimestamps in Bitcoin block 975480 (not checked here). The four language-model data
files (about 60 MB) are on request and were not seen; the search was not re-run here.

## What is not explained

- **The ten slips.** At eight positions the key and the printed cipher letter disagree and a letter is read from the sense;
  at four of them no key letter can give the printed letter, so those are slips in the cipher letters, Mauborgne's or a
  copyist's or printer's; the other four may be slips in the key text of the edition he used. Not explained, not tried to be
  explained here.
- **Edit of the key text.** "Field fortification" replaced by "It" is the contributor's choice and what makes 499 letters.
  The second envelope (the method) is lost, so Mauborgne's own rule is not known.
- **Printed letters of Kruh and Bauer** were not compared by eye by anyone in this record: the contributor's comparison with
  Bauer was made by two AI sessions; Kruh's printing was not seen. The books were not scanned. The Chaocipher Clearing
  House (chaocipher.com, page 027) reports that Bauer, in chapter 8, lists inaccuracies in Kruh's articles and thinks Kruh may
  have introduced errors into the transcription of this cipher, and that the message was said to be in a new system invented
  by Mauborgne: a possible source of the slips, not tested.
- **The printing of Article 29 used.** "a hostile party" and "who having penetrated" are not the wording of the Avalon copy
  nor of Bevans; which English printing Mauborgne had (the Army's own, 1914-15) was not looked at.

## Remaining gaps
- eight words with one wrong letter (positions 88, 122, 194, 238, 255, 397, 443, 462) - blocker: needs-physical-access; the sheet is lost, the slips cannot be placed in the sheet, a printing or the key edition
- printed letters of Kruh (1993) and Bauer (2017) against the transcription - blocker: needs-physical-access; in copyright, not scanned, comparison so far by AI sessions only
- which printing of the Regulations Mauborgne used - blocker: no-key-material; no source for his copy

## Escalation
- [n/a] siblings: a single item; the catalogue's Mauborgne 1917 cipher (664) is a different cipher
- [n/a] clear-pages: no clear pages; the plaintext envelope is lost
- [x] known-keys: the book key is the key; the 1909 edition checked, the 1912 edition by the contributor's screenshot
- [x] print: Kruh, Bauer and the Chaocipher Clearing House report no solution; Altifina unsolved; the books not read
- [n/a] key-rebuild: the key is a book text that reads, nothing to rebuild
- [n/a] retry: no unread groups remain except the eight slip letters, which no key letter can fix

## Files

`cipher.txt` (transcription), `key.txt` (key text), `plaintext.txt` (contributor's plaintext with British spellings),
`decode.py` (own decoder and controls), `decryption.txt` (raw, uncorrected), `reading.md` (reading with the holes marked),
`profile.json`. No translation: the plaintext is English.
