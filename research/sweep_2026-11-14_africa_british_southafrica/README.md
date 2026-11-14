# British and South African holdings, Africa slant (14 Nov 2026)

Run by a Claude Code sweep agent (Claude Sonnet 5.5) for the project, 14 Nov 2026, about 1 h wall clock of the 4 h allowed; stopped because every reachable host was exhausted. No Chrome tools in this session.
Result (second pass included): **3 candidate rows** (`candidates.json`), 8 key leads (`key_leads.json`). Pass 1 (catalogues) found one weak row; pass 2 (printed-source OCR grep) found the two better rows below. One printed page was viewed (Hake, p. 50); no archive leaf of an African cipher was seen on any reachable host.

## Routes that worked
- **TNA Discovery open API** (`harvest.py`, `harvest_series.py`, `harvest_places.py`, `harvest_places2.py`; `raw.jsonl` = 1,932 unique records, `harvest.log`, `series.out`, `places.out`, `places2.out`). `sps.departments` and `sps.recordSeries` filters both work. 2.5 s per request.
- **Birmingham Cadbury Research Library CalmView** (`calm_search.py`, `calm_record.py`; `calmview.bham.ac.uk/advanced.aspx`, same form as Lambeth). CMS archive, Chamberlain papers.
- **UCT AtoM** (`atom.py`, `atom.lib.uct.ac.za/index.php/informationobject/browse?query=`).
- **University of Pretoria DSpace 7 REST** (`dspace.py`, `repository.up.ac.za/server/api/discover/search/objects`).
- **British Library interim Archives and Manuscripts Catalogue** (`bl_search.py`, `bl_filter.py`; `searcharchives.bl.uk/?search_field=all_fields&q=`, answers plain curl; `bl_hits.jsonl`).
- **archive.org** FTS and metadata search (`ia_fts.py`, `ia_meta.py`; both answer, both too noisy for Africa: the FTS is OR-ish ranking).
- **Wellcome** catalogue API (`wellcome.py`).

## Routes blocked or unreachable from this network
Anubis proof-of-work (not solved): Bodleian Archives and Manuscripts (Rhodes House, Commonwealth and African collections). Omeka "verifying your browser" JS check: UCT Digital Collections. JS-only Epexio apps with no scriptable search: SOAS (archives.soas.ac.uk; Methodist, LMS, Africa missions) and LSE archives; I did not probe their internal APIs. 403: Archives Hub, Cambridge ArchiveSearch (RCS), Durham Sudan Archive (`www.dur.ac.uk`, `reed.dur.ac.uk`), NLS earlier, Stellenbosch scholar, Pretoria special collections page, UCL, Harvard HOLLIS, Northwestern, Michigan. No answer (connect failure, twice for Wits): Wits Historical Papers AtoM, South African National Archives (eAHRA and nationalarchives.gov.za), Cory/NAHECS, KZN/Killie Campbell, DISA, RGS (`collections.rgs.org`, `catalogue.rgs.org`), Edinburgh, Manchester, Liverpool, Leeds, Hull archives. Livingstone Online search page returned the same 42,963-byte page for cipher and cypher (no results parsed). Needs Chrome or a different network: Bodleian, SOAS, LSE, Cambridge, Durham, UCT Digital Collections, Wits, SAnA, RGS.

## Terms and hit counts

TNA Discovery, with `sps.departments`, dates 1500-1950 (count = records the API reports). Terms run per department: cipher, cypher, "in cipher", "in cypher", decipher, decypher, deciphered, decyphered, undeciphered, undecyphered, enciphered, "cipher telegram", "cypher telegram", "in code", "code telegram", "secret writing", cryptogram, "cipher key", "cypher key", "in secret characters".

