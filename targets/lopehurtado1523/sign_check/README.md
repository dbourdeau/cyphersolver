# R9866 / R9868 / R9869: two blind sign-shape sheets (24 Nov 2026, Brice Dudout, with Claude)

The images are DECODE R9866, R9868 and R9869. They are private: no image or crop is in this folder, and they are not
republished. Box coordinates in the keys are pixels of the DECODE images.

Brice Dudout saw each sign with example shapes from the same letters, with no reading and no value. The rules were
written and hashed before the thumbnails, in French, byte for byte as hashed:
- sheet 2411: `sheet-2411-rule.md`, 88168cf5...;
- sheet 2411b: `sheet-2411b-rule.md`, b3f419a4...

Keys were opened only after the answers were exported. The key (`key_merged.tsv`) and the readings are unchanged, and
no value is added. The look-alike families are the ones NOTES lists: barred m = f or c, delta vs barred delta, and the
two- vs three-bar cross.

## Sheet 2411 (15 questions, controls 3/3)
- **Sheet fault.** Two options (a "small delta with hook" and a "two-bar cross") had example crops that each show two
  different signs. The reviewer flagged both and we confirmed it. The barred-delta question (R9866 R14 l18) and the
  five cross questions are therefore **not used**. They were asked again on sheet 2411b.
- **Barred m.** ofendido (R9866 R1 l6), confianca (R9869 R10 l4) and desconfiados (R9868 R10 l3) show the barred m
  (= f, as in the key). reputacion (R9866 R4 l12, read c) shows the long barred f, not the barred m.
  - So "m̶ = f or c" is a label confusion. The proposal is m̶ = f only, and the label f (= c) where c is read.
  - After the sheet, an AI agent looked at every m̶ on the images. R9866 has 1 barred m and 20 long barred f
    (rows in `R9866_corrections.tsv`); R9869's five are barred m; R9868 already writes f.
  - These relabels are an AI look, checked blind at R4 l12 only.
- **R9868 R17 l22 "se puedan":** a barred delta with a tall stem = p, as read.
- **R9866 R3 l9 "to ∂ 8 9 ω m":** the sign is ʋ (m in the key), so the word reads "no **medio** por pocos". This is a
  proposal: R9866 would go 0.823 -> 0.827 if you accept it. The reading files are not changed.

## Sheet 2411b (10 questions, controls 3/3)
- **Three-bar cross = b at all four places asked:**
  - R9866 R13 l14 (buscarian) and R6 l21 (contribuciones): ʇʇ -> ʇʇʇ. Each word keeps one hole for T̄, which has no
    value in the key.
  - R9868 R13 l11 (obedecele): as already in its corrections table.
  - R9869 R11 l6 (buena): as transcribed.
- **Looped H with a long bar.** This is a form of its own, read at R9866 R13 l13 (a-v-r-i-a-n) and at the control R7 l23
  (sacarlo). Both places read a by sense, which matches the "ß-like = a" re-reads. Proposed label: `ʇʇH`, value a
  **{probable}** (sense only; no shape identity with ß is established). The crossed "dièse" sign stays r.
- **R9866 R7 l24 "resistir", 4th sign:** the long barred f (= c), so the signs give "recistir" (a possible spelling)
  where the sense wants s. Flagged, not decided.
- **R9866 R14 l18, first sign:** a looped delta (label `∂b`), a form of its own with no value. The only other place found
  is R9869 R1 l2 ("de B-eure" by sense).

## Count (README convention: cipher words only)

| | R9866 | R9868 | R9869 |
|---|---|---|---|
| before and after | 181/220 = 0.823 | 94/114 = 0.825 | 94/123 = 0.764 |
| if "medio" is adopted | 0.827 | | |

No word is gained or lost, because the words touched were already read or keep another hole. Status: read in part,
unchanged.

## Not proposed yet
- T̄ = u {probable}.
- Looped H = a at two further places (R9866 R3 l9; R6 l22 "sea de ayuda").

Both need a measure on a fresh letter, with a PREREG first (e.g. R9867).

## Credit
- Target, key and readings: Daniel Bourdeau.
- Blind reader of the sign forms: Brice Dudout.
- Sheets built, scored and integrated by Claude (AI agent).
- Images: DECODE R9866, R9868, R9869.
