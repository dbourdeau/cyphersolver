# Notes: the Sforza chancery letters in this folder

## What the documents are

Letters of the Sforza chancery of Milan, in cipher, kept in the Carteggio Sforzesco. Most are in Italian; the record pages name the Latin and French ones. The rows give no year.

## The system

Each letter is written with signs that stand for letters. Several signs can stand for one letter, and some signs are nulls. My labels name the sign shapes of one page only; the same label on two pages need not be the same sign.

## The key

- **From ciphertext, with my key:** R5415 p1, R5416 p1, R5419 p1, R5421 p1, R5432 p1, R5439 p1, R5453 p1, R5453 p2, R5456 p1.
- **From ciphertext, with my key of R5516, R5519 and R5522 (cartella 1598, entry 2634):** R5445 p1, with no further fit. By my record, my frozen read of this page gives the firm letters of the decode with that key. The key table here takes its values from that read, where the read shows one; no label shows two letters.
- A page read with the key of another page says so on its record page.

## The frozen read

My frozen read of each page is the read as it stands in my public repository (https://github.com/prabal-rje/branicki-1757/tree/main/sforza-160-records), commit 3068318 of 2026-11-19; b1b2f51 of 2026-11-19. A sign shows a letter in it only where the read is firm, so it differs from the plain decode. This folder adds no hash table and no other record of provenance.

## Years, as leads

These years are leads, not readings. The rows give no year.

- **R5453:** most likely 30 November 1491. Anne of Brittany was engaged to Charles VIII on 17 November and married him on 6 December 1491 (en.wikipedia, "Anne of Brittany"). The year rests on this one event.

## Strictly aligned sentence readings (23 November 2026)

Four blind ciphertext-only letters in this folder (`R5416`, `R5439`, `R5453`, `R5456`) now carry strictly aligned word-divided Italian readings (`readings/rXXXX_reading.md`) and English translations (`readings/rXXXX_en.md`), verified mechanically by `scripts/verify_readings.py` against the unedited decodes in `key/` (zero unmarked departures; every unknown sign `?`, unread sign `[?]`, null `·`, and bracketed restoration `[x]` counts as a hole):

| Record | Pages | Cipher words | Sure | Holes | Read share | Content |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `R5439` | p1 | 145 | 122 | 23 | 0.841 | Diplomatic counsel on preserving friendship and avoiding friction |
| `R5453` | p1, p2 | 158 | 131 | 27 | 0.829 | 30 Nov [1491]: Swiss League ambassadors, Anne of Brittany styled Queen of France, Duchess of Orléans granted Duchy of Bar, Bourges entry |
| `R5416` | p1 | 166 | 131 | 35 | 0.789 | Sarzana, April: Messer Ludovico, Diotesalvi, Aulla/Rissana, Tomasino, Ferrarese negotiations |
| `R5456` | p1 | 136 | 98 | 38 | 0.721 | Sarzana, 11 Sept: Giovanni da Folo from Genoa, Nicolosio de' Leonardi, 10,000 ducats, Angelo Acciaiuoli, Florence citadel restitution |
| **Total** | **5 pages** | **605** | **482** | **123** | **0.797** | **read in part (key recovered from ciphertext-only)** |

## Transcription doubts

The sign transcriptions in `transcription/` are unverified machine transcriptions of the DECODE images; no person has checked them against the scans. Every `[?]` unread sign, `?` unvalued label, and single-letter slip in `R5416`, `R5439`, `R5453`, and `R5456` stays open as a `[x]` or `[...]` hole in `readings/` and is verified as a hard barrier by `scripts/verify_readings.py`.

- Unknown/unread signs (`?`, `[?]`) and single-letter slips across `R5416`, `R5439`, `R5453`, and `R5456` (123 holes across 605 cipher words) - read: kept literal in `key/*_decode.txt` and bracketed `[x]` or `[...]` in `readings/`; checked: image, decode; no unmarked departure from the unedited mechanical decode.

## Remaining gaps

- **Five noisier records in this folder (`R5415`, `R5419`, `R5421`, `R5432`, `R5445`)** - blocker: open-codes; higher sign-label noise or shorter length (`R5445`) keeps them as decoded, not read until higher-resolution scans settle remaining sign splits.
- **Labels with no value (`?`)** - blocker: no-key-material; rare signs with too few occurrences to pin from ciphertext alone.
- **The nine records `R5425` to `R5430` and `R5463` to `R5465`** - blocker: no-key-material; no rows in the labels of their key in this folder.

## Escalation

- R5421 and R5432: the ledger's split of 6 November 2026 calls them clear leaves or wrappers. My transcription gives 1,397 and 1,443 cipher signs on their pages 1.
- R5445 p1: key not confirmed (225 signs, 44 labels). Its key table takes its values from my frozen read, which by my record gives the firm letters of the decode with my key of R5516, R5519 and R5522 (cartella 1598, entry 2634).

## Credits

See `README.md`. No DECODE image is published.
