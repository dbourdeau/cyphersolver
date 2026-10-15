# Pandolfo Malatesta, archbishop of Patras (Rome), to Gianfrancesco Gonzaga, 22 April 1428 (DECODE R1854 image 1)

Attempted, not solved (22 Sept and 5 Oct 2026). Catalogue entry 152. Split on 14 Oct 2026 from `targets/r1854/`
under the one-key rule (George Lasry, 14 Oct 2026): DECODE R1854 holds four letters to Gianfrancesco Gonzaga in four
ciphers; the other three are deciphered and each has its own page, a different cipher: image 2 (`targets/r1854/`,
Rome 9 Aug 1428), image 3 (`targets/mutiliana1428/`, Forlì 6 Nov 1428), images 4-5 (`targets/cattanei1430/`, Rome
Feb 1430). The solvers (`solve.py`, `solve_syl.py`) are in `targets/r1854/`; images are git-ignored there (main
checkout) and not reproduced (Archivio di Stato di Mantova).

## The letter

Signed by Pandolfo Malatesta, archbishop of Patras, brother of Gianfrancesco's wife Paola. It opens in clear with the
news of the peace between the duke of Milan and the league (the peace of Ferrara, 19 April 1428), "licet nondum
publicatam"; Pandolfo has conceived plans "valde utilia" for his brother-in-law, and the secret parts follow in three
runs: after "decrevi ne" (58 signs), after "quo modo valeat" (70) and after "nolit rem ipsam negligere" (134). Clear
text: `p1_clear.md`. Cipher: `p1v2.txt` (second, sign-by-sign pass, 262 signs, 3 runs; `ct_p1.txt` the cipher only;
`p1_tokens.txt` the first pass). The signs are letter-like (ſſ, η, ʒ, H, cc, ∩, I, ƀʒ, v, ꭏ), with separators strewn
between them.

## What was tried

- Annealing in Latin and Italian (15th/16th-c. and modern models), with and without word spaces, costed nulls,
  vowel and consonant classes, reversed by line, word and globally, digraph signs split or merged
  (`run_p1*.txt`, `run_la.txt`, `run_it-cinquecento.txt`, variants `p1*.txt`): no words.
- Control: the same solver reads a synthetic 266-letter monoalphabetic Latin text, also with 12% token noise
  (`synth.txt`, `synth_noise.txt`): P1 is not a simple substitution in these languages.
- Register keys (R1853) "cum Malatesta dni Pandulfi", "nova cum fratribus de Malatestis", "ultima / prima cum
  Karolo de Malatestis", "Ziffra nova" 1417 seeded into the anneal: -4.2/char, no fit. DECODE R1855 (Modena, Este
  keys incl. Malatesta Novello 1441) and R1852 (Florence Dieci di Balìa 1424-32): sign sets differ.
- Statistics: IC 0.056, 29 sign types, about 44% vowel-like signs; digraphic test (pair IC 0.005, no), periodic
  (column IC flat for periods 2-8), transposition (vowel alternation 0.713 > 200 shuffles: linear substituted text).
- Annealed in Spanish, Catalan, French, German, Portuguese and order-3 Latin/Italian with 150 restarts; a
  syllable-aware anneal (each sign a letter, one of 27 syllables/word signs, or null; `../r1854/solve_syl.py`).
- 5 Oct 2026: images re-fetched, run lines cropped at 3x (L05 matches `p1v2.txt` sign for sign); separators kept as
  five extra cipher signs (`p1_withsep.txt`), annealed in Latin and Italian, 10 restarts each: -2.76 / -2.63 per char,
  no words (`run_withsep_*.txt`).

## Remaining gaps
- 262 signs in 3 runs - blocker: no-key-material; not a monoalphabetic or homophonic substitution in Latin or Italian (solver controls pass on synthetic text with 12% noise); none of the register's Malatesta keys fits; the likely key material is Pandolfo's own ciphered letter of 1 Mar 1438 with its contemporary translation (ASMn AG b. 1081 c. 159-160 and b. 840 c. 95, Falcioni 2015), whose ciphertext is not online and not printed

## Escalation
- [x] siblings: R1853 (register, 14 images) read for keys; all other Mantova records on DECODE opened (R7858-R7888, R7888-R7890); none for 1428
- [x] clear-pages: the clear parts of the letter transcribed (p1_clear.md); no decipherment on the leaf
- [x] known-keys: register keys "cum Malatesta dni Pandulfi", "nova cum fratribus de Malatestis", "ultima / prima cum Karolo de Malatestis", "Ziffra nova" 1417 tried (-4.2/char); R1855 and R1852 opened, sign sets differ; Falcioni's 2004 note on Malatesta chancery ciphers is not online
- [x] print: web search (Pandolfo Malatesta, Gonzaga, cifra, 1428); Treccani DBI; Falcioni 2015 (Pandolfo and the council of Ferrara) prints the 1438 plaintext only
- [x] key-rebuild: annealed under 12 hypotheses (Latin, Italian, modern Italian, costed nulls, vowel classes, separators as spaces, word/line/global reversal, split and merged digraphs)
- [x] retry: second transcription pass (p1v2.txt) re-solved; digraphic, periodic and transposition tests; other languages, order-3 models, syllable-aware anneal; separators as signs (5 Oct 2026): no reading
