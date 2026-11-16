# Codex 533, ff. 1r-1v: independent verification record

Object: University of Pennsylvania, Kislak Center, Ms. Codex 533, first letter (ff. 1r-1v), autograph of Cosimo III, Grand Duke of Tuscany, to his envoy Anton Francesco Montauti. Undated; breaks off at the foot of 1v.
Verifier: an independent AI agent (Claude), 14 Nov 2026. Read from the saved full-size Penn images (`sources/raw/montauti_penn/codex533/full/`, 4514 x 5717; nothing new downloaded). Nothing posted, committed or sent; no other agent's file edited.

Files beside this record:
- `montauti_1r1v_PART1_blind.md`: the blind Part 1 (transcription line by line, decode tables, continuous text, translation, answers, date). Frozen before any of the first agent's notes or transcriptions were opened: sha256 3e37c4f0... in `PART1_FROZEN_SHA256.txt`.
- `crops/`: reference crops of every line used, the disputed places and the two sample runs.
- `dec.py` (decoder: key v3, then context values, then the usual 9→5 emendation), `crop.py`.

Declared contamination: the `_sources` note inside `round4/key_v3_context.json` (a key file I was allowed to open) names "ritornare qua" (1r), "Palatino", "marito", "Dusseldorf" and "havea" as places where the values occur. I read that before the images. "mia figlia", "permission-", "separarsi", "mia et di mia figlia", "calunnie", "vergogna" and all other clear text were not named in anything I had opened.

## Part 1 in brief (full text in the PART1 file)

Cipher runs, my blind digits (w = the c-and-loop sign):

| Run (their label) | Place | My digits | Key v3 | Reading |
|---|---|---|---|---|
| 1r a | 1r ll. 4-5 | 55 21 55 6w 6w 41 64 [6/w]4 60 11 55 w2 / 6w w6 5w 4[8/0] | l e l t t o r [r/e] p a l a t i n [o] | l'El[e]ttore Palatino |
| 1r b | 1r l. 6 | [5/9]6 w6 w2 4w 31 [5/9]0 55 31 11 | mia figlia (m, g need 9→5 if the heads are 9s) | (la) mia figlia |
| 1r b cont. | 1r l. 7 | [5/9]6 w6 [5/9]2 11 [9/5]1 21 11 | mi havea | mi havea |
| 1r c | 1r l. 8 | 60 21 64 [5/9]6 31 66 w6 ww 5w w2 | p e r m i s i [ww] n a | permission[e], ends in a |
| 1r d | 1r ll. 8-9 | 64 31 / 6w ww 64 5w 11 64 w4 62 [9/5]1 11 | r i t [ww] r n a r e [62] u a | ritornare qua |
| 1r e | 1r ll. 9-10 | 66 w4 60 11 / 64 11 64 66 31 | separarsi | separarsi |
| 1r f | 1r l. 10 | [5/9]6 11 64 31 6w ww | m a r i t [ww] | marito |
| 1v a | 1v ll. 2-3 | [5/9]6 w6 w2 21 6w 46 w6 [5/9]6 31 11 4[8/w] 31 [5/9]0 55 w4 / w2 | m i a e t d i m i a f i g l e a | mia et di mia figl[i]a |

The context-only values add three o's (ww: permission-, ritornare, marito) and one q (62: qua), plus the o of "Palatino" if the last sign pair is ww (my alternative is 48 read as 40, an emendation). They change no word's identity: every word they touch is fixed by its other letters.

Continuous text, with gaps (clear text lower case, cipher in capitals):

> [Signor Dottore?] So che V.S. applicherà? tutto lo? suo maggiore studio? in un negozio che mi sommamente? preme. Mi fa sapere L'EL[E]TTORE PALATINO [d(e)l? un? amico / del March(ese)?] ch[e]? li fu scritto [a Vienna? / giunse?] che la MIA FIGLIA MI HAVEA scritto per domandarmi la PERMISSION[E] [di? / e?] RITORNARE QUA e SEPARARSI dal? [suo? / mio? / uno?] MARITO; onde V.S. vede? bene? [... about 4 words ...] mi fa? credere? ch'insinuasse? il Principe e da un intrigo? [...] subbietto? una? simile, ci fanno vergogna, [...] e ci offen[...] [che? / nella?] reputatione e MIA ET DI MIA FIGL[I]A et? [...] grande [...] del pregio? di [...] e che simili calunnie [...] non fussero riportate? Però V.S. ci adopri? tutta la sua maggiore destrezza? e accuratezza?, non risparmiando a veruna fatica, e con ogni efficacia, e così mi voglia d[are] testim[onianza]? del suo amore fedele e sincero [...]. Se mai [...] bisognio che V.S. per mio servizio facessi un viaggio a Dusseldorf, crederei? che fussi bene che V.S. con scriverli o farli dire del mio sentimento? [...] [breaks off]

