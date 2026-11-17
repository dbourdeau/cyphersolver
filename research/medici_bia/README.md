# Medici Archive Project (BIA / MIA) sweep, 26 Oct 2026

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Target portal: the Medici Archive Project's document database
(formerly BIA, now **MIA**, `mia.medici.org`), which abstracts letters of the Archivio di Stato di Firenze (ASF),
*Mediceo del Principato* (MdP, 1537-1743).

**Result: the portal could not be searched.** One candidate row was written from the DECODE side, and two leads are
recorded below. The sweep should be rerun once someone with a MIA account can log in, or when ASF is back online.

## What blocked it

- `bia.medici.org` now redirects to `mia.medici.org/Mia`. Every route there, including the HTML app, `/Mia/index.html` and
  all `/Mia/json/...` endpoints tried, returns 302 to `LoginUser.do` (Spring Security login). medici.org's
  "Access MIA" page and library guides confirm that **registration is required** to search. The built-in browser
  profile is not signed in, and creating an account is not something the agent may do. No public or guest search,
  no open API and no data dump was found (`docsources.medici.org`, `/Mia/public`, `/Mia/guest` probed: 404 or no host).
- `https://bia.medici.org` has a certificate for the wrong name (curl `SEC_E_WRONG_PRINCIPAL`; the built-in browser
  also refuses it). The http URL lands on the same MIA login.
- **ASF is offline**: `archiviodistatofirenze.cultura.gov.it` times out on port 443 (curl and browser). So the
  online MdP inventories (`allegati_inventari_on_line/*.pdf`) and any ASF image viewer could not be checked.
  `targets/medici1425/NOTES.md` already records the ASF servers as down.
- The Wayback Machine (for cached old BIA `DocSources` pages) returned 429, then "temporarily offline".
- Web search turns up no indexed MIA record pages. MIA records are not crawled, so a search-engine route does not work.

### To unblock
Daniel (or anyone with a free MIA account) logs in to `https://mia.medici.org` in the built-in browser. A sweep agent
can then capture the XHR search endpoint (advanced search over the synopsis / "extract" field) and run the planned
terms: cipher, ciphered, encrypted, code, cifra, cifrato, cifrata, decifrato, "in cifra", deciphered, "with
decipherment". MIA synopses mark "in cipher" passages, so this should give dozens of rows (MdP volume, folio, MIA doc id).

## Candidate written (1)

| # | Item | Why kept |
|---|------|----------|
| 1 | ASF "Governo Mediceo - cifre ... nn. 1001-1214", item 174 = **DECODE R7397** (3 pp., N/A, no metadata) | the only ciphertext record in the DECODE Mediceo key volumes with no plaintext; keys R7396/R7398 sit on each side |

## Key lead: the Medici chancery key volumes on DECODE

DECODE holds **about 1,770 records from ASF "Governo Mediceo - cifre de' secoli XVII-XVIII"** (DECODE names
`ASFi_SIVol1`...`SIVol14` and `ASFi_SIIVol1`...`SIIVol9`, records R5687-R7459, nearly all record type 2 = key, status N/A).
They are the grand-ducal chancery's own cipher keys. Any MdP cipher letter found later through MIA should be tried
against them first (class A/B). Per-volume counts in the list dump: SIIVol1 217, SIIVol2 213, SIVol1 198, SIIVol6 191,
SIVol6 143, SIVol3 130, SIVol5 129, SIVol2 111, SIVol14 87, SIVol9 76, SIVol8 68, SIVol10 67, SIVol7 65, SIIVol9 33,
SIVol4 32, SIIVol7 12. Five ciphertext records are mixed in: R7019, R7021, R7024 and R7234 carry a plaintext (Cryptoole: solved),
and R7397 does not (the candidate above).

## Leads looked at and not kept

- **Penn, Kislak Center, Oversize Ms. Codex 531**: Cosimo III (16 letters, ff. 1-41, 1694-96) and Cardinal Francesco Maria
  de' Medici (34 letters, ff. 52-118, 1690-96) to Marchese Anton Francesco Montauti, Tuscan envoy in Vienna (the
  marriage negotiations for Cosimo's son). The catalogue says "many are partly in cipher", and the images are online
  (IIIF `https://colenda.library.upenn.edu/items/ark:/81431/p3h70809q/manifest`; Colenda is being replaced by
  digitalcollections.library.upenn.edu). Viewed ff. 6r and 17r, plus contact sheets of every leaf: Cosimo's letters carry long
  numeric cipher passages (two-digit groups such as 13 14 16 19 25, some with superscripts) with a **full interlinear
  decipherment** by the recipient. The cardinal's letters look clear. So the volume was **read at the time**. It is left out
  under the brief, but it is a good **key-rebuild source** for the 1690s Florence-Vienna cipher. That cipher may also
  appear among the DECODE Mediceo keys, and it would read any un-interlined Montauti despatches in MdP (Vienna
  legation files). Not in the repo (known.py: Montauti, Codex 531, Cosimo III: no hits).
  Since 15 Nov 2026 the Montauti papers have a target, [`targets/montauti1692/`](../../targets/montauti1692/) (Andrew
  Beling, with AI agents, pull request #665): Ms. Codex 533, Cosimo's autograph letters, in a different cipher of
  two-sign groups, its key rebuilt from the interlined despatches of Oversize Ms. Codex 534. The dotted number
  cipher of Codex 531 described here is not that key and is still not worked.
- **Marco Vito (Vienna) project on the encrypted Medici documents of 1486-1491** (letters to Lorenzo il Magnifico,
  *Mediceo avanti il Principato*). The project describes them as not yet decrypted, but it is pre-1537 (outside this
  portal), active work by another researcher, and the paper PDF (dspace.ut.ee) timed out. Already noted in
  `research/oldest/scan_2026-09-23/italy.md`.
- Bertomeu Masià's imperial ciphers of Florence 1537-38: keys reconstructed in print, so they are solved.
- Lasry/Simonetta/Biermann on Antonio Elio: the Medici despatches intercepted by the Carafa were broken at the time.

## Searches run
- curl / built-in browser: `bia.medici.org`, `mia.medici.org/Mia/*` (login wall), medici.org databases pages, ASF site
  (timeout), Wayback CDX (429/offline).
- Web: "Mediceo del Principato" with "in cipher" / "in cifra" / "non decifrata"; MAP + ciphered; cryptiana + Medici;
  Medici + HistoCrypt/Lasry; Marco Vito. No MdP cipher letter with an open status turned up in print or on the web.
- known.py: Mediceo, Medici, Firenze, Montauti, Codex 531, Cosimo III, R7397, R7234, R7024, R7021, R7019.
- DECODE list dump (`research/catalogue_harvest/decode/list.json`): 1,887 records with Florence/ASF in the holder or author;
  the ASF Dieci di Balia set (R3753-R3789) and the Niccolini set (R4034-R4054) are already covered by the repo.

No scripts were kept: the dump queries were one-line Python run against `list.json`/`views.jsonl`.
