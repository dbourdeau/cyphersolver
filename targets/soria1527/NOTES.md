# Lope de Soria (Mirandola) to Charles V, 13 Dec 1527 (not 1517) — RAH Salazar 9/17 ff. 31–34, DECODE R9487

Status: in progress. Read in part (14 Nov 2026): 260 of 291 words of the reading (0.893); A and the closing paragraph from the Claro, B and C from the Claro's half-lines and the cipher decoded with key B; code groups open, signs not rechecked on the image.

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): claro.md builds sentences for section A and the closing paragraph only; B and the start of C are half-lines on a torn leaf. R9487 is *decoded, not read* in profile.json; class already solved is kept (read at the time); fraction_read estimated 0.5. The f. 31v cipher block is intact and could fill the tear with key B.

Earlier status (before the 22 Oct 2026 reading audit): no write-up

**Verdict: read at the time. The court's decipherment ("Claro", sections A, B, C) is bound with the letter as
f. 34r.** The date is 1527, not 1517. Catalogue entry 142 is resolved and removed. Checked in one session on
2026-09-21.


**23 Oct 2026, re-read b35** (`R9487_reread_log.md`): the intact cipher of B (f. 31v, 8 lines) and of C (f. 33r, 5
lines) transcribed sign by sign from the DECODE images (`R9487_cipher_signs.txt`) and decoded with key B. It confirms
the Claro's half-lines and fills part of the tear (*que si es cierto seria [xad] de inconviniente*; *algunas
diuisiones*; *alla era arrivado el [?principe] [?de Orange]*; *no [?devan] de usar de [?sacatamiento] ... contra [par] y
hazer matrimonio*). `R9487_reading.md` / `R9487_en.md`: 0.50 plain, 0.682 explicit holes; B and the first line of C
keep unvalued code groups and polyphonic choices, so the letter stays **decoded, not read**.

## Sources

- DECODE R9487 ("Non-decrypted", 4 images, 13 Dec 1517). The images were fetched with the shared cookie into
  `decode/`. They are git-ignored, and RAH permission is needed to reproduce them.
- Sibling target `targets/soria1523/` (Soria in Genoa, 1523; key B rebuilt there from R9844).

## The document

| image | folio | content |
|---|---|---|
| 1 right | 31r | "Sacra Ces. y Cat. Md." Opens in clear: "Por diversas vias tengo escrito a V. Ces. Md. despues que se perdio Genova ... recibi en Ferrara a los seis de otubre". A: 7 cipher lines (torn at the right), then clear islands about Venice, Ferrara, Lombardy, the Pope and cardinals, "lo perdido ... temor que todos tiene", and more cipher lines at the foot |
| 2/3 left | 31v | 9 intact cipher lines, then clear: the galleys of France and Venice, Sicily, the Duke of Ferrara having entered the league, "restituir el estado a Federico", and cipher at the foot |
| 2/3 right | 32r–33r | clear: five thousand Germans, Bologna; waiting at Mirandola with the Duke of Genoa(?) for the Emperor's orders. On 33r: 5 cipher lines (C), clear "todos los enemigos se retiraron de cabe Milan ... Antonio de Leyva y corre por do quiere", then more cipher (torn) |
| 4 left | 33v | clear: "el papa ... ya era ido el papa a Orvieto", two Spanish and two German hostages, "el papa en su libertad enteramente", Antonio de Leyva |
| 4 right | 34r | docket "Al Rey. De Lope de Soria de la Mirandula xiij de deziembre [1]527"; **decipherment** "Claro" A, B, C in a secretary's hand. Transcribed in `claro.md` |

## Date: 1527

The pencilled "1517. 13. de Dec." at the head of f. 31r, which DECODE copied, is a misreading. The content is that of
Dec 1527. Genoa has been lost (to the French and Andrea Doria, Aug 1527). Clement VII has left Rome for Orvieto (7–8
Dec 1527) and is "en su libertad". Antonio de Leyva holds the field around Milan. Bourbon's jewels are pawned at Genoa
(Bourbon died at Rome in May 1527). Federico is to be restored (Gonzaga of Bozzolo?). The docket on f. 34r ends in
"…27".

## Checking the decipherment against the cipher

The cipher is the three-letter code plus homophonic letters of Soria's 1523 key B (`targets/soria1523/keyB.md`), used here
four years earlier.

