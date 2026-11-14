# rucellai1482: notes

Catalogue 2350 (ASF MAP LXXII 196, 200, 202, 206) and lead 2323 (LXXII 211): Bernardo Rucellai's 1482 letters from Milan in his "HP" sign cipher. Proposed as **read in part, key partial**. No images: the ASF MAP scans are cited, not reproduced.

## Material
- Key pair: LXXII 207 (cipher) and 208 ("Decifrato della n. 207", contemporary decipherment).
- Used up for tests: 204/205 (cipher and contemporary clear, test of 6 Nov 2026) and the glosses of 201 (test of 13 Nov 2026). See validation.txt.
- Bare letters read here: 196, 200, 202, 206, 211 (no decipherment on the leaf or filed with it).

## How the key was built
1. 6 Nov 2026: letter table K_T from 207/208 by EM alignment and greedy tuning; tested once on 204 against 205: 0.6018 (best shuffled 0.2281), not validated.
2. 13 Nov 2026: second transcription pass of 207; second test on 201 against its glosses: 0.5088 (best shuffled 0.2832), not validated.
3. 14 Nov 2026: two proposals from Claude Fable 5.2 runs (lots 11 and 12; used as tools, by Brice Dudout's API runs): rule corrections on 207 (fit 0.770, then 0.778), I, the dot, l with small o, crossed equals, B tried as values.
4. 14 Nov 2026 (this proposal, K_HP_v1):
   - the q-like signs of 207 re-examined one by one at 4x: the old token "g" merged a q with barred descender (now G) and a "g" with open lower loop (now 8); against 208, G = o and 8 = e; plain q stays o, and h before e-signs;
   - the five bare letters transcribed again, blind, with the 207 convention (1320 tokens; 90 % token agreement with the earlier pass); "g" there is always the barred q, and the open-loop "g" had been written c;
   - value changes kept only if they did not lower the 207 fit and raised the Italian likelihood of held-out letters (leave-one-letter-out); I = rr and dot = tt kept from the reading (signs absent from 207);
   - fit on 207: 0.8093 (lot 12: 0.7776); lexical coverage of the four unused bare letters 0.374 against 0.122 for the best of 200 shuffled keys.

## Status and limits
- **Not validated.** No HP passage with a clear is left unused, so no fresh measurement exists for this key. The only protocol figure for the system is 0.6018 against 0.2281 (an earlier key). The figures in validation.txt are consistency checks.
- Readings: sure + probable words cover 52-66 % of the decoded letters of the cipher runs (reading/). Remaining limits: 1272 px images (b/6/t, d/b, o/Q), a nomenclator not in the key (B, ⊙, crossed equals, "e d"), ℓ° (probably "che", restored only).
- Not seen: R. M. Comanducci, *Il carteggio di Bernardo Rucellai: inventario* (Olschki 1996), pp. XXIX-XXXI and Appendix III (Rucellai's keys, printed). The key sheet of Rucellai in P. D. Gabbrielli's volume of Dieci keys (no. 14, 1484-85) belongs to another system (the "##" family).

## Prior art
No decipherment of 196, 200, 202, 206 or 211 found (catalogue vetting of 6 Nov 2026; repository searched 14 Nov 2026: no target, PR or issue on these letters except our status notes). Mallett's edition of Lorenzo's Lettere cites only 204-205.
