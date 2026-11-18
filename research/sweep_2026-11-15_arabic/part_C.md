# Arabic cipher sweep, part C: France, Spain, Portugal, Italy, the Maghreb, United Kingdom (15 Nov 2026)

Run by a Claude Code session (model claude-fable-5-2), "claude session 15 Nov 2026, Arabic sweep part C". Goal: unread
enciphered texts in the Arabic language or script, any date to 1950, seen on images and vetted where possible. Nothing
solved, nothing merged or promoted. Rows: `candidates_C.json` (6 rows, 3 with a complete vetting block). Scratch
files and images are outside the repository.

## Result in one paragraph

Six rows. Three were seen at full size and carry a vetting block: **BnF Arabe 2562 ff. 54r-55v** (16th c., four pages
of recipes with about half the text in a numeral-and-letter cipher), **Wellcome MS Arabic 449 f. 1a** (17th-18th c.,
a 12-line numeral cryptogram) and **BnF Arabe 1966** (one line of numerals under a colophon of 1332). Three are
catalogue-only: **Bodleian MS. Laud Or. 139 f. 101a** (13th-c. manuscript, "undeciphered writing"), **Vat. ar. 34
f. 288v** (cryptographic inscription in Arabic and Coptic numerals) and **Cambridge Browne F. 43 / F. 16** (Subh-i
Azal's unexplained "cyphers"). All six are private or scribal ciphers inside manuscripts. **No Arabic-language
diplomatic or chancery cipher letter with an image online was found** in this area: the Spanish, Moroccan, Algerian
and Qatar Digital Library routes were blocked or unreachable from this network (see "Blocked"), and the Durham Sudan
and Abbas Hilmi material that could be opened is either English-language cipher or already decoded.

Two items are plausibly older than 1400 and were reported to the main session at once: Arabe 1966 (seen; the line is
undated and in paler ink than the 1332 colophon) and Laud Or. 139 (not seen).

## Routes that worked from this network

| Host | Route | Note |
|---|---|---|
| BnF Archives et manuscrits | `POST https://archivesetmanuscrits.bnf.fr/resultatRechercheSimple.html` with `TEXTE_LIBRE_INPUT=<term>&DOC_NUMERISE_INPUT_RADIO=all_docs` and a cookie jar from the home page | Works with curl. The "Documents numérisés" facet in the result page gives the Gallica ark of each hit (`val=https://gallica.bnf.fr/ark:/12148/btv1b...&filtre=Dao`). |
| Gallica images | `https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json` and `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<n>/<region>/<size>/0/default.jpg` | Works. `gallica.bnf.fr` itself (SRU, Pagination, IIIF) is 403 to curl. Many Arabe volumes are black-and-white microfilm, one opening per view. |
| archive.org | `advancedsearch.php`, `metadata/<id>/files`, `download/<id>/<id>_djvu.txt`; full text `services/search/beta/page_production/?service_backend=fts` | Works. The full-text search is too noisy for these terms (see below). |
| Fihrist | `git clone --depth 1 https://github.com/fihristorg/fihrist-mss` (TEI, scratch only) | The live site did not connect. The TEI covers BL, Bodleian, Cambridge, Wellcome, Rylands, SOAS, RAS and others. |
| Wellcome | `https://api.wellcomecollection.org/catalogue/v2/works?query=...&include=items` and `https://iiif.wellcomecollection.org/image/<id>.jp2/<region>/<size>/0/default.jpg` | Works. `wellcomecollection.org` pages are 403 to curl. |
| Digital Bodleian | `https://iiif.bodleian.ox.ac.uk/iiif/manifest/<uuid>.json` | Works. |
| Durham catalogue | `https://reed.dur.ac.uk/xtf/search?keyword=<term>` and `.../xtf/view?docId=ark/32150_<id>.xml` (whole finding aid as one HTML page) | Works. Digitised units: `https://iiif.durham.ac.uk/manifests/trifle/32150/<aa>/<bb>/<cc>/<id>/manifest` (id from the `n2t.durham.ac.uk/ark:/32150/<id>.html` links in the finding aid). Images come back at 1,024 px with a watermark when a larger size is asked for; region requests were not tried. |
| BAV OPAC | `https://opac.vatlib.it/mss/search?k_f=0&k_v=<term>&r=100` with cookie and Referer (as in `sweep_2026-11_digivatlib/opac.py`) | Works. |
| DigitArq (Torre do Tombo) | `https://digitarq.arquivos.pt/api/docs/search?query=<q>&archiveCode=ANTT` | Works. |
| DECODE | `sweep_2026-11-11_german/decode_search.py` | Works. |
| Cryptiana | `cryptiana.web.fc2.com/code/unsolved.htm`, `/code/GL.htm` | Works (Shift_JIS). Neither page has an Arabic-language item. |
| Chester Beatty | `https://viewer.cbl.ie/viewer/search/-/<term>/1/-/-/` in headless Chromium (plain JS page) | Worked for four terms, then showed an Anubis check: stopped. |

## Blocked or unreachable

| Host | What happened | Consequence |
|---|---|---|
| gallica.bnf.fr | 403 (Cloudflare page) to curl on SRU and Pagination | Used openapi.bnf.fr; no Gallica full-text search was possible. |
| PARES (pares.cultura.gob.es) | 429 on the first request (the home page) | Stopped. **Simancas, ACA and AHN were not searched at all** for Arabic letters in cipher. |
| bdh.bne.es | 403 | BNE digital library not searched. |
| qdl.qa | 403 with a browser User-Agent (one try) | Arabic and transliterated terms still not run on QDL. |
| eap.bl.uk | AWS WAF "Human Verification" captcha (HTTP 405, `x-amzn-waf-action: captcha`) | Endangered Archives Programme not searched. Needs a person in a browser. |
| cudl.lib.cam.ac.uk | 403 | Cambridge images not viewed (Browne F. 43, F. 16). |
| viewer.cbl.ie | Anubis proof-of-work page on the fifth query | Stopped after cipher, cryptogram, secret, cryptic. |
| fihrist.org.uk, calames.abes.fr, anom.archivesnationales.culture.gouv.fr, memoiredeshommes | no connection (curl 000) | Calames, BULAC and ANOM not searched. `bina.bulac.fr` search URL guessed wrong (404), not pursued. |
| francearchives.gouv.fr | 200 with a 266-byte page (script shell) | Not searched. |
| sudanmemory.org | 500 on the search URL tried | Not searched. |
| digital reader of the Durham Sudan Archive | not needed; `iiif.durham.ac.uk` answered | |

## Search terms and counts

**Durham (reed.dur.ac.uk XTF, whole catalogue):** cipher 23 items, cypher 26, "cipher sudan" 0, "in cipher arabic" 0,
"arabic cipher" 0, "code arabic" 3, cryptogram 3, "secret writing" 7, "cypher key" 2. Finding aids read for
cipher/cypher/code: Wingate (7 hits), Slatin (1), Hicks Pasha (2), Abbas Hilmi II (codebooks and "code" telegram files).

**BnF Archives et manuscrits:** "caractères de convention" 2 notices (Arabe 2357, Arabe 2562); "écriture de
convention" 0; "écriture secrète" arabe 1 (Arabe 1966); "en chiffres" arabe lettre: about 50 notices, all folio or
numeral uses; "cryptographie arabe" 0; "alphabets secrets" 6 (one Arabic: a table in a miscellany, key material);
"caractères secrets" 0; "lettre chiffrée" arabe 0. The 6 Nov sweep had already run cryptographie, cryptogramme,
écriture chiffrée, écriture secrète, alphabet secret.

**De Slane, Catalogue des manuscrits arabes (archive.org `cataloguearabes00bibluoft`, full text):** 41 hits for
écriture secrète / chiffré / chiffres / caractères secrets, conventionnels, de convention / cryptograph / alphabet
secret / écriture inconnue, and a second pass for déchiffr / inintelligible / "chilTres" (OCR) / écriture de
convention. Real hits: nos. 238 (key), 925, 1220, 1222, 1966, 2357, 2562. Blochet's and Vajda's later volumes are
not on archive.org as full text; their notices are in Archives et manuscrits and were covered by the term search only.

**Other catalogues grepped (archive.org full text), no cipher hit:** Casiri, Bibliotheca Arabico-Hispana Escurialensis
(2 vols; Latin terms; the OCR is poor, so this is weak); Derenbourg, Les manuscrits arabes de l'Escurial (only the
1884-1903 part `p2lesmanuscarab02dereuoft` found); Guillén Robles, Catálogo de los manuscritos árabes de la Biblioteca
Nacional de Madrid (1889); Ribera and Asín, Manuscritos árabes y aljamiados de la Biblioteca de la Junta (1912);
Catalogue des manuscrits arabes de Rabat (1953) and Lévi-Provençal, Les manuscrits arabes de Rabat (1921); Rieu,
Supplement to the Catalogue of the Arabic Manuscripts in the British Museum (1894: only "tables of strange and secret
alphabets", key material); Griffini, I manoscritti arabi della Biblioteca Ambrosiana (2 parts found). Not found on
archive.org as text: Arberry's Chester Beatty Handlist, Löfgren-Traini, Levi Della Vida's Elenco (the Secondo elenco
is there without OCR text), Fagnan's Algiers catalogue.

**Fihrist TEI (15,638 records):** pattern 1 (cipher, cypher, cryptogra-, secret script/alphabet/writing/character,
"in code", coded, unknown script, secret code) 28 records; pattern 2 (cryptic, encrypt, encoded, enigmatic script,
secret language/sign/letter/numeral, unidentified script, undecipher-, mysterious/strange script, magic script or
alphabet, abjad cipher, and the Arabic words قلم, تعمية, معمى, رموز) 189 records, nearly all the scribal formula
"bi-qalam" or book titles with "rumuz". Real hits: Wellcome MS Arabic 449, Wellcome MS Arabic 10, Bodleian Laud Or.
139, Cambridge Browne F. 16, F. 43, Q. 3, H. 22, and the Tipu Sultan volumes. BL Or 7243, named by the 6 Nov sweep from
the BL interim catalogue, has no cipher wording in its Fihrist record (Persian and Turkish Sufi verse): not confirmed.

**Wellcome API:** cryptogram 0; "cipher arabic manuscript" 0; "secret alphabet" 3 (none Arabic); "cryptography
arabic" 0; "secret writing arabic" 0. The cryptogram in MS Arabic 449 is only findable through the Fihrist TEI.

**BAV OPAC:** écriture secrète 0; caractères secrets 0; alphabet secret(s) 0; cryptograph* 9 (four Vat. ar.);
scrittura segreta 4 (none oriental); caractères de convention 0; "en chiffres" 101 and chiffré* 133 (folio-numbering
notes of the French catalogue of Vat. ar. and Borg. ar.); écriture conventionnelle 0; alfabeti segreti 0; caratteri
segreti 1 (Borg. lat. 898, read 2016); secret alphabet 0.

**DigitArq, ANTT:** "carta árabe cifra" 1, "arábico cifra" 1, "em árabe cifrada" 0, "caracteres árabes cifra" 0,
"aljamia cifra" 0, "carta em arábico em cifra" 1; none of the returned records joins Arabic and cipher.

**Chester Beatty viewer:** cipher 0, cryptogram 0, secret 12 (none relevant), cryptic 1 (T 444, a Turkish jafr text).

**archive.org full-text search:** "lettre arabe" "en chiffres" 321, "arabe chiffré" 54, "chiffre arabe" lettre sultan
déchiffrer 697, "en arábigo" "en cifra" 749, "carta árabe" cifrada 7, "cifra arábiga" (not finished). The first 20 of
each are crosswords, numeral notes and unrelated books; not read further.

**Web searches (about 15):** the Azizi papers on Moroccan cryptography, Durham Mahdist cipher, Arabic letters in
cipher in Spanish archives, Moroccan Makhzen cipher letters in Arabic, Tazi's book, and the per-document prior-art
searches listed in the vetting blocks. None named a digitised unread Arabic cipher letter.

## Pages viewed

| Item | Views | Size |
|---|---|---|
| BnF Arabe 1966 (btv1b11001551n) | views 50-54 at 900 px; view 50 lower right half at 2,000 px; the line at native resolution | crop 2,329 x 533 px; opening 5,824 x 4,448 |
| BnF Arabe 925 (btv1b11000308m) | views 136-141 at 900 px; view 141 right page at 2,000 px and a native crop | crop 1,814 x 1,361 px |
| BnF Arabe 2357 (btv1b11002192k) | views 14-62 as sheets at 520 px; views 22 and 25 enlarged to 1,800 px | |
| BnF Arabe 2562 (btv1b100375395) | views 55-60 at 800 px; ff. 54r, 54v, 55r, 55v crops at native resolution | pages about 1,435-1,503 x 2,276 px (the scan's limit) |
| Wellcome MS Arabic 449 | images 2-4 at 1,300 px; f. 1a in two native crops | 1,594 x 2,294 and 1,594 x 2,110 px |
| Wellcome MS Arabic 10 | images 1-6 and 210-227 at 600-800 px; image 5 at 1,900 px | |
| Durham HIL/274 (Ahmad Shawqi) | all 95 frames at 500 px; frames 4 and 14 at the 1,024 px the server returns | |

## Finds, best first

1. **BnF Arabe 2562, ff. 54r-55v** (16th c.). Four pages of recipes: rubrics and running words in clear Arabic, the
   names and quantities in strings of Arabic-Indic numerals with a few letters and signs. One recipe speaks of the
   sages of India and of commanding spirits. Bare, no key. The clear context makes it the most workable item here.
   Vetted, open.
2. **Wellcome MS Arabic 449, f. 1a** (17th-18th c.). Twelve lines of numerals bearing letter dots, with a few letters
   and a theta-like sign, about 150 signs, beside an owner's recipes; one more cipher line inside a clear recipe. Colour
   IIIF. Vetted, open. Serikoff's printed catalogue (2005) was not opened.
3. **BnF Arabe 1966, last page** (colophon Jumada I 732 / 1332). One line: a few Arabic letters, then about 28
   numerals. De Slane: "une ligne d'écriture secrète en chiffres indiens". Short, and the date of the line is not
   established. Vetted, open.
4. **Bodleian MS. Laud Or. 139, f. 101a** (before c. 1300). "Some curious letter forms and undeciphered writing"
   between two sections of text (Savage-Smith 2011). Not digitised. Catalogue row.
5. **Vat. ar. 34, f. 288v** (16th c.). "Inscriptio cryptographica e notis numericis arabicis et copticis composita",
   with no reading in the BAV record. Not digitised. Catalogue row; keys of the same Coptic milieu exist (below).
6. **Cambridge, Browne F. 43 and F. 16** (c. 1885-96). Subh-i Azal's "cyphers" in place of a scribe's name, which he
   declined to explain to Browne. Not seen (CUDL 403). Catalogue row.

Weak, not a row: **Wellcome MS Arabic 10** (Indo-Persian copy of Ibn al-Nafis, 988/1580). The record says a flyleaf
("fol. 004b") has "a text written in a cryptic alphabet". Image 5 shows a table of unlucky days of the months with
three or four lines in odd letter forms below it; I could not tell at 1,900 px whether they are a cipher or a cursive
hand, and the language is as likely Persian as Arabic.

## Closed: read, glossed, or not a text cipher

- **BnF Arabe 925**, last leaf (replacement leaf in a 14th-c. formulary; de Slane: "dix lignes d'une écriture de
  convention, qui paraissent renfermer une formule magique"). Seen at full size: a talisman recipe ("write on a tablet
  ... with musk and saffron") with about ten lines of signs of the Seven Seals kind (strokes, ladders, hash, mim) to be
  copied. Magical charakteres, no linguistic content shown. Not a lead.
- **BnF Arabe 2357, ff. 12-58** (17th c., treasure-hunting tract; de Slane: "passages en chiffres et en caractères de
  convention"). Seen on views 22 and 25: the sign lines are introduced by "this is what is written on the potsherd",
  i.e. talismans to copy; a few incense quantities are in signs too. Charakteres, not a lead.
- **BnF Arabe 1220, 1222** (talisman collections with "passages écrits en chiffres"): magical, not opened.
- **Vat. ar. 13** (9th-c. Gospels): the scribe's name is added in a Greek letter cipher and was interpreted in Greek
  minuscule in about the 13th century (BAV record 115495). Greek, glossed.
- **Vat. ar. 28** (1271): a scribe's invocation in Coptic cryptography between its Arabic and Coptic versions; "alia
  manus clavem cryptogrammatis addidit" (BAV record 116992). Read; the key is a key lead.
- **Vat. ar. 36** (note of 1544): the year is written in two signs of the "Davidic" alphabet published by Casanova,
  Journal Asiatique 1921, and is read in the BAV record (950 AH).
- **Borg. lat. 898**: read 2016 (Aldarrab, Knight, Megyesi), as instructed, skipped.
- **Durham, Abbas Hilmi II papers, HIL/274** (Ahmad Shawqi, "a number of coded telegrams", 1904-14): the frames are
  Khedivial Diwan telegram forms carrying the clear Arabic text, i.e. decoded copies. Read at the time.
- **Durham, Wingate papers**: the Arabic cipher traffic of the Sharif of Mecca in 1916 appears only as British
  decrypts and reports ("decyphered telegram from the Sharif to Faruqi", SAD.138/12/7-10; "coded messages between the
  Sharif and Faruqi", SAD.138/10/5-9; "the discovery of secret cyphers exchanged between Ali, Faisal and the Sharif",
  SAD.141/3). No ciphertext described. The other cypher entries (SAD.250/1/81 table of cypher codes 1884,
  SAD.246/7/54 cypher telegram on the Hicks disaster, SAD.255/1/328-329 translation of a cypher telegram of the
  Governor of Tripoli) are English or Ottoman and out of scope.
- **Saadian numeric cipher of Ahmad al-Mansur**: deciphered and published by G. S. Colin, "Note sur le système
  cryptographique du sultan Ahmad al-Mansur", Hespéris 7 (1927). The citation is from memory and was not opened in this
  session; the 15 Nov web search did not reach it.

## Key leads (no ciphertext, or keys that could read other items)

- **BnF Arabe 238, f. 384v**: "Clef d'un chiffre dont se servaient les écrivains coptes" (de Slane; Gallica
  btv1b11004021j per the Archives et manuscrits facet; not opened). Relevant to Vat. ar. 34.
- **Vat. ar. 28**: key added to the scribe's cryptogram (digitised, not opened).
- **Durham, Abbas Hilmi II papers, codebooks, digitised:** HIL/152/1-154 (two identical Arabic codebooks: names, past,
  present and imperative verb forms, terms, and a table giving each Arabic letter a code number), HIL/154/1-131
  (codebook of Izzat Pasha, same plan, Arabic), HIL/153 (Dalaman-Europe, French and Arabic), HIL/150 (Ottoman code
  book no. 75, 1910), HIL/149, 151, 155 (French). HIL/203/293-7 has "cypher keys" with Oppenheim's correspondence.
  These would read any undecoded Arabic telegram of the Khedive's circle of 1900-14.
- **BnF, "alphabets secrets"** in a miscellany (Archives et manuscrits notice cc30322v, Nuzhat al-mahafil); de Slane
  lists "Alphabets secrets" as item 15 of that miscellany (the shelf number was not noted here): tables only.
- **BL, Rieu Supplement p. 769**: ff. 50-58 "Tables of strange and secret alphabets" in a volume of mixed contents.
- **BL Delhi Persian 853**, ff. 303v-325r: "recipes for cryptography and writing in cyphers" (Persian, Arabic, Urdu).
- **Vat. Sbath 762**: Greek texts including "un alphabet chiffré avec clavier" (Greek, out of scope).

## Side leads (Persian or Ottoman, one line each)

- Cambridge, Browne Q. 3 (Persian occult compendium ascribed to Kashifi): words disguised in a "cabbalistic secret writing".
- Cambridge, Browne H. 22 ff. 145-173: a list "very difficult to read, being written in the cipher called raqam" (accounting numerals, not a cipher).
- BL IO Islamic 4684, 4685; RAS Persian 171: Tipu Sultan's "personal cypher" and paraph (signature devices; the RAS one "undeciphered"). No ciphertext described.
- Cambridge, Browne L. 6: Persian telegrams to and from Houtum-Schindler, 1876 (not said to be in code).
- Durham HIL/150: Ottoman code book no. 75 (1327-29 AH), digitised.
- Durham SAD.250/1/549-550: Palmer and Grenfell "re a note written in code by Gordon" (language not stated).
- Durham, Hicks Pasha registers of telegrams SAD.600/1 and 600/2/1-35 (1883): "Language: English, Arabic and cypher". The cypher is most likely the Egyptian Army's English one; not seen.
- Chester Beatty T 444: Turkish translation of al-Bistami's Miftah al-jafr (divination, not cipher).

## What is left

- **Spain**: everything. PARES answered 429 at the first request; the Arabic letters "en cifra" at Simancas, ACA and
  AHN, the Morisco material and BNE need another network or a browser session.
- **Maghreb**: the Makhzen numeric-cipher letters of the 19th century named by Tazi (Les codes secrets des
  correspondances marocaines à travers l'histoire, Rabat 1983) and by Azizi and Azizi (Cryptologia 35, 2011, and 37,
  2013; C2SI 2019) were not reached: the papers could not be opened here and the originals are in Rabat (Archives
  royales, Bibliothèque Hassania), not found online. ANOM (Abd el-Kader and tribal correspondence) and the SHD did not
  connect or were not searched. The 2025 article on the "Fasi pen" (Jordan Journal for History and Archaeology) is open
  access and was not read; it concerns numerals in court documents, which the brief excludes.
- **France**: Calames and BULAC did not connect. Blochet's and Vajda's catalogues were covered only through the
  Archives et manuscrits term search. Arabe 238 f. 384v (the Coptic scribes' key) should be opened with Vat. ar. 34.
- **Italy**: only the BAV OPAC was searched. Ambrosiana (Löfgren-Traini), the Medici Oriental Press papers, ASF and
  ASVe Arabic letters, and Naples were not reached. Order images of Vat. ar. 34 f. 288v.
- **United Kingdom**: QDL with Arabic terms (403), EAP (captcha), CUDL (403), the Durham telegram files HIL/64 and
  HIL/65 ("Arabic and code", 1,011 and 1,127 frames, digitised, not paged) and the Hicks registers. Bodleian: order
  f. 101a of Laud Or. 139. Edinburgh and the Rylands beyond what the Fihrist TEI holds were not searched. Serikoff's
  catalogue entry for WMS Arabic 449 should be read.
- **Method note**: every find came from a cataloguer's passing remark ("écriture secrète", "cryptogram", "undeciphered
  writing") in a manuscript catalogue, not from an archive of letters. The same grep on other large Arabic manuscript
  catalogues with full text (Ahlwardt for Berlin, Pertsch for Gotha, Leiden, the Garrett and Mingana catalogues) is the
  obvious next pass.