> English: "[...] I know Your Lordship will give your greatest care to a matter that presses me greatly. THE ELECTOR PALATINE lets me know [through a friend? / of the Marchese?] that it was written to him [...] that MY DAUGHTER HAD written to me to ask my PERMISSION TO RETURN HERE and TO SEPARATE from [her?] HUSBAND; so Your Lordship sees [...] they put us to shame, [...] and it offends [...] the reputation both MINE AND MY DAUGHTER'S [...] and that such calumnies [...] should not be repeated?. So Your Lordship is to use all your greatest skill and care, sparing no effort [...]. If it should ever be needed that Your Lordship, for my service, make a journey to Düsseldorf, I would think it well that Your Lordship, by writing to him or having him told of my feeling [...]"

Who says what (my blind answers; detail and Italian in the PART1 file):
- Cosimo writes to Montauti. The Elector Palatine is the one who informs Cosimo: "Mi fa sapere [L'ELETTORE PALATINO]". High confidence on the words; moderate that the Elector is grammatically the subject (verb-subject order, no other candidate).
- What reached the Elector: that it "li fu scritto" (was written to him) that the daughter "MI HAVEA scritto per domandarmi la PERMISSION[E] ... RITORNARE QUA e SEPARARSI dal ... MARITO". The writer of that report to the Elector is not identified by anything I can read with confidence ("amico"? "Marchese"?).
- The daughter's matter is a report at second or third hand of a request she supposedly made, not a fact Cosimo asserts and not his own request. He treats talk of this kind as shameful ("ci fanno vergogna", 1r l. 14), offensive to his and her reputation ("ci offen[...] ... reputatione e MIA ET DI MIA FIGLIA", 1v ll. 1-2), and calls it calumny ("simili calunnie", 1v l. 4). No explicit denial ("it is false") is among the words read.
- He wants Montauti to work against it with all his skill and effort ("ci adopri? tutta la sua maggiore destrezza? ... non risparmiando a veruna fatica"), so that such calumnies are not repeated (the purpose clause is doubtful), and if need be to travel to Düsseldorf on Cosimo's service and write to, or have told, someone ("scriverli o farli dire", most naturally the Elector) Cosimo's mind.
- Date from the text: after the marriage of Anna Maria Luisa to Johann Wilhelm (1691) and before his death (1716), from "Elettore Palatino", "mia figlia", "marito", "Dusseldorf". Nothing narrower on the page.

## Part 2. Comparison with the first agent (round 4b notes and `round4/reconciled_533_v2.tsv`, `disagreements_settled.tsv`)

### 5a. Cipher digits, difference by difference

My blind digits and theirs (second reconciled transcription) agree on every run of 1r-1v in the number of signs and in all but the following places:

| Place | Theirs | Mine | What the image shows (crop) | Decode effect |
|---|---|---|---|---|
| 1r a, sign 15 (the e/r after "Elettor") | 6 (settled for pass A, low-medium) | 6 or w, left open | A 6-shaped sign entered by a hairline from the crossbar of the 4; no open c is visible (`1r_glyph_w_and_6_elettore.jpg`, `1r_l04-05_...`). I agree a literal reading is 6, so the group is 64 = r and the word is "Elettor" + "Palatino" with no final e. | none on identity |
| 1r a cont., last two signs | [w/4] w = ww (o, context) | 4 8, read 40 (o) by 8→0 | An open c with a heavy diagonal, then a c-headed 8-like loop. Their c+diagonal w and my 4 are the same stroke; I now prefer theirs, because the same "c + diagonal" w occurs in 1r c (sign 18) and 1r f. | o either way; but it is a context-only value (theirs) or an emendation (mine), not key v3 |
| 1r c, sign 11 | 0, emended 0→6 | 6 | An oval whose top is joined by a hairline to the ascender of the next 6; the oval itself has no ascender of its own (`1r_l08_sign11_0_or_6.jpg`). Theirs is the more careful reading. | s either way |
| 1r b, 1r f, 1v a: the reversed-s heads | 9 at some, 5 at others, emended 9→5 | written 5\|9 | The same hooked head with a descender is used for undoubted 5s (in 55 = l). The 9→5 "emendations" are really readings of one letter form. | m, g, h, n: none on identity |
| 1v a, sign 22 | w (c over 8) | 8 or w | Agree w. | f |

