# Cairo Geniza cipher sweep, thorough pass (25 Nov 2026)

Run by a Claude Code session (claude-sonnet-5-5) for the project. Scope: unread cipher and secret-script letters and
documents in the Cairo Geniza (11th-13th c. first, later items noted), Judaeo-Arabic, Arabic, Hebrew, worked from the
catalogue's own data. Nothing promoted, nothing in `catalogue.json` or `leads.json`, `targets/` untouched.
Images, downloads and scripts stayed in the session scratch directory; no image is in the repository.

Note: the sweep folders named in the brief as earlier work (`sweep_2026-11-23_genizah_tables`, `..._22_arabic_hebrew_openn`,
`..._22_gotha_hebrew`, `..._23_hebrew_manuscripts`) do not exist on `main` or on the `integration-*` branches I could see, so
I read only `sweep_2026-11_hebrew`, `sweep_2026-11-15_arabic/part_A.md` (and parts D), `sweep_2026-11_arabic`, `uk_libraries`,
`vetting_2026-11-15_arabic_1`, `sweep_2026-11-15_wave15_arabic2` and `targets/ena4100`, `targets/tsas187240`.

## The key route: PGP publishes a bulk dump

`princetongenizalab/pgp-metadata` on GitHub (Zenodo DOI 10.5281/zenodo.15839055, CC-BY-NC, updated daily; this copy pushed
25 Nov 2026): `data/documents.csv` (36,564 documents: description, tags, type, languages, dates, IIIF manifest URLs),
`footnotes.csv` (25,617 scholarship records incl. digital editions), `fragments.csv`, `people.csv`, `places.csv`. Downloaded with
plain HTTP into a scratch folder; every document grepped locally. A second repo, `pgp-text` (transcriptions, 94 MB), was
**not** downloaded or grepped (see "What remains"). Note PGP's language field has a value "Greek/Coptic Numerals" (1,000+
documents, ordinary India Book / fiscal numerals) and "Unidentified (Hebrew script)", "Unidentified language and script",
"Unknown language in Devanagari script" (39 documents), all read.

### Queries and counts (documents matching, PGP dump, fields: tags, description, language note, date notes; footnotes separately)

