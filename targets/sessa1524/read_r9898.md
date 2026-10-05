# R9898: Duke of Sessa to Charles V, Rome, 24 February 1525 (RAH Salazar A-34 ff. 150-156)

Status: read in part (2 Oct 2026; pass 17 3 Oct 2026). Transcription and reading line by line: [r9898_cipher.txt](r9898_cipher.txt).
Key: [key_working.md](key_working.md), passes 1-16. Measured with `python measure_read.py r9898_cipher.txt`.

## The document

DECODE R9898, 7 images (P1 = f. 150r; P2 = 150v-151r; P5 = 151v-152r; P3 = 152v-153r; P4 = 153v-154r;
P6 = 154v-155r; P7 = 155v-156r). A long despatch in a secretary's cursive hand, clear and cipher interleaved, dated
in clear *De Roma a xxiiij de hebrero 1525*, the day of Pavia and so written before the news (the next letter, CSP
Spain iii.1 no. 23 of 26 Feb, congratulates the Emperor). It is not calendared in CSP iii.1 (checked on BHO by
Salazar A-34 folio). f. 155r is clear; heavy bleed-through on 150v-151r and 155v.

**Correction to pass 12 (NOTES):** the letter does carry a decipherment of the time, in part. Six cipher runs have a
marginal decipherment in a second hand: f. 150r (the opening reply), f. 152r (*que aqui ninguna cosa nos comunican
...*), f. 153v (*o de color del papa*), f. 154r (*se de buena parte que el datario ha tentado de reduzir al duque a
franceses ...*), f. 154v (three runs: *para que a la ...ra se pierda ... y cierto si mi obligacion no me forçara*;
*y viendo la malissima providencia que ha avido, dueleme grandemente hallarme ...*; *que tenemos toda Italia ...*)
and f. 156r (*no le plaze mucho al papa, aunque no quiere confessar, es en su menosprecio y que franceses le ayan
tomado en su protecion*). They were used as cribs (key_working.md pass 16); the rest of the cipher has none.

## Measurement

| | tokens |
|---|---|
| cipher tokens in the (b) reading | 3,059 |
| read as sense, pass 16 | 2,361 (77.2%) |
| read as sense, pass 17 (pooled tentative values) | 2,441 (**79.8%**); strict 77.9% |
| in open code groups | 300 |
| spelled letters that do not make a word | 398 |
| tentative values counted as read | 98 groups |

`lm.best_language` on the assembled reading: es-modern -2.28, ca -2.57, pt -2.86. The 398 letters without sense sit
mostly in the bleed-through pages (150v, 151r, 155v), where the cursive *r*/*u*/*n* signs (`ꝍ`, `Ɉ`, `b`) are not
told apart reliably; the reading there is a sign-level transcription, not a reading.

## Content (cipher passages, in order)

- **f. 150r.** Reply to the Emperor's letters of 15 Nov and 15 Dec: the Pope did not answer; he wants what was sent
  not seen there; it must not be let known to the Swiss what has been sent from the Emperor; from past works one can
  judge the government from here on (margin).
- **f. 150v-151r.** The Pope's arrangement with the King of France and the French, a copy of which he says he sent
  the Emperor; his accustomed neutrality; the Datary's French partisanship, *que abiertamente se conoce*; the
  French *han yntentado con el embaxador de Inglaterra* ...; the Pope told him he would assure him of the pension
  due during the truce if the Emperor or the King of France did not agree; *el dicho [embaxador] ha respondido muy
  bien*; the invasion of the Kingdom of Naples; *su fin principal ha consistido e consiste* (clear) in a run that is
  open (`hem`, `lin`); the dicha tregua o paz; the Datary and the French; *la experiencia le ha mostrado*; the
  Emperor's agents.
- **f. 151v-152r.** The French *han efetado y efetan*; the Emperor may be sure of the dissimulation used; they
  promise *los mismos partidos*; the viceroy; the ministers outside the Pope's circle; *aqui ninguna cosa nos
  comunican, sabiendo que las entendemos y conocemos; por conjeturas sabemos lo que ocurre* (margin).
- **f. 152v-153r.** The Pope's attitude to Albany's coming and the invasion of Naples; *lo de Inglaterra se va
  calentando*; the Datary and the money that did not reach the camp, *la grandissima necesidad que en el canpo se
  pudiese*; the Venetians and the Pope blame each other; the Archbishop of Capua at Piacenza, *con color de la
  platica de la paz*, to keep him away; *Micer Agostino Foyeta*; the Duke of Albany's reception (clear) and *su
  venida a la ynvasion del Reyno*; the King of France.
- **f. 153v-154r.** No provision made in the Kingdom (of Naples); the Duke of Albany's men are badly paid, horse
  short; *se de buena parte que el datario ha tentado de reduzir al duque a franceses* (margin) with money and
  promises from the King of France; the Datary approves; *Micer Agostino Foyeta*.
- **f. 154v.** Sessa ordered to San Germano by the viceroy *para que ... se pierda, que no para defensar lo; y
  cierto si mi obligacion no me forçara* ...; *y viendo la malissima providencia que ha avido, dueleme grandemente
  hallarme a lo que por razon y no por caso temo que suceda*; *que tenemos toda Italia ... y no partira* (margins).
- **f. 155v-156r.** Pavia expects relief; forcing the French in their strong position would be a manifest
  disadvantage; what results in Lombardy; *el datario*; the Emperor must either content himself with *la perdida*
  or ...; postscript (clear): the Duke of Ferrara has lent the King of France another 50,000 ducats and munitions,
  and (cipher, margin) *no le plaze mucho al papa, aunque no quiere confessar, es en su menosprecio y que franceses
  le ayan tomado en su protecion*.

## Key additions from this letter (pass 16)

From the margins: `v em` = cierto, `li` = mi, `Jac` = obliga-, `le` = me, `net` = halla (not *toma*), `nuh` =
grande, `kch` = mal (confirmed), `cap` = tem-, `lec` = -mos, `dug` = sabi-, `doh` = sabe-, `yol` = aqui, `sud` =
datario, `pand`/`Jur` = buena/parte, `kun` = duque, `nah` = govierno (tentative). From context: `ruc` = dicho,
`ges` = embaxador, `cex` = trata-, `lin` = necesidad, `tig` = contra (tentative values in key_working.md).

## Remaining gaps

- about 140 code groups open (`cas` x6; `bup`, `sur`, `pam`, `kal` x4-5; `pol`, `tuf`, `cor`, `var`, `Jir` x3; the
  rest once or twice) - blocker: open-codes; single contexts, absent from every deciphered sibling and from the six
  marginal decipherments
- 398 spelled-letter tokens without sense, mostly on ff. 150v-151r and 155v - blocker: illegible; bleed-through on
  the DECODE images makes the cursive r/u/n signs ambiguous; a better image (RAH) is needed
- the opening run on f. 150r is half lost under the margin decipherment and the gutter - blocker: illegible
