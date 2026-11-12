# Backfill sweep, 13 Nov 2026 (b169)

Cloud pass to replace solved items with vetted new leads. Plain curl only, no logins, no browser. Images were viewed in
scratch and deleted; none are in the repo. Row schema as in `research/archive_sweep_2026-10/BRIEF.md`; each row carries a
`vetting` block (fields of `docs/_check_catalogue.py`, plus `searches`), verdict `open`.

## Result

12 rows in `candidates.json`, all with an `open` vetting block. No `id` (assigned at merge).

| Archive | Rows | cls A | cls B | cls C |
|---|---|---|---|---|
| ASF Mediceo avanti il Principato (filze XLIII, XLIX, LI, LII, LIII) | 10 | 2 | 2 | 6 |
| ASF Mediceo del Principato 385 | 1 | 0 | 1 | 0 |
| Rigsarkivet, Pentz Glückstadt relations (unit 274999) | 1 | 0 | 1 | 0 |
| Total | 12 | 2 | 4 | 6 |

Sources: the MAP filze above were paged by an outside sweep (11 Nov 2026) that the repo's ASF passes did not cover
(`sweep_2026-11_asf_map_paging` did LXXII-LXXV, XLVIII, CXXXVII). Every row was re-opened on 13 Nov 2026.

## Routes

- ASF MAP IIIF `/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif`: 200.
  `/map/ricerca/ricerca-su-filza/?f=F&d=D&c=` answers 302 to the doc's viewer id.
- ASF PAD IIIF `mdp_carteggio_universale/<filza>/<seq>_C_<carta>_<R|V>.ptif`: 200.
- Rigsarkivet: `api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=<unit>` and `/ao/v1/images/<id>`: 200.
  Search API (`soeg.rigsarkivet.dk/api/v1/Search/arkivalier`, JSON POST): terms chiffer (33 hits), chifre (7),
  chiffre (6), dechiffreret (0), chiffreret (0). All cipher-titled units with images are already in the repo (e.g. 464 Lagau, 465 Biermann) or are key-only.
- DECODE live search `de-crypt.org/decrypt-web/RecordsList?search=`: 200 (results per row).
- Tomokiyo `cryptiana.web.fc2.com/code/italian.htm`: 200.
- dspace.ut.ee (Vito 2025 PDF): connection reset; not retried.

## Excluded after checking (not in candidates)

- MdP 402 A cc. 688-689 (bishop of Forlì, Augsburg, 10 May 1551): c. 688 is the chancery decipherment of c. 689. Read.
- MdP 402 A cc. 676-678 (Fabrizio Ferrari, 1551): a contemporary decipherment is filed beside it. c. 678 also has clear lines between the cipher lines.
- MAP XLIII doc. 4 (Capponi, 5 Jul 1486): partly glossed between the lines.
- MAP XCVI doc. 90 (2-line slip): the clear line under it may be its decipherment.
- MAP XLIX doc. 151 (Soderini slip, 1490): key sheet LXXII 183 is confirmed on the glossed parent letter, so the slip reads.
- MAP L (1,376 images paged at 1272 px, detector top 40 viewed): cipher pages 153-155 and 265-266 are glossed between the lines. No bare page in the top 40.
- Rigsarkivet: Biermann's drafts to Lilienkron 1675-76 (units 260195-7, Delta code): same correspondence as the open Lilienkron letters in catalogue 465, so not a new lead.
  TKUA Nederlandene B.41 images 308-313: marginal glosses. Arnfeldt 1630: archivists' keys on image 347.
  Jens Juel 1673 unit 261588: duplicate of lead 2531.

## Not done

- MAP filza LVI paging was stopped (disk). XXXIX, XL, XLIV, LVI-LIX were not paged.
- The notes of Lettere di Lorenzo VII-IX are not online and were not opened. Each MAP row's `edition` field says so.
  The Lettere print Lorenzo's own letters and cite incoming ones only in notes.
- Pentz unit 274999: images 137-503 (1639-45) not viewed.
