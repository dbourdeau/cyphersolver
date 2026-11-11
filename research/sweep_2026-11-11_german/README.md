# German archives sweep (11 Nov 2026, cloud session)

Result: **14 candidate rows** (`candidates.json`, built by `make_candidates.py`), **1 with a complete `open` vetting
block**, and 6 key-lead bundles (`key_leads.json`). 13 rows are archive-only leads from the GStA PK's own database, which
no earlier sweep had searched; one is a digitised Darmstadt unit whose cipher leaf was not found.

The earlier German sweeps (`archivportal_d`, `central_archives`, `sweep_2026-11_archivportal_more`, `_german_portals`,
`_german_portals_2`, `_austria_german_states`, `kalliope_ddb`, `_hab_swiss_german_libs`) had already run the cipher terms
on Archivportal-D/DDB, Arcinsys Hessen and Niedersachsen, Landesarchiv BW, gda.bayern.de and archiv.sachsen.de. Their
terms were not rerun there. This pass did two new things: the GStA database, and a digitised-only pass over the DDB.

## Routes from this network

| Host | Result |
|---|---|
| GStA PK database, `archive.spk-berlin.de/actaproweb` (ACTApro; the old `archivdatenbank.gsta.spk-berlin.de` is dead, HTTP 500) | **Works** in headless Chromium, no bot check. JSF form: `#searchForm:searchTerm_input`, 500 a page via `label[for="searchForm:j_idt249:4:item"]`, `#searchForm:searchButton`. `gsta_harvest.js` saves the result list per term. A page-load can hang on a blocked tracker (hotlog.ru): the scripts abort that request and wait for `domcontentloaded`. Full records: `gsta_detail.js` (opens the hit in the Tektonik view and clicks its node); it worked for hits near the top of a list and returned "not found" for the others, so several rows rest on the list snippet only. |
| DDB Solr API (`api.deutsche-digitale-bibliothek.de/2/search/index/search/select`) | Works, no key. `fq=digitalisat:true` limits to digitised records (`ddb_digi.py`). |
| `www.archivportal-d.de/item/<id>` pages | **Anubis challenge** to curl; not pursued. Use the API, and the provider's own viewer for images. |
| Arcinsys Hessen (`arcinsys.hessen.de`, images on `digitalisate-he.arcinsys.de`) | Works with curl. Drop `/thumbs/` for the full image; `arc_sheet.py` finds the last image by HEAD and fetches a unit. |
| archiv.sachsen.de, Arcinsys Niedersachsen, Landesarchiv BW OFS, gda.bayern.de | Answer 200; not re-harvested (finished by earlier sweeps). |
| `diglib.hab.de` | 200 (retest), but as the 9 Nov sweep found it has no searchable manuscript descriptions. `opac.lbs-braunschweig.gbv.de` still does not connect, so HAB Extravagantes remain unswept. |
| `www.leo-bw.de` | 403. `recherche.staatsarchiv.sachsen.de`: no connection. |
| DECODE `de-crypt.org/decrypt-web/RecordsList?cmd=search&search=` | Works with curl (`decode_search.py`). DECODE has **no GStA PK records** ("GStA", "Geheimes", "Dahlem", "Privy State": only Dresden and BL rows). |
| `friedrich.uni-trier.de` (Politische Correspondenz online) | Redirects to a university page; the edition is gone from there. Use the archive.org volumes (`politischecorre..herrgoog`, `politischecorres0Nfred`). |

## Terms and counts

**GStA database** (all archives, all levels): chiffriert 55, chiffrierte 39, chiffrierten 8, chiffrierter 7, Chiffre 29,
Chiffren 69, Chiffern 50, Geheimschrift 4, "in Ziffern" 8, Zifferschrift 0, verschlüsselt 11, dechiffriert 3,
unentziffert 1, "en chiffres" 1, Dechiffrierung 11, Chiffrierung 12, Ziffern 11, Ziffer 200 (numerals, not read),
entziffert 10, Entzifferung 29, chiffrirt 0, Chiffres 7, chiffré 1, "en chiffre" 3, dechiffrierte 3, Ziffernchiffre 2,
unaufgelöst 0, Geheimzeichen 1. The "only with digital documents" filter returned 0 for the cipher terms.
Most strong hits were already held from Archivportal-D (Ordensbriefarchiv 1505-25, Grumbach/Küstrin Rep. 39, Rep. 81
Mainz, Bevern, Saegert, Werther, Rep. 91 A, Nl Albrecht, Rep. 81 Dresden). New here are fonds the GStA has not delivered
to the DDB: **Rep. 64 (Neuchâtel/Orange inheritance), Rep. 34, Rep. 11 Akten, Rep. 81 Kopenhagen, BPH Rep. 56, V. HA
Westphalen, FA Lusi, Nl Boyen, Rep. 7 C**.

