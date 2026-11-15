# Bare System B passages, Codex 534 and Codex 531 (round 4, 13-14 Nov 2026)

Read by the agent (Claude) on 13-14 Nov 2026 from full-size IIIF images of University of Pennsylvania
Oversize Ms. Codex 534 (secretariat dispatches to the envoy Antonio Francesco Montauti at Vienna) and Ms. Codex 531.
Nobody deciphered these passages on the page: they carry no letters between the lines. The secretariat clerk who
enciphered them, and Montauti or his secretary who deciphered them at Vienna in 1694, read them first. This is a
reading with key v2. Key v2 itself was rebuilt from the recipient's interlinear decipherments on Codex 534 ff. 14r
and 15r, so this is not an independent solution of the system.

Key: `systemB/key_v2.json`, sha256 64783ab8... (checked by the script), **used unchanged**; plus 91 = u as given in the brief.
Script: `round4/bare_scripts/bare_decode.py` (writes `round4/bare_transcriptions.tsv`).
Images: `round4/bare_crops/` (full-size canvases 114r-118r, 531 f. 4r region, `SHA256SUMS`; working line crops under `lines/`).

## What was checked and what was not

- **Checked on the image:** every group listed in the TSV was read from full-size crops (about 1:1 or enlarged),
  and every doubtful group was re-cropped at higher zoom before it went into the table.
- **Not done as asked:** the two independent passes (forward, then backward, each written down before comparing)
  were not done for every line. I made one forward pass, then re-read each doubtful cluster on a fresh crop. The
  backward pass was done only for Codex 531 f. 4r and the 115r lines 1-4. Treat P1 (f. 114r) as a single reading.
- **Which sheet:** the f. 114r cipher is on the large sheet f. 114 itself (canvas "114r" shows that sheet alone).
  The 114v cipher line is on the same large sheet. 115r and 116r-v are full-size leaves; no small sheet lies on them.
- **Ff. 117r-118r** (letter of 15 May 1694, "Sig. Abate. Conforme diedi...") are **not bare System B**. They hold another
  cipher (small digit groups, mostly 1-3 and 9) with a letter-by-letter decipherment between the lines. That is
  interlined, so it is out of scope here.

## Scribal habits seen on the image (observation), and what I conclude from them (inference)

1. *Observed:* adjacent groups that share a sign are often written with that sign once: `5w4` where the sense needs
   `5w w4` (n e), `6w2` for `6w w2` (t a), `441` for `44 41` (c o), `660` for `66 60` (s p), `560` for `56 60`,
   `551` for `55 51`, `w66` for `w6 66`. The TSV writes these as `5w+w4` etc. *Inference:* this is a writing
   habit, not a different group. Every case gives the letters the context needs.
2. *Observed:* in the f. 114r hand a 6 is sometimes closed into an oval that looks like 0 (zoom on line 5 `64 46 31`,
   "ordine"). So 0 and 6 must be told apart from the loop and the stroke. Where I could not, the group carries "?".
3. *Observed:* the groups **w6** and **ww** are not in key v2 but are frequent (15 and 14 times).
   - w6 stands where the sense needs **i** every time: figl-i-a (twice), Roman-i, Gr-i-mani, d-i lu-i (twice), esib-i-zione,
     d-i Savoia, impenetrabil-i, d-i, L-i-ege... (contexts in the TSV).
   - ww stands where the sense needs **o** every time: c-o-testa, matrimoni-o, P-o-l-o-nia, vescovat-o, c-o-n (twice),
     C-o-lonia (twice), esibizi-o-ne, circospezi-o-ne, s'-o-pponga, f-o-rza.
   - *Inference (not applied to the decoding):* w6 = i and ww = o. Both are new homophones for key v3. They also fit
     the earlier guess that Cosimo's "c6" in Codex 533 is w6. Earlier annealer guess "w6 = e?" is contradicted.
4. *Observed:* groups that contain 0 or 9 and are not letters: 10, 110, 104, 106, 116, 30, 90, 39, 13, 22, 27, and w0/0w.
   Several have three digits. *Inference:* System B has a small numbered **code list for names and titles** on top of
   the letter table (see the table of unknown groups below). The names Grimani, Savoia, Colonia, Liegi, Baviera and Polonia
   are spelled out letter by letter, as the brief expected.
