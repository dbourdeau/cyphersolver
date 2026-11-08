# Guastalla, 24 September 1717: the duke refuses a "lettera reversale"

A letter partly in cipher from Antonio Ferdinando Gonzaga, Duke of Guastalla, to a correspondent who is not named. The Emperor's court offers the duke a grant of land, on condition that the duke gives up older claims. The duke refuses that condition.

- **Where:** Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera A, "Antonio Ferdinando, duca di Guastalla", cc. 15-16.
- **Scans:** https://lodovico.medialibrary.it/media/schedadl.aspx?id=848189d6-1008-497b-bcde-0e3a3ad9757f
- **Ledger:** catalogue 1569 at https://github.com/dbourdeau/cyphersolver lists this letter as open, together with two other Campori letters (1612 and 1725). This folder covers only the Guastalla letter.

## What it says

- The correspondent's letter of the 15th brings news from the imperial court. Trautson has come back from the country, and Starhemberg and Trautson are expected the next week.
- The duke cannot answer until the correspondent says plainly whether the court has dropped its demand for a "lettera reversale".
- That letter would have the same effect as the eleventh article of the declaration, or a worse one. It would be a silent abdication of the duke's rights, and the duke will never agree to it.
- The duke will accept the land only in the form of the old investitures granted to the family's forebears, with no harm to the duke or the duke's heirs.
- The income of the land is too small to justify any loss of those rights.
- The clear closing wishes the correspondent's son, "il Signor Contino", a return to health.

Read it: [Italian](reading.md), [English](translation.md).

## The cipher

- Most letters are two-digit numbers in alphabet order, from a = 30 to z = 67. The letter b = 25 is an exception.
- A word may end in one single digit for its last vowel: 5 a, 6 e, 7 i, 8 o, 9 u.
- A few short numbers stand for whole words. From context, 2 is "che", 18 is "non" and 1 is "e". About ten other code numbers stay unread. They probably stand for names and titles.

`key.tsv` gives every number.

## How it was read

From the ciphertext alone, with no other letter, key or crib.

Bespoke count matching and a bespoke fit, both based on Italian letter counts, found the key.

- **Transcription:** two passes agree on 92.0% of 3,064 digits. One pass had read the writer's 3 and 7 the other way round on two pages, and that was corrected first. Every difference was settled on the scan. In 22 places, the sense of the text chose between two shapes.
- **Score:** the key scores -2.04 nats per letter under an Italian model. Three shuffled copies of the text, each put through the same fit, score -3.69 to -3.75.
- **Held-out half:** a key found from the first half alone agrees with the full key on 98.3% of the second half.
- **Blind read:** a reader with no context called the text "Italian, virtually certain", and it called two shuffled controls noise. It translated about 85% of the sense, with the same gist.

One limit: in the first digit of a pair, the writer's 3 and 7 are hard to tell apart. Where the two passes disagreed there, the transcription writes 3. The key gives each 3x pair and its 7x twin the same letter, so this loses no reading. But it is a convention, not a fact of the scan.

## The date

The dateline reads "Guastalla 24 7bre 1717". In letters of this time, "7bre" means September. The catalogue gives 24 July 1717.

Ireneo Affò's history of Guastalla (vol. IV, 1785) tells of talks that led to an imperial draft of January 1718. That fits the September date.

## The names

- "Trauston" and "Starhemberg" read as names in the cipher. They match ministers at the imperial court in 1717: Prince Trautson and a Count Starhemberg. I have not checked this in print.
- The code pair 92 93, before "per cui", may stand for the Emperor. That is a guess.

## Earlier work

As far as I checked, nobody has read this letter. That is not proof that nobody has.

**Checked:**

- The ledger's catalogue, target folders and issues, live on 7 November 2026.
- All four pages of the letter, and the 13 other items in the same folder. None holds a clear copy, a key or a draft of this letter.
- Two catalogue searches: Campori records from Guastalla in 1716 to 1718, and Campori records marked "cifrata" from 1710 to 1725.
- Searches by name, and Affò's history, vol. IV. Affò tells the events, but does not quote or decipher this letter.

**Not checked:**

- The papers of the recipient, who is not named.
- The papers of the Gonzaga of Guastalla in Parma and Mantua, and the imperial archives in Vienna. A draft or a clear copy may survive there.

## Status

The cipher part reads as sense, apart from about ten code groups and a few doubtful passages. The reading marks each one.

The reading is with the cipher ledger as issue #329: https://github.com/dbourdeau/cyphersolver/issues/329

## Files

- `reading.md`: the letter in Italian
- `translation.md`: the letter in English
- `transcription.txt`: the numbers and the clear parts, line by line
- `decryption.txt`: the decryption, line by line
- `key.tsv`: the key

© 2026 Prabal Gupta. First published here, 7 November 2026. Released under CC BY 4.0: reuse it, and credit me.
