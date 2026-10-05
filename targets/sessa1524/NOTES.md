# Duke of Sessa (Luis Fernández de Córdoba) → Charles V, Rome, 18 April 1524 — RAH Salazar A-31 (9/31) ff. 128–131

DECODE R9877 (ff. 128–129) and R9878 (ff. 130–131), catalogued "Luis Fernández, Rome, April **1424**,
Non-decrypted, 4 pp. each". Picked on 2026-09-18 as the longest pre-1450 ciphertext (research/oldest/CANDIDATES.md A2).

## 1. Not 1424: it is 1524, and not a blind break

- **DECODE's date is a typo.** The same series runs on as R9888–R9895 "1524"; the senders are Luis Fernández de
  Córdoba, 2nd **Duke of Sessa**, imperial ambassador at Rome 1522–26, and Lope Hurtado de Mendoza (1499–1558);
  RAH 9/31 is **Colección Salazar y Castro A-31**, which Bergenroth calendars in *CSP Spain* vol. 2 for April–May
  1524 ("M. Re. Ac. d. Hist. Salazar. A. 31. f. …"). The target itself is dated on f. 128v: **"De Roma xviij de
  Abril 1524"**. R9878 (ff. 130–131) is the duplicate of the same letter, sent by a second courier (both copies
  end "Al visorrey escrivo en el mismo punto"). Bergenroth skipped this letter (he has only Lope Hurtado's of the
  same day, no. 642, from the A-33 abstracts).
- **Sibling letters in the same cipher carry contemporary decipherments** ("Decrypted" in DECODE): f. 138 with
  its clear on f. 140 (17 Apr, CSP 639), ff. 170–171 with clear on f. 172 (22 Apr, CSP 643), ff. 322–323 with
  clear on f. 324 (19 May, CSP 651). The decipherer is the court's (Pedro de Soria, per Bergenroth's vol. 3
  introduction). So the route is key-from-sibling, the project's standard one.