5. **q:** no group stood where a q was needed. No candidate for q was found.

## P1. Codex 534 ff. 114r-114v, letter of 24 April 1694

- Writer: secretariat clerk, signed for the Grand Duke Cosimo III ("Al piacere di V.S. / Il Gran Duca di Toscana", 114v);
  dated "Di Firenze li 24 Aprile 1694" (114v). Addressee Montauti at Vienna.
- Clear text before the first run: "Quanto al contenuto loro io osservo che il più sostanziale riguardo i Negoziati ...";
  after the last run (114v): "... nascano delle amarezze, e pregiudicio ...".
- 17 runs, 296 groups (counting `a+b` as two). Decoded with key v2: 267 (90%). Read as Italian: about 85%
  (lines 2, 4, 8 and 14 are only partly read).

Decoded with key v2 (unknown groups in brackets), then normalized:

| line | decoded | normalized Italian |
|---|---|---|
| 1-2 | ac[ww]te staacortedelabategriman###o | a c[o]te(s)ta [a?] corte dell'Abate Grimani [...]o |
| 3 | [110]disauoia | il [110] di Savoia |
| 4 | d[w6]acasarecol[15]lla[10][w6]suafigl[w6]a | d'accasare col... [15]... [10]... sua figlia (middle not read) |
| 5-6 | sinordinealap / acecomeal | sì in ordine alla pace come al(la) |
| 7 | incumbenzedelabate | le incumbenze dell'Abate (sud.o) |
| 8 | rogacheperpartede[13] | [prova?] che per parte de' [13] |
| 9 | [22]che | al [22] che |
| 10 | [106]ilmatrimoni[ww] | da [106] il matrimonio |
| 11 | [110]conlae[0w]dipol[ww][ww]nia | di med.o [110] con la [e0w] di Polonia |
| 12 | [106]che | a [106] che |
| 13 | uescouat[ww]diliegeleletordicol[ww]nia | al vescovato di Liegi l'Elettor di Colonia |
| 14 | [22]hastacail[w6]stelesi[22]noze | il [22] ... (partly read; ends "le s[ue] nozze"?) |
| 15 | c[ww]nladetae[0w] | con la detta [e0w] |
| 16 | inl[w6]egeleletordic[ww]lonia | in Liegi l'Elettor di Colonia |
| 17 | fralaugustis[w6]mecacaseaeleletoraledibauiera | fra l'Augustissima Casa e l'Elettorale di Baviera |

English (clear text joined; brackets = not read or code):
"...the most substantial point concerns the negotiations at that court of Abbot Grimani [...], and to make clear the design
that the [110] of Savoy is supposed to have of marrying [...] his daughter, and what the said minister was promoting,
both regarding the peace and the solicitation of the intended reinforcements ... the commissions of the said Abbot ...
They serve as [proof?] that on the part of [13] it was hinted to the [22] that the marriage of the same [110] with the
[e0w] of Poland should not be approved by [106]; and it likewise displeased [106] that the Elector of Cologne should compete
for the bishopric of Liège ... the [22] ... his marriage, as is said, with the said [e0w], and that he does not desist from
pursuing his efforts in Liège, the Elector of Cologne, it may be doubted that between the most august House and the
Electoral [House] of Bavaria bitterness may arise ..."

What it concerns (inference): the Savoy marriage project for the King of the Romans and Abbot Grimani's part in it, and the
Wittelsbach affairs of spring 1694: Joseph Clemens of Bavaria, Elector of Cologne, seeking the see of Liège (elected there
in 1694), and a Bavarian-Polish marriage (Max Emanuel married Teresa Kunegunda Sobieska in 1694-95). [e0w] in "con la [e0w]
di Polonia" / "con la detta [e0w]" would then be "Principessa", and [110] in "matrimonio di med.o [110]" would be the Elector
of Bavaria, which clashes with "il [110] di Savoia" in line 3. One of the two readings of 110 is wrong, or 110 is a
generic title ("Duca"/"Elettore"); not settled.

## P2. Codex 534 f. 115r, letter of [day unclear] May 1694 (best passage)

