# Florence (ASF Mediceo) sweep, 2 Nov 2026

Terms: none run. Counts: 0 records seen, 0 rows, 0 candidates (candidates.json is `[]`).

## What blocked it
Tested in a fresh Claude in Chrome tab, no login attempted, no check solved:
- archiviodistatofirenze.cultura.gov.it: does not answer (Chrome error page, host still down as in October).
- siusa-archivi.cultura.gov.it: same, Chrome error page.
- www.archiviodistato.firenze.it (old ASF host): same, Chrome error page.
- mia.medici.org (Medici Archive Project, ex-BIA): answers, but every route redirects to LoginUser.do; registration required, so not searched.
- archivesportaleurope.net: opens, but the search page returned only the filter boilerplate for "Mediceo cifra" (no result list rendered; ASF is not a known contributor). Nothing usable.

## Not reached
Mediceo del Principato, Mediceo avanti il Principato, Signori Carteggi inventories and any ASF image viewer; MIA synopses naming cifra/cifrata. Not tried: Internet Culturale, Archivi del Rinascimento (neither is known to hold ASF inventories).

## Unblock
A MIA account logged in by the user (see research/medici_bia/README.md), or ASF coming back online. Existing lead: DECODE R7397 (medici_bia/candidates.json).
