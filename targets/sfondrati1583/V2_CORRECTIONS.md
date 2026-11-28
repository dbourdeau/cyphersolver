# Paleographic v2 Audit Log (`#2077`) & Out-of-Sample `#2518` Summary

## 1. Visually Verified Scan Corrections in `transcript_2077_v2.txt`

`transcript_2077_core.txt` (`3,113` tokens) is preserved untouched for full reproducibility. Every correction below was independently verified at 4× zoom on `v2_audit_spots.png` and `v2_audit_spots2.png` before applying to `transcript_2077_v2.txt` (`3,116` tokens, `+3` from splitting 3 instances of `42.` → `24 2.`):

| # | Location | `v1` (`core`) | `v2` (Scan-Verified) | Visual Basis on 4× Crop |
|---:|---|---|---|---|
| 1 | `Item 6 p1 L04` | `19+` | `19|` | Plain upright `|` after `19` (no crossbar; *Joyosa*) |
| 2 | `Item 6 p1 L09` | `42.` | `24 2.` | Two tokens (`24` + `2.`, *cuydado*) |
| 3 | `Item 6 p1 L12` | `5.` | `5_m` | Dot centered **directly underneath** `5` (vs. mid-height right dot `5.`) |
| 4 | `Item 6 p2 L04` | `{ 21` | `{ 12|` | Crisp upright `1` before `2|` (*y parecer*) |
| 5 | `Item 6 p2 L08` | `5.` | `5_m` | Dot centered **directly underneath** `5` |
| 6 | `Item 6 p2 L15` | `35| 12|` | `35| 12|` *(kept; scan doubt)* | Originally flagged as a candidate for `35| 21` (*jornada*), but `v2` retains `35| 12|` (*haya passado* — where `35| = ya`, `12| = pa` on L15); *jornada* sits earlier on `Item 6 p2 L14` (`5. , 14| 21`). |
| 7 | `Item 16 p1 L01` | `42.` | `24 2.` | Clear `2`-hook + `+` followed by separate `2.` (*procedido*) |
| 8 | `Item 16 p1 L07` | `24 11.` | `22+ 11.` | Clear double-`2` + cross `+` (*termino*) |
| 9 | `Item 16 p2 L21` | `19e^` | `29e^` | Clear initial `2` before `9e^` (*ofrece*) |
| 10 | `Item 16 p2 L23` | `22, 17|` | `22| 13|` | Clear `22|` + `13|` (*maravilladisimo*) |
| 11 | `Item 16 p2 L24` | `19e^` | `29e^` | Clear initial `2` before `9e^` (*ofreciese*); note that `24` on `L24` is *que dio* (kept as `24`), whereas the `24 -> 22+` *comision* (`codision`) candidate sits on `Item 16 p2 L23` (`9. 24 19+ 21'`) and remains a documented scan doubt in `v2`. |
| 12 | `Item 16 p2 L25` | `100~ 24:` | `100~ 22+:` | Clear double-`2` + cross + dot (*100 mil ducados*) |
| 13 | `Item 16 p3 L04` | `42.` | `24 2.` | Clear `2` + `+` followed by separate `2.` (*acudido*) |
| 14 | `Item 16 p3 L13` | `5.` | `5_m` | Dot centered **directly underneath** `5` |
| 15 | `Item 16 p3 L15` | `32| 6.` | `32| 16.` | Crisp upright `1` joined into `6.` (*plazo*) |
| 16 | `Item 21 p2 L04` | `24 4+ 5.` | `22+ 4+ 5.` | Clear double-`2` + `+` (*mi hijo*) |
| 17 | `Item 21 p3 PS02` | `24,` | `22,` | Verifier fix: two `2`s + subscript tick, no crossbar (*margen de*) |
| 18 | `Item 21 p3 PS07` | `24^` | `22|^` | Clear `22|` + `^`, no crossbar (*maritimas*) |
| 19 | `Item 21 p3 PS08` | `12|` | `22|` | Verifier fix: two `2`s + `|` (*yerro de pluma*) |
| 20 | `Item 19 p1 L01` | `12|` | `12@` | Verifier fix: rounded `6`-loop `@` after `12` (*ha podido*) |

---

## 2. Blind Out-of-Sample Companion Sibling: Cat. `#2518` (`5 Oct 1583`)

- **Files:** `transcript_2518.txt`, `diplomatic_2518.txt`, 2.2× rulered crops + high-contrast stain zoom in `crops_2518/`.
- **Exact Counts:** **19 cipher lines** (`17` on `p. 1` incl. bottom-right wrap `sim` + `2` on `p. 2`), **`323` tokens** across **`149` distinct surface types** (`3` water-stain lacunae marked `[stain]` on `p.1 L01–L03`, zero guessing).
- **Notable Features Observed Blind on `#2518`:**
  - Underlined nomenclators: `21=` (2×), `38=` (1×), `38=|,` (1×), `23=^` (1×), `71=^` (1×).
  - Literal-numeral overbars: `5~` (`p1 L02`: `5~ 22+: 71=^`), `10~` (`p1 L04`: `10~ 2e^`).
  - `29`-base tokens: `29e*^` (`p1 L09`), `29|` (`p1 L13`).
  - `CVm`/`CVl` & `CV` codes: `hom` (4), `sim` (3), `hol` (2), `sa` (3), `xa` (2), `xol` (1), `ful` (1), `lim` (1), `com` (1), `him` (1), `gel` (1), `vil` (1), `he` (1), `De` (1), `fo` (1).
  - Exact `#2077` formulaic recurrence: `7^ 26+ 9 14.` (`p1 L07` — 5th verbatim occurrence across letters!).
