# UK blocked catalogues, Chrome pass (15 Nov 2026)

Source key `uk_blocked_chrome`. Retest, in the user's Chrome, of the item catalogues recorded as blocked in
`research/COVERAGE.md` (NLS, NLW, TCD, Lambeth, PRONI, NAI, NRS) plus Bodleian, Cambridge and Beinecke.
`candidates.json` holds **6 rows**, `key_leads.json` 2. All are scored from catalogue text; none was viewed, so none passes the
vetting bar. Nothing was merged or promoted. Rebuild the rows with `make_candidates.py`.

## Which source needed Chrome, and the route

| Source | Result | Route |
|---|---|---|
| NLS manuscripts.nls.uk (ArchivesSpace) | 403 to scripts; Cloudflare "Performing security verification" cleared by itself after about 20 s in Chrome, no checkbox | `/repositories/2/search?q[]=TERM&op[]=&field[]=&from_year[]=&to_year[]=&page=N`, same-origin `fetch()` from the page, rows `.recordrow`; terms cipher, cypher, ciphers, cyphers, in cipher, decipher, decyphered, cryptogram, secret writing, cypher key, key to cipher: 81 distinct records. Subject facet (`filter_fields[]=subjects&filter_values[]=Ciphers. Codes.`, with `q[]=*`) gives 26. About 70 hits are Balfour of Denmilne ownership ciphers and were dropped. Nearly everything else was already in `catalogue.json` or `leads.json` (MS.3471, 16962, 17018, 16914, 11732, 12551, 6135, Adv.MS.80.3.48-50, 80.7.7); new: Adv.MS.33.1.13 and the Gaelic scribal cipher |
| **NLW archives.library.wales (AtoM)** | **Newly swept.** Earlier sweeps: Cloudflare, then "catalogue unavailable". Today it opens in Chrome with no challenge | `/index.php/informationobject/browse?topLod=0&query=TERM&sort=relevance&page=N`, same-origin fetch, rows `article`; cipher 7, cypher 7, ciphers 2, cyphers 4, decipher 11, secret writing 11, cyfrin 4, dirgel 9; 54 distinct. Most are the Lord Rendel papers (Campbell/Hart telegrams, 1884-85, plaintext) and noise. Real: MS 9066E 2378 and MS 9235A. Welsh terms returned nothing cipher-related |
| Bodleian archives.bodleian.ox.ac.uk | Anubis passes in Chrome (as in `uk_libraries`) | Same ArchivesSpace route; 11 terms, 887 records, 200 with cipher words. Already swept in `uk_libraries` (274 records), so only a diff was taken: Thurloe/Rawl. A, Tanner, Carte, Clarendon 94, Add. C. 276, Talbot b. 29, Rawl. C. 392 are known. New: Talbot b. 19 only. Rawl. D. 571, D. 870, Eng. hist. g. 15 are deciphered copies, not ciphertext, so left out |
| Cambridge archivesearch.lib.cam.ac.uk | Opens in Chrome; 10 terms, 121 records, 97 with cipher words, 54 dated pre-1920 | Same route (25 per page). Already swept in `uk_libraries` (330 records). Known: Add.8863/3 (Ferdinand II to Mansfeld 1631), Add.110. New: Add.7475/2 (Rolfe 1905, 20th c.). Crewe, Mayo (Add.7490) and Macdonald items are decoded cypher telegrams, not taken |
| TCD digitalcollections.tcd.ie | A Cloudflare "One More Step / security check" interstitial showed once; it went away without any click, then the catalogue answered. "cypher": 0 records | `/catalog?q=cypher&search_field=all_fields` |
| TCD manuscripts catalogue `manuscripts.catalogue.tcd.ie` | **Blocked, not a bot wall**: `ERR_CONNECTION_RESET` in Chrome (same as the 3 Nov timeout to scripts). Not swept | none found |
| Beinecke / Yale `archives.yale.edu` | **403 Forbidden** for every path in Chrome, including `/` | none; the US gap is left to the `us_gaps` sweeps |
| John Rylands | `archives.library.manchester.ac.uk` does not resolve (guessed host wrong); not found. Rylands holdings are on Archives Hub, swept earlier | not searched here |

Not re-run (covered with item-level text in earlier sweeps and no new route today): Lambeth (cipher/cypher, `uk_libraries`,
`uk_retest`), PRONI eCatalogue (cipher 39, cypher 54), NRS (528 records, 29 Oct), National Archives of Ireland (no early item catalogue).
Hatfield, Longleat, Chatsworth, Chetham's, Bristol, Gloucestershire, Cheshire, Lancashire and Yorkshire record offices were not
tried: none has a public item-level search that was found in this pass (their material is reached through TNA Discovery and Archives Hub,
both swept). No CAPTCHA or human-verification checkbox was clicked or solved.

Technical notes for the next run: the browser tool refuses to return any string that looks like a URL with a query string, so strip
`? & = : /` from returned snippets; long-running crawls must be started without `await` (an awaited loop times out after 45 s) and polled.
Output per call is cut at about 900 characters, so print in slices of 6-9 rows.

## Rows

1. NLW MS 9066E 2378: 18 Jul 1663 news-letter with numerical cipher and key overleaf (best).
2. NLS Adv.MS.33.1.13: Denmilne vol. with the subject heading Ciphers. Codes. (Shirley, Savoy-Spain 1615).
3. Bodleian MS. Talbot b. 19: Grenville to Fitzgerald, Swiss Cantons, 1792-94, some in cipher.
4. NLS Adv.MS.72.1.33, 72.2.10, 72.1.5: Gaelic Beaton-school colophon cipher.
5. NLW MS 9235A: 17th-c. recipes and astrology with cipher notes.
6. Cambridge MS Add.7475/2: Rolfe to Grant Richards, 2 Feb 1905, written in cipher.

## Key leads

NLS Dep.353/11 (signal codes, early 19th c.); NLW Rendel papers, Campbell letters on Hart's cipher telegrams 1884-85.

## Left out, read at the time

NLS Adv.MS.35.4.14 (Thoirs of Muiresk commonplace books: "cipher drawings" are decorative); NLS Acc.14105 (Drake letter 1804, record
has no cipher text; the Drake lead is already in the ledgers); NLW Brecon letter of 1795 ("your cipher is on" a harness); Bodleian
MS. 16644/27 (decrypted diplomatic cypher, copy).
