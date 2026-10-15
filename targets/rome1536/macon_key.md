# Mascon's cipher (Charles Hémard de Denonville, cardinal de Mâcon, Rome 1535-1537)

Sources: G. Lasry's table for BnF fr. 3071 f. 9 (keyimg/BnF_fr3071_f9.png); S. Tomokiyo's reconstruction from
BnF fr. 3053 (keyimg/francisMacon.png; Tomokiyo's "Cipher-3 (1536)", a different Mâcon table, is keyimg/francisMacon3.png, and his second fr. 3053 table, the R4248 cipher, is targets/r4248/img/francisMacon2.png; cryptiana "francis.htm", section "BnF fr.3053 (1535-1537)").
Homophonic substitution, one glyph = one letter (plus a few doubled-letter signs), nulls, and a small code list.
No word division; the scribe leaves small gaps that often (not always) fall at word breaks.

ASCII aliases used in the transcription (decoder: `work_macon/dm.py`).

| plain | glyph (description) | alias |
|---|---|---|
| A | "3" | `3` |
| A | "8" | `8` |
| A | plain cross "+" | `+` |
| B | "7/Z" with a flat top and short foot (Z-like) | `z` |
| C | "4" (open, with descender) | `4` |
| C | small hook "⌐" / "r" | `c` |
| D | long "ʃ / 5" (s-shaped stroke) | `5` |
| E | "9" | `9` |
| E | small ring with a long tail to the right "o—" | `o` |
| E | ring with a small cross/bar above "ծ" | `b` |
| F | cross with two bars and a loop on top ("ᵽ" with bars) | `F` |
| G | "5/ʕ" with a hook (like a 5 with a curled foot) | `g` |
| H | "ϑ / 8 open" | `h` |
| I | triangle "Δ" (open, or filled) | `A` |
| I | slanted bar "λ / \\" | `L` |
| I | "# / ++" (two crossed double bars) | `H` |
| L | "10" | `l` |
| L | "×" (saltire) | `X` |
| LL | small square "□" (with dot) | `W` |
| M | "1 / ı" (single short stroke, often doubled "11") | `1` |
| M | "ꝗ" (9 or 7 with a crossbar on the descender) | `M` |
| N | "7" | `7` |
| N | big curly X "ꭓ / ✗✗" | `N` |
| O | long "ƒ" | `f` |
| O | "D" (closed box-like D) | `D` |
| P | "≠ / ǂ" (vertical stroke with two short bars, no loop) | `=` |
| P | tall hairpin "∩ / ∏" (two long downstrokes joined at top) | `P` |
| PP | "ꝏ / ω" (w-shaped) | `w` |
| Q | "ᴧa / ꭤ" (a caret joined to an a) | `q` |
| R | "27 / ʑ7" (2 above a 7) | `R` |
| R | "ɼ" small r with a dot on both sides ("·r·") | `r` |
| RR | "Ξ on a stem" (triple bar with a vertical) | `E` |
| S | "6" | `6` |
| S | "∞ / ꝏ" with a ball (horizontal eight) | `C` |
| S | reversed "ϑ / ɗ" | `s` |
| SS | "6 with a vertical" ("ɓ / ƃ") | `S` |
| T | large oval with an inner hook ("Ꮆ / G-loop") | `G` |
| T | curly saltire "Ӿ" (X with hooks) | `T` |
| U/V | "£ / ⱡ" (bar crossed by one or two short bars) | `U` |
| U/V | superscript "m" over a "5/ʒ" ("ᵐ₅") | `m` |
| U/V | bow-tie / heart "⋈" (filled) | `V` |
| X | "Ω / ꭥ" | `x` |
| ET | "fe / fc" ligature | `&` |
| null | "·r·" dotted small r (Tomokiyo) - see note | `n` |
| null | "c—" hook with a long tail; "E" | `~` |

Code groups (Tomokiyo): `30` = pape, `40` = (le) roy. Written with the digits clearly as a pair (not "3" + "o").

## Notes and corrections found while reading fr. 3071 no. 4

* The letter table above was checked against Lasry's glyph table (keyimg/BnF_fr3071_f9.png, enlarged in work_macon/kA-kF.png)
  and reads French throughout f. 9r lines 3-25 with no substitution change needed. Confirmed in running text:
  A = 3/8/+, C = 4, D = 5, E = 9 / ring-with-tail / ring-with-cross, I = triangle / slanted bar / #, L = 10 / x,
  N = 7, O = f / D, P = hairpin / double-barred stroke, R = "27" / dotted r, S = 6 / reversed 9, T = big looped G / curly X,
  U/V = pound-sign / superscript m over 5 / bow-tie, RR = triple bar on stem ("pierre", "corrompre", "Novarre", "declarer").
* **New code group: `20` = l'Empereur** (inferred, not in the tables): "a la devotion du dict 20", "se declarer
  partial de 20"; context (pope drifting to the Emperor's side if the marriages go ahead) leaves no real alternative.
* `30` = pape (glossed "le dict pappe" interlinear by a contemporary decipherer at f. 9r l. 4); `40` = roy
  ("la confederation du 40 avec le Turc").
* The dotted small r ("·r·") often appears where no letter is needed (after "au" in "audict", after "t" in
  "tseigneur", at line ends): treated as a null here, in agreement with Tomokiyo's null list. Where it must be R
  ("r r" in "corrompre"?) the double form probably reads RR rather than R+R: uncertain.
* The long "ſ / ∫" hairpin with one or two long descenders is P (not a null); a doubled "ſſ" at a word start on f. 9v
  may be a separate sign (unresolved; marked `[ſſ]`).
* Hard pairs in this hand: "4" (C) vs "24/27" (R) - the R sign is often written so compactly it looks like a 4,
  causing "declacant" for "declarant", "craindce" for "craindre"; "q" (M, 9 with crossbar) vs "ᴧa" (Q) - in l. 25
  "ce qu'il" came out "ce iuil", i.e. the q-sign was misread by me as the slanted-bar I; "7" (N) vs "q" (M).
