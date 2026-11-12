# ridolfi1646: Ludovico Ridolfi to the duque de Arcos, viceroy of Naples, Rome, 8 May 1646 (catalogue 748, AHNOB OSUNA,C.3456,D.107)

Status: read in part (Brice Dudout, 11 Nov 2026; 396 of 431 words = 91.9% by the README read bar, which leaves out the 5 unresolved codes, the 9 restored words and the 21 nomenclator values given by the sense alone; 5 nomenclator codes open; key validated on held-out page 5 by the contributor's pre-registered test, COV 0.817 vs 0.487 / 0.600). Before the blind re-reading on the images the same count gave 384/431 = 89.1%. The contributor's own count, which takes the 21 sense-only code values as read, is 417/431 = 96.8% (integration check of 12 Nov 2026 below).

Contributed by Brice Dudout (Europe chiffrée). Key proposed by Claude Fable 5.2 (Anthropic) from pages 1-4; held-out
validation, page 5 reading and write-up by Claude Opus 5.5 agents. Catalogue entry **748** (PARES sweep, "Not in the repo");
this target is the third item of that entry, D.107. No decipherment of the time, no edition found (see profile.json).

## Document

Toledo, Archivo Histórico de la Nobleza, OSUNA,C.3456,D.107 ([PARES 6449375](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/6449375)):
a five-page letter wholly in cipher except the date "Di Roma li 8 Maggio 1646", from Ludovico Ridolfi to Rodrigo Ponce de
León, IV duque de Arcos, viceroy of Naples. 1,412 groups (pages 1-4: 1,313; page 5: 99). The images were used for study
only; none is included here.

The other items of entry 748 are Spanish letters of Antonio Ronquillo (D.102-103, D.104-106); D.104 has its decipherment
of the time in D.105; both are in other systems than D.107. No other Ridolfi letter in cipher was found in
OSUNA (PARES, 28 Oct 2026).

## System and key (`key.tsv`)

A numbered Italian cipher: 20-24 = a e i o u; 25-44 = the alphabet a b c d e f g h i l m n o p [39?] q r s t u (so the
vowels have two codes each); syllables in series of five (b 49-53, m 54-58, l 59-63, n 65-69, d 70-74, t 75-79, g 80-84,
f 85-90 without 88, z 91-95), 64 and 97 = che, 98 = chi; three-digit groups 100-243 are a nomenclator; a barred sign X is
punctuation; a superscript dot over a group marks a doubled consonant. Spelling of the cipher: consonants mostly single
(paso, socorso), n for m before p (senpre, tenpo).

The key was proposed by Claude Fable 5.2 (Anthropic) in one API run on pages 1-4 alone (ciphertext-only), and frozen.
Values 28 d, 30 f, 35 m and the unattested syllables (58, 69, 79, 84, 92-95) are restored by the order of the alphabet and
of the series; 47 = z was restored on page 5 after the measure. The nomenclator is read by the sense only (107 Gran Duca,
121 Francesi, 126 V.E., 101 Sua Santità, 114 Duca, 100 Sua Maestà, 108 Cardinale); 103, 110, 115, 116 and 136 are open.

## Validation (`validation.txt`)

Page 5 was transcribed with pages 1-4 on 28 Oct 2026 and kept apart from every attempt; the model was never sent it. The
protocol was hashed before page 5 was decoded (PREREG SHA-256 ce607b24705b4ed2b6106e5a77395f3832429bdcae8c2eae902a42a8f9c2691d).
One measurement: **COV (share of decoded letters covered by Italian words of 4+ letters) 0.817 against at most 0.487 for
200 shuffled keys and at most 0.600 for 200 shuffles of the page's groups**. The thresholds (COV >= 0.75, >= best shuffled
key + 0.25, >= best group shuffle + 0.08) were calibrated beforehand on 51 windows of 99 groups taken from pages 1-4,
because our usual 0.85 / +0.30 rule rejects most in-sample windows of that size. All three held, and the pre-registered
sense check held: page 5 opens with "scrittura richiesta", closing the sentence left open at the end of page 4. The two
superscript dots of page 5 both fall on a doubled consonant (vorrei, accordasse), as the rule learnt on pages 1-4 predicts.
Reservation: the held-out page is small (99 groups), below the 150 groups we now ask for; the letter has no other page.

