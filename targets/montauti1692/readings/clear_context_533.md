# Clear sentences around the cipher runs of ff. 25r, 26r, 28v, 56r-57r, 63r and 70v (16 Nov 2026)

Daniel Bourdeau's review of pull request #665 listed these six entries as "decoded, not read" because the clear text
around the runs was not transcribed. This file gives that clear text, sentence by sentence, with the cipher words
joined in, so that a reader can judge whether each entry builds a sentence. **Result: none of the six does.** Two
clauses read as clauses (26r, "Vorrei che V.S. ... mi mandasse ... RELATION[E] DEL ..."; 57r, "che V.S. haveva
scritto per ... viaggio ... DUSSELDORF"), but in every sentence most clear words are doubtful, and the six entries
stay "decoded, not read". The cipher words are unchanged (`key/key_v3.json`, `readings/runs_533.tsv`,
`readings/words_533_strict.tsv`; no key value and no cipher word was re-decided).

## Method

- **Images:** Penn's full-size images (4514 x 5717 px) of ff. 25r, 26r, 28v, 56r, 57r, 63r, 70v, already held; the
  lower 45% of f. 56v fetched once at full size on 16 Nov 2026 (IIIF region `pct:0,55,100,45`, HTTP 200); f. 62v
  only at 1600 px. No image is committed.
- **Pass B (blind):** a separate AI agent (Opus) given only crops of the text blocks (about 2000 px wide) and the
  full images, with a neutral instruction: transcribe the plain Italian, write [CIPHER] for each run, keep the
  punctuation, mark doubt. It saw no transcription, no file of this folder and no decoded word. Its whole text,
  as written: `readings/verify/clear_passB_blind_2026-11-16.md`.
- **Pass A:** the AI agent that packaged this file, reading the same crops and closer crops of the lines next to
  each run. **Pass A is not independent of pass B:** it was made after pass B's report had come in, and it knew the
  decoded words and the clear words recorded in `runs_533.tsv`. Agreement between the passes is therefore an upper
  bound.
- **Reconciled text:** a clear word is **sure** only when both passes read it the same and neither marks it
  doubtful; a word read differently, or marked by either pass, is **doubtful** and counts as a hole. Cipher words
  are in CAPITALS, as in `runs_533.tsv`; their status is the one in `words_533_strict.tsv`.
- **Sentence:** from the previous full stop to the next, as the rule asks. Full stops are rare in this hand. Where a
  sentence runs over many lines, the span compared word by word is the clause around the runs, bounded by a colon or
  semicolon that both passes saw; the rest of the sentence is given from pass B and not counted.
- Abbreviations expanded in square brackets; (?) = doubtful; [...] = illegible word; [..] = hole inside a word.
- Translations are by an AI agent. No person has checked any reading in this file.

## Summary

| entry | span compared | clear words, passes agree | clear words sure | clear words doubtful | cipher words sure (strict list) | status |
|---|---|---|---|---|---|---|
| L25, f. 25r | lines 3-10 (two clauses) | 37 of 39 | 20 of 39 | 19 | 0 of 4 | decoded, not read |
| L26, f. 26r | lines 7-9 and 9-15 | 25 of 31 | 17 of 31 | 14 | 4 of 18 | decoded, not read (one clause reads) |
| L28, f. 28v | lines 5-10 | 13 of 19 | 4 of 19 | 15 | 1 of 5 | decoded, not read |
| L56, ff. 56r-57r | 56r lines 5-10; 56v last line to 57r line 2 | 37 of 45 | 14 of 45 | 31 | 3 of 3 | decoded, not read (one clause reads) |
| L63, f. 63r | lines 3-6 (two sentences) | 10 of 11 | 6 of 11 | 5 | 3 of 6 | decoded, not read |
| L70, f. 70v | lines 3-7 | 20 of 27 | 7 of 27 | 20 | 0 of 1 | decoded, not read |

Counts by entry are in `readings/clear_context_533.tsv`. The 56r-57r answer to the review's question: the three
cipher words are sure, but the clear text around them is not. On 56r both passes read only 11 of the 32 clear words
of the clause the same way and without doubt, and the clause has no readable verb before the run; on 57r the
clause "che V.S. haveva scritto per [...] viaggio [a?] DUSSELDORF" reads, but its sentence begins on 56v in words
neither pass could read. We therefore do not dispute "decoded, not read" for 56r-57r.

## L25, f. 25r (Firenze li [1?] Luglio/Agosto, no year)

Lines (from the top of the text block, after "S[igno]r Abate"):

| line | pass A | pass B (blind) |
|---|---|---|
| 3 | nal[i] (?): et il mio servitio (?) onde (?) a | nal[e] (?): et il mio servitio (?) ond[e] (?) a |
| 4 | dovuto (?) al [run a] se / e (?) egli | dovut[o] (?) al (?) [CIPHER] e (?) egli |
| 5 | [run b] a' (?) Pontefici (?); ora (?) | [CIPHER] a' / n'i (?) Pontefice (?); ora (?) |
| 6 | sentirò (?) da V.S. mi dirà (?) il suo | sentirò / sentirà (?) da (?) V.S. mi dirà / darà (?) il suo |
| 7 | Prudente consiglio se un vecchio | Prudente consiglio se un vecchio |
| 8 | Greco io fusse (?) mi pare eccell[ent]e (?) per (?) | Greco io fusse / farei (?) mi pare eccell[en]t[e] (?) per (?) |
| 9 | V.S. (?) le (?) a (?) medesimo (?) [run c] | Vi / V.S. (?) le (?) a / i (?) medesimi / medesime (?) [CIPHER] |
| 10 | di V.S. mi [run d]. Il | di V.S. mi / ni (?) [CIPHER]. Il |

No full stop before line 10, so the sentence runs from line 1; lines 1-2 ("Ho io (?) fatt[o] fare un bello luce (?) a
di avere il [...] [...] del (?) Cardi-", pass B) are not compared.

Reconciled, clause of runs a and b (after the colon in line 3 to the semicolon in line 5):
> et il mio servitio(?) onde(?) a dovuto(?) al(?) [... 1] e/se(?) egli QU[..] a'(?) Pontefice(?);

Reconciled, clause of runs c and d (to the full stop in line 10):
> ora(?) sentirò(?) da(?) V.S. mi dirà(?) il suo Prudente consiglio se un vecchio Greco io fusse(?) mi pare
> eccell[ent]e(?) per(?) V.S.(?) le(?) a(?) medesimo(?) COSTÀ di V.S. mi ADDIT[A]SSI(?).

English (AI agent): "... and my service(?) whence(?) owed(?) to [...] and he [...] the Pontiff(?); now(?) I shall
hear(?) from V.S. ... tell me his prudent counsel, whether an old Greek I were(?), it seems to me excellent(?)
for(?) V.S. the same(?) THERE of V.S. YOU SHOULD POINT OUT(?) TO ME."

Judgement: the clause around runs c and d has a sure core ("il suo Prudente consiglio se un vecchio Greco io ...
mi pare") but no sentence: the words before COSTÀ are doubtful and COSTÀ and ADDIT[A]SSI(?) do not attach to a
readable construction. Runs a and b decode to no word. Not evidence against the decode; not a reading.

## L26, f. 26r (Firenze li 11 d'Aprile 1693, year probable)

| line | pass A | pass B (blind) |
|---|---|---|
| 7 | a 94 (?) [...] havere (?) ci [...] lo (?) Pace (?) che / egli (?) | a 94 a[nni] (?) havere (?) ci (?) campare (?) lo (?) Pace (?) egli |
| 8 | del quadro [run a] esser (?) l'unico (?) | il (?) quando [CIPHER] et (?) l'unico (?) / l'huomo (?) |
| 9 | d'unico (?) [run b]. Vorrei che V.S. con una | amico [CIPHER]. Vorrei che V.S. con una |
| 10 | Curiosità (?) mi mandassi (?) un [run c] | Curiosità / Carità (?) mi mandasse / mandassi (?) un (?) [CIPHER] |
| 11 | [run c] | [CIPHER] |
| 12 | [run c] il Dominio (?) [run d] | [CIPHER] il Panire / Dovere / Bonine (?) [CIPHER] |
| 13 | [run d] | [CIPHER] |
| 14 | venuto (?) accettato (?) V.S. che non mi dice | quello (?) accettato / accennato (?) V.S. che (?) non mi dice |
| 15 | tanto (?) quello nuovo (?) che V.S. mi diede (?) | tanto (?) quello nuovo (?) che V.S. mi diede / dirà (?) |

Reconciled, end of the first sentence (lines 1-9; lines 1-6 not compared; the opening "Sig[no]r Abb[at]e devo
accusare a V.S. la (?) sua (?) lettera" is read by both):
> ... egli(?) del/il(?) quadro/quando(?) SERVIVI[..] esser/et(?) l'unico(?) d'unico/amico(?) DE[..].

Reconciled, second sentence (from line 9; no full stop to the foot of the page; it goes on to f. 26v, not
transcribed):
> Vorrei che V.S. con una Curiosità(?) mi mandasse(?) un(?) RELATION[E] DEL [... 8] SCA[..]UG[..]IO[..]E ET
> il Dominio/Panire(?) HAVRÀ [... 1] CON L[..] venuto/quello(?) accettato(?) V.S. che non mi dice tanto(?) quello
> nuovo(?) che V.S. mi diede(?) ...

English (AI agent): "I would like V.S., with some curiosity(?), to send me a REPORT OF [... 8] ... AND the
Dominion(?) WILL HAVE [...] WITH [...] ... accepted(?) V.S., who does not tell me so much(?) that news(?) which V.S.
gave(?) me ..."

Judgement: the opening clause reads, and RELATION[E] DEL fits it ("mi mandasse una relatione del ..."): with the
noun "relatione" the article should be "una", and both passes see "un" or "un(?)", which is either Cosimo's
shortening or a misreading. After DEL come the eight groups without a value and three unread words, so the clause
stops being a sentence. Runs a and b decode to no word. Pass B also notes on line 7 a pair of signs, "94", written
like cipher digits between plain words; `transcriptions/reconciled_533_v2.tsv` has no run on that line. Not checked
further.

## L28, f. 28v (Firenze li 25 d'Ottobre, no year)

| line | pass A | pass B (blind) |
|---|---|---|
| 4 | [...] [...] molti [...] (?) | Francesi (?) Inglesi (?) [...] e molti Italiani (?) [...] |
| 5 | Particolari (?): V.S. [run a] | Particolari (?): V.S. (?) [CIPHER] |
| 6 | [run a] dell' [run b] | [CIPHER] dalla / della (?) [CIPHER] |
| 7 | [run b] et l'S[..] (?) [run c] et delli | [CIPHER] et a quello (?) [CIPHER] et delli / tutti (?) |
| 8 | [run d] et presso (?) V.S. [...] | [CIPHER] et spero / stesso (?) V.S. (?) [...] |
| 9 | vestiti (?) [...] il suo [...] et mantenere (?) | vestirà (?) i (?) petto (?) il suo (?) corteggio (?) et mante[ne]- |
| 10 | le Carrozze (?) [...] credentiali (?) della (?) | re (?) le Carrozze (?) poi / più (?) credentiali (?) delle / della (?) |

Neither pass is sure whether the mark after "Particolari" is a colon or a full stop; pass B finds the next full
stop only at "Pace." in line 16. The span compared is lines 5-10.

Reconciled:
> V.S.(?) [... 1] dell[a](?) [MIA?] FIGLIOLA et l'S[..]/a quello(?) CORTE et delli(?) TOSCANI et presso/spero(?)
> V.S.(?) [...] vestirà/vestiti(?) [...] il suo(?) [...] et mantenere(?) le Carrozze(?) ...

English (AI agent): "V.S. [...] of [MY?] DAUGHTER and [...] COURT and of the TUSCANS and [...] V.S. [...] will dress(?)
[...] his [...] and maintain(?) the carriages(?) ..."

Judgement: the cipher words fit the frame "dell[a] ... figliola et ... corte et delli toscani" (the daughter's court
and the Tuscans), but the sentence has no readable verb near them, 15 of 19 clear words are doubtful, and run a
decodes to no word. Not a sentence.

## L56, ff. 56r-57r (Firenze li 19 d'Ottobre, no year)

### 56r (run a, MIA FIGLIA)

| line | pass A | pass B (blind) |
|---|---|---|
| 1 | Devo accusare a V.S. la [...] (?) | Devo accusare a V.S. la gratiss[i]ma |
| 5 | Vedo / quello (?) con (?) breve (?) bugie (?); che Tanto (?) desiderasse (?) | quello (?) ci sono (?) bugie (?); che (?) Paolo (?) Bichesse (?) |
| 6 | Del giardino (?) a (?) [run] | Pagiardine (?) / bugiardine (?) [~] a (?) [CIPHER] |
| 7 | et V.S. senti (?) di (?) fare tutte le diligenze | et V.S. sentì (?) / Serà (?) di (?) fare tutte le diligenze |
| 8 | per vedere di cui (?) l'ha (?) quelli fratelli (?) | per vedere di cui (?) l'ha (?) quelli (?) Frates / Frati (?) |
| 9 | [..]no (?) sapere che (?) dicano (?) preparati (?) intellet[..] (?) | [..]no (?) sapere che (?) dicano (?) preparati (?) intellet[...] (?) |
| 10 | per vedersi (?) sento (?) di dire (?). | per vedersi (?) sento (?) di dire (?). |

The sentence runs from line 1 ("Devo accusare a V.S. la ... lettera delli 9 ...") to the full stop in line 10; the
span compared is the clause after the semicolon in line 5. Pass A's lines 8-10 were read after pass B and largely
follow it.

Reconciled:
> che(?) Tanto/Paolo(?) desiderasse/Bichesse(?) del giardino/Pagiardine(?) a(?) MIA FIGLIA et V.S. senti(?) di(?)
> fare tutte le diligenze per vedere di cui(?) l'ha(?) quelli(?) fratelli/Frati(?) [..]no(?) sapere che(?)
> dicano(?) preparati(?) intellet[..](?) per vedersi(?) sento(?) di dire(?).

English (AI agent): "that [...] [of the garden?] to(?) MY DAUGHTER, and V.S. [...] to make every effort to see whose(?)
those [brothers?] are(?) ... to know what(?) they say(?) ..."

Judgement: MIA FIGLIA stands where a noun phrase can stand, after a doubtful "a", but the words before it are read
differently by the two passes and there is no readable sentence. Not a sentence.

### 56v-57r (run a, DUSSELDORF)

| line | pass A | pass B (blind) |
|---|---|---|
| 56v last | se lo faccio (?) fare (?): Il (?) benissimo (?) | le so (?) [...] [...]: Il (?) [...] |
| 57r 1 | [..]sse (?) Ieri / Iermi (?) che V.S. haveva scritto per | [..]sse (?) Ieri (?) che V.S. haveva (?) scritto (?) per |
| 57r 2 | a ve (?) viaggio a (?) [run] | a cui (?) viaggio (?) ~ [CIPHER] |
| 57r 3 | Mentre lo accerto (?) V.S. che lo servirò (?) · | Mentre lo accerto (?) V.S. che (?) lo servirò (?) |

Pass B had the lower half of 56v at 1600 px only; pass A read it on the full-size region fetched on 16 Nov 2026.
Neither pass sees a full stop between the run and "Mentre" (capital, at the line start); the span compared is from
the colon on 56v to "Mentre".

Reconciled:
> Il(?) [...] [..]sse(?) Ieri(?) che V.S. haveva(?) scritto(?) per [a ve / a cui](?) viaggio(?) a(?) DUSSELDORF

English (AI agent): "... yesterday(?) that V.S. had written for [...] journey(?) to(?) DÜSSELDORF."

Judgement: the clause "che V.S. haveva scritto per [...] viaggio a DUSSELDORF" reads, and the cipher word fits it.
The "a" before the run is a single stroke that could also be a cipher sign, so the merged notes' "viaggio a
Dusseldorf" rests on a doubtful "a". The head of the sentence is unread. Not a sentence read with scattered holes.

## L63, f. 63r (Firenze li 23 Settembre, no year)

| line | pass A | pass B (blind) |
|---|---|---|
| 1 | Lo voglio sperar [...] da V.S.: | Lo voglio sperar l'altrieri (?) / sapendo (?) da / che (?) V.S.: |
| 2 | un [...] scrivere (?) [...] altra (?) [...] | un (?) scriver (?) apparison (?) altra (?) a veggio (?) / Regno (?) |
| 3 | Come nell'altro foglio / corso (?) et [run a] | Come nell'altro foglio (?) et [CIPHER] |
| 4 | [run a] a (?) i (?) Bethella (?) [run b] | [CIPHER] a (?) Bechelli / Bethelli (?) [CIPHER] |
| 5 | [run b]. ma quanto | [CIPHER]. ma (?) quanto |
| 6 | sarà (?) per [run c]. O quanto | sarà / sento (?) per [CIPHER]. O quanto |
| 7 | sarebbe desiderabile la Pace per | sarebbe desiderabile la Pace per |

Reconciled, first sentence (from "Come"; the colon in line 1 taken as the boundary; the previous full stop was not
found):
> Come nell'altro foglio(?) et LI TEMPI a(?) Bechelli/Bethella(?) [..]A[..] QUALCHE FACILITÀ.

Reconciled, second sentence:
> ma(?) quanto sarà(?) per ULT[I]MO(?).

English (AI agent): "As in the other sheet(?), and THE TIMES ... Bechelli(?) ... SOME EASE. But how much it will be(?)
FINALLY(?)." The next sentence, in clear and read by both: "O quanto sarebbe desiderabile la Pace per Italia" ("Oh,
how desirable peace would be for Italy").

Judgement: the merged notes gave the clear words before run a as "come voll[e] avviso(?)"; both passes now read
"Come nell'altro foglio(?) et". With LI TEMPI and QUALCHE FACILITÀ the first sentence does not construe (no verb is
read; "a Bechelli(?)" may be a name in clear between the runs). "per ULT[I]MO" would be the idiom "per ultimo"
(finally), but "ma quanto sarà(?) per ultimo" is not a sentence we can translate with confidence. Not read.

## L70, f. 70v (Pisa li 17 Gennaio 169[3])

| line | pass A | pass B (blind) |
|---|---|---|
| 2 | Primo ne farei (?) due righi (?) della M[aes]tà (?) | Primo (?) ne (?) farei (?) due righi (?) della M[aes]tà (?) |
| 3 | Cesarea (?). Per sesta (?) lettera (?) ~ | Cesarea (?). Per sesto / questa (?) Lettera (?) ~ |
| 4 | [run] e il secondo de | [CIPHER] & / e (?) il secondo (?) de / del (?) |
| 5 | che è stato senza (?) mentre non potrei (?) | che (?) è stato (?) senza (?) mentre non potrei / potevi (?) |
| 6 | havendo (?) [...] [...] [...] lettera (?) d' | havendo (?) il (?) visto (?) la prima (?) lettera (?) d' |
| 7 | che (?) come lo havrà (?) [...] V.S. | Corte (?) come lo havrà (?) detto (?) V.S. |

No full stop was found after line 3 through line 7; the span compared is lines 3-7.

Reconciled:
> Per sesta/questa(?) lettera(?) AGOSTO e(?) il secondo(?) de(?) che(?) è(?) stato(?) senza(?) mentre non
> potrei(?) havendo(?) [... 4] lettera(?) d' che/Corte(?) come lo havrà(?) [...] V.S. ...

English (AI agent): "By the sixth(?) letter(?) AUGUST and the second of ... which has been without(?), while I could
not(?), having [...] the letter(?) of ... as V.S. will have [...] it ..."

Judgement: "Per [...] lettera agosto e il secondo de..." does not construe as read; with a month the expected form
would be "d'agosto", and no "d'" is written before the run. This is not evidence against "agosto" (a date phrase
cut short, or "de / [line 5]" belonging to a second date, would fit), but the sentence is not read.

## What this does not settle

- Every clear word above was read by AI agents on photographs; the hand needs a palaeographer.
- Pass A knew pass B's text and the decoded words; only pass B is blind.
- f. 26v (continuation of the 26r sentence) and f. 62v (start of the 63r letter) were not read at full size.
