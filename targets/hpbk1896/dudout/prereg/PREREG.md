# PREREG — Mabeyn->Yemen system B (cyphersolver 2646), held-out test of the gloss key
Written 15 Nov 2026, BEFORE scoring. Nothing on 575/577 has been compared with the key.

- Key: key/key_systemB_train.json, built only from the clerk's glosses on training sheets HPBK 541 and 585
  (blind passes A and B, arbitrated). 24 two-digit numerals. SHA-256 8304e7ee9cddb92e0c8a575caceb76ec782edac2c0f614b15a880129ccaee787
- Held-out: HPBK 575 (6 Feb 1900) and 577 (30 Apr 1899), glossed sheets not used for the key. Unit: two-digit
  numeral tokens whose numeral both passes read alike and that carry a usable gloss in at least one pass
  (bare tick "ـ", "-", "?" excluded): 174 tokens (149 + 25), counted before scoring.
  Reference files: transcription/merged_575.tsv SHA-256 48138d1e48cad250670c27fe1f47a71cf714ae92d9a0db2cd35068fae7ccbc83 ; merged_577.tsv SHA-256 05851f72d315f90a2b8016cfe9858e99c25b1dc0979c540c902c62bead279d0c
- Measure (one): share of tokens where the key letter, reduced to its dot-less skeleton class, equals the skeleton
  of pass A's or pass B's gloss (the glosses are mostly undotted). Numerals absent from the key count as misses.
- Controls: 200 within-class shuffles (letter values permuted over the key's 24 numerals), seed 2646, same rule.
- Bar: score >= 0.85 AND score >= best control + 0.30 -> "key confirmed on held-out glosses"; otherwise partial/failed.
- Script: scripts/score.py SHA-256 9c4c45456c0de74d8042fa79802dd4ce5556676fdf2b99656ca28114c231c3f0 ; command: python3 -I scripts/score.py key/key_systemB_train.json 575 577
- Descriptive only (not part of the bar): decode of the unglossed 587 and 602; comparison of 575 with the clear 1070.
- The portion 575+577 is burnt after this measurement.
