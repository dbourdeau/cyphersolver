# krassin1921: Krassin's Nr 451 and Lutowinoff's Nr 523, Berlin to Moscow, 1921 (NARA M316 roll 43; from catalogue 669)

Status: read (10 Nov 2026). Contributed by Harumi-Matsuba (issue #370; repository `Harumi-Matsuba/soviet1921-public`,
commit 5aac683, documents and data CC BY 4.0 per its licence file), who worked with Anthropic Claude (Claude Fable 5.2)
and used OpenAI Codex as a blind second transcriber and Claude Sonnet as a second judge. **No human has compared the
transcription with the images**, and the project has not seen the images (the NARA catalogue is refused by this
machine's network proxy on 10 Nov 2026); what the project checked is the key against the contributor's transcription
(`verify.py`, `VERIFICATION.md`).

Split from `kopp1921` (one key, one entry): this digraphic table with a square transposition is a different system
from the four-figure table of Kopp and Lutovinov's Nr 417, the Karakhan table and the five-figure SWET traffic, all of
which stay unread in `kopp1921` and `karakhan1921`.

## The documents

NARA RG 59, Central Decimal File 1910-29, 861.00, microfilm M316 roll 43 (861.00/8774-8910, NAID 604704577), typed
copies of radiograms intercepted at the US High Commission, Constantinople, and sent to State by Admiral Mark L. Bristol.
Frame headings as the contributor transcribed them (`contributor_sources.md`):

- Frames 0427-0428: "JUNE 14th 1921. FROM BERLIN TO MOSCOW", "TSCHITSCHERIN MOSKAU.", "WIEDERHOLUNG FUNKSPRUCH Nr 451
  VOM 30 MAI 1921. SOROK 76988 09086 ...", signed KRASSIN. 320 five-digit groups, 1,600 digits; the /21545/ at the head
  of frame 0428 repeats the last group of 0427 (a catchword) and is left out. `ciphertext_451.txt`.
- Frame 0432: "TSCHITSCHERIN DLJA LITWINOVA MOSKAU", "FUNKSPRUCH Nr 523 VOM 14 JUNI 1921. KOPIA TSCHITSCHERINU,
  MOLOTOWU SCHLJAPNIKOWU. DWADZAT TCHETYRE 15255 04134 ...", signed LUTOWINOFF. 115 groups, 575 digits (one short of
  24 x 24). `ciphertext_523.txt`.

Transcription: the contributor's, from the NARA catalogue OCR, one digit changed from the image (frame 0427, line 12,
group 2: an I typed above the first digit, read 1). A blind second transcription by OpenAI Codex from the images agrees
on 1,598 of 1,600 digits and 575 of 575 (his figures); one of the two differences is an overstruck digit (digit 182
of Nr 451, kept as 5, the plaintext wants 7).

## The cipher

Each letter becomes a pair of digits from a 5 x 6 table (`key.tsv`), first digit 6/7/8/9/0, second digit 0-5:

```
     0  1  2  3  4  5
6    е  в  ь  э  к  щ
7    а  ф  я  з  н  р
8    б  ы  г  л  ч  ю
9    ж  ·  ш  и  д  о
0    ·  т  п  х  у  м        06 = с   10 = full stop   33 = comma   00 = filler
```

The pairs are written row by row into a square of N x N digits (N/2 letters to a row), the rest filled with 00; N is
the Russian number word before the groups (SOROK = 40, DWADZAT TCHETYRE = 24). The square is sent column by column,
columns not permuted. Nr 451: digit columns first digit / second digit, rows read right to left. Nr 523: the mirror
image (second digit / first digit, rows left to right). Plaintext is telegraphic Russian, й written и, ё written е.

## How the key was found (contributor)

From the ciphertext alone (`contributor_method.md`): the number word matches the digit count (1,600 = 40 x 40); cut
into runs of N, the digits fall into alternating columns of high and low digits; pairing neighbouring columns gives
about 30 kinds of pair with an index of coincidence of 0.0551 / 0.0490. Simulated annealing on the 764 pairs of Nr 451
alone, scored with Russian letter 4-grams, no crib; three runs ended at the same score. Three values were then changed
on reading (10 full stop, 33 comma, 71 ф) and 28 was taken out of the table. Nr 523 was then deciphered with the
same table unchanged; it was not used to build it. Contributor's control: 1,000 shuffles of the table's letter values,
none as good as the real table in either message (mean 4-gram score real -11.127 / -12.329, best shuffled -14.686 /
-14.796).

## Project check (10 Nov 2026)

`verify.py` was written here from the description in the issue, not from the contributor's `decrypt.py`. Applied to
the contributor's ciphertext files it gives both texts identical, pair for pair, to the contributor's reading
(`decryption_451.txt`, `decryption_523.txt`; compare `reading_*.tsv`). The pair counts in `reading_*.tsv`: Nr 451 764
pairs, 750 marked read; Nr 523 288 pairs, 279 marked read; together 1,029 of 1,052 (97.8%). The Russian reads as
sentences in both messages (read through here; see the reading below). The images were not compared: the NARA catalogue
could not be reached.

