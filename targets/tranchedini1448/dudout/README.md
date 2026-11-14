# Tranchedini 1448 table: learnt on BnF ital. 1585 f. 28 (with f. 27), held-out test on f. 30 (with f. 29) — issue #616

Brice Dudout, with Claude Opus 5.5 (14 Nov 2026). Lead 1317 (Nicodemo Tranchedini to Francesco Sforza, Florence, 1447-49).
Images: Gallica, BnF italien 1585, ark:/12148/btv1b52525947w, views 52 (f. 27), 54 (f. 28), 56-57 (f. 29), 58-59 (f. 30).
Source gallica.bnf.fr / BnF. No image is included here.

The clear leaves ff. 27 and 29 are 18th/19th-century copies that already give the plaintext (with a dash where the copyist
could not read a sign). So nothing here is a new reading of these two letters: the contribution is the **1448 key table**
learnt from the pair, its **held-out test**, and the two **tests on the 1446 letters** that #616 asks for.

## Protocol (frozen before the test; `PREREG.md`, hashes in `HASHES.txt`)

1. **f. 28 transcribed twice** with the sign labels of `targets/tranchedini1446/texts/f134_signs.md` / `f139_A.md`
   (shape names; `texts/sign_legend.md`): pass A aligned by hand with f. 27 (`texts/f28_passA.txt`), pass B by a subagent
   that saw neither f. 27 nor pass A (`texts/f28_passB.txt`); settled on the image at 3-3.5x (`texts/f28_signs.txt`,
   9 runs, about 240 signs).
2. **Table** = majority of the settled values per label (`build_table.py` → `table_1448.json`, 65 labels with a value),
   frozen by SHA-256 before the measurement.
3. **f. 30 transcribed blind** (a subagent that saw neither f. 29 nor the table; `texts/f30_signs.txt`: 13 runs,
   846 signs, recto and verso; 29 shapes not in the legend labelled `@N01`-`@N34`). Reference words for each run taken from
   f. 29 by the clear words around the run, before decoding (`texts/f29_reference.txt`).
4. **One measurement** (`measure_f30.py` → `results/results_f30.json`): decoded runs vs reference, letters only (v=u, y=i,
   h dropped, doubles single), score = 1 − Levenshtein / reference length; 200 tables shuffled within classes
   (letters / nulls / word signs), seed 1448.

## Result on f. 30 (held out; above the 300-sign bar)

| | value |
|---|---|
| cipher signs / runs | 846 / 13 |
| signs with a 1448 value | 655 (77.4%) |
| **score (character agreement with f. 29)** | **0.650** |
| 200 shuffled tables | mean 0.201, sd 0.041, best 0.283 |
| z | 10.9 |
| verdict (thresholds of `PREREG.md`) | **partial**: above best control + 0.30, below 0.85 |

The decoded runs read as the copy, with holes where f. 30 uses signs that f. 28 does not have, e.g. R13
`cosimo··straintendersionissi·ma·i·a·oss·ressio·delivenetianietrecerli…` for "Cosimo mostra intendersi benissimo maxime a la
oppressione de Venetiani, et redurli…", R11 `…vedera·ro···dochecosimocevenghaet·strar·vichecetissaqvalcheco··chelavsse·ssiintendere`.
What is missing is mostly shapes absent from the short training slip (`@N03` trefoil, `@N18`, `@N20`, `@N15` …, `NON`, `dd`),
not wrong values. f. 30 is now burnt for this table.

## Test 1 — the f. 134 gloss signs (1446)

- **Fiorentini (V with a small circle on each top corner): same sign, same value in 1448.** On f. 28 it stands where f. 27
  has "li Fiorentini"; in the held-out f. 30 it occurs once (R4) and decodes "li fiorentini" against the copy's "de' Fiorentini".
- **stantie (bent F with a foot): not found** on f. 28 nor on f. 30 (the f. 30 reader looked for it). The nearest shape,
  `@N19` (bar with a bent foot crossed by a stem), stands where f. 29 has "pur(che)" and "re-pu-tacione", i.e. *pu*:
  not stantie. **Test 1 cannot pass for stantie: no 1448 witness.**
