# “Seventeenth” table: 4 telegrams, 17 April 1916 - 20 April 1916

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "“Seventeenth” table"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0591 | 17 April 1916 | Shanghai (0124) → Rosamonde (20/11 words) [Seventeenth] | JACAR B03050088500, PDF page 41
- 0593 | 18 April 1916 | Shanghai (035) → Rosamonde (12/11 words) [Seventeenth] | JACAR B03050088500, PDF page 43
- 0601a | 18 April 1916 | Tokyo (中山) → Yulangsie, 31 Rue du Consulat, Shanghai (18 words) | JACAR B03050088500, PDF page 51
- 0608a | 20 April 1916 | Shanghai (027) → Rosamonde (15/14 words) [Seventeenth] | JACAR B03050088600, PDF page 4

## System

Shanghai → “Rosamonde”, April 1916; clear indicator “Seventeenth”. Condenser of the Swatow family: consonants rotated, vowel order i u a e o. Table recovered in October 2026.

Key file: `key.tsv` (full table). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

97 of 97 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
with status and emendations), `reading.md` (Chinese text, doubtful codes in {braces}), `translation.md` (English).
Doubtful letters were re-read on the scans by Brice Dudout in blind panels before publication.

## Remaining gaps

- Codes marked doubtful (status "douteux") or unread ([?]) in `decryption.txt` / `reading.md`.

## Read share with sure codes only (18 Nov 2026)

Rule applied as written in PR #728 (owner's decision of 16 Nov 2026, README Conventions "The read share counts cipher words only"): sure only; a probable, inferred or unread unit is a hole. A Chinese telegram is wholly in cipher, and its unit here is the code: one four-figure code is one character, so
the share is counted in codes, not words (a word is one or two characters; no word count is made). Counted from the
status column of `decryption.txt`: `ok` and `confirmé:…` are sure; `douteux` (doubtful, the `{x}` of `reading.md`) and
`illisible` are holes.

| telegram | codes | sure | share | holes | state |
|---|---|---|---|---|---|
| 0591 | 24 | 15 | 0.625 | 9 douteux | read in part |
| 0593 | 18 | 9 | 0.500 | 9 douteux | read in part |
| 0601a | 30 | 24 | 0.800 | 6 douteux | read in part |
| 0608a | 25 | 21 | 0.840 | 4 douteux | read in part |

**69 of 97 codes sure (71.1%)**; 4 of 4 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0591: 24 codes, 9 holes -> stays read in part (more than 2 holes)
- 0593: 18 codes, 9 holes -> stays read in part (more than 2 holes)
- 0601a: 30 codes, 6 holes -> stays read in part (more than 2 holes)
- 0608a: 25 codes, 4 holes -> stays read in part (more than 2 holes)

The class stays **read in part**.
