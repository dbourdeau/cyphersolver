# chomentowski1713, R7476 p. 32: the twin digits 4 / 7 checked by a blind reader (sheet 2411e, Brice Dudout with Claude, 24 Nov 2026)

Status: in progress (a proposal on R7476 p. 32; Daniel's files and the state of R7476 are unchanged and left to the maintainer).
Next step: a visual pass on every 14x/17x, 24x/27x and 4x/7x group of R7476 pp. 31-34 with the hooked-7 rule, then re-run the explicit-hole score.

This sub-folder adds to Daniel's folder without touching its files. The key (`../syllabary.tsv`) is unchanged and no value
is added. Images: DECODE R7476 (Archiwum Narodowe w Krakowie, Zbiór Dzieduszyckich 26/32 nr 13), used privately;
**no image is committed**.

## The sheet (`sign_check/`)
`../R7476.txt` notes the 7 / 4 of this hand as ambiguous (N*). Brice Dudout read 11 questions on p. 32: 8 targets and 3
controls. Each showed one boxed digit and three thumbnail forms (angular 4, hooked figure, 9), with no values and no
readings. The selection rule (`sheet-2411e-rule.md`, in French, byte for byte, SHA-256 1ab7f943...) was hashed before
the thumbnails were made; the key (`sheet-2411e-key.json`, boxes only) was opened after the answers
(`sheet-2411e-answers.json`) were exported. **Controls 3/3.** Results: `sheet-2411e-results.tsv`.

## What the answers settle
The hand has two shapes: an angular 4, and a hooked figure that is its 7 (the "closed 7" of passes 4-6).
- Confirmed 4: p.32 L28 44 (both digits, Chocim), L16 141 (li), L27 142.
- Confirmed 7: L24 47 (d).
- **Hooked 7 where the transcription has 4** (proposed corrections, to be marked `!` in `../R7476.txt`):

| place | transcribed | read | value | effect |
|---|---|---|---|---|
| p.32 L13 | 141 | **171** | na | "... także wyjeżdżał **na** [...] Han [...]" (pass-4 "wyjeżdżali" becomes "wyjeżdżał na"); the faint gloss reads na |
| p.32 L24 | 244 | **247** | sa | "lecz nie maią do [?od] **samego** re[224]tcie ...": 247 154 85 = sa-me-go, the word of p.33 L26, where 244 was already taken "for sa" |
| p.32 L25 | 240 | **270** | t | no letter changes (240 was already read t) |

"od" (180 47) is spelt by the key, but the cut "do | od" comes from sense only: **[?od]**, {probable}.

## Count (cipher tokens read, base 1,621, convention of pass 7)
| | unresolved | read | share |
|---|---|---|---|
| before (pass 7, NOTES.md) | 83 | 1,538 | 94.9% |
| after the sheet (na, samego) | 79 | **1,542** | **95.1%** |
| with [?od] {probable} | 77 | 1,544 | 95.2% |

No word that was already read breaks. **The document's state does not follow from this count**: R7476 was set to
decoded, not read on 23 Oct 2026 by the explicit-hole score (v2, 0.524 < 0.60). **That score (0.524) has not been
re-run** on the corrected reading, so we claim no change of state.

## The reader's remark ("4 without the bottom stroke", q01 and q02)
It is a variant of the same 4, not a separate sign: the foot stroke comes and goes within one group (L28 44, L16 244),
and both remarked places carry sure 4-words (140 le, plenipotent; 44 Chocim). For the visual pass, the criterion is
the head (angle = 4, hook = 7), not the foot.

## Not changed (needs the visual pass first)
With the hooked 7 now a reading rule for this hand, several conflicts in `../syllabary.tsv` look like 7s read as 4:
240 glossed t (= 270 t, 13 places), 142 glossed ne (= 172), 245 glossed to/ta (= 275/272), 244 glossed sa/ty
(= 247/274). Nothing was changed there.

## Credit
- Blind reader of the digit shapes: Brice Dudout.
- Selection rule, sheet and integration: Claude (AI agent).
- Transcription, key and reading: Daniel Bourdeau; contemporary interlinear glosses. Images: DECODE R7476, not republished.
