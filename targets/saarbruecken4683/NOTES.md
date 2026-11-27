# saarbruecken4683: captivity of Count Gustav Adolf of Nassau-Saarbrücken, 1673-74 (Landesarchiv Saarland, Nassau-Saarbrücken II Nr. 4683)

## Document
Landesarchiv Saarland (Saarbrücken), Bestand Nassau-Saarbrücken II, Nr. 4683: a file of 344 leaves (finding aid) on the arrest of Count Gustav Adolf of Nassau-Saarbrücken (1632-1677). French troops occupied Saarbrücken on 2 Dec 1673; the count was arrested on 11 Dec 1673, taken to Nancy and then to Metz, and returned on 13 May 1674 (ADB, NDB). The file is the correspondence of his elder brother, Count Johann Ludwig of Nassau-Ottweiler (1625-1690), with relatives, agents and the Nassau houses (Usingen, Idstein, Weilburg) from December 1673 to March 1674. 47 double pages (fol. 159v-340r) were photographed by the archive and sent on 26 Nov 2026; the inventory of what each shows is in the pull request's working notes. Credit line required by the archive for any reproduction: "Landesarchiv Saarland, Nassau-Saarbrücken II Nr. 4683, fol. ...". No image is committed; their SHA-256 are in `frozen/IMAGES-SHA256SUMS.txt`.

## System and key (`key.tsv`)
- **System A** (all cipher passages of the file except fol. 290): numbers 40-199 are letters, on a table of 24 cells repeated every 24 numbers: letter = table[n mod 24], table from residue 0 = `z n b s e c s d h l i p k t w u m q a i g o r f` (so e = 52, 76, 100, 124, 148, 172; n = 49, 73, 97, 121, 145, 169). Residue 6 is voted s by the glosses; x would be expected, it is rare. Numbers from 200 up are a nomenclator: 50 values recovered from the glosses (236/248/260 Graf, 241/253/265 Kaiser, 266/278 König, 290 Frankreich, 284/626 Reich, 282/306 Memorial, 389/401 Schreiben, 622 Saarbrück, 345 Maintz, 334 Trier, 332/344/356/368 Köln, 552 Hocher, 745 Fürstenberg, 807 Montecuculi ...). The numbers are often written without a stop but split without ambiguity (a group starting with 1 has three digits, 4-9 two).
- **System H** (the letter from The Hague, fol. 290r-v): a = 1, b = 2, ... (i 9 and 22, k 10, u/v 20, w 21, z 24), with codes 70 England and 180 Prince of Orange (glossed). 15 is p, but the glosses read it n in nicht, sondern, genereux; 23 is x (expressen) but also stands in genugsamb.
- How the A key was obtained: 2,439 number-letter pairs from the interlinear decipherments of the received letters and the cipher margins of the drafts (`frozen/working/T1-T4.tsv`), majority per number (`frozen/CLE-K.json`), then reduced to residues mod 24 (`frozen/CLE-K24.json`, built by `frozen/scripts/mesure3b.py`).

## Validation (`validation.txt`)
Three pre-registered tests on system A (one failed, one not run for lack of material, one passed: 0.815 against a bar of 0.664 and a best control of 0.330), one on system H (0.948 against 0.301). The failed test and the deviations are stated there.

## Reading (`reading_290.md`, `translation_290.md`, `reading_293.md`, `translation_293.md`)
- Fol. 290r-v, The Hague 2/12 Feb 1674, signed "X X": 286 cipher words, 247 certain (86.4 %), 24 probable, 10 restored, 5 unresolved; read in part. The interlinear decipherment of the time covers it; our reading agrees with it and adds nothing to its content. The writer calls Gustav Adolf "our brother": a brother of the captive in the Netherlands (Walrad of Nassau-Usingen, in Dutch military service, is a hypothesis, not checked). The letter expects "in wenig Tagen den Frieden mit Engellandt": the Anglo-Dutch Treaty of Westminster was signed on 19 Feb 1674. "Duc de Bourneuille" is Alexandre-Hippolyte, prince de Bournonville, the imperial general; Homburg is Hohenburg/Homburg in the Saar, held by Lorraine at the time.
- Fol. 293r-v, a copy received on 23 Jan 1674, with no decipherment: first 41 lines (465 numbers) read in part, 56 of 80 cipher words certain (70 %). Here the reading is new. The copy may be another copy of the glossed letter fol. 279r-281r (received the same day); not yet compared.

## Transcription doubts
- 290r-v: 66 disagreements between the two blind passes, settled on the image in `frozen/transcriptions/ARBITRAGE-H-JOURNAL.md` (49 settled, 13 of them with a doubt, 7 left illegible); checked: image, decode, independent transcription.
- 290r l. 26: three signs left illegible ("[Bruder] [gefaßt]"); checked: image, decode; the gloss reads the sense.
- 293r l. 17: line ends "48 87 ??" (a digit cut at the edge of the inserted leaf); checked: image.
- 293r l. 27: a doubtful "8?" between 112 and 61 (stroke or digit); left as doubtful; checked: image.
- 293v l. 6: "80?" under a stain; checked: image.

## Prior art
Searched 26-27 Nov 2026: the repository's catalogue, leads and archive requests (nothing on this file); DECODE (not listed); web searches on the arrest of Gustav Adolf (biographies only: ADB, NDB, Wikipedia). No edition of the letters and no published key found. The content of the received letters is deciphered in the file itself (interlinear decipherments of the Ottweiler chancery).

## Remaining gaps
See `profile.json` `outcome.gaps`: open nomenclator groups; the rest of the copy fol. 293v-295r; the other received letters, deciphered at the time and not counted here; the writer of the Hague letter.

## Conditions of the images
Photographs supplied free of charge by the Landesarchiv Saarland on 26 Nov 2026 (Dr David Schnur), with permission to publish them online with the credit line above. Analysis with an AI assistant was not raised with the archive. None is committed.
