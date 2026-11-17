# Audit of the Costabili 1491-92 entry ("catalogue 348"), 16 Nov 2026

Asked: is the Costabili entry (DECODE R1162-R1168) wrongly `open`? For each letter, is a decipherment filed with it,
and is it printed in clear? Per-letter results and evidence are in `findings.json`. Images are in `img/` (git-ignored).

## The entry is not in the catalogue

The Costabili entry was added as 348 on 20 Oct 2026. It was renumbered 361 on 21 Oct (commit 19d1d4ee13), because 348
was already the Szembek postscript. On 2 Nov 2026 it was removed by legacy vetting batch L09 with verdict `partly_read`
(commit c4880d390a). The record is kept in `research/vetting_2026-10/removed_2026-11-02.json` as id 361.

Neither 348 nor 361 is in `catalogue.json`, here or in the main checkout. Lead 1900 was right to say "catalogue 361".
The b14 correction ("should read catalogue 348") is wrong and should be reversed.

## Results

| DF | DECODE | ASMo b. 2 | date | status | what is filed |
|---|---|---|---|---|---|
| 295908 | R1162 | 1491 no. 6 | 27 Feb 1491 | decipherment filed | interlinear gloss over every cipher group (recto); verso clear |
| 295909 | R1163 = R1164 | 1491 no. 7 | 17 Mar 1491 | decipherment filed | cipher slip (no. 8) attached to a clear letter, with a clear decipherment slip (no. 7) laid on it |
| 295914-a | R1165 | 1491 no. 12a | 15 Jun 1491 | decipherment filed | clear copy no. 12b = DF 295914 of the whole ciphered recto |
| 295935 | R1166 | 1491 no. 16 | 21 Jun 1491 | decipherment filed (partial) | interlinear glosses over most lines; about 4 cipher lines unglossed (2 on f. 1r, 2 on the last page) |
| 295963 | R1167 | 1491 no. 44a | 22 Dec 1491 | decipherment filed | clear copy no. 44b = DF 295963-a, same incipit and explicit (4 pp.) |
| 295974 | R1168 | 1492 no. 8 | 20 (+22/23) Mar 1492 | printed | Berzeviczy 1914 no. CLV in clear ("Titkos írásjegyekkel írva"); also interlinear glosses and clear copy no. 8c = DF 295974-3 |

Notes on the list:

- R1165 is not one of the DF numbers the entry or the lead gave. Vestigia files it as DF 295914-a. DF 295914 itself is
  its clear copy, 12b.
- Lasry's GL.htm and Tomokiyo's unsolved.htm have no Costabili item.
- Berzeviczy 1914 prints no Costabili letter of 1491 (its table of contents was read in the OCR).
- MDE Mátyás IV stops in 1490.

## Recommendation: close

Each of the six despatches has a decipherment filed with it, and R1168 is also in print. The only cipher with no
decipherment seen is about four lines of DF 295935. They use the same sign substitution, and the glosses on the same
leaf give the key to read them.

`catalogue.json` needs no change, since the entry left it on 2 Nov. Two things are owed:

- Reverse the 348/361 correction in lead 1900 and in the b14 README.
- Optionally, update the removed record's `partly_read` note with these facts.

## What was not seen

- Kuffart 2018 and Berzeviczy 1908 were not opened.
- The second Vestigia photo sets (ASMo filenames `1427...`) were not viewed page by page.
- Not viewed: DF 295974 images 2-9, 8c images 2-4, and 44b images 2-4.
- DECODE pages were not re-fetched. The R-number to DF mapping rests on date, ASMo number and page count.

## Scripts

- `vdoc.py <vestigia_id,...> [--img]` fetches the Vestigia document page and prints the record, notes, links
  (related, enclosed, parent) and image list. With `--img` it also saves the images to `img/`.
- The b14 scripts `vdf.py` and `vsub.py` (search by DF and sub-record) were reused by hand for the `-a/-b/-1..-3` probes.
