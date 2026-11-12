# mediceo1483: undated cipher letter, ASF Mediceo avanti il Principato XLVIII 214r (catalogue 2309), in the Siena no. 11 cipher

Status: read in part (Brice Dudout, 10 Nov 2026, updated 12 Nov 2026; partial reading explained: 46 certain, 13 probable, 11 restored words, 46 unresolved stretches, about 35-45 % of the letter read, far under the 95 % rule; key = George Lasry's Siena no. 11 key plus two derived values held on a fresh portion (D1 "PLUS ODAG" = c, TRI = che), partial by our protocol: failed on 2309 itself, 0.6419 and 0.6519 against at most 0.2045 on two held-out portions of a letter of the same family).

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
- The reading of 2309 covers **about 35-45 %** of the letter (12 Nov 2026; 35-40 % on 10 Nov).
- Two derived values are used for the reading: **D1** ("PLUS ODAG" = c) and **TRI** (▽) = "che". On 10 Nov D1 was an untested
  hypothesis; on 12 Nov both **held** on a portion never used before (XLVIII 294 c. 306r against c. 276r: D1 5 of 6, TRI 4 of 5,
  p = 0.005 each; test 3 below). They are values for single signs; the key as a whole stays partial.

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
  rule, declared as such; it was untested on 10 Nov and **held on 12 Nov** (test 3, next section).
- `key/K_SIENA11_D1_TRI.tsv` (SHA-256 0dcd95f6...): K_SIENA11_D1 plus **TRI = che** (12 Nov 2026), the one candidate value that
  held in test 3. Candidates that did not hold or could not be tested are not in it: PLUS alone = o (0 of 3), PIBAR = n (no
  occurrence), the nulls DIV, OO, ST (not testable by the statistic).
- Signs absent from the key (DIV 8, OO 2, DPLUS 2, WAVE and nine single forms, 2.8 % of the tokens) produce nothing.

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
3. **Held out again on XLVIII 294, 12 Nov 2026: D1 and TRI = che hold.** Portion: c. 306r lines 1-16 (411 cipher tokens, never
   transcribed, decoded or measured before), against the upper part of c. 276r (up to where the clear of test 2 begins). Pre-registered
   with three keys (Lasry + D1 for the verdict, Lasry alone as control, Lasry + D1 + candidate values as secondary) and two kinds of
   statistic, one run:
   - letter agreement **0.6519** against at most **0.1854** for 200 shuffled keys (margin 0.467): **partial** again (Lasry alone 0.6390);
   - D1: of the 6 "PLUS ODAG" in the portion, **5 align on "c"** in the clear (the sixth on nothing); 200 random-position controls,
     p = 0.005: **held**. ("ci sia amico o inimico", "pratiche col cardinale");
   - candidates: **TRI = che held** (4 of 5, p = 0.005: "che sono capitoli", "che ognuno"); PLUS alone = o did **not** hold (0 of 3);
     PIBAR = n not testable (no occurrence); the proposed nulls DIV, OO, ST cannot be tested this way.
   - The portion decodes as Italian with gaps (decoding / reading with restored letters): "adunalecteradiguistmaielichemiotdina" =
     "d'una lectera di Gui[do Mann]elli che mi o[r]dina"; "sononelatiudinicileimptesasisaessigiamile" = "sono nel[l]a [p]iu di[ff]icile
     imp[r]esa si [f]a[c]essi gia mile"; "cotestostato" = "cotesto stato".
   - Deviations (declared in `validation.txt`): the upper c. 276r had been looked at for anchors on 10 Nov; the transcriber knew the
     key and the candidates; the candidates come from material already seen. Test files in `validation/` (xlviii294_306r_H3_*).
   After this test no unused portion of XLVIII 294 with a clear is left.

So Lasry's key reads this sign family **in part, by our protocol**. The family is used by more than one Medici correspondent: Acciaiuoli in
Rome in 1478, Rucellai in 1485, and the writer of 2309.

### Integration check (12 Nov 2026)

The figures of tests 2 and 3 agree between `validation.txt`, `validation/xlviii294_306r_H3_measure.txt`, NOTES and the profile; they were not re-run, because the clear copy (c. 276) is deliberately not published and the project holds no copy, so no one else can repeat the tests (a gap below). The gain of D1 on the whole-portion agreement is small (0.6519 with, 0.6390 without). The read share is kept as certain plus probable words only (about 35%); restored words are holes.

## Reading (`transcription/`, `decryption/`, `reading/`, `translation.md`)

Read word by word on the decoding with K_SIENA11_D1 (10 Nov 2026), then again with K_SIENA11_D1_TRI (12 Nov 2026), Daniel's
conventions (plain certain, {probable}, [restored], ‹…› unresolved). 12 Nov: **46 certain, 13 probable, 11 words with restored
letters, 46 unresolved stretches** (10 Nov: 39 / 13 / 11 / 45). The certain and probable words cover about 35 % of the 683 decoded
letters, about 45 % with the restored ones (10 Nov: 33 % and 43 % of 665): **about 35-45 % read**. The gain is small: TRI adds six
"che" ("conte antonio che egli haueua", "che e utile a questo", "positi che si mostra"); D1 now rests on a held test, so the
readings that use it ("conducti", "conte", "con", "ducati") are no longer on an untested rule.

What reads: a matter of condottieri and their contracts ("conducti"). Count Antonio and Count Carlo appear, and something Count
Antonio "had ... in Venice". There is a sum of "uindici milia ducati" (15,000 ducats) and the word "diciotto". Further on: a "liberatione",
an "intentione" of "el signore", "non potendo", "utile a questo", "in questo modo".

Addressee probably Lorenzo de' Medici; writer not identified. Date: hypothesis only. If conte Carlo is Carlo Fortebraccio
(d. 1479) and conte Antonio is Antonio da Marsciano, about 1478-79 (Pazzi war); otherwise 1482-85 (War of Ferrara; the filza holds
papers of 1482-83).

Re-run at integration (10 Nov 2026): decoding the transcriptions with the key files again gives the same 313 letters for the
XLVIII 294 test portion, and 672 letters for XLVIII 214 against the published 665; the differences are only signs written between dots.

## Remaining gaps

- about 55-65 % of the letter (46 unresolved stretches and the 11 restored words) - blocker: open-codes; the text decodes with the key but long stretches do not read as words; 13 sign forms of 2309 are not in the key (TRI now is), and PIBAR = n and the nulls DIV, OO, ST are untested proposals
- PLUS alone: aligned twice on "c" in test 3, an observation made after the measurement (the pre-registered "o" failed) - blocker: open-codes; needs another letter of the "##" family with a clear (XLVIII 294 is used up; XLVIII 158 is too short)
- the clear copy c. 276 used for tests 2 and 3 is not published, so the tests cannot be repeated outside - blocker: needs-physical-access; the ASF filza is the only source
- the key is partial (0.6419 and 0.6519 against 0.85) and the transcription was made at 1272 px - blocker: needs-physical-access; a higher-resolution image of XLVIII 214 from the ASF would settle doubtful forms
- date, writer and addressee - blocker: open-codes; nothing on the leaf; the names read (conte Antonio, conte Carlo) do not settle the date

## Escalation

- [x] siblings: neighbours XLVIII 213 and 215 (Rucellai, July 1483, clear, no decipherment of 2309, Daniel's vetting); the "##" family of XLVIII (101-199, 158, 294) and our earlier rucellai-1482 work checked; 294 used for the held-out test
- [x] clear-pages: verso blank (show-through); no decipherment filed with 214 in the inventory; c. 276 (the clear of 294) used for the tests only (tests 2 and 3; not reproduced)
- [x] known-keys: Siena no. 11 (Lasry), MAP LXXII 183, CXIX 117 and the Dieci key of 1414 compared by sign set; Siena no. 11 and LXXII 183 tried on lines 1-5, Siena no. 11 kept
- [x] print: web search of 10 Nov 2026 found nothing on MAP XLVIII 214; Marco Vito's work (HistoCrypt 2025) is a Capponi key and letters of 1486-1491, not this leaf; DECODE has no MAP record (Daniel's vetting); Tomokiyo not searched
- [n/a] key-rebuild: deliberately not done in this round; the key is Lasry's and was applied unchanged plus two single values held on a fresh portion (D1, TRI = che, 12 Nov); any further value needs another held-out letter of the family with a clear
- [n/a] retry: the whole of 2309 has been decoded and seen, so no unseen portion is left for a regraded test; D1 was tested on 294 c. 306r on 12 Nov (held); the next steps are an HD image of 214 and another letter of the family with a clear
