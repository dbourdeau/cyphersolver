# PREREG C04 — dorffler-1686 (catalogue Bourdeau 1773), written 2026-11-12 ~19:40 CET BEFORE any look at img. 474

Agent: Opus only (no Fable, no API call). New protocol, new hash, never retroactive. Supersedes nothing in C03.

## History disclosed (fixed, not revisable)
- PROTOCOLE-C02 (b235a9ed…) set an absolute threshold of 0.85. PREREG-C03 (a4e2b1b7…), declared BEFORE its measure,
  lowered it to 0.75 (noisy gloss on both sides) and kept the margin + 0.30 over the best control.
- C03 single measure on img. 476 with TABLE-C03 (feb40aca…): S = 0.7354, best control 0.2637 -> **FAIL** (absolute
  threshold missed by 0.015). 476 can never be measured again; it is now TRAINING.
- C04 keeps the threshold at **0.75** (not lowered again) and the margin at **+ 0.30**.

## Table (frozen BEFORE this PREREG)
`c04/TABLE-C04.json` SHA-256 **14b38f499a961b99bc7707aa71106cf5f5ca140eaa27faae1728db827b41ef28**
(changes from TABLE-C03 and their training evidence: `c04/TABLE-C04-CHANGES.md` 242730da…). Built from training images
only (470, 475, 467, 468, 476). The original C03 table was built with Fable (claude-fable-5-2, C03 run); C04 changes are
Opus's. No change to the table after this PREREG.

## Held-out portion
img. **474** of SE/RA/2115/I/19/102 (R0003596), **right-hand page, all cipher lines and all gloss over them**.
474 was never sent to any API, never cropped for Fable, never transcribed, never viewed before this hash (C02 only made a
reduced overview `work/s474/ov.jpg` to locate cipher pages; it is not opened in C04 before the freeze of step 1).
Source: `/Volumes/SPOF_2/.../dorffler-1686/sources/full_R0003596_00474.jpg` (≈ 4000 px).

## Metric (identical to C03): `fable/measure.py` SHA-256 47ee24e4…ddb5, unchanged
S = 1 − Σ_b lev(D_b, G_b) / Σ_b max(|D_b|, |G_b|) over the scored blocks; D_b = TABLE-C04 applied to the block's
groups (unknown or '?' -> '#'), G_b = the block's gloss; normalisation of measure.py. Controls: 500 tables = TABLE-C04
with values permuted among its keys (seed 20261112).
**PASS = S ≥ 0.75 AND S ≥ max(controls) + 0.30.** Anything else = FAIL: no PR, no reading of unglossed parts, documented.
One run only. No second measure on 474.

## Blocks (fixed now)
A block = one physical cipher LINE of the right page of 474 (ids `474R-01`, `474R-02` … top to bottom); if clear text
interrupts a line, each cipher segment is its own block (`474R-05a`, `474R-05b`). The gloss of a block = the pale
interlinear writing directly ABOVE that cipher segment (observed rule, C03), from the x where the segment starts to the
x where it ends. Clear text in the dark main hand is never gloss.

## Step order (fixed now)
1. Hash this PREREG (SHA256SUMS). Only then: crops of 474 right page at full resolution (`work/c04/crops474/`).
2. **Cipher, two independent passes**: pass A = this agent (zoom crops, digit shapes only, no table consulted);
   pass B = a fresh Opus sub-agent given only the crops (no access to the table, to C01-C03 files or to pass A),
   instructed to transcribe digit groups only. Files `c04/T474-cipher-A.txt`, `-B.txt`, each hashed when written.
   **Reconciliation**: groups aligned per block; agreement kept; each disagreement re-examined by this agent on a
   ≥ 3× zoom of the group, deciding on digit shapes alone (no decoding, table not consulted); if still undecided ->
   '?'. Result `c04/T474-cipher.txt` + `c04/RECONCILE-cipher.txt` (every disagreement and its decision), hashed
   = **frozen**. Known confusions to watch: 0/8, 6/8, 5/6, 1/7, 3/8, 15/16, 40/48, the tall 1.
3. **Gloss, two independent passes, without decoding**, only after step 2 is frozen: pass A = this agent, pass B = a
   fresh Opus sub-agent (crops only; told to read the pale German/Latin interlinear writing and to report per block
   which words are illegible). Files `c04/G474-gloss-A.txt`, `-B.txt`, hashed. **Reconciliation**: word kept where A
   and B agree; disagreements re-examined by this agent on the image (letter shapes and German sense of the gloss
   itself, never the cipher); a word still undecided counts as illegible. Result `c04/G474-gloss.txt` +
   `c04/RECONCILE-gloss.txt`, hashed = **frozen**.
4. **Scoring set (rule fixed now, applied before decoding)**: a block is scored iff its gloss is present and, after
   reconciliation, every gloss word over it is read (no illegible word). Blocks with absent or partly illegible gloss
   get no G line (so measure.py excludes them) and are listed. If the scored blocks hold fewer than 120 groups in all,
   the result is **FAIL (insufficient)**, no fallback.
5. Decode with TABLE-C04, ONCE (`c04/D474.txt`); then ONE run:
   `python3 -I fable/measure.py c04/TABLE-C04.json c04/T474-cipher.txt c04/G474-gloss.txt` -> `c04/MEASURE-C04.txt`.

## Known limits (declared)
- Pass A's adjudicator knows the C04 table; adjudication is on shapes only and every decision is logged.
- Measure.py does not collapse doubled letters across group boundaries (e.g. c+k): same artefact as C03, accepted.

## If PASS — count (Daniel's 95 % rule)
- Glossed passages = « existing decipherment (partial contemporary interlinear) »; our contribution = the key and the
  reading of unglossed passages (468_R2 l. 1-5, 470 left, etc.), counted SEPARATELY: word-by-word sheet, sure /
  probable {x} / restored [x] / unresolved ‹…›; publication claim only if ≥ 95 % read by the sense on ≥ 300 characters.
- Then PR `targets/dorffler1686` per cyphersolver-pr/PROCEDURE.md, disclosing the C03 failure and threshold history.
