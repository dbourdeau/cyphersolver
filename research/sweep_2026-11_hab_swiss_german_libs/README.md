# HAB Wolfenbüttel and Swiss libraries sweep (9 Nov 2026)

Result: **0 candidate rows, 0 key leads.** Every route into HAB manuscript descriptions or Swiss manuscript full text was
either blocked, not searchable, or already swept. Written so the next attempt does not repeat these probes.

## Routes tried

| Route | Result |
|---|---|
| `https://diglib.hab.de/` (WDB) | **HTTP 200 now** (was TLS reset on 2-3 Nov), but it is only the portal for TEI editions and image frames (`/mss/<sig>/start.htm` is a frameset onto `show_image.php`). `?db=mss`, `?db=mss&list=ms[&catalog=..]` return empty bodies. No searchable manuscript-description text. |
| `oai.hab.de` | Squid "ERROR: URL could not be retrieved". |
| `opac.lbs-braunschweig.gbv.de` (HAB's OPAC, where Cod. Guelf./Extrav. records live) | still unreachable from curl (000) and from Chrome (navigation did not load). **This is the real blocker**: no HAB description text could be searched. |
| K10plus SRU `sru.k10plus.de/opac-de-627` | works, but `pica.isil/bib=DE-23` is unsupported or returns 0; `pica.mat=handschrift` matches printed books about manuscripts (chiffre 475, Geheimschrift 74, chiffren 120, ziffern 147, cifra 267 hits, all print). Not a manuscript index. Only incidental find: Regenbogen 2026, a study of the 1525 Austrian-Württemberg government ciphers in the Peasants' War (so already studied). |
| Heidelberg `digi.ub.uni-heidelberg.de/diglit/hab_mss*` (hosts HAB Extrav. letter scans, e.g. Cod. Guelf. 236.x, 65.1 Extrav., the Andreae/Duke August correspondence) | Anubis bot page for curl; opens in Chrome but is per-letter with no cipher search; titles carry no cipher note. Not a route. |
| e-codices.unifr.ch | `/en/search/all?sQueryTerm=` returns the shell page only (results are JS-loaded); collection is medieval codices, not letters. |
| e-manuscripta.ch search | JS bot check ("quick check"); not clicked through. Already swept by OAI-PMH in `swiss_austrian` (about 75k records, no ciphertext). e-rara is printed books. |
| Printed Heinemann/Milchsack HAB catalogue | already grepped in `sweep_2026-11_german_portals_2`; index "Geheimschriften" entries are treatises/colophons. |

Earlier sweeps checked first (so not repeated): `sweep_2026-11_german_portals`, `_german_portals_2`, `swiss_austrian`,
`browser_pass_oenb_basel_geneva`, `archivportal_d`, `kalliope_ddb` (Kalliope itself covers many HAB letters via the SRU term list).

## Excluded

Nothing was excluded on content; no item-level HAB or Swiss record with cipher letters was seen.

## What remains

- HAB Extravagantes (Butzmann 1972, in copyright) and Cod. Guelf. Novi/Noviss. descriptions: need the LBS OPAC (try another
  network or ask HAB) or the HAB "Handschriften" TEI dumps (a `www.hab.de` page may list them; not found in the time spent).
- Duke August the Younger (author of the *Cryptomenytices*) ran ciphered correspondence; Andreae letters in Heidelberg scans
  are the likeliest HAB cipher letters, but the scans would have to be paged by hand.
- e-manuscripta full-text search remains behind a JS check; only a Chrome pass could use it.
