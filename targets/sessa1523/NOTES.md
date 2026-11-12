# Duke of Sessa → Charles V, February–April 1523 — RAH Salazar A-27 (9/27), DECODE R9660–R9666

Status: in progress (23 Oct 2026, consistency pass: R9660 ff. 141v-146v still need the sign-by-sign re-transcription named in Remaining gaps, not-attempted). Read in part (follow-up 2026-09-21: R9665 read in full; R9660 transcribed in full and ~57% read)

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **R9665's three cipher
runs read** (two confirmed by the contemporary glosses). **R9660 is decoded, not read**: open groups and spelled
letters in nearly every line, only phrases can be built (10% of sentences clean, `docs/_check_reading.py`). The
~57% below is the share of tokens given a value, withdrawn as a reading figure; about 2% of the transcribed cipher
tokens read (estimated).

23 Oct 2026, re-read (REREAD_BRIEF batch b34, Claude Opus 5.5; `R9660_reread_log.md`): **R9660 kept decoded, not
read.** No text of it is reachable: the seven DECODE records of RAH 9/27 (R9660-R9666) and the neighbours R9656-R9659,
R9667-R9669 hold no decipherment; f. 141r is marked *Dup.da* (the duplicate); CSP Spain 2 has no Sessa letter of 20 Feb.
The sessa1524 key values of passes 16, 17 and b23 were applied for the first time (`reading_r9660_b34.txt`,
`research/reading_audit/b34_sessa_apply.py`): hole rate 0.28 -> 0.21; values that fail in an R9660 context (`cas`,
`rac`, `sir`, `le`, `nuf`, `foh`) left open here. Only the first cipher paragraph of f. 141r builds sentences:
`R9660_reading.md` (partial, 0.273 plain / 0.727 explicit holes), `R9660_en.md`.

Catalogue entry 146 ("Luis Fernández? (Sesa) to unknown recipient, 7 ciphertexts"). Worked 2026-09-21.

## 1. Identification: seven despatches of the Duke of Sessa to Charles V

RAH signatura 9/27 is **Colección Salazar y Castro A-27**. "Luis Fernández" is Luis Fernández de Córdoba, 2nd Duke
of Sessa, imperial ambassador in Rome (not his secretary); every letter is headed *S. C. C. M.*, so the recipient
is the Emperor. "Sesa" is right for the first letter only, which is dated from his duchy. Dates are read from the
letters' own date lines; CSP = Bergenroth, *Calendar of State Papers, Spain* vol. 2 (1866).

| DECODE | ff. | date line | CSP vol. 2 | status |
|---|---|---|---|---|
| R9660 | 141–147 | "En Sesa a xx de hebrero de 1523" | not calendared | cipher, **no decipherment** |
| R9661 | 149–152 | "En Roma, miercoles iiij de março 1523" | no. 534 (from the f. 190 copy, "cipher with contemporary deciphering") | duplicate of CSP 534 |
| R9662 | 308–326 | [12 Apr 1523] | no. 541, "a duplicate of the preceding despatch" | duplicate of CSP 540 |
| R9663 | 327–341 | [11 Apr 1523] | no. 540, ff. 327–343, "autograph in cipher, contemporary deciphering" | in print (calendar) |
| R9664 | 418–422 | "De Roma xxv de abril 1523" | no. 544, ff. 424–430 deciphered | duplicate of CSP 544 |
| R9665 | 437–438 | "De Roma xxvj de abril 1523" | not calendared | short, mostly clear |
| R9666 | 439–441 | "De Roma … abril 1523" | no. 545 (27 Apr, arrest of Cardinal Soderini of Volterra) | clear, "autograph" |

So four of the seven are the letters (or duplicates of letters) whose content Bergenroth calendared in English from
the court's decipherments kept in the same volume (ff. 190, 342–343, 424–430). Those decipherment leaves are not in
the DECODE records, so DECODE marks the ciphertexts "Non-decrypted".

## 2. The cipher is the 1524 Sessa cipher

The same code groups as [sessa1524](../sessa1524/NOTES.md) recur on every page: `gap` que, `sof` de, `suf` de la,
`qib` el, `mus` la, `kef` lo, `dim` se, `cob` si, `ka` le, `coh` Su Santidad, `bas` V.Md., `Jap` papa, `pu3 qes`
franceses, `lip` ningun-, `put` forma, `log` muy, `sis` despues, `njn` ha, the `f~` clear/cipher switch and the
`v db` null opener. The key rebuilt there (about 110 groups plus the letter alphabet, from the court's decipherments
of 1523–25 letters) applies unchanged.

