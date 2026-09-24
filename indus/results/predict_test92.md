# Ninety-second registered predictions: the jar signs 700, 705, 706

- tokens: 700 312, 705 233, 706 66; context signs 241.

## CF1 705 and 706 keep one company
- cosine 0.399; p = 0.0006.
- **CF1 holds.**

## CF2 700 keeps jar company
- mean cosine 700 to 705/706 0.021; p = 0.8709.
- **CF2 fails.**

## CF3 jars are followed by a number
- 705/706 tokens followed by a numeral: 123 of 233 (53%); threshold at least 50%.
- **CF3 holds.**

## CF4 the number is 33
- numerals after 705/706 that are 33 ({'33': 117, '2': 3, '1': 1, '31': 1}): 117 of 123 (95%); threshold at least 60%.
- **CF4 holds.**

## CF5 jars take long strokes
- long kind, after 705/706 119 of 123 (96.7%) against 299 of 1205 (24.8%), p = 0.0000.
- **CF5 holds.**

## CF6 jars are not counted
- 705/706 tokens after a numeral: 30 of 233 (13%); threshold at most 10%.
- **CF6 fails.**

## CF7 jar lines end in 520
- 705/706 lines ending in 520: 48 of 233 (21%); threshold at least 50%.
- **CF7 fails.**

## CF8 jar lines are on seals
- 705/706 lines on seals: 123 of 169 (73%); threshold at least 70%.
- **CF8 holds.**

## CF9 jars are Mohenjo-daran
- 705/706 lines, Mohenjo-daro 105 of 1215 (8.6%) against 44 of 818 (5.4%), p = 0.0032.
- **CF9 holds.**

## CF10 700 lines are on tablets
- 700 lines on tablets: 51 of 87 (59%); threshold at least 80%.
- **CF10 fails.**

## CF11 705 and 706 are free variants
- tokens with a sign before 173; MI 0.187; p = 0.8129.
- **CF11 holds.**

## CF12 the jar count ends in 520
- sign after '705/706 + numeral' is 520: 46 of 120 (38%); threshold at least 50%.
- **CF12 fails.**

## CF13 the jar count is three
- value 3 in '705/706 N 520' ({3: 46}): 46 of 46 (100%); threshold at least 80%.
- **CF13 holds.**

## CF14 jar lines are names
- 705/706 name lines: 120 of 233 (52%); threshold at least 60%.
- **CF14 fails.**

## CF15 700 is never a name sign
- 700 tokens inside a name body: 7 of 65 (11%); threshold at most 5%.
- **CF15 fails.**

## CF16 33 belongs to the jars
- signs before 33 that are 705/706 ({'705': 88, '706': 29, '711': 4, '717': 3, '171': 2}): 117 of 156 (75%); threshold at least 30%.
- **CF16 holds.**

## CF17 jars are followed by a number (B)
- 705/706 tokens followed by a numeral: 36 of 88 (41%); threshold at least 50%.
- **CF17 fails.**

## CF18 the number is 33 (B)
- numerals after 705/706 that are 33 ({'33': 36}): 36 of 36 (100%); threshold at least 60%.
- **CF18 holds.**

## CF19 the jar count is three (F)
- value 3 in '705/706 N 520' ({3: 37}): 37 of 37 (100%); threshold at least 80%.
- **CF19 holds.**

## CF20 the jars look alike
- categories 700 J, 705 None, 706 I.
- **CF20 fails.**

## Summary

Held: CF1, CF3, CF4, CF5, CF8, CF9, CF11, CF13, CF16, CF18, CF19. Failed: CF2, CF6, CF7, CF10, CF12, CF14, CF15, CF17, CF20.
