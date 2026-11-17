# Codex 533, ff. 1r-1v: blind verification, Part 1 (frozen before opening the first agent's notes)

Object: University of Pennsylvania, Kislak Center, Ms. Codex 533, first letter, folios 1 recto and 1 verso. Autograph of Cosimo III, Grand Duke of Tuscany, to Anton Francesco Montauti. No date line; the letter breaks off at the foot of 1 verso.
Images read: `sources/raw/montauti_penn/codex533/full/1r.jpg` and `1v.jpg` (4514 x 5717, already full size; nothing fetched). Crops in `crops/`.
Reader: verifier agent, 14 Nov 2026, from the images only. Key files opened: `systemB/key_v2.json`, `round4/key_v3.json`, `round4/key_v3_context.json`, `systemB/pairs_534_f14r.tsv` (Codex 534 interline evidence) and `systemB/fixed.json`.

Contamination to declare: the `_sources` note inside `round4/key_v3_context.json` names some 1r words as examples ("ritornare qua" on 1r; also "Palatino", "marito", "Dusseldorf", "havea"). I read those notes before the image. So my readings of those words are not fully blind. "mia figlia", "permission-", "separarsi", "mia et di mia figlia", "calunnie" and the whole clear text were not named anywhere I had opened.

Conventions. Clear text: `[ ]` expansion or editorial supply, `?` after a doubtful word, `[...n]` an unread word of about n letters. Cipher: pairs of digits, `w` = the eleventh sign (a c-shaped stroke with a closed loop after it; on this page the loop often looks like a 6, and when two w follow each other the second is often only an 8-like loop). Doubtful digits as `5|9` (first is my reading).

## 1. Transcription, line by line

### 1 recto

Heading, top left, alone: `S[ignor]? Dott[o]re?` (salutation, doubtful)

1. So che V[ostra] S[ignoria] applicherà? tutto lo? suo
2. maggiore studio? in un negozio
3. che mi sommamente? preme. / Mi
   (I take the first word of line 4, "mi", as starting the new sentence; the hooked mark in the left margin of line 3 is unexplained)
4. fa sapere `55 21 55 6w 6w 41 64 6|w 4 60 11 55 w2`
   - the third glyph group `6w` is written 6 + a c-with-loop sign with a long tail; the fourth `6w` is 6 + c with an 8-like loop; the group I give as `6|w 4` is a 6-shaped sign joined to the long crossbar of the preceding 4: read literally it is 64, as a w it is w4
5. `6w w6 5w 4 8|0` d[e]l? un? amico ch[e]? li fu scritto
6. a? Vienna? (or "[...6]", 2 strokes plus a word of about 6 letters; "giorni" also possible) che la `5|9 6 w6 w2 4w 31 5|9 0 55 31 11`
7. `5|9 6 w6 5|9 2 11 9|5 1 21 11` scritto p[er] domandarmi
8. la `60 21 64 5|9 6 31 66 w6 ww 5w w2` di `64 31`
   - `ww` here is c6 followed by a c with an 8-like loop
9. `6w ww 64 5w 11 64 w4 6 2 9|5 1 11` e `66 w4 60 11`
10. `64 11 64 66 31` dal? suo? `5|9 6 11 64 31 6w ww` onde
11. V[ostra] S[ignoria] vede? bene? quell[...3]? [...6] e? [...6]? (about 4 words unread)
12. mi fa? credere? ch'insinuasse? il Principe e
13. da un intrigo? nell'[...4]? subbietto? (doubtful throughout)
14. una? simile ci fanno vergogna, ch'el[...]

### 1 verso

1. e ci offend[...4]? nella reputazione e
2. `5|9 6 w6 w2 21 6w 46 w6 5|9 6 31 11 4 8|w 3|7 1 5 0 55 w 4`
3. `w2` et? [...2] dell'? grande e [...9]? [...7]? del pregio?
4. di [...7] e che simili calunnie ne[...5]?
5. non fussero? riportate. Però V[ostra] S[ignoria] ci adopri?
6. tutta la sua maggiore destrezza? e accuratezza?
7. non risparmiando a veruna fatica, e
8. con ogni efficacia, e così mi voglia d[are]? testim[onianza]?
9. dell suo amore fedele e sincero, il quale
10. a mi? sommamente spe[r]o? Se mai lo? potesse?
11. essere? bisognio che V[ostra] S[ignoria] per mio servizio
12. facessi un viaggio a Dusseldorf. Crederei?
13. che fussi bene che V[ostra] S[ignoria] con scriverli
14. o farli dire del mio sentimento?, ho? questi? [breaks off]

