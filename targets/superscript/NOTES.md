# 1520s superscript-digit ciphers (Worcester 1526/1527/1529, Gilino 1527, Garbino 1528) — tracker item #13

Status: read (9 Oct 2026). R8613, the "undeciphered" Worcester duplicate of 22 July 1527 (Ghinucci to Wolsey), deciphered to 97.9% (797 of 814 tokens) with a key recovered from the three sibling letters' contemporary decipherments (R8476, R8589, R8590, all in print); Gilino R8572 (to Francesco II Sforza, 15 Sept 1527) deciphered to 96.1% with the Sforza key DECODE R5258. Garbino belongs to catalogue entry 7 (vasto1527), not this target. Written up as docs/superscript.html.

## 9 Oct 2026: access restored, identifications

All DECODE images fetched full size with the cookie (`img/`, git-ignored). The DECODE records carry no DOC
transcriptions. Tomokiyo's table (`img/henryviii_worcester.png`, cryptiana henryviii.htm) fetched.

Letters and Papers iv (BHO, fetched 9 Oct 2026; L&P cites the OLD Cotton foliation, DECODE the new):

| DECODE | new f. | old f. | L&P iv | date, sender | what L&P says |
|---|---|---|---|---|---|
| R8476 | Vesp. C III 304 | 303 | 2727 | Ghinucci to Wolsey, Poissy, 24 Dec 1526 | "Hol., Lat., part cipher, pp. 6"; printed St. P. VI 552; "2. Decipher of part of the above [R.O.], commencing 'Dominatio v. R. vidit modum' and ending 'effectum facere non posse'" |
| R8589 | Vesp. C IV 313 | 291 | 5282 | Ghinucci to Wolsey, Valladolid, 12 Feb 1529 | "Hol., part cipher"; L&P PRINTS the deciphered Latin of the whole cipher passage ("Cum animadvertissemus ... plus brevitatis quam moræ hec mors afferet"); item 2 = Vesp. C VII 40, endorsed "1529, translata e cifris" |
| R8590 | Vesp. C IV 315 | (315) | 5300 | Ghinucci to [Wolsey], Valladolid, 15 Feb 1529 | quotes the interlinear decipherment ("Legeram enim quod in meis particularibus literis cifris additum fuerat ... perbecta essent") |
| R8613 | Vesp. C IV 363 | 332 | 3291 item 2 | Ghinucci to Wolsey, 22 July **1527** (heading "Dupplicata sub die 22 Julii 1527") | "Duplicate of the preceding, partly in cipher, undeciphered." Item 1 = Vit. B IX 127, Lat., mutilated, summarised in English (Imperialists want to split England from France; Avemaria offered 3,000,000; Tarbes; 1,000,000 for the children; envoy to free the Pope; rumour Wolsey goes to France to split the English and French Church from Rome) |
| R8572 | Vesp. C IV 214-218 | 199 | not found | Serno Gilino, Paredes [de Nava], 15 Sept 1527, Italian, to an "Illmo et Exmo unico mio Signore" | different system (B/D/6 bases + two-digit superscripts); DECODE city "Daredos" = Paredes |

So: R8589 and R8590 are a known-plaintext pair each (decipherment printed / interlined); R8476 has a contemporary
decipher (R.O.) and is printed in State Papers VI (1849) 552; R8613 is the only Worcester letter that nobody
deciphered (L&P: "undeciphered"). DECODE date for R8613 (1529) is wrong: 22 July 1527.

Tomokiyo's note "Sylvester Darius ... f.260, DECODE R8589" uses R8589 for a different folio; R8589 is f.313.

## History (15 Sept 2026, access blocked)


- Bishop of Worcester (Ghinucci): BL Cotton MS Vespasian C III f.304 (DECODE R8476); C IV f.313 (R8589),
  f.315 (R8590, deciphered — the key source), f.363 (R8613). Latin. cryptiana's partial syllable table:
  henryviii_worcester.png.
- Serno Gilino: Cotton MS Vespasian C IV f.214 (R8572). Latin, mostly two-digit superscripts.
- Garbino letter: BnF Clair. 327 ff.279-280 (+ fr.2988, 3019, 3022). Italian/Latin.

Blocker (2026-09-15): DECODE records exist but images are "Authentication required / Private Ciphertext";
BL's digitised-manuscripts viewer is unreliable since the 2023 attack; Gallica blocks this client. Without the
page images there is nothing to transcribe. If access is obtained: transcribe base-letter+superscript tokens,
seed with the R8590 deciphered fragments (Latin syllables), and extend by Latin LM + cribs (Charles V's court at
Valladolid, 1529; Wolsey as addressee).

