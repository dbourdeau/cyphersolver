# CORRECTION · the sealed plan for catalogue 698, v7-M · 17 Nov 2026

*Model-written (M), `claude-opus-5-5`, session `eea13873`. A dated correction, at the desk's two findings on ask 30 (its verdict of 20:05Z on 17 Nov). The sealed text, `visser698/PREREG_visser698_v7M_2026-11-17.md` (SHA-256 `fc31c799649c3844c7a1581df06f3363828051c8d253eca980b5f02c32c1d73a`, stamped 18:38:11Z), stays the record. Neither correction touches the design, the bars, the forecasts or the runs.*

## 1. §8 step 2 still carried the clause that weakness 12 now words otherwise
- **What the sealed text says.** In §8 step 2 (line 123), the cover file's rectangles "give where each sign's rectangle lies on the frame, not which tile is which".
- **Read it as weakness 12 has it,** in the desk's words: "They give where each sign's rectangle lies and, through the band the cover leaves at each place, roughly how tall each sign is. Set against the tiles' heights, that could place some tiles: in the desk's test, at most 8 of 27, with the offset chosen in hindsight. That it was not done rests on this chat's log."
- Draft v6 had the clause in two places, and the desk's verdict of 18:00Z named one of them; the desk prints that as its miss.
- **The match of the tiles** (`visser698/STRIPMATCH_v1.json`, stamped 20:17:52Z and 20:17:53Z) was made from the shapes alone, and no height was measured. That rests on this chat's log.

## 2. §13's `lang/lm.py` is not the file at the commit §15 item 5 names
- **Which `lm.py` §13 means.** The hash §13 gives, `4fc50cdd52276d6820aa79df8e6e5bf484673b4b932d2282581cc04dc407f1b4`, is `lang/lm.py` as the ledger had it from commit `c848f461e` (10 Nov) to the pin, `37fe838406c010e15734125dc0938b760a3d8ca1` (14 Nov). It is kept in this chat's `ledger_pin_37fe8384/lang/lm.py`, whose SHA-256 is the same.
- **It is the file that built the language models.**
  - `visser698/solve/build_lm_v1.py` loads `ledger_pin_37fe8384/lang/lm.py` by its path (its line 39), and writes that file's SHA-256 into each table's metadata as `engine_sha256` (its line 85).
  - `visser698/solve/lm/lm_es_v1.json` and `lm_de_v1.json` both carry `4fc50cdd…`.
  - The English tables are not built with `lm.py`: `lm_en_v1.json` says they are conditionals from the BAPCO plan's joint table.
- **It is not the file at `e857642f`,** which §15 item 5 names as the ledger at the seal. There `lang/lm.py` is `d4f2a016b7905d0c…`, after three changes on 16 Nov: `823a10ee2`, `c3ccf1a7e`, `23f006f8c`. This chat's clone shows each change by its file hash.
- **How to read the plan.** §15 item 5 gives the ledger's state at the seal, not the source of the engine. §1 already says the plan keeps the pin's file.