The project's n-gram validation (`docs/_validate.py`) has no Russian model in `lang/`, so it was not run; the
contributor's shuffled-table control and the fact that Nr 523, not used to build the table, reads with it, are the
statistical evidence.

## What they say

Russian with word breaks and the contributor's emendations: `contributor_reading.md`; English: `translation.md`.

- Nr 451, Krassin to Chicherin, 30 May 1921 (repeated 14 June): the Berlin trade representation works normally and is
  well spoken of by business circles and the Auswärtiges Amt; from talks with Lutovinov and Stomonyakov, the auditing
  commission has found rich material that shows the previous period of the Berlin representation in a very bad light;
  send Kulyabko to Berlin at once, the visa to be given by Stähler under the agreement; take no decisions before the
  commission's report, or the traces will be covered; Lutovinov and Stomonyakov will report in Moscow after the audit.
- Nr 523, Lutovinov to Chicherin for Litvinov, copies to Chicherin, Molotov and Shlyapnikov, 14 June 1921: he finds
  the position given to Kopp in Berlin inadmissible; Kopp says the Narkomindel has decided to keep him in Berlin as
  polpred; if so, Lutovinov protests against the appointment before the audit ends, asks to whom he should hand over,
  and will hand over to Brodovsky in a number of hours.

## Prior work

None found by the contributor (`contributor_prior_check.md`, 10 Nov 2026: this ledger at c59841baa, its issues and
pull requests, GitHub code search, Cryptiana, wenmi, Tiltman's "Experiences 1920-1939", Chernoperov's article on Kopp,
web searches in Russian and English). Not read by him or here: Sovetsko-germanskie otnosheniya vol. 2 (1971), DVP SSSR
vol. IV, Bol'shevistskoe rukovodstvo. Perepiska 1912-1927, TNA HW 12, NARA RG 457 6707N. The plaintext may be in print
there. The project's own notes on the file (`kopp1921`) had not read any figure message.

## Remaining gaps

- Pairs 16 (Nr 523, the day of the letter) and 76 53 18 (Nr 523, a number of hours) - blocker: too-short; numbers occur once each in two messages, no way to fix how digits are written
- Pairs 28 (three times, read комисс from context), 77 (twice, раб), 91 (once, ц) and 14 (once, taken as an error for 94 д) in Nr 451 - blocker: too-short; outside the 5 x 6 table, values from context only, no further message in this table to confirm them
- Eleven single wrong letters (Nr 451: то[ф]гого, все[м], бога[]ыи, ревизионо[з], ревизионо[н], высл[50]ть, до[54]лада; Nr 523: опре[о]эленоэ, п[д]ложениэ, окон[ю]ания, ко[у]у) - blocker: illegible; sending or interception errors on the typed sheet, two readers agree on the digits, one (высл[50]ть) is overstruck
- A human check of the transcription against the NARA frame images - blocker: needs-physical-access; the NARA catalogue is not reachable from the project
- Printed Soviet editions (Sovetsko-germanskie otnosheniya vol. 2, DVP SSSR IV) and HW 12 / RG 457 for a calibration text - blocker: needs-physical-access; not online

## Escalation

- [x] siblings: the contributor checked the OCR of M316 rolls 40-48 for a number word before the groups and alternating high/low columns; only these two messages were found. Kopp's Nr 417 table and the SWET traffic are other systems (kopp1921)
- [x] clear-pages: Bristol's covering despatch No. 153 (041-0871/0872) read for kopp1921; no decipherment in the file
- [x] known-keys: not needed, the table reads both messages; it is not one of the transposition keys of lejava1921 or voikov1921
- [x] print: contributor's search (`contributor_prior_check.md`); the Soviet document editions could not be read, recorded above
- [x] key-rebuild: the table was recovered by annealing on Nr 451 and confirmed on Nr 523; the off-table pairs were tried from context
- [n/a] retry: the whole of both texts has been decrypted with the full table; what is open is numbers, off-table pairs seen once or twice, and single garbled letters

## Files

| File | Content |
|---|---|
| `ciphertext_451.txt`, `ciphertext_523.txt` | the contributor's transcriptions, five-digit groups |
| `key.tsv` | the table, with the off-table pairs and their context values |
| `reading_451.tsv`, `reading_523.tsv` | the contributor's reading pair by pair, read/open |
| `decryption_451.txt`, `decryption_523.txt` | the project's re-decryption (`verify.py --write`) |
| `translation.md` | Russian reading and English translation of both messages |
| `contributor_*.md` | the contributor's README, method, reading, open points, prior-art search and sources |
| `verify.py`, `VERIFICATION.md` | the project's re-check |
| `profile.json` | the target profile |
