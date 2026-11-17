# Key scope

`key/code_B_table.tsv` is an **attestation index**, not the period key. It holds 344 groups: 330 code groups (1-699)
and 3 large numerals aligned by the solver with the clear text Casgrain printed under Bougainville's two cipher letters
(Collection des manuscrits du maréchal de Lévis III, 1890, pp. 103-108 and 112-114), plus the 11 groups the 1758 letter
uses that those letters never print. Each row keeps every printed occurrence with the text aligned there and the
solver's conflicts; a value seen once is only as good as the alignment around it.

Fourteen values are marked `inferred`: eleven groups not printed in the letters, and three (4, 448, 524) printed but
not with the value the 1758 letter needs. They come from the code's alphabetical order and from sense, and no test
has been run on them. A word of the reading that rests on one is marked `[?word]` and not counted as read.

The period key, "Pièces militaires No V" in Casgrain's note, was not located. Casgrain printed the cipher and its
clear text; Andrew Beling, with AI agents, built this index from them in November 2026.

Not the other Montcalm codes: code I (`targets/montcalm1758i`, the Marine's table) and code W
(`targets/montcalm1757w`, the War code) share no values with it beyond chance, nor does the Vaudreuil table of
ANOM C11E 10.
