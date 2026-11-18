# Riksarkivet, remaining private fonds and the catalogue terms again (14 Nov 2026)

Source key `riksarkivet_more`. Goal: the Riksarkivet collections the Diplomatica sweeps had not sheeted (Stedingk beyond the 59
volumes of `sweep_2026-11_riksarkivet_west`, Reuterholm, De la Gardie, Tessin, Oxenstierna, Kanslikollegium, Barthelemy), and a
fresh catalogue-level search for cipher words. **Result: 0 rows** in `candidates.json`; 2 catalogue-only key/copy items in
`key_leads.json`. Nothing padded.

## Method

1. **Catalogue text search** (`harvest.py`): NAD API `https://data.riksarkivet.se/api/records?text=<term>&max=100&offset=<n>`
   (header `User-Agent: curl/8.0`). 19 terms: chiffer, chiffer*, chiffr*, chiffrerad*, chiffrerade, dechiffr*, dechiffrerade,
   dechiffrering, ciffer, cifferskrift, chiffernyckel, nyckel till chiffer, rikskansler chiffer, chiffre, cifra, chifferbrev,
   chiffrerat, tolkade chifferbrev, afchiffrerade. Totals: chiffer 126, chiffer* 305, dechiffr* 22, dechiffrerade 14, the rest
   0-11; the terms ciffer, cifferskrift, chiffre, cifra, afchiffrerade and rikskansler chiffer return nothing. 332 unique hits (`hits_raw.json`).
2. **Dedupe** against `research/riksarkivet/hits.json` (326 hits of 24 Oct): only 7 hits are new, and none is a pre-1920 cipher
   letter (a 1950s cipher-machine spare parts box, a Tändsticks AB file on cipher machines, Berlin and Copenhagen legation
   dossiers with "Föreskrifter rörande chiffrering 1921" and "Chiffreringskorrespondens med beskickningen i Paris", a map). Two
   are worth a line and are in `key_leads.json`: Herslow's notes on the Russian 4- and 3-digit codes of 1914-18 (`SE/RA/721594/1`)
   and the Foreign Office copies of the German legation in Stockholm (`SE/RA/221/2212.21/114`, "Chiffrierte Telegramme" 1917).
   The old catalogue-note leads (Johan Casimir 1631, Nääs 1677, Meyerfeldt 1712-14) are already catalogue entries; the
   Riksarkivet note search is exhausted.
3. **Digitised volumes** (`nad_enum2.py`, facet `PartOfArchive:<fonds>`, `only_digitised_materials=true`): Reuterholmska 8,
   De la Gardieska 25, Tessinska 8, **Oxenstiernska 2**, **Kanslikollegium 7** (antiquity-office officials' memorials and an
   addressee register), Ericsbergsarkivet 363, Stedingkska 150 not yet sheeted. The query `Barthélemy` finds only the island
   (S:t Barthélemysamlingen, maps), not a papers fonds, so "Barthelemy" in the briefing has no volumes to sheet.
4. **Volume selection** (`build_units.py`, `units.json`): 78 volumes of 29,634 images, chosen for correspondence that could carry
   cipher: Reuterholm E 5134-5141 (Francesco Piranesi's letters, Italian, 1790-97), Tessin E 5712-5716 (Cronström's letters from
   Paris to Nicodemus Tessin d.y., 1691-1719), De la Gardie C/I (Adolf Johan, Moirous de Verrière 1662-68, Palm 1669-84, Bråms,
   Luthman, unsigned letters), Stedingk (Gustaf III's letters E 6616, letters from Russian ministers and unidentified writers
   E 6626-6636, the Petersburg papers E 6700, the 1826 mission E 6706, the 1788-90 Finnish-war field chancery E 6663-6677,
   letters 1759-90 E 6618-6621, family and official letters E 6648-6654), Ericsberg (not run, see below).
5. **Paging** (`process_vol.py`, `runq.py`, `runkey.py`): image series id from the APE EAD (`dao()`), every n-th image at 1200 px
   through lbiiif with `Referer: https://sok.riksarkivet.se/` (one request about every 1.5 s per stream, four streams at most, no
   bot check, no Chrome), the digit-run detector `digitscan.py` copied from the consuls sweep on each, 300-px thumbnails kept,
   and **autocontrast contact sheets of 36 evenly spaced thumbnails per volume viewed by eye** (`tools.py one`, `combo`),
   flagged pages and suspects opened at 800-2200 px.
   Strides: Reuterholm 4 (E 5135 and 5136 at 2), Tessin 4, De la Gardie 4-6, Stedingk 2 for the key volumes (E 6616, 6633, 6634,
   6636, 6700 at 1) and 6 for the rest.

