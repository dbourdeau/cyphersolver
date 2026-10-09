# Desmarets, Marly, 4 June 1710 (DECODE R10198)

Status: read with an existing decipherment (Tomokiyo's table); 96.8 % of the groups attested, 12 group types open

Outcome: read from Tomokiyo's published reconstruction of the 1710 code (Cryptiana 11B), applied to the 471 groups
read as one continuous stream. The key is Tomokiyo's, built from this very letter with Alexandre Pillon's alignment;
it was not broken here. Credit for the pointer goes to the author of issue #28 (yuanyi-350, 9 Oct 2026).

## Correction to the first attempt (21 Sept 2026)

The first version of this note said the French between the figure lines was not the decipherment and that no key
existed. Both were wrong. I had aligned each French line to the figure line under it, and the four models
(`em.py`, `em2.py`, `em3.py`, `emw.py`) could not converge, because the French and the figures are not in step:
the secretary deciphered on a separate sheet and wrote the clean text on the original, so the text drifts against the
numbers, and the last 22 figure lines carry the decipherment of the whole tail with no French at all. Tomokiyo says
so on Cryptiana (11B) and notes that the letter was printed in *L'Intermédiaire des curieux* 50 (1904). The fix is to
concatenate all 471 groups and apply a variable-length table (letters with homophones, syllables, a few short words).

## The document

DECODE R10198 "Desmaretz_1", contributed by Alexander Pillon. Nicolas Desmarets, Controller General of Finances,
Marly, 4 June 1710, to an unnamed "Monsieur". Three pages (590 px images, not public domain). 34 pairs of French line
over figure line, then 22 figure lines alone, then the clear closing formula and signature.
`transcription.txt`: 471 groups, 183 distinct, range 1–568.

## The reading

`tomokiyo_decode.py` holds the table as transcribed from Tomokiyo's image and decodes the transcription as one stream.
`reading.txt` is the stream with words divided by hand. 456 of 471 groups (96.8 %) are in the table and the whole
letter reads as sense, glossed lines and tail alike: the tail runs from "pouvoir qu'on vous envoie est assez estendu"
to "si l'on estoit demeure fermes dans les premieres resolutions". The sense is the one already read in the
interlinear French: the King wants peace, a safe peace, but means to protect "l'honneur du gouvernement"; further
demands must not reach "demembrements entiers"; the powers sent are wide enough; explanations and conferences are
needed, but this is "un relachement qui peut produire la paix".

Limits: Tomokiyo derived his table from this letter, so the check is against the sheet's own decipherment and
not independent of it. A few table cells are queried in his own table (e.g. 463 "temps?", 25 "S?"), and the table
shows some glosses as hand variants.

## Remaining gaps
- groups 23, 65, 94, 133, 147, 179, 189, 229, 534, 539, 559, 565 (15 tokens) - blocker: open-codes; not in Tomokiyo's table. 94 = ce (three places), 539 = l'esper and 565 = oit are clear from the context. 179+534 (differer), 133 (aplanir), 65 and 147 (renvoyer vostre courier), 189 and 229 are plausible only; 559 occurs twice and may be a null

## Escalation
- [x] siblings: no sibling record on DECODE; the Cryptiana note is the only parallel source
- [x] clear-pages: the interlinear French and the out-of-sync clear text on the sheet are the decipherment, as Tomokiyo says
- [x] known-keys: Tomokiyo's 1710 table applied
- [x] print: L'Intermédiaire des curieux 50 (1904) cited by Tomokiyo, not seen here; Boislisle III not searched
- [x] key-rebuild: the 12 missing types filled from the French glosses where the context fixes them
- [n/a] retry: no further groups can be fixed without a better image or another copy

## Files
`transcription.txt`, `tomokiyo_decode.py`, `reading.txt`, the superseded alignment scripts (`em*.py`, `offset_test.py`),
`profile.json`.
