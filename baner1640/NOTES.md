# Banér to Stålhandske, Hof, 29 December 1640 (intercepted copy, Kircher correspondence APUG 568 f. 239) — NOTES

**Status: read in part — 239 of 274 cipher tokens (87.2%) read as sense, measured (`python decode.py`), 22 Sept
2026.** First reading of the letter; key rebuilt here (`key.json`, 70 values) from context cribs. It reads: Banér
means "nach der Oberpfaltz und gegen die [442]" to march; the enemy will gather against him "und etwa auch die in
Schlesien agirende [361] dazu ziehen"; Stålhandske is to "gute acht geben" and, when the enemy moves, follow "mit
einer guten Fürsichtigkeit"; report "durch Espionen"; and tell Banér "wohin er seine Marche zu richten". Open: the
couriers' names (S1, S2), one corrupt stretch in S5, and all 14 code words. Reading of record: `reading.md`.

Catalogue: "Intercepted letter, Banér to Stålhandske" (new-solves sweep, 22 Sept 2026). Session 2026-09-22.

## Source

- Klaus Schmeh, "An unsolved encrypted letter from the 17th century", Cipherbrain, 2 June 2019
  (https://scienceblogs.de/klausis-krypto-kolumne/2019/06/02/an-unsolved-encrypted-letter-from-the-17th-century/).
  Two page images (617 x 935 and 655 x 901 px, plus a crop of the top of p. 2), sent by Philip Neal via Tony Gaffney,
  and Neal's transcription of the whole letter. Caption: "Copia litterarum interceptarum Generalis Baners Hoff in
  Silesia 29 Decembr. 1640 [568 239r, 568 239v, see also 239r, 239v]".
- "568 239r" is Archivio della Pontificia Università Gregoriana (APUG) 568 f. 239r, the last volume of Athanasius
  Kircher's correspondence (APUG 555-568). The copy of an intercepted Swedish letter was evidently sent to Kircher.
  The Museo Galileo image database of the Kircher correspondence (archimede.imss.fi.it/kircher) needs a registered
  login; not reached here. EMLO has no record of the item.
- Heading: "Copia Intercipirtes Schreibens General Baners an General Major Stallhausen" (= Torsten Stålhandske,
  commanding the Swedish forces in Silesia). Dated "Hoff den 29 Decem. A. 1640", signed "B".
- Comments on the post: Stålhandske identified (Thomas; Krajcovic); Richard SantaColoma tried Selenus 1624 (fail);
  Neal tried and failed, noting that "464 18 16 772" looks like two words round a two-letter word, and that Banér
  was about to march on Regensburg.

## The cipher

German letter in clear with seven enciphered passages (S1-S7 in `ct_neal.txt`, from Neal's transcription): 274
two-digit numbers (74 distinct, 2-98) and 14 three-digit numbers (361, 442, 464, 508, 513, 568, 766, 767, 770, 772,
773, 775, 778, 783). The two-digit numbers behave as a homophonic letter alphabet (no long repeats, flat profile);
the three-digit numbers are nomenclator words or names (508 and 568 are the two routes the duplicate of Banér's
letter of the 16th went by; 442 is what Banér means to march on, "... 442 loszugehen").

## Work log

- Transcription: Neal's, checked against the blog images where legible (the images are too small to verify every
  figure; "9?" in S7 is unreadable).
- Unseeded homophonic annealing (`solve.py`, de-1500s 5-gram): overfits to "en/ne/sie" strings. Not a solution.
- Crib "auf den 442": gives "d u e" elsewhere; dropped.
- Keys on DECODE (Riksarkivet, Chifferklaver låda II, R4103-R4329, 100+ records) scanned via the archivists' cover
  labels. Banér keys found and tested, none fits:
  - R4122 "Ciphera cum Dno Gustavo Horn, Dn. Johanne et Carolo Bannerio" (a = 76, 33, 34; early 1630s).
  - R4123 "J. Banér" code in use from late 1634 (a = 10, 41, 55, 83; words 106-862), same as R4325's "Generalis
    Campi Marschalli Johan Banneris Cyffer".
  - R4325 (1640, Kansliet) third alphabet (a = 5, 29, 55, 102) and fourth (a = 24, 54, 78, 102, 122).
  - R4266 (1640, Ekehielm; a = 20, 76, 44).
  Each tried as is and with value offsets -30..+30: all score as gibberish (about -6 nats/char).
- Cribs from context: S6 follows "mich aber von zeit zu zeit" and starts 40 16 23 28 29 = "durch"; "28 29" occurs
  seven times (ch). S7 has 26 18 23 28 81 ("durch"?). 18 64 26 and 16 64 40 both fit "und"; but "464 18 16 772"
  then gives "uu", so 18 and 16 are not both u.
- New shared model `de-1640s` (lang/: Theatrum Europaeum I 1635, Olearius 1647, Simplicissimus 1669 + the
  1470-1610 DTA prints).

## The break (22 Sept)

- Controls first (`ct_synth.txt`, `pt_synth.txt`): Theatrum Europaeum text of the same segment lengths enciphered
  with the R4123 key. The true plaintext scores -279 (de-1640s 5-gram), unconstrained optima -390 to -430: the LM
  alone is underdetermined at 274 tokens / 74 values, but with about 8 crib values a multiset annealer (every
  letter at most 4-6 homophones, `solve3.py --nb 1 --copies N`) lands on the true key (-275).
- Banded model (four bands, each a permutation, as in R4123/R4325): scanned b0 0-3, widths 24-27 with cribs; no
  layout scores near a solution. The key is not banded.
- Cribs "durch" (S6, after "mich aber von zeit zu zeit") and "und" gave, in the multiset annealer, "nach der ...
  pfaltz und" in S3. **S3 = "nach der Oberpfaltz und gegen die [442]"** fixes 20 values, every one consistent with
  durch/und. From there the key was extended word by word, each value checked in at least two words:
  S4 "etwa auch die in Schlesien agirende [361] dazu ziehen"; S5 "gute acht geben und sobaldt", "ehender",
  "solche", "Fürsichtigkeit nachvolgen"; S7 "wohin er seine(n) Marche zu richte(n) ... entgegen wolten"; S2
  "Johann ... über [568]".
- Slips of the copy or the transcription found by the reading: S4 first figure 66 (p) for 86 (e) ("etwa"); "d e i n"
  for "die in"; "Schlesien" has 36 (s) for an e and 93 (i) for n; "seine(n) (M)arche" and "E(sp)ionen" each lack a
  letter; "sobaldt e ich" has a stray e (for "er sich"?).
- The key (`key.json`): a 18 39 46 74 85; b 42 70 78; c 28 73 82 87; d 15 30 40 63; e 19 27 41 62 75 86;
  f 50 80; g 33 51 79; h 29 43 81; i/j 32 34 44 77 93; k 31; l 21 52 53 68; m 67; n 11 26 49 64 92 98;
  o 20 24 88; p 66; r 23 69; s 13 36 83; t 25 57 71 97; u/v 7 16 48 84 90; w 38 96; z 10 37 55.
  Unassigned: 2, 12, 60, 9? (illegible). Not in alphabetical or banded order.
- Code words: 361 (troops acting in Silesia: "Völker"?), 442 (what Banér marches against: Regensburg, or the
  Bavarians/imperialists), 464, 508 and 568 (routes or places of the two copies), 513, and the 7xx group, which
  falls where letters are missing: "darau[778]" (darauff), "au[772]" (auss), "ko[770]en" (kommen/können),
  "?o[783]en" (sollen/wollen?). The 7xx codes may be syllables or double letters; not settled.

## Remaining gaps

- S2 name after "Johann" (11 tokens, read "ohrs?acbuet") and S1 (4 tokens, "iobs", perhaps "Jobs(t)"), the couriers' names - blocker: illegible; only the 617-655 px blog images exist here, the letters as transcribed do not form a name, and every value but 12 is fixed elsewhere, so the figures are misread.
- S5 "eisen o vi rechte" (14 tokens), "o ?" before "ein guten" (2), the stray e in "sobaldt e ich" (1); S6 "? o" before [783] (2); S7 figure "9?" (1) - blocker: illegible; every value except 2 and 60 is fixed by other words, so the stretches are corrupt in Neal's transcription or in the copy; needs APUG 568 f. 239 at full resolution (Museo Galileo Kircher database, registered login) or the second copy the Cipherbrain caption points to.
- Code words 361, 442, 464, 508, 513, 568, 766, 767, 770, 772, 773, 775, 778, 783 - blocker: open-codes; no key survives (none of the Banér keys on DECODE is this one) and each occurs once; context gives only the sense.

## Escalation

- [x] siblings: DECODE has no record of this letter; the Riksarkivet key box II (R4103-R4329, 100+ records) scanned
  by API and cover labels; Banér keys R4122, R4123, R4325 and R4266 opened and transcribed.
- [x] clear-pages: the letter's clear text used throughout as context (every crib comes from it); no decipherment
  on the pages posted.
- [x] known-keys: R4122 (Horn-Banér), R4123 and R4325 (Banér 1634), R4325's third and fourth alphabets, R4266 tried
  as is and at offsets -30..+30: no fit.
- [x] print: web search for the letter, Cipherbrain comments, EMLO, Oxenstierna's printed letters (only Banér to
  Oxenstierna): no reading.
- [x] key-rebuild: key rebuilt from cribs by multiset annealing and word-by-word extension (above).
- [x] retry: every unread stretch re-run with the full key; the unread stretches use values fixed elsewhere, so no
  key change can read them: they need the image.

## DECODE update queued

`decode_updates/queue.json` (baner1640): the letter is not on DECODE; the four key records tried get their own metadata: R4122 = Horn / Johan and Carl Banér cipher, c. 1630-31 (Pomeranian nomenclator); R4123 = Banér-Oxenstierna code from late 1634 (AOSB II:6 nos. 116-118); R4325 = 1640 chancery register containing a copy of R4123 as "Generalis Campi Marschalli Johan Banneris Cyffer"; R4266 = Clavis Num. 2 cum Ekehielm, 1640. Alphabet transcriptions attached for R4122, R4123, R4325. Not sent: needs write access.
