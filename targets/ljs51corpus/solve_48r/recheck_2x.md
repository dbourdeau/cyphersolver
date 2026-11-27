# 2x recheck of the 48r l.8 - 48v l.13 disagreements (27 Nov 2026)

Masters 0084_0100 (f. 48r) and 0084_0101 (f. 48v), lines cropped at 2x, right and left halves:
`output/ljs51/crops/solve48r/x2_48r09_R.jpg` ... `x2_48v13_L.jpg`, stacked `x2_*_RL.jpg`, `x2_48v10_start.jpg`
(line start of 48v10), `x2_cmp_OM.jpg` (the OM signs of 48v02 and 48v08 side by side).
Positions are counted right to left, dividers not counted, as in `transcription.txt`.

## Flagged positions

| Line | Position | What is on the page | Verdict |
|---|---|---|---|
| 48r09 | #10 W surplus; ا dropped before #12 | HK W Q CR, all clear: the cipher writes ا ل ا ك ا ن ف (الاكانف) for الاكناف. The ا and ن are swapped, not an extra sign | scribal slip (transposition) |
| 48r10 | ب dropped before #4 | v HH AY TB W: nothing between AY and TB, no erasure | scribal slip (وطيها for وطيبها) |
| 48r11 | #5 TH surplus | two identical TH signs side by side, both clear | scribal slip (dittography, تتجافاها) |
| 48r12 | ل dropped before #5 | W TT X W E, no sign between W and TT. The TT here carries a hooked ascender on its right end that the TT of 48v01 lacks; it does not look like X (ل) | cannot tell (probably a slip, اصلاح; the hook may be a correction) |
| 48v02 | #4 SL, ه dropped, #6 O8 | TH SL SW O8 TB W is clear: the cipher reads ترميها. The DP disagreement comes from the record's توهمها | scribal reading confirmed, transcription right (record variant) |
| 48v02 | #8 W surplus | only one W after the divider: a small W written below the line (interlinear insertion) before X. The transcription has two (`W W X`) | **transcription error**: one W too many |
| 48v06 | #4 TB, ع dropped | v TBL TB TB W: the two triangle-over-bars signs are identical, nothing between them. The cipher reads وجهها for وجمعها | scribal variant (or slip) |
| 48v08 | #5 OM -> ق | a three-pronged cup, the same shape as the OM of العسي in 48v02 (`x2_cmp_OM.jpg`). Transcription right | key: OM is ق, not ع. Then 48v02 reads القسي ("the bows", with وتطعنها الاسنه "the spears"), not the record's العسي[?] |
| 48v09 | #6 O8, #7 E | O8 E SW R2 clear: يحمد; the record has وخمد | record variant, transcription right |
| 48v10 | م ا dropped before #2 | a fainter SW stands at the line start before W (missed), and the SW transcribed after the divider is written above the line over that divider (interlinear). Page: SW W / O8 S SW / CR O8 = ما يذم في | **transcription error**: SW missing at line start; the interlinear SW belongs to يذم |
| 48v12 | #11 HK -> م | the last sign is the zigzag SW, not HK (the HK of #6 in the same line is the different ح-like shape) | **transcription error**: HK -> SW |
| 48v13 | ا dropped before #1 | X is the first sign; nothing at the line start | scribal slip (جملها) |
| 48v13 | #5 W surplus | SL TRV TB W: there is no W between SL and TRV | **transcription error**: W not on the page |

## Divider corrections (no change to the signs)

- 48r10: no divider between SW and TRV (مباح is one group); a divider stands between E and LM (missed).
- 48r13: no divider between TBL and Q (جن).
- 48v03: no divider between X and W (الاسنه).
- 48v04: no divider after v (وهي).
- 48v05: no divider between W and TB (اهل).

## Recount (signs / dividers), v1 -> v2

48r08 12/1; 48r09 12/2; 48r10 12/4; 48r11 12/2; 48r12 10/2; 48r13 12/5 -> 12/4; 48v01 12/2;
48v02 14/3 -> 13/3; 48v03 12/2 -> 12/1; 48v04 12/5 -> 12/4; 48v05 11/3 -> 11/2; 48v06 10/3; 48v07 14/1;
48v08 13/4; 48v09 12/2; 48v10 13/4 -> 14/4; 48v11 12/2; 48v12 11/2; 48v13 13/2 -> 12/2. Total 229 -> 228 signs.

## Result

`transcription_v2.txt`, `verify_v2.py` (writes `key_48r_v2.json`, not `key_48r.json`): 228 signs, 220 take
their key letter (96.5%; v1 218 of 229, 95.2%), 3 surplus, 7 dropped. The remaining mismatches are the record's
readings (توهمها, وخمد, العسي) and the scribal slips above; against ترميها / يحمد / القسي the only true
disagreements left are the slips (الاكانف, وطيها, تتجافاها, اصلاح, وجهها, جملها) and the omitted ها-ا in منه ما.
Note: `verify.py` crashes on a cp1252 console after its first line (run with PYTHONUTF8=1).
