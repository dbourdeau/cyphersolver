# Geniza image screen (26 Nov 2026)

Run by Claude Code sessions for Daniel Bourdeau (model `claude-sonnet-5-5` for this sweep, with sub-agents for the
screening, the second looks and the vetting). Scope: the Princeton Geniza Project (PGP), whose documents the 25-26 Nov
sweeps had searched by **words** only. This pass looks at **images**, because a catalogue line that does not say
"cipher" hides a cipher from every word search.

**Result: no new catalogue entry.** The screen re-found every known Geniza cipher that was in its pool, and nothing
else of text length. One unclear table was added as a lead (no vetting block). The earlier word-based sweeps stand.

## Method

1. **Pool.** PGP's bulk dump (`princetongenizalab/pgp-metadata`, `documents.csv`, 36,580 documents on 26 Nov 2026) was
   filtered to documents with an image whose description or type could hide an odd leaf: magic, pen-trial / doodle,
   symbol, alphabet, "unknown / unidentified / illegible", plus untyped, literary and paraliterary documents. Plain
   accounts and lists were dropped. 3,630 documents: tier 1, 2,093 (magic, "unknown", or odd leaves in paraliterary,
   literary and untyped documents); tier 2, 1,537 (letters, lists, legal and state documents with weaker signals).
   `tiers.json` holds the ids.
2. **Images.** Up to two images per document at about 760 x 900 px (`scripts/harvest.py`, one request a second per
   host; Cambridge `images.lib.cam.ac.uk`, the Princeton figgy and static manifests). 3,624 of the 3,630 have images.
   Cambridge documents that failed under the derived image name were recovered from their manifests
   (`scripts/harvest_manifest.py`, 50 of 85). Six have none: 33983, 1423, 3223, 19346, 22580, 23820.
3. **Contact sheets.** 6 documents a sheet (tier 1) or 8 (tier 2), captioned with the PGP id and shelfmark
   (`scripts/sheets.py`). 252 sheets in batch 1, then 139 more in batches 2-8.
4. **Screening.** Sub-agents viewed every sheet and flagged anything that was not ordinary Hebrew or Arabic text, numerals
   or accounts, with a calibration sheet of five known Geniza ciphers. Flags were then resolved against PGP's
   description and, for the doubtful ones, at full size (`scripts/fetch_full.py`).
5. **Re-checks.** The first agents' notes on 111 sheets were thin (their images dropped out of context), so six agents
   re-viewed those sheets with a per-sheet recording protocol (one JSON line after each sheet, `screen/r*.jsonl`).
   28 flags that had been dismissed only from the PGP description were looked at full size
   (`screen/tocheck_results.json`), and 18 more unresolved leaves at the end (`screen3/final_check_results.json`).
6. **Vetting** of every candidate that survived: `candidates_V1-3.json`, `part_V1-3.md`.

`SCREEN_INSTRUCTIONS.md` (in `scripts/`) is the brief the later screeners worked from.

## The lesson of this screen: rotate the verso first

Of the eight leaves that looked like a new script at full size, **five were ordinary Hebrew or Judaeo-Arabic
photographed upside down**: T-S 18J4.3 verso (a letter edited by Goitein, *The Yemenites*, pp. 125-129), DK 315 verso,
T-S Misc.23.5 verso, T-S K15.52 verso (it opens «בשם רחום וחנון»), T-S AS 151.155 verso and T-S NS J408 verso
(the last two found in later batches); T-S AS 157.268 was pen scribble. A four-orientation view (original, 180, 90, 270)
is now required before anything is called a candidate.

## What the screen found, document by document

