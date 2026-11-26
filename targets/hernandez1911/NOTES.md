# hernandez1911: the Hernández letter-swap card, telegrams of 27 and 28 March 1911 (CEHM-Carso CMXV.15.1420.3-6 and 1430.3-3)

Status: read (9 Nov 2026; a second telegram filed 21 Nov 2026). CMXV.15.1420.3-6 was contributed by William Echols (issue #351; he worked with OpenAI's GPT-6.1 Sol in Codex): four coded words in a Spanish telegram, read with a five-pair letter-swap key from the key card filed for the recipient in the same fonds, and checked here against his submission (`VERIFICATION.md`). CMXV.15.1430.3-3 (28 March 1911) was contributed by Daniel Jalkut (PR #831, with Claude Code): ten coded words, deciphered at the time in pencil on the form; the same card gives the same text. The PR #831 review compared the card with its scan (CMXV.16.1557.1, scan 16) and the groups of 1430.3-3 with their image; the image of 1420.3-6 has not been compared.

Maintainers' note, 21 November 2026: four more telegrams of 27-31 March 1911 decode with this card (PR #831, Daniel Jalkut). 15.1420.5-6 builds sentences, 10 sure words of 19 (read in part); 15.1420.6-6, 15.1432.3-4 and 15.1447.1-3 give words and no sentence (decoded, not read). Filed here they would make this target read in part, which is the owner's decision, so they stay in `../duron1911/siblings/` for now (section "Sibling telegrams of the same card" below).

## The documents

Centro de Estudios de Historia de México (CEHM), Fundación Carlos Slim, Archivo Federico González Garza (Fondo CMXV), CMXV.15.1420.3-6, two images (front and reverse; CEHM record 12723, https://www.cehm.org.mx/Buscador/FichaBasica/12723?Tipo=A): a telegram of 27 March 1911 from Federico González Garza at El Paso, Texas, to Braulio Hernández at Presidio, Texas. The CEHM record calls it "texto en clave" and gives no decipherment; catalogue 1462 listed it among the telegrams of this fonds on that record.

`transcription.txt` is the contributor's transcription, `decryption.txt` each coded word with its decryption, `key.tsv` the key, `reading.md` and `translation.md` the reading in Spanish and English, `contributor_issue.md` his submission as filed.

CMXV.15.1430.3-3 (CEHM record 12729, "en clave", no text): a telegram from Presidio, 28 March 1911, 4:37 pm, signed "E H Leroy" (a cover name of Braulio Hernández in this traffic, as the contributor gives it), to Lic. Fred G. Garza, no. 16 Alberta Hotel, El Paso. All ten groups are coded. A pencil line at the head of the form gives the text deciphered at the time: "Total 160 h - Diga si viene refuerzo y", then a faint last word under the CEHM watermark that the review could not read; the pencil strokes in the typed groups fall at word ends of that text. It is not in the typed list CMXV.18.1795.1 (searched by the contributor, 20 Nov 2026). Catalogue 1462 listed it as undeciphered. Its transcription, decryption and reading (with the English) are the contributor's files in `../duron1911/siblings/` (the block or section headed CMXV.15.1430.3-3), which hold ten telegrams of PR #831 and are referenced from `profile.json`, not copied.

## What it says

"Did you receive the pills? You should stay there. Villarreal will leave Wednesday or Thursday, taking a cannon. Write back." The first two sentences and the signature are in clear; the four coded words are VILLARREAL, SALDRA, LLEVANDO and CANON (written without the tilde). The contributor gives no further background and none is added here.

CMXV.15.1430.3-3: "Total ciento sesenta hombres. Diga si viene refuerzo y cañón." ("A total of one hundred and sixty men. Say whether reinforcements and the cannon are coming.") The card's output is `total cieto sesenta hombres digas iviene reouerzo y canon`: the n of ciento is missing and refuerzo has s (plain o) for f. The pencil gloss gives both words, so all ten words are read from the decipherment of the time, and the card confirms nine of them and gives the last, cañón (CLESE, as in 1420.3-6).

## The cipher

The five pairs of letters L-A, N-E, R-I, S-O and T-U swap in place, in both directions; all other characters stay (`key.tsv`). The contributor takes the key from the Hernández key card in the same fonds, CMXV.16.1557.1, scan 16. The PR #831 review compared it with that scan (20 Nov 2026): the card is typed "Hernández : l n r s t / a e i o u", the five pairs of `key.tsv`. The same box holds the card headed "Herrera. Moreno." (scan 7) with which another telegram of the same fonds was read (`../mexico1911/`); that is a different key.

## Sibling telegrams of the same card (PR #831)

Daniel Jalkut applied the card to the Presidio telegrams of Braulio Hernández ("B. H. Leroy", "E. H. Leroy") of 27-31 March 1911 (`../duron1911/siblings/`; his notes there and in `../duron1911/WORKLOG.md`). The review's own decoder from `key.tsv` gives his decryption letter for letter (416 letters with this card). By telegram:

- CMXV.15.1430.3-3 (28 March): filed here (above).
- CMXV.15.1420.5-6 (27 March, 9:35 am): "[?Sánchez] [?tiene] [?cien] ochenta hom{b}res. Venga Villarreal [...] y tenga listo [...] [?cañón]. Salgo por él mañana [?a] [?mediodía]." 10 sure words of 19 (52.6%): read in part. All 20 groups compared with the CEHM image by the review.
- CMXV.15.1420.6-6 (27 March, 3:08 pm): salgo, hoy, carta, Luque, arreglos (5 of at least 10): decoded, not read.
- CMXV.15.1432.3-4 (29 March): total, Luque, entrevista (3 of 13 coded words): decoded, not read.
- CMXV.15.1447.1-3 (31 March, mostly clear): `revru Lorur Lichrh` = "invita sitiar Chih." (the review's reading) and `Orgtn` = sigue, 4 of 10 coded groups: decoded, not read.

These four are not filed in this profile yet: a "read in part" or "decoded, not read" text would make this target read in part (`docs/_texts.py` refuses a target classed read that holds one), and that change of class is the owner's to make. Until then their record is the contributor's files in `../duron1911/siblings/`.

## Remaining gaps

- A human check of the transcriptions and of the key card against the CEHM scans - blocker: needs-physical-access; the PR #831 review (an AI agent) compared the card with scan 16 and the groups of 1430.3-3 with its image over plain http, but no person has, the four coded words of 1420.3-6 were not compared with their image, and the images may not be redistributed
- Whether the telegrams are already in print (Narváez 2011 and 2019, the recipients' papers) - blocker: needs-physical-access; the contributors report none found, and the project did not search these books

## Escalation

- [x] siblings: the telegram of 19 May 1911 from the same fonds (`../mexico1911/`) read with another key card; five Presidio telegrams of 27-31 March 1911 decode with this card (PR #831): 1430.3-3 filed here, the other four in `../duron1911/siblings/` (see above)
- [x] clear-pages: the clear parts of 1420.3-6 read with the coded words, and no page is a decipherment of it; 1430.3-3 carries a pencil decipherment of the time on its form; neither is in the typed list CMXV.18.1795.1 (searched by the PR #831 contributor)
- [x] known-keys: the Hernández key card of the fonds (CMXV.16.1557.1 scan 16) is the key used
- [x] print: the contributors report no earlier publication found; the repository was checked by the project (no earlier reading of these telegrams)
- [n/a] key-rebuild: the key is the archive's card; nothing to rebuild for these coded words
- [n/a] retry: all coded words of both telegrams decode; nothing is left to retry

## Files

| File | Content |
|---|---|
| `transcription.txt` | the telegram of 27 March as transcribed (contributor) |
| `decryption.txt` | each coded word and its decryption |
| `reading.md`, `translation.md` | Spanish and English |
| `key.tsv` | the five letter pairs |
| `contributor_issue.md` | the submission as filed |
| `VERIFICATION.md` | what the project re-checked |
| `../duron1911/siblings/` | CMXV.15.1430.3-3 and the four other Hernández-card telegrams of PR #831: transcription, decryption, readings with translations (Daniel Jalkut's files, referenced from `profile.json`) |
| `profile.json` | the target profile |
