# Arabic cipher sweep (15 Nov 2026)

Run by a Claude Code session for Daniel Bourdeau, in four parallel passes. Scope: enciphered texts in the Arabic language
or script (Judaeo-Arabic included), any date to 1950, unread, seen on an image where one is online. Continues
`research/sweep_2026-11_arabic/` (6 Nov 2026, pre-1500 only) and `research/sweep_2026-11_hebrew/` (Geniza).

**State: not merged.** `candidates.json` holds 17 rows. `merge.py` (dry run, 15 Nov 2026) reports 17 new; nothing is in
`research/leads.json` or `catalogue.json`. The merge and any promotion wait for the owner's go-ahead.

No Chrome extension was available in this session (cloud container), so every host that showed a bot check is recorded
as blocked in the part notes and is still open for a Chrome pass.

## The four passes

| Notes | Area | Rows | With vetting block |
|---|---|---|---|
| [`part_A.md`](part_A.md) | North America (OPenn, Princeton, Digital Scriptorium) and the Cairo Geniza | 4 | 2 |
| [`part_B.md`](part_B.md) | German, Dutch and Nordic catalogues; Arabic papyri | 4 | 1 |
| [`part_C.md`](part_C.md) | France, Italy, UK (Spain not reached) | 6 | 3 |
| [`part_D.md`](part_D.md) | Literature-led pass; Middle East, Africa, Asia collections | 3 | 0 |

Each part file lists its routes, search terms with counts, pages viewed, closed items with citations, key leads, side
leads (Persian, Ottoman) and what is left.

## Rows with a complete vetting block (verdict open)

All six pass `vetting_problems()` in `docs/_check_catalogue.py`. The coordinating session re-opened each image on
15 Nov 2026 and confirmed that bare ciphertext is on it as described.

| Row | Item | Date | What is there | Caveat |
|---|---|---|---|---|
| 0 | Penn LJS 51, f. 106v | text c. 1330-1370, copy 15th c. | 7 lines of invented signs, about 120-130, word dividers; the compiler says he solved it and the manuscript breaks off | About 200 solved sibling passages in the same volume (plaintext follows each); ff. 10r-106r were checked for structure at about 480 px a page, not collated |
| 1 | JTS ENA 4100.7b | undated Geniza | 6 lines of a secret language in Hebrew letters, nearly every word beginning with alef, in a Judaeo-Arabic letter | Short; date not assessed |
| 4 | Berlin Ms. or. oct. 3629, f. 1a | copy dated 615 AH / 1217 | 2 lines, about 43 separate signs, on the title page | Seen only in Sellheim's printed plate (figure about 1,200 px wide); Sellheim queries the date for the cipher lines; his fig. 92 and Wüstenfeld 1879 are possible keys, untested |
| 8 | BnF Arabe 1966, last page | colophon 732 AH / 1332 | 1 line: a few Arabic letters, then about 28 Arabic-Indic numerals | Very short; line in paler ink than the colophon, may be later |
| 9 | BnF Arabe 2562, ff. 54r-55v | 16th c. | 4 pages of recipes, about half the text in numerals with a few letters and signs | Microfilm scan, 1,435-1,503 px wide |
| 10 | Wellcome MS Arabic 449, f. 1a | 17th-18th c. | 12-line numeral cryptogram with letter dots, about 150 signs | Serikoff's 2005 catalogue not opened |

## Rows without a vetting block (leads queue)

| Row | Item | Date | Why no block |
|---|---|---|---|
| 2 | CUL T-S K24.24 | undated Geniza | 11 lines of an unidentified script seen; editions of Geniza magical texts not opened, a known cursive not ruled out |
| 3 | CUL T-S 13J18.19 | 1139 | three words in Coptic numerals; partial, disputed readings in print (Gil-Fleischer 2001), not opened |
| 5 | Berlin Wetzstein I 203 | 1705 | catalogue only; key on f. 103a per Ahlwardt |
| 6 | Berlin Ms. or. oct. 1474, f. 1a | 16th c.? | one line, "Geheimschrift (?)", may be numerals |
| 7 | Penn Museum E16470 | undated papyrus | "Cipher (?)"; image too small, not established as Arabic or as cipher |
| 11 | Bodleian Laud Or. 139, f. 101a | MS before c. 1300 | catalogue only ("undeciphered writing"); leaf not digitised |
| 12 | Vat. ar. 34, f. 288v | 16th c. | catalogue only; not digitised |
| 13 | Cambridge, Browne F. 43 and F. 16 | c. 1885-96 | catalogue only |
| 14-16 | Institute of Ismaili Studies MS 1662, 1291, 1313 | 19th c. to 1929 | catalogue only; printed catalogues not opened |

## Corrections to earlier sweeps

- T-S NS J479 is read: Elbaum's 2022 Genizah blog post publishes his sign-to-Hebrew mapping (the 6 Nov Hebrew sweep
  listed it as unread).
- Penn LJS 51: the 6 Nov sweep left open whether every cipher letter has its transcription. All 212 pages were paged:
  only f. 106v is bare.
- P.Vindob. A. P. 5584 (a "Geheimschrift" sibling of lead 2832) is dinar-fraction numerals, not cipher (Bogensperger and
  Reinfandt, Tyche 34, 2019). The same article cites A. P. 11016 as described only.

## What is left

- Spain entirely (PARES 429, BNE 403); the Moroccan Makhzen cipher letters named in the literature.
- Qalamos / orient-digital (connection reset), so no Berlin leaf was opened; ONB image hosts likewise.
- vHMML, LoC, HathiTrust, Michigan, Harvard, Yale, Columbia, Princeton catalogue; QDL, EAP, CUDL search, Chester Beatty,
  Fihrist live site, NLI, Juma al-Majid, the Turkish YEK portal, Majlis: bot check or no connection from this network.
- Durham HIL/64 and HIL/65 ("Arabic and code" telegrams, about 2,100 digitised frames) not paged.
- Image orders: Bodleian Laud Or. 139 f. 101a; Vat. ar. 34 f. 288v; Berlin Ms. or. oct. 3629 f. 1a and f. 72b.
