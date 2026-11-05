# Italian state archives sweep, source key italian_state (2 Nov 2026)

**Result: 0 rows.** The cultura.gov.it hosts did not answer, so nothing was swept. `candidates.json` is an empty list.

## Host test (2 Nov 2026)
| Host | curl (12 s) | Chrome |
|---|---|---|
| www.cultura.gov.it | timeout | ERR_CONNECTION_RESET (own tab, read from the error page) |
| siusa-archivi.cultura.gov.it | timeout | navigation reported, page never read; the extension then dropped |
| archiviodistatomilano.cultura.gov.it | timeout | extension connection lost during the call |
| archiviodistatomantova.cultura.gov.it | timeout | not tried (extension lost) |
| archiviodistatofirenze.cultura.gov.it | timeout | not tried |
| www.archiviodistatovenezia.it | 301 (answers) | not tried |

The pattern matches the DigiVatLib and Internet Culturale resets in `research/chrome_pass_2026-11/README.md`: a network-level
block from this machine, not a bot check. No CAPTCHA was seen and none was touched; no login was used. Per the brief, stopped
after the host test and after the extension lost its connection (no retry loop). No web search was used (re-vet without web search).

## Not reached
Milan Sforzesco "Chiavi e cifrari" and Potenze estere, Mantua Gonzaga, Modena (Casa e Stato b. 141 etc.), Florence MAP, SIUSA,
and ASVe via the Da Mosto index (the ASVe site answered curl with a 301 but the Da Mosto index was not opened).
Known keys-not-ciphertext leads from `research/italian_catalogues/` remain the starting point; retry from another network.
