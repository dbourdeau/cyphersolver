# Blind re-readings of sign shapes, 11 Nov 2026 (follow-up to PR #212)

Key K4 (`key_K4.tsv`, SHA-256 b39635fe...) is unchanged. Only the transcription of ff. 67r-67v changed, and only where
Brice Dudout saw a different shape on the DECODE R2253 images. No image, crop or thumbnail is reproduced here.

## How the plates were made
- Format of the plates of 2 Nov (C09, C10): for each question, the line and the sign in question, next to reference
  shapes cut from other places of the same hand (atlas of sign shapes). Brice picks the shape he sees; no letter value,
  no decoding and no gloss are shown. Questions in random order (fixed seeds), with control questions whose answer is
  known from Mousset's edited letters (3 March and 1 April 1590, ff. 64-65v and 68-69).
- For each plate, the integration rule (what each answer does to the transcription, to the reading and to the count)
  was written and hashed (SHA-256) before the answers were opened. If one control failed, nothing would be integrated.
  Each answer applies to that one occurrence only; the key is never changed.

## The three plates
1. **FL2-L** (rule e141240c...; answers fea7c3ab...): 13 questions + 2 controls. Controls 2/2.
   The questions were the signs on which the machine proposals of a Claude Fable 5.2 run (text only, no image) depended.
   Result: 3 of its 9 first-tier readings confirmed by the shape seen ({semblable}, {Lesdiguieres}, {n'obiectant}),
   6 refuted (the readings d'enuoier, legation, aiant, aulcune, continuent and "[l]e duc" stay unresolved: Fable's
   "closed alpha = n" is refuted three times). The three long s asked about, transcribed TS (t), are all LS (m): one gives
   "{demande} secours" instead of "de {tant} de secours", the other two stay inside unresolved segments. F67r-03: the sign
   transcribed {ZR|ZO} is NEW_ZB (ff, already in K4): "{s'offre}".
   Two other first-tier proposals that depend on no doubtful sign were not posed and are kept as probable, as the rule
   written in advance says: "{qu'on} ce {lassera}" (count-neutral) and "{de} {me} {uoir}" (was ‹demeuoir|1›).
2. **TS/LS, plates A and B** (rule 8f2a7618..., script 6fb90179...; answers A 60803f9f..., B 3f4b3c2c...): every
   occurrence of the looped long s (TS = t) in the letter, 76 occurrences, against the plain long s (LS = m), + 6 controls.
   Controls 6/6. 69 TS confirmed, 2 hesitations {LS|TS} seen LS (no effect on the reading), 5 "other shape": three of them are a crossed o (below),
   two (in "etc" and "et") were set to "?" until plate 3. The plates could only confirm the transcription or lose words;
   none was gained.
3. **ox-1** (rule 1d423023..., script ac2fc97c..., amendment 4d2844b4... before the answers; answers 66ea6fa0...):
   8 questions + 2 controls. Controls 2/2. The "crossed o" of plate 2 is OX (o), a sign already in K4.
   Checked first outside the letter, on the reserved part of the 1 April letter (L1): OX stands for o 42 times out of 44
   in Mousset's text (prediction written in advance: at least 70%); TS is never opposite an o (0/76).
   The three occurrences are inside unresolved segments, which stay unresolved (‹augoulernee|2›, ‹meconltinlera|2›,
   ‹pouii|1›). The two "?" of plate 2 are TS seen on the image: {etc} and {et} come back as probable.

## Count (Daniel Bourdeau's rule)
| stage | words | certain | probable | restored | unresolved | certain + probable |
|---|---|---|---|---|---|---|
| PR #212, first commit (2 Nov) | | | | | | 85.8% |
| PR #212 as merged (2 Nov, second plate C10) | 481 | 313 | 102 | 8 | 58 | 86.3% |
| after FL2-L | 478 | 310 | 107 | 8 | 53 | 87.2% |
| after TS/LS A+B | 478 | 310 | 105 | 8 | 55 | 86.8% |
| after ox-1 (this version) | 478 | 310 | 107 | 8 | 53 | **87.2%** |

All counts are on the same letter, ff. 67r-67v only (the letters of 1 April and 3 March are never counted).
The word total moves from 481 to 478 because five passages are segmented differently (see `reading.md`).
Still below 95%: read in part.

## Declared limits
- Words unblocked by a re-read shape count at best as probable, never certain.
- The Fable 5.2 proposals were seen before the plates; on the plates the shapes, not the proposals, decided.
  "{lassera}" and "{de} {me} {uoir}" rest on the proposal and the key only (no doubtful sign in them).
- The identity of the crossed o was formed on the three unresolved words themselves; the only independent test is the
  one on L1 (42/44), and the plate settled the shape.
