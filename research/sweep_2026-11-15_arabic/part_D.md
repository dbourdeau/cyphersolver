# Arabic cipher sweep, part D: literature, and collections of the Middle East, Africa and Asia (15 Nov 2026)

Run by a Claude Code session (agent "claude session 15 Nov 2026, Arabic sweep part D", model claude-fable-5-2). Nothing was
solved, merged, promoted or committed. Rows are in `candidates_D.json`; scripts, downloads and contact sheets stayed in the
session scratch directory (not in the repository).

## Result in one paragraph

**3 rows, all from catalogue text, none with a vetting block, none dated before 1400.** No bare Arabic ciphertext was seen on
an image in this part. The three rows are 19th-20th century Tayyibi Ismaili manuscripts at the Institute of Ismaili Studies
(London) whose catalogues note cipher passages without reading them; none has page images online. The one large digitised
find, the papers of Khedive Abbas Hilmi II at Durham, turned out to hold **keys, not ciphertext**: two Arabic numeric
codebooks seen on the image (key leads), while the "coded telegrams" of the catalogue are the palace's clear decodes. The
literature pass found no Arabic cipher text that scholarship describes as unread and that is reachable online. Most of the
portals named in the brief were blocked or unreachable from this network (table below), so this part is thin on the
manuscript-collection side and that side is still open.

Pre-1400: nothing to report. The only pre-1400 codex met, IIS MS 1458 (Kitab al-riyad, older part before 760/1359), has its
secret-script colophon in the part added in 988/1580, and de Blois printed that colophon in 1984.

## Routes

| Source | Route | Result |
|---|---|---|
| Institute of Ismaili Studies, special-collections.iis.ac.uk (Axiell) | curl works. Search: `GET /search/simple/repeat?DatabaseChoices[1].Name=manuscripts&DatabaseChoices[1].Selected=True&...&Fields[0].Value=<term>&Fields[0].FieldName=Search_SearchSimple_FieldLabel&Fields[0].SearchInField=False` (cookie jar); records at `/Details/manuscripts/<n>` | 676 manuscript records. About 60 requests. Catalogue text only, no page images on the records |
| Durham University, catalogue XML `n2t.durham.ac.uk/ark:/32150/<id>.xml`, search `reed.dur.ac.uk/xtf/search?text=<q>;smode=simple` | curl works | Whole catalogues of the Abbas Hilmi II papers (1.9 MB) and the Wingate papers (4.6 MB) downloaded and grepped |
| Durham IIIF, `iiif.durham.ac.uk/manifests/trifle/32150/<aa>/<bb>/<cc>/<ark>/manifest` | curl works, slow (5-40 s an image). **The image server caps any request at 1,024 px on the long side**, also for a region, so a two-page microfilm frame cannot be brought to 1,500 px a page with plain IIIF calls; tiles (256 px) would be needed | about 235 requests: HIL/274 whole (95 canvases), HIL/57 whole (73), HIL/23 one canvas in three up to canvas 162 (55), HIL/152 and HIL/154 two canvases each |
| British Library interim catalogue, searcharchives.bl.uk | curl works (`/?search_field=all_fields&per_page=50&q=`) | 9 queries, no Arabic cipher text |
| Internet Archive | advancedsearch (metadata) and the full-text endpoint `services/search/beta/page_production/?service_backend=fts&user_query=` work, slow | 20 metadata queries, 5 full-text queries |
| AGDA (agda.ae) | JS application; headless Chromium showed the API: `GET https://agda.ae/api/catalogue-archive?search=<q>&lang=en&sort=rank:asc&page=1&pageSize=16&status=published` (curl works for Latin-script terms) | 7 queries, nothing in range |
| King Saud University, makhtota.ksu.edu.sa | curl works; `/manuscripts-list?title=<term>` searches titles only | 9 Arabic terms, treatise titles only |
| DECODE | `decode_search.py` | "Arabic", "Ismaili", "Hamdani", "Khedive": 0 records each |
| jjournals.ju.edu.jo (Jordan Journal for History and Archaeology) | curl with a full browser User-Agent (WebFetch got "Request Rejected") | one article read (Triki and Annak 2025) |
| **Blocked: sudanmemory.org** | Anubis "Making sure you're not a bot" page | not swept (Mahdist documents of the National Records Office, Khartoum) |
| **Blocked: eap.bl.uk** (Endangered Archives) | HTTP 202 with an empty body to curl and WebFetch | not swept (EAP051 and the African and Asian Arabic collections) |
| **Blocked: fihrist.org.uk** | no connection to curl, 503 to WebFetch (Anubis, as on 6 Nov) | not swept |
| **Blocked: nli.org.il** | 403 "Checking your browser..." on the one try | not swept (Yahuda collection) |
| **Blocked: almajidcenter.org** (Juma al-Majid) | Cloudflare 403 "Attention Required" | not swept |
| **Blocked: Wikimedia Commons API** | 429 on the 4th query of 10; stopped | 5 queries answered, nothing |
| Unreachable: portal.yek.gov.tr, dlib.ical.ir (Majlis), darah.org.sa | no connection (curl 000) | not swept |
| Not tried | al-Azhar, ZMT/vHMML (part A has HMML), Egyptian National Archives, Israel State Archives, Haganah archive, Zanzibar National Archives, Qatar National Library, kapl.org.sa (loads, no search run) | |

