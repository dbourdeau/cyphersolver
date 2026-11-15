# Vetting, Daniel Bourdeau (2026-11-15)

Run by a Claude Code session (Claude Opus 5.5) for Daniel Bourdeau, following `research/VET.md`, on three leads from the
Arabic sweep of 15 Nov 2026 (`research/sweep_2026-11-15_arabic/part_A.md`, `part_B.md`). No open issue or pull request
names them (PR #682 is the sweep itself). Result: 2 unvetted, 1 partly_read.

## Leads

- **2884, CUL T-S K24.24: unvetted.** About 250 signs of an unidentified script, real running text with no gloss, seen at
  2000 px and at native resolution. It is not edited in Schäfer-Shaked MTKG I-III (tables of contents of all three read),
  it is not in Bohak's 2010 cipher group, and its alphabet is not the K24.19 cipher. But no one has ruled out a known
  script (compare Bohak's Devanagari Geniza letter, T-S AS 159.247-248), and the MTKG Geniza-fragment registers and
  Bohak's inventory were not opened. It needs a palaeographer (Bohak or Elbaum) before it can be called a cipher.
- **2885, CUL T-S 13J18.19 (1139): partly_read.** India Book IV B no. 41 (Friedman's headnote, on PGP 9097) reports
  that Gil and Fleischer 2001, pp. 282-285, read word 1 as "marsha'at" and word 2 as "tarakh", by a different method for
  each, with nothing for the verso word. Friedman calls it unresolved. Gil-Fleischer was not opened. The recto codes
  were seen at native resolution with no gloss. The verso word (about 11 signs) has no reading in print and could be
  split off as a key-test target (the J277 and Bodl. heb. f 102/28 Coptic-numeral alphabets are not yet tested).
- **2889, Penn Museum E16470: unvetted.** The host serves only a 1600 px frame, in which the fragment is about 520 px
  across. The EXIF shows a 5944 x 5348 px master that is not online. Neither side is established as Arabic or as cipher;
  the separate signs may be numerals or fractions. It needs the master scan from the museum and a papyrologist.

## Routes

| Host | Result |
|---|---|
| geniza.princeton.edu (`/en/documents/<id>/`, `/scholarship/`) | plain curl, works; `/scholarship/` returns 404 for records with no bibliography |
| images.lib.cam.ac.uk IIIF | plain curl; `full` capped at 2000 px, native by regions |
| cdn.mohrsiebeck.com | the front-matter PDFs linked from each book page (`/en/book/magische-texte-aus-der-kairoer-geniza-<ISBN>/`) work; older CDN URLs from search results give 404 |
| collections.penn.museum | record and `_1600.jpg` work; other sizes 404 |
| cryptiana.web.fc2.com/code/GL.htm | works over https (Shift_JIS) |
| decode_search.py | works (sanity check: 'Vienna' gives 55 pages) |

## What is left

- 2884: an identification of the script, the MTKG I-III Geniza-Fragmente registers, and Bohak's inventory of Geniza magical texts.
- 2885: Gil and Fleischer 2001 pp. 282-285 and India Book IV B no. 41, note 1, to confirm the proposed methods.
- 2889: the museum's master scan.
