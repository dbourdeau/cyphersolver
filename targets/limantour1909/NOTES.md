# Partial decipherment of the 1909 López Portillo–Reyes correspondence

**Cyphersolver catalogue:** 1448  
**Key recovered by:** Alberto Garvía García  
**Status:** Substantial partial decipherment, pending independent verification.

Status: read in part (6 Nov 2026). Check of 6 Nov 2026: the control numbers and the 77 groups were read on four private CEHM screenshots and agree with this documentation; a second, clearer set of four the same day confirmed them, gave the character after 77 as s and supported the contributor's reading of segment C as *quejándose* (tentative); see `VERIFICATION.md` (numbers and plain words only, no images). Earlier project note (6 Nov 2026): this folder held the contributor's documentation as submitted in #308; after the images arrived the letter of 15 July and the names in the note of 29 July were decoded (`key.tsv`, `reading.md`, `translation.md`).

## Summary

This contribution documents a proposed numerical substitution key for the encrypted correspondence between José López Portillo y Rojas and General Bernardo Reyes (1909).

The contributor's strict evidence count comprises 28 independently supported values and kept 60 = Y provisional. After the clearer images of 6 Nov 2026 the project counts 60 = Y as the 29th strict value (VERIFICATION.md section 6); the contributor's evidence packet, kept as submitted, still says 28.

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

