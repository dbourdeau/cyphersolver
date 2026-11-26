# botti1710: code 17 is q, and some "17" are 12 = r (blind sign sheet 2411d, Brice Dudout with Claude, 24 Nov 2026)

Status: in progress (a proposal on one code of prabal-rje's key; the folder's state is unchanged and left to the maintainer).
Next step: a second sheet on the other "17" tokens that would break sure words if read q (R8469 T006 C19, C22, T003 C09).

This sub-folder adds to prabal-rje's botti1710 folder (PR #824) without touching its files. The key, the transcription
and the frozen decode are prabal-rje's. Credit: DECODE (records R8469, R8470), British Library Add MS 20443.
**No DECODE image is committed** (research use only; the crops stay private).

## The question
`key-and-read/key.tsv` leaves code 17 open ("r or q": the clerk writes r at 66 places, q at 39, l at 11). Zoomed 3-4x,
the second digit of the "17" groups looked like a straight 7 where the context wants q (quale, questa, quanto, qua) and
like this hand's 2 (round head, hooked tail) where it wants r (proprio, risposi). If so, those r places are 12 = r
misread as 17, and the true code 17 is q.

## The sheet (`sign_check/`)
Brice Dudout read 14 questions: 11 target signs and 3 controls. Each showed one boxed digit and three thumbnail forms
(7, 2, 3) from the same hand, with no values and no readings. The selection rule (`sheet-2411d-rule.md`, in French,
byte for byte, SHA-256 5a149cc3...) and its amendment (`sheet-2411d-rule-amendment.md`, 7ce8002e..., one example of 2
replaced before the sheet was served) were hashed before the sheet was shown. The key (`sheet-2411d-key.json`, boxes on
the DECODE pages only) was opened after the answers (`sheet-2411d-answers.json`) were exported. **Controls 3/3.**

## Answers (`sign_check/sheet-2411d-results.tsv`)
- **Digit 7 at 9 sites**: code 17 is there. Every site with a sure context reads q (quanto, quale, questa, qua).
- **Digit 2 at 2 sites** (proprio R8469 T006 C21, risposi T006 C23): these are code 12 = r, misread as 17 in the
  transcription.

## Proposal (all {probable}: the letter value comes from the sense; only the digit's shape is fixed by the reader)
1. Code 17 = q {probable}, instead of "r or q (open)" (`key_proposed_2411d.tsv`, one row changed plus one rule row).
2. Code 10 directly after 17 reads u {probable} (quanto, qui), as in the dotted letters (questo, quale, questa).
3. Transcription: R8469 T006 C21 "5121517u1" -> "5121512u1"; T006 C23 "17u195119u" -> "12u195119u" (sure: r = 12).

| on the 11 target groups, frozen cut | before | after |
|---|---|---|
| groups giving an Italian word | 2 / 11 (proprio, risposi) | **9 / 11** |
| "17" tokens with r or open q | 11 | 0 (9 q, 2 become 12 = r) |
| sure words broken | - | 0 |

Words gained (7, all {probable}): quale x2 (T6C24, T6C09), quanto (T5C16), a quanto (T3C13-14), qui (T5C22, cut 17|10|0),
qua (R8470 T004 C01), questa (T6C21). Still no word: T5C15 "qummosto" (probably a 2 too many, *questo*?) and T5C25
"qiieo".

## Not done
- No global switch of the other "17" tokens: q would break sure words (dinari R8469 T006 C22, rema T006 C19); these are
  probably more 12s misread and need their own sheet. In T003 C09-C10, "1712|1712" cuts 1|7|12 = o-b-r (obrobriosi).
- The dotted letters (255 tokens of code 17, about 100 before a 10) were not recounted on our side.
- The frozen decode is not reproduced byte for byte (its cut is not supplied); the count replays the 13 groups with 17
  found in R8468-R8470 on that cut. The repository's Italian lexicon has "roi": counted as not Italian.

## Credit
- Blind reader of the digit shapes: Brice Dudout.
- Selection rule, sheet and integration: Claude (AI agent).
- Key, transcription and decode: prabal-rje. Images: DECODE R8469, R8470 (British Library Add MS 20443), not republished.
