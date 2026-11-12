# Cipher telegrams to Setembrino de Carvalho, federal commander in Ceará (Juazeiro sedition), March-May 1914 (catalogue 1470)

Status: read in part (Brice Dudout, 12 Nov 2026; corrected at the integration check, 12 Nov 2026). By cipher group, which is the README's unit
(words), the seven telegrams in key MFTDBSJV are 92.3% read (168 of 182 groups with no restored letter and none unresolved) and the whole
file 83.8% (201 of 240). The contributor's own count is by cipher letter and gives 97.2% for the MFTDBSJV telegrams (1043 letters) and 95.8% for the
file (1440 letters); it is kept here once, labelled his, and the status he proposed ("read, with limited reserves") rested on it.

Reserves: (a) the formal pre-registered test of MFTDBSJV FAILED: S = 0.733 against the 0.85 criterion, because the pre-registered
lexicon was too small; the 0.865 comes from amendment A1, a larger lexicon chosen after that result, which is a changed rule and not a pass;
the controls stay below 0.13 either way, and the key is credible on other evidence (the pencil decipherment on the sheet agrees at every key position; the held-out telegrams read as
continuous Portuguese). (b) 10 March (LETCARIV, 82.8% of letters) and 20 May (OVHXZIRF, 95.1% of letters, 15 restored) are provisional: their keys are not validated.
(c) Two groups remain unread: MRELDTKRIMV (pagfis 1326) and SUQHSJU (pagfis 1328). The order of events (hashes frozen before the trials, single commits) is by the contributor's record.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, building on Daniel Bourdeau's vetting of 28 Oct and
3 Nov 2026 (`research/latam_vetting/1470_sample.txt`): he found the system (Vigenère, key of eight restarted at every word),
rebuilt MFTDBSJV from the pencil decipherment of the 14 March telegram, proposed LETCARIV for 10 March and made trial readings
of most March-April telegrams. Not published on the site. Text only: the CPDOC DocReader images are not reproduced.

## Documents

