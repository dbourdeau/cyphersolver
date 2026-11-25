# Notes: the Sforza chancery letters in this folder

## What the documents are

Letters of the Sforza chancery of Milan, in cipher, kept in the Carteggio Sforzesco. Most are in Italian; the record pages name the Latin and French ones. The rows give no year.

## The system

Each letter is written with signs that stand for letters. Several signs can stand for one letter, and some signs are nulls. My labels name the sign shapes of one page only; the same label on two pages need not be the same sign.

## The key

- **From key:** R5488 p1, R5528 p1, R5579 p1 and p2 use the archive's key sheet, DECODE record R5347. I read each value off the sheet and joined each sign of the page to a sign of the sheet.
- **From ciphertext, with my key:** R5297 p2, R5480 p1, R5504 p1, R5505 p2, R5509 p1, R5511 p1, R5513 p1, R5516 p1, R5519 p1, R5520 p1, R5521 p1, R5522 p1, R5523 p1, R5524 p1, R5529 p1, R5533 p1, R5533 p2, R5541 p1, R5543 p2, R5559 p1, R5563 p1, R5563 p2, R5564 p1, R5565 p1, R5574 p1, R5582 p1, R5583 p1, R5584 p1.
- **From ciphertext, with the values of my frozen read:** R5297 p1, R5521 p2, R5521 p3, R5542 p1. For these pages the key table gives, for each label, the value that my frozen read shows most often.
- A page read with the key of another page says so on its record page.

## The frozen read

My frozen read of each page is the read as it stands in my public repository (https://github.com/prabal-rje/branicki-1757/tree/main/sforza-160-records), commit 3068318 of 2026-11-19; b1b2f51 of 2026-11-19. A sign shows a letter in it only where the read is firm, so it differs from the plain decode. This folder adds no hash table and no other record of provenance.

## Years, as leads

These years are leads, not readings. The rows give no year.

- **R5521 and R5542:** most likely 20 July 1492. The pope is ill in the letter, and Innocent VIII died on 25 July 1492 (L. Pastor, *The History of the Popes*). On 2 July 1492 Milan urged that the bishop of Nitra be sent into Italy (A. Berzeviczy, Budapest 1914, no. CLXVII).
- **R5520, R5523 and R5541:** 1465 or before; most likely between 1455 and 1458. Jacopo Piccinino died in 1465, and a living "King of Aragon" fits Alfonso V, who died in 1458 (*Dizionario Biografico degli Italiani*, vol. 83).

## Strictly aligned sentence readings (23 November 2026)

Three blind ciphertext-only letters in this folder (`R5521`, `R5523`, `R5524`; none uses the archive key sheet R5347) now carry strictly aligned word-divided Italian readings (`readings/rXXXX_reading.md`) and English translations (`readings/rXXXX_en.md`), verified mechanically by `scripts/verify_readings.py` against the unedited decodes in `key/` (zero unmarked departures; every unknown sign `?`, unread sign `[?]`, null `·`, and bracketed restoration `[x]` counts as a hole):

| Record | Pages | Cipher words | Sure | Holes | Read share | Content |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `R5521` | p1, p2, p3 | 1,126 | 693 | 433 | 0.615 | Milan, 20 July [1492], signed *Ludovicus Maria Sfortia Dux Bari*: 50,000 + 200,000 ducat marriage dispensation, Bishop of Nitra traveling via Germany/Padua, Pope Innocent VIII's urinary illness (*ardore de urina*, *excoriatione de uesiga*), Prince of Capua in Rome, rumors of the Turk's preparations |
| `R5523` | p1 | 116 | 84 | 32 | 0.724 | Rome, 9 June [1455-1458]: confusion over Jacopo Piccinino's arrival, Tonio da Pesaro going to the King to put Piccinino in the pay of the Church |
| `R5524` | p1 | 135 | 89 | 46 | 0.659 | Ambassador returning from the King of Catalonia, arbitration terms, Governor of the Dauphiné with 1,370 cavalry, complaint over the House of Anjou |
| **Total** | **5 pages** | **1,377** | **866** | **511** | **0.629** | **read in part (key recovered from ciphertext-only)** |

## Transcription doubts

The sign transcriptions in `transcription/` are unverified machine transcriptions of the DECODE images; no person has checked them against the scans. Every `[?]` unread sign, `?` unvalued label, and polyphonic or misread sign (including `t` standing for `u`/`v`/`f` in `R5521`) stays explicitly marked inside `[x]` or `[...]` in `readings/` and counts as a hole in `scripts/verify_readings.py`.

- Unknown/unread signs (`?`, `[?]`) and polyphonic `t`/`u`/`f` slips in `R5521`, `R5523`, and `R5524` (511 holes across 1,377 cipher words) - read: kept literal in `key/*_decode.txt` and bracketed `[x]` or `[...]` in `readings/`; checked: image, decode; zero unmarked departures from the unedited mechanical decodes.

## Remaining gaps

- **Other records in this folder (28 additional blind pages and 4 R5347 key-sheet pages)** - blocker: open-codes; higher sign-label noise or unvalued labels (`?`) keep them as decoded, not read until higher-resolution scans settle remaining sign splits.
- **Labels with no value (`?`)** - blocker: no-key-material; rare signs with too few occurrences to pin from ciphertext alone.
- **R5501 p1** - blocker: illegible; rows and frozen read differ by one sign.

## Escalation

- R5504 p1 and R5505 p2 are in the ledger's family C. The ledger read R5504 page 1, lines 1 to 16, before me. It has no rows of R5505 page 2.

## Credits

See `README.md`. No DECODE image is published.
