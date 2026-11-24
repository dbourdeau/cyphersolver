# chateauneuf1691 — Châteauneuf (Castagnères) at Constantinople/Adrianople, 1691-1694: the five "non déchiffré" pieces of AE/B/I/381 (catalogue 539)

Source: Archives nationales, AE/B/I/381 (Correspondance consulaire, Constantinople, 1691-1694), reproduction ordered by Brice Dudout (51 JPEG, received 20 Nov 2026). Images are not distributed; cite « Archives nationales, AE/B/I/381 ».

## The code
One numeric nomenclator (groups 3-368) for all five pieces, 1691 to 1694, for letters to the King and to Pontchartrain alike: low numbers single letters with homophones (a = 9, 16; s = 22, 45, 47, 49; n = 20, 38; e = 29, 36; t = 27, 50 ...), middle numbers syllables (104 re, 107 ce, 138 de, 333 que, 342 oit), high numbers words and names (275 vizir, 284 seigneur, 285 venitiens, 301 majesté, 325 vaisseau, 328 empire, 332 ottoman, 345 Venise, 362 occasion). 365-368 and 355 behave as nulls (context only). 355 is a null in `key.tsv` and in `decryption.txt` (shown as ‹355›). KEY_v1 and KEY_v2 (`prereg/`, frozen by hash) still carry 355 = "a", which the EM alignment took from its one occurrence in f. 376 (0377 L1, after "Benincasa"); in the five pieces "a" gives "re-a-lution" (0154 R3) and nothing sensible at 0154 R4, 0154 R12, 0232 S1 and 0242 R1, so the reading treats it as a null and counts no word on it. The frozen measure used "a". Part of the letter range runs in alphabetical steps of 5: a 16, b 21, c 26, d 31, e 36, f 41, g 46, i 56; and a 9, b 14, c 19, d 24, e 29 (observation, not used to fix any value). It is not the Louis XIV -> Castagnères code of 1690 (Tomokiyo, Cryptiana louisxiv2; "le" = 195 there, 91 here).

