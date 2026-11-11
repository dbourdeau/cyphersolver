# ridolfi1646: Ludovico Ridolfi to the duque de Arcos, viceroy of Naples, Rome, 8 May 1646 (catalogue 748, AHNOB OSUNA,C.3456,D.107)

Status: read in part (Brice Dudout, 11 Nov 2026; 405 of 431 words certain or probable = 94.0%, 98.8% with 21 restored words; 5 nomenclator codes open; key validated on held-out page 5 by our pre-registered test, COV 0.817 vs 0.487 / 0.600). Next step: a blind re-reading on the images of the 21 restored groups, which would bring the letter over the 95% bar.

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

## Remaining gaps

- 21 restored words, mostly one-digit misreadings of transcription v1 - blocker: not-attempted; a blind re-reading of those groups on the PARES images would turn them into certain or probable readings (or not)
- 5 nomenclator codes (103, 110, 115, 116, 136) and the 21 nomenclator values given by the sense - blocker: open-codes; each code occurs once or a few times, and no nomenclator of Ridolfi is known; a second letter of his in this cipher (AGS Estado, Rome / Genoa 1645-46; ASFi Mediceo del Principato) would test them

## Escalation

- [x] siblings: the other items of catalogue 748 (D.102-106) are Ronquillo's Spanish letters in another system; no other Ridolfi cipher in OSUNA (PARES, 28 Oct 2026)
- [x] clear-pages: no decipherment or clear copy with D.107; AGS EST LEG 3600,146-147 (Ridolfi / Eraso / Gondi, 1645) are clear copies on another matter, descriptions read, not downloaded
- [x] known-keys: the D.106 table is ruled out analytically (40 = q is incompatible with it); the 1645 Frías key (KV2) does not read D.104 and was not applicable here
- [x] print: no edition found; nothing in this repository for C.3456 or Ridolfi
- [x] key-rebuild: key proposed ciphertext-only on pp. 1-4, frozen, validated once on held-out p. 5
- [ ] retry: blind re-reading of the 21 restored groups on the images (next step)

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
