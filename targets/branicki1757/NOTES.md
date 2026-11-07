# branicki1757: Branicki to Potocki (AGAD 446) and three letters of 1756-57 (AGAD 1398-1400), one reciprocal alphabet

Status: read in part (7 Nov 2026). Contributed by Prabal Gupta (issues #316 and #317; repository `prabal-rje/branicki-1757`, CC BY 4.0): a reciprocal substitution of 12 pairs plus a number code, found from the ciphertext of 446 and applied unchanged to 1398, 1399 and 1400. Checked here against its own files only (`VERIFICATION.md`); the AGAD scans are not reachable from the project, so no transcription was compared with a scan.

## Documents (all AGAD, Zbiór Anny z Potockich Ksawerowej Branickiej, zesp. 338, 1/338/0/1/...)

| Letter | Catalogue | Date | What it is | Reading |
|---|---|---|---|---|
| 446 | 1578 | Białystok, 22 March 1757 (the catalogue says May) | Jan Klemens Branicki to Antoni Potocki, palatine of Bełz: a manifesto against the abuse of an envoy's mission | `reading_446.md`, `translation_446.md`; 369 cipher words, 12 holes (0.967) |
| 1398 | 1579 | 24 July, probably 1757 | Matusewic, a field report on Apraxin's army at the Prussian frontier | `reading_1398.md`; 552 words, 25 holes (0.955); page 2 is rough |
| 1399 | 1579 | probably June or July 1756 | an insider's report on Hetman Radziwiłł's party, a fund of 146,000 francs for the 1757 dietines | `reading_1399.md`; 722 cipher words, 12 holes (0.983) |
| 1400 | 1579 | Nieśwież, 11 September 1756 | signed Boeven: the bloody dietine of Brest, a rival party spending 200,000 francs | `reading_1400.md`; 472 words, 3 holes (0.994) |

Catalogue 1579 also lists no. 1401 (a letter partly in Polish, perhaps to Branicka); it is not covered by this target and stays in the catalogue.

The readings, translations, transcriptions and decryptions are the contributor's (`transcription_*.txt`, `decryption_*.txt`, `reading_*.md`, `translation_*.md`), copied unchanged except that the paths in the headers point at this folder. `numbers.md` is his number code, `outside_checks.md` his outside checks (the 146,000 francs add up; the names appear in Konopczyński 1909), `clear_446.txt` the clear parts of 446, `pass_1398/` the two raw transcription passes of 1398 that his consensus file joins.

## The cipher

Each cipher letter stands for one plain letter, in pairs that swap (a-h, b-q, c-r, d-s, e-l, f-t, g-z, i-m, k-x, n-o, p-u, w-y); i/j and u/v are not distinguished. Three-digit numbers (about 215 to 900) are a nomenclator of titles, names and places in alphabetical order, with number words at 805 to 824 (1 to 9, tens, cent, mille); 830 to 850 fall at clause ends and act as punctuation, and numbers from 851 up look like nulls. 1400 dates itself in cipher (824 811 823 818 810 = "mil sept cent cinquante six").

## What the identifications rest on

The identification of the stolnik of 446 as Stanisław Poniatowski and of Boeven as Radziwiłł's secretary are the contributor's readings from one printed book (Konopczyński 1909) that the project did not open; no historian has checked them.

## Remaining gaps

- Page 2 of 1398: the transcription is rough and the reading repairs garbled stretches by sense - blocker: illegible; the two transcription passes differ, and the scans are not reachable from the project
- Number codes still open or guessed (195, 296, 367, 385, 386, 480, 496, 580, 775, 795, 841; names and titles such as 720 Stolnik, 350 France, 270 and 273 Czesnik read as `[?word]`) - blocker: open-codes; each occurs once or twice and no clear text fixes it
- The transcriptions against the AGAD scans by a human - blocker: needs-physical-access; the scans are on szukajwarchiwach.gov.pl, which the project's environment cannot reach, and the images may not be redistributed

## Escalation

- [x] siblings: the key of 446 applied unchanged to 1398, 1399 and 1400, the three other cipher letters catalogued with it; 1401 not tried
- [x] clear-pages: the clear parts of 446 (clear_446.txt) and the clear passages of 1399 read and compared with the cipher around them (Palatin de Trok, Princesse douairière); neither is a decipherment of the cipher
- [x] known-keys: no earlier key for the fonds is known; the contributor's count-matching solver and the project's lexicon test both give this key (VERIFICATION.md)
- [x] print: the contributor searched Konopczyński (1909) for the names; no printed copy of these letters was found; the project did not search further
- [x] key-rebuild: the key was found by the contributor's solver on French next-letter counts, then the number code was built from clear text, repeated context and the alphabetical order (numbers.md)
- [x] retry: the doubtful groups were retried by the contributor against the scans on 7 Nov 2026 (outside_checks.md, Corrections); the project did not retry them
