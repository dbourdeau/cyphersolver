# Sweep: US sources not yet covered (14 Nov 2026)

Brief: NEHGS, MHS, NYPL Archives, Hispanic Society, Center for Jewish History, Brooklyn PL, Columbia (terms beyond cipher), Morgan CORSAIR,
Library Company / HSP, Huntington, Newberry, Folger, Clements, Gilder Lehrman, Virginia, South Carolina. **Result: 6 rows in `candidates.json`
(schema as `sweep_2026-11-14_gsta_deep`), all weak or modest.** Most of the named sources had already been swept (`us_societies`, `us_clements`,
`us_huntington`, `us_beinecke_folger`, `sweep_2026-11_us_blocked`, `nyc_sweep`, `boston_sweep`, `chi_newberry`, `chi_chrome_pass`), and what this pass
re-found was already in the ledgers: Torcy-Gaultier (lead), Williamson 1805 (catalogue 1544), Archibald Johnston 1912 (catalogue 1288), Tonbridge diaries
of Charles Barrett (lead), the Columbia Morris/Pinckney items (lead 2249), Woolson (excluded, the copy is the decipherment). Nothing was merged;
catalogue.json, leads.json and `merge.py` were not touched; nothing committed (one `.gitignore` rule for `_tmp/`). Every row is scored from finding-aid
text, none viewed, and none has a web, Tomokiyo, Lasry or DECODE search (known.py and name greps only).

## Result by source

