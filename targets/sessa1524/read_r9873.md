# R9873: Duke of Sessa to Charles V, Rome, 14 April 1524 (RAH Salazar A-31 ff. 79-86)

Status: read in part (2 Oct 2026; pass 17 3 Oct 2026). Transcription and reading line by line: [r9873_cipher.txt](r9873_cipher.txt).
Key: [key_working.md](key_working.md), passes 1-16. Measured with `python measure_read.py r9873_cipher.txt`.

## The document

DECODE R9873, 8 images (P1 = f. 86v address + f. 79r; P7 = ff. 79v-80r; P3 = 80v-81r; P5 = 81v-82r; P2 = 82v-83r;
P4 = 83v-84r; P8 = 84v-85r; P6 = 85v-86r). Holograph, clear with cipher runs on ff. 80v-84r and a postscript wholly in
cipher on f. 86r, dated in clear *A xiiij de Abril 1524*. ff. 79r-80r, 84v-85v are clear.

No decipherment is bound with it. Bergenroth (CSP Spain ii no. 637) calendars it as "deciphered by Don Manuel de
Goicoechea" (19th century) and "in all essential parts identical with" no. 636, the triplicate of the same despatch
(Gayangos MS, contemporary deciphering), and no. 638 is a court abstract of it with Gattinara's notes. Those three
abstracts ([csp/csp2_636_638.txt](csp/csp2_636_638.txt)) were used as a topic crib only: they paraphrase in English,
so no group value was taken from them without a second Spanish context.

## Measurement

| | tokens |
|---|---|
| cipher tokens in the (b) reading | 2,473 |
| read as sense, pass 16 | 2,165 (87.5%) |
| read as sense, pass 17 (pooled tentative values; key_working.md) | 2,295 of 2,474 (**92.8%**); strict, pass-17 values open: 87.8% |
| in open code groups | 256 |
| spelled letters that do not make a word (a sign value or a transcription slip) | 52 |
| tentative values counted as read | 69 groups |

`lm.best_language` on the assembled reading: es-modern -2.03, ca -2.35, pt -2.67.

## Content (cipher passages, in order)

- **f. 80v-81r.** The disbanding of the army in Navarre was already known in Rome; it is said there that the Emperor
  will hold cortes in Burgos and then in Aragon and Catalonia and, with the service granted, come to Italy, which
  does not please this court. The coming of the Archbishop of Capua (he left Blois on the 7th with the truce
  articles; the Pope had a copy given to Sessa) would settle *estas alteraciones*. Sessa proposed two things: that
  the archbishop go from France to England first, *para satisfazer a la autoridad del rey*, and that the King of
  France pay the King of England the pension he used to pay before the war, for the length of the truce. Starting
  from the Pope it would have been easier; it was not done, *no se si del poco aparejo que saben* there is for
  carrying the war on; they try to settle things with less difficult conditions. Couriers by sea and by land
  (Rodrigo de Mayorga); the coming, quality and nature of *el dicho duque*.
- **f. 81v.** The Emperor's estimation; the 4,000 ducats the Lodi men took at the Stradella, sent by the Pope *con
  nombre que yva al [kam] de su casa*.
- **f. 82r.** The Pope at first *muy bravo*, then cooled; his difficulty in contributing to the army; the Florentines
  have given nothing; he has told Sessa he will write this week to the Cardinal of Cortona that Ippolito, his nephew,
  is to assist at the government (of Florence); he has made good the said 4,000 ducats lost and is sending another
  4,000 this week; he is *en grandissimo conflicto*, temporising, not willing to disdain the enemies; nothing hoped
  for has come from England; those near him conform him in this irresolution and draw him away, *si no Micer
  Agostino Foyeta* (Foglietta); Sessa declares himself *mas aficionado* (to the Pope's service).
- **f. 82v.** Sessa has found a sum of ducats on exchange for the viceroy's need to keep the army (with the bishops
  of Salamanca and Ávila). England: the nuncio's letters of 26 March say the King takes no great heart to undertake
  the war and waits for the Emperor's resolution; the Cardinal (Wolsey) said lately that if the Pope got the King of
  France to send a person *debaxo de alguna onesta color*, the truce or peace would be heard, so as not to seem to
  incline to it himself, *que seria perder de reputacion*; the English will not contribute to the war in Italy *por
  ninguna via*; Madama (Margaret) writes the same.
- **f. 83r.** Advice: the Emperor's estimation, in peace or in war, must grow and be kept, more with friends than
  with enemies; the confederates; to treat with the Pope; marriages and the advancement of his nephews; the Emperor's
  coming to Italy, *sin hablarlo con Su Sd.*; *no fiandose V.Md. en la que hizo con la buena memoria del papa Leon*.
- **f. 83v.** If the Emperor came to Italy with great power ...; the pontificate; Alberto Pio, Count of Carpi *(que
  da al B-e-r-t-o del C-a-r-p-i-o)* and his credit with the Datary.
- **f. 86r (postscript).** The Pope and his ministers are grieved beyond measure at the disbanding; those who advised
  his irresolution think they have won; he will not declare himself in a defensive or offensive league, although they
  judge there was never a time so fit to break the wings of the French; if on that frontier and in Picardy something
  were done, the Pope would decide, though Sessa has always known him inclined to abase the French; what holds him
  back is fear; they wait for what the Archbishop of Capua brings.

The order and substance match CSP 636 point for point (cortes; Capua from Blois; the two proposals; the pension; ill
prepared for war; 4,000 ducats at Lodi; the nuncio's letters of 26 March; the English will not contribute; Madame
Margaret; friends and enemies). That agreement is the check on the reading.

## Key additions from this letter (pass 16)

`ruc`/`rus` = dicho (with `rad` = dicha), `hay` = aunque (tentative), `fed` = rey de Francia, `xir` = cardenal,
`lot` = nuncio, `pof` = exercito, `kuc` = liga, `tig` = contra, `cuq` = tengo, `yod`/`quf` = amigo/enemigo,
`gat` = esto (*estonces*), and the name *Micer Agostino Foyeta*. These close the f. 128 residue *de lo suso[rus]
[hay] no* = *de lo susodicho, aunque no*.

## Remaining gaps

- about 120 code groups open, most attested once (`xoc` x4; `qat`, `var` x3; `yeg`, `siz`, `som`, `col`, `yam`,
  `Jam`, `cox`, `lon`, `dis`, `leg`, `gig`, `caz`, `lez`, `gul` x2) - blocker: open-codes; a single context does not
  fix them and no sibling decipherment contains them (pass-14 template search; the R9898 marginal decipherments)
- 52 spelled-letter tokens that do not assemble into words (e.g. *a-t-a-r-a-r*, *b-r-i-l-i-a*, *p-u-e-r-e*) -
  blocker: open-codes; one sign value or a transcription slip in each; a token-tile check (tokens.py) would settle them
- the duplicate/triplicate with Goicoechea's reading is not imaged - blocker: needs-physical-access (RAH; the
  triplicate is in the Gayangos MS, CSP 636)
