# Duke of Sessa (Luis Fernández de Córdoba) → Charles V, Rome, 18 April 1524 — RAH Salazar A-31 (9/31) ff. 128–131

DECODE R9877 (ff. 128–129) and R9878 (ff. 130–131), catalogued "Luis Fernández, Rome, April **1424**,
Non-decrypted, 4 pp. each". Picked on 2026-09-18 as the longest pre-1450 ciphertext (research/oldest/CANDIDATES.md A2).

Status: read in part

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**. f. 128's
nine cipher lines (R9877/R9878) build Spanish sentences with single-word holes (`texts/f128_decryption.md`).
**R9873 and R9898 are decoded, not read**: their files are line-by-line working decodes with an open code group or a
non-word in most sentences, and `read_r9873.md` / `read_r9898.md` give English gists, not texts. Reading figure 2.1%
(116 of 5,648 tokens across the three documents); the 90% (f. 128 alone) and the siblings' 92.8% / 79.8% are withdrawn
as reading figures.

23 Oct 2026, re-read (batch b23, REREAD_BRIEF): **R9873 now reads** (grade B): [r9873_reading.md](r9873_reading.md),
continuous Spanish in the 1524 spelling, every word aligned with the decode or the clear text
(`research/reading_audit/b23_sessa_align.py`), English in [r9873_en.md](r9873_en.md); 0.715 clean sentences counting
explicit holes (0.399 plain; the working file scored 0.13). f. 83r ll. 19-25 still does not hold. **R9898 stays
decoded, not read** ([r9898_reading.md](r9898_reading.md), partial, 0.47 on explicit holes): bleed-through pages and
some 140 single-context groups. New sibling R9899 (A-34 ff. 194-195, March 1525): one marginal decipherment, `hog` =
*querria*. Key values adopted: `gal` embia-, `hog` querria, `kaz` -mente (attested), `reb` dezi-, `dis` servido,
`cer` teni, `lar` miento, `sur`/`luc` parte, `tt` plural s, `gul` si, `nuf` gente, `qu` o, `gom` quatro (sense-only,
flagged). Reading figure 2.1% -> 45.8% (f. 128 + R9873 = 2,589 of 5,648 tokens). Log:
[texts/r9873-r9898_reread_log.md](texts/r9873-r9898_reread_log.md).

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
- R9873 read (23 Oct 2026, b23); about 70 open code groups, single contexts, and the stretch f. 83r ll. 19-25 - blocker: no-key-material; pooled with R9898, R9899, f. 128 and R9660, no deciphered occurrence; the triplicate with its contemporary deciphering (CSP 636, Gayangos MS) and Goicoechea's reading are not imaged or online
- R9898 decoded, not read (0.47 on explicit holes, b23): about 140 code groups seen once - blocker: no-key-material; not in the six marginal decipherments nor in any sibling
- R9898: letter tokens on the bleed-through pages ff. 150v-151r, 155v - blocker: illegible; re-cut at 1.5x and 2x without gain; DECODE's scans the only image (RAH Biblioteca Digital has no digitised A-34 that could be found)
- group `vo` (noun after *las dichas*, f. 128r) - blocker: no-key-material; absent from R9873, R9898, R9899 and every other downloaded page
- group `per` - blocker: no-key-material; absent from R9873, R9898, R9899 and every other downloaded page
- `hay` = aunque is tentative - blocker: no-key-material; no deciphered occurrence, and it does not read *aunque* in R9873 f. 81r
- clause *los m-re que r-ido los que no m-r-e-van* (f. 128) - blocker: no-key-material; one sign value still wrong, no sibling decipherment covers it

## Escalation
- [x] siblings: R9899 (A-34 ff. 194-195) checked 23 Oct 2026, one marginal decipherment (`hog` querria); R9878 duplicate collated; R9881, R9883/4, R9890, R9893, R9834, R9897, R9898 read against their clears (passes 1-14); R9873 and R9898 transcribed in full (pass 16)
- [x] clear-pages: clears f. 140, f. 172, f. 324, f. 485, f. 38, ff. 14v-15 aligned; R9898's six marginal decipherments found and aligned (pass 16; pass 12 had missed them)
- [x] known-keys: one cipher throughout 1523-25; the key was built from its own siblings, no other key of the series is known
- [x] print: Gayangos triplicate (CSP 636) and Goicoechea's reading (CSP 637) searched online 23 Oct 2026, not found (Kolosova 2016/17 thesis a lead); Bergenroth CSP Spain vol. 2 checked (f. 128 not calendared; R9873 = nos. 636-638, used as a topic crib); CSP iii.1 checked for R9898 (not calendared)
- [x] key-rebuild: key_working.md extended over 16 passes by crib alignment, template matching (tmatch.py) and the R9898 margins
- [x] retry: b23 re-read 23 Oct 2026: R9873 and R9898 written out as readings, open groups pooled with R9899 (new sibling) and R9660, f. 83r re-checked on the image; R9873 read, R9898 not; rerun 3 Oct 2026 with the pass-17 pooled values (R9873 92.8%, R9898 79.8%); rerun 21 Sept 2026 with the pass-15 key over R9660 (no change); rerun 2 Oct 2026 with the pass-16 key over f. 128: `rus` = dicho and `hay` = aunque fill the residue *de lo susodicho, aunque no*; `vo`, `per` and the m-re clause still open

## 23 Oct 2026 — verify sweep (reading audit v2): R9873 kept read
- Re-scored `r9873_reading.md` counting as holes every word that rests on a sense-only key value of the b23 log
  (sur/luc parte, tt plural s, reb dezi-, cer teni, lar miento, gom quatro, qu o, dis servido, gul si, nuf gente; 21
  words, located by their (a)-line contexts: `research/reading_audit/v2_sessa1524_sense.py`) and every word carrying
  a look-alike letter outside the attested 3 = i and the declared second values (ꝍ as i/j/d, Є/ε as i/y, 3 as j/l;
  11 words: dificultad x2, sobrino(s), Foyeta, aficionado, ynclinavan, aparejo, jamas, juzgan, aconsejado;
  `v2_sessa1524_look.py`).
- Scores: explicit holes 0.687 -> **0.632** (103/163, `v2_score.py`); b17 HOLES=1 0.715 -> 0.652; plain 0.38.
  Look-alike letters are about 95 of roughly 7,900 reading letters (1.2%), under the brief's 3%. The sentences hold
  outside f. 83r ll. 19-25 (already noted). Kept read, grade B, at the bar; the sense-only values stay flagged for a
  check against the triplicate's contemporary deciphering (Gayangos MS, CSP 636) or Kolosova's key if either is reached.

## Dudout corrections, 29 Oct 2026
- The period decipherment of the 14 Apr 1524 despatch (R9873) is BNE MSS/20214/52-1 ("Claro" A-D). Measured against it, our unbracketed words agree in 92.8% (1353/1458) and the [?] words in 34%. Value fixes: gul = quando (not si), hay = porque (not aunque; fum = otra), var probably como, gig = pudie-, fe = quisie-, pam = falta-, biz = yda (not venida), yer = alli (not Florencia), vol = dinero, xoc = ayuda, and others listed in his file. Same BNE volume holds four more Sessa cipher/clear pairs (52-4, -6, -10, -14) and two letters without a clear (52-7, 52-11). R9893 is a short letter of 24 Jul 1524, not 52-7; R9894 = CSP Spain ii no. 663 (29 Jul 1524), calendared with a contemporary deciphering. His extended key reads 52-7 at 94.0% of its ciphered part (under the bar).
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
