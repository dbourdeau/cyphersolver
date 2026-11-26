# Siena, Concistoro 2308 nos. 6 and 24: Cristofano's letters to the Signori, key R4755 (c. 1431-38)

Status: read in part (outside solution, verified here). Key recovered ciphertext-only by the solver, then matched
to the filed key DECODE R4755. No. 6 93.4% of its decrypted letters understood as submitted, **95.4% after the 14 Oct key correction (below)**; no. 24 72.7%, and its dorse
(8 run-over lines) is not in the submitted reading.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**. No. 6
reads as continuous Italian with scattered `‹...›` words. **No. 24 is decoded, not read**: runs of letters not
understood in most sentences (and the dorse unread) leave a gist, not sentences. Reading figure 28.6% (no. 6's 1,056
of 3,694 tokens); the 84.2% (decrypted letters understood) is withdrawn as a reading figure.

Split off from `targets/siena1421/` (the whole busta, catalogue 336), where nos. 6 and 24 were listed as one open
system ("nos. 6 + 24, no-key-material"). The transcriptions used below were made there on 24 Sept 2026.


**23 Oct 2026, re-read b35** (`no24_reread_log.md`): no. 24 (R4812) and neighbours R4811, R4813 re-fetched; no
attachment, transcription or decipherment; the images are the same JPEGs the 14 Oct run-by-run pass used. No. 24
stays **decoded, not read** (0.167); blocker illegible.

## Credit

- **Solution: George Lasry**, done with Claude and with the help of ChatGPT Astra; sent to Daniel Bourdeau on
  14 Oct 2026 as a 7-page PDF ("Siena, two ciphered letters to the Signori (Concistoro 2308, nos. 6 and 24)").
  As the PDF tells it, the key was first recovered by cryptanalysis from the ciphertext only (Claude, with the
  help of Astra), and the matching historical key table, DECODE R4755, was then found in the collection (Astra).
- contributor: George Lasry (settled 14 Oct 2026; the PDF itself names no person).
- **Credit as restated in his consolidated report of 17 Oct 2026** (`lasry_report.md`, the report's section on
  nos. 6? and 24, pp. 13-17, verbatim): "Solved ciphertext-only (October 2026) by George Lasry with CTTS built-in
  cryptanalysis, refined by Claude Opus 5.5 and GPT-6 Astra; the filed key R4755 was found to match afterwards."
  The 14 Oct PDF had put the recovery to Claude "with the help of Astra" and the find of R4755 to Astra. The profile,
  page and ledgers now use the report's wording (CTTS's own solver first, the two models refining).
- This project: independent verification on its own transcription (below), the key table as a tsv, the dorse of
  no. 24, the signature of no. 24, the dating check, and the DECODE corrections.

Files: `reading_no06.txt`, `reading_no24.txt` (the submitted reading, verbatim, credited); `key_R4755.tsv` (the
key, read here from the DECODE photograph, with the labels of our transcription); `verify.py` (the check);
`decode_no06.txt`, `decode_no24.txt` (our transcription decoded); `dorse24.py`, `decode_no24_dorse.txt`.

## The documents

| no. | DECODE | images | content | ciphertext (ours, measured) | theirs |
|---|---|---|---|---|---|
| 6 | R4795 (`Concistoro_2308_49`) | P2 text side, 15 lines; P1 verso, show-through and docket | dated 19 February, signed "Cristofano de Mont[...]" | 1,051 signs (`project_attempt/no06.tok` lines) | 1,007 |
| 24 | R4812 (`Concistoro_2308_66`) | P2 text side, 38 lines; P1 dorse: 8 run-over cipher lines + address "Magnifici et potenti signiori e ... Capitano di popolo della citta di Siena" | not dated; signed on the dorse (found here, below) | P2 2,638 signs; P1 dorse 637 (first pass) | 2,559 (P2 only) |

