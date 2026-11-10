# coahuila1906: Coahuila state code telegrams on the Mexican Kickapoo affair, Múzquiz / Saltillo, 25 Jun - 27 Jul 1906 (NARA M862 roll 342)

Status: read in part (Brice Dudout, 10 Nov 2026; partial reading explained: 80 coded words of the Guajardo/Cárdenas system, 42 certain, 31 probable, 3 restored, 4 unresolved, 73/80 = 91.3% read by sense without the restored words; by code groups 386/411 = 93.9%, 97.2% without T54; T54, 14 groups in another key, not read; key K1 partial by our protocol: held-out coverage 0.796 against at most 0.545 for 1,000 shuffled keys, pre-registered criterion > 0.80 not met).

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry **758** (Daniel's: found in the
slice L word-hit triage of RG 59, frame check of 30 Oct and vetting of 2 Nov 2026, verdict "open"). No target existed for it
on origin/main (10 Nov 2026); the catalogue entry is not touched in this pull request.

## What this folder is, and is not

A **partial reading explained**, published at Brice Dudout's explicit request (10 Nov 2026). The key (K1) is **ours**,
rebuilt from the copies alone with the clear context as the only help. It is **not validated by our own rule**: on the
held-out telegrams it covers 0.796 of the decoded letters with lexicon words, far above every one of 1,000 shuffled keys
(best 0.545), but **under the 0.80 we wrote down before the run** (missed by 0.004), and under the 0.85 we use elsewhere.
We say so plainly: the reading below is offered as a reading by sense, with its counts, not as a validated key.
As far as we found, the code was never read before: the Mexican Embassy told the State Department in November 1907 that it
"does not know the code", and the printed Senate hearings reproduce the numbers without a decipherment.

## Documents

NARA, RG 59, Numerical File 1906-1910, case 3706/35-45 (Kickapoo Indians), microfilm M862 roll 342 (file unit naId
19505183). Frames 0500-0504: Senator Teller's letter of 8 Nov 1907 (Douglas, Arizona) sending the telegrams for deciphering,
and the Department's memoranda. **Frames 0505-0513**: typed copies of nine telegrams made at the Múzquiz federal telegraph
office for the Senate subcommittee on the Mexican Kickapoo land frauds; the clear parts are already in the subcommittee
translator's English, the code numbers left as sent. Frames 0514-0517: Root to Teller, 14 Nov 1907 (the Embassy cannot
decipher it). The copies are numbered as filed (T35 ... T124 here):

| copy | frame | date 1906 | from → to | coded groups |
|---|---|---|---|---|
| T35 | 0505 | 25 Jun | L. A. Guajardo (Jefe Político, Múzquiz) → Governor Miguel Cárdenas (Saltillo) | 95 |
| T36 | 0506 | 25 Jun | Cárdenas → Guajardo | 84 |
| T53 | 0507 | 30 Jun | Guajardo → Cárdenas | 34 |
| T54 | 0508 | 30 Jun | Judge F. Valdés Llano → Cárdenas | 14 (another key) |
| T67 | 0509 | 2 Jul | Guajardo → Cárdenas | 72 |
| T82 | 0510 | 11 Jul | the same text as T67, another copy | (65) |
| T99 | 0511 | 17 Jul | R. C. Conine → Guajardo (at Monterrey), English | 42 |
| T104 | 0512 | 19 Jul | Guajardo → Cárdenas | 59 |
| T124 | 0513 | 27 Jul | Guajardo (Sabinas) → Ignacio E. Rivas | 11 |

411 coded groups without the second copy T82. **No images here**: the frames are on the NARA catalogue (links in
catalogue entry 758); by our own rule this folder carries text and key only.

## System and key (`key.tsv`)

A two-digit **homophonic letter substitution**. The tens come in pairs that give the same letter (1 = 9, 3 = 7, 4 = 8: 30 and
70 are both o, 35 and 75 r, 34 and 74 c, 33 and 73 a, 10 and 90 d, 19 and 99 t), and the unit gives the place in one of three
rows: A (tens 1/9) d y . a . h . x n t; B (tens 3/7) o . g a c r v . f l; C (tens 4/8) e h u i m s . . b p. The Spanish
*le* is left in clear (Bent-le-y, firmar-le). The key was fixed on two telegrams only (T36, from the governor, with the anchor
"para 40 76 43 99 73 75 quejas" = *evitar*, and T104) and frozen before the test; y (11/91), h (15/81) and q (93) were read
later by sense on the held-out telegrams and are marked "after freeze" in `key.tsv`. 86 and 28 (one occurrence each) are
unknown. Licence CC BY 4.0.

## Test of the key (`validation.txt`, `frozen/`)