| Term (regex) | Docs | Result |
|---|---|---|
| cipher / cypher | 39 | the known set (tags cipher x14) plus fiscal "cipher" = opening sign (adda, nuqila, basmala); new names: T-S NS 297.254, T-S Misc.28.232, ENA NS 38.10 (all fiscal or plain on the image) |
| cryptic | 98 | obscure content in nearly all; real signal: ENA NS 63.10, ENA 4101.14a, ENA NS 28.1, T-S AS 142.223, T-S NS 38a.133, ENA 3965.13 (all checked, none a cipher) |
| code / coded / encrypt / scramble | 17 | India Book code names (F 1908.44U, T-S 13J18.19), T-S AS 153.317 argot, Atbash colophon T-S NS 246.26.2 (903/4), ENA 3207.17 |
| crypto*, encoded, enciphered | 0 | |
| secret | 149 (151 with symbol) | secretaries, secret letters of T-S K2.4, "secret doorway"; no cipher |
| symbol(s) | 112 | fiscal currency signs; magic: ENA 3773.4, ENA NS 71.11, Moss. Ia,26.2, ENA 2585.3 |
| glyph / characters | 129 / 132 | glyph tag = Arabic fiscal opening sign (51 tagged); characters = "large characters", mirror imprints |
| unidentified/unknown script or language (lang field and description) | 39 + 344 text mentions | 39 language-flagged read one by one; image-checked 14; rest late accounts or tiny scraps |
| magical, amulet, charm, spell | 512 (258 tagged magic) | image-checked 25 with symbol/character/sign wording; see table |
| numerals, dots, Coptic numerals | 2,318 | 1,000+ ordinary Coptic-numeral accounts; tags "Coptic alphanumeral" 25 (charity lists); only T-S AS 185.121, JRL L 259, JRL Ar. 392 matter |
| siyaq, abjad, gematria | 19 | dates by gematria; abjad/Coptic correspondence tables JRL Ar. 392, 434 (keys) |
| invented, made-up, idiosyncratic | 151 | "invented" = nothing cipher-like except T-S NS J479 |
| atbash, albam, ayak, temurah, permutation | 23 | key and pen-trial material: T-S 16.140 (1121), K5.39, K5.47, ENA 3982.15, T-S AS 153.438, T-S AS 186.57, T-S Ar.35.135, AIU IX.A.46, IX.A.49, ENA 3759.5, JRL Ar. 434, CUL Or.1080 J277 |
| secret language / secret writing / ketav sod / malakhim / angelic | 4 | none new |
| undeciphered, indecipherable, unreadable | 61 (+141 looser) | "undeciphered note in Arabic script" = unread Arabic, not cipher; only T-S K5.7 means a cipher |
| doodle, pen trial, monogram, 'alama | 640 | not followed; fiscal and school |
| Indic / Ethiopic / Samaritan script | 15 | T-S AS 159.247/248 (Indic, Bohak 2008, FOTM), not a cipher |
| mirror / mirrored script | 347 (with glyph/character) | ink offsets, except Halper 453 (a deliberate mirror amulet, short) |
| Hebrew: כתב סודי, צופן, כתב נסתר, כתב מוצפן, לשון הסוד, אתב"ש | 0 real (3 incidental) | |
| Arabic: رموز, رمز, معمى, تعمية, كتابة سرية, شفرة, خط سري | 0 | |
| footnotes (editions, translations): cipher/encrypt/cryptogram/atbash/secret letters/coded/cryptic/invented script/ketav sod/tzofen | 3 (one real: ENA 3934.5 "Cipher" = fiscal opening sign) | the digital editions carry no cipher markers |

Tag facets: the dump has 2,715 distinct tags; every tag containing cipher, ciphers, bialphabetic, secret, glyph, cryptic,
mysterious sign, magic square, alphanumeral, Coptic alphabet, Greek alphabet, unknown language, doodle(s), geomancy, script(s)
was listed (81 documents) and the rare-tag ones opened; "bialphabetic" is a PGP tag for mixed-script writing (Arabic with
Hebrew names), not a cipher (except T-S AS 205.186, which is also tagged cipher).

## Other catalogues

| Source | Route | Result |
|---|---|---|
| Cambridge Digital Library search | Chrome; `/search/JSONAdvanced` returns HTTP 202 with an empty body (AWS WAF challenge), page is an empty shell | **blocked**; PGP carries the CUDL descriptions, so the loss is small. Not clicked through. Tab: cudl.lib.cam.ac.uk/search |
| Bodleian Hebrew and Judaica Manuscripts (hebrew.bodleian.ox.ac.uk, Genizah + others; the old genizah.bodleian URL redirects here) | curl hits an Anubis proof-of-work page; **Chrome passes it** (no CAPTCHA). Search is `/catalog/?q=` | cipher 1 (MS. Heb. e 94, the Halfon letters, known), cryptic 2 (MS. Heb. c 56/5 "Scribbling or cryptic writing?", viewed: Arabic pen trials with a basmala and names, PLAIN), secret writing 1 (MS. Heb. d 78, Rashi fragments: nothing), cypher 0, code 0, symbols 0, atbash 0, cryptogram 0, unidentified script 1 (MS. Reggio 43, not Genizah), shorthand 1 (MS. Heb. e 75, volume of Arabic fragments, not opened), magical 1 (MS. Heb. e 74: "Magical recipes", not opened), unintelligible 1 (MS. Heb. d 74). The catalogue is volume-level, so the hits are weak. Output filter of the browser tool blocks scripted result lists; results were read page by page |
| Penn Libraries catalogue (`find.library.upenn.edu/catalog.json`) | plain curl | genizah 1,136, geniza 306; "genizah cipher" 0, "genizah cryptic" 0, "genizah unidentified script" 0, "genizah secret" 3, "genizah symbols" 4, "genizah magic" 28, "genizah amulet" 6: all printed books and finding aids (Halper manuscripts are in PGP already) |
| Manchester Rylands (Luna) | curl returns a reCAPTCHA "Verify Access" page | **blocked**, not touched. JRL documents are covered through PGP (images by the princetongenizalab static IIIF manifests, which work by curl) |
| Friedberg Genizah Project (fjms.genizah.org) | front page loads; catalogue needs registration | not swept |
| National Library of Israel (KTIV) | not retried; Cloudflare in the 6 Nov sweep | not swept |
| JTS ENA, Bodleian MS heb., BL Or., AIU, Mosseri, Halper, Dropsie | all inside PGP's 36,564 documents, so covered by the dump grep. Image routes: JTS via figgy manifests + iiif-cloud (works), Bodleian via static manifests -> puliiif.princeton.edu (works), AIU/BL/NLI documents have no image URL in PGP (5 documents unviewed, below) | |
| Heidelberg p. Heid. Hebr. 22 verso | digi.ub.uni-heidelberg.de returns an Anubis bot check to scripts | blocked, not tried in Chrome |
| Göttingen, St Petersburg (RNL Firkovich), Vienna ONB Geniza | not reached | no cipher-specific route; not swept |

