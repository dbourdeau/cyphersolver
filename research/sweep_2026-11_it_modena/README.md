# Archivio di Stato di Modena sweep (2 Nov 2026)

Scope: Cancelleria ducale / Archivio Segreto Estense, Ambasciatori, cifrari. **Result: 0 candidate rows; blocked at the host test.**
`candidates.json` is an empty list. `research/COVERAGE.md` named in the brief does not exist in the checkout; the rest of the reading list was read,
plus the sibling Mantua, Milan and italian_state READMEs of the same day.

## Host test
| Host | curl | Chrome (own tab 1987533555) |
|---|---|---|
| asmo.cultura.gov.it | 000 (no answer, 10 s) | error page, tab fell back to newtab; get_page_text refused |
| archiviodistatomodena.cultura.gov.it, www.archiviodistatomodena.beniculturali.it | 000 | not tried |
| asmo.beniculturali.it (fileadmin PDFs) | 000 | not tried |
| web.archive.org copy of asmo.cultura.gov.it | 200 | stub only (HTTP 307 redirect to /home, nothing behind it) |
| web.archive.org copy of fileadmin/.../Estratto_guida_generale_modena.pdf | 200, 96 pp. | not needed |

Network-level block, same as the October outage and the Mantua/Milan runs. No bot check, no CAPTCHA, no login.

## What was read
- Guida generale extract (Wayback, 96 pp.): grep "cifr" gives only "Cifrario per il carteggio diplomatico" in Cancelleria and no item-level cipher notes. The Ambasciatori series is described at fonds level only.
- ASMo "L'Archivio si svela" article on Este ciphers (filodiritto.com, 21 Feb 2024): names Casa e Stato b. 141 n. 12.79 (Lucrezia Borgia to Alfonso I, Ferrara 8 Oct 1510, graphic substitution, "de Mantua" cipher), b. 141 n. 46 (the 1512 Lucrezia-Alfonso dissimulating cifrario), Cancelleria Cifrario b. 2 fasc. 1 (Ippolito I 1495; Alfonso I), and Cremonini 2019 (Cito cito volans, pp. 99-192) as the literature.
- 2 web searches (standard): ASMo cipher holdings (8 buste of 15th-18th c. cipher systems); the 1510 letter.

## Rows (1 returned, closed)
1. Lucrezia Borgia 1510 (ASMo Casa e Stato b. 141 n. 12.79): already decrypted by D. Palma (IA item giornalino-lettera-cifrata-lucrezia-borgia_202501, per research/ia_meta) and inside Cremonini 2019. Closed. Scan not opened (only the article text).
The cifrari (b. 141 n. 46; Cancelleria Cifrario b. 2) are keys, not ciphertext; not rows.

## Already held in the repo (not re-listed)
Catalogue and targets already hold the Ambasciatori Ungheria letters (b. 2/20, 2/21, 4/12, 4/26: Cistarelli, Bonzagni, Caprile) and DECODE ASMo records; Autografoteca Campori (Biblioteca Estense, not the archive) leads exist in leads.json.

## Not reached
Item-level Ambasciatori (Roma, Francia, Spagna, Venezia, Milano...), Carteggio principi esteri, Archivio per materie, Cifrario b. 1-8 contents, Segreteria di Stato: all need the ASMo inventory/portal. Retry from another network, or Wayback copies of the ASMo "strumenti_di_corredo" inventory PDFs (the Milan run showed this route works for fileadmin PDFs; only the Guida generale extract was tried here). Cremonini 2019 would give the item list for the cipher material.
