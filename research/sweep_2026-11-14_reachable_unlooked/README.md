# Sweep: the "not looked at, though reachable" sources (14 Nov 2026)

Brief: the COVERAGE.md row "Not looked at, though reachable". **Result: 17 rows in `candidates.json`, 4 key-only groups in
`key_leads.json`** (`make_candidates.py` builds both). Every row is scored from the finding-aid text (`seen: catalogue`),
none viewed; digitisation was not checked, so `needs_archive_scan: "yes"` throughout. `known.py` and a shelfmark grep
against catalogue.json, leads.json and every `candidates.json` / `key_leads.json` were run on each number; items already
held (GStA OBA 2987, 20039, 20349, 21069, 22448, 22472, 22473, 22490, 22717; Rep. 81 Mainz; Nl Saegert 63-104; Bevern Nr. 3-4;
Rep. 39 Nr. 58/289; Rep. 49 R Nr. 129; Nl Wittgenstein; FA Werther Nr. 36; Nl Albrecht Nr. 11) were dropped.
Nothing was merged, catalogue.json was not touched.

## Routes

| Source | Route | Result |
|---|---|---|
| **GStA PK own database (ACTApro)** | `https://archive.spk-berlin.de/actaproweb/search.xhtml` (the domain `archivdatenbank-online.gsta.spk-berlin.de` does not resolve; the link comes from gsta.preussischer-kulturbesitz.de/recherche/archivdatenbank.html). curl cannot get past the JSF form, but **inside a Chrome tab on that origin** `fetch` works: GET the page, copy the `searchForm` fields, set `searchForm:searchTerm_input`, POST with `searchForm:searchButton`. The date fields `searchForm:searchDurationStart1/End1` take years and **must be set to '' explicitly** or the server remembers the last range. **Paging does not work through fetch** (the paging form's ajax call returns page 1 again), so each query is kept to 25 hits by halving the year range (`hv` recursion in the console). About 1.5 s per request, polite. The tool output of the Chrome extension is capped near 1 KB: results were put into `document.body` and read with `get_page_text`. | 28 terms, 284 distinct records, 215 with a cipher word in the description, 155 dated before 1920. 16 of the 17 rows come from it (see below). Chiffren/key files go to `key_leads.json`. |
| **BU ArchivesSpace** (`archivesspace.bu.edu`) | curl gets 403; in Chrome the site loads and same-origin `fetch('/search?q[]=<term>&op[]=&field[]=&page=1')` returns HTML (`.recordrow`). | cipher 3 hits, cypher 3, cryptogram 2, other phrases 0. One real lead: the Jorge Gonzalez papers (THE-03-067), a "Cuadra Cypher" file on Bishop Quadra's ciphered letters (Simancas Estado 812-816). Tyler Kent collection is 1940 and out of range; the Samaritan Pentateuch hit is not a cipher. |
| **UMass Boston** (`openarchives.umb.edu`, CONTENTdm) | `https://openarchives.umb.edu/digital/api/search/searchterm/<term>/maxRecords/50`, plain curl, JSON | cipher 11, cypher 4, cryptogram 0; all 1970-2026 student papers, minutes and interviews. Nothing. |
| **Congregational Library** | `congregationallibrary.org/search?q=cipher` answers, no hit text; the ArchivesSpace host did not resolve | Nothing found; not exhausted (no item-level route found). |
| **NEHGS / AmericanAncestors** | the search page is a Drupal/JS app (`database-search-advanced-search?q=cipher`); curl gets only page chrome | Not searched. Needs a Chrome pass with the page rendered. |
| **Sächsisches Staatsarchiv (HStA Dresden)** | `www.archiv.sachsen.de` answers; its finding-aid browser is `/archiv/bestand.jsp` (tree only); no full-text search endpoint found (`/archiv/suche.jsp` and similar are 404). Its holdings are in Archivportal-D, which `research/archivportal_d` and `sweep_2026-11_archivportal_more` already paged for chiffr*/Ziffer*/verschluesselt (incl. Loc. 04414/04, 02974/09). | No new route; nothing added. |
| **KB Copenhagen** | `soeg.kb.dk` (Primo VE) loads in curl (200) but is a JS app; opening it in Chrome gave an error page (blocked by the extension's site rules) | Not searched. |
| **KBR, BnL/ANLux** | no new attempt; `sweep_2026-11_belgium_kbr_arch` found KBR's catalogue to be printed books only and BnL newspapers | Not repeated. |
| **Krigsarkivet, Rigsarkivet TKUA** | covered by the NAD API and soeg.rigsarkivet.dk in `research/scandinavia`; no new route | Not repeated. |

## What the GStA harvest found

Terms (hits dated 1400-1919 / undated): chiffriert 55, chiffrierte 39, chiffre 29, chiffren 69, dechiffriert 3, Dechiffrierung 11,
Geheimschrift 4, entziffert 10, Entzifferung 29, Chiffrenschluessel 1, verschluesselt 11, Geheimschluessel 1, Ziffern 11, en chiffres 1,
Geheimzeichen 1; 0 for chiffrirt, Chiffer, Ziffernschrift, Zifferschrift, cifra, cipher, chiffree, Zifferbrief, Kryptographie, Zahlenschrift;
"Ziffer" (200) and "in Zahlen" (114) are numerals and were not read item by item (a cipher-phrase filter found none).
About 80 of the cipher hits are dated before 1800, 75 in 1800-1919. Large groups:

- **I. HA Rep. 64 (Neuchatel)**: 52 volumes of 1694-1759 with reports "teils chiffriert", many "mit Entzifferung": three rows, the first and third with the
  decipherment filed beside the ciphertext. The best material of the sweep for a key rebuilt from plaintext pairs.
- **XX. HA OBA** (Teutonic Order, 1514-20): 12 hits, most already in the catalogue (OBA rows 530, 554, 555 and others); 3 new numbers in one row.
- **III. HA MdA** (Prussian foreign ministry, 1806-17): about 30 files titled "Chiffren": keys, in `key_leads.json`.
- Single items: Derfflinger 1674, Charles XI 1676, Kopenhagen 1743, Frederick II 1757, Haude 1761-62, Mary Stuart 1571, Louisa Ulrika 1756, Lusi 1790,
  Scharnhorst to Boyen 1810-13, Westphalia 1810-12, Woellner's notebook, Dohna 1803.
- Dropped as noise: handwriting "Entzifferung" (reading old script), ciphered telegram series of 1850-1920 in the BPH Saegert and Fehn papers
  already held or out of period, "Chiffre" meaning a signature or monogram.

## Honest limits

- Descriptions only; none of the 17 rows has been looked at on a scan, and no row has had a web, Tomokiyo or Lasry search.
  The vetting bar (README Conventions) is therefore not met for any of them.
- The ACTApro hit lists are the first 25 of each year-range slice; a slice with more than 25 hits is split down to a single year, so none were cut.
  The undated list was read only when it had 25 hits or fewer (all did except "Ziffer" and "in Zahlen").
- ACTApro covers part of GStA's holdings (the database is a fraction of the stock); Archivportal-D carries a different subset.
- Rows for Neuchatel group volumes by description; a lead per correspondent (one key per entry, Lasry's rule) needs the volumes seen.
- Quadra: a decipherment probably exists (Gonzalez 1981-82; CSP Spanish, Elizabeth); the row is kept as a lead only until that is checked.

## Chrome use

Own tab each time (closed afterwards): ACTApro (about 20 minutes of polite harvesting, no CAPTCHA, no bot check), BU ArchivesSpace
(no CAPTCHA; curl 403, Chrome loads). `soeg.kb.dk` and `archivesspace` hosts of other Boston bodies were not opened.
Source needing Chrome, for the next sweep: **ACTApro (JSF session) and BU ArchivesSpace.**
