# BAV Vat. lat. 8214 sweep (2026-11-16)

Run by Andrew Aymeloglu with Claude Code agents (Claude Fable, Claude Opus) on 15 Nov 2026, as part of the work on
catalogue 2368 (f. 298r-v of this volume), written up here as a sweep on 16 Nov 2026 at the maintainer's request on
issue #697: the two new leaves enter as leads through `research/`, not as catalogue entries.

Result: **2 rows** in `candidates.json` (ff. 68r and 198r), both seen on the images, both in the same cipher as
catalogue 2368. Neither row carries a `vetting` block: both are already read in part in `targets/mantua1524`, so
"open" would not be true, and the lead's verdict is left to the project.

## What was searched

- **One volume, paged leaf by leaf**: Biblioteca Apostolica Vaticana, Vat. lat. 8214, all 816 images on DigiVatLib
  (IIIF manifest `https://digi.vatlib.it/iiif/MSS_Vat.lat.8214/manifest.json`), looking for cipher, glosses, clear
  copies of cipher passages and keys. The volume holds letters and extracts sent to Federico II Gonzaga in 1523-24
  and belongs with Castiglione's papers (Vat. lat. 8204-8214 in catalogue 2368's vetting; the contributor counts
  Vat. lat. 8199-8213 as the same bequest).
- Route: DigiVatLib IIIF images at full size (1962 px), fetched 15 Nov 2026; the URLs and SHA-256 of the leaves used
  are in `targets/mantua1524/aaymeloglu/images.tsv`.

## Finds

| Shelfmark | Folios | Date | Who | Cipher | State |
|---|---|---|---|---|---|
| Vat. lat. 8214 | 68r | by 29 Jan 1524 (covering letter, Vat. lat. 8211 fr. 36) | a "we", plausibly Federico II Gonzaga to Castiglione | 23 lines, almost all cipher | seen, bare (A); decoded, not read, in targets/mantua1524 |
| Vat. lat. 8214 | 198r | 8 Apr 1524 | Capino de Capo, Robbio, to Federico II Gonzaga (extract) | 2 lines in 26 of clear text | seen, bare (A); read in part in targets/mantua1524 |

No other page of the volume has cipher, a gloss, a clear copy or a key. f. 298r-v is catalogue 2368 and is not
repeated here.

Also found, in Vat. lat. 8211 (letters to Castiglione, 1523-24; DigiVatLib microfilm scan, 915 px, "Low Quality"),
while looking for a clear copy of 68r. These belong to `targets/mantua1524` (same cipher, same key), where they are
documents marked not read and the text of the held-out test; they are not separate rows here:

| Shelfmark | Frames | Date | Who | Cipher | State |
|---|---|---|---|---|---|
| Vat. lat. 8211 | 36 (old f. 33) | endorsed 29 Jan 1524 | Gian Giacomo Calandra, Mantua, to Castiglione | none: the covering letter of 68r, clear text | context for 68r |
| Vat. lat. 8211 | 72R, 73L, 74R | 30 Mar 1524 | Calandra to Castiglione | long runs within clear text | seen, bare; not read (held-out test, failed its bar) |
| Vat. lat. 8211 | 76R, 78L | Apr 1524 | Calandra to Castiglione | runs within clear text | seen, bare; not read (held-out test) |
| Vat. lat. 8211 | 77 (filmed upside down) | 1524, not read | Calandra? to Castiglione | runs within clear text | seen, bare; not read (held-out test) |

## Duplicates and prior art

- `known.py` on "Cappini", "Capino", "Suardino", "Robbio": no catalogue entry, lead or target for either leaf other
  than `targets/mantua1524`; the "Robbio" hits (G. S. da Robbio, Cremona 1530, in the Milan sweeps) are another man
  and another letter.
- `decode_search.py` on "Vat. lat. 8214", "Gonzaga 1524", "Capino", "Castiglione": no DECODE record of these leaves
  (the two rows returned are unrelated: BL Add MS 20563 and an HHStA key of 1703).
- Benzoni, "Federico II Gonzaga", DBI 45 (1995), describes the 68r episode (blood-dyed urine shown to the physicians,
  admitted to Castiglione, "sano et gagliardo") and cites Vat. lat. 8214; the text he quotes from has not been found
  (see `targets/mantua1524/NOTES.md`, Escalation).
- Tomokiyo and Lasry were not searched for these two leaves beyond the searches recorded for catalogue 2368
  (6 Nov 2026), which found nothing for the volume.

## What is left

- The sibling volumes of Castiglione's papers: Vat. lat. 8211 was checked, frames 1-166 (with the covering letter
  of 68r at fr. 36 and the Calandra letters in this cipher above) and 190-209; its frames 167-189 and 210-575 were not.
  Vat. lat. 8199-8201 and 8210 were sampled only; 8202 is not digitised; 8203-8209 and 8212-8213 were not paged. No
  clear copy or decipherment of 68r was found.
- The ASMn originals (Archivio Gonzaga, Carteggio estero: Spagna for Suardino, Milano for Capino; Copialettere for
  Federico's minutes) are not online and were not seen.
