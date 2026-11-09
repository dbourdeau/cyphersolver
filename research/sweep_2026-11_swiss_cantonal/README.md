# Swiss cantonal and city archives sweep (9 Nov 2026)

Result: **5 candidate rows** (`candidates.json`, built by `make_candidates.py`), 6 key leads (`key_leads.json`). No Chrome, no BNE.

## Routes

| Route | Result |
|---|---|
| **Burgerbibliothek Bern** `https://katalog.burgerbib.ch/` (scopeArchiv) | **Works with curl**, same postback as `research/swiss_austrian/scope_harvest.py` (copied here). ~40 terms; 365 distinct records; the yield of this sweep. Images: `getimage.aspx?veid=ID&deid=10&sqnznr=1&width=1600&klid=9` works for real digitised leaves (Bongars Cod. B 149), but the "Korrespondenzkartei" units show only index-card thumbnails (deid=0) |
| **swisscollections.ch** (VuFind, all SLSP libraries: Basel UB, ZB Zurich, KB Vadiana, Zofingen, Solothurn, Luzern, Bern UB, Aarau, Trogen) | **Works with curl**: `/Search/Results?lookfor=T&type=AllFields&limit=100&page=N`; record MARC via `/Record/<id>/Details`. `/api/v1` is denied. 1,662 distinct records over 28 terms (`swisscoll.py`, `sc_a.jsonl`); about 95% printed books, music (basse chiffree), Basel economic archive. Real hits are in Vadiana |
| Staatsarchiv Bern (`www.query.sta.be.ch`), Stadtarchiv Zurich (`amsquery.stadt-zuerich.ch`), Schwyz (`query.staatsarchiv.sz.ch`) | scopeArchiv postback works; 0 relevant (Bern 1943 Chiffrierbuero; Zurich city: 20th c. "Chiffre" ads; Schwyz 0 hits for every term, suspicious but nothing to follow) |
| Staatsarchiv Zurich | already swept in `swiss_austrian` (270 hits, modern) |
| archives-online.org (federated search of ~50 Swiss archives) | page loads, but results arrive over SignalR (`/signalR/hubs`); not scripted. A browser session would give one search across StALU, StAAG, StASG, StAGR, StATG, StASO, AEN, ACV etc. |
| Basel `dls.staatsarchiv.bs.ch` | 403 to curl (needs browser; done in `browser_pass_oenb_basel_geneva`) |
| BGE Geneve `archives.bge-geneve.ch` | Anubis proof-of-work page; not passed |
| Other canton hosts (Luzern, Aargau, Graubuenden, Thurgau, Solothurn, Zug, St Gallen, Fribourg ...) | guessed `query.staatsarchiv.XX.ch` names do not resolve; use archives-online |

## Terms

Burgerbib: Chiffre 1, chiffriert 14, Chiffren 0, Geheimschrift 8, chiffre 1, chiffres 2, en chiffres 1, z.T.chiffriert 6, Chiffrierschluessel 3, verschluesselt 4, Chiffrenschrift 1, Kryptogramm 1, Entzifferung 2, Ziffern 205 and Schluessel 121 (read by title only; noise), wildcards (`chiffr*` 0, `Geheim*` 5, `ziffer*` 26).
swisscollections: chiffriert 1, Chiffre 68, Geheimschrift 49, Chiffren 46, plus chiffre/chiffree/cifra/cifre/Ziffern/Ziffernschrift/Entzifferung/dechiffriert/dechiffrement/cryptogramme/Kryptogramm/Schluessel.

## Excluded and why

- **Lead 1243 (Zurich Tanner 1917)**: already vetted on 9 Nov (Staatsarchiv Zurich ID 5421134); no new route found; Tanner 1917 not online. Left as is.
- **Vadiana Blarer/Bullinger "Geheimschrift"** (VadSlg Ms 36-37, ~1546-57, 5 letters): a few words in Bodenmann's published Blarer cipher (Bullinger Briefwechsel vol. 17; Bodenmann/Kess/Steiniger 2018). Already studied. Musculus's secret writing (Zofingen Pa 14, 1548): resolved by Bodenmann 2000.
- **Schobinger letters, Vienna 1619** (VadSlg Ms 94:174, 180, 190): merchant news letters, only a few cipher words ("S S I E"). Not rowed.
- Vadiana: Haller to Blarer 1559 (one cipher word on the address leaf), Anne de Montmorency 1551 (**rowed**).
- Bernoulli to Mencke 1722 (UBH L Ia 674): a chiffered anagram solution by Pemberton, not a letter cipher. Anquetil-Duperron / Albrecht 1683: numerals.
- Jung-Stilling diaries (UBH NL 67): already rejected elsewhere. Eichenwald "Chiffren" (composition), Basel Wirtschaftsarchiv, music with basse chiffree, hotels "Schluessel".
- Bongars 1597 rowed as class A but weak (names only).

## Prior art

Web searches (9 Nov 2026) for the Erlach/Bernhard set and the Montmorency letter found nothing. The Bern cards are "Korrespondenzkartei" entries and may be inexact. Erlach and Weimar editions (Droysen, Rohr) not checked.

## What remains

- A browser pass on archives-online.org (one search across all cantonal archives) with the terms above; Basel dls, Geneva BGE and AEG remain behind bot checks.
- Burgerbib: ask for scans of Mss.h.h.XXVII.85/87/92 (Morshauser reports 1637) and ES 603.
- Fribourg, Neuchatel, Ticino, Graubuenden archives not reached.
