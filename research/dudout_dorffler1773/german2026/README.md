# Catalogue 1773 (Dörffler): character-level test of TABLE-C04 on a fresh transcription (Mike German, November 2026)

Riksarkivet SE/RA/2115/I/19/100, 101, 102 and 103, Public Domain Mark. Text files only, no images.
This is a **test of the table**, plus a separate proposal of additions. **No reading is claimed.** The documents stay "decoded, not read".
TABLE-C04 is not copied here. Every figure uses `../table/TABLE-C04.json`, SHA-256 `14b38f499a961b99bc7707aa71106cf5f5ca140eaa27faae1728db827b41ef28`.

## The test
- **Material.** All 136 coded pages of the four volumes (`transcription/pages.txt`, Riksarkivet image numbers), read as 270 half-pages: 25,809 cipher numbers and the clerk's interlinear decryptions (`transcription/p5_lines.jsonl`, tag `L` = manuscript line, tag `G` = decryption).
- **Measure.** Share of the clerk's decryption letters that the decoding of the next two cipher lines reproduces in order, counting runs of 3+ letters only.
- **Control.** The same key with its values shuffled among its numbers, 200 draws.
- **Split.** Fit half = volume 19/102 plus even pages elsewhere. Test half = odd pages outside 19/102. "Fresh lines" = every line outside 19/102 except pages 277 and 304 of 19/100.
- **Who chose what.** I chose the split and the measure, on 15 November 2026, after TABLE-C04 was published. No hashes were frozen in advance. The record is the commit history of https://github.com/steps-re/dorffler-cipher.
- **Order of events.** I adopted the strip method after I had seen the whole-page test score (62.1%), because that score was low and I suspected my reading. So 71.6% is not a pre-registered number. The key did not change between the two readings.

## Result (`evaluation.txt`, from `scripts/evaluate.py`)
| Reading | Key | Test half | Shuffled, mean (best of 200) | Fresh lines |
|---|---|---|---|---|
| whole-page (`p5_lines.whole_page.jsonl`) | TABLE-C04 | 62.1% | 10.3% (13.9%) | 66.0% |
| strips (`p5_lines.jsonl`) | TABLE-C04 | 71.6% | 10.5% (14.1%) | 73.0% |
| strips | TABLE-C04 + `proposal/ADDITIONS.tsv` | 73.9% | 11.4% (14.8%) | 75.6% |

By volume, TABLE-C04 on the strip reading: 19/100 71.7%, 19/101 75.3%, 19/102 60.3%, 19/103 71.4%. On the fit half it is 66.8%.

### Harder controls (`evaluation.txt`, 200 draws each)
The plain shuffle moves values among all numbers. These keep more structure, or break only the pairing:

| Control | Test half, mean (best) | Fresh lines, mean (best) |
|---|---|---|
| TABLE-C04 itself | 71.6% | 73.0% |
| Values shuffled only among numbers of the same kind (letters 14-65, syllables 66-145, words and names 146+) | 7.0% (9.3%) | 7.2% (10.2%) |
| Each decryption scored against the numbers of a different line, any line in the set | 11.4% (12.7%) | 11.7% (12.6%) |
| Same, but a neighbouring line of the same page-half | 16.7% (25.5%) | 16.9% (22.8%) |

The neighbouring-line control is the closest. Its best draw, 25.5%, is the highest of any control and is still far under 71.6%, but a wrong line on the same page scores 16.7% on average because the same words recur there. These were run on the strip reading above. The test half is not affected by the re-read described under "Edge check".

## The two readings
- **Whole-page.** Two models (Gemini 4 Argon, Gemini 3.7 Flash) each read a whole half-page. Disputed numbers were re-checked on the image. This reading misreads 8 as 0 (28 as 20, 18 as 10, 87 as 07).
- **Strips.** Each half-page cut into 5 overlapping full-resolution strips, read by Gemini 4 Argon and stitched (`scripts/strips.py`, `scripts/consensus.py`). The key was never shown to the reader. 258 half-pages use this read, 3 use an 11-strip read (19/100 p. 393L and 402L, 19/101 p. 202R) and 9 keep the whole-page read because the strip read failed a key-free count check. A blind read of two pages by Claude agrees with the strip read on 93.7% and 85.7% of numbers, against 91.0% and 80.2% for the whole-page read.

