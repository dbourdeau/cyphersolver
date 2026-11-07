# Check of the contributor's key and readings (7 Nov 2026)

What an AI model (Claude) checked of the submission by Prabal Gupta (issues #316 and #317, repository
`prabal-rje/branicki-1757`, CC BY 4.0). The archive scans (AGAD, Warsaw) are not reachable from the project's
environment, so **no transcription was compared with a scan**. Everything below is a check of the files against each
other and against the key. No human palaeographer has repeated the check.

## 1. The key

`key.tsv` has 22 cipher letters and 12 pairs that swap: a-h, b-q, c-r, d-s, e-l, f-t, g-z, i-m, k-x, n-o, p-u, w-y. The
plaintext has no separate j, v or y of its own except through w = y: i stands for i and j, u for u and v, as in the
contributor's decryption lines.

## 2. The decryption is mechanical

Applying `key.tsv` to `transcription_446.txt` gives `decryption_446.txt` on 54 of its 58 lines; the other four (p2.14, p2.foot, p4.09, p4.foot) differ
only by the writer's insertion marks ^ and +, which the decryption keeps and the check strips. The reading
`reading_446.md` follows the decryption: word division, spelling, punctuation and the clear parts added, the number
groups resolved from `numbers.md`.

## 3. Does the key make French? (control)

No French language model could be built here (the Gutenberg corpus returns 403). A small lexicon test was used instead:
about 140 common French words (articles, prepositions, pronouns, auxiliary verbs, titles, number words, a few
words of these letters' subjects) were matched greedily, longest first, over the decrypted letters of each document
(cipher letters only, clear text removed, code numbers removed). The same test was run on 300 shuffled keys (the 22
plain letters permuted over the 22 cipher letters). The share of letters covered by lexicon words:

| Document | Letters | With the key | 300 shuffled keys: best, mean |
|---|---|---|---|
| 446 (22 March 1757) | 1,510 | 0.595 | 0.267, 0.095 |
| 1398 (24 July 1757?) | 2,442 | 0.533 | 0.268, 0.087 |
| 1399 (1756) | 3,062 | 0.593 | 0.234, 0.087 |
| 1400 (11 Sept 1756) | 2,169 | 0.556 | 0.255, 0.089 |

The same key, found on 446, reads three other letters of the same fonds with no change, written a year earlier or
later. Those readings begin, for instance, "mon maître ce que j'aurois fait moy même ... engagé de vous envoyer
copie de la lettre" (1399) and "Nieswiz ce onze septembre ... l'on apprend ici tous les jours des nouvelles fort
tragiques des diétines" (1400), which are the words of the typed readings. This is a statistical check of the key, not
a test of the readings, and it is the same material the key was found on for 446.

## 4. Checks inside the letters

- **The clear text in 1399.** Where the writer put a name in clear ("Mr le Palatin de Trok") the cipher has the
  title as a number ("Mr le [575] de Trok"), which is how 575 is fixed to Palatin; the same for Princesse (622) and
  the other values in `numbers.md` marked fixed.
- **The sum in 1399.** The letter gives the fund in words, "cent quarante et six mille francs". The five shares
  listed, 53,000 + 25,000 + 50,000 + 10,000 + 8,000, add up to 146,000, and the number-word code reads "[809] seigneurs",
  five. This was added up here and agrees.
- **The date of 1400.** The date line ends 824 811 823 818 810, which with the number words 805 to 824 reads "mil
  sept cent cinquante six"; the clear dateline says 11 September.

## 5. What was not checked

- The transcriptions against the scans (not reachable). The contributor corrected his first transcriptions against the
  scans on 7 Nov 2026 (`outside_checks.md`, "Corrections").
- Konopczyński, *Polska w dobie wojny siedmioletniej* (1909), the source of the outside checks on names (the table in
  `outside_checks.md`): not opened here. The identifications of Boeven as Radziwiłł's secretary and of the stolnik as
  Stanisław Poniatowski are the contributor's reading.
- Page 2 of 1398: the decryption has garbled stretches (for example lines r048 and r061 to r062) that the reading
  repairs by sense with the key and a French character model, not from the scan; its reading is graded C.
- The reading of the number groups: only the values of `numbers.md` marked fixed rest on clear text or repeated
  context; the "guesses" are read as `[?word]`.