One pre-registered measurement (protocol written at 07:36 CET on 28 Oct 2026, `frozen/PROTOCOL.md`, in French): lexical
coverage of the decoded letters of the six held-out telegrams (T35, T53, T67, T82, T99, T124; 319 letters), Spanish lexicon
of this repository (English for T99), against 1,000 shuffled keys of the same structure. Criterion fixed in advance:
coverage above the best control **and above 0.80**.

**Result: 0.796; best control 0.545 (p99 0.508); margin 0.251. Criterion NOT MET (0.796 < 0.80).** The key is far above
chance, but it fails the bar we set for ourselves, so we call it **partial**. Seen after the verdict: most misses are words
the translator cut into pieces (la-dron-es: only "dron" is in code), the values y/h/q that were not in the frozen key, and
86/28. No new measurement was made for this pull request.

## Reading (`transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`)

Re-read word by word as sentences on 10 Nov 2026. A word is counted when at least one of its letters is in code; the
translator's English pieces are not counted. **Certain** = every coded letter by the frozen key, word as it stands;
**probable** = needs a value read after the freeze, a letter from the other copy, a missing or doubled letter, or the
translator's pieces to complete it; **restored** = a coded value contradicts the reading; **unresolved** = no reading.

80 coded words (T82 counted once with T67): **42 certain, 31 probable, 3 restored, 4 unresolved**, 73/80 = **91.3%** read by
sense. By code groups (round C01): 386/411 = 93.9%, 386/397 = 97.2% without T54. The governor's telegram T36 and Guajardo's
T104 read in full. Unresolved: a‹86› and "aomang", "any" in T35 (a second accused and a phrase after "Bought suit"),
‹28› in T67. Restored: *advice* in Conine's English T99 (the copy has "advil"), *quien lo* in T124 (two transmission faults).

Content: Governor Cárdenas orders the Jefe Político of Múzquiz to act with prudence and impartiality, the recommendations in
favour of the American government's commissioners being lawful; Guajardo reports that Bentley (the Kickapoo agent) and
another are accused by an Indian of having forced him, at night and with blows, to sign an unknown document; that Bentley was
arrested by the Juez de Letras; that "the ones abuse as much as the others", the commissioner is demanding and Bentley's wife
insolent; and he reports a band of mule thieves, two of them Kickapoo, heading for the Río Bravo.

## Remaining gaps

- T54 (Judge Valdés Llano, 14 groups 0x/5x/6x) - blocker: no-key-material; another key, too short alone; needs other telegrams of the judge (Archivo General del Estado de Coahuila, Saltillo, or the federal telegraph originals)
- T35 a‹86›, "aomang" (33 30 84 73 98 72), "any" (33 18 11) and T67 ‹28› - blocker: open-codes; 86 and 28 occur once; the Spanish original of T35 would settle them
- K1 not validated (0.796 against the 0.80 set in advance) - blocker: too-short; a new test needs fresh telegrams of Guajardo or Cárdenas in the same system

## Escalation

- [x] siblings: frames 0500-0517 of the roll read (Teller's letter, the memoranda, Root's reply); no other coded telegram of the case on the roll
- [x] clear-pages: the clear parts of each copy are the translator's English of the same telegram, used as context only; no clear of the coded parts exists on the roll
- [x] known-keys: no Mexican state or governors' code of 1906 found in this repository or in print (catalogue 758 key_check, Root's reply of 14 Nov 1907)
- [x] print: the Senate hearings "Affairs of the Mexican Kickapoo Indians" (1907-08), vol. 2 pp. 1006-1008 (archive.org OCR), print the numbers with no decipherment; the index "cipher dispatches" refers to another affair
- [x] key-rebuild: key rebuilt by hand on T36 + T104, extended by the pairing rule of the tens and, after the freeze, y/h/q by sense
- [x] retry: every unread group re-examined with the extended key in the word-by-word re-reading of 10 Nov 2026; 86, 28, "aomang", "any" and T54 stay open; retried again at integration (10 Nov 2026, Daniel's session): 86 sits in an empty place of row C and 28 outside the rows, single occurrences, no reading forms

## Integration check (10 Nov 2026, PR #378)

The `frozen/` hashes verify (`sha256sum -c SHA256SUMS`); `frozen/validate.py` re-run from the repository root on
`frozen/TRANSCRIPTION.txt` gives the same key hash (9e58a2ceaedd5225), coverage 0.796 on 319 letters, controls max 0.545,
p99 0.508. `key.tsv` applied mechanically to `transcription.txt` reproduces `decryption.txt`; the group counts re-measure to
411 without T82 (T35 95, T36 84, T53 34, T54 14, T67 72, T99 42, T104 59, T124 11). The NARA frames and Wikimedia were not
reachable from the integrating session, so the page carries no image or portrait.
