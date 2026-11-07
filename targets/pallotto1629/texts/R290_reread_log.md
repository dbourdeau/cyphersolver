# Re-reading log, R290 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read". The repository held only the unedited automatic decode with the 6956 key
(`texts/R290_decrypt.txt`), DECODE's digit transcription with garbled clear-text annotations, and Kiewning's volume.

## What was done

1. **A better decode** (`reread_b01_decode.py`, used for the whole batch): the nulls 1 and 8 never sit inside a group;
   segmentation into 2- and 3-digit groups is chosen by an Italian 5-gram model; DECODE's uncertain digits are kept as
   alternatives; a 0 may be the null 8 (DECODE often reads the 8 of this hand as 0, checked on the R286 and R290 scans);
   61 nomenclator groups missing from the 6956 key were added from alignments with Kiewning's print
   (`reread_b01/extra_groups.json`, each with its evidence), and two key entries corrected (776 = tutto, not "quanto";
   567 = occasione, not "ordinatione").
2. **Existing text?** Kiewning 1897 Nr. 156 (10 Aug 1629), printed from the Roman decipherment. `reread_b01_match2.py`
   located it (hits in edition lines 23480-23552); `reread_b01_align.py` aligned the decode with it chunk by chunk:
   the first two pages agree with the print at 0.05-0.6 cost per letter, so the reading of paragraphs 1-3 is the print,
   its OCR corrected (e.g. "tomato" -> "tornato", "nnmero" -> "numero", "conreniente" -> "conveniente").
3. **The rest** (last lines of p. 2 and all of p. 3) is a German regest in Kiewning ("Sabran reiste gestern wenig
   befriedigt ab ... Wallenstein. Er ist durch Podagra aufgehalten ... Sohn des dänischen Königs ... Magdeburger
   Angelegenheit ... Kurfürst von Sachsen wenig zufrieden ... dem Edikt nicht nachgeben ... geistlichen Güter der Pfalz
   ... Lamormain"). Read here from the DECODE scans (IMG_R290_I2503, I2504, 1390-1404 x 2088): the clear words read on
   crops at full resolution (DECODE's clear-text transcription of p. 3 is mostly asterisks), each cipher run re-read
   from its codes (`reread_b01_show.py`) and checked against the scan where the decode broke (`R290_corrections.tsv`).
4. Points settled on the scan: "spronar il Re alla guerra" (DECODE misread "36 1 76 1 635" as "36 ? 7 2"); "Sento che
   questo veniva trattenuto" (775 = questo, after clear "Sento che"); "potria far più considerabili" (743 = far after
   clear "potria"); "editto de' beni ecclesiastici" (735 8 407).

## Holes and why

* "[?tutto] posto e risoluto": 776 = tutto by its other contexts; the phrase is odd and may hide a slip.
* "nel [?viaggio]": 06 50 20 + an unread three-digit group 994.
* "qualche […] circa il figlio del Re di Danimarca": the clear word after "qualche" is not legible on the scan.
* "l'[?Elettore di Sassonia]": the figures are 402 (an unread group in the E range of the nomenclator); the person is
  given by Kiewning's regest ("der Kurfürst von Sachsen"), so the name rests on the print, not on the key.
* "[?molto] mal sodisfatto", "non solo [?non vuole] ubbidir [?all']editto": the figures are 77 9(9?) and
  "o o o a ubbidir 202": partly carried; the sense is confirmed by the regest ("dem Edikt nicht nachgeben will").
* "secondo l'[?intento]": clear word, uncertain on the scan.

## Result

Read: all sentences hold; clean-sentence share 0.82 (`docs/_check_reading.py --file`), the holes are the seven listed.
