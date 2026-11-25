# Re-reading log, R9487 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b35)

## Starting point

Reading audit (22 Oct): "decoded, not read": the Claro (f. 34r) reads for A and the closing paragraph; B and the start
of C are torn half-lines. Before: `claro.md` scores 0.548 on `_check_reading.py` (file as a whole).

## 1. Is there a text already?

- DECODE R9487 re-fetched with the project cookie (`b35_fetch.py`): 4 images, no attachment, no comment. All four
  opened. The Claro on f. 34r is the only decipherment; the letter carries section marks A, B (f. 31r margin) and C.
- Neighbouring records R9486 (RAH 9/15) and R9488 (RAH 9/28): other volumes, nothing for this letter.
- Print: none found (not in the 1527 *Cartas* searched for soria1523).

## 2. The cipher, read on the image

The torn parts of the Claro are B and C, and their cipher is intact: **f. 31v, 8 lines (B)** and **f. 33r, 5 lines
(C)**. Both transcribed sign by sign from the DECODE images at full size (2.5x crops, scratchpad only):
`R9487_cipher_signs.txt` (sign names of `../soria1523/keyB.md`, a decode note per line). Decoded with key B:

- **B confirmed against the Claro where it survives**: *...presos en Roma ... de los ... se avian soltado* (Claro *se
  havian soltado*), *y huido a Narni* (∞ y m+ c y 4 = a-n-a-r-n-i), *es de maravillar de qualquiera
  des-con-cierto* (Claro *de qualquier desor[…]*), *esta la gente sin obediencia* (pob + y = si-n; xoc = gente, also in
  C *gentes*), *y con algunas diuisiones* (Claro *y con alg[…]*), *como conviene a su servicio* (peb h 4 r = servi-c-i-o),
  *alla era arrivado* (zeb = alla), *el [tob] del Vasto y dize que los ... venian* (Claro *el marques del Guasto y dize
  que los*).
- **New words where the Claro is torn**: *que si es cierto seria [xad] de inconviniente*; *qualquiera desconcierto que
  a [pur] en el dicho [yal]*; *algunas diuisiones*; *alla era arrivado el [?principe] [?de Orange]*; *venian con el
  [yal]*; in C *no [?devan] de usar de [?sacatamiento] ... contra [par] y hazer matrimonio con Francia*.
- Key observations (not adopted into keyB.md; one letter each): ∂ = s (*divisiones*, *algunas*, *usar*, *des-*;
  keyB has δ = e, a different sign); ꝗ = v and i (*maravillar*, *Narni* context, *diuisiones*); +o = y (the word *y*,
  three times); g = d (*soltado*). Code groups seen and valued by the Claro: zab = algun-, zuf = como, zeb = alla, xoc =
  gente, zif = -cierto, tob = marques (?). Groups left open: xad, soc, pur, pib, yod, ync, par, yal, tal, sab, saf, pil,
  pef, ꝑi.
- Where the Claro and the figures differ (C: Claro *por […] fazer*, figures *contra [par] y hazer*; Claro *dexan*,
  figures *devan*), the reading follows the figures with `[?]`.

## 3. Alignment

Every B and C word not in the Claro is in `R9487_cipher_signs.txt` with its signs; codes without value stay `[code]`;
partly carried words `[?word]`. Supplied words: none.

## 4. Score

| | before (claro.md, whole file) | after (R9487_reading.md, body) |
|---|---|---|
| b17 plain (LANG_=es) | 0.548 | 0.50 (11/22) |
| b17 HOLES=1 | — | **0.682 (15/22)** |

Early Spanish (1527): the explicit-hole figure is the bar, 0.68. Reader's judgement: A, the end of C and the closing
paragraph hold; B now holds in outline but has 9 holes in 4 sentences; the first sentence of C does not hold (the
Claro is torn and the cipher leaves *servido ... [par] [yof] ... era* unread). Polyphonic signs (ꝗ i/v, ∂) chosen by
sense in about 12 letters of B and C, over 3% of those passages. Stays **decoded, not read**; the reading is kept.

## Open

