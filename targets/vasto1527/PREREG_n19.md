# PREREG vasto1527 / no. 19 ff. 41r-42r — held-out check of Lasry's Cipher 2 letter key (14/11/2026)

Written BEFORE any scored decoding of the portion.

- Portion: no. 19 (BnF fr. 3022 ff. 41r, 41v, 42r; Gallica btv1b90601558 views 80-82), cipher passages, as transcribed in
  n19_transcription.txt, SHA-256 96471b9ad1e08465bf815aa0480fd1ce1592400b11f71396e6f67e94b55c1bff (612 space-separated groups).
  Lasry's published decryption stops at f. 40v; no part of ff. 41r-42r served his key or this project's code values.
- Key: Lasry's Cipher 2 letter key as published (prior/BnF_fr3022_f16.png), letter forms only, unchanged; his two-per-syllable
  signs and nomenclator groups are taken as fixed labels and are NOT scored. Glyphs absent from his key image are mapped as his
  own decryption reads them (exercito x-glyph -> x; crossed z in "dezir" -> n, as his 17vb "deni r").
- Metric: share of letter-only words (groups decoded wholly from letter signs, length >= 2) found in the repository Spanish
  lexicon lang/lexicons/es.json.gz, after j->i, v->u, y->i, ç->c, doubled letters kept.
- Controls: 200 keys made by shuffling the 21 plaintext letters among Lasry's 21 letter classes (homophone grouping kept),
  random.Random(20261114). Same metric.
- Threshold (fixed now): PASS if real >= 0.50 AND real >= best control + 0.30. Otherwise FAIL. One measurement only.
