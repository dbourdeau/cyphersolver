# German portals sweep 2 (3 Nov 2026)

Arcinsys Hessen and Niedersachsen, Landesarchiv BW, bavarikon, gda.bayern.de (Staatliche Archive Bayerns) and Wolfenbüttel
(HAB). Follows `sweep_2026-11_german_portals` (2 Nov), which used six Arcinsys terms, kept LABW only to 1750, did not touch
gda.bayern.de and could not reach HAB. Here every harvest runs from a script, with one request a second, and no bot check was met.

Result: 52 new leads (ids 1997-2048; 1989-1996 were taken on main by the UK retest, so this sweep's were renumbered to 2041-2048), **6 promoted** to the catalogue, 3 old leads closed.

## Result by portal

| Portal | Method | Hits | Result |
|---|---|---|---|
| gda.bayern.de | `gda_harvest.py`: requests session, POST `searchForm` with `primefaces.nonce` from the page (`PrimeFaces.csp.init`), 100 a page. Without the nonce: HTTP 500 | 32 terms, 1,996 unique, of which `Ziffer*` alone gave 1,672 (noise); 148 after filtering | 23 rows. **Every unit is "A = Analoges Archivale": no scans**, so all are archive-only |
| Arcinsys Hessen, Niedersachsen | `arcinsys_harvest.py`: `simpleSearch_search`, `search_getFacetTreeJson` (first id is the root), then POST `search_doSearch` with `tableStateJson` and the page's `_csrf` | 41 terms, 968 unique, 280 details fetched by `arcinsys_detail.py`, 95 with scans | 23 rows. Most strong Hesse units were already held from Archivportal-D |
| Landesarchiv BW | `labw_harvest.py`: POST `suche/ergebnis1.php`; print view gives `Bestellsignatur` | 43 terms, 924 unique, 280 after filtering | 6 rows |
| bavarikon | Chrome (Anubis passes by itself) | "chiffriert" 11, "verschlüsselt" 20 | Nothing: printed books and NDB articles. Confirms the 2 Nov result |
| Wolfenbüttel HAB | see below | | **`diglib.hab.de` still not reached** |

### HAB

`diglib.hab.de` and `opac.lbs-braunschweig.gbv.de` reset the connection from curl, WebFetch and Chrome (TLS error 35, same as 2 Nov); `www.hab.de` loads. So this
route is blocked by the network, not a bot check. As a substitute, all 27 volumes of Heinemann and Milchsack's printed catalogue on Internet Archive were grepped
for cipher words. The index has "Geheimschriften: 3095, 3405, 3432, 3586, 3689, 4028" and "occultographiae fragmenta: 3627". The entries read are treatises,
stray lines or a syllable-swap colophon, for example 3405 (a colophon "mit verstellten Silben"), no cipher letter and no leads. The OCR of the index is noisy, so numbers are approximate and not every entry
was found. The catalogue does not cover the Extravagantes (Butzmann 1972, in copyright), so that group is still **not swept**. Try another network, or the K10plus SRU (`sru.k10plus.de/opac-de-627`, works, `pica.tit=Geheimschrift` 211 records, not filtered to HAB).

## Full review of the open leads (3 Nov 2026)

All 77 open leads from these portals (this sweep and older Archivportal-D rows) were reviewed one by one; `review_summary.md` has every
outcome and reason, `review_*.json` the evidence, `apply_review.py` the application. Most promotions are `not online`: they rest on the
archive's description, so their key checks mostly say no key could be tried, and some will become key lookups once scanned (4 h 1815,
E 8 A 208/3, KHA A23-203, 1 Alt 8 Nr. 407). Paging was mostly on contact sheets, so a short cipher run could be missed.

Scans mattered: most leads whose scans could be viewed turned out interlined, key sheets or no cipher, which suggests a similar share of the
`not online` promotions may fall the same way when scanned. Hanoverian chancery files especially (the reviewed Cal. Br. and Hann. 92 pieces, Dep. 110 A Nr. 64).

Follow-ups: NLA HA Dep. 110 A Nr. 116, tables 539-609 (aufn_093, 095), have no gloss past 540 and may be a target; BayHStA Neuburger Abgabe 1989, 6286
needs Altmann 1978 checked; HStAD D 4 487/4 images 119-122 (1792) has the keyword "constantinopolitanus" written over the cipher, and a quick Vigenère and Beaufort test on a rough transcription gave no German.

Correction to the table below: "A = Analoges Archivale" does not by itself mean no scan (Gesandtschaft Wien 1703 is marked A and is digitised). A scan shows as a "Digitalisate" link on the record; none of the reviewed units has one.

## Key test and rule change (3 Nov 2026)

The 8 leads closed as key lookups were rechecked (`apply_key_rule.py`). Only HHStAW 170 III 29 could be tested, and it is not a key lookup: images 24-25 gloss the cipher of ff. 19-20 word by word and f. 22 is a clear copy, so it was read at the time (compared on one run, not every passage). 1690 is the same unit as 2004. 1980 (Oculist Order) stays key_lookup: its key is in print, not in the volume, and the Copiale parallel may mean the text is known.

