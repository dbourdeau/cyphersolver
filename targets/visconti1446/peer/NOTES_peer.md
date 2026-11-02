# Filippo Maria Visconti to Francesco Sforza, cipher slips of Nov 1446 - Jan 1447 (BnF ital. 1583 and 1584)

Status: read in part. Catalogue leads 1307 (ital. 1583, 1446) and 1312 (ital. 1584, 1447). Worked 28-29 Oct 2026.

**Verdict.** The duke's own key is DECODE R1857 image P17 ("Filippo Maria Duca di Milano", an 18th-century copy in
ASMi Potenze Sovrane cart. 1592), not connected with these slips before: external key matched. Calibrated on two 1447
slips that have contemporary translations (ital. 1584 ff. 5/6 and 8/9: 96.7% and 97.8% of cipher tokens give sense),
it reads the 1446 slips of ital. 1583 as follows (measured by `measure.py`, % of non-null cipher tokens):

| slip | DECODE | date | tokens | sense | % | clear text to check against |
| --- | --- | --- | ---: | ---: | ---: | --- |
| f. 110r | R7902 P1 | Milan, 1 Nov 1446 | 1937 | 1851 | 96.5 | 19th-c. copy, ital. 1597 f. 123 |
| f. 110v | R7902 P2 | (same letter) | 775 | 536 | 69.6 | same copy |
| f. 130 | R7904 | Milan, 2x Nov 1446 | 1037 | 574 | 56.6 | translation f. 131, not digitised |
| f. 136 | R7907 | Milan, 29 Nov 1446 | 562 | 514 | 95.0 | 19th-c. copy, ital. 1597 f. 154 |
| f. 154 | R7914 | Milan, 12 Dec 1446 | 2327 | 763 | 33.0 | none found |
| f. 158 | R7915 | Cusago, 31 Dec 1446 | 606 | 186 | 31.5 | none found |
| all six | | | 7244 (98 nulls) | 4424 | 61.9 | |

So the letter of 29 November and the recto of 1 November read in full against their copies (the verso of 1 November 69.6%), and three slips (25 Nov, 12 Dec, 31 Dec) stay
largely unread on the binarized DECODE scans: ital. 1583 is not on Gallica, and the barred letter forms that the key
separates cannot be told apart on these images. Read in part.

## The documents

- **BnF italien 1583** (Archivio Sforzesco I, 1433-1446; not digitised: microfilm MF 16151 only). The duke's cipher
  slips on parchment, listed by Mazzatinti (Archivio storico lombardo X, 1883; `../it1583/asl1883.txt`) as "In cifre:
  membr.": f. 110 (1 Nov), f. 130 (25 Nov; f. 131 "Traduzione della lettera precedente"), f. 136 (29 Nov), f. 145
  (1 Dec, not on DECODE), f. 154 (12 Dec), f. 158 (Cusago, 31 Dec), f. 162 (Cusago, 3 Jan 1447, not on DECODE).
  DECODE R7902, R7904, R7907, R7914, R7915 (images uploaded 2024, "Non-decrypted", no sender or receiver). R7903
  (f. 112, 7 Nov) is a clear letter, not a cipher. R7902 P2 is f. 110v with 17 lines of cipher (upper part); R7904
  image 2 and the lower half of R7902 P2 are show-through. R7914 P2 is the recto of f. 154, P1 the verso.
- **BnF italien 1584** (Archivio Sforzesco II, 1447; Gallica btv1b100373864, read through openapi.bnf.fr). 15 duke
  slips = 11 letters (`slips.tsv`); 8 have the contemporary clear text on the next leaf (ff. 6, 9, 16, 25, 38, 84,
  95, 103; Mazzatinti notes only 6 and 9) and all 11 have a 19th-c. fair copy beside them (ff. 7, 10, 17, 26, 29,
  35, 63, 73, 82, 92/93, 101). These letters were deciphered at the time or later: catalogue lead 1312 is an existing
  decipherment. Two of them (f. 5 = 10 Jan 1447, Abbiategrasso; f. 8 = 11 Jan) were transcribed sign by sign here and
  aligned with their contemporary translations to calibrate the key. The other nine were not transcribed.
