# nuevaclave1911: the "nueva clave" of April 1911, four telegrams of the Maderista junta read in part with a turning grille (CEHM-Carso CMXV.16.1551.3-4, 1561.3-13, 1561.5-13, 1569.3-10)

Status: read in part (Brice Dudout, 12 Nov 2026; corrected at the integration check, 12 Nov 2026; extended with issue #502 by SeldomPhooey and checked, 13 Nov 2026). Four telegrams of 18-20 April 1911 (San Antonio - El Paso), read in part with an
8 x 8 turning grille that an AI model proposed from the ciphertext. **The preregistered single measure on a held-out telegram, CMXV.16.1561.3-13, FAILED**
(car4 0.520 against the 0.70 threshold; margin +0.118 against the +0.30 required), because a letter is lost in its group YPXB and its second block is shifted
(`VALIDATION.md`); that failure stands. **The grille has since been checked by an outside document**: a typed period copy of 1569.3-10 (BNM, AMA Ms.M/T.2260 c.21) agrees with the grille's decryption on 174 of 176 letters. Since 13 Nov 2026 the held-out telegram is read in both blocks (one placeholder letter chosen by reading, two letters corrected). By the README rule (words, strict) 64 of 77 words are read = 83% (the first contributor's looser count takes the ten probable words as read: 74 of 77). The order of events (hashes frozen before the measure, single commits) is by the contributor's record.

This is a different cipher from the "Clave G.A." card that reads two other telegrams of the same traffic (`../mccarty1911/`, split apart on 12 Nov 2026): one key, one entry.

## The documents

Centro de Estudios de Historia de México (CEHM), Fundación Carlos Slim, Archivo Federico González Garza (Fondo CMXV): CMXV.16.1551.3-4 (18 April 1911, Adolfo González, San Antonio, to W. Olliphant = Federico González Garza, El Paso), CMXV.16.1561.5-13 (19 April, González Garza to Adolfo González, a copy of the outgoing telegram) and CMXV.16.1569.3-10 (20 April, Adolfo González to Olliphant). The CEHM holds the originals; its images are viewed on the public viewer for study and are not redistributed here. None carries a decipherment and none is in the typed list of period decipherments CMXV.18.1795.1, whose p. 11 notes "espacio para añadir 6 telegramas por traducir" (space to add 6 telegrams still to be translated); these are probably among them. Catalogue 1462 lists them as undeciphered.

## The "nueva clave": a turning grille (18-20 April 1911)

On 18 April Adolfo González ended a telegram in a new cipher with the clear words "nueva clave" (CMXV.16.1551.3-4); on 19 April González Garza asked him to keep the old key "por más rápida" (1561.7-13 above). Four telegrams of these days, with Spanish letter frequencies and many X, Y, Z, were not read by any card of the fonds; our own attempts (simple columnar transposition, widths 2-15, annealing; Caesar shifts) failed.

The key, proposed by Claude Fable 5.2 in one API run and checked by us with an independent decoder: an 8 x 8 turning grille (Fleissner) with 16 holes; each block of 64 cipher letters is written row by row, read through the holes row by row, and the grille is turned a quarter turn clockwise four times (`key_grille.txt`). The holes were derived from the nulls X/Z of the second block of 1551.3-4. One grille reads all four telegrams:

