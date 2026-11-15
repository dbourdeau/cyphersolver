# Arabic cipher sweep, part B: German-speaking, Dutch, Swiss and Nordic holdings, and Arabic papyri (15 Nov 2026)

Run by a Claude Code session (model Claude Fable 5.2), 15 Nov 2026, as part B of the Arabic-specific sweep. Aim: unread
enciphered texts in the Arabic language or script, to 1950, seen on images and vetted. Nothing solved, nothing merged or
promoted. Rows: `candidates_B.json` (4 rows, 1 with a complete `vetting` block). Scratch files and page images are outside
the repository.

## Result in one paragraph

One pre-1400 lead that meets the vetting bar: **Berlin, Ms. or. oct. 3629, f. 1a**, two lines (about 43 signs) of cipher on
the title page of a Qur'an-readings manual copied in 615 AH / 1217, reproduced and left unread by Sellheim (1976). One
catalogue-only lead with its own key (Berlin, Wetzstein I 203, autograph diwan of 1705). Two weak rows (a one-line
"Geheimschrift (?)" in Berlin Ms. or. oct. 1474; Penn Museum papyrus E16470, "Cipher (?)"). One sibling of lead 2832
closed (P.Vindob. A. P. 5584: numerals, not cipher). The printed catalogues of Gotha, Munich, Vienna, Leipzig, Hamburg,
Copenhagen and Leiden (Academy) have no ciphertext under the terms searched. Most digital portals of this area were not
reachable from this network (list below), so the manuscripts themselves were not opened.

## Routes

| Host | Result from this network |
|---|---|
| archive.org (`advancedsearch.php`, `/download/<id>/<id>_djvu.txt`, `/metadata/<id>`) | works with curl; about 75 requests. Lending-only items return 401 for the text (Grohmann, Arabische Chronologie / Arabische Papyruskunde 1966; APEL 1934 `arabicpapyriineg0000dral`) |
| digital.staatsbibliothek-berlin.de | the search page is a JavaScript application: curl gets the shell only; headless Playwright renders it (plain JS, no check). **The VOHD volumes are in it with full text**; a query with the phrase `"orientalischen Handschriften in Deutschland"` keeps the hits to that series. Oriental manuscripts themselves are not found by shelfmark in this portal |
| content.staatsbibliothek-berlin.de | works with curl: page OCR `…/dc/<PPN>-<8-digit page>.ocr.xml`, METS `…/dc/<PPN>.mets.xml`, image `…/dc/<PPN>-<page>/full/full/0/default.jpg` (full size about 2,300 x 3,200 px for the VOHD scans) |
| qalamos.net, www.qalamos.net, orient-digital.staatsbibliothek-berlin.de | **blocked**: connection reset to curl (browser UA) and 502 "upstream request failed" in Playwright, one attempt each. Not a bot check: the tunnel closes. Needs another network |
| orient-kohd.dl.uni-leipzig.de, mymssportal.dl.uni-leipzig.de, www.refaiya.uni-leipzig.de, www.rzuser.uni-heidelberg.de | unreachable (no connection) |
| www.apd.gwi.uni-muenchen.de (Arabic Papyrology Database) | answers curl, but a POST to `asearch.jsp` returns the empty form; the form driven in Playwright works. A search needs a text term: a metadata-only search (Remarks, Title, Kind) returns nothing, even for "letter". So only the translation full text was searched |
| search.onb.ac.at (Primo) | **works with curl** through the site's own guest REST service (`…/rest/v1/guestJwt/ONB`, then `…/primo-explore/v1/pnxs` with `qInclude=facet_rtype,exact,Papyrus`); about 45 requests. The page itself gave 502 in Playwright |
| data.onb.ac.at, api.onb.ac.at (IIIF), viewer.onb.ac.at | **blocked**: connection reset. No ONB image seen |
| tyche.univie.ac.at | works (PDF download) |
| collections.penn.museum | works; images at `/collections/assets/…_1600.jpg`. `www.penn.museum/collections/assets/…` returned 403 at the first request and was left |
| cryptiana.web.fc2.com | works over https (http redirects) |
| e-manuscripta.ch | **bot check** ("Verifying your browser"): blocked, not attempted further |
| dhb.thulb.uni-jena.de (Gotha / Jena) | **proof-of-work check** page: blocked |
| digitalcollections.universiteitleiden.nl | "Empty reply from server" to curl, twice: not swept |
| digitale-sammlungen.de (BSB MDZ) | search page renders in Playwright but answers "Leider ist bei der Suche ein Fehler aufgetreten": not swept |
| sru.k10plus.de | answers, but "Query feature unsupported" for the index names tried |

