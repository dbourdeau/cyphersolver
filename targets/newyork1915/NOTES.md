# “New York” table: 4 telegrams, 5 July 1914 - 20 February 1915

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "“New York” table"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0110b | 5 July 1914 | San Francisco → Toyama, Renanzaka ; signé Young China | JACAR B03050087400, PDF page 51
- 0211b | February 1915 | New York → “Sunwen”, Tokyo | JACAR B03050087600, PDF page 49
- 0198 | 18 February 1915 | New York → “Sunwen”, Tokyo | JACAR B03050087600, PDF page 36
- 0201 | 20 February 1915 | New York → “Sunwen”, Tokyo | JACAR B03050087600, PDF page 39

## System

New York → Sun Yat-sen, February 1915. Table recovered in October 2026. Also attested from San Francisco on 5 July 1914.

Key file: `key.tsv` (full table). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

109 of 109 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0110b | 9 | 9 | 1.000 | — | read |
| 0211b | 40 | 32 | 0.800 | 8 douteux | read in part |
| 0198 | 25 | 22 | 0.880 | 3 douteux | read in part |
| 0201 | 35 | 29 | 0.829 | 6 douteux | read in part |

**92 of 109 codes sure (84.4%)**; 3 of 4 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0211b: 40 codes, 8 holes -> stays read in part (40 or more)
- 0198: 25 codes, 3 holes -> stays read in part (more than 2 holes)
- 0201: 35 codes, 6 holes -> stays read in part (more than 2 holes)

The class stays **read in part**.
