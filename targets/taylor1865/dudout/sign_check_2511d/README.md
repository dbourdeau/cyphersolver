# Blind sign sheets D and E on vol. 196 fr. 0018, groups 26-49 (25 Nov 2026, Brice Dudout, with Claude)

This sheet continues sheet A of `../sign_check_2411/` (merged in #950) on the telegram of 10 February 1865, Taylor to
Beauregard (NARA RG 109 ch. II vol. 196, frame 0018, naId 45485022). Each target is a glyph where the letter read in the
nov1 alignment differs from the letter the known key (COME RETRIBUTION, offset 0) predicts. The key and the alignment
are unchanged.

Groups 26-49 had no glyph boxes. They were segmented by eye for this sheet. The box of g23p5 from sheet A was off by
one letter and was recomputed. The rule was written and hashed before any thumbnail was cut (`sheet-D-rule.md`, French,
byte for byte as hashed, SHA-256 4b0bc29d...). Amendment 1 only re-cropped two V examples, before any answer. Brice
Dudout saw each target next to real examples of the candidate letters from the same clerk. The forms were unlabelled.
The key (`sheet-D-key.json`) was opened only after the answers (`sheet-D-answers.json`, SHA-256 61d312fe...) were
exported.

## Controls: 3/3
g26p3 L, g39p2 M, g36p1 F (among E / F / F2). All three answered correctly, so the sheet counts.

## Results (12 targets, `sheet-D-results.tsv`; columns in French as in sheet A)
- **Re-read as the key predicts (7).** g29p2 F and g29p5 F (MOBILE), g32p2 L (THAN), g34p1 M (SENT), g35p4 F (EAST),
  g37p1 L (BUT), g48p3 L (FURLOUGHS). The three E / F / F2 answers are F, so the F2 label of sheet A stays on g4p1 alone.
- **Divergences confirmed as the clerk's own (4).** g14p2 I (key G, RETURNING), g23p5 C (key E, LITTLE),
  g27p2 G (key S, SERVICE), g31p1 R (key V, QUICKER; R would decipher as N, "QUICKEN", which does not fit).
- **Left for a follow-up (1).** For g5p1 (BRIGADES, read E, key Z), Brice answered "none / other form" and described
  a sign that looked to him like a mix of T and L, not quite this clerk's Z. It was checked on sheet E before any change.

## Follow-up sheet E: g5p1, a T-L mix or Z?
Rule `sheet-E-rule.md` (SHA-256 of the original 12d17840..., see "Redactions"), 3 targets and 3 controls, all on 0018.
- Targets: g5p1 against Z / T / L; g17p5 and g28p1 (two ordinary-looking Z) against Z / "TL". The "TL" option could only
  show g5p1 itself, as no other such sign exists; the rule declares this.
- Controls 3/3: g32p3 T, g44p1 L, g48p7 T (the last one among Z / "TL" / T).
- Answers (`sheet-E-answers.json`, `sheet-E-results.tsv`): g5p1 = **Z** (T and L rejected), with the remark "forme 2 de
  la question 3" ("option 2 of question 3"). In the key, that option is the "TL" thumbnail, which is g5p1 itself: Brice
  recognised the same sign. g17p5 = Z, g28p1 = Z.
- **Verdict: no separate letter.** g5p1 is this clerk's Z, written once with an irregular stroke (a flat top bar starting
  at the margin rule and a detached foot). No "TL" label enters the alphabet. g5p1 is re-read as the key predicts (Z),
  so the decipherment gives BRI-GADES. BRIGADES stays marked only because of g4p1 (F2, sheet A).

## Effect on 0018 (`owner-files.patch`, not applied; see `recount.md`)
| | before (after #950) | after |
|---|---|---|
| words without [?] | 28/44 | **34/44** |
| re-read glyph stream agreeing with the key | 185/203 | **193/203** (192 after D, 193 after E) |

Now unmarked: MOBILE, THAN, SENT, EAST, BUT, FURLOUGHS (last). The 10 words still marked keep their meaning-based
reading. The telegram is under 300 cipher letters, so, as the rule fixed in advance, this is **not** proposed as a
change to "read": it is a gain in sure words and in the clerk's alphabet. The status is your call.

`owner-files.patch` holds the proposed change to `v196-0018-beauregard_read_measure.txt` and
`v196-0018-beauregard_reading.md` (6 markers removed). We did not edit these files, `profile.json` or `NOTES.md`.
Apply it with `git apply targets/taylor1865/dudout/sign_check_2511d/owner-files.patch` if you agree.

## Redactions
- `sheet-D-answers.json`: Brice's free-text remark on q11 is replaced by "[redacted]". The file therefore differs from
  the exported original, whose SHA-256 is 61d312febcf4500ddea747d09ced5726113ecf8598b0eb94ce5ec3902031b1db.
- `sheet-E-rule.md`: the same remark, quoted in the rule, is replaced by "[citation retirée]". SHA-256 of the original
  rule: 12d17840398aed22eb547e18bdf7b0575aa3a5b5148db51b582701b8550b60e3.
- `sheet-D-key.json`, `sheet-E-key.json`: an internal handling note (`_note`) is removed; nothing else changes.
- `sheet-E-answers.json` is the exported original (SHA-256 c4fef58bda843b07dc7ba644a523c99aad9ad76b6366fbe988b6d72272049194).

No image or crop is committed (NARA, public domain).

## Credit
- Reading and alignment: Bryan Payne (PRs #186, #205) and the nov1 reading integrated here.
- Blind reader of the signs: Brice Dudout.
- Sheet built, scored and integrated by Claude (AI agent). This is not a human_check in the schema sense.