## 3. Sample reading (R9660, uncalendared)

The second cipher paragraph of f. 141r read by eye with the 1524 key: [reading_f141_sample.txt](reading_f141_sample.txt) (superseded by section 5). About
half the tokens resolve at once (*muy despues … a V.Md. de la … forma que el papa … de franceses … a ver a Su
Santidad* [clear: *mas con color*] *… de ningun …* [clear: *disposicion de entender*] *… lo que V.Md. …*).

## 4. Where it stops

Outcome: **identified; four letters already in print (calendared from contemporary decipherments); the two
uncalendared cipher letters (R9660, 20 Feb; R9665, 26 Apr) read in part only.** A full reading of the ~50
cipher-bearing pages is a transcription job with the existing key (the token-tile method of sessa1524), not a
cryptanalytic one; nothing about the cipher remains unknown beyond the groups already open in sessa1524. Next
step if resumed: tokens.py over R9660 ff. 141–147, then read against key_working.md; for the calendared letters,
compare Bergenroth's abstracts with the ciphertext as a check on the key.

Images: `img/` (DECODE, fetched with the saved cookie; RAH permission required, git-ignored). Metadata: `decode/`.

## 5. Follow-up (21 Sept 2026): R9660 and R9665 run through the key

**R9665 (26 Apr 1523): read in full.** Three short cipher runs in a clear letter ([reading_r9665.txt](reading_r9665.txt)).
f. 437r: *Su Santidad por esta bula es declarado contra Francia*, confirmed token for token by a contemporary margin
note, which also gives the one new group `hef` = *por*. f. 437v: interlinear decipherments of the time, *…al de Ancona*
(Cardinal Accolti, "muy buen servidor de V. Mt.") and *Su Sd. mejoro ayer*.

**R9660 (Sessa, 20 Feb 1523): transcribed in full, read in part.** A fair copy in a clean hand, ff. 141r–147r, about
2,050 cipher tokens: [reading_r9660.txt](reading_r9660.txt) (two parts). About 57% of tokens resolve; most of the rest are code groups
(~150 distinct, listed with contexts at the end of each file). The margin notes are the copyist's restored omissions,
not decipherments. New values from the two halves (they independently agree on `boz`, `z`, `q`) are in targets/sessa1524/key_working.md
pass 15; each half's values were then retried on the other (e.g. `yim` = duque reads in both).
Content: Adrian VI stands irresolute towards the French and refuses to join the league or give French envoys a
safe-conduct; the viceroy Lannoy's visit to Rome; Francis I's plan to take a third of church revenue in France; the
Swiss envoys' pay; the Duke of Bari (Francesco Sforza); Modena and Reggio against Alberto Pio da Carpi, committed to
Cardinals Volterra, Monte and Iacobacci; Soderini (Volterra) making war on the Medici "como enemigo" with the Pope's
favour; Siena after Petrucci's death (Francesco and Fabio Petrucci); the Datario, the bishopric of Tortosa; Rimini settled.

