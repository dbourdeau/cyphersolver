# mccarty1911: González Garza and "Adolfo González" (Gustavo A. Madero), El Paso - San Antonio, March-April 1911 (CEHM-Carso CMXV.15.1432.1-4, 16.1561.7-13, 16.1551.3-4, 16.1561.5-13, 16.1569.3-10)

Status: read in part (Brice Dudout, 12 Nov 2026). Three groups of telegrams of the San Antonio - El Paso traffic, March-April 1911:

- CMXV.15.1432.1-4 (29 March): read, 19 of 20 words, with the archive's "Clave G.A." key card, validated once on 769 cipher letters of eight sibling telegrams against their decipherments of the time (`VALIDATION.md`).
- CMXV.16.1561.7-13 (19 April): read, all four coded words, with the same validated card; the coded groups are joined before cutting into pairs.
- CMXV.16.1551.3-4, 1561.5-13 and 1569.3-10 (18-20 April), the "nueva clave": read in part with an 8 x 8 turning grille proposed by Claude Fable 5.2 (Anthropic). **The preregistered single measure on a held-out telegram, CMXV.16.1561.3-13, FAILED** (car4 0.520 against the 0.70 threshold; margin +0.118 against the +0.30 required), because a letter is lost in its group YPXB and its second block is shifted (`VALIDATION_grille.md`). A post-hoc trial is not counted. What supports the grille instead: five blocks of 64 letters read as fluent Spanish with no repair, while 200 random grilles score at most 0.402 on the held-out text; two repairs (one deletion, one insertion) are declared.

## The document

