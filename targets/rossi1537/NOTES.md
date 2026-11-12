# Pier Maria Rossi di San Secondo to Ferrante Gonzaga, San Secondo, 4 and 8 Nov 1537 (Biblioteca Estense, Autografoteca Campori, Rossi cc. 31-34)

Status: read in part (contributed, PR #451, issue #428). Key recovered from the ciphertext alone. By the README word rule 0.934 of the two letters is read (letter A 0.937, letter B 0.928; holes marked in the readings); by cipher units 93.07% with d and t taken from a blind shape test, 94.89% with a second look that was not blind.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Sent as issue #428; checked by Daniel Bourdeau on 11-12 Nov 2026, who asked for these files and raised the points answered under "Answers to the check on issue #428". Integrated on 12 Nov 2026 (see "Integration check").

Catalogue entry 1564 lists five letters of Gonzaga clients to Ferrante Gonzaga. This folder holds the two Rossi letters. The Muzio letters of the same entry are in `muzio1550` (pull request 445): a different cipher, with its own page. Entry 1564 now keeps only the Gosellini letter of 1555.

## The documents

| | Letter A | Letter B |
|---|---|---|
| Shelfmark | Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera R, Rossi (conte di San Secondo), cc. 31-32 | the same, cc. 33-34 |
| Date | San Secondo, 4 Nov 1537 | San Secondo, 8 Nov 1537 |
| Record | https://lodovico.medialibrary.it/media/schedadl.aspx?id=2d0df6d1-9d12-4da0-90ed-8de7d910b63e | https://lodovico.medialibrary.it/media/schedadl.aspx?id=4a838739-0cb9-409f-93e5-c1076143ddb3 |
| IIIF manifest | https://edl-jarvis.cultura.gov.it/meta/iiif/2d0df6d1-9d12-4da0-90ed-8de7d910b63e/manifest | https://edl-jarvis.cultura.gov.it/meta/iiif/4a838739-0cb9-409f-93e5-c1076143ddb3/manifest |
| Cipher | c. 31r, 22 lines (L01-L22), 910 units; c. 31v, 14 lines (V01-V14), 703 units | c. 33r, 17 lines (B01-B17), 755 units |
| Clear | four lines and the date at the foot of c. 31v, in the writer's hand | two lines, the date and the signature at the foot of c. 33r |
| Decipherment on the sheet | none | none |
| Other pages | address leaf: to Ferrante Gonzaga, viceroy of Sicily, "in Messina o dove sera" | address leaf |

The whole cipher is 53 lines and 2,368 units. Seven tokens inside the cipher are in clear and are not units: the roman numerals xx and xxxx on L13 (six x), and xij on B03. The Latin word *fuit* at the head of V10 is also in clear. Counting the clear tokens, letter A recto and letter B, the part sent in the issue, come to 916 + 756 = 1,672 tokens.

Images are not in the repository. The pages were fetched from the Estense IIIF service as 1,024 px tiles at full resolution and stitched.

The clear close of letter A says why the letter is in cipher: "havendo pensato che a questa V. Ex.tia haverà havuta la zifra, ho scritto questa". Rossi had sent Ferrante the cipher and assumed it had arrived.

## The system

Simple substitution on a symbol alphabet. Twenty letters; homophones for a (3), i (3), c (2), g (2) and u (2); no nulls and no code groups seen; roman numerals in clear. Key: `key.tsv`. Sign names are the codes of the first transcription; their legend is at the head of `transcription_A.txt`.

**The sign P stands for both d and t.** The first transcription gave one code, P, to a tall sign with a hat. On reading, that code turned out to cover two letters, d (89 times) and t (152 times). They are two shapes: for d the hook of the hat closes onto the stem; for t the hat stays open over a separate tick. A third tall sign, coded D, has a closed arch with a bowl at the foot and is l.

How well can the two shapes be told apart without knowing the word?

- A second look at every P sign, by a reader who knew the hypothesis (not blind), found the d shape on 79 of the 89 signs read d, leaned to d on 3, found the t shape on 4 (one of them a leaning) and could not decide 3.
- A blind test put each of the 256 P signs, cut out and under a random id, before a reader who saw only the crop. Where both that reader and the second look gave d or t, they agree on 178 of 215 signs: **82.8%**.
- Measured against the reading (recounted from `dt_ledger.tsv` at integration): of the 241 P signs read d or t, the blind classes A and B give the reading's letter on 187 (77.6%); the non-blind look gives it on 214 (88.8%). The contributor's 195 (80.9%) and 231 (95.9%) also count as agreeing 8 signs the blind reader called unclear and 17 signs the second look never saw, where the printed t happens to be the reading.

So the shape rule is real but not safe sign by sign, and **in practice d or t is chosen from context**. That is why the count with the blind classes (93.07%) is below the count with the non-blind look (94.89%): the non-blind reader could be led by the word. `dt_ledger.tsv` lists all 358 tall signs with both verdicts.

The blind test covers sign P only. For the l sign (D) the blind classifier's raw labels were not usable (it put most of them in the d class), and the scored labels set them from the transcription code. The l shape therefore has no blind confirmation; details in `blind_agreement.txt`.

Other weak points of the first transcription that the reading corrects: S (p) for 8 (u) ten times; the sign # is a in its small form and q in its tall form before u, and four times that q is followed by S where the word needs u.

## How the key was obtained

1. 11 Nov 2026. Both letters transcribed from the images by one reader, and the transcription frozen (hashes recorded) before any decoding: `transcription_A.txt`, `transcription_B.txt`.
2. An own annealer with Italian quadgrams, first tested on a synthetic text of 904 characters with d and t merged and homophones (86.5% of letters recovered), was run on the frozen transcription: six restarts of 50,000 steps, -4.227 per character, continuous Italian from the first run ("che Pinarolo et Turino sono socorsi et dodici pezi de artiglieria"). No crib and no gloss was used; the leaves carry no decipherment.
3. The key was completed by reading (rare letters b, f, g, m, p, z, which the solver had merged into frequent ones), and the reading aligned unit by unit to the frozen transcription.

Method: key recovered from the ciphertext alone.

## Checks

- **Count by units** (`counts.txt`, `units.tsv`, `scripts/build.py`). S = the key gives the letter the reading takes; E = the reading takes another letter; N = not read.

| | units | key alone, P printed t | d/t by the non-blind look | d/t by the blind test |
|---|---|---|---|---|
| A recto (c. 31r) | 910 | 820 = 90.11% | 851 = 93.52% | 829 = 91.10% |
| A verso (c. 31v) | 703 | 642 = 91.32% | 672 = 95.59% | 658 = 93.60% |
| A whole | 1,613 | 1,462 = 90.64% | 1,523 = 94.42% | 1,487 = 92.19% |
| B (c. 33r) | 755 | 699 = 92.58% | 724 = 95.89% | 717 = 94.97% |
| Both | 2,368 | 2,161 = 91.26% | 2,247 = 94.89% | 2,204 = 93.07% |

  With the leaning verdicts of the non-blind look counted as well: A recto 852 = 93.63%, A verso 673 = 95.73%, both letters 2,249 = 94.97%. Unread in every column: 73 units (A recto 40, A verso 7, B 26).
- **Count by words** (README read bar; our own count after `research/reading_audit/v2_score.py` and `v10_relabel.py`, which we read and did not run): letter A 344 words read and 23 holes (367 in all), 0.937; letter B 154 words read and 12 holes (166 in all), 0.928; both letters 498 of 533 = 0.934. Every unread group, every doubtful word and every word with a supplied letter is a hole.
- **Shuffled keys** (11 Nov; Italian quadgram score of the key-only decryption, 5,000 shuffled keys): whole text -4.319 against a best of -5.713; letter A -4.328 against -5.745; letter B -4.295 against -5.561. None of the 5,000 as good in any of the three. Letter B with a key voted from letter A's reading only: -4.314 against a best of -5.644, none as good; that key reads 698 of B's 755 units (the reading of B was made with the key in hand).
- **Solver on letter A only, applied to letter B**: score -4.258 against a best shuffle of -5.038, none as good; but only 622 of 755 units (82.38%), because the solver merges rare letters. A variant with a letter-frequency penalty did worse (62.78%) and was dropped.
- **Null controls** (11 Nov): the same annealer on five frequency-preserving permutations of the cipher stream ends at -4.610 each time (a degenerate key that prints i throughout), against -4.227 for the real stream. With each letter limited to its number of signs plus one: real -4.230; three controls -4.971, -4.983, -4.972.
- **Blind second transcription** (`transcription_blind.txt`, `transcription_blind_NOTES.md`, `transcription_blind_signs.tsv`, `blind_agreement.txt`): another session, which opened only the page images, transcribed all 53 lines in its own sign names. Aligned line by line, 2,247 of 2,363 unit pairs agree (95.09%); 19 units are in the second transcription only and 13 in the first only. It did not split d from t either. Decoded through the key and counted against the reading it gives 2,087 of 2,370 (88.06%).
- **Blind shape test**: above, and `blind_agreement.txt`.
- **The maintainer's check** (issue #428): his own decoder reproduced the 39 literal lines sent; his shuffled-key controls gave 0 of 5,000; he compared about 95 signs of letter B with the image.

## Answers to the check on issue #428

1. **Letter A verso.** V01-V14 (703 units) is here in full: transcription, decryption, reading, translation. All 2,368 units are in `units.tsv`.
2. **The recount.** Your figures were about 95.9% for letter B and about 93.6% for letter A recto. Ours: letter B, non-blind consensus, 724 of 755 = 95.89%. Letter A recto, non-blind consensus, 851 of 910 = 93.52% with firm verdicts and 852 of 910 = 93.63% with the one leaning verdict on that page. The issue gave no figure for A recto alone; its 94.42% was letter A whole (1,523 of 1,613), which the verso lifts (672 of 703 = 95.59%). Your 1,672 units for the part sent equals our 910 + 755 = 1,665 units plus the 7 clear tokens.
3. **Sign P.** Stated under "The system". One correction to the issue: the 178 of 215 counts firm and leaning verdicts of the non-blind look, not firm ones only as the issue said; with firm verdicts only it is 172 of 208 = 82.7%.
4. **Reading and translation.** `reading_A.md`, `reading_B.md`, `translation_A.md`, `translation_B.md`: complete, no ellipses, every hole in place; `holes.md` lists each hole with what the key gives there. Summaries are in `profile.json` and below. "Astolfo = del Vasto" stays unverified.
5. **Second transcription and ledger.** `transcription_blind.txt` and `dt_ledger.tsv`, with the stamped score outputs.

## Changes to the reading since the issue

The unit ledger is the one stamped on 11 Nov 2026 and is unchanged, so the figures above are those of the issue. The sentences differ from the issue's in these places, each from the image or from the aligned letters:

- L03-L04 "l'Angiolino mi espetta" is read as "is waiting for me" (the issue's "mi e spetta" was left unexplained). "verna fra" stays doubtful.
- L10 "tale uoche se retirato" is given as "tal è [?voce] che s'è retirato".
- L11 "[?capi]", L17 "spavent[ar]ebono" and "[?Vicencio]" (the last sign is o on the image, found on 11 Nov by the second look).
- B12 "[?vedeti] che principii": the six signs after the place-name are 8 i P i P : on the image. The place-name is then five signs, not eleven.
- B16 "non mi lassa [?viver] [?di] com[...]gie": a proposal, with S taken as u.
- The clear closes were read from the image (12 Nov 2026) and replace the issue's partial ones.
- Looked at again on the image and left unread: V02-V03 "so" and two signs; V03 "quela de" and four signs (the key gives "zais"); B12 the place after "Castel"; B16-B17.

## Summaries

**Letter A, 4 Nov 1537.** Written after supper and, the count says, a good deal of muscatel. He mocks an Imperial commander he calls Astolfo, who had written all over Italy that he would fight the French and has instead withdrawn "to preserve an army": twenty miles the first time, forty to come, unless "your successor, the most unconquered stradiot with his beard" holds them. The first news he expects is that Astolfo has ridden post to ask for money. Cesare Pallavicino has gone post-haste to the Marquis to be at "this glorious retreat". He recalls the departure from Genoa in December ("not a flight, or we would not have gone to the mole to embark") and Monfalconeto's advice, then stops himself, blames the wine, and says he speaks freely because he does not have to deal with Covos. He promises day by day reports of Astolfo's cowardices.

**Letter B, 8 Nov 1537.** The second retreat "of this coward Astolfo" was forty miles, as he had said, with twelve guns lost. He laughs fit to burst "like Margutte". Pinerolo and Turin are relieved; there is no money. Men from Mirandola have raided the Cremonese and sacked Piadena and a second place whose name is not read; most of the money used to come from Cremona. He must stop to keep company with "the gran Meo, your prince of Luzara", who has to be put to bed after supper.

## Persons and context

- The writer is Pier Maria III de' Rossi, count of San Secondo (1504-1547), married to Camilla Gonzaga. The addressee, Ferrante Gonzaga, was viceroy of Sicily; the address says so.
- **Astolfo** is a mock name (the boastful paladin of Ariosto and Pulci; "Marguto" in letter B is Pulci's Margutte, who dies laughing). From the retreat, the forty miles, and Pinerolo and Turin relieved, we take him to be the Imperial commander in Piedmont, Alfonso d'Avalos, marchese del Vasto. **Unverified**: the letters do not say so, and letter A also speaks of "il marchese" by title.
- In October and November 1537 the French under Montmorency forced the pass of Susa and relieved Turin and Pinerolo, del Vasto raised the sieges and withdrew, and a truce followed in November. Galeotto Pico of Mirandola was under French protection. This fits both letters. Sources for this paragraph are general reference works (Wikipedia, "Anne de Montmorency" and the Italian pages), not checked against a history of the campaign.
- **Zopo** ("our Lame One", whose consent Astolfo had), **Vicencio veneciano**, **Monfalconeto** and the **gran Meo** are not identified. "Your prince of Luzara" points to the Gonzaga of Luzzara; "principe" is mocking. **Covos** is Francisco de los Cobos, the Emperor's secretary.

## Integration check (12 Nov 2026)

Verification of the pull request files, before the write-up.

- **Decoder.** A decoder written separately from `key.tsv` and the first transcriptions (P printed t, the sign # read q before 8 and a elsewhere) reproduces the K lines of `decryption_A.txt` and `decryption_B.txt`: 53 of 53 lines, letter A recto and verso and letter B.
- **The ledger.** `units.tsv` has 2,368 rows, as stated; letter A verso (703 units) is now in it. From `dt_ledger.tsv`: blind against non-blind shape verdicts 178 of 215 = 82.8% (firm verdicts only 172 of 208), as stated. The two agreement figures against the reading are corrected under "The system" (187 of 241 and 214 of 241, not 195 and 231).
- **Words.** The word counts of the readings were recounted from `reading_A.md` (363 words, 21 bracketed holes plus the words inside multi-word brackets) and `reading_B.md` (166 words, 12 holes): they agree with 0.937 and 0.928. In `NOTES.md` the "344 words" and "154 words" are the words read, not the totals. No word of the readings is counted as a hole because of d/t alone; where the P signs were taken d or t from context, the unit count with the blind classes (93.07%) shows the effect.
- **Hashes.** The SHA-256 of each `MANIFEST.sha256` equals the message imprint of its RFC 3161 token (first timestamp 11 Nov 2026 21:08:07 GMT, blind shape test 21:10:37 GMT); the 14 stamped files that were sent hash-match their manifests. The first manifest also lists Gosellini files that are not in the folder and not part of this target. The signature chain of the tokens and the OpenTimestamps proofs were not verified. The frozen key differs from `key.tsv` only by the d value of P, the u/v and q readings of # and 8, and rows for signs without a value (declared above).
- **Image.** About 70 signs of the first part of V01-V03 (letter A verso, new in this folder) were compared with the Estense image of c. 31v and agree; the earlier verification of the issue compared about 95 signs of letter B lines 1-2. The d and t shapes cannot be told apart reliably at that size, as the shape test says.
- **Statistical test.** `docs/_validate.py` on `validation.tsv` (2,295 read tokens): verdict "underdetermined": the reading scores -2.330 per letter against -4.835 for random keys, but an annealer started from a random key on the real ciphertext reaches -2.323, so the letter model cannot tell the reading from a key fitted to the text. That is what the recovery by annealing predicts; it is not a pass.
- **Order of events.** That the first transcription was frozen before decoding rests on the contributor's record (one commit, his manifests); the token imprints and stamped files agree with it.
- **Catalogue.** Entry 1564 held five letters; the Rossi letters leave it here and the Muzio letters in `muzio1550`, a different cipher. The Gosellini letter of 1555 stays; the contributor's first manifest lists a file with Gosellini in its name (`gosellini_c12v_c13r_digits.txt`), which was not sent and was not looked at.

## Prior art

No edition or decipherment of these letters was found, and priority is not established. Checked on 11 Nov 2026: this repository (entry 1564 open, no target); the leaves (no decipherment); the Estense records; six web searches. Not checked: Archivio Gonzaga, Mantua, b. 1911; Archivio di Stato di Parma, Famiglia Rossi bb. 8-12; the Rossi di San Secondo archive (Lincei/Corsiniana), series I cart. 26; the Olschki volumes on the Gonzaga papers; the Guicciardini and Aretino correspondence editions.

## Limits

- Sessions of one model family did the transcriptions, the solving and the reading. No person read the signs without AI.
- d and t are chosen from context (above). The l shape has no blind confirmation.
- The reading of letter B was made with the key in hand; the independence in this folder is the frozen first transcription, the blind second transcription, the shuffled-key and null controls, and the blind shape test for sign P.
- The second look at the shapes was not blind.
- 73 units are unread; several words are doubtful (`holes.md`). The new doubtful words of 12 Nov were proposed by one reader from crops and are not in the unit ledger.
- The clear closes were read once from the image.
- The identifications are ours and unverified.

## Remaining gaps

- d and t: one transcription code (P) for two shapes, 256 units; the blind shape test agrees with the second look on 82.8% - blocker: illegible; the shapes are not reliably told apart on the image, so d or t is chosen from context; a person reading the heads on the original or a blind re-transcription that splits them would settle it
- the unread places L05, L08, L17 (a name), L21, V02-V03, B12 (a place near Piadena), B16-B17 (73 units in all) - blocker: illegible; looked at again on the image on 12 Nov 2026 and left unread
- the three signs without a value (A, the apostrophe mark, the bare tick) - blocker: too-short; two occurrences each
- the l shape (sign D) has no blind confirmation, and the second look was not blind - blocker: illegible; the blind classifier put most l signs in the d class
- prior art in the Archivio Gonzaga (Mantua, b. 1911), the Archivio di Stato di Parma (Famiglia Rossi bb. 8-12), the Rossi di San Secondo archive and the printed Gonzaga correspondence - blocker: needs-physical-access; not online as far as searched

## Escalation

- [x] siblings: letters A and B of the same file, and their address leaves, opened and read; the Gosellini letter of the same catalogue entry (a different cipher) was not part of this work
- [x] clear-pages: the clear closes of letters A and B read on 12 Nov 2026; no decipherment on any leaf
- [x] known-keys: the repository's Gonzaga keys belong to other systems and decades (Charles V chancery ciphers, the Nevers figure cipher, the Guastalla digit cipher); none was tried sign by sign
- [x] print: no edition or decipherment found (six web searches, the repository, the Estense records); the archives and editions listed under Prior art not reached
- [x] key-rebuild: annealer with Italian quadgrams on the frozen first transcription gave continuous Italian; rare letters completed by reading; the shuffled-key and null controls run
- [x] retry: every unread place looked at again on the image on 12 Nov 2026; the new doubtful words of that day are in `holes.md`

## Files

| File | What |
|---|---|
| transcription_A.txt, transcription_B.txt | first transcription, frozen before decoding |
| transcription_blind.txt, _NOTES.md, _signs.tsv | blind second transcription of both letters, its notes and sign list |
| key.tsv | the key, with counts |
| decryption_A.txt, decryption_B.txt | line by line: transcription, key output, key output with d/t by shape, aligned reading |
| units.tsv | one row per unit, with every verdict and class |
| dt_ledger.tsv | the 358 tall signs: non-blind verdict, blind class, reading |
| shape_verdicts_nonblind.tsv | the second look's verdicts as recorded on 11 Nov |
| counts.txt | the arithmetic |
| blind_agreement.txt | the two blind tests as scored |
| reading_A.md, reading_B.md, translation_A.md, translation_B.md, holes.md | sentences, translation, list of holes |
| scripts/build.py | makes units.tsv, the decryption files, dt_ledger.tsv and counts.txt from the stamped inputs (standard library) |
| timestamps/ | two stamps and the stamped files |

## Tools

Claude (Anthropic) models for the transcriptions, the solving, the scripts and the checks. Own Python: an annealer with Italian quadgrams, a shuffled-key baseline, a per-unit counter. Images: Estense Digital Library IIIF. The repository's scripts were not run by the contributor.
