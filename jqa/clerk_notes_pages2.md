# Clerk interlinear decodes, second batch (22 Sept 2026)

Frames on the NOTES.md to-do list (0047, 0056-57, 0211, 0228-0229, 0233, 0247), plus the neighbouring frames of
the same despatches.

| file | frames | pairs | notes |
|---|---|---|---|
| `clerk_0047.tsv` | 0047 right leaf, 21 code lines (1811: Kurakin's remonstrance, the annexation, the tariff) | 325 | the whole leaf is glossed; bilevel image; M where digits are blotted or the clerk wrote one word over several groups |
| `clerk_0048b.tsv` | 0048 left leaf, top block L1-L4 (groups not already in `clerk_0048.tsv`) and middle block L5-L8 ('possibility of their passage through the sound or the belt ... Baltic') | 84 | line ends lost in the gutter |
| `clerk_0210_0211.tsv` | 0210 right leaf, last 3 lines, and 0211 lines 1-9 (1812: Finland, the French subsidy offer, Sweden) | 132 | 0211 lines 5-9 are blotted by bleed-through; many groups there not read |
| `clerk_0247.tsv` | 0247 (No. 98, 17 Oct 1812), first two code lines only | 19 | faint pencil gloss; the lower six lines carry no decode, only stray marks |

**No interlinear decode:**
- 0056 and 0057 are clear text: the Department's decyphered copy of No. 46 ('Mr Adams No 46 decyphered', header on
  0055R). They are a clear page, not a gloss. Ford vol. 4 prints the text (Kamensky/Bagration passage, ford04 l. 4042).
- 0228, 0229 and 0233 are No. 95 (St Petersburg, 30 Sept 1812), the code text only, with no gloss. The Department's
  decyphered copy is on 0230-0232 ('Mr Adams No 95', clear, in the Department's order). Ford 4:~390 prints it
  (ford04 l. 18811). About 800 groups could be aligned with `align.py`. This is the best remaining source for the
  No. 88 open groups (see below).

## Readings that differ from code_table.tsv (graded H here; the coordinator should check these first)
- 220 = 'probab' in 'probab-le' (0047R19, over 220 586, 'it is probable that'); the table has 'proper' from 0184R11.
  Both may be right, if 220 = prob/prop is misread in one of the two places. Check the crop.
- 70 = 'commerce' (0047R19 and R20, 'treaty of commerce'); the table has 'necessary'.
- 94 = 'negotiation' (0047R15, R20); the table has 'therefore' (C).
- 1393 = 'these' (0047R14); the table has 'they'.
- 648 = 'million(s)' (0210R3, twice); the table has 'April'.
- 1162 = 'without' (0211L4); the table has 'way(s)' M.
- 1063 = 'cour' (0247, dis-cour-age); the table has 'cure'.
- 178 'hos' (hos-ti-li-ty), 1302 'ca' (ami-ca-ble), 148 'iff' (tar-iff), 458 'ues' (contin-ues) are all 0047.
- New numbers are listed by the checker; notable ones: 1303 back (twice), 1522 again, 45 principal, 20 ministers,
  39 Sweden (three times), 1432 joint, 993 francs, 341 Fin(land).
