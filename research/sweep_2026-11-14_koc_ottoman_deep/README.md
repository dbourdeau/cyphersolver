# Sweep: Koç CONTENTdm in depth, SALT, Persian/Egyptian, Commons, Europeana (14 Nov 2026)

Result: **6 rows in `candidates.json`** (`make_candidates.py`), same schema as `sweep_2026-11-14_russia_ottoman_nordic`.
Not merged, catalogue and leads untouched, nothing committed. `img/` (about 100 HPBK page images, CC BY-NC-ND 3.0 Koç)
and the contact sheets are working files and should stay out of git.

## What the deep pass found

**Koç holds nothing outside HPBK and MHC.** All 50 collections of `cdm21054.contentdm.oclc.org` were searched with 50 further
terms (`koc_all_terms.json`: şifre kâtibi, şifre kitabı, rumuz, remz, muamma, cifr, jafr, kod, code, coded, secret
writing, steganography, çözülemedi/çözümlenemedi, telgraf ...). Hits outside HPBK/MHC are noise: IR (institutional
repository theses on "code"), VGK press clippings ("muamma" = mystery), MC manuscripts (cifr = *Risāle-i Cifr ve Ed'iye*
MS 259, jafr divination; *Mecmū'a-i Mu'ammayāt* MS 189, riddle poems; Cezeri tajwīd "hurûf"), KUCIM (quantum cryptography
clipping). HPBK (1,040 records) and MHC (558) were enumerated whole (`hpbk_all.json`) and scanned for 25 cipher words in
title, description and subject: 121 HPBK records name a cipher; 117 were in the previous sweep, the other four are noise
("çözüm" = solution). Nothing new in titles, so the gain is from the images.

**The pages show two cipher systems and a crib on the page.** About 100 of the 122 cipher-titled HPBK images were fetched
(the rest 502 repeatedly) and a 12-up contact sheet of the telegram forms was read. The catalogue lumps them as "encrypted
telegram, content could not be deciphered"; they are not alike:
* **System A**, five-digit code groups (the 1898 sheets 772/688/533 are of this kind), with **Turkish words written over
  or between many groups** by the clerk: 563, 595, 600, 560, 542, 579, 550, 568, 556, 551, 565, 581 (1900-1902). A partial
  reading on the page.
* **System B**, a stream of **two-digit numerals (about 44-49, 55-59, 64-71) with one Arabic letter written over most
  numbers**: 546, 562, 575, 576, 577, 578, 580, 585, 587, 599, 602 (1896-1901). A letter-by-letter reading on the page.
* **Clear sheets** catalogued as "encrypted document": 725 (28 Apr 1901, the day of 578/599), 726 (5 Jun 1901, the day of
  576), 1070, 1068, 764 and 1859 are plain Ottoman fair copies, not ciphertext; 727 is the clear translation of 18 Dec 1898
  (already in the previous sweep). Many telegram forms (641, 665) are clear text too, so "telegram form" does not mean
  cipher; the page-shape classifier in `classify.json` is not reliable and was only used to pick images to look at.
* Same-day clusters of cipher plus clear items (44 dates, listed by the script in the session; main ones): 21 Feb 1901
  (595, 600), 28 Apr 1901 (578, 599, 725, 729, 748), 5 Jun 1901 (576, 726, 764), 9 Apr 1902 (542, 579, 732), 13 Apr 1902
  (550, 568, 766), 15 Feb 1900 (563, 569), 6 Feb 1900 (575, 1070), Oct 1902 Italian ultimatum (551, 447 and about 20 clear
  telegrams of 15-17 Oct).
* HPBK 1791 "document on special encryption book" never loaded (502 five times): the one item that may be a key.

Rows 1-3 follow from this. The two systems are split from each other and from the 1898 five-digit sheets (previous sweep,
row 1) on the one-key-per-entry rule; merge them if A is one code with the 1898 sheets.

## Other sources

