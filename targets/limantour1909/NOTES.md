# Partial decipherment of the 1909 López Portillo–Reyes correspondence

**Cyphersolver catalogue:** 1448  
**Key recovered by:** Alberto Garvía García  
**Status:** Substantial partial decipherment, pending independent verification.

Status: read in part (6 Nov 2026). Check of 6 Nov 2026: the control numbers and the 77 groups were read on four private CEHM screenshots and agree with this documentation; see `VERIFICATION.md` (numbers and plain words only, no images). Earlier project note (6 Nov 2026): this folder held the contributor's documentation as submitted in #308; after the images arrived the letter of 15 July and the names in the note of 29 July were decoded (`key.tsv`, `reading.md`, `translation.md`).

## Summary

This contribution documents a proposed numerical substitution key for the encrypted correspondence between José López Portillo y Rojas and General Bernardo Reyes (1909).

The strict evidence count comprises 28 independently supported values. The assignment 60 = Y remains provisional and must not be included in that count.

## Evidence and methodology

The full transcriptions, key table, proposed readings and supporting analysis are available in the research documentation:

https://gist.github.com/alberto-garvia/c5737f6e25b1dbb736fbe87bca4acf87

Published research report:
https://doi.org/10.5281/zenodo.23934776

## Original archival records

Centro de Estudios de Historia de México (CEHM), Archivo del General Bernardo Reyes:

- Letter of 15 July 1909, DLI.39.7680.2: https://www.cehm.org.mx/Buscador/FichaBasica/118144?Tipo=A
- Letter of 29 July 1909, DLI.39.7712.1: https://www.cehm.org.mx/Buscador/FichaBasica/118230?Tipo=A
- Telegram of 15 July 1909, DLI.39.7677.1: https://www.cehm.org.mx/Buscador/FichaBasica/118140?Tipo=A
- Telegram of 23 July 1909, DLI.39.7696.1: https://www.cehm.org.mx/Buscador/FichaBasica/118185?Tipo=A

The original images remain hosted by the CEHM and are not reproduced in this repository.

## Attribution

Cryptographic research and proposed key recovery: Alberto Garvía García.

Research documentation offered for incorporation under CC BY 4.0, with attribution to Alberto Garvía García and a reference to the published report.

## Remaining gaps

- Segment C of the letter (28 23 24 54 2) and the special codes 79 and 77 - blocker: open-codes; each occurs once, no context narrows them (79 is faintly aligned to "Sr. Presidente" in the 15 July telegram)
- The second name in the 29 July note (24 46 42 1 31, CREEL?) and the faint handwritten plaintext above it - blocker: illegible; 46 and 42 rest on one word, screenshots of modest resolution
- The character after 77 (e or a on the image, s in the contributor's file) - blocker: illegible; one typed character
- A check on the CEHM originals by a human - blocker: needs-physical-access; the screenshots are private and cehm.org.mx is not reachable from the project environment

## Escalation

- [x] siblings: the telegrams of 15 and 23 July (DLI.39.7677.1, DLI.39.7696.1) used as controls; the 29 July note read; other López Portillo ciphers in the fonds not opened
- [x] clear-pages: the typed plaintext below the 23 July telegram and the typed line on the 29 July note checked; neither is a decipherment of the letter
- [x] known-keys: the contributor's structural comparison with a 1895 key sheet (not seen by the project); no other key for this correspondence known
- [x] print: the contributor's Zenodo report (doi 10.5281/zenodo.23934776); a web search on 6 Nov 2026 (López Portillo, Reyes, 1909, clubs, Limantour, Creel) found no edition of these telegrams
- [x] key-rebuild: the 28 strict values extended with values from the 15 July telegram (26, 41, 20, 11) and from the letter's own words (key.tsv)
- [x] retry: segment C retried with the extended key; still n-d-c-s-e, not read
