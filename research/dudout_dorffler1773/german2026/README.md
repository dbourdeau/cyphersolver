# Catalogue 1773 (Dörffler): character-level test of TABLE-C04 on a fresh transcription (Mike German, November 2026)

Riksarkivet SE/RA/2115/I/19/100, 101, 102 and 103, Public Domain Mark. Text files only, no images.
This is a **test of the table**, plus a separate proposal of additions. **No reading is claimed.** The documents stay "decoded, not read".
TABLE-C04 is not copied here. Every figure uses `../table/TABLE-C04.json`, SHA-256 `14b38f499a961b99bc7707aa71106cf5f5ca140eaa27faae1728db827b41ef28`.

## The test
- **Material.** All 136 coded pages of the four volumes (`transcription/pages.txt`, Riksarkivet image numbers), read as 270 half-pages: 26,270 cipher numbers and the clerk's interlinear decryptions (`transcription/p5_lines.jsonl`, tag `L` = manuscript line, tag `G` = decryption).
- **Measure.** Share of the clerk's decryption letters that the decoding of the next two cipher lines reproduces in order, counting runs of 3+ letters only.
- **Control.** The same key with its values shuffled among its numbers, 200 draws.
- **Split.** Fit half = volume 19/102 plus even pages elsewhere. Test half = odd pages outside 19/102. "Fresh lines" = every line outside 19/102 except pages 277 and 304 of 19/100.
- **Who chose what.** I chose the split and the measure, on 15 November 2026, after TABLE-C04 was published. No hashes were frozen in advance. The record is the commit history of https://github.com/steps-re/dorffler-cipher.

## Result (`evaluation.txt`, from `scripts/evaluate.py`)
| Reading | Key | Test half | Shuffled, mean (best of 200) | Fresh lines |
|---|---|---|---|---|
| whole-page (`p5_lines.whole_page.jsonl`) | TABLE-C04 | 62.1% | 10.3% (13.9%) | 66.0% |
| strips (`p5_lines.jsonl`) | TABLE-C04 | 71.6% | 10.5% (14.1%) | 73.0% |
| strips | TABLE-C04 + `proposal/ADDITIONS.tsv` | 73.9% | 11.4% (14.8%) | 75.6% |

By volume, TABLE-C04 on the strip reading: 19/100 71.7%, 19/101 75.3%, 19/102 47.7%, 19/103 71.4%.

## The two readings
- **Whole-page.** Two models (Gemini 4 Argon, Gemini 3.7 Flash) each read a whole half-page. Disputed numbers were re-checked on the image. This reading misreads 8 as 0 (28 as 20, 18 as 10, 87 as 07).
- **Strips.** Each half-page cut into 5 overlapping full-resolution strips, read by Gemini 4 Argon and stitched (`scripts/strips.py`, `scripts/consensus.py`). The key was never shown to the reader. 249 half-pages use this read, 8 use an 11-strip read, and 13 keep the whole-page read because the strip read failed a key-free count check. A blind read of two pages by Claude agrees with the strip read on 93.7% and 85.7% of numbers, against 91.0% and 80.2% for the whole-page read.

## Proposal, separate from the table (`proposal/`)
- **Method.** For each number without a value, its fit-half occurrences are dealt into two disjoint sets. Gemini 4 Argon proposes a value from each set alone. A value is kept only if both agree (`scripts/cloze.py`, `proposal/cloze.jsonl`).
- **Check.** 62 entries of TABLE-C04 were hidden and run the same way. Both sets agreed on 58, and 53 of the 58 matched the table (`proposal/cloze_report.txt`).
- **15 fills and 6 weaker proposals** are in `proposal/ADDITIONS.tsv`. Two proposals disagree with the table: 210 viel (C04 wider) and 226 wur (C04 wer).
- **Out-of-range numbers.** Numbers under 14 (07, 02, 2, 8, 9, 11) in the whole-page reading were misreads of 87, 82 and similar. None is proposed.
- **Structure.** The word list 146-226 and the names list from 250 are alphabetical (95% and 99% of pairs in order, v-words before u-words). 227-249 is an unordered supplement.

## What did not work
- Pairing each decryption with cipher anywhere on its page (`scripts/align.py`): 60.9% against 62.1% on the whole-page reading.
- An 11-strip pass over 19/102 with a three-reading vote: 134 numbers changed, fit half 60.1% to 60.3%.
- An earlier set of 28 additions and a 64.7% figure are withdrawn. Their prompts showed test-half decryptions (found by D. Bourdeau, issue #696).

## Limits
- One reader family (Gemini) made the transcription. No person has read it against the images.
- The clerk's decryptions were re-read with the cipher, so the strip test has 415 test lines where the whole-page test had 422.
- 3.3% of numbers have no value under the table plus additions. 19/102 stays under 50%.
- The original key has not been found. Riksarkivet Chifferklaver (SE/RA/202) is not digitized.

## Reproduce
```
CIPHER_DATA=$PWD/transcription python3 scripts/evaluate.py ../table/TABLE-C04.json proposal/ADDITIONS.tsv
```
The reading scripts need the page images (Riksarkivet IIIF) and the `llm` CLI. The full pipeline, raw model reads and decode are at https://github.com/steps-re/dorffler-cipher.

Credits: TABLE-C04 and the layout of the code, Brice Dudout (Europe chiffrée) and Daniel Bourdeau. Transcription, test and proposal, Mike German (Steps Ventures). Tools: Gemini 4 Argon and Gemini 3.7 Flash (reading, proposals), Claude (code, blind check). Licence CC BY 4.0.
