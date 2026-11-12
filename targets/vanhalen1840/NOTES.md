# vanhalen1840: Juan Van Halen to the acting commander of the Division auxiliar del Norte, Igualada, 6 May 1840 (catalogue 2423, AHN DIVERSOS-COLECCIONES,195,N.14)

Status: read in part (Brice Dudout, 11 Nov 2026; integration check 12 Nov 2026). 27 of 30 cipher words read without correction = 90.0% by the README read bar (2 more words each need one number read otherwise, 1 needs a number supplied). Key proposed from the ciphertext of runs S1-S6; the contributor's pre-registered test on the held-out runs S7-S8 FAILED (condition C3 missed by 0.027; the original rule also not met), so the key is partial under the contributor's own frozen protocol. Open: three doubtful numbers (S8 no. 4, S2 no. 5, the omitted 2 of S1) and the transcription as a whole, not checked on the images.

Contributed by Brice Dudout (Europe chiffrée), pull request #408. Key proposed by Claude Fable 5.2 (Anthropic) from the training runs; protocol
addendum, held-out measurement, reading of the held-out runs and first notes by Claude Opus 5.5 agents. Catalogue entry
**2423** (Daniel Bourdeau, PARES sweep and vetting of 9 Nov 2026). No decipherment of the time, no edition found.

## Document

Madrid, Archivo Histórico Nacional, DIVERSOS-COLECCIONES,195,N.14
([PARES 4151130](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/4151130)): letter of general Juan Van
Halen (Ejército de Cataluña, Brigada de Reserva letterhead), Igualada, 6 May 1840, 10 a.m., to the brigadier acting
commander of the Auxiliary Division of the North. Three images: cover, and two pages of plain Spanish with eight runs of
dot-separated numbers: 144 numbers in `transcription.txt` (119 in S1-S6, 25 in S7-S8), 24 distinct. The contributor
counted 146, which holds only if the two "58" are read as "5.8"; the key reads 58 as one number. The images
(531x648 px) were used for study only; none is included here. Credit: Ministerio de Cultura, Archivo Histórico Nacional,
DIVERSOS-COLECCIONES,195,N.14.

## System and key (`key.tsv`)

Alphabets numbered on in succession, with homophones. Rank 1: m n o p q r s t u [10?] z = 1-11, then a b c d e f g h i j l
= 12-22; rank 2 starts again at a = 24 (d 27, e 28, l 34). a also has 58 and 70 (12 + 46, 24 + 46), which suggests a
period of 46 with ranks 3 and 4. No k; u serves for v. 70, which closes several runs, is a letter (a), not a separator
or null. No word division.

**24 values are attested**: they are the 24 distinct numbers of the letter, and they are the recovered part of the key.
**The 40 other rows of `key.tsv` are conjecture.** They follow from the structure (ranks 1-2 by alphabetical order,
ranks 3-4 by the period of 46), none of them occurs anywhere in the letter, and nothing here tests them. Ranks 3-4 rest
on two observed numbers only, 58 and 70; the proposer's own `frozen/fable-lot4-2026-11-11/KEY-VARIANTES.md` calls them
fragile and gives a variant in which 58 and 70 are plain extra homophones of a and those rows are wrong. 10, 23, 35-46,
69 and 81-92 are left open.

