# PREREG — sal-stubbs, pages (2) and (3) — written 2026-11-23 BEFORE any key is built or any decoding tried on these pages

Documents: SAL THO/57/127, images b (page (2), bar-and-tick script) and c (page (3), letter-like symbol script).
Inputs (frozen, SHA-256 in PREREG_P2_P3.sha256): blind/P2_A.tsv, P2_B.tsv, P2_disputes.json, P2_arbiter.tsv -> blind/P2_final.tsv -> P2_lines.json (69 main lines); blind/P3_A.tsv, P3_B.tsv, P3_disputes.json, P3_arbiter.tsv -> blind/P3_final.tsv -> P3_lines.json (35 main lines). Free-standing dots dropped. Left-margin columns (sideways) are NOT in these files: excluded from training and measure, read afterwards.
Known before this PREREG: sign inventories and frequencies only (P2: 2,512 signs, ~22 frequent codes; P3: ~1,630 glyphs, 21 names), and the page-(1) result (English narrative letter; page-(1) key failed its own pre-registered measure narrowly, 0.848 < 0.85). The page-(1) plaintext is NOT used as a crib for pages 2-3 (their text is expected to continue, not repeat, page 1; if a repeat is found it will be reported, not used for the measure).

## Hypothesis
H1 for each page separately: monoalphabetic simple substitution (one code = one letter, nulls possible), language English (same lexicon as page 1). Otherwise reported as such.

## Portions
- P2: training = lines 0–60 (2,208 signs); held-out = lines 61–68 (304 signs) = prereg/heldout_P2.json.
- P3: training = lines 0–27 (1,300 glyphs); held-out = lines 28–34 (327 glyphs) = prereg/heldout_P3.json.
Keys built only from training lines (annealing on English quadgrams of lm/en_* + manual word reading of training lines). Held-out not looked at decoded before the measure. One single measure per page; afterwards the portion is burnt.

## Key freeze
prereg/KEY_P2.json, prereg/KEY_P3.json, hashed (KEY_P2.sha256, KEY_P3.sha256) before the measure.

## Measure
prereg/score.py unchanged (SHA-256 fcf68893… as frozen in PREREG_P1.sha256): lexicon coverage of the decoded continuous string; 200 controls by permuting key values (seeds 1700+k); PASS iff S >= 0.85 AND S >= max(controls) + 0.30; < 300 signs = non mesurable.

## Reading count
Rule #728 as for page 1 (sure words only over plaintext words; probable/restored/unresolved = holes; < 40 words: read with <= 2 holes).
