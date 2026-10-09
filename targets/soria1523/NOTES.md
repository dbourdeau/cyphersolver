# Lope de Soria (Genoa) to Charles V, 1523 — RAH Salazar A-28 (9/28), DECODE R9488-R9498

Status: read (5 Oct 2026: 96.6% of cipher units read as sense, measured; measure/measure.py) (written up as docs/soria1523.html; the page still shows the earlier 'read in part')

Split entry (Lasry, 25 Sept 2026, 'split the entry into two cases if the achievements are of mixed types'): key-A letters = key recovered from ciphertext-only (primary, outcome.method), key-B letters = key from external plaintext; outcome.parts, one README row each.

Lasry review (25 Sept 2026): key B was rebuilt from an external plaintext (the court's decipherment of R9844), so the target is not 100% ciphertext-only. Method reclassed to 'key recovered based on plaintext from external sources'; key A alone remains a ciphertext-only break.

Catalogue entry 149 ("Lope de Soria to Charles V, 11 ciphertexts", scored by rule). Worked 2026-09-19.

## The records

| DECODE | ff. (9/28) | date (from the letter) | addressee | cipher | reading file |
|---|---|---|---|---|---|
| R9488 | 248-249 | Genoa, June 1523 | Emperor | A | read_r9488.md |
| R9489 | 250-251 | same letter, duplicate | Emperor | A | collated in keyA_june.txt |
| R9490 | 252-253 | same letter, triplicate | Emperor | A | spot-collated |
| R9491 | 440-442 | Genoa, 20 July 1523 | Gattinara ("V. Señoria") | B | read_r9491.md (+ _b) |
| R9492 | 443-448 | Genoa, July 1523 | Emperor | A body, B closing/post data | read_r9492.md |
| R9493 | 449-455 | same letter, duplicate | Emperor | A/B | not collated |
| R9494 | 478-479 | Genoa, 26 July 1523 | Emperor | B | read_r9494.md |
| R9495 | 480-481 | same, duplicate | Emperor | B | used to check R9494 |
| R9496 | 482-483 | same, triplicate | Emperor | B | not collated |
| R9497 | 577-579 | Genoa, 13 Aug 1523 | Emperor | B | read_r9497.md (+ _full) |
| R9498 | 581-584 | same, duplicate | Emperor | B | used to check R9497 |

DECODE's "1524" for R9494 and "1524 (?)" for R9498 are wrong: both letters are dated 1523.
Images: `img/` (git-ignored; fetched 2026-09-19 with the bordeaux cookie). Not public domain: RAH permission needed.

## Prior work

- Bergenroth, CSP Spain vol. 2 no. 586 calendars f. 577 (13 Aug 1523) from the clear parts only; no
  decipherment. The other items are not calendared.
- DECODE: all eleven "Non-decrypted".
- No key for either cipher found: the BRAH 9/15 key book (DECODE R9815-R9832) was checked page by page; none of
  its alphabets matches. A decrypted sibling of another envoy (Alonso Sánchez, R9768) uses a different cipher.

## Key B: from a court decipherment

DECODE R9844 (9/30 ff. 34-37, status Decrypted) is Soria to Gattinara, Genoa 30 Dec 1523, with the court's
"A claro / B claro" decipherment on ff. 36r-36v. Aligning its cipher (ff. 34r-35r) with the clear gave the
first code groups and letters (keyB_r9844.txt, keyB.md): homophonic letters plus a large three-letter code
(sub = que, zog = de, yed = en, xab = Francia, pic tab = su Magestad, ...). Consolidated letter table at the end
of keyB.md.

## Key A: broken ciphertext-only

No crib or key. The R9492 block (f. 444r-445v, ~1060 signs) was transcribed into ASCII glyph names
(keyA_r9492_f444.txt) and attacked with a simulated-annealing substitution solver (solve/hc.py) scored by a
character 4-gram model of Danvila's Castilian documents of 1520-21 (targets/adrian1521/danvila/mhe37.txt). Two
observations set it up: ~25 signs with word division kept (so nearly monoalphabetic), a lone sign 10x (= y),
and c+ꜩ always together (one sign, d). The solver produced "la liga general", "cinco mil infantes",
"exercito" from random starts; the rest was fixed by hand (keyA.md). Homophones confirmed by the three copies of
the June letter: α/ꝓ = o, ʒ/crossed ʒ = e, 9/ꝑ = a. Code words: cap = que, lod = de, luc = duque, lih = Milan,
cip = Venecia, mos = infanteria, lim = mil, leh = en, sig lod saq = Rey de Francia, rap = Italia.

Soria changed ciphers in late July 1523: R9492's body is key A and its closing and post data are key B.

## What the letters say (so far)

- June (R9488): Milan's secretary in Venice with the Infante's mandate to conclude the league; 18,000 ducats;
  Caracciolo off to Venice; infantry mutiny, pay, the Doge's offer of 500 infantry for a month.
- July (R9492): the French king's expected descent on Italy; 5,000 infantry in Provence; fear that the
  [rip] will play the Emperor as Ottaviano Fregoso played the league in 1515; money for pay. Post data (key B):
  Monsieur de Beaurain (Adrien de Croÿ, envoy to Bourbon) has arrived.
- 20 July to Gattinara (R9491): Siena, its "comunidades" and "tiranos", to be governed at the Emperor's hand;
  Beaurain at Turin.
- 26 July (R9494): Beaurain is the bearer; a Piedmontese courier; 28,000 escudos to a doctor at Constance to pay
  Swiss who are to descend on France; 12,000 to the treasurer.
- 13 Aug (R9497): Andrea Doria and the Prince of Salerno discontented with the King of France; Jeronimo Doria's
  approach; Antoniotto Adorno; the republic's capitulation.

30 Sept 2026 (Lasry asked for gap-free quotations): R9497 block 1 collated sign by sign with the duplicate R9498
(image P2, f. 583v). Corrections: 'pro...(prometido)' is 'quitado' (ꝑ° = q, -uitado in both copies: the King had
taken the enterprise of Genoa from Doria and Salerno); 'pari[ente]' is 'uno' (R9498 writes the code pep ꝑ̄ where
R9497 spells ▽yꝑ̄ 'uno', so Jeronimo Doria is 'uno de los principales de esta ciudad', not a kinsman); '[qua]tro'
is 'quatro' (a tall capital L = q in both copies, distinct from the angular L = t); 'sob 7.' is 'quiere' (sob = quier,
also R9491 'seb sob∞ cosa' = qualquiera cosa, M); 'xuf yic' = [hablado] (I, x-block runs F-L). New code values
tun = parte, xap = le, pep = un. The code's initial consonants run in alphabetical stretches (keyB.md). Continuous
text of block 1 in read_r9497_full.md.

## Measure and push to 95% (5 Oct 2026)

The old fraction_read (0.85) was an estimate from these notes, not a count: the readings were line tables of
cipher, clear and glosses, never aligned to tokens. `measure/measure.py` now counts it. Unit = one cipher sign or one
code group. Key-A letters: the mechanical key-A decrypt (`measure/deca.py`) of keyA_june.txt and keyA_r9492_v2.txt is
aligned line by line (difflib) to the hand readings `measure/r_june.txt`, `r_july.txt`. Key-B letters: hand-aligned,
one plaintext word per line with its units (`measure/kb_r9491.txt`, `kb_r9492.txt`, `kb_r9494.txt`, `kb_r9497.txt`).
A unit is read only if its word is unbracketed and passes a sense test (Castilian lexicon from Quijote, Vasto memorias and
Danvila 1520-21 with c/z, u/b, f/h variants and enclitics; proper-name list; or a 6+ letter word scoring >= -1.9/char
on es-golden-age, where gibberish scores -4 to -7). Context-only code values are bracketed and count unread.

| letter | before (estimate) | after (measured) |
|---|---|---|
| June (R9488-90, key A) | ~0.85 overall | 809/813 = 99.5% |
| July body (R9492-93, key A) | | 1127/1150 = 98.0% |
| July post data (R9492-93 f.448, key B) | | 271/274 = 98.9% |
| 20 July to Gattinara (R9491, key B) | | 476/529 = 90.0% |
| 26 July (R9494-96, key B) | | 328/357 = 91.9% |
| 13 Aug (R9497-98, key B) | | 401/410 = 97.8% |
| overall | 0.85 | 3,412/3,533 = 96.6% |

Per-letter LM of the read text -1.3 to -1.8/char, shuffled controls -5.8 to -6.0. 210 key-A units are read through
variants the mechanical table does not hold (P = a/g, 7 = i/b, cT = d/nt); they count because the word is forced.

What moved it:
- R9493 f.455r (the duplicate of R9492) has the closing in key A, struck, with the clerk's interlinear decipherment
  "es arrivado aqui monsr de beaurre y pues por el sera informado V. Md de todo lo mas ocurre", and the whole Post data
  in key A. As second witness to R9492's key-B text: zub = aqui, pef = todo, to = mas, pub = vaya; facilmente,
  podrian, topar, tomarlo. Key-A mul = porque (post data 'porque estando las galeras'; July L24 'la guerra porque desto').
- R9492 Post data read in full (was untouched): Beaurain wanted to sail on 'este vergantin'; Soria advised a good
  carrack instead, French galleys and brigantines being on this coast; the brigantine leaves with Lorenzo Mormino,
  Beaurain in three days by carrack. The clear foot of R9491 f.441r ('se a detenido este vergantin y Lorenzo Mormino')
  fixed xip c7yhr 2Fc4Qyr = Lorenço Mormino and yif = este (not 'dos'); pel = ver- (vergantin).
- R9496 collated for the first time: it opens with a paragraph R9494/R9495 lack: Beurren [partira] [..] con una carraca
  y yra derecho a Barcelona con el [..] Martin Centurion por embaxador de este duque y comunidad de Genova
  (yac = duque, xic = Genova, yud = embaxad-). R9494: pes = yo ('el e yo avemos escrito'), pef = todo, znb = aca,
  dexado (R9495 z-tail = x), Geneva (R9495 9# = g).
- R9491 re-read: pel = ver- ('aver de hazerse qualquiera cosa'), to = mas, sab = puede (also R9497 'no se puede parlar
  nada'), yac = duque, 'importa a su Magestad el buen govierno'. 'libertad' withdrawn: its group sob is 'quier' elsewhere.
- R9497: xag = hable (clear sequel 'abra hablado sobre ello'), xa = hasta, xob = hecha, tin = papa.
- Key A July: Bresa (7 = b), valas, coseletes re-read on R9492/R9493.

## Open

- Key-A codes rip (Venetians?), pur, qed (Swiss?), mul; key-B groups listed in docs/soria1523.html section 09.
- R9496 collated 5 Oct 2026 (opening paragraph new); R9498 collated for block 1 (30 Sept 2026). Measured readings: measure/.

## Remaining gaps
- key-A code words rip (4x), pur (3x), qed (2x), dus (2x), cop - blocker: open-codes; context only (Venetians? V. Magestad? Swiss?), every copy writes the same groups, no key-A crib exists
- July L10-L12 'an fec que la' and 'Q?o Lo79' (~12 signs) - blocker: illegible; R9492 and R9493 disagree sign by sign
- R9491 single key-B groups taf, tu, pud (3x, no one value fits), zib, sib (2x), tac, tad, xif, toya, and ~20 signs in l.3 and l.6-7 - blocker: open-codes; no duplicate of this letter, not in R9844 or any sibling
- R9494-96 te, per, tep, zu, tol, the day count before 'dias', and two phrases of R9496's extra paragraph - blocker: open-codes; three copies collated, they spell the same groups
- R9497 paf [tiempo], sud [respuesta], xuf yic [hablado], z7∞ [hara] - blocker: open-codes; bounded only by the alphabetical blocks, other words fit
- R9498 beyond block 1 not collated - blocker: not-attempted; block 2 and f.579r of R9497 read without it

## Escalation
- [x] siblings: all eleven records and the duplicates used; R9844 (30 Dec 1523) found with the court's decipherment
- [x] clear-pages: R9844 ff. 36r-36v "A claro / B claro" aligned for key B
- [x] known-keys: BRAH 9/15 key book (R9815-R9832) checked page by page, no match; Sanchez R9768 a different cipher
- [x] print: Bergenroth CSP Spain vol. 2 no. 586 (clear parts only)
- [x] key-rebuild: key A by annealing with a Castilian 4-gram model plus hand fixes; key B from R9844
- [x] retry (5 Oct 2026): R9493 (key-A copy of the post data, interlinear decipherment of the closing), R9495, R9496 (new paragraph) and the clear foot of R9491 used as second witnesses; every letter re-measured with measure/measure.py. Not done: other decrypted Soria letters of 1523-24 in Salazar 9/29-9/31 to attest the key-B residue