## 9 Oct 2026: system established, R8613 transcribed

- System (from R8589 aligned with the L&P 5282 plaintext, and the R8590 interlinear): syllabic substitution,
  base glyph = consonant row, superscript digit = syllable in the row (vowel order differs per row, homophones);
  bare glyphs = single letters (bare o = p, bare z = t ...); many nulls, which the contemporary decipherer of
  R8589/R8590 struck through with a light diagonal stroke. Details and values: `key.md`, `key.tsv`.
- R8476's cipher (24 Dec 1526) is printed in full in St. P. VI 552-556 (italics = deciphered; collated with the
  contemporary R.O. decipher). Its alignment is being done to enlarge the key (`r8476_tokens.txt`).
- R8613 (f.363, the undeciphered duplicate of 22 July 1527) transcribed in full: `r8613_tokens.txt` (2 pages,
  45 lines, ~760 cipher tokens). The copy is a clerk's clean hand with no strike marks, so nulls are unmarked.
- First pass with the R8589 key (`python decode.py r8613_tokens.txt`) already gives Latin: "Lautrec",
  "Avemaria", "apud nos", "quia redire", "pro certo tenerent", "dilationem", "perpetuam divisionem" -- matching
  the L&P summary of the Vit. B IX original (Avemaria, Lautrec, perpetual division from Rome).

## 9 Oct 2026: R8613 key extension by context (pass 1)

