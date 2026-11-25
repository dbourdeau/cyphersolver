# Benasque ALCORT D/0042: a key sheet of Charles V's circle, two failed tests (issue #779, 18-19 Nov 2026)

Brice Dudout (with Claude) looked at the key sheet **Fundacion Hospital de Benasque, Fondo Alcort, ES/FHB - CD/ALCORT/D/0042**
("Claves para interpretar un lenguaje cifrado", DARA id 764904), which the Benasque sweep of 15 Nov 2026 had listed as
a key leaf of the 17th century and of unknown relation (`research/sweep_2026-11-15_chrome_wave9/key_leads.json`).
The results are in issue #779. This folder records them, with the project's reading of them. The DARA images are
CC BY-NC-SA 4.0 and none is reproduced here.

## What the sheet is

- A homophonic alphabet (2 to 4 single signs per letter), doubled letters ("Duplicadas") and nulls ("Perdidas").
- About 85 code words written as consonant + vowel + m syllables (Papa = Bam, Emperador = Bem ... Partida = Zum).
- Its names are those of Charles V's circle around 1547-1553: Mauricio "Elector", Juan Federico "duque de Saxa", "Rey de
  Inglaterra" (Edward VI), Granvela, Juan de Vega, Fernando Gonzaga, a Principe de Piamonte listed apart from the duke
  of Savoy. It is an imperial cipher of those years, not a 17th-century one.
- It is not the imperial cipher of gonzaga1549, vargas1552 and the Simancas sheet (Papa = Bam against pollo).

## It is not the key to the other Alcort cipher sheets

Checked by sign overlap on the DARA images at 150-300 dpi (Dudout):

| Sheet | System | Result |
|---|---|---|
| D/0055 (catalogue 2860) | numbers 10-24 with diacritic marks | no syllabic code, no distinctive sign in common; the pencil on the first leaf is show-through from the verso |
| D/0086 (catalogue 2864) | numbers 1-228 separated by commas | not this system |
| D/0040 | a letter of 1683-85 in clear with numerical groups | not this system |
| D/0056 (catalogue 2861, Naples, 14 Apr 1575) | letters with a "t" suffix, accented vowels, numbers 2-96 | a few common forms only; none of the key's distinctive signs; the key has no two-digit numbers |

The catalogue entries 2860, 2861 and 2864 now say so in `vetting.key_check` (and `verify` in 2864).

## Two pre-registered tests on ALCORT D/0004, both failed

D/0004 (Ferdinand I, Prague, 22 Oct 1544, to Pedro Lasso de Castilla and Gamiz) is cipher in most part with a
decipherment of the time in the margins. The D/0042 alphabet was frozen (SHA-256) before each test; the margin gloss
was not read; the cipher was transcribed blind with the margin and foot masked; one measure against the gloss, compared
with 200 shuffled control keys. The bar was 0.85 and the best control plus 0.30.

| Test | Portion | Letter accuracy | Best of 200 shuffled keys | Result |
|---|---|---|---|---|
| 18 Nov, first | page 1 | 0.547 | 0.344 | **failed** (bar 0.85) |
| 18 Nov, second | page 3 (499 cipher tokens, two blind passes, arbitrated blind) | 0.812 | 0.442 | **failed** (bar 0.85 missed by 0.038; margin +0.37 cleared) |

Pages 1 and 3 are spent as test portions. Page 2 (about 1,000 signs) is untouched. The author's explanation of the
misses (post hoc, **not counted**): S01 (a) and S17 (e) are not told apart in the letter; beta and 66 act as separators
or nulls; one sign (lx) is n. Correcting the signs after the fact lifted page 1 only to about 0.62.

What the results do support: the signs and code words of the sheet occur in D/0004, the raw decode reads as Spanish in
places and reproduces some of the gloss ("y tanto sera mayor ... ni la calidad del negocio lo sufre"), and the subject
matches the gloss (the marriage of the Infanta Maria to the duke of Orleans, agreed at Crepy, September 1544). What they
do not support: calling the key validated. The names date the sheet c. 1547-1553, later than D/0004 by three to nine
years, which is itself a question.

## What this folder adds to the project

- One lead (`candidates.json`): D/0004 itself, because its own marginal decipherment lets a key be rebuilt from
  adjacent plaintext and tested on a held-out page. The earlier sweep had excluded it ("decipherment filed on the
  sheet, so not a lead"); the lead's `status` carries both failed tests.
- No target folder, no catalogue entry, no promotion. The D/0042 sheet is a key leaf, not a document with ciphertext,
  so it has no row of its own; the catalogue notes of 2860, 2861 and 2864 carry what was found.
- A final test on page 2 is possible. The corrected sign identifications are frozen and hashed first, the transcription
  is done in two blind passes, and the result is reported whichever way it goes. A pass would validate that corrected
  version, not the 0.812.

Asked of the author (issue #779): the two pre-registrations and hashes, the score files and the single-pass
transcription of the sheet, in a dated folder under `research/`.

The work is Brice Dudout's, with Claude; this README and the catalogue notes were written by the project from his
comments on issue #779.
