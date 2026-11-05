# Archivio di Stato di Mantova, Archivio Gonzaga sweep (2 Nov 2026)

**Result: 0 rows. Blocked at the host test; nothing swept.** `candidates.json` is an empty list.

## Host test (2 Nov 2026, own Chrome tab)
| Host | curl (10 s) | Chrome |
|---|---|---|
| archiviodistatomantova.cultura.gov.it | no answer (000) | Chrome error page, no content |
| www.archiviodistatomantova.beniculturali.it | no answer | Chrome error page |
| inventari-san.cultura.gov.it/inventari/965/pdf (SAN inventories, incl. Gonzaga Torelli/Luzio) | no answer | Chrome error page |
| archivi.cultura.gov.it (Guida Generale, Mantova_.pdf) | no answer | not tried |
| asmo.cultura.gov.it | no answer | not tried |

Same network-level block as `research/sweep_2026-11_italian_state/README.md`; no CAPTCHA or bot page was seen, no login used.
Archives Portal Europe loaded in the tab but was not searched (no Italian state-archive holdings of Gonzaga items expected there; not checked).
One web search (Gonzaga cifra/cifrari/copialettere) returned no busta with cipher letters. Its leads, none opened or verified:
Torelli, L'Archivio Gonzaga di Mantova (1920) is the finding aid; Ercole Gonzaga copialettere 1-6 in b. 1945 (1550-61); a
"Quaternetus ziffrarum" cited in a Urbino paper; accademianazionalevirgiliana.org quaderni 8 and 11 (answer 200 to curl, not read).

## Not reached
Everything: Carteggio inviati, Copialettere, cifrari, the SAN Gonzaga inventory PDFs. Retry from another network, or OCR the
SAN inventory PDFs / Torelli 1920 for "cifr". Already known here: DECODE R1853/R1854 (Mantova enciphered letters, Cattanei 1430)
and the Mantua b. 423 key lead in `research/italian_catalogues/`.