- Writer: a second, clearer secretariat hand, signed "Al piacere di V.S. / Il Gran Duca di Toscana"; dated "Di Firenze
  [?] Maggio 1694"; addressed "Sig. Ab. Anton Fran.co Montauti / Vienna". Answers Montauti's letter of the 17th of the
  previous month.
- Clear before: "Con le notizie della ..."; after: "In conto dell'Amb.re di Venezia faccia ella benissimo ...".
- 12 runs, 149 groups. Decoded with key v2: 131 (88%). Read as Italian: about 95% (all but [90], [30], [104], [6] [39], [w0]).

Decoded with key v2: `esib[w6]zi[ww]ne | acotestacortedal[110]d[w6]sauoia | figl[w6]a | rederoman[w6] |
[90]dalabategr[w6]mani | d[w6]luipermanenzain | partidoue | [w0]dilu[w6] | [30]osegretec[ww]l[104] |
impenetrabil[w6] | apertura | circospezt[ww]ne[6]e[39]`

Normalized Italian (cipher in italics in the source sense; clear text plain):
"Con le notizie della **esibizione**, che si supponeva fatta **a cotesta corte dal [110] di Savoia** della sua di Lei
**figlia** per il **Re de' Romani**, onde mi nasce motivo di ringraziarne la puntualità e vigilanza di V.S., la quale spero
che si terrà sempre più attenta sopra tutto altro che possa costà progettarsi **[90] dall'Abate Grimani durante la di lui
permanenza in** coteste **parti, dove**, se bene le **[w0] di lui** negoziazioni passavano molto **[30] o segrete col
[104]**, non sono però a lungo andare **impenetrabili** le cose per la naturale **apertura** e poca **circospezione [6] e [39]**."

English: "With the news of the **offer**, supposed to have been made **at that court by the [110] of Savoy**, of his
**daughter** for the **King of the Romans**, I have reason to thank you for your punctuality and vigilance, which I hope
will stay ever more alert to anything else that may be planned there **[90] by Abbot Grimani during his stay** in those
**parts, where**, although **his** negotiations passed very **[30] or secret with the [104]**, things are not in the long run
**impenetrable**, given the natural **openness** and little **circumspection [6] [39]**."

What it concerns: the Duke of Savoy's offer of a daughter as bride for Joseph, King of the Romans, and Abbot (Vincenzo)
Grimani's negotiations at Vienna. *Inference:* [110] = "Duca" (fits "dal [110] di Savoia" here and "il [110] di Savoia" on 114r).

## P3. Codex 534 ff. 116r-116v, letter of 15 May 1694

- Same clear hand as 115r; dated "Di Firenze 15 Maggio 1694" (116v), signed for the Grand Duke.
- Clear before: "Circa poi a coteste occorrenze non s'intende veramente perché il Sig.r ..."; after: "Del resto mi saranno
  molto care quelle ulteriori notizie ...".
- 3 runs, 55 groups; decoded 49 (89%); read as Italian about 90%.

Decoded: `[27]si[ww]pongaprogetid[w6][116]c[ww]ntantaf[ww]rzamentre | atuti | unsigranbene`
Normalized: "... perché il Sig.r **[27] s'opponga [a'] progetti di [116] con tanta forza, mentre** sono manifesti gli utili
che **a tutti** deriverebbero dallo stabilimento di **un sì gran bene**."
English: "... why Signor [27] opposes the plans of [116] with so much force, while the advantages that would come **to all**
from the establishment of **so great a good** are plain." The text does not say what the good is; in context of the
surrounding clear text (wartime contributions, ruin of commerce) it is probably the peace or Tuscan neutrality (inference).

## P4. Codex 531 f. 4r, letter of 17 July 1694

- Secretariat hand, signed for the Grand Duke; "Di Firenze 17 Luglio 1694"; to "Sig. Ab. Montauti, Vienna".
- Clear before: "Starò anche caro che stia attenta per rintracciare, se alcun lume trapelasse, de' negoziati de ...";
  after: "... potendo importar molto l'averne qualche sentore."
- 1 run, 17 groups (forward and backward reading agree); decoded 16 (94%); read 100% except the code.
- Decoded: `l[10]colabategrimani` → "de' negoziati de**l [10] coll'Abate Grimani**" = "of the negotiations of the [10] with
  Abbot Grimani". *Inference:* [10] is the same person as [110] (the Duke of Savoy); the 531 group shows one 1 only.

