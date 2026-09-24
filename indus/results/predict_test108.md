# Hundred-and-eighth registered predictions: the four genres as systems

- distinct lines 2722; genres {'closer': 228, 'count': 605, 'name': 1233, 'bare': 344, 'other': 312}.

## GS1 signs belong to genres
- genre-specific signs ({'name': 15, 'count': 1, 'closer': 5}): 21 of 138 (15%); threshold at least 30%.
- **GS1 fails.**

## GS2 every genre has its own signs
- genres with specific signs: ['closer', 'count', 'name'].
- **GS2 fails.**

## GS3 the object sets the genre
- F lines: 2475 items; MI 0.0699 bits; p = 0.0001.
- **GS3 holds.**

## GS4 the city sets the genre
- F lines: 1990 items; MI 0.0142 bits; p = 0.0001.
- **GS4 holds.**

## GS5 the period sets the genre
- Harappa lines: 485 items; MI 0.0029 bits; p = 0.7372.
- **GS5 fails.**

## GS6 closers write like names
- Jaccard name-closer 0.318, name-count 0.430.
- **GS6 fails.**

## GS7 bare lines write like counts
- Jaccard bare-count 0.448, bare-name 0.387.
- **GS7 holds.**

## GS8 the genre sets the length
- lines: 2410 items; MI 0.1246 bits; p = 0.0001.
- **GS8 holds.**

## GS9 the first sign tells the genre
- lines: 2231 items; MI 0.3860 bits; p = 0.0001.
- **GS9 holds.**

## GS10 the last sign tells more
- MI last 1.344 (p = 0.0001), first 0.386 (p = 0.0001).
- **GS10 holds.**

## GS11 one object, one genre
- multi-line objects 76; all one genre 15; p = 0.7204.
- **GS11 fails.**

## GS12 seals carry names
- seal lines that are names or closers: 942 of 1594 (59%); threshold at least 70%.
- **GS12 fails.**

## GS13 incised tablets count
- count or bare, TAB:I 80 of 196 (40.8%) against 130 of 355 (36.6%), p = 0.1895.
- **GS13 fails.**

## GS14 potsherds count or label
- potsherd lines that are bare or counts: 87 of 180 (48%); threshold at least 70%.
- **GS14 fails.**

## GS15 the small sites write the same genres
- MI 0.0106; p = 0.0001.
- **GS15 fails.**

## GS16 genre signs are rare
- shared against specific signs: 117 against 21; means 57.59 and 107.62; rank difference +4.0; p = 0.3315.
- **GS16 fails.**

## GS17 count signs come from blocks 1 and 3
- block 1 or 3, count-specific 0 of 1 (0.0%) against 6 of 20 (30.0%), p = 1.0000.
- **GS17 fails.**

## GS18 signs belong to genres (B)
- genre-specific signs ({'name': 6, 'closer': 1}): 7 of 74 (9%); threshold at least 30%.
- **GS18 fails.**

## GS19 the genre sets the length (B)
- lines: 837 items; MI 0.1117 bits; p = 0.0001.
- **GS19 holds.**

## GS20 signs belong to genres (F')
- genre-specific signs ({'name': 24, 'closer': 6, 'other': 1}): 31 of 116 (27%); threshold at least 30%.
- **GS20 fails.**

## Summary

Held: GS3, GS4, GS7, GS8, GS9, GS10, GS19. Failed: GS1, GS2, GS5, GS6, GS11, GS12, GS13, GS14, GS15, GS16, GS17, GS18, GS20.