| Dept | cipher | cypher | in cipher | in cypher | decipher | decypher | deciphered | decyphered | tel. (cipher/cypher) | in code | other nonzero |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CO | 42 | 74 | 4 | 5 | 5 | 1 | 5 | 1 | 11/12 | 0 | code telegram 1 |
| FO | 11 | 181 | 3 | 6 | 14 | 12 | 11 | 12 | 1/2 | 106 | secret writing 2, cypher key 1 |
| WO | 284 | 58 | 2 | 0 | 7 | 0 | 6 | 0 | 0/0 | 1 | enciphered 1, secret writing 2, cipher key 1 |
| T | 1 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0/0 | 1 | |
| DO | 0 | 5 | 0 | 0 | 0 | 7 | 0 | 7 | 0/0 | 0 | |
| CAB | 13 | 50 | 0 | 0 | 0 | 11 | 0 | 11 | 0/6 | 0 | |
| ADM | 118 | 101 | 0 | 2 | 23 | 3 | 21 | 3 | 0/0 | 3 | enciphered 12, cryptogram 1 |
| PRO (private collections) | 103 | 40 | 43 | 15 | 40 | 49 | 39 | 49 | 0/2 | 164 | undeciphered 2, enciphered 1, cipher key 1 |
| MPI | 0 on all terms | | | | | | | | | | |

Undeciphered, undecyphered, enciphered, cryptogram, "in secret characters" returned 0 in CO, FO, T, DO, CAB. Place x term (no department filter), 50 places x {cipher, cypher}: Africa, Gold Coast, Ashanti, Sierra Leone, Gambia, Lagos, Niger, Nigeria, Cape Colony, Natal, Zululand, Transvaal, Orange Free State, Basutoland, Bechuanaland, Rhodesia, Matabeleland, Nyasaland, Zanzibar, Uganda, Kenya, Sudan, Khartoum, Egypt, Abyssinia, Morocco, Tangier, Algiers, Tunis, Tripoli, Congo, Madagascar, Mauritius, Somaliland, Mafeking, Ladysmith, Kimberley, Delagoa Bay, Mozambique, Angola, Liberia, Senegal, Livingstone, Barbary, Fernando Po, Cameroons, Togoland, German East Africa, Benin, Zambezi, Swaziland: 100 queries, each 0-9 hits except where an unfiltered term was broad (see `places.out`; nothing usable). Second pass, 18 places x {"in figures", "in characters", "secret writing", decipher}: nonzero only "Africa secret writing" 6 (all WWII MI5 files KV 2), "Africa decipher" 5, "Cape decipher" 5, Egypt decipher 3, a few singletons (see `places2.out`); none a ciphertext. Series pass (`sps.recordSeries`, 56 series x cipher, cypher, decipher, decypher; `series.out`): SP 71, 72, 73, 74 (Barbary consuls) 0 hits for cipher/cypher/decipher; SP 75 1 ("English commissioners to Cecil, and decipher", 1600); SP 99 5 (Venice; already tracked or Italian); CO 96, 267, 179, 48, 49, 82, 98, 87, 291, CO 391 etc. 0; T 70 0; FO 76, 3, 8 and the Cape/Natal/West African CO series 0 (a few counts are only fuzzy matches, none about ciphertext).

