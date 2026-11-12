# Cipher telegrams to Setembrino de Carvalho, federal commander in Ceará (Juazeiro sedition), March-May 1914 (catalogue 1470)

Status: read, with limited reserves (Brice Dudout, 12 Nov 2026; the seven telegrams in key MFTDBSJV are read, 1043 cipher letters, 97.2%; whole file 1440 letters, 95.8%).

Reserves: (a) the formal pre-registered test of MFTDBSJV scored 0.733, under its 0.85 threshold, because the pre-registered
lexicon was too small; the 0.865 comes from amendment A1, frozen after that first result; the controls stay below 0.13 either
way. (b) 10 March (LETCARIV, 82.8%) and 20 May (OVHXZIRF, 95.1%) are provisional: their keys are not validated. (c) Two groups
remain unread: MRELDTKRIMV (pagfis 1326) and SUQHSJU (pagfis 1328).

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
pre-registered lexicon S = 0.733 (criterion 0.85 not met; misses are lexicon gaps), with the post-hoc enlarged lexicon of
amendment A1 S = 0.865 against max 0.129 for 2000 controls. Both are reported. LETCARIV and OVHXZIRF do not pass (short
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

- pagfis 1326, second group MRELDTKRIMV (11 letters, "complot ..."), unresolved; the contemporary pencil attempt failed too - blocker: keying-or-transmission-error.
- pagfis 1328, SUQHSJU ("teme ataque ..."), unresolved - blocker: keying-or-transmission-error.
- 10 March and 20 May keys not validated by the pre-registered test (93 and 304 letters, many one-step and Morse slips) - blocker: short-text.
- Cribs not used: FSC pce 1914.02.19/2 (typed clear copies of Vespasiano's telegrams) and FSC cont 1914.10.07/2 (catalogue 1471, key LBQPOHVJ) - next step: compare the clear copies with the March telegrams.
