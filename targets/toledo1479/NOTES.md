# toledo1479: an unsigned cipher letter to Lorenzo de' Medici from the court of Castile, 31 August 1479 (ASF, MAP LXXII 171)

Status: read in part (10 Nov 2026). Contributed by Prabal Gupta (issue #332; repository `prabal-rje/branicki-1757`, folder `medici-1479`, commit af80f5e, CC BY 4.0): a letter "De Spagna" in a letter cipher with code numbers and nomenclator symbols for persons, read in part from the ciphertext, with the clear words between the cipher runs as cribs. Checked here against its own files only (`VERIFICATION.md`); the archive's images are not reachable from the project, so no transcription was compared with an image here. The contributor's folder was last updated on 8 Nov 2026 (the issue text says 668 of 730 letter positions, 91.5%; the folder at af80f5e says 663, 90.8%; this page uses the folder).

## The document

Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP), filza LXXII, doc. 171 (old c. 203); viewer https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=79510. Catalogue 2322 listed it as a bare cipher letter. The verso reads "Magnifico et generoso domino Lorenzo de' Medici ... Firenze", with the note "1479 / Di Spagna / a dì 31 d'agosto"; the recto ends "In Toledo a ⟨30⟩ di ⟨56⟩", with ⟨56⟩ an unread code group. The printed MAP inventory, vol. III (1957), p. 183, lists it as "Anonimo. (De Spagna, 1479 ago. 31), n. 171" with no content. The writer is not named. The archive serves the images at 1,272 by 1,848 pixels, so the cipher signs are 8 to 14 pixels high.

`transcription.txt` is the contributor's line-by-line transcription (36 lines and the verso, signs as letters and symbols, clear text in brackets), `decryption.txt` his word-by-word decryption with a status mask per letter, `key.tsv` the key, `codes.md` the code groups that stay unread, `reading.md` (Italian) and `translation.md` (English) the reading, and `contributor_readme.md` his notes.

## What it says

In the contributor's reading: the writer sent his last letter through a merchant's house at Seville; someone has concluded or will conclude a league "a difensione degli stati" ("for the defence of the states"); the parties show "sì poca fermeza"; someone will greet them warmly and fill them with fine words; in a passage naming Santiglana and Osma someone "mostra esere afezionato a V. M." and "ve ne potete fidare"; a brother, a code item, is the "chomandatore magore d'Alchantara" and a close friend of the writer; "con lei si farà l'acordo" (the queen); someone is betrothed to a person who is a code item; a legate came for a code item, who accepted "una decima a preti" and "tocha la metà". The links to the peace of Alcáçovas (4 Sept 1479) are the contributor's inference. No sentence of the cipher is whole.

## The cipher

One sign stands for one letter, mostly in letter-like shapes; two signs both write h; word division is kept and clear words stand between the cipher runs (`key.tsv`, 20 signs). Code numbers and nomenclator symbols (a Φ with two dots, a dotted square, a dotted circle, a dotted triangle ...) stand for persons and other words: 60 occurrences, none valued. This is not the key of the 1478 letters of the same filza (there a cross is a; here it is d). No key sheet is known.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/detail.py toledo1479` re-applies `key.tsv` to `transcription.txt` and compares the letters with `reading.md`: 93 of 201 compared words depart (46%), key covering 79% of the tokens. The reading was then checked by hand and with an own read-only snippet, line by line.

- **The key gives the reading.** `key.tsv` (20 signs) applied to the raw tokens of all 113 cipher items of `decryption.txt` gives the literal decode printed there in 113 of 113. With the italic clear text, the ⟨code⟩ items, the [bracketed] proposals and the (round-bracket) expansions set aside, the letters of `reading.md` are the letters of the decode in every line but one.
- **Cause D, clear text of the manuscript (most of the 93 words).** The phrases the key does not produce ("a la fama che", "ma che modo a chostoro ano", "e tanto che sola potuto fuggire" ...) are the clear hand between the cipher runs: in [ ] in `transcription.txt`, in italics in `reading.md` (about 300 words). The audit drops the bracketed clear text from the transcription and so finds these words only in the reading. No code number or nomenclator symbol is given a value anywhere: all 60 stay ⟨..⟩.
- **Cause F, audit artefacts.** The script reads the key line for the sign `#` (h) as a comment and splits tokens on `+`, so the cross (d, 37 positions) is lost ("aifensione" for "a difensione"); it decodes the digits 3 and 6 inside code numbers as the letter signs 3 (r) and 6 (s), and the symbol P as the sign p (z).
- **Cause C, declared conventions.** Word division, accents, apostrophes and capitals are added; letters not written are in round brackets as the header of `reading.md` says: d(i) eight times (one of them in d(i)sposata), no(n), franc(o).
- **Cause B, one letter.** L24.4: the signs give `elegatochecera`; `decryption.txt` (reading column) and `reading.md` print "El legato che c'era", with a second l that has no sign and no mark. Elsewhere the reading keeps single consonants as written (fratelo, deto, acetato, tuto). Not changed here.
- **Cause E, the clear hand in two states.** The clear text in `reading.md` is not the clear text of `transcription.txt` in 16 of 36 lines: mostly words of the transcription replaced by "..." (L03 "a vr bon", L06 "stallono?"), but also other readings, e.g. L08 "10" against "18?", L13 "e degli? bra magnificenza imbasc..?" against "e di già? V. M. intenderà?", L30 "[clear]" against "ora ... Napole? ... e gli verranno?", L31 "nischono?" against "ne sono?". Both files call the clear hand provisional.

