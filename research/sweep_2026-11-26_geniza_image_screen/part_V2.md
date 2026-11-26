# Geniza image screen, part V2 (26 Nov 2026)

Three documents flagged by the PGP image screen, vetted by a Claude Code session (Claude Sonnet 5.5). Nothing merged or promoted.
Result: **no document is `open`**. One unclear row in `candidates_V2.json` (39839); two documents get no row.

| PGP id | Shelfmark | Verdict |
|---|---|---|
| 33989 | CUL Or.1700.7 verso | no row: Indic-script table, an ordinary (unread) script, no cipher shown |
| 39839 | T-S AS 205.41 | unclear row, no vetting block: Arabic-script letter table, type unknown |
| 33129 | JRL Genizah Ar. 434 (second image) | no row: pen-trial sheet; the box is Coptic-numeral-type signs, key/exercise material |

Scholarship: `footnotes.csv` (PGP, fetched 26 Nov 2026, 31.9 MB) has no record for any of the three ids or shelfmarks. PGP `documents.csv` records have no scholarship_records and no cipher tag.

## 33989 CUL Or.1700.7 verso

- **Seen.** Both sides, 1300 x 2000 px (verso) and 1340 x 2000 px (recto), plus a 2000 px native-detail crop of the lower grid. Recto: a damaged ketubba-type fragment in Hebrew script (large letters at top, cursive below). Verso: a ruled grid of about 8 rows with 3-8 cells each; each cell holds one short group of 1-4 signs. The signs are headline-less Indic letters with vowel marks (the forms look Gujarati/Kaithi-like: round bowls, no shirorekha), written in one practised hand. The scrap is torn, so row and cell counts are approximate.
- **Not a cipher.** The script family is Indic, i.e. an ordinary script that is simply unread here, not an invented sign system. The grid of short groups fits an Indic divination, numerology or letter table (PGP: "alphabetical (divination?) table"); neither a key nor a gloss is on the leaf. No Hebrew or Arabic letters are paired with the cells, so it is not a key table either. A cipher in Indic letters cannot be told from a table in the same letters without someone who reads the script.
- **Comparison.** Bohak's Devanagari letter T-S AS 159.247/248 (Cambridge Fragment of the Month, March 2008; PGP calls it possibly a Gujarati dialect; a 2013 Language Log thread suggests Kaithi) is the nearest published Indic Geniza text; it is a business-letter-like text, not a cipher. Or.1700.7 verso is a table, a different genre. No evidence of a shared hand was sought.
- **Duplicates.** known.py "Or.1700", "Or 1700", "33989": only an unrelated DECODE R-number (R7524, I33989) and a Szembek target note; leads.json and catalogue.json: nothing. decode_search "Or.1700": 2 unrelated rows (Dresden 4969, Vienna); "Genizah", "Geniza", "Rylands", "Taylor-Schechter": 0 rows (weak evidence).
- **Prior art searches.** (1) web "Or.1700.7 Genizah Indic Gujarati Devanagari table": only PGP 33989 and the Bohak/Language Log pages on AS 159.247; no study of this verso. (2) web "Bohak Devanagari T-S AS 159.247 fragment of the month": Bohak 2008 describes AS 159.247/248 only. (3) PGP footnotes.csv and documents.csv: nothing. (4) Tomokiyo unsolved.htm and GL.htm fetched and grepped for Genizah, Geniza, Cairo, Rylands, Or.1700: no hit. Not searched: Elbaum's blog posts individually, Schaefer-Shaked.
- **Keys.** None. The Coptic/Greek numeral tables are irrelevant (no numerals).
- **Next step if anyone cares.** A reader of Gujarati/Kaithi/Devanagari to identify the script and the table type (ask Bohak or the CUL Genizah Unit).

## 39839 T-S AS 205.41

