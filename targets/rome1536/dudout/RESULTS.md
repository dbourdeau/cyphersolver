# rome1536 / R4234: blind shape sheets rome1536-2511 and rome1536-2511b (25 Nov 2026), results

By Brice Dudout (with Claude). The reading edits are applied to `pass5/R4234_reading.md` in this PR. The same
diff is also in `R4234_reading.patch`.

## Method
- Each sheet has a selection rule (French), hashed before its images were cut:
  - `REGLE-SELECTION.md`, SHA-256 `db28edb934d31c94f7f22dff95b0483538e1a560f92c56eb9694065fb53c2724`
  - `REGLE-SELECTION-b.md`, SHA-256 `bf9965e6a14457e7cb44d557bf9742afc92fa3167640027e53f689d539c3027b`

  Both files are included unchanged.
- Each question showed the line with the sign boxed, the sign enlarged, and shape exemplars cut from places where
  context makes the value sure. Sheet a showed one exemplar per option, sheet b two.
- Options showed shapes only, never values, plus "none / other", "cannot tell", "illegible" and "not a sign".
- Questions were shuffled and hidden controls were mixed in.
- Images: Gallica native scans of BnF fr. 3053 (ark btv1b90601432, views 32-36). The images are not included.
- One reader (Brice Dudout). Answers are in `answers-rome1536-2511.json` and `answers-rome1536-2511b.json`. The map
  from options to signs is in `planche_key.json` and `planche_key_b.json`.

## Controls: 5 / 5 passed
- Sheet a: `fe` = ET, `+` = A+, big looped ꭓ of "toutes" = Tx.
- Sheet b: D and 27 (R) of "induire".
- Control K3 of rule b (the G of "seigneur", f16r L3) was dropped before sheet b was built: that G is drawn like the
  slanted D, so it would have had a look-alike option.

## Questions
| item | place | rule says | answer | applied |
|---|---|---|---|---|
| Q2 (a) | f16v L2 | Nx -> "cause, **ennemi** mortel" | Nx | yes |
| Q3 + Q4 (a) | f16v L27 | Of + Up -> "qu'il **debvoit** mettre" | Of, Up | yes |
| Q7 (a) | f18r L22 | FF -> "quelques **offres**" | FF | yes |
| Q8 (a) | f16r L10 | Up -> "au **dire** dudict evesque" | Up | yes |
| Q1 (a, then b) | f16r L1 | Gh -> "par **argent**" | a: Gh, but the reader asked "same sign?"; b: Gh | yes, from b |
| Q5 (a, then b) | f17r L21 | Gh -> "con[g]noisse" | D5 both times | no (status quo) |
| Q6 (a, then b) | f18r L16 | R27 -> "en parler a autre" | a: none (the R27 exemplar was flawed); b: C4 | no (status quo) |

Caveat on G: Q1 counts the upright compact 5 as G. That holds for the exemplars "ung" and "gentilhomme" (f17r
L5), but the G of "seigneur" (f16r L3) is drawn slanted like D, so not every G is compact. *Argent* also fits the
sense: "s'en accorder par argent avec l'Empereur".

## Word divisions (no sheet; signs as transcribed in pass 5, checked on the Gallica native)
- f16v L7: "par talladie(?) [?] l'intention [?]" -> "**part a la di{-e}stribution** des benefices". The cipher
  writes *diestribution*.
- f18r L17: "il y a de ma[n]iere(?)" -> "**il y va de ma vie**" (`I L10 I# Up A3 | D5 Eo Mq A+ Up I# Eo`).
- Not applied: f17v L6 "soubz vostre correction" is probable only.

## Score (research/reading_audit/v2_score.py, fr, explicit holes)
| | words | holes | read_share |
|---|---|---|---|
| before | 1,256 | 74 | 0.941 |
| after the two sheets and the two word divisions | 1,256 | 66 | **0.947** |

After: about 29 unresolved holes, 9 probable `(?)` and 20 supplied `[word]`.

Per folio: f16r 0.954, f16v 0.938, f17r 0.922, f17v 0.962, f18r 0.960, f18v 0.958.

**R4234 stays read in part (0.947, under the 0.95 bar). It needs about 4 more words, which no single-sign
question left in this letter can supply. f16r, f17v, f18r and f18v each read at 95 % or more.**
