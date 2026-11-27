# Proposal for `targets/magdeburg1647` (LASA A 1 Nr. 530, No. 29, view 244): blind sheet E, the last g/q places (25 Nov 2026)

For Malcolm McBratney (blind16 transcription and judge, PRs #524, #558, #688) and A. J. Beling (PR #578), copy Daniel
Bourdeau. Brice Dudout reviews this before anything is sent. It follows sheet D (same folder, same method).

**No image, crop or derivative is included.** The LASA licence forbids publishing or passing on reproductions without
written permission. Box coordinates in `sheet-E-key.json` are pixels of the 2500 x 2024 view 244.

## Credit
The transcription, the judge and the frozen key are McBratney's (`blind16/`, `blind16/FREEZE/key_upstream.tsv`). Prior
work on the target is Beling's. This proposal changes none of their files. It updates only our own folder,
`dudout/no29_fr244_sign_check/`.

## Why this sheet
Sheet D left three g/q places on view 244: L40 "ghx" (cum), L7 "ggflizglrb" (contractis, two failing letters) and L22
"ggfliz" (contra). L22 had been seen as g on sheet A, but that box (12 x 25 px) cut off the tail, which is what tells g
(tail curled to the left) from q (straight tail), and sheet A had no valid g control. So L22 was asked again with a box
around the whole letter. The rule was written and hashed before any thumbnail was cut (`sheet-E-rule.md`, SHA-256
2081e579...). The box amendment (`sheet-E-rule-amendment.md`: the L40 box was narrowed to keep out the next h and a stroke
of line 41) was made before the answers. The key was opened after the answers were exported (`sheet-E-answers.json`).

## Controls: 3/3
The g of "bqfedif" (L25, 2nd), the initial q of "ghrhrb" (L38) and the g of "ozifrbqf" (L29, 7th). All three are sure words
decided on sheet D, and none was used as a control or example before.

## Results (4 targets, one sign per question)

| line | transcribed (letter) | seen | decoded with the frozen key | judge reading | status |
|---|---|---|---|---|---|
| L40 | ghx (1st g) | q | cum | cum | sure |
| L7 | ggflizglrb (1st g) | q | contractis (with the 7th) | contractis | sure |
| L7 | ggflizglrb (7th g) | q | contractis (with the 1st) | contractis | sure |
| L22 | ggfliz (1st g), sheet A place asked again | g | oontra | contra | unchanged, E |

- L7 is counted only because both letters were seen as q, as the rule required.
- **L22**: g seen a second time, now with the whole letter boxed and valid g controls. The scribe wrote g (o) where the
  text needs c; the word stays E. It is the only group initial seen as g out of seven asked (sheets D and E).
- Decision: g and q stay two signs. No key value changes.

## Count (view 244, 432 rows of judge.tsv; your judge, unchanged)
- Words read: 257 -> **259 (59.5% -> 60.0%)**.
- Letters: E 110 -> 107; S 2035 -> 2038 (83.5% -> 83.6% of 2438).
- By category, after sheet E: 218 sure (50.5%; was 216); 41 {probable}; 76 restored (was 78); 39 unresolved;
  58 symbols or blots with no value.
- Below 95%: the status stays **decoded, not read**.
- With sheet E the g/q family of view 244 is done: the only places left are L4 "xzguld" and L22 "ggfliz", both seen as
  transcribed.
- This is a new pass on view 244 only. The record figure of the first pass (77.4% on views 244-245) is unchanged.

## Files (all in `dudout/no29_fr244_sign_check/`)
- New:
  - `sheet-E-rule.md` and `sheet-E-rule-amendment.md` (French, byte for byte as hashed);
  - `sheet-E-key.json`, `sheet-E-answers.json` and `sheet-E-results.tsv` (French column names, as for A-D);
  - `count-after-sheet-E.json`;
  - `sheet-E.patch` (the 2 changed rows of `judge_fr244_after.tsv`);
  - this file.
- Updated: `judge_fr244_after.tsv` (2 rows, `change` column), `README.md` (sheet E section, counts) and `SHA256SUMS.txt`.

## Next
- An eye check of the sheet C extension, family by family.
- View 245.

Blind reader: Brice Dudout. Sheet built, scored and integrated by Claude (AI agent).
