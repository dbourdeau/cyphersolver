# mccarty1911: González Garza to "John McCarty" (Adolfo González), El Paso, 29 March 1911 (CEHM-Carso CMXV.15.1432.1-4)

Status: read (Brice Dudout, 12 Nov 2026; 19 of 20 words, all six coded words decoded; "Ag" read as letters but not identified). Read with the archive's "Clave G.A." key card, validated once on 769 cipher letters of eight sibling telegrams against their decipherments of the time (`VALIDATION.md`).

## The document

Centro de Estudios de Historia de México (CEHM), Fundación Carlos Slim, Archivo Federico González Garza (Fondo CMXV), CMXV.15.1432.1-4, two images (front, blank back; CEHM record 12730, https://www.cehm.org.mx/Buscador/FichaBasica/12730?Tipo=A). The CEHM holds the original; its images are viewed on the public CEHM viewer for study and are not redistributed here. A Texas Telegraph Company sending form, typed: the sender's copy of a telegram from Federico González Garza at El Paso, Texas, 29 March 1911, to "John McCarty", 437 Main Ave., San Antonio, Texas, the cover name of Adolfo González (as the typed list CMXV.18.1795.1 and the CEHM record give it). The CEHM record calls it "en clave"; no decipherment stands on the sheet, and the telegram is not in 1795.1, the typed list of 66 coded telegrams deciphered at the time (all 45 pages searched). Catalogue 1462 lists it as undeciphered.

## What it says

"On the 13th, Dr and Ag separated at Galeana; the latter took the road to Guerrero and the former the road to Chihuahua, camping on the 23rd at Encinillas." Six words are coded: GALEANA, DR, AG, GUERRERO, CHIH (Chihuahua) and ENCINILLAS; the rest is clear. "Dr" is probably "Doctor", the cover name for Madero in this traffic: in the period decipherments of siblings, the gloss "Dr" stands where 1795.1 types "Madero" (CMXV.14.1392.1-2, 1411.4-4), and 1795.1 adds "(Madero)" after "matar doctor" (CMXV.15.1458.4-6). "Ag" is not identified. No further history is claimed here.

## The cipher

The "Clave G.A. (una de las usadas en San Antonio)" card, CMXV.16.1557.1, scans 12-13 (signed "Dr. V.G."): a digraphic table of two rows and fifteen columns. A plain letter is written as one of the five row letters of its row (W Z C T G, or M V P K I) followed by its column letter (B L R A F Q E N H D X Y O S J); `key.tsv`. The coded words of a run are read together, two letters at a time (`decryption.txt`). Two pairs are faulty in transmission: PACA ends in CA (m) for n, and KHTNI BGBTB PBEBP J has a stray EB; the sense fixes both (Galeana, Guerrero).

## Validation

The card was transcribed from the CEHM image the day before this reading and not changed since. A first measure on two telegrams (30 held-out letters) was too short to validate. The second, preregistered and run once (`VALIDATION.md`): the cipher of eight sibling telegrams of March-April 1911 was transcribed blind (pencil glosses filtered out of the scans), the pencil decipherments of the time were transcribed separately, and the card, as is, was applied. Agreement with the period clear A = 0.866 on 769 cipher letters, against at most 0.257 for 400 controls (permuted tables, shuffled text); thresholds 0.85 and +0.30 were fixed in advance. The card is therefore the key of this traffic, and 1432.1-4 is read with a validated key.

## Earlier work in this fonds

Catalogue 1462 (Daniel Bourdeau) pointed to the key cards CMXV.16.1557.1 and the typed decipherments CMXV.18.1795.1. Two telegrams of the fonds were read before with other cards of the same box: CMXV.15.1420.3-6 by William Echols with the Hernández card (`../hernandez1911/`, issue #351) and CMXV.18.1770.2-4 by Prabal Gupta with the "Herrera. Moreno." card (`../mexico1911/`, issue #330). This telegram uses neither of those cards.

## Remaining gaps

- "Ag": the letters are certain, the person is not identified - blocker: needs-physical-access; the period sources that might name him (the recipients' papers, Narváez 2011 and 2019) were not searched
- Whether the telegram is in print - blocker: needs-physical-access; the books are not available to the project
- A second reader's check of the transcription and of the card against the CEHM images - blocker: needs-physical-access; the images may not be redistributed

## Escalation

- [x] siblings: eight telegrams of the same traffic with period decipherments used to validate the card (`VALIDATION.md`)
- [x] clear-pages: the telegram is not in the typed decipherments CMXV.18.1795.1 and carries no gloss
- [x] known-keys: the "Clave G.A." card of the fonds is the key; the Hernández and Herrera Moreno cards do not read it
- [n/a] key-rebuild: the key is the archive's card; nothing to rebuild
- [x] retry: all six coded words decoded

## Files

| File | Content |
|---|---|
| `transcription.txt` | the telegram as typed (coded words in capitals) |
| `decryption.txt` | each coded run, its pairs and letters |
| `reading.md`, `translation.md` | Spanish and English |
| `key.tsv` | the "Clave G.A." card |
| `VALIDATION.md` | the preregistered test of the card on sibling telegrams |
| `profile.json` | the target profile |
