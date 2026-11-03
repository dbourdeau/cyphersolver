# 1332: independent check, 3 Nov 2026

Verdict: **confirmed with corrections.** The cipher of the 15 Oct letter is read, the key is right, and the entry stands as read in
part. I could not refute it. One sign in the transcription does not exist, which removes one of the editorial repairs, and the method
note misdescribes how the table was made. Neither changes the status.

The checker is an AI language-model reader viewing the images, like the solver. No human palaeographer has seen this. No solver file
was edited.

## 1. Blind test

I read the signs from the scans under my own shape names before opening any file in this folder except the scan listing. My readings
were saved and hashed first (sha256 below). The scans are the full IIIF size, 1434-1467 px wide.

| Document | Page | Signs read blind | Compared with | Result |
|---|---|---|---|---|
| 15 Oct | 34r, all 16 lines | 350 | solver's eye transcription | 344 identical; 6 merged by me, solver right on zoom |
| 13 Oct | 10r, l. 1-12 | 291 | machine pass (no eye transcription exists) | 90.4% in order |
| 18 Oct | 39v, l. 1-7 | 151 | raw machine decode | 84.6% of letters |
| 22 Oct | 45v, l. 1-7 | 172 | raw machine decode | 84.0% of letters |

On 34r the only difference is that I used one name for the two-barred and one-barred hash, which the solver splits as H2 (o) and Hh (l).
On zoom the six places are 3 two-barred and 3 one-barred, exactly as the solver has them. **Disagreement on 34r: 0 of 350 signs after
zoom, 6 of 350 (1.7%) before it.** The labels were matched to the solver's names after opening `sign_inventory.md`, one to one from the
shape descriptions. This covers only the first 18% of the letter.

The lower figures for the other letters measure the machine pass, not the key. See below: my reading through the same key meets the
gloss at 93-96%.

**Decrypting my own reading.** `key.tsv` on my 34r gives the solver's 34r text letter for letter once the hash signs are split.

**A table with nothing of the solver's in it.** I typed the glosses of 10r, 39v and 45v myself and fitted a table by EM from random
starts to my readings of those three pages only, with no value supplied. It gave the solver's value for every sign with enough support
(3 i, oo s, V t, A and < e, ou and uo n, U and ~ u, u and 1 a, Th and * o, Ls and Hs r, P c, D and I: m, B and wv p, +A t, g q, d and =O d,
C b, H3 and Hh l). Applied to my blind 34r, which it never saw:

    psidemo?stratilnemuelostentationemsaltemalicuiusexpeditionisuersusfacerepotuiesuelad?ucpoesqulfaciliushostesabobsidilneseuo?ugnation
    eagrieabstra?anturetstudiumquodillustrisduxmauritiuselectorsaxonieeainreexhacpartecumsubiectosibi?pimpendittuaarteetdiligentiaist?ic
    iuuareualuiesautualeresetcredimusquodturceilliad?etpp

303 of the solver's 334 letters in order. All 31 misses have a plain cause: signs that do not occur on the training pages (9, the
two-barred K, the codes), ii still taken as null, +Th as p, and H2 and Hh merged. None contradicts the reading. This is the check the
notes list as missing, for 34r.

## 2. Rerun of the decryption

A short script of my own on `transcription_15oct_ff34r-35v.txt` and `key.tsv` reproduces `decryption_15oct_ff34r-35v.txt` exactly: 82
lines, 1904 signs, 130 nulls, 1835 letters and code places, no sign missing from the key. `scripts/check_reading.py` also matches.

My blind pages through `key.tsv` against the glosses I typed, as letters found in order:

| Page | Letters decrypted | Found in my gloss | 200 shuffled tables, best |
|---|---|---|---|
| 10r | 278 | 93.2% | 45.2% |
| 39v | 143 | 95.1% | 43.1% |
| 45v | 169 | 95.9% | 42.9% |

The cipher also says things the gloss drops or changes, so the gloss was not simply copied back: 45v has Q6 after `regno illo nostro`
and the gloss has no Transiluania, and 39v gives `superemus` where the gloss has `speramus`.

## 3. Freeze and held-out passage

- `scripts/step_heldout_10r.py` reruns exactly: score 754, 442 of 518 (85.3%), shuffled mean 13.83, best 23, and 36.7%, 41.5%.
- `em.py` takes only lines 9r and 9v, and only the gloss blocks for 9r and 9v. f. 10r was not used.
- File times agree with the order claimed: `key_frozen.tsv` 00:12:22, first 34r strip 00:12:23, `decode.py` 00:21, transcription 00:27.
  Nothing is committed, so this is evidence, not proof. `marginal_gloss_9r_9v.txt` was last written 00:30:58, after the freeze. It still
  holds errors the signs correct (`inueniendae pecuniae`), so it was not fitted to the key, and my own gloss gives a higher figure anyway.
