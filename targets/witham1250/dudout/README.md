Status: in progress (Brice Dudout, 11 Nov 2026; class stays "not read": transcription corrected at #10-11, membership in the SDX sword-inscription family measured, no expansion read or testable). Next step: Winter 2016 and Oakeshott's Records read in full; a photograph of the other face; for Alphen, the Provincial Depot / Restaura photographs.

# Witham and Alphen sword inscriptions: transcription check and family test (Brice Dudout, with Claude)

A contribution to Daniel Bourdeau's targets `witham1250` and `alphen1200`. Text only. No image, crop or derivative of
any photograph is included: the British Museum photographs of BM 1858,1116.5 (licence not confirmed: the BM states
CC BY-NC-SA 4.0 in its image policy, but the live object page refused us, HTTP 403) and the Alphen photographs
(Madoc 2014, Worley & Wagner 2013; Archeon / Restaura) are cited by URL and number only.

## Files

| file | what |
|---|---|
| `TRANSCRIPTION.md` | Witham re-read position by position on two BM photographs; table of all published readings; Alphen transcription kept (van Hasselt's drawing) with its uncertain signs |
| `PROPOSITIONS.md` | prior proposals for both blades, scored by how many letters rest on a parallel, on a free choice, or on the misread #10-11 (a description, not a validation) |
| `tools/corpus.py` | the sibling inscriptions as published (Wagner et al. 2009, with page numbers), controls, solved acronym formulas, 44 Latin formulas |
| `tools/family2.py`, `RESULTS-family-lcs.txt` | longest common subsequence of Witham (both readings) with each of 18 siblings, against 5000 shuffles of the Witham letters (seed 20261111) |
| `tools/family3.py`, `RESULTS-family-controls.txt` | the same test for control strings, Witham reversed and the two Alphen faces, against Fyris 74 and Marburg (3000 shuffles, seed 7) |
| `tools/analyse.py`, `RESULTS.txt`, `RESULTS.json` | initial-letter statistics, prayer-acrostic fit (contiguous runs of initials / nomina sacra against 44 formulas, 1000 shuffles), substring family test |

All scripts are stdlib Python with fixed seeds (`python3 -I tools/family2.py` etc.). p-values are (k+1)/(n+1), where k
is the number of shuffles that reach the observed score: 0.0002 with 5000 shuffles means none did.

## Sources (read, not reproduced)

- British Library, Medieval manuscripts blog, J. Harrison, "Help us decipher this inscription", 3 Aug 2015, with the
  postscript note by Marc van Hasselt (7/10 Aug) and comment pages 1-4 and 6:
  https://blogs.bl.uk/digitisedmanuscripts/2015/08/help-us-decipher-this-inscription.html
  (inscription detail "image courtesy of the British Museum").
- British Museum collection, 1858,1116.5, image 00296785; database "Inscription Content" (2019 snapshot):
  https://www.britishmuseum.org/collection/object/H_1858-1116-5
- T. G. Wagner, J. Worley, A. Holst Blennow, G. Beckholmen, "Medieval Christian invocation inscriptions on sword
  blades", Waffen- und Kostuemkunde 51 (2009) 11-52, urn:nbn:se:uu:diva-113084.
- J. Worley, T. G. Wagner, "How to make swords talk", Waffen- und Kostuemkunde 55 (2013) 113-132,
  urn:nbn:se:uu:diva-208460.
- M. van Hasselt, Madoc 28/2 (2014) (Alphen blade; transcription and afb. 1).
- Stamford Mercury, 18 Aug 1826, quoted by Rob Wheeler in a BL blog comment of 7 Aug 2015 (the newspaper itself not seen).
- H. Winter, Waffen- und Kostuemkunde 58/2 (2016, rev. 2026), doi 10.71475/wkk.2016.2.115248: **not seen** (the
  Heidelberg page served an anti-bot check); cited from Daniel's summary in `../NOTES.md`.
