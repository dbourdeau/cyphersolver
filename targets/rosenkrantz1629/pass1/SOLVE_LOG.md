# SOLVE_LOG rosenkrantz1629 (training letters N12, N13, N14, N20 only; 304 sign tokens in letter runs, 53 types)

Run 1. tools/solve.py seed 1, 30000 iters x 4 restarts, no crib, no frequency term, 5-gram da1620 (3-gram for runs under 5). Score -691.0. FAILED: degenerate key (everything mapped to e/n/d/r: 'deednede', 'dendendended'). A many-to-one search with no frequency constraint collapses.

Run 2-3. Same, with a chi-square letter-frequency term (weight 1.0), seeds 1 and 2, 40000 iters x 4 restarts, no crib. Scores -848.7 and -836.4. FAILED: the two seeds give unrelated keys and no Danish ('eseng fuerdthelleme' / 'ufond itemsaaeptheo'). 304 letters over 53 types is too thin for a blind homophonic search.

Observation (from the frozen training text only). One seven-sign word recurs six times with small variants:
 N12 l2 "{och med de} TH BX 4 U LD FM OM"; N13 l1 "D8 PF X4 CD LD RH OM"; N13 l4 "OU GM X4 OU LD RH OMb";
 N14 277R l2 "OU GM + CD LD FM OMb 3"; N14 278L l3 "D8 BX X4 OU LD FM OMb 3"; N20 l6 "D8 GM X4 U LD FM OMb 3".
 Position 1 and position 4 share the sign OU, so the pattern is A B C A D E F. In the context (an envoy in London; "med de ...") the Danish word of that pattern is ENGELSK(E). Hypothesis H1: D8/TH/OU = e, PF/GM = n, X4 = g, LD = l, RH/FM = s, OM/OMb = k. BX, CD, U, 4, + left free (they may be variants or separate letters). This is a pattern-word guess from the ciphertext and its clear context, not outside key material.

Runs 4-6. H1 pinned (D8,TH,OU=e; PF,GM=n; X4=g; LD=l; RH,FM=s; OM,OMb=k), other 42 types free, chi weight 1.0, seeds 1, 2, 3, 40000 x 4. Scores -863.2, -862.3, -850.5. FAILED: outside the pinned word the three seeds disagree ('hudefsk' / 'drreask' / 'intedsk' for the word after "Engelsk och"); no run of Danish beyond the pinned word. Scores are no better than the unpinned runs (-848.7, -836.4), so H1 gets no support from the language model.

Runs 7-12. Merge schemes M1a (D8,TH,OU,CD,U,CU one class; PF,GM,BX; X4,+,4,XA,X3; LD,LH; RH,FM; OM,OMb; PI,MM; TB,OX; RG dropped; 36 types) and M1b (D8,TH,OU apart from CD,U,CU; 37 types), no crib, seeds 1-3, 40000 x 4. Scores -841.7, -844.2, -851.7 / -838.3, -852.7, -839.8. FAILED: seeds disagree, no Danish.

Control C1 (tools/synth.py, seed 5): 304 letters of Christian IV's Danish cut to the same 43 run lengths, enciphered with a random homophonic key. True plaintext scores -710.4 (chi 17.4, objective -727.8; in-sample text, so optimistic). Old schedule: 36 types -854.9, -866.3; 52 types -824.3, -820.6: NOT recovered. So the failures above were the solver's.
Solver change: geometric cooling T 3.0 -> 0.09, swap moves added, NR restarts. Control again: 36 types, 300000 x 1: -833.9, NOT recovered. 21 types and 28 types, 150000 x 2: -726.3 both, RECOVERED in full ("derti ilhaffuerduhu osrassmu ..."). Working limit of this solver on this much text: about 28 sign classes; it fails at 36.

Runs 13-20 (new schedule, 150000 x 2, seeds 1 and 2, no crib):
 M2 (29 classes, digits kept as signs): -844.4, -831.0. Seeds disagree. FAILED.
 M3 (M2 with the digits 1 2 3 5 6 7 9 dropped as nulls or numerals; 22 classes, 266 letters): -723.7, -724.2, the two seeds give the SAME key. Decode is not Danish ("hendt | denskalnnidn", "sinird | grsdns", "osntnrieguek"); the repeated word comes out "denskal"/"dendkal". -2.72 per letter, against -2.39 for true text in the control and -2.74 for the control's wrong optimum. FAILED: a stable false optimum.
 M4 (36 classes, digits kept): -817.3, -811.2. Seeds disagree. FAILED.
 M5 (M4 with digits dropped; 29 classes, 266 letters): -683.4, -683.3, same key from both seeds; -2.57 per letter. Decode is not Danish ("mfael | eringeriidea", "dhhnfoederanger", "kchuiismed"). FAILED: stable false optimum. M3 and M5 contradict each other (D8 = d in one, e in the other).
Runs 21-24. H1 (ENGELSK) pinned under M3 and M5, 150000 x 2, seeds 1, 2: M3 -816.8, -816.9; M5 -732.1, -731.3. Both worse than the unpinned optimum of the same scheme (-723.7; -683.3) and the text outside the pinned word is not Danish ("onged | engelskggaeg", "attenistengelsk", "griigerniemedggai"). H1 NOT supported. It stays a guess.

RESULT: no key. No run produced Danish. Nothing here is a reading.
For the record of the held-out test, the best-scoring converged candidate (M5, seed 1) is frozen as KEY.tsv and decoded once. It is a failed candidate, not a claimed key.
