# Carranza's cipher telegrams, May and June 1915

Ten telegrams of Venustiano Carranza's headquarters at Veracruz, in the war against Villa. They carry orders to generals and buying agents, for ammunition, money and rifles.

- **Where:** CEHM-Carso, Mexico City, Fondo CDLXXX, items 1.17.1, 1.22.1, 1.23.1, 1.24.1, 1.29.1, 1.32.1, 1.33.1, 1.39.1, 1.40.1 and 1.42.1.
- **Scans:** the CEHM catalogue, for example https://www.cehm.org.mx/Buscador/FichaBasica/38647?Tipo=A
- **Ledger:** catalogue 1464 at https://github.com/dbourdeau/cyphersolver lists these telegrams as open.

## What they say

- **To Obregón, Estación Trinidad, 17 May.** The line is being reinforced as far as Apam. New ammunition will take four or five days, so the convoy at Apam is to go on.
- **To Pablo González, Apizaco, 9 June.** A general who left that afternoon brings a million pesos in small bills.
- **To Nuevo Laredo, 17 May.** Ten thousand dollars go to the customs administrator for General Dávila. Two hundred thousand 7 mm cartridges and two hundred thousand .30-30 leave New York that day.
- **To Elías, New York, 9 June, very urgent.** Buy the nine hundred and fifteen Lee rifles and their ammunition as well, for shipment on the next day's steamer.
- **To Arredondo, Washington, 9 June.** Ask whether the American government will allow repairs to the steamer "Progreso" in New York.
- **To Sáenz, to Arredondo on 17 May, and to Denegri.** Shorter messages on family, a payment to the consul in Havana, and supplies.

Read them: [Spanish](reading.md), [English](translation.md).

## The keys

**Number telegrams.** Each number stands for one letter. The numbers 1-26, 27-52, 53-78 and 79-104 each run through the alphabet, each from its own start.

| Telegrams | 1-26 starts at | 27-52 starts at | 53-78 starts at | 79-104 starts at |
| --- | --- | --- | --- | --- |
| 1.17.1, 1.22.1, 1.23.1 | Y | U | A | Q |
| 1.24.1, 1.33.1 | Q | G | Q | K |
| 1.42.1 | W | G | E | M |

**Letter telegrams.** Thirteen pairs of letters swap. The clear word "lunes" or "miércoles" stands before the coded text. Those are the true weekdays of 17 May and 9 June 1915, so I take the word to name the day's table. That is my inference. `key.tsv` gives the pairs.

## How it was read

From the ciphertext alone, with no key sheet and no sibling decipherment.

Bespoke count matching based on Spanish next-letter counts opened the number telegrams. On the largest set (758 tokens) it gets 65% to 77% of tokens right on its own, over six runs. On the 199-token Obregón set it gets 35%. Those readable fragments gave the plan of the key. The letter telegrams came from a one-to-one solve on Spanish, then a reading of its output.

- **Transcription:** two passes agree on 99.2% of 1,292 tokens. The numbers are typed and clear. I checked sample pages on the scan, not every difference.
- **Score:** a four-start search gives -2.61 per letter on the Nuevo Laredo set and -2.26 on the Obregón set. Shuffled numbers give -5.7 to -5.9.
- **Held-out:** a key fitted on 1.17.1 alone reads 1.22.1 and 1.23.1. A key fitted on 1.24.1 alone reads 1.33.1.
- **Blind read:** a reader with no context named two shuffled strings as noise. It named the other four as Spanish, with the same gist as this reading.
- **Straight from the key:** 1,013 of the 1,050 number tokens (96.5%) give the reading's letter as typed. The others are mostly the clerk's own slips and overstruck digits, repaired by sense. `decryption.txt` keeps the letters as typed.

## Earlier work

**The key family may already be in print.** The ledger notes that Constitutionalist keys are known in print, and it names Ángel and Morales-Luna 2008 and Narváez 2025. It also notes key sheets in CEHM fondo XXI.

I did not reach the two likeliest places:

- Narváez, "Some Cryptographic Cases of the Constitutionalist Movement, 1914-1915", *Historia Mexicana* 75/2 (2025)
- Narváez, *Criptografía diplomática, política y militar en México (1813-1926)* (2019)

So these readings may already be in print. Someone with a copy should check both.

**Checked:**

- The ledger's catalogue, target folders and issues, live on 7 November 2026.
- Both sides of all ten sheets, and their CEHM cards. No clear copy or decipherment turned up.
- CEHM searches by name and shelf term, in part.

**Not checked:**

- The rest of CEHM fondo XXI, and the addressees' papers.
- Obregón's *Ocho mil kilómetros en campaña* (1917).
- Mexican state archives with no online images.

## What stays open

- **1.32.1, to Denegri, is the weakest reading.** It rests on 21 letters, and one sign that looks like ñ stands where t is needed.
- **The general in 1.42.1.** "Cosío Rovelo" is my guess at the name.
- **A short run at the end of the first page of 1.22.1** stays unsettled.

The cipher ledger confirmed that the key decodes the number telegrams to Spanish (issue #321). It holds its page until someone checks Narváez's 2025 article and 2019 book for the same tables.

## Files

- `reading.md`: the telegrams in Spanish, with coded text in capitals
- `translation.md`: the telegrams in English
- `transcription.txt`: the numbers, letters and clear words, as typed
- `decryption.txt`: the letter-for-letter decryption
- `key.tsv`: the keys

© 2026 Prabal Gupta. First published here, 7 November 2026. Released under CC BY 4.0: reuse it, and credit me.