- Code groups xad, soc, pur, pib, yod, ync, par, yal, tal, sab, saf, pil, pef - blocker: no-key-material (key B
  lacks them; Soria's 1523 letters give no values).
- C1 *peb yic ƀ7∂ zog par yof m+r9c4m+ ƀ7cm+7c∞r* - blocker: no-key-material (signs read, sense not reached).
- Last cipher lines at the foot of f. 31r - blocker: illegible (torn and faded).

## 14 Nov 2026: second pass (Claude, session of 14 Nov 2026; audit sections I and J)

No image in this pass: DECODE's public API answers for R9487 but marks the ciphertext private (images need a login,
none in this session). The work is on `R9487_cipher_signs.txt` as transcribed on 23 Oct, the Claro (`claro.md`) and
key B (`../soria1523/keyB.md`).

1. **The Claro's last sentence aligned with the last two cipher lines of C** (f. 33r lines 4-5), group by group:
   `yoc yal pu c m+ y zof par si tef saf c zio y +o r sub ƀ r y xoc ∂ sub ꝑi y y ∞ τ 7 E ∞ c zof pef ∂ pil yed L r ∂`
   against "el Emper[ado]r(?) seran con V. Ma[gesta]d por no recebir daño, pues son gentes que saben navegar con todos
   vientos". This gives *par* = V. Magestad, *saf* = recebi-, *zio* = da- (da-n-y-o), *ꝑi* = sabe- (sabe-n), *pef* =
   todo, *pil* = vi- (vi-en-t-o-s). The 23 Oct pass had left all six open. Each lies where key B's code order puts it
   (p-groups Se-Y: V. Magestad, todo, vi-; s-groups Pa-R: recebi-; z-groups A-De: da-).
2. **Carried back.** *par* occurs four times and fits each: *[?servidores] de V. Magestad*; *a ser contra V. Magestad y
   hazer matrimonio con Francia*; *seran con V. Magestad*; in B *[yod] [ync]s. V. Magestad lo [?provea] como conbiene a
   su servicio* (the Claro has "como conviene a su servi[cio]"). *zed* = bien (z-groups A-De): *con-bien-e* in B and *y
   bien se [sab] creer que* in C. Key B's own values not used on 23 Oct: *yof* = esto; *yic* = -do (so *pil +ud yed y
   ic* is probably vi-[+ud]-en-do with *yic* split by the transcription; left as vi[+ud]endo); n+ = p (the group
   written *nf* on 23 Oct): p-r-i-n-c-i-p-e in full, and p-o-v-e-a, [?provea].
3. **Words now carried by the figures**: *los dos venian* (`xip ∂ g r ∂` = lo-s d-o-s, with g = d as in *soltado*);
   *usar desacatamiento* (`zog` = de + s-a-c-a-t-a-m-i-e-n-t-o); *estavan* at B line 7 (the same `ynf pug` that the Claro
   gives as *estavan* at line 1); *el marques* (`tob`, the Claro's word).
4. **By sense and code order only, kept `[?word]`**: *yal* = [?exercito] (three places; key B 1523 has ella; the Claro's
   word at the third was read "Emper(?)" in September); *xad* + de = [?gran]de; a + *pur* = a[?ya]; *sab* = [?puede];
   [?podria] and [?pero] (a-o-d-r-i-a, a-e-r-a-o with p for the transcribed a); [?servidores]; [?de Orange].
5. **Still open**: *soc* (rey in key B; does not fit *en [soc] de los*), *zu*, *pib*, *yod*, *ync*, *tal*, *+ud*, *pur*
   at B line 7 with the two signs after it. Blocker: no-key-material for the groups; the image (login) for the signs.

Score (`research/reading_audit/b17_score.py`, LANG_=es): plain 0.583 (14/24), explicit holes **0.833** (20/24), before
0.50 and 0.682. Words of the reading body: 291; holes 31 (27 bracketed words and the four doubtful Claro words of A,
*obrado otros hazer* and the gap in *de los y*): 260 of 291 read as sense = 0.893.

Reader's judgement: A, the closing paragraph and the end of C read; B and the start of C now build sentences that can
be translated, with holes (4 of 24 sentences keep more than one hole in ten words). Under 95%: **read in part**. The
[?word]s of point 4 and every sign of B and C still need the image.