## Table of every candidate and its image verdict

Verdicts from page images (viewed by this session and two image-reading sub-agents, one process at a time; K24.37,
K24.19, K24.24, Or.1080 6.12 and NS 297.254 re-viewed by me; others on the agents' reading, so treat "PLAIN" or "FISCAL"
as probable). The agents' per-document notes (JSON lines) are kept in the session scratch folder, not in the repo.

### Real ciphertext or letter-number code (in PGP or catalogues)

| Shelfmark (PGP id) | Date | Language | Extent | Sign system | Plaintext, key or gloss | Reading exists? | Status |
|---|---|---|---|---|---|---|---|
| T-S K24.37 (32699) | undated | unknown | 8 lines, about 200 signs | invented angular alphabet, dash dividers, boxed lines | none | none; PGP calls it "maybe mirror Hebrew"; not in Bohak's list | **NEW** (not in earlier sweeps) |
| T-S K24.24 (33913) | undated | unknown | 10 lines of 28-35 signs (about 300) + about 7 marginal lines; verso plain Arabic | cursive angular signs, dots as dividers, Hebrew-cursive look, not Bohak's ring letters | none | none | known (15 Nov part A); image confirmed |
| CUL Or.1080 6.12 (19773) | undated | unknown | 4 lines, about 200 strokes, + about 20 below | rapid stroke script, unidentified (shorthand? numerals? foreign script?) | none | none | **NEW**, script identification first |
| T-S K5.7 (42030) | 11th c. | Hebrew (Bohak cipher) | 4 lines of about 38 signs | ring-letter cipher, colon dividers, signs below incl. Arabic consonants | key published (Bohak 2010) | Bohak family | known; key published, texts formulae |
| T-S K24.23 (32686) | 11th c. | Judaeo-Arabic | 4 lines of about 9 + 3 stroke lines | Bohak ring letters | key published | Bohak family; partial reading on the site (K24.23 and ENA 3211.2, a76bda9) | known |
| ENA 3207.17 (10130) | undated | unknown | 6.5 lines, about 75 signs, recto only | Arabic-like letters mixed with triangles, squares, X, rings | none; verso a rectangle figure with about 45 border signs | none | known name (6 Nov), first image check; **new** detail |
| ENA 3682.7 (6744) | undated | Greek-like capitals at end | about 7 lines, about 80 signs inside an ouroboros | ring-ended letter signs, same family as K5.7 and K24.23 | none; recto magical instructions | none | **NEW**, borderline cipher (may be free charakteres) |
| ENA 4100.7b (11951) | undated | Judaeo-Arabic | about 5 lines of 12-18 (about 70 signs) | Hebrew-like glyphs and digits | none | none (Zinger found it) | known, `targets/ena4100`; image confirmed |
| T-S AS 187.240 (42435) | undated | Hebrew | about 30-40 short lines in two systems | see `targets/tsas187240` | none | none | known; not re-viewed |
| T-S NS J479 (8804) | after 1295 | Judaeo-Arabic | one folio, about 1,200 glyphs | invented glyph cipher, 22 symbols | Elbaum's annotated mapping on Genizah blog | partial (Elbaum 2022), written up here | known |
| T-S NS 70.1 verso (26158) | undated | Judaeo-Arabic | a letter | Hebrew letters with dots | n/a | cracked by Bohak 2025, unpublished | known |
| T-S AS 205.186 (42291) | undated | Judaeo-Arabic | fragment | alef-tet with dots x10, x100 | n/a | Elbaum | known |
| T-S 13J18.19 (9097) | after 1139 | Judaeo-Arabic | 2 lines, about 11 numerals | Coptic numerals as letters | key candidates J277, Bodl. heb. f 102/28 | Gil and Fleischer partial | known; not re-viewed |
| CUL Or.1080 14.13 (31508) + 14.25 (31451) | undated | Arabic | 8 + 3 lines of about 25 marks + diagram | alif strokes and Indic digits, amulet | red Arabic instructions on 14.25 | none | **NEW**, probably a wafq/letter-number amulet code |
| T-S Ar.39.472 (20963) | undated | Arabic letters | about 45 cells, about 1,000 letters over 2 sides | abjad letter headings, non-word letter strings, numeral columns | red numbers | none | **NEW**, probably divinatory (ilm al-huruf / zairja) |
| ENA NS 71.11 (10063) | undated | Arabic | 5 lines, about 50 signs | ring-ended khawatim (seal signs) with a small repertoire, named khawatim in the text | none | none | **NEW** (amulet signs; cipher unlikely) |
| T-S AS 185.121 (39870) | undated | unknown | 2 lines of 12-14 Coptic-style numerals | numerals, "may spell words" per PGP | none | none | low confidence, probably accounts |