- **Seen.** Both sides (recto 1658 x 2000 px, verso 1651 x 2000 px) and two 2000 px crops of the recto at about native detail (native 2463 x 2971). Recto: ruled (faint) table, about 5 columns by 14 rows; cells hold short groups of Arabic-script letters in an old angular hand, many not forming words, a few red ordinals (4, 5, 6 and similar) beside red column dividers, a column of single letters at the right, and some extra marks; a recognisable "Allah" group near the bottom. Verso: Hebrew-script lines (upper part) and several narrow vertical columns of short items (lower part), apparently a second text; not studied.
- **Verdict.** Not shown to be a cipher. The layout (numbered cells, letter groups without word structure, red dividers) is that of an ilm al-huruf / zairja / jafr or abjad table, the same reading the 25 Nov sweep gave its sibling T-S Ar.39.472 (lead 3857, unvetted). The script is Arabic, so no new sign system. Left as one unclear row without a vetting block so the item is not lost; blocker named: an Arabic letter-science specialist.
- **Duplicates.** known.py "AS 205.41", "39839": only the 25 Nov sweep README ("letter grids, uncertain, probably school tables"); leads.json, catalogue.json: nothing. decode_search for Genizah/Geniza/Taylor-Schechter: 0 rows.
- **Prior art searches.** (1) web `"T-S AS 205.41" Genizah table letters cipher OR zairja OR jafr`: only PGP pages; PGP says "further examination required". (2) PGP footnotes.csv: no record. (3) Tomokiyo unsolved.htm and GL.htm grepped: no hit. (4) Related PGP hit T-S AS 137.341 (Coptic numerals table, fiscal-like) is a different leaf, already rejected by the 25 Nov sweep.
- **Keys.** None in the leaf. The abjad/Coptic keys (JRL Ar. 392, JRL L 259, CUL Or.1080 J277, Bodl. heb. f 102/28) were not tested: no text was shown, and the leaf has no Coptic numerals.

## 33129 JRL Genizah Ar. 434

- **Seen.** Image 1 (2000 x 1501 px; the leaf lies on its side) and image 2 (2000 x 1501 px) plus a 1600 px crop of the box and a 2000 px crop of the lower half. Image 2: top left a ruled box with 4 rows of 7-9 signs each. Rows 1 and 4 are drawn with forms that match the Coptic-numeral glyphs on the verso of JRL Ar. 392 (3-like, 5-like, 7-like, reversed-nine shapes, checked against that leaf, 1500 x 2000 px); row 3 mixes a cross, hooks and a Hebrew-like shape; row 2 is Arabic-like cursive. Around it: Hebrew alphabet drills (`אבגדהוזח...`, an `אתבש` atbash heading, letter sequences), Arabic pen trials (basmala, "abd mawlana", "al-hamdu"), a row of tally strokes and loose numerals. Image 1 carries more alphabet drills (abjad order, `abjad hawwaz`) and an Arabic line.
- **Verdict: not a cipher candidate.** The box is a trial of numeral-type signs among alphabet and pen-trial lines, consistent with the PGP description ("Pen trials ... Hebrew alphabets written in order of numerical value") and with the 25 Nov sweep's key/exercise reading. The 28-odd signs are neither a text-length run nor in word-like groups; no line of ciphertext, no plaintext beside it. It is key or school material for Coptic numerals, not ciphertext.
- **Duplicates.** known.py "Ar. 434", "Ar.434", "33129": only the 25 Nov sweep README table (key material); leads.json, catalogue.json: nothing. decode_search "Rylands": 0 rows.
- **Prior art searches.** (1) web `"Ar. 434" Rylands Genizah abjad Coptic numerals pen trial cipher key`: nothing on this leaf; only other Gaster Arabic records. (2) PGP documents.csv and footnotes.csv: no scholarship. (3) Tomokiyo unsolved.htm and GL.htm grepped: no hit. (4) 25 Nov sweep README: lists JRL Ar. 392 and 434 as correspondence/abjad keys.
- **Keys.** JRL Ar. 392 verso (viewed): abjad letters each over a Coptic-numeral glyph, about 16 pairs; JRL L 259 and CUL Or.1080 J277 are the other tables on record. Ar. 434's box was not tested against them as no running text exists.

## Routes and limits

CUDL IIIF (images.lib.cam.ac.uk) and the Princeton static IIIF manifests for JRL worked by plain curl; no bot check met. Not searched: Elbaum's Genizah blog posts individually, the Schaefer-Shaked volumes, the FGP catalogue (registration), HistoCrypt proceedings. Scratch: `/tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad/v2/`.
