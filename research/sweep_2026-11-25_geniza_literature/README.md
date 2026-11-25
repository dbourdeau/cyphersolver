# Cairo Geniza and medieval Hebrew/Arabic cryptography: literature survey (24 Nov 2026)

Literature survey only: web search and fetch, no image work, no candidates. Folder is dated 25 Nov to match the brief; the
searches were run on 24 Nov 2026. Scope: every cipher, secret script, coded letter or cryptic document from the Cairo Geniza
that scholarship mentions, plus Judaeo-Arabic, Hebrew and Arabic cryptography 1000-1400 in general, with the status of each
(read, partly read, published, open). Nothing here is in `catalogue.json`, `leads.json` or `targets/`. No `candidates.json`:
no item was seen on an image in this sweep, so none meets the vetting bar here.

What was already tabulated and is not repeated in full: `research/sweep_2026-11_hebrew/README.md` (Geniza table, the Bohak
family, negatives), `research/sweep_2026-11-15_arabic/part_A.md` (Geniza image checks, LJS 51). The folder named in the brief,
`research/sweep_2026-11-23_genizah_tables/`, **does not exist in this checkout** (pulled `origin/main` at 56daa14fe9); the
other two were read. Where this sweep disagrees with them it says so (section 6).

How to read the Source column: every factual claim carries the page it came from. "Snippet" means the fact comes from a
search-result summary and the page itself was not opened or could not be opened (marked). "not found" means searched for and
absent, not "does not exist".

## 1. Result in one paragraph

