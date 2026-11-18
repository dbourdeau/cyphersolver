# Blind look-up of 71 dictionary-code groups in Entick (notes)

Done by one look-up helper (Claude), 14 November 2026, working without being told what the groups mean. Finished at 2026-11-14 21:11 EST. I wrote nothing outside this folder and its `lookup_work/` subfolder.

## Inputs used
- `groups_numbers.tsv` (71 groups; 58 distinct page/column/line positions).
- 1776 London printing: page images in `sources/raw/entick_dictionary/bim_..._1776/pages/`, and the hOCR file.
- 1773 hOCR and 1781 (`11280377bsb`) hOCR, for controls C4 and C5.
- How pages map to hOCR files: 1776 image leaf = page - 1. 1773 hOCR has the same page numbers as 1776, but it is a **different setting**: some columns start one or two entries earlier or later. The 1781 printing has **different pagination** (for example its p.99 is in DES, and pp.425-426 fall in the Pantheon section).
- I did not use the pre-built `table_17xx.tsv` files. I rebuilt word and line lists from the raw hOCR myself (`lookup_work/w17xx.tsv`, `s17xx.tsv`).

## Counting rule, as applied
Line N is the Nth headword entry from the top of the column. I did not count:
- the running head;
- letter headings (the "Y." heading on p.426a);
- run-over lines (an indented definition continuation);
- the signature or catchword line at the foot of the page.

Short overflow fragments set at the right end of a line in brackets, such as "(ning man", "(loam" or "(tation", are not separate lines. A run-over line at the very top of a column, carried over from the previous page, is not an entry (p.290a).

## REAL (1776)
- **35 distinct positions (47 of the 71 group rows) were counted on the page images.** I read each column on an 860-px-wide whole-page view, and zoomed in where needed.
- **23 positions (24 rows) have no 1776 image.** I counted these from the hOCR. The OCR lines were placed on a line grid by their vertical spacing, so a line the OCR lost still takes up a slot. I then read the rows and judged entry or run-over by hand.
- **Confidence:** 36 image rows and 10 OCR rows are firm. 25 rows (20 positions) are doubtful, each with its reason in the table. The main reasons:
  - **Headword hidden in the binding.** Several odd-page a-columns lose the start of every headword in the binding. The count is firm there, but the word was supplied from the visible ending plus its alphabetical neighbours: 63a, 99a, 101a, 163a, 229a, 237a, 255a, 325a, 389a, 425a.
  - **Lines missing from the OCR, with no image to check.** 96b20 (ids 52 and 61), 300b9 (id 14) and 364b23 (id 69) are given as "illegible". 339b37 is ambiguous: either Sink, v. or the entry after it, because the gap is 6.5 line-heights. 356a28 and 356a29: the top of the column is garbled. Also 248b13 and 268b38.
  - **Hard calls on the counting rule:**
    - 229a37: the line "semblance of life" is a hyphenated continuation, but its indent is hidden in the binding. I treated it as a run-over; counting it would give Loamy.
    - 425a17: the line "reverence, adoration" was likewise treated as a run-over.
    - 290a4: the top line "by continued long possession" was treated as a run-over; counting it would give Presence-chamber.
    - 325a25: the second line ("...new flesh", read as Sarcotic) was counted as an entry.
- **Self-check against an earlier automatic count.** A crude automatic counter agreed with my image counts in only about two cases out of three. Its errors were missed run-overs, lost OCR lines and binding bleed. So I did not rely on any automatic count for REAL.

## Controls (C1-C5)
- Each control is marked `[img]` (counted on a page image) or `[ocr]` (counted from hOCR).
- **How the OCR controls were counted.** A script printed a compact list of each column's lines with provisional entry numbers. I then corrected by hand the obvious misclassifications: lost headwords that had been taken as run-overs, run-overs that had been taken as entries, and bleed from the facing page. These remain less reliable than REAL. Expect some to be off by one line, especially those marked "(doubtful)". Where the OCR was too garbled to count, I wrote "illegible".
- **1773 (C4).** Its OCR is much cleaner, and I checked all 58 positions by hand. C4 differs from REAL at 81b20, 82b5, 82b37, 99a17, 101a16, 108a9, 233b9, 332b28 and 382b28, and possibly at 339b37. At least some of these differences look like real resetting between the printings (for example, p.81b in 1773 begins at Ceremonial, Ceremonious, and Cerecloth is not there), not counting error. C4 was not used to fill in any REAL cell. Where it bears on an illegible or doubtful REAL, I say so here:
  - 1773 gives Conclude at 96b20, Quarryman at 300b9, Supporter at 364b23, Sink at 339b37 and Present, a. at 290a4.
  - The 1773 p.364b layout differs, so its Supporter is at line 23, while 1776 has Supporter at line 24.
- **1781 (C5).** Its OCR is poor on many pages. Pages 425 and 426 fall in the Pantheon section, so they are marked n/a.
- **C1 for p.141 and p.301:** these leaves are missing from the 1776 hOCR ("no OCR").

## Technical notes
- **Python flags.** Scripts that only parse the raw hOCR were run with `python3 -I`. The image scripts need PIL, which is installed in the user site-packages that `-I` disables. So I ran those with `python3 -E`, from my own `lookup_work/` folder, reading only the JPEG page images.
- **What I opened, and blinding.** Nothing on the off-limits list was opened. I listed the folder contents of `lee1779_gloss_test/` and of `arthur_lee_1779_2026-11-14/work/`, so I saw file names only (including TEST_PLAN_gloss.md, crops/, groups.tsv and judge_*.tsv). I opened none of them. From the `wt-lee1779` worktree I read only files in `scripts/`. No web access was used.
- **Working files** are in `lookup_work/`: `imgcol.py`, `ov.py`, `zoom.py`, `ocrrows.py`, `cdx.py`, `build.py`, plus the overview images.