Nowhere did I find a sign they read that the image does not show, or miss one. The 1r-1v digit transcription is confirmed.

### 5b. Clear text, difference by difference

| Place | Theirs | Mine | Image supports |
|---|---|---|---|
| 1r ll. 1-3 | not transcribed | "So che V.S. applicherà? tutto lo? suo maggiore studio? in un negozio che mi sommamente? preme." | Mine is an addition; words doubtful but the sense (a matter that presses him) is clear. |
| 1r l. 4 "mi fa sapere" | same | same | Both. |
| 1r l. 5 after run a | "del March[ese?](?) [...] gli fu scritto" | "d[e]l? un? amico ch[e]? li fu scritto" | Neither secure. The page has "dl", then a word of minims "am", then "anco" with a mark over the o, then a tall looped letter. "li fu scritto" is agreed. Unsettled (`1r_l05_disputed_amico_or_marchese.jpg`). |
| 1r l. 6 before run b | "[...] giunse(?) del la(?)" | "a? Vienna? che la" | The word after "giunse/Vienna" is written exactly like "che" in line 1 ("So che"): I read "che", not "del". For the word before it: a separate mark in the margin, then a looped initial, a dotted i, and minims ending in a flourish; no tall s is visible, which tells against "giunse" but does not prove "Vienna" (`1r_l06_disputed_vienna_or_giunse.jpg`). |
| 1r l. 7 "scritto per domandarmi" | same | same | Both; clear. |
| 1r l. 8 between runs c and d | "e(?)" / "per(?)" | "di" | One tall looped letter group. "di" fits "la permissione di ritornare"; nothing settles it. |
| 1r l. 10 before "marito" | "dal(?) mio(?)" / "dell' uno(?)" | "dal? suo?" | Unsettled; the first letter of the second word has a long head stroke (s or a minim with entry). |
| 1r ll. 11-14 | not transcribed | partial: "...onde V.S. vede? bene? ... mi fa? credere? ch'insinuasse? il Principe ... ci fanno vergogna" | Mine is partial; "ci fanno vergogna" is the most legible piece. |
| 1v l. 1 | tsv: "[...] Cristoforo(?) e"; notes: "e di offensione che [...] e" | "e ci offen[...]? [che?/nella?] reputatione e" | The word before "e" ends in a clear "-tione" with a dotted i, preceded by "-puta-": "reputatione", not "Cristoforo". The earlier word starts "offen-"; its ending is not clear enough to choose between "offende", "offensione" and others (`1v_l01_offen_reputatione.jpg`). |
| 1v l. 3 | "et l'Al[tezza?](?) [...] grande" | "et? [...] dell'? grande e [...]" | Unread by both. |
| 1v l. 4 | "et simili calunnie" (medium) | "e che simili calunnie" | "simili calunnie" agreed, independently. |
| 1v l. 5 | "non fussero riprovate(?). Però V.S." | "non fussero? riportate?. Però V.S. ci adopri?" | Agree on "non fussero", "Però V.S."; the participle is doubtful in both. |
| 1v ll. 6-14 | "Se mai potessi(?) haver bisogno che V.S. per mio servizio [...] viaggio a Düsseldorf(?)" | full lines (see Part 1) | "per mio servizio facessi un viaggio a Dusseldorf" is clear; "Dusseldorf" needs no query. My lines 6-9 (destrezza, non risparmiando a veruna fatica, efficacia, amore fedele e sincero) and 12-14 (crederei che fussi bene che V.S. con scriverli o farli dire) are additions. |

### 5c. Decode and who says what

