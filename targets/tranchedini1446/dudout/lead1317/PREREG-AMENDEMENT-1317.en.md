# PREREG amendment no. 2: one measurement of the frozen R5318 key on a new letter of lead 1317 (14 Nov 2026, evening)

English translation of the frozen French original `PREREG-AMENDEMENT-1317.md` (sha256 d69aba41..., in `HASHES-1317.txt`).
The French file is the one that was frozen; this translation was made afterwards for the pull request and changes nothing.

Written and frozen (SHA-256 in `HASHES-1317.txt`) BEFORE any sign-by-sign transcription of the portion and BEFORE any decoding.
Seen so far: only the whole thumbnails (at most 1400 px) of ital. 1585 views 67-68 (f. 35 r-v) and 137 (f. 71), to see the layout.
Brice Dudout's go-ahead (14 Nov, evening); lead 1317 is reserved for him in this repository until 14 Dec.

## Key (unchanged)
`../nicodemus-r5318/R5318_crosswalk.tsv`, sha256 04c8ae96e8a4e1c625abf95414f6c89d10fb778ee2ed2bcbcf1aa784f01437c1
(frozen by `PREREG-AMENDEMENT-R5318.md`, sha 30c70fcc...; in this repository: `targets/tranchedini1446/r5318/key_R5318_by_1448_label.tsv`,
same values, comments translated). It has never seen f. 35: R5318 is an independent key sheet; the shape crosswalk was made on f. 28 only.
No change to the key.

## Portion (one only)
- **BnF ital. 1585 f. 35 recto** (Gallica btv1b52525947w, view 67, image rotated by -90 degrees), Tranchedini, Florence, 29 Feb 1448:
  **all cipher runs of the recto, in order**, first line to last.
- If the recto gives fewer than 300 cipher signs, all cipher runs of the verso (view 68) are added, in order; nothing else.
- Portion never transcribed or decoded by us nor (according to this repository, ital1584_copies_B.md) by anyone: intact.
- Not used here (stay intact): ital. 1585 f. 71 (1449, period decipherment f. 70) and ital. 1584 f. 353 (1447, copy f. 352).

## Reference
Later clear copy ff. 34r-v + 36r (views 65, 66, 69; "complete, no blanks seen" according to the lead). For each run of f. 35 the
reference words are taken from the copy by the clear words around the run on f. 35, BEFORE decoding, and written to
`texts/f34_36_reference.txt` (format `Rn: words`). A dash or blank of the copyist = `[—]` (no letters).

## Transcription
Labels of `sign_legend.md` (1448 table); shapes not in it -> `@Nxx`. Two passes: A (me) and B (a subagent that sees neither the
copy, nor the key, nor pass A); disagreements settled on the image (zoom), without looking at the copy or the key; result
`texts/f35_signs.txt`. Pass A is made without looking at the copy or the key (I read the copy only after the settling, for the reference).

## Measurement (one only): `measure_f35.py` (sha in HASHES-1317.txt)
- Decoding: R5318 value of each label (multiple values `x|y`: the first); a label absent from the key -> nothing.
- Normalisation (as in PREREG.md): lower case, letters only, v->u, y->i, j->i, h dropped, doubled letters simplified.
- Score = 1 - sum Levenshtein(decoded run, reference) / sum of reference lengths.
- Controls: 200 keys shuffled inside classes (lower-case labels = letters/syllables; UPPER-CASE = word signs), seed 5318.
- Thresholds: **read** if score >= 0.85 AND score >= best control + 0.30; **partial** if only >= best control + 0.30; otherwise **failed**. z reported.
- After the measurement, f. 35r (and v if added) is burnt for this key.

## After the measurement (only if "read")
Reading of the letter (f. 35 r-v), strict word count as in this repository: sure / {probable} / [supplied] / <unresolved>; >= 95% = read.
Otherwise: the figures are reported, no reading is claimed.