- Also: the bar-o-bar-o sign, glossed *duca* on f. 134 (Daniel's reading), is **Venetiani** in 1448: f. 28 "li Venetiani";
  f. 30 six times, every time where f. 29 has "Venetiani". The double comb (*non*) does not occur on f. 28, so it has no
  1448 value (it is on f. 30). The Ш sign (Domnina *in*) stands for "come" on f. 28 (one use).

## Test 2 — f. 139 (1446) with the 1448 values (`test_1446.py` → `results/results_f139.json`)

Labels of Daniel's `texts/f139_signs.txt` crosswalked to the 1448 labels (`sign_legend.md`, column f139). Scored like
`table_test.py`, but with `it-cinquecento` **order 4** without spaces (the order-5 cache was not available offline;
Daniel's own values are rescored with the same model so the two lines compare):

| | 1448 table | Domnina/Lasry table + duca, Fiorentini, l (Daniel) |
|---|---|---|
| coverage of f. 139 tokens | 62.1% | 61.6% |
| letters scored | 516 | 443 |
| per letter | −2.209 | −2.320 |
| 200 within-class shuffles | mean −2.795, z 4.3 | mean −2.977, z 3.6 |

Of 40 label types valued in both tables, 34 have the same value (a, a', ce, co, de, e, g, h, i, l (@12, @102), li, mi, n, no, o,
pi, q, r, re, ri, ro, s, ss, t, ta, te, to, u, CHE, CON, ET, Fiorentini); 6 differ: IN (in / come), SFORZA (sforza / la V.S.),
VENEZIANI (duca / li Venetiani), o' (o / ti), r' (r / ra), si (si / so). So the 1448 key is of the same family and gives
f. 139 slightly better Italian than the later tables, but no more of it (coverage is the same).

## Decision rule (written in `PREREG.md` before the test) and outcome

"Join one entry" needed: test 1 passed for both signs AND, on f. 139, z ≥ 3, per-letter score ≥ −2.149 and coverage ≥ 62%.
- Fiorentini: pass. stantie: **no witness** in 1448 → not passed.
- z 4.3: pass. Coverage 62.1%: pass (just). Per-letter −2.209 vs −2.149: **not met as written** (the −2.149 was Daniel's
  order-5 figure; with the same order-4 model the 1448 values beat his table, −2.209 vs −2.320).

**Outcome by the rule: the 1448 table does not read f. 139; it is a neighbour's key** (same family, 34/40 shared values),
and lead 1317 should get its own target. The bar-o-bar-o = Venetiani in 1448 (against the single *duca* gloss of 1446)
is worth a look on the f. 139 side.

## Files
- `PREREG.md`, `HASHES.txt` — protocol and SHA-256 (PREREG, pass A, table, settled f. 28, scripts, reference, f. 30 transcription).
- `texts/sign_legend.md` — labels (shape names) with the crosswalk to the f. 139 labels; addendum for labels added at settling.
- `texts/f28_passA.txt`, `texts/f28_passB.txt`, `texts/f28_signs.txt` — the two passes and the settled training text with values.
- `texts/f30_signs.txt` — blind transcription of f. 30; `texts/f29_reference.txt` — reference words from f. 29.
- `table_1448.json` (+ `build_table.py`), `measure_f30.py` → `results/results_f30.json`, `test_1446.py` → `results/results_f139.json`
  (run `test_1446.py` from the repository root: `python3 targets/tranchedini1448/dudout/test_1446.py targets/tranchedini1448/dudout/table_1448.json`).

## Limits
- The training slip is short (about 240 signs): 65 labels valued, several only once; homophones and nomenclator signs of
  f. 30 that f. 28 lacks stay unknown. A second training pass (learning on f. 30 too) would cover more, but f. 30 is burnt
  for testing that table; another 1447-49 letter of lead 1317 (ital. 1584 f. 353; ital. 1585 ff. 35, 71) would be the next held-out text.
- Shape families hard to separate in this hand: rb/ri, i/i2, o2 variants, tt/dd; the f. 30 reader and the f. 28 readers did not
  always cut them the same way (this lowers the score, it cannot raise it).
- Credits: George Lasry (1452 table), Domnina (2018, Fig. 5), Daniel Bourdeau (f. 134/f. 139 labels, transcription and glosses,
  `table_test.py` and `lang.lm`).
