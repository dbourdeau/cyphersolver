# Milan state archive sweep (2 Nov 2026)

Scope: Archivio di Stato di Milano, Sforzesco "Chiavi e cifrari", Carteggio Visconteo-Sforzesco, Potenze estere, Carteggio diplomatico.
`research/COVERAGE.md`, named in the brief, does not exist in the checkout; the rest of the reading list was read.

## Blocked
`asmilano.cultura.gov.it` is NXDOMAIN. The real host, `archiviodistatomilano.cultura.gov.it`, and its `fileadmin` inventory PDFs
give a Chrome error page in the user's own Chrome (tab opened for this run), and time out in curl and WebFetch (ECONNRESET).
Also dead in Chrome or curl: `archiviodistatomilano.it`, `siusa-archivi.cultura.gov.it`, `lombardiarchivi.servizirl.it`, `www.cultura.gov.it`,
`icar.beniculturali.it`, `san.beniculturali.it`. So the October outage persists. No search of the ASMi catalogue was possible and no scan was seen.

## What worked
- **Wayback Machine** (`web.archive.org/web/2024/<URL>`) serves the ASMi inventory PDFs. Read: *Potenze sovrane e altre voci* (VS 2/1, 258 pp.,
  contains series 13 "Cancelleria segreta. Chiavi e cifrari", p. 216-219), *Potenze estere* (VS 1, summary), *Carteggio interno*, *Carteggio delle
  cancellerie dello Stato* (SA 2). Text grep for cifr*: only VS 2/1 has item-level cipher notes. Next: the other VS and SA inventories on the same route.
- Lombardia Beni Culturali answers in Chrome; it describes fonds only (MIBA002451, MIBA0024D5, MIBA00359B were swept on 28 Oct, `italian_catalogues`).

## Result
4 rows: 0 open, 2 unvetted leads (`candidates.json`), 2 duplicates of leads 1310 and 1311. Nothing was viewed, so nothing is marked open.
- Series 13 (3 scatole, 1447-1736): scat. 1597 and 1598 = DECODE R5380-R5474 and R5476-R5587, already leads 1310/1311 (unvetted); scat. 1591 holds 82 docs
  of 1494-1736 of which only nos. 63-64 are on DECODE (R5297-98); the inventory names Italian-Wars correspondents (row 1).
- Potenze sovrane scat. 1457/1458/1459/1462: single cipher lines in family letters (row 2).
- Keys: scat. 1598 holds an empty folder note for a 1712-13 cipher instruction (cardinal Paolucci / nuncio Odescalchi, Poland). Cerioni 1970 edited the keys; not read.

## Not reached
Potenze estere item level, Carteggio diplomatico / Dispacci reali (Spanish-Austrian period), Archivio Gonzaga (Mantua), Modena, Florence (not in my scope).
Per the brief nothing was added to leads.json, catalogue.json or merge.py, and no git command was run.