## Searches and their results

**IIS online catalogue** (manuscripts database, hits): "secret script" 6, cipher 4, code 12, coded 1, cryptic 3, secret 15,
"secret writing" 7, encrypted 0, cryptogram 1, undeciphered 0, sirriyya 0, symbols 5, "secret alphabet" 2, cryptography 2,
enciphered 0, ciphered 0, deciphered 0, "invented script" 1. All 33 distinct hit records were opened and read.

**Durham XTF**: "cipher arabic" 0; cipher 23 (Elliott, Ponsonby, Grey: European); cypher 26 (Wingate 7 hits, Hicks 2); "in
cipher" 5; "code arabic" 3 (Abbas Hilmi II papers 6 hits); "cipher mahdi*" 0; "secret writing" 7 (none Arabic).

**BL interim catalogue**: "Arabic cipher" (hits are records whose language field reads "Arabic and Cipher", i.e. Blenheim
papers in European cipher, plus Or 2579, see below); "Arabic cypher" 0; "cipher Gordon Khartoum"; "Gordon cipher Arabic";
"Gordon Khartoum cypher" (Add MS 34478 f. 115, Wolseley's cypher telegram to Gordon, English); "cipher Arabic Sudan" 0;
Arabic "in cipher" (Latin medical MSS).

**Internet Archive metadata**: title:(تعمية) 0; title:(المترجم) AND title:(حل) 0; title:("رسالة مشفرة") 0; شفرة AND مخطوط 0;
title:("كتابة سرية") 0; title:("قلم سري") 0; "Arabic cipher" 0; "letter in Arabic cipher" 0; "Arabic cypher" 0; title:(رموز) AND
title:(مخطوط) 2 (Ibn Wahshiyya, Shawq al-mustaham: alphabets); تعمية 3 and التعمية واستخراج المعمى 6 (the Mrayati volumes and
the 2018 dictionary of cryptologists); cipher AND language:Arabic 2 (modern); رسالة مشفرة 0; الكتابة السرية 39 (modern books);
"Mahdist cipher" 0; "Arabic secret writing manuscript" 20 (noise).
**Internet Archive full text**: "in Arabic cipher" 25 (numerals, except the Gordon item below); "Arabic cypher" 108 (numerals
and monograms, except FO Confidential Print on Gordon); "letter in Arabic cipher" 11 (a Goethe biography); "cipher in
Arabic" 20 (the word for zero); "written in cipher" Arabic manuscript colophon 1,481 (unsorted noise; Gacek's 1984 IIS
catalogue is on archive.org as `GacekCatalogueOfMSInIISLibrary1984FT` but its text file returned 404).

**Wikimedia Commons** (namespaces File and Category): "Arabic cipher" 906 (noise), "Arabic cryptography manuscript" 19 (two
al-Kindi page images, books), تعمية 57 (modern cryptography categories), "شفرة برقية" 0, "Arabic cryptogram" 22 (books); the
other five terms got 429.

