# carranza1915: Carranza's coded telegrams from Veracruz, May and June 1915 (CEHM-Carso Fondo CDLXXX 1.17.1 to 1.42.1)

Status: read (8 Nov 2026). Contributed by Prabal Gupta (issue #321; repository `prabal-rje/branicki-1757`, folder `carranza-1915`, commit af80f5e, CC BY 4.0): ten telegrams of Venustiano Carranza's headquarters at Veracruz, six in a number cipher and four in a letter-pair cipher, read from the ciphertext alone. Checked here against its own files only (`VERIFICATION.md`); the CEHM scans are not reachable from the project, so no transcription was compared with a scan here. **Priority is open:** the key family may already be in print. The contributor, in a later comment on issue #321 (8 Nov 2026; his `contributor_readme.md` predates it and says he had not reached Narváez), checked Narváez's 2025 article in `Historia Mexicana` 75/2 in full, including the figure images, and reports that it does not print these tables and does not decipher these telegrams (it prints other Constitutionalist tables, including reciprocal letter alphabets); Narváez's 2019 book *Criptografía diplomática, política y militar en México (1813-1926)*, Ángel and Morales-Luna (2008), the CEHM fondo XXI key sheets and Obregón's *Ocho mil kilómetros en campaña* were not checked.

## The documents

CEHM-Carso, Mexico City, Fondo CDLXXX (Miscelánea de documentos sobre Venustiano Carranza), items CDLXXX.1.17.1, 1.22.1, 1.23.1, 1.24.1, 1.29.1, 1.32.1, 1.33.1, 1.39.1, 1.40.1 and 1.42.1 (the CEHM card of 1.24.1 is https://www.cehm.org.mx/Buscador/FichaBasica/38647?Tipo=A). Catalogue 1464 listed these ten telegrams as open; the CEHM cards say "en clave numérica" or "en clave de letras" and give no content. The telegrams are orders from Carranza's headquarters (Veracruz, "Faros") to generals and buying agents, dated 17 and 18 May and 9 June 1915.

`transcription.txt` is the contributor's typed copy (numbers, letters and clear words as typed, blocks t01 to t11, 1.22.1 being on two pages), `decryption.txt` the letter-for-letter decryption as typed, with the clerk's slips, `reading.md` (Spanish, coded text in capitals) and `translation.md` (English) the reading, `key.tsv` the three number keys and three letter-pair tables, and `contributor_readme.md` his notes.

## What they say

To Obregón at Estación Trinidad (17 May): the line is being reinforced as far as Apam; new ammunition will take four or five days, so the convoy at Apam is to go on. To Pablo González at Apizaco (9 June): a general who left that afternoon brings a million pesos in small bills. To Nuevo Laredo (17 May): ten thousand dollars go to the customs administrator for General Dávila, and two hundred thousand 7 mm cartridges and two hundred thousand .30-30 leave New York that day; Dávila is to write to the First Headquarters on service matters. To Elías in New York (9 June, very urgent): buy also the nine hundred and fifteen Lee rifles with their ammunition for the next day's steamer. To Arredondo in Washington (9 June): find out whether the American government will allow the repairs to the steamer "Progreso" in New York, and (17 May) place 425 dollars with the consul in Havana. Shorter messages go to Sáenz (his brothers have arrived) and to Denegri in San Francisco (General Nájera brings war supplies and funds). The history is the contributor's reading of the text; not checked here.

## The cipher

**Number telegrams** (1.17.1, 1.22.1, 1.23.1, 1.24.1, 1.33.1, 1.42.1): each number stands for one letter; the numbers 1-26, 27-52, 53-78 and 79-104 each run through the alphabet from their own start letter. 1.17.1, 1.22.1 and 1.23.1: Y, U, A, Q; 1.24.1 and 1.33.1: Q, G, Q, K; 1.42.1: W, G, E, M (`key.tsv`). **Letter telegrams** (1.29.1, 1.32.1, 1.39.1, 1.40.1): thirteen pairs of letters swap; the clear word "lunes" or "miércoles" stands before the coded text, and these are the true weekdays of 17 May and 9 June 1915, so the contributor takes the word to name the day's table; that is his inference. The table of 1.32.1 is partial.

## Remaining gaps

- The name of the general in 1.42.1, "[Cosío Rovelo?]", the contributor's guess from the letters ICLNEO GENERAL CIOCIOROVEOO - blocker: illegible; the sheet carries no other occurrence and the typed letters do not fix it
- A short run at the end of the first page of 1.22.1 (marked [...] in the reading) - blocker: illegible; the second page continues the sentence but the run is not settled
- 1.32.1 (shown as typed in `decryption.txt`, without a decryption), read from its own 21 letters by the pattern of "para" and the pair key, with one sign that looks like ñ where t is needed - blocker: too-short; 21 letters give no second occurrence to confirm it
- A human check of the transcription against the CEHM scans (the contributor compared sample pages, not every difference) - blocker: needs-physical-access; cehm.org.mx is not reachable from the project and the images may not be redistributed
- Narváez (2019), Ángel and Morales-Luna (2008), the CEHM fondo XXI key sheets and Obregón (1917) for the same tables - blocker: needs-physical-access; not checked by the contributor and not available to the project

## Escalation

- [x] siblings: both sides of all ten sheets and their CEHM cards looked at by the contributor, with CEHM searches by name and shelf term in part; no clear copy or decipherment turned up
- [x] clear-pages: the clear words of the telegrams (heads, salutations, "lunes", "miércoles") read with the coded text; no page is a decipherment
- [x] known-keys: no earlier key for these telegrams is known to the contributor or the project; the key family may be in print (see the status line)
- [x] print: the contributor checked Narváez's 2025 article in full (the tables are not in it) and the ledger; the 2019 book, Ángel and Morales-Luna and fondo XXI were not checked
- [x] key-rebuild: the number keys were opened by count matching on Spanish next-letter counts (65% to 77% of tokens on the largest set of 758) and settled by reading; the letter pairs came from a one-to-one solve on Spanish (contributor)
- [x] retry: a key fitted on 1.17.1 alone reads 1.22.1 and 1.23.1 and one fitted on 1.24.1 alone reads 1.33.1 (contributor's figures, not repeated here); the doubtful places were retried by the contributor

## Files

| File | Content |
|---|---|
| `transcription.txt` | the telegrams as typed (contributor) |
| `decryption.txt` | letter-for-letter decryption as typed, with the clerk's slips (contributor) |
| `reading.md`, `translation.md` | Spanish and English (contributor) |
| `key.tsv` | the three number keys and the letter-pair tables |
| `contributor_readme.md` | the contributor's notes |
| `VERIFICATION.md` | what the project re-checked |
| `profile.json` | the target profile |
