# Continental blocked sources in Chrome (15 Nov 2026)

Brief: retry in Claude in Chrome (own tab, no CAPTCHA solved, about one request per 3-5 s) the continental sources earlier sweeps recorded as blocked.
**Result: 18 rows in `candidates.json` (7 class A, 8 class B, 3 weak class C), 3 key-only items in `key_leads.json`.** All scored from catalogue text
(`seen: catalogue`), none viewed on an image, no web/Tomokiyo/Lasry/DECODE search. `make_candidates.py` rebuilds both files. Nothing merged or committed;
`catalogue.json`, `leads.json` and `merge.py` untouched. Dedupe: `known.py`-style grep of shelfmarks and names (none of the OeNB Autogr./Cod. Ser. n. shelfmarks
is in the repo; the BnF rows are new by shelfmark but Bethune, Feuquieres and Biron are in the ledgers by name, so check siblings before merging).

## Source by source

| Source | Needed Chrome? | Result |
|---|---|---|
| **OeNB Primo** (`search.onb.ac.at/primo-explore`) | Yes (403 to scripts and to WebFetch). Opens in Chrome with no check | **Best yield, never swept before.** 12 rows. Route below |
| **Biblissima portal** (`portail.biblissima.fr/fr/bbma.view?q=...&vid=search-results`) | Yes, opens without a check (the old "Anubis" block did not appear) | 6 rows from BnF volumes. The portal mostly mirrors BnF Archives et manuscrits and Calames (already swept), so little else. 2,485 hits for "chiffre", 1,540 for "en chiffre", 49 for "lettre chiffrée" (47 manuscripts) |
| **Alvin** (`alvin-portal.org`) | Yes (Anubis passes in Chrome) | 0 rows, 2 key items. "chiffer" (18), "chiffre" (10) give the same set as the October and 9 Nov sweeps; "chiffrerad", "kryptografi" 0; "hemlig skrift" 1 (Forborgad skrifkonst). Trap below |
| **HathiTrust full text** (`babel.hathitrust.org/cgi/ls`) | Chrome shows a Cloudflare "Verify you are human" checkbox | **Stopped, per the brief.** Not clicked. Still the largest gap; needs the owner to clear the check in a tab |
| **manuscripta.at** | `403 Forbidden` in Chrome as well (home query URL) | Not reached. Not tried further |
| **CCFr** (`ccfr.bnf.fr`) | Home page opens in Chrome (cookie banner declined) | Not searched: its manuscript catalogue is Calames and FranceArchives, both swept (`calames_biblissima`, `sweep_2026-11_calames_rest`) |
| **Delpher** (`delpher.nl/nl/boeken`) | Opens in Chrome | Printed books only ("cijferschrift" 456 hits, music and children's books); not worked, no manuscript filter on this endpoint |
| **Hispana, BVPB, BDCyL** | Already done on 2 Nov in Chrome (`sweep_2026-11_es_hispana`, `_es_bvpb`, `_es_bdcyl`) | Not repeated |
| **BNE Digital** | Not touched (permission needed) | - |

## OeNB Primo route (new)

- Search URL, no login: `https://search.onb.ac.at/primo-explore/search?query=any,contains,<term>&tab=default_tab&search_scope=ONB_gesamtbestand&vid=ONB&facet=rtype,include,Korrespondenz&lang=de_DE&offset=<0,10,..>`.
  `facet=rtype,include,Handschrift` gives codices. Ten records a page, page text readable with `get_page_text` or `innerText`.
- The result list does not show notes. Open the record (click the title link; the detail is an overlay in the same page) and read `Umfang/Illustr./Format`,
  `Beschreibung` and `Signatur`. A page script can click `prm-brief-result-container h3 a`, wait 2-3 s, read `document.body.innerText` between "Details" and
  "Wikipedia", then `history.back()`: about 4 s a record, so run it fire-and-forget (the tool times out at 45 s) and read `window.__R` afterwards. Output of
  `javascript_tool` is cut at about 1,000 characters and blocks anything that looks like a URL with a query string.
- Citation link `http://data.onb.ac.at/rec/AC<number>` is stable.
- The autograph catalogue (Autographensammlung, Autogr.) states cipher in the extent line: "Brief in Geheimschrift", "Text teilw. in Geheimschrift", "von zeitgleicher
  Hand aufgeloest". Terms and hits in the correspondence facet: Geheimschrift 17, Chiffre 7 (noise: here "Unterschrift (Chiffre)" means a monogram signature),
  chiffriert 49, teilweise chiffriert 15, Zahlencode 21, Ziffern 10 (Alban Berg letters, music), verschluesselt 1, Zifferschrift and Chiffren 0. Handschrift facet:
  chiffriert 2, Geheimschrift 1 (a medieval lectionary, noise).
- Not done: Verschluesselung/Chiffrenschluessel/Kryptographie, the Nachlass facets, Papyrus (the Sator formula and an Arabic "letter in Geheimschrift" P.Vindob. A. P.
  11016, 9th c., unpublished, are in the Geheimschrift hits; not rows, the latter is worth a look as the oldest item found: **Egypt, Ihnas, 3rd c. AH / 9th c. AD**).

## Best finds

1. **Maximilian of Mexico (Ferdinand Max) to Alphons Dupont, 22 telegrams of 1862**, OeNB Autogr. 1312/30-13 to -34: number-code passages, each "von zeitgleicher Hand aufgeloest".
2. **Giorgio Basta to Kollonitz, 1605**, Autogr. 23/28-7: cipher letter with the German translation filed with it.
3. **BnF Francais 3702 and 3673 (Bethune, Rome 1625 and 1629)** and **3703 (Feuquieres 1634)**: 28-31 cipher lines each, every letter "avec chiffre et dechiffrement".
4. **Schlik correspondence, OeNB Cod. Ser. n. 1696-1698**: 28 partly ciphered letters of 1705-07, four writers (Palm about 22), the rest of the Rakoczi-war volume.
5. **Bragadin, Famagusta 1570**, Autogr. 4/6-1: ciphertext only, one page.

## Traps

- Alvin keeps earlier queries as extra AND terms in the session: a second `resultList.jsf?query=` URL returns "No hits" (title shows "Include: {Free text:a, Free text:b}").
  Type each term in the search box and press Enter instead (the session then resets to the one term).
- Biblissima: `javascript_tool` returns "[BLOCKED: Cookie/query string data]" for strings that contain a query string (record hrefs).
- Browser tab 1987536908 (first tab of this pass) was closed by another session part-way; each session should create its own.