- **BnF italien 1597** (Gallica btv1b10037396j, "Copie moderne di documenti dal 1439 al 1590"): 19th-c. fair copies
  numbered with the ital. 1583 document numbers in brackets. (41.) c126-127 = f. 110; (55.) c157 = f. 136; (59.) c160 =
  f. 145 (1 Dec, "Heri zonse qui Gaspare de li Ubaldini ..."); no copy of f. 130, f. 154 or f. 158 (c175-179 "Cusaghi
  31 Xbre" is a different clear letter dated 1 Jan 1447; c138-143 the Latin donation of 10 Nov 1446). The copy of
  f. 110 is a decipherment of the slip, not an independent text: it writes *gi* exactly where the cipher has the vuy
  sign and leaves "V+" blank at both places of the unidentified name sign. ital. 1598 (btv1b10037380f) starts with
  3 Jan 1447.

## The key

`key.md` (R1857 P17 as read) and `working_key.md` (the signs as used on the slips, with every correction and its
evidence). System: 2-5 homophones per letter; a sign for every vowel+consonant syllable (ab ... uz; the a-row on c-forms,
e on b-forms, i on ð-forms, o on p-forms, u on ∞-forms); the Latin-letter groups "per" = or, "par" = os, "fa" = it;
word signs (que, qua, qui, per, che, con, perché, non, quanto, come, quando, però); name signs on a hook (Duca di
Milano, gente d'arme, Roma, Duca di Ferrara, Conte d'Urbino, Papa, Veneziani, Re d'Aragona, S. Malatesta); 12 nulls,
and a filler tail after the signature. No word division. Corrections the clear texts proved: a c-like sign with a
top stroke = i (missing from the copy); S standing alone = e/et; II + 3/ı = vuy; ∿ð# = Marchese di Mantova; the word
signs written on a 9 base; ft-ligature = ap; ꝛo = ir; ♀ inside words = a; 9 with stroke = am/ad.

R1857 P11 (Marcolino Barbavara and Simone Arrigoni - Pietro da Pusterla; Tomokiyo's key for ital. 1584 f. 69) is a
sibling alphabet of the same family and does not read f. 5. R1857 P19 ("Cum Duci Mediolani") is a different system.

## What the letters say

- **f. 5, 10 Jan 1447 (Abbiategrasso)**: thanks for two letters and Pedro da Pusterla's report; the Marchese of
  Mantua must not go over to the Venetians; Rolando Pallavicino and Cremona. (Contemporary translation f. 6.)
- **f. 110, 1 Nov 1446**: a long letter of reassurance and reproach: Sforza has been told many times of the duke's
  good will; had he been stronger he would have been helped; neighbours in the wrong, obstinate people; "we have
  decided never [to act] against you".
- **f. 130, 2x Nov 1446**: the duke has sent off a brief and received Sforza's letters of the 14th (?) brought by one
  Picino; urges him to act and to come with all speed ("ve pregamo che vui vogliati prestisimo venire").
- **f. 136, 29 Nov 1446**: on the 15th of last month he received Sforza's breve and sent Zohanne del Maino the next
  day with full mandate; nothing has followed, and all Sforza's men-at-arms of Cremona have gone over to the enemy.
- **f. 154, 12 Dec 1446**: Pedro da Pusterla's mission; "secretamente" three times; largely unread.
- **f. 158, Cusago, 31 Dec 1446**: men-at-arms, Rome, "soccorso"; largely unread.

Full texts: `texts/f<NNN>_text.md` (reading), `texts/f<NNN>_en.md` (English), transcriptions
`texts/f<NNN>_transcription.tsv`, line-by-line readings `texts/f<NNN>_reading.md`, copies `texts/*_copy1597.md`.

## Prior work

- Contemporary translations of the 1447 slips in ital. 1584 (ff. 6, 9 ...), and 19th-c. fair copies of the 1446
  letters of 1 Nov, 29 Nov and 1 Dec in ital. 1597: decipherments existed, made from a key, before this project. They
  were found during the work (28-29 Oct 2026), after the key had been matched on f. 5 / f. 6; f. 110 and f. 136 were
  then aligned with them. None is printed.
- Satoshi Tomokiyo, Cryptiana "Undeciphered ciphers" ("Milanese Ciphers in BnF it.1584"): the key of ital. 1584 f. 69
  is DECODE R1857 (the Barbavara/Pusterla page); he had not studied the other slips. That pointed to the record.
- Mazzatinti (1883, 1887) inventories the volumes, headings only. Osio, Documenti diplomatici tratti dagli archivj
  milanesi III (1872) prints agents' reports and the Pusterla procuration of these months but none of these letters.
- DECODE: all five records "Non-decrypted", no metadata.

## Remaining gaps
- f. 154 (R7914, 12 Dec 1446): 1548 of 2311 non-null tokens unread - blocker: illegible; the binarized DECODE scans do not separate the h-form and barred-b families on which most open runs fall; ital. 1583 is not on Gallica, no clear copy in ital. 1597/1598; a colour scan or the microfilm (BnF MF 16151) would decide them
- f. 158 (R7915, Cusago 31 Dec 1446): 405 of 591 non-null tokens unread - blocker: illegible; same scans, darker image, no copy (ital. 1597 c175-179 is another letter)
- f. 130 (R7904, 2x Nov 1446): 440 of 1014 non-null tokens unread or without sense - blocker: needs-physical-access; the contemporary translation f. 131 is in ital. 1583, which is not digitised, and the long h-form/barred-b runs of lines 6, 9, 12, 13 are not separable on the scan
- f. 110v (R7902 P2, 17 lines): 234 of 770 non-null tokens unread - blocker: illegible; cramped lines on a scan whose lower half is show-through; the copy gives the sense but the signs are not counted as read where the image does not show them
- name signs ∿ð+ (f. 110, 2x; the 19th-c. copyist left it blank too) and ·A· (f. 130, 2x) - blocker: no-key-material; under blank headings in P17, no crib
- the day after "vigesimo" in f. 130's date (4 signs) - blocker: needs-physical-access; f. 131 would give it

## Escalation
- [x] siblings: ital. 1584 viewed canvases 1-140 (`slips.tsv`); ital. 1597 canvases 116-182 and ital. 1598 canvases 1-40 viewed for copies; DECODE R7898-R7915 (the 1446 records) fetched; copies found for ff. 110, 136, 145 only
- [x] clear-pages: R7902 P2 and R7914 P1 are cipher versos, R7904 image 2 is show-through; the clear leaves of ital. 1584 are the translations (ff. 6, 9 used)
- [x] known-keys: R1857 P17 fits; P11 (Barbavara/Pusterla) and P19 (Cum Duci Mediolani) do not; the 208 Sforza keys of ASMi cart. 1591/1597/1598 were scanned in Sept 2026 (`../it1583/NOTES.md`) and none is the duke's
- [x] print: Mazzatinti 1883/1887, Osio III (1872) grepped for Oct 1446 - Jan 1447, Tomokiyo's Cryptiana; none prints these letters
- [x] key-rebuild: `lattice.py` (beam search over the ambiguous glyph classes with it-cinquecento) failed its control on f. 136 (55.6% of ambiguous signs right), so it was not applied; the key itself was extended by alignment with the clear texts (`working_key.md`)
- [x] retry: f. 130 re-read with all corrections (48.1% -> 56.6%), f. 154 (31% -> 33%); f. 158 retried in pass 1 only after the f. 136 corrections, without gain on the dark scan

## Files

- `key.md`, `working_key.md`: the key and the signs as used.
- `texts/`: transcriptions (`*_transcription.tsv`, one row per sign: folio, line, pos, key value, note), line-by-line
  readings (`*_reading.md`), continuous texts (`*_text.md`), English (`*_en.md`), the clear texts used (`f006_clear.md`,
  `f009_clear.md`, `*_copy1597.md`), pass-1 versions (`*_pass1.*`).
- `measure.py`: the counts above. `slips.tsv`: the survey of both volumes. `lattice.py`: the failed LM decoder.
- `fetch_gallica.py` (openapi.bnf.fr IIIF; gallica.bnf.fr blocks scripts), `recinfo.py` (DECODE record pages in
  `decode/`). Images are git-ignored: DECODE images with the project cookie, Gallica through openapi.bnf.fr.
- `WORKLOG.md`: every step, failures included.
