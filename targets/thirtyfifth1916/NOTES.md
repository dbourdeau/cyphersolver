# “Thirty fifth” table (Hu Hanmin): 2 telegrams, 22 April 1916 - 24 April 1916

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "“Thirty fifth” table (Hu Hanmin)"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0627 | 22 April 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050088600, PDF page 23 | sent 10.15 am
- 0642b | 24 April 1916 | Shanghai → Tokyo (Rosamonde) | JACAR B03050088600, PDF page 38 | sent 6.26 pm

## System

Tokyo → “Junzaburo”, 22 April 1916, to be forwarded to Hu Hanmin (header in the “Shanghai” table), and Shanghai → “Rosamonde”, 24 April 1916, reply signed 展 (Hu Hanmin); clear indicator “Thirtyfifth”. Table recovered on 27 October 2026 (see the method).

Key file: `key.tsv` (full table). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

130 of 130 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0627 | 115 | 110 | 0.957 | 5 douteux | read |
| 0642b | 15 | 14 | 0.933 | 1 douteux | read (floor) |

**124 of 130 codes sure (95.4%)**; 1 of 2 telegrams under the bar, so the target goes **read -> read in part** (superseded on 19 Nov 2026 by the floor for short texts, below). Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0642b: 15 codes, 1 hole -> **read** (floor used)

Every document is now read: the class is **read** (no change from before the recount of 18 Nov).
