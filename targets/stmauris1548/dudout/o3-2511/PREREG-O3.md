# PREREG-O3 — stmauris1548 (WAINUT target), 1547 letter, cc. 1v + 2r — 25 Nov 2026, Claude Opus 5.5 (local), fil 🔓

Prepared on 25 Nov 2026 at Brice's request (« Prépare les planches proposées » ; PROGRAMME-RELECTURES-2311, line of 24 Nov:
« c.1v/2r restent neuves → 2e passe aveugle + nouveau PREREG »). Frozen by SHA-256 (PREREG-O3.sha256 + HANDOFF.md) BEFORE
any transcription of c. 1v / 2r exists. **Nothing is transcribed, decoded or measured by this file.** The next step (the two blind
passes) is run later by fresh agents.

## 0. Prior art (step 0, 25 Nov 2026)
- `gh pr list -R dbourdeau/cyphersolver --search stmauris1548 --state all` : only #240 (LcCompany/WAINUT, MERGED 4 Nov). No open PR.
- Clone `_shared/cyphersolver` main b13dd55072 (24 Nov 22:07 UTC): `targets/stmauris1548/key.tsv` and `SIGNS.md` are byte-identical
  to our frozen copies (hashes below); the 1547 letter is still "not transcribed" there.
- Our O2 (23 Nov): c. 1r, one blind pass, same key, **FAIL** (M 0.718 < 0.85 ; margin 0.280 < 0.30). c. 1r is burnt for testing.
  c. 1v and c. 2r have never been transcribed or decoded by anyone (us included): they are the fresh portion here.
- Third-party target: any result goes to WAINUT/Daniel by comment or PR crediting WAINUT, only with Brice's go.

## 1. Frozen inputs (unchanged from O2 unless stated)
- Images (Estense IIIF, CC BY-NC-SA, SPOF_2 only, symlink `scans/` → ../o2-2311/scans, never republished):
  c01v.jpg 32695183604f6f95b51f8e14d2acef3dfa59a7c9e2c601bbbc635ff127bb4269 (2753×3906) ;
  c02r.jpg ea2140f436da8d217822d336425857b51bd37bef2047ca20d966e56a962ecb24 (3176×3983).
- Key: WAINUT's table `../o2-2311/wainut-key.tsv` b9e69238cd30569c01b1566bc6548fb1d16a030c652ecca053c6a98b89d5e034, used
  UNCHANGED. Nothing learnt from the c. 1r decode is added to it (no value tuning, no new sign value).
- Sign names: `../o2-2311/wainut-SIGNS.md` 678be0a407b03ba391d5594e13d88b21c1e0394e856d830b6c1243c7c2ef85aa, plus the
  shape-only conventions block (header lines « Conventions decided » and « N-shapes introduced », no values) of
  `../o2-2311/transcription_1547_c1r_blind.txt` 024298c77b7fe3321bc24c852c23c0196645de9f32cd150131d1e770276ffecb, so that both
  passes name shapes the same way. The transcription rows of c. 1r and its decode are NOT shown to the transcribers.
- Tools: `../o2-2311/measure_o2.py` bc5d71cd253f9281c83ba95c46dd9e3c36bab514ac0ea67a99cbf8c3e5eb0088 (unchanged) ;
  `../o2-2311/wainut-scripts/compare.py` 364d8233f783da376b4342a7f39bbbef497e5c3517951a5af05c3512df14a3f3.
- Lexicon corpus: `_shared/cyphersolver/lang/corpora/fr-1520s-diplomatic.txt` 813012bd28f1ee3111fe8c0800cfa35ab638b83c7038ab3eef16c63e088b617e.

## 2. Portion
All cipher rows of c. 1v (main block ≈ 24 rows + the 4-row block below it) and of c. 2r (upper block ≈ 10 rows, down to the row
ending « ( » before the clear closing formula « Atant, Monseigneur… »). Row numbering: `1v L01…`, `2r L01…`, top to bottom.
Interlinear glosses in another hand (c. 1v ≈ L16, c. 2r ≈ L06-L07) and the clear text of c. 2r are ignored; transcribers
receive row crops of the cipher blocks only (the clear closing text and the signature are cropped out).

## 3. Transcription — TWO independent blind passes, then blind arbitration
- Pass A and pass B: two fresh agents, separately, each sees only the row crops (any zoom), SIGNS.md and the shape conventions
  of §1. No key, no value, no decode, no reading, no clear text, no access to the other pass. Unknown shapes: new names N9, N10…
  (N1-N8 reused when the shape matches their description). Each pass frozen by SHA-256 before the comparison.
- Gate: token agreement A/B (WAINUT `compare.py`, row by row) **< 0.80 → STOP, no measure** (transcription not reliable).
- Disagreements: a third fresh agent C sees, for each disputed position, the crop with the position boxed and the two candidate
  names with their SIGNS.md descriptions only (never values); it chooses A, B or « neither » ; « neither » → `?` (no letter).
- Merged file `transcription_1547_c1v2r_merged.txt` frozen by SHA-256 BEFORE any decoding. No later edit of any sign.
- N-shapes (N1…) have no value in the key: they give no letter (declared limit, as in O2).

## 4. The ONE measure (`measure_o2.py`, seed 1548)
`python3 ../o2-2311/measure_o2.py transcription_1547_c1v2r_merged.txt ../o2-2311/wainut-key.tsv <corpus> 1548`
M = share of decoded letters covered by a max-coverage segmentation into lexicon words (3-15 letters); controls: 200 tables,
values permuted among the key's signs.
**PASS iff** decoded letters ≥ 300 AND M ≥ 0.85 AND M ≥ max(controls) + 0.30. < 300 letters: not measurable.
Run once. No second measure, no re-transcription, no key change and re-run on c. 1v / 2r afterwards; pass A or B alone are not measured.

## 5. Counting / outcome
- PASS: c. 1v-2r are read by sense from the decode (Daniel's 95 % rule, #728 strict: S/P/R/I) ; c. 1r's decode may then be read
  as supporting data only (not validated by its own FAIL). The target's share is recomputed ; result proposed to WAINUT/Daniel
  with credit, only with Brice's go.
- FAIL: nothing on cc. 1v-2r is a validated text ; the decode is kept as data. The 1547 letter has then no fresh portion left
  for this key ; stop (a new attempt would need another letter of the same cipher, e.g. 12 Mar 1548, cc. 5r-8v).