## 2. Decoding (key v3 alone, then the two context-only values)

Key v3 = key v2 plus w6 = i and 91 = u. Context-only values, kept apart: ww = o and 62 = q.
Digits the hand confuses: 5/9 (here the 5 is written as a reversed-s form with a descender, the same form as the undoubted 5s in 55 = l, so "9" readings are weak), 3/7, 0/6. Letters that depend on a doubtful digit are marked with a star.

| Run | Place | Digits (my reading) | Key v3 alone | + context values | Reading |
|---|---|---|---|---|---|
| A | 1r 4-5 | 55 21 55 6w 6w 41 64 [6/w]4 60 11 55 w2 6w w6 5w 4[8/0] | l e l t t o r [r or e*] p a l a t i n [o*] | same | l'El[e]ttore Palatino. One e is not written (or I missed a sign); the e after "ttor" depends on reading a 6-shaped sign as w; the final o needs 48 read as 40 |
| B | 1r 6 | [5/9]6 w6 w2 4w 31 [5/9]0 55 31 11 | m* i a f i g* l i a | same | (la) mia figlia. i from w6 is a key v3 value |
| C | 1r 7 | [5/9]6 w6 [5/9]2 11 [9/5]1 21 11 | m* i h* a u e a | same | mi havea. u from 91 (v3), or from 51 (v2) if the 9 is a 5: either way u |
| D | 1r 8 | 60 21 64 [5/9]6 31 66 w6 ww 5w w2 | p e r m* i s i [ww] n a | p e r m i s i o n a | permisiona: "permission[e]" with the last letter a, not e. The o depends on ww (context-only) |
| E | 1r 8-9 | 64 31 6w ww 64 5w 11 64 w4 62 [9/5]1 11 | r i t [ww] r n a r e [62] u a | r i t o r n a r e q u a | ritornare qua. The o and the q are both context-only values |
| F | 1r 9-10 | 66 w4 60 11 64 11 64 66 31 | s e p a r a r s i | same | separarsi. Entirely key v2 |
| G | 1r 10 | [5/9]6 11 64 31 6w ww | m* a r i t [ww] | m a r i t o | marito. The o is context-only (written c6 + 8-like loop) |
| H | 1v 2-3 | [5/9]6 w6 w2 21 6w 46 w6 [5/9]6 31 11 4[8/w] 31 [5/9]0 55 w4 / w2 | m* i a e t d i m* i a [48] i g* l e a | same | mia et di mia figl[i]a. f needs the 8-like loop read as w (4w); the second-last letter decodes e (w4) where Italian needs i |

What the context-only values add: three letters o (in "ritornare", "marito", "permission-") and one q (in "qua"). None of them changes who or what the passage is about; every word they touch is already fixed by its other letters (r i t _ r n a r e, m a r i t _, _ u a after "ritornare").

## 3. Continuous text and translation

Italian (cipher in capitals, decoded; doubt marks as above):

> S[ignor]? Dott[o]re?
> So che V.S. applicherà? tutto lo? suo maggiore studio? in un negozio che mi sommamente? preme. Mi fa sapere L'EL[E]TTORE PALATINO d[e]l? un? amico ch[e]? li fu scritto a? Vienna? che la MIA FIGLIA MI HAVEA scritto per domandarmi la PERMISSION[E] di RITORNARE QUA e SEPARARSI dal? suo? MARITO; onde V.S. vede? bene? quell[...] [...] ... mi fa? credere? ch'insinuasse? il Principe e da un intrigo? nell'[...]? subbietto? una? simile ci fanno vergogna, ch'el[...] e ci offend[e]? nella reputazione e MIA ET DI MIA FIGL[I]A et? [...] dell'? grande e [...] [...] del pregio? di [...] e che simili calunnie ne[...]? non fussero? riportate. Però V.S. ci adopri? tutta la sua maggiore destrezza? e accuratezza?, non risparmiando a veruna fatica, e con ogni efficacia, e così mi voglia d[are]? testim[onianza]? del suo amore fedele e sincero, il quale a mi? sommamente spe[r]o?. Se mai lo? potesse? essere? bisognio che V.S. per mio servizio facessi un viaggio a Dusseldorf, crederei? che fussi bene che V.S. con scriverli o farli dire del mio sentimento?, ho? questi? ... [breaks off]