## Printed catalogues grepped (archive.org full text)

Pattern (case-insensitive, OCR variants): Geheimschrift, Geheimsehrift, Geheimfchrift, Chiffre, chiffr, Zifferschrift,
verschlüssel, Zeichenschrift, unbekannte/fremde Schrift, Kryptogr, geheime Schrift, geheime(n) Zeichen; for the Latin
catalogues also secret-, cryptogr-, ignot-, furtiv-, clandestin-; for the English ones cipher, cypher, crypto, secret
writing/script/alphabet/sign.

| Catalogue | Identifier(s) | Hits | Result |
|---|---|---|---|
| Ahlwardt, Verzeichniss der arabischen Handschriften, Berlin, 10 vols (Handschriften-Verzeichnisse Bd. 7-9, 16-22) | `diehandschriften07preu` … `22preu` | 7 (vols 1, 3, 9, 10) | vol. 1 no. 13, note on secret writing: **We. 203** (cipher passages, key f. 103a; row), We. 1669 f. 224a (alphabet), We. 1780, 4, f. 33b (alphabet), We. 1653, 2, f. 15b (sign-writing for magical ends), Mf. 173-175 (treatise matter). Index (vol. 10): "Geheimschrift und Zeichenschrift 13. 3047, 224a. 9734, 202. 10207". No. 2895 (WE. 120): "fremde Schriftzeichen, aus dem Arabischen verdreht, deren Tabelle am Ende des Werkes f. 65" (ff. 60-63; keyed; see key leads). Wider words: Geheim 149, geheim 71, Alphabete 26, räthselhaft 6, unverständlich 3 (all read: none is ciphertext) |
| Pertsch, Gotha: Arabic (one volume of five found), Persian, "Die orientalischen Handschriften" pts 1-2 | `diearabischenha00pertgoog`, `diepersischenha00pertgoog`, `dieorientalisch00pertgoog`, `b30096017` | 0 relevant | the other four Arabic volumes were not found on archive.org |
| Aumer, Munich | `11000375bsb` | 2 | cod. 654 f. 172 "über Geheimschrift": a chapter of Ibn Khaldun's Muqaddima (treatise) |
| Flügel, Vienna Hofbibliothek, 3 vols | `diearabischenper01vienuoft`-`03` | 1 | "Chiffre Diwani": accounting script (siyaqat), not cipher |
| Krafft, Vienna Oriental Academy | `10800301bsb` | 1 | the same accounting script "als eine nicht Jedermann geläufige Geheimschrift": not cipher |
| Vollers, Leipzig | `katalogderislam00leipgoog` | 0 | |
| Brockelmann, Hamburg | `verzeichnisderar00stad` | 0 | |
| Landauer, Strasbourg | `bub_gb_UD1FAAAAYAAJ` | 0 | |
| Mehren and others, Copenhagen, 3 vols | `codicesorientale01konguoft`-`03` | 0 relevant | (hits are "ignotus", "secretorum" in titles) |
| de Jong, Leiden, Royal Academy | `cataloguscodicum00rijkuoft` | 1 | a Dutch-language chemical book "charactere cryptographico" (not Arabic; see side leads) |
| Ahlwardt, Kurzes Verzeichniss Landberg / Glaser; Berlin poetry catalogue 1871; Kern Institute "Verzeichnis der arabischen handschriften" 1907; Lund | `kurzesverzeichni00preuuoft`, `kurzesverzeichn00staagoog`, `verzeichnissara00berlgoog`, `verzeichnisdera00univgoog`, `IA41552416_0199` | 0 | |

Not found on archive.org by title search, so not grepped: Pertsch Gotha Arabic vols 2-5, de Goeje / Dozy Leiden (the
two identifiers found return 404 for the text), Voorhoeve's Handlist, Tornberg (Uppsala), Seybold / Weisweiler
(Tübingen), Brockelmann (Breslau), Fleischer (Dresden, Leipzig Senate library).

