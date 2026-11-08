# Check of the contributor's keys and reading (8 Nov 2026, repository commit af80f5e)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #321). The CEHM scans are not reachable from the
project's environment, so **no transcription was compared with a scan by the project**. No human has repeated the check.

## 1. The number telegrams

The six number telegrams (blocks t01 to t07 of `transcription.txt`: 1.17.1, 1.22.1 on both pages, 1.23.1, 1.24.1, 1.33.1 and 1.42.1)
were decrypted again with the start letters of `key.tsv` by an own script: number n in a run of 26 stands for the letter that many
places after the run's start letter (Y U A Q for 1.17.1, 1.22.1 and 1.23.1; Q G Q K for 1.24.1 and 1.33.1; W G E M for 1.42.1).
The 1,056 number tokens give 1,056 letters; a sequence match against the letters of the contributor's `decryption.txt` gives 98.2%
(by telegram 97.4% to 100%). The contributor reports 1,013 of 1,050 tokens (96.5%) giving the reading's letter as typed; the
project's figure counts the decryption file, not the reading.

## 2. Control against random start letters

A word list of about 130 common Spanish words and words of the telegrams' own subjects was matched in the decryption of the
1,001 letters of the number telegrams with a fitted table (1.17.1 to 1.24.1 and 1.33.1 to 1.42.1, not counting the
second page of 1.22.1). With the contributor's start letters 62.8% of the letters fall in listed words; with 300 random sets of four
start letters per table the mean is 4.2% and the best 22.5%. The key makes Spanish and a random one does not. Examples of the
decryption: "situen al administrador de la aduana en esa a disposicion del gral davila diez mil dolares", "hoy salen de nueva
york doscientos mil cartuchos siete mm". The word list partly overlaps the vocabulary of the reading, so this is a check that the
key makes words of these telegrams, not an independent measure.

## 3. The letter telegrams

For 1.29.1, 1.39.1 and 1.40.1 the coded tokens of the transcription, swapped with the contributor's pair tables ("lunes" for 1.29.1,
"miércoles" for 1.39.1 and 1.40.1), agree with the decryption file letter for letter on all 244 coded letters (55, 63 and 126 letters), which shows that the file follows the tables, not that the tables are right. `decryption.txt` shows 1.32.1 as typed, without a decryption: its table is partial and its reading ("pertrechos y fondos para", with a sign like ñ standing where t is needed) rests on 21 letters. For example "qarnp nxnan" gives ENLAH ABANA, "en la
Habana".

## 4. What the project could not check

- The transcription against the scans (two passes agreeing on 99.2% of 1,292 tokens by the contributor's count; he checked sample pages, not every difference).
- The held-out tests, the blind reader and the search scores of the contributor.
- The history of the telegrams (Obregón's campaign, the steamer "Progreso", the Lee rifles) and the name "Cosío Rovelo".
- Whether the tables are in Narváez (2019), Ángel and Morales-Luna (2008) or the CEHM fondo XXI key sheets; the contributor checked Narváez (2025) in full and found them not printed there.
