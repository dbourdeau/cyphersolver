# Proposal for `targets/magdeburg1647` (LASA A 1 Nr. 530, No. 29, view 244): blind sheet D, the g/q/y family (25 Nov 2026)

For Malcolm McBratney (blind16 transcription and judge, PRs #524, #558, #688) and A. J. Beling (PR #578), copy Daniel
Bourdeau. Brice Dudout reviews this before anything is sent. It follows our sheets A, B and C (PR #947, merged).

**No image, crop or derivative is included.** The LASA licence forbids publishing or passing on reproductions without
written permission. Box coordinates in `sheet-D-key.json` are pixels of the 2500 x 2024 view 244.

## Credit
The transcription, the judge and the frozen key are McBratney's (`blind16/`, `blind16/FREEZE/key_upstream.tsv`). Prior
work on the target is Beling's. This proposal changes none of their files. It updates only our own folder,
`dudout/no29_fr244_sign_check/`.

## Why this sheet
Sheets A and B re-entered 13 g->q and 4 q->g. So in this hand the q form (straight tail) is distinct from g (tail curled
to the left). Sheet D checks the rest of the family on view 244. Its targets are words whose only failing letters are
g/q/y. It also asks again the two sheet B places that were badly boxed. The rule was written and hashed before any thumbnail
was cut (`sheet-D-rule.md`, SHA-256 04430d92...). The box amendment (`sheet-D-rule-amendment.md`) was made after the
contact sheet and before the answers. The key was opened after the answers were exported (`sheet-D-answers.json`).

## Controls: 3/3
The q of "zhqu" (L25), the g of "fgqu" (L32) and the initial q of "qzwbzx" (L36). All three are sure words, and none was
used on an earlier sheet.

## Results (12 targets)

| line | transcribed (letter) | seen | decoded with the frozen key | judge reading | status |
|---|---|---|---|---|---|
| L9 | Wtzgdzb (4th g) | q | placeas | placeas | sure |
| L11 | fgguxzutb (3rd g) | q | nochmahls | nochmahls | sure |
| L14 | uggufzquedfqytrqu (3rd g) | q | hochnachdencklich | hochnachdencklich | sure |
| L18 | xgguld (3rd g), sheet B place asked again | q | mochte | mochte | sure |
| L25 | bqfedif (2nd q) | g | sondern | sondern | sure |
| L29 | ozifrbqf (7th q) | g | garnison | garnison | sure |
| L35 | bdghfehx (3rd g) | q | secundum | secundum | sure |
| L38 | ghrhrb (1st g) | q | cuiuis | cuivis | sure |
| L39 | ghx (1st g) | q | cum | cum | sure |
| L42 | yhx (1st y) | q | cum | cum | sure |
| L26 | ggxdf (1st g) | q | comen | komen | {probable} |
| L26 | urdsdhyif (7th y), sheet B place asked again | y | hiebeukrn | hiebevorn | unchanged, E |

Notes on the last two rows and the initials:
- **comen**: Brice saw q, not the y we expected. The frozen key gives "comen", with c for k as in "erclaret" (sheet B) in
  the same hand. The word is counted, marked {probable}.
- **hiebeukrn**: y is confirmed. The scribe wrote y (k) where the text needs o, so the word stays E.
- **Group initials** (L26, L38, L39, L42): all four were seen as q. So these failing initials are slips of the
  transcription between twin forms, not a constant fault of the scribe. The only exception so far is L22 "ggfliz"
  (contra), which Brice saw as g on sheet A.
- **Decision**: g and q stay two signs. Merging them would break sure words. No key value changes.

## Count (view 244, 432 rows of judge.tsv; your judge, unchanged)
- Words read: 246 -> **257 (56.9% -> 59.5%)**.
- Letters: E 121 -> 110; S 2024 -> 2035 (83.0% -> 83.5% of 2438).
- By category, after sheet D:
  - 216 sure (50.0%; was 206);
  - 41 {probable} (was 40);
  - 78 restored, where the judge gives a reading from the sense but the key does not read the word (was 89);
  - 39 unresolved;
  - 58 symbols or blots with no value.
- Below 95%: the status stays **decoded, not read**.
- This is a new pass on view 244 only. The record figure of the first pass (77.4% on views 244-245) is unchanged.

## Files (all in `dudout/no29_fr244_sign_check/`)
- New:
  - `sheet-D-rule.md` and `sheet-D-rule-amendment.md` (French, byte for byte as hashed);
  - `sheet-D-key.json`, `sheet-D-answers.json` and `sheet-D-results.tsv` (French column names, as for A-C);
  - `count-after-sheet-D.json`;
  - `sheet-D.patch` (the 11 changed rows of `judge_fr244_after.tsv`);
  - this file.
- Updated: `judge_fr244_after.tsv` (11 rows, `change` column), `README.md` (sheet D section, counts) and `SHA256SUMS.txt`.

## Next
- Two g->q places were left unasked: L40 "ghx" (cum, the same word as L39) and L7 "ggflizglrb" (contractis, two
  letters). L22 "ggfliz" could be asked again with a checked box.
- An eye check of the sheet C extension, family by family.
- View 245.

Blind reader: Brice Dudout. Sheet built, scored and integrated by Claude (AI agent).
