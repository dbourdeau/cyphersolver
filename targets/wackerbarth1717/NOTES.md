# wackerbarth1717: Wackerbarth's cipher reports from Vienna, 1717 (Dresden, HStA 10026 Loc. 00713/01): Relation XXII to Augustus II, 14-16 June 1717, read in part; letter to Flemming of 24 April 1717 checked against its decipherment of the time

Status: read in part (Brice Dudout, 11 Nov 2026; Relation XXII: 716 cipher words, 575 certain, 66 probable, 66 restored, 9 unresolved = 641/716 = 89.5% read by sense, under the 95% rule; key rebuilt from the glosses of the time in the same volume, passed a held-out language test (z = 11.5) but FAILED its ground-truth test, and the condition for reading was decided after the measurement). Open: nomenclator numbers absent from the key, and nine homophones seen only in this letter.

> **Simultaneous work: Anne-Simone Rous.** Anne-Simone Rous (SBG Sachsen, Dresden) is working on this cipher correspondence
> of Wackerbarth and Flemming, 1700-1720 (about 6,500 folios; paper "The Keys of Diplomacy", University of Tartu repository,
> https://dspace.ut.ee/items/3b294689-0a66-4b84-80f3-f3d2ab78f45d). Her paper describes the 1717 system of this volume:
> numbers of one to three digits, mostly two, with 355 and 1000 in the nomenclator. It lists the 1717 letter as not
> deciphered. Our reading was made without contact with her and without her transcriptions. It should be cited **as
> simultaneous work alongside hers**, and she may well have gone further in the meantime.
>
> **The letter of 24 April 1717.** Her paper lists a letter of "24th July 1717" in this volume (ff. 29-33) as not deciphered.
> We think it is the letter of 24 April (ff. 29-32). In the volume as digitised, the decipherment sheet of the time at
> ff. 33-33v (views 0042-0043), headed "Le C.te de Wackerbarth du 24. d'avril 1717", renders its whole cipher, from the
> first words ("vues du Roy de Suede sur la Pologne") to the end. Our independent key agrees with it. We report this
> as a finding, and we may have misread her account.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (transcription, key, protocols, measurements,
reading and write-up). No human has yet read the reading against the scans.

## Document

Dresden, Sächsisches Hauptstaatsarchiv, 10026 Geheimes Kabinett, Loc. 00713/01: one volume (298 views) of August Christoph
von Wackerbarth's correspondence during his mission to Vienna in 1717. It holds letters to Jacob Heinrich von Flemming and
"Relations" to King Augustus II, in French with passages in cipher. Many cipher passages carry the decipherment of the time
between the lines. Some do not.
- **Relation XXII** (copy, "Sire"), Vienna 14-16 June 1717, ff. 71-80v (views 0089-0099). It mixes clear French and cipher.
  It has no decipherment of the time. **This is the target.**
- **Letter no. 15** to Flemming ("Monsieur"), Vienna 24 April 1717, ff. 29-32 (views 0037-0040), with its decipherment of
  the time on a separate sheet at ff. 33-33v (views 0042-0043). It is a check, not a new reading.

The scans are online at archiv.sachsen.de, marked "In Copyright". They were used for study only. **No image, crop or
derivative is included.** Credit: Sächsisches Staatsarchiv, Hauptstaatsarchiv Dresden.

## System and key (`key.tsv`, CC BY 4.0)

The volume uses two systems.
- **S1** (March-June 1717; also Relation XXII) is a homophonic substitution of French letters in one- and two-digit numbers
  (e = 2/10, i = 9, o = 16/22/33, t = 28/52 ...). Three-digit numbers are polygrams and a nomenclator (154 Votre Excellence,
  177 le Czar, 217 le roi d'Angleterre, 252 le roi de Prusse, 292 la Pologne, 355 premier). Numbers of four digits, 50xx and
  others, are nulls. Clear words are mixed in.
  S1 is **not** the Flemming key K0 (Loc. 00675/10, view 0080), nor its shifted variant, nor Wackerbarth's 1703 key.
- **S2** (Nov.-Dec. 1717) is K0. We checked five letters of S2 (views 0234, 0254, 0275, 0285, 0296), all glossed at the time:
  K0 decodes each one as glossed. This is a check only, with nothing new read. Codes outside K0 as transcribed: 174
  Weselowski, 217, 409 affaires, 578 rétablir. The parts of S2 without glosses (0246-0247, 0284, 0286) are not read.

Key c was built on the glossed S1 views only (0017, 0057-0062, 0071-0072, 0080-0081, 0086-0088). Cipher groups were aligned
on the glosses of the time (`frozen/scripts/align.py`), and manual entries were listed with their support
(`frozen/scripts/build_key_bc.py`). `key.tsv` has two sections:
- **section A** is key c exactly as frozen before the measurement (SHA-256 3322ae87...c49c). It is the only key used for any
  count.
- **section B** holds proposals from the reading, NOT used: corrections 20 = b and 78 = le; homophones seen at least three
  times (4 x, 38 h, 40 b, 73 z, 76 st, 79 la, 89 z, 92 t, 1000 et); nomenclator values proved by the sheet of 24 April
  (187 le roi de Suède, 314 Danzig, 198 Stanislas, 356 second, 364 "10e", 72 ch); and five single-case guesses.

## Validation (`validation.txt`; protocols in `frozen/`)

Every protocol was hashed before its run, and each run was made once. The record is mixed, and we give it in full:
1. **First protocol: both tests FAILED.** Test A (view 0040 against the sheet of the time) scored 0.204 against at most
   0.086 for 200 permuted keys, under the threshold. Test B (lexical cover) did not discriminate. We found the reason
   afterwards: the instrument, not the key. Test A was divided by a sheet four times longer than the portion tested.
2. **Second protocol.** The ground-truth test **A' FAILED**: the letter of 28 May 1717, glossed and held out, scored 0.339
   of gloss words exact against at most 0.128, margin 0.21 < 0.30. Its key lacked training data, and its threshold had not
   been calibrated. The held-out language test **B' PASSED**: view 0091, 353 groups never decoded, criterion L7 calibrated
   on the training set, z = 11.5, gap 0.74. The candidate criteria had been widened after the first calibration failed;
   this happened before the measurement and is declared. That protocol allowed a reading only if both tests passed.
3. **Third amendment, decided after the measurement (post hoc).** Brice Dudout chose to accept B' alone as the condition
   for reading Relation XXII, with Daniel's 95% rule as the final check. Under the rule of protocol 2 there would have been
   no reading. The amendment was hashed (7b0ee565...c151) before the remaining views were transcribed or any of 0092-0099
   was decoded.

## Reading (`reading.md`, `translation.md`)

**Relation XXII** has 716 cipher words: 575 certain, 66 probable, 66 restored, 9 unresolved. **641/716 = 89.5%: read in part.**
- The restored words each contain a number absent from key c. Nine such homophones recur in independent words (4 = x,
  18 times; 79 = la, 12 times). Counting them as probable would give about 97.9%. **That variant is NOT adopted**: it would
  be a second post hoc decision, and Brice Dudout has not taken it.
- **Reservations.** Three numbers are probably misread by the same slip, a "ч"-shaped 7 read as 4: 0097 G07 174 → 177 (le
  Czar), 0097 G15 4 → 7 (g), 0098 G03 184 → 187 (le roi de Suède). They are left as frozen and counted as they stand.
- **Content.** The chancellor Count Sinzendorf, by order of Charles VI, makes Wackerbarth an overture. The Emperor proposes a
  concert with the King of Poland and the King of England to restore the tranquillity of the Empire and an "entire peace" in
  the North on a "just balance", in keeping with the laws of the Empire. A triple alliance of the three is foreseen. The same
  overture was made the day before to Saint-Saphorin, George I's minister, who might act as a third party. The stay of the
  Russian troops in the Empire goes to the Diet of Ratisbon and to the directors of the Circles, to get them out and perhaps
  guarantee against their return. George I wants the same measures "regarding Poland", and no German province given back
  to the King of Sweden. Secrecy is strict: there was no referendary at the conference. Wackerbarth will take the waters at
  Baden while Sinzendorf is in Innsbruck.

**Letter of 24 April 1717** (`a24_reading.md`, `a24_translation.md`): key c reads 188 of 207 cipher words (90.8%), in sense
agreement with the decipherment sheet of the time. **This is not blind**: the sheet had been transcribed, for test A, before
the reading. The 7 unresolved words are nomenclator codes that the sheet resolves. The letter covers the King of Sweden's
designs on Poland (a landing near Danzig), the fear that Sweden might detach the Czar from the Northern League, and the
exchange of the county of Hanau, for which the Electors' consents must be won directly and not through the Emperor.

## Historical context (general knowledge; to be checked in the literature)

These points come from general historical knowledge, not from a search of the literature on this volume:
- Wackerbarth (1662-1734) was a Saxon cabinet minister and general.
- Flemming (1667-1728) was the first minister of Augustus II.
- Philipp Ludwig von Sinzendorf (1671-1742) was Hofkanzler of Charles VI.
- François-Louis de Pesme de Saint-Saphorin (1668-1737) was George I's minister in Vienna.
- The Russian troops of Peter I had been in Mecklenburg in 1716-17.
- The Hungarian campaign of 1717 is the Turkish war; Belgrade fell in August 1717.
**Hypothesis, not established:** the overture of June 1717 may be an early step towards the Treaty of Vienna of 5 January
1719 between Charles VI, George I (as Elector of Hanover) and Augustus II. We have not checked this against the
historiography.

## Prior art

- **Anne-Simone Rous**: simultaneous work on this corpus. See the box at the top. Her paper gives the 1717 system's structure
  and lists the 1717 letter as not deciphered.
- DECODE holds the Saxon Flemming key series (HStAD 10026 Loc. 03233/02; e.g. R5139, the key of Flemming with Wackerbarth,
  1700-1728, Lasry and Rous). We did not try those keys on S1. S2 is the Flemming key K0 of Loc. 00675/10. That key is
  related to our issue #357 on lead 1663 (Flemming to George I, Hannover).
- A quick web search (text only) found no edition of Wackerbarth's Relations of 1717. We have not searched printed
  collections (Sbornik RIO, Urkunden und Actenstücke, Saxon or Austrian state papers). An edition may exist that we do not
  know of.
- `catalogue.json` and `leads.json` are not touched. Neither has an entry for Loc. 00713/01.

## Remaining gaps

- 66 restored and 9 unresolved words of Relation XXII (numbers 4, 38, 40, 73, 76, 79, 89, 92, 1000 and single cases; codes 306, 4527, 289, 172, 169, 184, 1900205) - blocker: open-codes; these numbers are absent from key c (glossed nowhere in the training views); the values in key.tsv section B fit the sense but were found after the measurement and are not counted; codes 306, 172, 169 are persons or places named nowhere else in the volume
- the three probable misreadings 0097 G07, 0097 G15, 0098 G03 and the doubtful number 0089 M03 - blocker: illegible; to be re-read blind on the images (not done; no plate made)
- a ground-truth test of key c - blocker: no-key-material; no other glossed S1 letter of at least 300 groups is left in the volume (28 May and 24 April are used up); Rous's corpus may hold one

## Further work (outside this target's texts)

- Clear passages of Relation XXII not transcribed in full (views 0098-0099, marked "…"): clear text, not cipher; they would
  complete the translation.
- The parts of S2 without glosses (views 0246-0247, 0284, 0286) and the German enclosure A of 12 June without glosses
  (0073-0074): not transcribed yet; S2 should read with K0.

## Escalation

- [x] siblings: the volume (298 views) surveyed for cipher passages (PROTOCOLE §1 and Avenant 2 §1 list them); glossed S1 views used for the key (0017, 0057-0062, 0071-0072, 0075-0078 German enclosure excluded, 0080-0081, 0086-0088); S2 views 0234, 0254, 0275, 0285, 0296 checked with K0
- [x] clear-pages: the separate sheet at views 0042-0043 identified as the decipherment of the whole letter of 24 April (not only of its last passage, as the inventory note suggested); no clear copy of Relation XXII in the volume
- [x] known-keys: Flemming key K0 (Loc. 00675/10, view 0080) and its shifted variant, and Wackerbarth's 1703 key, compared: none is S1; K0 = S2. DECODE Loc. 03233/02 keys not tried on S1 (not done)
- [x] print: quick web search, no edition of the 1717 Relations found; Rous's paper read; printed state papers not searched
- [x] key-rebuild: key c rebuilt by alignment on all glossed S1 views; extension from the reading kept apart (section B) and not counted
- [x] retry: every unread number listed with the words it falls in (reading.md); misreadings noted, not corrected in the frozen transcription
