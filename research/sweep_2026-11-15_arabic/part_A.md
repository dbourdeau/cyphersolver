# Arabic cipher sweep, part A: North American holdings and the Cairo Geniza (15 Nov 2026)

Run by a Claude Code session (model claude-fable-5-2) for the project, 15 Nov 2026. Scope: unread enciphered texts in the
Arabic language or script (Judaeo-Arabic included), any date to 1950, in North American collections and the Cairo Geniza.
Nothing solved, merged, promoted or committed. Rows: `candidates_A.json` (4 rows, 2 with a complete `vetting` block).
Scripts and downloads are in the session scratch directory only (`.../scratchpad/partA/`), not in the repository.

## Result in one paragraph

Penn LJS 51 was paged from cover to cover (212 text pages). It is not a set of letters with a key table: it is a
14th-century Mamluk secretary's account of the cipher verses (*mutarjam*) he exchanged with colleagues, and after each
cipher passage he writes "I solved it" and gives the plaintext. One passage has no plaintext: the last one, **f. 106v**,
because the manuscript breaks off there. That is the best find. In the Geniza, **ENA 4100.7b** (six lines of a secret
language inside a family letter) is confirmed on the image and vetted open; **T-S K24.24** is a new lead (about 250 signs
of an unidentified script, not vetted); **T-S 13J18.19** (1139) is carried forward without a block because two partial
solutions are in print. T-S NS J479, which the 6 Nov sweep listed as unread, has a published reading and is closed.
The North American catalogues added nothing in Arabic beyond LJS 51: the "secret writing" notes at Princeton turned out,
on the images, to be talismanic signs.

## Routes

| Host | Route | Result |
|---|---|---|
| OPenn (`openn.library.upenn.edu`) | plain curl; `Data/0001/ljs51/data/web/0084_NNNN_web.jpg` (1422 x 1800 px), `.../master/0084_NNNN.tif` (2339 x 2959 px, 20 MB), TEI at `.../data/ljs51_TEI.xml`; collection list `Data/muslimworld_contents.csv` | works, and fast on this day (0.5 s per JPEG; the 6 Nov note about a throttled host no longer holds). About 232 requests used: budget reached, so LJS 409 and the TEI files of the other 944 "Manuscripts of the Muslim World" items were not fetched |
| Penn catalogue (`find.library.upenn.edu/catalog.json`) | plain curl, Blacklight JSON, facet `format_facet=Manuscript` | works; about 20 requests |
| Princeton Geniza Project (`geniza.princeton.edu`) | plain curl; `/en/documents/?q=...&page=N`, `/en/documents/<id>/`, `/scholarship/`, `/related/` | works; about 50 requests. A page past the last one returns 404 |
| CUDL images (`images.lib.cam.ac.uk/iiif/<id>.jp2`) | plain curl. `full/full` is capped at 2000 px on the long side; native resolution by `x,y,w,h/full` regions of 2000 px or less, stitched | works; about 70 requests |
| JTS images via Princeton IIIF (`iiif-cloud.princeton.edu/iiif/2/<id>/full/full/0/default.jpg`) | plain curl; the id is in the PGP page source | works, full size (5428 x 7230 px). This is the "JTS image route not tested" of the 6 Nov sweep |
| Princeton catalogue (`catalog.princeton.edu/catalog.json`) | plain curl | search JSON works (22 requests) but returns titles only. **Record pages (`/catalog/<id>/raw`) return a "Verifying connection" bot page**: stopped (my script ran 23 record requests before I read the first reply; all got the bot page) |
| DPUL (`dpul.princeton.edu/islamicmss/catalog.json`) | plain curl | search JSON works and gives call number, date and abstract (about 25 requests). **Record pages give the same "Verifying connection / Verify You Are Human" page**: stopped after 8 |
| Digital Scriptorium (`search.digital-scriptorium.org`) | plain curl; `catalog.json?search_field=shelfmark&q="Garrett no. 60L"`, then `/catalog/DS<n>` | works; the record page carries the Princeton note field and the figgy IIIF manifest URL. This is the way round the Princeton record pages without touching the bot check |
| Princeton figgy manifests and images (`figgy.princeton.edu/.../manifest`, `iiif-cloud.princeton.edu`) | plain curl | works |
| Cryptiana (`cryptiana.web.fc2.com/code/`) | https (http gives a 302) | works |
| vHMML Reading Room (`www.vhmml.org`) | curl | **connection reset** on three attempts (TLS never completes). Not swept |
| Library of Congress (`loc.gov ... fo=json`) | curl | **403** on the first request. Stopped |
| HathiTrust full-text search (`babel.hathitrust.org/cgi/ls`) | curl | **403** on the first request. Stopped. Michigan Islamic Manuscripts not swept |
| Michigan catalogue (`search.lib.umich.edu`) | curl | **403**. Stopped |
| Harvard LibraryCloud API and CURIOSity Islamic Heritage Project | curl | **403** both. Stopped |
| Columbia CLIO (`clio.columbia.edu/catalog.json`) | curl | **Anubis "Making sure you're not a bot" page**. Stopped |
| Yale digital collections (`collections.library.yale.edu/catalog.json`), Calisphere (UCLA) | curl | HTTP 202 with an empty body (WAF challenge). Stopped |
| McGill (WorldCat discovery), NLM Bethesda | curl | JS shell / static pages with no search; not swept |
| Walters (`thedigitalwalters.org` access list) | curl | static list fetched; 0 lines with cipher or secret |

