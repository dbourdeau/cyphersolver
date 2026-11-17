# Corroboration plan, catalogue 1637 (written before any helper is asked)

Written 16 Nov 2026 by the packaging AI agent, before viewing the chosen images and before asking the helper.

## Purpose
The claim "the letters of the supposed cipher series are in clear" rests on one pre-set test letter (image 040)
and one screening pass. This adds a second, independent sample.

## Choice of images (seeded, fixed now)
Pool: images 039-059, 067-068, 080-081, 085-088, excluding 040 (28 images).
`random.Random(1637).sample(pool, 3)` (Python 3.12) gives 086, 050, 043. Sorted: **043, 050, 086**.

## Preparation
Each image is a two-page spread. Each is cut into its left and right halves at full resolution and reduced for
viewing; any half judged upside down from a thumbnail (orientation only, no reading) is rotated 180 degrees. The
helper also receives a note that it may rotate any image itself if the text still looks inverted.

## The helper
ONE helper reader (Opus, medium effort). It is told nothing about the file, the catalogue, any key, our earlier
finding, or what we expect. It is given only the image crops and this question, for each image:
1. Is the writing alphabetic handwriting in a known script, or a cipher / symbol script?
2. If alphabetic: which script and which language?
3. Transcribe the first five lines of the main text (mark illegible words [...]).

## What counts against our finding
Any one of the three images judged cipher or symbol script (in whole or in a passage of the main text) counts
against the finding "no letter contains cipher". If that happens, packaging stops and the result is reported.
Answers are reported as they fall, without re-asking or re-tuning.
