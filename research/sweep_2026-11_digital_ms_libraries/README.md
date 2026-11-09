# Digital manuscript libraries with their own search APIs (9 Nov 2026)

Result: **0 candidate rows, 0 key leads.** Every named source was either already swept or returned only noise.

## Routes and results
| Source | Route | Terms / hits | Outcome |
|---|---|---|---|
| Manuscriptorium | castor Solr API; swept in `swiss_austrian` (`manu.py`, ~110 term variants incl. all Czech/German/Italian/Polish/Hungarian terms) | not rerun | Done; 95% printed noise, BNP letters already rows |
| BSB / MDZ | `https://www.digitale-sammlungen.de/api/search?handler=simple-metadata&query=T&pageSize=100&startPage=N` (works with curl). `bsb.py`: 26 terms (Chiffre, chiffriert, Geheimschrift, Ziffern, cifra, cipher, Korrespondenz Chiffre ...), non-print only | 288 non-print records | Noise: Strauss music sketches ("Ziffern"), medieval codices, autograph letters matched on "Brief" only, Cod.gall. 987 (1857-61 diplomatic letters, matched "Korrespondenz"). No cipher letter. Metadata is not indexed for cipher words, as `central_archives` found. Camerariana ("in Chiffern") is in `wainut_leads_2026-11-03` |
| Digital Bodleian | `https://digital.bodleian.ox.ac.uk/search/?q=T&format=json` with header `Accept: application/json` (SPA otherwise); `bod.py`, 26 terms | 20 objects | Noise (Hatton 113 partial-cipher signature, Godwin diary, St John's 17 cryptographic alphabets, Disraeli 1825 coded passage in a 19th-c. volume, not a lead). Archives side was done in `uk_libraries` |
| Wellcome | API | - | Done in `uk_libraries` |
| Polona | `polona.pl/api/search-service/search/simple` | - | Done in `polish_archives` |
| CUDL | AWS WAF 202/403 to scripts | - | Done in Chrome by `uk_libraries` |
| Digital Scriptorium | 403 to curl | - | Not reached (medieval/Renaissance US holdings, little cipher prospect) |
| dLib.si (Slovenia) | server-rendered results page exists, but the `keywords=` query syntax returned unfiltered/500 for non-ASCII terms | 0 usable | Not reached; JS/odd syntax |
| NSK Croatia | `digitalna.nsk.hr` 400/302 to scripts | - | Not reached |
| BNP, Europeana, Kalliope, Kramerius, DigiVatLib, ÖNB | earlier sweeps | - | not repeated |

## Left
Digital Scriptorium and NSK/dLib.si would need a browser (Chrome was reserved for another agent). Neither is a likely home for ciphered letters.
