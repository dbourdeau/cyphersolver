# b176 blind second reading: six Biermann-to-Klingenberg drafts, 1675 (Rigsarkivet unit 260195)

**Bottom line:** the blind re-read agrees with the first reader on 95 to 98% of cipher tokens in five letters. The sixth agrees on 85%, or 95% once you leave out a margin block in a different cipher. Blind strict decode quality is 76.8% to 91.2% per letter, and 579/693 = 83.55% across all six. All 12 shuffle runs have 0 of 5,000 shuffles at or above the true score. The main systematic disagreement is H against #: on 4-5x crops the disputed signs show **one bar**, so the first reader's `#` is wrong at the sampled sites.

| letter | b176 tx md5 | token agreement | blind strict S/(S+E+N) | shuffles (seed 20261112 / seed 7) | key adjudications | exposures |
|---|---|---|---|---|---|---|
| 1. 193R-194L [9?] Sep | 112a8fac | 113/118 = 95.76% | 35/(35+5+0) = 35/40 = 87.50% | 0/5000 >= true; true -3.9534; best -4.2129 / -4.2894 | H vs # x2 (517 H K; 1 H E): one bar, b176 right. 461 vs 460: clear 461, b176 right. First reader's 2 extra 'C': I read both as filled blots (deletions), unresolved | E1 (see below) |
| 2. 214R-216R 19 Sep | 5e47f80f | 302/307 = 98.37% | 93/(93+2+7) = 93/102 = 91.18% | 0/5000; true -4.1420; best -4.1970 / -4.2204 | H vs # x2: one bar, b176 right. <t> (plus-cross) vs P: unresolved shape label. Dash after 389 (b176 only) and 'I' after 518 (first only; I took it as overstruck): unresolved | E1 |
| 3. 234R-236L 23 Sep | f416dbf8 | 265/312 = 84.94% (excluding the Delta-family 235L margin, which only b176 transcribed: 265/278 = 95.32%) | 86/(86+15+11) = 86/112 = 76.79% (Delta margin left out as a different cipher) | 0/5000; true -4.1894; best -4.4898 / -4.4997 | H vs # x7: sampled sites one bar, b176 right. 178 vs 78: clear 178, b176 right. 203 vs 200: unresolved. C vs E x2 (no middle bar seen at 3x): b176. <hashK> vs K: overwrite, unresolved. Filled-loop G after L (b176 only): unresolved | E1 |
| 4. 248R-250R after 23 Sep | a2efefae | 371/390 = 95.13% (8+8 of the residue is the same margin block placed at two different points: placement, not reading) | 119/(119+10+12) = 119/141 = 84.40% | 0/5000; true -4.0300; best -4.2898 / -4.3268 | 501 vs 507: clear 507, **first reader right**. 419 vs 414: 419 at 3x, b176. 9 vs G (250): unresolved. <t> vs P: label | E1 |
| 5. 247R loose leaf | b931b5e5 | 134/137 = 97.81% | 41/(41+1+4) = 41/46 = 89.13% | 0/5000; true -4.0500; best -4.3081 / -4.3073 | 210 vs 280: clear 280, **first reader right**. **Both readers missed most of a left-margin cipher insert** keyed by the 3-bar mark over 'y H 78': `124? [blot] 172 E x / 233 [blot] E y K # 461 140`. b176 omitted it; the first reader got only 'x' and '140' | E1 |
| 6. 287R-289L + margin, Mar | 74d69904 | 619/635 = 97.48% | 205/(205+30+17) = 205/252 = 81.35% | 0/5000; true -4.0727; best -4.3471 / -4.3772 | H vs # x8: sampled sites one bar, b176 right. 500 vs 400 (margin): clear 5, b176 right. 520 vs 510: unresolved. L vs t x2 and 112 vs 111: unresolved. X vs x: unresolved | E1 |

**All six combined, strict:** 35+93+86+119+41+205 = 579 S; total units 40+102+112+141+46+252 = 693; 579/693 = **83.55%**.

## Method and checks
- **Images:** each fetched once by plain curl (15 images: 193-194, 214-216, 234-236, 247-250, 287-289). md5s are in IMAGES.md5. Full images deleted at the end and small crops kept.
- **Freezing:** each tx was frozen with `md5sum >> FROZEN.md5; date -u` before any alignment, decode or first-reader file was opened. Freeze times run from 16:30:45Z (letter 1) to 16:47:42Z (letter 6). The session server stopped once during letter 4. Work-in-progress notes were saved first and nothing was lost.
- **Bar counts:** every H/# was bar-counted on 3-5x crops. Signs not in the convention list are in angle brackets: `<I>` (serifed I), `<t>` (plus-shaped cross), `<invT>`, `<hashK>`, `<d>` (plain d), and the Delta-family set on the 235L margin.
- **Clear German:** long clear stretches are summarised as `{..clear..}`. Token agreement therefore counts **cipher tokens only**.
- **Scripts and keys:** scripts and key files were copied after freezing. md5 asserts pass: words e9698159, table 38c7c1e5, kt2.py 4d38a72d. Only paths were changed (sys.path and B in dec_once.py and shuffle_de152.py), and the change is logged. kt2.py is untouched.
- **Decode inputs:** each decode input (dec_in/) is a mechanical copy of the frozen tx. It strips the INS/MARG markers and maps `<I>`->I and `<invT>`->⊥ to match the tool's sign names. Each was decoded once (dec/). Python was run with `-I` throughout.
- **Alignment:** difflib alignment (scripts/align.py) with label-name normalisation only: o/0->O, [->C, umlaut quote marks dropped. Agreement = matched/(matched + replace span + one-sided tokens).
- **Judging:** strict judging was done once and frozen as judge/judged_runs.tsv (md5 appended to FROZEN.md5). Shuffles are in shuf/, with SUMMARY.txt.

## Judging slips noticed after the first pass (not rescored; first-pass figure stands)
- **Letter 4:** `DERoassissantz` was judged der (S) + oassissantz (N). Letter 6 shows `DERo` = "dero", so the better split is dero (S) + assissantz (N).
- **Letter 2:** `VERdonDEN` was judged N and is probably "verbunden" damaged by one sign. The '.' decode output was not counted as a unit.
- **Letter 5:** `GElermut` (N) sits next to the missed margin insert, so the run is incomplete.

## Exposures
- **E1** (logged 16:2x Z, before any transcription): the permitted chart CHART_copybook_H_vs_hash.png labels its rows "H = g" and "# = c". Two key values were seen. No tx existed yet, so there was nothing to freeze. H/# were still read by bar count only.
- **No other exposure before freezing.** First-reader files, sign maps and plaintext were first opened after all six were frozen.
- **Nothing else was touched:** no b165/b166/b172/stamps/reports/FILE_NOW files and no GitHub pages. Nothing was sent or posted.
