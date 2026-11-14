# camerarius1630 — Ludwig Camerarius's letters from The Hague, 1630 (catalogue 2313)

Status: in progress. Not written up: read in part with workable gaps (the glossed originals of the bare letters 432, 460 and the postscript on 454 are still to be looked for in the volume, whose images are online). Integration check of 14 Nov 2026 below: image 442 is read through its glossed original (read from existing decipherment), strict 402/420 = 95.7%.

Riksarkivet, Diplomatica Hollandica, SE/RA/2109/I/5/7 (series R0003234, 535 images; Public Domain Mark 1.0 in the
IIIF manifest). Letters of Ludwig Camerarius, Swedish resident at The Hague, to Gustav II Adolf and to a
"vir amice" correspondent (Lars Grubbe / Johan Skytte), 1626-28 and 1630.

## System
Latin clear text with (1) a two-part nomenclator of 3-4 digit groups (about 100-4200, some with ½, e.g. 1959 Imperator /
1959½ Imperio, 2066½ Caesar, 2106½ Rex Galliae, 2110 Rex Sueciae) and letter-signs (Lq Rex Sueciae, aa cum, rr et,
t in, uu a?); (2) words spelled with numbers 10-99, three homophones per letter in consecutive blocks
(`key.tsv`), nulls 10, 11, 88-90, 95, 97-99. A group may be followed by spelled endings (1018.24.19 diversionem,
843.62.17 conventus). Not the 1621-22 Solms code of `camerarius1621`.

## What is new
- `key.tsv`: letter table, validated on held-out image 498 (0.904 vs 0.277).
- `codes.tsv`: 109 code groups with their contemporary glosses, gathered from 11 glossed images; validated on the
  unglossed postscript 442 by a blind forced-choice test (59/59 vs 0.695). Groups seen several times always carry
  the same gloss (2110, 2811, 1659, 1370, 1915, 618, 683 ...).
- `reading.md`: image 442 (Post script, 20/30 Sept 1630) read in part, 0.81 by Daniel's rule. Superseded by
  `reading_442_v2.md` (update of 13 Nov, below).

## Update (13 Nov 2026, second part): glossed original of 441-443, image 444
- 441-443 ("Duplicata", to the King, 20/30 Sept 1630) is the bare copy of a glossed original on 438-440: letter on
  438R continued on 439L ("Hoc etiam nunc addere volui ..."), postscript on 439R ending on 440L. 442 is therefore NOT an
  unglossed text: its content is existing. Element-by-element alignment (`alignment_439-442.txt`): 352 of 361 cipher
  elements identical, the rest hard digits (3/7, 0/9, 5/8). The held-out portion of the code-list test
  (`transcription_442.txt`) is 442R (postscript) followed by 442L (end of the main letter), not one text.
- The code-list test stays blind and valid; the glosses of 439 now confirm all 59 judged occurrences at the level of
  lemma or referent (51 same word, 8 synonym or same person).
- `codes_438-444.tsv`: 158 code-gloss pairs read on 438R, 439R, 439L, 440L and 444R (to L. Grubbe, 20/30 Sept 1630),
  two passes (second blind; 613 of 636 cipher elements agreed, differences arbitrated on the image). 116 groups or signs are
  new to `codes.tsv` (e.g. 115 exauctoratio, 217 Amstelodam-, 241 / 1139 Anglia, 539 Bethlen Gabor, 579 Episcopatus,
  842 contribuere, 943 Dania, 1763 Hamburg-, 2065 mercatores, 2106 Rex Daniae, 2203 Legatus Anglicus, 2304 S. R. Mtas,
  2658 Parlament-, 2686 pecunia, 3906 vectigalia; signs Rn Rex Angliae, θ ex, F Bethlen Gabor). These new values are
  attested by the glosses of the time; no new measurement was made.
- Conflicts with `codes.tsv`: none of substance. uu ("a") is glossed "ab", "a (se)", "est" (twice) and sometimes not
  at all: value not fixed, perhaps a linking sign. 1902 Mareschallum confirmed on 444R (1982 in codes.tsv was a misread
  0/8); 203 "hic" confirmed (438R); 2102 is "Rex" (Regem, Rege), "Regia" being the adjective case; 2472 is glossed
  "cambii" on 438R but stands unglossed in a place where that does not fit on 439R. 6, 4000, 3999, 4200 are never glossed
  (3999 once with a dash): probably nulls.
- `reading_442_v2.md`: 442 read 0.988 (415 of 420 units) with the glosses of its original; existing decipherment, not
  claimed as new.
- 426 ("Duplicata" 6/16 Sept, to the "vir amice") also has its glossed original, on 425R ("Cl. vir, amice singularis",
  6/16 Sept, heavily glossed): existing too.

## Existing (not claimed)
The glossed letters (109, 402, 405-406, 409, 411-412, 414-415, 418-419, 422-423, 427, 498) carry the decipherment
of the time. Several letters exist in two copies (402/404, 405/407, 409/411, 410/412, 414/416, 418-419/420-421,
422/423); the unglossed copies are not new texts.

## Open
- 426 and 441-443 have glossed originals (425R; 438-440). Bare letters still without a known original: 432 (Duplicata
  13/23 Sept), 460 (19/29 Oct) and the postscript on 454; their originals may also be in the volume (not checked).
