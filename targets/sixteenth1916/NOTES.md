# “Sixteenth” table: 6 telegrams, 15 April 1916 - 22 April 1916

Status: no write-up (contributed by Brice Dudout and published on his Wenmi site; listed with a link to this folder in the "Brice Dudout's tables" section of docs/sunintercepts.html, decided 27 Oct 2026)

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site (telegrams page, system "“Sixteenth” table"):
https://bdudout.github.io/wenmi/en/telegrams.html . Already reported to this repository by email (11-23 Oct 2026) and
listed in `../sunyatsen/y1916/NOTES.md` ("Brice Dudout's wider corpus ... Not checked here"); this PR sends the full
texts required by CONTRIBUTING.md.

## The documents

Copies made by the Communications Bureau of the Ministry of Communications for the Foreign Ministry (Gaimushō
1.6.1.4-2-1-2, 特定人ノ発受郵便物取調), JACAR. The copies carry no decipherment.

- 0590 | 15 April 1916 | Shanghai (0125) → Nakayama 109 Harajuku (15 words) [Sixteenth] | JACAR B03050088500, PDF page 40
- 0592 | 18 April 1916 | Shanghai (03) → Nakayama 109 Harajuku (18 words) [Sixteenth] | JACAR B03050088500, PDF page 42
- 0603 | 19 April 1916 | Tokyo (中山) → Yamanaka, Banzaikwan, Shanghai (13 words) | JACAR B03050088500, PDF page 53
- 0616 | 21 April 1916 | Tokyo (中山) → Yamanaka, Banzaikwan, Shanghai (21 words) | JACAR B03050088600, PDF page 12
- 0629a | 22 April 1916 | Shanghai (015) → Nakayama Harajuku (7 words) [Sixteenth] | JACAR B03050088600, PDF page 25
- 0629b | 22 April 1916 | Shanghai (082) → Nakayama Harajuku (29 words) [Sixteenth] | JACAR B03050088600, PDF page 25

## System

Tokyo (中山) ↔ Shanghai and Yamanaka, April 1916; clear indicator “Sixteenth”. Condenser of the Swatow family: consonants rotated, vowel order e u o i a. Table recovered in October 2026.

Key file: `key.tsv` (full table). Each pair of syllables (four letters) gives one
four-digit standard telegraph code (電報新編), with no additive.

## Reading

168 of 168 codes give a character. `transcription.txt` (letters by code), `decryption.txt` (code by code,
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
| 0590 | 25 | 24 | 0.960 | 1 douteux | read |
| 0592 | 29 | 27 | 0.931 | 2 douteux | read (floor) |
| 0603 | 25 | 24 | 0.960 | 1 douteux | read |
| 0616 | 45 | 32 | 0.711 | 13 douteux | read in part |
| 0629a | 7 | 7 | 1.000 | — | read |
| 0629b | 37 | 31 | 0.838 | 6 douteux | read in part |

**145 of 168 codes sure (86.3%)**; 3 of 6 telegrams under the bar, so the target goes **read -> read
in part**. Before, the doubtful codes were counted as read. Many telegrams are short: one doubtful code puts a
telegram of under 20 codes below 95%. The codes marked `douteux` are counted as they stand; none was re-read on the
scans for this count. Counted by a script on
`decryption.txt`; `v10_relabel.py` does not measure Chinese readings.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more; for Chinese telegraphic codes one code is one word. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- 0592: 29 codes, 2 holes -> **read** (floor used)
- 0616: 45 codes, 13 holes -> stays read in part (40 or more)
- 0629b: 37 codes, 6 holes -> stays read in part (more than 2 holes)

The class stays **read in part**.
