# mediceo1483: undated cipher letter, ASF Mediceo avanti il Principato XLVIII 214r (catalogue 2309), in the Siena no. 11 cipher

Status: read in part (Brice Dudout, 10 Nov 2026; partial reading explained: 39 certain, 13 probable, 11 restored words, 45 unresolved stretches, about 35-40 % of the letter read, far under the 95 % rule; key = George Lasry's Siena no. 11 key, partial by our protocol: failed on 2309 itself, 0.6419 against 0.2045 on a held-out letter of the same family).

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry **2309** (Daniel Bourdeau's
catalogue and vetting n08/n18). **The key is George Lasry's** (`targets/siena11`, his report of 17 Oct 2026), not ours: our part is
to have recognised that this letter uses the Siena no. 11 cipher, to have transcribed it, tested the key and read it in part.

## What this folder is, and is not

A **partial reading explained**, at Brice Dudout's request. It is not a solution:
- The key is **Lasry's**, applied unchanged. It covers 96.4 % of the tokens of 2309 (759 of 787).
- A pre-registered test **on 2309 itself failed** (Italian word measure 0.2335 against at most 0.0719 for 200 shuffled keys, margin
  0.16 < 0.30).
- A second pre-registered test **on another letter of the same sign family** (XLVIII 294, c. 306v, against its contemporary clear
  copy c. 276) gives **0.6419 against 0.2045** (margin 0.437): **partial** (the margin passes, 0.85 is not reached).
- The reading of 2309 covers **about 35-40 %** of the letter.
- One derived rule, **D1** ("PLUS ODAG" = c), is used for the reading. It is **untested** (see below) and is offered as an open
  hypothesis, not a result.

## Document

Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP), filza XLVIII, doc. 214 (old c. 222), recto (riproduzione id 60059).
16 lines of cipher, 787 tokens, one clear phrase "Poi un altra volta" in l. 3 and an illegible closing paraph; no date, place,
address or signature; verso blank (show-through only), as Daniel's vetting says. No decipherment on the leaf or filed with it.
Transcribed from the ASF image at 1272 px (the IIIF maximum), by shape, with the sign names of `targets/siena11/transcripts/no11.txt`
and new names for forms not in it (DIV, TRI, WAVE, OO, ST, DPLUS, CIRC1/CIRC2, PIBAR, FB, TB, PB, TALL, 5).
**The ASF images are not reproduced here** (text only).

## System and key (`key/`)

The sign set is that of Siena no. 11 (Donato Acciaiuoli to Lorenzo de' Medici, Rome, 13 June 1478, DECODE R4800): ‖, ‡, #, ###, ω,
π, ⊥, τ, +o / o+, -o-, q‡, and above all the same nulls "g#", "31", "87". Sign-set coverage of the 2309 tokens by the keys compared
before any decoding: Siena no. 11 96.4 %, MAP LXXII 183 65.3 %, Dieci 1414 49.4 %, CXIX 117 39.0 %.

- `key/K_SIENA11.tsv` (SHA-256 e1ef0955...): **George Lasry's key**, as written in sign names by `research/siena2308/verify_lasry.py`
  (NO11_KEY + NO11_MERGE), with no change of value. Signs with two values in his figure take the value with the larger count.
  Header comments in French (the file is kept byte for byte as frozen and hashed).
- `key/K_SIENA11_D1.tsv` (SHA-256 e98d6e96...): the same plus **D1**, "PLUS ODAG" read as one sign = c. D1 was proposed **after**
  the failed test on 2309, from the decoding "hon / honte / hondutti" where "con / conte / condutti" is expected. It is a derived
  rule, declared as such, and is **not tested** (next section).
- Signs absent from Lasry's key (DIV 8, TRI 6, OO 2, DPLUS 2 and nine single forms, 3.6 % of the tokens) produce nothing.

## Tests of the key (`validation.txt`)

1. **On 2309 itself: failed.** One measurement on lines 6-16 (534 tokens): M5 0.2335 against at most 0.0719 for 200 shuffled
   keys, margin 0.16 < 0.30. The calibration declared beforehand shows the measure is harsh (the same script on Siena no. 11 itself
   gives 0.396 against 0.068), but the verdict is reported as it fell. The whole page has now been decoded and seen, so no fresh
   portion of 2309 remains for another test.
2. **Held out on XLVIII 294: partial.** XLVIII 294 (Bernardo Rucellai, February 1485) is in the same "##" sign family. Its clear copy
   of the time, c. 276, is the one Daniel's vetting n18 points to. One measurement on c. 306v l. 1-9 (339 cipher tokens) gives a letter
   agreement of **0.6419** against at most **0.2045** for 200 shuffled keys, a margin of **0.437**: **partial**.
   - The first portion chosen had no clear in c. 276, so amendment A1 moved the test before any transcription; deviations are
     declared in `validation.txt`.
   - The control without D1 gives the same 0.6419: the portion contains no "PLUS ODAG", so **D1 was not exercised**.
   - The signal reads as Italian: "mi pare da metterci uno sbaraglio di fare ogni forza", "considerato le revolutioni dette di
     sopra", "tanti tradimenti", "conestabile".
   - Test files: `validation/` (transcription and decoding of the portion; the clear of c. 276 is not reproduced).

So Lasry's key reads this sign family **in part, by our protocol**. The family is used by more than one Medici correspondent: Acciaiuoli in
Rome in 1478, Rucellai in 1485, and the writer of 2309.

## Reading (`transcription/`, `decryption/`, `reading/`, `translation.md`)

Read word by word on the decoding with K_SIENA11_D1 (10 Nov 2026), Daniel's conventions (plain certain, {probable}, [restored],
‹…› unresolved). **39 certain, 13 probable, 11 words with restored letters, 45 unresolved stretches.** The certain and probable words
cover about 33 % of the 665 decoded letters, about 43 % with the restored ones: **about 35-40 % read**.

