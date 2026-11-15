# PREREG-2 — Mabeyn->Yemen system B (cyphersolver 2646): second and LAST test (re-test on a fresh portion)
Written 15 Nov 2026 BEFORE any pass on the held-out sheets. Test 1 (575+577, 0.787, partial) is burnt.

- Key v2: key/key_systemB_v2.json, 27 numerals, SHA-256 33e491fa70ece9e76e128c7fbd6de753162066c81fc01c34115fae8f41f584c0. Built mechanically by scripts/build_key2.py from
  TRAINING glosses only (HPBK 541, 585 and the added training sheet 562; passes A+B). Rule in the script header.
  Override: 27 = ه (gloss shape). 48, 56, 76 not entered (fewer than 2 concordant training readings).
  The 575/577 misses were used only to know which numerals to look for in training, never as values.
- Held-out sheets (chosen in prereg2/CHOICE.md from a low-resolution contact sheet before reading glosses):
  HPBK 644, 652, 675. Two fresh blind passes (A, B) under transcription/BRIEF-PASS.md, aligned with scripts/align.py (R=70).
- Unit, measure, controls, bar: identical to test 1 and the same frozen scripts/score.py
  (SHA-256 9c4c45456c0de74d8042fa79802dd4ce5556676fdf2b99656ca28114c231c3f0): two-digit tokens whose numeral both
  passes read alike, with a usable gloss in at least one pass; hit if the key letter's skeleton class equals the
  skeleton of A's or B's gloss; numerals absent from the key are misses; 200 within-class shuffles, seed 2646.
  Bar: score >= 0.85 AND score >= best control + 0.30, else partial/failed. No third test.
- Arbitration: none on held-out glosses (the A/B pair is the reference, so the scorer does not need my eye).
- The merged held-out files are hashed after the passes and before the run (prereg2/SHA256SUMS-heldout.txt).
- Command: python3 -I scripts/score.py key/key_systemB_v2.json 644 652 675
- 1070 vs 575: qualitative only, not part of the score.
