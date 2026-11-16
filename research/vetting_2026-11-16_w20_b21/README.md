# Vetting wave 20, batch 21 (16 Nov 2026)

Claude Code session (Claude Opus 5.5). Leads 2760 1218 1162 2303 1613 2764 2173 2175 2172 2887 2714 2545 2544 1617 2691 2689 2690 2687.
These are proposals only (`proposals.json`, merged part by part from `parts/` with `add.py`). Nothing was applied to `research/leads.json` or `catalogue.json`.
Every vetting block passes `vetting_problems` except for the rule that a closed verdict cannot enter the catalogue.
The Tomokiyo and Lasry lists are the copies fetched 15 Nov 2026, searched with `prior.py`.

## Results

| lead | verdict | conf. | deciding fact |
|---|---|---|---|
| 2691 | read | high | Hungaricana 3799, 3803: Leonhard von Fels to Ferdinand I, Oct/Nov 1540, 'részben sifrírozva, sorközi feloldással' (FHKA Hoffinanz Ungarn RN 1, Konv. 1540, fol. 21-24, 33-38) |
| 2689 | partly_read | medium | 6 of 8 cipher pieces deciphered on the sheet or a separate leaf; 141595 = catalogue 1234; 141560 is Logschan's key; only Harrach's postscript (141355) has no decipherment recorded, and the archivist summarises its content |
| 2690 | read | medium | 42325: Angelo Carafa to Rizzi, Naples 18 Sep 1530, 'titkosírással és feloldás mellette'; 42326: cipher with 'fol. 70-71 ehhez készült feloldás?' |
| 2687 | read | high | all 12 Szeben regests (Gerendi and others, 1530-31) are deciphered on the sheet; six printed in Schuller 1898 |
| 2714 | not_cipher | high | Vogelsangh sheet is a 24-letter substitution key with no ciphertext (scan read, alphabet transcribed in the proposal) |
| 1162 | partly_read | medium | all 221 SLUB images paged: the cipher is single words in headings, glossed in clear in places ('Marbach' over 'Ā15b1z'); the wage marks have the author's key on the flyleaf |
| 1613 | partly_read | medium | SOAS catalogue (new route): telegrams catalogued with gist; 56/405 'code, translation & cost'; 22/27 decyphered; 56/284 'no translation' has its draft noted on the next page (56/285) |
| 2760, 1218, 2303, 2764, 2173, 2175, 2172, 2887, 2545, 2544, 1617 | none | | blockers in `proposals.json` notes |

## Record errors found

- 2691: the sender is Leonhard von Fels. The folios are 21-24 and 33-38. The first letter is dated 21 Oct 1540 in the regest text; the unit date is 1540.11.21.
- 2689: the Krakow envoy is Georg von Logschan (Lokschau), not "probably Laski". The Olomouc writer is Leonhard von Harrach.
- 2690: the sender is Angelo Carafa, writing to Jo. Fr. Rizzi.
- 2687: the senders are Bishop-elect Miklós Gerendi, the city of Szeben and Gáspár Horváth of Vingárt.
- 1617: the letter is dated 19 Jan 1534 (DDB record), not 1490.
- 2887: the shelfmark is Wetzstein II 203. This repeats an earlier correction.

## Routes and blockers today

- **SOAS archive catalogue** answers scripts at `https://archives.soas.ac.uk/records/PP_MS_1/EPRE/1/56/284`: use underscores for spaces and keep the slashes (`soas.py`). The old CalmView links redirect there.
- **SLUB IIIF** answers curl. Manifest: `iiif.slub-dresden.de/iiif/2/<id>/manifest.json`. `slub_sheets.py` builds contact sheets.
- **Hungaricana** regests answer by script (`regest.py`, from b12). **DDB Solr** returns full records (Tucher letter).
- **Blocked:**
  - archiviodistatofirenze.cultura.gov.it resets every connection (2760: MAP filza CV and inventory unreachable).
  - qalamos.net and orient-digital reset; content.staatsbibliothek-berlin.de answers 429.
  - klio.sh.ch (Schaffhausen) shows a proof-of-work page.
  - FranceArchives shows a JS wall.
  - Archives Hub returns 403.
- Images are in `img/` (git-ignored): the Amsterdam key scan, the SLUB pages and contact sheets.