**AGDA**: "Arabic cipher" 0, شفرة 1 (FO 1016/804, 1969), "cipher Arabic" 0, "Arabic code" 2 (1957, 1963), "bin Saud cipher" 0,
"cypher Arabic" 0; Arabic-script terms through curl failed (not JSON).

**KSU** (titles): المترجم 0, التعمية 0, المعمى 1 (Kanz al-asma fi kashf al-mu'amma: riddles), رموز / الرموز 5 (Hall al-rumuz
wa-mafatih al-kunuz x3, Sufi; two law titles), الأقلام 0, شفرة 0, مرموز 0, السرية 1 (tajwid).

**Web searches** (about 22, English and Arabic): Ismaili secret script and uncatalogued cipher notes; Schmeh's blog for Arabic
cryptograms (only the "Sufi fiddle", Top 50 no. 38, an unknown Arabic-looking script from a novel, not a cipher text of known
language); Mahdist cipher; HistoCrypt/Cryptologia Arabic or Moroccan cipher letters; Arab Revolt cipher (Tauber 2024);
unsolved Arabic-script cryptograms on Cipher Mysteries and elsewhere (none); Wingate and Arabic cipher; Arabic terms for an
enciphered historical letter (only news on European ciphers); Tomokiyo for Arabic (nothing on his site or blog); cipher
colophons and ownership notes (nothing specific); Zaydi or Yemeni secret script (only the Himyarite alphabet page of Berlin
Ms. or. quart. 110); Nusayri, Druze, Yezidi (Yezidi cryptic script literature; no unread manuscript named); Arabic alchemical
cipher (nothing outside Europe and North America); Abbas Hilmi codebooks (no study found); Azizi's Moroccan papers; Tazi's
book on Moroccan codes; Ibn Saud and Imam Yahya ciphers (nothing); Zanzibar sultans' letters in cipher (nothing); Gordon's
Arabic cipher messages; de Blois and the Hamdani cipher; the Tayyibi secret-script key.

## Finds, best first

All three are catalogue leads at the Institute of Ismaili Studies. `known.py` ("MS 1662", "Hamdani", "Institute of Ismaili",
"MS 1313", "MS 1291", "Kanz al-walad"): no hits. DECODE: 0 records.

1. **IIS MS 1662 [Handlist 105]**, Hamdani family scrapbook, 19th century. fol. 83b: "Notes written in the same system of
   cipher that Muhammad 'Ali used in Ms. 1499"; fol. 29a-b: a list of the imams "with some biographical information, much
   of it in cipher". de Blois (2011) reads the cipher line on fol. 21a (it has a decipherment over each letter) but prints
   no reading for 83b or 29a-b. The 83b system is that of MS 1499, a whole Kanz al-walad in an "invented script" which de
   Blois calls a straightforward cipher, crackable against the printed text: the key can be rebuilt, the notes are not on
   record as read. https://special-collections.iis.ac.uk/Details/manuscripts/154
2. **IIS MS 1291 (ArI, ZA)(b)**, an unidentified Tayyibi cosmological treatise, late 19th century, ff. 71r-86v, "part of the
   text in cryptic alphabet" (Cortese 2003), no reading given. Probably the standard Tayyibi secret script (key in print).
   https://special-collections.iis.ac.uk/Details/manuscripts/832
3. **IIS MS 1313 (ArI, ZA)**, Arba' masa'il fi'l-haqa'iq, copy of 5 Nov 1929, "cryptograms on p. 23" (Cortese 2003). Short;
   may be a cipher colophon or letter diagrams. https://special-collections.iis.ac.uk/Details/manuscripts/587

Why no vetting block: no image exists online for any of them, and the printed catalogues that might carry a reading (de
Blois 2011; Cortese 2003; Gacek 1984) were not opened in print; the online records reproduce their entries, but the
introductions (where de Blois describes the secret script) are not online.

## State of knowledge: Arabic cipher texts known to scholarship

"Not opened" means the work was not read in this session and the line rests on a catalogue, an abstract or the earlier
sweep; nothing here should be cited as checked beyond what the last column says.