CPDOC/FGV, Arquivo Fernando Setembrino de Carvalho, FSC pce 1914.03.10/4 (DocReader bib FSC_PACEARA, pagfis 1317-1332, 16
images): telegrams from Rio de Janeiro to Fortaleza, 10 March - 20 May 1914, from the Minister of War Gen. Vespasiano de
Albuquerque, his aide-de-camp 1st Lt Rego Barros (Setembrino's son-in-law) and E. Pamplona, during the federal intervention in
Ceará against the Juazeiro rising: reports that the government palace of Fortaleza (Franco Rabelo) was mined, with the
engineer's description of the works under the palace; politics of the Ceará factions (Thomaz Cavalcanti, Liberato); the
telegraph staff; a reply to the Pernambuco judge pending the Supreme Court; a reserved warning (20 May) that the Minister was
displeased by the cipher part of a telegraph conversation. Twelve telegrams, ten with cipher; most sent twice (Ct repeats).

The 14 March telegram carries a contemporary pencil decipherment (a verification here, not a new reading). The pagfis 1326
correction telegram carries a contemporary pencil attempt that stops at "complot amli..."; its second group is still open.

## System and key

Vigenère, standard 26-letter alphabet, plain = cipher - key, key of eight letters restarted at every cipher group (a group is
one word, sometimes two short words run together). MFTDBSJV for 14 March - 17 April (Vespasiano, Rego Barros, Pamplona).
10 March (Pamplona) is close to LETCARIV, which differs from MFTDBSJV by one step in six of eight positions; the clerk mixed
the two. 20 May (Rego Barros) uses another key, OVHXZIRF, found here ciphertext-only (period 8, not about 10 as estimated in
the vetting). `key.tsv` lists the three.

## Validation

`prereg.md` (frozen before any key trial, in French), `amendment_A1.md`, `validation.txt`. MFTDBSJV was fixed on the 14 March
telegram and its pencil decipherment only, then measured on a held-out 731 letters (18 March + 17 April): with the
pre-registered lexicon S = 0.733: the pre-registered test FAILED (criterion 0.85; the misses are lexicon gaps); with the post-hoc enlarged lexicon of
amendment A1, chosen after that result, S = 0.865 against max 0.129 for 2000 controls. Both are reported; the first is the result of the test. LETCARIV and OVHXZIRF do not pass (short
portions, many slips): provisional.

## Reading

`transcription.txt` (blind, made from the images by an agent that saw no other file), `decryption.txt` (mechanical),
`reading.md` (clean Portuguese text), `reading_count.md` (marked reading, count per telegram), `translation.md` (English). Key MFTDBSJV: 1043 cipher letters, 1013
sure, 1 probable, 11 restored, 18 unresolved = 97.2% (98.3% with restored letters). Whole file 1440 letters, 95.8%.

New against the vetting sample: complete transcription and reading of no. 52414 (three sheets: the tiled room for the
archive, the staircase under the great hall, Lt Bizerril sent to Crato), "e o preparo" (two words run together), OJTUB =
Ceará (service note), "de cuja", "música", the 10 March text ("substituído ... actual encarregado ... merecerá tua
confiança") and the 20 May key and text.

## Remaining gaps

- pagfis 1326, second group MRELDTKRIMV (11 letters, "complot ..."), unresolved; the contemporary pencil attempt failed too; no word under any rotation of MFTDBSJV, LETCARIV, OVHXZIRF or LBQPOHVJ (integration check) - blocker: too-short; a transmission slip is likely and 11 letters give nothing to test it on
- pagfis 1328, SUQHSJU ("teme ataque ..."), unresolved; no word under any rotation of the four keys; "general" would need three slips - blocker: too-short
- 10 March and 20 May keys not validated by the pre-registered test (93 and 304 letters, held-out parts of 34 and 152 letters, many one-step and Morse slips) - blocker: too-short
- Transcription against the CPDOC images, and the cribs FSC pce 1914.02.19/2 (typed clear copies of Vespasiano's telegrams) and FSC cont 1914.10.07/2 (catalogue 1471): the DocReader pages load their images by JavaScript, so they need a browser session that the integrating session did not have - blocker: needs-physical-access

## Escalation

- [x] siblings: the other telegrams of the folder (pagfis 1317-1332) are all read; the repeats (Ct strips) were used to choose variants
- [x] clear-pages: the pencil decipherment on pagfis 1319 is the crib that gave the key; the typed clear copies FSC pce 1914.02.19/2 not opened (see gaps)
- [x] known-keys: MFTDBSJV, LETCARIV, OVHXZIRF and LBQPOHVJ (catalogue 1471, 7 Oct 1914) tried on the two unread groups under every rotation: no word
- [x] print: no printed edition of these telegrams found in the vetting; none searched further here
- [x] key-rebuild: OVHXZIRF found by hill climbing on the even groups of 20 May; LETCARIV not extended (93 letters)
- [x] retry: the unread groups and the doubtful letters were retried with all four keys and with the Ct repeats

## Integration check (12 Nov 2026)

Done by an independent session after the PR was merged into the branch; nothing in the contributor's files was changed except this NOTES.md and profile.json.

- Own decoder from `key.tsv`: 242 of 243 mechanical groups of `decryption.txt` are identical (OJTUB is shown from the sheet's service note).
- The scripts of the pre-registered test and the Portuguese lexicon are not in the repository; the test was not re-run. Its numbers agree across prereg.md, amendment_A1.md, validation.txt and this file.
- Strict count by cipher group, from the markers of `reading_count.md` (a group with a restored letter or unresolved counts as not read): MFTDBSJV telegrams 168 of 182 = 92.3% (92.9% if the one probable group, OJTUB read from the service note, counts); whole file 201 of 240 = 83.8%. The contributor's letter counts stay in the status line, labelled his.
- Class changed from read to read in part; the validation verdict is fail (the pre-registered test), with the amendment called what it is.
- Method: key recovered based on adjacent plaintext (the pencil decipherment on the sheet of 14 March, which is a verification and not a new reading); LETCARIV is Daniel Bourdeau's, OVHXZIRF is new.
- Images not compared (DocReader needs a browser); the claims of the write-up were reviewed line by line against this file and the profile.