What reads: a matter of condottieri and their contracts ("conducti"). Count Antonio and Count Carlo appear, and something Count
Antonio "had ... in Venice". There is a sum of "uindici milia ducati" (15,000 ducats) and the word "diciotto". Further on: a "liberatione",
an "intentione" of "el signore", "non potendo", "utile a questo", "in questo modo".

Addressee probably Lorenzo de' Medici; writer not identified. Date: hypothesis only. If conte Carlo is Carlo Fortebraccio
(d. 1479) and conte Antonio is Antonio da Marsciano, about 1478-79 (Pazzi war); otherwise 1482-85 (War of Ferrara; the filza holds
papers of 1482-83).

## Remaining gaps

- about 60-65 % of the letter (45 unresolved stretches and the 11 restored words) - blocker: open-codes; the text decodes with Lasry's key but long stretches do not read as words; 14 sign forms of 2309 are not in his key
- D1 ("PLUS ODAG" = c) untested - blocker: open-codes; needs a held-out portion of the family with "PLUS ODAG" and a clear (e.g. 294 c. 306r against the lower part of c. 276r, which has been partly seen, so it must be chosen with care)
- the key is partial (0.6419 against 0.85) and the transcription was made at 1272 px - blocker: needs-physical-access; a higher-resolution image of XLVIII 214 from the ASF would settle doubtful forms
- date, writer and addressee - blocker: open-codes; nothing on the leaf; the names read (conte Antonio, conte Carlo) do not settle the date

## Escalation

- [x] siblings: neighbours XLVIII 213 and 215 (Rucellai, July 1483, clear, no decipherment of 2309, Daniel's vetting); the "##" family of XLVIII (101-199, 158, 294) and our earlier rucellai-1482 work checked; 294 used for the held-out test
- [x] clear-pages: verso blank (show-through); no decipherment filed with 214 in the inventory; c. 276 (the clear of 294) used for the test only
- [x] known-keys: Siena no. 11 (Lasry), MAP LXXII 183, CXIX 117 and the Dieci key of 1414 compared by sign set; Siena no. 11 and LXXII 183 tried on lines 1-5, Siena no. 11 kept
- [x] print: web search of 10 Nov 2026 found nothing on MAP XLVIII 214; Marco Vito's work (HistoCrypt 2025) is a Capponi key and letters of 1486-1491, not this leaf; DECODE has no MAP record (Daniel's vetting); Tomokiyo not searched
- [n/a] key-rebuild: deliberately not done in this round; the key is Lasry's and was applied unchanged (plus the declared D1), and any rebuild would need a fresh held-out portion with a clear first
- [n/a] retry: the whole of 2309 has been decoded and seen, so no unseen portion is left for a regraded test; the next step is a test of D1 on 294 c. 306r and an HD image
