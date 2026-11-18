# Chrome wave 12 (15 Nov 2026): Bergenroth date check of the RAH leads; regional portal probes

**Result: 0 new leads. Catalogue entries 2873 and 2869 closed (moved back to `research/leads.json`, verdict `read`); 2867 narrowed 14 to 9 letters, 2868 narrowed 45 to 29.**

## 1. Task 4: Calendar of State Papers Spain matched by sender and date, not folio
Wave 11 matched the Badator index letters to Bergenroth's entries by volume and folio. That misses entries where the CSP prints the folio with an en dash
('114-6'), a typo ('M. Re Ac.'), or a folio that differs from the index. Wave 12 re-read the full BHO pages (vol. 2: nodes 79737-79773, 1522-24; vol. 3: nodes
74485-74700, 1525-29; `fetch_csp.py`, `fetch_csp3.py`, 1.5 s pacing; the page texts are not kept, rerun the scripts) and matched each remaining index letter by
sender and dateline date.
- Vol. 2 (1522-24, `crossdate.py`, `crossdate2.py`, `entries.py`): leads 2870 (Lannoy), 2871 (Colonna), 2872 (Adorno), 2876 (Marin) have no printed letter of the same sender and date: unchanged. Lead 2873 (Adrian VI): both remaining letters are printed (Rome 30 Sep 1522, CSP no. 478, A.26 f.53, index f.58; Rome 2 Mar 1523, no. 532, A.27 f.174, index f.172, 'Autograph in cipher ... Deciphered by the Secretary Quintana', so a decipherment is filed). `demote_2873.py` moved the entry back to leads, verdict `read`.
- Vol. 3 (1525-29, `crossdate3.py`, `apply_vol3.py`, `vol3_result.json`): a letter is dropped when the CSP prints one of the same sender and date within 10 folios of the index folio. 2867 Perez: 5 dropped (9 kept; 1526-07-31 A-38 f.136+137 is kept because the CSP's same-day letter is at f.81, possibly a second letter). 2868 Caracciolo: 16 dropped (29 kept; 1528-09-18 A-43 f.173 vs CSP f.124 kept). 2869 Herrera: all 3 dropped, entry moved back to leads as `read`.
- Limits: the folio-distance rule is a judgement; a distant-folio same-day match was kept, a near one dropped as the letter or its copy. Volumes not seen. The index/CSP folio offsets (up to 5) are not explained.

## 2. Probes that gave nothing (tried in Chrome, 15 Nov 2026)
- **Archivi Nazionali portal** (`archivinazionali.cultura.gov.it/it/risultati-di-ricerca?search=...`; SAN redirects there): the `search` parameter is ignored on first load (the page shows the whole-portal totals, 1,255,919 results) and results are drawn by script; already swept by `sweep_2026-11_italian_state_retry`. Not repeated.
- **Belgium, AGATHA** (`agatha.arch.be`, the new State Archives search; `search.arch.be` shows an end-of-life notice): the 'Archive inventories' form (`/en/search/ead/results/`, POST `FREE`) returns inventory-level hits only (101 for 'chiffre', mostly 'chiffre d'affaires' and census/colonial inventories), no item hits; the pages carry reCAPTCHA. `research/belgium_lux` already holds the EAD full-text grep. Not pursued.
- **Lombardia Beni Culturali** (`/archivi/ricerca/`, fields denominazione, anni, testo): fonds-level descriptions only; the free-text form needs the hidden `where` value (`comparch`); the fetch returned only the page shell. Not pursued.
- **Valencia, ARV**: the catalogue is SAVEX (`savex.gva.es/flora/jsp/index_opac_archivo_es.jsp`, linked from `arv.gva.es/es/cataleg-savex`). In Chrome the host loads an error page ('Frame ... is showing an error page') and the tab stays wedged until closed. Blocked; try from another network.
- **Swiss `archives-quickaccess.ch`**: a login service for archive staff, not a search.
- Web searches for unread cipher letters in Italian and Spanish archives returned only studies of already-deciphered series (Milan Buglio, Venice dispacci, Soro 1539), nothing new.
