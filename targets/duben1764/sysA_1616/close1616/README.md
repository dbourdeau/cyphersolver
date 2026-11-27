# duben1764, system A (catalogue 1616): strict counts by the key, translations, and what closes the entry

Status of the two letters: **read through their decipherments of the time** (method: read from existing decipherment).
By the key alone they are **read in part**: key_c01 gives 48 % (6 Mar 1764) and 47 % (15 Nov 1765) of the cipher
words; with 38 values that the two letters impose on it (below), 59 % and 60 %.

Brice Dudout (with Claude), 27 Nov 2026. Text files only; no image is committed. The Riksarkivet images
(IIIF `A0073297_00101`-`00103`, `_00124`-`00126`) were looked at for the two checks named below, nothing else.

## Why this folder

Catalogue 1616 says "Key partial; strict counts and translations not yet made". The counts of 14 Nov 2026
(`../reading_1764-03-06.md`, 622 words, 0.998; `../reading_1765-11-15.md`, 610 words, 1.000; PR #641) count the
decipherments of the time over the whole letters. Two rules came after them:

- **the read share counts cipher words only** (README Conventions, 16 Nov 2026): 6 Mar 1764 has 304 of its 622
  words with no surviving cipher (the cipher stops at 103L.08), and 15 Nov 1765 has about 250 words of clear text;
- **only sure words count as read** (19 Nov 2026), and the decryption is the unedited output of the key
  (16 Nov 2026).

This folder recounts the two letters over their cipher words only, and says for each word whether the key gives it.
It does not change `../reading_*.md`, `key_c01.json`, any `tx/` file or any hashed file.

## Files

| file | what it is |
|---|---|
| `scripts/strict_align.py` | aligns the key values of the groups with the letters of the decipherment of the time (monotone dynamic programming) and classes every word |
| `scripts/local_fit.py` | for each group with no key_c01 value (or a value that never matches here), the value that the two letters impose, if any |
| `scripts/make_tables.py` | runs the count twice per letter (key_c01; key_c01 + additions) and writes the tables below |
| `key_c01_additions_1616.json` | the 38 values added, one by one, with every place, the alphabetical check and the comparison with key_c02 |
| `key_c01_plus_1616.json` | key_c01 with the 38 values in (a new file; key_c01.json is untouched) |
| `decode_<letter>_key_c01_plus_1616.txt` | the decryption: key_c01_plus_1616 applied to the transcription line by line, unedited (`../sysA_place.py`) |
| `strict_<letter>.tsv` | one row per cipher word: its class under key_c01 and with the additions, the groups and values under it |
| `marked_<letter>.txt` | the words in cipher order with their marks |
| `gaps_<letter>.tsv` | every place where the key gives other letters than the decipherment of the time |
| `counts.json` | the counts |
| `reading_1764-03-06_strict.md`, `reading_1765-11-15_strict.md` | the marked French text, an annotated English translation, and the gaps of each letter |

## Method

1. **Cipher**: the groups of `tx/c1764-03-06.txt` (101R-102L) and the C lines of `tx/g1765-11-15.txt`, in order.
   Groups below 100 are nulls; 100, 400, 508 have an empty value in key_c01 and are dropped (as in `sysA_place.py`).
2. **Witness**: the decipherment of the time. 6 Mar: the clear 102R.01-103L.08 (`tx/p1764-03-06.txt`, struck words
   out, insertions in). 15 Nov: the G lines of the gloss (`tx/g1765-11-15.txt`); the T lines are clear text and are
   not counted. The glossator's abbreviations "L: L: M: M:" and "St" are written out ("Leurs Majestés", "Saint"),
   because the cipher spells them (405 . 426 jeste . 578 s; 581 sa . 365 int).
3. **Words** are runs of letters, as `research/reading_audit/v10_relabel.py` counts them (d'avoir = 2 words).
4. **Classes** (from the groups under each word's letters):

| mark | class | meaning |
|---|---|---|
| word | sure | every letter is given by a key value equal to those letters (two stated conventions: y = i, *roi* / *Roy*; a value that spells in full a word the witness elides, *de* / *d'*) |
| word° | sure on an added value | the same, but at least one letter rests on one of the 38 added values |
| {word} | probable | at least one group gives other letters (a gap between key and witness): the word is the witness's |
| [word] | restored | at least one letter has no key value under it, or no group: the decipherment of the time supplies it |
| ‹…› | irresolved | cipher with no witness that the key does not read |

   Nothing is read "by sense" here: every word comes either from the key or from the decipherment of the time.

## Counts (cipher words only)

| letter | cipher words | sure (key_c01) | sure on added values | probable | restored | irresolved | key_c01 alone | key_c01 + 38 | by the 19 Nov rule (key or decipherment of the time) |
|---|---|---|---|---|---|---|---|---|---|
| 6 Mar 1764, 101R-102L (clear 102R.01-103L.08) | 321 | 154 | 34 | 47 | 86 | 0 | 154/321 = **0.480** | 188/321 = **0.586** | 321/321 = **1.000** |
| 15 Nov 1765, 124R-126 (gloss) | 360 | 171 | 45 | 48 | 95 | 1 | 169/360 = **0.469** | 216/360 = **0.600** | 359/360 = **0.997** |

- The columns "sure (key_c01)" to "irresolved" are the run with the additions ("sure (key_c01)": words whose letters
  all rest on key_c01 values). key_c01 alone (no addition): 6 Mar 154 sure, 67 probable, 100 restored; 15 Nov 169
  sure, 60 probable, 130 restored (the alignment moves by two words between the runs).
- 15 Nov: 359 gloss words, plus one irresolved stretch at 125R.13 (`583 578 579 583 581 449 579`, between "On ne"
  and "marque"; no gloss above it and no French from the key; counted as one word, extent unknown).
- 6 Mar: the 304 words after 103L.08 ("a cet ocasion ... Ses promesses") have no cipher in the volume
  (`../README.md`, finding 2). They are outside the count; their only witness is the clear of the time.
- Doubtful groups: 12 sure words (6 Mar) and 5 (15 Nov) rest on a group marked `?` in the transcription.
- Stability: with other alignment costs (unvalued group 0.4-0.8 + 0.1-0.25 per letter, skipped letter 0.8-1.2, wrong
  value + 0.3-1.0) the sure counts move by at most 2 words per letter.

**Class.** By the 19 Nov 2026 rule ("a word is read when the key gives it, or the plain text beside it does") both
letters are **read** over their cipher words: 1.000 and 0.997. That is a reading through the decipherments of the
time, not by the key: the key gives about half the cipher words with key_c01, three in five with the additions. The
wording used for 15/4 May 1764 in PR #759 applies: read through the period decipherment; the key decodes part of it.

## Key: 38 values imposed by the two letters (`key_c01_additions_1616.json`)

Rule: the group has no key_c01 value, or a key_c01 value that equals its witness letters nowhere in these two
letters; it occurs at least twice; one value makes it take exactly the witness letters at **every** place, each
place re-aligned between the nearest groups that key_c01 gives exactly; the value lowers the alignment cost. The
alphabetical place in the one-part code is checked and noted. 29 new values, 9 that replace a key_c01 value:

- new: 108 a, 110 ad, 115 ag, 181 com, 187 contr, 190 cour, 241 e, 244 e, 247 ec, 258 ent, 305 ge, 341 hon,
  365 int, 425 man, 427 mais, 451 na, 464 non, 465 nord, 472 nt, 489 op, 507 po, 590 svede, 592 soi, 602 ste,
  614 ten, 627 tra, 635 u, 644 ul, 647 une;
- replacing key_c01 values that never match here: 114 saff → affaire, 179 qu → cette, 183 con → com,
  215 en → dans, 372 ita → ir, 409 ac → les, 455 nuiro → nu, 541 ett → qui, 595 uran → sur.

Not added: values that occur once (they change no count; `scripts/local_fit.py` lists them); 259 *entre* (fits both
6 Mar places and the alphabetical place, but key_c01's *ond* comes from letter 96 and key_c02 keeps it); 279 *fai*
(fits both 15 Nov places, key_c02 keeps *e*); 488 *on* / *ont* (the three places disagree); 546 *que* (101R.07
"manqueroit" wants *quer*). Values that recur but are not unanimous are left as they are: 448 *on* (gives *n* at 8
of 10 places), 351 *kie* (*je* at 4 of 7), 581 *sama* (*sa* at 6 of 9), 423 *mes* (*me* at 4 of 5), 106 *aj* (*a* at
5 of 6), 396 *limp*, 352 *ontje*, 397 *lo*, 494 *so*. These are the largest sources of "probable" words.

365 *int* holds at four places (l'introduction, point, interpretation, Saint). The fifth place, 125L.13, is
transcribed `365?`; on the image the first digit is a 2 crossed by the scribe's stroke: **265** (*et*), as the gloss
reads. The transcription is left as filed; the word "et" there is counted probable.

**Afterwards**, the 38 values were compared with key_c02 (PR #759, open, built by another alignment over four
letters): 37 are the same; key_c02 has no value for 592. The comparison was made after the values were fixed and
changed none of them.

**Limit.** The 38 values come from the same two letters they are used to count. Words on them are counted apart
(word°); they are confirmed by the decipherment of the time at two places or more, not tested on unseen text. No
new measure was run and no held-out portion was used.

## Gaps between the key and the decipherments of the time

`gaps_<letter>.tsv` lists 59 places (6 Mar) and 68 (15 Nov). Most are key values cut badly by the alignment of
letter 96 (above). The places where the cipher and the decipherment of the time differ in wording:

- 124R.06: the cipher has `135 au . 517 . 584 si`, "**Aussi** bien", before the scribe's stroke; the gloss begins
  after the stroke, "Si bien". The gloss drops a word.
- 101R.11 / 102R.09 and 124R.08 / 124R.07: 215 is *dans* in both witnesses, where key_c01 had *en*.
- 102R.12: the cipher has `221 du` ("**du** bruit qui couroit"), the clear "des bruit".
- 126.12: the cipher runs `179 cette . 533 . 351 . 452 ne . 555 re . 507 po . 448 . 212 . 578 s . 586 su . 374 it .
  262 es`: after "ne" no group that the key reads gives "me" or "pas"; the gloss has "je ne me Reponde pas des
  Suites" (533 and 212 have no value; 212 is *de* if "tende" at 126.10 is read the same way; not settled).
- 125R.13: seven groups between "On ne" and "marque" that no witness covers (the irresolved stretch).
- The glossator abbreviates (L: L: M: M:, St) where the cipher spells the words out.

## Transcription doubts settled here

- 365? (125L.13) - read: 265; checked: image (A0073297_00125, left page, 13th number line), decode (265 = et, the
  gloss "contribuer, et s'en faire"); the transcription file is not changed.
- 124R.06, groups before the stroke - read: `56 75 100 135 517` stand before the stroke and the gloss starts at 584;
  checked: image (A0073297_00124, right page).

## Closing catalogue 1616

The entry asks for "strict counts and translations of the two period decipherments". They are here, over cipher
words, word by word, with the share the key gives. Both letters are read through the decipherments of the time
(1.000 and 0.997 of cipher words); the key reads them in part (0.586 and 0.600 with the additions). What stays open
is blocked from outside or belongs to other documents:

- the cipher of 6 Mar 1764 after 103L.08 is not in the volume (outside blocker);
- the writer "C. F.?" of 15 Nov 1765 is not identified (needs another source);
- the key is partial (open codes, mis-cut values); that is a gap of the target, not of these two texts;
- the other Chiffer n:o 1 letters in the entry's `needs` (15 May, 20/31 Aug 1764, 90R-93L, 104R-105L, 87-89) are
  other documents, worked in PR #759.

Under README Conventions, "Open items, and closing issues" (8 Nov 2026), these go to `## Remaining gaps` in NOTES.md
and to `profile.json`; nothing has to keep the entry open.

## Re-run (from `targets/duben1764/`)

```
python3 -I sysA_1616/close1616/scripts/make_tables.py
python3 -I sysA_1616/close1616/scripts/strict_align.py 1764-03-06 dudout/system_a/key_c01.json --json /tmp/a64.json
python3 -I sysA_1616/close1616/scripts/strict_align.py 1765-11-15 dudout/system_a/key_c01.json --json /tmp/a65.json
python3 -I sysA_1616/close1616/scripts/local_fit.py dudout/system_a/key_c01.json /tmp/a64.json /tmp/a65.json
python3 -I sysA_1616/sysA_place.py sysA_1616/close1616/key_c01_plus_1616.json tx/c1764-03-06.txt tx/p1764-03-06.txt
python3 -I sysA_1616/sysA_place.py sysA_1616/close1616/key_c01_plus_1616.json tx/g1765-11-15.txt tx/g_p.txt
```

## Limits

- The transcriptions are by AI agents, one pass each, not checked by a palaeographer; 50 (6 Mar) and 18 (15 Nov)
  groups are marked `?`.
- The class of each word depends on an automatic alignment; word edges can move by a letter. The totals are stable
  (above), single words may not be.
- The decipherments of the time are counted as witnesses as they are written, misspellings included (`cellei`,
  `envisageait`, `Stockgolm`); a misspelt word whose groups the key reads is still counted on its key letters.

## Hostile reading (what a reviewer should doubt first)

1. **Circularity.** The 38 values come from the two letters they help to count. That is why the key_c01 figures
   (0.480, 0.469) are given first and the words on added values are marked apart. 101R, the held-out page of the
   27 Oct check of key_c01, is among the places the values were read from: no held-out claim is made for
   `key_c01_plus_1616.json`, and none of the earlier measures is re-run or changed.
2. **Conventions.** 14 words are counted sure through a stated convention: 12 *d'* written *de* in the cipher, and
   *Roy*, *Royaume* (y = i). Without the conventions the shares fall by 0.025 (6 Mar) and 0.017 (15 Nov).
3. **Short words.** A one-letter group that matches (*a*, *s*) is weak evidence on its own; the counts follow the
   rule, which does not weigh words.
4. **The alignment decides word edges.** Totals were stable under four cost settings (within 2 words); single words
   at a group boundary can move between "probable" and "restored". Neither class is read, so the read share does not
   move with them.
5. **The 6 Mar tail.** The 304 words after 103L.08 rest on the clear of the time alone. They are outside this count
   but they are half the letter; the whole-letter figure of 14 Nov (0.998) stays the decipherer's text, not the
   key's.
6. **The witnesses are not perfect.** Four places where the cipher and the decipherment of the time differ are listed
   above ("Aussi bien", "du bruit", 126.12, 125R.13); the decipherers' texts were not corrected from the key.
7. **Identifications** in the translations (Breteuil at Stockholm, Ogier at Copenhagen, Korff, Moltke) are ours,
   from standard reference knowledge, not checked in a source here.
