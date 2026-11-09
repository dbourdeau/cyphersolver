# Literature lists sweep (9 Nov 2026): published lists of undeciphered archival ciphers

Result: **0 candidate rows.** Every named, archive-held, still-unread item found in the published lists was already in the
repo (catalogue, leads, targets or a sweep note). `candidates.json` is `[]`. One item could not be given a citable shelfmark
(Hutten 1535, below).

## Routes that worked
- **HistoCrypt 2018-2023** (ecp.ep.liu.se, free PDFs; whole-volume PDFs for 2018/2019/2020/2021 via `issue/download/<id>/<galley>`,
  per-article PDFs for 2022/2023 via the `citation_pdf_url` meta tag). 33 papers and the four volumes text-extracted with PyMuPDF
  and grepped for undeciphered/unsolved/not deciphered/remains. Archive items that came up: Rabenhaupt 1646 (solved in the 2021
  paper), Slovak aristocratic archives 2023 (covered by `sweep_2026-11_czech_slovak`), Slovak attache telegrams 1939-45 in the
  national archive ("unsolved challenge", 20th-c. telegrams, no shelfmark given), Polish-Soviet War intercepts in CAW (2021
  paper, collection level, "mostly undeciphered", covered by Polish sweeps), Sacco's 1916 notebook (private family papers).
  Nothing new.
- **Tomokiyo "Unsolved Historical Ciphers"** (local copy `unsolved.htm`, last modified 15 Sep 2026): all ~100 entries read; 130+
  shelfmarks/names checked with `chk.py` (batch wrapper over `known.py`). Every unsolved entry is already in the repo (Clair. 327
  / Ranzo / Gilino, Throckmorton / Wod / Moray, SP 53, Espagnol 318, Segur, Cocquet, Ottobon, Bordeaux/Condé Add MS 4200,
  Colbert, Rupert, Hyde, Thurloe, Chaulnes, Catinat, Stepney, Marmont, Berthier, D'Estaing, Armstrong, Barney/Mallory ...).
- **Tomokiyo blog 2022-2026** (cryptiana.blogspot.com year archives, 180 post titles scanned): the "undeciphered" posts (Louis XIII
  1635, Blencowe/Geertruidenberg, Richelieu/Mazarin, Armstrong, Mirabeau, Moncada 1524) are all known or solved here.
- **Klausis Krypto Kolumne** unsolved-cryptograms category (scienceblogs.de, 450 titles, 2017-2022, pages 1-42): the pre-1900
  archival items (Charles I Isle of Wight, Catherine/Marie de Medici, Maximilian I 1494-95 letters in the Archives
  departementales du Nord, Louis XIV to Chaulnes 1693, Vatican 1628, Utah War 1858, Bunch, Leona Vicario, Spinelli/Beinecke,
  Nuchterlein's Vienna pages) are known here or solved in the comments (Vienna RKA K1 pages 481-493 were read by Thomas/Narga in the post comments, 22 Oct 2018).
- WebSearch for Cipher Mysteries / Cryptologia lists returned nothing item-level (no usable list pages).

## Blocked
- `dspace.ut.ee` (HistoCrypt 2024 and 2025 proceedings, Tartu): TLS reset from this network (curl and WebFetch). `dblp.org`:
  Anubis check. `journals.wlb-stuttgart.de`: Anubis. Not clicked through. So HistoCrypt 2024 and 2025 were read only through
  search-result abstracts: Wackerbarth/Flemming 1700-1720 (known), Heusner 1637 (known/solved), Brougham 1724 (solved in paper),
  Suriname ciphertext (in catalogue), Bellecombe 1782-85 (see below).

## Not usable (checked, left out)
- **Bellecombe, governor, to the Secretary of State for the Navy, 1782-85** (HistoCrypt 2025, Pierrot et al.): ANOM Aix; three
  ciphered letters, one 96% recovered by the authors; the other two not stated as unread, no shelfmarks, not online. No row.
- **Philipp von Hutten to Matthias Zimmermann, Coro, 1535**: last three lines in cipher, "never deciphered" per Schmeh
  (blog 23 Oct 2018, `scienceblogs.de/klausis-krypto-kolumne/2018/10/23/an-unsolved-cryptogram-by-a-german-conquistador/`) citing a
  scan in Schmitt and Hutten, *Das Gold der Neuen Welt* (Hildburghausen 1996). Not in the repo (known.py: 0 hits for Welser/Zimmermann
  letter). Could not find the archive or shelfmark of the original (three searches); the printed edition is the only
  source. Worth a follow-up: look in Schmitt's edition for the Hutten family archive signature, then add as a class C row.
- **Louis XIII to ?, 6 April 1635 (1633 per T. Ernst's transcription), "Mon Cousin, bac racle ..."**: nonsense-word jargon code;
  held by the autograph dealer David Chelli, not an archive; not in the repo; no shelfmark. Not a row.
- Dealer/private/Reddit items (Lehmann 1860, Kosewitz/Sommerda, stamp-album letter, postcards, Bickley lexicon, Sacco notebook):
  no archive record.

## Remaining
Pre-2018 HistoCrypt abstracts are covered; 2024/2025 volumes need a network where `dspace.ut.ee` answers (title lists were
only seen through search). Schmeh's category pages before 2017 and his non-"unsolved" tags were not walked.
Files: `chk.py` (batch duplicate check over `known.py`'s corpus).
