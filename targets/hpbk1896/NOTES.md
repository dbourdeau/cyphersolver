# hpbk1896: Hilmi Pasha telegrams, palace to Yemen, 1896-1902 (Koc University HPBK)

Status: in progress

Catalogue entries 2646 (system B), 2647 (system A), 2575 and 2577 (pooled, corrected). Not read. This file records the first
session (14 Nov 2026): what the pages are, what was tried, what stopped it.

## Material

Koc University, Hilmi Pasa Belgeleri Koleksiyonu (HPBK), CC BY-NC-ND 3.0. Telegram forms received at Yemen, with the cipher
text copied onto the form by the receiving clerk. Two systems, both in Eastern Arabic digits:

* **System A** (2647: 542, 551, 560, 563, 565, 568, 569, 579, 581, 600, 656, 660; also 772 of 1898): five-digit groups, bold
  purple ink on 600. Clear Ottoman words are mixed in among the groups in the same ink (600: bulunan, esbab, Cibla ...). Over
  about a third of the groups a black-ink word or fragment (mecmua, kasde, ...) is written by the decoding clerk.
* **System B** (2646: 495, 498, 518, 524, 527, 536, 541, 546, 562, 575, 577, 580, 583, 585, 587, 602, 623, 644, 652, 675,
  1761; also 533, 688, 576, 578, 599, 483): pale pencil numerals, mostly two digits made of 4-9 (44-49, 55-59, 64-71 per the
  earlier sweep), with a dark-ink Arabic letter over most of them (599, 578), and in places a dark word over a three-digit
  numeral. 587 is a different state: dark numerals with no clerk's letters, a few clear words between.

## What was done

* **Image route corrected.** `libdigitalcollections.ku.edu.tr/iiif/2/HPBK:<item id>/full/full/0/default.jpg` (the item id
  itself, not item id minus 2; checked by pixel comparison of 587 against the CONTENTdm copy: mean difference 4.4 against
  12.0 for id-2) gives 2000-px pages for 587, 602, 576, 578, 599, 600, 725. 483 does not load under its own id. The sweep's
  `img/` copies are 764 px wide and too small to read digits.
* **System B, 599 and 578, read as far as legibility allowed (not a transcription).** The clerk's layer is two-level: a dark
  Arabic letter or word over a pale numeral. At the top of 599, read right to left: a word over each numeral group:
  Yemen, vilayet, -nde (numerals 695?, 442?, 668), then isabe (717?), then the letters n (over 41) and m (over 28). The
  numeral 668 appears twice on 599 with the same suffix (nde) over it, and again in 578. So system B appears to mix
  **three-digit numerals standing for words or suffixes** with **two-digit numerals standing for single letters**: a
  nomenclator, not a pure substitution. This rests on a few groups, not on a table.
* **System A, 600, first two lines.** `tr/hpbk600_sample.txt`: 6 five-digit groups read approximately, with the black glosses.
  The five-digit groups use mostly the digits 4, 6, 7 (like system B's common numerals 44, 66, 67), but a six-letter word
  (mecmua) sits over a five-digit group, so system A is not system B regrouped into fives.

## Why it stopped

Transcription is the blocker, not the cryptanalysis. Pale pencil numerals on 578/599 are ambiguous in digit shape (4 and 2, 6
and 7 look alike in this hand), the dark letters sit over a neighbouring numeral as often as over their own, and lines are
slanted and overlap. A colour-layer separation (dark ink below grey 105, pale ink below 165) did not isolate the pencil; it
is too close to the paper tone. About 250 numerals per sheet make hand reading error-prone: no table was built, and no table
is claimed. The held-out test of 587 and 602 was not run (no table to test). The same-day clear sheets (725, 748, 726, 764,
1070, 732, 766, 727) were not transcribed. Percent read: system A 0%, system B 0% (the clerk's partial reading on the
page is not counted as ours).

## Remaining gaps

* System B numeral-to-letter and numeral-to-word table: not built; open-codes. Needs a careful hand transcription of 578
  against the clear 725/748 of the same day, then 599, 546, 562, 575, 577, 580, 585.
* System A group-to-word table: not built; open-codes, 12 sheets, black glosses on about a third of the groups.
* Sheets 483, 495, 498, 518, 524, 527, 533, 536, 620, 688, 1761, 1791 did not load in the sweep; retry under the item id.
* 587 and 602 (B) and the clear same-day crib sheets (725/748, 726/764, 1070, 732, 766, 727) untouched.

## Escalation

Tried: image route, hand reading of 599/578 (B) and 600 (A), layer separation (failed). Not tried: a per-line hand
transcription of 578 against 725/748; clustering numeral glyphs; the cipher book HPBK 1791 (needs a re-fetch); Ben-Bassat,
Turcica 46 (2015), and BOA HR.SFR / DH.SFR for the Yildiz-Yemen code books; asking Koc whether 1791 is a code book.
