# Sforza informer at Sarzana, seven cipher letters (ASMi cart. 1598; catalogue 2629, family B of catalogue 1311)

Read in part (15 Nov 2026). Key recovered from ciphertext-only. Measured read share 0.897.

Split out of `targets/sforza1598` (family B) because it has its own key (one key, one entry). The work log, with every step and the
controls, is in `../sforza1598/NOTES.md` under "family B". The working files (flags, emendations, crops) are in `../sforza1598/famB/`.

## Documents
Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, cart. 1598 (via DECODE). All seven are wholly in cipher, with no year written:
- R5562, no. 88, 5 December, from Sarzana(?), 686 signs
- R5572, no. 98, 13 March, from Sarzana
- R5573, no. 99, 23 March, from Sarzana
- R5575, no. 101, 20 February, from Sarzana
- R5576, no. 102, 7 June, from Sarzana
- R5577, no. 103, 17 July, from Sarzana
- R5586, no. 112, 8 February, from Florence

## Cipher and key
A homophonic substitution of about 35 signs, with one to three signs per letter (`keyB2.json`). Two pairs of look-alike signs:
- The underlined "rr4" is o; the plain "r4" is m.
- S is h; the 5-like sign is v.

The o-with-cross and the digit-like signs 6 and 10 are nulls set between doubled letters. No code words were seen.

## How it was read
1. CTTS (Lasry's solver, run headless) on R5562 alone: 24.09 M against 10.73 M shuffled. Two seeds agree.
2. The key read the six other letters unchanged. Cover by words of 4+ letters: 0.54-0.67, against 0.10-0.17 shuffled.
3. Review: 130 positions flagged by a 5-gram model. 38 fixes were confirmed on image crops and 5 dropped.
4. The doubling-mark nulls were then identified.

Read share 0.897, measured with a strict segmenter that counts chancery spellings as unread:

| Letter | Read share |
|---|---|
| R5562 | 0.905 |
| R5576 | 0.932 |
| R5572 | 0.899 |
| R5577 | 0.923 |
| R5575 | 0.896 |
| R5586 | 0.850 |
| R5573 | 0.930 |

## Setting
The names fit the exile of Ludovico Sforza at Pisa (May 1477 - Sept 1479), under the regency of Bona of Savoy and Gian Galeazzo
("Madona", "el Signore"):
- Tommasino Campofregoso, lord of Sarzana
- Corsica, held by Milan from 1464 to 1481
- Nicodemo Tranchedini (DBI: at Genoa in 1478)

Working date 1477-1479. The writer is a Sforza informer at Sarzana close to Ludovico, and arranged to be given the chancellorship of
Volterra as cover. Not checked in the archival registers.

## Remaining gaps
- R5586 ends of ll. 9, 11, 12 and a struck word in l. 13 - blocker: illegible; creases, holes and an erasure on the leaf
- R5562 date line, first letters of the place name - blocker: illegible; left edge torn
- R5586 date line in numeral-like signs (dd, bb, e) - blocker: open-codes; signs outside the letter key, each once
- open words mamiglio, si s-gain (R5562), mascano (R5575), canteera, vala (R5573), promqso (R5577), Miser Andremto (R5572) - blocker: open-codes; no single look-alike fix, needs a box-level transcription of those lines

## Escalation
- [x] siblings: all 110 letters of cart. 1598 grouped by hand; no other letter uses this key
- [x] clear-pages: the clear leaves in cart. 1598 were checked; none is a decipherment of these letters
- [x] known-keys: the 93 key sheets of cart. 1598 and the 115 of cart. 1597 were scanned (for family C); no family B alphabet among them
- [x] print: DBI and web reference works for the names; no edition of these letters found
- [x] key-rebuild: key annealed on R5562, refined by 5-gram flags, image checks and the doubling-mark nulls
- [x] retry: every flagged position and open word was retried with the refined key; whole-line image pass on the open words
