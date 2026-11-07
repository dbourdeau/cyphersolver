# Re-reading log, R289 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.145). Available: DECODE's transcription
(`decode/R289.txt`, four pages, images 2498-2501), the batch decode `reread_b01/R289_dec.txt` and its alignment
`reread_b01/R289_align.txt`.

## What was done

1. **Despatch identified**: Kiewning 1897, Nr. 156 (heading "156. Pallotto an Barberini, 1629 August 10, dechiffr. 29.
   August"; the running heads read "Nr. 166"), Nunz. di Germania 119 fol. 22-27, edition lines ~23369-23495. R289 is
   its first part; it ends "In questa conformità venne da me il giorno seguente", and R290 begins "‹i›l Questembergh, al
   quale ...". The sheet's head reads "Di Vienna 10 di Agosto 1629"; no register letter is written as on R288 ("B 24"),
   but a large "C" stands under the address.
2. **Print**: every chunk of the decode aligns with the print at 0.07-0.6 cost per letter, except run 16.0 (0.85),
   where the OCR interleaves two footnotes into the text ("sequitar etc. e non adsequitur etc."). The reading is the
   print with OCR corrected (daN. S re = da N. S.re, 8. M u / S. M a = S. M.tà, 8. B n0 = S. B.ne, inaggiori = maggiori,
   zeloSO = zelo, caleri-ano = caleriano, Christ 100 = Christianissimo, 21 giorno = 21 giorni, sequitar = sequitur,
   il tarc ö dir = il far o dir, etc.).
3. **Clear words** checked on the scans: "forse" (after the cipher group 734), "haver sentito che" (with "et" = 79
   written above), "era", "ma più tosto, che", "maggiorm.te", "ma al fine restò", "far ogni magg.re e più"; and the
   gloss "In conformità della risposta" over the first cipher line. All agree with the print; DECODE's clear-text
   readings ("frisi", "hav?er senior il?e", "fareo *ni mag?f?") are replaced by these.
4. **Figures against print**, checked with `reread_b01_show.py` where the decode differed:
   * "si aggiungeva quello di veder" — figures 99 50 06 29 99 90 1 60 20 (aggiungeva); print "si aggiunga". Reading
     follows the figures.
   * "inviarlo ancora al re di Francia" — 733 = ancora; print "anche". Reading follows the figures.
   * "la somma riverenza et osservanza che porta S. M.tà alla sede apostolica" — 22 07 36 25 00 8 670 = porta S. M.tà;
     print "che portava". Reading follows the figures.
   * "dependeva da N. S.re" — the decoder's "da pero" is 67 [577 0]: 577 = N. S. followed by a null read as 0; print kept.
   * "per publico bene della christianità" — the figures here are garbled (33 06 25 09 66 02 46 65 32 07 73 50, "dutelarsi
     co la i"); print kept, figures not reconciled.
   * "il far o dir cosa" — figures 74 37 69 36 ("le gli dir"); print kept.
   * "sequitur" — figures 64 36 50 202 79 (the decoder's {consiglio}); print kept.

## Holes

None marked: every word is carried by the print (and, where they differ, by the figures as listed above). The one
stretch where the figures do not support the print's words ("per publico bene") is noted above.

## Group values (proposals, not entered in extra_groups.json)

* 734 = ancorché — "[734] forse stimolato da altri" (Kiewning "ancorche forse"); alphabetically between 733 ancora and
  735 bene.
* 397 = glie (glie ne); 607 = (me)zzo; 904 = "i e"?; 449 = Don Gonzalo; 566 = principe Savelli (cf. 596 in R287 for the
  same name: one of the two is a misreading); 406 = esercito; 930 = soldate(sca); 357 = poiché per; 920 = (quell)a santa
  sede; 992 = Questembergh (992 + 907 + 955 cover "Questembergh" in "il qu[992][907]alchiodi[955]"); 574 = si quello
  (one alignment each, from `R289_align.txt`; not checked further).
* 290 = Cardinal di Richelieu here ("richiamatovi il [290]", Kiewning "il Cardinal di Richelieu"), which supports the
  same reading in R287 ("al re e [290]").
* 220 aligns with three different things ("pu", "iport", "Christ") — not a group; a misread or mis-segmented pair.

## Result

Read: clean-sentence share 0.145 -> 0.847 (`docs/_check_reading.py --file`, 111 sentences, 94 clean; the unclean ones
are long sentences with archaic forms, no holes).
