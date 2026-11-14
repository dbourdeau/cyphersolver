# North and East Africa and the literature route (14 Nov 2026)

Run by a Claude agent (Sonnet 5.5) for the project, one of four parallel Africa sweeps; contributor not named. Area: Maghreb and
Egypt, Ethiopia/Eritrea/Somalia, indigenous African scripts, and the literature (Tomokiyo, HistoCrypt/Lasry, Cryptologia, 20th-c.
liberation-movement ciphers). Nothing outside this folder was edited. Images stayed in a scratch directory.
`terms.log` holds every query with its hit count; the scripts here re-run them.

## Result

**2 candidate rows** (`candidates.json`), 1 with a complete vetting block, **4 key leads** (`key_leads.json`). Africa north and east
is thin on online ciphertext; the one real find came from the Durham Sudan Archive, which is digitised and open.

| Rank | Item | Seen | Notes |
|---|---|---|---|
| 1 | **Gordon at Khartoum, two-digit Arabic-numeral cipher note to the Mudir of Dongola**, Durham Sudan Archive, Wingate Papers SAD.250/1/550 (covering letter 549, Palmer to Grenfell, 15 Nov 1886) | image | One leaf, about 14 lines, roughly 80-95 groups, a few Arabic words in clear, Gordon's signature, year read as 1302 AH. Palmer: Gordon "evidently had a code", Khalil Ibrahim of Dongola "has the key". No decipherment on or with the leaf. Not on DECODE, not on Tomokiyo, no Lasry paper. Hansard 14 Nov 1884: four Arabic cipher letters from Gordon reached Debbeh. Free IIIF images. Vetting block complete (verdict open). |
| 2 | Hicks Pasha registers of telegrams 1883, Durham SAD.866/5/1-46 and SAD.600/2/1-35, "English, Arabic and cypher" | catalogue | Not digitised; unknown how much cypher text. Weak. |

Key leads: **SAD.250/1/81** (seen: a Nile Expedition cipher table, officers' columns plus Arabic letters and Arabic-Indic numerals,
digitised; a candidate key for row 1, untested), Abbas Hilmi II papers HIL/203/293-7 (cypher keys, WWI), Leach papers SAD.208/2/11-13
(word-letter cypher memorandum), and the Kitchener "Arabic cipher" telegrams (already inside lead 1159).

Next step for row 1: transcribe the groups from the IIIF image (a request returns at most 1024 px a side; ask for regions, e.g.
`.../47adbd88e481884e8d8dabcdef4935b1.jp2/200,0,1000,1000/full/0/default.jpg`), read the Arabic words and the date, then test
SAD.250/1/81 and the Kitchener Arabic-script telegrams (TNA PRO 30/57/4/77-109) as keys and cribs.

## Routes that worked

| Host | Route | Use |
|---|---|---|
| Durham Archives and Special Collections | `reed.dur.ac.uk/xtf/search?keyword=` and `view?docId=ark/32150_...;doc.view=entire_text`, plain curl. The finding aid links each digitised unit to `n2t.durham.ac.uk/ark:/32150/<id>.html`; IIIF manifest `iiif.durham.ac.uk/manifests/trifle/32150/<id[0:2]>/<id[2:4]>/<id[4:6]>/<id>/manifest`, images need no login | `durham.py`, `durham_ctx.py`, `dur_iiif.py` |
| TNA Discovery API | curl (python TLS is reset); `sps.searchQuery` is AND, `sps.dateTo` works; also indexes SOAS and other A2A holders | `tna_africa.py` |
| Europeana Search API | public `api2demo` key; Boolean works, matching is loose | `europeana.py` |
| archive.org full-text search | `services/search/beta/page_production` (fts backend); returns whole books, OR-like, no proximity | `ia_fts.py`; advancedsearch metadata also works |
| LoC search JSON | `loc.gov/search/?fo=json`, 30-45 s a call, sporadic 503 | `loc.py` |
| Persee search | HTML works, relevance is fuzzy | `persee.py` |
| Wellcome catalogue API | works, 0 relevant | `wellcome.py` |
| Tomokiyo cryptiana | `cryptiana.web.fc2.com/code/*.htm`: all 295 pages linked from `crypto.htm` fetched and grepped for African terms | scratch only |
| Gutenberg | Hake's edition of Gordon's Khartoum journals (49224) searched for cipher | scratch only |

## Routes that blocked or gave nothing