## Search terms and hit counts

**Princeton Geniza Project** (document search): cipher 39; `tag:"cipher"` 13; "cipher to examine" 20,697 (OR search, first
250 read); cryptic 97; code 111 (almost all "codex"); encrypted 0; cryptogram 0; cryptography 0; enciphered 0;
undeciphered 51; indecipherable 1; secret 148; "secret script" 7,580 and "secret writing" 2,928 and "unidentified script"
7,885 and "unknown script" 10,612 (OR searches, first 250 of each, nothing beyond the cipher tag); glyphs 99; symbols 81;
atbash 12. Outcome: the 13 tagged items are the whole set. "Undeciphered" means an Arabic-script note nobody has read
yet (bad hand), "glyph" and "cipher" in Arabic-script documents mean the fiscal opening sign (*adda*, *yudfa'*), a
basmala monogram or an *'alama*; "cryptic" means obscure wording. PGP hits read as possible sign texts and not opened:
ENA NS 63.10 (PGP 32133, "unconnected Arabic script interspersed with cryptic symbols", tag magic), AIU XII.41 (PGP
30954, a cross, "cryptic symbols" and a mirrored Arabic alphabet), T-S Ar.39.472 (PGP 20963, single letters "possibly
abbreviations or codes"), T-S AS 185.121 (PGP 39870, Coptic numerals that may spell words).

**Princeton catalogue**, facets Manuscript + Arabic: cipher 1, cypher 4, cryptogram 0, cryptography 0, "secret alphabet"
4, "secret script" 6, "secret writing" 3, coded 3, encrypted 1 (the Penn LJS 51 e-record), "in code" 3, secret 14,
تعمية 0, مترجم 2, المعمى 0, شفرة 0, أقلام 13, رموز 24, alphabets 608 (first 100), "unidentified script" 55,
undeciphered 1. **DPUL Islamic Manuscripts**: cipher 0, cypher 0, cryptogram 0, cryptography 0, "secret alphabet" 5,
"secret script" 3, "secret writing" 4, coded 0, encrypted 0, secret 11, alphabets 5, تعمية 0, مترجم 0, المعمى 0, شفرة 0,
أقلام 3, رموز 12, undeciphered 0, "unidentified script" 6. The رموز and أقلام hits are hadith sigla, arithmetic "pens"
and *jafr*; the "unidentified script" hits are Babi/Azali and miscellany records, not opened.

**Penn catalogue**, facet Manuscript: cipher 36, cypher 2, cryptogram 14, cryptography 15, "secret alphabet" 0, "secret
script" 0, "secret writing" 0, encrypted 7, encoded 105, "in code" 81, تعمية 0, المعمى 0, أقلام 0, "arabic cipher" 0,
"arabic alphabets symbols" 2, "arabic secret" 0, "persian cipher" 0, "ottoman cipher" 0 (رموز: request failed, not
retried). The only Arabic-script hits are LJS 51 and LJS 409; the rest are European cipher manuscripts, Hebrew amulets
and theses. **OPenn "Manuscripts of the Muslim World"** title list (944 items, titles only): LJS 51, LJS 409, Columbia
MS Or. 16 (charms and talismans), MS Or. 152a (letter magic), Penn Ms. Codex 1963 (*Hall al-tilsam*); descriptions not read.

**Digital Scriptorium**: cipher with the Arabic language facet 0; cipher alone 3 (none Arabic). Its search covers
titles, not the note field, so it is only useful for looking up a known shelfmark.

## Penn LJS 51, page by page

All 225 images were fetched; the 212 text pages (images 0084_0006 to 0084_0217, ff. 1r-106v) were viewed. Images 6-23
(ff. 1r-9v) at 640 px a page, 24-217 on contact sheets at 480 px a page, ff. 16v-17r, 61v, 71r-v, 74r-v and 86r at
1422 px, f. 106v from the master TIFF (2339 x 2959 px). At 480 px the layout is certain (cipher block, then Arabic)
and the solution formula is legible; I did not read every Arabic line, so the statement below rests on the layout and
the formula, not on a collation of each plaintext.

- **What the book is.** A first-person narrative, acephalous and incomplete at the end. The compiler exchanges cipher
  verses with named men: "wa-kataba li ..." (X wrote to me) or "katabtu lahu" (I wrote to him), a block of two to twelve
  lines in an invented alphabet with a dotted vertical stroke between words, then "fa-halaltuhu sari'an ... wa-huwa"
  (I solved it quickly, and it is:) and the verses in Arabic, often with remarks on which letters fell first (f. 2v
  lists the order: ya', nun, alif, mim ...) and on tricks (dropped letters, lam-alif as one sign, unusual words).
  Named people include Shihab al-Din al-mutarjim, al-maqarr al-makhdumi al-'Ala'i, Ibn Fadl Allah (ff. 17r, 39v),
  Burhan al-Din al-Qudsi, Taj al-Din Ibn al-Mulayh, Amin al-Din the Hanafi qadi of Hama, a qadi Nasir al-Din who was
  muwaqqi' al-dast (f. 74r), and the authorities Ibn 'Adlan, Ibn Dunaynir and al-Kindi (f. 61v: "by God, had Ibn 'Adlan
  lived, or Ibn Dunaynir or ... or al-Kindi, and seen this solution ..."). An anecdote on f. 86r is dated
  "in the year seven hundred and thirty-odd" at Alexandria. So the text is Mamluk, about 1330-1370; Penn dates the copy
  to the 15th century ("14--", Syria?). Names were read from the images at web resolution and are not collated.
- **Transcriptions.** Every cipher passage but one is followed by its plaintext in the running text. In addition a
  minority carry small red Arabic letters over the signs (an interlinear key or gloss): ff. 1r, 1v, 51v, 52v, 53r, 54v,
  55v (partly), 57v, 59v, 87r, 87v, 88r, 89v, 90r, 90v, 91r, 93v, 95v, 97r, 97v. F. 63v is a "tree" script (*qalam
  mushajjar*) with red marks. There are no separate key tables anywhere in the volume: Penn's "approximately 150
  alphabets" are the alphabets used in the messages, each recoverable from its message and plaintext.
- **The one cipher with no plaintext: f. 106v** (image 0084_0217). "Wa-kataba li Ibn al-Qaysarani", then seven lines of
  signs, about 20 a line, roughly 120-130 signs in about 30 word groups; three or four small red letters over the first
  signs of line 1 only; then "fa-halaltuha fi l-hal ... wa-wajadtuhu ja'ala al-lam alif ..." and the leaf ends, with the
  rest lost. Row 1 of `candidates_A.json`, vetted open. The red letters and the lam-alif remark are free hints.
- **Lost plaintext elsewhere.** F. 1r is torn and abraded (cipher with red gloss, the Arabic below mostly gone) and
  f. 1v has lost its lower outer corner; both are glossed in red, so they are read, not leads.
- **As a corpus.** About 200 cipher/plaintext pairs in about 150 alphabets, with the solver's own notes on method: the
  oldest body of real Arabic cipher messages found by this project, and unstudied as far as the searches show. That is
  worth a target of its own (a key-recovery and edition exercise), separate from the f. 106v lead.

Prior art searched: Penn TEI and catalogue, Digital Scriptorium DS738, the Penn facsimile record, web searches in
English and Arabic, Voynich Ninja thread 4685 (glyph comparisons; replies behind a login), Cryptiana (unsolved.htm,
crypto.htm, GL.htm), DECODE. Nothing. Not opened: *Transformation of Knowledge* (2006) p. 43, the Schoenberg catalogue
entry cited by the 6 Nov sweep.

## Finds, best first

1. **Penn LJS 51, f. 106v**: see above. Vetted `open`. Text 14th c., copy 15th c.
2. **JTS ENA 4100.7b** (PGP 11951): letter of a son in Qus to his mother. Recto image 5428 x 7230 px viewed whole and
   lines 6-14 at full resolution: about 17 lines in Hebrew script, of which lines 7-12 are a secret-language passage in
   ordinary Hebrew letters where nearly every word begins with alef; no gloss, no key; verso is a second letter in
   Arabic and Hebrew script. This is the letter Elbaum's 2022 blog attributes to Oded Zinger ("almost all the words
   begin with alef"), so it is a word game or an added-letter jargon, not a sign cipher. PGP shows no transcription and
   says "needs examination/decipherment". Undated. Vetted `open`.
3. **CUL T-S K24.24** (PGP 33913 and 32108): one side has 11 lines of an unidentified sign script, about 250 signs,
   slanted strokes and dots between groups, with a faint marginal column; the other side is large Arabic script.
   Viewed at 2000 px and the top half at native 3806 x 3664 px. New lead. No vetting block: the K box is the magic box
   and neither Schaefer-Shaked, *Magische Texte aus der Kairoer Geniza*, nor Bohak's inventory was opened; the script
   has also not been ruled out as a known cursive.
4. **CUL T-S 13J18.19** (PGP 9097), dated after 1 Nisan 1139: Ibn Ezra to Halfon b. Netanel. Recto at native 5685 x
   8199 px: five Coptic-numeral signs in line 11 and three at the start of line 12; verso line 5 (about 11 signs) not
   opened. PGP (Friedman, India Book IV B no. 41): Gil and Fleischer (2001, pp. 282-285) proposed readings for the
   first two words by two different methods and none for the third; Friedman leaves it open. Row without a block.

## Closed or read (no row)

- **CUL T-S NS J479** (PGP 8804; the 6 Nov Hebrew sweep's lead): **read.** Alan Elbaum, "Q&A Wednesday: Secret codes and
  erotic prose", Cambridge Genizah Research Unit blog, 22 Jun 2022 (updated 16 May 2025): he assigned the roughly 22
  signs to the Hebrew alphabet and published an annotated image "showing the 'translation' of the cipher into Hebrew
  script"; the PGP description summarises the content (signature, two Burda verses, a legal formula, erotic passages).
  Both sides fetched at native 3097 x 4366 px.
- **CUL T-S NS 70.1 verso** (PGP 26158): "cracked by Gideon Bohak in 2025", to be published by Bohak, Zinger and Elbaum
  (PGP). Verso viewed (933 x 2000 px): Hebrew letters with dots. Read, unpublished.
- **CUL T-S AS 205.186** (PGP 42291): deciphered by Elbaum (alef-tet with dots for tens and hundreds), on PGP.
- **CUL T-S K24.19, K24.23, Misc.10.60, Misc.11.91, Misc.22.218, ENA 3211.1-2**: Bohak, "Cracking the Code and Finding
  the Gold", in *Edicion de textos magicos* (CSIC, Madrid 2010), 9-23. K24.23 recto viewed (923 x 2000 px, upper half):
  lines of the alef-heavy substitution between plain Judaeo-Arabic lines, as Bohak describes.
- **CUL T-S K5.7** (PGP 42030): viewed (995 x 2000 px, upper half). Columns of ring-letter charakteres with small signs
  beside them. Magical characters, not a text cipher.
- **JTS ENA 3207.17** (PGP 10130): both sides viewed (4992 x 6666 px, reduced to 1900 px). Recto lower half: six lines
  mixing Arabic letters with ringed signs, squares and triangles, under a Judaeo-Arabic recipe that ends "... to be
  hung on her"; verso a talisman box. An amulet formula in charakteres, not a cipher.
- **CUL T-S AS 187.240** (PGP 42435): already a target, `targets/tsas187240/` (in progress), so no row. Seen again at
  native resolution (5344 x 4624 px, one side). Two observations for that folder, not tested: the plain Hebrew lines
  look like Psalm 45:2 used as a pen trial ("... lomar ani ma'asai le-melekh / leshoni 'et sofer ..."), and the dotted
  two-letter groups next to them look like the alphabet written in pairs (alef-bet, gimel-dalet, he-waw, zayin-het,
  tet-yod, kaf-lamed, mem-samekh ...), which would be a pairing key. The glyph block is one two-line formula written
  three times. The language is Hebrew, not Arabic.
- **Princeton Garrett 60L** (Jami on the Kafiya, 1806; DS15096 "a line of secret writing" on f. 1a): f. 1a viewed at
  1000 px. The line is the Seven Seals of Solomon (star, three strokes, mim, ladder ...), a talisman. Not a cipher.
- **Princeton Garrett 329Bq** (Diwan of al-Mutanabbi, 1653; DS28427 "secret writing and other inscriptions"): images
  310-318 viewed at 1000 px. Image 317 has an 8 x 8 word square of Arabic words with a row of talismanic signs under
  it. Not a cipher text.
- **Princeton Garrett 330H** (al-Khabisi on the Kafiya, 1451; DS2587 "some secret writing?"): ff. 1a-2a and 158b-159b
  and both pastedowns viewed at 1000 px: Persian verses, ownership notes, a seal, diagonal notes in a cursive hand.
  No cipher seen at that size; not checked closer.

## Key leads (alphabets and treatises, no ciphertext)

- Penn LJS 51 as a whole: about 150 solved alphabets (above).
- Princeton Garrett 52B (1700-1799): treatise on ancient, alchemical and magical alphabets with tables and Arabic
  equivalents, and "transcriptions of secret scripts used in a series of texts, such as the Rasa'il Ikhwan al-Safa'"
  (ff. 30a-b). DPUL bg257f09h, DS29452. Not viewed.
- Princeton Garrett 598Y (*Majmu'at fawa'id*, autograph of Abu al-Tayyib al-Ghazzi, 1601): "secret/magic alphabet of
  Ikhwan al-Safa'" on one folio (DS17009). Not viewed.
- Princeton Garrett 117L (1825): a "secret alphabet" among the flyleaf inscriptions (DS29113). Not viewed.
- Princeton New Series or Third Series copy of *Risalah fi kayfiyat istikhraj al-huruf al-tabi'iyah wa-al-Hindiyah
  wa-aqlam al-hukama' al-sab'ah* (catalogue id 9962618393506421): alphabets of the seven sages. Title only.
- Princeton *al-Rumuz al-mustatabah fi maktub al-kimiya' wa-al-kitabah* (ids 9978492483506421, 9978492473506421):
  alchemical signs. Title only.
- Penn LJS 409 (*Kitab al-Kashf wa-al-bayan*; *Idah al-rumuz*): alchemy with a partial code and its key on f. 3r
  (6 Nov sweep). Not paged here (OPenn budget).
- Geniza keys, unchanged from 6 Nov: CUL Or.1080 J277, Bodl. MS heb. f 102/28, JRL L 259 (PGP 30280, tables matching
  Hebrew and Coptic numerals, "worth consulting for deciphering fragments that use Coptic numerals as a cipher"),
  T-S K2.4.

## Side leads (Persian, Ottoman), one line each

- Princeton Islamic MSS Third Series 265, *Kitab-i Baleybelen* (1500-1699): dictionary and grammar of Baleybelen, the
  constructed secret language of Muhyi-yi Gulseni (Ottoman; a language, not a cipher).
- Penn catalogue: no Persian or Ottoman cipher manuscript under the terms run.

## What is left

- **vHMML Reading Room** (Arabic, Garshuni): unreachable from this network (connection reset). The largest unswept
  catalogue in this part; needs a browser or another network.
- **LoC, HathiTrust (Michigan Islamic Manuscripts), Michigan, Harvard, Columbia, Yale, UCLA**: all refused scripts on
  the first request (403, Anubis or a WAF 202). Not swept. McGill, NLM, Free Library: no searchable route found.
- **Princeton**: record pages are behind a bot check; the "secret alphabet/script/writing" hits were resolved through
  Digital Scriptorium, but the 55 "unidentified script" and 24 رموز records were judged from titles only. Garrett 330H
  deserves one look at full size. The Michaelides and Third Series documentary papers were not searched separately.
- **OPenn Muslim World** (944 items): only titles were searched; the TEI summaries were not fetched. LJS 409 not paged.
- **LJS 51**: a word-for-word check that each of the roughly 200 passages has its plaintext (I checked layout and
  formula at 480 px); a transcription of f. 106v from the master TIFF.
- **Geniza**: T-S K24.24 needs the Schaefer-Shaked and Bohak check and the Arabic side read; T-S 13J18.19 needs
  Gil-Fleischer pp. 282-285 and India Book IV B no. 41 opened, and verso line 5 viewed; ENA NS 63.10, AIU XII.41,
  T-S Ar.39.472 and T-S AS 185.121 were not opened. The Friedberg Genizah Project catalogue (registration) and the
  CUDL catalogue search (WAF) remain unswept, as on 6 Nov.
- Courtesy: Bohak, Zinger and Elbaum are working the Geniza ciphers (NS 70.1 unpublished); write to the Princeton
  Geniza Project before anything on ENA 4100.7b or K24.24 is published.
