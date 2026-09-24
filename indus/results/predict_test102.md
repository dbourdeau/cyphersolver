# Hundred-and-second registered predictions: shape blocks and what they do

- signs with a role 138.

## SB1 the block sets the position
- signs: 138 items; MI 0.1518 bits; p = 0.0611.
- **SB1 fails.**

## SB2 the block sets the genre
- tokens: 9229 items; MI 0.0611 bits; p = 0.0001.
- **SB2 holds.**

## SB3 the block sets counting
- tokens: 10031 items; MI 0.0135 bits; p = 0.0001.
- **SB3 holds.**

## SB4 the block sets the class
- classed heads: 70 items; MI 0.2508 bits; p = 0.0015.
- **SB4 holds.**

## SB5 the block sets the medium
- F tokens: 9676 items; MI 0.0263 bits; p = 0.0001.
- **SB5 holds.**

## SB6 the block sets the city
- F tokens: 8948 items; MI 0.0199 bits; p = 0.0001.
- **SB6 holds.**

## SB7 heads come from two blocks
- two commonest blocks ({7: 292, 1: 283, 2: 282, 4: 161}): 575 of 1722 (33%); threshold at least 50%.
- **SB7 fails.**

## SB8 fish are medial
- block-2 fish that are medial: 8 of 10 (80%); threshold at least 80%.
- **SB8 holds.**

## SB9 block 7 is counted
- counted, block-7 tokens 244 of 2273 (10.7%) against 1349 of 7758 (17.4%), p = 1.0000.
- **SB9 fails.**

## SB10 block 8 holds the ends
- specialist, block-8 signs 4 of 18 (22.2%) against 17 of 120 (14.2%), p = 0.2817.
- **SB10 fails.**

## SB11 block 1 heads names
- last body sign, block-1 tokens 283 of 449 (63.0%) against 1439 of 4629 (31.1%), p = 0.0000.
- **SB11 holds.**

## SB12 neighbours come from different blocks
- same-block adjacent pairs 928; p = 1.0000 (1,000 shuffles).
- **SB12 fails.**

## SB13 opener and head from different families
- names 744; different blocks 653; p = 0.9137.
- **SB13 fails.**

## SB14 the block sets the ending
- distinct names: 970 items; MI 0.1967 bits; p = 0.0001.
- **SB14 holds.**

## SB15 block roles hold in B
- blocks with the same majority role: 7 of 7 (100%); threshold at least 80%.
- **SB15 holds.**

## SB16 the category sets the position
- categorised signs: 64 items; MI 0.3384 bits; p = 0.0731.
- **SB16 fails.**

## SB17 the category sets counting
- tokens: 6292 items; MI 0.0440 bits; p = 0.0001.
- **SB17 holds.**

## SB18 block 3 is a formula block
- formula, block-3 tokens 430 of 740 (58.1%) against 3560 of 9291 (38.3%), p = 0.0000.
- **SB18 holds.**

## SB19 block 5 heads more than block 3
- last body sign, block 5 79 of 443 (17.8%) against 141 of 347 (40.6%), p = 1.0000.
- **SB19 fails.**

## SB20 block 9 is rare
- other against block-9 signs: 508 against 31; means 19.00 and 12.23; rank difference +25.9; p = 0.1815.
- **SB20 fails.**

## Summary

Held: SB2, SB3, SB4, SB5, SB6, SB8, SB11, SB14, SB15, SB17, SB18. Failed: SB1, SB7, SB9, SB10, SB12, SB13, SB16, SB19, SB20.