DPLA 403 (needs a key); Google Books API 429 at the first call (stopped); NARA catalogue (JS shell, API needs a key); Founders Online
(HTTP 202 JS gate); Calisphere (202); FranceArchives (JS and cookie redirect that loops with curl); Internet Culturale (bot-check form,
not touched); Archives Hub 403; Cambridge ArchiveSearch 403; Bodleian Archives (Anubis proof of work); IWM collections 403;
Europeana web UI 403; HathiTrust and quod.lib.umich.edu 403; Gallica, PARES and BNE as per `COVERAGE.md` (not retried);
Wikimedia Commons and Wikisource answered with non-JSON (rate limit) after a handful of calls, stopped; EAP (BL) 202 JS gate; CUDL
(per the Hebrew sweep); Dar al-Kutub, Bibliotheca Alexandrina, MECA Oxford, SOAS Calm and ANOM did not answer (connection failure); Delpher answered but its result pages were not parsed (not tried further). None of these needed Chrome for a result that I could not get elsewhere, but all of them would
need it for a real sweep: FranceArchives (ANOM, Maghreb protectorate files), Internet Culturale, Founders Online, NARA.

## Search terms and hit counts

Complete per-query counts are in `terms.log`. Summary:

- **TNA Discovery**, 25 places x 6 terms (cipher, cypher, "in cipher", decipher, cryptogram, code telegram) to 1950: 64 of 150 queries non-empty. Read by hand: all pre-1940 non-Hansard rows. Relevant: Kitchener papers PRO 30/57/4 (already lead 1159; PRO 30/57/4/119 already catalogue 356), SOAS Mackinnon Emin Pasha file 56 p.261 (cipher telegram re Tippoo Tib, 28 Mar 1890, summarised so read). Everything else was WW2 HW/AIR/WO files, FO file-code strings ("code 16"), or monograms.
- **Durham XTF** keyword counts: cipher 23 items, cypher 26, ciphers 23, cyphers 26, cryptogram 3, decyphered 2, deciphered 17, undeciphered 2, "in code" 909 (noise), coded message 2, cypher telegram 4, secret code 2, code book 17, cryptic 21, plus "invisible ink", "numerical code", "secret alphabet", "cipher key". Every Sudan Archive / Middle East record among them was opened and the cipher contexts read (Wingate, Slatin, Hicks, Abbas Hilmi II, Clayton, Dingwall, Foley, K. Wood, G. Wood, Aglen x2, Fouracres, Hebbert, Leach, Kenrick, Piper, Wylde, Eden, R. Russell, Roper, Acland, Sarsfield-Hall, Allison, King, Mavrogordato, Bollard, Manton, Macphail, Bloss, Sandison, R. L. Hill, Baker Baker, Lowe, Cunnison, Manwell, McReavy). Most mention "cypher officer" or cypher clerk posts (1938-1947) and nothing else.
- **archive.org FTS**, 13 co-occurrence queries (e.g. "in cipher" AND Tangier AND consul 237, ... AND Khartoum AND Gordon 354, "cipher" AND Mahdi AND telegram 14): book-level hits, dominated by encyclopaedias and dictionaries; unusable. Not repeated.
- **LoC**, 10 queries (519 to 2,544 hits): only commercial telegraph code books and Theodore Roosevelt Papers noise.
- **Europeana**, 21 queries: none relevant (BnF Arabic-numeral "chiffre" noise, museum scarabs).
- **Wellcome**, 8 queries: 1 hit, irrelevant. **Persee**, 5 queries: no relevant title in the first ten of each. **Commons**, 7 queries: book scans only.
- **Web searches** (Gordon cipher; Barbary consul ciphers; Adwa/Baratieri; German East Africa codes; Mau Mau; Operation Vula; FLN; Lasry/HistoCrypt Africa; Azizi Morocco; Ethiopian asmat; Ge'ez ciphers): see Literature.

## Literature route

- **Tomokiyo** (295 pages grepped): no Africa page. African mentions only in passing: the Luederitz 1911 consular telegram (already catalogue 356), Jefferson's codes for Barclay (Morocco) and Lambe (Algiers) in `jeffersn.htm` (US material, other sweeps), GL.htm Duquesne on the Tripolins (French, 17th c.), the Schiner 1520 page, and the Cryptologia index entries for Azizi and Azizi, "Instances of Arabic Cryptography in Morocco" I and II (Cryptologia 35 (2011) and 37 (2013); Moroccan treatises and examples, not unread ciphertext as far as the abstracts show; full text not obtained).
- **HistoCrypt / Lasry**: the only African item found is Bean, Lasry and Weierud, "The Biafran Ciphers" (Lisbon-Biafra telex, transposition, 1967-70; out of range). Nothing on Egypt, Sudan, Ethiopia or the Maghreb.
- **Gordon journals** (Hake edition, Gutenberg 49224): Gordon repeatedly writes that he cannot decipher telegrams from Egerton, Wolseley, Nubar and Baring because Stewart took the cipher books, and that three long cipher telegrams are "pasted on the other side" of journal pages; he also says he captured the European telegrams in cipher. The journal manuscripts (British Library; shelfmark not verified here) would hold those pasted telegrams: a lead to check, not entered as a row because I did not see the pages or confirm the shelfmark.
- **Barbary consuls**: Eaton's Tunis letter of 9 Oct 1802 gives its cipher key from the Lear family papers (Founders Online footnote), so the Eaton/Lear cipher is keyed and printed; no unread consular cipher was found. The Naval Documents of the Barbary Wars volumes (ibiblio, archive.org) were not grepped.
- **Telegraph code books** (LoC hits: Bennett, Watkins, Marconi, Bentley's, Slater's Telegraphic Code 1890): printed commercial codes used on colonial telegrams. Key material only.

## In scope per BRIEF but not found

Barbary-state, Egyptian and Ethiopian diplomatic or consular ciphers 1500-1900 with images online: none found beyond row 1. The sources that would hold them are not online or are gated: TNA SP 71 and FO 3/FO 99 (not digitised, catalogue text does not mark cipher), Spanish AHN (PARES blocked), Dutch Staten-Generaal "secrete brieven Barbarije" (inventory-level, nothing marks cipher; see the Dutch sweeps), Venice and Medici (BIA unreachable), French ANOM and the Nantes protectorate files (FranceArchives gated), Italian colonial files (not online).

## Exclusions and out-of-range items (README only)

- **Scripts, not ciphers; left out unless a concrete cipher text exists**: Nsibidi (ideographic signs; no cipher text), Vai, Bamum, Mende (Kikakui), Loma (syllabaries, read and documented), Adinkra (symbol set), Ajami (African languages in Arabic script), Tifinagh and Libyco-Berber (partly read; the unread part is a language problem), Meroitic (phonetically read since Griffith 1911, language mostly not understood: a language problem, not a cipher), Garamantian (no distinct script identified). Sudanese and Timbuktu talismanic magic squares (wafq) and ta'miya ring-letter writing: D'Ottone's work is in the Arabic sweep (SOAS MS 12217, Mashhad); none seen as new ciphertext.
- **Ethiopia**: asmat scrolls and "caracteres a lunettes" (magical signs; secret divine names) are talismanic scripts, not enciphered messages; no Ge'ez cipher text turned up. No Jesuit mission cipher letter was found online (the AHU/Torre do Tombo side is the Portugal sweep's). Italian colonial codes 1880s-1930s: no source online.
- **Already read or glossed**: Wingate SAD.255/1/328-329 (translation of a cypher telegram, Tripoli, 1893), SAD.138/12/7-10 ("decyphered telegram", 1916), Kitchener PRO 30/57/4 "code and translation" items, SOAS Mackinnon 1890 Tippoo Tib telegram (content summarised), Eaton's Tunis cipher (key printed).
- **Out of range (after 1950)**: Biafra 1967-70 (Bean, Lasry, Weierud); Operation Vula (ANC, 1988-90; software released 2024, one-time pad); FLN/ALN signals in the Algerian war (no cipher source found; French SHD files); Mau Mau (nothing coded found; the Hanslope Park migrated archive is at Kew); FRELIMO (nothing searched beyond this). WW2 North Africa (Fellers "Black Code", Italian codes, GC&CS HW files, TNA AIR 29/711, HW 3/19): solved or administrative.
- **Administrative**: Durham "cypher officer" biographies (1938-47), FO 371 1906 "Abyssinia: code 1" file codes, MINT medals with "cypher" monograms, "Bentley's Phrase Code" (NAM).

