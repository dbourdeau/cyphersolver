# vittoria1686: Vittoria Gonzaga to her brother, catalogue 1570

Status: in progress. Not yet written up: no site page or README row. Read in part: 237 of 267 cipher words (88.8%, 30 holes) over the four letters, by Matthew Kennedy's completion of 21-23 Nov 2026 (PR #853, `kennedy_2026/`), carried into this file and `profile.json` on 24 Nov 2026 (section "Integration of PR #853" at the end). The table and the paragraphs down to "Decrypt audit" are WAINUT's of 3 Nov 2026 (PR #226: 172 of 198 number words, 86.9%, on the passages then transcribed) and are kept as he wrote them.

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

The five gaps of Matthew Kennedy's completion (`kennedy_2026/NOTES.md`, 23 Nov 2026), carried here on 24 Nov 2026. The first four add up to his 30 holes (2 + 3 + 1 + 24); the fifth is outside the count.

- code 159 (2 uses: L2_11r_01, L4_20r_01; proposed [per]) - blocker: open-codes; taken from context at two places, no key sheet of the time in the Campori dossier
- codes 109 ([Duca], L4_21r_02), 182 ([V.E.], L4_20r_01) and 13 ([et], L4_20r_01), one use each, 3 words - blocker: open-codes; each rests on one place; WAINUT read the third group as 15 (d'), see "Two keys, not chosen" below
- `45 30 85` (L3_23r_02, literally let, proposed [?lettere]), 1 word - blocker: too-short; three letters, no second use (possibly `25 30 85`, fat[ti])
- 24 cipher words in which the reading supplies letters the writer did not write: abbreviations expanded (citat[ion]e, d[ucat]i, Cam[er]a and others), the four word-final `3` of Letter 1 read as e (renditz, spesz, mz, z in the decryption) and one dittography; 14 in Letter 1, 3 in Letter 2, 4 in Letter 3, 3 in Letter 4 - blocker: too-short; the cause is the writer's abbreviations and slips, not a missing key (the contributor's `no-key-material` is relabelled here, 24 Nov 2026). The words are holes by the sure-word rule (README Conventions, 19 Nov 2026), and only a second copy of a letter, or the same word written out in full, could close one. The checker's list has no word for a writer's abbreviation; `too-short` is the nearest, as armstrong and vilaflor1663 use it for supplied letters
- clear-text doubts [?Galioto] / [?Galeota] (c. 4r) and [?Banchi] for B.i (c. 21r), and the cipher word of L1_4r_09, anima (Kennedy) against ansia (WAINUT) - blocker: needs-physical-access; the middle digits are tight in the ink on the Estense image (the contributor's statement; not compared with the image at integration)

## Escalation

Matthew Kennedy's six steps (`kennedy_2026/NOTES.md`), as he states them; not repeated at integration.

- [x] siblings: the four Vittoria Gonzaga items of the Autografoteca Campori (cc. 3-4, 11-12, 20-21, 22-23) looked through; no further cipher leaf and no key sheet
- [x] clear-pages: the clear leaves (cc. 3r, 4v, 11v-12v, 20v, 21v, 23v) and the clear text around the numbers checked; none is a decipherment of the time
- [x] known-keys: WAINUT's `key.tsv` (PR #226) compared; no key sheet of the time for these letters found online; not the Mantuan chancery ciphers of 1544-46
- [x] print: web and catalogue search for an edition of the Santa Chiara letters of 1686-91; none found
- [x] key-rebuild: the swapped-pair alphabet rebuilt, with dot-marked 5 = b, 2 = u/v, 3 = z, 7 = o and proposals for the five codes; a blind anneal on Letter 1 alone agrees with the key on 381 of 397 held-out letter tokens of Letters 2-4 (the review of PR #853 reran the verifier: same figure)
- [x] retry: every doubtful sign re-read on native-size crops; the decryption files made the literal output of `key_kennedy.tsv`; every supplied letter bracketed; recount by the strict rule, 237 of 267

## Transcription doubts

From `kennedy_2026/NOTES.md` (his checks against the Estense crops; none repeated at integration). The first two are the places where the two contributors read the same ink differently; neither is chosen here.

- 13 (c. 20r l. 2, L4_20r_01) - read: 13 [et] (Kennedy), 15 d' (WAINUT); checked: image, decode, transcription; one digit pair between dan[n]o and interesse; both readings kept open
- 10 55 50 60 10 (c. 4r l. 7, L1_4r_09) - read: anima (Kennedy), 10 55 90 50 10 ansia (WAINUT); checked: image, decode, transcription; the middle digits are tight; both readings kept open
- 45 30 85 (c. 23r l. 2) - read: not read ([?lettere]); checked: image, decode; literally let, possibly 25 30 85; a hole
- 450, 2010550, 902304045108550 (c. 3v l. 4) - read: li, cani, svegl[i]ati; checked: image, decode; adjacent 5s run together (45+50 written 450) and a 50 left out
- 2074545[1/2]0853075104530 (c. 4r l. 1) - read: Collaterale; checked: image, decode; the 1 of 10 has a curved top like a 2
- 9: (c. 4r l. 5) - read: S. (S. Paulo); checked: image, decode; 90 without its 0 before the abbreviation mark
- 2550404550 (c. 4r l. 19) - read: figli[o]; checked: image, decode; bare figli, then a space and non; the o is supplied, a hole
- 50 (c. 21r l. 6, before carre) - read: the clear numeral 50; checked: image, decode; unmarked, the same shape as cipher 50 = i; the decryption prints i
- 753060301550 1550, 853055285, 90 (c. 3v ll. 9 and 7, c. 4r l. 22) - read: remedi[o] [dittogr. di], tenut[o], s[i]; checked: image, decode; literal in the decryption, bracketed in the reading
- 85 35 7 or 45 35 7 (c. 21r l. 4, first group; WAINUT, 3 Nov 2026) - read: [?l'ho]; checked: image, decode, transcription; under a blot, his blind check gave t'ho; see "Key and tests" above, with the 21 changes of `retranscription_log_1570.tsv`

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

**Not done here.** No site page and no README row (the target stays in progress); `python docs/_validate.py vittoria1686` not run; no DECODE queue entry; no comparison of any group with the Estense images. Where the Italian corpus of `IT_pack.npz` comes from rests on the contributor's statement.
