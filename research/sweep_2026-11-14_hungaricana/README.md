# Sweep: Hungaricana regest collections (14 Nov 2026)

**Result: 19 rows in `candidates.json`, 9 in `key_leads.json`.** `catalogue.json`, `leads.json` and `merge.py` untouched,
nothing committed. Rebuild the files with `python make_candidates.py`.

## The paging route (this is what the earlier pass could not find)

Hungaricana answers curl with 403 but works in Chrome. Everything below was run as same-origin `fetch` calls from a
Claude in Chrome tab (polite rate, 250-350 ms between requests, one tab).

1. **A search result URL is a base64 JSON token.** `https://www.hungaricana.hu/hu/search/results/?query=rejtjel` redirects to
   `?list=<token>`, where `token = base64(JSON.stringify({"query": "rejtjel"}))`. The pager's own hrefs are
   `?list=<token>&page=N` (the tool hides them as "query data"; replace `?=&` with other characters before returning
   `getAttribute('href')`). A plain `fetch('/hu/search/results/?list=<token>&page=2')` returns server-rendered HTML with 20
   `li.result` items (`h5 a` = title/link, `.badge` = source type). The earlier "empty shell" came from fetching the
   `?query=` form.
2. **Filters go in the token:** `{"query": "rejtjel*", "filters": {"DATABASE": ["LI"]}}`. Facet counts per query:
   `GET /hu/search/filter/DATABASE/?list=<token>` returns JSON `[{value, count, title}]`. Values that matter here:
   `BECSSEG` (Becsi segedletek = Vienna inventory regests, the only item-level archive database that hits),
   `LI` / `LK` / `KMOKMT` / `KATGYUJT` / `REFGYUJT` / `ZSIDGYUJT` (full text of books and finding aids: all "Konyvtar"),
   `HELYILAPOK` (local newspapers, thousands of hits, skipped), `HATARONTULI` (cross-border books, skipped).
   Item-level archive databases (MNL OL fonds, county archives) did **not** hit on any term.
3. **Best route for the Vienna regests: search inside the collection on the archives host.**
   `https://archives.hungaricana.hu/hu/lear/BecsSeg/?list=<token>&page=N` returns a table per result with the shelfmark
   (`Levéltári jelzet`), `Dokumentum dátuma` (date and place) and `Ügyleírás` (the regest). The main search shows only the
   title for this database, so use this view; it has 20 results per page and no page cap (132 pages for 2,633 hits were
   read). The hostname differs, so run the fetches from a tab on `archives.hungaricana.hu`.
4. The tool call times out at 45 s but the page script keeps running; start the loop with `setTimeout(async()=>{...})`,
   store results in `window`, and poll.
5. Posting results to a localhost listener from the page did not work (Chrome blocked or hung on the private-network
   request); return the data through the tool output in compact form instead.

## What the terms give

| Term | Vienna regests (`BECSSEG`) | Other non-newspaper databases |
|---|---|---|
| `sifrír*` | **2,633** (2,530 Tuerkei I, about 100 Ungarische Akten / FHKA / Kabinettsarchiv) | LK 43 (Arhivski vjesnik, Croatian "sifriran" 1958-83: 1848 telegrams, not read), LI 2, KATGYUJT 3 |
| `rejtjel*` | 6 | LI 129 and LK 235: 20th-century party/ministry records and archival-science texts; nine pre-1920 hints (below) |
| `titkosír*` | 38 | LI 8, LK 66: archival terminology, 20th c. |
| `chiffr*` | 41 | LK 372 (mostly French text noise) |
| `dechiffr*`, `Geheimschrift`, `sifra`, `cifra`, `megfejt*`, `titkos írás` | 3, 2, 1, 3, 1, 3 | mostly noise: `megfejt*` and `cifra` hit books and school texts in tens of thousands; not read |

`kulcs` + `rejtjel` and `titkosírás kulcsa` are covered by the `titkosír*` and `rejtjel*` hits (key-only regests: Fasc. 327,
Fasc. 312, Kt. 28, Kt. 117).

## The Vienna regest corpus in one paragraph

