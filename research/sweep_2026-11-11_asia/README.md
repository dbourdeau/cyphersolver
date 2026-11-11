# Asia sweep, 11 Nov 2026 (cloud session): Abhilekh Patal, JACAR volumes, IMH notes

Result: **10 rows in `candidates.json`, all archive-description leads (no vetting block)**; 4 key leads in
`key_leads.json`; notes on the 18 existing Abhilekh leads (`abhilekh_leads_notes.json`) and the 9 IMH leads
(`imh_leads_notes.json`). JACAR volume hits: opened, nothing to add.

## Routes from this network

* **abhilekh-patal.in**: answers plain HTTP requests (search pages and item pages, HTTP 200). Only the search and
  ItemDetails pages were used. No headless browser, no Document Viewer form, no PDF from s3.abhilekh-patal.in, no
  login: page images were **not** seen for any row (coordinator rule, 11 Nov). Paging is slow (about 17 s a page).
* **jacar.archives.go.jp**: `/aj/search` and `/das/meta/<ref>` answer. `/das/image/<ref>` returned **404** here, so the
  PDF recipe of `research/jacar/pdf.py` did not work and no JACAR image was viewed.
* **archivesonline.mh.sinica.edu.tw**: no answer (curl exit 35), as on 6 Nov. `catalog.digitalarchives.tw` and its
  cover thumbnails answer 200.
* **qdl.qa**: 403, skipped. **de-crypt.org** RecordsList search answers (used for prior art).

## 1. Abhilekh Patal

`research/asia_india/README.md` describes the portal. Scripts here: `ap.py` (copy of the client), `ap_first.py`
(first page under title asc and desc, logs counts to `first.log`), `ap_details.py` (item pages ->
`ap_details.jsonl`), `ap_filter.py`, `make_candidates.py`.

