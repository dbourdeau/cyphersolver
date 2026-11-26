# breant1673: Bréant (Cologne) to M. de Réveillon (Kaiserswerth), 26 Dec 1673 and 8 Jan 1674, Médiathèque Georges-Delaw, Sedan, fonds Gourjault, carton 170: contemporary decipherment transcribed, nomenclator rebuilt from it

Status: read from the existing contemporary decipherment (Brice Dudout, 18 Nov 2026; 161 of 163 cipher words sure, 2 probable, 0 restored, 0 unresolved, 0.988); key rebuilt from it, 90 groups.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. No new reading is claimed: both letters carry a contemporary interlinear decipherment, so the content is existing. What is new is the transcription of the cipher, the alignment of the decipherment on it word by word, and the key as a reusable table.

## Source and credit

Médiathèque Georges-Delaw, Sedan, fonds Gourjault, carton 170, piece 3 (ff. 26-27, letter of 26 Dec 1673) and piece 4 (ff. 28-29, letter of 8 Jan 1674). The carton holds 6 pieces on 33 folios ("1 à 6 / 1 à 33" on its folder, written on the back of letters addressed to M. de Réveillon).

Images: Médiathèque Georges-Delaw, Sedan (fonds Gourjault, cartons 170 and 199), obtained through the Société d'histoire et d'archéologie du Sedanais (SHAS). The form of this credit has been asked of the SHAS and will be adjusted to its reply.

**No image is in this repository, and none may be added**: the photographs were sent for research use only. The shelfmark is given instead; the transcription is from those photographs. The digits are an AI transcription (Claude Opus 5.5 agents), with a human blind check of the doubtful shapes only (Brice Dudout, 18 Nov 2026), not a palaeographic check of the whole.

## The documents

| piece | folios | date | cipher | contemporary decipherment |
|---|---|---|---|---|
| 170-3 | ff. 26-27 | Cologne, 26 Dec 1673, signed Bréant, with a ciphered postscript | 245 groups, 96 cipher words | interlinear, word by word (a few blanks; one passage struck through by the decipherer) |
| 170-4 | ff. 28-29 | Cologne, 8 Jan 1674, signed Bréant; postscript in clear | 149 groups, 67 cipher words | interlinear, group by group (syllables) |

Bréant is a French agent at the Cologne peace congress (Dutch War); Réveillon commands the French garrison of Kaiserswerth, a Rhine place of the Elector of Cologne. On 26 Dec 1673 the French plenipotentiaries want to know whether he can hold the place with his French and Swiss troops, with Germans inside it as well, and they fear that the Elector ("M. de Cologne") may "turn his coat" and listen to the Emperor's proposals; Réveillon is to keep it between M. de Chamilly, himself and Bréant. On 8 Jan 1674 Bréant writes that the Elector has given his word to listen to no proposal from the Emperor until he has the King's answer to his letter, and that Réveillon will be warned in time.

## The system and the key (`key.tsv`)

Numerical syllabic nomenclator, groups 6 to 319, separated by colons on the page. Both letters use the same key (checked: 179 217 247 287 243 = "mpereur" in both, 296 = vous, 316 = z).

90 distinct groups: 61 sure (two or more consistent occurrences), 27 single (one occurrence, given by the decipherer and the word), 2 inferred (74, 319). Apart from the names (6 Roi, 24 M. de Chamilly, 47 M. de Cologne) and a few homophones (56, 93, 102, 106, 167, 257), the table is **approximately alphabetical**, from a = 55 to z = 316: it holds by initial letter, with whole words filed under it (estat 109, estre 119, faire 128, place 230, trouppes 284, tout 285, vous 296), but not strictly within a letter. Inversions: 103 ent before 104 en, 159 j before 163 il, 106/108 et before 109 estat and 113 ennemy, and 257 qui. Group 319 shows that the table goes beyond 316. u/v, i/j and s/z are not distinguished.

Four values rest on that approximate order and the context rather than on the decipherer alone (the three below, and 319 = sa/za in {casaque}, beyond 316): 208 = o (not vo: "propositions" = p-ro-po-si-ti-208-n-s, and 208 falls between 196 ni and 210 ont; of its two occurrences, one is in the struck-through {avoit}), 293 = vo ("envoyera"; this rests on the order, since the decipherer wrote "no" there) and 74 = ca (between 73 c and 75 ce, in the struck-through {casaque}). In `key.tsv`, 208 keeps the status `sure` (two occurrences) and 293 `single`: of the 61 sure groups, **only 208 rests on the order**; of the 27 single, only 293; the 2 inferred (74, 319) do too. The other 60 sure groups do not rest on the order. The header of `key.tsv` says the same; no value or status was changed.

