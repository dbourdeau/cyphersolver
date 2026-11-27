# sirdar1909: Sirdar (Wingate) to Herbert, Khartoum to Cairo, 9 Jan 1909 (catalogue 2907)

Durham University Library, Abbas Hilmi II papers, HIL/64/400. Promoted by the wave 16 Durham sweep
(research/sweep_2026-11-15_wave16_durham), which also listed the cipher/clear pairs of the same file used here.

## Key
Simple substitution, letters run together and regrouped in fives, a null at each end of a run. Built only on
HIL/64/402 = 403 (3 Jan 1909) and HIL/64/239 sheet 1 = HIL/64/118 (30 Nov 1908): `verification/build_v1.txt`,
`verification/key_v1.tsv`. Not reciprocal throughout, though many pairs are (a/p, b/m, c/l, d/k, e/y, f/h, o/t, r/x,
s/w). Unknown: cipher i, n, z. Clerks' variants: w written h once ("railway"); g and q confused.

## Held-out test v1 (tools/holdout, #1014 convention)
Manifest `verification/MANIFEST_v1.sha256`, SHA-256 a9259625e324fbb71b62a30cdb539d205924ce711ad488f30b64f02c0aafbccc,
frozen 2026-11-27 11:49:45 UTC, hash posted in the body of issue #1023 (created 12:03:41 UTC) before the run.
Held-out: HIL/64/240 = 119 (same telegram, sheet 2) and HIL/64/214 = 62 (26 Sept 1908), 301 signs, two blind passes
merged mechanically. Measured once, 2026-11-27 12:30 UTC:

**char 0.3051, best of 200 shuffled controls 0.2237 (mean 0.1115, z = 5.03, 0/200 at or above): NOT VALIDATED.**

Per run, for information only (not decisive, reported as announced in the protocol): 240 run A 0.75, run B 0.81;
214 0.17. The Nov 1908 runs decode as the clear copy apart from the blind passes' '?' and one clerk's k for o; the
Sept 1908 telegram does not decode at all. The risk declared in the protocol came true: 214 is in another alphabet. The
measurement does not validate the key; the passage is burnt and a new test would need a new passage of the
Nov 1908 - Jan 1909 alphabet (none other found in HIL/64-65 by the sweep).

## Reading
`reading_400.md`: "kindly wire me any remarks you may have to make", 10 of 10 words read as sense (5 sure, 5 probable).
Under the 300-character length of the read bar. Images not included (Durham's reuse terms not checked).