- 1551.3-4 (18 April, San Antonio to El Paso): both blocks, no repair: "It occurs to me that the forces could get water from the north-east: pass it on. I hope that with the funds sent they will have enough; if not, let me know." 17 words, 100 %.
- 1569.3-10 (20 April, San Antonio to El Paso): blocks 1-2 with no repair; all three blocks with no repair (the group is IRRXNO, 192 letters; the first transcription read IRXNO and needed a restored letter): "An American officer thinks an assault on Juárez inadvisable because it is mined. It would be better to attack without pause, dividing the army into three shifts of eight hours each; so the garrison would surrender from exhaustion." 26 words, 24 sure (92 % strict).
- 1561.3-13 (19 April, 5:25 p.m., San Antonio to El Paso; the former held-out telegram, read by SeldomPhooey, issue #502): block 1 with no repair; block 2 with one placeholder letter inserted in YPXB (index 96, chosen by reading): "In my opinion an armistice would amount to the destruction of the insurgent forces. They should attack Juárez without delay if there is a probability of success. [?Parras] attacked." 17 words, 14 sure (82 %); tardanza and probabilidades each need one letter corrected, parras is unresolved.
- 1561.5-13 (19 April, El Paso to San Antonio): block 1 with no repair; block 2 after deleting one extra letter: "Key. S. Dr on the outskirts of Juárez, ready to attack. Communicated with S. Terrazas. Our messenger: armistice probable. Funds insufficient." 17 words, 88 % (five letters corrected by the sense, two single S unresolved).

Readings and counts: `reading.md`, `translation.md`, `decryption.txt`.

### Validation: the preregistered measure FAILED; an outside check of the grille succeeded

Before anything was sent to the model, one whole telegram of the same family was held out: CMXV.16.1561.3-13 (Adolfo González to Olliphant, 19 April, 127 letters); protocol, statistic, thresholds and scripts were hashed. The model returned a fixed key for it; we ran the measure once: car4 = 0.520 against the 0.70 threshold, margin +0.118 over the best of 400 controls (200 random grilles at most 0.402) against the +0.30 required. Not validated. Cause: the held-out telegram has lost a letter in its four-letter group YPXB, so its second block is shifted; its first block came out intact ("opino armisticio equivaldria destruccion fuerzas insurgentes deben atac..."). A post-hoc trial with the model's own rule for a short group is not counted. The grille rests instead on five blocks of 64 letters that read as fluent Spanish with no repair, one grille across three telegrams and both directions, and nulls placed as a grille places them; one repair in the pull request (a deletion in 1561.5-13; the insertion in 1569.3-10 fell away, see below) is declared and was chosen while looking at the text (`VALIDATION.md`).

**Outside check, 13 Nov 2026 (issue #502, SeldomPhooey; rechecked here).** A typed period copy of 1569.3-10 (BNM, Archivo Francisco I. Madero, AMA Ms.M/T.2260 c.21, "COPIA DE TELEGRAMA", signed G. A. M.) agrees with the grille's decryption of the 192 letters on 174 of 176 letters of text (three edits: t for p in *por*, a doubled v, an i in *lograriase*). The copy played no part in finding the grille. It confirms the hole positions on all 64 cells, not the word cuts or corrected letters of the other telegrams, and it does not say when or from what it was copied. The preregistered measure remains failed and is not turned into a pass by this; the first block of 1561.3-13 (never sent to the model) also reads, and scores -4.36 per letter against -6.54 for the best of 300 random grilles (own control). The key is recorded as recovered (every cell of the grille is fixed and checked), still without a preregistered validation.

### Not translated at the time

None of these telegrams is in the typed list of period decipherments CMXV.18.1795.1. On its p. 11, after the San Antonio telegrams of 17-18 April, the typist left a note: "espacio para añadir 6 telegramas por traducir" (space to add 6 telegrams still to be translated); the grille telegrams are probably among them.

### Credits for this part

Claude Fable 5.2 (Anthropic) proposed the grille and the readings in one API run (a tool we used; cost 3.09 USD); Brice Dudout's project transcribed the telegrams, set the protocol, checked the grille with an independent decoder, ran the measure and wrote this up. The CEHM (Fundación Carlos Slim) holds the originals.

### Credits

An AI model (Claude Fable 5.2, Anthropic; named in the contributor's files) proposed the grille and the readings in one API run (cost 3.09 USD, as the contributor states); Brice Dudout's project transcribed the telegrams, set the protocol, checked the grille with an independent decoder, ran the measure and wrote this up. The CEHM (Fundación Carlos Slim) holds the originals. Catalogue 1462 and the pointer to the key cards: Daniel Bourdeau.

## Remaining gaps

- A preregistered validation of the turning grille on a telegram not yet seen: the held-out telegram is spent; the outside check (typed copy of 1569.3-10) now stands in for it - blocker: no-key-material; no other telegram in the grille is known among the 136 coded pieces of the fonds harvested so far
- 1561.5-13: letters 29, 38, 57, 68, 87 and the extra letter near 73 to be checked on the original; the two single "S" - blocker: needs-physical-access
- The pencil letters "v e" above ESSFP on 1551.3-4 - blocker: too-short; two letters, not explained by the grille
- 1561.3-13: the placeholder in YPXB is chosen by reading (positions 94-98 tried), tardanza and probabilidades each need a letter corrected, parras (a place? Parras, Coahuila) is unresolved - blocker: needs-physical-access; the printed sources that might carry the telegram (Narváez 2019, Fabela, González Garza 1936) were not examined by anyone
- The CEHM catalogue records 12,803 and 12,804 (descriptions of 1561.3-13 and 1561.4-13) look swapped, so catalogue 1462's "1561.4-13" is very probably 1561.3-13; confirmed on both images and both records here, not by the CEHM - blocker: no-key-material (needs the CEHM)
- A second reader's check of the transcriptions against the CEHM images: done for 1561.3-13 (front), 1569.3-10 (IRRXNO) and 1551.3-4 (ERDEO) on 13 Nov 2026; not done for 1561.5-13 (its 16th group XXMSY or XXNSY, letters 29, 38, 57, 68, 87) - blocker: needs-physical-access

## Escalation

- [x] siblings: the eight telegrams of the Clave G.A. test and 1561.7-13 (Clave G.A., `../mccarty1911/`) opened; none is in the grille
- [x] clear-pages: none of the three is in the typed decipherments CMXV.18.1795.1 and none carries a gloss
- [x] known-keys: every card of the fonds (CMXV.16.1557.1) tried on the five telegrams, group by group: none reads them (best coverage 0.50 < 0.70)
- [x] print: no printed edition of these telegrams is known; Narváez 2011 and 2019 not available to the project
- [x] key-rebuild: columnar transposition (widths 2-15) and Caesar shifts failed; the grille was proposed by an AI model from the ciphertext
- [x] retry: the shifted blocks were retried with the declared repairs (a deletion in 1561.5-13, a placeholder in 1561.3-13); the insertion in 1569.3-10 was replaced by the corrected transcription IRRXNO (13 Nov 2026)

## Integration check (12 Nov 2026)

Done by an independent session after the PR was merged into the branch.

- Own Fleissner decoder from `key.txt` (written from the grid, clockwise quarter turns) reproduces every block of `decryption.txt`: the five blocks read, the shifted blocks come out unreadable as stated.
- Control: 0 of 2000 random grilles of the same family (one hole per rotation orbit) score as well as this grille on the five fluent blocks (Spanish 4-gram per letter: -4.65 against at best -7.10, mean -8.06). The grille was fitted on these blocks, so this shows fit and not validation.
- "No repair" means no insertion or deletion: the five blocks still contain six letters corrected by the sense (listo, atacar, nuestro, por, contrario, and a doubled v in convendría), and the repaired block of 1561.5-13 two more (mensagero, armisticio).
- Strict word count (README rule): 1551.3-4 16 of 17, 1561.5-13 9 of 17, 1569.3-10 23 of 26; 48 of 60 = 80%.
- The failed measure could not be re-run (the held-out cipher is not published); it is reported as failed, with what else supports the grille kept apart from it.
- Split out of `mccarty1911`: the grille and the Clave G.A. card are different systems.

## Check of issue #502 (13 Nov 2026)

Done by an independent session; the contributor is SeldomPhooey (AI agents, no human cryptographer or historian, as they state).

- Own decoder written from the grid reproduces the issue's table of block 2 at the placeholder positions 94-98 and its 192-letter decryption of 1569.3-10 with IRRXNO; the contributor's difflib script, rerun, gives 176/176 letters and 174 identical.
- Images fetched from the CEHM viewer and the UNAM repository (SHA-256 of the 1561.3-13 front and of the BNM copy match the issue): the transcription of 1561.3-13 matches group by group; 1569.3-10 reads irrxno (two r's); 1551.3-4 reads erdeo. The BNM leaf is as quoted.
- CEHM records 12803 and 12804 fetched: 12803 (item 3-13) describes funds and Olivas, and the image at 4-13 is the funds/Olivas telegram with pencil decodes ("fondos", "olivas", "mil treinta"); the image at 3-13 is all cipher. The swap is consistent with both images; the CEHM has not confirmed it, so catalogue 1462 carries the swap as "very probably" and "not confirmed by the CEHM"; its undeciphered list drops 3-13 (read in part) and 4-13 (deciphered at the time) with that hedge.
- Counts: strict 64 of 77 words (above). The first three telegrams change only through the corrected transcriptions (1551.3-4 17 of 17, 1569.3-10 24 of 26).
- Not adopted: the contributor's remark that catalogue 1462's "alias John McCarty" may conflate Alfonso Madero with Gustavo (typed list 1795.1) was not checked against the list.

## Files

| File | Content |
|---|---|
| `key.txt` | the turning grille |
| `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md` | the four telegrams in the grille (1561.3-13 added 13 Nov 2026) |
| `VALIDATION.md` | the failed preregistered measure, what supports the grille, and the outside check of 13 Nov 2026 |
| `profile.json` | the target profile |
