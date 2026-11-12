# Catalogue 2236: ELTE G. 4 Fol. Tom. V p. 1461 (27 Oct 1629)

Worked 12 Nov 2026 by WAINUT (AI language-model agents; no human palaeographer checked the text).

## The document, and a correction to the catalogue entry

The catalogue lists p. 1461 as a despatch of Johann Ludwig von Kuefstein from Constantinople to Ferdinand III. The page
says otherwise. The clear heading addresses "Wolgeborner Freyherr ... vielgeehrter Herr Orator" (Kuefstein, the imperial
orator), the dating line in clear is "Wien den .27. Octobris A° 629", and the clear subscription is "Dienstbeflissene /
N. Röm. Kays. Mayt. Hoffkriegs Presidendt vnd Räthe". So it is a letter **from the Imperial War Council (Hofkriegsrat)
in Vienna to Kuefstein**, written in his cipher, and it is presumably the received original or a file copy kept in his
papers. (In 1629 the emperor was Ferdinand II, not Ferdinand III.) The slug proposed here is `hofkriegsrat1629`.
The clear words are read from a halftone plate and are uncertain in detail; the direction of the letter is not.

- Shelfmark: Budapest, ELTE Egyetemi Könyvtár, Kézirattár, G. 4 Fol. Tom. V, p. 1461 (Lang 2015, C.Kuf.16).
- Image used: the plate in Donath Regina, "A diplomáciai titkosírás XVII. századi használatához", Magyar Könyvszemle
  80 (1964) no. 1, pp. 55-62, plate on p. 57. EPA article PDF
  https://epa.oszk.hu/00000/00021/00254/pdf/MKSZ_EPA00021_1964_80_01_047-073.pdf (page index 10, a 2562 x 3581 halftone
  scan; fetched once, 12 Nov 2026, User-Agent WAINUT-research). The manuscript itself was not found digitised.
- Extent: 18 cipher lines, 102 cipher words (602 signs, 32 distinct, counted without word gaps and punctuation),
  between the clear heading and the clear date.

## System

Graphic-sign substitution of letters, with word spaces and the writer's commas and points kept. Vowels a, e, i, o, u
have two signs each (a `5`/`oo`, e `3`/`pi`, i `8`/`c`, o `6` and two more in the table, u `7`/`III`); the other letters
one each. u and v are one sign. A sign shaped like a q with a crossed and curled tail (`gx`) stands where no letter is
wanted: between doubled letters (her-r, des-sen, wis-sen, zusam-men, an-noch, got-tlicher, taus-sent) and at three
word edges; it is read as a null. Donath also prints code signs for "Eure Maiestät", "Eure Kaiserliche Maiestät" and
"Sultan" from other letters; the opening group of this letter (`dg 1 5 f & q 2 6 8 gx 3` + `A°`) does not decrypt with
the letter key and is probably such a code group for the Emperor.

## Key source

Donath 1964 p. 58 prints the alphabet of Kuefstein's cipher (a-z, with the vowel homophones), rebuilt from the glossed
drafts in the volume. (The catalogue and Lang say only fragments were printed; the p. 58 table is in fact a full letter
alphabet.) `key_frozen.tsv` is that table, mapped to the shape tokens of `SIGN_CONVENTIONS.md`, plus two nulls fixed
from the plate (`gx`, and a flourish `&` before one initial w). Written before the first decryption run. After that run
one token was renamed (`#` to `dg`, because the script read `#` as a comment); no value changed. The hash in
`FROZEN.sha256` was taken after the rename.
`key.tsv` is identical: nothing was added after the freeze.

The k sign is printed by Donath as a looped p-like type; on the plate it is a small circle with a dot or a short stem.
The match rests on the table position and on the words it builds (geschickhten, Turckhen, starckh, volckh, khomen).

## Held-out test

Not used to build the key: Donath's three glossed specimens (Tom. V pp. 615 German, 1069 Italian, 755 Latin; pp. 60-62
of the article), copied sign by sign into the same tokens (`heldout_specimens.tsv`). Applying `key_frozen.tsv`:
**373 of 377 signs (98.9%)** give Donath's gloss letter (615: 69/70; 1069: 165/167; 755: 139/140). The four misses are
single signs (r for e in "wenig", s for q in "quali", t for i in "essi", u for r in "rei") and look like slips in the
drafts or in the print. Caveat: the table and the glosses come from the same author and volume, so this tests the
mapping of Donath's types to the plate shapes and the internal consistency of her key, not an independent key.

