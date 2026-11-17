# Montcalm to Bougainville, 21 November 1758, in Bougainville's "code B"

Status: in progress (folder only, no page)

Class: decoded, not read (key recovered based on plaintext from external sources). Code B is rebuilt from the cipher
letters Casgrain printed with their clear text, and applied to a letter of Montcalm's that has no decipherment. 96 of
its 112 groups take a value the printed letters show; 16 take a value inferred from the order of the code, and every
word that rests on one is marked and not counted as read.

Andrew Beling, with AI agents, did this work between 11 and 17 November 2026. AI agents did all of it; no person has
checked it.

## The letter

Archives nationales (AN), fonds Bougainville, 155AP/2, dossier 1756-1758, piece 25. The AN description (FranceArchives
record of 155AP/2, read 17 Nov 2026) has: "Pièce 25. Lettre autographe, en partie chiffrée, de Montcalm à
Bougainville, parti en mission en France. Montréal, 21 novembre 1758." Three images on the AN's server, public:
[FRAN_0093_0816_L](https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0093_0816_L-medium.jpg)
(the recto: clear text, eight lines of figures in two paragraphs, clear text, a line at the foot),
[FRAN_0093_0817_L](https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0093_0817_L-medium.jpg)
(a postscript in clear dated "Ce 29 9bre", in a hand that looks different) and
[FRAN_0093_0818_L](https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0093_0818_L-medium.jpg)
(the address leaf, to Bougainville at Paris). No image is included in this folder; like `montcalm1757w` and
`montcalm1758i`, it links the archive's images.

Bougainville had just left Canada to plead the colony's case at court (he sailed in November 1758 and was back in May
1759). Montcalm writes in clear about Bougainville's letters of the 8th and 11th and his mission, then puts two
paragraphs in figures, then returns to clear for the weather, Mme Hérault and farewells. The figures are Bougainville's
own code: 110 is Québec, 73 M. de Vaudreuil, 97 la Louisiane, 74 M. Bigot, as in his letters of 1759 (below), and
Montcalm writes a "+" after some numbers where Casgrain prints "*".

The repository's Archives nationales sweep lists the piece (`research/central_archives/candidates.json`, together
with ANOM F3 15), not viewed. `targets/montcalm1758i/results/letter1758_with_sheet.txt` already holds one raw line of
an earlier code B decode of this letter, used there only to show that the Marine's code I sheet does not fit it.

## Code B and how it was rebuilt

H.-R. Casgrain, *Collection des manuscrits du maréchal de Lévis*, III, *Lettres de la cour de Versailles* (Québec
1890), prints two letters of Bougainville to Montcalm in figures with the clear text set between the lines:

| Id | Letter | Casgrain III | Printed groups |
|---|---|---|---|
| B1 | Bougainville to Montcalm, Blaye, "18 mars 1758" (that is 1759), "Pour vous seul" | no. XLVI, pp. 103-108 | 804 |
| B2 | Bougainville to Montcalm, the same day, to be shown to the governor general | no. XLVII, pp. 112-114 | 307 |

