# How the key was built from the chancery's glosses

No key sheet survives for this code in what we saw. The Danish chancery deciphered most of Petkum's letters between the lines; the letters in this folder are the ones it did not (no interlinear writing on the film). The key was read off the glossed sister leaves and then applied, unchanged, to the bare letters.

| file | what it is | when fixed (UTC, 12 Nov 2026) |
|---|---|---|
| `KEY_v1_gloss_377_401.tsv` | v1: values read under the glosses on images 377 (27 Jan 1665) and 401 of unit 261267, one gloss example per value in the source column (tier A), plus the row rule (tier B: syllables in rows of five, a e i o u, on consecutive numbers) and one-anchor rows (tier C). md5 f1b15343 | frozen 01:29:32, before the 573 transcription was decoded |
| `KEY_v2_additions_574R.tsv` | 17 additions read from the glosses on image 574 right (the relation of 10 Dec 1665), tier A2: U4 = x, HB = z, 61, 165, 116 and other code words | seen after p.2-3 had been decoded; used for the held-out pages only |
| `KEY_v2.tsv` | v1 + those additions. md5 20ddf240 | frozen 01:35:14, before pp.1 and 4 were transcribed |
| `../key.tsv` | KEY_v3 = v2 with one correction: code 51 is 'le Roy de Danemark (V. M.)', not 'la France' (our misreading of the 401 gloss; 574 right reads 'V. M.'). md5 ddc02e4a. The key of every count in this folder except A1 | 01:37 (b94 LOG); first stamped 01:43:29 GMT |
| `rowrule_check_574R.tsv` | 17 values predicted by the row rule before 574 right was read, then met under its glosses: 17 agree, 0 contradict | after v1 |
| `paulmyer_gloss_checks.tsv` | glosses on Paulmyer's own leaves (unit 261294) against KEY_v3: same code; nothing taken from them | 12:20 to 12:37 |

Tiers in `key.tsv`: 84 rows A, 17 A2, 46 B, 8 C (155 rows). The decoder prints A2 values as `(x?)` (it tests `tier in 'AB'`), and the shuffled-key control neither scores nor shuffles them; the counter treats them like A. This display quirk is the contributor's and is kept so that the decryptions stay byte-identical to the ones stamped.
