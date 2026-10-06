# Banér to Stålhandske, Hof, 29 December 1640 (intercepted copy, Kircher correspondence APUG 568 f. 239) — NOTES

**Status: read in part — 246 of 275 cipher tokens (89.5%) inside words read as sense, measured (`python measure_sense.py`),
5 Oct 2026** (was 246/274 by `decode.py`, which also counted a stray 'n' after code 513). First reading of the letter; key rebuilt here (`key.json`, 70 values) from context cribs. It reads: Banér
means "nach der Oberpfaltz und gegen die [442]" to march; the enemy will gather against him "und etwa auch die in
Schlesien agirende [361] dazu ziehen"; Stålhandske is to "gute acht geben" and, when the enemy moves, follow "mit
einer guten Fürsichtigkeit"; report "durch Espionen"; and tell Banér "wohin er seine Marche zu richten". Open: the
second courier's name (S2), one corrupt stretch in S5 (both confirmed on the manuscript: the copy is corrupt), and all
14 code words (no key). Reading of record: `reading.md`.

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

## The manuscript (22 Sept, second pass)

The Museo Galileo serves the Kircher scans openly at `https://archimede.imss.fi.it/kircher/568/large/239r.jpg` and
`239v.jpg` (1469 x 2304 px; the login page only guards the search database). Every cipher line re-read from them:
Neal's transcription is right except S4 first figure 86 (Neal 66, now "etwa" needs no emendation), S4 "Schl-86-sien"
(Neal 36), S5 "g u 47 e n" (Neal 57; 47 = t, new value) and S7 figure = 92 (n, "richten"). `ct_neal.txt` carries the
corrections. S1 "34 20 78 83 [508]" reads "Jobs[508]" = Jobst + a surname in code (M). With the figures confirmed,
the remaining stretches (S2 name, S5 "eisen o vi rechte", S6 "? o") use values fixed by other words: this copy is
corrupt there. Re-measured: 246 of 274 (89.8%).

Digit-confusion search (`emend.py`: up to two confusable figures per stretch, ranked by de-1640s in context) finds
no reading for the S5 stretch. Hypothesis, not counted: the 7xx codes are letters, giving "au[772] solche [766]eise"
= "auf solche Weise" and "darau[778]" = "darauf".

## The 7xx codes are letters (22 Sept, third pass)

Freeing every value used in the unread stretches and treating the 7xx codes as letter symbols (`solve3_7x.py`, rest
of the key fixed), the annealer returns "auf solche Weise" (772 = f, 766 = W) on its own, and "sie ko[m]en, dass sie
mö[g]en" in S6 (770 = m, 60 = m, 783 = g), which fits the clear "wie seine und des feindes gelegenheit sey ...
berichten". 778 = f (darauf). Treating all three-digit numbers as letters does not read (361-568 stay word codes).
Re-measured: 246 of 274 (89.8%); codes read as letters 5 of 14.

## Push to 95% (5 Oct 2026)

- Image re-transcription: every unread stretch re-read from `img/239r.jpg` (Museo Galileo, 1469x2304) at 2x zoom
  (S2 line 2, S5 lines 6-8, S6). All figures confirm `ct_neal.txt` except S6, where the manuscript has "13. 12. 32":
  Neal dropped the 12. "E-s-p-ionen" is now complete and **12 = p** (key.json). In S2 the name reads "ohrs p acbuet"
  with every value fixed: still no name, so the copy is corrupt there.
- S5 "[766]eise n o u i r e c h t e zu": tried "auf solche Weise movirte/moviret", "nachrichte", "noch richte" in
  context with de-1640s; none fits the confirmed figures and none scores clearly best. "o 2 ein guten" = "mit einer
  guten" needs two figures changed. Not counted.
- Measure check: `decode.py` counts every token outside hand-marked unread spans; the lone "n" after [513] in S2 was
  counted though it makes no word. New `measure_sense.py` splits the decrypt into the reading's words (asserting the
  split equals the decrypt) and counts tokens inside sense words only: **246 of 275 (89.5%)**; de-1640s -1.49/char on
  the sense words. The target stays below 95%: the 29 open tokens are the corrupt name (11+1), the S5 stretch (14+2)
  and the stray e (1), all with confirmed figures and fixed values.

## Remaining gaps

- S2 name after "Johann" (11 tokens, read "ohrspacbuet", plus the lone n after [513]) - blocker: needs-physical-access; the figures are confirmed on the manuscript and every value is fixed by other words (12 = p since 5 Oct), so the only known copy is corrupt; the sent original or a register copy in Banér's papers (Riksarkivet) is needed and is not digitised.
- S5 "eisen o vi rechte" (14 tokens), "o ?" before "ein guten" (2), the stray e in "sobaldt e ich" (1) - blocker: needs-physical-access; figures confirmed on the manuscript, values fixed elsewhere, so the copy is corrupt; only another witness would settle them.
- Code words 361, 442, 464, 508, 513, 568, 767, 773, 775 (766, 770, 772, 778, 783 read as letters) - blocker: no-key-material; no key survives (none of the Banér keys on DECODE is this one), each occurs once, and context gives only the sense.

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
- [x] retry (5 Oct 2026): unread stretches re-transcribed at 2x from the scan; S6 12 restored (12 = p); S5 candidate
  readings scored in context, none fits; sense measure written (`measure_sense.py`).
- [x] retry: manuscript scans fetched (Museo Galileo) and every line re-read; four figures corrected; every unread
  stretch re-run with the full key and with digit-confusion emendation (`emend.py`); S1 read (Jobs[t]), S7 completed.

## DECODE update queued

`decode_updates/queue.json` (baner1640): the letter is not on DECODE; the four key records tried get their own metadata: R4122 = Horn / Johan and Carl Banér cipher, c. 1630-31 (Pomeranian nomenclator); R4123 = Banér-Oxenstierna code from late 1634 (AOSB II:6 nos. 116-118); R4325 = 1640 chancery register containing a copy of R4123 as "Generalis Campi Marschalli Johan Banneris Cyffer"; R4266 = Clavis Num. 2 cum Ekehielm, 1640. Alphabet transcriptions attached for R4122, R4123, R4325. Not sent: needs write access.
