# Cairo Geniza cipher sweep, follow-up (26 Nov 2026)

Run by a Claude Code session (claude-sonnet-5-5) on what the thorough pass of 25 Nov left (`sweep_2026-11-25_geniza_thorough`,
`..._geniza_literature`, `vetting_2026-11-25_geniza_and_backlog`). Nothing promoted; `catalogue.json`, `leads.json` and
`targets/` untouched. Images and downloads stayed in the session scratch folder; none is in the repository. One Chrome tab
(a second tab belonged to another session and was not touched). No CAPTCHA was solved.

## Counts per source

| Source | Route | What was done | Result |
|---|---|---|---|
| `pgp-text` (transcriptions) | codeload zip, 58 MB, 10,767 `.txt` and 11,669 annotation files | grep of every transcription for cipher / cypher / encrypt / cryptic / crypto, "code", bracket notes (sign, symbol, glyph, character, magical, unidentified, drawing, diagram, figure), Hebrew (צופן, כתב סודי, סימנים, סמלים, מוצפן), Arabic (رموز, شفرة, معمى, تعمية, علامات), secret, atbash/albam/ayak/temurah, "Coptic", "Greek letters" | **0 editor markers for a cipher.** cipher 3 hits (all "deciphered"/"undecipherable name"), code 0, bracket sign/symbol 36 (all "[signed]", "[signatures]"), Hebrew 7 (all ordinary words: "siman", "tsofen" = hide), Arabic 1 (ordinary), secret 133 (secretary, secret meetings), atbash 4 (Turkish "ayak"). Hits worth an image: PGP 42084 = T-S K1.127 (Aramaic amulet, "a series of magical figures" = charakteres inside an amulet; not a cipher); PGP 1069 and 4643 ("[In Arabic characters:]", script change) |
| `pgp-text`, Coptic numeral signs | regex over U+102E0-102FF | 31 documents carry Coptic Epact numeral signs; letters among them: T-S 13J18.19, T-S 12.543 (Minyat Zifta contributions 1266, accounts), T-S AS 147.18 (money note), CUL Or.1080 J1 / T-S 8J19.33 etc. (Greek words) | only **13J18.19** carries numerals as text |
| PGP metadata, India Book / Ben Yiju / Madmun / Halfon | `documents.csv`, 2,424 documents | 61 with numeral, code, cipher, secret, cryptic, symbol words | see "India Book" below |
| Unimaged PGP records | see "Seven unimaged records" | 2 opened, 5 blocked or not online | |
| Cross-check images viewed | CUDL IIIF, PGP static IIIF, JTS figgy, Chrome | 13J18.19 (both sides), ENA 4100.7b, T-S NS J479 (both sides + Elbaum's annotated blog image), CUL Or.1080 J277 verso, Bodl. MS heb. f 102/28 recto, JRL B 5652 (both sides), T-S K5.7 recto, T-S K24.23 verso | below |
| Catalogues in Chrome | Bodleian Hebrew (Anubis passed), BL archives search | "unknown script" 0, "invented alphabet" 1 (MS. Heb. e. 73, a 36-part Arabic volume, not a hit), charakteres / magical signs 0, "secret alphabet / secret script / in cipher / Coptic numerals" 1 (MS. Heb. e. 94, the Halfon volume, known). BL: record `Or 10656` exists ("Miscellaneous genizah fragments", 26 folios), not shown as digitised | no new item |

## India Book and merchant letters with numerals or code names

Question: do the India Book / Halfon / Ben Yiju / Madmun letters carry a Coptic-numeral cipher ("a secret code that
hasn't yet been cracked", Ashur, as reported by Elbaum)? Answer from the PGP dump and its transcriptions:

- **T-S 13J18.19 (PGP 9097; IB IV 41) is the only letter** whose PGP description says "Coptic numerals used as a code
  ... substitution mechanism not determined" (recto lines 11-12, verso line 5). It is almost certainly the passage Ashur
  means. No other India Book letter (2,424 documents scanned by tag and description) carries such a note. All the other
  Greek/Coptic-numeral India Book items (about 30: T-S Ar.54.19, ENA 1822a.66 and .72, T-S AS 176.264, 183.199, NS 297.252,
  10J30.12 ...) are accounts and orders of payment, plain numbers.
- **Code names** (nomenclator style, not ciphertext): F 1908.44U (PGP 9096, "written in coded language", "the elephant"),
  Bodl. MS heb. e 94/30 (9102, the elephant again), T-S 13J18.19 itself ("the elephant", "the man you know").
  `CUL Or.1080 J225` (9046) is a "secret letter" in the sense of a confidential one, not a cipher.
- Other flags read and dropped: T-S AS 187.101 + 102 (42413, Spanish-hand accounts, "merits examination" for the Maghribi
  numeral system), T-S NS 312.55 (41911, marginal jottings of 3 lines in Judaeo-Arabic, ordinary), T-S AS 145.36 (a two-word note
  on a ketubba verso), ENA 1822a.18 ("very cryptic" Arabic legal note).

**13J18.19 (about 25 signs in three passages), worked on the PGP transcription.** The PGP text carries the numerals as Coptic
Epact signs in visual left-to-right order. Decoded by value they are ordinary Hebrew gematria letters read right to left:
recto l. 12 = 400, 70, 300, 3, 40 = ת ע ש ג מ; recto l. 13 = 40, 70, 8 = מ ע ח; verso l. 5 = 1, 60, 100, 400, 40 | 1, 100 |
1, ?, 8, 8 = א ס ק ת מ | א ק | א ? ח ח (the editors' own transcription of the verso, "אסקתמ אק א.חה", matches). So the first
layer is plain numeral-to-letter by value; the remaining layer yields no word. Tested: all 21 Caesar shifts of the Hebrew
alphabet, atbash and albam, on both reading orders, against a 144,000-type word list from every PGP Hebrew-script
transcription (1.98 million tokens): no hit above chance (the 2-3 letter strings match everything, the 5-6 letter strings
nothing). The J277 verso (viewed) holds alphabet and pair tables, not a numeral table; Bodl. MS heb. f 102/28 (viewed) is a
Hebrew-script text page whose cipher section was not isolated. The verso numerals are cursive and small at the 1367 x 2000
px that CUDL serves; the editors' own note says several are doubtful. **Not read; first layer established.**

## Seven unimaged records

| Record | Route | Result |
|---|---|---|
| p. Heid. Hebr. 22 verso (PGP 37734) | digi.ub.uni-heidelberg.de, **Chrome loaded it with no bot check** (`/diglit/p_hebr_22/0002`) | = P. Heid. Arab. III 50; recto a draft petition to the Fatimid al-Hafiz (527 AH), verso an Arabic text on the terrors of death and the grave, already edited (Dietrich). Plain Arabic hand: **not a cipher** |
| NLI 577.1/63 (PGP 33652) | `iiif.nli.org.il` manifest and the NLI item page | **Blocked**: Cloudflare "you have been blocked" (hard block, not a CAPTCHA), curl and Chrome. Left alone. Host: iiif.nli.org.il, www.nli.org.il. PGP: invocation of Muhammad and "a string of magical characters": magic, not a cipher candidate |
| AIU XII.41, XII.68, VI.B.157, VI.B.174 | AIU's own digital library does not resolve (bibliotheque-numerique.aiu.org, bibliotheque.aiu.org: no host; www.aiu.org 503); the AIU Genizah images are on NLI Ktiv, which is blocked as above | **not viewed**. PGP descriptions only: XII.41 verso a cross and "cryptic symbols" over a partly mirrored Arabic alphabet; XII.68 magic with number grids; VI.B.157 magic squares in Arabic and Hebrew letters; VI.B.174 accounts with "mysterious symbols, triangles, circles, lines, dots" beside a name. None looks like text cipher; VI.B.174 and XII.41 are worth an eye if NLI opens |
| BL OR 10656.25 | BL archives search (Chrome): record `Or 10656` found, 26 folios; BL Digitised Manuscripts page does not list it | **not online** as far as found. PGP: columns of symbols "(astronomical? not Coptic numerals)" under an Arabic document |

## Cross-check questions (literature README section 6 and 9)

1. **Is ENA 4100.7b the Zinger letter? Probably yes, not proved.** Elbaum's description: Zinger found a letter in Arabic
   and Judaeo-Arabic with a cipher portion, "nearly every word beginning with alef". PGP 11951: Judaeo-Arabic letter, lines 7-12
   a cipher "noticed by OZ", tagged `cipher`. The leaf viewed (JTS CC0 image, both letters bold Hebrew-script hand) has the cipher
   lines in ordinary Hebrew letters, and the 17 Nov reading in `targets/ena4100` counts 22 of 31 words starting with alef.
   Person, object description and the alef property all agree; only the blog's missing shelfmark keeps it unconfirmed.
2. **Do ENA 4100.7b and T-S NS J479 share glyphs? No.** ENA 4100.7b writes its cipher lines in the ordinary Hebrew alphabet
   (alef, lamed, resh, gimel, nun, final forms). J479 (viewed, both sides, and Elbaum's annotated photograph) uses about 22
   invented glyphs (loops, circled strokes, flags, a boxed cluster) plus some Arabic and Hebrew-script lines. There is no sign
   table to build: one is an alphabet-letter cipher, the other a glyph cipher. What they share is the alef-initial word pattern
   (alef-heavy in both), which could point to the same habit of marking words with a prefix or a null; that is a hypothesis,
   not tested. Elbaum's annotated image is a photograph with hand circles and a few Arabic lines, with no legible mapping
   table, so J479's mapping could not be checked from it.
3. **T-S 13J18.19 verso line 5 against the J277 and Bodl. f 102/28 keys:** viewed; see the 13J18.19 paragraph above. First layer is
   gematria by value; no shift, atbash or albam key gives a word; neither key page is a numeral table in the images.
4. **Is T-S K24.23 the Bohak cipher? Yes (recto, viewed 15 Nov); the verso (viewed now) is blank.**
5. **T-S K5.7: cipher, not a charakteres table.** Four vertical lines of about 38 colon-divided ring-ended letters, the K24.19
   system; a candidate row is in `candidates.json`.
6. **JRL B 5652 (Manchester Luna is reCAPTCHA; not touched). Images by PGP's static IIIF manifest, curl.** Image -1 (recto) is
   a plain Judaeo-Arabic letter in a rough hand, as PGP says. **Image -2 (verso) is five to six lines of ring-ended cipher
   signs, about 90, of the Bohak type**: confirmed, and not described in PGP. New row in `candidates.json`.
7. **Nimorad atbash colophon:** shelfmark is **T-S NS 246.26.2** (PGP 42614, CUDL id MS-TS-NS-00246-00026-00002, Nehemiah
   13:20-31, 903/4). "T-S NS 324.26.2" in the Cambridge FOTM text is a slip.

## Ciphertext found, new against known

| Item | Extent | Status |
|---|---|---|
| JRL B 5652 verso | about 90 ring signs | **new to PGP** (cipher side undescribed); Manchester's own note knew it (snippet) |
| T-S K5.7 recto | about 150 ring signs | known as a name; **now classed a text cipher**, row written |
| T-S 13J18.19 | about 25 numerals | known (Gil and Fleischer, Ashur); first layer (gematria) shown here |
| ENA 4100.7b | six lines | known; Zinger letter question answered |
| Everything else seen this pass | | known, plain, fiscal or magic (above) |

## Not done, blocked, for the user

- **National Library of Israel** (iiif.nli.org.il, www.nli.org.il): hard Cloudflare block of this IP, not a CAPTCHA, so
  NLI 577.1/63 and all AIU Genizah leaves (AIU XII.41, XII.68, VI.B.157, VI.B.174) stay unseen. Retry from another network, or
  ask the NLI/AIU for the images.
- **Manchester Luna**: reCAPTCHA, left alone (PGP's IIIF copies of the JRL leaves work).
- **Cambridge CUDL search**: AWS WAF (HTTP 202 empty); not tried again, PGP carries the CUDL descriptions. Bodleian Hebrew passes in
  Chrome (five more term searches, no hit). JTS ENA, Dropsie/Penn CAJS on OPenn and Manchester are inside PGP's 36,564
  documents; no separate catalogue search was run for them beyond the PGP grep.
- **BL Or 10656.25**: not found online.
- Not done: Friedberg (registration), Heidelberg other leaves, Goitein's *Mediterranean Society* and *India Book* volumes (books).
- Courtesy: Bohak, Zinger, Elbaum and the PGP work these ciphers; write to the PGP (and Rylands Genizah curators for B 5652)
  before sending a reading.

## What remains

1. JRL B 5652 verso and T-S K5.7: transcribe the ring signs and test against Bohak 2010; with T-S K12.60 verso (key-type
   material) these are the cheapest readings in the Geniza set.
2. 13J18.19: a better image than CUDL's 1367 px (Cambridge reproduction request) to settle the verso numerals before any
   second-layer search; test the Hebrew word list on other layers (Arabic transliteration in Hebrew letters, name lists).
3. NLI/AIU images when the block lifts; AIU VI.B.174 and XII.41 first.
4. Documents added to PGP after 25 Nov 2026 are not in the dump.