## VOHD full text (SBB digital), terms and hits

Query form `<term> "orientalischen Handschriften in Deutschland"`: Geheimschrift 7, Zahlenschrift 3, Geheimschriften 5,
geheimer Schrift 8 (Tibetan, unrelated), verschlüsselt 1 (a date given in words, not cipher), Kryptographie 1,
Geheimalphabet 0, Kryptogramm 0, Zifferschrift 0; Geheimzeichen, Chiffre, chiffriert: the count did not render (no
relevant hit lines). "Geheimschrift arabische Handschriften" without the series phrase: 30 hits, printed books only.
The series phrase is not on every page of every volume, so this is a sample of VOHD, not the whole of it.

Arabic-script results: Sellheim, Materialien zur arabischen Literaturgeschichte I (VOHD XVII A 1, 1976) pp. 23 and 177,
and II (XVII A 2, 1987) pp. 65 and 124. Pages read in the OCR: A 1 images 50-52, 203-206, plate captions 412-467;
A 2 images 92-94, 153, 460-464. Plates viewed at full size: A 1 Tafel 55 and 59 (images 461, 465), A 2 Tafel 20-23
(images 460-463).

## Papyri: searches

- **APD**, translation full text (wildcards on): secret 22 (all "secretary", "secretly", "no secret in it"), Geheim 4
  ("im Geheimen", "Geheimnis"), cipher 2 ("undeciphered" Greek letters and a signature), unintelligible 3 (a love charm),
  Zauber 5 (P.Bad. V 160, magical signs), Geheimschrift 0, crypt 0, chiffr 0, "unknown script" 0, "secret script" 0,
  unverständlich 0, magic 0. No cipher papyrus among edited texts. Remarks / title / kind fields could not be searched alone.
- **Karabacek, PERF (1894)** (`bub_gb_RDMPAQAAMAAJ`, `papyruserzherzog00kara`): "Geheimschrift" at two numbers only:
  **844** (= A. P. 11016, lead 2832, no row here) and **850** (A. P. 5584, verso "Notizen in Geheimschrift (siehe Nr.
  844)": closed, below). At 844 Karabacek writes that the collection "besitzt mehrere Proben davon" and that he believes
  he has found the key, with three sample equations ("deine Saaten", "für alle", "vermehre deinen Antheil").
- **Grohmann, CPR III/1, Allgemeine Einführung (1924)** (`corpuspapyrorumr11unse`, `mdp.39015020864834`): the table of
  the Vienna collection has a line "Koptisch-arabische Geheimschrift" with the figures 10, 6 and 0 in its three columns
  (column heads not legible in the OCR), and note 3 says these pieces are filed under the Arabic inventory numbers.
  No inventory numbers are given.
- **ONB catalogue, Papyrus facet** (terms and totals): Geheimschrift 5 (A. P. 11016; the Sator formula G 40906; two
  Greek / Coptic magical pieces; A. P. 9911 mirror writing), "A. P. 5584" 1, unbekannte Schrift 3, unbekannter Schrift 1
  (A. P. 10024, picture of a demon), unbekannte Zeichen 3 (A. P. 7109: "zwei Zeichen unbekannter Herkunft"), Spiegelschrift
  5, andere Zeichen 77, Inhalt unbekannt 114, magische Zeichen 29, Zauberzeichen 2, unlesbar 8, unleserlich 10, Schrift
  unbekannt 24, nicht identifiziert 21, Charaktere 1, Kritzelei 1, rätselhaft 1; zero for Kryptographie, kryptographisch,
  Geheimzeichen, geheim, Chiffre, chiffriert, verschlüsselt, Kryptogramm, unentziffert, nicht entziffert, secret, cipher,
  cryptography, Zeichenschrift, Geheimalphabet, Pseudoschrift. **No second Arabic piece is catalogued as Geheimschrift**:
  Karabacek's and Grohmann's other pieces cannot be found by term.
- **Grohmann, Arabic Papyri in the Egyptian Library, vols 1-5** (archive.org texts): cipher / cryptogr / secret writing:
  0 (hits are "decipher" in the ordinary sense).
- **Grohmann, From the World of Arabic Papyri (1952)**: not on archive.org under any title searched; not seen. His
  list of papyri with secret writing is therefore **not checked**.