### Key tables and key-like material

| Shelfmark | Content |
|---|---|
| T-S K12.60 verso (41966) | grid of about 20 ring-ended charakteres each beside a small letter: candidate key for the ring-letter family; to compare with Bohak's key |
| JRL L 259 (30280) | Hebrew letters, three registers (units, tens, hundreds), paired with Coptic-style numeral signs: key for Coptic-numeral ciphers |
| JRL Genizah Ar. 392 (34992) | about 16 pairs, Arabic letters over Coptic-numeral glyphs |
| JRL Genizah Ar. 434 (33129) | Hebrew alphabet in numerical order, atbash heading, boxed grid |
| CUL Or.1080 J277, Bodl. heb. f 102/28, T-S K2.4 | known keys (6 Nov sweep) |
| T-S AS 205.41 (39839), T-S NS 137.149 (39372) | letter grids, uncertain, probably school tables |
| Atbash pen trials (T-S 16.140 of 1121, K5.39, K5.47, ENA 3982.15, AS 153.438, AS 186.57, Ar.35.135, AIU IX.A.46/49, ENA 3759.5) | alphabets only |
| T-S NS 246.26.2 (903/4), Av 4876 colophon (1116) | scribe's name in atbash, a name only |

### Checked and rejected (image verdict)

FISCAL: T-S NS 297.254 (viewed, ordinary Arabic account with opening glyph), ENA NS 38.10, ENA NS 28.1, ENA 3965.13, ENA 3286.21,
T-S NS 301.59, T-S NS J569, JRL Ar. 412, ENA 3936.2. PLAIN: T-S Misc.28.232, T-S AS 137.341, T-S AS 142.223, T-S NS 38a.133,
ENA 2899.25 (modern number scribble), ENA 2985.1, T-S AS 184.96, CUL Or.1080 9.7, ENA 3956.2, T-S AS 213.7, T-S AS 180.7,
Bodl. MS heb. c 56/5. MAGIC (talismanic signs, no letter text): ENA NS 63.10, T-S AS 143.26 + ENA NS 73.12, ENA 3773.4, Moss.
Ia,26.2, ENA 2585.3, T-S NS 297.68, T-S NS 324.59, T-S NS 322.19 (Hebrew letters each repeated 5-10 times), JRL Ar. 831,
CUL Or.1080 14.27, T-S K25.159, ENA 3141.1. SHORTHAND: T-S AS 150.135, Bodl. MS heb. f 56/1-3 (Exodus 20 with each word cut to 1-2
letters, known plaintext). OTHER: ENA 4101.14a (Hebrew labels over stroke tallies), ENA 2847.9, T-S AS 208.58, JRL B 2610, T-S Ar.35.206,
T-S AS 187.103 (geomancy dots), T-S AS 187.75 (arithmetic). ILLEGIBLE: ENA NS 77.272, T-S AS 208.82.
**Not imaged** (no image URL in PGP): AIU XII.41, AIU XII.68, AIU VI.B.174, AIU VI.B.157, BL OR 10656.25; NLI 577.1/63 (Cloudflare);
p. Heid. Hebr. 22 verso (Heidelberg bot check).