## What is left

1. Row 1 transcription and the key test (Durham images are free). Also scan the other 734 Wingate digitised units for further Arabic-numeral pages: the finding aid does not describe them as cipher, so only paging finds them (start with the Nile Campaign units SAD.250/1/1-58, 134-226, 1884-85, and SAD.255/1/294-371).
2. Gordon's Khartoum journals (BL) with the pasted cipher telegrams; Hake's apparatus for each numbered item.
3. TNA PRO 30/57/4 Kitchener Arabic-script telegrams (lead 1159) against the SAD.250/1/81 table.
4. Hosts that need Chrome: FranceArchives (ANOM, Nantes), Internet Culturale, Founders Online, NARA Catalog (Barbary consuls), Archives Hub, Bodleian Archives (Rhodes House Africa), Cambridge ArchiveSearch (RCS, Churchill), IWM, EAP.
5. Naval Documents of the Barbary Wars (7 vols) and Cathcart's letterbook: grep for printed ciphertext with no editor's decode.
6. Azizi and Azizi (Cryptologia 2011, 2013) and Azizi (C2SI 2019): check for Moroccan manuscript ciphertexts.
7. Not searched at all: Egypt under Muhammad Ali (French consul Drovetti files, Napoleon's Egyptian campaign ciphers), Mamluk chancery (the Arabic sweep covers the treatises), Somali and Eritrean colonial files, Italian state archives for Eritrea, Sudan Archive collections not matched by a cipher word.