- Web searches (4): nothing on cipher papyri beyond the Penn Museum record and the Tyche article.
- Not reached: Heidelberg, Berlin (P.Berl.Arab.), Hamburg, Strasbourg, Michaelides (Cambridge), Khalili, Utah portals.

## Finds, best first

1. **Berlin, Ms. or. oct. 3629, f. 1a (and margin of f. 72b), 615 AH / 1217.** Row 1, complete vetting block, verdict
   open. Two lines, about 43 separate signs, on the title page of ad-Dani's at-Taisir; Sellheim I no. 12, p. 23, Tafel 55
   Abb. 69 ("Geheimschrift, 615/1217 ?"); no reading in Sellheim. Seen as the printed facsimile at 2307 x 3264 px (the
   figure about 1,200 px wide); the leaf itself not seen. Possible key in print, untested: Sellheim Abb. 92 and
   Wüstenfeld 1879. Short, and the date is that of the copy.
2. **Berlin, Wetzstein I 203 (Ahlwardt 8012), 1705.** Row 2, no vetting block (catalogue only). Autograph of extracts
   from the diwans of Darwish Mustafa al-Khaza'ini as-Sukkari; "eine Geheimschrift an einigen Stellen angewandt, wozu
   der Schlüssel f. 103a mitgetheilt ist" (Ahlwardt no. 13 note). Keyed in the volume, no reading known. Needs Qalamos.
3. **Berlin, Ms. or. oct. 1474, f. 1a.** Row 3, no vetting block. One line of about 16 signs, "Geheimschrift (?)" in
   Sellheim II no. 119, p. 65, Tafel 22 Abb. 37 (seen, 2184 x 3171 px page). May be numerals or a tally.
4. **Penn Museum E16470, papyrus.** Row 4, no vetting block. "Recto: Arabic. Verso: Cipher (?)." Both images seen, but
   the host caps the frame at 1600 x 1440 px and the fragment is about 520 px across. Neither side is clearly Arabic;
   the separate signs may be Greek-Coptic numerals or fraction signs.

## Closed or read (no row)

- **P.Vindob. A. P. 5584 (PERF 850), 9th c.**: Karabacek's "Notizen in Geheimschrift" are dinar-fraction numerals
  (circle = 1 dinar, angle = 1/2, stroke = 1/3, dots = 1/6, 1/8 …), following Y. Rāġib; edition I. Bogensperger and
  L. Reinfandt, "Textile Termini und Dinar-Zahlen auf einem arabischen Papyrus des 9. Jahrhunderts", Tyche 34 (2019)
  5-26, doi 10.25365/tyche-2019-34-2 (PDF read). The article adds that these signs do not match those of A. P. 11016
  (PERF 844), which it cites as described only: useful for lead 2832.
- **Berlin, Ms. or. oct. 3938, f. 1a**: owner's note of Muhammad ash-Shanawani al-Khatib (d. 1233/1817) "darunter
  vollständig wiederholt in Geheimschrift, und zwar in einer Zahlenschrift in der Abgad-Folge" (Sellheim I no. 49,
  p. 177, Abb. 92, seen). Plain text stands above it: read. It is a key lead (below).
- **Konya, Mevlana Museum** manuscript of 'Attar's Asrar-nama: the scribe's name in abjad numeral writing (Sellheim II
  p. 124, citing Ullmann): read by Sellheim; Persian context.
- **P.Vindob. A. P. 9911, 10937; A. Ch. 25639**: mirror writing (a basmala, an offset of a letter, a cut-paper band):
  not cipher.
- **P.Bad. V 160; P.MargoliouthMonneret II 3; ONB amulets A. Ch. 16088, 16089, A. P. 7719, A. Perg. 33**: magical signs
  and nomina barbara: not cipher.
- **Vienna Oriental Academy (Krafft) and Flügel "Chiffre Diwani"**: siyaqat accounting script.

## Key leads (alphabets and keys without ciphertext, or with the plain text beside it)

- Berlin We. 1669, f. 224a (Ahlwardt 3047): a secret alphabet, a sign under each letter, attributed to Ibn al-'Arabi.
- Berlin We. 1780, 4, f. 33b: "eine andere Art" of secret writing (Ahlwardt no. 13 note).
- Berlin WE. 120 (Ahlwardt 2895), copy of 1771: ff. 60-63 "fremde Schriftzeichen, aus dem Arabischen verdreht" with
  their table on f. 65: a keyed passage in a Sufi work. If the passages are longer than samples this is a class A lead;
  not viewed (Qalamos).
