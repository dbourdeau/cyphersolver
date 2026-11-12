# Adjudication rule for the read-share statement (fixed and frozen before the adjudicated text was decoded)

1. Transcription: `transcriptions/adjudicated.tsv`, built by `scripts/adjudicate.py` from the three-way sign alignment
   (`scripts/align.py`, `alignment/three_way_signs.tsv`). Majority column: each reader-1 sign takes the KEY_B label that
   at least two of the three readers give, each reader mapped by their own frozen mapping (reader 2 `reader2_mapping.md`,
   reader 3 `reader3_mapping.md`, both written before those readers decoded). No post-hoc mapping corrections
   (reader 3's own later finding that its Z is reader 1's S is NOT applied). L/l (both s) and S/h (both k) are merged
   because the key gives them the same value. No agreement: `?`. Unanimous column: all three must agree.
2. Unit division and the three code numbers are reader 1's (103 units).
3. Decode once with `key_B.txt` (unchanged; md5 224da5d5d7fea3c20ef63e1efe655b2e).
4. Label each unit mechanically, no judgement after decoding:
   - code number -> E;
   - decode contains `?` (no agreement, or a sign with no key value) -> N;
   - decode equals a form in `transcriptions/s_forms.txt` (forms judged S by any reader before this step) -> S;
   - anything else -> E (decodes fully but is not a form any reader judged a word; listed, never promoted).
5. Read share = S/(S+E+N). Reported beside, never instead of, the three readers' own figures.