| CSP no. | date | letter | Salazar A. 31 | DECODE |
|---|---|---|---|---|
| 633/635 | 13 Apr | Lope Hurtado → Emperor / → Gattinara | ff. 61–67 | R9871, R9872 Decrypted |
| 637 | 14 Apr | Sessa → Emperor (Goicoechea's 19th-c. reading) | f. 79 | R9873 ff. 79–86 |
| 639 | 17 Apr | Sessa → Emperor | ff. 138–140 | R9881 **Decrypted** |
| — | **18 Apr** | **Sessa → Emperor, this letter + duplicate** | **ff. 128–131** | **R9877, R9878** |
| 643 | 22 Apr | Sessa → Emperor | ff. 163–172 | R9883, R9884 **Decrypted** |
| 651 | 19 May | Sessa → Emperor | ff. 320–324 | R9890 **Decrypted** |

## 2. The cipher (Sessa–Charles V, Rome, 1524)

Mixed nomenclator in a rounded chancery hand: three-letter code groups for words and syllables (`gap` que, `sof`
de, `mus` la, `dim` se…), single letters and signs for spelling (`α` a, `ott` t, `4` o, `#` g, `nf` p, `ꝑo` the
plural -s suffix), `f~` as the clear/cipher switch and clause mark, `v db` as a null opener of each cipher
paragraph. Working key with evidence: [key_working.md](key_working.md). Cipher/clear pairs:
[pairs_f170.txt](pairs_f170.txt), [cipher_f138.txt](cipher_f138.txt) against [clear_f140.txt](clear_f140.txt),
[clear_f172.txt](clear_f172.txt), [clear_f324.txt](clear_f324.txt).

Secure code values (each aligned in at least one sibling): que `gap`, de `sof`, del/de l- `suf`, la `mus`, las
`mus ꝑo`, el `qib`, lo `kef`, no `ler`/`lex`, se `dim`, le/les `ka`, y `q+`, he `ma`, en `qid`, su Santidad `coh`,
rey `fad`, paz `Jep`, tregua `bob`, Francia `po3`, Inglaterra `mef`, suyços `cum`, arçobispo de Capua `yom`,
persona `lax`, platica `tud`, muy `log`, con `tat`/`tar`, mal `kch`, esta `qet`, sabe `dog`, sabia `dug`, mas `kah`,
scrito `pur`, muestra `luf`, ni `lep`, otra `lum`, parte `lux`, uno `baq`, otro `Jom`, por `hef`, forma `put`,
ningun- `lip`, franceses `qes`, ha `mn`, os `Jim`, di `g3`, do `ram`, si `cob`, t `ott`, ca `ttt α`.

## 3. Reading of ff. 128–131 (2026-09-18, in part; eight passes, see key_working.md)

Clear opening (f. 128r): *Teniendo escripto y cerrado el pliego del duplicado de xiiij deste que sera con esta, vi
una letra del obispo Verulano que esta en Constancia, de que aqui embio copia. Luego embie a Su Santidad a
suplicalle me mandase avisar de alguna particularidad para dar noticia della do conviniese. Mandome a mi Felice su
secretario, el qual me ha dicho que las letras que tiene son del dicho Verulano de vj y vij del presente, do dize
que hera acabada la dieta, y que Lucerna no concluyo de dar ayuda a franceses; que los cantones de Berna y Friburk
y Solodor, y para mas facilitarla y traer los animos del pueblo, publican que los suyços en Lombardia estavan
cercados y en grand peligro, con que juntava hasta el numero de ocho mill, que davan nombre de partir muy presto,
pero que el no podia saber el quando, por estar en Costancia donde algunos de sus amigos de Suyça le escrivian para
que exortase a Sus. que buscase alguna buena forma de paz. Esto es lo que me ha referido.*

Cipher (eight lines on f. 128r, one on f. 128v; the duplicate ff. 130–131 is token-for-token the same). Method:
every line cut into tokens by `tokens.py` (sheets in `tok/`, one PNG per token in `tok/*_tiles/`), the same done
for the deciphered siblings f. 138, ff. 168v, 170–171 and 322, and values assigned by aligning those against
their clears (f. 140, f. 172, f. 324). Transcription: [transcription_f128.txt](transcription_f128.txt).

> ¶ las dichas [vo]s no le las mostraron, que le ponen sospecha que desea aver algo que r-e-f-i-e-r-a de lo suso
> [ruc] [hay] no / **me parece que concuerda mucho con lo primero y postrero que el dicho obispo dize al maestro de
> postas** / hablé en la ora a Su Santidad a **pedirle que haya provisión** de [pa]-r-a los casos de suyços,
> persuadiéndole los m-re que r-ido los que no m-r-e-van / **pues tiene color para ello, aviendo començado** la
> plática de la paz y tregua r-[…] **entender lo que mas podré. Al visorrey escrivo en el mismo punto.**

Sense: Felice will not show Sessa the bishop's own letters, since they make him suspect that Sessa wants to get
something out of them for himself; Sessa nonetheless finds the report consistent with what the bishop writes to
the postmaster (Gabriel de Tassis: his Italian letter of 6 April, *tutti Elvetij son in arme … expedisca volando a
Milano et Roma*, is bound as f. 131); he went at once to the Pope to ask for a provision of money for the Swiss
business, persuading him that he has the colour (pretext) for it, having opened the peace-and-truce negotiation.
This is the news Bergenroth abstracts from the 22 April letter (CSP 643).

Pass 10 (the January 1525 letter R9897, same cipher, verbose clear on ff. 14v–15; fetched with the saved DECODE
cookie) attested `rad` = *dicha*, `boy`/`bez` = *-ido*, `Є` = *h*, `kel` = `kef` (*los*), and `lif 3` = *quiere*
(key_working.md, pass 10). Unread now: `vo` (the noun after *dichas*: the bishop's letters or their copies),
`z y` (the verb after *quiere*, *mostrar* from the sense), `per`, `rus`, `hay`, and the clause *los m-re que r-ido
los que no m-r-e-van*, where one sign value (probably `v`) is still wrong. The other 1525 letter, R9898 (14 pp.),
was then read through as well (pass 12): it seemed to carry no decipherment (wrong: see section 5, it has six marginal ones), so it gave only
contexts (`z y` also after *si*; `ruc`/`rus` is a person who *ha respondido*; `hud` again in *la plática de la paz*).
Pass 13 (the 24 July 1524 letter R9893, cipher f. 483 with its clear on f. 485) corrected `lif` to *mostrar*
(*ni se quiere mostrar* = `lep dim fa lif 3 α`, `fa` = *quiere*) and gave `zum` = *hay*, `tas` *cosa*, `luh`
*mundo*, `qit` *estado*, `lic` *monsieur*, `gel` *qual*. Open now: `vo`, `z y` (after *mostrar*; also after
*si* in 1525; probably a conjunction, *porque* or *diziendo*), `per`, `rus`/`ruc` (a person), and the clause
*los m-re que r-ido*.

Pass 14 matched templates of the unread tokens against every downloaded page (`tmatch.py`). The September 1523
letter R9834, whose cipher faces its clear on f. 38, gives `z y` = *-on* (*dilataron*, *concedieron*), so the first
sentence reads *las dichas [vo]s no le las mostraron*. `ruc` and `hay` occur only in the 14 April 1524 letter R9873,
which has no decipherment; `vo` and `per` match nowhere. Those four are the residue.

The seven 1523 Sessa letters DECODE marks "Decrypted" (R9676, R9691, R9693, R9781, R9834, R9836, R9841; about 50
pages, fetched into `img/` with the cookie) use **the same cipher** (`sof`, `gap`, `ram`, `bas`, `qes`, `lex`, `cih`
all recur; R9781's August 1523 cipher block has its clear on f. 651). They are the remaining source for the four
open groups; aligning them is the same token-sheet work as passes 1–13. Pass 11 (the rest of
R9897, ff. 10–13v, against ff. 14v–15) confirmed `hud` = *plática*, `rad` = *dicha*, and added *larga*, *fue*,
*esto*, *tiempo*, *para*, *después*, *llegar*, *miento*, but none of the five (key_working.md, pass 11).

## 4. Images

DECODE images (RAH material, not public domain) are git-ignored in `img/`; only the public 200-px thumbnails and
the record pages are in `decode/`. Filesrv names: IMG_R9877_I46030_P1/P2, IMG_R9878_I46033_P1/P2,
IMG_R9881_I46038_P1/P2, IMG_R9884_I46049_P1–P4, IMG_R9890_I46073_P1–P3 (P4 not yet fetched), plus the neighbours
in section 1. Daniel downloads them logged in and drops them in `img/`.

To attest the nine open groups, the next deciphered Sessa letters (same correspondent, a year later, "Decrypted",
14 pp. each) are the ones to fetch, logged in, into `img/`:
- https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R9897_I46110_P1.jpg … `_P7.jpg` (9/34 ff. 10–16, 1525)
- https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R9898_I46118_P1.jpg … `_P7.jpg` (9/34 ff. 150–156, 1525)
Then `python tokens.py <img> x0 y0 x1 y1 tok/<name>.png` per cipher line and search the tile sheets for `rad`,
`vo`, `lif`, `per`, `kel`, `boy`, `rus`, `hay`.

## 5. R9873 (14 Apr 1524) and R9898 (24 Feb 1525) transcribed and read in part (pass 16, 2 Oct 2026)

Both letters were transcribed in full from `img/` into the (a) cipher / (b) reading convention of
`targets/sessa1523/reading_r9660.txt`: [r9873_cipher.txt](r9873_cipher.txt), [r9898_cipher.txt](r9898_cipher.txt).
Readings, content and gaps: [read_r9873.md](read_r9873.md), [read_r9898.md](read_r9898.md). Share read as sense,
measured by [measure_read.py](measure_read.py) (each assembled word scored on `lang` `es-golden-age`):

| letter | cipher tokens | read as sense | open groups | letters without sense | status |
|---|---|---|---|---|---|
| R9873, Sessa 14 Apr 1524, A-31 ff. 79-86 | 2,473 | 2,165 (87.5%) | 256 tokens | 52 | read in part |
| R9898, Sessa 24 Feb 1525, A-34 ff. 150-156 | 3,059 | 2,361 (77.2%) | 300 tokens | 398 (bleed-through) | read in part |

- **R9898 is not without decipherment** (corrects pass 12 above): six cipher runs carry a contemporary marginal
  decipherment in a second hand (ff. 150r, 152r, 153v, 154r, 154v x3, 156r). They are the cribs of pass 16.
- **R9873** is CSP Spain ii 637 (Goicoechea's 19th-c. reading, not bound); no. 636 is the triplicate with its
  deciphering, no. 638 the court abstract ([csp/csp2_636_638.txt](csp/csp2_636_638.txt)). The reading follows no. 636
  topic by topic (cortes and the coming to Italy; Capua from Blois; the two proposals; the pension; 4,000 ducats at
  Lodi; the nuncio's letters of 26 March; Wolsey's "honest colour"; the English will not contribute).
- Pass 16 values (key_working.md): `ruc`/`rus` = dicho, `hay` = aunque (tentative), `v em` = cierto, `li` = mi,
  `le` = me, `net` = halla, `lec` = -mos, `yol` = aqui, `sud` = datario, `fed` = rey de Francia, `xir` = cardenal,
  `lot` = nuncio, `pof` = exercito, `kuc` = liga, `tig` = contra, `cuq` = tengo, `yod`/`quf` = amigo/enemigo, and
  the name *Micer Agostino Foyeta* (Foglietta). For f. 128 this closes two of the four residue groups:
  *de lo suso[rus] [hay] no* = **de lo susodicho, aunque no, me parece que concuerda mucho con lo primero**.


**Pass 17 (3 Oct 2026, target 95%).** Open groups pooled across R9873, R9898 and R9660 (key_working.md pass 17),
R9873's non-words re-checked at 1.5-1.6x, CSP 636 used phrase by phrase, the RAH Biblioteca Digital checked for a
better image of R9898 (its search sits behind a bot wall; web search finds no digitised Salazar A-34; DECODE's scans
remain the only images). measure_read.py now joins words broken across lines and accepts period spellings found in
the es corpora. Result, before -> after (strict = pass-17 tentative values counted as open):

| letter | pass 16 | pass 17 | pass 17 strict |
|---|---|---|---|
| R9873 | 87.5% | 92.8% | 87.8% |
| R9898 | 77.2% | 79.8% | 77.9% |
| f. 128 (transcription_f128.txt) | 88% (102/116) | 90% (104/116), not re-measured with measure_read.py (mixed file) | |

95% was not reached. What stands between: about 100 R9873 groups and 140 R9898 groups seen only once (no
deciphered occurrence anywhere), and R9898's bleed-through pages, which do not resolve at higher zoom.

## Remaining gaps
- group `vo` (noun after *las dichas*, f. 128r) - blocker: open-codes; absent from R9873 and R9898 as well (pass 16) and from every other downloaded page (pass 14)
- group `per` - blocker: open-codes; absent from R9873 and R9898 (pass 16) and every other downloaded page (pass 14)
- `hay` = aunque is tentative (four contexts in R9873, none deciphered) - blocker: open-codes; no deciphered occurrence
- clause *los m-re que r-ido los que no m-r-e-van* - blocker: open-codes; one sign value (probably `v`) still wrong after 16 passes
- R9873: about 100 code groups (145 tokens) and 34 spelled letters without sense - blocker: open-codes; single contexts after pooling with R9898 and R9660 (pass 17); the non-words were re-checked at full zoom and stand as written
- R9898: about 140 code groups (237 tokens) - blocker: open-codes; single contexts after pooling (pass 17), not in the six marginal decipherments
- R9898: 381 letter tokens on the bleed-through pages ff. 150v-151r, 155v - blocker: illegible; re-cut at 1.5x without gain; no other image route (RAH Biblioteca Digital has no digitised A-34 that could be found)

## Escalation
- [x] siblings: R9878 duplicate collated; R9881, R9883/4, R9890, R9893, R9834, R9897, R9898 read against their clears (passes 1-14); R9873 and R9898 transcribed in full (pass 16)
- [x] clear-pages: clears f. 140, f. 172, f. 324, f. 485, f. 38, ff. 14v-15 aligned; R9898's six marginal decipherments found and aligned (pass 16; pass 12 had missed them)
- [x] known-keys: one cipher throughout 1523-25; the key was built from its own siblings, no other key of the series is known
- [x] print: Bergenroth CSP Spain vol. 2 checked (f. 128 not calendared; R9873 = nos. 636-638, used as a topic crib); CSP iii.1 checked for R9898 (not calendared)
- [x] key-rebuild: key_working.md extended over 16 passes by crib alignment, template matching (tmatch.py) and the R9898 margins
- [x] retry: rerun 3 Oct 2026 with the pass-17 pooled values (R9873 92.8%, R9898 79.8%); rerun 21 Sept 2026 with the pass-15 key over R9660 (no change); rerun 2 Oct 2026 with the pass-16 key over f. 128: `rus` = dicho and `hay` = aunque fill the residue *de lo susodicho, aunque no*; `vo`, `per` and the m-re clause still open
