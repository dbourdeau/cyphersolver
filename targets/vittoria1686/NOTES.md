# vittoria1686: Vittoria Gonzaga to her brother, catalogue 1570

Read in part, key recovered from ciphertext-only: five letters, 379 of 422 cipher words sure (89.8%, 43 holes), counted by `scripts/count_words.py` on 24 Nov 2026 (section "The fifth letter, 24 Nov 2026" at the end). At a stopping point: every hole has an outside blocker. The fifth letter (cc. 24v-25r, 18 Sept 1691) was transcribed, decrypted and read on 24 Nov 2026 by an AI agent for the maintainers; its reading has no reading review yet and needs a second reader. Letters 1-4: Matthew Kennedy's completion of 21-23 Nov 2026 (PR #853, `kennedy_2026/`), integrated on 24 Nov 2026. The table and the paragraphs down to "Decrypt audit" are WAINUT's of 3 Nov 2026 (PR #226: 172 of 198 number words, 86.9%, on the passages then transcribed) and are kept as he wrote them.

Worked 3 Nov 2026 by WAINUT with AI language-model agents viewing the images. No human palaeographer has checked it.

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera G, Gonzaga, Vittoria (Sec. XVII-XVIII), cc. 3-4, 11-12, 20-21, 22-23. Letters of a nun at Santa Chiara, Naples, 1686-91.

| Status | Number words | As sense (A) | No restored or changed letter (C) | Doubtful | Not read |
|---|---|---|---|---|---|
| read in part | 198 | 172 (86.9%) | 172 (86.9%) | 17 | 9 |

A and C are equal because no word carries a marked repair: where a group fails, the word is printed as a proposal and left out. Code group 104 (che) counts as sense in both. The 95% bar is not met. Per page in `repairs_numbers.md`; the counts are from `scripts/check_marks.py numbers`. They cover number words only.

An earlier claim of 105 of 132 (80%) held only for what had then been transcribed. All number lines on cc. 20r, 21r and 22v are now transcribed from native-size tiles. Low-resolution views of cc. 3r, 4v, 11v, 12r, 20v, 21v and 23v show no numbers; c. 12v was not viewed.

## Images

Estense IIIF, CC BY-NC-SA, linked and not committed. Manifests at `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest`: c9e23554-5ac5-4f19-b69a-2afff92d9bd5 (cc. 3-4), bf531a45-4b5f-4dcc-8fa6-b998f8688d4a (cc. 11-12), 6d986a52-84d8-4c9d-b9b4-98a326d97739 (cc. 20-21), e7f8b77c-bdcb-43d1-843b-bea02df7f201 (cc. 22-23). A whole page is served at about 1400 px, but region requests return native size (about 5000 px page width).

## System

Simple substitution by number, with spaces left between words. The alphabet is numbered in fives with each neighbouring pair swapped: a 10, b 5, c 20, d 15, e 30, f 25, g 40, h 35, i 50, l 45, m 60, n 55, o 70, p 65, q 80, r 75, s 90, t 85. Two signs are off the pattern: o is usually 7, and u/v is 2 where the pattern predicts 100; 2 2 is the pair vu, as in vuole at 3v.2 and 21r.3. A stroke over a group doubles the letter (danno, 20r.2). Code groups: 104 che, context only, fits all 10 uses; 159 perhaps per, 2 uses, doubtful; 109 and 182 not identified.

## Key and tests

The table was built by hand from cc. 3v and 4r (fidarci di nessuno, Paulo, nulla, sequestro), the writer leaving the word divisions. It is not from a contemporary decipherment. The swapped-pair pattern is a further check, since the table was not built on it.

- **Independent blind check** (`VERIFY.md`, unchanged). An agent read 57 groups of cc. 20r and 21r from native tiles before seeing the table: 5 disagreements, 8.8%. All resolved on zoom, none against the solver. Its digits, decrypted with the table, score -10.452 against shuffled tables mean -15.147, best -13.197 (500 tables). Injective annealing on 224 groups blind, with no key, recovered 11 of the 18 letter values.
- **The lines added on 3 Nov are not blind.** They were read after the check, by one agent who knew the key. `retranscription_log_1570.tsv` lists 21 changes from first read to final, in about 290 groups, and one sign kept against the sense. Most were settled by shape on zoom plus sense, and 10 against 20, 45 against 55 and 85, and 3 against 5 are close in this hand. A lone l or t rests partly on sense. These words were not read by anyone else, though the check's first-pass digits gave the same outline: "di Torre Maggiore mi ha fatto scrivere da Pompeo", "facci havere", "tratte di grano", "risposto con cerim. e che", "erano aperte le tratte", "porte di ferro", "disturbare il carico", "sarebbe stato il maggior danno d'interesse da".
- **Disagreement logged.** 21r.4 first group: the check gives t'ho (85 35 7); under the blot the solver reads 45, l'ho, which fits a reply to Pompeo's message. The shape does not decide it. The reading keeps [?l'ho].
- cc. 3v, 4r, 11r, 22r, 23r were read at about 1400 px only, and the transcription was typed after the table was known; four groups were first read differently (listed at the end of `transcription_numbers.txt`). No blind reader saw them. Their weak words ([?sperate], [?sequestratore], spaltta) may improve at native size.

## Context