Six readings of the decipherer disagree with the key; all are settled by the words: 153 = i ("informé", written "s"), 159 = j ("jusques", written "qu?"), 99 = e ("envoyera", written "t"), 221 = po ("point", written "pa"), 228 = par ("par un gentilhomme", written "pas") and 293 = vo ("envoyera", written "no"). A blind reading sheet of doubtful digit shapes (Brice Dudout, 18 Nov 2026, two controls passed) settled 163 (not 168) and 257 in the 1674 letter.

## Reading and counts (rule #728)

Files: `breant-1673-12-26_transcription.txt`, `breant-1674-01-08_transcription.txt` (cipher groups by passage), `breant-1673-12-26_decryption.txt`, `breant-1674-01-08_decryption.txt` (word by word: groups, key values, word, status, note), `reading.md` (both letters as sentences), `translation.md`.

| letter | cipher words | groups | sure | probable `{x}` | restored `[x]` | unresolved | sure share |
|---|---|---|---|---|---|---|---|
| 26 Dec 1673 | 96 | 245 | 94 | 2 | 0 | 0 | 0.979 |
| 8 Jan 1674 | 67 | 149 | 67 | 0 | 0 | 0 | 1.000 |
| both | 163 | 394 | 161 | 2 | 0 | 0 | 0.988 |

Only sure words count; a name code counts as one word. A word is sure when the contemporary decipherer, the key and the context agree. **"Sure" here means agreement with the contemporary gloss plus sense; it is not an independent test of the key**, which was rebuilt from that same gloss (the six values above where the gloss disagrees, 153, 159, 99, 221, 228 and 293, are settled by the words). The independent test is the Escalation item below. The two probable words, {avoit} (a-o-i-t, v not enciphered) and {casaque} (74 319 236 = ca-sa?-que), are in the one passage the decipherer struck through ("M. de Cologne avoit à tourner caza que"). Encipherer's slips that leave the word certain: one extra i (153) in "veuille", one extra e (99) in "sçaurez", the i of "faict" and the u of "j(u)ste" and "j(u)sques" not enciphered; a group struck through by the encipherer before "avec" in the postscript (57?) is left out.

Two group readings differ between our first word list of the 1674 letter and the aligned reading published here: "qu'il" before "ayt" in passage 3 (257 167 here, 257 164 in the first list) and "adverti" in passage 6 (243 here, 247 in the first list). Both words stay sure either way (164 and 167 are both l; the decipherer wrote "r(e)" over the second); they are to be looked at again on the image.

## Transcription doubts

From the files of this folder (the decryption notes and the paragraphs above). The photographs are for research use
only and are not in the repository: the image checks below are the contributor's (the blind reading sheet answered by
Brice Dudout on 18 Nov 2026, two controls passed, and the agents' passes), not checks made at the write-up of 24 Nov 2026.

