# Girolamo Augustoni (as catalogued), 9 Oct 1612 (Biblioteca Estense, Autografoteca Campori, Lettera A, Augustoni c. 1; catalogue row 1569)

Status: read in part (contributed, PR #452, issue #427). Key recovered from the ciphertext alone. By the README word rule 0.849 of the page is read (clear text and cipher together, 56 hole words); by cipher units 537 of 587 = 91.5% by the reviewer's strict rule on the transcription frozen on 11 Nov 2026. The 94.0% of the issue is withdrawn.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Sent as issue #427; checked by Daniel Bourdeau on 12 Nov 2026, who asked for these files and raised the points answered under "Answers to the check on issue #427". Integrated on 12 Nov 2026 (see "Integration check").

## The document

| | |
|---|---|
| Shelfmark | Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera A, Augustoni, Girolamo, c. 1 |
| Record | https://lodovico.medialibrary.it/media/schedadl.aspx?id=516e565f-7451-43fe-a2fc-533c0b5efeee |
| Images | IIIF manifest https://edl-jarvis.cultura.gov.it/meta/iiif/516e565f-7451-43fe-a2fc-533c0b5efeee/manifest ; c. 1r stitched from 1,024 px tiles at full resolution, 2390 x 3508 px. No image is in this folder |
| Date | 9 Oct 1612: the close ("li 9. ... 1612", month doubtful on our reading) and the verso docket ("... 9 8bre 1612") |
| Writer | Girolamo Augustoni by the library's catalogue. We have not read the signature and cannot confirm the name from the sheet |
| Recipient | not named on c. 1r: "Sig.r mio", "V.S.", voi |
| Place | "Di Carp." in the close, perhaps Carpi; doubtful |
| What is on c. 1r | 29 lines of body and a postscript of about 12 lines, in clear Italian with 112 words or signs in cipher. The page begins in mid-sentence; an earlier sheet is not in the record. The verso has no cipher |
| Units | 600: 580 cipher signs, 3 signs not legible (`?`), 4 clear-script letters inside cipher words, 6 of the abbreviation sign `&`, 7 codes (`I.` five times, `PP.`, `25.`) |

## The system

A simple substitution with letter-like signs: 25 signs for 19 letters in `key.tsv` (two signs each for a, c, e, g, u; three for p; u and v one letter; no q, z or x). Single words and phrases are enciphered inside a clear letter, with word division kept. Persons are hidden twice over: by codes written in clear script with points (`I.`, `PP.`, `25.`, and `.50.` in the clear text), which the key does not touch and which we have not identified. One abbreviation compound (`&`) is written as a single sign.

## How the key was obtained

1. First transcription of the cipher words (pass 1), frozen. An annealer of our own with an Italian quadgram model, four restarts of 20,000 steps, no crib and no gloss: two restarts gave Italian (rimetendolo, volessero, dubitiamo, li feudi, compromesso, negotiato, la causa). The output showed that pass 1 had merged two pairs of signs (the a sign 4 with the u sign q; the t sign g with the u sign y).
2. Second transcription by the same reader (pass 2), **not blind**: made after the solver output. The key was frozen from it: `timestamps/first/stamped/KEY_aug1612.tsv`.
3. A blind second reader (`transcription_blind.txt`): another session that opened only the page images, with its own sign names, frozen (md5 88b10684...) before it opened the key, pass 1, pass 2 or any decode.
4. A consensus of pass 2 and the blind transcription, settled on crops, with a single decoder, a file of label aliases, a file of 13 coordinate overrides and a ledger of one row per unit (`timestamps/repair/stamped/`, stamped 11 Nov 2026 21:22 GMT).
5. 12 Nov 2026: the reviewer's readings checked on the image (`review.tsv`), the clear text read in full for the first time, and these files made.

## Aliases and overrides: what is not the key

A review of our own files called this reading plausible rather than solid because the decode leans on aliases and overrides. This is exactly what they are (`aliases.tsv`, `overrides.tsv`, and the last block of `counts.txt`).

- **Key table**: 25 sign-to-letter values, fixed on 11 Nov from the solver and from reading pass 2. Of the 562 units the ledger counts as read by the unit rule, 535 are read by a key sign under its own label.
- **Renamed labels, 19 units**: the blind reader named two signs differently (R for the capital p-form K, D for the tailed e z). These are the same written signs under other names; no reading decision is involved. The blind reader's x (3 units) is likewise the looped t sign g.
- **One split made after decoding, 8 units**: the blind reader used one label, u, for two forms: the plain u of two angular minims (f in the key) and a rounded form with a curl at the top right. In the consensus the rounded form is labelled υ and read as the n sign (o), at L06, L07, L12 twice, L13, L16 twice and L23. **This split was made after the decode was known**, from the look of the signs on crops, by a reader who knew what each word should be. It is the one alias that is a reading decision. In the blind transcription's own count all 8 are scored emended. If the 8 are scored emended in the consensus as well, the reviewer's figure of 91.5% becomes 530 of 587 = 90.29% (`counts.txt`, tally E).
- **13 overrides by coordinate**, all listed in `overrides.tsv` with their reasons, none ever counted as read: 4 clear-script letters inside cipher words (L04 o and s; L14 4 and v); 6 cipher signs given a value from context (L09 the gutter sign, L12 the Z form, L14 and L19 the signs under blots, L21 and L24 the closed a for f); 3 signs marked unread (L10 the gutter sign; L19 signs 2 and 3). They were fixed by looking at crops after the decode, not blind. The issue listed 4 of the 13 as examples; all 13 were in the stamped file.
- **No value at all**: the `&` sign and the codes.

## Counts

All figures are full counts over `units.tsv`, made by `scripts/build.py` and printed with their parts in `counts.txt`. S = the key and the label aliases give the letter that is read; E = emended, supplied or overridden; N = unread.

| Tally | S | E | N | Units | S / units |
|---|---|---|---|---|---|
| A. Issue, unit rule (cipher signs only) | 562 | 6 | 15 | 583 | 96.40% |
| B. Issue, "conservative" (cipher signs only): the 94.0% | 548 | 20 | 15 | 583 | 94.00% |
| C. The reviewer's rule, our count | 538 | 34 | 15 | 587 | 91.65% |
| D. The reviewer's own count | 537 | 35 | 15 | 587 | 91.48% |
| E. As C, with the 8 rounded-u units also emended | 530 | 42 | 15 | 587 | 90.29% |
| H. Blind transcription, the reviewer's rule | 517 | 53 | 17 | 587 | 88.07% |
| I. After the image review of 12 Nov, unit rule (not blind) | 573 | 14 | 1 | 588 | 97.45% |
| J. After the image review, whole-word rule (not blind) | 534 | 53 | 1 | 588 | 90.82% |

**Why 94.0% did not reproduce.** B and C differ in two ways, and the reviewer is right on both. (1) B left out of the total the four clear-script letters inside cipher words (o and s in `6osp`, 4 and v in `4v`): 583 + 4 = 587. (2) B's rule made a word wholly emended only when a letter had been supplied (HONE{S}TARE, HABB{I}NO). COSI and CONSCESSO, whose key output differs from the reading, kept their other letters as read: 2 units of COSI and 8 of CONSCESSO. So S is 548 - 10 = 538 and E is 20 + 10 + 4 = 34. The reviewer has 537 and 35. The one unit is probably the blot sign of CONSCESSO, which B already held as emended: taking all nine units of the word off 548 gives 537. That is our inference, not his statement. We state his figure.

**The blind figure.** The issue cited 90.2% for the blind transcription (526 of 583, tally G in `counts.txt`). Under the reviewer's rule it is 517 of 587 = 88.07%.

**After the review.** With the reviewer's three readings, one unit is unread (the gutter sign on L10). No unit was moved to "read" on the strength of a sign relabelled after the word was known: the relabelled, added and emended signs are E. By units 573 of 588; with every emended word counted wholly emended, 534 of 588, which is lower than C because three more words are now read with an emendation.

**By words.** Of 99 cipher word rows, 85 are literal in the stamped ledger; without the two words completed at the torn edge, 83, the reviewer's number. `reading.md` has 314 words and 56 holes by the README rule as we count it: 0.849. That figure covers the body and the postscript as far as "ci aiuti"; the clear lines after it (names, news, close) are only partly read and are set apart.

## Checks

- Shuffled keys, our own script, 11 Nov: the blind transcription under the key puts 394 of 587 cipher signs in Italian dictionary words (67.12%); the best of 5,000 shuffled keys puts 60 (10.22%); none of the 5,000 reaches the real key (`timestamps/first/stamped/baseline_R2.out`). On pass 2: 301 of 607 against a best of 40. The reviewer reports his own control: 0 of 5,000.
- The stamped decoder reproduces the stamped counts: `timestamps/repair/stamped/CHECKS.txt`.
- `scripts/build.py` checks that the cipher words in `transcription.txt` equal the stamped consensus words (30 lines, 112 words: pass) and reproduces tallies A, B and G from the stamped ledger.
- `docs/_validate.py` was not run; no `outcome.validation` is claimed.

## Answers to the check on issue #427

1. **94.0% does not reproduce: 537 of 587 = 91.5%.** Agreed. See "Counts": both tallies, the 4 units left out of our total and the 10 units wrongly kept as read. Our count by his rule is 538; we cannot place the last unit for certain.
2. **Three undeclared emendations (COSI, CONSCESSO, AV).** Agreed. All three were in the override file, and the lines of the issue showed the key output beside the reading, but the issue listed only 4 of the 13 overrides and its count did not treat the three as emended words. `holes.md` now lists all 14 emendations with place, cipher, key output, reading and reason; `overrides.tsv` has all 13 overrides by coordinate.
3. **L16 INGANO.** The reviewer is right. On the image a long faint stem stands before the u and was dropped by both our transcriptions; the u is the rounded form. `pυl4oc` gives INGANO by the key: "et scoprir l'ingano". Our note of 11 Nov had the stroke as a "hairline lead-in" and did not adopt the word.
4. **L19 ASTUTIA.** Right as to the word; we differ on one sign. On our image the signs are 4, a 7 form, g, a blot with a long stem below it, g, p, 4. The blot hides sign 4, the u. Sign 2 looks to us like the r sign, not the s sign, and no sign is hidden by the first blot, which sits over the top of the opening 4. So we read a[s]t[u]tia with the s emended. The clear word after it is probably "cavato": "Habbiamo però con astutia cavato una letera del Prevosto".
5. **L17-18 SCR[I]TURA.** Right. The sign before the hyphen is the 7 form (r), small; both our readers had y. The i is not on the sheet and nothing is lost at the edge there: the hyphen follows the r directly.
6. **L14 CONSCENSO.** Right as to the word (consenso). The sign is wholly under the blot on our image, so we cannot confirm its shape; it stays an emended unit with the value n in place of our s.
7. **L04 "sia".** Right: "se la cosa sia così". Our first pass had "sia"; the blind reader and the issue had "sua".
8. **Full transcription with the clear text, key with aliases and all overrides, decryption, reading, translation, summary, second transcription.** All here; see "Files".

## Other corrections to the issue, found while reading the clear text

- **".50." is not "S.S.".** The issue read "ma da S.S. non fu parlato" and translated "His Holiness said nothing". The sheet has `.50.`, written with points like `25.`, here and in the postscript ("se .50. dica da dovero"). It is a code for a person. The Pope does not appear in the letter.
- **"at Milan"** in the issue's summary came from the postscript, which names the Governor of Milan and "siamo stati a Milano". Where the arbitration was to be held is not said.
- **"I. is very melancholy"**: "stava", was.
- The clear text of the issue was "approximate" and had nine ellipses. It is now read in full, by one reader, with doubtful words marked. Several clear words changed: "over non habbino havuto ardire", "Et se pur la vera causa", "di ricever le sue ragioni" ("di ricever" was missing in the issue), "hanno scritti più", "et scoprir l'", "Che al sicuro quella aggionta", "Puol anco esser", "che ci concorrono", "senza pena", "stava molto malenconico", "et ha assai procurato", "ma non ha mai voluto", "siate informato", "senza bisogno", "nel scriver al Prevosto".

## Summary

Part of a report, in the first person plural, to a correspondent addressed as "Sig.r mio" and "V.S.", about a negotiation over fiefs. Rochetta is named. The other side had said they wanted various things; a person hidden as 50 said nothing and referred the matter to the Provost, and it was settled through a person hidden as I. The writer doubts this: he thinks they wanted something else and lost their nerve. The ministers pressed harder than I. himself for the fiefs not to be excluded from the "compromesso" (the agreement to arbitrate); the Grand Chancellor and the Provost were agreed. By cunning the writer's side has got hold of a letter of the Provost, which says that a certain addition can only mean the total exclusion of the fiefs, the last words being there to save appearances. Or perhaps they mean no such thing: the deed is only a private one, without a penalty, and the party is a minor. I. was very low and has tried to visit PP., who would not have it. The reader is told to keep informed and on guard, not to show his hand without need, and to take care in writing to the Provost. The postscript adds that the Governor of Milan has offered to write to the King and has written to the Spanish ambassador, and that the writer doubts whether 50 is in earnest.

## Persons and context

Not established. I., PP., 25 and 50 are not identified. "Gran Canceliero", "Governor of Milan", "the King" and "Ambassador of Spain" suggest the Spanish State of Milan, and "Di Carp." may be Carpi; neither is verified, and which fiefs and which house are meant we do not know. The attribution to Girolamo Augustoni is the library's. `[?A.V.]` on L14 is doubtful (see `holes.md`). No claim is made about the dispute beyond what the text says.

## Integration check (12 Nov 2026)

Verification of the pull request files, before the write-up.

- **Decoder.** A decoder written separately from `key.tsv` and the label aliases (R = K, D = z, x = g, the rounded u = n) reproduces the K lines of `decryption.txt` for all 30 lines that carry cipher (112 cipher words); the 11 clear-only lines have no K line.
- **Words.** `reading.md` has 355 words with the bracketed groups counted as one, 53 of them holes: 0.851. The contributor's 0.849 (314 words read and 56 holes, 370 in all) is the figure kept; the clear text and the cipher are counted together, doubtful clear words are holes, the codes I., PP., 25. and .50. are holes.
- **Units.** The tallies in `counts.txt` are internally consistent (A, B, C, D reconcile unit by unit). The strict figure for the class is not the unit count: it is the word figure above; the unit figure is the reviewer's rule, and 94.0% is withdrawn.
- **Hashes.** The SHA-256 of each `MANIFEST.sha256` equals the message imprint of its RFC 3161 token (first 11 Nov 2026 21:08:13 GMT, repair 21:22:32 GMT); the 26 stamped files that were sent hash-match their manifests. The signature chain and the OpenTimestamps proofs were not verified. The consensus transcription is not blind, and the rounded-u split was made after decoding (declared above).
- **Image.** Not re-imaged at integration. The earlier verification of the issue compared about 35 cipher words (about 200 signs) of c. 1r with the image and found the three readings now adopted (INGANO, ASTUTIA, SCR[I]TURA), CONSCENSO and "sia". The clear text and the postscript were read once by one reader and have no second reader.
- **Statistical test.** `docs/_validate.py` on `validation.tsv` (583 cipher tokens after the review, 27 types): pass (reading -2.179 per letter, random keys -4.981, key annealed onto shuffled ciphertext at best -2.979).
- **Order of events.** That the first key was frozen on 11 Nov and the blind transcription made before the key was opened rests on the contributor's record (his manifests and md5 values); the token imprints and stamped files agree with it.
- **Catalogue.** Entry 1569 held Augustoni (1612) and Olivazzi (1725), unrelated; Augustoni leaves it and Olivazzi stays. The vetting note called the cipher "Greek-letter-like", "about 20 lines": it is 112 cipher words inside a clear letter on 29 lines and a postscript.

## Prior art

None found; priority not established. Checked on 11 Nov 2026: this repository (row 1569 open, no target, no pull request), the catalogue vetting, web searches for the letter and its matter, and the Archivio di Stato di Modena inventory of the Cancelleria ducale, Ambasciatori, Milano (no Augustoni between 1600 and 1620). Not checked: Biblioteca comunale di Correggio, "Notizie sparse della famiglia Augustoni"; Archivio di Stato di Milano, Carteggio delle cancellerie dello Stato; the printed Campori catalogue; the Este agents' series in Modena page by page.

## Limits

- One page, 587 cipher units, one hand. The key has values seen few times (H once, L twice, h four times) and one sign with a value from a single word (Z).
- The consensus transcription is not blind; the blind one reads 88.07% under the reviewer's rule.
- The image review of 12 Nov and the whole clear text are the work of one reader who knew the key and the proposed words. No second reader has seen them.
- The postscript's clear hand is read only in part; the names, the place and the signature are not established.
- `&` has no key value; four "per" are from context and two places are unread.
- The repository's checker scripts were not run by us (see the pull request text).
- The RFC 3161 tokens' hash and time were read; the signature chain and the OpenTimestamps proofs were not verified.

## Remaining gaps

- codes for persons: I. (five times), PP., 25. and .50. (twice, in the clear text) - blocker: open-codes; not identified, and no other letter of the correspondence has been looked for
- the abbreviation sign & (6 units): "per" from context at four places, unread at L13 and L16 - blocker: too-short; no key value, no other occurrence to test it
- one cipher unit unread: the sign in the gutter at the start of L10 - blocker: illegible; the bowl is lost in the fold; the original or a better image of the fold is needed
- signs under blots (L14, L19) and one sign emended against its shape (L19 sign 2); the reviewer and the contributor read the blots differently - blocker: illegible; values come from the word
- the rounded u-form read as n (8 units), a split made after decoding - blocker: illegible; the two forms of u are told apart only by a reader who knows the word; a blind re-transcription is the test
- the clear text: doubtful words in the body, the postscript read in part, signature, place and names not established - blocker: illegible; one reader with the key known, in a fast hand; a person who reads the hand should go over `transcription.txt`
- prior art at Correggio (Biblioteca comunale, "Notizie sparse della famiglia Augustoni"), in the Archivio di Stato di Milano and the printed Campori catalogue - blocker: needs-physical-access; not online as far as searched

## Escalation

- [x] siblings: no other record of Augustoni in the catalogue entry; Olivazzi (1725), the other item of entry 1569, is a different cipher and was not part of this work
- [x] clear-pages: the verso has no cipher and the leaf no decipherment; the clear text of the letter itself was read in full on 12 Nov 2026 and used to settle doubtful words
- [x] known-keys: none known for Augustoni or this correspondence (the catalogue vetting found no key in the repository)
- [x] print: no edition or reading found (the repository, the catalogue vetting, web searches, the Modena Cancelleria ducale inventory for Milan 1600-1620); Correggio, Milan and the printed Campori catalogue not reached
- [x] key-rebuild: annealer with Italian quadgrams on the first transcription gave Italian without a crib; the key was completed by reading and frozen
- [x] retry: the image review of 12 Nov 2026 re-read the unread and doubtful words with the key; three words closed (INGANO, ASTUTIA, SCR[I]TURA); what stays open is listed above

## Files

| File | What it is |
|---|---|
| `transcription.txt` | the whole page line by line: cipher words in braces exactly as frozen on 11 Nov, clear text as read on 12 Nov |
| `transcription_blind.txt` | the blind second transcription, byte for byte as stamped, with its own sign legend and its notes of the clear words |
| `key.tsv`, `aliases.tsv`, `overrides.tsv` | the 25 key values; the label aliases; all 13 overrides by coordinate |
| `review.tsv` | the 16 unit changes of the image review of 12 Nov 2026 |
| `decryption.txt` | each line three times: as transcribed, under the key alone, as read |
| `units.tsv` | one row per unit: the stamped ledger and the state after the review |
| `counts.txt` | every tally with its parts, and the reconciliation with the reviewer's count |
| `reading.md`, `translation.md` | the complete Italian reading and English translation, holes in place |
| `holes.md` | every emendation, every sign without a key value, every hole and doubtful word |
| `scripts/build.py` | makes the key, alias, override, unit, decryption and count files from `timestamps/repair/stamped/` and `review.tsv`; standard library; runs in this folder |
| `timestamps/` | the two RFC 3161 tokens, their manifests, and 25 of the stamped files (`timestamps/README.md`) |
| `profile.json` | the profile |

## Tools

Claude (Anthropic) models for the transcriptions, the solving, the scripts, the image checks and these files; own Python (an annealer with Italian quadgrams, a shuffled-key baseline, a per-unit counter). Images: Estense Digital Library IIIF.