Values added from R8613's own context, each confirmed in at least one other place where possible
(see `key.tsv` evidence column): S=u, o8=du, e3=co, n2=Caesar, n_=s, V=i, q2=be, d5=mi, x4=lo, n3=ga,
a(bare)=d, h(bare)=o, [=b, m=r, e9=cu, d2=mu, e6=ca, C=o, Cd=o, d+=m, q+=a, w(‒ω)=f, z+=t, plus nulls
(y7, g8, V13, o19, y6, q3, v18, p3, p7, Q8, T14, x18, p4 ...).
Readings secured so far (all agree with the L&P 3291 summary of the Vit. B IX original):
- "unionem inter [..] non diu duraturam" (P1 l9-10)
- "ut aliquam ansam dimit[t]atur qua possint ipsi aut nos semper ad colloquia redire. Saepeque apud nos instant
  ut particulariter super hoc apud consiliarios(?) Caesaris tamquam ex nobis instemus, ostendentes satis aperte
  cupere se magnopere ut tractatus omnino ... concludatur" (P1 l13-17)
- "per Avemariam diebus preteritis tres milliones obtulisse Caesar Nobis dixit" (P1 l18-19)
- "a fine sue commissionis dixit de Lautrec in discessu ipsius fratris sibi dixisse quod non erat parcendum pro
  liberatione filiorum ... usque ad millionem ... numquam antea fuisset oblatum minus millione. Sed ... nullo modo
  videtur verisimile quod de uno tantum millione Lautrec ageret, sed potius de millione ultra id oblata"
- "quod Nobis innuit Caesar, videlicet fuisse petitam longam dilationem ad illos tres milliones ... solutionemque(?)
  dividendam in plures pagas"
- "putant eum qui a Caesare ad[..] mittitur in nulla habere commissionem super eius liberatione ... et hic
  divulgari ad obturandum ora obloquentium tam hic quam alibi de detentione"
- "D.V.R. veniat in Galliam curaturam inter alia ut ecclesia [Anglicana] et [Gallicana] a Romana separetur non
  quidem durante captivitate et ad ... liberationem, ut dicitur, sed ad perpetuam divisionem"
Open: P1 l1-8 (the opening: Imperialists, separation of England from France, conditions) and scattered tokens.

## DECODE queue

- R8476 (Vesp. C III f.304): language of clear and cipher is Latin, not English; date 24 Dec 1526, Poissy; sender
  Girolamo Ghinucci, Bishop of Worcester, to Wolsey; L&P iv 2727; full text with the deciphered passages printed in
  State Papers Henry VIII vol. VI (1849) pp. 552-556 (contemporary decipher in the Record Office). Status could be
  "Decrypted (printed)". Transcription and alignment: `r8476_tokens.txt`.
- R8589 (Vesp. C IV f.313, old f.291): Latin; Ghinucci to Wolsey, Valladolid 12 Feb 1529; L&P iv 5282, which prints
  the Latin decipherment of the whole cipher passage; a contemporary translation "translata e cifris" is Vesp. C VII
  f.40. The MS itself carries the decipherer's null strokes. Transcription: `r8589_tokens.txt`.
- R8590 (Vesp. C IV f.315): Latin; Ghinucci to [Wolsey], Valladolid 15 Feb 1529; L&P iv 5300; interlinear
  decipherment on the page.
- R8613 (Vesp. C IV f.363, old f.332): date is 22 July **1527** (heading "Dupplicata sub die 22 Julii 1527"; the
  "1529" is the binder's heading), not 1529; sender Ghinucci, to Wolsey; L&P iv 3291 item 2 ("partly in cipher,
  undeciphered"); the original is Cotton Vitellius B IX f.127 (mutilated). Reading and key from this project:
  `r8613_reading.txt`, `key.tsv`, token transcription `r8613_tokens.txt`.
- R8572 (Vesp. C IV ff.214-218, old f.199): city "Daredos" is Paredes [de Nava]; language Italian; letter of
  15 Sept 1527 to an Italian prince ("Illmo et Exmo unico mio Signore"); a different cipher (two-digit code numbers
  on barred base letters), not the Worcester superscript cipher.
- The four Worcester records could be linked as one key family; R8581 (Darius, Vesp. C IV f.289) is the record
  Tomokiyo cites as "R8589".

## 9 Oct 2026: R8476 aligned, R8613 deciphered (pass 2)

- R8476 (f.304r-v) transcribed and aligned with St.P. VI 552-556 by a sub-agent: 845 cipher tokens, 251 distinct,
  42 struck nulls (all align as nulls). Output `r8476_tokens.txt`, `r8476_key.tsv`. It confirmed the row values
  and gave the code words: L8 Regia Majestas, K5 Rex Gallorum, K6 Italia, n2 Cesar, x1 Hispania, y6 Pontifex,
  d4 Gallia, mm9 Orator Pontificis, mm1 videtur, U6/o6 habere, Yp4 expeditionem, ɔ7 D.V.R. and others.
  Known conflicts in the scribe's own usage (two glyph forms collapsing in my names): m = r / x (x in "ex"),
  r = s / m, tw = m / r, # = s (R8476) vs o (R8590, R8613), h = s (R8476) vs o (R8613).
- With those codes R8613 now reads (`r8613_reading.txt`): 814 cipher tokens (`r8613_cipher.txt`, measured), 34
  unread (4.2%), i.e. ~95.8% of tokens given a value that reads as sense in context; several single readings are
  marked (?) and rest on one occurrence. The content agrees point by point with the L&P 3291 summary of the
  mutilated original Vit. B IX f.127 (Imperialists want to draw the King to themselves and part him from the
  French king; they think the amity will not last; the French offered 3,000,000 through Avemaria; the friar's
  account of Lautrec's order not to spare money for the French king's sons, "usque ad millionem"; the Emperor's
  hint of a long respite for paying the three millions in instalments ("in plures pagas"); the Imperial envoy to
  the Pope has no commission for his release; the rumour that Wolsey goes to France to separate the English and
  French church from Rome "non quidem durante Pontificis captivitate ... sed ad perpetuam divisionem").
- Prior solution: none for R8613 (L&P: "undeciphered"); the summary of the original (L&P 3291) was known before
  the attempt and was used as a context check; the Latin plaintext of the cipher passages is new.

## Remaining gaps

- R8613 P1 l1 "[..1] habere cupere, ho[..2]" (c; b t7) - blocker: open-codes; single occurrences, no sibling letter has these tokens and the original (Vit. B IX f.127) is mutilated and not imaged.
- R8613 P1 l7 "oblatis eis [..1]" and l11 "cupere [..1]" (the "." mark; Q8) - blocker: too-short; one token each, Q8 is a null elsewhere and nothing fixes a value here.
- R8613 P1 l8 "[..3] ad venirent" (W14 K h) - blocker: open-codes; three tokens in one place, W14 probably a null, K/h have conflicting values between letters.
- R8613 P2 l7, l13, l16 single tokens (bn, d8, b6) - blocker: open-codes; single occurrences, no second instance in R8476, R8589, R8590 or R8613.
- R8613 P2 l19 "disseminari [..3] is(tos?)" and l22 "[..3] sed ad perpetuam" (mm19 u r; n7 c1 d4) - blocker: open-codes; single occurrences in unusual combinations, no sibling with them.
- Gilino R8572: 9 unread tokens (Bp, "q o", a small o, "b o" in a struck group, o.29 xp b+) and ~108 tokens in 45 doubtful words, listed in gilino/reading_r8572.txt - blocker: illegible; the writer's own a/o and i/e confusions and glyphs that the image does not separate (struck groups, cramped superscripts); no second copy of the letter exists.

## Escalation

- [x] siblings: all four Worcester records (R8476, R8589, R8590, R8613) used. 9 Oct 2026: the DECODE neighbours of R8572 and R8613 opened by API (R8566-R8579, R8604-R8619) and the Ghinucci/Wigorn records listed (R8552-R8616): all other Cotton Vesp. C IV records are Lee/Poyntz/Worcester despatches in the English letter cipher (images of R8540, R8558, R8573, R8582, R8607 checked by eye), not this key; R8617 onward is Add MS 20443. Ghinucci's other July 1527 letters with decipherments (L&P 3273, 3321) are Record Office items, not on DECODE.
- [x] clear-pages: R8613 has no decipherment, gloss or clear copy on either page (clerk's "Dupplicata"); R8572's only extra page is the address leaf (P10), which named the recipient; no "clear" or "postscript" pages on the neighbouring records.
- [x] known-keys: Tomokiyo's partial Worcester table (cryptiana henryviii.htm) and the three deciphered siblings merged into key.tsv; for Gilino the DECODE Sforza key files (ASMi cart. 1591 R5235-R5309) scanned, R5258 fits; R5256, R5237, R5248, R5287 checked and do not.
- [x] print: L&P iv (BHO) for every letter, State Papers VI and VII (archive.org), Tomokiyo; R8613's original (Vit. B IX f.127) is only summarised in L&P 3291; R8572 not in L&P.
- [x] key-rebuild: Worcester key rebuilt from three known-plaintext letters (R8589 via L&P 5282, R8590 interlinear, R8476 via St.P. VI) and extended by context in R8613; Gilino key R5258 extended from context (gilino/key_r8572.tsv).
- [x] retry: every open R8613 token re-read on zoomed crops (pass of 9 Oct, P1 l1-11, l17; P2 l13, l17; second pass P1 l4, l6) and re-run with the extended key: "pinguiores eis" (P1 l4) and "spes nutriret" (P1 l6-7) settled, 16 tokens; 17 tokens remain. Gilino unread tokens re-checked on crops by the transcribing sub-agent (24 corrections).

## 9 Oct 2026: second image pass on R8613, sibling check, close

- P1 l4 re-read on a full-resolution crop: the last two tokens are p+ and ɔ10, not "p10 +?". With h1 = s (h = s as in R8476),
  u8 = o, Z9 and ɔ10 nulls, Q1 = i: "Et si pinguiores eis offerret conditiones" (parallel to l7 "oblatis eis ...
  pinguioribus conditionibus"). u8 and Q1 rest on this one place (grade C).
- P1 l6: the token read "v3" has a descender: y3 = nu. p+ a1 h xi14 y3 T Z2 K13 K9 z = s pe s - nu t - ri re t:
  "nisi hec eos spes nutriret" (h = s again; xi14 and Z2 nulls).
- Measure: 814 cipher tokens, 17 unread -> 797 (97.9%) given a value that reads as sense (`r8613_reading.txt`).
- Siblings opened by the DECODE API (above); nothing in this key besides the four Worcester records.
- Garbino (BnF Clair. 327 ff.279-280; fr. 3022 no. 20) is not this cipher: it is the Ranzo initial-letter + number code,
  catalogue entry 7 (`targets/vasto1527/`), and stays open there. It is out of scope for this target.
- Outcome: R8613 key recovered based on plaintext from external sources (the siblings' printed and interlinear
  decipherments), 97.9%; R8572 read after matching with key from external sources (DECODE R5258), 96.1%. Both letters
  over the read bar; the remaining tokens are scattered single occurrences.

## 9 Oct 2026: Gilino (R8572) transcribed; key search in the Sforza key files

- Sub-agent transcription `r8572_tokens.txt` (~3,157 tokens, 198 distinct; 162 cipher lines on 9 pages) and the
  clear passages `r8572_clear.txt`. Address leaf (P10): "Illmo et Exmo Dno Dno Mediolani Duci ... Cremone": the
  letter is to **Francesco II Sforza, Duke of Milan, at Cremona**; "el Gilino" is a Sforza agent at the imperial
  court; dated Paredes [de Nava] 15 Sept 1527. The clear text names Gattinara, Bourbon, the French and English
  ambassadors, Ludovico Catti (Ferrara), the bishop of Tarbes (who gave him copies of intercepted letters),
  Caiazzo, Monteleone, Marco Pio. No decipherment on the MS.
- System: barred base glyphs (6, B, D, d, o, H, A, P, R) with two-digit numbers 20-80, plus ~40 unnumbered signs.
  A one-token-one-letter homophonic anneal (Italian 'it-cinquecento' 4-gram, frequency penalty) gave no Italian
  (-2.9/char, restarts disagree): the numbered groups are syllables/words, not single letters.
- Key search: DECODE holds ~377 Sforza key records (ASMi Carteggio Sforzesco cart. 1591/1597/1598, PDFs). R5256
  (cart. 1591 no. 22) is the same family (barred B/D with numbers for names: Papa B20, Imperatore D20, Gran
  Cancelliere D22, Antonio Leyva D26, Duca di Milano B28 ...), 1520s, but its syllable table differs. A full scan of
  the key files for Gilino's table is running.
- **Key found: DECODE R5258** (ASMi Carteggio Sforzesco cart. 1591 no. 24, docket "Cum equite Bilie / extracta ex
  cifris"), by a sub-agent scanning the contact sheets of cart. 1591 (R5235-R5300) and R5301-R5309 (cart. 1597/1598
  R5310-R5611 not examined after the match). Its barred "G" = Gilino's "6"; rows B.31-50 ba..gu, B.51-55 fa..fu,
  D.51-65 la..nu, 6.56-80 pa..tu, o.33-47 va..zu; words H.26 cosa, H.27 che, H.28 come, R.23 con, R.28 ancora,
  D.40 sara; letters and nulls (a++ etc.) also on the sheet. First application gives Italian throughout ("firmato
  da molti", "le galere di Napoli", "cento milla ducati del cambio", "la morte di Borbone", "dalli oratori
  confederati", "nuncio in credenza", "camerero di Sua Santita"). Notes: `gilino/key_R5258.md`, first decoder
  `gilino/dec.py`, `gilino/final.py`, output `gilino/r8572_test_decrypt.txt`. Key renders in `img/` (git-ignored).
- Name question: the key is "with the Cavaliere Bilia", the letter is signed "Servo el Gilino" (checked on the
  image); R5287 (cart. 1591 no. 53, 7 Nov 1525) lists "Cavallero billia" and "Ghilino" as two people. Open.
- Other Sforza keys for the same men: R5237 (Bilia, plain numeric alphabet), R5248 ("Cum Camillo Gilino in
  Fiandra", digraph-to-digit key), R5236 and R5287 (nomenclators naming Gilino).

## 9 Oct 2026: Gilino R8572 deciphered with R5258

- Sub-agent reading `gilino/reading_r8572.txt` (decoder `gilino/decode_r8572.py`, `gilino/build_reading.py`; key
  `gilino/key_r8572.tsv`, 183 rows with source sheet/context; 24 transcription corrections in
  `gilino/transcription_corrections.txt`; English summary `gilino/summary_r8572.txt`). Measure: 3,111 cipher tokens,
  122 nulls, 2,989 significant, 9 unread, ~108 in doubtful words -> 2,872 read as sense = 96.1%; it-cinquecento
  LM -1.52/char on the word-divided text.
- Folio order differs from DECODE image order: P1 > P2 > P7 > P3 > P5 > P4 > P6 > P8 > P9 (ff.214r-218r).
- Content: Gattinara out of favour over two intercepted letters to the Viceroy of Naples about relieving Genoa (the
  confessor and secretary Lalemand his enemies); the Duke should have "the Bilia" keep in with Gattinara now that
  Bourbon is dead; the new Portuguese ambassador and a letter in the Pope's own hand; two papal briefs; the
  Abbatino's mission and Gregorio Casale; Paolo Luzzasco to go over to the Emperor with 300 light horse; the French
  ambassadors insist the Duke keep Milan; the Emperor said to revoke the Pope's liberation after the Lombard news;
  Andrea da Burgo "pro opprimenda Italia"; investiture of Milan sent to the Infante with 100,000 ducats.
- Bilia vs Gilino: the cipher names Bilia in the third person, and R5287's codes for Bilia (A28) and Ghilino (A29)
  do not occur; R5258 is a key drawn from the Bilia correspondence that Gilino also used.
- Prior solution: none found (no decipherment on the MS, not in L&P); the key was in the Milan archive, filed under
  another correspondent, not previously tied to this letter.

## DECODE queue (Gilino)

- R8572: author "Gilino" (sign. "Servo el Gilino"), recipient Francesco II Sforza, Duke of Milan, at Cremona (address
  leaf P10); origin Paredes [de Nava] (not "Daredos"); language Italian; key = DECODE R5258 (ASMi Carteggio
  Sforzesco cart. 1591 no. 24); image order vs folio order as above; reading in `gilino/reading_r8572.txt`.
- R5258: link to R8572 as the key that reads it (docket "Cum equite Bilie / extracta ex cifris").
