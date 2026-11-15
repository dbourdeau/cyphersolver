# figueroa1534: second held-out measurement, cipher image 04 (15 Nov 2026)

A second single measurement under the same frozen rule as the image 06 one (`../README.md`), on AGS Estado
1379,14-18 (PARES 3615615), cipher image 04. **Image 04 was the last intact portion of this 1547 letter; it is now
spent.** Re-run both measurements from the parent folder:

    sh ../rerun.sh       # checks every SHA-256, regenerates both outputs byte for byte (Python 3.9.6 here)

## Result

| key | score | best within-class control (threshold plan) | margin | best whole-key control | outside the key |
|---|---|---|---|---|---|
| **K4** (the key of PR #621, unchanged, a456e5bb…) | **0.887** | 0.554 | **+0.333** | 0.504 | 13.8 % |
| K5 (K4 + 8 shape-split candidate labels) | 0.879 | 0.542 | +0.337 | 0.490 | 10.6 % |

530 tokens as scored, 200 + 200 controls, seed 744; thresholds unchanged (≥ 0.85, ≥ best within-class + 0.30,
≤ 20 % outside the key): both pass. The reference window picked by the alignment is the clear copy of image 13 from
« Yo desseo » (characters 2610-3530 of the joined clear file); it ends where the image 05 window of an earlier
measurement begins (« para tener a esta gente… »), so the two do not overlap.

**K5 is only a candidate.** Its 8 new labels come from Brice's answers to shape sheet 312d (lot 1553, no clear text).
Only 3 of them occur in image 04 (`Ꝉ°ᵖ` po ×15, `σ7` bo ×1, `+ᶜ` ce ×1): only **po** has real support; `Xᵗ` te,
`ɏᵘ` su, `ꞓʳ` cre, `ṅ` fa, `+ⁿ` ne were not tested at all. K5 decodes 35 more characters at 0.008 lower precision.
It is not used for any reading in this PR.

## Files (byte-identical copies of the frozen files)

| file | what | SHA-256 | frozen |
|---|---|---|---|
| `PREREG-AMENDEMENT-312d.md` | the amendment to the PREREG (French): K5, labels v5, the image 04 protocol, thresholds unchanged, declared deviations | a8d590dc…a645c | 15 Nov 00:54 CET, before any look at image 04 |
| `PREREG-AMENDEMENT-312d.sha256` | the freeze record as written, with its original paths (the PNG plates and Brice's answers are not included) | — | 00:54 |
| `img04_ARB.txt` [T_IMG04_ARB.txt] | image 04, arbitrated shape transcription: pass A (522), pass B (525), 70 % agreement, arbitration on the image (524 signs, 31 unread), three separate blind sub-agents, no values, no clear | 5c0651a0…ec72 | 01:31, before the clear copy was read (`T-IMG04.sha256`) |
| `clear_1547_ref_img04_joined.txt` | **our transcription** of the clear copy of the time: images 11-13 up to « Yo desseo » (read after 01:31) joined to the earlier transcription of image 13 from « Yo desseo » onward | eda0da63…f2f9 | used as read |
| `K4.tsv` | the key, as in `../K4.tsv` | a456e5bb…2ed6 | unchanged |
| `K5.tsv` | K4 + 8 candidate labels | 7c65d701…0657 | 00:54 |
| `score_atlas.py`, `score_k4.py` | the scorers, as in `..` | 21ed80a2…, 536a871b… | unchanged |
| `MESURE-312d-IMG04.txt` | the recorded output: 4 comment lines written at the time, then K5 (score_atlas, score_k4), then K4 (score_atlas) | aa9f8de4…1e3c | 01:39 |

## Declared deviation

The orchestrating agent had seen on screen about 200 characters of the clear image 13 from « Yo desseo », which the
alignment then picked as the window. It did no transcription of image 04: passes A, B and the arbitration were done
by three separate sub-agents that never saw the clear copy, the values or earlier transcriptions. The order of the
freezes rests on the contributor's local SHA-256 records and times. No AGS image or crop is included.
