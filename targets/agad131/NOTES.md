# agad131: a letter from Wilno, 11 July 1757, on subsidies and the Strutyński affair (AGAD 1/338/0/1/131)

Status: read in part (10 Nov 2026). Contributed by Prabal Gupta (issue #331; repository `prabal-rje/branicki-1757`, folder `agad-131`, commit af80f5e, CC BY 4.0): a letter in clear Polish and French cipher, read with the key of letter 446 (target `branicki1757`) applied without change. Checked here against its own files only (`VERIFICATION.md`); the AGAD scans are not reachable from the project, so no transcription was compared with a scan here.

## The document

AGAD Warsaw, fonds 338, 1/338/0/1/131, five scans (https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28223838). Dated "D. 11. July 1757, z Wilna"; it ends "manu notus", with no name. Catalogue 1580 listed it among letters partly in cipher with no reading. The addressee is a patron in the Branicki circle (the contributor reads "His Excellency [?Branicki], Grand General of the Crown"); the writer is probably Matuszewicz, an inference of the contributor from letter 1398, which ends with the same memorial and is signed "Matusewic".

`transcription.txt` is the contributor's transcription, line by line (clear Polish in << >>, cipher letters as written, code numbers as digit groups), made by Claude Opus 5.5 and compared with a blind GPT-6.1 Sol pass (88% token agreement); `decryption.txt` the decryption under the 446 key; `key.tsv` the 24-letter key; `reading.md` (Polish and French) and `translation.md` (English) the reading; `contributor_readme.md` his notes.

## What it says

In the contributor's reading: the Castellan of Brest [?Abramowicz] and Count Pociej, Strażnik of Lithuania, ask His Excellency for protection and a subsidy for the coming Tribunal; beyond the French subsidy the Prince Grand General of Lithuania gave a thousand ducats, and their borrowing reached two hundred thousand francs; the Castellan asks support for a memorial of his nephew Ciechanowiecki, Starost of Opsa, to go to the French ambassador, the Count de L'Hôpital; Strutyński, Starost of Szakinów, came armed to the dietine at Brasław to kill a Ciechanowiecki, fled, and Field Marshal Apraksin stopped the Tribunal's case; rumours follow of a crime at [?St Petersburg] about 1730 and of a betrayal of King Stanisław at [?Danzig]. Konopczyński (1909, p. 216) and Matuszewicz's memoirs (vol. II, p. 237; vol. III, pp. 84, 136) tell the Strutyński affair but do not give this letter on those pages (contributor).

## The cipher

The key of letter 446 with no change: a reciprocal alphabet of twelve pairs (a-h, b-q, c-r, d-s, e-l, f-t, g-z, i-m, k-x, n-o, p-u, w-y) plus a number code; numbers from 830 up and the opening row of numbers act as punctuation or nulls. Value 580 is Pétersbourg; the contributor proposes 185 = Branicki and 275 = Dantzig (conjectures); 190 is open. A count-matching fit on this letter alone gives the same key for 97.7% of letter tokens (contributor's figure; the key scores -2.74 nats per letter under a French model against -3.42 to -3.50 for three shuffled controls, not repeated here).

## Remaining gaps

- Code group 190 and the proposed values 185 = Branicki and 275 = Dantzig, which are conjectures - blocker: open-codes; each occurs a few times and no text fixes it
- Three cipher signs, one before "de Russie" and two in the proposed "réponse", and the doubtful words and unread codes of the reading, 22 holes in 576 cipher words (measured 14 Nov 2026; the contributor had estimated about 25 of some 460) (Autres, Ce pourquoi, par de, massacre, cris/crimes, d'être entré, tous, marque; Pińsk, Szkultyn, Königsberg, Bruwen/Bouwen) - blocker: illegible; look-alike hand (c, e and r; n, o and u; g and q; w and y)
- About 300 transcription differences between the two passes (88% agreement on 2,514 tokens) not settled one by one on the scan - blocker: needs-physical-access; the scans are not reachable from the project
- Unit 83 (Beck, 1757) and the rest of the fonds, key sheet 1196, and the Radziwiłł and Branicki papers in other archives - blocker: needs-physical-access; not searched by the contributor and not available to the project

## Read share and state (14 Nov 2026)

Recount by Brice Dudout (PR #559, `VERIFICATION.md` section 4), checked at the integration: the French cipher passages of
`reading.md` give 576 words and 22 holes, 0.963 (own split of the paragraphs: 563 words, 22 holes, 0.962; the line
between Polish and French inside the "JMPan de [?Bruwen]" paragraph is drawn by hand); the whole file gives 895 words,
27 holes, 0.971. An own decoder from key.tsv gives 2,447 of 2,449 letters of decryption.txt (p4.14 and p4.17: capital X,
outside the key, given as K). The word share is above 0.95, but the letter stays **read in part** under the read bar's
other conditions: three cipher signs are unread and code 190 is open (not every letter read), and the about 300
differences between the two transcription passes have not been settled on the scans (the AGAD scans on
szukajwarchiwach are not reached from the project; blocker needs-physical-access above).

## Escalation

- [x] siblings: letters 446, 1398, 1399 and 1400 compared by the contributor for shared passages (none; they share titles); unit 83 and the rest of the fonds were not searched
- [x] clear-pages: the clear Polish of the letter is read with the cipher; no page is a decipherment
- [x] known-keys: the key of letter 446 applies unchanged
- [x] print: the contributor checked the ledger, Konopczyński (1909) and Matuszewicz's memoirs on the affair: not this letter; key sheet 1196 and other archives not checked
- [x] key-rebuild: a count-matching fit on this letter alone gives the 446 key for 97.7% of tokens (contributor)
- [x] retry: the contributor re-read the hard lines on enlarged images on 7 Nov 2026; the remaining look-alike signs stay doubtful

## Files

| File | Content |
|---|---|
| `transcription.txt` | the letter line by line (contributor) |
| `decryption.txt` | decryption under the 446 key, line by line (contributor) |
| `key.tsv` | the 24-letter key |
| `reading.md`, `translation.md` | Polish and French, and English (contributor) |
| `contributor_readme.md` | the contributor's notes |
| `VERIFICATION.md` | what the project re-checked |
| `profile.json` | the target profile |