- The special codes 79 and 77 - blocker: open-codes; 77 occurs once and nothing narrows it. 79 is provisionally "Sr. Presidente" (section "Code 79" below): it stands once in the letter and once in the 15 July telegram, but it is a code for a phrase, matched by position to a pencilled plain text in one telegram, so it stays unread in every count
- Segment C (28 23 24 54 2) is read as quejándose only by assuming 24 is a slip for an o code (contributor's proposal) - blocker: needs-physical-access; the original must show whether a number was corrected or mistyped
- The second name in the 29 July note (24 46 42 1 31, CREEL?) and the faint handwritten plaintext above it - blocker: illegible; 46 and 42 rest on one word; the handwriting above the cipher is faint even on the clearer images
- A check on the CEHM originals by a human - blocker: needs-physical-access; the first check was on private screenshots. Since 14 Nov 2026 the public CEHM image of the letter (visor.cehm.org.mx over plain http) has been read here too and agrees (section of 14 Nov 2026); the two control telegrams and the note were not fetched again; no human has checked the originals

## Escalation

- [x] siblings: the telegrams of 15 and 23 July (DLI.39.7677.1, DLI.39.7696.1) used as controls; the 29 July note read; the telegram of 19 July (DLI.39.7681.1, with a pencil gloss) opened on 14 Nov 2026 after issue #606: it checks 14 = B and 19 = I. Whether the fonds holds further López Portillo ciphers was not searched
- [x] clear-pages: the typed plaintext below the 23 July telegram and the typed line on the 29 July note checked; neither is a decipherment of the letter
- [x] known-keys: the contributor's structural comparison with a 1895 key sheet (not seen by the project); no other key for this correspondence known
- [x] print: the contributor's Zenodo report (doi 10.5281/zenodo.23934776); a web search on 6 Nov 2026 (López Portillo, Reyes, 1909, clubs, Limantour, Creel) found no edition of these telegrams
- [x] key-rebuild: the 29 strict values extended with values from the 15 July telegram (26, 41, 20, 11) and from the letter's own words (key.tsv)
- [x] retry: segment C retried with the extended key (n-d-c-s-e) and again with the contributor's proposed slip (n-d-o-s-e, quejándose) on the clearer images of 6 Nov 2026; kept tentative

## A third glossed telegram: DLI.39.7681.1, 19 July 1909 (issue #606, 14 Nov 2026)

Brice Dudout (issue #606) pointed to a further López Portillo telegram of the same fonds with a contemporary clear written on it. Checked here on the public CEHM image (`http://visor.cehm.org.mx/assets/docx/fondos/jzd/DLI/39/7681/1/DLI.39.7681.1.0001.jpg`, 1949 x 2559, plain http, no login; not in git).

- The sheet: a telegram in pencil, "Sr. Gral. Dn. B. Reyes, Galeana", signed José López Portillo y Rojas, stamped 7681. Text: "Cumpliré tus encargos = mañana 47-56-14-32-19-24-15-37-17 Carta 24-32-57-14 iniciador". Below the signature, in another pencil hand: "mañana publicará carta Club iniciador". The date and the place of sending (the issue gives 19 July 1909) are in the faint heading and were not read here.
- The 13 groups read here on the image are the 13 the issue gives, 15 included (the issue says an earlier unpublished transcription had 13 there).
- With `key.tsv`: 47 P, 56 U, 14 B, 32 L, 19 I, 24 C, 15 A, 37 R, 17 A = publicara; 24 C, 32 L, 57 U, 14 B = club. Both words are the words of the gloss. No value of the key is contradicted.
- What changes: 14 = B and 19 = I were "letter-word" values (each fixed by one word of the letter of 15 July, so not independent of the key). A contemporary clear now gives them; `key.tsv` marks them `telegram7681`. 14 stands twice in this telegram (publicara, club). The other eleven group occurrences (15, 17, 24 twice, 32 twice, 37, 47, 56, 57) are strict values confirmed on a text that was not used to build the key.
- The counts are kept as they were defined. The strict count stays 29: the contributor's 28 from the seven control sequences, and 60 = Y. Outside it, values that a contemporary clear gives are now six: 26, 41, 20, 11 (telegram of 15 July, 11 partly cut off on the screenshot) and 14, 19 (this telegram). The issue's "31 instead of 29" adds 14 and 19 to the strict count; by the same reasoning the four of 15 July would be added as well (35). The line in `reading.md` on "certain" groups (every value in the strict set) is not recounted.
- The same day the public image of the letter of 15 July was fetched by the same route (`.../DLI/39/7680/2/DLI.39.7680.2.0001.jpg`, 1934 x 2557): the 77 groups of `transcription_7680.txt` agree with it, the typed s after 77 included. The check of 6 Nov was on private screenshots because the project environment did not reach the CEHM then; the image host answers over plain http (found for duron1911).
- Credit for the key stays with Alberto Garvía García; Brice Dudout is credited for the pointer.

## Code 79 (issue #245, comments of 14 and 21 Nov 2026)

Alberto Garvía García asked twice on the closed issue #245 that the code 79 be shown as a provisional "Sr. Presidente", in the reading and in the interactive decipherment, instead of "?". Check made here on 21 Nov 2026 on the public CEHM image of the telegram DLI.39.7677.1 (`http://visor.cehm.org.mx/assets/docx/fondos/jzd/DLI/39/7677/1/DLI.39.7677.1.0001.jpg`, 2009 x 2636, plain http, no login; not in git), read by an AI model at full size; no human has checked it:

- The cipher lines read `79-1-26-3-41-20-8-11 decla-rado 15-48-31-17-7-16 aclara-ción Ruégote 2-54-47-1-38-3-54 carta mía`, signed José López Portillo y Rojas. Below the signature a second pencil hand has the plain text, which begins "Sr. Presidente enemigo declarado". The words the cipher carries are therefore Sr. Presidente (79), enemigo (1 26 3 41 20 8 11), aplaza (15 48 31 17 7 16) and esperes (2 54 47 1 38 3 54); the words left clear are declarado, aclaración, Ruégote and carta mía.
- So 79 is the only group where "Sr. Presidente" stands: nothing else comes before the seven numbers of enemigo. In the letter the same code opens the clause "He sabido de buena fuente que 79 habla de tí como de un enemigo".
- The last number of the first line, 11, which was partly cut off on the phone screenshots, is complete on the public image (8-11).

What this settles and what it does not. It removes the doubt that 79 is only "faint": the group is legible and its place in the line is unambiguous. It does not make 79 a letter value: it is a code for a phrase, it stands in one telegram and one letter, the plain text is a pencilled note by another hand, and one AI reader made the check. By the rule that a probable word is a hole, 79 stays unread in every count (84 of 89 groups, the strict count of 29, the read shares): no number changes. Whether the plain text beside it counts as giving it (README, rule of 19 Nov 2026: "or the plain text beside it does") is for the maintainers. Until then it is shown as provisional: `[79: Sr. Presidente?]` in `reading.md` and `translation.md`, and "Sr. Presidente?" in the uncertain class of the interactive decipherment.