| Text | Date | State | Where the reading or key is | Checked here |
|---|---|---|---|---|
| Worked cryptograms in the treatises (Ibn 'Adlan, Ibn al-Durayhim's Miftah al-kunuz, Ibn Dunaynir, al-Qalqashandi's section) | 13th-15th c. | read: solved in the treatises themselves and by the editors | Mrayati, Meer Alam, at-Tayyan, Arabic Origins of Cryptology (KFCRIS); Bosworth, JSS 8 (1963); Al-Kadi, Cryptologia 16 (1992) | not opened; no source met says an example was left unsolved (same finding as the 6 Nov sweep). Open question, needs the volumes |
| Ayyubid and Mamluk chancery cipher | 12th-15th c. | no surviving cryptogram named | Schwartz, Cryptologia 33 (2009) | not opened (6 Nov sweep) |
| Penn LJS 51, cipher letters in about 150 alphabets | 15th c. | read: Arabic transcriptions with the letters | 6 Nov sweep; leaf-by-leaf check still not done | not revisited (North America, another part) |
| Geniza Judaeo-Arabic cipher letters (T-S NS 70.1, T-S AS 205.186, T-S NS J479, ENA 4100.7b) | 11th-13th c. | read or being read (Bohak, Zinger, Elbaum); ENA 4100.7b six lines unread | 6 Nov sweep and the Hebrew sweep | not revisited |
| SOAS MS 12217, Qur'an fragment in cipher | uncertain | read | D'Ottone-Rambach, JIM 11 (2020) 133-176 | not opened |
| Mashhad, Babur's coded Qur'an | 16th c. | read | D'Ottone-Rambach, JIM 16 (2025) 125-162 | not opened |
| Borg cipher (Vatican) | 17th c. | read 2016; the cipher text is Latin, only the first page is Arabic script | Aldarrab, Knight, Megyesi | not opened; out of scope (Latin) |
| IIS MS 1458, Kitab al-riyad: colophon with the da'i's and scribe's names in Tayyibi secret script | 988/1580 (codex before 760/1359) | read | de Blois, "The oldest known Fatimid manuscript from Yemen", 1984 (colophon printed); IIS record | IIS record read |
| IIS MS 1499, Kanz al-walad wholly in an invented script | c. 1877-1887 | read in effect: known text, de Blois "crack the code easily enough" | de Blois 2011; ed. Ghalib 1971 | IIS record read; no table of the cipher seen |
| IIS MS 1662 fol. 21a, opening of a letter of the "hidden imam" in cipher | 19th c. copy | read: decipherment over each letter, quoted by de Blois | IIS record | IIS record read |
| **IIS MS 1662 fols 29a-b, 83b** | 19th c. | **no reading on record** | row 1 | IIS record read |
| Tayyibi secret script used for single names and words: IIS MS 1493 (scribe's name, read by de Blois), MS 1460 (names such as Abu Bakr), MS 10 (B) fols 147a, 148a, 173a, 176b, MS 211 (C), MS 1272 (words in red), MS 1251 (names in margins) | 1580-1907 | key known; single words in known works | Strothmann, Gnosis-Texte der Ismailiten (1943), introduction (per Gacek's note "see Strothmann, Introd."); de Blois 2011 introduction; tables in IIS MS 1455 fol. 1a and MS 1662 fol. 23a | IIS records read; Strothmann and de Blois not opened. Too short for rows |
| **IIS MS 1291 (b), MS 1313** | late 19th c., 1929 | **noted by Cortese, no reading given** | rows 2, 3 | IIS records read |
| Sultan Ahmad al-Mansur's cipher (Morocco) | late 16th c. | system described; whether every surviving letter is read was not established | Azizi and Azizi, Cryptologia 35 (2011) 41-51 and 37 (2013) 328-337; Azizi, C2SI 2019 (LNCS 11445) | not opened (abstracts only) |
| Moroccan Makhzen numeric code (names of the court, then an abjad table, dots between letters) | 19th c. | a key document, printed | al-Tazi, al-Rumuz al-sirriyya fi l-murasalat al-maghribiyya (1983) p. 53, quoted as "Document 02" in Triki and Annak, Jordan Journal for History and Archaeology 19/1 (2025) 190-193 | Triki and Annak read (PDF); Tazi not opened. Tazi's book is the place to look for unread Makhzen cipher letters |
| Gordon's Arabic cypher messages from Khartoum to the Khedive's keeper of the seal | 1884 | read at the time in Cairo with the Khedive's cypher; decodes printed | Foreign Office Confidential Print, Egypt and the Sudan (archive.org `foreign-office-confidential-print-egypt-and-the-sudan`: "Arabic cypher from Gordon ... the following is in Arabic cypher"; "four Arabic cypher letters") | full-text snippets only. Facsimiles of one such message "sent out ... secreted in a quill" were shown at Southampton in 1884 (archive.org `sim_armed-forces-journal_1884-12-20_22_21`, issue of 20 Dec 1884); the originals were not located |
| Khedive Abbas Hilmi II: coded telegrams of Ahmad Shawqi | 1904-1914 | read at the time: the file holds the palace's clear decodes | Durham HIL/274 (see below) | all 95 canvases viewed |
| Sharif Husayn's and the Arab Revolt's cipher traffic | 1916-1918 | read at the time by the British | Tauber, Journal of Intelligence History 23/2 (2024) 110-119 (abstract: the British "deciphered and regularly read all the communications of their Arab allies"); Durham SAD.138/10/5-9, 37-39, 41-42 (Arab Bureau on coded messages between the Sharif and Faruqi, Jul 1916) and SAD.138/12/7-10 (a "decyphered telegram from the Sharif to Faruqi") | abstract and Durham catalogue only; SAD.138 is not digitised; whether Arabic groups survive there is unknown |
| Ottoman Turkish cipher telegrams of the Hejaz, Yemen and Syria | 1896-1918 | already leads and catalogue entries | Koc and Ottoman sweeps | out of scope here |
| Mahdist state | 1881-1898 | no Mahdist cipher met in any source searched | | Sudan Memory blocked |
| Urabi, Senussi, Rif, Ibn Saud, Imam Yahya, Zanzibar, Mandate Palestine and Syria | 1880-1950 | no surviving Arabic ciphertext located; one search each at most | | open |
| Nusayri, Druze, Yezidi secret scripts; alchemical and magical manuscripts with enciphered recipes | | no unread text named in what was searched | | one search each; open |

## Closed on the image: Durham, Abbas Hilmi II papers

The Durham catalogue (HIL) marks "code" in four places. All were followed.

- **HIL/274, Ahmad Shawqi Bey, 1904-1914**, "a number of coded telegrams": all 95 canvases viewed as contact sheets
  (700 px frames) and three at the server's 1,024 px maximum (HIL/274/7-8, 168-169, 170-171). The telegrams are sheets
  headed with the printed calligraphic title of the Khedivial telegraph office and written out in clear Arabic, with
  receipt notes, i.e. the decoded copies; the rest are clear letters and numbered reports. No numeral groups on any frame.
  Read at the time; not a lead. Caveat: 1,024 px for a two-sheet frame is below the 1,500 px rule, so this is a screening
  for cipher groups (which would show at that size), not a reading of every line.
- **HIL/57, Crowned heads, 1903-1939** ("Language: ... code"): the first 24 of 73 canvases viewed, all European-language
  letters and telegram forms in clear; the item meant by "code" was not found. European in any case.
- **HIL/64, HIL/65, Telegrams Egypt and Sudan, 1911-1914** ("Arabic and use of code"; "partially encoded message from Phipps
  to Slatin", HIL/65/157-158): British intelligence telegrams in English; out of scope, not viewed.
- **HIL/23, Izzat Pasha, 1898-1912** (holder of codebook HIL/154): 55 of 228 canvases viewed (every third, up to canvas 162):
  clear Arabic letters throughout, no numeral groups.

Also closed: BL **Or 2579** (Qirqisani, 11th-12th c.) came up for "Arabic cipher"; the record means the numeral marking the
middle of a quire. Not a cipher.

## Key leads (keys with no ciphertext; not rows)

| Item | What it is | Seen |
|---|---|---|
| Durham **HIL/154/1-131**, "Codebook of 'Izzat Pasha", undated | Arabic numeric codebook: names (pp. 3-74), past, present and imperative verb forms, and a table giving each letter of the alphabet a code number, with instructions | image: canvases HIL/154/7-8 and 67-68 at 1,024 px (frame of an open pocket notebook, columns of four-digit Eastern Arabic numbers each beside an Arabic word in alphabetical order). https://n2t.durham.ac.uk/ark:/32150/t1mfq977v36q.html |
| Durham **HIL/152/1-154**, two identical codebooks, undated, unsigned | same plan as HIL/154 (names, verb tenses, terms, letter table) | downloaded, not opened on screen. https://n2t.durham.ac.uk/ark:/32150/t1m7s75dc88v.html |
| Durham HIL/149 (1914; codes for "M.B.F.", "A.B.Ch.", "M.P.M."), HIL/151 (despatches for Shafiq Pasha), HIL/153 (Dalaman-Europe), HIL/155 (the Khedive's cabinet chief) | codebooks catalogued as French (153: French and Arabic) | catalogue only; side items |
| Durham HIL/203/293-297 | Oppenheim correspondence "with formula and ?sample of synthetic ink and cypher keys", 1914-1918 | catalogue only |
| Durham SAD.250/1/81 (Wingate papers) | "Table of cypher codes for senior army personnel", 1880s | catalogue only; presumably English |
| IIS MS 1455 fol. 1a; MS 1662 fol. 23a | tables of the Tayyibi secret script | catalogue only |
| al-Tazi 1983, p. 53 | Makhzen numeric code key (Morocco, 19th c.) | at second hand |

These keys matter for Egyptian palace telegrams elsewhere: any numeric Arabic telegram of the Khedive's circle of
1898-1914 (Egyptian National Archives, Abdin; Ottoman archives) should be tried against HIL/152 and HIL/154 first.

## Side leads (one line each)

- Ottoman Turkish: Durham HIL/150/1-82, printed Turkish code book no. 75, Istanbul 1327-1329 AH (digitised): a key for
  Ottoman cipher telegrams of 1911-1913, worth trying on the Koc HPBK five-digit telegrams (they are earlier, 1898-1902).
- English, Sudan: Durham SAD.250/1/549-550, E. Palmer and Grenfell "re a note written in code by Gordon" (1886-87), not
  digitised; SAD.246/7/54 cypher telegram reporting the Hicks disaster (Nov 1883); SAD.255/1 "translation of a cypher ..."
  (May 1893, catalogue line cut off in my extract).
- English: BL Add MS 34478 f. 115, Wolseley's cypher telegram to Gordon, 1884.
- Persian: none met in this part beyond what the 6 Nov and 14 Nov sweeps list.

## What is left

1. **The blocked hosts need a real browser**: Sudan Memory (Anubis), EAP (empty 202), Fihrist (Anubis), NLI (browser check),
   Juma al-Majid (Cloudflare), Commons after the 429. Unreachable from here: YEK portal, Majlis, Darah.
2. **IIS**: ask for images of MS 1662 fols 29a-b and 83b, MS 1499 (sample), MS 1291 ff. 71r-86v, MS 1313 p. 23; read de
   Blois 2011 (introduction on secret script, entries 1499 and 1662) and Cortese 2003 in print. With images, rows 2 and 3
   are probably lookups and row 1 a short key rebuild.
3. **Durham, Abbas Hilmi II papers**: only HIL/274 was screened whole. HIL/23 is two thirds unscreened (and nothing beyond
   canvas 162); the many Arabic files of palace agents (Shafiq Pasha's telegrams of 1908-1909 among them) were not opened.
   A file that does not say "code" can still hold numeric telegrams. The 1,024 px cap means tiles for any close reading.
4. **Literature not opened**: the Mrayati series itself (are all worked cryptograms solved?), Schwartz 2009, Azizi 2011/2013,
   Tazi 1983 (the best chance of unread Moroccan cipher letters, with keys), Tauber 2024 (sources for Sharifian cipher
   telegrams: which archive holds the groups), Strothmann 1943, Gacek 1984, Poonawala 1977.
5. **Not attempted**: Egyptian National Archives, Israel State Archives and Haganah intercepts, Zanzibar National Archives,
   King Abdulaziz Foundation, Qatar National Library, al-Azhar, ZMT; Arabic terms on QDL (still open from the QDL sweep);
   Gordon's original Arabic cypher slips (the Royal Engineers Museum and the Gordon papers at the BL were not searched for them).
