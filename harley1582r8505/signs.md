# Sign chart, Harley 1582 ff. 263-264 (DECODE R8505)

ASCII names used in all transcriptions. Calibration examples (crops in img/, read by hand) at the bottom.

| name | shape |
|---|---|
| L | right angle L |
| 7 | reversed L / 7 hook (bar on top, stem down on right) |
| Gm | Gamma: stem with bar to the right on top (Γ) |
| X | chi, long left-hand stroke (sometimes with a small loop at lower left) |
| Xo | lambda/chi with a small o hanging at its right (ƛo), one sign |
| psi | psi / Y cup on a stem |
| w | omega with a flat bar over it (ϖ) |
| wT | same with a vertical/cross stroke through the top (ϖ with t) |
| w0 | plain round omega ω, no bar |
| wf | omega joined to a long-s/f stroke (ωʃ), written as one unit |
| f | tall long-s with a hook top, no omega (ʃ / ƒ) |
| G | 9 / G-shaped loop with descender |
| n | eta (η), n with long right leg |
| U | double-u with a tail (Ʋ / ꝝ-like, "vv") |
| Usq | square-bottomed single U (⊔) |
| o | small circle with a lead-in tail/dash from the left (—o, σ) |
| u | open cup / c with left tail (ᴗ-, ɕ), not closed |
| B | beta β |
| b | small loop at the foot of an ascender (like ♭ / ƀ / 'b' without a bowl on the right) |
| dd | c with ascender on the right (Latin d shape, ᑯ, "c|") |
| d | delta ∂-loop crossed by a long vertical stroke (looks like a crossed 'd' with loop, ǂ∂) |
| Oi | small circle with a vertical stroke through it (Ф / ⦶) |
| phi | phi: loop on a long stem (φ, large) |
| q | 4-like / q with bar across the stem (ꝗ / ϙ) |
| E | epsilon ε |
| Eb | epsilon/ ∈ crossed by a vertical stroke (Ɛ|) |
| # | two verticals, two horizontals |
| H | two verticals, one horizontal crossing (ⵜⵜ, ⧺) |
| ne | one vertical, two horizontals (ǂ) |
| F | one vertical with two horizontals only to one side (≠/F-like) |
| T | inverted T with a loop at the right foot (⊥ with loop, 'ъ'-like) |
| Pi | Pi Π |
| PiG | Pi with an extra stroke/hook on the right (ΠΓ, 'm'-like) |
| sh | Cyrillic sha Ш (three-pronged) |
| hg | hourglass ⧗ (X closed top and bottom) |
| cy | c+y ligature with a long curling descender (one sign) |
| y | plain y |
| c | small open c |
| I | I-beam bar with serifs |
| + | small cross |
| II | two short vertical bars (could be the number 11) |
Numbers are written between dots: .81. .21. .51. -> transcribe as #81 #21 #51.
Dot groups: `..` two dots, `.:.` or `∴` three/four dots -> transcribe as `:` (a separate token).

Transcription format (one line per MS line containing cipher):
`<page>.<line#> | clear before | S I G N S space separated | clear after`
Unsure: `name?`; alternatives: `a/b?`; illegible: `?`. Where there is a visible gap between sign groups write ` / `.

## Calibration (f.263r, hand-read)
- "Joinct que" Xo 7 : / psi X / wf G / Xo n / U Gm o B
- next line: L b d # T Pi sh q f 7 w o Gm : L b wf X wT L E L o d # T #81 7 B phi q u Xo n E wf L b ne 7 o Eb H Gm #21
- next: Oi X psi f Gm o dd w | vers les exemples et eschantillons | hg T G Xo 7 b : Pi o E B wT L | donne grand | Xo q U wf w 7 E T
- "a tant paty" PiG f # 7 E b Pi q T L Oi f F dd : X sh n ne q #81 Pi f # L E : psi b Usq Gm w dd Gm U # Gm E

## Corrections from the second reading of f.264v (p4), after the break

Three distinctions the chart above did not make. They are the reason no sign in `ct_p1..p4.txt`
mapped to **m** or **b**, and why `b`/`T` and `E` were self-contradictory.

| name | shape | letter | was read as |
|---|---|---|---|
| `:2` `:3` `:4` | the **dot groups** (two, three, four dots). A letter, not punctuation; all three counts behave alike. The count is kept only so the question can be re-opened. | **m** | `:` (treated as a separator) |
| `phi` | φ — a closed **oval pierced by a long vertical stem**, stem visible above *and* below the oval | **b** | `phi`, but mixed with `f` |
| `f` | ƒ/ʃ — a tall long-s: hook/loop at the **top of the stem only**, often with a short cross-bar to the left; nothing pierces a closed oval | u | `phi` |
| `E3` | ε — epsilon with **two bowls** open to the left ("reversed 3"), no crossing stroke | **s** | `E` |
| `E` | ϵ — **lunate** epsilon, a C with one middle bar | a | `E` |
| `Eb` | ε with a long vertical through it | t | (unchanged) |
| `T` | ъ — stem with a short **bar to the left at the top** and a closed loop at the foot | u | `b` |
| `b` | stem with a closed loop at the foot and **no top bar** | n | `b` |

Controls: `7 Eb :2 psi G o B Gm b Tu o wf` = "et **m**aintenant"; `Xo psi :3 G B dd 7` = "l'a**m**itié";
`:4 PiG b n c Gm q wT ne L` = "**M**onsieur de"; end of 4.4 + start of 4.5 = "de **b**eau|caire"
(Beaucaire on the Rhône); p2 l.17 `... T b Gm phi sh b o 7 E wT` = "d'une **b**onne ar[mée]";
`Gm E3 wf w Pi u Eb L` = "e**s**troite"; `b Gm J L E3 n psi dd w L` = "nece**ss**aire".
