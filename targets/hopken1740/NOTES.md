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

## Transcription

- Pass 1 (10 Nov 2026, two AI agents, Swedish gloss in view): pairs_322_324.tsv (57 runs, 1,047 groups) and
  pairs_325_327.tsv (66 runs, 1,071 groups). Digits fairly dependable; the gloss column is rough and loosely aligned
  (the gloss often sits a row early or late), so only 23 runs are marked K. No blind digit-only pass yet.
- Right-edge groups on 326-327 and six groups on 323-324 are cut or doubtful (`?`).
- A hard-EM run on the 23 K runs (scripts/build_key.py, copied from hopken1739) gave no usable values: the gloss extents
  are too loose. Word-level pairing (wordpairs_*.tsv) is in progress.

## Seeds

seeds.tsv: 24 values read by eye from recurring glosses (1825 att, 1232 be, 1007 skrif, 1602 wa, 1251 de, 1749 n,
1765 1053 1736 dro-gue-man ...). Not yet confirmed by a key build.

## Remaining gaps

- Whole despatch: key not built - blocker: not-attempted (word-level pairing in progress)
- Which bare pages of the volume use this code is not established.

## Escalation

- [ ] siblings: find the bare pages of R0003582 in this code (groups above 1749 are the mark)
- [ ] clear-pages
- [ ] known-keys
- [ ] print
- [ ] key-rebuild: word-level pairs, then EM with seeds
- [ ] retry

## Image sources

https://lbiiif.riksarkivet.se/arkis!R0003582_00NNN/full/max/0/default.jpg, NNN = 322-327, fetched one at a time; scans/
is git-ignored.
