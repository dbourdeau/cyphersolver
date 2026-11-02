# Lope Hurtado de Mendoza (Rome) to Charles V, 1523–24 — catalogue no. 148

Status: in progress (read in part: R9846, R9866, R9868, R9869 read; R9867 and the 1523 letters open)


**22 Oct 2026, re-read (REREAD_BRIEF, batch b07; `R9667-R9869_reread_log.md`):**
* **Read now** (clean-sentence share of the reading body): **R9866** 0.667, **R9868** 0.638, **R9869** 0.622 (grade B).
  `<doc>_reading.md`, `<doc>_en.md`, `<doc>_corrections.tsv`. Every cipher run re-read on full-resolution crops of the
  DECODE images: most "unread" letters were look-alike labels, not missing key: the ß-like a transcribed `ʇʇ` (r),
  `y ʇʇ` = one sign ɣ̶ (g: coligados, enemigos, colegio), m̶ = f or c, ʒ = p. R9868 f. 430v now reads (Colonna for
  protector; Vespasiano obeys him as he did his father Prospero). R9869's f. 444v clear transcribed in full.
* **Still decoded, not read**: R9867 (0.389, open codes); R9683 and R9667 (the clear carries the whole-letter score,
  0.636 and 0.767, but their cipher passages do not build sentences: 1523 sign set not in the 1524 key, no crib);
  R9695 not attempted further. Partial readings kept for R9867, R9683, R9667.
* New probable code values (key files unchanged): zm = como, ʃeg = tengo, zub = alla (1522), zad ~ zed (arçobispo).
* No existing text: no decipherment on the images; RAH Biblioteca Digital behind a bot check (not passed).
* R9846 English written (`R9846_en.md`). Method now key recovered based on adjacent plaintext (three letters with the
  rebuilt key); fraction_read 0.23 -> 0.66 (estimated, tokens of the letters that read).

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
* **Read**: R9846 ff. 130r-v, from the clerk's contemporary clear on f. 133r (`r9846_clear.txt`), which covers the
  transcribed cipher clause for clause. English translation still to be written.
* **Decoded, not read**: R9667, R9683, R9695, R9866, R9867, R9868, R9869. Their clear text reads; the cipher runs give
  word pieces with unknown code groups in nearly every clause.
