# Ordensbriefarchiv, Schoenberg ciphers of 1523 and 1524 (catalogue 553 and 556): existing contemporary decipherments

Status: read in part (existing: contemporary interlinear decipherments, and a contemporary Aufloesung for 1524; Brice Dudout, 25 Nov 2026). OBA 25970: 80.0% of words sure (88 sure, 8 probable, 14 unresolved, of 110 words); OBA 26859: read in full from its period Aufloesung.

**Nothing here is a new decipherment.** Both letters were deciphered at the time, on the sheets themselves. What this folder adds: a transcription of the period glosses of OBA 25970 (never printed), the way that letter is laid out (columns of three), the 1524 key alphabet, and the observation that the 1523 and 1524 keys differ.

Sources: Geheimes Staatsarchiv Preussischer Kulturbesitz (GStA PK), XX. HA OBA Nr. 25970 and Nr. 26859 (paid scan order by Brice Dudout, received 25 Nov 2026; the images are not included, please cite the shelfmarks). For OBA 25970: Erich Joachim, Die Politik des letzten Hochmeisters in Preussen Albrecht von Brandenburg, vol. III (1895), p. 65 n. 1 cites the letter ("in Chiffern. D. 87") and summarises its content (pp. 65-66) without printing it.

AI analysis was not raised with the archive; the project's method was not presented to it at the time.

## OBA 25970 (catalogue 553): Schoenberg to Grand Master Albrecht, Nuremberg, 27 Feb 1523
Fully in cipher, signed in clear. The finding aid notes no Aufloesung, but **every sign carries a contemporary interlinear gloss** (one letter per sign). The cipher is a simple substitution with homophones (two signs each for e, n, s, u, h), **written in columns**: in each band of three lines one reads the first sign of line 1, then of line 2, then of line 3, then the next column. The last band ends with the date in cipher, "Nurnbergk freytags nach invocavit im dreyundzway[ntzigsten]", which matches the regest (27 Feb 1523) and confirms the reading order.

Reading of the glosses (original spelling; {probable}, ‹unresolved›):

> Ich hab euch zwir geschriben, mein ankunft het mich versehen, es wern euch diselben brif ankomen. Clingenbeck sagt mir aber, es sey nit, ich mus zu euch, vnd hab Franckreych zugesagt uber virzehen tag, so ich bey euch kom, nit bey euch zu verharren. ‹gerwegen› {schreybt} mir, wu ich bey euch komen sol. Mein ‹suersehen› ‹sea› ‹wer› ‹aahi› zu Nurnberg kam, ‹besten› {do} ich ‹heui› {antwort} und beschaydt warten {wil} {ich}, ‹go?ye› mein lang aussen bleyben so euch darzu {geraychen}, das ir euch ‹v?› ainmal armuts zu {erweren} habt, und ‹wer?o?n› ‹de?› ab man wenig an ‹dic?a?ht›, das ich ‹dennest› nit tod gewest. ‹datis› Nurnbergk freytags nach invocavit im {dreyundzwayntzigsten}.

English (sure parts): "I have written to you twice ... these same letters will have reached you. But Klingenbeck tells me it is not so, that I must come to you; and I have promised France, within fourteen days, when I come to you, not to stay with you. ... writes to me where I should come to you. ... [I] came to Nuremberg ... I will wait for your answer and decision ... that my long absence may serve you to that end, that you may for once defend yourself against poverty ... that I was not dead. Nuremberg, Friday after Invocavit, [15]23."

Count (Daniel's rule, whole letter): 88 sure, 8 probable, 0 restored, 14 unresolved, of 110 words: 80.0% sure (87.3% with the probable words). Corrected in integration review of PR #987, 26 Nov 2026: the words were recounted (110, not 112), and "erweren" is now marked probable, since the gloss gives "erwern" and one e is supplied. Read in part. The short tail in the right margin (end of the year) is not transcribed sign by sign.

**Key check, failed.** One pre-registered test, run once: a key tallied from band 1 (86 cells) predicted the glosses of bands 2-5 (314 held-out cells) at **0.707**, against at best 0.201 for 200 shuffled keys. That **misses the 0.85 bar**. 13% of held-out signs never occur in band 1, and some of our glyph labels merge neighbouring shapes. So `key_oba25970.json` is a **working table, not a validated key**. The reading above rests on the period glosses, not on this table.

## OBA 26859 (catalogue 556, already left out of the unread group): Schoenberg to Daniel Gundelfinger at Lyon, 22 Apr 1524
The letter has interlinear glosses, a separate contemporary **Aufloesung** slip, and the **key alphabet** slip (`key_oba26859.json`). Aufloesung (original spelling):

> der reichstag hat ein end vnd ist anfrucht zergangen vnd ist fvr kein reichstag angesehen gross vfrvr ist hiaussen waiß ‹and› wohin der bvnd wurd dis somer den adel wider vber zihen vnd glaub vber {di schlicken}

English: "The Reichstag has ended and broken up without fruit, and it is not regarded as a Reichstag. There is great unrest out here; [no one] knows where the League will go; it will march against the nobility again this summer, and I believe [it will fall] on the Schlicks."
The slip gives one sign per letter (two for i) and a sign "2" for "und". On the first cipher line it agrees with the period clear text on all 20 signs checked.

## The 1523 and 1524 keys differ
The keys are not the same: T = h in 1523 but T = n in 1524, and most signs differ. The 1524 slip therefore does not open OBA 25970. It probably does not open the other 1523 letters either. It should, though, fit the remaining 1524 letters to Gundelfinger (OBA 26695, 26815, 26824, 26969; not seen).

## Suggestions for the catalogue (Daniel decides)
- 553: OBA 25970 is deciphered on the sheet. It could leave the "no Aufloesung noted" group, or be listed as existing / read in part.
- 556: the 1524 key alphabet is now in hand for 26695, 26815, 26824 and 26969.

## Files
- `oba25970_cells.tsv`: one row per sign, bands 1-5 (band, column, row 1-3 within the band, glyph label, period gloss). This is the frozen transcription used for the test.
- `oba25970_band6_glosses.txt`: glosses of band 6 (lines 16-18), column by column.
- `key_oba25970.json`: working table tallied from the glosses (not validated).
- `key_oba26859.json`: the 1524 key alphabet from slip 2.
