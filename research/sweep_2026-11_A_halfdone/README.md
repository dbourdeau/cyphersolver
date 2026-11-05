# Sweep "A": the half-done runs (4 Nov 2026)

Brief: finish the runs that earlier sweeps left half done (`research/COVERAGE.md`, "Started and not finished"): Internet Culturale
full text, PARES bare terms and the ACA registers, the szukajwarchiwach `szh` harvest, then Calames and Archivportal-D if time
allowed. Nothing outside this folder was edited, except one new file written next to the earlier pass:
`research/chrome_pass_2026-11/szh_export.json` (the export step 3 asked for). No commit.

**Result in one line:** 5 candidate rows (`candidates.json`), 2 of them with images online; four of the five runs closed as
"nothing new in the source"; one new access route found (PARES-HTR) that turns out to be a crib index rather than a cipher index.

| Run | Result |
|---|---|
| 1. Internet Culturale full text | Closed. The full-text index holds printed books and newspapers only. 0 rows. |
| 2a. PARES "cifra", "descifrado" | Done by century facet: 279 + 147 hits. 1 row, plus key and crib leads below. |
| 2b. ACA reg. 3225 and neighbours | **Not reached.** PARES has no text index for the Cancillería registers (see below). New route found: PARES-HTR. |
| 3. szukajwarchiwach `szh` | Exported to disk. Triage agrees with the 2 Nov polish_harvest sweep; 3 further rows. |
| 4. Calames, Archivportal-D | Not repeated: `sweep_2026-11_calames_rest` and `sweep_2026-11_archivportal_more` (2-3 Nov) already did both. |

## 1. Internet Culturale full text

`/it/16/search?q=cifra&instance=ocrindice` ("Full-text: 28,624 hits"; the link on the normal result page, which I clicked).
Facets are plain query parameters, e.g. `&__meta_typeLivello=monografia`, `&__meta_issued=1581`, `&facetUnlimited=issued`.
Opened in Chrome as same-origin `fetch`, 0.8-1 s apart, no check met.

- Of 28,586 "testo a stampa" hits, 27,443 are periodicals (Trieste, Taranto, Perugia newspapers, 1877-1923) and 1,143 are monographs.
  No manuscripts and no archival units: the index is OCR of printed matter. Of the other levels, "unita documentaria" (35) are
  Ricordi newspaper clippings, "unita archivistica" (2) Muratori-archive records (and one "spoglio" ballet record), "bando" (9) Venetian printed edicts.
- All 1,143 monographs for "cifra" were paged and kept (`ic_fulltext_harvest.json`, titles and OAI ids; plus 35 "unita documentaria").
  344 carry a year before 1700 by my regex: all printed books ("cifra" = figure, digit or sum; a few treatises and Roccamora's
  "Cifre dell'eucharistia", 1685, a devotional work).
- Variants run on the monograph filter and read by title, all printed: cifrata (63), cifrato (26), cifrate (10), cifrati (55),
  "in cifra" (104), decifrare (36), decifrata (1), discifrare (6), cifrario (5), "lettere in cifra" (2). Counts only: cifre
  (28,050), "scrittura in cifra" (6, all periodicals).
- **Rows: 0.** The manuscripts that mention a cipher are in the catalogue (not the full-text) index, which the 2 Nov pass already read
  (Machiavelli, Autografi Palatini). Nothing in the full text is archival.

## 2. PARES

### 2a. Bare terms, by century facet
`sweep.py` and `run_batch.py` (copies of the `pares_ags` scripts, so their output stays in this folder; `hits.jsonl`,
`hits_progress.json`). PARES ignores `anio1/anio2`; the working date filter is the start-century facet `idFI=<n>`
(13 = S.XIII ... 19 = S.XIX, 0 = undated). About 40 requests in all (batches of 5, 12 and 5, 6 probes, 9 description pages), one at a
time, 20 s plus jitter, shared stamp file, no 429, no bot check, no Chrome needed for these.

| Term | S.XIV | S.XV | S.XVI | S.XVII | S.XVIII | S.XIX | undated | total |
|---|---|---|---|---|---|---|---|---|
| cifra | 2 | 12 | 47 | 51 | 58 | 104 | 5 | 279 |
| descifrado | 0 | 0 | 73 | 63 | 4 | 7 | 0 | 147 |

