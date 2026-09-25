# Lope de Soria (Genoa) to Charles V, 1523 — RAH Salazar A-28 (9/28), DECODE R9488-R9498

Status: read in part (written up as docs/soria1523.html)

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
character 4-gram model of Danvila's Castilian documents of 1520-21 (adrian1521/danvila/mhe37.txt). Two
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

## Open

- Key-A codes rip (Venetians?), pur, qed (Swiss?), mul; key-B groups listed in docs/soria1523.html section 09.
- R9496, R9498 not collated sign by sign. R9492 reading final: read_r9492_v2.md.

## Remaining gaps
- key-A code words rip, pur, qed, mul, dus, cop and the opener TZ - blocker: open-codes; 1-3 occurrences each, rip/pur/qed guessed from context only
- key-B groups yac, fob, taf, tu, pel, pug, zib, sib, xif, sab, 7 pes, per (and guessed paf, tin, sud, xa) - blocker: open-codes; not attested in the R9844 crib
- R9493, R9496, R9498 sign-by-sign collation - blocker: not-attempted; duplicates, only spot-checked
- R9491 lines 1-7 and the personal names in R9494 (grade M) - blocker: open-codes; key-B values not confirmed

## Escalation
- [x] siblings: all eleven records and the duplicates used; R9844 (30 Dec 1523) found with the court's decipherment
- [x] clear-pages: R9844 ff. 36r-36v "A claro / B claro" aligned for key B
- [x] known-keys: BRAH 9/15 key book (R9815-R9832) checked page by page, no match; Sanchez R9768 a different cipher
- [x] print: Bergenroth CSP Spain vol. 2 no. 586 (clear parts only)
- [x] key-rebuild: key A by annealing with a Castilian 4-gram model plus hand fixes; key B from R9844
- [ ] retry: not done — look for other decrypted Soria letters of 1523-24 in the Salazar series (9/29-9/31 on DECODE) to attest the key-B residue, then rerun the open groups and collate R9493/R9496/R9498
