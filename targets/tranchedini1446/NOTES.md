# Nicodemo Tranchedini (and Boccaccino Alamanni), Florence, to Francesco Sforza, 27-29 Nov 1446 and 19-22 Feb 1448 (BnF italien 1583 ff. 134, 139; DECODE R7905, R7908; italien 1585 ff. 28, 30), catalogue 1308 and lead 1317

Status: in progress. Leaves identified, the cipher located (two of the five leaves of the lead) and f. 139 transcribed once (778 signs, rough); no reading yet. Opened 4 Nov 2026 (Claude Sonnet 5.5). Since 14 Nov 2026: the key sheet DECODE R5318 ("Nicodemus") is this key by the contributor's record (Brice Dudout, PR #630), and the two letters of Feb 1448 (lead 1317, reserved for Brice Dudout; PR #625) are kept here as the same key in a later state (`dudout1448/`). f. 139 is decoded in part, not read.

## What the five DECODE records of the lead really are (images seen 4 Nov 2026)

| DECODE | folio | date | what is on the image | cipher? |
|---|---|---|---|---|
| R7905 (P1, P2 address) | f. 134, mount (54) | 27 Nov 1446, Florence, Nicodemo to Sforza | short clear letter with **six or seven runs of signs**; over most runs a small contemporary hand wrote the plain words between the lines | yes, short; glossed |
| R7906 (P1, P2 address) | f. 135, mount (56) | 28 Nov 1446, Florence, Nicodemo to Sforza | a full page of clear Italian (news from Cesena, Malatesta, Roberto da Sanseverino, Venice; says "scriverey questo in ciffra" but is itself clear) | **no** |
| R7908 | f. 139, mount (57) | 29 Nov 1446, Florence, Boccaccino Alamanni and Nicodemo to Sforza | one page, about 28 lines: clear Latin/Italian words alternating with long runs of signs; seal, damaged foot | **yes, the real target** (about 800-1000 signs) |
| R7909 | **f. 145**, mount (59) | **1 Dec 1446, Milan, Duke Filippo Maria Visconti to Sforza** | a membrane slip wholly in cipher, same hand and alphabet as f. 136 (R7907); pencil 145, mount number 146 | yes, but **not Tranchedini's: it belongs to `../visconti1446/` (key R5323)** |
| R7910 | f. 147, mount (61) | 3 Dec 1446, Sforza's camp "in valle Fagnani", Sforza to Alamanni and Nicodemo | clear minute with corrections: the reply to their letter of 29 Nov (the money for the troops, the quarters at Montevarchi, Cosimo) | **no** (useful as context for f. 139) |

Catalogue 1308 calls R7909 "f. 143 ... cleanest full-sign leaf": that is wrong, and `../visconti1446/NOTES.md` lists f. 145 as "not on DECODE":
it is R7909. Also wrong in the lead: the Gallica ark is ital. 1587 (`../it1583/NOTES.md`); ital. 1583 is not on Gallica (microfilm MF 16151).
Mazzatinti's inventory (`../visconti1446/mazzatinti_ff.txt`) lists f. 133 (Nicodemo, 25 Nov, "in cifre"), f. 132 (his postscript), f. 126 and f. 162
(Nicodemo, 30 Nov) as further Tranchedini items; none of them is on the DECODE records of this lead (not looked for yet).

## Key family

- f. 134's glosses show the **non** sign (double comb) is the same as in Domnina (2018, Fig. 5, from ASMi Carteggio Sforzesco 41 no. 106, 1454) and George Lasry's
  1452 reconstruction (`../tranchedini1452/lasry/report/images/key_2.png`; `key_1.jpg` is Domnina's figure). The alphabet of f. 139 looks the same on a first
  look: + = e, 8 = i, an inverted T = r, an inverted V = to, a dotted slash = u/v.
- Domnina notes the code "was evolving over time" and the same sign sometimes has another value in 1453 than in 1454: a 1446 key can differ in
  many values and in the nomenclator. Her key (81 signs) and Lasry's (55) are both later than these letters. No 1446 key sheet was known on 4 Nov; see the sections of 14 Nov 2026 (DECODE R5318).
- Word signs in 1446 that are not in either later table: one sign for *stantie* and one for *Fiorentini* (glosses, f. 134). So the nomenclator has to be
  recovered here, not read off.
- Tranchedini's key of 1471-78 (Francesco Tranchedino's codex, Cerioni 1970; 253 signs) does not match the later letter that Domnina studied; not compared with f. 139.

## Prior art (4 Nov 2026)

