# Malsburg 1637: Otto von der Malsburg's cipher letters to Landgrave Wilhelm V (HStAM 4 h Nr. 1411)

Status: in progress (was: read in part (Daniel Bourdeau's numerical cipher: 95.9% of 9,736 cipher tokens; Larry Beck with ChatGPT: separate alphabetic key recovered, substantial German recovered with source and editorial uncertainties; code referents open))

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: ff. 12-13, 18,
23-24, 25 and the alphabetic block (German sentences, codes as name holes). **Decoded, not read**: ff. 3, 14, 15-17,
28-29 (and the duplicate 30-31), 32-33: open codes, bracketed letters or noise in most sentences. 95.9% (tokens in
dictionary words) is withdrawn as a reading figure; 43.6% of the tokens are in documents that read (4,468 of 10,246).

22 Oct 2026, re-read (REREAD_BRIEF, batch b08, `HCP496-509_reread_log.md`): the five unread records re-read on the
HCPortal scans, readings and English in `HCP496/502/503/507/509_reading.md`, `_en.md`. **f. 3 (HCPortal 496) now reads**
(clean share 0.667, B): the garrisons' upkeep, the end of the contributions, the safe-conduct for envoys to Cologne.
ff. 14, 15-16 and 28-29 (with the duplicate 30-31 as control copy, `HCP507_corrections.tsv`) build German sentences around
the codes but stay decoded, not read (0.167, 0.375, 0.437): two to six open codes or signs in most sentences. ff. 32-33:
the French letter of "232" transcribed from the scan and read (0.77 as French); the German extracts in the second hand
not re-transcribed, so the record stays decoded, not read (0.545 overall). Key unchanged; the crossed H (ll and tt) and
the lone 7 (st, ö, b) have no single value and are left open. fraction_read 0.436 -> 0.480 (4,923 of 10,246).

The numerical-cipher result below is Bourdeau's work. The contribution integrated on 2 October 2026 concerns
the separate ten-line alphabetic block of 7/17 January 1637. Its repeating shifts are **4, 5, 3, 6, 2** over
**abcdefghiklmnopqrstuwxyz**. The literal output, proposed German reading and translation are kept separate in
`alphabetic/`. No percentage of coherent alphabetic plaintext has been measured; 95.9% remains a numerical-cipher
measure, not a combined result. The referents of 43, 45 and the angular pair labelled LL remain unidentified.

- **Record.** Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411, "Korrespondenz in Chiffren mit dem
  Generalkommissar Otto v.d. Malsburg betr. Kriegführung in Münster und Westfalen", ff. 3-33. HCPortal cryptograms
  496, 497, 502-509 (all "Not solved" on HCPortal). Catalogue entry 338.
- **Images.** 18 HCPortal originals (ff. 3, 4, 12-18, 23-25, 28-33), fetched by `fetch_images.py` into `img/`
  (git-ignored), with the HCPortal record JSON.
- **What it is.** Letters from Otto von der Malsburg, Hesse-Kassel's General Commissary, to Landgrave Wilhelm V at
  Kassel ("Durchleuchtiger Hochgeborner Gnädiger Fürst und Herr"), January to March 1637, mostly from Wesel. Each is
  a clear letter with long cipher runs, and several are almost wholly cipher.

| folio | HCPortal | date | what |
|---|---|---|---|
| 3 (4 = address) | 496 | 5/15 Jan 1637 | signed Otto von der Malsburg; two cipher blocks |
| 12 (13 = address) | 497 | Wesel, 7/17 Jan 1637 | three cipher blocks, and a separate letter-cipher block (see below) |
| 14 | 502 | Jan 1637 | four cipher blocks |
| 15 | 503 | Jan 1637 | "Triplicat", one block |
| 16 (17 = address) | 503 | 30 Jan 1637 (HCPortal date) | two blocks; a clear list of officers on the right leaf |
| 18 | 504 | 14/24 Feb 1637 | subscribed "E. F. G. Dr:", Malsburg's hand |
| 23-24 | 505 | 7/17 Feb 1637 | signed "Otto von der Malsburgk"; nearly all cipher |
| 25 | 506 | 5 Mar / 23 Feb 1637 | signed |
| 28-29 | 507 | 28 Mar 1637 (old style) | nearly all cipher |
| 30-31 | 508 | the same | "Duplicat" of ff. 28-29; used as a check copy, not counted |
| 32-33 | 509 | 3 Apr 1637 and Mar 1637 | a French letter signed "232", and German news extracts in a second hand, both with cipher runs in the same key |

## The numerical system (Bourdeau)

A German homophonic substitution written in two-digit groups (10-99, dots between), with letter signs for
common digraphs and a small code of three-digit groups for names and military nouns.

- **Two-digit table** (`key.txt`): 89 groups, 2-7 homophones per letter (e 7, u 7, a 6, o 6, n 5, i 5, t 5 ...).
  No regular pattern (unlike the Sixtinus key of Dec 1635, HCPortal key 5, which has the same layout).
- **Letter signs**: N, D = ch; Y, G = ei; Z, O = st; W, P = ss; L, A = tt; R, C, E, M = mm; X, j, J = sch; H, H# = ll;
  S, F, F# = au; T, B = ff. Single figures are plain numerals ("5 [tausend] reichsthaler").
- **Codes** (`codes.txt`): about 45 three-digit groups (115-269), 151 tokens. Five inferred from context: 128 Cöln,
  130 Hamburg, 188 die Staaten, 273 Compagnien, 253 Regiment. The rest are open. A few more signs (V triangle,
  K, Q, f, m, 4#, +, XX) behave as codes and are open.

## Verify first: the Hesse-Kassel key sheets

- HCPortal holds 176 key records for the Marburg key volumes (`research/catalogue_harvest/hcportal/keys/`, index
  `keys_index.txt`, harvested 28 Sept 2026 through `api/cipher-keys/<id>`), each with its named users. None is
  Malsburg's key. Key 31's name list gives "Otto v. der Malßburg - 523", so he appears in other keys only as a name code.
- Key 5 (Sixtinus, Dec 1635) and key 30 ("1637 or before") are the same family: a two-digit homophonic table,
  letter signs and codes from 111. Key 5's addenda share several code numbers with Malsburg's (193, 201, 210, 212),
  but its table does not decode f. 3. Keys 38 and 49 do not fit either.

## Numerical-cipher method (Bourdeau)

1. Transcription: f. 3 by hand from 2x line crops (`lines.py`, `crop.py`); the other pages by two transcription
   agents in the same format (`f0NN.txt`). The duplicate (ff. 30-31) was used to correct ff. 28-29.
2. Homophonic annealing (`solve.py`, lang `de-1640s`, order 5, no spaces, letter signs and codes as breaks, a
   letter-frequency penalty): f. 3 alone (455 groups) gave noise; ff. 3+12+18 (1,575 groups in the first transcription; 1,806 in the current one) converged in all four
   restarts on the same key and German text ("das ich auch noch nit weiss ... die garnisonen ... die contributiones
   vom platten lande").
3. Letter signs read from context (noch, möglich = N; lassen = W; geschlossen = X; Statthalter Nesselrode = L, P;
   Stettin = A), then fixed in the solver; the digit table re-annealed and polished over all pages.
4. Reading measure (`measure.py`): each cipher run decoded and segmented into words from the DTA 1470-1670
   vocabulary plus `extra.txt` (names and spellings confirmed in context). A shuffled-key control scores 50-58%.
5. Re-check of the unread spots against the scans (`unread.py`, `work/unread_spots.tsv`, `work/recheck_log.tsv`).

## The letter-cipher block on f. 12

At the foot of digital image 0012, after "... Churf. in Beyern salvo geschehen werden;", ten lines are written
in lower-case letters with 43, 45 and two angular signs labelled LL. The repository's `f012`/"f. 12" identifies
the digital image, not a verified manuscript foliation. The annotation is tentatively read **[E?]: Sixt: / cla:**;
its exact reading, expansion and attribution are unresolved. It is not evidence by itself for "ex Sixtini clave",
a particular Sixtinus, or the author of the appended intelligence.

Bourdeau's earlier attempts included monoalphabetic and homophonic annealing in German, Latin, French, Italian
and Dutch; homophonic models with nulls; periodic IC for periods 1-15 (0.050-0.060); Caesar shifts; the MORITZ
reciprocal alphabet (key 105); and the Reuschenberg alphabet (key 2). Those attempts did not produce the current
reading. The subsequent repeating-shift result supersedes the earlier suggestion that the passage was not periodic.

### Contribution and provenance

Larry Beck directed the subsequent alphabetic investigation with ChatGPT, using Bourdeau's provisional
transcription and the authentic HCPortal image. ChatGPT performed the computational work, separate image-reading
passes and drafting. "Independent" image readings here mean separate model passes, including passes without
the proposed plaintext; they are **not** review by an independent human paleographer. The exact discovery date,
complete model-ID history and number of contributor sessions are not established by the supplied record and are
not reconstructed here. The dated steps in `profile.json` record this contribution's integration and reproduction
on 2 October 2026, not an invented discovery chronology. It must not be treated as a continuation of Bourdeau's
original Claude session for model-performance analysis.

Source: HStAM 4 h Nr. 1411, digital image 0012, HCPortal cryptogram 497,
[authentic 2834 x 4284 image](https://api.hcportal.eu/media/1395/79511677516420.jpg).
No generated detail was used. The numerical decipherment and source presentation remain credited to Bourdeau.

### Alphabetic mechanism and counting

Use `a=0` through `z=23` in `abcdefghiklmnopqrstuwxyz`; encrypt by adding and decrypt by subtracting
`[4,5,3,6,2]` modulo 24. The first ordinary letter uses shift 4 (phase 0). Phase continues across all ten
manuscript lines. Normalize `ü` to `u`, `ÿ` to `y` and provisional `j` to `i`. Isolated 43, 45 and LL labels,
punctuation and the blot label are outside the alphabetic stream and advance it by zero in the selected model.
This is a constraint modulo five, not a recovered expansion length or code meaning.

The legacy command `python docs/_check_profile.py --measure targets/malsburg1637/ct/hcp497_letters.txt --letters`
counts 531 alphabetic characters, including the four `L` characters of the two editorial `LL` labels and the
four letters of the editorial `[blot]` label. Excluding those labels leaves **523** normalized cipher positions.
The selected image-reading branch has **510**. The legacy file is preserved unchanged. The 33-run alignment
accounts for 15 one-letter deletions, one insertion, one length-increasing `u` to `ii` replacement and 16
substitutions, a net reduction of 13. This is an alignment of transcripts, not a unique history of scribal errors.

The inherited reports record a search of all 7,962,624 five-position keys on the unchanged opening 112 letters,
with a frozen four-letter language model, yielding the same best key and top ten on replay. They also record
25 original and 99 addendum verifier checks and 125 consistent special-group advancement tests. Those historical
search claims must be distinguished from the lightweight public verifier's actual scope: it reproduces the
preserved original and selected inputs, phases, literal outputs and defined source alternatives. Re-encryption
checks consistency only; it cannot authenticate a manuscript reading.

### Reading and its limits

The complete ten-line edition is `alphabetic/alphabetic_edition.csv`; `alphabetic/alphabetic_reading.md` explains
the editorial layers. The selected literal begins:

> der.[43].stehetitzoaufmsprungewollen.[45].seinergernlosseinundihn
> entbehrenkonnensoistesnunzeitdas.[LL]schreibenweilsiesehendaserm

The paragraph discusses a possible departure, disagreement with Swedish generals over command, reciprocal
joining of forces, actions associated with LL that no longer please the central figure, and the authority he
seeks. The opening `wollen ... so` is read conditionally. It does not establish that anyone actually wanted him
dismissed. The material after `das [LL] schreiben` may state proposed letter contents, so later clauses must not
be turned into completed decisions. French service, payment, arrears, resignation and formal discharge are not
established by this January paragraph. `contentiren lassen` is translated as having him given satisfaction.

The source branch retains `wurden` after singular `er`, malformed `tqouppen` and `itzigdn`, and the blot. Editorial
`[Trouppen?]` and `[itzigen?]` are conjectures. At L4:37 (global 212), source `w`, phase 1, shift 5 yields `q`;
`trouppen` would require source `x` or an isolated shift 4. At L9:42 (global 473), source `g`, phase 2, shift 3
yields `d`; `itzigen` would require `h` or an isolated shift 2. Changing the whole key to `[4,4,2,6,2]` alters 202
other positions and damages secure words. The local-error proposals do not justify changing the cipher inputs.

Six binary source choices define a bounded 64-branch test: L3 h/u, L6 g/q, L7 overlap count 0/1, L8 y/iy, L8 n/r
and L9 m/n. Sixteen branches have 510 letters, 32 have 511 and 16 have 512. `schwedischengeneralen` and
`descommendohalber` survive all 64; `oglichkeitcontentirenlassen` survives 16. These anchors had already been
consulted, so this is sensitivity analysis, not independent prediction. L7 h/? and L10 t/? remain provisional;
the blot's unknown extent is not exhausted by these branches. No numerical confidence follows from the counts.

### Code referents and specific documentary leads

There are three unresolved labels in five occurrences: 43 once, 45 twice, LL twice. Graphic comparison favors
43, but no identity follows. LL names two angular signs without establishing Latin letters, initials, 11 or 44.
The labels need not be personal names or three different people; 45 and LL could encode different expressions
for the same party. Malsburg need not be the author or speaker of copied intelligence.

The strongest historical lead is Franz von Geyso, *Beiträge zur Politik und Kriegführung Hessens*, Dritter Teil,
ZHG 55 (1926), [p. 99 n. 2](https://www.vhghessen.de/inhalt/zhg/zhg_55/Geyso_Beitraege.pdf). Geyso says Melander,
through Malsburg, sought absolute authority from the Landgrave, citing **Malsburg, Wesel, 16 November 1636,
Kr. A. 1636, III**. This is a secondary paraphrase, not a quotation from the uninspected original. Internal
disciplinary authority need not be the same issue as command alongside Swedish generals. Melander is a candidate
for documentary investigation, not the decipherment of 43.

Geyso pp. 115-117 and Wilhelm Hofmann, *Peter Melander, Reichsgraf zu Holzappel* (1882),
[pp. 68-69](https://archive.org/details/petermelanderre00schagoog/page/n74/mode/2up), report or print offers to retain
Melander with command and office. Geyso dates the associated letters to 16 and 18 January 1637 and warns that
Hofmann's text differs from the originals. This weighs against a completed-dismissal account; it neither proves
nor disproves the conditional reading. The original January letters have not been inspected.

The specific missing comparisons are:

- [LHA Koblenz, Bestand 47, Nr. 4400](https://apertus.rlp.de/index.php?PLINK=1&ID=d5c14d42-f356-4ff4-8509-b39dc6dbbcbe):
  catalogue entry for cipher codes, 1635-1641, among Melander's papers. Sheets uninspected. A match needs dated users
  and several independent code correspondences, not merely matching 43 or 45.
- Malsburg's 16 November 1636 letter cited by Geyso: current shelfmark/folio unresolved.
  [HStAM 4 h 2208, Bd. 5/2](https://arcinsys.hessen.de/arcinsys/detailAction.action?detailid=v2343475), July-December
  1636, is a catalogue lead for Malsburg/Melander correspondence, not a proved concordance to Kr. A. 1636, III.
- [HStAM 4 h 2209, Bd. 6/1](https://arcinsys.hessen.de/arcinsys/detailAction.action?detailid=v1018318), January-March
  1637, fits Geyso's volume/date reference T. VI, P. 1, but the individual letters are not located. LHA Koblenz
  47/15947 is another catalogue lead for 1637 Wilhelm and Malsburg letters.
- [HStAM 4 f Staaten F, Frankreich 1297](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails?archivalDescriptionId=2045812)
  holds Hoff reports, 1636-1637. The March extract with the second LL-like sign ends with literal `hoffuo[156]`.
  A Hoff report of 17/27 March 1637, if present, could test attribution. The attribution, suffix and transfer of
  the sign's meaning to January remain unproved.

Keys 5, 30 and 31 in HStAM 4 d 1218 Teil 1 were compared. Key 30 has alphabetic 43=P and 45=W, with separate
three-digit codes for Melander and Wilhelm; this does not license Peter/Wilhelm identifications. Key 31 includes
Melander 200/500, Sixtinus 521 and Malsburg 523, without a demonstrated match to this paragraph. Key 5 names both
Wilhelm Burckhard and Nicolaus Sixtinus, so `Sixt:` cannot select one. The February French-service passage and
March Wartenberg/discharge passage have later dates and unresolved antecedents; they do not identify January's
figures. The March duplicate is a transcription control, not an independent report.

## Reading (summary; the measured text is `reading_segmented.txt`)

Spelling as the cipher gives it (u/v, i/j merged); [..] = unread; codes in <>.

- **f. 3, 5/15 Jan 1637.** "... das ich auch noch nit weiss, wo hervor unsere garnisonen hiernechst der unterhalt ...
  genommen werden soll, da die contributiones vom platten lande sowol alhier als in <239> ein ende haben; und wirt man
  nunmehr alle monat auf [..] man <193> ... zwolf viertel casselische viertel, weil die unterofficirer duppelt commis
  bekommen." Then: "es ist noch zeit, das man sich beim konig von Ungern ... [wegen] der friedenstractaten und salvum
  conductum vor die gesanten nach <128 Cöln> sollicitire; <176> wirt one <140> nit anfangen zu tractiren."
- **f. 12, Wesel 7/17 Jan.** He does not know whether to go to <148> or to the army; the recruits and Dalwig's
  Verehrungsgelder; Eberstein's <253 Regiment>; travel "durch Friesslant mit wagen und pferden zu gehen ist
  unmöglich". "Es ist von guter hant avisiret, dass man zu Regenspurg geschlossen, [den] gesanten nach <128> keinen
  salvum conductum zu erteilen"; Statthalter Nesselrode reports that the Bishop of Würzburg wrote in August; the
  Roman King; talks "apart zu <130 Hamburg> oder Lübeck".
- **f. 14, Jan.** Hermannstein (Ehrenbreitstein) and its provisioning; Obrist Hoffman's troops; marches by Marburg,
  Corbach, Brilon, the "rechte strasse von <128> auf <189>"; Jan de Werth at Cologne (clear).
- **ff. 15-16, Jan.** No audience yet; notice of the end of the Stillstand; companies and dragoons, recruiting
  patents already issued; the ambassador of <188 die Staaten>; money and horses; no chance yet to come to <129>.
- **f. 18, 14/24 Feb.** "Es seint aber die <212> ein teils so erfroren, das auch etliche zu kruppeln worden";
  the obligation over the loss before Hermannstein; the new recruiters.
- **ff. 23-24, 7/17 Feb.** The dispute over whether Hermannstein was "effectivement proviandiret"; ransom and
  "Verehrungen" for the commanders; Reichsthaler owed "auf rechnung"; "befinden nun in der that, das wir mit einem
  Frantzosen gehandelt haben"; peace talks in Picardy, nobody sent to <128>; Marggraf Sigmund of Brandenburg's
  commission; a separate peace with the imperial commissioners; "unsere garnisonen seint also verderbet".
- **f. 25, 5 Mar / 23 Feb.** <120> has resolved to content the Reuter; ransom for prisoners; letters of exchange.
- **ff. 28-29, 28 Mar.** The journey by the Watten; twelve-pound cannon and constables; Jan de Werth between Ruhr
  and <268>; the States' alliance and a muster place in Cleves; the conjunction at Cloppenburg, Quakenbrück,
  Minden, Vechta, Wildeshausen, Diepholz; the obristen Uffeln and Carpf.
- **ff. 32-33.** A French letter signed "232", 3 Apr 1637 ("par la lettre de n[ost]re ambassadeur extraordinaire ...
  à Londres ... copie"; "audict ambassadeur"; "ledict Sengell"), and German news extracts from London of 16/26 Mar
  ("<129> der Pfalz der nechst", "Printz Robert"), in the same key; paired large capitals (AA, GG, OO, XX, CC, KK)
  are name signs.

## Measurement

`measure.py` segments each decoded run into words from the DTA 1470-1670 vocabulary (forms seen at least twice,
three letters or more, plus a short list of real two-letter words) and `extra.txt` (names, spellings and French
words, each checked in context); for f. 32 the French `fr-henri4` vocabulary is added. A token is read when every
letter it gives lies in a word. Result (duplicate ff. 30-31 left out): **9,338 of 9,736 cipher tokens (95.9%)**;
193 tokens are open codes or name signs, so 97.9% of the non-code text reads. Per record: 496 96.5%, 497 96.9%,
502 92.8%, 503 95.0%, 504 96.9%, 505 97.6%, 506 97.5%, 507 96.0%, 509 88.1% (second hands). Shuffled-key control:
50-58%. The f. 12 letter block is not counted: it is another system. Its legacy raw count of 531 includes
editorial labels; the normalized inherited input has 523 positions and the selected source branch 510.
The alphabetic contribution does not change Bourdeau's numerical-cipher numerator or denominator. No combined
fraction or measured coherent fraction is claimed.

## 23 Oct 2026: verification 3 (explicit-hole score): 497, 504, 505, 506 demoted

The four letters kept read by the 22 Oct audit (ff. 12-13, 18, 23-24, 25) have no reading file: their text is the
machine segmentation in `reading_segmented.txt` (dictionary word division with breaks such as "nich twi eichen weg an
stellens och", bracketed letters, <nnn> codes). Scored block by block: f012-f013 0.0, f018 0.5, f023-f024 0.5, f025
0.286 explicit-hole (hole rate 0.21-0.32). They are now decoded, not read; the next step is the b08 method on the
scans (sentence by sentence, breaks checked on the image), which for the five sibling letters lifted only f. 3 over
the bar. fraction_read 0.480 -> 0.094 (f. 3 and the alphabetic block, 965 of 10,246 tokens).

## 23 Oct 2026 (r2b): 497 and 506 re-read and read; 504, 505 decoded, not read; sibling spelling restored

Batch r2b (`HCP497-506_reread_log.md`). **Spelling:** the b08 normalisation of the sibling readings (alhir -> alhier,
hette -> hätte, Feint -> Feind ...) is undone: `research/reading_audit/r2b_mals_denorm.py` walks each reading against its
decode stream and puts back the writer's form the figures give (496 10 words, 502 10, 503 11, 507 87, 509 none). The
explicit-hole scores do not move; 496 stays read (0.667). **Re-read:** the HCPortal scans 0012, 0018, 0023-0025 fetched
to the scratchpad; HCPortal 497, 504, 505, 506 read sentence by sentence from the b08_dec decode (key.txt unchanged), the
breaks checked on full-resolution crops (f. 25 l. 15: a struck 40 and 42 for "12?", `HCP506_corrections.tsv`; f. 18
"Reiterei noch"; f. 24 "mit de[m] Reiderlant"), aligned word by word with `b08_align.py`, slips bracketed; readings and
English `HCP497/504/505/506_reading.md`, `_en.md`. `v2_score.py` explicit holes: **497 0.632 and 506 0.625: read (B)**;
504 0.562 and 505 0.545 stay decoded, not read (open codes and signs in most sentences). fraction_read 0.094 -> 0.221
(496 + alphabetic block + 497 + 506 = 2,269 of 10,246 tokens).

Note for a later pass: on the German explicit-hole measure HCP507 (ff. 28-29) scores 0.662 and HCP509 0.659; the b08
decisions used the plain share (0.437, 0.545). 507 may now clear the bar on a reader's review; 509's German extracts
are still not re-transcribed.

## 23 Oct 2026 (r2k): 507 read; 509's German extracts transcribed, 509 still decoded, not read

Batch r2k (`HCP507-509_reread_log.md`). **HCPortal 507 (ff. 28-29):** reviewed as a reader on the decode, the
writer's duplicate ff. 30-31 and scan 0028 (l. 33 spot check: "i AU wartenberg" is in the figures); one more word
re-spelt from the figures ("nitt", `r2b_mals_denorm.py`). The sentences hold; `v2_score.py` explicit holes 0.662
(47/71; plain 0.38): **read (B)**. **HCPortal 509 (ff. 32-33):** the German news extracts in the second hand (three
pieces: from London 16/26 Mar, 5 Apr / 26 Mar and 17/27 Mar 1637, and a Paris note) transcribed line by line on 2-3x
crops of scans 0032-0033 and set around the decoded runs (`HCP509_reading.md`, `_en.md`; the line transcription is in
the log): Parma's neutrality and Sabbioneta, the English East India company and the Palatine manifesto, La Valette on
the Moselle, the Anglo-French league and Saint-Chaumont, Rohan's victory, Colonel Rosen. Score: whole body 0.667
explicit holes, but the German extracts alone 0.50 (24/48): the record stays **decoded, not read**; its blockers are
now the unvalued codes and signs (no-key-material) and about 30 words of the fast hand (illegible), no longer
not-attempted. fraction_read 0.221 -> 0.530 (5,434 of 10,246 tokens).

## Remaining gaps
- HCPortal 504 (f. 18) and 505 (ff. 23-24): decoded, not read after the 23 Oct 2026 re-read on the scans (explicit holes 0.562, 0.545; HCP504/505_reading.md) - blocker: no-key-material; the sentences build, but open codes (504: 212, 122, 120, 123, 148, 260; 505: thirteen) and signs stand in most of them. HCPortal 497 and 506 closed 23 Oct 2026: read (0.632, 0.625)
- ff. 14, 15-16 decoded, not read after the 22 Oct 2026 re-read (clean share 0.167, 0.375; readings HCP502/503_reading.md) - blocker: no-key-material; the sentences build, but two to six open codes or signs stand in most of them; f. 14 also torn at the right edge. ff. 28-29 (HCPortal 507) closed 23 Oct 2026 (r2k): read, 0.662 explicit holes
- ff. 32-33 (HCPortal 509), German news extracts: codes and signs 248, 129, 155, 148, 133, 126, 115, 123, 156, OO, AA, XX, square, GG, CC, KK, LL, V - blocker: no-key-material; clear text transcribed 23 Oct 2026 (r2k), extracts 0.50 explicit holes (record 0.667 with the French letter, kept decoded, not read); the codes and signs stand in nearly every cipher-bearing sentence, occur once or twice and are not in key.txt
- ff. 32-33 (HCPortal 509): about 30 words of the fast second hand in the extracts - blocker: illegible; unread or doubtful at 2-3x on the HCPortal scans 0032-0033
- about 40 three-digit codes and name signs (193 tokens: 120, 122, 129, 140, 148, 176, 193, 212 ... V, K, f, 4#, +, AA, GG ...) - blocker: no-key-material; mostly single occurrences, five valued from context (128, 130, 188, 253, 273, grade I)
- alphabetic 43, 45 and LL (three labels, five tokens) - blocker: no-key-material; no primary key equation or named parallel, and no demonstrated shared nomenclature with the numerical system; LHA Koblenz 47/4400 remains uninspected
- alphabetic source alternatives in lines 3, 6, 7, 8, 9 and 10, plus the blot - blocker: illegible; selected 510-position branch and bounded alternatives retained; a human comparison with the original or better authentic imaging is needed to decide ambiguous strokes and the blot's extent
- alphabetic residual forms tqouppen, itzigdn and er ... wurden - blocker: no-key-material; the alphabetic mechanism is recovered, but no independent primary parallel or fair copy has been located to establish the intended forms; literal output and conjectures remain separate, and physical access has not been shown necessary
- exact reading of the annotation - blocker: illegible; [E?]: Sixt: / cla: remains tentative; a clearer authentic image or comparison with the same hand is needed before expanding it
- provenance of the appended intelligence - blocker: no-key-material; no contemporary source attribution or matching named parallel established; a possible Hoff comparison and original correspondence remain uninspected, without a claim that they require physical access

## Escalation
- [x] siblings: all ten records of HStAM 4 h 1411 transcribed; ff. 30-31 duplicate ff. 28-29 and served as a check copy
- [x] clear-pages: no decipherment on any leaf; the address sides (ff. 4, 13, 17) carry no cipher
- [x] known-keys: all 176 HCPortal key records of the Marburg key volumes harvested; keys 5, 30, 38, 49 tried on the digits and 2, 105 on the letter block; none fits
- [x] print: web and LAGIS search for an edition of the letters; none found
- [x] key-rebuild: digit table annealed from the ciphertext and polished over all pages; signs and five codes valued from context
- [x] retry: 236 unread groups re-checked against the scans (24 misreads, 2 doubled groups corrected, 210 confirmed)
- [x] retry (23 Oct 2026, r2k): 507 reviewed as a reader on decode, duplicate and scan, read (0.662); 509 German extracts transcribed on the scans, still decoded, not read (extracts 0.50)
- [x] retry (23 Oct 2026, r2b): 497, 504, 505, 506 re-read sentence by sentence on the HCPortal scans; 497 and 506 now read; the b08 spelling normalisation undone in the sibling readings
- [x] retry (22 Oct 2026, b08): the five unread records re-read sentence by sentence on the HCPortal scans; ff. 28-29 against the duplicate ff. 30-31 (9 readings taken from it); f. 32 one label corrected and the French letter transcribed; f. 3 now reads

Alphabetic contribution, integrated 2 October 2026:

- [x] siblings: 18 related leaf transcriptions compared, including the February letter, March duplicate and
  second LL-like occurrence; ordinary numerical 43/45 are letter values and cannot be transferred as name codes
- [x] clear-pages: address image 0013 and appended-intelligence context considered; no matching deciphered copy
  of the alphabetic paragraph established, and the annotation does not by itself assign authorship
- [x] known-keys: Sixtinus-family sheets 0040-0042, 0121-0122 and 0123-0126 compared; no matching nomenclature
  established; the newly located Koblenz 47/4400 catalogue entry has no inspected sheets
- [x] print: the contributor's prior Grotius/Anhalt searches and the Geyso/Hofmann and Oxenstierna comparisons
  produced contextual parallels and specific missing documents, but no named version of this paragraph
- [x] key-rebuild: the five shifts reproduce the inherited and selected literals; separate source and editorial
  layers prevent fitting the ciphertext to a candidate identity
- [x] retry: source alternatives combined in the bounded 64-branch audit; local residuals tested against phase
  changes and a global replacement key, without accepting conjectural plaintext as a source reading
