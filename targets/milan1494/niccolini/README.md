# Niccolini's bare cipher passages, MAP LXXIV docs 42, 49, 81, 90 (catalogue 2380): attempted, not read

Siblings of the Milan embassy cipher, added here as agreed on issue #589 (16 and 18 Nov 2026). Malcolm McBratney (Brisbane), working with Claude (Anthropic): Claude Fable as blind reader, Claude Opus as decoder and as a separate judge.

**No person has checked the transcriptions.** They were made by an AI model from the ASF images listed below.

## Result (first blind pass, figure of record)

| Doc | Leaf, date | Cipher signs | Strict judge (word units) | Shuffle, seed 20261112 / 7 (>= real, of 5,000) | Class |
|---|---|---|---|---|---|
| 42 | c. 90r, Pavia 3 Aug 1492, postscript | 95 | S 16, E 1, N 9: 16/26 = 61.5% | 0 / 0 (real 0.5217, max 0.4747 / 0.4673) | below our 65% line: attempted, not read |
| 49 | c. 104r, Pavia 20 Aug 1492, one line | 20 | S 0, E 1, N 4: 0/5 = 0% | 14 / 10 (fail) | not read |
| 81 | c. 177r, 21 Dec 1492 (place abbreviated "Vig." [unverified: Vigevano]), one line | 38 | S 4, E 0, N 4: 4/8 = 50.0% | 0 / 1 (real 0.6000) | not read |
| 90 | c. 200r, postscript sheet, Jan 1493, one line | 24 | S 2, E 1, N 3: 2/6 = 33.3% | 158 / 139 (fail) | not read |

All four are below our own 65% line, so none is filed as a reading. Doc 42 decodes into Italian in places (judge's gist: "el re di Francia ... dal governo [22] ... et il re ... e apto ad governare lui per non ..."), and its shuffle control passes (0 of 5,000 at both seeds), which suggests the 1494 sheet is close to the 1492 key but not the same in every sign. Doc 81 is the same on a smaller scale. Docs 49 and 90 are too short for the control.

## Method (declared in `FREEZE_PLAN.md` before any result)

1. Key: `../aaymeloglu/key.json` (main, sha256 abf087fb7f1176113e58cceea3c0731686b7cbcc5e6b81a17ffc4c16004cc89a), the Milan embassy sheet MAP LXXII 183 of 1494, unchanged. Applying it to Niccolini's letters of 1492-93 tests whether the same key served; a Niccolini-specific key (from his glossed letters in this filza) was not built.
2. Images: ASF IIP server, region crops of A0000183 (doc 42), A0000209 (49), A0000357 (81), A0000403 (90), captured in Malcolm's browser on 19 Nov 2026 (`FETCH_MD5.txt`; images not committed). Viewer pages: [81477](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=81477), [81503](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=81503), [81651](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=81651), [81697](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=81697).
3. Blind sheet: neutral labels S01-S67 with shape descriptions only (`blind/SHEET.tsv`, built by `scripts/build_sheet.py`); the label-to-key map `sheet_to_key.tsv` was kept out of the reader's folder. The reader saw only the sheet, `blind/BRIEF.md` and the eight crops.
4. Blind transcription frozen 2026-11-19T01:03:11Z (`blind/FREEZE.txt`), then decoded once (`scripts/decode_once.py blind > decode_once.txt`, reproduces byte for byte).
5. A separate judge (`judge/JUDGE_BRIEF.md`) saw only the decode and the clear words around each run: `judge/judge.tsv`, `judge/JUDGE_NOTES.md`.
6. Shuffle control: `scripts/shuffle.py blind <wordlist>` (dictionary cover, letter values permuted among signs; word list of Ariosto and Dante not committed, md5 083a93d9885337306f524c2b188bf6a5), output `shuffle_out.txt`.

The main session captured the images and knew the key; it did not transcribe or judge.

## Known limits
- The reader flagged several signs as off the sheet (NEW1-NEW3) and some doubtful pairs; and in doc 42 L2.3 and L4.2 it was unsure whether the first signs are clear abbreviations (`blind/READER_NOTES.md`).
- The judge counted each unreadable leftover string as one N unit, so N is on the low side.
- Prior art (`PRIOR_ART.md`): no reading of these passages found (catalogue 2380 vetting; Desjardins prints other Niccolini despatches only). Specialist literature not searched.

## Next, if anyone wants it
A key built from Niccolini's own glossed letters of 1492-93 (docs 6, 21, 32, 35-37, 59, 62, 72, 78, 81 c. 176r, 97), then a declared second pass on doc 42 and 81.