Searched: Domnina 2018 (ECP 149), Cipher Mysteries, Tomokiyo (via catalogue vetting of 2 Nov), a web search on the shelfmark and correspondents. No decipherment or
edition of f. 134 or f. 139 found; Mazzatinti gives headings only. The interlinear glosses on f. 134 are a decipherment of the time of those runs only.
Prior art: open.

## Method / log

See `WORKLOG.md`. Short version: images copied from the it1583 worktree, five leaves viewed, f. 139 and f. 134 cropped at 2-5x, glosses on f. 134 read
(`texts/f134_glosses.md`), Domnina's Figure 5 extracted and compared with Lasry's table (same figure). No transcription of f. 139 yet.

## 4 Nov 2026 (later): f. 139 transcribed, first table test

- **Transcription** (`texts/f139_A.md` lines 1-21, `texts/f139_B.md` lines 22-43, merged without the duplicate row L21 into `texts/f139_signs.txt`): two agents read crops at
  3-6x and named each sign after Domnina's / Lasry's table where they could, `@NN` otherwise. Measured with `docs/_check_profile.py --measure`: **778 cipher
  signs, 172 distinct labels, IC 0.017**; 240 signs (31%) carry an unmatched `@NN` or `?`. The 172 types are certainly too many (the key has perhaps 80-100):
  the two agents numbered their `@` shapes separately (A: `@01`-`@44`, B: `@101`-`@158`) and split look-alikes. The page has about 43 text lines, not 45; L21 and
  L22 are the same row; L31-L33 may double-count one row; the foot (L41-L43) is clear. Runs often cross the line break.
- **Anchors that held:** line 3 after "a darvi": ce n to mi l a = *cento mila* (before the clear "4m cavalli et 2m fanti"); L6 has a run that reads "...te se i mi li a" =
  *sei milia(?)*; the comb sign = *non* (also glossed on f. 134); the bar-o-bar-o sign (Veneziani in the tables) closes runs after "ala via" (L2), "pighar la via" (L10),
  "l'impresa contra" (L21), "da tener" (L25) and so on: 11 times, so the letter is about the Venetians' way/party. CON and IN, CHE, ET are matched with moderate confidence.
- **Test of the table** (`table_test.py`): on 54 stretches of at least three table-valued signs (259 signs), the 1454/1452 values gave -3.91 per letter against -4.62 (z = 2.5), **but that run scored text without spaces against the model that includes spaces (the benchmark "Italian is -1.5" was for spaced text). Corrected 5 Nov with the no-space model (order 5): -2.16 vs -3.04 for shuffled values (sd 0.23), z = 3.9; real Italian without spaces scores about -1.8.** The table does carry signal on f. 139.
  Either the 1446 key differs from the 1452/1454 table in many values (Domnina says the code evolved), or the transcription is too noisy, or both.
- **Not done:** no unification of the `@` shapes across the two files (needs a common sign sheet: crop every occurrence and compare side by side), no 1446 key table,
  no alignment of the f. 134 glosses sign by sign, no control text (a control needs a solver, and a solver needs a clean transcription).
- **Next steps** (in order): (1) one sign inventory for f. 139 by cropping every occurrence of the frequent unmatched shapes (`@101` x18, `@102` x16, `@12` x16,
  `@06`, `@08`, `@15`, `@09`, `@18`, `@111`) and merging look-alikes; (2) transcribe f. 134's runs sign by sign and align them with the glosses (the only 1446 witnesses);
  (3) re-run `table_test.py` with the 1446 values, then a crib attack on the runs that sit between clear words ("che el [..] habia el modo", "a darvi cento mila [..]");
  (4) the Ambrosiana "ex cifra Nicodemi" decipherment (Z 219 sup., 1452) and Cerioni 1970 for the key.

## 5 Nov 2026: one sign inventory for f. 139 (automatic)

- **Method:** `seg.py` deskews the leaf by 0.8 degrees, finds 41 text lines from projection peaks and cuts the glyph groups of each line; `cluster.py` clusters the 1080 narrow groups (Ward, 90 clusters) and writes contact sheets (`seg/clu_90_*.png`, git-ignored) that I checked by eye; `seqs.py` writes `texts/f139_seg.txt` (cluster id per group, `W` = wide group, `x<id>` = cluster of clear-text fragments).
- **Result:** 863 narrow cipher-looking signs in **73 types** (the two hand transcriptions had 172 labels), IC 0.0177. The frequent clusters are visually clean (+, 8, 9, 2, three slash variants, filled and dotted A, b with bar, the comb, the clover, the Sforza sign). Not separated yet: 237 wide groups (clear words or linked signs such as the Veneziani and che signs) and 217 clear-text fragments, which pollute a few clusters (c32 mixes Veneziani with word fragments).
- **Table test again** (`table_test2.py`, 40 clusters mapped by eye to the Domnina/Lasry values, 70 stretches, 276 signs): -3.48 per letter vs -4.06 (sd 0.26) shuffled, z 2.2. Same weak fit as with the hand labels, so the later table does not give Italian here whichever transcription is used; the 1446 values are different or my by-eye mapping is partly wrong.
- **Next:** separate the wide groups and clear fragments; learn 1446 values from the cribs (cento mila, non, Veneziani, the f. 134 glosses) with a homophonic solver and a control text.

