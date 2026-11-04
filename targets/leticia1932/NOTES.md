# Jefatura civil y militar del Amazonas: cipher telegrams of the Leticia crisis, Sept 1932 (catalogue 1526)

Status: read in part (Brice Dudout, 4 Nov 2026; the alphabetic telegrams are read, 787 cipher words, 99.5%; the numeric telegram No. 143, f. 151, is open).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, building on Daniel Bourdeau's vetting of 28 Oct 2026:
he transcribed the key (`research/latam_vetting/1526_key_garv114.tsv`) and read ff. 149 and 153 first (`1526_sample.txt`). Not
published on the site. Text only: the DataViva images carry no explicit licence and are not reproduced.

## Documents

AGN Colombia, Archivos Privados, Fondo General Amadeo Rodríguez Vergara, Asuntos militares, CO.AGN.AP.GARV..2.2.4, ff. 85-177
(DataViva 68e57156a1660dc4d1aa35ed). Seventeen cipher telegrams read here (copies counted once), Bogotá <-> Puerto Asís,
9-27 Sept 1932. Cipher telegrams between the Ministry of War in Bogotá and Gen. Amadeo Rodríguez Vergara, civil and military chief of the Amazonas, at Puerto Asís, 9-27 September 1932, the first weeks after the Peruvian seizure of Leticia (1 Sept 1932): ammunition from Bofors, the gunboats Cartagena, Santa Marta and Barranquilla, the state of the troops (499 men, corrected to 599), the move to Caucayá, the passage of Güepí, the Napo and the risk of a conflict with Ecuador, Peruvian reinforcements to Loreto, censorship of soldiers' letters.

Five of them have a contemporary clear text in the same file (f. 117 for No. 57, image Folio_127Recto for No. 83, f. 137 for
No. 110, f. 139 for No. 12599, f. 157 for No. 12.441) and f. 141 carries a pencil gloss of its last sentence: for those, this is a
verification of the period decipherment, not a new reading. The other eleven have no decipherment in the file.

## System and key

Sección I key of 31 Jan 1931 (GARV..1.1.4 f. 44r; rules f. 43r): seven simple-substitution alphabets, one per weekday, vowels to
vowels; day name and D (forwards) or R (reversed) in clear at the head. All telegrams seen are D. f. 134 is headed "Martes D" but
enciphered with the Lunes alphabet; ff. 109, 141, 170 have no heading (Lunes, Lunes, Martes). Many keying or transmission slips
(b/h, i/e/a, dropped letters). `key_garv114_f44.tsv` is Daniel's transcription, confirmed independently.

## Validation

`validation.txt`: one pre-registered measurement on a held-out telegram (No. 82, 661 letters): characters 0.977, words 0.854,
against 0.381 / 0.039 for the best of 200 permuted keys.

## Reading

`transcription.txt` (all telegrams, in order), `decryption.txt` (mechanical, per telegram), `reading.md` (Spanish, marked, with
the count per telegram), `translation.md` (English). 787 cipher words: 759 certain, 24 probable, 4 unresolved = 99.5%.
f. 138 was transcribed for this pull request; the other transcriptions date from the reading session.

## Remaining gaps

- f. 151, telegram No. 143 (Lt-Col. Paz, 25 Sept 1932), about 160 numbers 1-181 in another (numeric) system - blocker: no-key-material; the 1931 day key does not apply and no key for it is in hand; candidate: the Presidency key, GARV..2.2.1 ff. 6v, 8, 10 (not yet fetched or tested).
- Four unresolved words (zeffe f. 107, pascama f. 153, hsla f. 159, gixhtlo f. 170); f. 153 does not fully construe around "relator ... yo" - blocker: illegible; keying slips, f. 159 to re-read at full resolution.

Also open, not blocking: the clear words of most telegrams were left out of the transcriptions (the reading gives the cipher
parts), and the historiography of the Colombia-Peru war has not been searched beyond the catalogue's searches of 3 Nov.

## Escalation

- [x] siblings: the file's other telegrams were read; GARV..2.3.1, 2.3.2, 2.4.1 ("con traducción") not opened.
- [x] clear-pages: five contemporary clear texts in the file used as checks (ff. 117, 127, 137, 139, 157; gloss f. 141).
- [x] known-keys: the Sección I key of 1931 (GARV..1.1.4 f. 44r) is the key and was applied.
- [x] print: no edition or study of these telegrams found (catalogue, 3 Nov 2026).
- [n/a] key-rebuild: not needed for the alphabetic system; f. 151 would need the Presidency key first.
- [x] retry: every unresolved or probable word re-decoded with the frozen key and regraded (notes in reading.md); f. 151 is outside this key.

## Prior work

Daniel Bourdeau: key and sample reading (above); catalogue verdict "open" ("key lookup"). No publication found (catalogue, 3 Nov
2026: DECODE, Cryptiana, Lasry, FRUS 1932 vol. V, web searches). Contemporary clear texts for five telegrams, as listed.
