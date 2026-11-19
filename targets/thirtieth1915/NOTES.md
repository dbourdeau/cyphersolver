# “Thirtieth” table: 10 telegrams, 26 February 1915 - 5 May 1915

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "“Thirtieth” table"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0211 | 26 February 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087600, PDF page 49 | sent 3.32 pm
- 0203 | 27 February 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087600, PDF page 41 | sent 11.43 am
- 0220 | 7 March 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087600, PDF page 58 | sent 11.12 am
- 0224 | 10 March 1915 | Tokyo (頭山) → “Junzaburo”, Shanghai | JACAR B03050087700, PDF page 4 | sent 11.10 am
- 0233a | 12 March 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087700, PDF page 13 | sent 1.57 pm
- 0233b | 13 March 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087700, PDF page 13 | sent 2.3 pm
- 0243 | 30 March 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087700, PDF page 23 | sent 11.30 am
- 0246 | 31 March 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087700, PDF page 26 | sent 11.55 am
- 0255 | 11 April 1915 | Shanghai → “Rosamonde”, Tokyo | JACAR B03050087700, PDF page 35 | sent 3.22 pm
- 0261 | 5 May 1915 | Shanghai → “Rosamonde”, Tokyo (“Thirtieth”) | JACAR B03050087700, PDF page 41 | sent 5.40 pm

## System

Shanghai → “Rosamonde” and Tokyo → “Junzaburo”, February–May 1915; clear indicator “Thirtieth”. Table recovered in October 2026.

Key file: `key.tsv` (full table). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

262 of 263 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0211 | 36 | 33 | 0.917 | 3 douteux | read in part |
| 0203 | 16 | 16 | 1.000 | — | read |
| 0220 | 19 | 17 | 0.895 | 2 douteux | read (floor) |
| 0224 | 25 | 23 | 0.920 | 2 douteux | read (floor) |
| 0233a | 20 | 19 | 0.950 | 1 douteux | read |
| 0233b | 23 | 16 | 0.696 | 7 douteux | read in part |
| 0243 | 32 | 26 | 0.812 | 6 douteux | read in part |
| 0246 | 7 | 6 | 0.857 | 1 douteux | read (floor) |
| 0255 | 25 | 23 | 0.920 | 2 douteux | read (floor) |
| 0261 | 60 | 58 | 0.967 | 2 douteux | read |

**237 of 263 codes sure (90.1%)**; 7 of 10 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0220: 19 codes, 2 holes -> **read** (floor used)
- 0224: 25 codes, 2 holes -> **read** (floor used)
- 0246: 7 codes, 1 hole -> **read** (floor used)
- 0255: 25 codes, 2 holes -> **read** (floor used)
- 0211: 36 codes, 3 holes -> stays read in part (more than 2 holes)
- 0233b: 23 codes, 7 holes -> stays read in part (more than 2 holes)
- 0243: 32 codes, 6 holes -> stays read in part (more than 2 holes)

The class stays **read in part**.
