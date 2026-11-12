# PREREG — sanchez-1522, lot 3 (12 Nov 2026, fil 🔓, Claude Opus 5.5, C04)

Frozen by SHA-256 (line added to HANDOFF.md) BEFORE any decoding of R9614, R9640, R9647 and BEFORE the second pass on the
† words of R9610 is applied. Only dry run made before freezing: `measure_lot3.py` on R9607 f. 65r (a lot-1 letter, not the
held-out portion), to check the script runs.

## 0. Blind transcriptions (frozen before this PREREG, no decoding done)
- R9614 (18 June 1522, ff. 208r-210v) `transcriptions/R9614_signs.txt` 335600bed7118534a73c0a4dcf367efa42f337701c79cfedc3f6ddaa47fd761e
- R9640 (22 Oct 1522, ff. 139r-141r) `transcriptions/R9640_signs.txt` dbe0a813db6ec04ec5f8e669c6126badc69498b5d89d2cec8746aa694a072434
- R9647 (7 Nov 1522 by its clear date, ff. 257r-258v) `transcriptions/R9647_signs.txt` 4312f3ff91ab45c14b527dafe1cbd51830c3fe8e44f3f8c7250f6275a6b86f3a
- R9610 independent second pass (fresh agent, blind to the first transcription and to any reading)
  `transcriptions/R9610_signs_pass2.txt` f58dbbe0e8b2a91042f998a3ea53934c324cad0beb943a7936d4994f26db757c

## 1. Key and sign table
Daniel's key unchanged (key_codes.tsv b81cc226…bb58). Reading table `tools/decode_lot3.py` = the lot-2 table + labels that
are Daniel's own (alpha.py / R9593 legend / NOTES table), used by the new transcriptions: `9` = l (already), `OO` = g (bold ∞),
`U` = u|v (ʃ#), `⊥` = r, `3f` = a, `x` = h. These are not adjustments (no value is invented; they are entries of Daniel's table).

## 2. The ONE measure (tests the four C03 code proposals)
Adjustment tested: dud = vino, sod = govierno, lud = presente, cid = xxii (proposed by C03 from R9610/R9607; no other code,
no sign-label rule). Sign-label correction rules (q/g→l, oo→g, Z→d, P→v, Lo→s, tt #→u) are **not** adopted as rules; † words
are handled only by §3.
- Held-out portion H: **R9647 f. 257r, all 30 lines** (658 tokens, all cipher). R9647 is not used for any adjustment; the
  burnt R9632 f. 200r ll. 7-25 is not used.
- Tool `tools/measure_lot3.py`: K = key unchanged + single-valued map (measure.py SIGNS + mo h, xo s, 9 l, OO g, U u, ⊥ r,
  3f a, x h); K' = K + the four values. S = measure.py LM (4-gram, Quijote, per char). G = S(K') − S(K).
- Controls (600, seed 20261113): C1 200 permuted K', C2 200 token shuffles with K'; C3 200 random value sets for the four
  codes, drawn from the key's plain values.
- **PASS iff** decoded(K') ≥ 300 chars AND S(K') > max(C1∪C2) AND z ≥ 5 AND at least one of the four codes occurs in H AND
  G > 0 AND G beats ≥ 190 of the 200 C3 gains. Otherwise FAIL; no second measure, no re-transcription of H afterwards.
- On PASS: the codes that occur in H are adopted, and the words they give are counted P (probable). Codes absent from H stay
  proposals (I). On FAIL: none adopted, every count is made with the key unchanged.

## 3. Second pass on the image for the † words of R9610 (R9607 has no † word)
Tool `tools/pass2_check.py` on `transcriptions/R9610_reading.txt` and the pass-2 transcription above: a {w†} word is
CONFIRMED iff it has ≥ 3 letters and is spelled exactly by a contiguous run of whole tokens of the pass-2 lines L−1..L+1,
decoded with the key unchanged and the declared alternatives. Control: the same test on the window 7 lines further on;
confirmations are applied only if the control rate ≤ 10 %. A confirmed † word becomes P (strict count); the others stay
†, counted I in the strict count. No word is downgraded; no code value is added.

## 4. Counting (unchanged): Daniel's 95 % rule
Per letter S / P / R / I; "read" iff (S+P)/(S+P+R+I) ≥ 95 %, else "read in part". Clear words not counted. Readings in
the lot-2 markup ({w} P, {w†} P only in the loose figure, [w] R, <w> I), counted by `tools/count_reading.py`.
