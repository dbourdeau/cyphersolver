# Pandolfo Malatesta, archbishop of Patras (Rome), to Gianfrancesco Gonzaga, 22 April 1428 (DECODE R1854 image 1)

Status: read with an outside key (Prizmic, 5 Nov 2026), checked here; written up on docs/malatesta1428.html.

Attempted by us 22 Sept-14 Oct 2026 and not solved; read on 5 Nov 2026 with a key by Mark Vladimir Prizmic. Catalogue entry 152 (removed on reading). Split on 14 Oct 2026 from `targets/r1854/`
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

## Outside reading (5 Nov 2026)

Mark Vladimir Prizmic (independent researcher, Anaheim; ORCID 0009-0005-7729-3029), working with Claude from Satoshi
Tomokiyo's 309-sign transcription of this image and his CTTS trial, reads all three runs. Preprint:
https://doi.org/10.5281/zenodo.23969170. He emailed Tomokiyo and copied us the same day; Tomokiyo accepted his five
corrections to the transcription and declined co-authorship of the planned fuller article. Plaintext: Latin, a
homophonic substitution with two nulls (Tomokiyo's v and g) and north-Italian x for s.

- Run 1 (after "decrevi ne"): de suis gentibus armigeris cassandis vel quid aliud peragendum [one sign unread] delliberet
- Run 2 (after "quo modo valeat"): absque discrimine et multo dispendio provincie Moree, patrie siquidem fertilis et amene, rex effici
- Run 3: De eo autem regno magnificum comitem Riciardum bene informatum puto, quoniam ad illud cum serenissima sorore
  nostra domina vaxilissa tetendit, et iterum deinde etiam sui ocaxione redivit.

His corrections: sign 30 in "cassandis" and "peragendum" is the double-c sign (d); the second 24 in "peragendum" and
the 24 in "discrimine" are plain H (r), the scribe omitting the c; the x in "Moree" is the looped sign 45 (o); the
final cc of the run-1 lines is dropped. Sign 23 (once, before "delliberet") stays unread.

Checked here (5 Nov 2026), with the key (`key.json`) and the corrected transcription
(`transcription_tomokiyo_corrected.txt`) he sent as attachments; `dec.py` re-decodes and runs the control:
- The key applied to the 308 signs gives his three runs letter for letter (66, 82 and 160 signs); sign 23 is the one
  unread sign, and 5 signs are nulls.
- Latin model `la`: -5.25 per letter against -6.90 for the best of 300 keys with the letters shuffled among the sign
  classes (mean -7.88); `lm.best_language` names Latin (-2.18).
- Our own `p1v2.txt` agrees sign for sign at both ends of run 1 (`cc ss Z K bz Z` = d-e-s-u-i-s; `cc ss g cc ss 8 vb 8
  bz x n H y I` = d-e-l-l-i-b-e-r-e-t, vb a null).
- The plaintext fits the clear text around each run: run 2 follows "me sciat quo modo valeat", run 3 precedes "amplitudinem
  tantam vendicare ... sibi et natis", and "ne ... delliberet" has "amplitudo Vestra" as its third-person subject.
  Pandolfo is Paola's brother (clear text), so "sorore nostra" fits Cleofe Malatesta, the Despot Theodore II's wife
  (Prizmic's identification, citing the DBI).
- Why we failed: 262 signs against 308. The corrected transcription counts as cipher letters the marks we had set aside
  as separators (the double slash is i, the three dots a). The 5 Oct anneal with separators kept as five extra signs
  still found nothing. We did not diff the two transcriptions beyond that.
- Limits: the key was built together with the reading, so the control shows the transcription and key are consistent, not
  that the cipher was broken independently; the preprint does not say whether the clear text served as cribs, so the
  outcome is "read after matching with key from external sources", not a ciphertext-only break by this project.

Still open outside the cipher: who Count Riciardo was and whether Gonzaga was ever offered the Morea; the doubtful
words of the clear text (prepositum?, fratrem?, sensu?) need a better image than DECODE's. Page: `docs/malatesta1428.html`.

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
- sign 23, once, before "delliberet" - blocker: illegible; the sentence is complete without it, so it may be a null; one sign, no other occurrence to compare

## Escalation
- [x] siblings: R1853 (register, 14 images) read for keys; all other Mantova records on DECODE opened (R7858-R7888, R7888-R7890); none for 1428
- [x] clear-pages: the clear parts of the letter transcribed (p1_clear.md); no decipherment on the leaf
- [x] known-keys: register keys "cum Malatesta dni Pandulfi", "nova cum fratribus de Malatestis", "ultima / prima cum Karolo de Malatestis", "Ziffra nova" 1417 tried (-4.2/char); R1855 and R1852 opened, sign sets differ
- [x] print: web search; Treccani DBI; Falcioni (Pandolfo and the council of Ferrara) prints the 1438 plaintext only; Prizmic's preprint (5 Nov 2026) is the reading
- [x] key-rebuild: Prizmic's key received and applied (key.json); annealed under 12 hypotheses here without success before that
- [x] retry: corrected transcription (308 signs) decoded with the key: 307 read, sign 23 open
