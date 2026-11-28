# Grid G0 — “文密”: 7 telegrams, 23 June 1916 - 30 September 1916

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "Grid G0 — “文密”"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0348 | 23 June 1916 | Tokyo → Zhaoqing (軍務院, 岑) | JACAR B03050089900 | sent 8.13 pm
- 0386 | 30 June 1916 | Tokyo → Zhaoqing (軍務院, 岑) | JACAR B03050089900 | sent 2.45 pm
- 0406 | 12 July 1916 | Tokyo → Shanghai (中華新報, 轉文羣) | JACAR B03050090000 | sent 2.50 pm
- 0415 | 18 July 1916 | Tokyo → Zhaoqing (軍務院) | JACAR B03050090000 | sent 5.30 pm
- 0416b | 19 July 1916 | Tokyo → Zhaoqing (軍務院) | JACAR B03050090000 | sent 5.50 pm
- 0455b | 13 September 1916 | Tokyo → Zhaoqing (岑都司令) | JACAR B03050090100 | sent 7.30 pm
- 0462 | 30 September 1916 | Tokyo → Zhaoqing (都司令部, 李印泉) | JACAR B03050090100 | sent 11 am

## System

Tokyo → Military Affairs Council (Zhaoqing) and Shanghai, June–September 1916. Coordinate grid of 20 consonants × 5 vowels, recovered in October 2026.

Key file: `key.tsv` (observed cells (98)). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

351 of 351 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0348 | 64 | 64 | 1.000 | — | read |
| 0386 | 38 | 35 | 0.921 | 3 douteux | read in part |
| 0406 | 81 | 78 | 0.963 | 3 douteux | read |
| 0415 | 77 | 74 | 0.961 | 3 douteux | read |
| 0416b | 20 | 19 | 0.950 | 1 douteux | read |
| 0455b | 18 | 18 | 1.000 | — | read |
| 0462 | 53 | 53 | 1.000 | — | read |

**341 of 351 codes sure (97.2%)**; 1 of 7 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0386: 38 codes, 3 holes -> stays read in part (more than 2 holes)

The class stays **read in part**.
