# Girolamo Muzio to Ferrante Gonzaga, Rome, 11 Jan 1550 (Biblioteca Estense, Autografoteca Campori, Muzio c. 3r)

Status: read in part, codes open (contributed, issue #405). Key recovered from the sister letter of 12 Jan 1550 and completed on c. 3r. By cipher units 98.1% of c. 3r is read by the key; by words 0.909 with codes and emended words counted as holes, 0.957 with the codes counted apart.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Sent as issue #405 on 11 Nov 2026; checked by Daniel Bourdeau on 12 Nov 2026 ("the reading holds"), who asked for these files and raised the points answered under "Corrections of 12 Nov 2026". Not yet written up on the site.

Catalogue entry 1564 lists five letters of Gonzaga clients to Ferrante Gonzaga. This folder is one of the five, the Muzio letter of 11 Jan 1550, with the Muzio letter of the next day that the key rests on. The Rossi letters of the same entry are not treated here.

## The documents

| | c. 3r (the target) | cc. 5r-5v (sister letter) |
|---|---|---|
| Shelfmark | Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera M, Muzio, Girolamo, cc. 3-4 | the same, cc. 5-6 |
| Date | Rome, 11 Jan 1550 | Rome, 12 Jan 1550 |
| Record | https://lodovico.medialibrary.it/media/schedadl.aspx?id=3b88f5b4-35eb-4f51-a153-84c520bb5df3 | record 9af96fa2-e4c2-4980-9e60-067568443db3 |
| IIIF manifest | https://edl-jarvis.cultura.gov.it/meta/iiif/3b88f5b4-35eb-4f51-a153-84c520bb5df3/manifest | https://edl-jarvis.cultura.gov.it/meta/iiif/9af96fa2-e4c2-4980-9e60-067568443db3/manifest |
| Cipher | one block of 25 lines, 860 units, all the news of the letter | two passages inside clear text: 9 lines on c. 5r, 3 lines on c. 5v; 339 units |
| Clear | heading and four closing lines | most of the letter |
| Decipherment on the sheet | none | an early hand: letters over one cipher line (c. 5r) and a marginal decipherment (c. 5v) |
| Other pages | c. 3v and c. 4r blank; c. 4v address and docket | c. 6r blank; c. 6v address and docket |

c. 3v and c. 4r are blank (seen on the images, 12 Nov 2026): the catalogue's "cc. 3-4, Lettera cifrata" is one page of cipher. The c. 5v cipher passage and its marginal decipherment are not in the catalogue note.

Images are not in the repository. Image service of c. 3r: `https://edl-jarvis.cultura.gov.it/images/iiif/db/27d0aeea-71cb-48aa-b6ac-5b62061aafe5`; c. 5r `.../a2eb7280-f634-40f6-934e-3f8701789e88`; c. 5v `.../9f6cca8a-93b4-4676-8c9a-a49972015df8`. A region is `<service>/<x,y,w,h>/max/0/default.jpg`. Sizes above the listed ones are refused for the whole page; regions work at full size.

## The system

Simple substitution on letter-like signs and single digits, written without word division. Two signs each for a, e, i, o, u and s; own signs for the doubled letters ll, rr, tt, pp, nn, ff; four digit pairs (38, 39, 42, 43) as nulls and a barred circle as a stop between clauses; a small code: number groups 13, 24, 25, 26, 1o, 4o and one sign (CE) for titles and persons. Key: `key.tsv`, 47 rows. Legend of the sign names: head of `transcription_c3r.txt`.

The o sign and the i sign differ by one minim (three or two minims, then a tail). All but one of the differences between the two transcriptions are there.

## How the key was obtained

1. 10 Nov 2026. First transcription of c. 3r (904 tokens, 29 types). The sign set was compared with the Gonzaga keys in this repository (ferrante1549, ercole1544, capilupi1545, bresegno1548): none fits.
2. 11 Nov. An own homophonic annealer (Italian quadgrams) recovered a synthetic text of the same size, then failed on the letter and on five variants that split ligatures (best -4.30 per character, no Italian). The cause, found later: the first transcription merged look-alike signs.
3. 11 Nov. The sister letter c. 5r has a cipher passage inside clear text, with word dividers added on the sheet and an early hand's letters t r a d ij o a over one line. With the two signs before them this gave c o n t r a d. The clear text before and after the passage and the dividers then gave "per questo" and "scoperta questa pratica", and so most of the alphabet.
4. 11 Nov. c. 3r transcribed again from line strips with the look-alike signs split (861 units, `timestamps/stamped/c3r_pass2.txt`), and the key completed by reading. The reader knew values from line 5 on.
5. 12 Nov. The c. 5v passage, not used before, was transcribed and decrypted with the key as it stood: "scrivere al CE nostro ma poi non havendo risposta di quello che 25 ha mandato". The early hand's margin beside it reads "scriver al Car.le n[ost]ro, ma poi no[n] havendo risposta di q[ue]llo ch[e] V. Ex. gli ha ma[ndato]". That is a test the key had not seen, and it gives two code values: CE = Cardinale, 25 = V. Ecc.

So the method is "key recovered based on adjacent plaintext": the first values come from a decipherment on a neighbouring leaf of the same file and from clear text around a cipher passage. It is not a ciphertext-only solution.

## Checks

- **Count by units, c. 3r** (`counts_c3r.txt`, `units_c3r.tsv`, `scripts/decrypt.py`): 860 units. Read by the key 844 (806 letters, 38 nulls) = 98.14%. Letters only: 806 of 822 = 98.05%. Emended 5; unread signs 2; code groups 9 (3 confirmed by the c. 5v margin, 4 with a value from context only, 2 with no value). Codes counted apart: 844 of 851 = 99.18%.
- **Count by words, c. 3r** (README read bar; our own count after `research/reading_audit/v2_score.py` and `v10_relabel.py`, which we read and did not run): 180 words and 18 holes, read share 0.909. The 18: code groups 13 and 24 (2); context-only values for 26 three times and 4o once (8, one per word); five emended words (5); the two single signs (3). With the nine code tokens counted apart: 176 words and 8 holes, 0.957.
- **Reading against units**: the Italian reading, stripped of spaces and marks, equals the units' values letter for letter (839 characters).
- **Shuffled keys** (11 Nov, on version 1 of the transcription; not repeated on version 2): Italian quadgram score of the key-only decryption of c. 3r -3.922 per character; 5,000 shuffled keys, best -6.295, none as good. Lines 21-25 with a key voted from lines 1-20 only: -3.866 against a best of -5.965, none as good (the reader of lines 21-25 knew the key). The c. 5r passage with the c. 3r key: -4.012 against -5.951, none as good.
- **Blind second transcription** (`transcription_c3r_blind.txt`, `transcription_c3r_blind_NOTES.md`, `blind_agreement.txt`): another session, with no key and no reading, agrees with version 1 on 851 of 861 units (98.84%).
- **Image check of 12 Nov** (`corrections_c3r.tsv`): the 10 units where the two transcriptions differ, viewed at full resolution in 1,024 px tiles and 3x crops. The blind reader was right on 9, the first reader on 1.
- **Sister letter**: the key reads both passages (327 of 339 units by the key; `counts_c5.txt`), and the c. 5v decryption matches the early marginal decipherment word for word except for a "gli" the margin adds.
- **Outside audit** (11 Nov, reported by the contributor, files not here): a decoder re-implemented with non-Anthropic models from the transcription and key of version 1 gave the same text. The maintainer's own decoder did the same on issue 405.

## Corrections of 12 Nov 2026 (answer to the check on issue #405)

1. **Undeclared emendation.** Version 1 gave "dofficole" by the key, read "difficile", and declared one change. Both signs were looked at again on the image: each has two minims and a tail, the i sign. The sheet has "difficile". Both are now corrections of the transcription, and neither is an emendation.
2. **L20.** The sign after "ne s" has three minims and a tail, the o sign, the same form as the o of "andonati" earlier on the line. The sheet has "ne so come": "Né so come gli Imperiali ... habiano da condiscendere". Confirmed as proposed.
3. **L23.** The last sign of "uot-" has two minims and a tail; the o two signs before it has three. The sheet has "i uoti": "a dargli i voti". Confirmed as proposed. The emended article "il" of version 1 is withdrawn.
4. **The same test on every unit where the two transcriptions differ** gave four more corrections that version 1 had carried as emendations (L01 "si", L07 "importi", L14 first sign, L19 "tutto"), one change of word (L09 "conformando", not "confirmando") and one sign struck from the transcription (L17: there is no 8 between "co" and the sign OP, so "con gli" is "co" plus an unread sign). L25 "di uoler" was checked and kept.
5. **Emendations now** (`emendations_c3r.tsv`): five, and two unread signs. Omega for ss three times (fosse, creasse, esser); "polto" for "molto" (a clear 3 on the sheet); "aute" and two struck signs for "auto-" in "autorità".
6. **Figures by tokens and by words**: under Checks. The corrections are marked in place in the reading with `°`; codes are counted apart in `outcome.codes_open`.
7. **Title and entry**: this is one letter of the five in catalogue entry 1564 and has its own folder.
8. **c. 3v and c. 4r are blank.**

The crops made for these checks are not in the repository; each row of `corrections_c3r.tsv` gives the IIIF region to fetch.

## Prior art

No reading of the c. 3r cipher was found. Checked on 11 Nov 2026: Ronchini, Lettere di Girolamo Muzio (Parma 1864), read on the page images for January 1550: it has a different, clear letter of 11 Jan 1550 (no. LXXVI), none of 12 Jan, and none of this content; the Lettere of 1590 (poor OCR); Pastor vol. 13 (cites Muzio through Ronchini); Vandini's appendices to the Campori catalogue (no Muzio entry); the Estense records ("Lettera cifrata", "parzialmente cifrata", no notes); this repository; Cryptiana; HistoCrypt.

Ronchini no. LXXV, 10 Jan 1550, pp. 132-133, is the companion letter the cipher mentions ("per una altra mia, che vien con questa, le scrivo della cedula del Cardinale de Medici"): "Per una cedula del Card.le di Medici, comunicata ad uno de suoi amico mio, s'intende che il Car.le Farnese ha preso a favorire Monte".

Not checked: the Parma originals of Ferrante Gonzaga's papers (the main risk: a key or a deciphered copy may be there); Negri's 2000 edition of the Lettere; Concilium Tridentinum vol. II; Meister 1906; studies of the conclave of 1549-50. On the sister letter an early hand had already deciphered seven signs and one passage.

## Limits

- Several sessions of one model family did the transcriptions and the reading. No person read the signs without AI.
- The first reader of c. 3r was not blind from line 5 on. The independence in this folder is the blind second transcription and the c. 5v margin.
- The sister letter's cipher was read once, by a reader who knew the key, at 60-70% scale, without the minim check done on c. 3r. Its clear text was read once at quarter scale and is not collated.
- Code values 26 (Sua Maestà), 4o (Duca di) and 1o (Don Diego) rest on context. The persons named in the summary are our identifications.
- The hand of the interlinear letters and of the margin is not Muzio's; its date is not established. The abbreviation after "V." in the margin is read "Ex.".
- The shuffled-key controls were run on version 1 of the transcription.

## Tools

Claude (Anthropic) models for the transcriptions, the solving, the scripts and the checks. Own Python and C: an annealer with Italian quadgrams, a per-unit counter, a shuffled-key baseline, a transcription comparer. Images: Estense Digital Library IIIF. The repository's checker scripts were read, not run (the contributor does not run downloaded code); the checks they make were verified by hand and are listed in the pull request.

## Files

- `transcription_c3r.txt`: c. 3r, version 2. `corrections_c3r.tsv`: the nine units changed, with the IIIF region for each. `emendations_c3r.tsv`: the five emendations and two unread signs.
- `key.tsv`: the key, with a status for every row.
- `decryption_c3r.txt`: line by line, cipher then key decryption, unrepaired. `units_c3r.tsv`, `counts_c3r.txt`: every unit with its class; the counts.
- `reading_c3r.md`, `translation_c3r.md`: Italian and English, every correction, emendation and hole marked in place. `editorial.md`: marks and notes. `clear_c3r.md`: the clear heading and closing lines of c. 3r, cc. 3v-4v.
- `transcription_c5.txt`, `decryption_c5.txt`, `units_c5.tsv`, `counts_c5.txt`, `reading_c5.md`, `translation_c5.md`: the sister letter of 12 Jan 1550 in full.
- `SUMMARY.md`: what the letters say, and the context.
- `transcription_c3r_blind.txt`, `transcription_c3r_blind_NOTES.md`, `blind_agreement.txt`: the blind second transcription and the agreement figures.
- `timestamps/`: the manifest, the RFC 3161 token, the OpenTimestamps proof, the stamped files, how to verify.
- `scripts/decrypt.py`, `scripts/compare_blind.py`: standard library; they write the decryption, unit and count files and print the agreement.
- `profile.json`.

## Remaining gaps

- Code groups 13 and 24 have no value; 26 and 4o (and 1o on the sister letter) are from context. Blocker: open codes; needs a key sheet or more letters in this cipher.
- Two signs on c. 3r and one on c. 5r occur once and are unread. Blocker: too short.
- Omega as ss three times: a polyphone or a second form. Blocker: not told apart on the image.
- The sister letter's cipher passages need a blind pass with minim counts. Blocker: not attempted.
- The early hand on cc. 5r-5v is not dated. Blocker: needs the archive.
- Prior art in the Parma papers and the conclave literature is unchecked. Blocker: not attempted.

## Escalation

- A blind transcription of the c. 5r and c. 5v passages.
- The other Muzio letters to Ferrante Gonzaga in the Campori series, for more text in this cipher and the open codes.
- Archivio di Stato di Parma, Ferrante Gonzaga's papers: Muzio's letters of January 1550, any key, any deciphered copy.
