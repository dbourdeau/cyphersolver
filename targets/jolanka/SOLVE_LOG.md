# SOLVE_LOG: jolanka (training cards only; card 96 never read by a solver)

| # | tool and settings | result |
|---|---|---|
| 1 | tools/solve.py v1, seed 1, 4 restarts x 6000 steps, many-to-one keys allowed, 4-gram no-space model, accents kept | FAILED. Two faults: plain-writing tokens in braces leaked into the sign stream, and the many-to-one search collapsed to "tetete..." (score -2.837 per sign). Key discarded. |
| 2 | tools/solve.py v2 (one-to-one keys, swap moves, simulated annealing T 0.6 to 0.01, full rescoring), seed 1, 6 restarts x 12,000 steps, accents kept, 29 sign types, 2,176 training signs | Restarts 0, 2 and 3 reach -3.9156 per sign and read as Hungarian ("szeretet...egyetlen remenyem ne daragudjon"). Restarts 4-5 stall at about -5.2. Key saved: solve_out_seed1_fold0.json |
| 3 | same, seed 7, 3 restarts x 25,000 steps | same key, -3.9156 (restarts 1-2 stall at -5.2) |
| 4 | same, seed 20261112, 3 restarts x 25,000 steps | same key, -3.9156 |
| 5 | Reading of the TRAINING decode (cards 76, 77, 79, 80, 81, 84) for key repair; held-out card 96 not decoded | Three changes to the solver key, each from training words: EIGHT c -> k ("8 E V1+a ONE E RC" = kedves-, card 81 l.17; EIGHT and ESS then share k); OVAL h -> cs ("OVAL H2 ESS" = csak, "SIX H3 OVAL H3 RC" = becses, card 80 l.2); V1 p -> d (card 76 l.1 "szeretet(t) edes"). |
| 6 | Fault found in the frozen transcription while reading the training decode | The label V1+a merges at least three written signs: it stands where the sense needs h (hogy, 19 times in training), d (edes-, 12 times) and p (megkaptam). The transcription is frozen, so it is NOT corrected: V1+a keeps the solver's value d and every h and p written with it will decode wrongly. Some V2 are also the d sign misread (kedveben decodes "cenveben"). Listed in REPORT.md as the main open problem. |

Not tried: fold accents (fold=1 option of solve.py); 5-gram scoring; any homophone or nomenclator model (not needed: the simple key reads). Shorthand (Gabelsberger, Stolze-Schrey) ruled out by the result: one sign per letter, no abbreviation.