## 5 Nov 2026 (later): correction, partial decode with the table, solvers

- **Correction:** the tests of 4 Nov used a spaced language model on unspaced output. With `lm.load('it-cinquecento', order=5, spaces=False)` the hand-labelled stretches give z = 3.9 (table -2.16, shuffled -3.04), and the clustered by-eye mapping z = 1.8 (-2.23 vs -2.50). Statements "z 2.5, mostly noise" in earlier notes, in the profile and in catalogue 1308 are replaced.
- **Partial decode** (`texts/f139_partial_decode.txt`: clear words kept, table values for matched labels, `_` unmatched, `[a/b]` two candidates). Readable stretches: "o qui hauete che" (L32), "cento mila" (L3), "...imilia" (L6, milia), "et sforza pen..." (L16), "non in", "et non per", "nnauero ... che", "o che pi ne da" before the clear "pigliasso tal stato" (L27), and the Veneziani sign closing runs ("la presa contra ... veneziani in par[te]", L21-L22, L25, L30). So the table letters are largely right; the nomenclator and syllable signs (the unmatched 31%) are what is missing.
- **Solver 1** (`solver.py`, all 75 types of `texts/f139_runs.txt` free, 691 signs): real -2.54, sign order shuffled -2.59, synthetic cipher of the same shape: true key -2.32, solver -2.42, 1 of 53 types recovered. The data are too few for a ciphertext-only solver (no power on the control).
- **Solver 2** (`solver2.py`, table values fixed for 455 of 788 labelled tokens, 115 free types): real -2.30 against -2.51 to -2.60 with shuffled order. Held-out control fails: freeing the 5 / 10 most frequent matched labels restores 2/5 and 0/10 table values at the same score (-2.31, -2.29), so the solver's values for free labels (e.g. @101 = ne) are not evidence; it overfits with frequent syllables.
- **Next:** read the unmatched shapes from the clear context instead of a score: the repeated runs (the "la presa contra [..] veneziani" family, names after "Cosimo", the f. 147 reply as plaintext), and align f. 134's glosses sign by sign.

## 5 Nov 2026 (last): reading the unmatched shapes from context

