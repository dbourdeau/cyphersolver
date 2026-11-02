# Blathwayt 1729: intelligence report from Port Sainte-Marie, summer 1729 (catalogue 826; notes on 827 and 828)

Status: no write-up (duplicate of docs/portstemarie1729.html, the existing page for the same sheet; Brice Dudout's fuller reading, 105 of 108 words, is not yet folded into it; decision pending, 30 Oct 2026)
Status: read (Brice Dudout, 28 Oct 2026; 105 of 108 words read in their sense, 88 certain, 17 probable, 3 unresolved; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Published write-up (local, to be pushed when the GitHub account is restored):
https://bdudout.github.io/europe-chiffree/en/documents.html#blathwayt-1729

## Document

The Huntington Library (San Marino, California), William Blathwayt papers (Addenda), mssBLA 191, box 3, p. 5 (Huntington Digital Library, p15150coll7 61005); catalogue: “Enclosure: Two letters from Port Ste Marie: (a) undated, in cipher”.
Summer 1729 (undated; arrived with a letter of 21 July 1729, forwarded on 8 August 1729). El Puerto de Santa María (Andalusia) → “Milord” (Cessnock, Scotland) → London (Duke of Newcastle).
Sender: Anonymous informer (“the correspondent at Port Saint Mary’s”). Recipient: “Milord”, probably Alexander Hume-Campbell, 2nd Earl of Marchmont, recipient of the reports in the collection; covering letter from Cessnock, 8 August 1729, to the Duke of Newcastle, Secretary of State.
Huntington Digital Library: https://hdl.huntington.org/digital/collection/p15150coll7/id/61008. Images not included.

An informer in British pay at El Puerto de Santa María (Port Sainte-Marie, across the bay from Cadiz) writes in a numerical code to “Milord”, who forwards the sheet to the Duke of Newcastle on 8 August 1729. No decipherment is written on it. The same collection holds seven other pieces from the same network (January 1728 – August 1729) deciphered between the lines by a clerk: they allowed us to rebuild the code book, then to read the sheet.

## System and key

One-part numerical code (≈ 1 to 1324): for each initial, first the letters, syllables and short words, then the long words, in alphabetical order (285 do, 287 don, 289 du; 307 découvrir, 320 démarche, 322 dernier); several numbers for frequent words; 1205–1213 = one to nine, 1–17 = tens, hundred, thousand; beyond, nulls and separators.

`key.tsv` = table K2. Table K1 (333 numbers) was rebuilt only from the contemporary interlinear decipherments of seven sister
pieces in the same collection (HDL 61081 Jan 1728; 60963 = mssBLA 187, 23 Jun 1729; 60917-60920 copies 29 Jun-19 Jul 1729;
60887 14 Jul 1729; 60893-60894 undated 1729) and frozen (SHA-256 ea45b4c7...f439) before validation. K2 (397 numbers) adds the
held-out piece of 4 Aug 1729 (HDL 60907-60909) after validation.

## Validation

Held-out piece of 4 Aug 1729 (HDL 60907): 153 numbers transcribed with their contemporary gloss after the freeze. K1 covers 123;
its reading agrees with the gloss for 95.9% of words and 95.2% of characters, against a 99th percentile of 2.4% / 22.9% for 200
permuted-table controls. Interpolation check: for the 28 new numbers of the held-out piece, the alphabetical place between two K1
values gives the right initial letter 27 times. Caveat: the contemporary gloss is on the same image as the numbers.

## Reading

First published decipherment, to our knowledge. 141 numbers, 108 words. Published under Daniel Bourdeau’s rule: 95% of the words read in their sense. Here: 105 of 108 words read in their sense (97.2%), of which 88 certain (81.5%), 17 probable (15.7%), 0 restored and 3 unresolved (2.8%): ‹214›, se‹711›s and ‹pr›ès. The probable words are numbers absent from the contemporary decipherments, read from their place in the code book and from the sense (see the notes).

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- Context. In 1729 the Spanish court was in Andalusia and the “accommodation” between Spain, Great Britain and France that led to the Treaty of Seville (9 November 1729) was being negotiated. Benjamin Keene was the British minister at Madrid; the informer complains of being kept out. In the deciphered sister pieces he says that José Patiño “has taken a liking to me” (14 July 1729) and that “Monsieur Keene confides nothing to me”; the piece of 4 August 1729, endorsed “Not sent because not material and containing a complaint against Mr. Keene”, repeats the complaint. This one, by contrast, went to Newcastle.
- The probable words. The code book is in alphabetical order, so a number absent from the contemporary decipherments can be read from its place between two known values, then from the sense. On the held-out piece (4 August 1729) this rule gives the right initial for 27 of 28 new numbers. obligation 805 (between ou 802 and obstin 807); quinze 6 (series 1–17 of tens: 8 vingt, 16 cent, 17 mille, attested in clear); six 1210 (series 1206 deux, 1207 trois, 1209 cinq, 1211 sept, 1212 huit, 1213 neuf); mars 689·34·1013 (689 precedes 690 = “m”, attested in no·ve·m·br·e; 34 ar; 1013 s); aujourd’hui 103 (attested; the reading 163 = “ce” is not excluded, a blot covers the middle digit); ferez 460·945 (460 between faut 456 and fait 461; 945 res, attested in ad·res·se); dois 285·594 (285 between des 282 and don 287); agir 58 (glossed “agit” on 14 July 1729); ordre 816, twice (long o- words, after obstination 807 and before p 821); tout 1118 (cluster tou/tout 1112–1119); service 1052 (between sentiment 1049 and soupçon 1063); merci 726 (between marque 719 and mettre 731); ignore, ignorance 585 (between ie 581 and il 588); vos 1152 (between vo 1150 and vous 1153); conduite 222 (between conclu 219 and confidence 224).
- Unresolved words and caveats. ‹214› (between conce 211 and confidence 224: a word in con-; re-read on the image by Brice Dudout as 214, not 274) names what is leaving: a person or the court; we do not restore it. se‹711›s (711 between majesté 709 and malheur 713) follows “aucun ordre des”; ‹pr›ès (836, between pour 835 and près 838, followed by “es”) may be “près”. The month “mars” reads well (m·ar·s) but is surprising on a sheet that arrived in July: the informer may be dating from the older letter he answers. “Monsieur Keene ne m’aime”: the cipher has no full negative.
- The same code elsewhere (catalogue nos. 827 and 828). The Madrid letter of 13 September 1728 on Ripperdá’s escape (mssBLA 186) carries one line in this code: 659.78.73.18.438.468.470.278.190.1102.53 = “L’ambassadeur ‹73› a été fort ‹470› de cette affaire” (“the ‹73› ambassador was very ‹470› at this affair”; 73 between avoit 69 and ambassadeur 78; 470 is an unattested f- word): partial reading, 9 of 11 words. In the statement on Rottembourg (mssBLA 184), the numbers 1240, 1243 and 1250 are, according to the contemporary decipherments, nulls or separators (1240 is inserted in the middle of “Ken·ne” on 4 August 1729): “et Monsieur 1240 de 1243 la Paz” therefore reads “and Monsieur de la Paz”, the Spanish Secretary of State; that piece hides no other word.
- Prior work. The Huntington catalogue notes no decipherment; the sheet carries none. As of 28 October 2026 Daniel Bourdeau’s repository holds only the catalogue entries (nos. 826–828).
