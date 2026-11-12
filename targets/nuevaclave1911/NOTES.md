# nuevaclave1911: the "nueva clave" of April 1911, three telegrams of the Maderista junta read in part with a turning grille (CEHM-Carso CMXV.16.1551.3-4, 1561.5-13, 1569.3-10)

Status: read in part (Brice Dudout, 12 Nov 2026; corrected at the integration check, 12 Nov 2026). Three telegrams of 18-20 April 1911 (San Antonio - El Paso), read in part with an
8 x 8 turning grille that an AI model proposed from the ciphertext. **The preregistered single measure on a held-out telegram, CMXV.16.1561.3-13, FAILED**
(car4 0.520 against the 0.70 threshold; margin +0.118 against the +0.30 required), because a letter is lost in its group YPXB and its second block is shifted
(`VALIDATION.md`). The key is not validated. By the README rule (words) 48 of 60 words are read = 80% (the contributor's 95% counts the nine probable words as read).
The order of events (hashes frozen before the measure, single commits) is by the contributor's record.

This is a different cipher from the "Clave G.A." card that reads two other telegrams of the same traffic (`../mccarty1911/`, split apart on 12 Nov 2026): one key, one entry.

## The documents

Centro de Estudios de Historia de México (CEHM), Fundación Carlos Slim, Archivo Federico González Garza (Fondo CMXV): CMXV.16.1551.3-4 (18 April 1911, Adolfo González, San Antonio, to W. Olliphant = Federico González Garza, El Paso), CMXV.16.1561.5-13 (19 April, González Garza to Adolfo González, a copy of the outgoing telegram) and CMXV.16.1569.3-10 (20 April, Adolfo González to Olliphant). The CEHM holds the originals; its images are viewed on the public viewer for study and are not redistributed here. None carries a decipherment and none is in the typed list of period decipherments CMXV.18.1795.1, whose p. 11 notes "espacio para añadir 6 telegramas por traducir" (space to add 6 telegrams still to be translated); these are probably among them. Catalogue 1462 lists them as undeciphered.

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

### Credits

An AI model (Claude Fable 5.2, Anthropic; named in the contributor's files) proposed the grille and the readings in one API run (cost 3.09 USD, as the contributor states); Brice Dudout's project transcribed the telegrams, set the protocol, checked the grille with an independent decoder, ran the measure and wrote this up. The CEHM (Fundación Carlos Slim) holds the originals. Catalogue 1462 and the pointer to the key cards: Daniel Bourdeau.

## Remaining gaps

- A validation of the turning grille: the only held-out telegram is spent; another telegram in the grille, not yet seen, would be needed - blocker: no-key-material; none is known among the 136 coded pieces of the fonds harvested so far
- 1561.5-13: letters 29, 38, 57, 68, 87 and the extra letter near 73 to be checked on the original; the two single "S" - blocker: needs-physical-access
- The pencil letters "v e" above ESSFP on 1551.3-4 - blocker: too-short; two letters, not explained by the grille
- The held-out telegram 1561.3-13: its cipher is not in the repository, only its hash, so a third party cannot repeat the failed measure (its first block, 64 letters never sent to the model, read as Spanish) - blocker: needs-physical-access
- A second reader's check of the transcriptions against the CEHM images - blocker: needs-physical-access; the images may not be redistributed, and visor.cehm.org.mx failed TLS verification in the integrating session

## Escalation

- [x] siblings: the eight telegrams of the Clave G.A. test and 1561.7-13 (Clave G.A., `../mccarty1911/`) opened; none is in the grille
- [x] clear-pages: none of the three is in the typed decipherments CMXV.18.1795.1 and none carries a gloss
- [x] known-keys: every card of the fonds (CMXV.16.1557.1) tried on the five telegrams, group by group: none reads them (best coverage 0.50 < 0.70)
- [x] print: no printed edition of these telegrams is known; Narváez 2011 and 2019 not available to the project
- [x] key-rebuild: columnar transposition (widths 2-15) and Caesar shifts failed; the grille was proposed by an AI model from the ciphertext
- [x] retry: the shifted blocks were retried with the declared repairs (one deletion, one insertion)

## Integration check (12 Nov 2026)

Done by an independent session after the PR was merged into the branch.

- Own Fleissner decoder from `key.txt` (written from the grid, clockwise quarter turns) reproduces every block of `decryption.txt`: the five blocks read, the shifted blocks come out unreadable as stated.
- Control: 0 of 2000 random grilles of the same family (one hole per rotation orbit) score as well as this grille on the five fluent blocks (Spanish 4-gram per letter: -4.65 against at best -7.10, mean -8.06). The grille was fitted on these blocks, so this shows fit and not validation.
- "No repair" means no insertion or deletion: the five blocks still contain six letters corrected by the sense (listo, atacar, nuestro, por, contrario, and a doubled v in convendría), and the repaired block of 1561.5-13 two more (mensagero, armisticio).
- Strict word count (README rule): 1551.3-4 16 of 17, 1561.5-13 9 of 17, 1569.3-10 23 of 26; 48 of 60 = 80%.
- The failed measure could not be re-run (the held-out cipher is not published); it is reported as failed, with what else supports the grille kept apart from it.
- Split out of `mccarty1911`: the grille and the Clave G.A. card are different systems.

## Files

| File | Content |
|---|---|
| `key.txt` | the turning grille |
| `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md` | the three telegrams in the grille |
| `VALIDATION.md` | the failed preregistered measure and what supports the grille |
| `profile.json` | the target profile |
