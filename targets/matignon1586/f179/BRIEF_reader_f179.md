# Brief: sign-by-sign reading of Matignon's Cipher-3, BnF fr. 15571 f. 179 (1585–86)

You read a French letter enciphered with a known homophonic table. Output LETTERS, one per cipher sign, in order.
Do not write words, do not smooth into French, and do not fill gaps by guessing what the sentence "should" say.

## Key (S. Tomokiyo's reconstruction): open `key/henryiii_Matignon3.png` first
- **Layout:** the header row is the plaintext letter; the signs below it are its homophones.
- **Word signs** (bottom strip):
  - 60 = faire
  - a β-like "de" sign = de
  - 20 = la
  - 18 = le
  - a p with a stroke (or a hooked z) = pour
  - a big C enclosing n = que
  - ∴ = qui
- **Boxes:** n, t and u have variant y-shapes.
- **Nulls column:** v.

## Additions noted by Tomokiyo for THIS leaf (margin of his working image)
- Z-shaped sign → o
- ξ → e
- n-shape → e
- t-shape → r
- X → j (i)
- L with a loop or bar (Ɫ) → p
- ω → t

## Conventions verified on the sibling leaf f. 276 (same cipher, maybe a different hand: use them as hints)
- **a, n:**
  - `o`-shaped sign = a; `ꝑ` (p with tail) = a.
  - η-like sign = n or a.
  - `y` = n or t.
- **e:** the `ʞ`/`k`/`r`-like sign = e; ξ = e.
- **Consonants:**
  - `b` = s; `ß` = s; `ſ` (long s) = b.
  - `⊥` = r; `+` = l; capped `ſſ` = ll.
  - 23 = g; 30 = m; 14 = p.
  - `m` / `£` / `ℓ` = d.
  - `2` = c; c with a hook = h.
  - `∂` = f.
- **u:** 87/57 = u; a C-shape with a small mark inside = u.
- **o and i:**
  - `δ` = o.
  - `θ` (crossed ∂) = i; ζ (z-topped hook) = i; ※ or a two-stroke # = i.
  - ϱ with a hook below = i.
- **Three crossed strokes `###`** = the word "et".
- **Vertical stroke `|`:** it is likely a word separator or null. Write it as `|`.

## Input
- **Line strips:** `f179/crops/L01_0.jpg` … `L21_2.jpg`. There are three overlapping segments per line, left to right; don't repeat signs in the overlaps. A strip may show bits of the neighbouring lines at its top or bottom edge; read only the line in the middle.
- **Whole lines at higher resolution:** `L01_full_hi.jpg` … `L21_full_hi.jpg`.
- **Whole page:** `f179/deskew.jpg` (large).
- **Read only these files and the key image.** No other project files, and no web.

## Output, per line

    L05: d e l e s n e o ... | (letters separated by spaces; word signs as =de =la =le =que =qui =pour =faire =et; unknown sign ?;
         two possible values a/n; separator |)

Then give one line of your best word division for that line in [brackets], as a reading aid only.

Finish with a list of the signs you could not map and where they occur.
