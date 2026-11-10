# Toledo, 1479: a cipher letter to Lorenzo de' Medici

An unsigned letter to Lorenzo de' Medici from the court of Castile, partly in cipher. It is read in part.

- **Where:** Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 171 (old c. 203).
- **Scans:** the archive's viewer, https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=79510
- **Address and date:** the verso reads "Magnifico et generoso domino Lorenzo de' Medici ... Firenze", with the note "1479 / Di Spagna / a dì 31 d'agosto". The letter ends "In Toledo a ⟨30⟩ di ⟨56⟩", where ⟨56⟩ is an unread code group.
- **Ledger:** catalogue 2322 at https://github.com/dbourdeau/cyphersolver lists it as a bare cipher letter, not yet attempted.

## What it says

Code numbers and symbols hide most persons. They are shown here as ⟨code⟩. No sentence of the cipher is whole yet.

- The writer sent his last letter through a merchant's house at Seville.
- ⟨code⟩ has concluded, or will conclude, a league ("lega") "a difensione degli stati": for the defence of the states.
- Some parties show "sì poca fermeza": so little firmness.
- "farà loro buona cera e gl'enpierà di buone parole": someone will greet them warmly and fill them with fine words. The subject is not written.
- In a passage that names Santiglana and Osma, someone "mostra esere afezionato a V. M.": he shows himself devoted to Your Magnificence. The writer adds: "ve ne potete fidare", you can trust him.
- A brother of his, ⟨code⟩, is the "chomandatore magore d'Alchantara", the comendador mayor of Alcántara. He is "molto mio amico", a very close friend of the writer.
- With the queen, "con lei si farà l'acordo": an agreement will be made. Someone "è d(i)sposata", is married or betrothed, to ⟨code⟩ of ⟨code⟩. The word is not secure.
- A legate had come on behalf of ⟨code⟩. ⟨code⟩ has accepted "una decima a preti", a tithe on the clergy, and ⟨code⟩ "tocha la metà", receives half.
- "visto il pocho amore che è tra loro": seeing the little affection between them.

Read it: [Italian](reading.md), [English](translation.md).

**Context.** In 1479 Florence was at war with the Pope and the King of Naples, after the Pazzi conspiracy of 1478. Castile and Portugal made peace at Alcáçovas on 4 September 1479. Queen Isabella had negotiated it with Beatriz of Portugal, and the treaty arranged royal betrothals. The letter names neither event in clear. The link is my inference.

## The key

- One sign stands for each letter, mostly in letter-like shapes. Two signs both write h.
- Word division is kept. Clear words stand between the cipher runs.
- Code numbers and nomenclator symbols, such as a Φ with two dots, stand for persons and other words. They stay unread: 60 occurrences, listed in `codes.md`.
- `key.tsv` gives the values and the words that fix them.

I worked with AI models. They transcribed the signs from the archive's images and found the key from the cipher alone, with the clear words as cribs. Then they re-read every doubtful sign against the images, and kept one value for each sign. No key sheet of this cipher is known.

## Checks

- **Independent review:** a second AI model checked every changed reading against the key and the images. It found no reading that the signs contradict. Its points of doubt are applied below and in the files.

- **Extent, by words:** of 113 cipher words, 88 are read in full (77.9%), 21 hold a doubtful letter, and 4 are open. The 60 code items for persons and other words are not read.
- **Extent, by letters:** of 730 letter positions in the cipher, 663 are read (90.8%), 47 are doubtful (6.4%) and 20 are open (2.7%).
- **Word-list control:** under the key, 65.3% of the cipher's letter positions fall in words of a 15th-century Italian word list. 200 shuffled keys give 1.9% on average, and 11.4% at most.
- **Blind check, first stage:** a reader that saw only the early decode agreed with 30 of its 31 read words, and contradicted none.
- **Method check:** Italian test texts of the same shape, with 5% of the signs misread, read at 98.5% to 99.8%.

## What stays open

- Seven spans hold 43 unsettled positions, in lines 4, 8, 12, 13, 22 and 29.
- The clear hand in lines 19–20, 28 and 33–35 is only partly read.
- No coded person is identified, and the writer is not named.
- The archive serves the images at 1,272 by 1,848 pixels, so the cipher signs are only 8 to 14 pixels high. Sharper photographs should settle most doubtful signs.

## Earlier work

As far as I checked, nobody has published a reading of this letter. That is not proof that nobody has.

**Checked:**

- the printed inventory, *Archivio mediceo avanti il Principato. Inventario*, vol. III (1957), p. 183. It lists "Anonimo. (De Spagna, 1479 ago. 31), n. 171", with no content, and it does not mark the cipher;
- the ledger, live on 8 November 2026;
- web searches for the shelfmark and for the content.

**Not checked:**

- *Lettere di Lorenzo de' Medici*, vols. III and IV, ed. Nicolai Rubinstein. Their notes cite letters that Lorenzo received. Someone with these volumes should check them for this letter.
- Studies of Florentines in Castile in 1478 to 1480.

## Status

Read in part: 88 of 113 cipher words (77.9%), and 90.8% of the cipher's letter positions. About 60 code items stay unread. That is below the ledger's bar for a complete reading.

## Files

- `reading.md`: the letter in Italian, with doubts and gaps marked
- `translation.md`: the letter in English
- `transcription.txt`: the signs and the clear parts, line by line
- `decryption.txt`: each cipher word, its literal decode and its reading
- `key.tsv`: the key
- `codes.md`: the code groups and symbols that stay unread

© 2026 Prabal Gupta. First published here, 8 November 2026. Released under CC BY 4.0: reuse it, and credit me.
