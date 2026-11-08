# gonzaga1542: Charles V to Ferrante Gonzaga, viceroy of Sicily, Monzón, 11 August 1542

Status: read (7 Nov 2026, refreshed from the contributor's repository at commit f465095). Contributed by Prabal Gupta (issue #318; repository `prabal-rje/branicki-1757`, folder `charles-v-1542`, CC BY 4.0): a cipher of consonant signs with a small digit above each that adds the vowel, found from the sign statistics of the letter alone and read as Spanish. Checked here against its own files only (`VERIFICATION.md`); the Estense scans are not reachable from the project, so no transcription was compared with a scan here. The contributor checked the transcription on the scans at full size on 7 Nov 2026 and settled the doubtful places (`doubtful_places.md`).

## The document

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. IV, cc. 109-110 (Lodovico Media Library record c710a32c-42a7-4159-8abc-472aed58f7c9; scans licensed CC BY-NC-SA, not copied here). Catalogue 1560 (the other leaf of that entry, the undated cipher letter at cc. 131-132, is a different matter and stays in the catalogue). A letter of the Emperor, signed "Yo el Rey" and countersigned "Idiáquez", to Ferrante Gonzaga, Prince of Molfetta, as viceroy of Sicily (the catalogue's "governor of Milan" is his office from 1546); the back gives the address and marks this copy as the duplicate. Part of it is in clear Spanish: the heading, the opening, the closing and several links between the cipher passages. The cipher fills most of the body.

`reading.md` and `translation.md` are the contributor's, with the cipher in bold; `transcription.txt` the cipher as written with the clear text between double angle brackets (the sign shapes are given by labels, a label names a shape and not a value), `decryption.txt` the line-by-line decryption, `key.tsv` the table with the count of uses of each sign, `doubtful_places.md` every place where the reading leaves the key, `contributor_notes.md` the contributor's own notes (how it was solved, the check against Capasso, what stays open).

## What it says

Sicily cannot pay for its infantry, its galleys and the fort of La Goleta without help; the Emperor's other kingdoms are as short, so no help can come; La Goleta must be provided for because of the Turkish fleet; the spies report that the main French effort is coming to the frontier of Perpignan and that the French threaten Navarre; the pay of the Count of Anguillara (Virginio Orsini) and of the Viscount Cicala for his galleys must be paid, because Cicala is being solicited for another contract.

## The cipher

A base sign is a consonant and a small digit above it adds the vowel (1 to 5 and 6 to 0 both run a, e, i, o, u); a sign with no digit is a single letter; a further sign marks a doubled or palatal consonant; two shapes are nulls. See `key.tsv`.

## What the reading rests on beyond the key

`decryption.txt` is `key.tsv` applied to `transcription.txt` (checked here on all 31 cipher lines, VERIFICATION.md). The reading leaves the key at the places listed in `doubtful_places.md`; most of them are the clear misspellings of a writer or a syllable written twice. The name "Anguillara" comes from the string "lannuilara" with one sign differing, and is supported by Capasso, "Il governo di Don Ferrante Gonzaga in Sicilia", Archivio Storico Siciliano n.s. 31 (1906), pp. 387 and 409, read by the contributor in the Internet Archive text (the project did not open it). One value rests on its four uses: g with the digit 6 gives "ha" (all four in "haver"); without it the reading would have 10 holes.

## Remaining gaps

- Six words marked in the reading ([g]randes, [?allí], t[a]n, e[x]pedientes, [?screbir], amena[ça]van): a letter or a syllable left out or a wrong sign by the writer, and the Duplicada day [?xj] - blocker: illegible; the scan shows no sign for the missing letter, or a blot
- A human check of the transcription against the Estense scans, and the chancery's clear draft that may survive in a Spanish archive - blocker: needs-physical-access; the Lodovico Media Library is not reachable from the project and the images may not be redistributed

## Escalation

- [x] siblings: the other Karl V to Gonzaga letters of the same file (1549, 1552) have their own decipherments and signs (`gonzaga1549`); this letter's cipher is a different system, so none applies
- [x] clear-pages: the clear passages of the letter read and compared with the cipher around them (Goleta, Perpiñán, Cigala); none is a decipherment of the cipher
- [x] known-keys: not the 1548 numeric key; the contributor searched the family of keys of the file; no other key for 1542 is known
- [x] print: the contributor found no printed copy of the letter, and checked its content against Capasso (1906); the project did not search further
- [x] key-rebuild: the table was found by a solver on a Spanish letter model from the sign statistics of the letter alone and repeated from six starts; the contributor then read every place where the reading leaves the key (doubtful_places.md)
- [x] retry: every doubtful place was retried by the contributor on the scans at full size, enlarged two to four times; the two signs missing at line ends were added and settled "que es solicitado" and "que sucediesse"; the project did not retry them
