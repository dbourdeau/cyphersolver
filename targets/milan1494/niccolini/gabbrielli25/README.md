# Gabbrielli key no. 25 (K_G25) tested on Niccolini's glossed letters, 1492-93: attempted, not read

Brice Dudout, working with Claude (Anthropic): Claude Opus 5.5 as main agent and as blind transcribers, edge marker and arbiter (separate sub-agents). Work of 14-20 Nov 2026, filed after #797, as offered there and accepted by Malcolm McBratney.

**K_G25 is not validated.** Four pre-registered stages (P02-P05) were run against the contemporary interlinear glosses of Niccolini's letters. Two could not be measured, one was below its size floor, and the one measurement (P05) failed its bar: 0.4987 against 0.85. It beats all 400 controls by about 0.18. So the key is probably related to Niccolini's cipher, but it is not his key as it stands, or the transcriptions are too noisy at 1272 px, or both.

**No decoding of the bare passages (catalogue 2380) is presented.** K_G25 was never applied to Malcolm McBratney's four blind transcriptions in `../blind/` (docs 42, 49, 81, 90), nor to any other bare passage. The only decodes in this folder are the measurement output of P05 on glossed letters, set against the chancery gloss. They are not a reading.

**No person has checked the transcriptions.** All the files here were made by AI agents.

**No images.** No ASF image, crop or derivative is included, and neither is the sign plate `CATALOGUE_F.jpg` (see below). The images are named and hashed in the frozen files.

## The key: K_G25 (`kg25/`)

- Source: P. D. Gabbrielli, *Chiavi delle cifre delle lettere ai Dieci di Balìa*, vol. 1 (ASF, 1863-64), key no. 25, headed "an. 1492, Alamannis (de) Petrus", from Carteggi dei Dieci di Balìa, filza 39. We read it on the Ilardi microfilm, reel 58, image 58-29, at Yale Dataverse (doi:10.60600/YU/XKVOWE). The image is not reproduced here.
- It is Piero Alamanni's key of 1492. It is not a key made for Niccolini, and it is not the 1494 sheet MAP LXXII 183 in `../../aaymeloglu/key.json`. The two were not compared sign by sign here.
- How it was built (14 Nov 2026):
  - Pass 1: the main agent wrote `KG25_passe1_principal.tsv`. Declared bias: that agent had read a summary of an earlier quick test, which compared our working table K_T with key 25 shape by shape. It did not open K_T itself.
  - Pass 2: a blind sub-agent saw only the images of the Gabbrielli sheet and wrote `KG25_passe2_aveugle.tsv`.
  - The two passes agree on column, rank and shape for every sign but one: the second doubled-consonant sign, mm (pass 1) or nn (pass 2). On the enlarged image it was settled as nn, with mm kept as the alternative (`doute` in the JSON).
  - The result was frozen as `K_G25.json` (sha256 `3a81cd6d1c12e14a70530b9a251c28e5162a8a99200f9b22f9dc15f1c2c41611`).
- Content: 39 shapes. a, e, i and o have 3 shapes each; c, h, l, m, n, r, t and u/v have 2; d, f, p, q, s and x have 1. There are four doubles (ll, nn, rr, tt) and et. The sheet has no b, g or z, no nulls and no name codes. The shape descriptions in the JSON are in French, as frozen.
- Neutral labels: the transcribers never saw K_G25. They worked from a plate of the 39 shapes cut from the sheet image, labelled F01-F39 with no values (`CATALOGUE_F.jpg`, sha256 `5cbd6f5e4a1320136c2064f3bed682d1380b0f890c7ae08bb593d5d8dc8fab0a`). The plate is a derivative of the Yale image and is not included. `MAP_F_vers_G.json` (sha256 `eb23f56e49f38193309403ac1b55587e171fe43a042ed843b5404a4a4ec1461e`) maps each F label to its K_G25 shape. With the descriptions in `K_G25.json`, that is all the plate carried. Signs that are not on the plate are written `X:<description>`, and code groups are written `K:<shape>`.

## The four stages

Every PREREG was hashed before any transcription of its portion and before any decoding. Each PREREG is in French, as written. The hashes are in the `*.sha256` files next to them. Bar for every stage: character agreement ≥ 0.85, and ≥ the best of the controls + 0.30, on ≥ 300 cipher signs (P02-P04) or ≥ 300 gloss letters (P05). If X: signs make up more than 20% of the tokens, the stage is inconclusive.

