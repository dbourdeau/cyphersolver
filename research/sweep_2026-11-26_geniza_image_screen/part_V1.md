# Geniza image screen, part V1 (26 Nov 2026): PGP 1766, 10112, 30290

Vetting by a Claude Code session (Claude Sonnet 5.5) for Daniel Bourdeau. Result: no row. None of the three is an open cipher.
`candidates_V1.json` is `[]`. Nothing merged, promoted, built or committed; images stayed in the session scratch folder.

| PGP | Shelfmark | Verdict | One line |
|---|---|---|---|
| 1766 | CUL T-S 18J4.3 verso | not a cipher | Goitein's Judaeo-Arabic letter continuation and address, scanned upside down; the "angular signs" are Hebrew letters turned 180 degrees |
| 30290 | DK 315 verso | not a cipher | Judaeo-Arabic jottings, address and a letter-square, also scanned upside down; not the ENA 4100.7b system |
| 10112 | JTS ENA 2847.9 verso | not open (script unidentified, 3 short lines) | pencil cursive of about three short lines, no script identified; no ENA 2847.10 in PGP |

## Lesson for the screen: check orientation first

Two of the three "unfamiliar scripts" are ordinary Hebrew-script Judaeo-Arabic photographed with the verso rotated 180 degrees. Before judging a
verso as a secret script, rotate it. The screen's other verso hits (and the 25 Nov sweep's K24.37 and K24.24, which are not rotated Hebrew on
my earlier reading but were not re-checked here) should be re-viewed rotated.

## 1766, CUL T-S 18J4.3 (verso, image 2): not a cipher

- **Seen.** CUDL IIIF image 2, native 3047 x 11883 px (a long narrow strip). The earlier 512 x 2000 view was too small. I viewed region crops
  of 1832 x 2000 px (top), 1920 x 380 px (the two top lines at about native scale) and 2000 x 1560 px crops of the lower block, plus the recto
  (500 x 2000 px, a Judaeo-Arabic cursive letter).
- **What is there.** Dark-ink text in two groups: 2 lines near the top and about 17 lines in the lower third, plus 3 lines of faint grey pencil
  Arabic-script cursive near the top (the "undeciphered lines in Arabic script" of PGP's description; not read here, they look like ordinary Arabic
  cursive). The dark lines look like angular hook signs with word gaps only because the image is upside down. Rotated 180 degrees the crop
  reads as Hebrew-script Judaeo-Arabic cursive; the repeated word is Goitein's "מולאנא" (our lord), and a line I read as "...מולאנא כאן ... ג'רא" corresponds to
  Goitein's verso line "אן אעלם מולאנא באלדי ג'רא".
- **Reading exists.** PGP footnote record (footnotes.csv, document 1766): S. D. Goitein, *The Yemenites* (Hebrew, Ben-Zvi 1983), pp. 125-129, listed as
  Edition and **Digital Edition**, with a "verso" section of about 17 lines (ending "...ואשתהי גואב אלכתאב ושלום / צעיר עבדיו / המודה חסדיו / עוץ"
  and an address to Perahya the judge). Also Goitein's unpublished edition (T-S 18, 5D.1.3) and index card 10969. The verso text mentions the
  Book on Fevers (Isaac Israeli) in plain Judaeo-Arabic ("כתאב אלחמיאת ללאסראילי"). The line count of the digital edition's verso matches the dark text I count.
- **Not checked.** I did not read every word of the rotated verso against the edition; the match is by the signature block, the repeated "מולאנא" and the line count. PGP's "Greek/Coptic numerals" is not borne out.
- **Searches.** (1) web "T-S 18J4.3 Genizah Perahya Iwad Ibn al-Yamani verso": no record outside PGP. (2) web Goitein/Yemenites/Ibn al-Yamani/Abraham Maimonides/Book on Fevers/cipher: nothing about a cipher; Goitein edition found via PGP footnotes.csv instead. (3) web "Geniza secret script Bohak cipher ... buhran": returned T-S NS 70.1 and T-S NS J479 only (no link). (4) `known.py` "T-S 18J4", "18J4.3", "Perahya": no hits; `decode_search.py` Genizah, Geniza, Perahya, Iwad, Cairo, Judaeo-Arabic: 0 records; leads.json and catalogue.json: no entry.
- **Verdict.** not_cipher (image rotated; plain Judaeo-Arabic, edited by Goitein).

## 30290, DK 315 (verso, image 2): not a cipher

- **Seen.** NLI IIIF (manifest iiif.nli.org.il, image FL160305220, native 4320 x 6549 px): whole leaf at 1319 x 2000 px, then crops at 2000 x 480 px and
  2000 x 580 px (about native scale) of each block, rotated 180 degrees for reading.
