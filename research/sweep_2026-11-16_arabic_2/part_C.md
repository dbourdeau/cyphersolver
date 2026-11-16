# Arabic cipher sweep 2, part C: printed catalogues of Arabic manuscripts (16 Nov 2026)

Run for Daniel Bourdeau by a Claude Code session (Claude Opus 5.5), "Arabic sweep 2 part C". Goal: unread enciphered
texts in the Arabic language or script (to 1950), found by searching the full text of printed manuscript catalogues,
then seen on images and vetted. Nothing solved, merged, promoted or committed. Rows: `candidates_C.json`
(**2 rows, 0 with a vetting block**: both are catalogue-only, because the image hosts showed bot checks). Scratch
files are outside the repository.

## Result in one paragraph

About 60 catalogue volumes were grepped. They produced **one new Arabic lead**: **Gotha, Pertsch no. 2507** (probably
Ms. orient. A 2507), the 13th volume of a Sirat al-Mujahidin (Dhat al-Himma / Delhemma) set copied in 1139/1727, whose
inserted end leaf carries "eine Notiz in Geheimschrift" beside a reader's note of 1178/1764-65. Part B of the 15 Nov
sweep grepped the same archive.org volume and missed it, because the OCR splits the word as "Geheim-|schrift" over a
line end. There is also **one side row from Sachau's Syriac catalogue** (Berlin Sachau 218 f. 231a: four lines of
cipher in numerals, letters and invented signs, after a Karshuni prayer; language not known). Neither could be seen:
the Gotha viewer and the Deutsche Digitale Bibliothek returned proof-of-work bot pages, and the SBB viewer is a
JavaScript application. Every other hit was a treatise, an alphabet, magical signs, accounting script (siyaq, raqam),
a coded date or a tughra ("cypher" of a sultan). **Method note for later sweeps: join hyphenated line ends before
grepping djvu text.** I re-grepped the catalogues the 15 Nov sweep had covered (Ahlwardt's 10 volumes, Flügel, Krafft,
Aumer, Vollers, Mehren, de Jong, De Slane) with the line ends joined. Gotha was the only one that changed.

## Routes