**DDB, archives sector, digitised only** (`ddb_digi.py`, 45 terms with wildcards): chiffr* 181, Chiffre/Chiffren 81,
entziffer* 71, Geheimschrift* 32, "mit Ziffern" 17, Chiffer* 15, verschlüssel* 9, dechiffr* 7, others 0-3, Ziffer 297.
639 unique, 233 with a cipher word in title or abstract, 79 already in the repo by id or shelfmark; the other 154 read
as lines. Nothing new with ciphertext beyond the two Darmstadt units below: the rest are keys, cipher administration,
20th-century files, gravestones and "Chiffray" patents.

## Viewed

- **HStAD D 12 Nr. 30/41** (Lichtenberg, minister at Darmstadt, 1798-1819; "teilweise chiffriertes Schreiben ... 1801"):
  all 197 images paged on contact sheets; images 195-196 opened large. Four-digit code groups inside a German letter,
  **each with its French or German meaning written above** ("manoeuvres de l'armée", "ordonnances", "Bombardier"). Read
  at the time: excluded.
- **HStAD D 4 Nr. 185/3** (Georg II, 414 microfilm openings): all fetched, paged at 40 a sheet, which is too small for
  double-page microfilm; the partly ciphered letter was not located. Kept as a lead, no block.

## The one vetted row

GStA PK I. HA Rep. 64 Nr. 828: Martinet's ciphered message from Môtiers-Travers, December 1758, which the archive
describes as "teils entziffert". Not online, so `seen.kind` is "not online" and the block rests on the description.

## Excluded, and why

- GStA I. HA Rep. 34 Nr. 5876, Derfflinger's reports from The Hague 1674 ("z. T. chiffriert"): *Urkunden und Actenstücke*
  vol. 13 (archive.org, opened) prints his relations "in unverkürztem Wortlaut" (pp. 793 ff.), so they are read.
- GStA I. HA Rep. 94 A, V, Nr. 26, Frederick II to Zegelin 19 Nov 1775: "Dechiffrierung ist überschrieben".
- GStA I. HA Rep. 132 Nr. 2 (1700, digitised): only the signatures of the Warsaw informants are in cipher.
- GStA Rep. 64 files described "chiffriert mit Entzifferung" / "chiffriert und entziffert" (Nr. 686, 695-706, 713, 741-752,
  764, 855, 951, 952 ...), Rep. 81 Dresden Nr. 781-791 and Rep. 81 Frankfurt Nr. 167-173 ("mit Auflösung").
- LAV NRW W, V 105 Nr. 797 (Frederick II to Vincke 1768, digitised): "in Chiffre mit Klartext".
- Bare keys: see `key_leads.json` (the long III. HA MdA "Chiffren" series 1806-1846 is already noted in `archivportal_d`).

## Why only one block

Per the brief, a row whose edition could not be opened gets no block. That holds for the Rexin file (Politische
Correspondenz vols. 20-22: the download was cut off by a container restart), Queen Ulrike's letters (Arnheim 1910, not on
archive.org), Scharnhorst (Kunisch edition), Wittgenstein/Stein, Finckenstein 1743. For the Neuchâtel series Bourgeois
(1887) quotes ciphered pieces by content, so decipherments probably lie in the files.

## What remains

- GStA: full records for FA Lusi Nr. 3, V. HA Westphalen 304/393, Rep. 81 Kopenhagen 254 (list snippets only); the
  Rep. 64 files Nr. 707-710, 715, 724, 753, 760 (snippets only); a tree walk of Rep. 64 and Rep. 11 "Türkei" for files
  whose description has no cipher word. Terms not run: Zahlenchiffre, Chiffreschrift, Chiffrierschlüssel, entschlüsselt,
  chiffriertes, cifra.
- Open the Politische Correspondenz at Rexin 1761-62 and Finckenstein 28 Sept 1743, then vet those two rows.
- HStAD D 4 Nr. 185/3: page at full size to find the cipher letter.
- HAB Extravagantes (OPAC unreachable), LEO-BW (403).

Scripts: `gsta_harvest.js`, `gsta_detail.js` (Playwright; `NODE_PATH=$(npm root -g)`), `ddb_digi.py`, `arc_sheet.py`,
`sheets.py`, `decode_search.py`, `make_candidates.py`. Images and harvests stayed in the session scratch folder.
