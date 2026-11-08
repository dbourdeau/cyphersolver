# guastalla1717: the Duke of Guastalla refuses a "lettera reversale", 24 September 1717 (Biblioteca Estense, Autografoteca Campori, Lettera A, cc. 15-16)

Status: read in part (8 Nov 2026). Contributed by Prabal Gupta (issue #329; repository `prabal-rje/branicki-1757`, folder `guastalla-1717`, commit af80f5e, CC BY 4.0): a letter in Italian, clear at the start and the end and in a cipher of two-digit numbers between them, read from the ciphertext alone. Checked here against its own files only (`VERIFICATION.md`); the Estense scans (licence CC BY-NC-SA) are not reachable from the project and are not reproduced, so no transcription was compared with a scan here.

## The document

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera A, "Antonio Ferdinando, duca di Guastalla", cc. 15-16, four pages (https://lodovico.medialibrary.it/media/schedadl.aspx?id=848189d6-1008-497b-bcde-0e3a3ad9757f). Catalogue 1569 listed it with two other Campori letters (Augustoni, 1612; Olivazzi, 1725), which have other ciphers and stay in the catalogue. The Estense record dates it 24 July 1717 and calls it "Lettera parzialmente cifrata"; the dateline of the letter reads "Guastalla 24 7bre 1717", and "7bre" in letters of the time means September, so the date is 24 September 1717. The signature is "Ant. Ferd. Gonzaga" (Antonio Ferdinando Gonzaga, Duke of Guastalla); the correspondent is not named.

`transcription.txt` is the contributor's line-by-line transcription of the numbers and the clear parts, `decryption.txt` his line-by-line decryption, `key.tsv` the key with counts, `reading.md` (Italian) and `translation.md` (English) the reading by clause, and `contributor_readme.md` his notes (how it was read, the date, the names, what was searched).

## What it says

The correspondent's letter of the 15th brings news from the imperial court: Trautson has come back from his estates and Starhemberg and Trautson are expected the next week. The duke cannot answer until the correspondent says plainly whether the court has dropped its demand for a "lettera reversale", which would have the effect of the eleventh article of the declaration or a worse one, a silent abdication of his rights to which he will never agree. He will accept the land only in the form of the old investitures granted to the family's forebears, with no harm to himself or his heirs; its income is too small to justify any loss of those rights. The clear closing wishes the correspondent's son, "il Signor Contino", a return to health. Trautson and Starhemberg are the contributor's reading of names in the cipher, matched by him to ministers of the imperial court in 1717, a match he has not checked in print.

## The cipher

Letters are two-digit numbers in alphabet order from a = 30 to z = 67 (b = 25 is an exception; 32 two-digit values stand for letters, several letters having a twin, such as 37 and 77 for e and 30 and 70 for a, and the writer's 3 and 7 in the first digit are hard to tell apart, so the transcription writes 3). A word may end in one single digit for its last vowel (5 a, 6 e, 7 i, 8 o, 9 u). A few short numbers stand for whole words: 2 "che", 18 "non" and 1 "e" from context; about ten other code groups (10, 11, 12, 13, 14, 16, 20, 26, 92, 93) stay unread and probably stand for names and titles. `key.tsv` has every number.

## Remaining gaps

- Ten code groups (10, 11, 12, 13, 14, 16, 20, 26, 92, 93) unread or doubtful, probably names and titles; 92 93 before "per cui" may stand for the Emperor, a guess - blocker: open-codes; each occurs once to a few times and no text fixes it
- Doubtful passages marked [?] in the reading (page 1 line 15, page 3 line 4, page 4 line 9, and a few single words) - blocker: illegible; the shapes of 3 and 7 and some digits are ambiguous and only the sense chose between readings
- A human check of the transcription against the Estense scans - blocker: needs-physical-access; the scans are not reachable from the project and are licensed CC BY-NC-SA
- The papers of the recipient (not named), the Gonzaga of Guastalla in Parma and Mantua and the imperial archives in Vienna, where a draft or clear copy may survive - blocker: needs-physical-access; not searched by the contributor and not available to the project

## Escalation

- [x] siblings: the other 13 items in the same Campori folder and all four pages of the letter looked at by the contributor; none holds a clear copy, a key or a draft; the other two letters of catalogue 1569 use other ciphers
- [x] clear-pages: the clear opening and closing of the letter are the only clear parts; no decipherment stands on the sheets
- [x] known-keys: no earlier key for this correspondence is known to the contributor or the project
- [x] print: the contributor searched the ledger, two Campori catalogue searches (Guastalla 1716 to 1718, "cifrata" 1710 to 1725), names, and Affò's history of Guastalla vol. IV (1785), which tells the events but does not quote this letter; the recipients' papers and Vienna were not searched
- [x] key-rebuild: the key was found by the contributor's count-matching fit on Italian letter counts and settled by reading; a key from the first half alone agrees with the full key on 98.3% of the second half (his figure)
- [x] retry: the doubtful groups were retried by the contributor against the scan; the project did not retry them

## Files

| File | Content |
|---|---|
| `transcription.txt` | the numbers and the clear parts, line by line (contributor) |
| `decryption.txt` | line-by-line decryption (contributor) |
| `reading.md`, `translation.md` | Italian and English by clause (contributor) |
| `key.tsv` | the key with counts and notes (contributor) |
| `contributor_readme.md` | the contributor's notes |
| `VERIFICATION.md` | what the project re-checked |
| `profile.json` | the target profile |
