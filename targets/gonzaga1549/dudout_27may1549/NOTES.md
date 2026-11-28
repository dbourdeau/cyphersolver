# 27 May 1549, Charles V to Ferrante Gonzaga: c. 31v decoded with a frozen key (KB5), measured once against the contemporary decipherment (cc. 12r-12v)

Contributed by Brice Dudout, working with Claude (Anthropic), 17 Nov 2026. Status: **decoded, not read** (one pre-registered test,
rank 1/201, letters 0.648, under the 0.85 line). Nothing here is emended and nothing is a validated key. c. 31v is now used up (burnt) for us.

**Credits.** Malcolm McBratney (PR #684, `../mcbratney_27may1549/`) located this letter, its cipher cc. 31-36 and its contemporary
decipherment cc. 12-15, and published the sign table (`key_cv1549.tsv` = `sign_table.tsv`) that we compared our key with. Our test only
uses the page he left untouched (31v).

## Why this test
The 4 Jul 1549 tests (`../dudout_4jul1549/`, PR #763) left two corrections seen on burnt lines and never applied: in the 4 July copyist's
labels, `g` (the sign with a descending loop) reads **y**, and `4` reads **o**. KB5 = KB4 + those two changes, nothing else. The point was to
test KB5 once on a page of another 1549 letter never transcribed or decoded by anyone.

## Prior art (checked 17 Nov 2026, before transcription)
- PR #684 (McBratney, merged 16 Nov): c. 31r only transcribed and decoded (64.1% of units, "decoded, not read"); decipherment transcribed for
  c. 12r lines 1-15 only. His notes: 31v-36r "not transcribed or decoded"; his PR body mentions a separate mechanical pass on cc. 31v-36v
  at 38.71%, not filed. Nobody has read 31v; no reservation, no open PR or issue on this letter (`gh` search, 17 Nov).
- What we had seen before freezing: the PR body, `FREEZE.txt`, a few located lines of `PRIOR_ART.md` and `NOTES_mcbratney.md` (the list of cipher
  pages). **Not opened before our transcription was frozen:** `KEY_NOTES.md` (its list of missing values comes from the 31v-36v pass),
  the decipherment, reading, decryption, ledger, analysis and score files. Our own session of 29 Oct had looked at cc. 12-15 at page scale
  (no transcription, no value taken); none of our keys was learnt on this letter.
- The plaintext is not new: the decipherment is in the same file. Bertomeu Masiá 2009 still unchecked, as for the other letters here.

## Protocol (originals in French; frozen files and sha256 in `FREEZE.txt`)
1. `key_dudout_kb5.tsv` and `PREREG_C14_fr.md` frozen first (sha256 489a213b..., d5a6e857...). Portion = all the cipher of c. 31v
   (16 lines, then the paragraph "Hase visto el discurso hecho ..." with 10 more lines). Pass = letters >= 0.85 AND >= best of 200 controls + 0.30.
2. Two blind passes on native-resolution IIIF crops: **pass A by a second sub-agent** that saw no key, no reference and no decode
   (`27may1549_31v_signs_passA.txt`, hashed before pass B was written); pass B by us without opening A. A wrote in the label convention of the
   4 July transcriptions, B in the convention of the 9 Dec chancery hand. Agreement after mapping the two conventions: 316/456 = 0.693.
   Arbitration rules, written before any decode (`27may1549_31v_signs.txt` header): the 4 July convention (the one KB5 is defined on);
   the round sign with a curled stem = `th` (as in the 9 Dec training file; McBratney's own transcription of 31r also calls it theta),
   the straight 9 = `q`; unresolved reading differences go to A. 454 tokens; clear words and Latin code words kept as anchors, not tokens.
3. Reference (`27may1549_12r-12v_decipherment_passage.txt`) transcribed by us from cc. 12r-12v **after** the transcription was frozen.
   Three segments bounded by the original's clear words ("Hase visto el discurso hecho", "y por", "que estos dias ... hermano suyo",
   "como vos mismo"). The start of the page is mechanical (161 tokens of 31r after "En lo demas tocante", counted on McBratney's 31r file,
   times 488/322 letters per token, cut at a word boundary).
4. One measurement, `score_27may1549.py`, seed 527.

## Result
`27may1549_score.txt`: 454 tokens, key coverage 0.907, reference 805 letters.
**Letters 0.648, words 0.382; controls max 0.209 / 0.075; rank 1/201. Under 0.85: PARTIAL, not validated.**
Information only, computed after and declared in the PREREG: the same tokens with KB4 give 0.631, so g = y and 4 = o add +0.017.
Post hoc (information only): the page in fact begins at "-rable lo qual le podreys", 9 words after the mechanical start; with that exact start, 0.693.
Daniel's strict count (`27may1549_reading_ledger.txt`, reference words classed by the alignment): with the exact start, 79 sure + 43 probable
of 175 words; **sure = 0.451** (sure + probable 0.697). Far under 0.95, and under the 0.65 line: decoded, not read.

## Why it falls short (seen after the measurement; nothing re-measured)
The key is the right one (margin +0.44 over the best control); the losses are in the transcription labels of this hand, not in g/4:
- the Latin-looking `x` (crossed strokes, 17 tokens) has no value in KB5, and `x` (closed ∞) is right only 4 times out of 13: in this hand
  the two forms are not separated the way our labels separate them;
- `co` (ω closed at the top, 6), `th-` (barred round sign, 6), `~`, `u` and `X` have no or wrong values;
- `7x` (y with a barred stem) = se is right 15/19, `ap` = n 30/33, `g` = y 10/13.
- the Latin code word `oblimco` stands for "el principe Doria" (decipherment 12v: "el principe doria en la mar").

## The passage (decipherment cc. 12r-12v, our transcription, abbreviations expanded)
"[tole]rable, lo qual le podreys embiar a dezir muy deveras, porque en semejantes cosas que acase han offrecido se ha visto que quando se le habla
viuamente se llegan ala razon, pero esto sea de manera que no se meta mano en las armas por el inconviniente y estoruo que se podria seguir alas
otras cosas publicas y particulares mas que al presente se offrece; pues auisandonos aca delo que de mano en mano passare, se os podra rescreuir
lo que deueys hazer mas adelante, conforme alo que se entendiere del stado y progresso delas de franceses, señaladamente con Inglaterra, y tambien
del effecto que haura hecho el principe Doria en la mar. Hase visto el discurso hecho por Nicolo de Rison(?), señor de Cloua(?), cerca de inuadir
la Prouença y Delfinado, con todo lo de mas que de su persona nos escreuis; y porque estos dias passados vino aqui un hermano suyo a proponernos
de si el mesmo desino, y hallandole facil y de poco fundamento y sustancia en sus palabras, se le rechaço la platica, ala qual el tiempo y
necessidades en que nos hallamos dan mal lugar, como vos mismo lo podeys considerar."
(uncertain in our reading of the decipherment: the two names, "paces", "acase".)

English (working translation, unchecked): "... [in]tolerable, which you may send to tell him in earnest, for in such matters as have arisen
it has been seen that when he is spoken to sharply they come to reason; but let this be done so that no hand is laid to arms, because of the
harm and hindrance that could follow to other public and private affairs, more than at present arise. Keep us informed of what happens from
time to time and you will be told what you are to do next, according to what is learnt of the state and progress of the French affairs,
especially with England, and also of the effect of Prince Doria's action at sea. We have seen the plan made by Nicolò de Rison(?), lord of
Cloua(?), to invade Provence and the Dauphiné, with all you write of his person; and since a brother of his came here lately to propose the same
design to us, and we found it light and of little foundation and substance in his words, the proposal was turned down, for which the time and
the needs in which we find ourselves leave little room, as you yourself can judge."

Images: Biblioteca Estense Universitaria / Lodovico Media Library (CC BY-NC-SA), records bbdff1f6-f75f-44e1-b9d0-c66a83a9a7a9 (cipher) and
968f7688-4b71-44f2-9954-737adabf92c3 (decipherment); used for study only and not reproduced here.
