# Brief: sign-by-sign reading of Matignon's Cipher-3, BnF fr. 15572 f. 276 (1586)

You read a French letter enciphered with a known homophonic table. Output LETTERS, one per cipher sign, in order.
Do not write words, do not smooth into French, do not fill gaps by guessing what the sentence "should" say.

## Key (S. Tomokiyo's reconstruction, `key/henryiii_Matignon3.png`, open it first)
Header row = plaintext letter; the signs below it are its homophones. Bottom strip = word signs:
60 = faire, a β-like "de" sign = de, 20 = la, 18 = le, a p with a stroke (or hooked z) = pour, a big C enclosing n = que, ∴ = qui.
Boxes: n/t/u have variant y-shapes. Nulls column = v.

## Conventions verified on this hand (use them)
- `o`-shaped sign = a ; `ꝑ` (p with tail) = a ; 7-like / η-like short sign = a or n (see table)
- `ʞ`/`k`-like sign = e ; plain `u`-shape = e ; `ξ`/ε = e ; `r`-shape = e
- `b` = s ; `ß` = s ; `ſ` (long s) = b ; `⊥` = r ; `+` = l ; `ſſ` with a cap = ll ; 23 = g ; 30 = m ; 14 = p ; 87/57 = u
- `δ` = o ; a big open hook curve (ɤ/ζ) = o ; `θ` (crossed ∂) = i ; `m` = d ; `ℓ`/`£` = d ; `ʒ` (3 with tail) = u
- `2` = c ; c with a hook = h ; `y` = n or t ; `ϱ` (p-like with loop) = p
- `ß` with a long tail stroke = the word sign "de" ; `C` with a small u/n inside = "que" ; `∴` = "qui"

## Worked example (verified against S. Tomokiyo's published opening)
L01 = la guiolle est en doubte du pu pour les amis de …
L02 = la roussiere sont et grand nombre auec luy …

## Input
Crops: f276/crops/L01_0.jpg … L22_2.jpg (3 overlapping segments per line,
left to right). Whole page for context: f276/slip_ov.jpg.
Read only these files and the key image. No web.

## Output, per line
    L05: d e l e s n e o ... | (letters separated by spaces; word signs as =de =la =le =que =qui =pour =faire; unknown sign ?;
         two possible values a/n)
then one line of your best word division for that line in [brackets], marked as a reading aid only.
Finish with a list of signs you could not map and where they occur.
