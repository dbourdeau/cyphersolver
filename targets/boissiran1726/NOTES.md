# boissiran1726 — Three cipher letters from the Poussard family to M. de Boissiran, Bordeaux and Saintonge, 1725–1726 (AD Charente-Maritime, 4 J 1524)

Catalogue 369 (« Robert de Boissiran, correspondance (dont plusieurs lettres chiffrées) », 1623–1732). Lead 1963 and archive request ar-147 are the same file (duplicates of 369).

Source: Archives départementales de la Charente-Maritime (La Rochelle), fonds Boissiran, **4 J 1524**. Photographed in the reading room on 26 Nov 2026 by a volunteer of the **Cercle généalogique d'Aunis (CGAunis)**, [name if she agrees]. 23 photographs. **Private study only: no image, crop or derivative is included or linked here** until the volunteer and the AD17 agree. File names of the photographs are given so that the work can be checked against them later.

## Prior art
None found: catalogue 369 says « ciphertext not seen »; no DECODE record (Boissiran, 4 J 1524); no edition, no web hit (searches of 26 Nov 2026). Pencil glosses on letters B and C (« a Bordeaux le … aoust », « … juillet », a name « Anne Poussart ») decode only the place-and-date lines and the signature: they are contemporary or later clear notes, not a decipherment of the letters. First reading.