* **title=cypher (4,507 now)**: re-paged under the stable sort `dc.title,asc` rather than resuming the date sort
  (the old file's date sort was not in year order). Stopped by hand at page 230 of 451: 2,012 records in
  `hits/title_cypher_titleasc.jsonl`, 1,381 of them new; with the October files 2,865 distinct records have now
  been read. **Pages 231-451 of the title sort are still unread**: resume with
  `python3 ap.py hits/title_cypher_titleasc.jsonl title=cypher,contains --start 230`.
* Phrase queries (title field; a multi-word value is a phrase; counts in `first.log`): cipher telegram 63, code telegram 103,
  cypher messages 77, cipher messages 28, code messages 24, intercepted telegram 41, Chinese cypher 16, foreign cypher 30,
  Russian cypher 7, German cypher 6, Chinese code 6, Chinese telegrams 5, undeciphered 7 (seals, as in October),
  secret code 6, Afghan code 6 (law codes); 0 for: cypher telegram undeciphered, letter in cypher, cypher letter,
  Persian / Afghan / Turkish / Bolshevik / Japanese / French / enemy cypher, Russian code, German code. "in cypher"
  is not a phrase to the server ("in" is dropped: 4,507). Two `title=` values are not ANDed, and `branch=` is not a
  search field. Only the first 10 hits under each of two sorts were read for the queries above 20 hits.
* The record pages still carry only title, department, branch, file number, pages and OCR keywords. No abstract,
  no free preview. So "ciphertext is in the file" rests on the titles.

### What was found

The productive vein is not the pre-1900 consultations but the Foreign Department's own **Cypher Confidential** and
**Deposit Cypher** series, 1904-1917, where the Cypher Branch handled *foreign* cipher telegrams taken off the Indian
telegraph system for the Intelligence Branch / General Staff. Most records exist twice or three times (PR_0000040...,
PR_0000060..., PR_2112...; same file, same size). Rows, best first:

1. 1912, Deposit Cypher Nos. 86-87 (PR_000004118254): "Message in Chinese Cypher from Yaoshikinan [Yuan Shikai], Peking which cannot be properly decyphered", 14 pp.
2. 1904-05, Confidential B Frontier, File 67/77 (PR_211200042292): Russian cypher telegrams obtained at Meshed and the Russian Consul at Bombay's telegrams, 72 pp.
3. 1907-09, Confidential B External C, File 45506 (PR_000006228785): Chinese officials' cypher telegrams in the Chumbi valley, with Capt. Campbell's key, 40 pp. (class B).
4. 1908-15, Cypher Confidential File 19/45 (PR_000004147891) and five siblings: Chinese telegrams acquired for the General Staff, 67 pp.
5. 1908-12, Cypher Confidential 1909 Nos. 72-75 (PR_000004129547) and siblings: foreign cypher telegrams acquired in Persia and the Gulf, 89 + 44 pp.
6. 1916, Cypher Confidential File 72/81 (PR_000004051912): German cypher messages intercepted at Bushire and Butcher Island, 26 pp.; sibling 1915 Bushire code books file, 87 pp.
7. 1917, Deposit Cypher No. 19 (PR_000004084171): Chinese code telegrams intercepted by the Canadian censorship, 71 pp.
8. 1917, External-B Nos. 38-42: Siamese Government cypher telegrams detained at Rangoon, 18 pp.
9. 1920, External-B: German Legation Tehran cypher telegrams given to the Russian expert Jukowsky, 14 + 26 pp.
10. 1943, External 79-X-43-Sec.: Tibetan Government code message via the Lhasa mission wireless, 32 pp.

No row has a vetting block: nothing was viewed, the descriptions are titles, and a decipher inside a file cannot be
excluded. Prior art run: DECODE RecordsList searches (Bushire, Canadian, Chinese telegram, Tehran, Kabul, Meshed,
Yatung, Tibet, Siam, Yuan: 0 rows each; "India": 5 rows, so the search works), grep of the repo `unsolved.htm`,
`known.py` (Yatung, Meshed, Chumbi, Jukowsky, the PR numbers: no hits; Bushire hits only the QDL 1918-26 entry),
and five web searches (in the rows). Rows 8-10 had no web search of their own.

### Excluded

Code administration (supply, issue, withdrawal, safe custody, post copies, paraphrase rules, staff): well over 95% of
hits again. Government telegrams "in cypher" with their decyphers. "Translation of code messages found concealed on
Ghulam Reza near Kermanshah, 1918" (NAIDLF00578521; read, kept as a key lead). "Decyphering ... of an unintelligible
cypher message from Macartney", 1908 (PR_000006260229; a British message). Censorship files about foreign consuls'
right to use cipher (Russian Legation Tehran 1919, Persian Consul Basrah 1916, Japanese consul Simla 1919, Italian and
allied consuls 1915, Japanese mission Yunnanfu 1917): policy, no text implied. 1914 "interception of telegrams
including cypher telegrams to and from Tibet" (PR_000007023974, 6 pp.): policy. Nothing pre-1900 beyond the October
rows turned up in the pages read (1878 "concluding portion of your cipher message" is a clear telegram about one).

### The 18 existing leads (1354-1371)

All 21 record pages were fetched again (`ap_details.jsonl`). Each shows the same metadata as on 28 Oct and nothing
else: no description, no preview; images only through the login. `abhilekh_leads_notes.json` gives, per lead id,
the title, file number, pages and OCR keywords as seen. They stay unvetted.

## 2. JACAR: volume-level hits

`research/jacar/cands_raw.json` (the 144 undated volume hits) is git-ignored and absent from this checkout, so the
set was rebuilt: `jacar_volumes.py` runs the 28 October terms with the level filter `f_type=2` (簿冊). **75 distinct
volume records** (`jacar_volumes.jsonl`): 暗号 20, 密書 39, 傍受 7, 暗号書 4, 密電 3, 電信暗号 3, 隠語 3, 秘密通信 2,
暗号電報 1, 電報 検閲 1, the other terms 0. `jacar.py` here parses volume rows (their link is `?fond=<ref>`), and
`jacar_open.py` lists the items under a volume (`jacar_vol_items.jsonl`). 16 volumes were opened, chosen by title;
the rest are Japanese code-book custody, 機密書類 registers and broadcast-monitoring files.

Opened, nothing for the catalogue:
* C09085472400 (1877, Seinan war, 39 items): 暗号 here means the weekly challenge-and-answer passwords and bugle signals.
* A06040058900 (Sasebo prize court, 1904-06): office correspondence on its own telegraph code.
* A06040124100 / 124300 / 124500 (prize ship Fuping "secret papers", 1904): a Letts diary, an English letter of
  8 Oct 1904 and a Russian-language sheet (7 frames, A06040124600). Not described as cipher; image not viewed (404).
* B07090505600 (suspect foreigners 1911-14), B02031683300 (密電情報, 1930-31: Chinese telegrams in Japanese
  translation, read), B03030503700, B12080889300 (1933 leak inquiry), B13080683900 (Qing documents bought 1899-1900,
  clear Chinese), B08090122900, B12081333000, C10071834300, B07091181100, B03041712800 (Korean emperor's secret
  letters: clear), C06031038800 (1882-84 Korea incident; the kana run in C06031039100 is transcription noise in a
  clear telegram).

Not opened: the other 59 volume titles (list in `jacar_volumes.jsonl`).

## 3. Academia Sinica IMH leads (1372-1380)

Notes only (`imh_leads_notes.json`): the reader site is still unreachable, so nothing is added to the 6 Nov
vetting notes except that the cover thumbnails now answer curl from this network.

## What remains

* Abhilekh: pages 231-451 of title=cypher; full paging of code telegram (103), cypher messages (77), cipher telegram
  (63), foreign cypher (30); keywords=cypher / cipher (1,656 / 660) still only sampled. A logged-in look at the ten
  rows (and the 18 older ones) is the step that decides them.
* JACAR: a working image route from this network; the Fuping Russian sheet.