The key was proposed by Claude Fable 5.2 (Anthropic) in one API run, sent the training runs S1-S6 only, and frozen. Its
anchor is the isomorph "en contacto" in S6 (one window in the text, none in 5,000 shuffles); the attested values then
fall in alphabetical order for 16 of 16 consecutive pairs, which the model did not impose (best of 100,000 permuted
keys: 6). Earlier work of ours on the same runs (index of coincidence 0.059, monoalphabetic and homophonic annealing,
Gronsfeld-type tests, cribs; issues #363 and #367) had failed.

## Validation (`validation.txt`): the pre-registered test failed

**What was declared.** The protocol of 9 Nov 2026 (`frozen/PROTOCOLE.md`, P01) named the runs S7 and S8 (25 numbers) as
held out and they were never sent to the model. Its rule: lexical cover >= 0.85 and >= the best shuffled-key control
+ 0.30. Because that rule has almost no power on 25 numbers (4% on in-sample windows), an addendum
(`frozen/PROTOCOLE-AVENANT-LOT4.md`, SHA-256 41a8ea9a...) replaced it with three conditions, thresholds calibrated on
S1-S6: C1 cover >= 0.75; C2 letter-model score >= best of 200 shuffled keys + 0.22; C3 letter-model score >= best of
200 shuffles of the held-out numbers + 0.08; the measure passes only if all three hold. The addendum (section 5) also
says what a failure means: "MESURE NON VALIDÉE -> clé PARTIELLE", whatever the sense.

**Order of events, by the contributor's record.** The files say that the addendum was hashed with the key and the
calibration before S7-S8 were decoded (addendum frozen 14:17:49 CET, measurement 14:18, on 11 Nov 2026). The pull
request is a single commit (14:29) and there is no outside timestamp, so this order rests on the contributor's word.
The addendum was written after the key and the reading of S1-S6 existed, and it declares that its author had seen the
lengths of the held-out runs and the number of "70" in them.

**The score.** One measurement (`frozen/RESULTAT-LOT4-sortie-brute.txt`):
- original rule P01: cover 0.880, best control 0.760, margin 0.120 against 0.30 required: **not met**;
- C1: cover 0.880 >= 0.75: passed;
- C2: letter-model score -1.048 against -1.359 for the best of 200 shuffled keys (needed -1.139): passed;
- C3: -1.048 against -1.101 for the best of 200 shuffles of the held-out numbers (needed -1.021): **failed, short by 0.027**.

**Verdict: the test failed**, under the addendum and under the original rule. The contributor's frozen result file
(`frozen/RESULTAT-LOT4.md`) says so: "MESURE LOT4 : NON VALIDÉE", "Clé : PARTIELLE", "pas de publication". The pull
request's wording "validated with limited reservations" was a relabelling made after the result; it is withdrawn here.
The held-out runs are used up: no second measurement can be made on this letter.

**What else makes the key credible** (none of this is the pre-registered test):
- the 24 attested values run in alphabetical order (m...z = 1-11, a...i = 12-20, a/d/e/l = 24/27/28/34), 16 of 16
  consecutive pairs by the contributor's count (best of 100,000 permuted keys: 6; this figure was not re-run at integration);
- the six training runs give continuous Spanish that fits the clear words on both sides of every run;
- the held-out run S7 decodes with no correction to "la caretera", the complement the clear "sobre" asks for;
- every number of S7-S8 was already attested in S1-S6 (14 distinct, none new), so the held-out decode uses no conjectural value;
- against larger controls made at the independent verification: 0 of 6,000 shuffled keys and 5 of 6,000 shuffles of the
  held-out numbers score as well as the key.

Against it: S8 "dicbosa" becomes "dichosa" only if S8 no. 4 (13 in pass 1, 18 in pass 2) is read 19, a confusion outside
the classes the addendum declared, and the contributor's own sense check for S8 is recorded as not met. A test on 25
numbers that uses only values already fitted cannot carry "validated" on its own.

## Reading (`reading.md`, `translation.md`)

30 cipher words: 27 read with no correction, 2 probable ({custodiar}, {dichosa}: one number read otherwise each),
1 restored (ve[n]ir: one number supplied), 0 unresolved. **By the README read bar, 27/30 = 90.0%**: a guessed word and
a supplied word do not count as read. The class is therefore **read in part** (under 95%). At 30 words one word is
3.3 points, so the bar allows a single doubtful word. The contributor's count was 29/30 = 96.7% (probable words counted
as read); it is not used here.

The cipher hides the logistics: "As in that case a sufficient force must come to Montblanc to guard the said funds, it
would be desirable that Your Lordship should meet me in the said city on the eleventh, in case the march by Cervera of
the Barcelona convoy does not bring us into contact before that date on the road." The funds are the 1,503 [reales?] to
be paid at Tarragona between the 10th and 12th May. The second run closes the letter: the Carlist bands of Llarch and
Marcó, on leave, roam the Priorat, and we shall watch them "on that confounded road" (the plain words just before this
run are uncertain readings at the resolution of the images).

## Integration check (12 Nov 2026)

Pull request #408 was verified independently before integration (read-only; the report is summarised here) and the
corrections were applied to this folder.

Reproduced:
- SHA-256 of every frozen file (protocol, addendum, key, scripts, calibration output, both transcription passes, the
  copy sent to the model) matches; `key.tsv` has the same 64 values as `frozen/KEY.tsv`.
- A second decoder written from `key.tsv` gives the same eight strings as `decryption.txt`, 0 differences.
- The original rule re-run with `frozen/scripts/measure.py` unchanged: cover 0.880, best control 0.760, margin 0.120.
- C1 0.880; C2 -1.051 against -1.357; C3 -1.051 against -1.102, missed by 0.029. The third-decimal differences come
  from the letter-model corpus: the contributor's Don Quijote extract is not in the pull request, and the Gutenberg
  text was used instead.