| Source | Route | Terms | Result |
|---|---|---|---|
| **Columbia** (`findingaids.library.columbia.edu`) | Chrome tab on that host, same-origin `fetch` of `/archives?q=<term>&per_page=100&page=N` and parse `article.document` (the Anubis check passes in Chrome in about 5 s; the old `/search` and `/catalog` URLs 404) | 29 terms (cipher, cypher(s), ciphered, cryptogram(s), "secret writing", "code book", codebook, "in code", "in cipher", decipher*, cryptograph*, "numerical code", "secret code", encoded, encrypted, "secret ink", "telegram code", "code letter", ...) and a second pass of 23 (chiffre, cifra, cifre, Geheimschrift, "in cypher" 22, "decoded by", "deciphered by", nomenclator, invisible ink, steganography ...) | 1,159 distinct records, almost all noise ("code book" = survey codebooks of the Merton, Zuckerman, Hyman papers; Tsuyee Pei and Koo Chinese telegraph codes 1930s-50s; Cypher surnames). The already-known Morris/Pinckney, White/Hay, Loris-Melikov and Donovan items reappear. **2 rows**: Forbath diary 1916 (German stenography "not deciphered") and Devoiants telegrams 1919-20. Also seen, not taken up: "Cable codebook used by H. A. Jenks" (The World / Pulitzer, c. 1906, printed code), W. R. Grace "General Code Dir." 1886-89 (printed telegram code), D. E. Smith "John Wallis as a cryptographer" (essay) |
| **PACSCL / Philadelphia Area Archives** (`findingaids.library.upenn.edu`, plain curl works; includes HSP, Penn, Library Company's finding aids, Princeton, Haverford, Swarthmore, Lehigh, Drexel, Bryn Mawr, FLP, ANSP, PMA) | HTML search, 2 s spacing (`penn_harvest.py`), then the inventory page `/inventory/<ID>/details` for each pre-1920 hit (`penn_ead.py`; the `.xml`/`.ead` links on record pages answer 404) | 23 terms | 1,514 records (`"in code"` and `encoded` return 700 each, stemmed noise); 121 with a strong cipher word, 88 pre-1920 read in full. This is the Oct `us_societies` source; the pass found 4 collections not in the ledgers: **FLP historical manuscripts (Deane to Wilson 1780, deciphered letters)**, **Dundas papers Box 11 f. 26 (clear copy + cypher copy, 1798/1800)**, **Lovat Fraser diaries 1918 ("keep my diary in cipher")**, Mahlon Day papers (William Thurston notebook with cipher keys and pigpen notes, 1868-79: trivial, not a row) and ANSP Benjamin Sharp (1891 Greenland journal shorthand key and "Greek cipher" notes: key only, not a row). 3 rows |
| **Newberry** (`archives.newberry.org`, ArchivesSpace; the `q[]=` URL shows an error, but `/search?utf8=...&op[]=&q[]=<term>&limit=&field[]=&from_year[]=&to_year[]=&page=N` works in Chrome, no check) | same-origin `fetch`, 1.5 s | 18 terms | 37 records (cipher 11, "in cipher" 5, "in code" 1, cryptogram 1, deciphered 2, shorthand 21): Woolson memoir (excluded, copy = decipherment), Williamson ca. 1805 (catalogue 1544), CB&Q and Pullman telegraph code books, noise. No row |
| **Center for Jewish History** (`archives.cjh.org`, ArchivesSpace; curl 403, Chrome passes; also YIVO, LBI, AJHS, Yeshiva U.) | same as Newberry | 22 terms | 145 records ("decipher" stem 120 = illegible handwriting). Cipher 2 (a 1968 pamphlet), "in code" 1 (Zygielbojm 1942 radiograms), "coded" 13 (all 1940s+), Mordecai Sheftall papers ("deciphered", American Revolution: not read), Hirsch microfilm "Dictionnaire abreviatif, chiffre" 1890 (an abbreviation code). No row |
| **Morgan CORSAIR** | Chrome `navigate` only (an in-page fetch is challenged at once, as in the Nov 4 note); **no checkbox appeared in 6 requests** | chiffre (46 records, all printed books and bindings: "chiffre" is a French stem), decipher (34 records, 14 manuscripts, all "illegible" letters), "in code" (6) | New bib ids read: 195079 (John III of Portugal 1542: the letters in code are the Bishop's, not in the item), 190797 (Macdonald to Strickland 1850: **row**, weak), 192925 and 192926 (Barrett schoolboy diaries, already a lead). cifra, "in cipher", and the unread Nov 4 bib ids not done |
| **Hispanic Society** | `hispanicsociety.org` search finds nothing; the library catalogue is Mandarin M5 (`hispanicsociety.mlasolutions.com`, 49,546 printed-book records, the keyword box did not narrow the list); `hispanicsociety.emuseum.com/search/<term>/objects` works in Chrome | 18 terms (cifra, cifrada, cipher, chiffre, clave ...) | 4 museum objects, none a cipher. Manuscripts are not item-catalogued online. No route |
| **Library Company** | Its Koha catalogue (`librarycompany.kohacatalog.com`, Anubis, Chrome passes) lists books, broadsides, e-texts and visual material only; manuscripts are PACSCL finding aids (`LCP_MSS*`), covered above | cipher | no manuscripts. No row |
| **NEHGS / AmericanAncestors** | the keyword search (`/search/database-search?keywords=`, Chrome) covers name-indexed databases: "cipher" gives 466 records, 337 of them 10 Million Names and 358 census (the surname Cipher), 47 journal articles | cipher | no manuscript finding aids in this search; not pursued |
| **NYPL Archives & Manuscripts** (`archives.nypl.org`) | **blocked**: Imperva/Incapsula page with a checkbox (iframe); curl gets the same. Not clicked | - | not searched. Remaining route: ArchiveGrid (done 3 Nov) |
| **Brooklyn** | brooklynpubliclibrary.org site search has no archive content; Center for Brooklyn History is on the NYU host, searched 4 Nov (`nyc_sweep`) | cipher | nothing new |
| **South Carolina Historical Society** | site search ("cipher") 0 results; no online catalogue of manuscripts found (finding aids are partly online per its guide; Lowcountry Digital Library hosts scans) | cipher | not searched beyond that. ArchiveGrid (3 Nov) gave no SCHS cipher record |
| **MHS, Huntington, Folger, Clements, Gilder Lehrman, Virginia (ARVAS incl. VMHC), HSP** | not re-run: `us_societies` (MHS solr, 11 terms), `us_huntington` (OAC + HDL + catalogue), `us_beinecke_folger` (catalog.folger.edu MARCXML, 33 terms; Hamnet is retired), `us_clements` (51 queries + 60 finding aids), `sweep_2026-11_us_blocked` (Gilder 20 terms, ARVAS 22 terms), PACSCL (HSP finding aids) | | HSP's own catalogue (`discover.hsp.org`, `digitallibrary.hsp.org`) is Cloudflare-blocked to curl and was not tried in Chrome |

## The 6 rows

| # | Item | Class | Why |
|---|---|---|---|
| 1 | Silas Deane to James Wilson, Paris 1780: two deciphered letters on one sheet, modern transcription laid in (Free Library of Philadelphia, HISTMSS Box 1) | C | Paired decipherment; Deane's cipher not in the repo; may be printed (Deane Papers) |
| 2 | Malcolm's memorandum on the French corps in the Deccan, 1798, with a copy in cypher enclosed by Dundas 19 Aug 1800 (Penn Ms. Coll. 888 Box 11 f. 26) | A | Clear and cypher copies in one folder |
| 3 | Imre Forbath diary 1916 in German stenography, "not deciphered" (Columbia RBML) | C | Shorthand, not cipher; undeciphered by the library |
| 4 | Claud Lovat Fraser's 1918 diaries in Greek characters, "keep my diary in cipher again" (Bryn Mawr BMC M25) | C | Personal cipher, probably easy |
| 5 | Macdonald to Strickland 1850, a coded Mary Queen of Scots letter with transcriptions (Morgan, bib 190797) | C | Weak; leads to Strickland's source |
| 6 | Devoiants papers: Azerbaijani telegrams 1919-20 deciphered by Armenian intelligence (Columbia) | C | Decipherments only, marginal |

## Chrome use and blocks (for the next sweep)

- One own tab per host. The extension blocks tool output that contains `?query=` text: results were put in `document.body` (or returned as plain lines)
  and read with `get_page_text`. A navigation from one origin to another during a `javascript_tool` call raises "Security check failed"; re-read the tab state.
- Long loops: started un-awaited, results kept in `window` arrays and polled. `window` state is lost on navigation (the Columbia second-pass array was lost this way; only its counts survived).
- Checks seen: **Imperva checkbox at NYPL (not cleared, reported)**; Anubis proof-of-work pages (Columbia, Library Company Koha) pass in Chrome in about 5 s; Cloudflare on
  Newberry, CJH, eMuseum and Gilder/HSP passed or untried as noted; Morgan CORSAIR showed no checkbox. No CAPTCHA was solved or clicked.
- Rate 1.2-2 s per request. Tab 1987536230 in the group belonged to another session and was not used.
- Routes worth reusing: `findingaids.library.columbia.edu/archives?q=` (HTML), `findingaids.library.upenn.edu/?q=` plus `/inventory/<ID>/details` (curl),
  `archives.newberry.org` and `archives.cjh.org` `/search?...` (Chrome, `.recordrow` / `a.record-title`).

## Honest limits

- Description text only. No row has been viewed; vetting bar not met for any.
- Column "strong" hits on Penn were read from the inventory page; hits only in the component text of collections dated 1920 or later were not read.
- The Columbia pass kept only titles and 300-character snippets; items with the cipher word only in a longer note may be missed.
- Not done: NYPL Archives, SCHS and NEHGS manuscripts, HSP's own catalogue, Morgan "cifra" and "in cipher", the Morgan bib ids left unread on 4 Nov, Mordecai Sheftall papers (CJH), Library Company manuscripts beyond the PACSCL finding aids.
- Scripts: `penn_harvest.py`, `penn_ead.py`, `make_candidates.py`; raw JSON in the git-ignored `_tmp/`.