- Berlin Mf. 173-175 (Ahlwardt 9734; vol. IV ff. 202-203 "Einiges über Geheimschrift") and Ahlwardt 10207 (a work on
  writing that "handelt auch über Geheimschrift"): treatise matter.
- Berlin Ms. or. oct. 3938, f. 1a (Sellheim Abb. 92): a plain / cipher pair in the abjad numeral cipher.
- F. Wüstenfeld, "Ueber eine arabische Geheimschrift", Nachrichten der K. Gesellschaft der Wissenschaften zu
  Göttingen 1879 (cited in VOHD; not opened).
- Munich cod. arab. 654, f. 172: Ibn Khaldun on secret writing.
- Ahlwardt vol. 1, the entry just before no. 13 (number not checked): a book of invented alphabets (the Ibn Wahshiyya type), "fast alle ... müssige Erfindung".

## Side leads (not Arabic-language cipher; not followed)

- Hebrew VOHD (VI): a Book of Job "in Geheimschrift" with its key (Frankfurt; VOHD VI 1a, PPN1879047160 images 88-89); a collection of
  segullot "in Geheimschrift, z. T. arabisch" (VOHD VI, PPN1879395037 image 212): Hebrew-script, belongs to the Hebrew sweep.
- Berlin, bohairic-Arabic liturgical manuscript: f. 12r "eine Zahlenschrift" (VOHD, PPN1880623285 image 120): Coptic numerals.
- Syriac / Karshuni VOHD V: a note on a cipher that uses numerals for letters (PPN1879044919 image 154).
- Leiden, Royal Academy (de Jong catalogue): an octavo of 180 ff. in Dutch "charactere cryptographico", chemistry and
  pharmacy, with a hint to the key in the catalogue.
- Vienna, P.Vindob. Pehl. 556-574: Pahlavi papyri "Inhalt unbekannt" (script known, not cipher).
- No Persian or Ottoman Turkish cipher text was met.

## What is left

- **Qalamos** (needs another network or a browser): Ms. or. oct. 3629 ff. 1a and 72b; Wetzstein I 203 (cipher passages
  and f. 103a); WE. 120 ff. 60-65; Ms. or. oct. 1474 f. 1a; We. 1669, We. 1780, We. 1653; then its own search for
  Geheimschrift, Geheimalphabet, Chiffre, تعمية, مترجم, رموز across all German collections.
- **ONB**: images of A. P. 11016 and a way to find the other "koptisch-arabische Geheimschrift" pieces (ask the
  Papyrussammlung; Grohmann's and Karabacek's working lists).
- Grohmann, From the World of Arabic Papyri (1952) and Arabische Paläographie: his list of papyri with secret writing.
- Ullmann, Die Natur- und Geheimwissenschaften im Islam (1972) pp. 2-3 and Wüstenfeld 1879, for row 1.
- The remaining printed catalogues (Pertsch vols 2-5, de Goeje / Voorhoeve, Tornberg, Seybold / Weisweiler,
  Brockelmann Breslau, Fleischer) and the VOHD volumes page by page (the phrase search is a sample).
- Portals not reached: Leiden digital collections, BSB MDZ, Gotha, e-manuscripta / e-rara, Basel, Zürich, SLUB, Refaiya;
  the Heidelberg, Berlin, Hamburg, Strasbourg, Michaelides, Khalili and Utah papyrus portals.
- Arabic-language terms (تعمية, مترجم, المعمى, شفرة, رموز) were not run anywhere: none of the reachable search
  services indexes Arabic-script descriptions.
- Penn Museum E16470: a full-resolution scan and a papyrologist's identification.

## Scripts (kept in the session scratch directory, not in the repository)

`ias.sh` (archive.org search), `getia.sh` / `getia2.py` (full texts), `grepcat.sh`, `render.js` and `sbbs.js` (Playwright:
SBB digital search), `sbb/ocr.py` (SBB page OCR), `apd.js` (APD form), `onbq.py` / `onbabs.py` (ONB Primo guest search).