- **f. 147 (Sforza's reply of 3 Dec, R7910) read at the top:** he answers "quello mi scrivete per la vostra de di 29 del passato" and says he answers "maxime supra lo facto del dinaro e dele stantie" (money and quarters), then the quarters at Montevarchi (about 3500 horse). So the topic of f. 139 is money for the troops and quarters; this fits the clear "cento mila ... 4m cavalli et 2m fanti". It gives no wording to match against (the reply is a paraphrase, not a copy).
- **Value inference by language model, held out** (`heldout.py`): freeing one table-valued label at a time (the 25 most frequent) and letting the model pick its value restores 5 of 25 with a letters-only pool and 2 of 25 with syllables. With 45% of the tokens unknown, the context is too broken: no value of an unmatched shape is accepted from a score.
- **Crib search** (`cribs.py`, 19 words from the clear text of f. 134/139 and f. 147: denaro, stantie, cavalli, Cosimo, Fiorentini, Milanesi, ducati, Montevarchi, conte, compagnie, gente, pace, guerra, duca ...; unmatched sign = 1-2 unknown letters; 300 order-shuffled controls): none of them is spelled out letter by letter (gente and conte once each, conte below chance). So money, quarters, places and parties are written by word signs of the nomenclator, not spelled; that fits the glosses on f. 134 (one sign each for stantie and Fiorentini).
- **What this means:** the table gives the spelled stretches (qui hauete che, cento mila, sei milia) but the letter's content words are signs of a 1446 nomenclator that no table holds. They can be learned only from an aligned plaintext/ciphertext pair. The f. 134 glosses are such a pair but short (six runs); the next real step is to transcribe f. 134's runs sign by sign and read off the word signs (stantie, Fiorentini, gente d'arme, le compagnie), then look for those signs in f. 139.

## 5 Nov 2026 (end): f. 134 runs sign by sign, a new reading of the bar-o-bar-o sign

- `texts/f134_signs.md` lists the seven glossed runs sign by sign. The glosses of f. 134 are the only 1446 witnesses to the nomenclator.
- **The bar-o-bar-o sign is glossed *duca*, not Veneziani.** Run 3 (line 4, gloss "alle vice(?) del duce") ends with it and the gloss's last word sits over it. In the 1454 tables the same shape is Veneziani, so the 1446 nomenclator differs there (the Duke, Filippo Maria Visconti, was then the other party; in 1454 Venice was). It closes runs on f. 139 eleven times after "adherirvi ala via", "pighar la via", "l'impresa contra", "al fauor de", "adyutassi": read as *duca* they give "la via del duca", "al favor del duca", "l'impresa contra [..] duca", which fits the Duke's own letter to Sforza of 1 Dec (f. 145, R7909) and Sforza's reply of 3 Dec. This replaces my statement that the letter is about the Venetians' side. **Tentative: one gloss and the contexts; not a decipherment.** The partial decode file still prints the sign as `veneziani` (the table name).
- **Run 6, "le compagnie in":** le (loop-cross), co (b with dot), m, pa (four circles), g (bar-o-bar) are table values, so *compagnie* is spelled with table syllables in 1446: five table values attested directly in 1446 by one gloss (besides non).
- **Fiorentini = a V with a small circle on each top corner** (one sign). The f. 139 transcriber labelled that V form SFORZA? (the table's Sforza is the U form): the V form on f. 139 should be read Fiorentini unless a context says otherwise.
- **"gente d'arme in Toscana"** is written twice (runs 1 and 4) in 11 and 8 signs: a spelled/syllabic phrase with homophones, not one word sign. Money, quarters and the parties are therefore a mix: word signs for stantie, Fiorentini and duca, spelling for the rest.
- **Next:** align the f. 139 inventory to these three word signs (find every V-with-circles and bent-F), re-read the runs around "duca" and "Fiorentini", then look at the crossing of the Duke's letter f. 145 with the same nomenclator (visconti1446).

## 5 Nov 2026 (re-read): duca and Fiorentini on f. 139

- **Fiorentini (V with a small circle on each top corner):** found on f. 139 at L7 (end of the run after "a luy modo"), L23, L28 and L36 (a rotated form, a triangle on its side with one circle, at L5 and L35, is unchecked). Clear context at L36: "... fermamente credeva(no) che [Fiorentini] debiano hauer per male" (that the Florentines would take it ill), at L28: "mostrassiue uolcie far una bona p. a [Fiorentini]". The agent's SFORZA? label at L7 was this sign; the U form (Sforza) is at L31, L34 and L37 only.
- **Duca (bar-o-bar-o):** 11 occurrences on f. 139, read with the f. 134 gloss: L2 "adherirvi ala via [..] duca [..] et duca"; L10 "pighar la via [..] duca / che come e dito"; L16 "al fauor de [..] duca, debiate sforzar la ..."; L36 "ad pregarlo adyutassi [duca]"; L21/22 "l'impresa contra [..] duca in parte". It reads as sense each time.
- **Positional check (new):** the sign before the duca sign is the "o" sign in 5 of 11 cases (base rate of o 6.6% of tokens, binomial p = 4e-4), and four runs end "e X o DUCA" with X = @12 or @102 (both a 9-form): read X = l it is "e lo duca" (L6, L10, L22 with a doubled l, L25). So @12 and @102 are probably l (the table's l is a 9 with dots), which also fits the solver's own choice of "li" for both, although the solver failed its held-out control. Tentative.
- **What the letter then says (sketch, not a reading):** the two Florentine agents report that Cosimo urges Sforza to take "la via del duca" (the Duke of Milan, who wrote to him on 1 Dec, f. 145), promise 100,000 [ducats] for 4000 horse and 2000 foot, urge him to favour the Duke and to ask him to help, and warn that the Florentines would take it ill. This rests on the clear text plus these two signs; the cipher runs themselves are still unread.
- **Relabelled (relabel.py, `texts/f139_relabelled.txt`):** the 9-shape signs @12 and @102 are one sign (32 uses). Scanning all 55 candidate values for it with everything else fixed, **l** scores best (-2.120 against -2.187 for i; z 2.3 among the 55). With l, duca and Fiorentini the table letters score -2.149 over 456 letters, z 4.0 against 100 shuffled assignments. 'e lo duca' now stands in six runs, plus 'duca in' twice, 'cento mila hor.', 'hauete che'. 487 of 788 run signs carry a value (62%), 301 do not: the reading bar (95%) is far off.
- **Control:** hiding a table sign and scanning it back restores u, a, e, i (rank 1) and o (rank 2) (>= 16 uses each) but not re, te, p, c, n (rank 2-26): the scan only works for the commonest signs. So only @12 = l is taken (tentative); @101 (hooked x, 18 uses, often last in a run) scores best as e but only z 1.8 and is **not** taken. Other unmatched shapes (<= 9 uses) show no clear best.
- **Rotated V:** the first sign of L5 (the run continued from L4) is a left-pointing triangle with circles on its right edge: the Fiorentini sign turned on its side, unconfirmed. L35 has no V in the labels.
- **Word signs after clear function words:** none; no sign repeats twice after the same clear word.
- **Next:** the 301 unmatched signs. Candidates: transcribe f. 134 runs 1-6 against their glosses for more values (gente d'arme in Toscana is spelled), and f. 147 (Sforza's reply, clear) for the content words; re-do the f. 139 transcription of the unmatched shapes with the cluster inventory, since @NN labels split look-alikes.

## 14 Nov 2026: issue #616 (Brice Dudout), two cipher and clear pairs of February 1448 by the same envoy

Brice Dudout points to BnF italien 1585 (Gallica `btv1b52525947w`): f. 28 (cipher) with f. 27 (clear), 19 Feb 1448, and
f. 30 (cipher) with f. 29 (clear), 22 Feb 1448, as the aligned pair that the entry of 5 Nov above says is needed.

Checked here:
- **The pairs are real and already in the repository**, under lead 1317 (`research/leads.json`; Nicodemo Tranchedini to
  Francesco Sforza, 1447-49) and in `research/venice_milan_print/ital1584_copies_B.md` (leaf-by-leaf check of
  29 Oct 2026, itself after a pointer of Brice Dudout's of that day): f. 28 = canvas 54, f. 27 = canvas 52, f. 30 =
  canvases 58-59, f. 29 = canvases 56-57. This file did not cite them; it does now.
- Canvases 52 and 54 fetched again from openapi.bnf.fr (IIIF, no bot check): f. 28 is a slip of 20 lines signed
  "Idem Nicodemus", "Florentie 19 februarii 1448", about 13 lines of cipher runs between clear words; f. 27 is its text
  in clear from "essendo Cosimo et l'altri in camera" to "qualche altro bel tracto".
- **What kind of clear text it is:** not a decipherment of 1448. Ff. 27 and 29 are neat copies in an 18th- or
  19th-century hand with a French date in the margin ("1448. 19 février"). Where the copyist could not read a sign he
  left a dash and drew the sign in the margin: two on f. 27 ("et dice — Cosimo", "de' — Milanesi"), about six on f. 29
  ("fiorini —", "Ragona —", "Fiorentini — Milanesi", "facto —"). So the copies are an existing decipherment of the
  spelled text and of most word signs, and they are silent exactly on some nomenclator signs.
- The sign shapes of f. 28 look like those of f. 139 on a first look (the double comb, 8, inverted T and V, the dotted
  slash, the long runs of small o); not compared sign by sign.

What it is good for here: a 1448 table built on f. 28 against f. 27 and tested on f. 30 against f. 29 would be fifteen
months later than f. 139, against six and eight years for the tables of Lasry (1452) and Domnina (1454) that give
62% of its signs a value. Word signs for Cosimo, Fiorentini, Venetiani, Milanesi, the Signor Sigismondo and sums of
money are the kind f. 139 lacks. Whether the 1446 and 1448 nomenclators agree is not known: f. 134's gloss signs for
*stantie* and *Fiorentini* are the first test.

Where it belongs: the 1448 letters are lead 1317, not this target. If the 1448 table proves to be this target's key,
one key, one entry applies and the letters join one folder; if not, the table is a neighbour's key used as a start,
and 1317 gets its own target. Brice Dudout offers to build the table with the sign labels of `texts/f134_signs.md`,
learning on f. 28 and keeping f. 30 held out. Not attempted here.

## 14 Nov 2026 (night): PR #625 (Brice Dudout), the 1448 table and its held-out test, checked

Files, filed as `targets/tranchedini1448/dudout/` and since moved to `dudout1448/` (table learnt on BnF ital. 1585 f. 28 against the later copy f. 27; one
held-out measurement on f. 30 against f. 29; the two tests on this target that issue #616 asked for). Checked here:

| claim | filed | re-run here | how |
|---|---|---|---|
| SHA-256 of PREREG, pass A, table, settled f. 28, two scripts, reference, f. 30 text | 8 values | 8 of 8 match | `sha256sum -c HASHES.txt` |
| table from the settled f. 28 text | 65 labels | 65; file byte-identical | `build_table.py` |
| f. 30: signs / runs / signs with a value | 846 / 13 / 655 (77.4%) | same | `measure_f30.py`; own decoder |
| f. 30: character agreement with f. 29 | 0.650 | 0.650 | his script; a second decoder written here gives 0.650 |
| 200 within-class shuffles | mean 0.201, best 0.283, z 10.9 | same; 200 shuffles over all labels (own decoder): best 0.256 | both |
| verdict by his thresholds | partial | partial (0.650 is above 0.283 + 0.30 and below 0.85) | |
| f. 139 with the 1448 values (order-4 model) | coverage 62.1%, -2.209, z 4.3; his rescoring of the table used here: 61.6%, -2.320, z 3.6 | same | `test_1446.py` |
| label types valued by both tables | 34 of 40 the same | same | |

- **Images** (openapi.bnf.fr IIIF, no bot check; views 54, 56, 58): 36 signs of f. 28 (runs R1 to R3, lines 4 to 7) and
  61 signs of f. 30 (run R1, lines 5 and 6) compared with his transcriptions: 35 of 36 and 60 of 61 agree, the two others
  are shapes that the crop does not settle (the gamma sign on f. 28 line 4; the loop-with-dot on f. 30 line 6). The f. 29
  reference words for R1 to R4 match the copy (view 56), dashes included.
- **Order of events:** the hashes match the files; that the table was frozen before f. 30 was looked at, and that the two
  blind passes were blind, is by the contributor's record (one commit, no outside time stamp).
- **What the test shows.** The held-out figure is real and far from chance, and by his own pre-set thresholds it is
  "partial", not "read": 191 of 846 signs of f. 30 have no value because the training slip (about 240 signs) does not
  hold them. Nothing is read anew: ff. 27 and 29 already give the text of both letters (existing decipherment in later
  copies, with dashes for a few word signs).
- **His joining rule, as written, is not met** and is recorded as not met: *stantie* has no witness on ff. 28 or 30, and
  the f. 139 score (-2.209, order-4 model) is below the -2.149 he took as the bar (an order-5 figure; with one model for
  both tables the 1448 values score better than the table used here, -2.209 against -2.320). Two of the three failing
  conditions are therefore about the size of the training slip and about the model, not about the key. The question
  whether 1448 is this target's key is settled with the key sheet of PR #630, in the next section.
- **Signs:** Fiorentini (V with a circle on each top corner) has the same value in 1448 (f. 28 once, f. 30 once). The
  bar-o-bar-o sign, glossed *duca* on f. 134, stands seven times where the copies have *Venetiani* (f. 28 once, f. 30 six times).
- No reading is added by this pull request, so no `reading_review` is recorded for it.

## 14 Nov 2026 (night): PR #630 (Brice Dudout), the key sheet DECODE R5318 "Nicodemus", checked

Files: `r5318/` (two transcriptions of the sheet, the second blind by the contributor's record; the settled key given
against the 1448 shape labels; `compare.py` and its results). This answers the escalation item "cart. 1597 headings not
searched for Nicodemo".

**What could and could not be checked.** The DECODE record page opens without a login (ID 5318,
"Carteggio_Sforzesco_scat._n.1597_18", Milan State Archives, record dates 1450-1555, no names) but its image is
"Authentication required": the sheet was not seen here. Its heading "Nicodemus", the pencil note "Chiave della cifra di
Nicodemo del gennaio ... 1451", that it is a later copy, and every shape on it are **by the contributor's record**. The
SHA-256 he gives for the settled key (04c8ae96...) is of a working file that is not in the pull request; the filed
`key_R5318_by_1448_label.tsv` hashes e78881b96a84..., so the freeze cannot be checked. Cerioni 1970 (the Sforza cipher
keys), which may print this key, is **not checked**, by him or here.

| claim | filed | re-run here | how |
|---|---|---|---|
| 1448 labels with an R5318 sign of the same shape: same value | 54 of 58 | 54 of 58 | `compare.py`, output identical to `results_R5318.json` |
| the same with the labels of his blind pass B | 42 of 49 | 42 of 49 | same |
| f. 28 valued tokens that R5318 decodes as settled | 194 of 222 = 0.874 | same | same |
| 200 within-class shuffles of the R5318 values | mean 0.028, best 0.126, z 31.7 | same | same |
| coverage of f. 28 / f. 139 tokens | 94.6% / 62.1% | same | same |
| the five glossed word signs of f. 134 are on R5318 with the glossed value | stantie, duca, gente d'arme, Toscana, Fiorentini | the shapes he records for these five entries, in both passes, are the shapes of `texts/f134_signs.md` (runs 2, 3, 4, 4, 7: bent F with a foot; bar-o-bar-o; M; o-dot-o; V with a circle on each top corner); pass B saw the circle on one corner only for Fiorentini | files compared; sheet not seen |

**What it gives this target.**
- The reading of the bar-o-bar-o sign as *duca* (5 Nov, from one gloss and the contexts) is confirmed by a key sheet, by
  the contributor's record: R5318 has Duca on that sign and Venetiani on another (o-bar-theta-bar).
- *stantie*, *Fiorentini*, *gente d'arme* and *Toscana* of the f. 134 glosses are nomenclator entries of the same sheet,
  and *compagnie* is spelled with its syllables (le, co, m, pa, g).
- For f. 139 R5318 gives values, not a reading: through the crosswalk of `dudout1448/test_1446.py` it values the same
  62.1% of the 778 transcribed signs as the 1448 table; the 301 signs without a value are shapes that the transcription
  of 4-5 Nov did not match to any table (`@NN` labels), and they have to be matched against the sheet's 180 or so entries
  from the image. No word share is claimed: **f. 139 is decoded in part, not read.**
- No held-out measurement of R5318 exists (his statement, and right: f. 30 was spent on the 1448 table, f. 139 has no
  clear text, f. 28 and the glosses are short and were used to build the crosswalk).

## 14 Nov 2026 (night): is the key of Feb 1448 this key? One key in two states; one entry

Brice Dudout's own pre-set rule in PR #625 says "neighbour's key" (previous section: not met as written). His PR #630,
filed a few hours later, says "one family, one key with small changes". Weighed here:

For one key:
1. 54 of 58 shared shapes carry the same value on a sheet that was not learnt from the 1448 letters (42 of 49 with his
   blind labels), and R5318 decodes 0.874 of the valued tokens of f. 28 against 0.126 for the best shuffle.
2. **R5318 on the held-out f. 30** (`r5318/f30_check.py`, written here; a comparison after the fact, f. 30 being spent):
   with his crosswalk R5318 gives a value to 687 of 846 signs (81.2%) and scores 0.598 against the copy f. 29, 0.630 with
   the bar-o-bar-o sign read *Venetiani*; the table learnt on f. 28, a letter three days older, scores 0.650. Shuffles
   stay under 0.25. A sheet in the 1446 state reads the 1448 letter about as well as a table made from its neighbour.
3. **R5318 holds the signs that f. 30 has and the 1448 table lacks.** Seventeen shapes of f. 30 without a 1448 value
   match an R5318 entry by the written shape descriptions alone (his "New shapes" list against his two passes of the
   sheet): among them *Re de Ragona* (an angle with a circle and a dot; six uses on f. 30, and the copy has "Re de
   Ragona/Raghona" six times in those runs), *Fiorini* (a capital R, where the copy has "docento milia fiorini"), *non*
   (the comb, eight uses), and the syllables pe, me, le, lu, su, pu, ga, ge. With these 17 values R5318 scores 0.698
   (0.729 with *Venetiani*) on 751 valued signs, and the 1448 table 0.778 on 727. The matching was done here from the
   descriptions, with the reference text in view, and not on the image of the sheet: it is an indication, not a test.
4. The other differences he lists (na/bo, bi/ri, sa/cc, te/ti on the A) are inside the shape families that his notes
   call hard to separate in this hand; none is shown to be a change of the key.
5. His joining rule failed on *stantie* having no witness in two letters of 1448 and on a score bar taken from another
   language-model order. Neither measures whether the key is the same; R5318 does hold *stantie*.

Against:
- **One nomenclator sign changed.** Bar-o-bar-o is *Duca* on f. 134 (gloss) and on R5318, and *Venetiani* seven times in
  Feb 1448 where the later copies have the word. The Duke, Filippo Maria Visconti, died in August 1447. R5318's own sign
  for Venetiani has not been looked for on ff. 28 and 30.
- The joining rule was his, written before the test, and it was not met. That stays on record as a failed joining test.

**Decision: the same key, in a state of Nov 1446 (R5318, f. 134, f. 139) and a state of Feb 1448 with at least one
nomenclator sign reassigned.** One key, one entry: the 1448 letters stay in this folder (`dudout1448/`, moved from the
`targets/tranchedini1448/dudout/` he proposed, path references updated, his files otherwise as filed) and get no target
of their own. The change of state is recorded, not smoothed over: a reading of 1448 takes bar-o-bar-o as *Venetiani*, a
reading of 1446 as *Duca*. Lead 1317 stays in `research/leads.json` with its reservation for Brice Dudout (verdict
"partly_read": its letters have later clear copies); its note now points here.

Not decided here: the later tables (Lasry 1452, Domnina 1454; `../tranchedini1452/`) also have *Veneziani* on
bar-o-bar-o, so the 1448 state may simply be theirs. Whether `tranchedini1452` is this same key again has not been
tested (R5318 against Lasry's table sign by sign) and is left to the maintainers.

## Remaining gaps

- f. 139: every cipher run (778 signs transcribed, 62.1% with a value through R5318 or the tables, 301 unmatched shapes; decoded in part, not read) - blocker: none outside for a holder of a DECODE login; the unmatched shapes have to be matched against the R5318 sheet on its image (authentication required; seen by Brice Dudout only), then the runs decoded and counted by words
- ff. 28 and 30 of Feb 1448 (`dudout1448/`): the text is known from the later copies ff. 27 and 29; the 191 signs of f. 30 without a 1448 value, and the word signs the copyist left as dashes (two on f. 27, about six on f. 29), are not yet read from R5318 - blocker: none outside; the 17 matches of `r5318/f30_check.py` were made from shape descriptions and need the image of the sheet
- A held-out measurement of R5318: none exists - blocker: none outside; the other letters of lead 1317 (ital. 1584 f. 353; ital. 1585 ff. 35, 71, each with a clear copy or a 15th-century decipherment) are untranscribed and would serve
- R5318 itself: not seen here (DECODE login); heading, pencil date 1451 and shapes by the contributor's record; Cerioni 1970 not checked for a printed copy of the key - blocker: needs a DECODE account or the ASMi original (cart. 1597, no. 176)
- Whether `tranchedini1452` (Lasry's table, 1452) is this key in its later state: not tested - blocker: none outside
- f. 134: seven short runs transcribed sign by sign (texts/f134_signs.md) but only partly aligned to the glosses (span marks approximate) - blocker: none outside
- f. 145 (R7909, Duke's slip, key R5323): not read; belongs to visconti1446 - blocker: none outside (Gallica ital. 1597 canvas 160 holds a 19th-c. copy)

## Escalation

- [x] siblings: the five records of the lead identified; f. 145 moved to visconti1446; f. 135 and f. 147 are clear; f. 133/132/126/162 not on the lead's records
- [x] clear-pages: f. 147 read at the top (dinaro, stantie, Montevarchi: the topic, no wording to match); f. 135 clear news, not matched
- [x] known-keys: Domnina's key and Lasry's table applied to f. 139 (table_test.py, corrected: z 3.9 with the no-space model); cart. 1597 searched on 14 Nov 2026 by Brice Dudout (PR #630): the key sheet DECODE R5318, headed "Nicodemus", is this key by the contributor's record (image behind a DECODE login, not seen here); it values 62.1% of the f. 139 signs as transcribed
- [x] print: web search; no edition found
- [x] key-rebuild: attempted; solvers fail held-out controls (solver.py, solver2.py, heldout.py); content words are nomenclator signs (cribs.py)
- [x] siblings and clear-pages, 14 Nov 2026 (issue #616, PR #625, Brice Dudout): the same envoy's letters of 19 and 22 Feb 1448 (BnF ital. 1585 ff. 28, 30; lead 1317) have later clear copies beside them (ff. 27, 29) with a few word signs left blank; table built on f. 28, held-out f. 30 at 0.650 (partial by his thresholds); the table does not read f. 139 (joining rule not met)
- [ ] retry, open since 14 Nov 2026: match the 301 unmatched f. 139 shapes and the f. 30 shapes against R5318 on its image, decode, count by words; measure R5318 on a fresh letter of lead 1317
- [x] retry (5 Nov): f. 134 transcribed (duca, Fiorentini, compagnie), f. 139 relabelled with them and l (z 4.0, 62% of signs valued); 301 signs open

## For visconti1446 (not edited there)

f. 145 (1 Dec 1446) is DECODE R7909 (mount (59.), pencil 145), not "not on DECODE"; copy this into `../visconti1446/NOTES.md` and its `peer/slips.tsv` row when that target is next worked.