Other hosts:
- Birmingham CalmView: cipher 8, cypher 20, "in cipher" 8, decipher 20 (first page, capped), deciphered 15, "cypher telegram" 7, "cipher telegram" 5, "secret writing" 20 (noise), cryptogram 2, undeciphered 2, "key to cypher" 2, "in code" 20 (noise), enciphered 0, "key to cipher" 0.
- UCT AtoM: cipher 0, cypher 1 (Sir B. Walker papers BC356, naval; no cipher evidence), decipher 4, deciphered 3, "secret writing" 2, "secret code" 1, cryptogram 0, coded 0, cryptic 1, "invisible ink" 0, "in code" 207 (noise). Hits were Geis family letter translations, Dirk Bax, Brody transcripts: none cipher.
- Pretoria DSpace: "in cipher" 146, cypher 54, deciphered 1,420, "secret writing" 3,979, cryptogram 15 (full-text matches across digitised Africana books, newspapers and theses; the hits are modern cryptography theses, novels such as "A woman's part in a revolution" 1897 and Jameson biographies, and fuzzy matches). No manuscript or item-level cipher.
- BL interim catalogue: "cipher|cypher" x 47 African place names, 94 queries (`bl_run.py`, `bl_run.out`), 156 unique records; only 4 have cipher within 220 characters of an African name (Add MS 61535 Algiers consul Cole; Add MS 38237 Gordon; IOR/L/PS/12/385 Aden telegram; Mss Eur D623/4 Mauritius 1798). None is a lead (see exclusions).
- Wellcome: cipher 70, cypher 110, nothing African (Galton cipher key GALTON/1/1/7/2, Tughra woodcuts, early cipher books).
- archive.org FTS: three Africa phrase queries ("in cipher" with Zanzibar Sultan, Khartoum Gordon, Gold Coast) gave 7,613, 6,032 and 444 page hits of noise (Crispi memoirs, Wolseley letters, German diplomatic documents). Metadata search "(cipher or cypher) AND African place AND texts" gave only newspaper issues and Trithemius.
- Web search: two searches found only the Livingstone 1871 Bambarre letter (faded ink, deciphered 2010, not a cipher).

## Finds, ranked (after pass 2)
1. **Egerton to Gordon, Cairo, 30 Aug 1884, numeric cipher telegram** (23 six-digit groups printed in Hake's edition of Gordon's Khartoum journals, Book I p. 50 footnote 67; page image viewed from the archive.org PDF, digits checked against the OCR of two editions and Gutenberg 49224). Gordon: "which I cannot decipher" (Stewart had the cipher books). Plaintext not in the book. Short, code not published: solvability 2, difficulty 5. Distinct from the catalogue's PRO 30/57/4/119 and from the Durham SAD.250/1/550 lead of the north-east literature sweep. The Appendix X 'Arabic Cipher Telegram' (Wolseley, 20 Sep 1884) prints no ciphertext (checked on the page image, p. 379).
2. **Yonge to Dundas, Cape Town, 6 Jan 1801, secret**: the papers of a Dutch passenger Prediger bound for Batavia, "some in cypher", "a long letter in cypher" survives (Theal, Records of the Cape Colony vol. III p. 387). Same name and years as the solved `batavia1800` letter (Raad der Aziatische Bezittingen to C. J. Prediger, 2-digit grid key): a possible ready key. Original is in TNA CO 48, volume not identified; no image.
3. Dawes, CMS/B/OMS/C/W/O31/29-30 (1823), as in pass 1 (below, now rank 3).

### Pass 1 find
1. **CMS/B/OMS/C/W/O31/29-30, William Dawes, 1823** (Cadbury Research Library): "Letters to used for cypher" and "Key to cypher". West Indies (Antigua) but the writer was the former governor of Sierra Leone. Probably an alphabet and its key; needs the Library to say. Score 2/3/2. Not on DECODE.

That is the whole list. Africa gave nothing else that is both enciphered and unread.

