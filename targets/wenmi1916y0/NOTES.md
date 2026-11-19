# Grid Y0 — indicator “Cg”: 10 telegrams, 17 July 1916 - 11 November 1916

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "Grid Y0 — indicator “Cg”"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0413 | 17 July 1916 | Tokyo → Shanghai (中華新報) → Yunnan | JACAR B03050090000 | sent 4.30 pm
- 0416a | 19 July 1916 | Tokyo → Shanghai (中華新報, 轉文羣轉滇督) | JACAR B03050090000 | sent 5.50 pm
- 0449 | 8 September 1916 | Tokyo → Kunming (唐都督) | JACAR B03050090100 | sent 7 pm
- 0455a | 13 September 1916 | Tokyo → Kunming (唐都督) | JACAR B03050090100 | sent 7.30 pm
- 0467 | 11 October 1916 | Tokyo → Kunming (唐都督) | JACAR B03050090100 | sent 5.46 pm
- 0473 | 20 October 1916 | Tokyo → Kunming (唐督軍) | JACAR B03050090100 | sent 7.30 pm
- 0489a | 5 November 1916 | Tokyo → Kunming (唐督軍) | JACAR B03050090100 | sent 11.55 am
- 0496a | 9 November 1916 | Tokyo → Kunming (唐督軍) | JACAR B03050090100 | sent 6.25 pm
- 0498 | 9 November 1916 | Kunming → Tokyo (趙伸 c/o 関正雄) | JACAR B03050090100 | sent 2.35 pm
- 0494a | 11 November 1916 | Tokyo → Kunming (財政廳) | JACAR B03050090100 | sent 8.35 pm

## System

Tokyo ↔ Yunnan, July–November 1916. Grid of 17 consonants × 6 vowels (including y), recovered in October 2026.

Key file: `key.tsv` (observed cells (96)). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

454 of 456 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0413 | 42 | 42 | 1.000 | — | read |
| 0416a | 29 | 29 | 1.000 | — | read |
| 0449 | 35 | 33 | 0.943 | 2 douteux | read (floor) |
| 0455a | 32 | 32 | 1.000 | — | read |
| 0467 | 47 | 44 | 0.936 | 3 douteux | read in part |
| 0473 | 61 | 58 | 0.951 | 1 illisible, 2 douteux | read |
| 0489a | 9 | 9 | 1.000 | — | read |
| 0496a | 45 | 44 | 0.978 | 1 douteux | read |
| 0498 | 117 | 102 | 0.872 | 14 douteux, 1 illisible | read in part |
| 0494a | 39 | 37 | 0.949 | 2 douteux | read (floor) |

**430 of 456 codes sure (94.3%)**; 4 of 10 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0449: 35 codes, 2 holes -> **read** (floor used)
- 0494a: 39 codes, 2 holes -> **read** (floor used)
- 0467: 47 codes, 3 holes -> stays read in part (40 or more)
- 0498: 117 codes, 15 holes -> stays read in part (40 or more)

The class stays **read in part**.