## Transcription

`SIGN_CONVENTIONS.md` written first (shapes only), and brought into line with the tokens the transcription uses after
the blind review (it had kept some drafted names that were never used and lacked `Y`, `+`, `gx`, `o`, `1`, `f` and
the bracketed insertion `[574]`; no token was renamed). Pass 1 from line halves at 2.4x (`work/lines/S1_*`), pass 2 from
fresh crops, line thirds at 3x with light smoothing (`S2_*`), plus 4x close-ups (`Z_*`). 17 sign-level disagreements
were settled on the crops and are listed at the foot of `transcription_p1461.txt`. Remaining shape doubts: L03 "2 o"
(two signs before "herrn"), the last sign of L05 "drey" (y or z), a p-shaped h in L17, the opening code group, and (raised by the blind review) the first sign of "dan" in L06, which
may be `d` (m) rather than `q` (d).

## Reading

`scripts/decrypt.py` gives `decryption_p1461.txt`; `reading_p1461.md` gives the text line by line, as running text in
the writer's spelling, and again in normalised spelling. `scripts/check_marks.py` rebuilds the decryption from
transcription + key and passes (18 lines, 0 unmarked departures). There are no changed or added letters: every word is
the mechanical decryption, except three holes and one doubtful word marked `[?man]`.

Word counts (102 cipher words): **98 read verbatim from the signs**, 0 with a marked repair, 0 from a gloss, 1 guess,
3 holes (`[1]` and `[2]`, the opening code group; `[3]`, the two-sign group in "[3]herrn", whose "herrn" is read).
Read share 98/102 = 96.1%.

The guess is L06 "von drey taussent [?man] starckh". The signs (`q oo o-`) give "dan", which makes little sense there;
"drey taussent man starckh" (three thousand men strong) is the idiom. The blind review saw at 4x zoom that the first
sign's stem rises well above the bowl as well as below it, so it may be `d` (= m) rather than `q` (= d). The halftone
does not settle it, so the transcription keeps `q` and the word is not counted as read. (The first version counted it
verbatim, 99/102.)

Dan's checker (`docs/_check_reading.py`, origin/main d9e716b15 of 12 Nov 2026), on the final files: the running text
in the writer's spelling, clean share 0.50 (5 of 10 sentences); the holes it counts there are period spellings missing
from its German word list (allergenedigister, geschickhten, Turckhen, starckh, aigentliche, gdst, volckh,
turckhischen, dorthen, khomen). The normalised running text: 0.90 (9 of 10 sentences; the one unclean sentence is the
first, with `[1] [2] [3]` and `[?man]`). Folder mode: `decryption_p1461.txt` 0.722 (13/18), `reading_p1461.md` 0.583
(42/72; the file holds the line-by-line block, both running texts and English notes). The first version of these
notes gave 0.635 for the reading file; that figure could not be reproduced (the blind review measured 0.508, 32/63, on
that version, before the notes on `[?man]` were added). `research/reading_audit/v2_score.py` on the running text in
the writer's spelling: hole rate 0.041 (98 words), so a read share of 0.96.

Proposed state: **read** (96% of words from the signs; all sentences coherent German; the holes and the one doubtful
word are in the first sentence).

Content in brief: the Emperor has learned from Kuefstein's letter how he was received at Ofen (Buda) by some 3,000
Turks, and wants exact information on what troops these were, whether they came from Ofen or from other Turkish places
and borders, and whether they have dispersed or are still together; the Council writes on his order.

## Prior art (checked 12 Nov 2026)

- Donath 1964 reproduces the page as a plate and prints the alphabet, but deciphers only other letters (pp. 615, 755,
  1069); she does not give the text of p. 1461. Lang 2015 (repertory p. 259) marks p. 1461 and the key undeciphered.
- Vetting of 4 Nov 2026 (catalogue entry): no DECODE record, Tomokiyo mentions the system only, no Lasry item.
- One web search (Kuefstein, 1629, Hofkriegsrat, Ofen, cipher, Donath): no decipherment found. Szabados J., "A 'titkos
  levelezés' szerepe a 17. századi Habsburg-oszmán diplomáciában", Acta Historica (Szeged) 148 (2024) uses ELTE G4
  Tom. IV-V for Kuefstein's courier network; its text does not cite p. 1461 or give a decipherment. Brandl-Szabados
  2024 on the preparation of the embassy was seen in the search results only, not opened.
