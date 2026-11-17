# C06: TABLE-C04 + Mike German's additions, pre-registered, NOT measured (no fresh portion yet)

Status: in progress (table C06 frozen and its single measure pre-registered; no fresh glossed portion is digitised, so nothing was measured). Next step: obtain images of Oxenstiernska samlingen E 1109 / E 1110 (see below), then run `PREREG-C06.md` once.

## What is here
- `TABLE-C06.json` (SHA-256 7f6c2890…062f): `../table/TABLE-C04.json` unchanged + the 21 rows of Mike German's
  `german2026/proposal/ADDITIONS.tsv` (PR #742, commit ca0ee14b; copy `ADDITIONS-German2026.tsv`). 15 fills; 6 weaker
  values marked `_weaker`: 210 viel (accepted correction of "wider"), 226 wur (probable correction of "wer"),
  295 ekm, 301 franckreich, 312 hertzog, 317 konig. TABLE-C04 itself stays frozen as published.
- `PREREG-C06.md` (SHA-256 219a4d0a…33e3): one measure, written before any fresh portion was seen. Metric = German's
  "clerk's letters" (letters of the interlinear decryption reproduced in order by the decode, runs of 3+, no word
  boundaries: the lesson of C05); 200 shuffled-value controls; PASS = S >= 0.70 AND >= best control + 0.30 (why 0.70
  and not 0.85 is argued in the PREREG); >= 150 groups and >= 300 gloss letters; two blind transcription passes.
- `measure_c06.py`: the scorer. Self-test on spent page 19/102 img. 474 with German's transcription (no verdict):
  TABLE-C04 0.685, TABLE-C06 0.733, best of 200 shuffled 0.17 / 0.19.

## Why no measure
A fair test of the additions needs cipher with a contemporary decryption that neither TABLE-C04 nor the additions have
seen. There is none in the digitised material:
- 19/100-103: all 136 coded pages are in German's transcription; the fit half produced the additions and the test half
  was already scored with them (0.739). 474, 476 and 277/304 were spent by C03-C05.
- Series SE/RA/2115/I/19 has only volumes 100-103 (Riksarkivet open API and OAI-PMH, 17 Nov 2026).
- Dörffler's earlier volumes SE/RA/2115/I/12/60-62 (1667-79; IIIF R0003614, R0003598, R0003615): 12/62 checked on
  600 px thumbnails (about 210 of 1,065 images: every image from 1018 to 1064, then one in 3 to one in 8 across the
  rest of the volume, 1673-79): no numeric cipher seen. A sample can miss a short passage.
  12/60 and 12/61 not checked.
- Not digitised, and the best candidate: Oxenstiernska samlingen, Gabriel Turesson Oxenstierna af Croneborg,
  SE/RA/720701/III/03/E 1109 (1681-87) and E 1110 (1688, 1690, 1691), "Inkomna brev Dörffler, S." Letters from the
  same resident in the same years, likely in the same code. Also not digitised: SE/RA/2115/I/17/91 (letters to
  Anders Lilliehöök, 1674-80).

Credits: TABLE-C04, Brice Dudout and Daniel Bourdeau; additions, Mike German (Steps Ventures),
https://github.com/steps-re/dorffler-cipher. Licence CC BY 4.0.