| Stage | Portion (ASF MAP LXXIV) | Blind transcriptions | Result |
|---|---|---|---|
| P02 (`kg25/PREREG-P02-KG25.md`, `a357769b…c6f0`) | doc. 78, pos. 329-331 | `P02_SIGNES_T2`, `P02_GLOSE_T2`, `P02_SIGNES_T3` | **not measurable**: 329 is in clear; only 15 F signs under a complete gloss ("lega col papa", "costoro et noi"). Nothing decoded. |
| P03 (`p03/PREREG-P03-KG25.md`, `04aba341…c41d`, script `measure_p03.py`; extension note `NOTE-EXTENSION-P03.md`) | docs 35, 36, 37, 59, 72, 81 c. 176r: pos. 158, 159, 161, then 167, 351, 254, 300, 299 | T2 (transcriber A), T3 (B, base pages only), A2 (extension) | **not measurable**: about 1,580 F signs, but only 86 under a complete gloss. Nothing decoded. |
| P04 (`p04/PREREG-P04.md`, `60fae8c9…14c3a7`, script `measure_p04.py`; amendment `AVENANT-P04-A1.md`) | doc. 97, pos. 443-444 (Milan, July 149?) | `P04_SIGNES_T2`, `P04_GLOSE_T2` (FINAL = T2 by the amendment) | **not measurable**: 32 runs and 1,065 F signs, but no run has a complete gloss (the gloss stops before the end of each line). Nothing decoded. |
| P05, plan B (`p05/PREREG-P05.md`, `0a17c250…6fec`, script `measure_p05.py`) | P04 + P03 runs with a partial gloss and a marked edge | T3 of 443-444 (B), edge marks for P03 (E), blind arbitration T2/T3 (A′, log `P05_ARBITRAGE.md`) | **failed**: 0.4987 (see below). |

### P05, the only measurement

- Metric: the legible fragments of each partial gloss (cut at the gaps, ≥ 5 letters) are aligned in order on the decode, at unit cost. Skips outside the fragments are free, so this is a local alignment. Agreement = 1 − total cost / total letters.
- Units: 39 runs, 778 gloss letters (doc. 97: 531; P03: 247), 955 F, 114 X and 18 K tokens. X share 0.105.
- The T97 filter removed 9 runs of 443-444 that overlap the 25 short sequences of 443 used for K_T.
- Result: agreement **0.4987**.
  - Key controls (200 permutations of the K_G25 values, seed 2380): best 0.3123, mean 0.2769.
  - Gloss controls (200 permutations of the fragment lists between units, seed 2381): best 0.3201, mean 0.2826.
  - Bar: ≥ 0.85 and ≥ 0.6201. **Failed.**
- Not decisive: doc. 97 0.537, P03 0.417, 443 0.531, 444 0.575, 299 0.506. Words of ≥ 3 letters found: 0.085.
- Blank runs on made-up data, frozen with the PREREG (`BLANC_P05.txt`): the right key gives 0.97; the right key with 15% of the tokens wrong gives 0.82; with 30% wrong it gives 0.75. Arbitration changed 78 tokens out of about 1,220, after 233 disagreements between T2 and T3 (about 19%).
- `RESULTAT_P05_brut.txt` is the script output. `python3 -I measure_p05.py --measure P05_SIGNES_FINAL.tsv P05_GLOSE_FINAL.tsv P05_BORDS_P03.tsv`, run from `p05/`, reproduces it byte for byte from this folder (sha256 `57eb3a8d…9d62`). The same holds for `measure_p04.py` and `RESULTAT_P04_brut.txt`.
- The portion is now used up: doc. 97, pos. 443-444, and P03 pos. 158, 159, 161, 167, 254, 299, 300, 351.

### Inputs from earlier work

`transcription/T_doc97_p443.txt` is the frozen P01 transcription of 25 short glossed sequences of pos. 443 (9 Nov 2026, sha256 `d958eefd…0925`). The P05 script reads it only to apply the T97 filter. It uses the older P01 sign notation and not the F labels.

The earlier P01 result was a working table K_T from the glosses of docs 6, 21, 32, 62 and 97, measured once on doc. 78, pos. 332: 0.698 against 0.85, best of 200 controls 0.138, not validated. It was reported on #797. Its files are not part of this PR.

## Hashes and paths

The `*.sha256` files are the records made at each freeze. Only their absolute local path prefixes were removed. Lines for the images and for `CATALOGUE_F.jpg` are marked `[not included]`. `SHA256SUMS.txt` lists every file committed here. Folder layout is kept, so the scripts run unchanged: they find `kg25/`, `p03/` and `transcription/` from their parent folder. Not included: the unfrozen draft of P04 and the transcribers' working folders (image crops).

## Credits

- Malcolm McBratney: the blind transcriptions of the four bare passages and the sheet S01-S67 in `../blind/` (#797). They are referenced here and not used: K_G25 was not applied to them. He left this pass to us on #797.
- Andrew Aymeloglu: the 1494 key `../../aaymeloglu/key.json`. Not used here.
- Key no. 25: Gabbrielli's manuscript at the ASF, read on the Ilardi microfilm (Yale Dataverse, doi:10.60600/YU/XKVOWE).

## Next, if anyone wants it

- Dieci di Balìa, Carteggi, Responsive, filza 39 (the filza Gabbrielli cites for key 25). It may hold deciphered copies of these letters. It is not online.
- A high-resolution reproduction from the ASF (more than 1272 px), to separate the shapes that the three transcribers kept confusing: F12/F16/F39 (6/b), F25/F26/X:9, F13/F01/F36, F27/F15/X:5.
- A K_G25′ could be drawn from where K_G25 misses on the used-up portion. That would be exploratory only, and it would have to be tested on new material.