## Excluded and why
- Kitchener papers PRO 30/57/4/26 and 3/11 (1884): "Translation from Arabic script cipher" with its translation (read). PRO 30/57/4/77-78: "Please use Arabic cipher ... part in Arabic script" is an instruction, not a ciphertext. PRO 30/57/4/119 (Wolseley to Gordon, "cipher unknown") is already in the catalogue.
- Chamberlain papers (Birmingham JC10/5, JC13/1, JC14/2, JC29): all "decipher"/"telegram cipher" entries carry the decipher (Milner, Hely-Hutchinson, Roberts 1897-1902). Read at the time.
- CO series hits: administrative notes on cipher telegrams (Gambia CO 323/698/47 "cipher copies not included", Cameroons/Fernando Po CO 649/1/67, 649/9/26-27, Bahamas, Jamaica, Windwards); CO 166 and CO 245 Martinique/Larnage letters are "Deciphered". No ciphertext.
- FO 367/FO 371 1906 Liberia/Boma/Egypt telegram files: mention a garbled or undecipherable telegram; text not shown, administrative, 1906 (outside 1350-1900 priority; candidates only if the text were attached, none found). FO 800/42/7 Grey to Hardinge on Congo troops: "letter in cypher", 1906, decoded at the time. FO 800/1/61, FO 244/785 (Congo cyphers), FO 608/87/18: administrative.
- WO 132/7 (Buller cypher telegram lists 1899-1900) and WO 33/56/A433 ('Z' cipher South Africa supplement, missing): no ciphertext.
- FCO 141/13563-13578 Nigeria secret despatches with cyphers 1896-1908: forwarding notes (see key leads).
- Add MS 61535 (Cole at Algiers 1706-10): the volume's cipher language belongs to the Hedges letters from Constantinople; the Algiers letters are Turkish/Italian/Arabic. Not a lead.
- IOR/L/PS/12/385, IOR/L/PS/10/844 and similar 1919-1940 cypher telegram files: 20th century, administrative.
- SP 89/86/139 (Walpole, Gibraltar and Tangier news sent in ciphered letters via Holland): the cipher letters are other folios, not described.
- Hits for Wellcome, UCT, Pretoria as above: not cipher.

## What is left
- **Needs Chrome or another network**: Bodleian (Rhodes House, MSS Afr., Commonwealth and African collections: Anubis); SOAS and LSE (Epexio JS apps); Cambridge RCS and Durham Sudan Archive (403); Archives Hub (403); UCT Digital Collections (browser check); Wits, SAnA/NAHECS, Cory, RGS (no answer); NLS (403 earlier).
- Not done: Theal's *Records of the Cape Colony*, *Records of South-Eastern Africa*, *Annals of Natal* and *Basutoland Records* are on archive.org (e.g. `recordsofcapecol00thea_1`, `recordscapecolo05offigoog`, `basutolandrecor00theagoog`, `annalsofnatal02birdiala`); their OCR could be grepped for cipher mentions to find printed-but-unread items. Not downloaded here.
- Not done: Tomokiyo and Lasry searches for the single row; Royal African Company (T 70) item level; CMS Birmingham with more terms ("code", "secret characters", "figures"); Dutch (Nationaal Archief VOC Kaap, WIC Elmina) and Portuguese (AHU) are other sweeps' ground.
- Catalogue wording is the limit: TNA's Africa series (CO 96 Gold Coast, CO 267 Sierra Leone, CO 179 Natal, CO 48 Cape, SP 71-75 Barbary, FO 76 Tripoli) are described at volume level, so a ciphered letter inside never shows in term searches. Paging those volumes needs images, and TNA does not hold digital images of them; the Barbary SP volumes would need a visit or a scan order.


## Pass 2 (14 Nov 2026, after the coordinator's request)

