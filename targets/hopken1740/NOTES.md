# Höpken and Carlson, Pera (Constantinople), to the King of Sweden, despatch No. 2 of 15/26 January 1740 (second code)

Status: in progress. The despatch is deciphered in full from the contemporary gloss (98.9% of groups in confident words,
measured); the write-up (site page, ledgers) is not done yet. Opened 10 Nov 2026 as a split from `hopken1739` (catalogue 1771).

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/21 (R0003582). Two copies of the same despatch, both marked
duplicate, in the same encipherment: images 321-331 (the chancery decipherer struck the groups through and wrote the
Swedish plaintext above; signed "Pera i Constantinopel d. 15/26 Jan: 1740", C. F. v. Höpken, E. Carlson) and images
332-342 (332-333 glossed, 334-342 bare; note on 332 "ankom med en express d. 5 Maji 1740"). It reports the conclusion
and exchange of the Swedish-Ottoman defensive alliance treaty.

## Why a separate target

This is a different code from the French-glossed enclosures of `hopken1739` (images 255-261): groups run to about 1999
(1774, 1800, 1825, 1868, 1869 are plain on image 326) against at most 1749 there, and values clash (1532 = Suède there, a
syllable inside Swedish words here; "Credit" is enciphered differently). One key, one entry.

## Transcription and pairing

- Pass 1 (two AI agents, gloss in view) on 322-327: pairs_322_324.tsv, pairs_325_327.tsv; rough, superseded, kept for the record.
- Pass 2: word-level pairs from full-size crops, five AI agents (wordpairs_*.tsv, images 321-331): each gloss word with
  the groups under it and a segmentation, one piece per group. K = digits and reading confident, X = doubtful, C = clear text.
- Pass 3: the X lines of 322-327 rechecked on high-zoom crops with the key (94 lines, 63 settled).
- **Second copy as a blind control.** The bare copy on 332 and 334-342 was transcribed digits-only by three agents told
  to open no other file (bare_332_336.txt, bare_337_339.txt, bare_340_342.txt; 3,082 groups). 2,987 (97%) are identical
  in sequence to the glossed copy. At each one-for-one difference where the bare group was not doubtful, the bare digit
  was taken (scripts/apply_bare.py; 25 + 91 groups, each noted in the pairs' note column): the differences are almost
  all 5/6, 2/8 and gutter-cut digits under the strike-through of the glossed copy, and the bare digit is the one that
  agrees with the key. Image 333 (a second glossed copy of the text of 322) is not transcribed; it was consulted for
  three lines of 322.
- Pass 4: the 63 lines still X rechecked against both copies; 51 settled, 1 reclassed as clear text, 11 remain.
- Judgement calls, all noted in the pairs: in five lines the groups spell a different word from the gloss (dertil/derwid,
  öfwer/om, af/om, är den/är det, en orsak/orsaken) and at 327 r06 the gloss "hwarpå" stands over groups that spell
  "wärde"; three words have no gloss and are restored from confirmed values ([derom], [til], [ej]); [tre] (327 r05, gloss
  blotted) and [söka] (328 r16, no gloss) are restored from key values; "22 Decembre" (324 r04) rests on a doubled
  group 1865 and the gloss "d. 2".

## Key and tests

scripts/make_key.py takes the most frequent piece per group from the K lines (a/å/ä and o/ö folded: the code does not
distinguish them; i/j and u/v are one letter each). Final key.tsv: 235 confirmed, 15 mixed, 78 single. A syllabary with
word codes (1516 Ott: Porten, 1413 Kongl. Majt, 1171 Ambassadeur, 1450 alliance, 1526 negociation, 1360 tractat, 1256
Ryssland, 1123 Franckrike, 1265 Swerige, 1902 Tessin, 1915 Reis Effendi, 1287 Stor Viziren, 1560 Sultan, 1179 Venedig,
1669 subsidier). Groups above 1749 are ordinary syllables. No nulls. Homophones for common letters and syllables.

Held-out test (scripts/heldout_test.py): a key built from 322-325 only was frozen before the 326-327 pairs came back
(key_frozen_322_325.tsv, FROZEN.sha256). On the K lines of 326-327 as first paired: 598 groups, 522 in the key, **457
(76% of all, 88% of those known) give exactly the piece the pairing assigns**; shuffled-key control mean 3.5, maximum
33 of 500. Caveat: the agent pairing 326-327 had seeds.tsv and worked where wordpairs_324_325.tsv already lay, so the
test is not strictly blind. The same frozen key on 330-331 gives 517 of 591 (87%), but that agent had key.tsv in view;
it is a consistency figure, not a held-out one.

## Outcome

3,450 groups on images 321-331; 3,411 (98.9%) lie in words whose digits and reading are both confident, 39 in 11
doubtful words (scripts/make_texts.py prints the count). reading_sv.txt is the Swedish text in order, translation_en.txt
the English, decryption.txt the key applied group by group, transcription.txt the groups. This is the contemporary
decipherment transcribed and checked against a rebuilt code list and a second copy; it is not a break of bare cipher.

## Remaining gaps

- 7 words with a value conflict (322 r15 i, 324 l01 Ryska gränsen, 325 l14 bewijs, 326 l01 slutande, 328 r08 försäkra, 328 l09 aldrahögstes, 328 l18 allernådigst) - blocker: open-codes; both copies agree on the digits, the word reads from the gloss, probably slips of the encipherer or a homophone not separated
- 3 words where the split between groups is unknown (327 r06 "1500", 330 l08 willkor, 331 l14 pröfwas) - blocker: open-codes; 1640, 1689, 1771 not fixed
- 1 gloss unread (323 l08, a name over 1313, looks like "v: Haren") - blocker: open-codes; single occurrence, clear in both copies
- A few clear (unenciphered) words are doubtful in the hand (330 l02-03, r02, r03; 321 inserted word) - blocker: illegible

## Escalation

- [x] siblings: leaves before and after opened; the despatch runs 321-331 and a second copy 332-342, used as a control
- [x] clear-pages: the gloss is the decipherment
- [x] known-keys: not the hopken1739 code (values clash); stade1710 key does not fit (see hopken1739 NOTES)
- [x] print: no edition found (web searches of 10 Nov 2026, see hopken1739 NOTES)
- [x] key-rebuild: word-level pairs, key frozen and tested, 235 confirmed values
- [x] retry: doubtful lines rechecked twice, against both copies; 11 remain

Not part of this target: which other (bare) despatches of the volume use this code. Groups above 1749 are the mark;
the key here is the place to start.

## Image sources

https://lbiiif.riksarkivet.se/arkis!R0003582_00NNN/full/max/0/default.jpg, NNN = 319-342, fetched one at a time; scans/
is git-ignored.
