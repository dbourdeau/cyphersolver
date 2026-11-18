# Vetting, Koc/Ottoman deep-sweep leads 2646-2651 and the HPBK leads 2576, 2578, 2579 (14 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5). `research/sweep_2026-11-14_koc_ottoman_deep` (6 rows) merged as leads 2646-2651;
`make.py` builds `vetting.json`; `python research/vet.py --check` passes.

- **Reconciled by key.** On viewing, the HPBK telegrams are two systems: **A** (five-digit groups, Turkish words over the groups) and
  **B** (two-digit numerals, one Arabic letter over most). The old pooled rows were split: 2646 = system B (21 sheets), 2647 = system A
  (12 sheets), both promoted. Old leads 2576 (17 items), 2578 (36) and 2579 (37) closed as duplicates: every sheet was viewed, the
  cipher ones sit in 2646/2647, the rest are clear letters. Catalogue 2575 and 2577 (already promoted) were pooled across A and B;
  their folio_note and status carry a correction (2575: only 772 is system A; 533 and 688 are system B; 2577: 576, 578, 599, 483 are B,
  550 and 595 are A). Their id sets were not changed.
- **Route.** The cdm21054 image route 502s on some items; the record JSON (`/digital/api/collections/HPBK/items/<id>/false`) names the real
  image host, `libdigitalcollections.ku.edu.tr/iiif/2/HPBK:<page id>/full/1100,/0/default.jpg` (page id is the item id minus 2), which
  served all 18 items that never loaded. Images are working files and stay out of git.
- **2649** (Morier 1808, IOR/L/PS/9/67/18): folio 2r seen in a Chrome tab on QDL (numerals only); promoted, narrowed to /18.
- **Closed:** 2648 (HPBK 1791 is a blank wrapper, not a cipher book), 2651 (same items as 2581).
- **Left:** 2650 (Open Jerusalem unreachable), 2581 (1921, held), 2584.
