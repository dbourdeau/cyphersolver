# duhart1921: Pedro Duhart to "Vicente Gutiérrez", New York, 29 August 1921 (catalogue 1445)

WAINUT, 12 Nov 2026. Work by AI language-model agents for WAINUT; no human palaeographer checked the text.

Read in part, 13 Nov 2026: all 17 runs decrypt, 50 of 57 cipher words are read as typed (87.7%), seven carry an encipherer's slip. Written up on the site (duhart1921.html) at the integration of PR #511.

## Document

- CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo DCXXI Archivo de Félix Díaz,
  **DCXXI.3.231.1** (archivo no. 90934). Typed letter, 3 pages, Bayer letterhead, New York, 29 Aug 1921, signed
  P. Duhart, to "Sr Vicente Gutierrez, 1433 Pleasant St., New Orleans, La."; received stamp "SEP 2 REC'D". The
  greetings to "Isabelita" (Isabel Alcolea, Díaz's wife, per the CEHM record) and the subject lead the contributor
  to identify "Vicente Gutiérrez" as a cover name for Félix Díaz (inferred; the letter does not name Díaz).
- Record: https://www.cehm.org.mx/Buscador/FichaBasica/90934?Tipo=A
- Images (no login; the https host fails TLS, plain http answers):
  `http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/3/231/1/DCXXI.3.231.1.000{1,2,3}.jpg` (1995 px wide).
  Scans are not in this folder's git copy. `scripts/fetch.py DCXXI.3.231.1` fetches them (1.6 s apart).
- The CEHM record says "existen veintiún claves no descifradas que corresponden a personajes felicistas".

## System

Clear Spanish with 17 runs of typed capitals (R01-R17): 15 runs of personal names, one telegram phrase (R11) and
one English sentence that Duhart quotes "textually" from a financier (R12). The cipher is a **reciprocal swap of
five letter pairs**:

| pair | A-G | E-R | I-S | L-O | P-U |
|---|---|---|---|---|---|

Every other letter stands for itself (seen: B C D F H J K M N Q T V W X Y Z). Word spaces are dropped inside a
name and kept in R11 and R12. The encipherer slips: five times a plain letter (or a wrong letter) is typed where
its partner was due (R06, R08, R16, R17 twice), and three letters are left out (R03 twice, R17). In R05 the letter
in the same place as R16's slip is an A typed over another letter, which looks like the same slip caught in time.

This is not either of the systems Narváez (2015) described in the same fondo (Argumedo's numbers, A=34 ... Z=23;
Wellington's Gronsfeld-type key 313).

## Key source and held-out test

There is no key or gloss on the pages. The key was read off **R12 alone** by probable words:
`SF THSI MGN HGI GNYTHSNA TL DL WSTH THSI MGTTRE S WLN'T ERCLMMRND TL UPTG DGMN NSCKRO` gives
IF THIS MAN HAS ANYTHING TO DO WITH THIS MATTER I WON'T RECOMMEND TO PUT A DAMN NICKEL, which shows all five pairs
both ways (S/I and I/S in THSI, G/A and A/G in GNYTHSNA, R/E and E/R in MGTTRE, L/O and O/L in TL and NSCKRO,
U/P and P/U in UPTG). Frozen as `key_frozen.tsv` (`FROZEN.sha256`) before the other runs were decrypted.

Held-out (`scripts/heldout.py`, `expected.tsv`): the 16 other runs, decrypted with the frozen key, against the
names and the phrase the clear text points to: **11 of 16 runs exact; 252 of 260 letters (96.9%)**. The five
misses are the encipherer slips listed above, not key errors. The seven letters R12 did not show (B F J Q V X Z)
all decrypt as themselves in the held-out runs (RUBIO, RAFAEL, NARANJO, ESQUIVEL, NAVARRETE, EXCLUYENDO, GARZA).
Caveat: the expected forms were written after the decryption, from the decryption and the clear text, so this is
a consistency test, not a blind prediction. Key files: `key_frozen.tsv` and `key.tsv` hold the same 10 entries
(cipher letter to plain letter, the five pairs written both ways); `key.tsv` differs only in its comment line. The internal check is stronger: the two men of R01 and R05 (the general
who claims the capital and the man who "manages" him) return as R15 and R16 on p. 3 with the same claim; "el Sr
1o" is the first of R01-R04 and "los Sres 2o 3o y 4o" the other three.

## Reading

`reading_DCXXI.3.231.1.md` (marked runs, then each run in its clear Spanish sentence),
`translation_DCXXI.3.231.1.md` (English). `scripts/check_marks.py` rebuilds `decryption_DCXXI.3.231.1.txt`
from the transcription and the frozen key and fails on any unmarked departure: it passes.

Words: **57 cipher words: 50 verbatim from the signs (87.7%), 7 with a marked repair, 0 from a gloss, 0 holes.** By the README read bar a word with a restored or replaced letter is not read as typed, so 87.7% is the share; the contributor's own figure counts the seven repaired words as read (100%, no holes).
Repairs: ESQU{+I}VEL, OBR{+E}GON (R03), ALDAP{R/E} (R06), ALD{N/A}PE (R08), NE{A/G}RETE (R16),
GA{E/R}CI{G/A} and NARA{+N}JO (R17).

Dan's `docs/_check_reading.py` (13 Nov 2026): reading file 0.686 clean share (48 of 70 sentences; 0.676 on 12 Nov,
before one note was reworded), translation 0.806 (29 of 36), decryption 0.167 (the
decryption is unspaced names, which the period word lists do not know; the reading's unclean sentences are the
name lists and modern unaccented Spanish words such as "telefono", "Ud", "concurri").

State proposed: **not prose** (as in ralamb1657 image 104/114: short runs set into a clear letter). All runs are
deciphered and R12 is a whole English sentence read verbatim. Class at the integration: **read in part** (see Integration check).

Persons named. The runs give names as written; the identifications below are the contributor's, from those names
and the 1921 exile in New York, and the first names in brackets are not in the letter:
"General Samuel Cuellar" (R01) and "Garcia Cuellar" (R15), identified as General Samuel García Cuéllar; Manuel
Calero; Toribio Esquivel Obregón; Rafael Martínez Carrillo (three of these four are identified as signers of the
"Essay on the Reconstruction of Mexico" named in clear on p. 3); López Negrete (no first name in the letter); Garza
Aldape (probably [Manuel] Garza Aldape); García Naranjo (probably [Nemesio] García Naranjo); Rubio Navarrete
(probably [General Guillermo] Rubio Navarrete); Villar (probably [Pedro del] Villar); and Cantú (probably
[Esteban] Cantú), Lucio Blanco, Pablo González, Cándido Aguilar and Murguía (probably [Francisco] Murguía), whom
the contributor identifies as rebel chiefs of 1921. R11, the phrase of Duhart's telegram of the 15th, is
"excluyendo actual representante": the friends will join only without the present representative. That the
financier's "this man" in R12 is the same representative is inferred from the context, not said in clear.

## Prior art (checked 12 Nov 2026)

- CEHM catalogue: "claves no descifradas".
- Narváez, R., "Sobre algunos criptosistemas mexicanos de principios del siglo XX", Documenta & Instrumenta 13
  (2015), pp. 107-132 (https://revistas.ucm.es/index.php/DOCU/article/view/49742), read in full text: deciphers
  DCXXI.3.244.1, 3.250.2 (Argumedo) and 6.588.1 (Wellington); no mention of Duhart or this letter, and no
  reciprocal letter swap.
- One web search on Duhart, Félix Díaz, Garza Aldape, García Naranjo, Rubio Navarrete and the 1921 New York juntas:
  general literature on the felicista exile only (Henderson 1981; Henderson and Zarauz López), nothing on this letter.
- Dan's repo origin/main (65445e3f8, 12 Nov 2026): no target folder, PR or issue on Duhart, DCXXI or felicista.

## Independent review (13 Nov 2026)

An AI language-model agent working for WAINUT, separate from the solver, opened the scans and copied the capitals
blind from its own crops before reading this transcription. Its list names R01-R06, R08 and R09 on p. 1, R12-R14 on
p. 2 and R15-R17 on p. 3 (14 runs; the review's own tally line says 12 of 17): 0 disagreements, including the
overstrike in R05 letter 8 and the encipherer slips kept in R06, R08, R16 and R17. It re-ran `check_marks.py`
(passes: 57 words, 50 verbatim, 7 repaired, 0 holes), decoded R01, R03, R12 and R14 by hand with the same output,
checked `key_frozen.tsv` against `FROZEN.sha256`, and reproduced the held-out result (11 of 16 runs exact, 252 of
260 letters). It counted 8 of 8 context sentences without holes. It agreed with the state not prose and graded the
reading A. It raised no correction to the transcription or the reading.

## Remaining gaps

- The seven repaired words (ESQUIVEL, OBREGON, ALDAPE twice, NEGRETE, GARCIA, NARANJO) - blocker: illegible; the typist's signs are wrong or a sign is missing (an encipherer slip: a plain letter typed where its partner was due, or a letter left out), so no key reads them as typed; each name occurs correctly elsewhere in the letter.

## Limits of the check (not gaps in the reading)

- Independent blind review (13 Nov 2026, an AI language-model agent separate from the solver): the runs it copied blind
  from crops agree letter for letter with the transcription; R07, R10 and R11 were not in its spot-check. No human
  palaeographer has checked the text.
- The held-out expected forms (`expected.tsv`) were written after the decryption, so the held-out figure is a
  consistency test (the reviewer repeated this caveat).
- Identifications of persons are the contributor's, by surname and context. The letter gives first names only for
  Samuel, Manuel, Toribio, Rafael, Lucio, Pablo and Cándido; the other first names are bracketed and marked "probably".
- Who "this man" / the "actual representante" is is not said in clear in this letter.
- The other 11 letters of catalogue entry 1445 are not in this target (other systems, listed below; the catalogue entry
  stays, narrowed). Seen at contact-sheet size on 12 Nov 2026: Mina (3.263.1, 3.278.1) use groups of numbers and letters
  (e.g. 35-33-15-16-6-3-07-Z), Amaya (3.242.1) two-digit numbers with a few pencil letters written over them; neither is
  this letter swap. DCXXI.3.323.1 (Sánchez) is target sanchez1922 (key 313). Not worked: DCXXI.3.256.2 (same family as
  Mina), 3.301.2 and 5.514.1 ("Ch.", two-digit numbers), 5.474.2 (Lozano, two-digit numbers with pencil names in the
  margin), 3.288.1 (Suárez, cipher not located at contact-sheet size), 6.576.1 and 7.656.1 (not viewed beyond download).
- The companion records DCXXI.3.231.1-2 (Gutiérrez's reply) and 3.231.2-2 (a letter in clear jargon, "bonita mañana",
  "felitus") were not worked.

## Integration check (13 Nov 2026)

Done by the integrating session. Reproduced: `heldout.py` 11 of 16 runs exact, 252 of 260 letters (96.9%); `check_marks.py`
passes (57 words, 50 verbatim, 7 repaired, 0 holes); the decryption file rebuilds identically; `key_frozen.tsv` matches
`FROZEN.sha256`. Own decode of R01, R03, R12 and R14 from the five pairs gives the same text. Images DCXXI.3.231.1.0001 and
.0002 fetched from the CEHM viewer (plain http, no host refused) and compared with the transcription: R01-R10 (p. 1) and
R11-R14 (p. 2), about 290 of the 325 letters, all agree; p. 3 (R15-R17) was not compared by the integrating session. The held-out
expected forms were written after the decryption (the contributor says so): a consistency test, not a prediction; the
frozen file has no external timestamp, so the order of events is by the contributor's record. Class changed from read to
**read in part**: seven of 57 words carry a restored or replaced letter and the README rule does not count them as read, so
the strict share is 50 of 57 (87.7%); the contributor's 100% counts them. Not claimed: the identity of "Vicente
Gutiérrez" or of the "actual representante" (the contributor's inference).

## Escalation

- [x] siblings: the 12 records of catalogue entry 1445 opened at contact-sheet size; the others use number or number-and-letter systems (Mina, Amaya) or are sanchez1922 (a different key, its own page)
- [x] clear-pages: none on the pages; the clear Spanish names the same men as the runs
- [x] known-keys: Narváez's two felicista systems (Argumedo's numbers, Wellington's 313) tried in the notes; neither fits a letter swap
- [x] print: Narváez 2015 read in full; one web search on the persons; nothing on this letter
- [n/a] key-rebuild: the key is complete (ten entries, five pairs); the seven repaired words are typing slips, not missing values
- [x] retry: every run decoded again with the frozen key; the five misses are slips, as listed
