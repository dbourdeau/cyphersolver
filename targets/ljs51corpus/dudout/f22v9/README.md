# LJS 51, f. 22v l.9-13 + 23r l.1 (chain 22v.9): shape-class re-transcription and held-out key test

Contribution by dudout (Brice Dudout, with Claude). Images: University of Pennsylvania, LJS 51, OPenn (Penn IIIF, 2343 px; f. 22v = canvas 50, f. 23r = canvas 51).

**Result: capped (not validated).** The frozen criterion was missed, but there is a clear signal above the controls in the primary test. No key is claimed.

## Prior work

`targets/ljs51corpus/keys_eye/22v.9.json` (Daniel Bourdeau, origin/main d8ac608093) gives a by-eye key, "not keyed". It has 40% letter and 45% skeleton consistency, while the sign count and the repeated runs fit the compiler's plaintext. Daniel suggested a 2-3x sign-by-sign pass in shape classes. This contribution is that pass, followed by one frozen test.

## What was done

1. **Blind transcription.** Two Opus sub-agents transcribed the cipher in shape classes from the images only, without the plaintext or Daniel's JSON (`A.txt`, `B.txt`).
   - Agreement was 74/81 signs strictly (91.4%), or 78/80 (97.5%) once the labels were matched.
   - The arbitration is in `arbitrage.txt`: 81 signs, 22 classes. The arbiter had seen the plaintext; this is declared.
2. **Freeze.** `PREREG_v1.md`, `procedure.py` and the data were frozen with `tools/holdout/freeze.py` (PR #1014) at 2026-11-28T14:30:38Z.
   - `MANIFEST_v1.sha256` = `3541c57c54128b4e031e030d4138d49f52dbc43371a80ddfb58723b4efbbf80b`.
   - The hash was posted on #1023 at 14:35:23Z, and the measurement started at 14:35:39Z.
3. **One measurement.**
   - Method: a gapped hard-EM sign-to-letter alignment that allows homophones, null signs and dropped letters. It learns a key on one half and decodes the other half. The score is LCS / held-out letters, against 200 controls that run the same procedure with the training plaintext shuffled.

| Test | Variant chosen (training half only) | Score | Best control | Mean control | Coverage | Pass |
|---|---|---|---|---|---|---|
| Primary: learn signs 1-40, test 41-81 | plain order, no separate hamza, word 1 = بني | **0.692** | 0.359 | 0.231 | 0.83 | no (< 0.85; margin +0.33 is met) |
| Inverse (declared): learn 41-81, test 1-40 | plain order, word 1 = لبني | 0.488 | 0.350 | 0.250 | 0.78 | no |

The primary decode of signs 41-81 is `انبﻻمارا?ال?اامل?ب?وال?ومعندو?ولذالك?دنذر`. The compiler's text is `لبنيﻻخبارالشاملشوقوالصومعندوصولذلكقدنذر`.

In the primary test the score beats all 200 controls by more than 0.30, so the plaintext is the right text and the cipher is essentially a substitution. However, 40 training signs do not reach the 0.85 threshold. The PREREG declared this power limit in advance: on synthetic data of the same size, a true key reached 0.85 in only 3 of 10 trials.

## Exploratory observations after the measurement (whole text, NOT validated)

Both halves have now been measured, so nothing below can be tested again on this chain. Files: `measurement/post_full_alignment.json` and `measurement/post_reading_sheet.txt`.

- **Class S1 (the dotted hook with a descending tail) is a hamza sign.** It falls on أثبتك (sign 31), أعتذر (36) and الشآم (53, ء before alif S10). It also starts both copies of the first word (signs 1 and 41), where the compiler writes ل. This fits the compiler's note on 23r l.2-3, "the hamza is other than the alif". It also suggests that the cipher's word may be أبني and not لبني; we leave that open.
- **ذلك is enciphered twice as ذالك**, with an extra alif sign S10 (signs 25-28 and 73-76). This is a plene spelling, and a candidate for the "error" the compiler mentions ("وقد خبط فيه").
- **The teeth letters share signs.** S3 covers ب ي ن و, and S6 covers ت ث ن. Over the repeated classes, the alignment's consistency is 0.795 at letter level and 0.877 at skeleton level, against Daniel's 0.40 / 0.453. This is a self-fit, which inflates it.
- **Reading sheet (Daniel's 95% rule):** 10 of 21 words are sure, 4 probable, 1 restored and 6 unresolved, so the rule is far from met. No reading is claimed beyond the compiler's own plaintext.

## Files

- `A.txt`, `B.txt`, `arbitrage.txt`: transcriptions. `clair_23r.txt`: the compiler's plaintext.
- `PREREG_v1.md` (in French), `procedure.py`, `MANIFEST_v1.sha256`: the frozen material.
- `measurement/result.json`: the measurement, with all 200 control scores for each test.
- `measurement/post_*`: the exploratory analysis made after the measurement.
