# Hundred-and-thirty-seventh registered predictions: sign shapes

- glyphs rendered 698; rare 304, common 82.

## SH1 rare signs are compounds
- rare compounds 51 of 304 (17%) against common 9 of 82 (11%); p = 0.1310.
- **SH1 fails.**

## SH2 a compound stands where its base stands
- bases among frame-mates 4 of 51 (chance about 6.1).
- **SH2 fails.**

## SH3 look-alikes keep company
- pairs 1500; Spearman 0.005; p = 0.4216 (1,000 shuffles).
- **SH3 fails.**

## SH4 catalogue neighbours look alike
- adjacent-number against random pairs: 576 against 1728; means 0.37 and 0.19; rank difference +809.2; p = 0.0001.
- **SH4 holds.**

## SH5 the free variants look alike
- mean IoU 0.566; 95th percentile of random pairs 0.302.
- **SH5 holds.**

## SH6 fish look alike
- members 20; mean IoU 0.323; p = 0.0010 (1,000 random sets).
- **SH6 holds.**

## SH7 the 520 heads look fishy
- 520 against 740 non-fish heads, best IoU with a fish: 4 against 60; means 0.23 and 0.25; rank difference -12.0; p = 0.8872.
- **SH7 fails.**

## SH8 closers look alike
- members 11; mean IoU 0.231; p = 0.0100 (1,000 random sets).
- **SH8 holds.**

## SH9 rare signs are more complex
- rare against common ink: 304 against 82; means 336.34 and 283.99; rank difference +47.1; p = 0.0007.
- **SH9 holds.**

## SH10 compounds keep the base position
- compound tokens in the base sign's usual position: 28 of 75 (37%); threshold at least 60%.
- **SH10 fails.**

- example compounds: 103>100, 117>90, 121>90, 122>142, 123>90, 126>90, 127>125, 133>90, 138>90, 141>140, 145>90, 168>520, 172>440, 228>220, 256>520.
## Summary

Held: SH4, SH5, SH6, SH8, SH9. Failed: SH1, SH2, SH3, SH7, SH10.