Both open with a clear salutation ("Magnifici et potentes domini domini mei singularissimi ...") and run on in
cipher without word division. Key: R4755 (`Concistoro_2308_10`), fasc. 1, one sheet, heading "Cifra cum
Christofano [M?]tucci(?)"; DECODE's name is "Cifra cum Christoforo Ghinucci[?]". The surname on the sheet is hard
to read; the signature of no. 6, "Cristofano de Mont‹vccia›" in the submitted reading, points to the same name
(Montucci?), not to Ghinucci. Left as a question in the DECODE note, not asserted.

Note against ourselves: `siena1421/NOTES.md` (24 Sept; now `research/siena2308/README.md`) already indexed R4755 as "Cifra cum Christofano ...
(Papa, Fiorentini, Veneziani, Duca di Milano, Niccolò Piccinino, Conte Francesco, Lucca ...)", dated it c. 1440 and
never tried it on nos. 6/24: the fasc. 1 alphabets were compared with the letters "by eye", and this one was missed.

## The key (R4755), checked on the DECODE photograph

The photograph `IMG_R4755_I27827_P.jpg` was fetched with the DECODE cookie on 14 Oct 2026 (git-ignored, ASSi
image); it is the same sheet as the image in the PDF. Read here: 21 letters a-u plus x, z (y has no sign); four
homophones each for a, e, i, o, u, one sign for every other letter (k, h, x included), so 36 cipher signs (k, x,
z and the o-sign "S" do not occur in these letters). Nulls, headed "Nichil importantes": seven signs (ŋ-like, a, f,
B, E, G, h). Word signs: 18 (Papa, Fiorentini, Viniziani, Duca di Milano, Nicholo Piccinino, Conte Francesco,
Luccha, Pisa, Pistoia, Siena, Pontremoli, Parma, Pietrasanta, Genova, Bologna, Messer Thomaso, Cavagli, Fanti).
All of this matches the PDF's description (36 signs for 21 letters, 18 word signs, 7 nulls).

Word signs that occur, by our transcription: CIRC 20 (= Lucca 16 + Piccinino 4: Lucca's ⊙ and Piccinino's
circled D were merged by our transcribers), RX/RX+ (Viniziani), BIGX 1 (Fiorentini), and the Duca di Milano Φ,
which our labels merged with PHI = m. Our transcribers had flagged exactly these point-framed signs as "probable
name codes". So **5 of 18 word signs occur**, as claimed (Lucca 16, Piccinino 4, Duca di Milano 3, Viniziani 2,
Fiorentini 1 in their count; our counts agree for Lucca + Piccinino = 20).

## Verification (14 Oct 2026, `python targets/siena1431/verify.py [--seed-only]`)

Our transcription of nos. 6 and 24 (made 24 Sept by agents A, H, I, before any key; sign legend in
`project_attempt/no06.txt`) was decoded with the key and compared with the submitted reading by a DP
alignment (gap cost 6).

1. **Key read off the sheet by eye only** (31 of our labels given the key value of the sign they look like, no
   fitting; `--seed-only`): our decode equals their letter at 650/941 = **69.1%** of their decrypted letters in
   no. 6 and 1,586/2,286 = **69.4%** in no. 24. LM (it-cinquecento, order 5, no spaces, per char): our decode
   -3.53 / -3.62 against a shuffled-key control of mean -4.77 / -4.77 (best of 20: -4.22 / -4.19).
2. **Labels fitted by EM** (each of our labels takes the value it aligns with most, 6 rounds, seeded from 1):
   751/941 = **79.8%** (no. 6), 1,743/2,286 = **76.2%** (no. 24) with one value per label; **90.5%** and
   **88.2%** when a label our transcribers used for two key signs counts for both. LM -3.06 / -3.34 against a
   control mean -4.03 / -4.04 (best -3.63 / -3.56). Their own reading scores -2.42 / -2.69.