| Document | Result |
|---|---|
| T-S NS J479 (8804) | known; read by Elbaum (Genizah blog, 2022) |
| CUL Or.1080 6.12 (19773) | known as lead **3856**, unvetted: four lines of an unidentified cursive; not shown to be a cipher |
| T-S AS 187.240 (42435) | known; target `tsas187240` |
| T-S K5.7 (42030) | known; catalogue 3757 |
| T-S K24.23 (32686), K24.19, K24.24, K24.37 | known (Bohak family; catalogue 2884 and 3855) |
| CUL Or.1080 14.13 + 14.25 (31508) | known as lead **3858**, closed `not_cipher` (protective amulet with a red Arabic caption) |
| CUL Or.1700.7 verso (33989) | **not a cipher**: ruled grid of Gujarati- or Kaithi-like Indic letters, an Indic divination table |
| T-S AS 205.41 (39839) | **unclear**: ruled table of Arabic-script letter groups with red numbers; probably a letter-science table like lead 3857. New row, **no vetting block** (importance 1, solvability 1) |
| JRL Genizah Ar. 392 (34992, 33087) | **key material**: Arabic letters in abjad order with a Coptic numeral under each |
| JRL Genizah Ar. 434 (33129) | **key / pen-trial material**: a box of 4 rows of signs whose rows 1 and 4 match the Coptic-numeral glyphs of Ar. 392 |
| JRL L 259 (30280), DK 248 (34091) | **key tables**: Hebrew and Greek/Coptic numerals set against letters; no running text |
| T-S 16.140 (7412) | **key material**: Hebrew alphabet, reversed alphabet and the atbash table, on the verso of a 1121 agreement |
| T-S 12.740 (38170) | not a cipher: a Bohairic Coptic magical prayer; the verso has a Coptic alphabet glossed in Hebrew letters (key material for Coptic-letter ciphers) |
| T-S 18J4.3, DK 315, T-S Misc.23.5, T-S K15.52 versos | upside-down Hebrew / Judaeo-Arabic (see above) |
| T-S AS 156.48 verso (17961), T-S AS 185.19 verso (41368) | not ciphers: Hebrew letters with ink splotches; a letter exercise |
| ENA 2847.9 verso (10112) | not open: three short pencil lines, script unidentified, too short; its neighbour ENA 2847.10 is not in the PGP dump |
| T-S AS 157.268 (16809) | pen scribble: a field of short repeated curved strokes |
| T-S AS 185.121 (39870) | ordinary: about 25-30 cursive Coptic numerals in a copied practice string |
| T-S AS 187.75 + 187.99 + 187.198 (42412) | ordinary: arithmetic sheets in Western Arabic numerals |
| CUL Or.1081 2.75.1 (31467) | **undecided, weak**: about 70 Hebrew letters in 2-5-letter groups with no recognisable word and a Latin pen trial; no row |

Class B (charakteres, magic squares, geomancy figures, amulets without text-like structure) came to about 60 leaves; none
is a lead. They are listed in the `*_candidates.json` files under `screen/` and `screen3/`.

## How well does the screen find ciphers?

Of the known Geniza ciphers that were in the pool, the screen flagged 8 of 9. Five of those were on the calibration
sheet, so that figure is biased; of the four not shown (Or.1080 6.12, T-S K5.7, ENA 3207.17, T-S AS 205.186) it flagged
three. The miss is **T-S AS 205.186**, a damaged fragment with a dotted alef-to-tet numeral cipher.
This is a small sample, a screen at about 500 px a document, and many dismissals rest on PGP's description.

## What is not covered

- **Ciphers inside letters.** Three of the 13 known Geniza ciphers are letters with a cipher passage in them (ENA 4100.7b,
  T-S 13J18.19, T-S NS 70.1), and none of them was in the pool. The word searches found them only because a cataloguer
  noted the passage. PGP has 11,439 letters; only about 430 were screened. Screening the rest would take about 22,000 images.
- Six documents with no image; leaves too small to judge on a contact sheet (many ENA fragments).
- Documents without a PGP image: the NLI and AIU leaves, still behind Cloudflare; the Friedberg catalogue (registration).
- Anything whose description and picture both look ordinary but hold a cipher in a corner of the leaf.

## Files

`candidates.json` (the one unclear row), `candidates_V1-3.json`, `part_V1-3.md` (vetting evidence), `screen/` and `screen3/`
(per-sheet logs and candidate lists), `scripts/`, `tiers.json`.