Nothing was changed in the key, the transcription or the reading; no value was missing from `key.tsv`. After: 93 of 201, unchanged, since the departures are the manuscript's clear text and artefacts of the script. Not checked: any sign against an image. Elsewhere in these notes the key is called "20 signs" (The cipher) and "the 19-sign key" (Escalation); the file has 20 signs for 19 letters.

**Marked on 16 Nov 2026.** One place in `reading.md`: L24 "El legato" is now "El (l)egato", in the file's own convention (its header: round brackets expand letters not written). No letter and no header line changed. The reading column of `decryption.txt` (L24.4, "el legato che c'era") and `translation.md` were left as the contributor gave them. The differing states of the clear hand (cause E) were not touched. `research/reading_audit/v2_score.py reading.md it`: hole rate 0.173 before and after. The page `docs/toledo1479.html` was not changed: no statement on it was found false.

## Remaining gaps

- About 60 code numbers and nomenclator symbols for persons and other words (listed in `codes.md`) - blocker: open-codes; each occurs one to six times and no text fixes them
- 21 doubtful and 4 open cipher words, 43 unsettled letter positions in seven spans (lines 4, 8, 12, 13, 22 and 29; across the whole cipher 47 positions are doubtful and 20 open), and the clear hand of lines 19-20, 28 and 33-35 - blocker: illegible; the images are 1,272 by 1,848 pixels and the signs 8 to 14 pixels high, so sharper photographs are needed
- A human check of the transcription against the archive's images (the contributor's was an AI's re-read) - blocker: needs-physical-access; the images are not reachable from the project
- Rubinstein's edition, *Lettere di Lorenzo de' Medici* vols. III and IV (notes citing letters Lorenzo received), and studies of Florentines in Castile 1478-80 - blocker: needs-physical-access; not checked by the contributor and not available to the project

## Escalation

- [x] siblings: the contributor notes that the key differs from that of the 1478 letters of the same filza (a cross is a there and d here); the other letters of the filza were not read for this target
- [x] clear-pages: the clear words between the cipher runs were used as cribs; the clear closing and heading are partly read
- [x] known-keys: no key sheet of this cipher is known; the 1478 key does not apply
- [x] print: the contributor searched the printed MAP inventory, the ledger and the web; Rubinstein's edition and studies of Florentines in Castile were not checked
- [x] key-rebuild: the 19-sign key was found from the cipher with the clear words as cribs and re-read against the images (contributor)
- [x] retry: the doubtful signs were re-read against the images by the contributor; further progress needs sharper photographs

## Files

| File | Content |
|---|---|
| `transcription.txt` | the signs and the clear parts, line by line (contributor) |
| `decryption.txt` | each cipher word, its literal decode, status and reading (contributor) |
| `key.tsv` | the key with the words that fix each value (contributor) |
| `codes.md` | the code groups and symbols that stay unread (contributor) |
| `reading.md`, `translation.md` | Italian and English (contributor) |
| `contributor_readme.md` | the contributor's notes |
| `VERIFICATION.md` | what the project re-checked |
| `profile.json` | the target profile |