3. Where we disagree, it is our transcription, not their key: our labels merge key signs that differ on the sheet
   - `t` = three key signs: o (+), q (t), f (o+t ligature);
   - `c` = h (c) and n (e-like); `c^` and `e` are both n;
   - `0` = a (o) and, 23 times, i (+o with the cross not seen);
   - `g` = i (ʒ-like) and, 16 times, e; `THETA` = d and, 25 times, o;
   - `d` and `u` are one a-sign (a reversed c with a tail); `VENUS` and `YCROSS` are one e-sign (♀);
   - CIRC = Lucca and Piccinino; PHI = m and Duca di Milano.
   No case found where a key value has to be changed to fit our transcription. The p p pair = e, which our
   notes (24 Sept) had flagged as a unit, is a key sign ("pp" under e on the sheet).
4. No independent re-transcription of their sign inventory was possible (the PDF gives their reading, not their
   transcription); their element counts (1,007 and 2,559) are close to ours (1,051 and 2,638).

Conclusion: the solution holds. The key is the right one, and our own transcription, made blind, decodes
to their letters at 69% with the key read by eye and 88-91% once our merged labels are allowed for.

## Sense share (the read bar)

Counted on their reading (letters inside ‹...› or {...} = decrypted but not understood; word signs count as one):
- **no. 6**: 62 of 941 not understood: **93.4% understood**. Below the 95% bar, but the gaps are scattered
  (‹b·›, ‹teaite›, ‹kanaa·not›, ‹adiertenaa›, ‹nilalado›, the surname ‹vccia›).
- **no. 24 (P2)**: 623 of 2,286 not understood: **72.7% understood**. Many runs: ‹chaaeiisai›, ‹lnifesstt›,
  ‹tromel··aeraomiliaetc·oa›, ‹carpelaelotecednelgnnpei›, ‹vannoafonatificas›, ‹eqnleodiaferraerapeo› ...
  Revised 14 Oct (below): 1,815 of 2,279 = **79.6%** (`reading_no24_rev.txt`).
- **no. 24 dorse (P1)**: not in the submitted reading at all (below).
Both letters: **read in part**.

## No. 24 dorse: decoded here (`dorse24.py`)

The letter runs over onto the back: 8 cipher lines above the address (our first-pass transcription by agent E,
637 tokens, own sign legend, `project_attempt/no24.txt`). Mapped onto the key by sign shape and decoded,
it reads in stretches (LM -3.42 against a shuffled control of -3.96, best -3.63):

- L02 "... cose sono ... segrete ..." (things that are secret)
- L05 "... umilemente mi racoma[ndo] ..." (the closing recommendation)
- L06 "... a la uostra ... Signoria ..."
- L08 "... a uostra ... Signoria. Crist[ofa]no ... si racoman[d]a"

