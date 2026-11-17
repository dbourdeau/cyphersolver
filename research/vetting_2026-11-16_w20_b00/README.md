# Wave 20 vetting, batch b00 (16 Nov 2026)

Claude Code session (Claude Opus 5.5). 18 leads: 1913 1914 1373 1372 1374 1376 1377 1379 1375 1380 2420 2418 2779 2757 2756 2778 1590 1596.
Proposals are in `proposals.json`, built by `make.py`. Nothing in `research/leads.json` or `catalogue.json` was edited.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2757 | open | medium | AEV Cn B 10/1/8: Torcy to J. E. de Courten, Marly 9 Jan 1704, 1 p., "en partie chiffrée", no decipherment noted; the key tables of Nov 1703 are in the same dossier (10/1/1-2) |
| 2778 | open (narrow to FQ 238) | medium | AEV Marclay FQ 238 "Lettre (en partie chiffrée)", c. 1630, public. FQ 372 (dated 22 Oct 1639, Ivrea) "à déchiffrer" reads as an illegible hand (same usage in FQ 365) |
| 2756 | partly_read | high | AEV titles: 5/11/6 "en partie déchiffrée" and 5/11/7 "déchiffrée" by Courten; Stainville's tables 5/11/8 and 8bis are in the dossier |
| 1377 | read | medium | IMH 03-33-162-04-001 is a copy file; p. 1 is the typed English plaintext of a Reinsch telegram (1921-3756) |
| 1380 | read | medium | IMH 03-32-498-02-016/-020 p. 1: the ministry's outgoing draft cover and the telegraph section's receipt for a decoded telegram |
| 2779 | none (key only) | high | AEV Kalbermatten P 196 is a 1723 cipher list, one sheet, with no ciphertext; move it to key leads |
| 1379 | none | low | p. 1 is a Finance Ministry note: a telegram from the legation in France could not be decoded with any ten-digit code book; original attached. 03-44-035 holds telegram drafts of 1926, not code books |
| 1372 | none | low | shelfmark found: 03-46-007-01-019; p. 1 is the receipt cover only |
| 1373-1376 | none | low | IMH reader still unreachable; covers only |
| 1913, 1914 | none | low | AAV not online; the MNL records on Archives Portal Europe return 403 to script |
| 2418 | none | low | Musée 205 not identified; Le Glay II prints the 1519 election papers from Lille, with cipher passages in clear |
| 2420 | none | low | Tant's entry has no cipher word; no AD Aube inventory online |
| 1590, 1596 | none | low | szukajwarchiwach now blocks scripts (Incapsula); no scans |

## Routes
- **AEV (Valais) answers scripts:** use the SRU `https://scopequery.vs.ch/SRU/?operation=searchRetrieve&version=1.2&query=isad.reference="..."` (or `isad.title=word`; a truncation `*` returns nothing), then `detail.aspx?Id=N`. Unit pages give the access rule (Courten: owner's permission; Marclay, Kalbermatten: public). `aev.py` and `aev_detail.py` do both steps.
- IMH: `catalog.digitalarchives.tw` record pages link one first-page image each (`image.digitalarchives.tw/ImageCache/...`), and curl can fetch them. `archivesonline.mh.sinica.edu.tw` still fails (curl exits 35 and 56).
- Blocked to scripts on 16 Nov: Archives Portal Europe (403), szukajwarchiwach.gov.pl (Incapsula), agad.gov.pl/inwentarze (403).
- Tomokiyo and Lasry lists: the copies fetched 15 Nov, searched with `tg.py`.

## Record errors found
- 2757: the place is Marly, not Versailles.
- 2778: FQ 372 is dated 22 Oct 1639, at Ivrea.
- 2779: the date is 1723, not undated.
- 1372: the shelfmark is 03-46-007-01-019; the Waijiaobu received it on 1 Sep 1920.
- 1379: 03-44-035 is not a set of code books, and the series dates from c. 1926-27, not c. 1920.
