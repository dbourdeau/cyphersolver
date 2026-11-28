# PREREG C09 — lead 1561 (Philip → Ferrante Gonzaga, 25 Jun 1546, 14 Mar 1553, "16 Jun 1563"), 27 Nov 2026

Written and hashed BEFORE any decoding of our transcriptions. Nothing of the three letters has been decoded by us before
this file (the dry run of the scorer used token-shuffled copies of the files, see §6).

## 1. Frozen inputs (SHA-256)
- Transcriptions (two blind readers A, B per letter, shape names only, then shape-only arbitration; FREEZE-BLIND.sha256, FREEZE-ARB.sha256):
  - arb/1546_ARB.txt `3b2567b9165fffa217bc3661166d5aee52691ede1997247675e471702eace242` (23 lines, 545 tokens; A/B agreed on 0.892 of places)
  - arb/1553_ARB.txt `c94d262d4a36b4e0f410dfc388ba6de40aa8953bd072641bf2dfdb3bfef759c8` (64 lines, 1383 tokens; agreement 0.765)
  - arb/x_ARB.txt `3b96c3895f664790fef1b96359762a59405efa8ec06cdec79335f1ad5f0d4838` (30 lines, 878 tokens; agreement 0.712)
- Key: WAINUT's `targets/gonzaga1549/wainut/key.tsv`, origin/main 84dd1788e2, `47a2b2f313879e7b938a261a4391b015806ef245f417057afacf5f52ce36c651`
  (the Imperial Cipher of 1544-1554 as recovered by WAINUT). Used as is: bracketed values = hole.
- Name crosswalk atlas name → WAINUT name: CROSSWALK-C09.tsv `ca98efc068de361ea0b0c6af8d2632c0e284acacc5c59ad9644cad62cd8ab293`.
  Built before any transcription was read from the co-occurrence of names at the aligned places of the 14 Nov 1549 letter
  (project vs WAINUT, compare_readings.py), rule ≥ 0.6, plus 7 manual rows (one, `/`, added now; the others before the transcriptions).
  NOT mapped (count as holes): every `?class` of the glossaries, `#`, atlas-grammar names absent from the crosswalk, code groups
  other than dide/mus/quod/gien/em/gaces/pollo. Signs with dots below = cancelled (empty), WAINUT's own rule.
- Reference for 1553: Beling's working transcription of the Spanish enclosure cc. 37r-38r (`beling_march1553/spanish_enclosure.txt`,
  `9336d173241cbefe7092084c544681c05440cf98ecf3a1219200d9b4f019bc05`), split into 6 paragraphs exactly as in Beling's calibrate.py.
- Scorer: mesure_c09.py `a439100e0ea856c85af4e1a574456dd32c598ecf7962547d0fb7c8cf2f121c78`.

## 2. Held-out portion and metric
- 1553, PRIMARY: paragraphs 4-6 (our lines P40r-L08…L15, P40r-L16…L23, P40v-L01…L08; the blocks are fixed by the page layout and
  the '/' paragraph ends, see PARA_LINES), against the enclosure paragraphs 4-6 (865 letters; Beling's hold-out too).
  Metric: Levenshtein edits (Beling's normalisation and Distance), holes dropped. Paragraphs 1-3 reported as secondary only.
- 1546 and "1563": no clear exists. Metric: share of decoded letters covered by words of ≥ 4 letters of a Spanish lexicon
  built from the repo's clear readings of the same correspondence (list in the script; 1553 enclosure included, none of the
  three letters' own decodes).

## 3. Controls (≥ 200 required; 1000 each, seed 1561)
- Family K: the key's values shuffled among its labels (1000).
- Family O: the same decoded tokens in shuffled order (inside each paragraph for 1553; inside the letter for 1546/x), real key (1000).
  Family O was added after the dry run showed that a frequency-preserving text beats family K alone.

## 4. Thresholds (decided now)
- KEY CONFIRMED on a letter: zero ties or wins in BOTH families (rank 1/2001).
- 1553 progress claim: held-out edits < 621 (Beling's figure for WAINUT's single blind pass with the same key).
- No absolute threshold on 1553: the enclosure is a separate Spanish witness whose role (draft, extract, decipherment) is unknown.
- Reading by sense (Daniel's rule: 95 % of words SURE over ≥ 300 characters; sure / {probable} / [restored] / ‹unresolved› counted
  apart; a value taken from sense alone stays {probable}; for 1553, a word supplied from the enclosure is [restored], never sure)
  is done ONLY for a letter whose key is confirmed. A failed letter stays "decoded, not read".

## 5. Single measurement
`python3 mesure_c09.py <repo>/targets/gonzaga1549 <work_dir>`, run once; MESURE-C09.json kept as produced. No change to
transcriptions, crosswalk, key or script after the run; any later correction is an amendment and is not measured.

## 6. Declared risks
- The PREREG author knows key.tsv and saw the shape transcriptions (not decoded). The crosswalk was frozen before the transcriptions.
- The dry run used token-shuffled transcriptions (letters' token order destroyed); it decoded no real sequence.
- The reader instructions named some forms of this hand (ſ, theta, xo) from reader B's 1546 report, before the 1553 and x passes.
- The 1546 strips were cut by projection; the x strips by fixed peaks and one manual fix (P24v-L13…L15).