- **What is there.** Verso: pencil leaf numbers (315a-d); at the top two Hebrew lines upright (a clear Judaeo-Arabic jotting "כל מאמן ובחק ובמע..." and a few alef-shaped pen trials);
  a scatter of alef forms and triangle-like marks; a block of about 3 lines at left and 3 at right of dense angular signs (12-25 per line); a boxed letter-square
  (ה י ל ו ל ה / א א ב ם ... / ל ו י ... / ה ל ו ל י ה, about 4 columns, clear Hebrew letters) with pen-flourishes; and a clear 3-line block at the foot with a lone "على" and strokes.
  The dense angular lines are **Hebrew-script Judaeo-Arabic written upside down**: turned 180 degrees I read "...אלי אסכנדריה ..." (to Alexandria; the address, matching PGP's "Verso contains the address"),
  "...ען הדא אלכתאב ..." (about this letter), "אפרים יהודי", etc. Words begin with alef because of the Arabic article and alef-initial words, not because of a code.
  The letter-square is a magic or exercise square of divine-name letters (HYLWLH), a jotting, not ciphertext. PGP calls the verso "a lot of random jottings".
- **Not ENA 4100.7b.** I viewed ENA 4100.7b lines 5-14 (PGP 11951, 2000 x 930 px crop): crude large cursive Hebrew letters on a stained leaf, words formed from a few recurring letters. DK 315 is a different, regular hand, the lines are legible Judaeo-Arabic when rotated, and no passage is ciphered. The shared "begins with alef" remark is the only link, and it does not hold here.
- **Searches.** (1) web "DK 315 / Kaufmann 315 Genizah letter Najm al-Mu'allim Musafir ha-Bavli": only PGP (30290, related Bodl. MS heb. d 66/23, PGP 6459); no edition or cipher discussion. (2) web Elbaum blog / Zinger letter / alef / DK 315: Cambridge Genizah blog 22 Jun 2022 (Elbaum, the Qus letter, 2883); nothing on DK 315. (3) PGP footnotes.csv for 30290: no scholarship records. (4) `known.py` "DK 315", "Kaufmann 315": no hits; `decode_search.py` Kaufmann, Genizah: 0; leads.json and catalogue.json: no entry. (5) Tomokiyo `unsolved.htm` and `GL.htm` fetched 26 Nov 2026 and grepped for Genizah, Geniza, Cairo, Hebrew, Judaeo, Coptic, Yemen, Bohak: 0 hits.
- **Verdict.** not_cipher (upside-down Judaeo-Arabic jottings and a letter-square).

## 10112, JTS ENA 2847.9 (verso, image 2): no row

- **Seen.** Figgy/iiif-cloud image 2 at 1500 x 2000 px (the sheet is only about 850 px across, so a 850 x 770 px crop at about native scale, also rotated 180 degrees).
  Three lines of grey pencil (or soft graphite) cursive strokes: a large looped first line, a line with dots and colons (Arabic-style diacritics or numeral dots), and a long ligatured third line with a flourish. No ink, no word-like repeated groups I can segment.
- **Identification.** I cannot say which script. The strokes look like fluent Arabic-script cursive or siyaq-like shorthand, or a pen trial, more than Coptic or Greek. Not a demonstrated cipher, and about 3 short lines is not text length.
- **ENA 2847.10.** Not in the PGP dump: `documents.csv` has only ENA 2847.6 (PGP 10111, medical instructions) and ENA 2847.9 (10112) under ENA 2847. I could not check the faint script on the neighbouring verso.
- **Searches.** (1) web "ENA 2847 Genizah verso unidentified script Coptic Greek": only the PGP record, 3 languages; no scholarship. (2) PGP footnotes.csv for 10112: no records. (3) `known.py` "ENA 2847": one hit, the 25 Nov sweep README listing ENA 2847.9 under "OTHER" (not a row). `decode_search.py` Genizah, Geniza: 0. Tomokiyo and Lasry greps as above: 0.
- **Verdict.** Not open. Unvetted if ever revisited: needs a palaeographer to identify the script; blocker is script identification and length (3 lines). No row.

## Keys

No key applies to any of the three. Coptic and Greek numeral tables (JRL Ar. 392, JRL L 259, CUL Or.1080 J277, Bodl. heb. f 102/28) were not needed: none of the three shows numeral signs. Bohak's ring-letter cipher (T-S K24.19) is for Hebrew-script ring signs, which none of these show.

## Side notes for the sweep

- PGP T-S NS 70.1 (26158): verso "Letter in Judaeo-Arabic written in a cipher", tag cipher, "The cipher was cracked by Gideon Bohak in 2025", to be published by Bohak, Zinger and Elbaum (page fetched 26 Nov 2026). Not a lead here, but any Bohak-family lead from this screen should be checked against that forthcoming publication, and it is a prior-art flag for catalogue 2883 if the Zinger letter turns out to be related (not shown).
- Fetch note: CUDL region requests occasionally reset the connection through the proxy; retrying once after a few seconds worked. Footnotes.csv was fetched from raw.githubusercontent.com into scratch.