## Reading (`reading.md`, `translation.md`)

431 words: 390 certain, 27 probable, 9 restored, 5 unresolved. 21 of the 27 probable words are nomenclator values given
by the sense alone, and the README read bar does not count those: **396/431 = 91.9%, read in part**. Before the blind
re-reading (below) the classes were 378 / 27 / 21 / 5, and the same count gave 384/431 = 89.1%. The 21 restored
words were 19 one-digit confusions of transcription v1 between shapes of this hand (2/3/7, 1/2, 3/4, 6/8...), second
readings or a group omitted, and 2 on page 5 (47 = z, 26 for 76); 12 are now confirmed on the images.

## Blind re-reading on the images (11 Nov 2026)

Brice Dudout re-read on the PARES images, blind, the doubtful digit of the 19 groups whose correction a shape can settle
(frozen/BLIND-REREADING.md). For each, the sheet showed the line, the group enlarged and two reference shapes from certain
words elsewhere in the letter, in random order, without values or glosses; two controls with known answers were mixed in.
The integration rule was written and hashed before the sheet was opened (SHA-256 b61a4fd7446559b170195e52c46cb8a83b4834f01e17565350137fba5dfe3adf);
answers SHA-256 c692c679177bdabd9cd9b80d22018233ade6b89b80eedd90b395aa94f0c46ee6. Both controls passed, so the rule was applied.
- 12 corrections confirmed, so 12 words pass from restored to certain: il (1.01), atacatto (1.16), lontano and miglia (1.21),
  perche (2.13), risolutione (3.19), al and Signor (4.02), al (4.04), mandero (4.11), termini (4.17), oferte (5.05).
- 6 images match transcription v1 (still restored: probable cipher-clerk error): il (1.16), Bologna and Milano (2.03),
  quando and al (3.08), loro (4.01).
- 1 undecided: quando (1.12), answer "other" with the remark "5 or 9" (recorded, not a confirmation).
- 2 not on the sheet: di (1.06, a group left out, normal space on the image) and lunghezza (5.02, 47 = z is a value, not a shape).
- Recount with the same script on a copy of the readings where the 12 words lost their marks (frozen/v2/): 390 / 27 / 9 / 5.
- Reservation: one reader; "certain" for the 12 words follows the hashed rule (the word then reads entirely with the frozen
  key); no image or thumbnail is included.

Content: the Pope has refused Don Antonio Ronquillo passage for the five hundred horse the viceroy is sending to help the
Grand Duke of Tuscany, but would grant it towards the State of Milan; Ridolfi advises accepting, since from Forlì the
cavalry can still turn into Tuscany, twelve miles away, if the French attack. No news of the French fleet beyond a
felucca's report that it is in the Gulf of La Spezia; the troops cannot cross the snow-bound Garfagnana, so a landing
towards the Val di Taro and the Parmesan is more likely, which makes Souvré's long talks with "that Duke" suspicious.
Vendôme writes of the Huguenots' resolution to rise and of his own to lead them; the Almirante would pay him the twelve
thousand ducats once ordered by the King. The Bouillon negotiation is stuck; Ridolfi fears that Bouillon, in despair, will
come to terms with the French, Mazarin always doubling his offers. (May 1646 is the month of the French expedition against
the Tuscan presidios.)

## Integration check (11 Nov 2026)