- **The method note is wrong on one point.** NOTES says the table came "with no value supplied by us" from random tables. `scripts/em.py`
  fixes 14 sign values in every restart (the `known` dict). The 197 restarts cannot be reproduced from it. The result is not affected: I
  reran it with `known` removed and it locked at restart 6, score 1254, and all 36 frozen letter values came out the same. Seven frozen
  nulls (Ex, Eo, n:, m:, d:, e, ii) were also set by hand; EM gave them letters.
- `step_machine_check.py` now gives best 39.0%, mean 32.2%, not 39.5% and 32.5%, because `key.tsv` changed afterwards. 1664 of 1835 (90.7%)
  stands. It compares with the solver's own final text, so as the notes say it shows the shapes only.

## 4. Language, events, marking

The Latin is sound chancery prose from start to finish: long periods, correct subjunctives, `quominus`, `utpote a uiro prudente`,
`in seruitiis nostris`. The events fit: Temesvár and Lippa lost that summer, Eger under siege, Maurice's army on the Győr side, Castaldo
short of pay. The letter matches its sisters: the 39v gloss asks for `motum aliquem versus Lippam` and says Maurice is drawing the Turks
off Agria. That also means the theme could have been expected, but the signs give the text with no help from it. The English follows
the Latin; I found no error of sense.

Context-only values are marked: Q7 with a question mark, sign 24 in the notes. I found no silent repair in the decryption. Code values
checked on the images:

- Q6: f. 9r l. 3, `...nostri [Q6] ... succedant`, gloss `Transiluanie succedant`. Good.
- Q3 and H9: f. 46r l. 11, `quidem [Q3] cum [H9] ad agriam`, then `moratur`, gloss at the foot of 45v. Good.
- Q8: 39v twice against `Lippen.`. Good.

### Corrections

1. **35r.11: the last sign does not exist.** The transcription ends `... oo V Ls <`. The line ends at `Ls`, with bare paper after it (crop
   at 4x). The `<` came from the machine pass, which split the shape as `oo B < Ls`. So the text is `cura nostr|a si`, and the repair
   `nostr{a/e}{-a}` and the note `nostre a` should both go. Signs 1903, letters 1834.
2. **35r.24, line end.** After Z# there is a faint mark right against the edge, in the stain: a slanting stroke over a short bar, with a
   dot, the shape of `z` (i). If so, `{+i}ndustria` is on the page and is no repair. I rate this probable, not certain. Mark it as a
   doubtful sign.
3. **35r.27, line end.** I can see V and no separate A. The `e` of `milites` is sense, not sign. Better shown as doubtful in the count; the
   solver's own note already says so, but the word is counted as having no restored letter.
4. **34v.06, the numeral on the rho.** It is open at the top, nearer S or 5 than the closed 8 of 34r.05, 34r.17 and 39v. Q5 would be a
   different place. It is probably a loosely written 8, and the sense fits, but it is not listed as doubtful and should be.

The other repairs hold on the image: `habemes` (a clear `<`), `singslari` (a clear oo), `rationibu`, `diutiu`. Sign 24 is a plain 2 and 4 before
K. A non-blind look at all 27 line ends of 35r and all 11 lines of 35v found nothing else, but one phantom sign means the pass was not
perfect. Pass B leaned on the machine at this spot, whatever "every line read by eye" says.

## 5. Shuffled tables

Trigram model trained only on my typed glosses and the clear parts of the letter (2186 letters, nothing from the cipher reading):

| Table on the full transcription | Score per trigram |
|---|---|
| `key.tsv` | -2.567 |
| 500 shuffled, all values: mean, best | -3.676, -3.512 (21.6 sd above the mean) |
| 500 shuffled, letters only: mean, best | -3.669, -3.513 (25.5 sd above the mean) |

Single-sign changes raise this score by 0.007 at most. That is noise from a small training text, not a better key.

## 6. Words, by the 95% rule

Rerun of the count: 317 words, 316 read as sense (99.7%), 310 with no change (97.8%). After correction 1: **316 of 317 (99.7%) as sense,
311 of 317 (98.1%) with no restored or changed letter.** On the strictest count, with Q8 at 34v.06 also open, 315 of 317 (99.4%) and
310 of 317 (97.8%) if `milites` moves the other way. All are over 95%.

| Document | Honest status |
|---|---|
| 15 Oct 1552, ff. 34r-36r | **read**, one code word open (Q7) |
| 13 Oct 1552, ff. 9r-15v | not read; contemporary gloss; transcription job; the table fits |
| 18 Oct 1552, ff. 37r-42v | not read; contemporary gloss; transcription job; the table fits |
| 22 Oct 1552, ff. 43r-48v | not read; contemporary gloss; transcription job; the table fits |
| Entry 1332 | **read in part** |

