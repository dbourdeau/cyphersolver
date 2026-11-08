# Check of the contributor's key and readings (7 Nov 2026, refreshed at commit f465095)

What an AI model (Claude) checked of the submission by Prabal Gupta (issues #316 and #317, repository
`prabal-rje/branicki-1757`, CC BY 4.0). The archive scans (AGAD, Warsaw) are not reachable from the project's
environment, so **no transcription was compared with a scan by the project**. Everything below is a check of the files
against each other and against the key. No human palaeographer has repeated the check. The first version of this
check (published the same day) was made on an earlier snapshot of the repository; this one uses its commit f465095.

## 1. The key

`key.tsv` has 24 rows (22 cipher letters; x for k and y for w were added by the contributor in the refresh, the
decryptions always used them) and 12 pairs that swap: a-h, b-q, c-r, d-s, e-l, f-t, g-z, i-m, k-x, n-o, p-u, w-y. The
plaintext does not distinguish i from j or u from v, as in the contributor's decryption lines.

## 2. The decryption is mechanical

Applying `key.tsv` to `transcription_446.txt` gives `decryption_446.txt` on all 58 of its lines (number groups kept in
brackets, the writer's insertion marks kept). The reading `reading_446.md` follows the decryption: word division,
spelling, punctuation and the clear parts added, the number groups resolved from `numbers.md`.

## 3. Does the key make French? (control)

No French language model could be built here (the Gutenberg corpus returns 403). A small lexicon test was used instead:
about 140 common French words (articles, prepositions, pronouns, auxiliary verbs, titles, number words, a few
words of these letters' subjects) were matched greedily, longest first, over the decrypted letters of each document
(cipher letters only, clear text removed, code numbers removed). The same test was run on 300 shuffled keys (the plain
letters permuted over the cipher letters). The share of letters covered by lexicon words:

| Document | Letters | With the key | 300 shuffled keys: best, mean |
|---|---|---|---|
| 446 (22 March 1757) | 1,510 | 0.595 | 0.266, 0.075 |
| 1398 (24 July 1757) | 2,507 | 0.541 | 0.276, 0.074 |
| 1399 (1756) | 3,086 | 0.587 | 0.236, 0.076 |
| 1400 (11 Sept 1756) | 2,184 | 0.549 | 0.231, 0.075 |

The same key, found on 446, reads three other letters of the same fonds with no change, written a year earlier or
later. This is a statistical check of the key, not a test of the readings, and it is the same material the key was found
on for 446.

## 4. Checks inside the letters

- **The clear text in 1399.** Where the writer put a name in clear ("Mr le Palatin de Trok") the cipher has the
  title as a number ("Mr le [575] de Trok"), which is how 575 is fixed to Palatin; the same for Princesse (622) and
  the other values in `numbers.md` marked fixed.
- **The sum in 1399.** The letter gives the fund in words, "cent quarante et six mille francs". The five shares
  listed, 53,000 + 25,000 + 50,000 + 10,000 + 8,000, add up to 146,000, and the number-word code reads "[809] seigneurs",
  five. This was added up here and agrees.
- **The date of 1400.** The date line ends 824 811 823 818 810, which with the number words 805 to 824 reads "mil
  sept cent cinquante six"; the clear dateline says 11 September.
- **Holes.** Counted from the reading files with the same rule for every letter (an unread code group, a `[...]`
  stretch or a `[?word]` is a hole): 446 7 of 369 cipher words, 1398 16 of 584, 1399 6 of 725, 1400 2 of 472. Letters
  supplied in square brackets (such as "fa[r]ine") are not counted as holes by this rule.

## 5. What the contributor checked, and what was not checked

- The contributor reports checking the transcriptions against the scans and the memoirs on 7 Nov 2026 and correcting them
  (`outside_checks.md`, "Corrections"); pages 2 to 4 of 1398 were reread with the key in view, which is not a blind reading,
  and then compared with three blind passes sign by sign on the enlarged scan (`pass_1398/comparison.tsv`: 37 signs
  changed, 6 left out). The project did not repeat any of this.
- Konopczyński (1909) and Matuszewicz's memoirs (1876), read by the contributor mostly in OCR, are the source of the
  outside checks on names and events. They agree with the letters in most points; the memoirs disagree on the hetman's
  share and the total of the fund (100,000 against 53,000; 200,000 złoty against 146,000 francs). The project did not open
  either book. The identifications of Boeven as Radziwiłł's secretary, of the stolnik of 446 as Stanisław Poniatowski and
  of Matusewic as Marcin Matuszewicz are the contributor's readings.
- The number groups: only the values of `numbers.md` marked fixed rest on clear text or repeated context; the "guesses"
  are read as `[?word]`.