## Results

**No cipher seen in any of the 5,636 images paged (19% of the 29,634 in the chosen volumes; every image of E 6700).**

| Fonds | Volumes paged | Images paged / in volume | What the sheets show |
|---|---|---|---|
| Reuterholm E 5134-5141 | 8 | 1,320 / 3,480 | Piranesi's Italian letters, a few printed notices, medals, lists; clear. One sheet (E 5135 image 331) is a struck-through letter with the next sheet showing through; read at 2000 px it is cancelled text, not number groups |
| Tessin E 5712-5716 | 5 | 629 / 2,423 | Cronström's French letters, accounts; clear |
| De la Gardie E 1329, 1330, 1358, 1387, 1494, 1521, 1646 B, 1656 | 8 | 903 / 2,788 | Swedish and French letters, muster tables; clear. Moirous de Verrière's French news letters read at 800 px (images 49, 75, 125, 175, 249, 261, 311, 349): clear |
| Stedingk (28 volumes, list in `stats.txt`) | 28 | 2,784 / 10,431 | French and Swedish letters, short billets from Russian ministers (E 6634, 6636), Gustaf III's letters (E 6616), war orders, bulletins; clear. E 6706 paged to image 330 of 466 (stride 2), E 6648 at stride 6 |
| Oxenstierna E 1039, 1040; Kanslikollegium E IV 8-14, D IV b/1 | 0 | 0 | Not sheeted: letters to the wives of Johan Oxenstierna and the antiquity office's officials; no envoy or cipher context |
| Ericsberg (27 volumes, 9,969 images) | 0 | 0 | Queued last and cut off; not run |

The digit-run detector is a poor screen on these hands: it fires on printed headings and neat copperplate (Stedingk E 6668
images 101 and 106 are printed royal notices; E 6700 images 80, 84, 88 are clear bulletins), and it did not score known
bare cipher (Wulff, Salé, images 11-13; Camerarius 426) at 1200 px. It is kept for the record, not as evidence of absence.

## Why this is a null result and what it does not show

- A 1-in-4 to 1-in-6 sample finds a volume that carries cipher often, not one that has a single ciphered letter; "no cipher
  seen" is not "no cipher". Volumes with Russian ministers' notes (E 6633, 6634, 6636, 6700) and Gustaf III (E 6616) were paged at
  1-in-2 or every image because ciphered postscripts are most likely there (Stedingk's drafts, E 6601 image 108 and E 6588 image
  60 in the west sweep, mark "Apostille en chiffre"; the ciphered originals are not among the digitised volumes).
- Short code groups inside clear sentences show only at 800 px (consuls sweep, Logie's form); sheets at 300 px do not show them.
- Reuterholm's own key is at `SE/RA/720741/~/28`, which is not digitised.

## What blocked

- **De la Gardie E 1649** (`R7000021`, 543 images, unsigned undated letters): the image server answers 401 to the image route
  that works for the other `R70000xx` series (`blocked.txt`). Not tried through the viewer.
- **Ericsberg Vol. 306 and 311**: manifest requests reset the connection (`build.log`).
- The image server was quick at one stream (about 0.9 s an image) and ran at roughly 1.2 images a second with four streams.
  A first full-rate run fell behind; strides above were set to finish the batch.

## Not reached

- Ericsberg: 27 volumes, 9,969 images (Hedvig Elisabeth Charlotta's letters `B 1/13-15`, `B 2/26`; C. G. Tessin papers `02/07/04/1-12`;
  Gustaf III to C. G. Tessin, Klingspor and Sophia Albertina Vol. 294; Vol. 303-314), already known to hold keys
  (`research/riksarkivet`, `research/scandinavia`).
- Stedingk E 6706 remainder, E 6618-6621 and E 6648 only at 1 in 6; the family and accounts volumes were not selected.
- De la Gardie E 1649 (401).

## Files

`harvest.py`, `hits_raw.json` (term search); `nad_enum2.py`, `enum2.json` (digitised volumes by fonds); `build_units.py`,
`units.json`; `process_vol.py`, `runq.py`, `runkey.py`, `digitscan.py`, `rik_common.py`, `tools.py`, `stats.py`, `stats.txt`;
`blocked.txt`; `candidates.json` (empty); `key_leads.json`. Page images and sheets stayed in the session scratchpad.