Centro de Estudios de Historia de México (CEHM), Fundación Carlos Slim, Archivo Federico González Garza (Fondo CMXV), CMXV.15.1432.1-4, two images (front, blank back; CEHM record 12730, https://www.cehm.org.mx/Buscador/FichaBasica/12730?Tipo=A). The CEHM holds the original; its images are viewed on the public CEHM viewer for study and are not redistributed here. A Texas Telegraph Company sending form, typed: the sender's copy of a telegram from Federico González Garza at El Paso, Texas, 29 March 1911, to "John McCarty", 437 Main Ave., San Antonio, Texas, the cover name of Adolfo González (as the typed list CMXV.18.1795.1 and the CEHM record give it). The CEHM record calls it "en clave"; no decipherment stands on the sheet, and the telegram is not in 1795.1, the typed list of 66 coded telegrams deciphered at the time (all 45 pages searched). Catalogue 1462 lists it as undeciphered.

## What it says

"On the 13th, Dr and Ag separated at Galeana; the latter took the road to Guerrero and the former the road to Chihuahua, camping on the 23rd at Encinillas." Six words are coded: GALEANA, DR, AG, GUERRERO, CHIH (Chihuahua) and ENCINILLAS; the rest is clear. "Dr" is probably "Doctor", the cover name for Madero in this traffic: in the period decipherments of siblings, the gloss "Dr" stands where 1795.1 types "Madero" (CMXV.14.1392.1-2, 1411.4-4), and 1795.1 adds "(Madero)" after "matar doctor" (CMXV.15.1458.4-6). "Ag" is not identified. No further history is claimed here.

## The cipher

The "Clave G.A. (una de las usadas en San Antonio)" card, CMXV.16.1557.1, scans 12-13 (signed "Dr. V.G."): a digraphic table of two rows and fifteen columns. A plain letter is written as one of the five row letters of its row (W Z C T G, or M V P K I) followed by its column letter (B L R A F Q E N H D X Y O S J); `key.tsv`. The coded words of a run are read together, two letters at a time (`decryption.txt`). Two pairs are faulty in transmission: PACA ends in CA (m) for n, and KHTNI BGBTB PBEBP J has a stray EB; the sense fixes both (Galeana, Guerrero).

## Validation

The card was transcribed from the CEHM image the day before this reading and not changed since. A first measure on two telegrams (30 held-out letters) was too short to validate. The second, preregistered and run once (`VALIDATION.md`): the cipher of eight sibling telegrams of March-April 1911 was transcribed blind (pencil glosses filtered out of the scans), the pencil decipherments of the time were transcribed separately, and the card, as is, was applied. Agreement with the period clear A = 0.866 on 769 cipher letters, against at most 0.257 for 400 controls (permuted tables, shuffled text); thresholds 0.85 and +0.30 were fixed in advance. The card is therefore the key of this traffic, and 1432.1-4 is read with a validated key.

## The second telegram in the Clave G.A.: CMXV.16.1561.7-13 (19 April 1911)

A typed copy of a telegram from González Garza at El Paso to Adolfo González, 437 Main Ave., San Antonio; no gloss, not in 1795.1. Four coded words: KNGB = DR, PYZYG HVRIB = CLAVE, PLMJP AVNVJ ZF = FONDOS, MFZHC BZDCN PB = PARQUE (`decryption_1561-7-13.txt`). "Dr wants Elías to come too. While the crisis lasts, go on using the old key, since it is quicker. Send funds and ammunition of all kinds at once." All 21 words read. An earlier attempt of ours (12 Nov) had decoded group by group and failed: the pairs run across the five-letter groups (PY ZY G|H VR IB); the model pointed this out. The card is the one validated in `VALIDATION.md`, unchanged.

## The "nueva clave": a turning grille (18-20 April 1911)

On 18 April Adolfo González ended a telegram in a new cipher with the clear words "nueva clave" (CMXV.16.1551.3-4); on 19 April González Garza asked him to keep the old key "por más rápida" (1561.7-13 above). Three telegrams of these days, with Spanish letter frequencies and many X, Y, Z, were not read by any card of the fonds; our own attempts (simple columnar transposition, widths 2-15, annealing; Caesar shifts) failed.

The key, proposed by Claude Fable 5.2 in one API run and checked by us with an independent decoder: an 8 x 8 turning grille (Fleissner) with 16 holes; each block of 64 cipher letters is written row by row, read through the holes row by row, and the grille is turned a quarter turn clockwise four times (`key_grille.txt`). The holes were derived from the nulls X/Z of the second block of 1551.3-4. One grille reads all three telegrams:

- 1551.3-4 (18 April, San Antonio to El Paso): both blocks, no repair: "It occurs to me that the forces could get water from the north-east: pass it on. I hope that with the funds sent they will have enough; if not, let me know." 17 words, 100 %.
- 1569.3-10 (20 April, San Antonio to El Paso): blocks 1-2 with no repair; block 3 after restoring one lost letter in IRXNO: "An American officer thinks an assault on Juárez inadvisable because it is mined. It would be better to attack without pause, dividing the army into three shifts of eight hours each; so the garrison would surrender from exhaustion." 26 words, 96 %.
- 1561.5-13 (19 April, El Paso to San Antonio): block 1 with no repair; block 2 after deleting one extra letter: "Key. S. Dr on the outskirts of Juárez, ready to attack. Communicated with S. Terrazas. Our messenger: armistice probable. Funds insufficient." 17 words, 88 % (five letters corrected by the sense, two single S unresolved).

Readings and counts: `reading_grille.md`, `translation_grille.md`, `decryption_grille.txt`.

### Validation: the preregistered measure FAILED

Before anything was sent to the model, one whole telegram of the same family was held out: CMXV.16.1561.3-13 (Adolfo González to Olliphant, 19 April, 127 letters); protocol, statistic, thresholds and scripts were hashed. The model returned a fixed key for it; we ran the measure once: car4 = 0.520 against the 0.70 threshold, margin +0.118 over the best of 400 controls (200 random grilles at most 0.402) against the +0.30 required. Not validated. Cause: the held-out telegram has lost a letter in its four-letter group YPXB, so its second block is shifted; its first block came out intact ("opino armisticio equivaldria destruccion fuerzas insurgentes deben atac..."). A post-hoc trial with the model's own rule for a short group is not counted. The grille rests instead on five blocks of 64 letters that read as fluent Spanish with no repair, one grille across three telegrams and both directions, and nulls placed as a grille places them; two repairs (one deletion in 1561.5-13, one insertion in 1569.3-10) are declared and were chosen while looking at the text (`VALIDATION_grille.md`).

### Not translated at the time

None of these telegrams is in the typed list of period decipherments CMXV.18.1795.1. On its p. 11, after the San Antonio telegrams of 17-18 April, the typist left a note: "espacio para añadir 6 telegramas por traducir" (space to add 6 telegrams still to be translated); the grille telegrams are probably among them.

### Credits for this part

Claude Fable 5.2 (Anthropic) proposed the grille and the readings in one API run (a tool we used; cost 3.09 USD); Brice Dudout's project transcribed the telegrams, set the protocol, checked the grille with an independent decoder, ran the measure and wrote this up. The CEHM (Fundación Carlos Slim) holds the originals.

## Earlier work in this fonds

Catalogue 1462 (Daniel Bourdeau) pointed to the key cards CMXV.16.1557.1 and the typed decipherments CMXV.18.1795.1. Two telegrams of the fonds were read before with other cards of the same box: CMXV.15.1420.3-6 by William Echols with the Hernández card (`../hernandez1911/`, issue #351) and CMXV.18.1770.2-4 by Prabal Gupta with the "Herrera. Moreno." card (`../mexico1911/`, issue #330). This telegram uses neither of those cards.

## Remaining gaps

- "Ag": the letters are certain, the person is not identified - blocker: needs-physical-access; the period sources that might name him (the recipients' papers, Narváez 2011 and 2019) were not searched
- Whether the telegram is in print - blocker: needs-physical-access; the books are not available to the project
- A second reader's check of the transcriptions and of the card against the CEHM images - blocker: needs-physical-access; the images may not be redistributed
- A validation of the turning grille: the only held-out telegram is spent; another telegram in the grille, not yet seen, would be needed - blocker: no-key-material; none is known among the 136 coded pieces of the fonds harvested so far
- 1561.5-13: letters 29, 38, 57, 68, 87 and the extra letter near 73 to be checked on the original; the two single "S" - blocker: needs-physical-access
- The pencil letters "v e" above ESSFP on 1551.3-4 - blocker: too-short; two letters, not explained by the grille

## Escalation

- [x] siblings: eight telegrams of the same traffic with period decipherments used to validate the card (`VALIDATION.md`)
- [x] clear-pages: the telegram is not in the typed decipherments CMXV.18.1795.1 and carries no gloss
- [x] known-keys: the "Clave G.A." card of the fonds is the key; the Hernández and Herrera Moreno cards do not read it
- [n/a] key-rebuild: the key is the archive's card; nothing to rebuild
- [x] retry: all six coded words decoded; 1561.7-13 re-decoded with the groups joined
- [n/a] print: no printed edition of these telegrams is known to the project; the likely books (Narváez 2011, 2019) are not available (see gaps)
- [x] key-rebuild (grille): key recovered from the cipher (Claude Fable 5.2), preregistered measure failed, declared

## Files

| File | Content |
|---|---|
| `transcription.txt` | the telegram as typed (coded words in capitals) |
| `decryption.txt` | each coded run, its pairs and letters |
| `reading.md`, `translation.md` | Spanish and English |
| `key.tsv` | the "Clave G.A." card |
| `VALIDATION.md` | the preregistered test of the card on sibling telegrams |
| `transcription_1561-7-13.txt`, `decryption_1561-7-13.txt`, `reading_1561-7-13.md`, `translation_1561-7-13.md` | the telegram of 19 April in the Clave G.A. |
| `key_grille.txt` | the turning grille |
| `transcription_grille.txt`, `decryption_grille.txt`, `reading_grille.md`, `translation_grille.md` | the three telegrams in the grille |
| `VALIDATION_grille.md` | the failed preregistered measure and what supports the grille |
| `profile.json` | the target profile |