Rule changed at Daniel Bourdeau's request: a key in the same volume no longer disqualifies a cipher if no decipherment exists (README Conventions; `vetting.key_in_volume`; "key in volume" pill). Promoted under it, **all untested** because neither key nor cipher is online: 1970, 1979, 2004, 2006, 2009, 2016.

Same-volume cases from other sweeps were not re-reviewed: 1252 (Wellcome MS 309, bound-in key of 1889) and possibly 1568 and 1526 need a look under the new rule.

## Promoted to the catalogue (first pass)

| Id | Item | Evidence |
|---|---|---|
| 2012 | NLA HA Dep. 110 A Nr. 111, Count Münster's agents on the Russo-French war, 1810-13 | **Scan viewed**: ff. 141-143 are unbroken digits with nothing over them; archive says "ein Teil nicht dechiffriert". Other pieces in the file are interlined, a likely crib |
| 1649 | HStAD D 4 Nr. 343/3, notebook among Ernst Ludwig's papers, 1732, origin unknown (was a lead) | **Scan viewed**: readable German with a few word signs, no gloss. The weakest of the six: short, few signs. The old lead's Ernst Ludwig attribution and 1667-78 date were corrected from the finding aid |
| 2014 | NLA WO 1 Alt 22 Nr. 786-788, Gross's 404 reports from Moscow and St Petersburg, 1731-40, "in Chiffern" | Not online; archive's description |
| 2007 | BayHStA MA Politisches Archiv 9, Gravenreuth at Napoleon's headquarters, 1805, "aufgelöst und nicht aufgelöst" | Not online; archive's description |
| 2001 | BayHStA Grassegger-Sammlung 15280, letter to Gise on the Polish crown, 1667 | Not online; archive's description |
| 2046 | BayHStA Kasten blau 61/3, Wippermann, 1639-51, "nicht aufgelöste Chiffren" | Not online; archive's description |

The prior-art searches behind these are web searches and `known.py`; several sources appeared only as snippets and are marked so in the vetting blocks. Tomokiyo's site was not read page by page.

## Closed

Leads 1943, 1944, 1622 (NLA HA L 1 Nr. 548 and 562, Heinrich 1519 and 1522): the file's first leaves are a 19th-century archivist's sheet with the key table and the deciphered words.

Seen and not added: HStAD D 4 Nr. 113/9 (1643) carries its decipherment between the lines (image 3) and in the margin (image 15); it is listed under catalogue 568.

## Best leads still open

- **HHStAW 171 S 995** (already catalogue 566): whole openings of running sign cipher, 1606-29, the largest unread text seen in this sweep. Viewed at image 19. Its key candidate C 667 is scanned (139 images, images 40 and 100-101 viewed: von Reydt's numeric key, name lists, a sign key "Erste Ziffer"), not compared sign by sign. This is the one to attempt next.
- NLA WO 1 Alt 8 Nr. 549, Heinrich the Younger 1540-42, "große Teile chiffriert": not promoted, because a printed study reproduces his single-letter cipher from 1 Alt 8 Nr. 490, so it may be a key lookup.
- BayHStA MA 16 (1812 campaign): "Chiffren (nicht aufgelöst)", but cipher tables are in the same volume.
- HStAM 4 h Nr. 1411 is `targets/malsburg1637`; the scans are now known to be free on Arcinsys.

## Key leads (bare keys, not rows)

BayHStA Kurbayern Äußeres Archiv 2681 (Maximilian I's keys 1620-48), 2397, 2398 (1631, Chiffrenalphabet); StAN Schwedische Kriegsakten 80 (Nuremberg number key 1633, reads catalogue 587?); BayHStA Gesandtschaft Paris 65 (Palatine key 1717-58); BayHStA Kriegsarchiv Serienakten 246 (table 1743-44); signature 633 "Die Chiffern und Chiffriersysteme" 1799-1917; 75736-75758 (Bavarian legation ciphers 1832); StAN Ansbach 16999 (tables 1754); GLA 48 Chiffren units; HStA Stuttgart A 16 a Bü 237, 402; NLA WO 2 Alt Nr. 2837-2842; HHStAW 171 C 667, Z 1807 (Z 1807 image 10 also holds a page of sign cipher).

## Duplicate checks

`newcheck.py` matches shelfmarks loosely, but the archive prefix must be left off: "HStAD D 4 343/1" missed the catalogue's "Hessisches Staatsarchiv Darmstadt, D 4 Nr. 343/1". The first pass therefore reported most of Hesse as new, and re-reading the catalogue's shelfmarks by hand corrected it. Two more (GLA 50 Nr. 924, HStA Stuttgart A 205 III Bü 5) only once the print view gave the real signature. **Get the real signature before checking.**

Not all 52 leads had `known.py` run on every name; the merge also drops exact shelfmark matches. Expect a few overlaps among the unvetted leads.

## Tool notes

- Thumbnails on `digitalisate-he.arcinsys.de` and `arcinsys-digitalisate.niedersachsen.de` are about 150 px, too small to spot cipher; drop `/thumbs/` for the full image (curl works). Probe the last image with HEAD.
- Scans were viewed only for the items named here. Images stayed in the session's scratchpad, not in the repo.
- A run of `merge.py --write` on an unpatched `candidates.json` was reverted before anything was committed; run the patch and the merge with `set -e`.
