# PREREG-O4 — stmauris1548 (WAINUT target), letter of 12 Mar 1548, cc. 5r-8v — 25 Nov 2026, Claude Opus 5.5 (local), fil 🔓

Prepared on 25 Nov 2026 at Brice's request (« Oui prépare le PREREG stmauris » ; images: « Oui télécharge »). Frozen by
SHA-256 (PREREG-O4.sha256 + HANDOFF.md) BEFORE any transcription of the 12 Mar 1548 letter exists and BEFORE anyone has
looked at its pages: the 8 images were fetched by script and hashed, not opened. **Nothing is transcribed, decoded or
measured by this file.** The passes, the merge and the measure are run later by fresh agents.

## 0. Prior art (step 0, 25 Nov 2026)
- `gh pr list -R dbourdeau/cyphersolver --search stmauris --state all`: only #240 (WAINUT, MERGED 3 Nov). Search « Mauris »:
  #240, #242 (WAINUT leads), #273 (ours, leads), #707 (renard1549, another letter). No PR, open or closed, on 12 Mar 1548.
- cyphersolver origin/main b81c613843 (25 Nov 08:45 UTC), `targets/stmauris1548/`: transcriptions only of l2 (10 Jan 1548,
  passes A/B + merge) and l4 (2 Aug 1548); NOTES l. 19 and l. 160-161: « 12 Mar 1548 | 5r-8v (cipher blocks) | not
  transcribed »; profile.json `mar12` has no transcription. `key.tsv` and `SIGNS.md` on main are byte-identical to our frozen
  copies (hashes below).
- Our side: O2 (c. 1r, FAIL) and O3 (cc. 1v-2r, FAIL, M 0.784) used only the 1547 letter (canvases of manifest b70e7528…).
  No file of this dossier refers to cc. 5r-8v except the manifest list. Our BNE 7913/127 work is another cipher (PP1).
  => the 12 Mar 1548 letter is a fresh portion for WAINUT's key.
- Third-party target: any result goes to WAINUT/Daniel by comment or PR crediting WAINUT, only with Brice's go.

## 1. Frozen inputs
- Images: Estense IIIF manifest 65514839-924d-447b-962f-547fa30c0f7f (canvases 0-7 = 0005r…0008v), fetched full size on
  25 Nov 2026 by WAINUT's `fetch.py` (tiles ≤ 1500×640, 1.1 s apart, UA "research-client", run with `/usr/bin/python3 -I` via runpy from the scratchpad, the user site-packages path added
  explicitly for PIL only; no browser; 8 pages, no error, 09:47-09:55),
  stored on SPOF_2 only (`../o2-2311/scans/` → /Volumes/SPOF_2/…/o2-2311/scans; symlink `scans` here), CC BY-NC-SA, never
  republished:
  c05r.jpg bc86784710559954e6f9068d46ffe3772f82d0d95aff7046456cef44ae6e562c (5011×7156, canvas 0)
  c05v.jpg cc17c276fca59b532efe8ad86d1ef3ba9bd26233dbfcc85aedb1e4347ad16338 (4991×7095, canvas 1)
  c06r.jpg 5b20698e9aee56b3441306819ac68f58d50bbc294bc04628fdd60502a94bd0da (4987×7144, canvas 2)
  c06v.jpg ab26245b16c2da866925db8c1178fdacc95bc033af0511a402dd467d208bf9be (4983×7103, canvas 3)
  c07r.jpg 181f5beed7cb8cfb5be077401dec532e3bad7c967999674b6576d494fd612bec (5007×7124, canvas 4)
  c07v.jpg 5a58769a159ef0b6ade1f5c492abae963c97d62a032dac71e75a9025a3f17f76 (5007×7144, canvas 5)
  c08r.jpg 0e44580a8652908eab6be08c73ca767b1a34fcbb5391eaa05162ca39fdb31eff (4971×7116, canvas 6)
  c08v.jpg 9a5ec5641b57b804841a1c454fa980136a8a08cbf89e9a59224829619f6dd5ee (5011×7152, canvas 7) ;
  role: c05r-c06r = portion P, c06v-c08v = reserve R (§2).