## Proposal, separate from the table (`proposal/`)
- **Method.** For each number without a value, its fit-half occurrences are dealt into two disjoint sets. Gemini 4 Argon proposes a value from each set alone. A value is kept only if both agree (`scripts/cloze.py`, `proposal/cloze.jsonl`). Four rows of `ADDITIONS.tsv` do not follow this rule and were added by hand: 295 (ekm) and 312 (hertzog), where the two sets did not agree (295: "eure koenigliche majestaet" against "euer kayserlich majestaet"; 312: herzog against hertzog), and 301 and 317, where the sets agreed on frankreich and koenig but I entered the clerk's spelling (franckreich, konig). The first two are my reading of the clerk's decryptions.
- **Check.** 62 entries of TABLE-C04 were hidden and run the same way. Both sets agreed on 58, and 53 of the 58 matched the table (`proposal/cloze_report.txt`).
- **15 fills and 6 weaker proposals** are in `proposal/ADDITIONS.tsv`. The fills and the hidden-entry check used the earlier reading of 19/102 (see "Edge check") and were not re-run on the corrected one. Two proposals disagree with the table: 210 viel (C04 wider) and 226 wur (C04 wer).
- **Out-of-range numbers.** Numbers under 14 (07, 02, 2, 8, 9, 11) in the whole-page reading were misreads of 87, 82 and similar. None is proposed.
- **Structure.** The word list 146-226 and the names list from 250 are alphabetical (95% and 99% of pairs in order, v-words before u-words). 227-249 is an unordered supplement.

## Edge check (19/102, added after review)
D. Bourdeau found that the lines I aligned for 19/102 p. 470L lack the first 7-8 numbers of each line. `scripts/edge_check.py` (output in `edge_check.txt`) compares each half with B. Dudout's blind cipher transcriptions of 470, 475 and 476 (`../training/`) and counts numbers per cipher line. Against the earlier reading it showed:
- **The cause.** 27 left-hand halves of 19/102 had been read from crops of the page image that were offset to the right. Their cipher lines lost the first 5-8 numbers, and the crop took in part of the facing page. p. 470L shared 50.7% of Dudout's numbers with the shared run starting at his 8th number (median start index 7, where 0 is his first number), 475L shared 11.4% (index 5), 476L 32.9% (index 7). Five of the 8 halves read as 11 strips were among them, and 4 of the 13 whole-page halves, all in 19/102. I did not trace why the crop was offset.
- **The fix.** I re-read those 27 halves from a standard half crop, 5 strips of 25% with 6% overlap, same model and prompt (`transcription/strips_recrop_19-102.jsonl`, raw reads) and replaced their rows in `p5_lines.jsonl`. Afterwards 470L shares 87.3% (index 1.5), 475L 67.8% (index 1) and 476L 56.2% (index 1) with Dudout's lines. I have not looked into the gap that remains on 475L and 476L. The median count of numbers per cipher line in the 19/102 left halves with at least 3 such lines is now 15-21, where it was 9-13.
- **What it changed.** 19/102 under TABLE-C04 goes from 47.7% to 60.3% (61.3% with the additions), and the fit half from 60.3% to 66.8%. Several of these halves are plain text (p. 510L is Latin) and the numbers the old reading gave them belonged to the facing page, so 19/102 now has 384 scored lines, not 510. The test half and the fresh lines contain no 19/102 line and did not change: 71.6% and 73.0%.
- **The other 11-strip halves.** 19/100 p. 393L, 19/100 p. 402L and 19/101 p. 202R were re-read the same way. Their numbers per line match the earlier read (median 28 against 27, 17.5 against 17.5, 16 against 18.5 on 3 lines), so I kept the earlier read. 19/100 p. 295L, which has short cipher lines, was re-read as a spot check and gave the same median (11.5).
- **Not redone.** The cloze fills, the hidden-entry check and the table of what failed below were built on the earlier reading of 19/102. They have not been re-run. No person has compared the new reads with the images, apart from the 470 comparison with Dudout's transcription.

## What did not work
- Pairing each decryption with cipher anywhere on its page (`scripts/align.py`): 60.9% against 62.1% on the whole-page reading.
- An 11-strip pass over 19/102 with a three-reading vote: 134 numbers changed, fit half 60.1% to 60.3%. (Some of this pass used the offset crops, so it says little.)
- An earlier set of 28 additions and a 64.7% figure are withdrawn. Their prompts showed test-half decryptions (found by D. Bourdeau, issue #696).

## Limits
- One reader family (Gemini) made the transcription. No person has read it against the images.
- The clerk's decryptions were re-read with the cipher, so the strip test has 415 test lines where the whole-page test had 422.
- 3.1% of numbers have no value under the table plus additions.
- The original key has not been found. Riksarkivet Chifferklaver (SE/RA/202) is not digitized.

## Reproduce
```
CIPHER_DATA=$PWD/transcription python3 scripts/evaluate.py ../table/TABLE-C04.json proposal/ADDITIONS.tsv
CIPHER_DATA=$PWD/transcription python3 scripts/edge_check.py
```
The reading scripts need the page images (Riksarkivet IIIF) and the `llm` CLI. `scripts/cloze.py` also needs `VERTEX_PROJECT_ID` set to your own Vertex project. The full pipeline, raw model reads and decode are at https://github.com/steps-re/dorffler-cipher.

Credits: TABLE-C04 and the layout of the code, Brice Dudout (Europe chiffrée) and Daniel Bourdeau. Transcription, test and proposal, Mike German (Steps Ventures). Tools: Gemini 4 Argon and Gemini 3.7 Flash (reading, proposals), Claude (code, blind check). Licence CC BY 4.0.