- Calibration re-run (`calib_lot4.py`): thresholds 0.75 / 0.21 / 0.08, power 82.7% (contributor: 0.75 / 0.22 / 0.08,
  82.0%); power of the original rule 4.3%.
- Word count of `reading.md`: 30 words, 27 / 2 / 1.

Found:
- With pass 2 of the transcription (S8 no. 4 = 18) C3 would pass by 0.004. Pass 1 was declared decisive beforehand, so
  the failure stands, but the outcome turns on one doubtful digit.
- C3 depends on the random seed: it passes in only 3 to 6 of 30 blocks of 200 shuffles.
- The 40 structural key values occur nowhere in the letter.
- `docs/_check_reading.py` scores `reading.md` 0.659 (marginal) because the file is mostly English notes; the Spanish
  sentences themselves were read against `translation.md` and construe (reading_review A, three marked holes).

Corrected in this folder: status and class (read in part, 0.90); "validated with limited reservations" removed from
NOTES, `profile.json` and `validation.txt`; 144 numbers, not 146; the 40 structural values labelled conjecture
(`key.tsv` header, here, profile); the order of events marked as the contributor's record; `outcome.key` partial;
profile verification step set to failed.

Not done: **the transcription was not checked against the images.** PARES answered HTTP 429 to three attempts at
verification and again at integration on 12 Nov 2026 (one connection reset, one 429), and no browser was available to the integrating
session. The three doubtful numbers remain unchecked. This source needs a browser session (Chrome).

## Remaining gaps

- S8 no. 4 (13 in pass 1, 18 in pass 2, read 19 = h for "dichosa") - blocker: illegible; the sign was already doubtful on Brice Dudout's blind sheet of 9 Nov 2026 at 531x648 px; a re-reading on a better image would settle it; PARES refused scripted access (HTTP 429) on 12 Nov 2026
- S2 no. 5 (13 read as 3 for "custodiar") and the 2 missing in S1 ("ve[n]ir") - blocker: illegible; one-digit doubts at the resolution PARES serves; may also be slips of the cipher clerk; not checked on the image (PARES HTTP 429)
- the transcription of all eight runs against the images - blocker: illegible; made by an AI agent from 531x648 px images with one blind human check of 12 signs; not checked at integration because PARES answered HTTP 429 and no browser was available
- the key beyond the 24 attested values (40 values given by the structure, conjecture; 10, 23, 35-46, 69, 81-92 open) - blocker: no-key-material; only this letter is known in the cipher and none of those numbers occurs in it
- a second test of the key - blocker: no-key-material; the held-out runs are used up and the one pre-registered test failed; the Army of Catalonia cipher table of 1839-40 or a sibling letter (fonds 195, N.13/N.15; Archivo General Militar; Espartero papers) would test it

## Escalation

- [x] siblings: PARES "cifrada" sweep of the fonds 195 finds no other cipher item; N.13 and N.15 not looked at
- [x] clear-pages: no decipherment on the leaves or the cover; the plain text gives the context used for the sense check
- [x] known-keys: none known for the Army of Catalonia 1839-40
- [x] print: no edition found (catalogue 2423 vetting, 9 Nov 2026)
- [x] key-rebuild: key proposed ciphertext-only on S1-S6, frozen, measured once on held-out S7-S8: the test failed (C1, C2 passed; C3 missed by 0.027)
- [n/a] retry: the three doubtful numbers can only be settled on a better image, and PARES refused scripted access (HTTP 429) on 12 Nov 2026; nothing else is unread

## Files

| file | content |
|---|---|
| `transcription.txt` | the eight runs, numbers as written |
| `key.tsv` | the key, CC BY 4.0, attested values and conjectural (structural) values marked |
| `decryption.txt` | mechanical decryption with the key, no correction (S7-S8 = output of the single measure) |
| `reading.md` | the reading (Spanish, spelling of the letter), marks and count |
| `translation.md` | English translation of the whole letter |
| `validation.txt` | protocol order, the single measurement (failed), other evidence |
| `frozen/` | the hashed working files (French): PROTOCOLE.md (P01) and PROTOCOLE.sha256, PROTOCOLE-AVENANT-LOT4.md and AVENANT-LOT4.sha256, KEY.tsv, transcription passes 1 and 2, the copy sent to the model (T only), clair.txt (plain text around the runs), RESULTAT-LOT4.md and the raw output, scripts (scorer, calibration and its output, measure, earlier solvers), and the model's files (fable-lot4-2026-11-11/: key proposals, variants, reading of S1-S6, power check). In AVENANT-LOT4.sha256 the two paths outside the folder were replaced by their names (lexicon = lang/lexicons/es.json.gz of this repository, same SHA-256; the Quijote extract is not included). |
