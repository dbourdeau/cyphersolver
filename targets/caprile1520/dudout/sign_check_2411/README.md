# caprile1520: blind sign-shape sheet 2411 (R1139 / R1136), 24 Nov 2026

**Who did what**
- Reader: Brice Dudout (Europe chiffrée).
- Sheet: built and scored by AI agents (Claude), so it is not a `human_check`.
- Images: DECODE R1139 and R1136, looked at privately. No image or crop is committed.

**Files in this folder**
- `sheet-2411-rule.md`: the selection rule, in French, as hashed (SHA-256 f3424253…8438). It was written before any thumbnail was cut and before the answers.
- `sheet-2411-key.json`: the answer key, opened only after the answers.
- `sheet-2411-answers.json`: the answers (SHA-256 eb7246a7…07f1).
- `sheet-2411-results.tsv`: the results table.
- `R1139_count_728.tsv` and `R1136_count_728.tsv`: our own word-level application of the #728 rule. This is not Daniel's sentence figure.
- `proposed-alphabet/`: a working copy with 4, crossed y (yb) and crossed q (q+) as three signs. It is a proposal only. `key21.json`, the transcriptions and the readings of the target are unchanged.

**Sheet fault:** box A4 (R1136 L12) was enlarged after the rule was hashed, so that it includes the stem. It is the same sign at the same place, and it has no effect on the result.

## Results (9 signs, 3 of 3 controls)

| place | label | answer | consequence |
|---|---|---|---|
| R1139 L01 "z 4 o" | 4 | crossed y | "com[e]" is carried by y = e; no value for 4 is needed there (proposed relabel 4 -> y) |
| R1139 L01 end "4 8 1 7" | 4 | 4 | confirmed |
| R1136 L10 "QB 4 x" | 4 | 4 | confirmed |
| R1136 L12 "4 Z" | 4 | 4 | confirmed |
| R1139 L04 | q+ | neither, remark "crossed q" | its own form, not 4, not crossed y, not plain q |
| R1139 L06 | q? | neither, remark "crossed q" | same; proposed q? -> q+ |
| R1139 L07 end | q+ | neither, no remark | unresolved |
| R1139 L03 | p+ | crossed p | p+ = p (= n in key21), to be tested; the s given there by sense ("si n'e intrato") is not supported |
| R1139 L07 end "1 1" | 1 1 | u | proposed U (= g in key21); the stretch still gives no word |

The 4 / q+ / crossed-y family is not one sign, so no merge is proposed. A later look through both pages found one more crossed q, at R1136 L05 "QB [q+] D T PHI", inside an unread stretch.

**{probable}, by sense only:** q+ = a at the two places that are read: "[?a] de che vi scrivi" (L04) and "meser [?a] Alfonso" (L06). That is the value of plain q, so the crossed q may just be a variant of q.

## Count (word level, #728)

| | sure | {probable} | restored | unresolved |
|---|---|---|---|---|
| R1139 before | 118 | 11 | 1 | 10 |
| R1139 after | 119 | 10 | 1 | 10 |
| R1136 | 80 | 3 | 0 | 31 |

- R1139: the 140 cipher words go from 118 to 119 sure (84.3% to 85.0%). The only new word is "come".
- R1136: unchanged out of 114 words.
- Both texts stay decoded, not read.

**Caveat:** key21 groups crossed y with plain y. "come" therefore rests on the grouped value e. The sheet shows the shape, not the value.
