# Cardinal Alessandrino to the nuncio in Spain, 1567–69, and a letter of 1572 — read

**14 Nov 2026 (title, owner decision):** the target is now titled for what it holds: the ten ciphers of Spagna 6/I, from Alessandrino (R94 of 7 November 1567, the rest of 1568 and 1569), and R115, of about the end of January 1572 and not his (writer not established). R115 stays in this target (same DECODE series, same key with its extension; "one key, one entry"). The folder name and the slug `alessandrino1568` are unchanged. Section "Title" at the end.

**14 Nov 2026 (verification):** R99 and R115, the two letters under the 95% bar since 24 Oct, re-read on the DECODE images and decipherments: R99 94.7% -> 98.9%, R115 88.5% -> 97.4%; all eleven letters now read. Codes 2020, 4050 and 9070 resolved; R115 probably of January 1572. Section at the end.

Status: read (23 Oct 2026, r2g: all eleven letters read; R93, R96-R99, R102, R115 from the contemporary decipherments found on their DECODE cleartext images; 24 Oct 2026 R99 and R115 under the 95% bar; 14 Nov 2026 both re-read by Brice Dudout and over it, PR #604).

**22 Oct 2026, reading audit** (George Lasry's test): R93, R96, R97, R98, R99, R102 and R115 build Italian sentences with scattered slips; **R94, R95, R100 and R101 are decoded, not read**: the beam search's digit choices corrupt words in most of their sentences (R94 "liberagemptume", R95 "desersaleaniosina", R100 ends in ??????, R101 "unmannifestsobismain"). Claim read -> read in part; 7,036 of 10,555 items (66.7%) in letters that read.

**22 Oct 2026, re-read (REREAD_BRIEF, batch aless; texts/R94-R101_reread_log.md)**: the DECODE "cleartext" images
of these records hold the **contemporary decipherments** of three of the four: R94 on f. 45r (covering letter Rome 7
Nov 1567, f. 44r, "Con questa un poco di cifra" — so R94 is of 1567), R95 on f. 58r, R100 under the cipher on f.
280r. Transcribed (texts/R94_decifrato_f45r.txt, R95_decifrato_f58r.txt, R100_decifrato_f280r.txt) and aligned with
the figures (`reread_aless_align.py`); the disagreements showed what Lasry's key lacked: **9 also = "con"**, **dotted 0
= z**, **0^.0 = et**, doubled letters enciphered once, X0Y0 codes written X0Y, 3 0 9 = qua, and code values 1040
lettere (not "Regina di Francia"), 3020 quando, 3060 -mente, 4020 come, 4040 Milano, 4080 et, 5070/6050
Imbasciatore, 6060 Inquisitione, 8090 havere (not "sauere"), 2 0 9 = "chi" (chinea, Chiesa). R101 (no decipherment)
re-decoded with the extended key (`reread_aless_decode.py`) and read word by word: the chinea accepted with the
fisc's protest, devolution under the investitures of Julius II and III, the schism in Naples, notaries and executors
imprisoned. Readings + English: texts/R94|R95|R100|R101_reading.md, _en.md; clean-sentence share 1.00, 0.94, 1.00,
0.84 (before 0.75, 0.89, 0.78, 0.81 on the garbled decodes). State decoded, not read -> read; class back to read.

Catalogue items 253 (class B) and 254. ASV (AAV), Segreteria di Stato, Spagna 6/I, items 1–10 ("Lettere orig. e
cifre del cardinale Alessandrino dal 16 gennaio 1568 …"), DECODE R93–R102; and Spagna 6/II item 13 (catalogued 1569; of early 1572, see the integration check of 14 Nov 2026), DECODE R115.
Sender of the ten letters of 6/I: Michele Bonelli, Cardinal Alessandrino, nephew and secretary of Pius V. Sender of R115: not
Alessandrino, not established (integration check of 14 Nov 2026). Recipient: the nuncio at Madrid,
Giovan Battista Castagna. The letters are undated on DECODE; folio order puts 6/I in 1568 (R94 is of 7 Nov 1567 by its covering letter).

**Result (21 Sept 2026): read.** All eleven ciphertexts read end to end with George Lasry's reconstructed key.

## Key

Lasry's reconstruction (DOC_R9x_D32xx.txt, 24 Oct 2020), attached to every record; DECODE lists the records as
"partially decrypted" because the key is there, but no plaintext was posted.

- Polyphonic: each digit stands for two letters — 1 u|t, 2 i|m, 3 f|g, 4 a|l, 5 o|s, 6 e|n, 7 d|r, 8 b|c, 9 p|z.
  0 is a null. No h, q.
- Nomenclator: four digits X0Y0 (1010 Nostro Signore, 1090 V. S., 2090 che, 3010 Re, 4030 S. M.tà, 5020 per,
  6090 quel, 7090 quello, 8010 Re di Francia …) and dotted pairs (0^.0 comma, 30^.9 qua). Full list in decrypt.py.

Because each digit has two readings and the zeros make X0Y0 codes ambiguous with letter+null pairs, the text is
chosen by a beam search scored by the shared Italian model (`lang/`, it-cinquecento, no spaces):
`python decrypt.py > decrypt_raw.txt`. Output is unspaced; `[WORD]` = nomenclator, `[NN.]` = dotted group not in
Lasry's list. Each page ends in a run of padding (strings like `fcpfbrpf`), which is the cipher clerk's filler.

## The letters (gist from decrypt_raw.txt)

- R93 (6/I/1, f. 6r): friends of the crown of France have asked here that the Pope promote a marriage of one of the
  French King's daughters to His Catholic Majesty; the Pope would not move without knowing the King's mind; the
  nuncio is to sound it in the way he thinks best, assuring him no word will be said before his intention is known.
- R94 (6/I/2, f. 42r): jurisdiction. The Pope does not mean to revoke the King's privileges but to remove abuses grown
  through his ministers; the ministers try to strip the Holy See of its authority; the King should hear this freely.
- R95 (6/I/3, f. 55r): reply on the ministers' claims, the crusade alms ("elemosina … indulgentia"), the Pope's
  offer of a pension; the King must not be thought alienated from the Holy See.
- R96 (6/I/4, f. 81r): awaiting the nuncio's answer on the marriage; union of the three principal princes of
  Christendom; a heretic prosecuted by the Holy Office; the Hermits of St Jerome (Jeronimites).
- R97 (6/I/5, ff. 88r–89v, 4 pp.): Bolognese exiles (fuorusciti) sheltered in the King's lands, the Cavaliere
  Gualengo; the King as the Holy See's feudatory for Naples must hand back exiles under the investiture; the Turk in
  Adrianople, a French ambassador there, the German Protestants promising the Sultan help; danger to Christendom.
- R98 (6/I/6, f. 136r): the King's orders to his ministers about the clergy are delayed by waiting for commissions.
- R99 (6/I/7, f. 169r–v): the Order of St John and its Grand Master; Don John of Austria; the Milan senate against
  the archbishop (Borromeo) over the Corpus Domini procession; the Pope will use spiritual arms.
- R100 (6/I/8): the King's ministers' proceedings; a brief to be executed.
- R101 (6/I/9, f. 291r–v): Naples census (the hackney and the feudal dues of St Peter's day), the investiture, the
  schism threatened by the ministers; the King's realms will be troubled if he does not remedy it.
- R102 (6/I/10, f. 306r): a prelate "deputato in regno" failing in his office; the Pope might have made him cardinal.
- R115 (6/II/13, f. 641r, catalogued 1569, of early 1572): pensions on a see, the King's nomination, a commission; the Council.

## Grades and what is open

- Reading is continuous Italian throughout; individual letters are model choices (M), words H where the context
  forces them. Lasry's tentative glosses kept: 1040 Regina di Francia?, 3040 Fiandra?, 8090 sauere?, 2020 con?.
- Unlisted dotted groups met: [01.] [02.] [03.] [04.] [08.] [09.] [1.] [40.] [43.] [44.] [51.] [60.] [70.] [80.] [90.]
  — mostly punctuation-like (04. and 60. recur where a comma or "et" fits); not resolved.
- Not done: comparison with the contemporary decifrati and with Serrano, *Correspondencia diplomática entre España y
  la Santa Sede durante el pontificado de S. Pío V* (1914), which prints Alessandrino–Castagna letters of 1566–68 and
  may give some of these in clear. HathiTrust full-text search returned 403 from here.
- Transcriptions are DECODE's (TimB 2016, RebAn, Midas) and were not re-checked against the images.

## Verification 4, 23 Oct 2026

The v4 sweep could not score R93, R96, R97, R98, R99, R102 and R115: their entries pointed at the unspaced beam
decodes (`texts/<rec>_decryption.txt`). Each was re-decoded with the key as extended from the R94/R95/R100
decipherments (`reread_aless_decode.py`, which the 22 Oct re-read had used only on the four) and word-divided as
`texts/<rec>_reading.md`, every beam choice not checked on the figures bracketed. v2_score, explicit holes:

| record | explicit holes | hole rate | words |
|---|---|---|---|
| R102 | 0.556 | 0.115 | 122 |
| R97 | 0.486 | 0.137 | 422 |
| R99 | 0.45 | 0.161 | 242 |
| R96 | 0.429 | 0.176 | 153 |
| R93 | 0.375 | 0.156 | 90 |
| R98 | 0.333 | 0.258 | 128 |
| R115 | 0.167 | 0.301 | 136 |

The audit's "build Italian sentences with scattered slips" does not hold once the text is divided into words: the
polyphonic digits leave many words as model choices. All seven **demoted to decoded, not read** (partial readings
kept). Class read -> read in part; fraction_read 1.0 -> 0.333 (3,519 of 10,555 items in R94, R95, R100, R101). The
way forward is the one that worked for R94-R101: open these records' DECODE cleartext images for contemporary
decipherments, then re-read on the figures with `reread_aless_align.py`.

## Re-read r2g, 23 Oct 2026: the seven demoted letters read from their decipherments

Every DECODE image and attachment of R93, R96, R97, R98, R99, R102 and R115 (and the record pages of R92, R103, R114,
R116) was opened at full resolution (`research/reading_audit/r2g_fetch.py`, project cookie, scratchpad only). **Each
of the seven has its contemporary decipherment among the "cleartext" images**: R93 slip f. 8 (D1216), R96 slip f. 80
(D1255; covering letter Rome 19 May 1568, f. 79), R97 f. 90r-v (D1264-65), R98 slip f. 139 (D1275), R99 leaf after f.
169 (D1284), R102 slip f. 307 (D1308; covering letter docketed June-Aug 1569), R115 half-sheet with f. 641 (D1340).
Transcribed as `texts/<rec>_decifrato_*.txt`, aligned with the figures (`reread_aless_align.py`, now with multi-page
runs and dotted-group word signs) and read with the figures deciding where the decipherer differs
(`texts/R93-R115_corrections.tsv`). Readings and English: `texts/<rec>_reading.md`, `_en.md`; log
`texts/R93-R115_reread_log.md`. New code values (key.md): 2010 Imperatore, 4010 Re di Francia (not Lasry's Sua
Santità), 1020 esser, 8020 avviso, 8070 Ugonotti, 3050/6030 Italia, 7040 galere, 9090 havendo, 6020 causa, 7030
Cardinale, 7070 Imbasciatore, dotted 1+8 ancora, 9+8 acciò. Persons: Count Ercole Tassone, Piali Pasha (R97), Cardinal
Espinosa (R102), Francisco de Reinoso for Monreale (R115).

v2_score, explicit holes (before -> after): R93 0.375 -> 1.0, R96 0.429 -> 1.0, R97 0.486 -> 1.0, R98 0.333 -> 1.0,
R99 0.45 -> 0.87, R102 0.556 -> 1.0, R115 0.167 -> 0.667. All seven decoded, not read -> read; class read in part ->
read; fraction_read 0.333 -> 1.0 (10,555 / 10,555 items).

## Remaining gaps

- R94 (2 short gaps): "9 0 4 0 2 0" before S.M. and the verb 6 2 4 7 6 after "comincia" - blocker: no-key-material; the contemporary decipherer left the first unread and guessed the second; no other text of the letter (Serrano 1914 not reachable)
- R95 (4 holes): dotted groups [08.] (the Crusade?) and [3.] (a person), "co[…]", "[?fece]" - blocker: illegible; the decipherment is illegible at these words
- R101 (5 holes): two places in row 1 under a burn and a hole in the paper, one illegible group in row 14, "[?Sora]", code 6020 (9090 havendo and 8020 avviso read 23 Oct from the R99/R93 decipherments) - blocker: illegible
- R93, R96-R98, R102 (read 23 Oct 2026): short unread runs and codes inside the readings - R93 one group; R96 the heretic's surname, [?quanto]; R97 four runs, "Duca di Ferrara" (4060 5050) and "Principe di Condé" (dotted 3+4) on the decipherer's word only; R98 [?possa], [?et]; R102 three words - blocker: no-key-material; the decipherers left them blank or wrote words the figures do not carry, and the codes occur nowhere else
- R99, R115 (read 14 Nov 2026): R99 [?poco] (a slip), [?e] (a blot), [con] (no figure); R115 [?Francesco] (a slip), [?ancora] (burn hole), the name after "negocio de" (4 1 8 2 4 4 2), one 5 2 not placed - blocker: illegible / no-key-material
- Serrano, Correspondencia diplomatica ... Pio V (1914): not checked - blocker: needs-physical-access (HathiTrust 403 from here, not on archive.org)

## Escalation

- [x] siblings: all eleven Spagna 6/I and 6/II ciphers decoded with the same key; the R94/R95/R100 decipherments extended it and the extension read R101
- [x] clear-pages: 22 Oct 2026, all 45 DECODE cleartext images of R94, R95, R100, R101 looked at; decipherments found for R94 (f. 45r), R95 (f. 58r), R100 (f. 280r), none for R101; R94's covering letter dates it 7 Nov 1567. 23 Oct 2026 (r2g): every image of R93, R96-R99, R102, R115 opened; decipherments found for all seven (R93 f. 8, R96 f. 80, R97 f. 90r-v, R98 f. 139, R99 after f. 169, R102 f. 307, R115 with f. 641); neighbours R103 and R114 looked at
- [x] known-keys: Lasry's reconstructed key (DECODE, 2020)
- [x] print: 22 Oct 2026, Serrano 1914 searched again: not on archive.org, HathiTrust full text 403, Google Books API quota exhausted; Serrano's Liga de Lepanto (1918-19) begins in 1570 - not reached
- [x] key-rebuild: 23 Oct 2026 (r2g) extended again (2010, 4010, 1020, 8020, 8070, 3050, 6030, 7040, 9090, 6020, 7030, 7070, dotted 1+8, 9+8); 22 Oct 2026, key extended from the decipherments (9 = con, dotted 0 = z, 0^.0 = et, codes 1040, 3020, 3060, 4020, 4040, 4080, 5070, 6050, 6060, 8090); [01.], [03.], [08.], [3.], [4.]8 (= perché), 9090, 6020, 8020 partly or not resolved
- [x] retry: 22 Oct 2026, R94, R95, R100, R101 re-read (texts/R94-R101_reread_log.md); all four build sentences; 23 Oct 2026 the other seven re-decoded with the extended key and word-divided: below the bar; same day (r2g) read from their decipherments (texts/R93-R115_reread_log.md)

## Verification 14 Nov 2026 (R99, R115; Claude Opus 5.5)

The two letters under the read bar (R99 0.947, R115 0.885 on 24 Oct) were re-read on the full DECODE images of the
ciphers (R99 ff. 169r-v, R115 f. 641r) and of their contemporary decipherments (R99 D1284, R115 D1340), opened at
native resolution in a private scratch copy (DECODE R99, R115; images not committed). The disputed lines were
transcribed a second time by a separate pass that saw only the crops, not the DECODE transcription or this reading:
of the 11 crops (about 300 figures), 6 agree figure for figure with DECODE; in the other 5 the differences are the place
of dots (R99 "0̇ 2010", the blind pass seeing the mark above "2 0" and one doubtful 0; R99 "9 0̇ 8"; R115 "3 0̇ 8", "0 1̇ 0":
same groups), one "1" in R115 "s(u)a", and the last figures of R115 line 12, read "1? 5? 0 1?" where DECODE and this
reading have "3 0 1" (3010, the decipherer's "S.M.").

**R99.** The stretch after "d'Oria" reads "essendone stato ricerco da N.S.; ma inteso questo" (2020 = essendo; 7 2 8 6 7 8 5 =
ricerco; 2 4 = ma), and the decipherer, re-read, has "[?essendone stato ricerco da S.S.]" and "ma inteso" there (the 23 Oct
transcription "come sono certo che V.S. haverà inteso" was a misreading). The second 2020 is the decipherer's
"essendosi fatto" (not "è stato fatto"). The head of the Milan paragraph is "Il Duca d'Alburquerque ha usato novamente in
Milano uno atto di propria autorità": a dotted 2010 that the decipherer first wrote "Imp.re" and corrected above the line
to "Duca d'Alburquerque a usa[to]" (read "Della dalla Chiesa a Milano" on 23 Oct); Gabriel de la Cueva, duke of
Alburquerque, governor of Milan 1564-71, against Archbishop Carlo Borromeo. "acciò" is the dotted 9 + 8 group. Left: [?poco]
(1 for 9), [?e] (a blot), [con] (no figure). read_share 0.947 -> **0.989** (259 words, 3 holes).

**R115.** "fino [?…] [9070] [2]" was a misdivision: fin 5090 qui 7020 risposta (the decipherer "sinqui risposta"); 9070 does
not occur. "del vero [?…]; di [?…] che" is "del vero valore di esso; di che" (the 2 that ended the old run starts 2090).
Dotted 3 + 8 = quanto, twice ("quanto prima potrà", "Quanto al negocio"; the decipherer "q.to"; the same group reads
"quanto alla" in R95). "et avisarmi poi […]" is "con le prime" (9 = con; the decipherer "c[on] le pr.e"). "[?…] la causa de
[?…] […] [?la] tratta" is "Quanto al negocio de [name], poi che Re lo tratta di costà" (4 5 = lo; the decipherer "la").
4050 (or 4 + 5070) = Monsignor Reverendissimo, the decipherer's "Mons.r R.mo" (read "Commendatore" on 23 Oct). 2010 is the
Pope here ("scalco segreto di N.S."). Left: [?Francesco] (6 for a), [?ancora] (burn hole), the name 4 1 8 2 4 4 2 (the
decipherer "lucadi", not carried), one 5 2. read_share 0.885 -> **0.974** (151 words, 4 holes).

**R115's date (probable, not proved).** The writer "wrote to Monsignor Reverendissimo d'Alessandrino" on 30 November
asking him to obtain the nomination from the King: this fits Cardinal Alessandrino at the King's court on his legation
of 1571-72, so the letter is probably of about late January 1572, like the clear letters on the record (ff. 639, 642),
and its writer is not Alessandrino. A 2010 that means the Pope, not the Emperor as in 1568, fits a different list.
Title and route left as they are for Daniel to decide. [Decided at the integration check below: R115 dated 1572 from the archive's description of the volume.]

**Measurement.** The new values (2020 essendo, 7020 risposta, 4050 Monsignor Reverendissimo, dotted 2010 il Duca
d'Alburquerque, dotted 3 + 8 quanto) are read from the contemporary decipherments, not found by search; key frozen
(texts/key.md, SHA-256 4c86fbca89de5b5c3fe06e3546178af0aee352ccf98affdb085891404fe1b2ef). **Not measurable:** outside
R99 and R115 the codes occur only once more (dotted 3 + 8 in R95, already read "quanto alla" there), far from 300 fresh
signs. read_share as `research/reading_audit/v10_relabel.py` counts it.

## Integration check, 14 Nov 2026 (PR #604, Brice Dudout)

The class change to read is applied.

- Recount with `research/reading_audit/v10_relabel.share`: R99 259 words and 3 holes, 0.989; R115 151 words and 4
  holes, 0.974, as the pull request says. The other nine letters are between 0.968 (R101) and 1.0 (R100). In R99 and
  R115 every hole is one word, so the count by marks is the count by words.
- The new words were checked against DECODE's own transcriptions of 2016 (`decode/DOC_R99_D1670_1670.txt`,
  `DOC_R115_D1685_1685.txt`) with a separate small decoder: in "stato ricerco da", "ma inteso", "usato", "valore di
  esso", "fin", "alcuna", "poi con le prime", "lo tratta di costa" and "Alesandrino" every figure is one of the two
  letters of its figure. The same figures also spell "tolto" for "usato", as the reading's note says.
- Two code values rest only on the contributor's re-reading of the decipherer's hand, which had been read differently
  on 23 Oct: dotted 2010 = il Duca d'Alburquerque (then "Della dalla Chiesa a Milano") and 4050 = Monsignor
  Reverendissimo (then "Commendatore"). Counted as holes, R99 is at 0.977 and R115 at 0.968, still over the bar.
- Not checked here: the images. DECODE gives the full-size images and the decipherment leaves (D1284, D1340) only to
  an account ("Insufficient permissions"); the blind second pass is by the contributor's record.
- **R115 is of 1572 and is not Alessandrino's.** The DECODE record of R115 carries the archive's description of
  Spagna 6/II: "Lett. orig. dei cardinali Alessandrino, Rusticucci e di Ugolino Gualterucci al nunzio, dal 1 jan
  1569 - 29 dec. 1570, ff. 341-581 ... dal 3 jan 1572 - 1 maggio 1572, ff. 584-674". The cipher is f. 641, in the 1572
  part, between clear letters of January 1572 (ff. 639, 642). The cipher itself spells "Scrissi a [4050] Alesandrino
  dua mesi sono, l'ultimo di novembre": the writer wrote to Alessandrino, so he is someone else, writing about two
  months after 30 November 1571. The description names Cardinal Rusticucci and Ugolino Gualterucci beside Alessandrino
  for this volume; which of the two wrote f. 641 is not established here. That Alessandrino was then on his legation
  to Spain and Portugal, and that Rusticucci held the secretariat meanwhile, is background not checked against a source
  here. `profile.json` documents: R115 year 1569 -> 1572. The page and the README row say so. The target's title is
  unchanged: it names the ten letters of 6/I (November 1567 to summer 1569). [Changed the same evening by the owner's decision: section "Title" below.]
- R115's 2010 = N.S. (Emperor in the letters of 1568) and its 4050 fit a revised list of codes; the letter figures and
  the other codes (1010, 2060, 2090, 3010, 5020, 5090, 7090) are the same, so R115 stays in this target.

## Title, 14 Nov 2026 (owner decision)

Old title: "Cardinal Alessandrino to the nuncio in Spain, 1568–69". New title: "Cardinal Alessandrino to the nuncio in
Spain, 1567–69, and a letter of 1572".

- R115 stays in this target. It is in the same DECODE series and the same nunciature correspondence, and it was read
  with the same key and its extension; a target of its own would be a one-letter entry in the same key, against "one
  key, one entry". The slug and folder name `alessandrino1568` and every link are kept.
- The ten letters of Spagna 6/I are Alessandrino's by the archive's description of the volume ("Lettere orig. e cifre
  del cardinale Alessandrino dal 16 gennaio 1568 …"). Their dates, where there is evidence: R94 7 November 1567
  (covering letter, f. 44r); R96 19 May 1568 (covering letter, f. 79); R99 summer 1568 (clear letters ff. 164-168, 21
  June - 27 July 1568); R100 spring 1569 (neighbouring clear letters, f. 282r Rome 25 April 1569, f. 279r May 1569);
  R102 summer 1569 (covering letter docketed June-Aug 1569). R93, R95, R97, R98 and R101 have no date evidence of
  their own recorded here beyond their place in the volume (the readings head R95 "early 1568" and R101 "summer
  1569" without stating the evidence). The range is therefore 1567–69, not 1568–69: the title now says so. `profile.json` documents carry
  these dates (they were all "unknown", year 1568).
- R115: about the end of January 1572, not written by Alessandrino, writer not established; the archive's description
  names Cardinal Rusticucci and Ugolino Gualterucci beside Alessandrino for ff. 584-674 (integration check above).
  Its 2010 stands for the Pope (the Emperor in the letters of 1568), which fits a revised code list.
- Not stated anywhere as fact: that Alessandrino was away on his legation, that the letter was "written in his
  absence" (the manifest blurb said so; removed), or that the writer belonged to the papal secretariat. The headings
  of `texts/R115_reading.md` and `R115_en.md`, filed with PR #604 as "The papal secretariat (not Alessandrino) …", were
  changed on 14 Nov 2026 to "Not Alessandrino (writer not established)"; no source in this folder establishes the
  office of the writer.
- Surfaces changed: `docs/_manifest.py` (title, year, blurb), the page, this file, `profile.json` (title, document
  dates), README row, `SOLVED_CATALOGUE.md`, `SOLVED_RANKING.md`, `CATALOGUE.md`, the findings line,
  `decode_updates/queue.json` (R115 sender).
