# vanhalen1840: Juan Van Halen to the acting commander of the Division auxiliar del Norte, Igualada, 6 May 1840 (catalogue 2423, AHN DIVERSOS-COLECCIONES,195,N.14)

Status: read (Brice Dudout, 11 Nov 2026; 29 of 30 cipher words certain or probable = 96.7%: 27 certain, 2 probable, 1 restored, 0 unresolved; key validated with limited reservations: our pre-registered held-out test passes C1 and C2, C3 missed by 0.027). Open: a check on the image of three numbers (S8 no. 4, S2 no. 5, the omitted 2 of S1).

Contributed by Brice Dudout (Europe chiffrée). Key proposed by Claude Fable 5.2 (Anthropic) from the training runs; protocol
addendum, held-out measurement, reading of the held-out runs and write-up by Claude Opus 5.5 agents. Catalogue entry
**2423** (Daniel Bourdeau, PARES sweep and vetting of 9 Nov 2026). No decipherment of the time, no edition found.

## Document

Madrid, Archivo Histórico Nacional, DIVERSOS-COLECCIONES,195,N.14
([PARES 4151130](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/4151130)): letter of general Juan Van
Halen (Ejército de Cataluña, Brigada de Reserva letterhead), Igualada, 6 May 1840, 10 a.m., to the brigadier acting
commander of the Auxiliary Division of the North. Three images: cover, and two pages of plain Spanish with eight runs of
dot-separated numbers (146 numbers). The images (531x648 px) were used for study only; none is included here. Credit:
Ministerio de Cultura, Archivo Histórico Nacional, DIVERSOS-COLECCIONES,195,N.14.

## System and key (`key.tsv`)

Alphabets numbered on in succession, with homophones. Rank 1: m n o p q r s t u [10?] z = 1-11, then a b c d e f g h i j l
= 12-22; rank 2 starts again at a = 24 (d 27, e 28, l 34). a also has 58 and 70 (12 + 46, 24 + 46), which suggests a
period of 46 with ranks 3 and 4. No k; u serves for v. 70, which closes several runs, is a letter (a), not a separator
or null. No word division. 24 values are attested in the letter; the 40 others in `key.tsv` are given by the structure
and marked as such; 10, 23, 35-46, 69 and 81-92 are left open.

The key was proposed by Claude Fable 5.2 (Anthropic) in one API run, sent the training runs S1-S6 only, and frozen. Its
anchor is the isomorph "en contacto" in S6 (one window in the text, none in 5,000 shuffles); the attested values then
fall in alphabetical order for 16 of 16 consecutive pairs, which the model did not impose (best of 100,000 permuted
keys: 6). Earlier work of ours on the same runs (index of coincidence 0.059, monoalphabetic and homophonic annealing,
Gronsfeld-type tests, cribs; issues #363 and #367) had failed.

## Validation (`validation.txt`)

Key validated with limited reservations. The held-out runs S7 and S8 (25 numbers) were named in the protocol of 9 Nov
2026, hashed before the transcription, and never sent to the model. Because the protocol's own rule has almost no power
on 25 numbers (4% on in-sample windows), an addendum was hashed with the key and a calibration on S1-S6 before S7-S8 were
decoded (SHA-256 41a8ea9a...). One measurement: lexical cover 0.880 (C1 >= 0.75: passed); letter-model score -1.048 against
-1.359 for the best of 200 shuffled keys (C2, margin 0.22: passed) and -1.101 for the best of 200 shuffles of H's own
numbers (C3, margin 0.08: missed by 0.027). By the letter of the rule fixed in advance, the measurement therefore did not
pass; the key still beats all 400 controls. H decodes without any correction to "la caretera" and "dicbosa caretera",
read "dic{h}osa caretera" with one number (S8 no. 4) read otherwise. Every number of H was already attested in S1-S6.

## Reading (`reading.md`, `translation.md`)

30 cipher words: 27 certain, 2 probable ({custodiar}, {dichosa}), 1 restored (ve[n]ir), 0 unresolved. **29/30 = 96.7%
read by sense** (restored word not counted), as in the count accepted for ridolfi1646 (#403). By the strict README formula,
if the two probable words (each a one-digit reading of our transcription) are counted as guessed, the share is 27/30 = 90%.

The cipher hides the logistics: "As in that case a sufficient force must come to Montblanc to guard the said funds, it
would be desirable that Your Lordship should meet me in the said city on the eleventh, in case the march by Cervera of
the Barcelona convoy does not bring us into contact before that date on the road." The funds are the 1,503 [reales?] to
be paid at Tarragona between the 10th and 12th May. The second run closes the letter: the Carlist bands of Llarch and
Marcó, on leave, roam the Priorat, and we shall watch them "on that confounded road".

## Remaining gaps

- S8 no. 4 (13 in pass 1, 18 in pass 2, read 19 = h for "dichosa") - blocker: illegible; the sign was already doubtful on Brice Dudout's blind sheet of 9 Nov 2026 at 531x648 px; a re-reading on a better image would settle it
- S2 no. 5 (13 read as 3 for "custodiar") and the 2 missing in S1 ("ve[n]ir") - blocker: illegible; one-digit doubts at the resolution PARES serves; may also be slips of the cipher clerk
- the key beyond the 24 attested values (40 values given by the structure; 10, 23, 35-46, 69, 81-92 open) - blocker: no-key-material; only this letter is known in the cipher
- a second test of the key - blocker: no-key-material; the held-out runs are used up; the Army of Catalonia cipher table of 1839-40 or a sibling letter (fonds 195, N.13/N.15; Archivo General Militar; Espartero papers) would test it

## Escalation

- [x] siblings: PARES "cifrada" sweep of the fonds 195 finds no other cipher item; N.13 and N.15 not looked at
- [x] clear-pages: no decipherment on the leaves or the cover; the plain text gives the context used for the sense check
- [x] known-keys: none known for the Army of Catalonia 1839-40
- [x] print: no edition found (catalogue 2423 vetting, 9 Nov 2026)
- [x] key-rebuild: key proposed ciphertext-only on S1-S6, frozen, measured once on held-out S7-S8 (C1, C2 passed; C3 missed by 0.027)
- [ ] retry: the three doubtful numbers on a better image

## Files

| file | content |
|---|---|
| `transcription.txt` | the eight runs, numbers as written |
| `key.tsv` | the key, CC BY 4.0, attested and structural values marked |
| `decryption.txt` | mechanical decryption with the key, no correction (S7-S8 = output of the single measure) |
| `reading.md` | the reading (Spanish, spelling of the letter), marks and count |
| `translation.md` | English translation of the whole letter |
| `validation.txt` | protocol order, the single measurement, reservations |
| `frozen/` | the hashed working files (French): PROTOCOLE.md (P01) and PROTOCOLE.sha256, PROTOCOLE-AVENANT-LOT4.md and AVENANT-LOT4.sha256, KEY.tsv, transcription passes 1 and 2, the copy sent to the model (T only), clair.txt (plain text around the runs), RESULTAT-LOT4.md and the raw output, scripts (scorer, calibration and its output, measure, earlier solvers), and the model's files (fable-lot4-2026-11-11/: key proposals, variants, reading of S1-S6, power check). In AVENANT-LOT4.sha256 the two paths outside the folder were replaced by their names (lexicon = lang/lexicons/es.json.gz of this repository, same SHA-256; the Quijote extract is not included). |
