# R9614 recount, before and after the second sign plate of 25 Nov 2026 (2511b, `oo` / `OO`)

Counter: `scripts/count_reading.py`, unchanged. Before = `R9614_reading.txt` with `sanchez1522-planche-2511.patch` applied.
After = the same file with `sanchez1522-planche-2511b.patch` applied on top.

| | words | sure | probable | probable† | restored | unresolved | sure / words (README rule) | (sure + probable) / words |
|---|---|---|---|---|---|---|---|---|
| main (2134221795) | 1,258 | 785 | 187 | 131 | 0 | 155 | 62.4 % | 77.3 % |
| after plate 2511 | 1,256 | 844 | 204 | 53 | 0 | 155 | 67.2 % | 83.4 % |
| after plate 2511b | 1,254 | **845** | **213** | 45 | 0 | **151** | **67.4 %** | **84.4 %** |

- 22 lines change; 14 words change status or reading, 8 unresolved words only change their raw spelling.
- probable† -> probable: *tregua* ×6, *entregar*; probable† -> sure: *gascones*. Unresolved -> sure: *gana*;
  unresolved -> probable: *postigo*, *Pregay* (a proper name, so taken from the sense and kept probable).
- Two merges (two words fewer): "al <dvnas>" -> *algunas* (sure; code al + g v n a s, split over 208r.15-16) and
  "en danyo" -> *enganyo* = *engaño* (sure, 208v.27).
- One wrong sure word corrected: 210r.26 *de* -> *ge* ("yo ge los dixe"; R9613 "yo ge les"). The sure but wrong *danyo* of
  208v.27 goes into *enganyo*.

Per page (after): 208r 152 S / 235 (64.7 %), 208v 176 / 250 (70.4 %), 209r 147 / 215 (68.4 %), 209v 153 / 246 (62.2 %),
210r 173 / 245 (70.6 %), 210v 44 / 63 (69.8 %).

External check (not used to read any word), `scripts/cmp9613.py`: sure words aligned equal with R9613's decipherment
727/844 = 86.1 % -> 730/845 = 86.4 % (equal or near 89.0 % -> 89.5 %).

**Status: still "read in part".** Daniel's threshold (95 % of words read by sense) is not reached on any measure.
