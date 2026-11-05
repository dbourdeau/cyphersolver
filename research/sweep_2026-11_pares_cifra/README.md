# sweep_2026-11_pares_cifra (PARES "cifra" / "descifrado", AGI Ultramar, AHN region)

Result: **0 rows** in candidates.json (empty list). Nothing was padded.

## What blocked
- 2 Nov 2026, 21:13-21:16 UTC: PARES answered **429 Too Many Requests** to the first request of every attempt:
  `catalogo/find?nm=&texto=descifrado` through `run.py` (sweep.py's session recipe, 3 s delay, own hits/progress
  files here) at 21:13:55 and again after a 100 s wait at 21:15:39; a plain curl to `find?texto=cifra` (429); and
  one load of the same URL in the user's Chrome (429 page). Same machine IP as the Oct 2026 block (see
  research/pares_ags/README.md); other fleet agents share it. Per the brief, no further Chrome tabs were opened and
  nothing was retried in a loop. 5 requests in all.

## Not reached
- "cifra" and "descifrado" (never run in October either; only "descifrado" probes of 1 request each, no rows).
- AGI Ultramar and AHN region runs.
- Nothing was screened with known.py, since there were no new hits.

## To resume
`python research/sweep_2026-11_pares_cifra/run.py cifra` (then `descifrado`, then facet jobs such as
`run.py cifra idFI=16`) writes to this folder's hits.jsonl / progress.json only (MAXREQ env caps requests, default 12;
note run.py sets a 3 s delay as briefed, but use the 20 s sweep.py default if the IP is shared and was blocked).
Facets (`idFI=<century>`, `idD=S`) are the working date filter; anio1/anio2 are ignored by PARES. Wait until a probe
returns 200 first. Keep only units with images and no decipherment noted; run known.py on legajo and folio.