- 425R glosses not transcribed yet (they would add the groups of 426).
- A contemporary key is probably at Riksarkivet: Chifferklaver I:19 A ("L. Camerario 1 bok") and I:22, not digitised.
- One AI reader; no human palaeographic check.

## Integration check (14 Nov 2026, PR #549)

- **Reproduction.** An own decoder (key.tsv for the numbers 10-99, codes.tsv + codes_438-444.tsv for the groups) on
  `transcription_442.txt` gives the same spelled words and code values as `decryption_442_v2.txt` (si illas, retinentes, nihil,
  educi, removeatur, dimissuros, nec passuri, ipsos, tale onus, proximus ...). 132 code occurrences counted by the decoder (the
  contributor: 126 counted + 11 nulls, with signs counted differently); the 20.26.72.28 group decodes "meal", which the contributor
  reads "meam" (uncertain in both copies; gloss "nram" on 439).
- **Images.** Riksarkivet IIIF full/max answered (no bot check). Image 442 right page compared with `transcription_442.txt` line by
  line: about 110 cipher elements, all agree, the 7 written like a 3 as the contributor declares (2780 looks like 2380, 786 like 386);
  15?2 looks like 1532/1552 (the original has 1572); 3821 is written over a struck group. Image 439 right, lines 1-18: the glosses
  (Princeps Henricus, negotiationem nram cum Statibus Generalibus praecipue, Hollandiae, saniora consilia, Comitis Wilhelmi, copiis,
  exauctorationem eorum, hostium manum, in praejudicium Mtis Vrae, si illas retinentes, diversionem, particularem, aut eas, nomine Mtis Vrae,
  sumptibus, menses sustentarent, certi, se polliceri, Statuum, Hollandorum conventum nihil, sperandum, Princeps Neoburgicus, Infanta,
  milites Hispanicos ex Juliaco) agree with `reading_442_v2.md`. Over 786.79.3206 the gloss line reads "milites"; whether 3206 has a
  gloss of its own was not settled.
- **Strict count (README read bar).** 442: 402/420 = **95.7%**: the 403 sure units of the contributor less "meam"; the 12 probable and 5
  unresolved units are holes. The contributor's figure, counting probable units, is 415/420 = 0.988 (0.963 with the 11 probable nulls as
  unresolved). This is a reading of a duplicate through its glossed original: **read from existing decipherment**, not new content.
- **Tests.** Both held-out tests are by the contributor's record: protocols, hashes, decoys, the judge's passages and answers are in his
  working folder, not here. The code-list test (59/59 against 0.695; 55/55 against 0.673 without the 4 items emptied by the clean-up
  flaw) was blind with respect to the code list; its held-out text turned out to have a decipherment of the time on 438-440, which the
  test did not use (by the contributor's record). The glosses of 439 agree with the list for the 59 items (51 same word, 8 synonym or
  same referent); a forced choice against random decoys shows the values fit, it does not prove each gloss.
- **Class.** The target is **read in part**: the only letters read have decipherments of the time; the bare letters 432, 460 and the
  postscript on 454 are not read, and their glossed originals have not been looked for. Gaps workable, so folder only (`Status: in
  progress`), no page. The profile class "read" and method "key recovered based on adjacent plaintext" were changed to "read in part" and
  "read from existing decipherment".
- **One key, one entry: camerarius1621.** Not the same code. The 1621-22 Solms code (German, one-part, letters below about 70) and this
  code (Latin, 3-4 digit groups, letters 10-99 in blocks of three) share six group numbers, and all six differ in value (487 Cantzler /
  belli, 722 Dennemarck / casu, 2095 Niedersächsischer Creis / exigua, 2472 Reichstag? / cambii, 2503 Resolution / negotiation-,
  3143 Werbung / Sueciam). Separate entries; same writer.
- `_check_reading.py`: decryption_442_v2.txt 25/48 sentences clean (0.521, names and period forms outside the word list).

## Remaining gaps

- Bare letters 432 (Duplicata 13/23 Sept 1630), 460 (19/29 Oct 1630) and the postscript on 454: not read - blocker: not attempted. Their
  glossed originals may be in the volume (426 has one on 425R, 441-443 on 438-440); the 535 images are online.
- Glosses of 425R (original of 426) not transcribed - blocker: not attempted.
- 442: 5 unresolved units (uu before 1914, 3206, 2472, 2917, 3821; not glossed on the original either) and 12 probable - blocker: open-codes.
- uu has no fixed value (glossed ab, a se, est) - blocker: open-codes.
- The tests' files (hashes, decoys, judge answers) are not in the repository - order of events by the contributor's record.
- One AI reader, no human palaeographic check; 3/7, 0/9, 5/8 easy to confuse.

## Escalation

- [ ] siblings: look for the glossed originals of 432, 460 and 454 among the images of the volume (as 425R for 426 and 438-440 for 441-443).
- [x] clear-pages: the glosses of 109, 402-427, 438-440, 444, 498 used (codes.tsv, codes_438-444.tsv).
- [ ] known keys: Riksarkivet Chifferklaver I:19 A ("L. Camerario 1 bok") and I:22, not digitised; camerarius1621 checked (a different code).
- [ ] print: F. H. Schubert, *Ludwig Camerarius* (1955), and Stålhane 1934 not opened.
- [x] key rebuild: letter table and code list rebuilt from the glosses and tested (contributor's record).
- [ ] retry: once originals are found, read 432, 460, 454; a bare letter with no original is the ciphertext-only test of the list.