| Source | What was done | Result |
|---|---|---|
| SALT Research (archives.saltresearch.org) | curl 403 (Cloudflare "Attention Required"); the 2 Nov sweep ran 18 terms in Chrome (Eldem diary only) | Not repeated. Gap remains for Ottoman Bank and Ali Ekrem-type collections: no new term list tried |
| QDL pre-1900 (IOR Persia/Gulf) | Chrome, same-origin fetch of `/en/search/site/<q>?f[0]=date_range:[1800 TO 1899]` for cypher, cipher, decypher, decipher, "in cypher", code (206 records, 33 naming a cipher) | The earlier QDL sweep stopped at 1900. New: Morier 1808 numerical-code letters IOR/L/PS/9/67/18-21 (row 4). Not new: IOR/L/PS/9/76/212, /217 (Jones 1802, target jones1802) and R/15/1/134 f. 32 (1852, Armenian script, not a cipher). Translations of ciphered Persian letters, no ciphertext: IOR/L/PS/9/71/128 (Mu'tamid al-Dawla, 1827), IOR/L/PS/9/69/164 (Abbas Mirza coded letter, 1824), IOR/L/PS/9/67/75, /91 (Malcolm 1810 "deciphered"), IOR/G/29/32 (cypher dispatch to Gardane, 1810, excluded from the copy) |
| Open Jerusalem (Ali Ekrem Bey collection, 1907 encrypted telegrams) | WebFetch ECONNREFUSED, Chrome navigation did not complete | Row 5 from a search-engine snippet only |
| Europeana API (`api2demo`) | `eu3.py`: 20 terms (şifreli, ramz, rumuz, chiffre, code secret, Geheimschrift ...) with Turkey/Ottoman/Persia/Egypt filters, 122 records | Noise: Koç's own 1921 items, BnF Persian/Turkish literary manuscripts, printed cipher manuals (Bavarian State Library, ÖNB: Fleissner 1881, Sittler 1889, "Dictionnaire chiffré" 1851), Judeo-Moroccan postal letters 1897-1909 matched "code secret" generically (not checked). 0 rows |
| Wikimedia Commons | `commons.py`: 30 terms, namespace 6; the API throttled about a third of the calls (HTML, not JSON) | Milliyet issues 1929-34, books, Internet Archive PDFs, Selim I tughra. No Ottoman cipher telegram. Persian/Egyptian/Arabic-cryptography terms were among the throttled calls; not retried |
| Atatürk Library (katalog.ibb.gov.tr) | not retried (no connection in the 2 Nov sweep) | not reached |
| BOA (katalog.devletarsivleri.gov.tr) | not retried: login with an arithmetic CAPTCHA, never solved | blocked; HR.ŞFR, DH.ŞFR (Ben-Bassat, Turcica 46, 2015, WWI telegrams to Syria with 9 coding types; Cryptologia 2023, 1811-1877) are the places to ask the owner for |
| Egyptian Khedival / Qajar | web search (2 queries) and the QDL pass | Qajar: Iranica's "romūz" entry and Meftāḥ-al-Molk's cipher manuals only; no Khedival cipher archive item found. Yale Ghani Qajar collection shows no cipher items in search snippets (not searched in depth) |

## Blocks and routes

| Source | Block |
|---|---|
| Koç image server | 502 on first request, often on retries; 23 of the 122 cipher-titled items never loaded in about 30 minutes of polite requests (199, 477, 483, 486, 495, 498, 518, 524, 527, 533, 536, 620, 688, 1160, 1761, 1791 among them). Needs a later pass |
| qdl.qa | Cloudflare 403 to curl/WebFetch; opens in Chrome; same-origin fetch of search pages works (about 1 s per page) |
| archives.saltresearch.org | Cloudflare 403 to curl |
| openjerusalem.org | unreachable from Python, WebFetch and Chrome |
| BOA | CAPTCHA login (not solved) |
| Shared Chrome | another session was using the browser; my tab was closed |

## Next

1. Transcribe 600 and 595 (same day, system A) and 576/578 (system B); tabulate the over-written words and letters; test on the
   rest of each system. System B is the best bet: a letter above every numeral on pages with a plain reading of the same days.
2. Re-fetch the 23 missing images and the 1791 cipher-book item; open 732/766 and the Oct 1902 clear telegrams as cribs for 551.
3. Open the Morier 1808 files in Chrome (row 4) and the Open Jerusalem records from another network (row 5).
4. DECODE: none of this is on DECODE as far as known.py shows; a queue entry for the two systems is owed if a reading follows.
