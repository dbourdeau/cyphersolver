# camerarius1630 — Ludwig Camerarius's letters from The Hague, 1630 (catalogue 2313)

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
