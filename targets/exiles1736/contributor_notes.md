# AGAD 1401: a Polish letter on Stanisław's abdication, 4 February [?1736]

An unsigned letter in Polish and Latin, written among the Polish exiles in Prussia. France has told them that it can no longer keep King Stanisław Leszczyński on the Polish throne.

- **Where:** AGAD Warsaw, fonds 338, reference code 1/338/0/1/1401.
- **Scans:** https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28225114
- **Ledger:** catalogue 1579 at https://github.com/dbourdeau/cyphersolver leaves this letter open. Its 1398, 1399 and 1400 are the French letters in this repo. This letter uses a different cipher.

## What it says

- France has agreed preliminary articles with Vienna, and an armistice. It says that it cannot keep Stanisław on the Polish throne.
- A courier, Orlik, brings this as happy news. The exiles receive it in despair.
- The exiles answer with two conditions. Europe must first recognize Stanisław as lawful King of Poland for life. Then Stanisław must call a Diet, use the royal rights there, and only then abdicate.
- A second courier leaves Versailles on 11 January. The reply says that Du Theil has gone to Vienna with these articles, and that Stanisław must abdicate at once.
- Stanisław presses for the abdication. The confederated estates refuse, and they ask for some weeks to deliberate.
- Two lords leave for Warsaw, with passports from Keyserling, the Russian envoy.
- The writer asks the addressee what the Turkish power and the Khan plan.

Read it: [Polish and Latin](reading.md), [English](translation.md).

## The cipher

One number stands for one letter, with a dash between words. `key.tsv` gives all 30 letter signs. Code groups are written without dots, and they stand for names. This is a different cipher from the French letters, with its own key.

| Code group | Reading | Evidence |
| --- | --- | --- |
| 125 | Stanisław | 12 uses, and every one fits King Stanisław. He abdicated in January 1736. |
| 455 | August | 2 uses: his reign begins only after the abdication. |
| 136, 142 | Warszawa | The clear text beside them names Warszawa twice. |
| 675 | [?Monti] | A guess. The text calls 675 the minister named to the confederated estates. I found no text that names Monti so in 1736. |

Two undotted groups are not code. In the letter key, 435 is 4.3.5, "ham", and 4345 is 4.3.45, "han". Both are the Khan, in the passage on the Tatars. Each splits into key numbers in one way only.

These stay unread: 145, 156, 175, 195, 289, 505, 613, 715 and 5455. `../branicki1757/numbers.md` (the groups of letter 1401 are listed there) lists what I tried on each.

## How it was read

From the ciphertext alone, with no other letter, key or crib.

Bespoke count matching based on Polish next-letter counts deciphered 98.2% of letter tokens, on this letter alone. It misses only rare signs. Reading the numbers against the Polish gives the same values, and settles those signs.

- **Transcription:** two passes agree on 99.1% of 2,844 tokens. Each of the 23 differences was settled on the scan. A later check on the scan split one more group: in row p7.19, "5 - 79" is two words, not "5.79".
- **Score:** the key scores -3.52 per letter under a Polish model. Three shuffled controls score -4.70 to -4.86.
- **Solver:** a solver on that model agrees with the key on 93.1% of tokens.
- **Blind read:** a reader with no context named this text as Polish with Latin, and it named three controls as noise. It translated about 85% of the clauses.

Limits of these checks:

- The Polish model comes from 19th-century and 20th-century text, and the letter has long Latin stretches. So a wrong key can outscore the true one: the solver's key scores -3.07.
- I changed the model once after a first look, because runs of one letter were winning. The margin over the controls was 1.11 before that change and 1.19 after.
- I ran no held-out half. A short solve on half the text fell into a degenerate key, which says nothing about the split.

## The date

The date line reads "D. 4. Feb:", and the year's third digit looks like 2. The contents fix 1736: the preliminaries of Vienna, and a courier sent on 11 January. That year is my inference.

## The addressee

The catalogue card says that the letter is perhaps to Branicka. The text addresses a man, and it asks what the Turkish power plans. So the card looks wrong to me. The signature is a flourish that I cannot read.

## Earlier work

As far as I checked, nobody has read this letter. That is not proof that nobody has.

**Checked:**

- The ledger's catalogue, target folders and issues, live on 7 November 2026.
- The card and scans of this letter, and the cards of 1397, 1402 and 1403. No clear copy or decipherment of this text turned up.
- A text comparison with letters 446, 1398, 1399 and 1400. They share only stray phrases.
- A keyword scan of Konopczyński 1909, and one web search on the names.

**Not checked:**

- The rest of the Branicka fonds, unit by unit.
- Other archives that hold the exiles' papers of 1736.
- Printed editions of the 1733-1736 correspondence.

## Status

The reading marks the cipher in bold. The cipher parts hold 530 words, and 518 read, 97.7%. The 12 holes are nine open code groups, two uses of [?Monti], and "cza[s]", which the writer wrote with 12 for 21.

The clear parts are a working reading, not an edition. No historian has checked this reading yet.

## Files

- `reading.md`: the letter in Polish and Latin
- `translation.md`: the letter in English
- `transcription.txt`: the numbers and the clear parts, line by line
- `decryption.txt`: the decryption, line by line
- `key.tsv`: the letter key

© 2026 Prabal Gupta. First published here, 7 November 2026. Released under CC BY 4.0: reuse it, and credit me.