So **no. 24 is signed on its dorse by "Cristofano"**, the same writer as no. 6 ("Cristofano de Mont[...] si
racomanda"); the PDF calls no. 24 unsigned because it did not reach the dorse. The surname letters after
"Crist..." do not come out of the first-pass transcription. Graded C (probable): the forename and the formula are
clear; the rest of the dorse is not yet sense.

## Dating

The PDF dates both letters "about 1431-1432" from the war of Florence against Lucca (1429-33): Piccinino on the
road to Lucca; the King of Hungary (Sigismund in Italy 1431-33); the Council of Basel (1431); the "marquis of
Mantua" (a title "Sigismund created in 1432-1433").

Checked: the marquisate of Mantua was conferred by Sigismund on Gianfrancesco Gonzaga in September 1433, after the
peace of Ferrara (April 1433) that closed that war. No. 24 also says the marquis "è acordato col Duca di Milano"
and names "il ducha Alberto ... re d'Ongnaria". Gonzaga left Venetian service and went over to Filippo Maria
Visconti in 1438; Albert of Austria (Duke Albert V) became King of Hungary in December 1437 and King of the
Romans in 1438; Sigismund died in December 1437 ("lo 'mperadore non verrà" fits either a living emperor who stays
away or the vacancy). Florence attacked Lucca again in 1437-38, with Piccinino on the Milanese side. So **no. 24
fits 1437-38 at least as well as 1431-32**, and the Mantua title argues against a date before September 1433.
No. 6 (19 February; Piccinino's men opening the road to Lucca; Antonio Petrucci's chancellor back from Milan) fits
February 1431 or February 1437/38 (Sienese style 1430 or 1436/37). Recorded as c. 1431-38; the PDF's 1431-32 is
not adopted. This is reasoning from the decrypted content, graded M; the archive does not date either letter.

## No. 6 pushed past 95% (14 Oct 2026)

Two key values were misapplied in both the submitted reading and our check, and are settled on the key sheet R4755:
- **z is the compound "So"** (an S with a small o attached), drawn so in the z column; plain S is o. Our transcription had split it into S + u/0. Seen on the DECODE image of no. 6 in all three places: line 7 "c So d" (aduert-en-z-a), line 11 "s e n So 5 o H pp" (senz-a auere), line 13 "c So 7" (Vincen-z-o). At "bi-S-gnio" (line 7) the S stands alone and is o: *bisognio*.
- **4 = u** (the u column reads 9, H, 4, ϵ); our check had mapped 4 to i.

Readings changed (reading_no06_rev.txt; the submitted reading is kept unchanged in reading_no06.txt):
- "buona ‹adiertenaa›" → "buona **aduertenza**" (*avvertenza*)
- "tornò da Milano [a] Sena ‹aaa›vere" → "tornò da Milano **senza avere** fact[o] **nula** ‹lado›": the chancellor came back from Milan *without having done anything*, not "to Siena"; no editorial insertion needed
- "facti di Vincena{ao} da Camerino" → "facti di **Vincenzo** da Camerino"

Measured with the same rule (verify.py `understood`): 896 of 939 decrypted letters understood = **95.4%** (was 879/941 = 93.4%). Without the *nula* change: 95.0% (the margin is thin). The signature "Montuccia" would add five letters but is not legible enough on the image and is not counted.
No. 6 now meets the read bar; no. 24 stays read in part, so the target as a whole stays read in part.

## No. 24 revised: 72.7% to 79.6% (14 Oct 2026)

The ‹...› runs of the submitted reading were taken one at a time, longest first (`revise24.py`, which writes
`reading_no24_rev.txt`; the submitted reading stays unchanged in `reading_no24.txt`). For each run: the signs of our
transcription aligned with it, the alternative values of our merged labels (t = o/q/f, c = h/n, 0 = a/i,
"t 0" = the i-sign +o, PHI = m/Duca, the So compound = z, 4 = u), the it-cinquecento model with spaces to
segment the candidates, and the DECODE photograph of R4812 (fetched with the cookie, git-ignored; 2248 x 4000,
signs about 20 px) for the doubtful signs.

Measure (verify.py `understood`, same rule as before): submitted 1,663/2,286 = **72.7%**; z/4 corrections only
1,666/2,286 = 72.9%; plus the image-checked runs 1,718/2,284 = 75.2%; plus the runs constrained by context
1,815/2,279 = **79.6%**. 23 changes: 7 image-checked (I), 3 key corrections (Z), 13 constrained by context
and the language model (C). Changes:

| line | submitted | revised | | evidence |
|---|---|---|---|---|
| 7 | n[o]ie ‹vict› sonno | n[o]ie vi sonno | Z | 4 = u (key column); "per le molte noie vi sonno ogni dì" |
| 8 | grann ‹digniacciatie› e | grandi ghiacciatie e | I | c = h (plain c on the image, not the e-like n); +o = i; E, h nulls: "e grandi ghiacciate" (great frosts; a February letter) |
| 8 | gl[i] ‹chamino› le | gl[i] chamino le | C | letters as read; "e gli chamino le convien fare" (the roads he has to take) |
| 8 | ‹easprepensoo› pochi | ‹easpro› penso pochi | C | "penso pochi dì" (I think, in a few days); the first five letters stay open |
| 9 | perché ‹aorlteaposi› cominca a diria ‹aaree› perché | perché e or 'l tenpo si cominca a dirizare; perché | I | So-compound = z (image: S with the small o attached after x); "perché e' or 'l tenpo si cominca a dirizare" (the weather begins to mend) |
| 12 | a{a} Lucca ‹evscet› di Fiorentini | a{a} Lucca e uscit[i] di Fiorentini | C | g = i (key); "ambassadors ... and exiles of the Florentines" (the fuorusciti) |
| 14 | e ‹fanto›, q[u]anto | e fano, q[u]anto | C | t = f, B and a nulls: "e fanno, quanto l'è posibile" |
| 19 | continuo ‹alvrechie›; | continuo a l'vrechie; | C | "io li so continuo a l'orecchie" (I keep at his ear) |
| 28 | ‹dvctdisterli› (duca d'Osterlich?) | duc[a] d'Isterlic (duca d'Osterlich) | C | Albert V of Austria; Osterlich/Isterlich |
| 28 | che è a ‹qacto› re | che è a facto re | C | t = f: "che è [stato] facto re d'Ongnaria" (made King of Hungary, Dec 1437) |
| 24 | uno ‹svvfai›‹iglioatire› a Lucca | uno ‹svv›fa[m]iglio a dire a Lucca | C | "à mandato uno [suo] famiglio a dire a Lucca" (sent a servant to say) |
| 20 | ‹lnpossa› conprendare ‹lvivera› Lucca | le possa conprendare lui verà Lucca | C | "per questa le possa comprendere: lui verrà [a] Lucca" |
| 37 | gar[z]{a}one | gar{a}zone | Z | So-compound = z: "garzone" |
| 2 | ‹prerdom› ‹·› sare' | ‹prerao› Duca di Milano sare' | I | image: the line-end Φ is point-framed (·Φ·), the word sign Duca di Milano, not m: "... il Duca di Milano sare' disposto di soccorrere Lucca" |
| 15 | ‹loachamenaqano› assai | lo a Chamerino; assai | I | image: our "t W" is "+o" (the i-sign); "fanno, quanto l'è posibile, a e cond[urlo] lo a Chamerino", parallel to "di condurlo a Lucca" |
| 6 | sol‹nparqiirdicid› ‹roe› | sol‹n› per quind{g}ci d ‹roe› | C | 4 = u, t = q: "per quindici d[ì]"; the sign after d (η or ʒ) not certain on the image |
| 31 | per lo ‹qnala› soto | per lo q‹n›ale soto | C | "per lo quale sono morti quatordici gente nel camino" |
| 30 | no[n] ‹avinga› [a]dvegna | no[n] avinga [a]dvegna | C | "se questa [gu]era non avinga" (avvenga) |
| 37 | ritorni a q[u]a ‹asalr› per | ritorni a casa ‹l› per | C | d+ = c: "il garzone ritorni a casa per solecitare" |
| 17 | licen[t]ia ‹·epaga·› | licen[t]ia [de'] Viniziani ‹epaga·› | I | image: point-framed ℞ = Viniziani (word sign the reading had dropped) |
| 19 | ‹··› io li so | [a'] Viniziani; io li so | I | image: point-framed ℞ = Viniziani; x THETA = "io" |
| 30 | ‹eqnleodiaferraerapeo› pro‹·›ente | ‹eqnleodi› a Fer‹la›era pe[r] lo pro‹·›ente | I | image: f e r, nulls h F, then l a e r a, p e l o: "a Fer[r]ara pe[r] lo presente" (the Council at Ferrara, Jan. 1438); the -la- stays open |
| 26 | se n'à a {a}fa[r]lo | senza {a}fal{a}[l]o | Z | So-compound = z: "e che senza fallo il marchese di Mantova è acordato col Duca di Milano" |

What the new readings add:
- **Dating.** "il ducha Alberto, duca d'Isterlic, che è a facto re d'Ongnaria" (*made* King of Hungary: Albert of
  Austria, December 1437) and "a Fer[r]ara pe[r] lo presente" (the Council, moved from Basel to Ferrara in January
  1438) put no. 24 in **early 1438**, which the dating section above had argued from the Mantua title.
- **Word signs the reading had dropped.** Two point-framed ℞ = Viniziani (lines 17, 19 of our transcription) and
  the point-framed Φ at the end of line 2 = Duca di Milano: "[il] Duca di Milano sare' disposto di soccorrere Lucca".
- **Camerino.** "fanno, quanto l'è posibile, ... lo a Chamerino": our "t W" is the i-sign +o on the image, so
  ‹loachamenaqano› is "lo a Chamerino", parallel to "di condurlo a Lucca" a line earlier.
- **Weather and roads.** "per le molte noie vi sonno ogni dì e grandi ghiacciate, e gli chamino le convien fare
  ... penso pochi dì ... perché e' or 'l tenpo si cominca a dirizare" (great frosts; the weather begins to mend):
  c = h on the image, and z is the So compound after "diri-".

What stays open (464 letters, 20.4%): ‹carpelaelotecednelgnnpei›, ‹vannoafonatificas›,
‹stanaeecasiscroie›, ‹aeraomiliaetc·oa›, ‹nroaraavtalprq›, ‹adenanfaalag›, ‹escodrovaeto›, ‹ecesacoerta›,
‹dolelbspasa›, ‹piiinnanaai› and some 60 shorter runs. Our transcription decodes them to the same non-words as the
submitted reading; on the image the signs are as transcribed, or the doubtful ones (c/e-like n, ʒ = e or i, η)
cannot be told apart at this resolution. Lines 33-35 (the Petrucci passage) are the worst. Not forced: a run that
does not read stays in ‹...›.

## Remaining gaps

- no. 24 P2, the ‹...› runs left after the 14 Oct revision (464 of 2,279 decrypted letters, 20.4%) - blocker: illegible; checked again 23 Oct 2026 (b35): the DECODE images are the only ones (20-25 px per sign); a sign-level re-check needs the ASSi original
- no. 6, 43 letters in ‹...› (4.6%) after the 14 Oct correction - blocker: illegible; scattered single words, not legible enough at the DECODE resolution
- no. 24 dorse P1 (637 tokens), beyond the closing formula and signature - blocker: illegible; cramped and partly lost at the fold
- the writer's surname (Mont‹vccia›; key heading "[M?]tucci") - blocker: illegible

## Escalation

- [x] siblings: every record of the busta opened in siena1421 (keys R4746-R4789, letters R4790-R4814, R1858); nos. 6 and 24 confirmed as one system; no other letter of the busta is in this key (nos. 14, 18, 25 have their own keys).
- [x] clear-pages: no. 6 P1 (verso, docket only) and no. 24 P1 (dorse, run-over cipher + address) checked; no decipherment on either.
- [x] known-keys: R4755 applied (the solver's match, confirmed here on the DECODE photograph); the other fasc. 1 keys were tried on these letters in siena1421 and do not fit.
- [x] print: Meister 1902 (pp. 50-53, three Sienese keys of the 1430s, other values), the 1952 inventory, Treccani DBI (Petrucci); no printed decipherment of either letter found.
- [x] key-rebuild: the key is complete for every letter sign that occurs (36 signs, 7 nulls); the gaps are not key gaps.
- [x] retry: both letters decoded again from our own blind transcription (verify.py), and the dorse of no. 24 decoded for the first time (dorse24.py); the ‹...› runs stay unread under both transcriptions; 14 Oct: each run of no. 24 retried against the merged-label alternatives and the R4812 image (72.7% to 79.6%).

## The report of 17 Oct 2026 against this entry

George Lasry's consolidated report (`lasry_report.md`) repeats the 14 Oct PDF's reading of both letters and does not
take in this entry's work of 14 Oct. Kept as he wrote it there; this entry's readings and dating stand beside it:

- **Credit**: CTTS built-in cryptanalysis first, refined by Claude Opus 5.5 and GPT-6 Astra; R4755 found afterwards
  (adopted, see Credit above).
- **Dating**: the report keeps "about 1431-1432" (the marquis of Mantua "a title Sigismund created in 1432-1433");
  this entry has c. 1431-38, no. 24 early 1438 ("duca d'Isterlic, che è a facto re d'Ongnaria", "a Fer[r]ara pe[r] lo
  presente", above).
- **No. 24 signed**: the report calls no. 24 "unsigned"; its dorse is signed "Crist[ofa]no ... si racoman[d]a" (above).
- **No. 6 corrections**: the report still reads "tornò da Milano a Sena …vere fact…", "buona … a prese", "Vincena da
  Camerino"; with z = So and 4 = u (14 Oct, on the key sheet) these are "senza avere fact[o] nula", "buona
  aduertenza", "Vincenzo da Camerino" (95.4% understood).
- **Counts**: the report has about 1,000 (no. 6) and 2,560 (no. 24) elements, 3,570 in all; ours 1,051 and 2,638, plus
  637 on the dorse of no. 24.
- **Piece number**: the report writes "No. 6?" (the pencil number is doubtful there); here "no. 6".

## Questions for George

1. The report credits CTTS's built-in cryptanalysis, refined by Claude Opus 5.5 and GPT-6 Astra; the 14 Oct PDF said
   Claude "with the help of" Astra, and that Astra found R4755. Which tool gave the first working key, and who found
   R4755? The profile now follows the report.
2. Dating: would you accept early 1438 for no. 24 (Albert "facto re d'Ongnaria", Dec 1437; the Council "a Ferrara",
   Jan 1438; Mantua's marquisate dates from Sept 1433), or do you keep 1431-1432?
3. The dorse of no. 24 (8 run-over cipher lines) closes "Crist[ofa]no ... si racoman[d]a": do you read it too?
4. Why "No. 6?": is the pencil number on R4795 unclear on your image?

## 24 Nov 2026 - no. 24: the merged "t" sign, blind sheet (Brice Dudout, with Claude), `dudout/sign_check_2411a/`
Our transcription uses one label "t" for three signs of R4755: + (o), the footed t (q) and the o+t ligature (f).
Brice Dudout read 12 places of R4812 P2 blind (9 targets, 3 controls, 3/3). The hand keeps the forms apart:
- 5 plain + (o);
- 3 "+o" (the key's i-sign, a cross with a round on its right arm), one of them {probable};
- 1 cross with two dots, a form not on the key sheet, with no value.

The places fall on letters already read or inside runs that stay unread. So the understood letters stay at 1,815 of
2,279 (79.6%) and no word changes. A relabelled copy of the transcription and reading is in the folder. Next: a pass
over the 162 "t" places, starting inside the unread runs.

## 24 Nov 2026 - no. 24: the merged "c" label, blind sheet (Brice Dudout, with Claude), `dudout/sign_check_2411b/`
Our transcription uses one label "c" (and partly "e") for two signs of R4755: the plain open c (h) and the c with a
tongue (n). Brice Dudout read 11 places of R4812 P2 blind (8 targets, 3 controls, 3/3). He asked whether the two are
one form; both merges break sure words (all n: 26, all h: 100), and the image keeps them apart, so two signs are kept.
3 plain c (one gives "par che", one falls in an unread run, one would give "vegho": "vegno" kept, its n now probable)
and 5 tongued c on letters already read. Understood letters stay at 1,815 of 2,279 (79.6%); no word changes.