- A printed decipherment of this page was not found; the key is printed (Donath p. 58) and was used as such.

## Integration check (12 Nov 2026)

Checked before the write-up, by a reader who did not take part; the contributor's figures stand.

- **Key and scripts.** `sha256sum key_frozen.tsv` equals `FROZEN.sha256` (6799b8a3...). `scripts/heldout.py` re-run: 373/377 =
  98.9% (615: 69/70, 1069: 165/167, 755: 139/140). `scripts/check_marks.py`: 18 lines, 0 unmarked departures.
  A separate decoder written from `key_frozen.tsv` and `transcription_p1461.txt` gives a decryption identical to
  `decryption_p1461.txt`, line by line.
- **Source.** The EPA article PDF was fetched again (HTTP 200): the plate of p. 1461 is on journal p. 57 (PDF page 11) and
  the alphabet table on p. 58. The table is a full letter alphabet in Donath's hand (a-z, two signs for each vowel); the
  opening words of the plate (g e n e d i g i s t e r, 'Wien den', the date and the subscription) agree with the transcription at
  the resolution seen (110 dpi); individual signs were not re-checked at high zoom.
- **Count.** 98 of 102 = 96.1% (3 holes and the guess [?man]); over the read bar. The three values fixed on the plate
  (gx, & as nulls, the dotted circle as k) are counted as read because the words they sit in read as German; the page says
  they rest on position and are outside the held-out test.
- **Test.** The held-out specimens are Donath's own glossed drafts, from the same author and volume as the table, so the
  test shows the mapping of printed types to plate shapes, not an independent key; the freeze order is by the
  contributor's record (single commit).
- **Catalogue.** Entry 2236 (title, correspondents, place) is corrected: the page is a letter from the Hofkriegsrat in Vienna to
  Kuefstein, not a despatch of Kuefstein from Constantinople to Ferdinand III; it leaves the catalogue (CATALOGUE.md).
  There is no DECODE record (`decode_ids` empty).
- **Not done here.** The manuscript (not digitised, as far as found), a human palaeographer, a second image of the
  doubtful signs.

## Remaining gaps

- The opening group `[1] [2]` and `[3]` before "herrn" are unread; a sheet of code words for this cipher (if the
  volume holds one) would settle them.
- The image is a 1964 halftone plate; the manuscript was not seen. A check on ELTE's original (or a better image)
  is needed for the clear heading and subscription, and for the single doubtful signs listed above.
- The held-out test is not independent of Donath's work (see above).
- The held-out test does not cover the three values fixed on the plate itself: `gx` and `&` as nulls and the dotted
  circle `o` as k (Donath prints a p-like sign for k). They rest on where they stand in the text (`o` only in ck/kh
  positions, `gx` only between doubled letters or at a word edge), not on the 98.9%.
- L06 "[?man]" (signs give "dan"): the first sign may be `d` rather than `q`; a better image would settle it.
- The blind review (12 Nov 2026, an independent AI language-model agent, not a person) agreed with the state read,
  grade B; it checked four lines sign by sign on the plate. No human palaeographer has checked the text.

## Files

`SIGN_CONVENTIONS.md`, `transcription_p1461_pass1.txt`, `transcription_p1461_pass2.txt`, `transcription_p1461.txt`,
`key_frozen.tsv`, `key.tsv`, `FROZEN.sha256`, `heldout_specimens.tsv`, `heldout_result.txt`, `decryption_p1461.txt`,
`reading_p1461.md`, `translation_p1461.md`, `scripts/` (decrypt.py, check_marks.py, heldout.py), `profile.json`.
The line crops are not in the repository; they were cut from the EPA PDF page named above.

Reproduce (from this folder; `-X utf8` keeps the `A°` sign intact on a Windows console):
`python -X utf8 -I scripts/decrypt.py transcription_p1461.txt key_frozen.tsv`;
`python -X utf8 -I scripts/check_marks.py transcription_p1461.txt key_frozen.tsv reading_p1461.md`;
`python -X utf8 -I scripts/heldout.py heldout_specimens.tsv key_frozen.tsv`.
