# Codebook — page (3), letter-like symbol script (blind transcription)

Each image shows ONE line (LINE nn) in two parts (part 1 = left half, part 2 = right half; part 2 starts with about one glyph that repeats the end of part 1: write it once). Ignore pieces of the lines above/below. Some lower lines begin with a glyph lying SIDEWAYS (rotated 90°) at the far left: that belongs to a margin column, write it as {M} and do not try to name it.
The images are made of 50-px vertical slices: small steps at slice joins are artefacts.

Write each glyph with the ASCII name below (the glyphs look like letters, digits or Greek letters; the name only says what it looks like):
| name | looks like |
|---|---|
| 7 | ¬ : horizontal stroke then a vertical stroke going down on the right (like a 7 or ˥) |
| 2 | digit 2 |
| 3 | digit 3 / ʒ with a flat top |
| 4 | digit 4 |
| g | latin g (round head, long descending tail) |
| h | latin h, possibly with a small curl inside the bowl |
| k | like h/k with a loop or a kick on the right side (ƙ). If you cannot see a consistent difference between h and k on this page, use h everywhere and say so. |
| + | a cross / ⊥ with a curved left foot (ɫ, ⊥, †); usually written low |
| W | the large Ψ / ш-like cup glyph (three upstrokes, sometimes with hooks) |
| z | ξ (a ladder of 2-3 stacked curls with a tail) |
| a | α (alpha) |
| d | ∂ / d with a curled top going left |
| w | ω (omega) |
| f | φ (phi) |
| Q | θ (theta) |
| b | b or 6 (a loop with a tall stem) |
| y | ϒ / ɣ / ŷ-like (a two-armed cup on a stem) |
| P | a ʒ joined to a ¬ (looks like Ʒ7 written as one glyph) |
| N | a Π / ı¬ (short left leg, top bar, longer right leg), often with a dot above |
| . | a free-standing dot (write it as its own token, also when it sits right after a glyph like + .) |

If a glyph fits none of these, invent a new name of the form #1, #2 … and describe it once in a comment line at the end of the file (`# #1 = …`). Uncertain glyph: add ? (e.g. h?). Unreadable: ?
Output: one row per LINE: `nn<TAB>g 7 2 4 h …` (glyph names separated by single spaces, left to right, part 1 then part 2).
Do not guess letters or meanings. Do not use any other transcription.

## Names added after the two blind passes (for the arbiter)
- J = small ʔ/ʒ-like hook ending in a heavy dot at the foot (pass 1 called it #1, pass 2 #2)
- 8 = figure-8 glyph of two stacked closed loops
- a γ-like 7 with a long tail curving down-left is written 7 (pass 1 had named it #2)
- free-standing dots are dropped from the comparison