| Host | Result |
|---|---|
| archive.org `advancedsearch.php`, `metadata/<id>/files`, `download/<id>/<file>_djvu.txt` | Works (about 130 requests, 2-3 s apart). The title metadata is thin: many catalogues are not found by title or creator search |
| archive.org full-text search (`services/search/beta/page_production/?service_backend=fts`) | Works. Useful for finding catalogues by phrase (it found Sachau's Syriac catalogue and the Casey Wood catalogue) |
| Digital Scriptorium `search.digital-scriptorium.org/catalog.json?q=` and record HTML | Works. The `.json` record route returns a 500, so use the HTML page |
| Princeton figgy manifest and `iiif-cloud.princeton.edu` | Works, full resolution |
| `iiif.archive.org` (Columbia images) | Works, with occasional 504 errors |
| babel.hathitrust.org full-text search | **403**. Stopped. (The catalog.hathitrust.org API answers) |
| dhb.thulb.uni-jena.de (Gotha/Erfurt viewer) | **Proof-of-work challenge** (`/rep-pow-challenge`). Not passed |
| deutsche-digitale-bibliothek.de | **Anubis "Making sure you're not a bot"** page. Not passed |
| digitalcollections.universiteitleiden.nl | **F5 TSPD JavaScript challenge**; search URLs time out. Not passed |
| digital.staatsbibliothek-berlin.de | JavaScript (Meteor) application. Not opened; the K10plus SRU refused the query form I tried |
| qalamos.net, orient-digital.staatsbibliothek-berlin.de | No connection (curl 000) |
| www.islamicmanuscripts.info (Witkam's Leiden Inventory) | The domain is now a parking page; the inventory is gone from there |

## Catalogues grepped (archive.org djvu text, line ends joined)

Pattern: cipher, cypher, cryptogra-, secret writing/alphabet/script/characters/signs/letters, "in code", unknown
characters/script, undecipher-, "not deciphered", encipher-, cryptic, enigmatic script, mystic letters, strange
characters; écriture secrète / de convention, caractères secrets / inconnus / de convention, chiffr-, cryptograph-,
indéchiffr-, inintelligib-; Geheimschrift, Geheimzeichen, Geheimalphabet, Geheimsprache, geheime Schrift/Zeichen,
Chiffre(-schrift), Zifferschrift, unentziffert; cifra, cifrat-, scrittura segreta, caratteri segreti/ignoti; Latin
cryptograph-, steganograph-, (litteris/characteribus/notis/scriptura) arcan-/occult-/ignot-/secret-, alphabetum
mysticum; Arabic تعمية, المعمى, معمى, قلم سري, كتابة سرية, حروف مجهولة, خط غريب, مرموز, الاقلام. "decipher" counted only
when negated.

| Catalogue | Identifier | Hits | Result |
|---|---|---|---|
| Pertsch, Gotha, Arabic vol. 4 (nos. 2xxx) | `diearabischenha00pertgoog` | 2 | **no. 2507: "Notiz in Geheimschrift" (row)**; a "Geheimschreiber" (secretary) |
| Cambridge, Browne, Hand-list of the Muhammadan MSS (1900) | `handlistofmuhamm00cambuoft` | 4 | Kk. 2. 17 (Castell's English shorthand); Add. 273 (Burckhardt papers, "table of cyphers": key or numerals, see key leads); a Samaritan-Arabic fragment collection of Petermann's with "a specimen of the artificial script known in Persia as Khatt-i-sarm ... or some similar form of cryptography" (specimen, see key leads) |
| Cambridge, Browne, Supplementary Hand-list (1922) | `supplementaryhan00cambuoft` | 2 | Corpus 541, Corpus 395: siyaq accounting script (not cipher) |
| Cambridge, Browne, Persian catalogue (1896) | `catalogueofpersi00cambrich` | 5 | raqam accounting script (4); Castell's cipher notes in a Persian lexicon (English) |
| Cambridge, Palmer, Trinity College (1870) | `10800040bsb` | 4 | "mystic letters" (charms, Qur'anic letters); 1 "unknown character" = Persian script so described by Norris's executor |
| Oxford, Uri (1787) | `UriBodleianOrientalMss1` | 0 relevant | Latin "arcana" is titles only |
| Oxford, Nicoll, pars II vol. 1 (1821) | `BibliothecaeBodleianaeCodicumManuscriP2F1_201406` | 0 | |
| BM, Rosen and Forshall, pars I (Syriac and Karshuni, 1838) | `RosenAndForshall...` | 0 | Cureton and Rieu, pars II (Arabic, 1846-71), **not found** on archive.org |
| India Office, Loth (1877) | `catalogueofarabi01greauoft` | 0 | |
| India Office, Ross and Browne, two collections (1902) | `cu31924029605478` | 1 | "Hindi cyphers" = numerals in a margin |
| Mingana, Catalogue of the Mingana Collection, vols 1-3 (Syriac and Garshuni, Christian Arabic) | `MinganaCatalogueOfTheMinganaCollection.I`, `Book0187Mingana.MinganaII`, `...III` | 6 | "cryptic hints" (an apocalypse), "strange alphabetical combinations" (chapter numbers), "mystical letters" (titles): none relevant |
| Mingana Islamic Arabic (Hopwood 1985 part) | `mingana-manuscripts-volume5` | 0 | |
| Leiden, de Goeje, CCO vol. 5 | `DeGoejeCatalogus...Vol5` | 2 | "alphabetum mysticum" (magical alphabets, key material) |
| Leiden, CCO 2nd ed. vols 1-2 (1888-1907) | `india.history.resource.89866` | 0 | |
| Leiden, Specimen catalogi (1820); de Jong (1862) | `b30095992`, `cataloguscodicum00rijkuoft` | 0 / 1 | de Jong: a Dutch chemical book in cipher (side lead of the 15 Nov sweep) |
| Florence, Assemani, Mediceae Laurentianae et Palatinae (1742) | `AssemaniBML` | 0 | |
| Milan, Griffini, Ambrosiana (2 parts) | `imanoscrittiarab01/03milauoft` | 0 | Hammer's 1839 Ambrosiana catalogue not found |
| Italy, Cataloghi dei codici orientali di alcune biblioteche d'Italia (1878-1904) | `cataloghideicodiciorientalidialcun` | 1 | "inintelligibili" (a damaged leaf of a Hebrew commentary) |
| Venice, Assemani, Naniana (1787) | `catalogodecodici00asse` | 2 | talismans with "caratteri ignoti o vogliam dire Cifre" (magical); a numeral |
| Algiers, Fagnan (Catalogue général t. 18, 1893) | `cataloguegnr181893fran` | 7 | magic squares, number tables, foliation in unrecognised numerals: no cipher |
| Paris, Arsenal, Martin (9 vols, 1885-99) | `cataloguedesman01-08bibl`, `92`, `93` | 0 Arabic | every chiffr- hit in an Arabic/Oriental context was foliation; "Chiffres inexpliqués" (vol. 6 p. 202) is not Oriental |
| St Petersburg, Dorn, Bibliothèque impériale publique (1852) | `cataloguedesman00rostgoog` | 8 | tughras, numerals |
| Brill / Landberg catalogues (1883, 1886) | `cataloguedemanus00ejbruoft`, `catalogueduneco00firgoog` | 3 | déchiffrer (reading difficulties) |
| Bologna, Marsigli (1885); Diyarbakir, Mardin, Seert (Scher) | `remarquessurlesm00univuoft`, `NoticeSur...`, `Manuscrits...Mardin`, `Catalogue...Seert` | 2 | numerals |
| Tübingen (?), "Verzeichnis der arabischen Handschriften" (1907) | `verzeichnisdera00univgoog` | 0 | |
| Cairo, Fihrist al-kutub al-'arabiyya ... al-Kutubkhana al-Khidiwiyya, vols 1-7 (1888-92) | `FihristAlKutub...Vol.1`-`7Pt.2` | 6 | **The OCR is unusable** (Arabic recognised as noise). Hits: two titles on mu'amma, Tashil al-majaz ila fann al-mu'amma wa-l-alghaz, al-Nubdha al-saniyya fi ta'miyat ...: treatises. Grep of this Fihrist is not a real coverage |
| Bankipore, Calcutta Madrasah, Bombay, Salar Jung (in part), Oriental MSS Persian/Arabic/Hindustani (1916), Fraser (1742), Hyderabad, Oudh (1854) | various | 0 | |
| Sachau, Syriac MSS, Berlin (1899), 2 vols | `SachauHandschriften23` | 10 | Syriac cipher alphabets (Bardesanes, Simon, Mar Narses: key material, nos. 90, 224, 240-277, 338, 552, 706, 717, 794, 803, 807); **no. 188 = Sachau 218 f. 231a (row)**; **no. 179 = Sachau 221 f. 20b**, "zwei Zeilen in einer Geheimschrift" after a Syriac text (side lead) |
| McGill, Casey Wood collection (1927) | `McGillLibrary-124315-2581` | 0 | |
| Wüstenfeld, Das Heerwesen der Muhammedaner (1880) | `dasheerwesender00aeligoog` | 2 | siege recipes in a secret script, deciphered by Wüstenfeld (GGA Nachrichten 1879 no. 15): read |

Re-grepped with line ends joined (covered 15 Nov; no new hit): Ahlwardt, Berlin, 10 vols (`diehandschriften07`-`22preu`,
same seven hits as part B); Flügel, Vienna, 3 vols; Krafft (Vienna Academy); Aumer (Munich); Vollers (Leipzig);
Brockelmann (Hamburg); Landauer (Strasbourg); Mehren (Copenhagen, 3 vols); de Jong (Leiden Academy); De Slane (BnF).

Not found on archive.org with full text, so not grepped: Cureton and Rieu (BM pars II); Pusey (Bodleian, 1835);
Beeston; Palmer (King's); Arberry (Chester Beatty, 8 vols); Mingana (Rylands, 1934); Blochet (BnF nouvelles
acquisitions); Vajda; Voorhoeve (Leiden handlist); de Goeje and Houtsma CCO vols 1-4 and 6 (1851-77); Hammer
(Ambrosiana, 1839); Naples; Karatay (Topkapı); Süleymaniye Defter; Hitti, Faris and Abd al-Malik (Garrett, 1938; the
Mach handlist `bwb_T5-CVS-488` is lending-only, no text); Nemoy (Yale); Rosen (Musée asiatique; Institut des langues
orientales); Ewald and Seybold (Tübingen); Tornberg and Zetterstéen (Uppsala); Pertsch Gotha Arabic vols 1-3 and 5;
any Michigan or Harvard Arabic catalogue.

## Digital Scriptorium terms (all collections)

"secret writing" 3, cryptogram 0, "secret script" 0, "secret alphabet" 2, cryptic 3, cryptography 2, "unidentified
script" 1, "in code" 3, undeciphered 3, cypher 2, "secret characters" 0, "secret letters" 1, enciphered 0. The Arabic
hits not already treated by the 15 Nov part A:

- **Princeton Garrett 471H, f. 57b** (copied Jumada I 923 / June 1517; DS2759, "a line of secret letters, a paragraph
  on using secret letters and two tughras"). Seen at full resolution (canvas 4,949 x 7,226 px; the top band at
  2,000 px). It is a basmala-like line of letters mixed with stroke clusters (three-stroke "ااا" groups) and a boxed
  sign, followed by a clear Arabic paragraph saying that one should write these letters on the back of a book,
  because God gave each thing a property (khassiyya) and the property of these letters helps the student of
  learning. A protective talismanic formula, explained on the leaf. **Closed: magical, not a cipher.**
- **Columbia MS Or 34** (algebra, copied by Muhammad 'Ashiq at Lahore, 18th c.; DS6699): the cataloguer says the year
  of the colophon (f. 49v) is "in code, undeciphered". A coded year in a colophon, not a text cipher. Pages up to
  f. 49r were viewed (iiif.archive.org, 1,600 px); f. 49v was not reached (504 errors). Closed as a date, not a lead;
  someone may want to read the year.
- Garrett 5657Y and 1491Y ("cypher"): the Sultan's imperial cypher, i.e. the tughra, in an owner's title. Not leads.

## Finds

1. **Gotha, Pertsch no. 2507** (row 0). Catalogue only. Pertsch 1883, vol. 4, p. 373, quoted in the row. Not seen:
   the Gotha viewer and DDB both answered with a proof-of-work bot page. Dedup: known.py (Gotha, 2507, Dhat al-Himma,
   Delhemma) shows no Arabic hit; DECODE search (Gotha, Dhat al-Himma) 0 records; Tomokiyo's snapshot has no Arabic
   or Gotha item; two web searches (shelfmark plus romance; Pertsch 2507 plus Geheimschrift) found nothing. No
   vetting block, because the leaf was not seen.
2. **Berlin, Sachau 218, f. 231a** (row 1). Catalogue only. Syriac-Karshuni miscellany from Midyat; four lines of
   cipher. Its language is not known, so it belongs to this sweep only if the cipher turns out to be Karshuni Arabic.
   known.py and DECODE: nothing; one web search: nothing.

No item dated before 1400 was found, so nothing was sent to the main session.

## Closed or not a lead

- Princeton Garrett 471H f. 57b: protective formula with its explanation (above).
- Columbia MS Or 34: coded colophon year (above).
- Cambridge Corpus 541, Corpus 395; Browne Persian catalogue raqam items; Vienna "Chiffre Diwani"; Krafft's K'irma:
  accounting scripts.
- Munich cod. 654 f. 172; Wüstenfeld 1879/1880 (siege recipes): treatise matter / deciphered in print.
- Leiden CCO vol. 5 "alphabetum mysticum"; Naniana talismans "caratteri ignoti ... Cifre"; Algiers magic squares;
  Trinity "mystic letters": magical.
- Dar al-Kutub Fihrist titles on mu'amma and ta'miya: treatises.
- Kk. 2. 17 and the Persian lexicon in Cambridge: Edmund Castell's English shorthand/cipher, out of scope.

## Key leads

- **Cambridge University Library, Add. 273** (Burckhardt papers, Aleppo and Syria, c. 1805-12): among 45 pieces, a
  "table of cyphers" (Browne 1900, no. 1501). Probably a numeral or siyaq table; not seen (CUDL was 403 on 15 Nov).
- **Cambridge, Petermann's Samaritan fragments** (Browne 1900, no. 1531; the shelfmark reads "Add. 1899" in the OCR,
  not checked): the sixth fragment carries "a specimen of the artificial script known in Persia as Khatt-i-sarm ... or
  some similar form of cryptography", in pencil, beside Samaritan and Rabbinic lines.
- **Berlin, Sachau's Syriac cipher alphabets** (Bardesanes, Simon, Mar Narses and others): Sachau nos. 90 (Sachau 116,
  f. 1a), 224 (Sachau 93, f. 75b) and pp. 338, 552, 706, 717, 794, 803, 807 of his catalogue. They are the keys to try
  on Sachau 218 f. 231a and Sachau 221 f. 20b.
- Leiden CCO vol. 5: alphabetum mysticum tables in two Sufi/occult codices.

## Side leads (not Arabic, or language unknown; one line each)

- Berlin, Sachau 221 (Sachau 1899 no. 179, Tur Abdin miscellany), f. 20b: "zwei Zeilen in einer Geheimschrift" after
  the canons of Dionysius bar Salibi (Syriac).
- Berlin, Sachau 92 (Sachau 1899 no. 168, the nearest preceding entry heading in the OCR; Karshuni): "einige Zeichen
  einer Chiffreschrift, das Alphabet, Federproben" on the left flyleaf: alphabet plus a few signs, key-like.

## What is left

- **See the Gotha leaf**: a person in a browser past the proof-of-work page on dhb.thulb.uni-jena.de, or a scan
  request to the Forschungsbibliothek Gotha (Ms. orient. A 2507, last two leaves). With the image, the row can be
  vetted or closed.
- **See Sachau 218 f. 231a** (SBB digital collections, a JavaScript page: try headless Playwright, which this pass did
  not try, or find the PPN through Stabikat).
- **Catalogues not on archive.org as text** (list above), above all Cureton and Rieu, Arberry's Chester Beatty
  handlist, Voorhoeve, Hitti's Garrett catalogue, Karatay and Pertsch Gotha vols 1-3 and 5. HathiTrust full text (403
  here) and Google Books would cover several of them.
- **The Dar al-Kutub Fihrist** needs a better OCR (or the Arabic catalogues on al-Maktaba al-Shamela / waqfeya) before
  an Arabic-term grep means anything.
- **Leiden** (digital collections behind an F5 challenge) and Witkam's Inventory (the islamicmanuscripts.info domain
  has lapsed; Brill's printed edition was not looked for).
- Columbia MS Or 34 f. 49v: read the coded year if anyone wants it.