Conservative English:

> [Signor Doctor?]
> I know that Your Lordship will apply all your greatest care to a business that presses me greatly. THE ELECTOR PALATINE lets me know, [through? / from?] a friend, that it was written to him [at? Vienna?] that MY DAUGHTER HAD written to me to ask my PERMISSION TO RETURN HERE and TO SEPARATE from [her?] HUSBAND; so Your Lordship sees well [...] [... makes me believe that the Prince insinuated it? ... and by a ...? ... a similar ...? ...] they put us to shame, [...] and it offends us in the reputation both MINE AND MY DAUGHTER'S, [and ... great ... of the esteem? of ...] and that such calumnies [...] should not be repeated. So Your Lordship is to apply all your greatest skill and care, sparing no effort, and with every effectiveness, and so give me proof? of your faithful and sincere love, which I greatly hope for?. If it should ever be necessary that Your Lordship, for my service, make a journey to Düsseldorf, I would think it well that Your Lordship, by writing to him or having him told of my feeling?, [...] [breaks off]

Answers, from the text alone:

- Who is telling what to whom. Cosimo (first person: "mi fa sapere", "domandarmi", "mia figlia") writes to Montauti ("V.S."). He reports that the Elector Palatine has let him know something. Words: "Mi fa sapere L'ELETTORE PALATINO". Confidence: high for "mi fa sapere" and for the cipher "l'Elettore Palatino" (one e short); moderate that "mi" begins the sentence and that the Elector is its subject (Italian verb-subject order; no other subject is available).
- Who is said to have written or said what. Layered: the Elector lets Cosimo know that something "li fu scritto" (was written to him), possibly through or from a friend ("d[e]l? un? amico", doubtful); what was written to the Elector is that Cosimo's daughter "mi havea scritto per domandarmi la permission[e] di ritornare qua e separarsi dal suo marito" (had written to Cosimo to ask his permission to return here and to separate from her husband). Confidence: high for the chain Elector, "li fu scritto", daughter "mi havea scritto per domandarmi"; low for "amico" and "Vienna".
- How the matter about the daughter is presented. Not as a fact Cosimo asserts, not as his own request: it is a report, at second or third hand, of a story that she had asked him for leave. He then treats such talk as shameful and offensive ("ci fanno vergogna", "ci offend[e] nella reputazione e mia et di mia figlia") and calls it calumny ("simili calunnie", 1v line 4, read clearly). I take it as a slander he rejects, but I note that the explicit sentence "this is false" is not among the words I could read; the rejection is carried by "vergogna", "offend-", "calunnie". Confidence: high that he resents it as damaging to reputation; moderate that "calunnie" refers to this story (it stands six lines later, but no other story is in the letter).
- What he wants Montauti to do. Apply all his skill and effort, sparing no labour ("ci adopri? tutta la sua maggiore destrezza? ... non risparmiando a veruna fatica"), apparently so that "simili calunnie ... non fussero? riportate" (such calumnies not be repeated), and, if need be, travel to Düsseldorf on Cosimo's service ("per mio servizio facessi un viaggio a Dusseldorf") and write to or have someone (him: "scriverli o farli dire", probably the Elector) told of Cosimo's mind. Confidence: high for the effort and the Düsseldorf journey; moderate for the "non fussero riportate" purpose clause.

## 4. Date (from the text only)

- The Elector Palatine is the daughter's husband's side: Cosimo's only daughter, Anna Maria Luisa de' Medici, married Johann Wilhelm of Pfalz-Neuburg, Elector Palatine, in 1691; the court sat at Düsseldorf. "l'Elettore Palatino", "mia figlia", "dal suo marito" and "un viaggio a Dusseldorf" together put the letter after the marriage (June 1691) and before Johann Wilhelm's death (June 1716). Note that the letter calls the Elector by title and the husband "suo marito" separately; it does not say outright that they are the same person, though that is the natural sense.
- "il Principe" (1r line 12, doubtful) is unidentified; it could be one of Cosimo's sons (Ferdinando or Gian Gastone) or another prince.
- "a? Vienna?" (1r line 6), if right, would point to Montauti or the informant at the imperial court.
- No other dating element read. Narrower dating must come from the volume's other dated letters, not from this page.
