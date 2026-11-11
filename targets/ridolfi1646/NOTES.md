# ridolfi1646: Ludovico Ridolfi to the duque de Arcos, viceroy of Naples, Rome, 8 May 1646 (catalogue 748, AHNOB OSUNA,C.3456,D.107)

Status: read in part (Brice Dudout, 11 Nov 2026; 405 of 431 words certain or probable = 94.0%, 98.8% with 21 restored words; 5 nomenclator codes open; key validated on held-out page 5 by our pre-registered test, COV 0.817 vs 0.487 / 0.600). Open: a blind re-reading on the images of the 21 restored groups, which on this count would bring the letter over the 95% bar.

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

431 words: 378 certain, 27 probable, 21 restored, 5 unresolved. **405/431 = 94.0% read by sense** (Daniel's rule,
restored words not counted): **read in part**; 98.8% with the restored words. Of the restored words, 19 are one-digit
confusions of transcription v1 between shapes of this hand (2/3/7, 1/2, 3/4, 6/8...) or a group omitted, and 2 are on
page 5 (47 = z, 26 for 76); 21 of the 27 probable words are nomenclator values given by the sense.

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

## Remaining gaps

- 21 restored words, mostly one-digit misreadings of transcription v1 - blocker: open-codes; not nomenclator codes but doubtful figures of the transcription, retried on the texts on 11 Nov 2026 (none contradicted, none confirmed); a blind re-reading of those groups on the PARES images would settle each, and stays workable (PARES answered HTTP 429 to the integrating session; no image is in the repository)
- 5 nomenclator codes (103, 110, 115, 116, 136) and the 21 nomenclator values given by the sense - blocker: open-codes; each code occurs once or a few times, and no nomenclator of Ridolfi is known; a second letter of his in this cipher (AGS Estado, Rome / Genoa 1645-46; ASFi Mediceo del Principato) would test them

## Escalation

- [x] siblings: the other items of catalogue 748 (D.102-106) are Ronquillo's Spanish letters in another system; no other Ridolfi cipher in OSUNA (PARES, 28 Oct 2026)
- [x] clear-pages: no decipherment or clear copy with D.107; AGS EST LEG 3600,146-147 (Ridolfi / Eraso / Gondi, 1645) are clear copies on another matter, descriptions read, not downloaded
- [x] known-keys: the D.106 table is ruled out analytically (40 = q is incompatible with it); the 1645 Frías key (KV2) does not read D.104 and was not applicable here
- [x] print: no edition found; nothing in this repository for C.3456 or Ridolfi
- [x] key-rebuild: key proposed ciphertext-only on pp. 1-4, frozen, validated once on held-out p. 5
- [x] retry: every restored group run again against the frozen transcription and the key on 11 Nov 2026 (integration check above) and regraded: no class changed; the image re-reading of the 21 groups is still to do

## Files

| file | content |
|---|---|
| `transcription.txt` | transcription v1 of pp. 1-5, groups as written |
| `key.tsv` | the key, CC BY 4.0 |
| `decryption.txt` | mechanical decryption with the key, no correction (p. 5 = output of the single measure) |
| `reading.md` | the reading (Italian, spelling of the letter), marks, count, restored words |
| `translation.md` | English translation |
| `validation.txt` | protocol order, the single measurement and its reservations |
| `frozen/` | the hashed working files (French): PREREG.md, FREEZE.sha256, POST-MESURE.sha256, RESULTAT.md, the proposer's key and readings, our decoder, metric, calibration and measure scripts with their outputs, transcription v1. The lexicon `lexique-it-cyphersolver.json` listed in FREEZE.sha256 is `lang/lexicons/it.json.gz` of this repository, decompressed (same SHA-256). |
