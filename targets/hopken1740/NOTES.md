# Höpken and Carlson, Constantinople, to the King of Sweden, January 1740: the Swedish-glossed despatches (second code)

Status: in progress. Opened 10 Nov 2026 as a split from `hopken1739` (catalogue 1771); no key yet, no write-up.

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/21 (R0003582), images 322-327. A despatch of January 1740 on the
Swedish-Ottoman alliance treaty (the Porte's dragoman, exchange of the treaty exemplars and ratifications, the French
ambassador's part, a present for the Reis Efendi; content from the pass-1 glosses, not yet checked). The chancery
decipherer struck the groups through and wrote the Swedish plaintext above.

## Why a separate target

This is a different code from the French-glossed enclosures of `hopken1739` (images 255-261): groups run to about 1999
(1774, 1800, 1825, 1868, 1869 are plain on image 326) against at most 1749 there, and values clash (1532 = Suède there, a
syllable inside Swedish words here; "Credit" is enciphered differently). One key, one entry.

## Transcription and pairing

- Pass 1 (10 Nov 2026, two AI agents, Swedish gloss in view): pairs_322_324.tsv, pairs_325_327.tsv. Digits fairly
  dependable, gloss rough and loosely aligned; superseded by pass 2 and kept for the record.
- Pass 2: word-level pairs re-read from full-size crops by three AI agents (wordpairs_322_323.tsv, _324_325, _326_327):
  each gloss word with the groups under it and a segmentation, one piece per group. K = digits and reading confident,
  X = doubtful, C = clear text. No blind digit-only pass was made.
- Pass 3: a fourth agent rechecked the 94 X lines on high-zoom crops with the full key; 63 became K, 31 stay X. In five
  lines the groups spell a different word from the gloss (dertil/derwid, öfwer/om, af/om, är den/är det, en orsak/
  orsaken) and the cipher word is taken; three words have no gloss and are restored from confirmed values ([derom],
  [til], [ej]). The gloss wording is in the note column.

## Key and held-out test

scripts/make_key.py takes the most frequent piece per group from the K lines (a/å/ä and o/ö folded: the code does not
distinguish them). A key built from 322-325 only was frozen before the 326-327 pairs came back
(key_frozen_322_325.tsv, FROZEN.sha256) and tested on the K lines of 326-327 (scripts/heldout_test.py): 598 groups, 522
in the key, **457 (76% of all, 88% of those known) give exactly the piece the pairing assigns** (525 of 687 when rerun after pass 3 added K lines); with the key's values
shuffled among its groups, mean 3.5, maximum 33 over 500 shuffles. Caveat: the agent pairing 326-327 had seeds.tsv and
worked in the folder where wordpairs_324_325.tsv already lay, so the test is not strictly blind.
Final key.tsv (all pages, after pass 3): 190 confirmed, 23 mixed, 87 single. A syllabary with word codes (1516 Ott:
Porten, 1171 Ambassadeur, 1450 alliance, 1526 negociation, 1360 tractat, 1256 Ryssland, 1123 Franckrike, 1902 Tessin,
1915 Reis Effendi, 1287 Stor Viziren, 1560 Sultan, 1179 Venedig). Groups above 1749 are ordinary syllables. No nulls.
Homophones for common letters and syllables (r, t, d, l, m, s, de, si, ha, ta).

## Outcome so far

2,119 groups on the six images; 2,027 (95.7%) lie in words whose digits and reading are both confident, 92 in 31
doubtful words (scripts/make_texts.py prints the count). The text reads as continuous Swedish (reading_sv.txt, English
in translation_en.txt): the dragoman brings the signed alliance treaty and asks for secrecy; the envoys argue for a
prompt exchange; the French ambassador has turned helpful after an express from Venice (Count Tessin's work at the
French court); a present of purses to Ragib Efendi; exemplars exchanged on 14/25 of the month. This is the
contemporary decipherment transcribed, with the code list rebuilt from it; not a break of bare cipher.
The month and year (January 1740) are inferred from the content and the volume order, not read from a heading.

## Remaining gaps

- The despatch starts before image 322 and runs on to 328; 321 and 328 are not transcribed - blocker: not-attempted
- 15 words with a value conflict (1221, 1661, 1795, 1502, 1023, 1663, 1465, 1633, 1406, 1809 ...) - blocker: open-codes; the word reads from the gloss, the group's value is unsettled
- 7 words with a group cut at the gutter of the scan (323 l16, 324 l01, 326 l02, 327 l04-10) - blocker: needs-physical-access; the fold hides the last digit
- 4 words with a digit under a strike or blot (322 r16, 323 r18, 325 l14, 327 l10) - blocker: illegible
- 4 glosses unread (323 l08 "v: Haren"?, 327 r05, 327 r18 twice) - blocker: open-codes
- Which bare pages of the volume use this code is not established - blocker: not-attempted

## Escalation

- [ ] siblings: 321 and 328 (the rest of this despatch) and the bare pages in this code not yet opened
- [x] clear-pages: the gloss is the decipherment
- [x] known-keys: not the hopken1739 code (values clash); stade1710 key does not fit (see hopken1739 NOTES)
- [x] print: no edition found (web searches of 10 Nov 2026, see hopken1739 NOTES)
- [x] key-rebuild: word-level pairs, key frozen and tested, 190 confirmed values
- [x] retry: 94 doubtful lines rechecked with the key, 63 settled

## Image sources

https://lbiiif.riksarkivet.se/arkis!R0003582_00NNN/full/max/0/default.jpg, NNN = 322-327, fetched one at a time; scans/
is git-ignored.