Mainly Neapolitan estate business: the sequestration of San Paolo by Don Paolo Ruffo, the Marquis of Casalnuovo, Bisceglia, the Collaterale, grain licences (tratte), the Camera, a plea for a safeguard. The Sangro family held Torremaggiore in this period, which would fit a title for group 109; this is from memory and not checked. Dates and names here are as the letters give them. No person is identified from outside sources.

## Prior art: open

Checked 3 Nov 2026. One web search (Vittoria Gonzaga 1691 with Ruffo, San Paolo, Bisceglia) found no edition. That does not clear the letters. Nothing here is claimed as new, and `first_break` is left out of the profile. This repository has no target folder for them at head 3c777efd5; `catalogue.json` lists entry 1570 as an open lead.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/detail.py vittoria1686` re-applies `key.tsv` to `transcription_numbers.txt` and compares the letters with `reading_numbers.md`: 92 of 239 compared words depart (38%), key covering 78% of the tokens. Checked with an own read-only snippet (the folder's scripts were not run).

- **The key gives the decryption.** `key.tsv` applied to `transcription_numbers.txt` gives `decryption_numbers.txt` in 37 of 37 lines.
- **The reading is the marked source with the marks taken off.** The Italian part of `edit_numbers.txt`, with `<< >>` and the `=signs` notes removed, is `reading_numbers.md` word for word. Inside the `<< >>` number passages the 795 letters given (the printed word, or the `=signs` form where one is noted) are the 795 letters of the decrypt, in order.
- **Cause D, clear text of the manuscript (most of the 92 words).** The phrases the key does not produce ("nessun modo", "suppl.to per Sua et amore", "Il Sig.or Marchese di Casale Nuovo", "Per amor di Dio ci compatisca, che non possiamo", "Io sono mal pensante V.E. lo sa, e cosi sto fermo" ...) are clear words of the letters, in [ ] in the transcription and outside `<< >>` in `edit_numbers.txt`. The audit drops them from the transcription and finds them only in the reading.
- **Marked proposals and unread words, not cause B.** 26 places carry a note in `edit_numbers.txt`: 15 `[?word]` proposals (e.g. `[?sequestratore]` for `seculnorio`), 7 `[...]` (e.g. for `banatte`, `couolo`), and 4 spellings (vuole for `uuole`, S.o, S., D.). The 22 proposals and unread words are bracketed in the reading; the 4 spellings change no letter. The code words [che] (104) and [?per] (159) are in `key.tsv`. Unmarked emendations found: 0.
- **Cause F.** The `[...]` and `[?..]` markers and the dropped clear text account for the script's "replaced" gaps (e.g. decrypt `couolo uoleua` against reading "[...] voleva").
- **Cause E, small.** The reading prints clear words that the transcription file does not hold (c. 20r "attese a far partire Nicola che") and leaves out clear words that it does hold (11r.2, 20r.2, 21r.8 "e bene chiamo", 22v.2). The header of `reading_numbers.md` says only the nearest clear words are given.

Nothing was changed in the key, the transcription or the reading. After: 92 of 239, unchanged. Not checked: any group against an image.

**Marked on 16 Nov 2026.** Nothing: no unmarked departure was found and there is no page.

## Remaining gaps

State after the fifth letter (24 Nov 2026, last section): 43 holes over five letters (Letter 1 14, Letter 2 3, Letter 3 5, Letter 4 3, Letter 5 18), listed by `scripts/count_words.py`. The first three items are the 18 of Letter 5 (9 + 2 + 7). The next three and the 23 supplied-letter words make up the 25 of Letters 1-4 (1 + 1 + 23). The last is clear text, outside the count. The codes 159, 109, 182 and 13, open until 24 Nov 2026, read at every place in the five letters and are graded sure (`key_additions_2026-11-24.tsv`).

- code groups of the letter of 18 Sept 1691 with no sure value: 171 (probable Signor, one use), 161 (probable questo, two uses), 165, 185, 162, 168, 160, 200 (one use each), 9 words - blocker: no-key-material; each stands once (161 twice, in the same letter) in the five cipher letters; no key sheet of the time in the Campori dossier or in print; the other eleven letters of 1687 and later show no number passage at 780 px
- ricausranno (L5_24v_08, read [?ricavaranno]) and bcri (L5_24v_13, B[a]ri), 2 words - blocker: too-short; the writer's slips: on native-size enlargements the groups are a clear 90 and a clear 20 where 10 is wanted; the one-digit rule of README Conventions is for a surviving period key only. No blocker word fits a writer's slip; too-short is the nearest, as for the supplied letters
- Monsig[nor]e, l[ette]ra, esec[u]t[ion]e, carricam[ent]o, negot[i]o, rovin[a]to and dic[e] in the letter of 18 Sept 1691, 7 words - blocker: too-short; the writer's abbreviations (five with a raised ending) and a word-final bare 3, as the 23 words below
- `45 30 85` (L3_23r_02, literally let, proposed [?lettere]), 1 word - blocker: too-short; three letters, no second use. On the native-size crop the last group is 85 and the first digit is 1 or 4 (det or let), so neither `25 30 85` (fat[ti]) nor WAINUT's `15 30 45` (del)
- the word before ho on c. 21r (line 21r.4 in WAINUT's file, L4_21r_03 in Kennedy's): e in Kennedy's reading, [?l'ho] in WAINUT's, t'ho in the blind check of 3 Nov, 1 word - blocker: illegible; the group is under a blot on the native-size crop and the three readings cannot be told apart
- 23 cipher words in which the reading supplies letters the writer did not write (14 in Letter 1, 3 in Letter 2, 4 in Letter 3, 2 in Letter 4): ten abbreviations (Vic[ari]a, p[ad]re, citat[ion]e, d[ucat]i, inter[ess]i, ten[en]te, Cam[er]a twice, precet[t]i, cerim[oni]e, nine of them with a raised ending in the transcription); the four word-final `3` of Letter 1 read as e (renditz, spesz, mz, z in the decryption); and nine words with a letter or an ending left out or written twice (no[n], tenut[o], svegl[i]ati, remedi[o], the dittography di, figli[o], an[n]i, s[i], vesco[vo]) - blocker: too-short; the cause is the writer's abbreviations and slips, not a missing key (the contributor's `no-key-material` was relabelled on 24 Nov 2026). The words are holes by the sure-word rule (README Conventions, 19 Nov 2026) however plain the word is: vescovo is written out on c. 22r of the same letter, and that does not put the letters on c. 22v. Nothing outside the letters can add what she did not write. The checker's list has no word for a writer's abbreviation; `too-short` is the nearest, as armstrong and vilaflor1663 use it for supplied letters. dan[n]o left this group on 24 Nov 2026: the doubling stroke is on the image
- clear-text doubts [?Galioto] / [?Galeota] (c. 4r) and [?Banchi] for B.i (c. 21r) - blocker: needs-physical-access; the contributor's statement, not looked at in the check of 24 Nov 2026; clear text, outside the count. (The cipher word anima against ansia, listed here until 24 Nov 2026, is settled: see the doubts below.)

## Escalation

Matthew Kennedy's six steps (`kennedy_2026/NOTES.md`) as he states them, with what the stopping-point check of 24 Nov 2026 added. The siblings step turned up a fifth cipher letter; the last two steps were done on it later that day (last section).

- [x] siblings: the four Vittoria Gonzaga items the library marks as cipher (cc. 3-4, 11-12, 20-21, 22-23) looked through by the contributors. 24 Nov 2026: the dossier has 18 records (cc. 1-33); the twelve other records of 1687 and later, one of them undated (cc. 5-10, 13-19, 24-33), viewed at 780 px. cc. 24v-25r (18 Sept 1691) carries about 15 lines of the same number cipher; no number passage seen on the others at that size. No key sheet. No target on main in the same key
- [x] clear-pages: the clear leaves (cc. 3r, 4v, 11v-12v, 20v, 21v, 23v) and the clear text around the numbers checked by the contributors; none is a decipherment of the time. 24 Nov 2026: the clear text of c. 24v names "S.r Duca di Torre Mag.e"
- [x] known-keys: WAINUT's `key.tsv` (PR #226) compared; no key sheet of the time for these letters found online; not the Mantuan chancery ciphers of 1544-46 (Kennedy); guastalla1717, the nearest target on main, is another cipher
- [x] print: web and catalogue search for an edition of the Santa Chiara letters of 1686-91; none found
- [x] key-rebuild: done on the four letters (the swapped-pair alphabet with dot-marked 5 = b, 2 = u/v, 3 = z, 7 = o and proposals for the five codes; a blind anneal on Letter 1 alone agrees with the key on 381 of 397 held-out letter tokens of Letters 2-4, rerun by the review of PR #853). 24 Nov 2026: the letter of 18 Sept 1691 reads with the letter values unchanged; 159, 13, 182 and 109 read at every place in the five letters and are graded sure; 171 and 161 probable; six new groups get no value (`key_additions_2026-11-24.tsv`). Three Lodovico keyword searches for the Duke of Torre Maggiore's own letters found none
- [x] retry: done on the four letters (every doubtful sign re-read on native-size crops by the contributor; the decryption files made the literal output of `key_kennedy.tsv`; every supplied letter bracketed; 237 of 267). 24 Nov 2026: svegl[i]ati settled on the image (no 50; the hole stands); recount over five letters by `scripts/count_words.py`, 379 of 422

## Transcription doubts

From `kennedy_2026/NOTES.md` (his checks against the Estense crops), with the verdicts of the check of 24 Nov 2026 on the first eight: an AI agent for the maintainers, not a person, looking at native-size crops of the Estense IIIF images with no overlay. The contributors' files were not changed.

- 13 (c. 20r l. 2, L4_20r_01) - read: 13 (Kennedy; also WAINUT's first reading of 3 Nov, changed by him to 15 for the sense, `retranscription_log_1570.tsv`); checked: image, decode, transcription; on the crop the second digit is a 3 with two open bowls, unlike the 5 of the 15 and the 55 beside it. The value is not settled: [et] from context, one use
- 55 with a stroke (c. 20r l. 2, L4_20r_01) - read: danno; checked: image, decode, transcription; a hooked stroke stands over `55 7` on the crop, as in WAINUT's `55~`; both keys say the stroke doubles the letter. Kennedy's transcription file does not carry it and his reading prints dan[n]o
- 15 50 (c. 20r l. 2, before 182) - read: di (Kennedy), 15 10 da (WAINUT); checked: image, decode, transcription; the crop shows 1 and two S-shaped 5s before the 0: 15 50
- 10 55 50 60 10 (c. 4r l. 7, L1_4r_09) - read: anima (Kennedy), 10 55 90 50 10 ansia (WAINUT); checked: image, decode, transcription; on the crop the fourth group is 60, its 6 with the long hooked ascender of the 65 that opens the line, which ansia cannot have; the third group is blotted and is read 50 from the word
- 45 30 85 (c. 23r l. 2) - read: not read ([?lettere]); checked: image, decode, transcription; on the crop the last group is 85 (Kennedy; WAINUT had 45) and the first digit is 1 or 4; det or let; a hole
- 2 2 7 45 (c. 21r, line 21r.3 in WAINUT's file, L4_21r_03 in Kennedy's) - read: vuol; checked: image, decode, transcription; the last sign is faint; Kennedy has 45, WAINUT 85 with [?vuol]; the crop allows either, the 4 and the 8 of this hand being close; kept as vuol on the sense
- 15 50 or 15 10 (c. 21r, end of line 21r.3, after carre) - read: di (Kennedy), da (WAINUT); checked: image, decode, transcription; on the crop the third sign is a straight stroke with a flag, like the 1 before it and unlike the S-shaped 5 of the 50 earlier in the line: 15 10, da. A sure word either way
- the group before 35 7 (c. 21r, line 21r.4, L4_21r_03) - read: not read; checked: image, decode, transcription; under a blot on the crop; e (Kennedy, 30), l' (WAINUT, 45) and t' (the blind check, 85) cannot be told apart; a hole. See "Key and tests" above, with the 21 changes of `retranscription_log_1570.tsv`
- 450, 2010550, 902304045108550 (c. 3v l. 4) - read: li, cani, svegl[i]ati; checked: image, decode; adjacent 5s run together (45+50 written 450) and a 50 left out. Settled on 24 Nov 2026 on a native-size region of the line: the ink is 90 2 30 40 45 10 85 50, with no 50 between 45 and 10 (the 1 of 10 carries a dot), so this line is right, `transcription_full.txt` (which gives the 50) is wrong there, and svegl[i]ati stays a hole. The contributor's file was not edited
- 2074545[1/2]0853075104530 (c. 4r l. 1) - read: Collaterale; checked: image, decode; the 1 of 10 has a curved top like a 2
- 9: (c. 4r l. 5) - read: S. (S. Paulo); checked: image, decode; 90 without its 0 before the abbreviation mark
- 2550404550 (c. 4r l. 19) - read: figli[o]; checked: image, decode; bare figli, then a space and non; the o is supplied, a hole
- 50 (c. 21r l. 6, before carre) - read: the clear numeral 50; checked: image, decode; unmarked, the same shape as cipher 50 = i; the decryption prints i
- 753060301550 1550, 853055285, 90 (c. 3v ll. 9 and 7, c. 4r l. 22) - read: remedi[o] [dittogr. di], tenut[o], s[i]; checked: image, decode; literal in the decryption, bracketed in the reading

Letter of 18 Sept 1691 (cc. 24v-25r), transcribed 24 Nov 2026 by an AI agent for the maintainers that knew the key, in two passes on native-size regions (1000-px segments at 1.2x, then 800-px segments at other cut points at 1.6x); each place below was looked at again enlarged 2-4x with no overlay. Line ids as in `transcription_cc24v-25r.txt`. No independent transcription exists. In this hand 4 and 8 are close: the 4 usually has a loop at the top and a stroke below the line, the 8 a bowl on the line; where a place breaks that habit the decode decides.

- 15 30 45 before 171 (L5_24v_03) - read: del; checked: image, decode; the 4 is drawn with a heavy bowl at the foot, like this hand's 8 (det); del is the only word, and the clear text has "l.ra del S.r Duca"
- 13 (L5_24v_03 and L5_24v_05) - read: 13 at both places; checked: image, decode; a 3 with two bowls and a flat top, unlike the S-shaped 5 of the 15 in the same lines
- 182 (L5_24v_04, L5_24v_10) and 162, 185 (L5_24v_06) - read: 182, 182, 185, 162; checked: image, decode (code groups: the decode shows a person at both places of 182, as at c. 20r); pass 1 read the first as 162; on enlargement the middle digit of 182 and 185 has a short closed top like the 8 of 80, the 6 of 162 the tall hooked ascender of every 6 on the page
- 10 45 (L5_24v_04) - read: al; checked: image, decode; pass 1 hesitated between 104 (che) and 10 45; the 4 is followed by a long-s 5 like the 5 of the 65 next to it
- 50 70 (L5_24v_05) - read: io; checked: image, decode; a heavy S-shaped 5 and o, then 70; not the dot-marked 5 (b)
- 10 90 65 30 85 85 10 75 7 (L5_24v_05) - read: aspettaro; checked: image, decode; the first 85 has a stroke below the line like a 4 (aspeltaro is no word)
- 85^e (L5_24v_06) - read: esecot(e), reading esec[u]t[ion]e; checked: image, decode; the group before 85 is a clear 7 with a flat top, not 2: the writer put o for u; the raised sign is an e
- 20 10 75 75 50 = / = 20 10 60.^o (L5_24v_06-07) - read: carricam[ent]o; checked: image, decode; two dots after 50 at the line end are a hyphen, as after pes on L5_24v_10; the raised sign over the abbreviation point is a 7 (o)
- 15 50 20 3 (L5_24v_07) - read: dic[e]; checked: image, decode; the last sign is a 3 with a flourish and no closed 0; a word-final bare 3, as the four of Letter 1; dice is the sense
- 55 7 55 (L5_24v_08, first word after che) - read: non; checked: image, decode; the last two strokes are joined at the top and could be read 75 (nor is no word)
- 75 50 20 10 2 90 75 10 55 55 7 (L5_24v_08) - read: [?ricavaranno]; checked: image, decode; pass 1 read an extra 20 10, pass 2 and a native-scale view show one; the group after 2 is a clear 9 with its loop and long tail (no 3, no 1), so the key gives ricausranno; ricavaranno (10) or ricaveranno (30) is the sense; a hole
- 30 25 25 50 20 10 20 30 60 30 55 85 30 (L5_24v_09) - read: efficacemente; checked: image, decode; a blot covers the 6 of 60, whose ascender shows
- 5 30 55 30 15 30 85 85 10 (L5_24v_10) - read: benedetta; checked: image, decode; pass 1 split it as belle detta (45 45); enlarged, the 0 of the first 30 and the 55 are in heavier ink and the word runs on without a space
- 75 7 2 50 55^to (L5_24v_11) - read: rovin[a]to; checked: image, decode; the raised ending is an 85 with a 7 over it (to)
- 65 30 55 30 85 75 10 75 30 (L5_24v_12) - read: penetrare; checked: image, decode; pass 1 read 65 30 55 90 10 75 30 (pensare); the fourth group has no tail below the line (30, not 90) and is followed by an 85
- 2 50 2 30 (L5_24v_13) - read: vive; checked: image, decode; pass 1 took the second group for 80; enlarged it is an S-shaped 5 with a looped top, open on the left, unlike the closed 8 of the 80 in queste above
- 90 10 45 2 85 30 (L5_24v_13) - read: salute; checked: image, decode; a small gap after 90 10; pass 1 read a second 2, pass 2 one
- 5 20 75 50 (L5_24v_13) - read: B[a]ri; checked: image, decode; the second group is a clear 2 with its base stroke and an o, unlike the 1o of provincia beside it; Bari is the sense; a hole
- 2 50 30 55 30 and 10 45 85 75 7 (L5_24v_14) - read: viene, altro; checked: image, decode; pass 1 read 2 30 30 and missed the 75 of altro
- q.ste (end of L5_24v_14) - read: clear abbreviation, not resolved; checked: image, decode (the sentence around it); a q crossed by a stroke, a long s with a crossbar and e, with a raised stroke; queste does not fit after della, quale would; not a catchword (c. 25r opens with cipher); outside the count
- 60 7 45 85 50 (L5_25r_01) - read: molti; checked: image, decode; the third group has the 4 with its stroke below the line, the fourth the 8 with its bowl on the line
- 75 7 2 50 55 10 (L5_25r_01) - read: rovina; checked: image, decode; at the page edge the 1 of 10 is curled like a 2, as Kennedy found at c. 4r l. 1
- 90 10 (L5_25r_02) - read: sa; checked: image, decode; the 1 is curled
- 25 7 75 60 10 55 70 (L5_25r_02) - read: formano; checked: image, decode; the last group is a 7 with a small raised o after it, 7 or 70, o either way
- 60 7 15 70 (L5_25r_02) - read: modo; checked: image, decode; the 5 of 15 is closed at the foot like an 8; the key has no 18
- 85 30 60 65 7 (L5_25r_03) - read: tempo; checked: image, decode; pass 1 read a second 60; enlarged there is one 6, then o, then 65

## Gaps listed on 3 Nov 2026 (WAINUT), kept for the record

What `kennedy_2026/NOTES.md` says of each follows the list (his statements; no image was opened at integration).

- Native-size re-read and a blind second pass of cc. 3v, 4r, 11r, 22r, 23r.
- Blind second read of the new lines on cc. 20r, 21r, 22v, and of the 21 changes logged.
- Code groups 109 and 182. Group 159. The group `10 00` at 11r.1.
- 17 doubtful words and 9 words not read, listed in `repairs_numbers.md`, among them c. 21r [?vuol], where the last sign looks like 85, and c. 22v [?Vesc.].
- "i carre da tratte di grano": the sense is clear, but carre for carra or carri is left as the groups give it.
- c. 12v was not viewed. The clear parts of the letters are not transcribed.

Kennedy reports every doubtful sign re-read on native-size Estense crops, the clear leaves cc. 11v-12v checked (no decipherment of the time), values proposed for 109, 182 and 159, the `10 00` of c. 11r read as the clear numeral 1000, and "50 carre" read with a clear numeral 50. No blind second transcription by a reader who did not know the key is recorded for any page, and the clear parts of the letters are transcribed only around the number passages.

## Independent completion and visual check, 21 Nov 2026 (Matthew Kennedy)

An independent full-corpus completion and visual check covering all four letters (`read in part` under the strict `cyphersolver` word rule: **237/267 strict sure cipher words = 88.8%, 30 holes**, out of 251 alphabetic / 1,028 tokens + 16 nomenclator = 267 cipher words, plus 2 inline clear numerals = 269 total entries; **266/267** including bracketed editorial expansions and context-inferred low-frequency codes, adding the previously untranscribed lower half of `c. 4r`), proposing values for all five nomenclator codes (`104=che`, `159=per`, `109=Duca`, `182=V.E.`, `13=et`), confirming `3=z`, and resolving the doubtful/unread passages listed under `## Remaining gaps` above (`stamo disperate`, `secutorio`, `Spagna`, `abbatte`, `tutti pollicinelli`, `uscire`, `citat[ion]e ... d[ucat]i *1000* ... inter[ess]i`, `il vescovo lo voleva carcerare`, `luogo ten[en]te di Cam[er]a ... precet[t]i`), is placed in `kennedy_2026/` (`kennedy_2026/NOTES.md`, `key_kennedy.tsv`, per-letter aligned file sets for `cc03r-04v_1686-04-02`, `cc11r-12v_1688-04-13`, `cc22r-23v_1691-09-04`, and `cc20r-21v_1691-10-16`, combined `*_full.{txt,md}` files, `verify_vittoria_gonzaga.py`, and bundled public-domain Italian model inputs `IT_pack.npz` and `IT_top_lexicon_words.json`). WAINUT's 3 Nov 2026 files and `profile.json` are left untouched pending maintainer review.