(S.XIII "cifra" and S.XIV/XV/undated "descifrado" returned PARES's "no results" error page.) 119 of the 421 ids are not in
`pares_ags/hits.jsonl`. Nearly all the new ones are siblings of rows already in `pares_ags/candidates.json`:
Genoa legajos, the AHNOB Osuna and Santa Cruz letter series.

What came out:
- **1 row:** AGI Indiferente 737 no. 171 (1554), five cipher letters, 13 folios; the first is deciphered in Panama 29 R.6 N.23.
  Images online. The best new lead of this sweep.
- **1 row (class A):** Genoa 1633, EST,LEG,3591,181 no. 2 and 183, a cipher chapter and its probable clear copy.
- 62 of the 70 new "descifrado" ids are AGS Estado Genoa letters (mostly 1534-1599; Gomez Suarez de Figueroa 1534-57, Pedro de
  Mendoza 1579-83, Padilla 1571-73, Doria, a few of 1607-45) whose descriptions mention a decipherment. Not read one by one: they are
  probably crib pairs, so no rows.
- OSUNA,C.1981,D.123 (30 Dec 1650): two identical cipher letters on the imprisonment of Andres Chavarri for misusing the despatch
  cipher. Same affair as the catalogue entry that quotes Chavarri (D.113 row): treat as its sibling. Not digitised.
- PTR,LEG,54,46 (7 Sep 1507): the Princess of Wales to Almazan asking if he deciphered her letters properly. Puebla/Catherine
  family; background for catalogue 617 (Puebla 1506), no ciphertext.
- The 7 ACA Sastago hits (Diversos, Sastago 193, Lio B, nos. 79/58-79/77, 1495-98) are DECODE R10172 ff., already in the repo (Cryptoole
  snapshot, catalogue 349).

**Key leads (keys or notices of keys, no ciphertext):**
- ACA, Generalitat, Correspondencia del virrey Conde de Santa Coloma, carta num. 498 (PARES 1520934, Sept 1637, images): "Cifra con
  que se entendera la correspondencia que tendra la torre de la Macana con este campo" (Perpignan front, Franco-Spanish war).
- AHN Estado 193 Exp. 66 (PARES 12709762, before 1733, images): cipher for the reserved correspondence of the marques de Castelar
  with Jose de Viana (pairs with the Viana 1729-30 rows of the Paz pass).
- AGI Mexico 58 R.1 N.18 (PARES 363113, 20 Mar 1689, 2 fs, images): the viceroy Monclova hands the cipher "que se le dio" to his successor
  the conde de Galve (N.21, PARES 363116, same date and a "cifra" hit, description not fetched).
- AGS MP-ESCRITURA_CIFRA nos. 1-7 and 27 (PARES 17804-17810 and 17830, 1658-1695; nos. 1, 2, 7 with images): cipher sheets for the galleon
  generals and the viceroys of Peru and New Spain (no. 27: the cipher for letters to the bishop of Heliopolis, 1675). AGS Estado leg. 1932 ff. 245, 246, 422, 423 and leg. 1933 ff. 77, 277: minutes
  sending the "cifra general" to the Dorias in Genoa, 1607-12 (the minute may carry the table); leg. 1434 f. 88 is Andrea Doria's receipt
  of a new cipher. AGI Filipinas 385 N.7 (1748) and 390 N.30
  (1771): a governor asking for, then acknowledging, a cipher. FRIAS C.642 D.74 (PARES 3949058, 1802, not digitised): "Tabla de
  descifrado de mensajes".

### 2b. ACA Cancillería regs. 3225 and neighbours (oldest/CANDIDATES.md A1): not reached
- PARES text search does not index the registers. "Registros 3225", "3225", "ACA,CANCILLERIA,REG,3225", "Cancilleria Registro 3225" and
  "lugarteniente reina Maria Valencia 1435" return "No se han encontrado datos" (or the error page when an `idA` facet is sent without
  `idFI`). The Cancillería pieces PARES describes at item level are the Pergaminos (e.g. ACA,CANCILLERIA,Pergaminos,Alfonso IV-V,
  Serie general, 183, PARES 12979430, a 1421 grant by Queen Maria as lieutenant). Reg. 3225 has to be reached by browsing the PARES
  tree (ACA > Cancillería > Registros) and paging the images; not attempted (hundreds of folios, no index).
- **New route: PARES-HTR** (`https://pares.cultura.gob.es/pares-htr/`, Handwritten Text Recognition with probabilistic indexing, in the
  Chrome tab, no login). It covers five series, three of them relevant: 3 = **ACA Cancillería 1479-1556** (Fernando II regs. 3521-3870
  and Carlos I regs. 3871-4282; so not reg. 3225, which is 1435), 4 = AGS Registro General del Sello 1502-17, 6 = AGS registros de cédulas
  1490-1691. Method: POST `/pares-htr/search.action` (`loteId`, `search`, `t` = confidence, `max`, `page` from 0), then
  `/pares-htr/select-document.action` with `archive`, `folderId` (the hidden internal id in the result row, not the signatura), then
  `/pares-htr/select-page.action` with `number` for one page; the page comes back as a base64 JPEG (0.5-2 MB).
  Results are in `htr_hits.json`.
  - "cifra": series 3, 27 registers at confidence 50 (56 at 20), series 4 none (1 at 20), series 6 two (four at 20). "cifras" 12/20 and
    "cifre" 6/14 in series 3. Zero hits for cifrada, cifrado, cifrar, descifrar, xifra, xifres, cifra with c-cedilla or z, ciffra, cyfra.
  - Registers with the densest hits (page numbers are viewer indices): **3686 (Fernando II) 9 pages of "cifra" at 99% (203-257) and "cifras"
    on 240, 248**; 3900 bis (Carlos I) 4 pages; 3613 three; 3929, 3605, 3924, 3987, 3753 two each (`htr_hits.json` has the lot).
  - **What the hits are.** I viewed four pages (3686 pp. 211, 248; 3900 bis pp. 90, 161). They are clear register copies of letters that were
    sent in cipher, each with the heading "En cifra" / "Carta en cifra scripta al Visorey de Sicilia" / "En cifra sobre las treguas de
    Flandes con Francia" (Charles V at Monzon, truce of Bomy, 1537), and a Catholic Monarchs letter marked "En cifra" signed by Coloma
    (3686 p. 248). So the registers hold the plaintext of cipher letters, not their cipher text. For this project that is a crib index: the cipher
    originals of Ferdinand II and Charles V letters (AGS Estado, ACA Sastago, DECODE records) can be paired with the registered
    plaintext. The same hit lists are therefore the way to find plaintext for open cipher letters of 1479-1556, not new rows.
  - Not done: the other ~45 register pages, and any attempt to read the cipher originals. HTR text is not exposed, only the page image
    with the hit boxed.

## 3. szukajwarchiwach: the `szh` harvest, exported
- **Export route.** A `fetch` or form POST from the Polish https origin to a local receiver on 127.0.0.1 hung (Chrome's local-network rule),
  as the polish_harvest sweep also found. What worked: a tiny Python server on 127.0.0.1 whose page reads `location.hash` and POSTs it to
  itself; the Polish page set `location.href = 'http://127.0.0.1:PORT/#' + encodeURIComponent(data)` (a top-level navigation, up to
  about 1.5 MB). The same hand-off carried the Internet Culturale and PARES-HTR data. The receiver was not committed (scratch only).
- **File:** `research/chrome_pass_2026-11/szh_export.json` (697 KB, git-untracked): keys `i`, `cur`, `live`, `hits` (1,883 records keyed by
  signatura|title: `t` title, `y` dates, `op` note, `s` signatura, `a` archive, `h` link, `k` scan flag, `q` term indices), `counts` (65
  terms), `err`. Two terms failed in the first run: "szyfrowe" (a TypeError) and "Chiffrierschlussel" (crumb mismatch).
- **Triage** (1,217 records start in 1900-50; about 650 match a loose cipher regex, 251 a strict one):
  - Radom 58/387: 125 records, all Radom ghetto identity-card files where "Szyfra" is a given name. 0 rows. The 1900-50 "Szyfra" hits
    elsewhere are the same name (Lodz 39/181 and Piotrkow 48/243 trade registers, Kielce court files).
  - The rest: Polska Policja Panstwowa cipher instructions (AAN 2/349), cipher-office administration, Home Army and PPR "szyfrogramy"
    1944-48 (Studium Polski Podziemnej 722/113 and 722/1, Lodz 39/1022), Russian-language police and court files, thieves' house marks.
  - Four rows already exist in `sweep_2026-11_polish_harvest`. I add **3**: AAN 2/39/0/13/2067 (Russian Embassy in Rome, 1917),
    2/100/0/19/4508 (Paderewski, 1940-41), 2/100/0/4.15/781 (Paderewski 1919 notebook, sibling of the existing lead 779).
  - **Correction to the scan flag:** the `k` flag in `szh` is 1 for AAN units 779, 781, 2067, 4508, 256 and 830, yet their detail pages
    say "Brak kopii cyfrowych" (not digitised; some have microfilm). Do not read `k` as "scans online" for AAN.

## 4. Calames, Archivportal-D
Already done after the COVERAGE.md note: `research/sweep_2026-11_calames_rest` (all 2,203 bodies re-read, 52 rows) and
`research/sweep_2026-11_archivportal_more` (about 15,800 records, 82 rows; the first 200 "chiffriert" slots had already been exhausted
on 26 Oct). I made no request to either and added nothing. COVERAGE.md still lists both under "Started and not finished"; those rows can go.

## What is left
- ACA reg. 3225 and the 1430s lieutenancy registers: browse them in PARES by hand, or ask ACA for a list of the registers' folios.
- PARES-HTR: view the remaining register pages for the "cifra" hits; then pair the registered plaintexts with AGS Estado cipher originals.
  Series 6 (cedulas) and 4 (Sello) have only a handful of hits.
- PARES bare terms: "cifra" for the S.XIII facet is empty; "descifrado" for undated records errored (no hits). Other forms ("cifras", "cifrado",
  "clave", "contracifra") were not run by century. AHNOB Osuna D.123 and similar items are not digitised.
- Prior art: one web search for the Indiferente 737 row only. Tomokiyo, Lasry and the editions are not searched for any row.
- Internet Culturale: nothing; only the catalogue (non-full-text) index holds manuscripts, already read.

## Files
`candidates.json`, `make_candidates.py`; `hits.jsonl`, `hits_progress.json`, `sweep.py`, `run_batch.py`, `pares_run*.log` (PARES bare terms);
`aca_probe.py`, `pares_desc.py`, `desc.jsonl`, `pares_desc*.log` (probes and description pages); `htr_hits.json` (PARES-HTR);
`ic_fulltext_harvest.json` (Internet Culturale monographs and units).