- Decode: identical words (l'Elettor[e] Palatino, mia figlia mi havea, permission[e], ritornare qua, separarsi, marito, mia et di mia figl[i]a). Same two unexplained slips (w2 for the final e of "permissione"; w4 for the i of "figlia"), found independently.
- Who says what: we agree. The Elector informs Cosimo ("mi fa sapere"); something was written to the Elector ("li fu scritto"); its content is that the daughter had written to Cosimo to ask leave to return and separate. I would add, from text they did not read: the opening sentence frames it as "un negozio che mi sommamente preme"; 1r l. 14 has "ci fanno vergogna"; and the closing third of 1v is a set of instructions to Montauti (all his skill, no effort spared, a journey to Düsseldorf if needed, writing to or having someone told).

## Part 2, 6. The proposed headline

Proposed: "Cosimo reports in cipher a story, passed on by the Elector, that his daughter had asked leave to come home and separate, and treats it as an offence."

| Part | On the page? | Rests on |
|---|---|---|
| The Elector is the one telling Cosimo | Yes. Clear "mi fa sapere" + cipher "L'ELETTOR[E] PALATINO". | "Elettor": 6w written once with an 8-like loop (a reading of the w form, not an emendation); one e not written. "Palatin-": key v2 + w6 = i (key v3). The final o: context value ww or an 8→0 emendation. "Elettore" with final e: only if a 6-shaped sign is taken as w. The identification of the Elector is safe without any of these. |
| The story is that she asked leave ("scritto per domandarmi la permissione") | Yes. "MIA FIGLIA MI HAVEA" (cipher) + "scritto per domandarmi" (clear) + "la PERMISSION[E]" (cipher). | "mia", "mi": w6 = i (key v3). "havea": 91 = u (key v3) or 51 (key v2) by 9/5; h needs the reversed-s head read as 5. "permission-": o from ww (context only); the last letter is written a, not e. |
| To return and to separate from her husband | Yes. "RITORNARE QUA e SEPARARSI dal [...] MARITO". | "ritornare": o from ww (context). "qua": q from 62 (context), u from 91 (key v3) or 51. "separarsi": key v2 alone, no emendation. "marito": o from ww (context). The possessive ("suo"?) is not settled. "come home" is fair for "ritornare qua"; "to Florence" is an inference from "qua". |
| Cosimo calls it an offence and a calumny | Partly. "offen[...]" (1v l. 1, clear text, word form unsettled), "ci fanno vergogna" (1r l. 14), "simili calunnie" (1v l. 4, read by both of us). | Clear text only, no key values. But "simili calunnie" means "such calumnies": it classes talk of this kind as calumny; there is no sentence that names this report as false. "treats it as an offence" stands; "calls it a calumny" is a fair gloss only if worded as "speaks of such calumnies". |
| "reports in cipher" | Partly. | The verbs ("mi fa sapere", "li fu scritto", "scritto per domandarmi") are clear text; the cipher covers the names and the key nouns and verbs. |

Verdict: the headline stands in substance. Every element is on the page; none depends on the context-only values for its identity (they supply single letters in words already fixed), and the only emendations are the 9→5 / 0→6 readings of one letter form. Two adjustments: say "partly in cipher", and say that the report reached Cosimo through the Elector from someone who wrote to him (the third link is on the page as "li fu scritto", its author unread).

Wording I would defend:

> "In an undated letter partly in cipher (after the 1691 marriage), Cosimo III tells his envoy Montauti that the Elector Palatine has let him know of a report, written to the Elector, that Cosimo's daughter had written to Cosimo asking permission to return home and separate from her husband. Cosimo says such talk shames and offends his and his daughter's reputation, speaks of 'such calumnies', and asks Montauti to use all his skill against it, if need be by a journey to Düsseldorf."

Do not write that she asked to separate, nor that Cosimo denied it in so many words.

## Part 2, 7. Two other runs the notes call "read whole"

Chosen: 28v d ("toscani") with its neighbour 28v c ("corte"), and 70v a ("agosto"). I transcribed each from the image before opening their digits.

| Run | My digits (blind) | Theirs | Decode | Depends on |
|---|---|---|---|---|
| 28v c | 44 w w(8-like) 64 6w w4 | 4 4 w [8/w] 6 4 6 w w 4 | c o r t e | o from ww (context only); otherwise key v2 |
| 28v d | 6w ww 66 44 w2 [5/9]w w6 | 6 w w w 6 6 4 4 w 2 [9/5] w w 6 | t o s c a n i | o from ww (context); n needs the hooked head read as 5; i from w6 (key v3) |
| 70v a | w2 [9/5]0 ww 66 6[8=w] 41 | w 2 9 0 w w 6 6 6 [w/8] 4 1 | a g o s t o | g by 9→5; first o from ww (context); t needs the 8-like loop read as w; last o key v2 |

Result: both runs confirmed sign for sign; no difference in digits. Both lean on ww = o, which is not attested under any interline: the readings are compelling as Italian, but they are context readings, as the notes say.

## What remains open

- The clear text at 1r ll. 5-6 (who wrote to the Elector; "amico" / "Marchese"; "Vienna" / "giunse"), 1r ll. 11-13, and 1v ll. 1 and 3. A palaeographer reading of 1r-1v is still the step before any quotation.
- Whether the c-and-loop sign and the bare 6 are distinct at 1r a sign 15 (Elettor vs Elettore): it does not affect the identification.
- ww = o and 62 = q remain context values; nothing here tests them independently.
