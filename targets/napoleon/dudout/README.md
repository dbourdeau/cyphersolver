# "Berthier to Napoleon, 22 December 1812": read with the Great Cipher of 1812 — a letter of King Joseph (Brice Dudout)

Status: read (Brice Dudout, 12 Oct 2026, count 29 Oct 2026; 233 of 233 words read in their sense, 225 certain, 3 probable, 5 restored, 0 unresolved; Daniel Bourdeau's 95% rule).

**Priority.** Ilia Chirtulov was the first to find that the Great Paris Cipher (Grand Chiffre of 1812) reads this cryptogram and that the writer is King Joseph (result received by S. Tomokiyo on 4 Oct 2026, reported on Cryptiana, https://cryptiana.web.fc2.com/code/unsolved.htm, on 12 Oct 2026). This folder is an independent re-reading, done without knowing that result, which adds the complete line-by-line reading, the re-reading of the cipher on the 1969 plate (8 groups corrected), a permutation control and the sister letter. Published: https://bdudout.github.io/joseph-napoleon/ (site currently offline: the GitHub account is suspended).

## What it is

The 325 groups printed by J. Vilcoq, "Le chiffre sous le Premier Empire", Revue historique des Armées 1969 no. 4 (plate after p. 24, digitised by Persée, DOI 10.3406/rharm.1969.8686), captioned as a dispatch of Berthier to Napoleon of 22 Dec 1812 (Archives nationales). The plate is page 3 of the dispatch. Read with the deciphering table of the Great Cipher of 1812 (the code of the French armies in Spain, 1,200 groups extended to 1,400; table at the Service historique de la Défense, "B n° 30", photographed by Jean-François Bouchaudy), it gives a French letter written in Spain by a king to the Emperor: news cut off since Napoleon left Paris, no returns from the Army of the North, quadruplicates of the Salamanca dispatches, a copy of a dispatch of General Reille enclosed, the "concentration" it demands. It cannot be Berthier's, who was then with the remnants of the Grande Armée in East Prussia. A letter of Joseph to the Minister of War, Madrid, 23 Dec 1812 (Du Casse, Mémoires et correspondance du roi Joseph, vol. IX, 1854), covers the same matter with the same phrases (Reille's enclosed letter, "I knew well... but I did not believe it in so bad a state").

## Method and validation

- Tant's ARCSI tables of Imperial great ciphers tried first: unrelated words (negative). The Great Cipher of 1812 read from the first line: 918 je · 1045 n · 1100 ait · 493 aucun · 359 nouvelles · 989 de · 1105 Votre · 73 Majesté ... The Spanish additions above 1,200 fit: 1202 Valladolid, 1238 "l'armée du nord de l'Espagne", 1388 Salamanque.
- Control: French 4-gram score (model trained on an independent text, Berthier's letters of December 1812 printed by Chuquet, 1912) of the decoded text -2.11 per character, against -2.63 median and -2.43 best for 1,000 decodings with the numbers of the same table shuffled (0 of 1,000 reach it); Tant's tables -2.72 to -2.82. Homophones as expected: de = 13, 544, 710, 989, 1060; que = 69, 607, 893.
- Re-reading of the plate (Persée high resolution): 8 groups differ from the online transcription and each correction makes the passage clear (see transcription.txt header). This also settles the 356/656 variant you noted between unsolved.htm and napoleon2.htm: the plate reads 356 ("préjudice"), but the sense requires 656 ("quel"): a slip of the encoder or copyist; likewise 325 ("paix") where a full stop (225) fits.
- Sister letter: Joseph to the Minister of War, 23 Dec 1812 (above): an independent confirmation of the content, not a word-for-word collation.

## Count by the 95% rule

233 words of cipher text (elisions counted as two words): 225 certain, 3 probable (compte 559, sous 1086, [q]ue 131), 5 restored from the sense (ni 851 and ité 1051 on a fold of the table, illegible in both photographs; quel[le]s 356 for 656; concentration 495 "car" for "cen"; exigeât 320 "C" for "t"), 0 unresolved.

## Files

- `transcription.txt`: the 325 groups as re-read on the 1969 plate.
- `key_entries.tsv`: the 226 table entries read for this text (original spelling); the photographs are not redistributed (see Bouchaudy's site).
- `decode.py`, `decryption.txt`: group by group with its table value.
- `reading.md`: line-by-line reading, running French text, doubtful groups, count.
- `translation.md`: English translation.

## Credits

Ilia Chirtulov (first identification of the key and of the writer, via S. Tomokiyo); S. Tomokiyo (Cryptiana: the cryptogram's transcription and the survey of Napoleonic ciphers); Jean-François Bouchaudy (photographs of the table, The codebooks of Napoleon I, http://www.jfbouch.fr/crypto/napoleon/index.html); J. Vilcoq (1969 plate). Reading, re-reading of the plate, control and write-up: Brice Dudout with Claude (Anthropic). CC BY 4.0, as the joseph-napoleon repository.
