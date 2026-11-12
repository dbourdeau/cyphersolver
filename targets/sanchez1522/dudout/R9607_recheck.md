# R9607 — declared re-check of C02's unresolved words (lot 2, 12 Nov 2026, C03)

Rule frozen in `PREREG_lot2.md` §3 (SHA-256 1d8a047d…5ccf) before this re-check. Input unchanged: C02's frozen blind
transcription `R9607_signs.txt` (4276b855…7b39) and C02's reading. Tool `tools/recheck_r9607.py` (1e7e4c08…95a0),
lexicon = Don Quijote words seen ≥ 2 times + `tools/extra_words.txt`; output kept in `R9607_recheck_output.txt`
(625 letter runs: 268 UNIQUE, 49 ambiguous, 308 without any full segmentation).

A C02 <…> word became P only where its run is UNIQUE (or ambiguous with exactly one segmentation fitting the sentence),
the word maps one-to-one onto C02's word slot, and it makes Spanish in context. No code value was added.

| line | C02 (I) | run | re-check (P) | context |
|---|---|---|---|---|
| 67r.11 | <ahi> | Z X ai | **ahi** (= hay) | "y aqui ahi […] que no creen lo que estos dizen" |
| 67r.24 | <ardr> | n g 3 g | **ayer** | "… ayer en las […] de vino aqui …" |
| 67r.25 | <soma> | Yo # B n | **toma** | "de la toma da de […]" (tomada) |
| 67r.27 | <sdner> | Yo 3 t4 y g | **tener** | "Estos dizen tener cartas de […] a xxiv horas" |
| 67v.01 | <sdnian> | Yo 3 t4 ai n t4 | **tenian** | "dizen que no tenian si no quando …" |

Rejected although the tool proposed a word: runs that span several of C02's word slots (65v.11 "y echo pero",
66v.17 "mendare podria", 67r.02 "tiene cien…"), runs whose only segmentations miss the word the sense needs (66v.12 and
66v.25 <sidma>, sense "tierra", tool "si era | ti era"; 67r.07 <mario>, sense "sumario", tool "ma rio | mar io";
66v.28 <sdner>, same group as 67r.27 but its run includes the -n of "dizen" and has no segmentation), and runs giving a
word that does not fit (66r.05 <possa> → "posta").

**Count, same 1,555 words: before 1,121 S + 116 P + 2 R + 316 I = 79.5 % ; after 1,121 S + 121 P + 2 R + 311 I = 79.9 %.**
Still read in part. The mechanical rule recovers little because most of C02's unresolved words are not look-alike
substitutions but shape-label errors that the declared alternatives do not cover. The lot-2 transcription of R9610
shows which ones (see `R9610_reading.md`, notes): my and C02's label `q` is often the l-sign (9) (pol q = mil, Q n q m # =
salvo), `oo` covers both of Daniel's ∞ signs (oo = d, OO = g: seguros, cargo, pagado), `Z` is sometimes the d-like ∂
(conduto, perdida), the pair `tt #` is one sign (alpha.py's `jt` = u/v: nueva, Savoya, estavan), and `m o` is the single
sign `mo` = h in alpha.py. Applying these to R9607 would be a re-transcription, which the PREREG did not declare; it is
left for a letter-by-letter second pass on the image.

## The 63 code groups absent from the key, seen again in R9610 (proposals only, not applied)
| group | R9607 (C02) | R9610 | suggested value | support |
|---|---|---|---|---|
| dud | 66r.12, 66v.25 "dizen que <dud> aqui por ver la […]" | 133r.23 "estos que <dud> mas por espia que por otro"; 133v.05 "el dicho embaxador no <dud> a otro" | **vino** | 4 contexts; d-block bracket ded veni < dod vi < dud |
| lud | 65r.01 "a <ce> del <lud> recebi" | 134r.08 "estando escriviendo la <lud>" | **presente** | 2 contexts; l-block bracket near lod principal (loose) |
| bic | — | 132r.10, 134r.05 | ? | 2 contexts, no value fits both |
| ni | 66r.13, 66r.14 | 133r.14, 133r.25 | ? | — |
| ci | 65r.15, 66v.25, 67r.28 | 133r.19 "lanças <ci> mil gascones" | ? | — |
| nig | 65r.19, 67r.11 | 133r.27 "de estos <nig> christianos" | ? (a quantifier) | — |

Groups new in R9610 with a structural value: **sod = govierno** (3 contexts: "el mal <sod> de Lautrec", "al […] del
<sod> de estos", "los del <sod> dizen"; s-block bracket sid governador < sod), **cid = xxii** (133v.15 "cartas de <cid>
de abril"; c-block numerals cab xv … cud xxiv, cad xx, so cid falls on xxii).
