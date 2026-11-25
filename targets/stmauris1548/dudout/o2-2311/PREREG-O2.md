# PREREG-O2 — stmauris1548 (WAINUT target), 1547 letter c. 1r — 23 Nov 2026, lot O2, Claude Opus 5.5 (local)

Frozen by SHA-256 (HANDOFF.md of the parent folder) BEFORE the transcription is decoded and BEFORE the measure.

## 0. Prior art (step 0, 23 Nov 2026 ~23 h)
- `targets/stmauris1548` = WAINUT (LcCompany) PR #240 (MERGED 4 Nov). PRs citing Mauris: #240, #242 (leads), #707 (renard1549,
  another letter). No PR, open or closed, on the 1547 letter (cc. 1r-2r) or 12 Mar 1548 (cc. 5r-8v): both "not transcribed"
  in main 9812a45218 (profile gaps, NOTES l. 18-19, 160, 185). Our own folder (BNE 7913/127) is another cipher (Tomokiyo).
- Third-party target: any result goes to WAINUT/Daniel by comment or PR crediting WAINUT, only with Brice's go.

## 1. Frozen inputs
- Images: Estense IIIF, manifest b70e7528-…, canvases 0-2 fetched full size by WAINUT's `fetch.py` (UA neutral), on SPOF_2
  `scans/` (symlink): c01r.jpg 882f467e…, c01v.jpg 32695183…, c02r.jpg ea2140f4… (CC BY-NC-SA, never republished here).
- Key: WAINUT's current table `wainut-key.tsv` (main 9812a45218) b9e69238cd30569c01b1566bc6548fb1d16a030c652ecca053c6a98b89d5e034,
  used unchanged (includes the values set after their 2 Aug test: they are tested here too).
- Sign names: `wainut-SIGNS.md` 678be0a4… (descriptions only; WAINUT's reference crops are not available to the transcriber).
- Tool: `measure_o2.py` bc5d71cd253f9281c83ba95c46dd9e3c36bab514ac0ea67a99cbf8c3e5eb0088, `wainut-scripts/compare.py` 364d8233….
- Lexicon corpus: `_shared/cyphersolver/lang/corpora/fr-1520s-diplomatic.txt` 813012bd28f1ee3111fe8c0800cfa35ab638b83c7038ab3eef16c63e088b617e.

## 2. Portion
All cipher rows of c. 1r (≈ 27 rows: opening block after "Monseigneur" and the main block). Never transcribed by anyone.
Transcription: ONE blind pass by a fresh agent that sees only the images and SIGNS.md (no key, no value, no reading, no
clear text), glosses ignored, frozen by SHA-256 before decoding (`transcription_1547_c1r_blind.txt`). Declared limit: one
pass only (WAINUT had two for 10 Jan); new unknown shapes get the transcriber's own N-names, which have no value here.

## 3. The ONE measure (`measure_o2.py`, seed 1547)
M = share of decoded letters covered by a max-coverage segmentation into lexicon words (3-15 letters) of the corpus above.
Controls: 200 tables, values permuted among the key's signs.
**PASS iff** decoded letters ≥ 300 AND M ≥ 0.85 AND M ≥ max(controls) + 0.30. < 300 letters: not measurable.
No second measure, no re-transcription of c. 1r for a new test afterwards (c. 1v and 2r stay fresh).

## 4. Counting
On PASS: c. 1r is read by sense from the decode (95 % rule, #728 strict: S/P/R/I), and the share read for the target is
recomputed (two letters read in part → three). On FAIL: nothing is read on c. 1r as a validated text; the decode is kept
as data only.
