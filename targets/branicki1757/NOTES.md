# branicki1757: Branicki to Potocki (AGAD 446) and three letters of 1756-57 (AGAD 1398-1400), one reciprocal alphabet

Status: read (7 Nov 2026, refreshed from the contributor's repository at commit f465095). Contributed by Prabal Gupta (issues #316 and #317; repository `prabal-rje/branicki-1757`, CC BY 4.0): a reciprocal substitution of 12 pairs plus a nomenclator of three-digit numbers, found from the ciphertext of 446 and applied unchanged to 1398, 1399 and 1400. Checked here against its own files and the key only (`VERIFICATION.md`); the AGAD scans are not reachable from the project, so no transcription was compared with a scan here. The contributor checked the transcriptions against the scans (with AI models) and corrected them on 7 Nov 2026.

## Documents (all AGAD, Zbiór Anny z Potockich Ksawerowej Branickiej, zesp. 338, 1/338/0/1/...)

| Letter | Catalogue | Date | What it is | Reading (cipher words, holes, share read) |
|---|---|---|---|---|
| 446 | 1578 | Białystok, 22 March 1757 (the catalogue says May) | Jan Klemens Branicki to Antoni Potocki, palatine of Bełz: a manifesto against the abuse of an envoy's mission | `reading_446.md`, `translation_446.md`; 369 words, 7 holes, 0.981 |
| 1398 | 1579 | Jaswojnie, 24 July 1757 | Marcin Matuszewicz (signed Matusewic), a field report on Apraxin's army at the Prussian frontier | `reading_1398.md`; 584 words, 16 holes, 0.973; all four pages |
| 1399 | 1579 | 1756, before August | an insider's report on Hetman Radziwiłł's party, a fund of 146,000 francs for the 1757 dietines | `reading_1399.md`; 725 cipher words, 6 holes, 0.992 |
| 1400 | 1579 | Nieśwież, 11 September 1756 | signed Boeven: the bloody dietine of Brest, a rival party spending 200,000 francs | `reading_1400.md`; 472 words, 2 holes, 0.996 |

Over the four letters 2,119 of 2,150 cipher words read (98.6%), counted from the reading files (unread code groups, `[?...]` stretches and `[?word]` doubtful readings are holes). The contributor counts 590 of 613 (1398), 744 of 750 (1399) and 490 of 493 (1400).

The readings, translations, transcriptions and decryptions are the contributor's (`transcription_*.txt`, `decryption_*.txt`, `reading_*.md`, `translation_*.md`), copied from his repository at commit f465095, except that the paths in the headers point at this folder. `numbers.md` is his number code (it also lists the groups of letter 1401, which has its own cipher and its own target), `outside_checks.md` his outside checks (the 146,000 francs add up; the names appear in Konopczyński 1909 and Matuszewicz's memoirs), `clear_446.txt` the clear parts of 446, `pass_1398/` the three blind passes of pages 2 to 4 of 1398 and their comparison with the reread.

## The cipher

Each cipher letter stands for one plain letter, in pairs that swap (a-h, b-q, c-r, d-s, e-l, f-t, g-z, i-m, k-x, n-o, p-u, w-y); i/j and u/v are not distinguished. Three-digit numbers (about 215 to 900) are a nomenclator of titles, names and places in alphabetical order, with number words at 805 to 824 (1 to 9, tens, cent, mille); 830 to 850 fall at clause ends and act as punctuation, and numbers from 851 up look like nulls. 1400 dates itself in cipher (824 811 823 818 810 = "mil sept cent cinquante six").

## What the identifications rest on

The contributor identifies the writer of 1398 as Marcin Matuszewicz (his memoirs have him at Jaswojnie with Siruć on 26 July 1757), the stolnik of 446 as Stanisław Poniatowski, and Boeven as Radziwiłł's secretary, from Konopczyński (1909) and the memoirs (ed. Pawiński, 1876), read mostly in OCR. The memoirs and the letter agree on the Iwie congress of 1756, the lords and four of the five shares, and disagree on the hetman's share (100,000 against 53,000) and the total (200,000 złoty against 146,000 francs); no historian has checked these. The project did not open either book.

## Remaining gaps

- Number codes still open or guessed (195, 296, 367, 385, 386, 480, 496, 580, 775, 795, 841; names and titles read as `[?word]` such as 720 Stolnik, 350 France, 270 and 273 Czesnik) - blocker: open-codes; each occurs once or twice and no clear text fixes it; the contributor tried the other letters of the fonds, Konopczyński and the memoirs on every one (`numbers.md`)
- A human check of the transcriptions against the AGAD scans, including the fifth letter of the signature of 1398 (y or p) - blocker: needs-physical-access; the scans are on szukajwarchiwach.gov.pl, which the project's environment cannot reach, and the images may not be redistributed

Catalogue 1579 also listed no. 1401 (a letter partly in Polish, perhaps to Branicka). It is a different cipher (one number per letter) and has its own target (`exiles1736`).

## Escalation

- [x] siblings: the key of 446 applied unchanged to 1398, 1399 and 1400, the three other cipher letters catalogued with it; letter 1401 has a different cipher; letter 131 of the fonds searched by the contributor for the open codes
- [x] clear-pages: the clear parts of 446 (clear_446.txt) and the clear passages of 1399 read and compared with the cipher around them (Palatin de Trok, Princesse douairière); neither is a decipherment of the cipher
- [x] known-keys: no earlier key for the fonds is known; the contributor's count-matching solver and the project's lexicon test both give this key (VERIFICATION.md)
- [x] print: the contributor searched Konopczyński (1909) and Matuszewicz's memoirs (1876) for the names and events; no printed copy of these letters was found; the project did not search further
- [x] key-rebuild: the key was found by the contributor's solver on French next-letter counts, then the number code was built from clear text, repeated context and the alphabetical order (numbers.md)
- [x] retry: every open group was retried by the contributor against the other letters and both books, and 1398 pages 2 to 4 were reread and compared with three blind passes on the enlarged scan (outside_checks.md, Corrections); the project did not retry them