### Printed-source OCR grep (`ia_ids.py`, `ia_dl_grep.py`; ids in `ids.json`; raw OCR in scratch)
254 archive.org ids picked by metadata queries; 38 had no usable OCR (`short/none` in `ia_dl_grep.out`, e.g. `recordscapecolo28offigoog`, `recordscapecolo15offigoog`, `laterannalsofnat0000alan`, `papersconcerning0057unse`), 216 were grepped for cipher, cypher, decipher, decypher, cyphered, ciphered, "in code", "secret writing", cryptogram, cryptograph (175 context windows, `ocr_hits.jsonl`, trimmed). Sets: Theal Records of the Cape Colony (about 36 volume scans over several copies, 91 ids incl. duplicates), Records of South-Eastern Africa (8 ids), Basutoland Records (4), Moodie's Record, Bird/Annals of Natal (3 of 4 readable), Precis of the Archives of the Cape of Good Hope (59 ids), Gold Coast and Sierra Leone parliamentary correspondence (about 12), Zanzibar, Bechuanaland, Gordon's journals (Hake, 2 editions), Gordon at Khartoum (Blunt), Story of the Soudan War, Too Late for Gordon, Emin Pasha, Oswell. Not covered: any Theal volume whose scan was `short/none`, and Theal volumes archive.org did not list. Explorer books were grepped in a separate step (`ia_explorers.py`, below).
Result: nearly all hits are figurative ("cyphering", "a mere cypher", "decipher the old records"). Real ones: Yonge/Prediger (row 2); Heren XVII to Riebeeck 1656 (cypher key sent, key lead); Riebeeck "alphabet (? in cipher)" (key lead); Gordon journals (row 1 and key lead); Emin Pasha (key lead); Egerton and Wolseley telegrams in Blunt and Soudan War as narrative only.
Calendars of State Papers Colonial: the archive.org series are America and the West Indies, and East Indies; none covers Africa or Barbary, so not grepped. There is no printed SP 71 (Barbary) calendar.

### Explorer books (`ia_explorers.py`)
139 ids from 26 title phrases (Livingstone's Missionary Travels, Zambesi narrative and Last Journals; Stanley's How I Found Livingstone, Through the Dark Continent, In Darkest Africa, Coomassie and Magdala; Burton's First Footsteps, Lake Regions, Zanzibar; Baker's Albert N'yanza and Ismailia; Speke; Emin Pasha; Slatin's Fire and Sword in the Sudan; Churchill-era Soudan books). 53 had no usable OCR, 86 were grepped (87 windows). Only narrative mentions: Slatin (a French-cypher message from Marcopoli Bey 1883; a half-ciphered Arabic telegram of Gordon to the Khedive read by Abdel Halim Effendi; a note written by Gordon "in French cypher language" shown to the Khalifa), Livingstone editors' "deciphering" of faded journals (handwriting, not cipher). No ciphertext printed. The Slatin and Gordon items are further Khartoum cipher pointers (originals unlocated), not rows.

### Hosts retried or newly tried
Wits (AtoM host), SAnA (eahra, nationalarchives.gov.za), Cory/NAHECS: retried, still no answer (connect failure). Rhodes University pages answer but the catalogues are an Alma JS app and `researchrepository.ru.ac.za` is Cloudflare-blocked. RGS: `collections.rgs.org` and `catalogue.rgs.org` no answer; the site's search page points to `rgs.koha-ptfs.co.uk`, Cloudflare-blocked (403). National Army Museum: answers, "cipher", "cypher", Zulu/Boer/Sudan/Egypt combinations, "code telegram", "secret code": 0 results each (simple search is object-level). IWM and Europeana: Cloudflare challenge (403). HathiTrust (babel and catalog): Cloudflare 403. Google Books API: 429 quota exceeded (stopped). Wikimedia Commons API: 429 (stopped); Wikisource API answers, one query only ("in cipher" Khartoum: 1 hit, Queen Victoria life, not relevant). Livingstone Online: no usable result.

### 20th century range
Nothing found with cipher text on an image. archive.org FTS for Mafeking, Ladysmith, Kimberley, Maji Maji: noise (biographies). TNA WO 108 / CO 417 series searches (pass 1): 0. The only 20th-century hits are 1906 FO telegram files (Liberia, Boma), administrative.

### Left after pass 2
Burton, Speke, Baker, Stanley, Livingstone printed editions (ids not collected by the title filter; do by explicit identifiers); Theal volumes with missing OCR; TNA CO 48 volume for 6 Jan 1801 and an image of the Prediger cypher; the FO plaintext of Egerton's telegram; Durham SAD.250 (IIIF works, covered by the north-east literature sweep); Bodleian, SOAS, LSE, Cambridge, RGS, Wits, SAnA, Cory still need a browser or another network.
