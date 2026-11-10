# 1901 General Staff outgoing table (grid), as stated by Harumi-Matsuba (issue #374) and re-implemented in decode.py

Two digits per kana; tens digit = vowel row, units digit = consonant column.

| | tens digit | units digit |
|---|---|---|
| lower half 01-50 | 0 a, 1 i, 2 u, 3 e, 4 o | 1 vowel kana, 2 k, 3 g, 4 s, 5 z, 6 t, 7 d, 8 n, 9 h, 0 b (b column = 10 20 30 40 50) |
| upper half 51-95 | 5 a, 6 i, 7 u, 8 e, 9 o | 1 p, 2 m, 3 y, 4 r; 55 = ワ, 65 = ン |

Examples: ア01 カ02 バ10 シ14 ウ21 オ41 ノ48 ボ50 パ51 マ52 ワ55 ミ62 リ64 ン65 ヨ93. ヲ is sent as オ (41).

Values seen in the drafts but not in the table: 59, 60, 80, 89, 99 (ten occurrences), probably word codes (contributor's conjecture,
unconfirmed). 22 table values never occur in the drafts and are filled from the rule only. Units 6-8 of the upper half and
75, 85, 95 are unknown.

Not the serial table (00-67) of the incoming telegrams of the same months (issue #371); `decode.py` prints that table's decode beside
each run: 21 of 148 pairs fall outside its range and the rest give no words.
