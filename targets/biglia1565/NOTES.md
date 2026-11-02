# Melchiorre Biglia, nuncio in Vienna, 1565: two cipher letters (Ambrosiana, Trotti 22, fols 6v-7v)

Status: read in part (Brice Dudout, 29 Oct 2026; letter 2 read: 362 of 381 cipher words read in their sense = 95.0%, 313 certain, 42 probable, 7 restored, 19 unresolved; letter 1: 689 of 729 = 94.5%, not published).

Contributed by Brice Dudout (Europe chiffrée), 29 Oct 2026. Write-up (to be published when the account is restored):
https://bdudout.github.io/europe-chiffree/en/documents.html#biglia-1565

## Documents

Milan, Veneranda Biblioteca Ambrosiana, Trotti 22, fol. 7r lines 33–45 and fol. 7v lines 1–23 (register of Biglia’s letters; digitised by the Università Cattolica, no reuse licence: no image reproduced).
Letter 2: “a li [cinque] di decembre del sesanta [cinque]”: December 1565; the day (5?) is restored, not read. Vienna (“uiena”) → Rome.
Sender: Melchiorre Biglia, apostolic nuncio to Maximilian II. Recipient: not named in the cipher; “V.S.” (restored reading), probably a cardinal of the Curia.
Images: Università Cattolica digital library (manifest "No Downloadable", no licence; not copied here).
Neighbouring plain-text letters in the register: fol. 6r (to Altemps, 15 Nov 1565 = Dengel no. 7) and fol. 7v bottom (to the Emperor, Augsburg, 16 Jan 1566).

Vienna, late 1565. Melchiorre Biglia, sent by Pius IV as nuncio to Emperor Maximilian II, is conducting a difficult negotiation: the Emperor asks for the right of priests in his lands to marry (the “connubio”), which Rome refuses; in return the Pope offers military help against the Turk. The register of Biglia’s letters at the Ambrosiana holds two letters entirely in cipher, never published (Dengel, who edited the nunciature in 1926, prints nothing of them). We publish the second one here. Biglia answers the reproaches he received from Rome for a “bad start” to the negotiation that offended the Emperor; he discusses the offer of four thousand foot or two thousand horse, advises that the Emperor send “a person of his blood” at their head, and recounts the visit of Doctors Zasius and Weber, of the privy council, who came to dine with him.

## System and key

numerical syllabic cipher written without spaces, words separated by “00”: a single digit = vowel or bare consonant (2 e/s, 3 u/l, 4 i/t, 5 a/n, 7 o/r); two digits = row consonant (0 m/g/v, 1 c/p, 2 s, 3 l, 4 t, 5 n, 6 d/f, 7 r, 8 soft c/b, 9 gn) + column vowel (1/2/8 e, 3 u, 4/6 i, 5 a, 7/9 o); codes 59 qua, 97 che, 19 per; a small nomenclator (11 S.M., 9 e, 49 non, 3 questo, 4 quel, 87 connubio, 21 Imperatore).
`key.tsv` = key K5d, reconstructed from the ciphertext alone (no contemporary key or decipherment found).

## Validation

Protocol written and hashed before any computation. Training part: letter 1 fol. 6v to 7r line 2, and letter 2.
Held-out part, never decoded before the measurement: letter 1, fol. 7r lines 3-27 (1,543 digits, 252 words).
Key frozen (SHA-256 50f9f337...) and then measured once: lexical agreement 0.761 (175/230 words of 3+ digits found in an
Italian word list, after a spelling normalisation fixed before the measurement: v/u, j/i, h dropped, doubled letters reduced)
against at most 0.500 (mean 0.352) for 200 control keys; threshold fixed in advance: 0.65. A loader bug found later
dropped a few line-final digits (about 5 of the 252 held-out words): it worked against the key, so the validation stands.

## Reading

Counted per letter, one unit = one cipher word between "00" separators (headers and struck passages excluded).
"Certain" = exact output of the frozen key (checked by script). Any value taken from context (bare 1 = c/p, 6 = f, 8 = b;
joined nomenclator codes; corrections of the transcription made after re-reading the image) counts as probable at best.
A nomenclator value is certain only with three independent contexts. The reading was frozen (SHA-256) before counting.
Letter 2: 381 words; 313 certain, 42 probable, 7 restored, 19 unresolved -> 95.0% read by sense (exactly the threshold;
strict, certain + probable: 93.2%). Letter 1: 729 words; 604 / 68 / 17 / 40 -> 94.5% (not published).
The day of the date is restored ([cinque] from the year 1565 only); "di decembre del sesanta" is read.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv` (letter 2 only).

## Notes

- S.M. (code 11, sure: ≥ 3 contexts) designates the Emperor; its exact wording (“S.M.”, “l’imperatore”) cannot be decided. Code 21, which is se by the key, also bears the value Imperatore in the first letter (polyphony declared before reading); it does not occur here.
- [V.S.] (code 45, in by the key): value restored from the sense; the recipient is not named.
- {S.M. questo} (7r 36): two nomenclator codes written without a separator (11 + 3); 3 = questo is always followed by “000”, as here.
- {ofrendo} (7v 1) and {molto obligo} (7v 14) assume the bare values 6 = f and 8 = b, which are not in the validated key: probable readings only.
- Ciasio and Vueber are read exactly; their identification with Johann Ulrich Zasius and Johann Baptist Weber, Maximilian II’s councillors whom Delfino recommended to Commendone as “consiglieri primarii”, is probable (Dengel, NB II/5).
- The connubio: marriage of priests, which Maximilian II asked of Rome; Dengel (NB II/5, introduction) recalls that the Emperor hoped to obtain it until the death of Pius IV on 9 December 1565.
- The date: “uiena” and “di decembre del {sesanta}” are read; code 14569, twice, is restored [cinque] only from the year 1565 given by the neighbouring plain-text letters (15/11/1565 before, 16/1/1566 after). The day is not established. 7v 22 ends with an isolated word (1886) that is not read, and the date with another (10869).
- Re-reading of the image: 7v 22–23, the short line ending the text stops after “1886”; “64” (di) opens the date line (probable reading).

## Remaining gaps
- 19 unresolved words of letter 2 (7r ll. 38-41 and 7v ll. 10-23), each inside a sentence that otherwise reads - blocker: no-key-material; code groups with no value in any key, sibling or print, each occurs once, no context narrows them
- letter 1 (fols 6v-7r l. 27; 729 words, 94.5% read, 40 unresolved) - blocker: no-key-material; read by Brice Dudout but its text is not published here, so it is not counted

## Escalation
- [x] siblings: the register's neighbouring letters (fol. 6r to Altemps, 15 Nov 1565; fol. 7v bottom to the Emperor, 16 Jan 1566) are in plain text; letter 1 is the sibling cipher and trained the key
- [x] clear-pages: no decipherment or interlinear on the register leaves (cipher letters entirely in cipher)
- [x] known-keys: no contemporary key or decipherment found for this register; none to try
- [x] print: Dengel, Nuntiaturberichte II/5 (1926) uses the register but prints neither cipher letter; web search on read phrases negative (profile, 29 Oct 2026)
- [x] key-rebuild: key K5d rebuilt from the ciphertext alone (annealing on letter 1 and letter 2, then by hand) and frozen before validation
- [x] retry: reading frozen (SHA-256) and recounted word by word after the key was fixed; the 19 left cannot be settled by context
