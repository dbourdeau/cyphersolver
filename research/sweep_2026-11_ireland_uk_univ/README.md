# Ireland / UK universities and county offices (9 Nov 2026), source key `ireland_uk_univ`

Result: **0 candidate rows**. This area was already swept almost completely (`uk_tna`, `tna_discovery`, `uk_libraries`,
`sweep_2026-11_uk_ireland`, `sweep_2026-11_uk_retest`, `archiveshub`); TNA Discovery already indexes most county record offices.

## Routes
| Source | Route | Result |
|---|---|---|
| NLI Sources (sources.nli.ie, VuFind) | Cloudflare 403 to curl; opens in Chrome; same-origin fetch pages 1-3 of "cipher" (51 hits) worked, then returned 0 results (challenge/rate), stopped | It is an index of Irish-history sources held mostly in BL, Bodleian, TCD, Vatican etc., largely calendared/printed (Ormonde, Orrery, Wallis letter-book, Tanari Brussels cipher, Gualterio tables). Nothing item-level new; NLI catalogue.nli.ie itself 403, not reached |
| Durham (reed.dur.ac.uk/xtf) | curl works | "cipher/cypher/in cipher/decipher": Elliott MSS 9 (Francis I to Richer 1547) and 10 (Mazarin to Henri Arnauld 1646) are ciphers but come with a deciphered transcription (Bougé; deciphered text written in): excluded. Rest is Sudan/Egypt 19th-20th c. telegrams (Wingate, Hicks Pasha, Grey, Ponsonby) and Wylde 1877 (Gordon recommending a cipher) |
| Edinburgh Univ. ArchivesSpace | curl, `q[]=` form | cipher/cypher/cryptogram/in cipher: 1 hit each, a medieval ownership note; nothing |
| Hull History Centre | curl `/catalogue?q=&search_field=all_fields` | cipher 0; cypher 3 (U DDHO/3/19, /30 Reichenbach's cypher c.1730, already in `archiveshub`) |
| Royal Society CalmView | curl | "database down for maintenance"; retry later (low expectation, scientific papers) |
| Cambridge ArchiveSearch, UCD, Leeds, Archives Hub, Bodleian | 403 / Cloudflare / Anubis to scripts | covered by earlier sweeps in Chrome (Cambridge, Bodleian, Hub); UCD, Leeds not reached |
| Rylands, St Andrews, Glasgow, Cork, Irish Jesuit/Franciscan | hosts timed out or no item catalogue; a web search found no Irish cipher letter | not swept |
| Wellcome API | works, already done in `uk_libraries` | not repeated |

## Left
NLI catalogue.nli.ie and UCD Archives (Chrome pass with Cloudflare cleared), Leeds Special Collections, Rylands ELGAR,
St Andrews/Glasgow catalogues, Royal Society retry, Chatsworth/Longleat (no online item catalogue).