- C (f. 33r, the 5 intact lines): `4∞Lc4zryqr zof xab` = *matrimonio con Francia* (4=m/i, ∞=a, L=t, c=r, r=o, y=n,
  zof=con, xab=Francia); `si tef` = *por no*; `y∞τ7ε∞c zof` = *navegar con*; `sub` = *que*. The claro has "fazer
  matrimonio con Francia ... por no recebir daño pues son gentes que saben navegar con todos vientos".
- A (f. 31r): `zrLqL∞yh∞ zog` = *[q]uitança[s] de*, and the claro has "les haya fecho quitanças de toda la suma".

So f. 34r is the decipherment of this letter's cipher.

## Gaps

- Claro B and the start of C are torn (see `claro.md`). The f. 31v cipher block (9 lines) is intact. Decoding it with
  key B would fill the claro's gaps if it is section B. Not attempted in this session: the sign-by-sign transcription
  is not done. Blocker: not-attempted.
- The last cipher lines on f. 31r and f. 33r are torn and faded.

## Why no write-up

The letter was read at the time, and its decipherment is bound with it. The new results are identifying f. 34r as
that decipherment and correcting the date to 1527. Per CLAUDE.md this is `Status: no write-up`. The DECODE date and
status correction are queued in `decode_updates/queue.json`.

## 14 Nov 2026: second re-read, read in part

Done from the files in the folder (no image: DECODE R9487 is behind a login, none in this session); log in
`R9487_reread_log.md`, section "14 Nov 2026".

- The Claro's last sentence (*seran con V. Magestad por no recebir daño ... saben navegar con todos vientos*) was aligned
  group by group with the last two cipher lines of C. It gives six code groups the 23 Oct pass had left open: *par* =
  V. Magestad, *saf* = recebi-, *zio* = da-, *ꝑi* = sabe-, *pef* = todo, *pil* = vi-.
- Carried back, *par* fits its four places (*contra V. Magestad y hazer matrimonio con Francia*; *V. Magestad lo
  [?provea] como conbiene a su servicio*). With key B's own *yof* = esto and n+ = p, and *zed* = bien, the figures now
  give *el principe*, *los dos venian con el [?exercito]*, *no dexan de usar desacatamiento*, *y bien se [?puede] creer*.
- *yal* (three times) is read [?exercito] by sense and code order only; the Claro's word there was read "Emper(?)".
- `R9487_reading.md` and `R9487_en.md` rewritten. Score: explicit holes 0.833 (20/24), plain 0.583; before 0.682 and 0.50.
  260 of 291 words read as sense (0.893).
- The entry is now `read in part` (was decoded, not read), and the class `read in part` (was already solved): the
  court read the letter at the time, but its decipherment is torn, and what is in hand reads in part.
- Open: the groups *soc*, *zu*, *pib*, *yod*, *ync*, *tal*, *+ud*, one *pur*; the [?word]s; the image check.

## Remaining gaps

- code groups of B and C with no value (soc, zu, pib, yod, ync, tal, +ud, pur at B line 7) - blocker: no-key-material; key B lacks them or gives a value that does not fit (soc = rey), and the Claro is torn there
- words read by sense or with a sign other than the one transcribed ([?exercito] for yal, [?gran]de, a[?ya], [?puede], [?provea], [?de Orange], [?servidores], [?podria], [?pero]) - blocker: no-key-material for the groups; for the signs the DECODE R9487 images (login) are needed and were not available on 14 Nov 2026
- the Claro's *obrado otros hazer mil* and *de los y de las joyas* in A, and *ronuezino e sprann* in the closing paragraph - blocker: illegible; doubtful readings of the Claro's hand on the DECODE image (login needed to look again)
- last cipher lines of f. 31r and f. 33r (the cipher of A and of the closing paragraph) - blocker: illegible; torn and faded, read from the Claro only

## Escalation

- [x] siblings: soria1523 (key B) used to check the Claro against the cipher
- [x] clear-pages: the Claro, f. 34r, transcribed in claro.md
- [x] known-keys: Soria's 1523 key B fits (spot checks on A and C)
- [x] print: nothing found for this letter (23 Oct 2026)
- [n/a] key-rebuild: key B exists
- [x] retry: 23 Oct 2026 (b35), f. 31v and f. 33r cipher transcribed and decoded with key B; 14 Nov 2026, the Claro's last sentence aligned with the cipher (six groups valued), read in part
