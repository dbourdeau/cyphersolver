# Clear copies in LASA A 1 Nr. 540 Bd. 1 (Beling addition, 12-13 Nov 2026)

Landesarchiv Sachsen-Anhalt, A 1 Nr. 540 Bd. 1 holds clear copies of the envoys' diary with its numbered annexes.
Images: `https://recherche.landesarchiv.sachsen-anhalt.de/images/A_1/Nr_540_Bd_1/max/A_1__Nr_540_Bd_1__NNNN.jpg`
(curl, 12 Nov 2026; SHA-256 of each file as fetched in `source_images.json`; the viewer stamps each delivery with the
request time, so a new fetch gives a new hash). Images are not committed.

This folder plays the part for the 1645 annexes that `nr529/` plays for f.5, f.6 and f.101: a clear text of the same
annex, written by the envoys' office, against which the cipher slips of Nr. 530 can be compared.

| cipher in Nr. 530 | clear copy in Nr. 540 Bd. 1 | date evidence | files |
|---|---|---|---|
| No. 32 (1645 series), ff. 210r-211r, frames 240-241 | ff. 599r-600v, frames 648-650 | cover letter frame 643; the preceding diary closes on frame 647; the annex heading "No. 32" on frame 648; the packet is dated **19 March 1645** | `f210_collation.tsv` (witness locators), `f210_clear_units.tsv` (the clear text in 20 normalised prose units), `f210_delta_crosswalk.tsv`, `f210_gaps.tsv`, `f210_UPDATES.md`, `f210_PRIOR_ART.md` |
| No. 31 (1645 series), f. 212r-v, frames 242-243 | f. 585r-v, frames 633-634 | the diary on frame 632 (f. 584r) ends "Signatum Osnabrück den 12. Martii Ao 1645"; its dorse and the annex heading "No. 31" are on frame 633 | the clear text sits beside each cipher record in `../units/f212_BEL.tsv` (column `clear_correspondence`) |

A further revised draft of No. 32 is in Nr. 529, frames 91, 93 and 94 (cited in `f210_collation.tsv`).

What these copies are and are not:

- They are the envoys' own clear text of the annex, not a decipherment of our slip, and they differ from the cipher in
  places (connectives, a cancelled phrase, *Caesareis*/*Caesarianis*, *könte*/*müste*; listed in `f210_gaps.tsv`
  and in the notes of `../units/f212_BEL.tsv`).
- They are not new to history: Braun (2015) treats the March 1645 conversations from Lampadius's reports
  (`../PRIOR_ART_BEL.md`). No edition of these exact Nr. 530 cipher slips was found in that bounded check.
- Our readings of Nos. 31 and 32 were made **with these copies open**. They are source-assisted readings, not an
  independent recovery of the plaintext from the cipher.
- The alignment of No. 32 is at the level of paragraph units, not word by word; a clear unit repeated beside several
  cipher records is not a claim that each record was read as that whole unit.
- These copies were not searched for f.102, f.104 or f.204; the gap in `../NOTES.md` that names Nr. 540 for those
  slips stays open.
