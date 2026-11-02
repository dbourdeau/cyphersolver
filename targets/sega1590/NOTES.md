# Sega 1590: Filippo Sega, Bishop of Piacenza, Paris, 26 November 1590 and 16 January 1591 (AAV Francia 32, ff. 17r-v and 71r-v)

Status: read (Brice Dudout, 29 Oct 2026; two letters, 134 of 136 enciphered words read in their sense: 26 Nov 1590, 82 of 84 (79 certain, 3 probable, 2 unresolved); 16 Jan 1591, 52 of 52 (46 certain, 6 probable); Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 29 Oct 2026. Not in the current catalogue (it was listed as no. 881, "Sega, Francia 32", an entry since withdrawn); submitted as a new cipher with solution.
Published write-up (local, to be pushed when the GitHub account is restored): https://bdudout.github.io/europe-chiffree/en/documents.html#sega-1590

## Document

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32, f. 17r-v: letter of Filippo Sega ("il Vescovo di Piacenza"), dated "Di Parigi li 26 di Novembre 1590",
to a cardinal ("Ill.mo et R.mo Mons. Padron mio Col.mo"; other letters of the series are addressed to Cardinal Enrico Caetani). Mostly in clear; one enciphered passage
of 14 lines on f. 17r and 1 line at the top of f. 17v. Images: DECODE R5612 (views 3-4), https://de-crypt.org/decrypt-web/RecordsView/5612 - not included (DECODE terms: research use only).

Second letter (added 29 Oct 2026): Francia 32, f. 71r-v, Sega to Cardinal Caetani ("Ill.mo Caetano"), "Di Parigi li xvi di Genn.o 1591": in clear with about twenty short enciphered groups set inside the sentences. Images: DECODE R5616 (views 3 and 7), https://de-crypt.org/decrypt-web/RecordsView/5616 - not included. A faint registration note at the head of f. 71r ("... Decifrata 17 ...") shows that a contemporary decipherment once existed; it is not among the DECODE images.

Not included here: a third letter of Sega, the duplicate ("Dupp.ta") of early January 1591 in Francia 32, ff. 49v-54v (DECODE R5615, https://de-crypt.org/decrypt-web/RecordsView/5615, images not included), was transcribed and decoded with the same key 65 over its whole enciphered text, but read only in part: 1,319 enciphered words, 1,094 read in their sense (82.9%: 886 certain, 205 probable, 3 restored, 225 unresolved), below Daniel Bourdeau's 95% threshold; the copy is also incomplete (f. 54v ends in the cipher, with no subscription). It is published on our site as a partial reading with the unresolved words shown in place (https://bdudout.github.io/europe-chiffree/en/documents.html#sega1591-dupl), and is not submitted here as a reading.

## System and key

Meister (1906), key no. 65, "cifra servita in legatione sub Sisto V" (pp. 435-436): letters as digit pairs, vowels as signs on the pair or on a single digit,
nulls 7 8 9 0, code letters and symbols for common words, three-digit nomenclator. George Lasry identified this key for Sega's letter of 9 January 1591 (BnF fr. 3613; see targets/sega1591).
Applied here unchanged (`key.tsv`).

## Validation (held out)

Protocol written and hashed before calculation. Sega's letter of 21 December 1590 (Francia 32, ff. 228v and 231) has a contemporary decipherment on f. 230
("decifrato 26 di Marzo 1591"; DECODE R5621, https://de-crypt.org/decrypt-web/RecordsView/5621). The decifrato was transcribed and frozen first; the cipher was then decoded with key 65 unchanged:
268/287 characters (0.934) and 56/65 words (0.862) agree, against at most 0.551 / 0.492 for 200 controls with permuted letter values (word codes unchanged).
Criterion 0.85 / 0.75 met. Caveat: the transcriptions were made with the key in mind.

## Reading

26 Nov 1590: 84 enciphered words (345 signs): 82 read in their sense (97.6%) under Daniel Bourdeau's 95% rule: 79 certain (94.0%), 3 probable (3.6%), 0 restored, 2 unresolved (2.4%): <canonizatorio> (digits certain, sense not established) and <c> (22 followed by a dotted 9, a null).

16 Jan 1591: 52 enciphered words, all read in their sense (100%): 46 certain (88.5%), 6 probable (11.5%), 0 restored, 0 unresolved. Clear text of the letter in quotation marks (abridged "...").

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- Context: Paris, end of November 1590, just after the siege was lifted by Farnese. The clear text before the cipher speaks of a bishop held prisoner, of the "sacrilege" that causes a great stir and of requests for his "rilassatione"; the cipher keeps Sega's judgement (the bishop leans to the "opposite party", Navarre's) and his plan to temporise. On f. 17v, in clear, he asks that the Pope unmask those who "seguitano il partito contrario".
- Contemporary decipherment of the letter of 9 January 1591 (your targets/sega1591): AAV Francia 32 keeps it next to the cipher (DECODE R5613, https://de-crypt.org/decrypt-web/RecordsView/5613, "Decifrato", beginning "Che Lignerac è stato inviato d'ordine di Umena in Poitù et Bretagna a sollecitare l'impresa di Tours"), which agrees with Lasry's reading. The sega1591 profile says "plaintext: none known" - this is a catalogue correction.
- Sega's letter of 2 July 1591 (DECODE R5618, https://de-crypt.org/decrypt-web/RecordsView/5618) uses another system (digits without signs, many 1s, 7s, 9s): by a criterion fixed before calculation, key 65 segments only 62.5% of its pairs (threshold 85%) and was rejected.
- Letter of 16 Jan 1591: Sega says Mayenne ("Umena", 128) wrote "non so che di bono per me a Roma", that he needs no stronger intercession with the Pope than that of the Duke of Bavaria, and that he has awaited "quel pomo" for many years (hypothesis: the red hat; Sega was made cardinal by Innocent IX in December 1591).
- Prior work: no edition of Sega's 1590-1591 dispatches found (the Acta Nuntiaturae Gallicae do not cover Sega; M. Penzi 2017 is a study).