Published scholarship on Geniza ciphers is thin and has not moved much since Bohak 2010: one article (Bohak, "Cracking the
Code and Finding the Gold", 2010), one Cambridge blog Q&A (Elbaum, 22 Jun 2022, updated 16 May 2025), the Princeton Geniza
Project (PGP) catalogue notes, and one forthcoming edition (T-S NS 70.1, Bohak, Zinger, Elbaum). No Cryptologia, HistoCrypt
or Lasry/Megyesi/Knight paper on a Geniza or Judaeo-Arabic cipher was found. PGP carries 13 documents under the tag `cipher`
(checked live, 24 Nov 2026). Of the Geniza items that are real ciphertexts, the unread ones are few: **T-S AS 187.240**,
**T-S K24.24**, **ENA 4100.7b** (lines 7-12), the **Coptic-numeral passages of T-S 13J18.19** (Gil and Fleischer read two
words, third open), and the unlocated **India Book Coptic-numeral "code"** that Amir Ashur mentions. Everything else is read,
a key, a pen trial or a fiscal sign. On the Arabic side the scholarship is about **treatises** (Ibn al-Durayhim, Ibn
Adlan, Qalqashandi, al-Kindi) and **alphabet books** (Ibn Wahshiyya, LJS 51), not about surviving enciphered letters
1000-1400. The few Arabic-script ciphertexts that scholarship names are an encrypted Qur'an (SOAS MS 12217, read by
D'Ottone, date not found) and Ismaili/Bohra secret-script copies (IIS MS 1499, easy by comparison with other copies).

## 2. PGP `cipher` tag: the 13 documents (live, 24 Nov 2026)

Source: <https://geniza.princeton.edu/en/documents/?q=tag%3A%22cipher%22> (curl). Descriptions are PGP's.

| # | Shelfmark (PGPID) | What PGP says | Status | Source of status |
|---|---|---|---|---|
| 1 | Bodl. MS heb. f 102/28 (19549) | tribes of Israel in a cipher on Greek/Coptic numeral values | key-type specimen | PGP list above |
| 2 | T-S AS 187.240 (42435) | pen-trial bifolio with a cipher section, "merits examination (might be solvable based on the surrounding formulae)"; in PGP since 2026 | **open** | PGP list above; no edition found |
| 3 | T-S K5.7 (42030) | magical characteres "in an indecipherable cipher" (from CUDL); in PGP since 2026 | charakteres; same group as Bohak's per PGP 32681 | <https://geniza.princeton.edu/en/documents/32681/> |
| 4 | T-S NS 70.1 verso (26158) | Judaeo-Arabic letter in a cipher; recto an Arabic-script medical prescription | **read** (Bohak, 2025), **unpublished** | <https://geniza.princeton.edu/documents/26158> |
| 5 | T-S NS 297.254 (24835) | bifolio of accounts in Arabic script and Greek/Coptic numerals | numerals in accounts, not a secret writing | PGP list above |
| 6 | T-S AS 205.186 (42291) | letter fragment, mostly a Hebrew-script cipher alef-tet with one dot = x10, two dots = x100; tags `bialphabetic`, `cipher`; "identified and deciphered by Alan Elbaum" | **read** (trivial); content "needs further study" | <https://geniza.princeton.edu/documents/42291/> (via search snippet) |
| 7 | T-S K24.19 (32681) | Hebrew spell in cipher: Khatun daughter of Qatzur adjures the jinn to reveal hidden gold | **read and published** (Bohak 2010) | <https://geniza.princeton.edu/en/documents/32681/> |
| 8 | T-S K24.23 (32686) | Judaeo-Arabic formulary "written in part with a cipher" (from FGP) | same cipher as K24.19 per Bohak; titles and formulae | PGP list above |
| 9 | T-S K24.24 (33913) | "Magical fragment, perhaps. Unidentified alphabet or cipher." Language and script unidentified; one related document; no scholarship | **open** | <https://geniza.princeton.edu/en/documents/33913/> |
| 10 | T-S Misc.28.232 (23415) | Arabic business letter; tagged `cipher` because of the *adda* ("paid") mark at top left | fiscal sign, not a cipher text | <https://geniza.princeton.edu/en/documents/23415/> |
| 11 | CUL Or.1080 J277 (34004) | verso: three keys to Hebrew ciphers: (1) same as Bodl. MS heb. f 102/28, (2) atbash, (3) a pangram mnemonic *haqets 'atsel dayk ...*; recto praises of God, syrup prescription | **keys** | <https://geniza.princeton.edu/en/documents/34004/> |
| 12 | ENA 4100.7b (11951) | son in Qus to his mother; Judaeo-Arabic with lines 7-12 in a cipher "noticed by OZ"; verso another letter, "Needs examination/decipherment"; JTS images CC0; tags `cipher`, `to examine` | **open** | <https://geniza.princeton.edu/en/documents/11951/> |
| 13 | T-S NS J479 (8804) | folio of jottings in an "idiosyncratic (unique?) cipher"; dating no earlier than mid-13th c. (al-Busiri, 1213-95); tags `cipher`, `sex`, `sufism`; one Select Bibliography entry, one Discussion | **partly read** (see section 6) | <https://geniza.princeton.edu/en/documents/8804> |

## 3. Master table: Geniza and other Hebrew-script items

Rank column: A = unread, real ciphertext, worth attacking; B = unread but short or doubtful; C = read or published; D = key
or not a cipher. Details of images come from the earlier sweeps (CUDL IIIF by curl); this sweep did not open images.

| Rk | Item | Date | Language / system | Length | Who read it, where published | Image online | Unread remainder |
|---|---|---|---|---|---|---|---|
| A | **T-S AS 187.240** (CUL; PGP 42435) | undated; paper | Hebrew; dotted letter groups plus a glyph block (earlier sweeps) | bifolio, about 30-40 short lines | nobody; no scholarship record in PGP (0) | CUDL IIIF `MS-TS-AS-00187-00240-000-0000{1,2}.jp2` (`research/sweep_2026-11_hebrew/README.md`); PGP page, reproduction via genizah@lib.cam.ac.uk | all. Already `targets/tsas187240/` (Status: in progress) |
| A | **T-S K24.24** (CUL; PGP 33913) | undated | "unidentified alphabet or cipher", magic | fragment, 2 images (1r, 1v) | nobody; 0 bibliography; 1 related document (not opened) | PGP page (CUL images) | all |
| A | **ENA 4100.7b** lines 7-12 (JTS; PGP 11951) | undated | Judaeo-Arabic letter, cipher lines "probably also Judaeo-Arabic" | 6 lines; verso another letter | nobody; one PGP transcription present (the non-cipher part) | JTS images, CC0 (PGP page) | cipher lines, and the verso letter ("needs decipherment"). Already `targets/ena4100/` |
| A | **T-S 13J18.19** (CUL; PGP 9097) | after 1 Nisan 1139 | Judaeo-Arabic letter, Yitzhaq b. Avraham Ibn Ezra (Spain) to Halfon b. Netanel; Greek/Coptic numerals recto ll. 11-12, verso l. 5 "probably standing in for Hebrew letters; substitution method not determined" | 3 passages, about 15-20 signs | Gil and Fleischer 2001 (the book on Judah Halevi and his circle; PGP's English rendering of the title is garbled), pp. 282-285: first two words ("the wicked" and "tarakh") by two different methods, third open; editor (Friedman) leaves it unresolved. Edition: Goitein, Friedman, Ashur, *India Book 4: Halfon the Traveling Merchant Scholar* (Ben Zvi Institute, 2013), vol. 4B | CUDL; PGP tags `IB4`, `India Book` | the third passage; whether one key fits all three; verso numerals uncertain (editor's "1s look like 4s, the 60 doubtful, one might be 900") |
| A? | **India Book Coptic-numeral "code"** | 11th-12th c. | merchants' letters, Coptic numerals "to create a secret code that hasn't yet been cracked" (Ashur, as reported by Elbaum) | **not found** (no shelfmark given) | nobody | not located | unlocated. Worth one targeted PGP pass (tags `India Book`, language "Greek/Coptic Numerals"); see section 8 |
| A? | **Zinger's cipher letter** ("a letter in Arabic and Judaeo-Arabic with a portion in an incomprehensible cipher", "nearly every word beginning with alef") | not given | Arabic / Judaeo-Arabic | not given | not published (not found) | not given | **Probably ENA 4100.7b** (PGP: "noticed by OZ", 6 cipher lines), unconfirmed; the Q&A gives no shelfmark |
| C | **T-S NS 70.1 verso** (CUL; PGP 26158) | undated | Judaeo-Arabic letter in cipher | one letter | cracked by Gideon Bohak in 2025; to be published by Bohak, Oded Zinger, Alan Elbaum (PGP); **no publication found** | PGP images 1r/1v (CUL) | nothing known to be unread; the key and text are unpublished. Do not duplicate; ask or wait |
| C | **T-S AS 205.186** | undated | Judaeo-Arabic, alef-tet with dots x10/x100 | letter fragment, damaged | Elbaum (PGP) | CUDL | content of the damaged fragment "needs further study" |
| C | **Bohak cipher family**: T-S K24.19 (continuous text), K24.23, Misc.10.60, Misc.11.91, Misc.22.218, ENA 3211.1-2, T-S K5.7 (PGP says similar) and JRL B 5652 (Manchester catalogue note, snippet) | 11th c. by script (Bohak, from earlier sweep) | substitution cipher, Hebrew letters, "not attested elsewhere", about 20 signs read as an alphabet; Bohak suggests a possible non-Jewish, Islamic-cryptography origin (search snippet of the article abstract) | titles, formulae, one spell | Bohak, "Cracking the Code and Finding the Gold: A Dream Request from the Cairo Genizah", in Álvarez-Pedrosa Núñez and Torallas Tovar (eds.), *Edición de textos mágicos de la Antigüedad y de la Edad Media* (Madrid: CSIC, 2010), 9-23. PDF: <https://www.academia.edu/37186516/> (403 to WebFetch; page 15-16 read in the 6 Nov sweep) | CUDL; Manchester Luna (lunatest hosts, snippet) | JRL B 5652 is listed by PGP as a letter (32630: "Very rudimentary hand", waṣiyya) while the Manchester catalogue says its fragments 1-2 carry the same cipher; the two descriptions do not obviously refer to the same leaves (not resolved) |
| C | **T-S NS J479** | after c. 1250 (al-Busiri) | Judaeo-Arabic in a unique ~22-sign cipher; Arabic petition lines; two Burda verses; sexual passages; signature *al-faqir Ishaq al-yahudi*; ends "all of this is lies" | one folio, both sides | Alan Elbaum, "Q&A Wednesday: Secret codes and erotic prose", Cambridge Genizah Research Unit blog, 22 Jun 2022, updated 16 May 2025: partial alphabet mapping plus annotated image; he doubts it is a simple substitution (almost every word begins with alef) | blog images (`.../2025/05/t-s_ns_j479r.jpg`, `..._annotated.png`); CUDL | the full decipherment and an edition are not published (see section 6 for the disagreement between sweeps) |
| C | **LJS 51** (Penn) | possibly 15th c., Syria | Arabic; Mamluk secretary's cipher verses with solutions | 106 leaves | Penn catalogue (Digital Scriptorium DS738); f. 106v has no plaintext (earlier sweep) | OPenn | f. 106v |
| D | **CUL Or.1080 J277**, **Bodl. MS heb. f 102/28** | undated | key lists (Coptic-numeral cipher, atbash, pangram) | keys | PGP only | CUDL / Bodleian | candidate keys for 13J18.19 |
| D | **T-S K2.4** (PGP 29394) | 22 May 1135 | Judaeo-Arabic; instructions on ciphers (atbash, term *qabala*) | keys | from the 6 Nov sweep (PGP description) | CUDL | oldest dated Hebrew-script cipher key found |
| D | Primer exercises: atbash, albam, *'ayiq bekar* in children's alphabet primers, e.g. T-S K5.4, K5.14, K5.49 | 11th-12th c. (Michaels: various) | letter-pair exercises | alphabets | Marc Michaels, "Manuscripts from the Cairo Genizah as Educative Tools", *Manuscript and Text Cultures* 3/1 (2024), p. 66-67 (DOI 10.56004/v3.1mm; read from the PDF <https://mtc-journal.org/index.php/mtc/article/download/61/79>); he calls them "fundamentally ciphers" and finds their presence in primers odd; cites Olszowy-Schlanger 2003 pp. 60-63 on atbash only | CUDL | none (exercises) |
| D | Atbash colophon names: Joseph b. Nimorad, Nehemiah fragment, 903/4 CE (CUDL MS-TS-NS-00246-00026-00002; Cambridge FOTM gives the shelfmark as T-S NS 324.26.2, a discrepancy not resolved); a Geniza colophon of Av 4876 AM (1116 CE) with Halfon b. Joseph in atbash (search snippet only) | 904, 1116 | atbash on one name | a name | catalogue/FOTM notes | CUDL (the page itself gave 403 to WebFetch) | none |
| D | **T-S Ar.35.109** | 11th c. hand (Engel) | Greek letter names, syllabary and abecedaries in Hebrew script, with permutations of consonants and vowels | bifolio | Julia Krivoruchko, Cambridge Fragment of the Month 2023 (<https://www.lib.cam.ac.uk/node/1360391>, snippet); Bohak transcribed it | CUDL | not a cipher: a manual for reading Greek |
| D | **T-S NS 297.254**, **T-S AS 177.466**, **T-S NS 305.156**, **T-S Ar.38.94**, **JRL Genizah Ar. 180**, **ENA 3934.5**, T-S Misc.28.232 | 11th-12th c. | "cipher" = the Arabic-script opening sign (*adda*, *yudfa'*) or Greek/Coptic numeral accounts | fiscal | PGP | CUDL | none |
| D | **T-S K24.37** (PGP 32699) | undated | "mysterious writing ... might be mirror-image Hebrew script. Needs examination." No cipher claimed | fragment | nobody | PGP | probably a mirror imprint; not a cipher lead |
| D | **AIU XII.41** (PGP) | undated | Arabic alphabet, partly mirrored, "a cross and cryptic symbols on verso" (PGP list, snippet) | unknown | nobody | AIU/PGP | not opened by anyone in these sweeps; low value |
| D | T-S AS 178.169 | undated | list pairing Arabic phrases with nonsense words | list | 6 Nov sweep | CUDL | code list, Arabic script |
| D | Halfon letters (F 1908.44U, Bodl. heb. e 94/30) and 13J18.19 code names ("the elephant") | 1139 | nomenclator-style code names | letters | India Book 4 | CUDL, Bodleian | not ciphertext |

## 4. Non-Geniza Hebrew-script and Samaritan material (1000-1400 and neighbours)

| Item | Status | Source |
|---|---|---|
| Samaritan *tashqil* cryptograms (scribe's name in a letter grid; Abisha scroll) | short, read; the disputed words are guessed, not read | <https://library.biblicalarchaeology.org/endnote/endnote-19-the-abisha-scroll-3000-years-old/> (snippet) |
| Dead Sea Scrolls Cryptic A/B | out of period; Cryptic B reading claimed in 2025 by one scholar (17 of 22 letters per the 6 Nov sweep); unconfirmed | <https://greekreporter.com/2025/12/13/millennia-old-unknown-alphabet-dead-sea-scrolls-deciphered/> (snippet) |
| Karaite / Firkovich secret script | **not found**; a search for a cipher in the Firkovich collection returned nothing relevant | search 24 Nov |
| Ashkenazi Hasidei cipher alphabets, Eleazar of Worms | letter permutation (Idel), not preserved ciphertext; **not found** as a text | Universalis and seforimblog snippets |
| Ibn Ezra / Judah Halevi encrypted verses | **not found**: riddles (Halevi about 50, some unsolved) and letter mysticism (*Sefer ha-Shem*), no cipher. Ibn Ezra's four-quiescent-letters riddle: Itzhaki and del Valle | <https://jstudies.huji.ac.il/sites/default/files/jstudies/files/sifrut_-_31_-_press_-_04_-_golden.pdf> (snippet); <https://plato.stanford.edu/archives/spr2017/entries/ibn-ezra/> |
| Maimonides circle code names, "secret writing" | **not found**: only the archival-sign discussion (Goitein on a mark that could be a code for the keepers of the Qusayr archive, per a PGP-related paper, snippet) and the Halfon code names above | search 24 Nov |
| Goitein, *A Mediterranean Society*, on cipher letters | **not found** by search; the volumes were not read here. Goitein's *Letters of Medieval Jewish Traders* has no cipher in the search results. Needs the book, or a PGP full-text pass | search 24 Nov |
| Hebrew cipher in Christian chancery | **not found** (6 Nov sweep) | `research/sweep_2026-11_hebrew/README.md` |
| Zafenat Pane'ah, Abraham Menahem Rapa of Porto | 16th c. treatise on cryptography; out of period | <https://seforimblog.com/2021/03/abraham-menahem-ben-jacob-ha-kohen-rapa-mi-porto-rapaport-ashkenazi-a-renaissance-rabbi-of-interest/> (snippet) |
| *Cryptologia* 37:4 (2013), 338-344, "Atbah-Type Ciphers in the Christian Orient and Numerical Rules in the Construction of Christian Substitution Ciphers" | Greek, Coptic, Syriac counterparts of atbah; author not retrieved | <https://dl.acm.org/doi/10.5555/2535512.2535517> (403; snippet) |
| Bohak, "Magic ... Genizah"; Schäfer and Shaked, *Magische Texte aus der Kairoer Geniza* (3 vols) | the volumes were not found online; no cipher claim located in them. Needs the books | search 24 Nov |

Genizah blog posts that came up and are **not** about ciphers: "More about less: A New Shorthand Targum Manuscript" (8 Feb
2024: a vocalisation sign used "purely as a cipher"), "Targumic poems of the Pentateuch" (18 Nov 2021: sidra sign marks),
"'Coptic' numerals and Genizah studies" (Magdalen M. Connolly, 2 Jun 2021, updated 17 Jul 2025: the Unit will use *ḥurūf
al-zimām*; cites Chrisomalis 2010, Gacek 2009, Fournet 2020; says nothing of numerals as a secret code; the shelfmarks
shown are T-S AS 145.45, NS 306.115, Misc. 8.99, NS 98.11). URLs: `https://genizahfragments.lib.cam.ac.uk/2021/06/02/coptic-numerals-and-genizah-studies/`
and the others under the same host.

## 5. Arabic-language and Arabic-script cryptology 1000-1400

| Item | Date | What it is | Status | Source |
|---|---|---|---|---|
| Qalqashandi, *Subh al-a'sha* (completed 1412), cipher chapter, drawing on Ibn al-Durayhim (1312-61) | 1412 | chancery manual with a cryptology section: ciphers, a multi-substitution cipher, cryptanalysis with letter-frequency tables | treatise, printed (Cairo editions); volume number **not confirmed** (brief says vol. 9; the pages found do not say). Bosworth, "The section on codes and their decipherment in Qalqashandi's Subh al-a'sha", *Journal of Semitic Studies* 8 (1963), 24-26 | <https://en.wikipedia.org/wiki/Al-Qalqashandi> (snippet; Bosworth reference taken from a Cambridge reference list in the same search) |
| Ibn al-Durayhim, *Miftah al-kunuz fi idah al-marmuz* | c. 1350 | treatise, once thought lost; found in Istanbul, Süleymaniye, with more than 15 other Arabic cryptology manuscripts (9th-15th c.), edited by Mrayati and team, in Arabic 1987 | published; treatise not ciphertext | <https://muslimheritage.com/arab-origins-of-cryptology/> (snippet) |
| Al-Kadi, "Origins of Cryptology: The Arab Contributions", *Cryptologia* 16/2 (1992), 97-126 | | survey | published | <https://membres-ljk.imag.fr/Bernard.Ycart/mel/hm/AlKadi_cryptology.pdf> (listed) |
| Mrayati, Meer Alam, at-Tayyan (eds.), *Arabic Origins of Cryptology*, vols 1-4 (incl. Ibn 'Adlan, Ibn Dunaynir, al-Kindi) | 2002-2004 | editions with English translation | published (vol. 4 = Ibn Dunaynir, per a listing) | <https://en.wikipedia.org/wiki/Ibn_Adlan> (snippet) |
| Schwartz, "Charting Arabic Cryptology's Evolution", *Cryptologia* 33/4 (2009), 297-304 | | links the phases of the Istanbul treatises to the bureaucratic trends of the regimes; suggests espionage use | published; the article was not read | dblp / typeset.io listing (snippet) |
| Ibn Wahshiyya (attributed), *Shawq al-mustaham* | attribution doubtful; dated c. 1022-23 in one source | cipher alphabets for magic formulas; Hammer-Purgstall, *Ancient Alphabets and Hieroglyphic Characters Explained* (1806) | alphabet book, published; Hämeen-Anttila, *The Last Pagans of Iraq* (Brill 2006) is the study cited | <https://www.Wikipedia.com/wiki/Ibn_Wahshiyya> (snippet) |
| **LJS 51** (Penn) | possibly 15th c., Syria | Mamluk secretary's cipher verses, about 150 alphabets, solved passages | f. 106v unsolved | <https://search.digital-scriptorium.org/catalog/DS738>; OPenn <https://openn.library.upenn.edu/Data/0001/html/ljs51.html>; facsimile <https://repository.upenn.edu/sims_ebooks/13> |
| **SOAS MS 12217**, Qur'an fragment (Surahs 2:88-6:89, lacunae) in a peculiar cipher script; Marsden bequest | date **not found** (SOAS gives none) | D'Ottone Rambach, "The Qur'an Encrypted: A Unique Qur'anic Manuscript in Cipher", *Journal of Islamic Manuscripts* 11/2 (2020), 133-176, DOI 10.1163/1878464X-01102001, said to decode it (abstract: "the opportunity to decode", dating and localizing the codex); ring-letter (Brillenbuchstaben) tradition | read in the article (abstract only seen; the PDF is on academia, "if interested please email me") | <https://research.uniroma1.it/en/node/26696> (403 to WebFetch; snippet); shelfmark from a garbled abstract and a SOAS search hit (<https://library.soas.ac.uk/Record/ms_12217-item1>, host did not resolve). The shelfmark link to the article is not confirmed |
| Coded Qur'an associated with Babur Shah, Mashhad | not found | D'Ottone, Journal of Islamic Manuscripts 2025 | not examined; snippet only; Timurid/Mughal, outside 1000-1400 probably | search 24 Nov |
| IIS MS 1499, *Kanz al-walad* (al-Hamidi, d. 1162), copy in an invented script | flyleaf: 1294-1304 (cataloguer doubts) | "a straightforward cipher", easy to crack by comparison with other copies; no key given | **no image online** ("No image available") | <https://special-collections.iis.ac.uk/Details/manuscripts/45> |
| Ismaili and Bohra secret scripts, Akkerman, *A Neo-Fatimid Treasury of Books* (Edinburgh UP, 2023), ch. 6 "Script and the Language of Secrecy", "Khizana Scripts" | modern Bohra practice on Fatimid books | open access | published; chapter not read here | <https://library.oapen.org/handle/20.500.12657/60230> (snippet) |
| Fatimid or Ayyubid chancery ciphers, surviving enciphered letters | | **not found**: searches on Mamluk/Ayyubid chancery returned ordinary diplomatics (Bauden, Dekkiche) and the Fatimid fiscal *nuqila* sign, which is an archival sign, not a cipher | no ciphertext identified | <https://orbi.uliege.be/bitstream/2268/201052/1/9789004384620_Bauden_Ch1_offprint.pdf> (snippet) |
| Ottoman diplomatic ciphers from 1797 | out of period | Cryptologia 46/6 | published | <https://www.tandfonline.com/doi/abs/10.1080/01611194.2021.1919943> |
| Bodleian miniature Qur'an, hidden English eulogy of More's circle, 1531 | out of period | read by Cornelius Berthold and Claudia Colini by frequency analysis; published in *Moreana* (volume not given) | read | <https://www.csmc.uni-hamburg.de/news/2023-05-31-secret-messages.html> |
| Borg cipher (Aldarrab, Knight, Megyesi) and the DECRYPT survey, *Cryptologia* 2020, section "A page in Arabic?" | 17th c.; Arabic only on page one | not a medieval Arabic cipher | read | <https://en.wikipedia.org/wiki/Borg_cipher> |
| Merchant argot and cryptic phrases (Judaeo-Arabic "coded expressions", the *DRKY* puzzle in AIU XII.116 / ENA NS 48.2) | 1130s | an unclear word, not a cipher | not cipher | <https://ora.ox.ac.uk/objects/uuid:2c513b7c-1d95-45e6-aa6b-bea301fd1698/files/rxp68kj77c> (snippet) |

## 6. Where the sources disagree (cross-check list for the image sweep)

1. **T-S NS J479: "not read" or "read"?** The Hebrew sweep (6 Nov) says unread, Elbaum's mapping unpublished. The Arabic part A
   (15 Nov) says read, because Elbaum published an annotated image. The Q&A (as fetched here) says: about 22 symbols assigned
   to the Hebrew alphabet, some letters with several glyphs, most words begin with alef so it is probably not a plain
   substitution, the writer "may have been working out" the alphabet, contents summarised (petition, two Burda verses,
   erotic vocabulary, "all of this is lies"). PGP gives no transcription. **Honest status: partly read; mapping and gist
   published as a blog image and summary, no edition, no full text.** A target on it would still need a first full
   transcription.
2. **Is Zinger's letter ENA 4100.7b?** PGP says the cipher lines were "noticed by OZ" (Oded Zinger); the blog says Zinger found
   "a letter in Arabic and Judaeo-Arabic with a portion in an incomprehensible cipher" where nearly every word begins with
   alef. Same man, same description of the object; not confirmed. If true, ENA 4100.7b's cipher shares the alef-initial
   property noted for J479, so the two should be tried against each other.
3. **JRL B 5652**: Manchester's catalogue note (via a Luna test host, snippet) says its two fragments carry the Bohak
   cipher; the PGP record 32630 describes a Judaeo-Arabic letter with a rudimentary hand. Check which leaves.
4. **Shelfmark of the Nimorad colophon**: CUDL ID `MS-TS-NS-00246-00026-00002` against Cambridge FOTM "T-S NS 324.26.2".
5. **PGP's `cipher` tag is partly fiscal**: five of the 13 are *adda*/numeral signs or key lists; do not count them as ciphertexts.
6. T-S K5.7: PGP/CUDL "indecipherable cipher"; the 15 Nov Arabic part A viewed it and called it ring-letter charakteres, not a
   text cipher. Bohak's article group, however, includes it per PGP. Likely a charakteres table inside the Bohak recipe book.
7. The brief's folder `sweep_2026-11-23_genizah_tables` is absent from this checkout (see top).

## 7. Calls, announcements, projects, people (public pages only)

| What | Detail | Source |
|---|---|---|
| T-S NS 70.1 edition | "will be published by Bohak, Oded Zinger, and Alan Elbaum"; no date; no publication found 24 Nov 2026 | <https://geniza.princeton.edu/documents/26158> |
| PGP "to examine" tag | ENA 4100.7b carries `to examine`; AS 187.240 "merits examination"; K24.37 "Needs examination": PGP itself flags these as open | the PGP pages cited above |
| Elbaum's Q&A | invites no crowdsourcing; the annotated image is the only output | <https://genizahfragments.lib.cam.ac.uk/2022/06/22/qa-wednesday-secret-codes-and-erotic-prose-with-alan-elbaum/> |
| **MiDRASH** (National Library of Israel; ERC Synergy grant, EUR 10 million per press; eScriptorium handwriting recognition; partners Elijah Lab at Haifa and the Princeton Geniza Project; Tel Aviv University layout classifier per CORDIS 101071829) | automatic transcription of about 400,000 Geniza fragments, about 160 million words, with researcher review feeding the model; a public "Transcribe-a-thon" ran 24-27 Nov 2025; the National Library said it would process 10 million more Hebrew manuscript images. Cipher texts are not mentioned. A full-text search over it could find cipher-like lines (words made of unusual letter sets), but the search portal was not found | <https://www.jns.org/feature/ai-unlocks-cairo-genizahs-hidden-world> (Sharon Altshul, 24 Nov 2025); <https://www.ynetnews.com/jewish-world/article/sy100wmgwwl>; <https://www.washingtonjewishweek.com/ai-unlocks-cairo-genizahs-hidden-world/>; <https://cordis.europa.eu/project/id/101071829/reporting> (all snippets) |
| Cambridge Genizah Research Unit | head Ben Outhwaite (named in *Genizah Fragments* 56); image reproduction requests go to **genizah@lib.cam.ac.uk** (printed on every PGP page); blog `genizahfragments.lib.cam.ac.uk` (its last posts in the 24 Nov search were dated 16 Nov 2026) | <https://wwwe.lib.cam.ac.uk/GF/Genizah_Fragments_56.pdf>; PGP pages |
| Princeton Geniza Project / Lab | Alan Elbaum, senior researcher: <https://genizalab.princeton.edu/people/alan-elbaum>; PGP site has a "Contact Us" menu (<https://geniza.princeton.edu/>), address not read | blog post above |
| Gideon Bohak (Tel Aviv University) | profile <https://english.tau.ac.il/profile/gbohak>; the page was not fetched, no address read | search 24 Nov |
| Oded Zinger | cited by Elbaum and PGP; no page opened | blog post |
| Amir Ashur | India Book editor; the Coptic-numeral code remark | blog post; PGP 9097 |
| Arianna D'Ottone Rambach (Sapienza) | ta'miya Qur'an; academia copy asks to be emailed (no address read) | <https://www.academia.edu/43006720/> (from the blog post) |
| Friedberg Genizah Project | catalogue needs registration; PGP's K24.23 description is "information from FGP" | <https://fjms.genizah.org> (6 Nov sweep) |
| Open "forthcoming": Bohak 2010 is the only printed cipher edition; Manchester's note once listed it "forthcoming" | stale | Luna snippet |

Not found: any open call for cipher solvers on the Geniza, any crowdsourcing project for cipher fragments, any HistoCrypt
or Cryptologia paper on a Geniza cipher, any Lasry/Megyesi/Knight work on Judaeo-Arabic. (The project's own
cyphersolver.com is returned by search for LJS 51; that is this project, not outside work.)

## 8. Ranked list: unread and worth attacking

1. **T-S AS 187.240.** Real cipher blocks (letter groups and a repeated glyph formula), no edition, PGP itself says it may be
   solvable from the surrounding formulae. Already a target; continue. Test the J277 keys and the paired-letter observation
   from the 15 Nov sweep.
2. **ENA 4100.7b, lines 7-12 (and the verso letter).** Six cipher lines in a personal letter, CC0 images, likely Zinger's
   letter; cross-test any key against J479 and the alef-initial property. Already `targets/ena4100/`.
3. **T-S K24.24.** Unidentified alphabet or cipher, no scholarship, not yet an item in any target. Cheapest to look at: if it
   is a charakteres sheet it closes at once; if it is text it is a fresh cipher. Has a related document in PGP (id not read).
4. **T-S NS J479.** Partly read; unpublished full reading and no edition. The cribs are known (signature, Burda verses,
   petition formula, the alphabet written out). Needs coordination with Elbaum before anything is published.
5. **T-S 13J18.19 (1139).** Short (about 15-20 numerals) but dated and with two partial published solutions that used
   different methods; a key search over J277 and Bodl. f 102/28 is cheap. Third passage open.
6. **India Book Coptic-numeral code** (unlocated). If the letters can be found, they would be the only cluster of the same
   system. Locate through PGP tag `India Book` and primary language "Greek/Coptic Numerals", then read for runs that are not
   sums.
7. **T-S NS 70.1.** Cracked but unpublished; low priority for us because Bohak, Zinger and Elbaum hold it. Hold.
8. **Manchester JRL B 5652** and other Bohak-family leaves: read or key published; only worth it if a leaf is long.

Not worth attacking: T-S K24.37 (mirror imprint), the fiscal `cipher` documents, the primer exercises, T-S Ar.35.109.

## 9. What the image sweep should cross-check

- PGP 33913 (T-S K24.24): the related document, and whether the script is charakteres, a pen trial or text; both sides.
- ENA 4100.7b: the JTS images (CC0); the alef-initial property; whether the verso "needs decipherment" part is also cipher.
- T-S NS J479 and ENA 4100.7b side by side: do they share glyphs? (Elbaum's annotated PNG is a ready-made key.)
- T-S 13J18.19: verso line 5 numerals (not yet viewed), against J277 and Bodl. f 102/28.
- JRL B 5652 images on Manchester Luna: confirm the cipher leaves.
- AIU XII.41 verso "cryptic symbols": nobody has opened it in these sweeps.
- PGP K24.23: whether it is the Bohak cipher or a different one (the 15 Nov sweep viewed recto only).
- T-S K5.7: charakteres table or cipher.
- T-S NS 246.26.2 versus NS 324.26.2 (Nimorad colophon), as a shelfmark check only.
- Search the PGP and CUDL for Greek/Coptic-numeral runs in India Book letters.

## 10. Routes and failures

| Host | Route | Result |
|---|---|---|
| geniza.princeton.edu documents and tag search | WebFetch of record pages; curl of the tag list | works |
| genizahfragments.lib.cam.ac.uk | WebFetch (search, tag and post pages) | works; `www.lib.cam.ac.uk/node/N` and `/collections/departments/taylor-schechter-genizah-research-unit/...` now 301 to `www.libraries.cam.ac.uk` home (the old FOTM and node pages cannot be reached; blog is the working host) |
| academia.edu, research.uniroma1.it, dl.acm.org, tandfonline.com, cudl.lib.cam.ac.uk view pages | WebFetch | 403 |
| mtc-journal.org PDF | WebFetch saved the PDF; text via PyMuPDF | works |
| library.soas.ac.uk | WebFetch | host not resolved |
| Searches not tried: HathiTrust full text, Google Books, Goitein's volumes, Schäfer-Shaked, the Bohak PDF beyond the snippet, the Friedberg catalogue | | left for a session with Chrome |
