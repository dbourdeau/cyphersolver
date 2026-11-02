# Russia sweep, 2 Nov 2026 (27 rows)

Rows: `candidates.json`, built by `make_candidates.py`. All are leads scored from archive descriptions (nothing viewed).
`known.py` run on the fonds and names (Pokotilov, Ф. 560, Ф. 1614, Kovalevsky, Timiryazev, RGIA, Ф. 472): no hits.

## What was reached (scripts, one request per 2.5-3 s)
| Source | Method | Result |
|---|---|---|
| RGIA, fgurgia.ru (KAISA) | simple search + `/ajax/tree/<index>` JSON, 18 Russian stems (шифрован, цифирь, тайнопис, дешифр ...), case level | 194 cases; about 25 are real ciphered-correspondence files 1875-1917; 23 rows. Most others are cipher-regulation files, monogram "шифр" (royal cypher) awards, or decrypted copies |
| RGAVMF, rgavmf.ru/search | Drupal search, item titles, pre-1917 filter, 13 stems | 208 items; mostly keys and cipher regulation (key leads, not rows); 4 rows |
| docs.historyrussia.org | metadata search, 8,200 rows over 13 terms | Printed, edited documents; "шифр" mostly means the archive shelfmark. Ciphered Petrine letters there (Dolgorukov, Denmark/Holland 1710-12; Podlinnye tsarskie pisma t. VI-VII) are printed with the decipherment: read, no rows |
| Internet Archive full text | 27 Russian phrase queries ("писано цифирью" ...), 286 page hits | Petrovsky sbornik, Alexei case, Vorontsov archive, Russkaya starina: ciphered passages printed with plaintext. No rows |
| Wikisource-ru | API search, 11 terms, then HTTP 429 | Printed texts, no shelfmarks; stopped |
| Prozhito | no public search API found | not swept |

## Blocked
* **rgada.info, archives.ru, rusarchives.ru, prlib.ru**: connection reset or timeout from this machine; Chrome (one tab, rgada.info) shows the same error page. Network-level, not a bot check, so stopped as instructed. avpri.ru does not resolve. garf.su returns 403 to curl (not retried in Chrome, no time).
* RGIA scan availability was not checked per case; rows say "unknown".

## Not reached
RGADA, AVPRI, GARF, RNB, RSL manuscripts, Presidential Library: the sources most likely to hold 17th-18th century Russian ciphers. Try another network or Chrome on GARF. Pre-1850 RGIA is thin in the index for these terms.

## Key leads (no rows)
RGAVMF Ф. 16 Оп. 1 Д. 113 and Д. 50 (Likhachev's ciphers, Far East); Ф. 243 Оп. 1-3 Д. 9514; Ф. 418 Оп. 1-4 Д. 5487А; RGIA Ф. 508 Оп. 3 Д. 1070-1071 (palace police keys, 1850-1917), Ф. 600 Оп. 10 Д. 1162-1164 (Persia bank dictionaries), Ф. 560 Оп. 28 Д. 96-98 (cipher dictionaries issued), Ф. 23 Оп. 33 Д. 369 (1916 dictionary), Ф. 472 Оп. 66 Д. 46 (telegraph cipher 1896-1900).

## Honest note
Few rows (27 against the 60 aimed at) and almost all are 1875-1917 ministerial telegram files, the weakest class. Several (Kovalevsky 1880, Cromariot, Butakov) may have decrypted copies filed with them. Not padded.
