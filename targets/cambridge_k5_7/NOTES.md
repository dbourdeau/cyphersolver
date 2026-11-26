# Cambridge University Library, T-S K5.7

Four rows of signs survive on the recto of this Cairo Genizah fragment. Gideon Bohak identified the upper signs from the substitution alphabet of T-S K24.19. The first two columns, read vertically, give four alephs and the Hebrew divine name YHWH. The interior sequence and the small signs below it remain unexplained. The handwriting of a separate recipe book that uses this cipher has been assigned to the 11th century. K5.7 itself is undated. [Cambridge recto](https://images.lib.cam.ac.uk/iiif/MS-TS-K-00005-00007-000-00001.jp2/full/1200,/0/default.jpg) · [Bohak, pp. 13–15, figs. 2–3](https://albert.ias.edu/bitstreams/b463280e-28c4-4605-b811-75bfa57ddc38/download) · [Princeton Geniza Project 42030](https://geniza.princeton.edu/en/documents/42030/)

Earlier repository sweeps describe the same fragment as magical characters and as an unchecked member of Bohak's cipher group. The reason to study it as a cipher target is the independently attested sign alphabet and its readable Hebrew border. Whether the interior encodes prose remains open. Catalogue entry 3757 is this fragment's interior. [Catalogue 3757](https://dbourdeau.github.io/cyphersolver/catalogue.html#3757) · [Arabic sweep](../../research/sweep_2026-11-15_arabic/part_A.md) · [Hebrew sweep](../../research/sweep_2026-11_hebrew/README.md)

## Transcription doubts

- Count signs from the right. Interior position 1 is full position 3. The upper-letter column follows the working transcription of Bohak's edition. A question mark marks a tentative value, a dash an unidentified sign and a period a lost position. The first row loses its left end. The register includes seven lost positions there.
- Bohak describes four rows of 26 signs. The working transcription has 27 positions in row 2, including both borders. Tests requiring 22 interior signs try every single interior omission. No deletion is adopted in the register.
- X denotes the recurring unidentified form at full positions 12, 6 and 10 of rows 2, 3 and 4 in this count. The computational register retains a dash at those positions. In rows 2 and 4, full positions 10–12 read nun–dalet–X and X–dalet–nun. Assigning a sound value to X remains conjectural.
- The lower-mark labels come from one masked rereading of shuffled crops by an observer already familiar with the image. Of 98 extant cells, 30 received clear labels, 35 tentative labels and 33 remained unclassified. A lone question mark does not establish a blank. The blind ID connects each entry to its crop. [Cell register](lower-register.tsv) · [Crops 1–49](lower-sheet-1.png) · [Crops 50–98](lower-sheet-50.png)

## Reproducing the checks

Run these commands from this directory with Python 3.9 or newer. They use the standard library.

    python -X utf8 check.py
    python -X utf8 paired_inventory.py
    python -X utf8 rounds_5_8.py
    python -X utf8 recipe_rounds.py bound
    python -X utf8 recipe_rounds.py route
    python -X utf8 recipe_rounds.py key

A model with one complete Hebrew alphabet per row requires at least eight cell substitutions, even after allowing one row 2 omission and filling doubtful cells freely. Lamed, pe and resh tie at that minimum for X. The bound counts individual cells and does not establish that the scribe made errors. The separate witness T-S Misc.22.218 supplies an unexplained seven-consonant sequence in Bohak's edition. Neither the tested grid routes nor the second substitutions recovered it in a fully legible passage of K5.7. [Structural checks](rounds-5-8.md) · [Alphabet bound and recipe comparison](rounds-9-11.md)

## Remaining gaps

A reading must explain the repeated upper consonants, distinguish or account for the lower marks, and predict interior cells beyond the shared opening of rows 2 and 4. The language and purpose of the interior remain unknown.
