Status: read in part (Brice Dudout, 12 Nov 2026: system B key rebuilt from the 5 Oct 1764 contemporary clear and validated on 328 held-out groups, 0.563 vs 400 controls max 0.083; 121-124L about 70% of word tokens sure or probable).

# duben1764 / dudout: system B ("Chiffer n:o 2"), catalogue 450

Brice Dudout, with Claude Opus 5.5, 12 Nov 2026. Builds on Daniel Bourdeau's transcriptions (tx/c1764-10-05.txt,
tx/p1764-10-05.final.txt, tx/c-chiffer2-121-124.txt) and on our system A work (issue #437, key_c01).

## Extent of system B and its contemporary clear

| Images | Content | Contemporary clear |
|---|---|---|
| 118R, 119L, 119R (5 lines) | Düben to the King ("Sire Votre Majesté"), St Petersburg, 5 Oct 1764; 821 groups | **Yes: image 120** (whole letter) |
| 121 | 31 Dec 1764 v.st.; to "mon cher Comte" (see 122L) | No (the faint grey marks between the lines are show-through from the verso; no legible gloss) |
| 122L, 122R, 123R, 124L | continuation (no date seen); 122R has one sentence in clear, "Je Vous conjure, mon cher Comte, ..." | No |

121-124L hold 1,247 groups with no contemporary decipherment, so the outcome is not "existing decipherment".
124R-126 are system A (catalogue 1616, issue #437).

## The 5 Oct 1764 clear on 120 is the decipherment of 118-119

NOTES says the 120 text is a draft, not a decipherment, and that "repeats do not line up". They do line up:
the repeats of the cipher fall where the clear repeats a word, at the same relative position.

| Cipher run | Positions in cipher | Clear | Positions in clear |
|---|---|---|---|
| 155.453 | 0.36, 0.52, 0.90, 0.97 | Votre Majesté | 0.34, 0.52, 0.93, 1.00 |
| 403.240.709 | 0.21, 0.73 | dispositions | 0.21, 0.74 |
| 126.54.133 | 0.10, 0.52 | les interets | 0.11, 0.52 |
| 215.9.549.317 | 0.07, 0.14, 0.39 | que j'ai | 0.07, 0.14, 0.38 |

The earlier mismatch came from reading 215.9.549.317 as "Votre Majesté".

The system is a **fixed** two-part syllabic nomenclator with homophones. Some values:
- letters and syllables: 614 n, 119 r, 354 e, 712 u, 133 s, 136 de, 410 re, 709 si, 132 vo, 640 tre;
- whole words: 453 majesté, 155 votre, 54 interet;
- 549 marks the apostrophe (que 9 549 317 = que j'ai; 614 549 317 344 = n'ayent; 736 549 604 607 = qu'elle);
- 9 = j. Groups under 100 are **not** all nulls (54, 9, 4 os, 20 ter); 3 is a null.

It is unrelated to key_c01 (system A) and to the tables at 218-220.

## Key and the single measure

- **Build.** The key was built on 118.00-119L.06 only (493 groups) against the 120 clear. We used anchored EM alignment, the method of key_c01:
  - a ±30-letter band around 10 checkpoints, all in the build part;
  - 26 hand-anchored values;
  - script `scripts/align_cp.py`.
  - The result is `key_systemB_c03.json`: 171 values, 8 long low-count strings set to unknown by a rule fixed beforehand.
- **Held out.** 119L.07-119R.05 (328 groups) was never used to build the key. We checked it on the full-resolution image without the key: no disagreement with Daniel's transcription.
- **Preregistration.** `frozen/PREREG.md` (French, SHA-256 in `frozen/SHA256SUMS-PREREG`; paths there are those of our working dossier) was frozen before the measure. It fixes:
  - the measure: share of the clear (from the end of the build alignment) covered by common blocks of 4 letters or more, using difflib;
  - 400 controls: 200 permuted keys and 200 shuffled orders of the held-out text;
  - the thresholds: M ≥ 0.35, M above every control, and a margin ≥ 0.15.

| | Value |
|---|---|
| Held-out groups / known to the key | 328 / 255 |
| **M (real)** | **0.563** |
| Permuted keys, max / mean | 0.083 / 0.043 |
| Shuffled text, max / mean | 0.076 / 0.044 |
| Margin over the max control | 0.480 |
| Verdict | **validated** |

The held-out decode runs past the end of the 120 clear with the closing formula
"le tres [humble] et tres ob[eissa]nt ser[vite]ur", which the clear page omits (`measure_result.json`, field D).

## Reading of 121-124L (no contemporary clear)

- **Coverage.** The measured key knows 1,032 of the 1,247 groups (82.8%; `decode_121-124L_frozen_key.txt`).
- **Extension.** 25 values were then added from the context of these pages, after the measure and not measured separately (`key_systemB_c03b_additions.json`). They raise coverage to 1,130 groups (90.6%; `decode_121-124L_extended_key.txt`). Some of them:
  - 290 Comte and 20 ter (twice "du Comte Os-ter-ma-n");
  - 217 vous, 116 sa, 129 pour, 733 lui, 224 is, 101 nu, 121 ble, 792 lettre, 325 pas, 526 est.
- **Reading.** `reading_121-124L_fr.md`, with English in `reading_121-124L_en.md`.
  - A mechanical count of the word tokens gives 442 sure and 77 probable out of 744, about 70%. That is under 95%, so the state is **read in part**.
  - About 105 values (215 groups) stay unresolved; most of them occur once or twice.
- **Content.** Düben writes to "mon cher Comte" (Gyldenstolpe) on:
  - the King's orders about Count Osterman (the Russian minister in Stockholm) and the marks of the Empress's favour sought for him;
  - the Empress's support for the King's interests at the coming Diet;
  - his own failure to obtain more ("ce n'est assurément pas ma faute");
  - the little confidence shown him. He asks that his letters be returned to him on his return.
- **Points for you:**
  - 523 reads "a" here (l'arrivée) and "na" in the build.
  - 366 ("to" in "tout") was mis-cut as "betou" in the build key; corrected only in the extended key.

## Files

- `key_systemB_c03.json`: the measured key, frozen.
- `key_systemB_c03b_additions.json`: the 25 post-measure additions.
- `key_systemB_c03b_extended.json`: the measured key with those additions.
- `frozen/`: PREREG, SHA-256 list, checkpoints, anchors, build and held-out transcriptions.
- `measure_result.json`: the measure output.
- `scripts/`: aligner, measure and decoder.
- `decode_1764-10-05.txt`: the whole 5 Oct cipher decoded with the extended key (96% of groups known).
- `decode_121-124L_*.txt`, `reading_121-124L_fr.md`, `reading_121-124L_en.md`: decodes and reading of 121-124L.

## Not done

- No independent transcription of 121-124L; Daniel's is used as is. We checked only lines 121.01-04 and 121.10-12 against the image, with no disagreement.
- The 25 post-measure values are not validated by a second held-out text, since none with a clear remains.
- No images are included. They are Riksarkivet's, Public Domain Mark per the IIIF manifest.
