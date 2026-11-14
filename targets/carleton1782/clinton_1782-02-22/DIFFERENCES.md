# Witness differences and unresolved readings

The `clear` column in `alignment.tsv` is an **aligned reading**, not an assertion that every number independently produces that word. `W` denotes an unmarked word-code pair; `S` a whole x-marked spelled sequence; `C` unciphered text, including suffixes; `U` unread material. Ditto first coordinates are expanded. Locations identify manuscript columns, not physical line numbers. Editorial unit numbering is continuous and is not a manuscript numbering system.

## Material differences

| Location | Cipher evidence | Quadruplicate clear witness | Consequence |
|---|---|---|---|
| 11.C2 beginning | 21-1 / 23-6 / 12-4 / 5-18 / 11-1 | About a fortnight since an | Locally aligns these five units; 23-6 = a remains suspicious because 9-1 regularly serves a. It is not a hard headword constraint. |
| 11.C2 | 11-1 before Intelligent and Attack | an | Prior Carleton alignment calls this any. Retain an/any family; do not assume exact book headword. |
| 11.C4 introduction | 49-9 / 33-9 / 46-9 / 1-17 / 1-2 | Intelligence has been received since the above by | Prior/frozen values suggest “Intelligence is just received by.” The clear witness expands/rephrases. 49-9 differs from opening 47-9; unresolved numeric or code variant. |
| 11A.C1 | man / 33-9 / 17-1 / KAINTUCK | man, a Virginian at Kain Tuck | Cipher reads “man is at Kaintuck”; it omits the Virginian description. Earlier low-resolution guesses Pittsburk and Fairs Creek were discarded after source enlargement and fixed-key reading. |
| 11A.C3 | clear sets / 3-14 / 13-14 | set off on | 3-14 elsewhere of, here off in context; do not invent a new code. |
| 11A.C4 | WABACHE | Wabashe | Spelling variant retained. |
| 11A.C5 | 9-19 / 20-9 | the information | Prior 9-19 is this: proposed cipher reading “this information.” |
| 11A.C5 | 5-22 and 2-17 | who and returned | Earlier Carleton has whose with se suffix, and returning. These may be flexible inflection/headword uses; exact word-list headwords are not proved. |
| 11B.C1 | 2-2 / 5-19 | by the | 2-2 looks distinct from frequent 1-2 by. Keep provisional; original manuscript may clarify copying error. |
| 11B.C3 | give CANADA / 4-19 / 5-19 / 2-6 | give the French Canada | Cipher order is “give Canada to the French.” |
| 11B.C4 | glaring strip after enough; 4-19 [?] duce | to reduce | U record retains unread prefix/word code. Apparent to code and following it/that/engagement/by are also partly affected. Do not backfill a numeric code from the clear copy. |
| 11B.C4 | after That, apparent 2-5 and 1-2 | this engagement by | No separate this securely located. Allocation of 2-5 to engagement remains provisional under glare. |
| 11B.C4 | visible 2-5 after “to the” | French | Expected 2-6 from repeated French elsewhere. Preserve digit discrepancy; do not establish French = 2-5 or two meanings for this number. |
| 11B ending | H.C. | full subscription H. Clinton | Signature abbreviation; no missing cipher paragraph inferred. |
| p.12 clear continuation | acquaint; not yet; extra money-account sentence | p.9 inform; not; no money-account sentence | Clear witness differences, not part of numeric cipher. |

## Fixed-key spelling discrepancies retained

The key remains byte-for-byte unchanged. Five of 44 spelled units do not exactly match their aligned clear-copy word (allowing i/j and spacing). They are displayed in `spellings.tsv`, not repaired silently:

- Intelligent: copied numerals include three 8-like entries, giving **intllligent**. The expected e would require 14; ambiguous repeated entries require original-manuscript or sharper-copy checking.
- New York: **newyhrk**, because the visible entry is 11-1 rather than expected 11-2.
- Stores: **storis**, apparent 20-14 rather than expected 20-13.
- Wabashe: **wabache**, a plausible historical spelling variation, not necessarily an error.
- agreed: **hggreed**, first entry looks 18-5 rather than 18-1, and two g entries are present. Preserve both features.

Several initial numerical misreadings were corrected after mechanical mismatch prompted source enlargement: Intelligent's second entry 15; New York's first coordinate 18; Schuyler's repeated line 18; Lafayette's line 18 and position 29; Result's position 18; Stores' position 6. This was iterative source-assisted transcription, not blind validation. Uncertain survivors remain visible.

## Book-identity constraints

`word_constraints.tsv` enumerates 100 distinct observed pairs, including qualified associations. It is a lookup constraint table, not a recovered book. No assumed page/line/column interpretation is required beyond the two coordinates in their written order.

Strong whole-word examples to test in a proposed printed source include 12-4 fortnight, 27-9 invade, 23-11 learnt, 15-3 channel, 4-24 yet, 34-14 our, 22-34 waiting, 2-10 know, 26-3 Command, 41-19 two, 51-18 State, 34-17 Regiments, 12-19 Troops, 43-19 Hundred, 23-18 Spaniards, 7-4 Detroit, 45-17 rout, 2-14 Ohio, 22-19 thence, 6-20 up, 41-8 head, 42-15 place, 51-9 induce, 3-20 undertake, 30-1 accounts, 15-7 Garrison, 41-22 weak, 20-9 information, 17-15 Prisoners, 48-18 Some, 17-4 Officers, 17-22 will, 46-8 Combined, 18-18 successfull, 43-18 seen, 49-15 proceedings.

A candidate must explain multiple exact coordinate positions and both letters' shared uses, not merely contain these words. Inflected/archaic spellings and documented suffixes must be tested explicitly. Reserve qualified pairs (23-6, 49-9, 2-2, 2-5, 11-1, 2-17, 5-22, and glare entries) from exact rejection/acceptance criteria until resolved. No candidate printed word list has been identified or tested here.
