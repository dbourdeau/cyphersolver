# Chrome wave 13 (15 Nov 2026): non-European archives and English-language collections

**Result: 4 new leads (one Montauti 'Ciphers' folder at Stanford; three Waseda Okuma-papers rows carried over from the unmerged `sweep_2026-11-15_jacar_retry`). Nothing promoted (no ciphertext seen).**

## Routes tried
| Source | Outcome |
|---|---|
| **Online Archive of California** (`oac.cdlib.org`) | Works in Chrome. Search parameter is `q` (the `query` parameter shown in the page URL is ignored: 9.6 million entries). `/search?q=<term>&group=false&per_page=100&page=N` fetched same-origin and parsed (`article` elements). Terms: cipher (483 entries; 'ciphers' is stemmed to the same set), cypher (102), cryptogram (30), "secret writing" (13), "in cipher" (22), "in code" (69), cifra (20), chiffre (15); cifrado not reached (the OAC returns HTTP 405 after about 10 fast requests; wait several minutes, 6 s pacing). Almost all hits are 20th-century or noise (Francis Bacon Library at Huntington, American Cryptogram Association, railroad and business codes). Pre-1865 material is already in the catalogue (Huntington Loudoun, Blathwayt, Duckworth rows, Civil War cipher books). New: Stanford M0320 Montauti papers, folder 'Ciphers' (lead 1 of this wave). |
| **Duke Archives and Manuscripts** (`archives.lib.duke.edu`) | Answers without a challenge now. `/catalog?q=<term>&search_field=all_fields&per_page=100&group=false` same-origin. 10 terms: 8 hits for 'cipher', all noise or already known (Frank Baker papers 'Journals, diaries, and cipher 1732-1791' is John Wesley's shorthand diary; Mazzoni pamphlet 'CIPHER LETTER' is Egidi's 1906 offprint on Giovanna I of Naples 1380, a printed study). No lead. |
| **TARO Texas** (`txarchives.org`) | Anubis passes in Chrome, but the search API `/api/finding_aid/search/` ignores every query parameter tried (params, query, q, generalField) and returns the first 10,000 finding aids; the page shows 'cipher' as 10,000 results. Unusable for text search. |
| **LAC Collection Search** (`recherche-collection-search.bac-lac.gc.ca`) | Cloudflare 'Just a moment' did not clear in 17 s; not clicked. |
| **Archives Hub** | Cloudflare, tried once, skipped. |
| **natlib.govt.nz, collections.archives.govt.nz** | Blank page (blocked) in Chrome. |
| **NYPL Archives** | Loads an Incapsula shell; search results not delivered to a same-origin fetch; not clicked. |
| **UConn ArchivesSpace** | 403. **UVA archives, Hagley finding aids**: ERR_TOO_MANY_REDIRECTS. |
| **Waseda kotenseki** | Still 'Scheduled Maintenance' (15 Nov 2026). |
| **JACAR rest_refs (2,122 body-text records)** | `scan1.py` restarted single-threaded in the worktree (`scan_rest.jsonl`, not committed, about 4 s a record); first 73 records: administrative only, no digit runs. Not finished at the time of the push. |

## Not reached
AGN Mexico, Colombia, Argentina and Chile catalogues, BNDigital, SIAN, South African archives (eHive, NAAIRS), Sri Lanka, Ethiopia, Philippines: no new route found or tried beyond what `canada_latam`, `latam_*` and `asia_*` recorded.