## Key source and measure (pre-registered, prereg/)
- Key source: the period interlinear decipherment of the letter of 17 Jan 1694 (f. 376, 119 cipher lines, ~1,546 groups; key_source/gloss_376.txt). Alignment of number runs with gloss letters by EM over monotone segmentations (tools/em.py), then hand curation -> KEY_v1 (169 codes).
- PREREG (SHA-256 in prereg/SHA256SUMS_prereg.txt) written before any key, by its own heading (the hash list records it together with KEY_v1 and the transcriptions under one time, 2026-11-20 13:32, so the order rests on the contributor's record): held-out portion = all of f. 452 (21 Sep 1694, 457 groups, glossed); one measure; character agreement after normalisation; 200 controls by permuting the key values; pass iff >= 0.85 AND >= best control + 0.30.
- Result (prereg/MEASURE_452.txt): **0.830 vs best control 0.102 — FAIL at the pre-registered bar** (margin over controls met, absolute bar missed by 0.02). The decode is visibly correct French; the shortfall comes from codes left out of KEY_v1, among them three common values attested in the f. 376 gloss that were omitted by oversight during curation (81 la, 50 t, 70 guerre). f. 452 is burnt; no other glossed portion was ordered, so no second measure is possible.
- KEY_v2 (post-measure, not validated): KEY_v1 + 14 values added after the measure: 6 from the f. 376 gloss that KEY_v1 left out (81 la, 50 t, 70 guerre, 233, 217, 353) and 8 read from the f. 452 period decipherment (145 turc, 209 françois, 270 iu, 276 bo, 318 estat, 3 il, 109, 262) (`prereg/KEY_v2_additions_sources.json`). Values fixed from context only (11 il, 43 o, 103 ont, nulls) are listed in key.tsv and counted as holes.

## Transcription of the undeciphered pieces
Two independent blind passes (P1 forward, P2 reverse order, AI agents without key) and a blind arbiter on the 12 disagreements/gutter places (blind/). 597 groups; 13 diff blocks between passes, settled by the arbiter; 4 groups lost in the binding.

## Result
Read in part. 238 of 271 cipher words sure (0.878): f. 152 134/150, f. 155 25/30, f. 232 31/35, f. 239 13/18, f. 433 35/38 (reading.md; 239 of 271 and 26/30 until the key replay of 24 Nov 2026, see "Key replay"; 240 of 272 and 135/151 before that, until 24 Nov 2026, when the "a" that sentence 4 of f. 152 counted on the null 355 at 0154 R4 was taken out). No period decipherment of these five pieces exists in the volume (inventory: "la partie chiffrée n'est pas déchiffrée").

## Historical gist
1691: Châteauneuf proposes to Louis XIV that the Venetians (at war with the Porte) lose the French protection under which some 200 of them still traded at Constantinople "by tolerance", and that their Levant trade pass instead on French ships with passports from La Haye (ambassador at Venice) or himself, with penalties for French merchants lending their names; the King answers that no consent may give up rights stipulated by the capitulations. 1692: Fabre is to keep Venetian ships out of Ottoman ports under any (French, English, Dutch) flag without Châteauneuf appearing to have consented; the Venetian siege of La Canée had stirred the Turks against Venice. 1694: Châteauneuf avoided pressing the Vizier while the enemies spread the rumour of an imminent French peace.

## Remaining gaps
- Code groups 305, 280, 177, 69, 146, 152, 61, 64, 33, 59, 196, 108, 232, 166 have no attested value, and the 57 of 0154 R3 has one (st) that gives no sense there - blocker: needs-physical-access; each occurs once or twice in these five pieces, and the two glossed letters we hold carry none of them except 61 (once in f. 452, 0453 L2, where the decipherment of the time writes nothing for it). A value can only be attested by more glossed text in this code (the 16 further glossed pieces of the volume, not reproduced) or by clear copies of these letters, if they survive elsewhere (see Escalation); none was found online. Probable values from the layout of the table are in "Retry of 24 Nov 2026"; they are not counted (blocker was open-codes until 24 Nov 2026)
- Four groups lost in the binding (0233 L, 0243 L, 0439 L) - blocker: illegible; the gutters are cut in the reproduction, a flat re-shoot is needed
- Validation of KEY_v2 - blocker: needs-physical-access; the 16 other glossed pieces of AE/B/I/381 (f. 131, 222, 261, 289, 317, 325, 330, 339, 398, 400, 409, 422, 425, 448, 470, 472) are not ordered, and f. 452 is spent; they would give a fresh held-out portion
- 355 = null rather than "a" - blocker: needs-physical-access; one occurrence in the glossed letter (f. 376), none in f. 452; it can only be tested on another glossed piece of the volume, and none is reproduced (blocker was open-codes until 24 Nov 2026)

## Retry of 24 Nov 2026
Made at the write-up by an AI agent for the maintainers, from the files of this folder. No image was opened.

Layout of the table. Set out in ten columns by the last digit, the values of key.tsv run in alphabetical order down
each column, and each column takes up where the one before stops. For each letter the syllables come first, in the
order a e i o u, then the words; the words of one letter are not in strict order (126 anglois, 156 Angleterre,
226 anglois; 275 vizir, 285 vénitiens, 325 vaisseau).
- ...1: 81 la, 91 le, 101 li, 111 lo, 121 lu; 141 luy, 161 leur; 201 ma to 231 mo; 281 monsieur, 301 majesté, 311 ministre, 321 mesme, 331 manière, 341 moy
- ...2: 102 ment; 162 na to 202 nu; 222 (né)cessaire, 262 negoc-; 332 ottoman, 342 oit, 352 oient, 362 occasion
- ...3: 93 ou, 113 on (and 103 ont, from context); 133 pa to 173 pu; 203 porte, 213 plus, 223 pour, 253 pas, 273 point, 313 par; 323 qua, 333 que, 343 qui, 353 quo, 363 qu
- ...4: 94 ra to 134 ru; 144 roy, 174 république, 194 résolution; 234 sa to 274 su; 284 seigneur, 344 sujet, 364 sçavoir
- ...5: 75 ta to 115 tu; 145 turc, 175 tout, 215 traitté; 225 va to 255 vo; 275 vizir, 285 vénitiens, 325 vaisseau, 335 vou(s), 345 Venise; then the nulls 355 and 365
- ...6: 126 anglois, 156 Angleterre, 186 aussy, 226 anglois; 246 ba to 286 bu; 336 beaucoup; then the null 366
- ...7: 67 bien; 97 ca to 137 cu; 197 Constantinople, 217 capitulations, 297 car, 317 commerce, 337 compte; then the null 367
- ...8: 128 da to 168 du; 208 des; 278 entre, 288 eux, 298 est, 308 elle, 318 estat, 328 empire, 348 envoy-; then the null 368
- ...9: 99 fa to 139 fu; 149 France, 189 faire, 209 françois, 249 favor-; 279 ge, 289 gi
- ...0: 70 guerre, 80 grand; 100 ha, 110 (c)he; 150 Hollande, 170 hollandois; 200 ay; 230 ja to 270 ju
Two values do not fit their place: 233 "ue" (KEY_v2, from the f. 376 gloss) stands among the P words, and 200 "ay"
between the H and the J words (at 0382 R15 the gloss "que je luy proposay pour" has no letter left for it). 110 is
"he" rather than "che" (Carat-c-he, tru-c-he-ment, a-c-he-ter) and 222 the whole word "nécessaire". The numbers
below 59 are single letters and endings in runs of five (as noted under "The code").

The open groups against the layout and their sentences. None of these values is attested by a glossed line, so
every one stays a hole and the count does not change.
- 305 (0154 L1): among the V words (285 vénitiens, 325 vaisseau); "si ‹305› Majesté" - probable: vostre
- 280 (0154 L1): the cell after 270 ju; "si Vostre Majesté ‹280› que" - probable: juge
- 146 (0154 R7): among the A words (126 anglois, 156 Angleterre); "sous la protection des trois ‹146›s" - probable: ambassadeur(s), for France, England and Holland, rather than "crowns" or "nations"
- 166 (0439 L3, underlined by the scribe): among the A words; "conclure sa paix avec les ‹166›s" - alliés or allemands; "Impériaux" does not fit the column
- 196 (0156 L3): among the A words (186 aussy); "des ‹196›s qui ont esté stipulés par les capitulations" - avantages or articles; "droits" does not fit the column
- 108 (0233 L5): above 128 da, where the C words would run on after 337 compte; "animé les Turcs ‹108› les Vénitiens" - probable: contre
- 69 (0154 L4): above 99 fa, where the E words would run on after 348 envoy-; "{on peut faire} ‹69›-d-re à la République que" - probable: enten(dre), "faire entendre à la République que", rather than "répondre"
- 177 (0154 L1): among the C words; the sentence wants "ne" ("ne doivent plus jouir"), which is 172. Both blind passes read 177. A slip of the clerk or a 2 taken for a 7; not settled without the image
- 57 at 0154 R3: its value st gives no sense before "que si cette résolution"; "et" (52 or 54) would. P1 saw the group overwritten and perhaps struck through, P2 read 51?, the arbiter 57 (probable). Not settled
- 33 and 59: twice each, always as a pair around one or two groups (33 po 59 at 0155 L3; 33 232 qu 59 at 0242 R1), and nowhere in the two glossed letters (about 2,000 groups). Both sentences are complete without what stands between them: "et imposer {une peine considérable ...}" and "{du dessein de} ne plus recevoir les vaisseaux vénitiens". Hypothesis: a pair of signs that cancels what is written between them. 232 (among the N words) is then inside a cancelled run
- 61: at 0154 R11 it follows 152 at the head of the run ("{qu'à l'exception} 152 61 du seul juif Conigliani"). In the glossed letter of 21 Sep 1694 (0453 L2) the numbers are 138 234 61 81 234 19 104 36 ... and the decipherment of the time reads "de la sacrée personne": it writes nothing for 234 (sa) nor for 61, and the transcriber noted a double dot between them. Hypothesis: 61 cancels the group before it (the clerk wrote "de sa", cancelled "sa" and went on "la sacrée personne"). The Grand Chiffre of 1691 has such a group, "Annule le groupe précédent" (Bazeries's table, `targets/feuquieres/grand_chiffre_1691.tsv`, group 27). 152 is then a cancelled group, and the passage reads "qu'à l'exception du seul juif Conigliani"
- 64 (0154 R11): once, after "na" at the end of the same run ("Conigliani na 64 {je n'en ay pas vu un seul}"). Perhaps a second sign of the same kind, or the end of a word na-; open
If the cancelling signs were accepted, three words would leave f. 152 sentence 8, two sentence 11 and three f. 239
(238 of 263, 0.905; f. 239 13 of 15). They are not: a sign fixed from the sentence alone is a context-only value.
The name in sentence 8: Israel Conegliano, a Jewish physician, acted for Venice at Constantinople in these years
(D. Kaufmann, Dr. Israel Conegliano, Budapest 1895, which also tells the affair of the Venetians under French
protection from the Venetian side; seen in the archive.org text, not checked further).

## Escalation
- [x] siblings: the five pieces compared with each other; one nomenclator found for 1691 to 1694. 24 Nov 2026: the keys of the same state and decade held in the repository compared by number: Vergier to Pontchartrain, 1696 (`targets/vergier1696`, George Lasry's key: le 196, que 259, de 133), the Grand Chiffre of 1691 (`targets/feuquieres`, Bazeries: 91 Mon, 333 Di) and the 1690 code below; here le 91, que 333, de 138. None is this table. The catalogue entry also pointed to "twelve Châteauneuf despatches elsewhere" (BL Add MS 61574, DECODE R8052 to R8089, former catalogue 294): by the DECODE list (38 records) those are of 1717-18, most from The Hague, more than twenty years later and from another post; no transcription of them is in the repository and they were not compared
- [x] clear-pages: clear passages of the pieces and the inventory (FRAN_IR_003977) read; no decipherment of these pieces. 24 Nov 2026: clear copies looked for outside the volume. Hurmuzaki (1886) prints Châteauneuf's despatches to the King from the archives of the French foreign ministry and cites its "Vol. 23" for those of 1691 and "Vol. 24" for December 1692 (presumably the Turquie series of the Correspondance politique; not checked), so the originals of the despatches and the minutes of the King's replies may be there; and the CADN répertoire of the Constantinople embassy, série A, lists a volume at Nantes, 166PO/A/6, "Marquis de Chateauneuf et marquis de Ferriol, 1689-1709, Correspondance avec la cour" (microfilm 2 Mi 2217). Neither was found online, and neither was seen; whether they hold these five letters is not known
- [x] known-keys: the period decipherments of f. 376 and f. 452 of the same volume used as key source; the 1690 code (Tomokiyo) compared and is a different code. 24 Nov 2026: the lead that the catalogue vetting named as the first thing to check (leads.json 1177, Chantilly Ms 1905, letters of the King and ministers to the duc de Vendôme, 1697-98, "avec une table de déchiffrement") is another correspondence, is not online and was not seen
- [x] print: catalogue 539 vetting (2 Nov 2026) found no edition or decipherment of these pieces. 24 Nov 2026: archive.org full text searched for phrases of the clear passages and for the five letters by date, and three web searches. Hurmuzaki, Documente, Supl. I vol. 1 prints extracts of Châteauneuf's despatches of 1691-92 on Moldavia, Wallachia, Transylvania and Poland (31 Mar, 16 Apr and 21 May 1691, 26 Nov and 21 Dec 1692 among them), none of the passages in cipher here; Kaufmann, Dr. Israel Conegliano (1895) tells the affair from the Venetian side and prints no French letter. No print of the five pieces found
- [x] key-rebuild: KEY_v1 frozen, one measure, KEY_v2 built afterwards (post-measure, not validated). 24 Nov 2026: the layout of the table worked out (ten columns, alphabetical down each) and used to bracket the open groups
- [x] retry: 24 Nov 2026, every open group run again against the layout of the table and its sentence ("Retry of 24 Nov 2026"): seven get a probable word (two of them a choice of two), 177 and the 57 of 0154 R3 look like slips, 33, 59, 61 and perhaps 64 read as cancelling signs, which leaves 152 and 232 as cancelled groups. None is attested, so all stay holes and the retry changes no count. A second measure of the key still waits on a fresh glossed portion

## Key replay
`replay.py` (24 Nov 2026, AI agent for the maintainers) applies key.tsv to transcription.txt and compares the result
with reading.md (`python docs/_replay.py chateauneuf1691`; `replay.tsv`). The first run showed 18 words printed
otherwise than the key gives them, with no mark:
- four words that the reading already counts as holes in {braces} (résolution, désister, j'eusse, recevoir);
- six printed in a regular spelling where the clerk's own is a word as it stands: passeports (passepors), presteroient
  (preteroient), parust (parut), faites (faittes), seuls (seul), d'empescher (d'empecher). reading.md now prints the
  clerk's spelling; the count is unchanged;
- devez for de-ue-47: 47 and 49 are s in key.tsv, but the decipherer of the time writes z for them in trouuez,
  obligez, reputez, jugez, donnerez (47) and auez (49), and s in aupres (47). Declared as s or z; key.tsv not changed;
- d'empescher again: 110 is "che" in key.tsv, "he" in the three glossed words that hold it (Carat-c-he,
  tru-c-he-ment, a-c-he-ter). Compared as he; key.tsv not changed;
- three word codes printed as the word they stand for: 145 turc as Turcs (the decipherer writes "des Turcs que des"
  for the bare code, 0455 L6), 335 vou as vous (bare code glossed vous at 0384 L11 and 0460 L3), and 174 republic as
  République. The last is not attested in that form: the glossed letters have the code once, in "Republicains"
  (0378 L7). The two République of f. 152 are still counted as sure; that is a judgment, stated on the page;
- consentement in f. 155: the cipher has 127 28 244 20 85 102, co-m-se-n-te-ment, with 28 (m, as in no-m-b-re and
  te-m-s) where 38 (n) is wanted; the letter of 21 Oct 1692 has 127 38 for the same word. A letter corrected, so the
  word is now {consentement} and a hole: f. 155 25 of 30, the five pieces 238 of 271 (0.878).
After these changes the replay reproduces the reading with no unmarked difference: of the 262 words it divides the
cipher passages into, 239 are the key's output letter for letter, one differs by i/y (troys) and one by s/z (devez),
15 are marked and 6 are left unread (five on a number with no value, one on the 57, whose key value is st); beside
them stand 10 bare numbers, nine with no value and the null 355 (replay.tsv). Those 241 are the 238 counted
here plus "ici" and "y" (holes for a doubtful figure and a stray letter) and the "na" of the unresolved na-64.

## Transcription doubts
The image checks are the contributor's: two blind passes (P1, P2) and a blind arbiter working from enlarged crops
(`blind/`, 20 Nov 2026). No image was opened at the write-up; the decode checks are of 24 Nov 2026.
- 117? (0154 L1, last group, at the fold) - read: 117 (ci, "i-ci"); checked: image, decode, transcription; arbiter probable (two clear 1s and a 7-like top stroke, the digit may run into the binding), P1 "56? ###", P2 "117?"; "jouir ici à l'avenir" makes sense, the word stays a hole ({ici})
- 54? (0154 L4, last group) - read: 54 (et); checked: image, decode, transcription; arbiter sure, P1 54, P2 54?; "par tolérance et la simplicité" makes sense
- 57 (0154 R3, first group after "des Turcs") - read: 57 (st), unresolved; checked: image, decode, transcription; arbiter probable (a real group, ink blot on the 5, top bar of a 7), P1 "57?^" perhaps struck through, P2 "51?"; "st que si cette résolution" gives no sense, kept as a hole
- 333 (0154 R3, second group, first 3 retraced) - read: 333 (que); checked: image, decode, transcription; arbiter probable, both passes 333; "que si cette" fits
- 162 (0154 R11, last group but one) - read: 162 (na); checked: image, decode, transcription; arbiter sure (closed loop like the 6 of 64), P1 152, P2 162; no word comes out either way, hole
- 182 (0154 R11, second 182, blot on the 8) - read: 182 (ni); checked: image, decode, transcription; both passes 182, no arbiter crop; "Co-ni-g-li-a-ni" spells Conigliani
- 49 (0156 L4) - read: 49 (s); checked: image, decode, transcription; arbiter sure (a 4, not 11), P1 119, P2 49; "stipulés par" fits, 119 (fi) would not
- 333? (0156 L1, last group, at the fold) - read: 333 (que); checked: image, decode, transcription; arbiter sure; "mais quoy que" fits
- 55? (0233 L1, last group, small at the fold) - read: 55 (u), doubtful; checked: image, decode, transcription; both passes 55?, no arbiter crop; "ie-u/se" for "j'eusse" fits, the word stays a hole
- ### (0233 L2, after 138) - read: lost; checked: image, decode, transcription; arbiter: a group exists, only the left edge of its first digit shows; "de-?-se-i-n" suggests dessein, hole
- 9### (0233 L4) - read: 9 and lost digits; checked: image, decode, transcription; arbiter probable for the 9; "?-ne-e" after "du siège de la" suggests 97 (ca), Canée, hole
- 108 (0233 L5, last group) - read: 108; checked: image, decode, transcription; arbiter sure, P1 108?, P2 108; the group has no attested value
- 8### (0243 L1, last group) - read: 8 and lost digits; checked: image, decode, transcription; arbiter sure for the 8, a second digit begins with a left arc; "du ? Seigneur" suggests 80 (grand), hole
- 93 (0438 R2) - read: 93 (ou), one group; checked: image, decode, transcription; arbiter sure (no dot between 9 and 3), P1 93?; "un temps où nos ennemis" fits
- 22? (0439 L3) and 134? (0439 L4), last groups - read: 22 (s), 134 (ru); checked: image, decode, transcription; arbiter sure for both; "lais/ser" and "bru/it" fit
- 3### (0439 L5, last group) - read: 3 and lost digits; checked: image, decode, transcription; arbiter probable for the 3; "ve-?" suggests veu (32), hole
- 235^ (0154 R1), 313^ (0233 L1), 138^ (0233 L4), 166^ (0439 L3) - read: as written; checked: image, decode, transcription; retraced digits (235, 138; 313 marked by P1 only) and an underline (166) noted by the passes, read alike by both, no arbiter crop; "ve-cu", "par-u-t" and "de" fit, 166 has no attested value
- 177 (0154 L1) - read: 177, unresolved; checked: image, decode, transcription; both passes 177 with no mark, no arbiter crop; the sentence wants ne (172); raised by the decode on 24 Nov 2026, hole
- 39 (0156 L3, first group) - read: 39 (f); checked: image, decode, transcription; both passes 39 with no mark, no arbiter crop; "de-si-st-f-r" for désister has a stray f where an e is wanted (29 or 36); raised by the decode, the word stays a hole
- 28 (0156 L3, in co-m-se-n-te-ment) - read: 28 (m); checked: image, decode, transcription; both passes 28, no arbiter crop; the word wants n (38), as in the same word at 0233 L2; raised by the key replay on 24 Nov 2026, the word is now a hole
- 42 (0154 R16, in se-u-l-y) - read: 42 (y); checked: image, decode, transcription; both passes 42, no arbiter crop; "qui feroient seul y le commerce" has a stray y where the plural (47, s or z) would fit; raised by the decode, the y stays a hole
- 114 (0242 R1) - read: 114 (ri); checked: image, decode, transcription; both passes 114, no arbiter crop; "ri-ce-vo-i-r" for recevoir (104 re is wanted); raised by the decode, the word stays a hole
- 33 and 59 (0155 L3, 0242 R1) - read: 33 and 59; checked: image, decode, transcription; both passes alike in both places, no arbiter crop; P1 warns that this hand's 5 is easily taken for a 3 (55/33), but 55 (u) gives no word either; no attested value

## Conditions of use of the images
- Source: Archives nationales, AE/B/I/381. Brice Dudout ordered the reproduction on 2 Nov 2026 through the Archives nationales' online inventory service (reproduction no. 102 974 276), as an ordinary digital file, declaring private use. The invoice (RE-2026-0337, 30.20 EUR for AE/B/I/381 and AE/B/I/414) was paid by Brice Dudout on 17 Nov 2026, and the 51 JPEG files arrived on 20 Nov 2026 by a download link.
- No written conditions of reuse came with the files or with the invoice e-mail, as far as our records show; we have not read the invoice PDF or the delivery message for terms. Whether reuse of the images is allowed has not been confirmed, so the images are not committed or distributed (the files give shelfmark and image numbers only).
- Nobody has agreed to AI analysis: the question was not put to the Archives nationales. This is a question of the conditions of use, not an unread piece of the text, so it is no longer listed under Remaining gaps (24 Nov 2026). The pieces were transcribed and read with AI assistants on the strength of the private-use order alone.

## File map for the hashes
`prereg/SHA256SUMS_prereg.txt` was written in the working folder, where the transcriptions sat in `transcr/`. In this
folder they are `key_source/` (gloss_376.txt, gloss_452.txt, CONVENTIONS.md) and `blind/` (blind_P1.txt, blind_P2.txt,
arbiter.txt). The list holds ten hashes for nine files (KEY_v2 twice: 8c946279... and, at 13:38, the final
161bde95...). Eight of the nine files match the files here: PREREG.md, gloss_376, gloss_452, both blind passes,
the arbiter, KEY_v1 and the final KEY_v2. `key_source/CONVENTIONS.md` does not match. It was edited after hashing,
and its text is the transcribers' instructions only. It is not an input to the key or the measure.