On integration (PR #403) the project re-ran the contributor's frozen scripts and recounted the texts.

- `frozen/scripts/mesure.py`, run on the frozen files with `lang/lexicons/it.json.gz` decompressed as the lexicon (SHA-256
  f4d2f270..., the value in `FREEZE.sha256`), gives the same output as `frozen/scripts/mesure.out`, byte for byte: COV 0.817;
  200 shuffled keys max 0.487, mean 0.251; 200 group shuffles max 0.600, mean 0.415. The script checks every hash of
  `FREEZE.sha256` first; `POST-MESURE.sha256` also checks out.
- `calib.py` reproduces `calib.out` (51 windows of 99 groups; minima 0.783, 0.256, 0.098; the 0.85 / +0.30 rule rejects 44
  of 51), and `decompte.py` reproduces `decompte.out`.
- `key.tsv` carries the frozen proposal unchanged, plus the rows marked as added (47 = z, the nomenclator values, the dot).
  Decoding `transcription.txt` (1,412 groups, identical to `frozen/transcr/`) with it reproduces `decryption.txt` line for line.
- `reading.md` recounted: 378 certain, 27 probable, 21 restored, 5 unresolved of 431 words, so 405/431 = 94.0%. The count
  takes words as its unit and leaves out restored and unresolved words, as the README read bar does. It counts as read
  the 21 nomenclator values given by the sense alone; with those left out too (the README formula leaves out every
  guessed word) the share is 384/431 = 89.1%, and the image check of the restored words would then bring it to 94.0%, not
  over the bar. The letter is under 95% on either count: read in part.
- By the contributor's usual rule (>= 0.85 and >= best control + 0.30) page 5 would not pass: 0.817, and +0.217 over the best
  group shuffle. The rule applied was calibrated for 99 groups on pages 1-4 and hashed before the measure, as declared
  above. The reading itself is the stronger evidence: five pages of connected Italian, and page 5 closing the sentence of page 4.
- Not verifiable from the repository: that page 5 was withheld from the model run, and that the hashes predate the
  decoding of page 5 (the folder arrived in one commit). Both are the contributor's statement.
- Reading read clause by clause against `decryption.txt` and `translation.md`: every clause construes and the translation
  follows it. Not checked against the images: PARES answered HTTP 429 to the integrating session and no image is in the folder.
- The nomenclator range "100-243" above is wider than what the letter shows: the twelve codes that occur lie between 100 and
  136; 243 is only the first reading of a doubtful group (3.20, 243/23) that the reading takes as 23.
- DECODE: `research/archive_sweep_2026-10/known.py` (harvested DECODE dump and repository) on "C.3456" and "Ridolfi" finds only
  catalogue entry 748 for this letter; no DECODE record. The live database was not queried.
- Retry on the texts (the escalation step, as far as it goes without images): the 19 restored words of pages 1-4 are those of
  `frozen/EMENDATIONS.tsv`, hashed before page 5 was decoded. Three of them take the second reading the transcription itself
  carries (1.17 22/27, 3.20 243/23, 4.19 68/67; `reading.md` lists the last as a 7/8 confusion), one supplies an omitted
  group, fifteen change one digit (74 for 34 three times, 24 for 34 twice). On page 5, 47 lies outside the key and 26 is
  read as 76. None contradicts a certain letter and none can be confirmed without the images, so all 21 stay restored.

## Integration check (12 Nov 2026)

On integration of PR #406 (the blind re-reading) the project recounted the files; an independent verifier's report is the
basis of this section.

- The counts reproduce. `frozen/v2/decompte_v2.py` gives `decompte_v2.out` again (390 / 27 / 9 / 5 of 431), and it differs
  from `frozen/scripts/decompte.py` by one path line. The readings in `frozen/v2/lecture-v2/` differ from the frozen ones by
  the twelve restoration marks removed and nothing else. `frozen/v2/SHA256SUMS` checks out on its four files. A second
  decoder written from `key.tsv` reproduces `decryption.txt` on 93 of 93 lines; the PR does not touch the key, the
  transcription or the decryption.
- **Class corrected.** The PR set `Status: read` and `class: read` on 417/431 = 96.8%. That count takes as read the 21
  nomenclator values given by the sense alone (107 six times, 121 five, 126 three, 114 three, 101 twice, 100 and 108 once).
  The README read bar does not count a nomenclator value given by the sense alone, so the figure for this target is
  **396/431 = 91.9%, read in part**, and the profile and the status line are set back to that. 417/431 = 96.8% is the
  contributor's count. `frozen/BLIND-REREADING.md`, a hashed working file of the contributor, still ends "-> read"; it is
  left as it came.
- **How far the twelve confirmations are corroborated.** Each rests on one human reader choosing between two shapes. The
  only other reading of the images available is Malcolm McBratney's transcription (issue #421, next section). It has the
  corrected digit at seven of the twelve places: il 1.01, lontano 2.01, risolutione 3.20, al 4.05, mandero 4.13 and
  termini 4.19 outright, and oferte 5.07 after his own check on the image. At the other five (atacatto 1.17, miglia 2.01,
  perche 2.13, al 4.04, Signor 4.04; places as in `transcription.txt`) his first reader read the uncorrected digit, as
  transcription v1 did, so those five rest on the single blind reader against two machine transcriptions. If the five
  stayed restored the strict count would be 391/431 = 90.7% (412/431 = 95.6% on the contributor's count).
- Not checkable from the repository: that the integration rule was hashed before the sheet was opened (the rule and the
  answer file are not in the folder; their hashes b61a4fd7... and c692c679... are the contributor's statement), and the
  images themselves (PARES HTTP 429 again).
- `FREEZE.sha256` and `POST-MESURE.sha256` check out except for the lexicon file, which is not in the folder (it is
  `lang/lexicons/it.json.gz` decompressed, as the Files table says).
- `_check_reading.py` gives 0.365 on `reading.md`; the marks (brackets, braces, code numbers) break the words it looks for.
  The Italian was read clause by clause again and construes; the translation follows it.

## Independent recovery by Malcolm McBratney (issue #421, 12 Nov 2026)

Malcolm McBratney (Brisbane), working with Claude (Anthropic), reported in
[issue #421](https://github.com/dbourdeau/cyphersolver/issues/421) a recovery of the same letter made, by his record, on
11 Nov 2026 without knowledge of PR #403: his own transcription of the six PARES images, a key from the ciphertext alone,
a decryption, a reading and a translation. He submits it as corroboration, not to dispute credit. His texts are in the
issue and are not copied here. The comparison below was made token by token and value by value.

- **Key.** All 71 of his two-digit letter and syllable values are identical to `key.tsv`, including 47 = z, 64 = 97 = che,
  98 = chi and the unattested 28, 30, 35 restored by the order of the alphabet. He adds 45 x? and 46 y?; this key adds the
  weak 92-95 z-series. The code values agree on 100, 101, 108, 114, 121 and 126, and on the guesses 116 Genova? and
  136 Modena?.
- **Transcription.** Both have 93 lines and 1,412 tokens with the same line lengths; 1,393 of 1,412 tokens agree with the
  first reading of `transcription.txt` (98.65%). Of the 19 that differ, 5 equal this transcription's b-alternative and in
  6 he emends back to this transcription's value.
- **Decryption and reading.** A decoder written from his stated key reproduces all 93 of his decryption lines. His
  reading is the same word for word except for the points below.
- **Open point, 107.** He reads "Duca di Modena?"; this target reads Gran Duca (Tuscany). The letter says the prince's
  border is no more than twelve miles from Forlì, which fits the Tuscan Romagna and not Modena; that is a judgement from
  the geography, not a source check, and 107 stays a value given by the sense.
- **Open point, confino / confine (reading 1.21, transcription 1.22).** He reports that the image shows 66 (ne) for the last
  group, giving confine; this transcription has 68 (no), confino, counted certain. Not checked on the image here.
- Smaller differences: spiaggie against {spiagge}; stano glossed [stando]; 103 "Francia?" (open here).
- **What it does not settle.** At il 1.17, Bologna, Milano, quando 3.08 and loro 4.02 he reads the same digit as
  transcription v1, which supports "written so by the clerk", as the blind sheet found. For al 3.12 there are now three
  readings (24 here, 74 his, 34 intended). At quando 1.12 he transcribed 79 and says the image shows 73; the blind
  reader answered "5 or 9": still open. di 1.08 is absent in his transcription too. 47 = z is the same inference, not a
  second attestation. Codes 103, 110, 115, 116 and 136 stay open, and the agreeing code values are sense readings by the
  same family of models, so they converge without proving each other.
- **Independence.** The timeline is not checkable from the repository: his times (transcription frozen 04:47 UTC, key
  06:39 UTC) are his own file clocks, his first server-stamped record is an email of 10:30:58 UTC, after the commit of
  PR #403 (10:07:02 UTC), and the files and their md5 sums were not supplied. The work itself points to an independent
  reading: 14 transcription errors of his own that this transcription does not have, a different 107, and confine.
- Not reproducible from the issue: his quadgram control, the 280/283 held-out figure, the second reader's 1,391/1,411
  (the letter has 1,412 tokens) and his strict shares 96.20% / 95.54%.

Recorded as a same-day independent corroboration of the key (one key, one entry): a `verification` credit in
`profile.json`, "independent verification" in `outcome.verification`.

## Remaining gaps

- 9 restored words - blocker: open-codes; none is settled by the independent transcription of issue #421 either; after the blind re-reading on the images (11 Nov 2026), 6 are groups whose image shows the digit of transcription v1 (probable cipher-clerk error, nothing more to read on the image), 1 is undecided (quando 1.12), 1 is a group the encipherer left out (di 1.06) and 1 is a value seen only once (47 = z, lunghezza 5.02; a second use of 47 would settle it)
- 5 nomenclator codes (103, 110, 115, 116, 136) and the 21 nomenclator values given by the sense - blocker: open-codes; each code occurs once or a few times, and no nomenclator of Ridolfi is known; a second letter of his in this cipher (AGS Estado, Rome / Genoa 1645-46; ASFi Mediceo del Principato) would test them. The identity of 107 is one of these: Gran Duca (Tuscany) here, "Duca di Modena?" in issue #421
- the PARES images were not seen by the project - blocker: needs-physical-access; PARES answered HTTP 429 to the integrating sessions of 11 and 12 Nov 2026 and no image is in the folder, so the blind sheet, its rule and answer files (not in the repository) and the digit at 1.22 (confino 68 / confine 66) were not checked here

## Escalation

- [x] siblings: the other items of catalogue 748 (D.102-106) are Ronquillo's Spanish letters in another system; no other Ridolfi cipher in OSUNA (PARES, 28 Oct 2026)
- [x] clear-pages: no decipherment or clear copy with D.107; AGS EST LEG 3600,146-147 (Ridolfi / Eraso / Gondi, 1645) are clear copies on another matter, descriptions read, not downloaded
- [x] known-keys: the D.106 table is ruled out analytically (40 = q is incompatible with it); the 1645 Frías key (KV2) does not read D.104 and was not applicable here
- [x] print: no edition found; nothing in this repository for C.3456 or Ridolfi
- [x] key-rebuild: key proposed ciphertext-only on pp. 1-4, frozen, validated once on held-out p. 5
- [x] retry: every restored group run again against the frozen transcription and the key on 11 Nov 2026 (integration check above) and regraded: no class changed
- [x] retry: blind re-reading of the cipher digits on the images by Brice Dudout (11 Nov 2026): 12 of 19 corrections confirmed (12 words restored -> certain), 6 images match transcription v1, 1 undecided; 396/431 = 91.9% by the read bar, still read in part
- [x] retry: token-by-token comparison with Malcolm McBratney's independent transcription and key (issue #421, 12 Nov 2026): same key, 7 of the 12 confirmed digits also in his transcription, none of the 9 restored words or 5 open codes settled

## Files

| file | content |
|---|---|
| `transcription.txt` | transcription v1 of pp. 1-5, groups as written |
| `key.tsv` | the key, CC BY 4.0 |
| `decryption.txt` | mechanical decryption with the key, no correction (p. 5 = output of the single measure) |
| `reading.md` | the reading (Italian, spelling of the letter), marks, count, restored words |
| `translation.md` | English translation |
| `validation.txt` | protocol order, the single measurement and its reservations |
| `frozen/` | the hashed working files (French): PREREG.md, FREEZE.sha256, POST-MESURE.sha256, RESULTAT.md, the proposer's key and readings, our decoder, metric, calibration and measure scripts with their outputs, transcription v1; BLIND-REREADING.md (the blind re-reading of 11 Nov 2026, in English) and v2/ (the readings with the 12 confirmed words unmarked, the counting script and its output). The lexicon `lexique-it-cyphersolver.json` listed in FREEZE.sha256 is `lang/lexicons/it.json.gz` of this repository, decompressed (same SHA-256). |