## The documents (photographs 20261126_*.jpg)
| Doc | Pages (photo) | Date (in cipher) | Address (clear) | State |
|---|---|---|---|---|
| A | 160923, 160935, 160941 (retakes 161747, 161755, 161811); address 160900 | « ce 26 may 1726 » (archivist's pencil 1736/1786 is wrong) | « Monsieur Deboissiran, [conseiller] à la table royalle, à Saintes » | read in part |
| B | 161214, 161231 (retakes 161631, 161700); address 161614 | « a bordeaux le 14 aoust 1725 » | « Monsieur de Boissiran en son logis à Boissiran » | read in part (first reading) |
| C | 161523, 161533, 161541; address 161345 | « a bordeaux le .. iuillet 1725 » | « Monsieur Deboissiran dans son logis à Boissiran près Royan » | decoded, not read |
| key | 162030 (with 162003, 162013 on the same sheet) | — | — | key sheet, not prose |
Also in the bundle: an account in clear of 18 Feb 1664 (153345).

## The system and the key
The key sheet (« mode d'emploi », photo 162030) carries three tables: (1) a letter-for-letter substitution (plain a b c d … → p r h m …), used for a short line on 162013 and not treated here; (2) the cipher letters of table 1 numbered with digits; (3) the working table, plain letter → digit, which is table 2 sorted. Each digit stands for two or three letters: **0 a/x · 1 d/p · 2 f/r · 3 b/h · 4 m/y · 5 e/l · 6 c/g/u · 7 i/n · 8 q/s · 9 o/t** (`key.tsv`). Words are separated by spaces or dots. Dots over digits are frequent on the key and in the letters; their value was not established and they are ignored. So the decryption gives, for each digit, a set of letters, and the reading chooses by sense (`que` = 865, `de` = 15, `monsieur` = 49787562).
The key is the period key of the bundle, not a reconstruction. It was frozen (SHA-256) on 26 Nov 2026 before any transcription of the letters was decoded.

## Transcription (blind/)
Two blind passes per letter by two AI agents that had not seen the key sheet, then a blind arbiter (third agent, no key). Differences: A 81 of 483 groups; B 36; C 116 (34 left doubtful). Arbitrated texts frozen: `transcription_A.txt` (SHA-256 250228663369…d86a), `_B`, `_C` (`blind/TRANSCRIPTIONS-BC.sha256`). The digits come from the photographs only.

## Validation of the key (prereg/)
- **PREREG 1 (failed by design).** Held-out portion A p2.23–p3.08 (358 digits); measure = share of groups that segment fully into words of a 49,486-form French lexicon; 200 permuted-key controls; criterion ≥ 0.85 and ≥ best control + 0.30. Result 0.987 against 0.974: **failed**. The metric could not discriminate (almost any digit string segments into short words under 2–3 letters per digit). Declared, portion burnt.
- **PREREG 2 (passed).** After a power check on the burnt portion (key 0.7255 against 0.2745), metric changed to: a group of ≥ 4 digits counts when one of its expansions is exactly a lexicon form of ≥ 4 letters (no segmentation); 400 controls (200 permuted keys + 200 random keys with the same structure of 2–3 letters per digit). Hashed, then one measure on the fresh portion A p1.01–p1.09 (40 groups): **0.85 against best control 0.425**, mean 0.121. Criterion (≥ 0.50 and ≥ best + 0.30, both fixed before) met: key validated. The power check on a burnt portion and the second PREREG are declared in `prereg/PREREG-2-BOISSIRAN-A.md`.
The lexicon (`LEXIQUE-FR-EARLY.txt`, 49,486 forms) is ours and not committed; `measure.py` and `measure2.py` read it from our working tree.

## Reading
Rule: sure = the key gives the word from the transcription as it stands (choosing within each digit's set is the reading); probable `{x}` = one or two digits differ from the transcription; supplied `[x]`; unread `[...]`.
| Doc | Words | Sure | Probable | Supplied | Unread | Sure share |
|---|---|---|---|---|---|---|
| A | 487 | 427 | 30 | 2 | 28 | 0.877 |
| B | 253 | 225 | 5 | 2 | 21 | 0.889 |
Read in part. On three portions of letter A over 300 characters, the share read by sense (sure + probable + supplied) is 0.991, 0.960 and 0.975; on the whole letter 0.943.

## Content and context
- **A** (26 May 1726, to M. de Boissiran, conseiller at the « table royale » of Saintes — presumably the Table de marbre or a royal court seat; to be checked). The writer, who signs « votre très humble servante Poussard », denounces a woman, « hipocrite », « une femme si dangereuse », who spreads what happens in the house, went « dimanche dernier » to speak to two gentlemen, and boasts of her power over Boissiran's mind; the writer keeps to her room and says she will never abandon her blood and her « pauvres enfants ». Then estate business: the metayer wants the terms of the metairie and whether to mow the meadows, two calves; the metayer's father, recently dead, had stood surety for a miller who set fire to a mill, a loss of 2,000 livres.
- **B** (Bordeaux, 14 Aug 1725): a mother to her son (« mon cher fils », « ta chère et sincère amie Poussard »): a passage by ship to Marennes, a maidservant, cabbages and shoes, a letter from his procureur, his cordonnier, and anger at his letter.
- **C** (Bordeaux, July 1725): to be read; words seen: « mon cher fils », « Rochefort », « malheureuse », « crime », « ta tante Garnier », « adieu mon cher petit mari ».
- Signature: the cipher 19688021 (A, B, and C) gives P/D-o-u-s-s-a-r-d; « Toussart » (T = 9) and « Goussart » (G = 6) are excluded. The pencil note on B reads « Anne Poussart ». The family relation of the Poussard writer(s) to Boissiran is to be established.

## Transcription doubts
- 3 (tailed ʒ) taken for 7 in seven words of A (chagrin, horreur, a bout, abandonner, j'abandonneray, abuse, humble) - read: 3; checked: decode, transcription (two blind passes, several flagged [3/7]); not yet on the enlarged image, so the words stay probable {x}.
- 4 (open ч or crossed ϕ) against 6, 7 and 9 in four words of A (n'aye, m'enuoye, escriue, nouuelle) - read: 4, 7 or 5 as the word needs; checked: decode, transcription (both passes flagged [4/9] or [4/7]); not yet on the image, words stay probable.
- 0 taken for 9 in three words of A (pas, seruante, j'abandonneray) - read: 0; checked: decode, transcription; not yet on the image, words stay probable.
- 9 taken for 7 in two words of A (croire, caution) - read: 9; checked: decode, transcription; not yet on the image, words stay probable.
- stain at A p1.19 (« 86119#2952 », supporter) - read: no digit (the word is whole without one); checked: decode, transcription (passes A and B), arbiter on the image.
- B and C: every doubt of the arbiter is kept as [x/y] in transcription_B.txt and transcription_C.txt and listed with its reason in blind/ARBITRAGE-lettreB.md and blind/ARBITRAGE-lettreC.md - read: as marked; checked: image (arbiter), transcription (two passes).
- dots over digits - read: not transcribed in the frozen texts; checked: image (both passes noted them), decode (the key table does not use them).

## Remaining gaps
- Letter C, line starts of p. 1 (left half, 17 lines) and p. 3 (top, 6 lines) - blocker: illegible; out of focus on the photographs and p. 3 is holed; sharp photographs asked for through the volunteer.
- Probable words of A (30) and holes of B (21) - blocker: not-attempted; a blind sign check of the 3/7, 4/6/9 and 0/9 shapes on the photographs is open and workable.
- Names in A (p3.01, p3.05, Caux, Cauerne) and the identity of the Poussard writer(s) - blocker: not-attempted; genealogy of the Boissiran and Poussard families not yet searched.
- Table 1 of the key sheet (letter cipher) and the short line of photo 162013 - blocker: not-attempted; outside these three letters.

## Escalation
- [x] siblings: the three letters of the bundle are read with the same key sheet; the other pieces photographed (account of 1664) are in clear. The rest of 4 J 1524 (« plusieurs lettres chiffrées », 1623-1732) was not photographed.
- [x] clear-pages: addresses and pencil glosses agree with the decode (B: « le 14 aoust 1725 »; C: « … iuillet 1725 »; signature « Poussart »).
- [x] known-keys: the period key sheet of the bundle, applied unchanged.
- [x] print: no edition found (web search, 26 Nov 2026).
- [n/a] key-rebuild: the key is the period sheet; it decodes all three letters.
- [ ] retry: the probable words of A and the holes of B on the enlarged images (open, see Remaining gaps).