- Key: WAINUT's table `../o2-2311/wainut-key.tsv` b9e69238cd30569c01b1566bc6548fb1d16a030c652ecca053c6a98b89d5e034 (= main
  b81c613843), used UNCHANGED. Nothing learnt from the O2/O3 decodes is added to it.
- Transcriber inputs (`input/`): `SIGNS.md` 678be0a407b03ba391d5594e13d88b21c1e0394e856d830b6c1243c7c2ef85aa (= WAINUT's) ;
  `SHAPES-KEY-NAMES.md` 107506b175d73aeb7d833cf900bfdd4b40446f5a403dabcf6f7296c41cf0509c ; `BRIEF-PASSE-O4.md` a1c7b711e0de3a5f5cf4fd24ac3e12b9664bce9d0f59018d7fc54b100c270f2c.
- Tools: `tools/measure_o4.py` f940b3545e51bb3f5f65dfeafded612a80d418d71f39141c76b5f5655ae6c4b7 (= `../o2-2311/measure_o2.py` bc5d71cd… with the guard, NIL/struck handling and
  z output of §5; segmentation, lexicon, controls and thresholds unchanged) ; `../o2-2311/wainut-scripts/compare.py`
  364d8233f783da376b4342a7f39bbbef497e5c3517951a5af05c3512df14a3f3 (`load` only, no BMAP).
- Lexicon corpus: `../../../_shared/cyphersolver/lang/corpora/fr-1520s-diplomatic.txt`
  813012bd28f1ee3111fe8c0800cfa35ab638b83c7038ab3eef16c63e088b617e.
- The crop tool and the arbitration-package tool are written at execution time, before pass A starts, and their SHA-256 are
  recorded in RESULTAT-O4 (they cut images; they never read names or values).

## 2. Portion — designated BEFORE any page is seen
- **Portion P = every cipher row of cc. 5r, 5v and 6r** (canvases 0, 1, 2), in page order, rows numbered `5r L01…`, `5v L01…`,
  `6r L01…` top to bottom within each page. Chosen blind, by position only: the first three pages of the letter.
- Excluded everywhere: clear (plain-language) text, the clear note in the margin of 5r (WAINUT profile), interlinear or
  marginal glosses in another hand, address and endorsements. The person who makes the crops (orchestrator) opens only the
  pages of P (and, on extension, the next page only), marks the cipher rows on overview images and crops them; it does not transcribe, decode or read the clear text.
- **Size rule (≥ 300 letters).** After the merge (§3) and BEFORE decoding, count the merged tokens whose name is a key name
  (names only; no value is looked at). If that count is < 340, the portion is extended by whole pages in fixed order 6v, 7r,
  7v, 8r, 8v, one page at a time, each added page going through the same two blind passes, gate and arbitration, until the
  count is ≥ 340 or the letter ends. Each extension is logged with its time before decoding. If the whole letter stays < 340,
  the measure is still run once; `measure_o4.py` reports NOT MEASURABLE below 300 decoded letters.
- **Reserve R = cc. 6v, 7r, 7v, 8r, 8v** (all that the size rule does not consume): not cropped, not opened at full size, not
  transcribed and not decoded in O4. It stays the fresh portion for any later test of this key (O5), with its own PREREG.
  If P passes, R is also the natural held-out page set for reading by sense (not counted as a test).

## 3. Transcription — TWO independent blind passes, gate, blind arbitration, merge
- Pass A and pass B: two fresh Opus agents, separately; each sees only the row crops of P, `input/SIGNS.md`,
  `input/SHAPES-KEY-NAMES.md` and `input/BRIEF-PASSE-O4.md`. No key, no value, no decode, no reading, no clear text, no access
  to the other pass nor to O2/O3. Each pass frozen by SHA-256 before the comparison.
- **Transcriber namespace from the start (fixes O3 point 4).** Reference names = SIGNS.md + SHAPES-KEY-NAMES.md (all are key
  names or SIGNS.md base names). Any other shape gets the transcriber's own name `t1`, `t2`… (unreadable sign: `t?`), never
  `N…`. The c. 1r conventions block used in O3 (its N1-N8 collided with WAINUT's N-names and merged 8/N15, y/yg, fs/fz) is NOT
  given. Before the comparison, each pass's `t` names are prefixed `tA-…` / `tB-…` (a t1 of A and a t1 of B are not assumed
  to be the same shape). Checked on key.tsv: no key name starts with `t` or is `NIL` (measure_o4.py asserts it).
- Gate: token agreement A/B (`compare.load`, row by row, difflib, names compared as written, no BMAP) **< 0.80 → STOP, no
  measure**. Every `t` position is therefore a disagreement and goes to arbitration (either choice gives no letter).
- Disagreements: a third fresh Opus agent C sees, for each disputed position, the crop with the position boxed and the
  candidate names with their descriptions (SIGNS.md / SHAPES-KEY-NAMES.md / the pass's own t description), never values; it
  chooses A, B or « neither ». **« neither » is written `NIL`** (fixes O3 point 3: `compare.load` drops a lone `?`, which
  would glue the neighbours): `NIL` gives no letter and cuts word coverage. If A and B differ in length at a position, NIL is
  repeated max(len A, len B) times (as in O3).
- Merged file `transcription_1548-03-12_P_merged.txt` frozen by SHA-256 BEFORE any decoding. No later edit of any sign.
  `t…`, `tA-…`, `tB-…`, `NIL` and struck signs (`X_` → NIL) give no letter (declared limit).

## 4. The ONE measure (`tools/measure_o4.py`, **seed 120348**)
`python3 -I tools/measure_o4.py transcription_1548-03-12_P_merged.txt ../o2-2311/wainut-key.tsv <corpus> 120348`
- Guard first: any token that is not a key name, `NIL`, a `t…` name or a struck sign → ABORT before decoding (names listed,
  no value shown). Expected case: a SIGNS.md name that has no row in key.tsv (e.g. bare `+`, `n`, `3`, `5`); it is renamed
  `tS-<name>` (no letter) in a logged naming step and the guard rerun. Nothing else may be changed. This is not a second
  measure: no letter has been produced.
- M = share of decoded letters covered by a max-coverage segmentation into lexicon words (3-15 letters) of the corpus;
  controls: 200 tables, values permuted among the key's signs (seed 120348; O2 used 1547, O3 1548).
- **PASS iff** decoded letters ≥ 300 AND M ≥ 0.85 AND M ≥ max(controls) + 0.30. < 300 letters: NOT MEASURABLE.
  Same thresholds as O2/O3.
- Run once. No second measure, no re-transcription, no key change and re-run on P afterwards; pass A or B alone are not
  measured.

## 5. z output (fixes O3 point 6)
`measure_o4.py` prints and writes in its JSON line the controls' mean, population SD and **z = (M − mean)/SD**, for
information only: z is NOT a criterion and does not change the verdict of §4.

## 6. Outcome
- PASS: P is read by sense from the decode (Daniel's 95 % rule, #728 strict: S/P/R/I); R may then be decoded and read as
  supporting data. The target's share is recomputed; result proposed to WAINUT/Daniel with credit, only with Brice's go.
- FAIL: nothing on P is a validated text; the decode is kept as data; P is burnt. R stays fresh (unopened) for a possible O5.
- In both cases RESULTAT-O4.md gives the chain of hashes with times, agreement, arbitration counts, extension log (if any),
  M, controls, z, and any execution point, as in RESULTAT-O3.
