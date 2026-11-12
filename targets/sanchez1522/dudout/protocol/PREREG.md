# PREREG — sanchez-1522, lot 1 (12 Nov 2026, fil 🔓, Claude Opus 5.5)

Frozen by SHA-256 (line added to HANDOFF.md) BEFORE any decoding of any lot-1 transcription with Daniel's key.

## What is tested
Whether Daniel Bourdeau's key for targets/sanchez1522 (Tomokiyo 2025 nomenclature + Daniel's additions, `key_codes.tsv`,
and the letter-sign table of `alpha.py` / `R9593_signs.txt` / NOTES), **unchanged**, turns lot-1 cipher into Spanish.
Key files at dbourdeau/cyphersolver origin/main 62b62c5b5c8b9869f0e267d34582bbe67b6f00e0:
- key_codes.tsv b81cc2266f5cbd23f4e69555c3f2d27dea43fa4a71ee0721dd1d68c9166bcb58
- alpha.py 26dfe3f61db5cde59c6d74cce0c2102a71037346a5a6a7afcf1e80f34b8a5739

## Held-out portion (one, ≥ 300 characters)
`transcriptions/HELDOUT_R9632_f200r_l07-25.txt` — DECODE R9632, image P2 right page (f. 200r), lines 7-25, 386 tokens,
transcribed blind by sign shape. SHA-256 d10f10482d8848858ccee03e0509a558bb2db9d6d50e3fe242f6b97018b74758.
R9632 is **not** used for any key adjustment in this session (no new code value, no sign value is taken from it).
Any key adjustment made later from other letters (R9607 etc.) is NOT applied to this measure: the measure runs on the
unchanged key above.

## The one measure
`tools/measure.py` (SHA-256 7835c782488f49dc0e8bc59a43cec30c24de79e24a40aace491ad54bb3df5eb2):
- decode: code group → key_codes.tsv value; shape label → letter by the fixed map SIGNS in the script (from Daniel's
  files); nulls, clear words and unread spans dropped; unknown codes dropped and counted;
- score S = mean log-probability per character, 4-gram character model, no spaces, add-0.1 smoothing, trained on
  Don Quijote (Gutenberg text, `duran-1718/dl/corpus/quijote.txt`, SHA-256 27f5064a…036429e), u/v, i/j/y merged;
- 400 controls, seed 20261112: C1 = 200 permuted keys (code values permuted among codes, letter values among sign
  labels); C2 = 200 shuffles of the token order with the true key.

## Thresholds (set now)
PASS iff decoded length ≥ 300 characters AND S_real > max(400 controls) AND z = (S_real − mean_c)/sd_c ≥ 5.
Otherwise FAIL, declared as such; no second measure on this portion, no re-transcription of it after the result.

## Counting rule (Daniel's 95 % rule), per letter
Per letter, cipher words of the reading are counted S (sure: read as Spanish in sense), P (probable), R (restored:
supplied from sense, gap or copy), I (unresolved). "read" iff (S+P)/(S+P+R+I) ≥ 95 %, restored excluded from the
numerator; otherwise "read in part". Clear-text passages are not counted as read cipher.
