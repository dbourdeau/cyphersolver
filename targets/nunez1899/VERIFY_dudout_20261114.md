# nunez1899: independent check of the key (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/nunez1899` reads only `key.tsv` and `transcription_9926.txt` (not `scripts/decrypt.py`).
22 lines; 65 code tokens (the two-word code *garlopas abocados* = E.U. taken as one code each time); 1 code word without
value (*ampida*, L06). Every line is identical to `decryption_9926.txt`. Key correction: none.

## Scan (CEHM CDLIV.1a.1883.38.9926.0002, public JPG)
L04 word 8 "curadela" (= CANTIDAD), under the pencil docket "Hacienda": the visible strokes agree with c-u-r-a-d-e-l-a;
the d and e stay uncertain, as noted. L20 "pareciendo.." (under the CEHM watermark) not re-read.

## Read bar (README)
The recorded 0.933 (111 of 119 words; {+de} x2, {+aquí}, {+empréstito}, {+en}, {-te se} and [?depositen] not read) follows
the README rule. `research/reading_audit/v10_relabel.measure` gives 0.990 on `reading_9926.md`: `v2_score.holes` does not
treat the `{+x}` and `{-x}` markers as holes. A run of `v10_relabel.py --apply` would move this document to "read"
wrongly.