The word "Solved" in the claim should apply to the 15 Oct cipher only.

Q7 stays open and the note in `key.tsv`, "not found in any gloss", claims too much. No real search has been made. The solver's rho template
(`work/hits_rho.png`) found only the sign it was cut from and one other, and missed the known signs on 34r, 9r, 45v and 46r. Mine, with four
templates, did no better. The glosses need reading by eye for it. "Not found in the glosses viewed" is what can be said.

I did not check that every cipher block has gloss beyond the pages viewed (9r, 10r, 39v, 45v, 46r). The last line of 46r was not traced.
ff. 34r, 34v, 35r and 35v have none, as claimed.

## 7. Printed?

Two searches found no edition and no decipherment of this letter. That is weak evidence, as Veress, *Documente* I, was again not opened and
the Vienna minute was not sought.

Carpentieri, *Verbum* 13/2 (2012), p. 471, full text searched by keyword, not read through, confirms the layout: the cipher of ff. 9r-15v, 37r-42v and 43r-48v was
deciphered in the margins, and she does not list the other. She also says the existence of editions of these documents remains to be
established, so the point is open in print.

Collision: `research/dudout_2026-10-29/README.md` in the public repo says Dudout's reading of this letter is withdrawn (0.731 of words) and held,
and his corrections file still says it is read. On GitHub today (main at 3c777efd5) there is no `targets/castaldo1552`, a code search finds
the name only in those two files, and neither the first 100 branches nor the latest 100 pull requests name it. **He must be asked before any PR.** Our text may match a reading he already has.

## Must fix before a PR

1. Remove the phantom `<` at 35r.11 and the `nostra` repair; update the counts (1903 signs, 1834 letters, 311 words).
2. Mark as doubtful: the faint mark at 35r.24, the A at 35r.27, the numeral at 34v.06.
3. Correct NOTES on the table: 14 seed values in the script on disk, seven nulls set by hand, and an unseeded rerun gives the same letters.
4. Change `key.tsv` on Q7 to "not found in the glosses viewed".
5. Update the shuffled figures of test B, or rerun with the final key.
6. Ask Dudout. Open Veress.

## Blind reading of f. 34r (own labels, before any solver file was opened)

    PT Ex OO DQ Z MM Sicut CE DL NN LT
    BB DB XS OU^ OO VV LS II NN AH 3 HH OU CA DB WW LT HH TH TO VV CA OU
    VV UP AH 3 TH OU LT DB TO FF HHH VV LT DB II HHH Z OP WW H2 SI OO
    CA XX BR LT EQ 3 VV H2 TH OU H2 OO SI CA LS OO WW OO DQ NN Q8 MM
    TT II OP LT LS CA BR TH VV WW 3 ii LT OO WW CA HH II EQ AT2 SI OP BR TH NN
    ii LT OO G2 WW HH TT UP OP H2 HHH 3 SI OO AT1 TH OO VV LT OO UP DH CE
    XS DH OO H2 DL Z HH OU CA OO CA WW XS G9 WW OD OU II VV 3 TH OU CA
    II OD LS H2 CA UP DH OO VV LS II AT2 FF OU VV WW LS CA VV OO VV SI NN
    DL Z SI DB G2 WW TH DL 3 7 WW OO VV LS H2 OO EQ SI XX DB II WW
    LX H2 VV Z SI OO CA HHH LT OP VV TH LS OO II XX TH OU 3 LT MM
    LT II 3 OU LX CA LT XX AT1 II OP BR FF LS VV LT OP WW DB OO SI DH NN
    Z CA OP VV TH TO 3 DH H2 Ex DQ HS MM PT H2 DB BR CA OU DL 3 VV MM
    VV WW II UP LS VV CA LT VV EQ Z HHH H2 OD CA OU VV 3 II 3 OO VV AT2 Z OP
    H2 WW SI II LS CA WW II HHH WW 3 ii LT OO II WW VV WW II HH LT NN
    LS CA OO LT VV OP LX CA DL Z DB SI OO G2 WW TH DL VV WW LS OP LT CE
    3 7 H2 II DL Ex BB Q7 DQ LT VV NN Q8 MM CE Sicut PT DQ PT

sha256 of the four blind files, computed before the first solver file was opened:

    e580b7992b0fd180fdee10f19beacc13e5ae1ac231c7922e2ecf404f75c32e36  34r
    2819e966a457882ba1c7afd903ac7d57442610fe1b45be4c6bfc53457e1c7781  10r
    a45b6758344f2cf3436737c3054f839da8ceeac404d06d57eea44403602eb2c0  39v
    58527d4669c046902acae084418850538f1dbbe91d70f208ce1af4755868c7ba  45v
