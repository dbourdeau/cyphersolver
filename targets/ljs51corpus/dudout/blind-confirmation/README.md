# LJS 51: blind (ciphertext-only) confirmation of the by-eye keys, and Ibn ʿAdlān's length rule

Role: **verification**. Prior work: D. Bourdeau, `targets/ljs51corpus/keys_eye/` and `keys.tsv` (199 keys built from the
compiler's plaintext, "not independently confirmed"), `keys_eye/REPORT.md`, and the blind break of 48r.8
(`targets/ljs51f48r/`, `solve_48r/anneal_sp.py`). All at `origin/main` d8ac608093. This folder adds nothing to the
readings: it checks the keys from the ciphertext alone.

## Design (frozen before measuring)
- Freeze: `freeze/MANIFEST.sha256` (34 files), SHA-256 `f2e53f5726ff25bcaef7f6a4c84dc8a43fc0387073a19d20ecba66cc2662eb6d`,
  frozen 2026-11-28T14:35:43Z, posted on #1023 (issuecomment-7240798107) before the run. Protocol: `freeze/PREREG.md`
  (French). One run; nothing changed afterwards.
- Input: the `cipher_lines` of `keys_eye/<chain>.json` only (`transcriptions/*.sig`).
- Language model: our own letter 4-gram model (4 OpenITI texts: al-ʿUmarī, al-Ḥillī, al-Ṣafadī ×2), not `lang/`.
  Ibn Nubāta's dīwān was kept out and used for synthetic calibration. Leak check: 12-grams of each plaintext found in
  the model corpus: 0% for 17 chains, 3.2% for 69v.11.
- Solver: simulated annealing, simple substitution with homophones (penalty λ = 8 per extra sign sharing a letter),
  word dividers kept, both reading directions tried, 20 restarts × 500,000 iterations, seed 2811.
- Controls: 200 per chain, shuffled ciphertext (divider positions kept), solved by the same solver.
- Metric: character agreement with the compiler's plaintext (`chains_all.json`), difflib over the longer string.
  Pass: ≥ 0.85 AND ≥ best control + 0.30.

## Results (`results/RESULTS.tsv`, `CURVE.md`, `DISAGREEMENTS.md`)

| chain | signs | classes | agreement | best control | z | pass |
|---|---|---|---|---|---|---|
| 20r.8+47r.1 * | 336 | 26 | 0.98 | 0.30 | 15.9 | yes |
| 22r.1 | 167 | 32 | 0.11 | 0.34 | −1.3 | no |
| 19r.7 | 145 | 26 | 0.94 | 0.34 | 15.2 | yes |
| 105v.6 | 130 | 28 | 0.72 | 0.32 | 9.8 | no |
| 18r.11 | 129 | 29 | 0.44 | 0.36 | 4.4 | no |
| 23r.9 | 125 | 22 | 0.79 | 0.38 | 9.0 | no |
| 61r.3 | 113 | 24 | 0.10 | 0.28 | −1.3 | no |
| 30r.4 * | 111 | 25 | 0.96 | 0.36 | 12.7 | yes |
| 42r.2 | 104 | 21 | 0.88 | 0.37 | 12.3 | yes |
| 39v.12 | 101 | 23 | 0.90 | 0.35 | 11.5 | yes |
| 82r.9 | 85 | 19 | 0.74 | 0.35 | 9.4 | no |
| 46r.11 | 78 | 20 | 0.88 | 0.37 | 10.6 | yes |
| 69v.11 (no dividers) | 73 | 20 | 0.18 | 0.37 | −0.7 | no |
| 35v.8 | 71 | 23 | 0.65 | 0.34 | 8.3 | no |
| 41r.3 | 60 | 20 | 0.88 | 0.38 | 11.3 | yes |
| 31r.11 | 56 | 16 | 0.96 | 0.41 | 10.5 | yes |
| 6v.11 (no dividers) | 41 | 18 | 0.24 | 0.37 | 0.0 | no |
| 56v.8 | 31 | 18 | 0.26 | 0.45 | 0.3 | no |

\* not blind for us: 30r.4's key was used in our 30v.7 test; 20r.8+47r.1 enciphers the 48r.8 riddle, whose plaintext
we knew. Counted apart.

- **Strict pass: 6 of the 16 truly blind chains** (19r.7, 42r.2, 39v.12, 46r.11, 41r.3, 31r.11), plus the 2 declared
  chains. For these 6 the compiler's plaintext, and so Daniel's key, is confirmed from the ciphertext alone.
- **Ranked first of 201 but under 0.85: 5 chains** (105v.6 0.72, 23r.9 0.79, 82r.9 0.74, 35v.8 0.65, 18r.11 0.44;
  z 4-10). The solver found most of the key; this is strong evidence but not a pass under the frozen rule.
- **At chance: 5 chains.** 22r.1 and 61r.3 (113-167 signs, with dividers) fail completely: worth a look, since
  length is not the cause (another system, a different reading order or a class problem). 69v.11 and 6v.11 have no
  dividers; 56v.8 has 31 signs.
- **Disagreements** with Daniel's keys on the passed chains (32 signs) are all on signs seen 1-3 times: the expected
  errors of a blind solver on rare letters. None points to an error in Daniel's keys.

## Ibn ʿAdlān's rule (about 90 letters)
Pass rate by length: 30-45 signs 0/2; 46-60 2/2; 61-75 0/2; 76-90 1/2; 91-120 3/4; 121-170 1/5; >170 1/1. With
dividers, success starts near 55-60 signs (31r.11, 41r.3) and is not assured even at 170 (22r.1). On 18 real
fourteenth-century ciphers, length alone does not decide: word division, the number of sign classes per letter and
the cipher type matter as much. The sample is small (2 chains per short bracket); this is a first measurement, not a
law.

## Limits (declared in the PREREG)
1. The sign classes were drawn up by Daniel knowing the plaintext; merges and splits may help the solver.
2. λ, restarts and iterations were set on synthetic ciphers and on 48r.8 (declared positive control) before freezing.
3. Freeze by SHA-256 manifest posted on #1023, not `tools/holdout/freeze.py` (PR #1014): `measure.py` tests a fixed key
   against shuffled keys, while this test re-solves shuffled ciphertexts.
4. The scripts in `scripts/` are the frozen copies, kept byte for byte; their data paths are those of the machine
   where they ran and must be edited to re-run. The model files (`lm4_*.bin`, 2.8 MB each) are not committed; rerun
   `build_lm.py` on the four OpenITI texts named in `common.py` (their hashes are in the manifest).

Credit: Brice Dudout (design, rules); Claude Opus 5.5 agent (code, run, write-up). Images: none used.