- 163 or 168 (8 Jan 1674, passage 4, the second "qu'il", before "envoyera") - read: 163; checked: image, decode; blind reading sheet: 163, not 168; 239 163 = qu-il, where 168 = la gives no word
- 257 (8 Jan 1674, passage 3, "qu'il" before "ayt") - read: 257; checked: image, decode; blind reading sheet: 257; 257 167 = qui-l; the only occurrence of 257 in the two letters
- 167 or 164 (8 Jan 1674, passage 3, the group after 257) - read: 167; checked: image (two readings by the contributor's agents, 164 in the first word list and 167 in the aligned reading, not looked at again), decode; 164 and 167 are both l in the key, so the word is "qu'il" either way; the digit stays open
- 243 or 247 (8 Jan 1674, passage 6, "adverti") - read: 243; checked: image (two readings by the contributor's agents, 247 in the first word list and 243 in the aligned reading, not looked at again), decode; 243 = r gives a-d-ve-r-ti and 247 = re gives a-d-ve-re-ti; the decipherer wrote "r(e)" over the group; the word is "adverti" either way; the digit stays open
- a group struck through before 102 (26 Dec 1673, postscript, "avec") - read: left out, perhaps 57; checked: image, decode; the encipherer struck it through; 57 = av would complete av-e-c, and the decipherer wrote "avec"; it is not in the transcription and not in the counts

## Prior work

Nothing in `catalogue.json` or `research/leads.json` (main 42068aa8, 19 Nov 2026), in the targets, or in the open pull requests for Gourjault, Bréant, Baluze, Réveillon or Sedan; no printed edition of the decipherment found by web search (18 Nov 2026). The contemporary decipherment on the letters is credited as prior solution.

## Remaining gaps

- {avoit} and {casaque}: in the struck-through passage, 74 and 319 inferred from the approximately alphabetical order (blocker: too-short).

Not gaps in the cipher, but said here: the writer's clear text is not transcribed in full ("(…)" in the reading; it holds no cipher), and the digits are an AI transcription (one agent reader), with a human blind check of the doubtful shapes only, not a palaeographic check of the whole.

## Escalation / independent test

- Other letters of the same correspondence (carton 170, pieces 1-2 and 5-6) would test the key on a text not used to build it. A question on the other ciphered pieces of cartons 170 and 199 was sent to the library on 18 Nov 2026.

### Carton 170.1, ff. 3-4 (19 Nov 2026): not measurable, descriptive only

Source: Médiathèque Georges-Delaw, Sedan, fonds Gourjault, carton 170.1, obtained through the SHAS (the form of the credit is still to be confirmed, as for the other pieces). No image, crop or full transcription of this letter is in the repository; only this summary and the figures.

- The piece: Louvois to M. de Réveillon, Versailles, 19 March 1674, marked "Duplicata" (the only ciphered letter of the 17 in carton 170.1, all from Louvois to Réveillon). Same nomenclator, 201 groups, with a contemporary gloss group by group. The table is therefore the Louvois–Réveillon table, which Bréant also used. Content (existing, from the gloss): Réveillon is to leave Kaiserswerth with all the King's troops on the order of Courtin and Barrillon, and to leave the munitions and artillery against a receipt from the Elector of Cologne's officer.
- Preregistration in this folder, as frozen (in French, unchanged so that the hashes hold): `c170-1/PREREG.md` (SHA-256 3e5b337b45f39bf46d063514f2a5be4e52b8ace9792ca96cba5e399d6449e88f, written 19 Nov 2026 16:12, before the first transcription pass at 16:18) and `c170-1/PREREG-ADDENDUM-fusion.md` (fusion rules written after the two passes and the arbitration, before any decoding; SHA-256 80002b78a5726d87d6f42e89dbe7879092eb9820efbe388ed175f9cf67a673cb); `c170-1/PREREG.sha256` lists these and the hashes of the working files (transcription passes, arbitration, measurement script and result), which stay out of the repository with the images. The frozen key `key-pr798-1abb47a.tsv` is `key.tsv` at commit 1abb47a (SHA-256 25052e57...a42221), which anyone can check from git. The times are those of our own log; the hash was not published before the transcription, so "before" rests on that log.
- Protocol: preregistration frozen by SHA-256 before any transcription (exposure declared: the writing agent knew the key, so it neither transcribed nor arbitrated). Two blind transcriptions without the key (201/201 groups identical), blind arbitration of the doubtful cases, one measurement with the key of this PR as is (key.tsv at 1abb47a, no value added or corrected). Measure: share of groups whose key value equals the normalised gloss, on groups with sure digits, in the key and with a legible gloss of their own; criterion fixed in advance: M ≥ 0.85 and M ≥ best of 200 permuted-key controls + 0.30, with at least 300 gloss letters.
- **Result: not measurable (282 < 300 gloss letters).** The figures are descriptive only: M = 0.879 (145/165), best of 200 controls 0.127 (mean 0.016). The 20 disagreements are all readings of the gloss's letter shapes (v read n in "vous" ×6, u read "&" or n, t/f/long s, etc.); none calls for another key value.
- 208 = o is confirmed independently ("munitions"); 293 and 74 do not occur.
- 9 new values given by the gloss fall between their neighbours in the key: 62 ba, 94 di, 111 elle, 125 fi, 131 g, 172 lo, 190 mu, 209 ordre, 218 pi. None is added to key.tsv.
- Rule #728 count of this letter with the key alone: 62 of 78 cipher words sure (79.5 %); not "read" by the key, content existing.
- The formal independent test stays open: it needs another letter with at least 300 gloss letters (cartons 170.2 to 170.4, or the Louvois correspondence at the Service historique de la Défense, series A1).
- Checked at the write-up (24 Nov 2026, AI agent for the maintainers): `c170-1/PREREG.md` and `c170-1/PREREG-ADDENDUM-fusion.md` hash to the two values above when taken from git (LF line ends; a Windows checkout with CRLF gives other values). 25052e57...a42221 is `key.tsv` as first committed in this repository (e733944d4c; the pull request's 1abb47a is not an object here after the rebase). The later commit 701f67c27e changed only the header comments: the 90 data rows are identical. The working files of the test (passes, arbitration, script, result) are not in the repository, so the figures of the result were not recomputed here.

## Tools

Claude Opus 5.5 agents (transcription from the photographs, alignment, key, write-up); Brice Dudout chose the target, answered the blind reading sheet and set the counting rule. No model API calls.
