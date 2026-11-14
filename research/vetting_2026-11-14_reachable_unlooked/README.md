# Vetting, reachable-unlooked sweep leads 2585-2598 (14 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5) for the project. The sweep `research/sweep_2026-11-14_reachable_unlooked`
was merged as leads 2585-2598 (rows 7, 9 and 10 were already leads 2498, 2501, 2499). ACTApro records were fetched from a
Chrome tab on archive.spk-berlin.de (same-origin `fetch`, 1.5 s apart). No ACTApro record carried an image, so no ciphertext
was seen: every block rests on the archive's description (`seen.kind` "not online", access "archive"). The Chrome tab was
shared with another session partway through, which cost three records.

- **2585** Rep. 64 Nr. 695 (Neuchatel, Jan-Jul 1705): `open`, narrowed to one volume (siblings kept in `folio_note`); decipherment filed in the volume.
- **2590, 2593, 2594**: `duplicate` of 2500, 2503, 2502 (same GStA files, different spelling of the shelfmark).
- **2597** Dohna Nr. 51: `not_cipher` (a note on a cipher key, no ciphertext).
- **2586, 2587**: `unvetted`, groups of Rep. 64 volumes overlapping 2495-2497 and 2494; split one volume per entry first.
- **2588** Derfflinger 1674: `unvetted`, printed in Urkunden und Actenstuecke vol. 13 per the 11 Nov sweep; confirm and close read.
- **2589, 2591, 2592, 2595, 2596**: `unvetted`, record not fully read or edition to check (reasons on each lead).
- **2598** Quadra / BU Gonzalez papers: `unvetted`; Hume's CSP Spanish vol. 1 prints Quadra's letters, BHO returned 401.

Routes: ACTApro same-origin fetch works; BU ArchivesSpace opens in Chrome (403 to WebFetch); British History Online 401 to WebFetch.