## Integration of PR #853, 24 Nov 2026

Done by an AI agent for the maintainers, not a person, from the files of this folder and the review of the pull request. No image was opened.

**Count carried.** Read in part: 237 of 267 cipher words, 88.8%, 30 holes (Letter 1, 2 Apr 1686: 141 of 155, 14 holes; Letter 2, 13 Apr 1688: 11 of 15, 4 holes; Letter 3, 4 Sept 1691: 19 of 24, 5 holes; Letter 4, 16 Oct 1691: 66 of 73, 7 holes). The review of the pull request recounted the holes from the four reading files (14, 4, 5, 7), and its own decoder, written from `key_kennedy.tsv` and `transcription_full.txt` alone, gives `decryption_full.txt` on all 55 lines. Letters 2 and 3 have fewer than 40 cipher words but 4 and 5 holes, so the short-text floor (2 holes) does not apply to them. No letter reaches 95%.

**Two keys, not chosen.** The folder holds WAINUT's `key.tsv` (3 Nov 2026) and `kennedy_2026/key_kennedy.tsv`; both are named in `profile.json` `outcome.key_file`. The letter values are the same. They differ in these places:

- the group between dan[n]o and interesse on c. 20r: Kennedy transcribes 13 and gives it the code value et; WAINUT transcribes 15, the letter d (d'interesse). `key.tsv` has no 13.
- 159: per in `key_kennedy.tsv`, [?per] marked doubtful in `key.tsv` (the same word).
- 109 and 182: Duca and V.E. in `key_kennedy.tsv`, not identified in `key.tsv`.
- 3 = z (tozzo) and the dot-marked `.5.` for b are in `key_kennedy.tsv` only; `key.tsv` has 5 = b and says z is unseen.
- 104 che: the same in both.

Which of 13 and 15 the ink has is not settled here; it is a gap and a transcription doubt above.

**Credit.** WAINUT (PR #226): the first key and reading. Matthew Kennedy (GitHub dragstripfarm, PR #853): the completion, the lower half of c. 4r, the values proposed for the codes and the statistical checks. By his statement the work was done in his own workflow with Gemini 4 (`gemini-4-neon-xhigh`, via Google Antigravity IDE) for first-pass visual triage, scripting and Italian drafting, and he checked the glyphs, key and readings against the scans himself. That statement was not checked here.

**Reading reviews.** The four grades in `kennedy_2026/NOTES.md` (Codex, for the maintainers, 22 Nov 2026: B, A, B, A) were given before the decryption files were made literal on 23 Nov; the words of the readings did not change. At this integration the four Italian readings were read through as sentences with the English beside them, and `decryption_full.txt` was compared with `reading_full.md` for Letters 2, 3 and 4 and the end of Letter 1; grade B is recorded for each letter in `profile.json`. The cipher passages complete the clear sentences around them in all four letters. Places that do not read smoothly: "ha tenut[o] V.E. di tal materia" (c. 3v; the English supplies "us unaware"), "s[i] presto senta la nascita" (c. 4r), and "e [?lettere] precet[t]i" (c. 23r).

**Not done here.** No site page and no README row (the target stays in progress); `python docs/_validate.py vittoria1686` not run; no DECODE queue entry; no comparison of any group with the Estense images. Where the Italian corpus of `IT_pack.npz` comes from rests on the contributor's statement. (Later the same day the 13 of c. 20r was settled on the image and a queue hold was added: next section.)

## Stopping-point check, 24 Nov 2026

Done by an AI agent for the maintainers (Claude Fable 5.2), not a person, before a write-up that was then not made. Sources: the files of this folder, the two reviews of PR #853, the Estense catalogue (Lodovico) and its IIIF images. The crops were fetched to a scratch folder and are not in the repository.

**Result.** Not a stopping point. The dossier holds a fifth letter in the same cipher that nobody has transcribed, and it carries again the code groups that are open in the other four. No page and no README row. Catalogue entry 1570 stays and is refreshed (`known`, `open`, the fifth record). The DECODE queue has a hold.

**The two transcriptions, group by group.** On the passages both contributors transcribed (cc. 3v, the upper half of 4r, 11r, 20r, 21r, 22r, 22v, 23r), a sequence match of the number groups (own read-only script, not kept) finds 776 of the 808 groups of `transcription_numbers.txt` in `kennedy_2026/transcription_full.txt`, in the same order. They differ at 30 places. At most of them WAINUT's first reading at about 1,400 px gives no word and Kennedy's gives one: stcmo / stamo, seculnorio / secutorio, spaltta / Spagna, banatte / abbatte, lutti / tutti, uocire / uscire, citale / citat.e, couolo / il vescovo lo. At six places the choice is between two words, or neither is one: ansia / anima (c. 4r), d' / [13] and da / di (c. 20r), da / di and l'ho / e ho (c. 21r), del / let (c. 23r). uuot / vuol (c. 21r) hangs on one faint sign.

**13 against 15.** `key.tsv` has no 13; `key_kennedy.tsv` has 13 = et. In the four letters the sign 13 stands at one place, between danno and interesse on c. 20r. 15 stands at 42 places (Kennedy's count) and is d at every one. At the one place both values give Italian: "il maggior danno d'interesse da [182]" (WAINUT) and "il maggior dan[n]o [et] interesse di [V.E.]" (Kennedy). The context does not decide. The files lean to 13: WAINUT's own log has 13 as his first reading from the native tiles, changed to 15 for the sense. The image decides the digit: 13, and di after interesse, not da (doubts above). So the transcription of the place is Kennedy's and WAINUT's d' falls. What 13 stands for is still a value from context on one use. That it is a group of the cipher and not a slip of the pen for 15 is supported by the letter of 18 Sept 1691, where it stands again.

**Keys.** The letter values of the two key files are the same. `key_kennedy.tsv` covers every sign of the transcription (3, the dot-marked 5, the doubling stroke, 13); `key.tsv` is the first key and stays beside it in `profile.json`. No code value is taken as settled except 104 che.

**Count.** 237 of 267 on the four letters, the same figure with another make-up: danno is written in full with its doubling stroke (one hole fewer); the word before ho on c. 21r (line 21r.4) is under a blot (one hole more). Letter 4 stays at 66 of 73. The contributors' files were not edited: the reading file of Letter 4 still prints dan[n]o and e ho, and its transcription still has 15 50 after carre.

**The 23 words with supplied letters.** They are the writer's own abbreviations and slips. A second use shows what a word is (vescovo in full on c. 22r; Camera twice in the same short form) but puts no letter on the page, so by the sure-word rule each stays a hole and no sibling letter can change that. The four word-final 3 of Letter 1 fit e at all four places, and the grammar wants it at two (le rendit3 sue, alle spes3). A rule "3 at the end of a word is e" in a key file would make them key output. The review of PR #853 left that choice to the contributor, who printed the literal z and marked the repair; it is left as it is.

**Siblings.** On main no other target has this shelfmark or this key. `guastalla1717` (the Duke of Guastalla, 1717, same library) is two-digit numbers in alphabet order from 30 to 67, another system. In the library, a search of the Lodovico catalogue by shelfmark lists 18 records for "Gonzaga, Vittoria (Sec. XVII-XVIII)", cc. 1-33: two of 1626 from Mantua (cc. 1 and 2), fifteen from Naples of 1686 to 1701, and one with no date (cc. 32-33). Four are described as "Lettera parzialmente cifrata". The twelve records left when the four and the Mantua pair are set aside (cc. 5-6, 7-8, 9-10, 13-14, 15-16, 17, 18-19, 24-25, 26-27, 28-29, 30-31, 32-33; 46 page images) were viewed at 780 px wide. One has numbers:

- cc. 24-25, 18 Sept 1691, record `eab58d9b-6ca2-44c8-bc90-eb88a5c05fb0`, manifest `https://edl-jarvis.cultura.gov.it/meta/iiif/eab58d9b-6ca2-44c8-bc90-eb88a5c05fb0/manifest`. The record does not call it a cipher letter.
- c. 24v, image service `https://edl-jarvis.cultura.gov.it/images/iiif/db/a4f2072b-913c-4b55-a55d-da8bd18e4113` (4999 x 6780 px): a run at the end of one line and the start of the next (about y 2540 to 3060), then a block of twelve lines with one run-over, from about y 3800 to the foot of the page.
- c. 25r, image service `https://edl-jarvis.cultura.gov.it/images/iiif/db/313d8600-7c1b-4ddb-b7a2-0f9b313f094c` (4983 x 6708 px): the first three lines.
- On the order of 200 cipher words by eye. Not counted.

At 780 px a line or a block of numbers shows; a single group inside clear text could be missed. For the other eleven the finding is "no number passage seen", not "none".

**Sample of c. 24v (six native-size crops).** With the letter values of the key the short run reads "non so Monsig.re come / la sentira" (55 7 55 / 90 7 / 60 7 55 90 50 40 with a raised ending / 20 7 60 30, then 45 10 / 90 30 55 85 50 75 10). The block opens "[?ho] levato il foglio [?in] cifra dalla l.ra nel 171 109 13 e il seguente". The same cipher. The groups 171, 109 and 13 are on a native-size crop; 104, 159, 182 and 161, 162, 165, 168 were seen at reduced size only. If "e il" after 13 is right, et does not fit 13 there as it stands. The clear text of the same page has "acclusa l.ra del S.r Duca di Torre Mag.e": she names the Duke of Torre Maggiore in clear four weeks before c. 21r. That supports [Duca] for 109 and does not prove it. This was a look, not a transcription; no file was made from it.

**One key, one entry.** The fifth letter belongs to this target: the same writer, the same brother, the same cipher, the weeks between Letters 3 and 4.

**Next step.** Transcribe cc. 24v-25r from native-size crops (the server gives regions of up to about 1,600 px a side), list the doubtful signs, decrypt with the letter values, and read it with its clear text. Then put every use of 159, 109, 182, 13 and the new groups side by side, settle svegl[i]ati on c. 3v from the image, and recount over five letters. Only then decide the class and write the page.

**Not done.** No transcription of cc. 24v-25r. cc. 3v, 11r, 22r and 22v not looked at on the image. The clear-text doubts not looked at. `docs/_validate.py` not run. No image kept, nothing sent to anyone.

## The fifth letter, 24 Nov 2026

Done by an AI agent for the maintainers (Claude Opus 5.5), not a person. Sources: the Estense IIIF images of record `eab58d9b-6ca2-44c8-bc90-eb88a5c05fb0` (cc. 24v and 25r, native-size regions; the earlier agent's tiles of the same day were re-checked and new regions fetched one at a time), `kennedy_2026/key_kennedy.tsv`, and the files of this folder. No image is kept in the repository.

**Transcription.** `transcription_cc24v-25r.txt`: a run of two lines in the clear text of c. 24v, a block of twelve lines with one run-over at its foot, and three lines at the head of c. 25r. 603 groups, 34 distinct, 155 cipher words (`docs/_check_profile.py --measure ... --digits --drop-first`). Two passes over every line at different cut points and enlargements; every place where they differed and every doubtful sign was settled on a further enlargement (Transcription doubts above). The reader knew the key, and one reader made both passes, so this is not a blind or independent transcription.

**Decryption.** `decryption_cc24v-25r.txt`, the output of `scripts/decode_cc24v-25r.py` (`kennedy_2026/key_kennedy.tsv` applied group by group, nothing edited). Every letter value of the key gives Italian without a change.

**Reading.** `reading_cc24v-25r.md` and `translation_cc24v-25r.md`. After a short run on c. 24v ("non so Monsig[nor]e come la sentirà"), she writes that she has taken the cipher sheet out of the letter of the [?Signor] Duca, "et è il seguente", and copies it: the Duke will wait for October to load the grain when the boats come, as V.E. tells him; this blessed plague, which has ruined [?questo] [168], no one knows what it is, while "in queste parte si vive con salute"; in the province of Bari they die of hunger; "in ogni modo il tempo lo scoprirà". It is the grain business that the letter of 16 Oct 1691 (Letter 4) takes up four weeks later, when the same Duke asks through Pompeo for 50 carra of licences. The reading has no reading review: its author does not sign one, and a second reader is owed before a page can stand on it.

**Code values** (`key_additions_2026-11-24.tsv`, with places). Graded sure: 159 per (five places in three letters), 13 et (three places, two letters), 182 V.E. (three places, two letters), 109 Duca (two places, and the clear text of c. 24v names the same Duke). They close five holes of Letters 2 and 4: [per] on c. 11r, and [per], [et], [V.E.] and [Duca] on cc. 20r and 21r. Probable, so holes: 171 Signor (one place) and 161 questo (two places that other words fit). No value: 165, 185, 162, 168, 160 and 200. WAINUT's d' for the group on c. 20r fails: it is 13 at all three places. The judgment call is 182: V.S. would also fit its two places on c. 24v.

**Count** (`scripts/count_words.py`, which prints both gradings). Letter 1 141 of 155 (14 holes); Letter 2 12 of 15 (3); Letter 3 19 of 24 (5); Letter 4 70 of 73 (3, 95.9%: over the read bar); Letter 5 137 of 155 (18, 88.4%). All five: 379 of 422, 43 holes, 89.8%. With only 104 sure, as before: Letters 1-4 237 of 267, all five 366 of 422. Read in part: four of the five letters are under 95%.

**Stopping point.** Yes. Every hole has an outside blocker: the writer's abbreviations, a word-final bare 3 and two slips with clear groups (too-short; nothing outside the letters can add what she did not write), a word under a blot (illegible), a three-letter word on c. 23r (too-short), and eight code groups that stand once (161 twice) with no key sheet in the dossier or in print (no-key-material). svegl[i]ati on c. 3v was checked on the image: the hole stands. Three Lodovico keyword searches for the Duke's own letters found nothing. The other eleven letters of the dossier were seen at 780 px only (no number passage seen); a lone code group in clear text there could have been missed, which is noted and not counted as a workable gap.

**Validation.** `docs/_validate.py vittoria1686 --write` on `validation.tsv` (all five letters, 1,631 read tokens, it-cinquecento): pass (random keys z 5.9; a key annealed onto shuffled ciphertext best -3.244 against -2.036 for the reading).

**Write-up, 24 Nov 2026.** `docs/vittoria1686.html`, its manifest lines, the lead crop `docs/vittoria1686_lead.jpg` (c. 24v, Estense Digital Library, CC BY-NC-SA), `docs/reveal/vittoria1686.json`, the key node in `docs/keys.json`, the portrait skip, the README row, the findings line, `SOLVED_CATALOGUE.md` no. 410, a provisional `SOLVED_RANKING.md` row (2.65; the ranks below it not renumbered), catalogue entry 1570 removed and listed in `CATALOGUE.md`, and the DECODE queue skip refreshed. Not done there: the build, the claims review and `--reviewed`, and the reading review of Letter 5 by a second reader.

**Not done.** No reading review of Letter 5. No key replay (`replay.py`). The clear text of cc. 24r-25v is given only next to the cipher; `q.ste` at the foot of c. 24v is unresolved (clear, outside the count).