* Method now read from existing decipherment (R9846), parts for the rest; 0.45 withdrawn as a reading figure (~0.23,
  estimated, is R9846's transcribed share).

RAH Salazar A-28 (Signatura 9/28) and A-30 (9/30). DECODE R9667, R9683, R9695, R9846, R9866, R9867,
R9868, R9869. All eight marked "Non-decrypted". Opened 2026-09-21.

The catalogue entry calls this "Jun 1523, unknown recipient, 8 ciphertexts". Neither label is right: the
eight records are **five letters to the Emperor and at least two to a "muy Illustre señor"**, running from
May 1523 to March 1524, in two different volumes.

## The eight records

| rec | folios | date (from the document) | to | state |
|---|---|---|---|---|
| R9667 | 9/28 ff. 6-9 | Rome, 5 May 1523 | Emperor | clear with cipher runs; the mirrored "Claro" leaf beside it is the **Abbot of Nájera's** clear of 2 May 1523, not Hurtado's; CSP Spain ii **548** abstracts it from a contemporary deciphering not among the images |
| R9683 | 9/28 f. 171 | Rome, 10 June 1523 | Emperor | clear with 8 cipher lines; no decipherment; not in CSP |
| R9695 | 9/28 ff. 339-340 | Rome, viij **July** 1523 (DECODE: June) | Emperor | autograph draft, clear with cipher lines, much struck through; not in CSP |
| R9846 | 9/30 ff. 130-133 | Rome, 3 and 5 Feb 1524 | Emperor | almost all cipher (ff. 130r-132v); **clear version on f. 133r** (first third imaged); CSP Spain ii **617** |
| R9866 | 9/30 ff. 285-286 | Rome, 28 Feb 1524 | Grand Chancellor Gattinara | half cipher; no decipherment; not in CSP |
| R9867 | 9/30 f. 351 | Rome, 4 Jan 1524 (date spelled in cipher) | Emperor | wholly cipher, 30 lines; not in CSP |
| R9868 | 9/30 ff. 430-431 | Rome, 20 Mar 1524 | Grand Chancellor Gattinara | half cipher; not in CSP |
| R9869 | 9/30 ff. 444-445 | Rome, 28 Mar 1524 | Emperor | half cipher; not in CSP |

The CSP check used Bergenroth's CSP Spain vol. 2, pp. 547–709 (fetched to `csp/`), grepping "Salazar. A. 28/30. f."
for each folio. R9667 = no. 548 (A. 28 ff. 6-9) and R9846 = no. 617 (A. 30 ff. 130-133). The other six folios are not
calendared.

## Cipher

It is the same system as the 1522 letters (`targets/lopehurtado/`, catalogue 144): latin-trigram codes (`ton` que, `zar` de,
`xul` lo, `rab` vuestra magestad, `taf` papa, `yub`/`ɣub` el, `tu` no, `tod` otro, `teg` para, `sed`, `xug` la) plus a
letter alphabet of cursive signs. The 1522 key is the starting point.

## The key from R9846's clear (the way in)

R9846 f. 133r is the clerk's clear of the first third of the 5 Feb 1524 letter. Aligned clause for clause
against ff. 130r-130v (38 cipher lines): `key_1524.tsv`, 105 values (65 confirmed), plus `key_1524_additions.tsv`
and `key_1523_additions.tsv`. Most of the homophonic letter alphabet falls out of exact-count spelled runs
(`r9846_alignment.md`). 1522 values n/e/a/o re-confirmed; 25 of the 1522 codes re-confirmed.
**The key moved between 1522 and 1524:** `tef` is *paz* in 1522 but *nec-* (necesidad, necesario) three times in 1524;
`L` is i in 1522 but r here.

R9667's "Claro" leaf is a trap: mirrored, docketed "Del abbad de Najera a dos de mayo" - the clear of the Abbot
of Nájera's letter, bound beside Hurtado's. No crib for R9667.

## What was read (all "read in part"; coverage = tokens with a value, an upper bound)

| rec | cipher tokens valued | reads as Spanish | gist |
|---|---|---|---|
| R9667 | fragments | little | benefices for the Pope's servants (list on f. 7); CSP 548 has the content |
| R9683 | 67/91 | fragments | clear: Pope well disposed since Volterra's arrest; restore benefices of the camarero and Francisco |
| R9695 | 184/249 | no | clear: rumoured poisoning, Duke of Camarino's men in prison, naturalisations for the Pope's intimates |
| R9846 | crib third read; rest per CSP 617 | first third | Beaurain's coming; the Pope wants France ruined or a truce |
| R9867 | 418/467 | ~60% | Beaurain has left the Pope content; the Emperor must not show need of money |
| R9866 | 561/649 | a quarter to a third | to Gattinara: the French mean to stay this side of the Alps; the writer's unpaid salary |
| R9868 | 328/353 | f. 430r mostly | to Gattinara: Capua gone, all business hangs on the Datary, who must be satisfied |
| R9869 | 310/339 | about two thirds | Pope's money offer via Beaurain; Florence undecided; the archbishop of Capua to be well received |

Readings in `read_r*.md`. Where it stops: about 30 code groups (`xun`, `xor`, `zad`, `ʃal`, `ʃub`, `rub` vs `yub`...),
and look-alike signs (∂ vs barred ∂, two- vs three-bar crosses, barred m = f or c) needing better images than DECODE's.
The unimaged f. 133v (rest of R9846's clear) would give more; RAH Biblioteca Digital, Salazar A-30.

## Remaining gaps

- R9667 (5 May 1523), cipher runs decoded, not read - blocker: no-key-material (1523 sign set, no crib); needs-physical-access for the contemporary decipherment CSP 548 used (RAH Salazar A-28)
- R9683 (June 1523), cipher passage decoded, not read - blocker: no-key-material (1523 sign set, no crib)
- R9695 (8 July 1523), decoded, not read - blocker: no-key-material; not attempted further on 22 Oct (struck autograph draft)
- R9867 (4 Jan 1524), decoded, not read (0.389) - blocker: no-key-material (rub, ʃug, tol, xer, xal, xir, ʃal, co, ℮, ʃφ)
- R9866, R9868, R9869: read 22 Oct 2026 (b07); scattered holes on open codes - blocker: no-key-material
- R9846 ff. 130v-132v beyond the crib third - blocker: needs-physical-access; f. 133v, the rest of the clerk's clear, is not imaged on DECODE; RAH Biblioteca Digital (bot check), Salazar A-30
- About 20 code groups (rub, ʃug, zid, tol, tid, zib, xer, xir, xal, ʃal, yab, tas, toc, yic, co ...) - blocker: no-key-material; no crib
- Look-alike signs - mostly resolved word by word on 22 Oct (`<doc>_corrections.tsv`); the rest blocker: illegible at DECODE resolution

## Escalation

- [x] siblings: all eight records in Salazar 9/28 and 9/30 opened and dated; the 1522 letters (targets/lopehurtado/) used
- [x] clear-pages: R9846 f. 133r clear aligned (key_1524.tsv); R9667's 'Claro' leaf checked and shown to be Najera's
- [x] known-keys: the 1522 key applied; 25 codes and n/e/a/o re-confirmed, tef and L shown to have moved
- [x] print: Bergenroth CSP Spain ii pp. 547-709 grepped by Salazar folio: nos. 548 and 617, the other six not calendared
- [x] key-rebuild: key_1524.tsv (105 values, 65 confirmed) plus 1523/1524 additions from exact-count runs
- [x] retry: 21 Sept merged key and open-code pass (`retry_2026-09-21.md`); 22 Oct sign-by-sign re-read on the images (b07): R9866, R9868, R9869 read; CSP 548 used for R9667 run C only

## Dudout corrections, 29 Oct 2026
- Pacheco y de Leyva, La politica espanola en Italia, vol. I (1919), no. 120 prints the Abbot of Najera's letter of 2 May 1523 (RAH Salazar A-28 ff. 1-2, 'claro y cifra') deciphered: this is the 'Claro' leaf noted beside R9667. The same edition prints about 33 letters of 1522 from BNE Sigt. mod. 18.678 (nos. 49-105); catalogue 1274 is closed as read.
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