## Prior art for the new rows

Web searches 25 Nov 2026 for T-S K24.37 and for Or.1080 6.12 / T-S Ar.39.472 / K24.24 with cipher and Bohak: only the PGP
records and the already known Bohak (K24.19 family), Elbaum (NS J479) and Bohak/Zinger/Elbaum (NS 70.1) items. K24.37 is in none of the
Bohak lists. Not searched this session: Schaefer-Shaked/Bohak inventories, FGP, the Cambridge blog archive beyond 2022.
The PGP records are the only description of each document, so no reading is known.

## Ranked for a reading attempt

1. **T-S K24.24** (about 300 signs, 10 lines, one clean system, already a lead) with **T-S K24.37** (about 200 signs, 8
   lines, dash-divided): the two may be one cipher (same box, both invented alphabets, neither in Bohak's ring-letter set); about 500
   signs together. First test: compare sign inventories, then a word-shape (dash group) analysis. Coordinate with PGP.
2. **CUL Or.1080 6.12** (about 200 strokes): identify the script first; may end as shorthand or numerals.
3. **ENA 3207.17 + ENA 3682.7 + T-S K5.7**: ring and geometric letter signs, 75-150 signs each, in the Bohak family; a
   reading is probably a key match with Bohak 2010 plus T-S K12.60.
4. ENA 4100.7b (70 signs, `targets/ena4100`, plain-text frame around it), T-S AS 187.240 (existing targets).
5. Low: CUL Or.1080 14.13, T-S Ar.39.472 (amulet and divination tables, likely published key types).

## What remains

- `pgp-text` (transcriptions, 94 MB) not grepped for editors' markers like "[cipher]", "[symbols]".
- CUDL search (WAF), FGP (registration), NLI (Cloudflare), Manchester Luna (reCAPTCHA), Heidelberg (bot check): blocked. The
  tabs were not cleared; the Bodleian Anubis page did pass in Chrome.
- 5 documents without image URLs (AIU XII.41, XII.68, VI.B.174, VI.B.157; BL OR 10656.25) and NLI 577.1/63.
- Bodleian Hebrew catalogue hits MS. Heb. e 75 and e 74 not opened; their Genizah fragments are in PGP anyway.
- The "PLAIN/FISCAL" verdicts of the sub-agents were not independently re-viewed (except those listed above), and no
  K24.37/K24.24 transcription was attempted; the Bohak key was not compared.
- Documents added to PGP after 25 Nov 2026 are not in the dump.
- Courtesy: Bohak, Zinger and Elbaum work these ciphers; write to the Princeton Geniza Project before sending anything on K24.37, K24.24 or ENA 4100.7b.
