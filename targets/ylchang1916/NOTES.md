# Huang Xing's table: 9 telegrams, 26 May 1916 - 6 June 1916

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "Huang Xing's table"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0091a | 26 May 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050089100, PDF page 32 | sent 6.10 pm
- 0095a | 28 May 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050089100, PDF page 36 | sent 9.15 pm
- 0115b | 30 May 1916 | Shanghai → Tokyo (Ylchang) | JACAR B03050089100, PDF page 56 | sent 3.35 pm
- 0130b | 31 May 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050089200, PDF page 13 | sent 2.50 pm
- 0131b | 31 May 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050089200, PDF page 14
- 0144a | 2 June 1916 | Shanghai → Tokyo (Ylchang) | JACAR B03050089200, PDF page 27
- 0145 | 3 June 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050089200, PDF page 28 | sent 10.10 am
- 0152b | 6 June 1916 | Tokyo → Shanghai (Junzaburo) | JACAR B03050089200, PDF page 35 | sent 2.45 pm
- 0160a | 6 June 1916 | Shanghai → Tokyo (Ylchang) | JACAR B03050089200, PDF page 43 | sent 4.34 pm

## System

Tokyo (Huang Xing) → “Junzaburo”, without indicator, and Shanghai → “Ylchang” (Huang Xing), late May – June 1916. Table recovered in October 2026. Not to be confused with the three-kana code of another telegram of Huang Xing (25 May 1916, to Lin Hu and Li Genyuan), whose system was identified by D. Bourdeau and whose formula by S. Tomokiyo[22, 23].

Key file: `key.tsv` (observed cells (92)). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

264 of 266 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0091a | 20 | 18 | 0.900 | 2 douteux | read (floor) |
| 0095a | 20 | 18 | 0.900 | 2 douteux | read (floor) |
| 0115b | 55 | 41 | 0.745 | 13 douteux, 1 illisible | read in part |
| 0130b | 24 | 24 | 1.000 | — | read |
| 0131b | 20 | 19 | 0.950 | 1 douteux | read |
| 0144a | 15 | 12 | 0.800 | 3 douteux | read in part |
| 0145 | 47 | 43 | 0.915 | 4 douteux | read in part |
| 0152b | 25 | 23 | 0.920 | 2 douteux | read (floor) |
| 0160a | 40 | 35 | 0.875 | 5 douteux | read in part |

**233 of 266 codes sure (87.6%)**; 7 of 9 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0091a: 20 codes, 2 holes -> **read** (floor used)
- 0095a: 20 codes, 2 holes -> **read** (floor used)
- 0152b: 25 codes, 2 holes -> **read** (floor used)
- 0115b: 55 codes, 14 holes -> stays read in part (40 or more)
- 0144a: 15 codes, 3 holes -> stays read in part (more than 2 holes)
- 0145: 47 codes, 4 holes -> stays read in part (40 or more)
- 0160a: 40 codes, 5 holes -> stays read in part (40 or more)

The class stays **read in part**.
