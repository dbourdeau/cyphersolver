# vittoria1686: Vittoria Gonzaga to her brother, catalogue 1570

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

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

- Native-size re-read and a blind second pass of cc. 3v, 4r, 11r, 22r, 23r.
- Blind second read of the new lines on cc. 20r, 21r, 22v, and of the 21 changes logged.
- Code groups 109 and 182. Group 159. The group `10 00` at 11r.1.
- 17 doubtful words and 9 words not read, listed in `repairs_numbers.md`, among them c. 21r [?vuol], where the last sign looks like 85, and c. 22v [?Vesc.].
- "i carre da tratte di grano": the sense is clear, but carre for carra or carri is left as the groups give it.
- c. 12v was not viewed. The clear parts of the letters are not transcribed.