## Remaining gaps
- R9660 decoded, not read (about 2,050 cipher tokens; after b34 a hole about every fifth word; only f. 141r's first cipher paragraph builds sentences) - blocker: no-key-material; about 100 code groups (472 occurrences) unattested in any deciphered Sessa page, the code not alphabetical
- R9660 decipherment (of this duplicate or of the first copy), if it survives - blocker: needs-physical-access; RAH volume 9/27, not imaged (seven DECODE records only; RAH Biblioteca Digital refuses automated access)
- R9660 spelled runs that do not form words as transcribed, ff. 141v-146v - blocker: not-attempted; a sign-by-sign re-transcription at full size, as done for f. 141r in b34
- R9661-R9664 cipher text re-read (CSP 534, 540, 541, 544) - blocker: needs-physical-access; read at the time and calendared by Bergenroth; the full decipherments are those same unimaged leaves
- groups open in the sessa1524 key (vo, per, hay) - blocker: needs-physical-access; inherited, no attestation in any decipherment on DECODE

## Escalation
- [x] siblings: all seven records R9660-R9666 fetched and dated; the sessa1524 sibling key identified from shared groups
- [x] clear-pages: every page of R9660-R9666 opened; the only glosses are R9665's (read) and R9660's copyist insertions (not decipherments); the decipherment leaves ff. 190, 342-343, 424-430 are not in these seven records (neighbouring DECODE records R9656-R9659, R9667-R9669 searched 23 Oct 2026: none)
- [x] known-keys: sessa1524 key_working.md applied; it fits unchanged
- [x] print: Bergenroth CSP Spain vol. 2 matched by folio (nos. 534, 540, 541, 544, 545); R9660 and R9665 not calendared
- [x] key-rebuild: 15 values added from R9660/R9665 context and the R9665 gloss (key_working.md pass 15)
- [x] retry: both halves of R9660 re-read with the pass-15 key; remaining groups have single or context-poor occurrences
- [x] retry: 23 Oct 2026 (b34) pass 16/17/b23 values applied to R9660, f. 141r paragraph re-checked at full size and built into sentences; rest kept decoded, not read

Outcome class: an audit on 21 Sept 2026 set this target to "already solved" because the court deciphered these
letters at the time. That applies to R9661-R9664 and to R9665's short runs, but not to R9660: it has no decipherment
bound with it and is not in Bergenroth. Its reading here (section 5, ~57%) is this project's own, so the class
stays "read in part".

## Sign-by-sign re-read of R9660 ff. 141v-146v, 12 Nov 2026 (Brice Dudout)

The gap "R9660 spelled runs that do not form words as transcribed, ff. 141v-146v" was attempted: the six pages were
re-read sign by sign on DECODE R9660 at full size against the b34 (a) lines. Part 1's sign written ꝍ is two signs
(a 6 with a top bar = r; a z-hook over o = s, part 2's ꝛo); a flat-topped g with a flag is d (pudiera, pedir, sin
duda, auditor); a reversed c with a stroke is q (conquistar, asiento que, ynquietud); the angle sign is ñ (compañia,
engañados, cuñado, dañaria); part 2's "ges" is qes = es (es justo, escusa, esperanças, restitucion). 124 lines change;
the transcription and 25 doubtful signs were frozen by SHA-256 before decoding. One pre-registered measure on those
lines, with one fixed key built from b34's own values: -2.423 against -2.453 per character for b34 (a), all 400
controls below (a quote-tracking bug in the frozen script skipped about half the portion; fixed, -2.507 vs -2.518,
controls below; the fix was made after the first result, and the frozen run itself passed both pre-set criteria; the gain over
b34 under one key is small, 0.03 and 0.01 per letter: the measure shows the re-read is not worse and carries Spanish, not an
improvement of substance). By the README rule a word that holds a value used from context only (x = r in resolve / restante /
Volterra, ε = i in hizieron, 9 = d, xir = cardenal) is a hole, not read: ff. 141v-146v go from 2,479 to 2,634 of the tokens sure
(69.7% -> 73.4% of 3,556 / 3,587), and 82 -> 188 more are "probable" with a context-only value; the contributor's own figure,
sure + probable, is 72.0% -> 78.7% (re-read lines 70.5% -> 80.0%). Either way R9660 stays under the bar
(`_check_reading` clean share unchanged, 0.175 -> 0.167); most of what is left is the ~100 unattested code groups. The
context-only values are not added to the key. Order of events (frozen hashes dated 12:16-12:18) by the contributor's record;
the check of signs was made with b34's (b) readings in view, so it is not a blind reading. Details: [`dudout/README.md`](dudout/README.md).

### Integration check (12 Nov 2026)

Reproduced: `scripts/measure_reread.py` (-2.4227 vs -2.4533, controls max -2.7277, p 0.0025) and
`measure_reread_fix.py --per-line-quotes` (-2.5066 vs -2.5181) give the stated figures; the frozen SHA-256 prefixes match.
`scripts/count95.py` on the shipped reading file gives 2,656 sure + 190 probable + 741 unresolved of 3,587 (79.3% sure or
probable, 74.0% sure only), not the 2,634 + 188 + 765 (78.7%) of `count95.txt`: the committed figures are kept, the
difference (0.6 point) is noted. Corrections: strict share used as the headline (sure only; probable = context-only values
are holes), the quote bug named as a change made after the result. Not checked: the sign changes against the DECODE
images (login).