## Unknown groups (key v2 has no value)

| group | count | contexts (folio, line of TSV) | value suggested by context (inference only) |
|---|---|---|---|
| **w6** | 15 | 114r 4,14,16,17; 115r 1-6, 8, 10; 116r 1 | i |
| **ww** | 14 | 114r 1,10,11,13,15,16; 115r 1,9,12; 116r 1 | o |
| 110 | 3 | "il [110] di Savoia" 114r; "dal [110] di Savoia" 115r; "matrimonio di med.o [110] con la..." 114r | title, probably Duca |
| 10 | 2 | "negoziati del [10] coll'Abate Grimani" 531; 114r line 4 (doubtful reading) | same as 110? |
| 106 | 2 | "approvato da [106] il matrimonio"; "non piaciuta a [106] che" (114r) | a person or court (Emperor or Pope?) |
| 22 | 3 | "insinuare al [22] che"; "il [22] ha..."; 114r line 14 doubtful | a person |
| 104 | 1 | "segrete col [104], non sono..." 115r | a person or court |
| 116 | 1 | "progetti di [116] con tanta forza" 116r | a person or power |
| 27 | 1 | "il Sig.r [27] s'opponga" 116r | a person's name |
| 13 | 1 | "per parte de' [13] sia stato fatto insinuare" 114r | a person or power |
| 90 | 1 | "costà progettarsi [90] dall'Abate Grimani" 115r | unclear (a word such as "anche"?) |
| 30 | 1 | "passavano molto [30] o segrete" 115r | a word ("riservate"?) |
| 39 | 1 | "circospezione [6] e [39]." 115r end | a word or name; "6" is a lone sign |
| w0 | 1 | "se bene le [w0] di lui negoziazioni" 115r | null? (sense complete without it) |
| 0w | 2 | "con la [e 0w] di Polonia"; "con la detta [e 0w]" 114r | with the preceding 21: a title (Principessa?) |
| 15 | 1 | 114r line 4, doubtful reading | — |

Groups with w that are not in key v2: **w6** (15), **ww** (14), **w0** (1), **0w** (2). No w8 was seen in these passages.
Alternatives tested on the shapes: for w6 the shapes allow only w6 or 6w (6w = t gives "figlta", "Romant", "Grtmani");
for ww the shapes allow ww, w4 or 40 misread (w4 = e gives "cetesta", "Pelenia"; the strokes have no 4 crossbar);
for 110/106/104/116 the shapes allow reading 11+0x or 1+10x, but no split gives a letter that fits the sense.

## Other bare System B in Codex 534 ff. 1-119 (survey, not read)

From contact sheets and zooms of all images 1r-118v (sub-agent survey, 14 Nov 2026; scratch notes only). From f. 37 on,
the cipher showing at the right edge of rectos 37r-113r is the underlying f. 114r; the entries below are on the small
sheets lying on top of it.

24v (~6 lines, 1691); 33r, 33v, 34r (~15, 8, 20); 34v (3); 42r (~8, letter ends 42v, 29 Nov 1692); 48r, 48v (~5, 4);
51r (3); 54r, 54v (~15, 6; 13 Jan 1692 Florentine style); 57v (~5); 63r, 63v (~5, 10); 65r, 65v (~10, 5); 66r-67v
(~3, 13, 15, 6; Pisa 9 Feb 1692); 73v (~5, 1 Aug 1693); 77r, 77v (~8, 5; 15 Aug 1693); 78r, 78v (~14, 2); 81v (1);
87r (2); 88v (2, 3 Oct 1693); 98v (~10, Ambrogiana 31 Oct 1693); 99r, 99v, 100r (~12, 16, 18); 100v (5, 7 Nov 1693);
102r (~6); 103v (~7, Nov 1693). Interlined (not bare): 14r, 15r, 21r, 117r-118r.
About 330 lines, i.e. several thousand groups, wait to be read.

## Recommended next step

Freeze key v3 = v2 + w6 = i, ww = o (and the shared-sign writing rule), then test it on a held-out bare passage written
down before decoding, e.g. 99v-100r (Oct-Nov 1693), with a proper forward and backward transcription.
