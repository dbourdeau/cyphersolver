# R9614 recount, before and after the sign plate of 25 Nov 2026

Counter: `scripts/count_reading.py`, unchanged. Before = `R9614_reading.txt` on `main` (2134221795). After = the same file
with `sanchez1522-planche-2511.patch` applied.

| | words | sure | probable | probable† | restored | unresolved | sure / words (README rule) | (sure + probable) / words |
|---|---|---|---|---|---|---|---|---|
| before | 1,258 | 785 | 187 | 131 | 0 | 155 | 62.4 % | 77.3 % |
| after | 1,256 | **844** | 204 | 53 | 0 | 155 | **67.2 %** | **83.4 %** |

- 78 words leave probable† (one sign to be taken as another): 61 become sure, 17 probable. The 155 unresolved words
  do not move.
- Two words counted twice in the 12 Nov reading are dropped: "el" 208r.16 (the tokens `veg 9 #` spell "ello") and "lo"
  208v.27 (the tokens `oo n t4 gp #` spell "danyo"). Hence 1,258 -> 1,256 words.
- Cautious variant: if the 45 sure words that hold only by the y value of the small sign were kept probable, sure would be
  799 (63.6 %); sure + probable stays 83.4 %.

Per page (after): 208r 152 S / 236 (64.4 %), 208v 176 / 251 (70.1 %), 209r 147 / 215 (68.4 %), 209v 152 / 246 (61.8 %),
210r 173 / 245 (70.6 %), 210v 44 / 63 (69.8 %).

External check (not used to read any word): word alignment with the clerk's decipherment of R9613, the same letter
(`scripts/cmp9613.py`, `R9614_vs_R9613.txt`): sure words aligned equal 674/785 = 85.9 % before, 727/844 = 86.1 % after
(equal or near 88.4 % -> 89.0 %): 59 more sure words, 53 more aligned equal.

**Status: still "read in part".** Daniel's threshold (95 % of words read by sense) is not reached on any measure.