Casgrain gives the key as "Pièces militaires No V" of the Lévis papers; that key was not found (see Remaining gaps).
The scan used is [archive.org `collectiondesman03lv`](https://archive.org/details/collectiondesman03lv); every figure
line was read against the page images (`letters/B1.tr`, `letters/B2.tr`: figure lines F, clear lines C, page marks).
The figures and the clear lines are set independently on Casgrain's pages, so the unit of alignment is the paragraph.

**All readings of B1 and B2 are Casgrain's printed clear text.** Whether that text is a period decipherment or the
editors' own, made with the key then among the Lévis papers, was not established. What is added here is the table.

`solver/solve.py` aligns every printed group with a stretch of the printed clear text (annealed Gibbs sampling per
paragraph, forward-filtering and backward-sampling, then a final most-probable pass; four seeds, 600 sweeps; run
11 Nov 2026). The result (`key/code_B_solver_table.tsv`) has 330 code groups between 1 and 699 and three large
numerals; in the reference run 60 groups show a conflict and 146 are seen once. The numbers follow the alphabet: a
one-part code, letters with homophones at 1-45 (a 1, 3, 5; c 6, 8; ... t 37, 40; u 39, 43; z 45), names and set
phrases at about 47-200 (73 M. de Vaudreuil, 74 M. Bigot, 97 la Louisiane, 110 Québec), then syllables and words in
order (ba 240, ... de 312, ... ma 447, mi 449, ... ra 568, ... un 661, vos 666, votre 667, vous 668). A "+" (Casgrain's
"*") marks a second entry under the same number: 568 ra, 568+ re; 433+ la, 434+ le.

`key/code_B_table.tsv` (built by `build_key_table.py`) gives every group: the value used, `attested` or `inferred`, a
column naming the kind of inference, how often the group is printed in B1 and B2 and how often with that value, and
each place (letter, page, paragraph and group number, and the clear text aligned there). Where the solver joined a
neighbour's letters to a value (74 "mbigotmpea", 97 "lalouisiannea", 550 "projetcontr"), the value used is trimmed
and the note says so. 427 "je" is attested in "je finis" (B1 p. 108) but aligned inside "jalousies" on p. 104: a
conflict, recorded.

## The tests, in order

1. **Hold-out test of the alignment (11 Nov 2026), rule written before the runs** (`tests/holdout_result.txt`,
   `solver/holdout.py`). For each letter, a table is built from the other letter alone (seed 1, 600 sweeps; each
   group takes its commonest aligned value) and the left-out letter is decoded with it. Measured: the share of the
   characters of Casgrain's printed clear text (letters and digits, accents removed) matched by the decode
   (difflib, no junk heuristic); chance = the same table with its values shuffled among its groups, mean of 20.
   - B1 decoded with a table from B2: 466 of 804 groups known; **32.0% of the clear text recovered, against 11.1%**.
   - B2 decoded with a table from B1: 231 of 307 groups known; **49.2%, against 17.1%**.

   What it shows: the aligner recovers code B values from one letter that hold in the other, well above chance. What
   it does not show: anything about the values used only in the 1758 letter, or about the 1758 letter at all. The rule
   is written in the same file as the results; there is no hash of it from before the runs. On 17 Nov 2026 the copied
   scripts were run again: Python 3.9.6, the version of the first run, gives the same figures; Python 3.12 gives 32.7%
   against 11.5% and 51.6% against 17.4%.
2. **Transcription of the 1758 figures.** First reading 11-12 Nov 2026 on 2x-4x crops, with the code in view
   (`transcriptions/first_reading_2026-11-12/`, hashed there). This reading was made after a first decode, and one
   change came in that way (674, not 634), so it is not blind.
3. **Second, blind reading (17 Nov 2026), Test M.** The plan (`tests/PLAN_tests.md`, sha256 in
   `tests/PLAN_FREEZE.txt`, 15:24 UTC) was hashed before the reader started. A second reader had the page image only,
   no transcription, code table or reading; its figures were hashed on completion (`transcriptions/blind_2026-11-17/`,
   `FREEZE.txt`, 15:26 UTC). Rule: pass if at least 106 of 112 groups agree exactly (digits and "+").
   **111 of 112 agree: pass** (`tests/test_M_result.txt`; `tests/score_test_M.py` gives the same). The one difference
   is P1L1 group 7: 34 in the first reading, 35 in the blind one (34 = r, 35 = s). It is kept open in
   `transcriptions/figures_reconciled.txt` as 34|35; it changes no word counted here, since the word ("suspecté") also
   rests on the inferred 591. The blind reader confirms 674 (not 634) and 666 (not 668) as first choices; its other
   doubts (42|48, 340|360, 262|263, "1 18" or 118) are first choices that agree with the first reading. The reader's
   notes are `transcriptions/blind_2026-11-17/NOTES_reader.md`.
4. **The values inferred for this letter (12 Nov 2026): no test.** See below.
5. **Statistical check of the decode (17 Nov 2026)** (`docs/_validate.py`, `validation.tsv` from `make_validation.py`,
   inferred values and 34|35 left unread): 95 tokens, 58 types; the decode scores -2.125 per letter against -3.057 for
   200 random keys (z 5.8), but a key annealed onto shuffled ciphertext reaches -1.945 (mean -2.002). Verdict
   **underdetermined**: on 95 tokens of a syllabic code the letter model cannot tell this decode from a fitted key. It
   neither confirms nor refutes it.
6. **Outside confirmation of the sense.** A week later Montcalm wrote to Bourlamaque (27 Nov 1758; date from Chapais
   1911, p. 480): "Bougainville m'a écrit que vous avez goûté toutes mes vues, et notamment in extremis ma retraite à la
   Louisiane, pourvu que le ministre l'ordonne à Vaudreuil, et que celui-ci y travaille d'avance" (Casgrain V, p. 280).
   Montcalm's journal has him leave for Québec on 22 December (Casgrain VII, pp. 491-492). He calls Mme Péan "ma
   commère" (Montcalm to Lévis, Casgrain VI, p. 97). Bougainville's reply from France reports on both projects:
   "Retraite à la Louisianne admirée, non acceptée" and "Projet contre la Caroline approuvé, non suivi faute
   d'argent" (B1, Casgrain III pp. 103-104). This supports the sense of the second paragraph and of "janvier"; it does
   not test any single inferred value.

## The reading

`decode_1758b.py` (standard library) decodes `transcriptions/figures_reconciled.txt` with `key/code_B_table.tsv` and
writes `results/decode_line_by_line.txt`; every inferred value is printed `[?value]`. 112 groups; 16 with an inferred
value; 1 where the two readings of the figures differ.

`reading_fr.txt` (normalised spelling) and `reading_fr_diplomatic.txt` (Montcalm's spelling) give the two paragraphs;
`translation_en.txt` is an English translation made by an AI agent. Marks: `[?word]` rests on an inferred value;
`word(?)` is read only by emending what Montcalm wrote; `[word]` has no group and is supplied.

> M. Bigot vous(?) aura [?suspecté]. Je serai à Québec le premier [?janvier], si ma [?commère] veut. Je [?chercherai] à
> l'en(?) consoler ; [?cependant] la [?Beaubassin] sera [?sûre] de la [?préférence].
>
> Votre(?) projet de [?la Caroline] bon, [?possible] à [?peu] de frais. Songez à celui de la retraite par la Louisiane
> in(?) extremis, [?et] [?sur] cela des(?) [?ordres] [à] M. de Vaudreuil pour qu'il préparât les [?moyens] le cas
> arrivant.

The sense, if the inferred values hold: Bigot will have been suspicious of Bougainville; Montcalm will be in Québec on
1 January and will console his "commère" (Mme Péan) for Bougainville's going, though Mme de Beaubassin keeps first
place; the Carolina project is good and cheap, and the court should order Vaudreuil to prepare a retreat to Louisiana
in extremis. "in extremis" is underlined in the manuscript.

**Words that rest on inferred values** (none counted as read):

| Group | Value | Kind | Basis | Words |
|---|---|---|---|---|
| 674 | janvier | not in the printed letters | 675 février (B2 p. 112) and 681 août (B2 p. 114) are attested | janvier |
| 591 | su | not in the printed letters | S block sa 587, se 588, si 589, so 590; three uses in this letter | suspecté, sûre, sur |
| 340 | eau | not in the printed letters | between donné 336 and écri 342 | Beaubassin |
| 286 | cependant | not in the printed letters | between celui 284 and cer 287 | cependant |
| 293 | cher | not in the printed letters | C block, before choi 295 | chercherai |
| 349 | ence | not in the printed letters | between en 348 and enfin 352 | préférence |
| 461 | moyens | not in the printed letters | between monsieur 457 and munitions 465; other words fit | moyens |
| 505 | ordres | not in the printed letters | between on 502 and ou 508; other words fit | ordres |
| 535 | possible | not in the printed letters | between point 532 and pour 537; poste, port fit too | possible |
| 44 | et | not in the printed letters | end of the letter block; from sense only | et |
| 101 | la Caroline | not in the printed letters | place-name block after 97 la Louisiane; weak, since B1 spells "la Caroline" out | la Caroline |
| 4 | b | printed, not with this value | printed twice in B2 as the numeral 4; b from the letter block | Beaubassin |
| 448 | me | printed, not with this value | solver "nne" in a name and "memanqu" in "me manque" (B1 p. 108); me from ma 447, mi 449 | commère |
| 524 | peu | printed, not with this value | solver "p" inside "dépense" (B1 p. 104); peu from perdez 523 and place 526 | peu |

The audit of 17 Nov 2026 counted "11 values not attested in the printed letters": those are the eleven groups the
letters never print (the first eleven rows, 101 among them). Groups 4, 448 and 524 are printed in the letters, but not
with the value this letter needs, and are treated the same way: 14 inferred values, 16 tokens.

**Emended words** (every group attested, the word read only by changing what is written): 666 "vos" read as "vous";
668 "vous" read as "votre"; 435+ "lin" (attested once, in "Chauve-lin", B1 p. 108) read as "l'en" and, in "lin
extremis", as "in"; 325 "der" read as "des". Montcalm's 568 "ra" in "pre-pa-ra" is read as "préparât"
(imperfect subjunctive) with no change. "à" before "M. de Vaudreuil" has no group and is supplied.

**Read share**, the repository's way (`measure_read_share.py`, which calls `research/reading_audit/v10_relabel.share`;
cipher words only; `results/read_share.json`):

- strict, as marked: **0.686** (48 of 70 words; inferred, emended and supplied words unread);
- if the 14 inferred values are accepted: **0.914** (64 of 70; emended and supplied words still unread);
- if the emendations are accepted too: 0.986 (69 of 70).

With the strict marks no sentence is clean (`docs/_check_reading.py`: 0 of 7), so the letter is recorded as "decoded,
not read". The share of tokens with an attested value is 96 of 112 (0.857), `outcome.fraction_read`; it is not a share
of words read.

The clear text of the letter and the postscript on the second page are outside this reading. A working transcription
by AI agents is in `transcriptions/full_page.txt`, unchecked, with its guesses marked.

## Casgrain's nine "absolument incompréhensibles" groups (vol. III, p. 108)

In B1, at "M. Molé ... montre beaucoup [ ] pour vous", Casgrain's footnote says the text had the nine groups
`9 425* 449 38 661 306 618 3 43`, "absolument incompréhensibles", and that seven others (`312 255 467 648 23 502 618`,
"de bonne volonté") were put in their place to give a sense. Decoded with code B the nine give
**d · in · mi · s · un · cou · te · a · u**, "... un couteau". Each value is attested elsewhere in B1 and B2, 2 to 15
times (9 d 3 of 4 printings, 425* in 7, 449 mi 5, 38 s 13 of 15, 661 un 5, 306 cou 2, 618 te 15, 3 a 15, 43 u 2 of 3;
the conflicts are listed in `results/p108_groups.txt`). The sentence still does not make sense with them. This is a
decode of what Casgrain printed, not an emendation of his text; it shows only that the nine groups are good code B
values, not a misprint of the editor's seven, and that they do not say "de bonne volonté".

## Prior work searched, and what was not searched

Searched for a print of this letter, in clear or deciphered, with its phrases ("in extremis", "Beaubassin",
"commère", "21 9bre 1758", "21 novembre 1758", "retraite par la Louisiane", "Madame Hérault", "lettre d'adieu",
"le cas arrivant", "à peu de frais") in the full text, accents and spacing normalised; every hit read:

- R. de Kerallain, *La jeunesse de Bougainville et la guerre de Sept Ans* (Paris 1896), archive.org
  `lesfranpcais00kerarich` and `lesfranaisaucan00keragoog`. Kerallain had family papers. He cites this letter once,
  p. 116 note 1, "(Montcalm à Bougainville, 21 novembre 1758)", for a fact that is in the clear postscript of 29
  November on the second page (Berryer's wife a niece "à la mode de Bretagne" of the intendant). He prints no figures
  and no deciphered words. He also notes "ma commère" for Mme Péan from Montcalm's letters to Lévis.
- *Rapport de l'archiviste de la province de Québec*, 1920-21 to 1941-42 (archive.org `rapport01queb` to
  `rapport19queb`) and 1924-25 to 1926-27 (`rapport02queb_0`, `rapport03queb_0`, `rapport04queb_0`). The 1923-24 volume
  prints Bougainville's mission memoirs and his journal; it quotes his own 1759 cipher letter in clear, not this one.
- Casgrain, *Collection des manuscrits du maréchal de Lévis* I-XII (Lettres du marquis de Montcalm, VI; Journal, VII;
  Lettres de la cour de Versailles, III; and the rest), archive.org `collectiondesman01lv` to `12lv` and `00lv`: only
  the Bourlamaque letter quoted above (V, p. 280).
- Casgrain, *Guerre du Canada 1756-1760: Montcalm et Lévis* (1891), archive.org `guerreducanada01casgrich`, `02`.
- T. Chapais, *Le marquis de Montcalm* (1911), archive.org `lemarquisdemont00chap`: the Bourlamaque letter only.
- A. Doughty and G. W. Parmelee, *The Siege of Quebec* (1901), vols. I-VI (archive.org `siegeofquebec01doug`,
  `siegeofquebecbat02doug`, `03doug`, `siegeofquebecbat04douguoft`, `siegequebecandb06parmgoog`,
  `siegeofquebecbat06doug`): the Bougainville correspondence printed there is of 1759.
- R. Waddington, *La guerre de Sept Ans* III, archive.org `laguerredeseptan03wadd`: quotes Bougainville's B1
  (pp. 258-259), not this letter.
- *Collection de manuscrits ... relatifs à la Nouvelle-France* I-IV (1883-85), archive.org `collectiondemanu01blan` to
  `04blan`.
- The AN description of 155AP/2 (FranceArchives): no edition or decipherment mentioned.
- Gallica, two searches in the browser (17 Nov 2026): `"retraite par la Louisiane" Montcalm`, no result;
  `Beaubassin "in extremis" Bougainville`, four results (Casgrain VI; L. Lemonnier, *Histoire du Canada français*,
  1949; *Revue de l'histoire des colonies françaises*; N. Bourassa, *Jacques et Marie*, 1866), none of them this letter
  by their extracts.

Not searched or not reached: Bougainville, *Écrits sur le Canada* (ed. R. Lamontagne, 1993 and 2003; its letters run
from March 1756 to September 1759): on 12 Nov 2026 only the publisher's within-book search was used (Beaubassin on
pp. 74, 87, 406, none identified as this letter; "extremis" and "commère" no hits), and Google Books refused requests
on 17 Nov (too many requests), so the volume was not seen; M. Martin-Allanic, *Bougainville navigateur* (1964), which
quotes family letters; E. P. Hamilton's English translation of Bougainville's journal (1964); HathiTrust full text;
the catalogue of the London sale of 24 June 1957, which dispersed some pieces of this dossier (piece 25 is still
present). No search can show that the letter is unpublished; none of the sources above prints it or its cipher.

## What was not checked

- No person has read the figures, the decode, the reading or the translation.
- The clear text of the letter and the postscript are working readings, not checked (`transcriptions/full_page.txt`).
- The solver's table was not re-derived; the hold-out test was re-run, the four solver runs were not.
- Casgrain's figures in B1 and B2 were read against archive.org images of one scan, not against the Lévis manuscripts.
- Whether code B is the "petit chiffre" Paulmy sent Montcalm in 1757 (Casgrain III, p. 64) was not settled: code B is
  attested only between Montcalm and Bougainville.

## Remaining gaps

- Groups 674, 591, 340, 286, 293, 349, 461, 505, 535, 44, 101 (never printed in B1 or B2) and 4, 448, 524 (printed,
  not with the value needed): 16 tokens, 16 words of the reading - blocker: open-codes; values from the code's order
  and from sense, untested; the period key "Pièces militaires No V" was not located and no further code B text was
  found.
- P1L1 group 7, 34 or 35 - blocker: illegible; the two readers of the AN image (1699 x 2000 px) disagree; no larger
  image was looked for; the word also rests on the inferred 591.
- Five words read by emending what Montcalm wrote (vos, vous, lin twice, der) - blocker: open-codes; the groups are
  attested with the values written; only the key or another code B letter of Montcalm's would show whether his copy
  of the code differed or he slipped.

## Escalation

- [x] siblings: AN 155AP/2 images FRAN_0093_0702 to 1020 (dossier 1756-1758 and the 1759 correspondence to late
  August 1759) looked at as contact sheets on 12 Nov 2026: only piece 25 has figures; 1021-1400 seen only as
  thumbnails, 1401 onward not seen. Casgrain I-XII print figures only in vol. III (B1, B2 and the four code I letters).
- [x] clear-pages: the clear text of piece 25, its postscript page (0817) and its address leaf (0818) carry no
  decipherment.
- [x] known-keys: the Marine's code I sheet e001295272 (`targets/montcalm1758i`): 0 exact agreements on the 112 groups;
  code B against code I 0 of 292 shared numbers and code W 0 of 238 (`targets/montcalm1758i/results/`); against the
  Vaudreuil table of C11E 10 (`targets/vaudreuil1760`), 0 of 329 code B groups give the same value.
- [x] print: see "Prior work searched" above; Kerallain 1896 cites the letter for its clear postscript only.
- [x] key-rebuild: 14 values bracketed from the code's alphabetical order and set by sense (above); not tested.
- [x] retry: the figures read a second time, blind (Test M, 111 of 112); every inferred value and emendation regraded
  and marked in the reading.

## Files

- `NOTES.md`, `KEY_SCOPE.md`, `profile.json`.
- `key/code_B_table.tsv` (the key, with attestations and the inferred column), `key/code_B_solver_table.tsv` (the
  solver's table of 11 Nov 2026, unchanged), `build_key_table.py`.
- `letters/B1.tr`, `letters/B2.tr` (Casgrain's figures and clear text), `letters/B1_aligned.tsv`,
  `letters/B2_aligned.tsv` (one row per printed group with the clear text aligned to it, reference run).
- `solver/` (`common.py`, `solve.py`, `holdout.py`, unchanged from 11 Nov 2026; `python solver/holdout.py OUTDIR
  letters/B1.tr letters/B2.tr`, about three minutes).
- `transcriptions/figures_reconciled.txt`, `transcriptions/first_reading_2026-11-12/` (with its SHA256SUMS; the
  second file it lists is the CMNF IV p. 153 transcription, now `targets/montcalm1757w/support/CMNF4_p153_figures.txt`,
  same sha256), `transcriptions/blind_2026-11-17/` (figures, FREEZE.txt, reader's notes), `transcriptions/full_page.txt`.
- `tests/` (plan, plan hash, Test M result, `score_test_M.py`; hold-out rule and result, hold-out decodes). The plan
  file also holds Test L, a test of another target, kept so that its hash matches.
- `decode_1758b.py`, `results/decode_line_by_line.txt`; `reading_fr.txt`, `reading_fr_diplomatic.txt`,
  `translation_en.txt`; `measure_read_share.py`, `results/read_share.json`; `make_validation.py`, `validation.tsv`;
  `results/p108_groups.txt`.

Re-run from the repository root: `python targets/montcalm1758b/build_key_table.py`,
`python targets/montcalm1758b/decode_1758b.py`, `python targets/montcalm1758b/measure_read_share.py`,
`python targets/montcalm1758b/tests/score_test_M.py`.