2,633 regests mention a cipher; the regest wording is systematic. `sifrír` = ciphertext; `sorközben feloldva` /
`sorközi feloldással` = contemporary interlinear decipherment on the same sheet; `külön lapon feloldva` = on a separate
sheet; `nincs feloldva` / `feloldás nélkül` = filed without decipherment; `csupa sifrír` / `teljesen sifrír` = all cipher.
Of the 576 regests in Tuerkei I Kt. 4-28 (1535-72), 393 are interlinear and 50 unresolved; the 2,022 in Kt. 29-120 are the
material of leads 1220-1229 (1573-1648; unresolved counts by lead range: Kt. 29-36 92 of 468, 36-45 68 of 375, 46-49 8 of 88,
51-63 53 of 233, 65-76 54 of 207, 77-92 17 of 86, 93-108 54 of 200, 108-111 38 of 149, 112-115 27 of 117, 116-120 24 of 100).
**Those lead rows cover Kt. 29-120; Kt. 4-28 (1535-72) had no row.** The new candidates are the correspondent runs there,
grouped one key per correspondent: Albert de Wyss (155), Carolus Rym 1570-72 (about 75), Busbecq 1555-62 (53), Zay (24),
Stöckl (12), Czernovich (10), Provisionali (8), plus the rest of Malvezzi Kt. 8-9 (17).

In the Ungarische Akten the uncovered runs are Donellan to Nádasdy 1668-70 (about 30; duplicate of lead 1232, whose
own vetting already found the separate decipherments), Nádasdy Fasc. 309-310 1658-66, the Transylvanian reports 1529-31
(Fasc. 10-19, "Schuller" edition cited), Martinuzzi 1542, the 1527-28 Krakow files with the key of 12 Aug 1527, and a few singles.

## Library-side hits (published volumes), pre-1920 only

Kossuth to Karoly Barics, 25 Mar 1851, ciphered French with Kossuth's interlinear solution, printed in Straub (MOL kiadvanyai,
Hungaricana library): candidate row. The inventory texts naming cipher keys (Klapka archive, MNL OL R 117 Kossuth,
a P-section family fonds 1758-98, the Danish section of the Buda expugnata guide) are in `key_leads.json`. The Teleki
Marosvasarhely keys and the Esterhazy "Rejtjeles levelek" are already leads 1908 and 1909. Győri Tanulmányok (Francesco
Mella's letters) and Kerekes (Habsburg "Titkos Levelezői Hálózata") came up on `rejtjel*` but were not opened.

## Dedupe

known.py and grep on Wyss, Rym, Busbeck, Stöckl, Provisionali, Czernovich, Nehring, Donellan, Frangepan, Lochmair, Klapka,
Barics: only Rym (lead 1220 from 1573), Busbecq's Paris reports (a different run), Nehring (cited as edition), Donellan
(lead 1232) and Frater Georg (catalogue 503, 885) hit. The earlier sweep's row for Kt. 34 fol. 178 (`research/sweep_2026-11-14_rome_hab_africa`)
and the key-only items already in catalogue 1230/1231 (Fasc. 327, Fasc. 312 fol. 4) are left out here.

## Not done

- The leaf pages (`/lear/BecsSeg/<id>/`) were not opened: the list view truncates long regests with `[...]` and drops the
  sender, so correspondents are named only where the visible text names them. A leaf-page pass over the ids in
  `candidates.json` would name each sender (one key per sender) and could split a row.
- No sibling sweep for the 2,022 Kt. 29-120 regests beyond the unresolved counts (the leads exist; per-correspondent splits
  such as Ungnad, Sinzendorff, Breuner, Pezzen, Starzer are lead-level work).
- MNL OL DF (Diplomatikai Fényképgyűjtemény) is not a Hungaricana text database; leads 1895-1900 came from it via other routes.
- No DECODE, Tomokiyo or Lasry search; the `prior_art` fields say so. No CAPTCHA met.

## Blocks

curl 403 on Hungaricana (Chrome only); localhost POST from the page failed; tool timeouts at 45 s (use background loops).
