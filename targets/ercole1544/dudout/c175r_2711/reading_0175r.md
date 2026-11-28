# c. 175r: reading of the arbitrated transcription (Brice Dudout, with Claude, 27 Nov 2026)

Source: `transcription_0175r_arb.txt` (first choices: `transcription_0175r_arb_first.txt`), decoded with the folder's
`key.tsv` by the folder's `scripts/decode.py` (`decryption_0175r_arb.txt`). Since 27 Nov (evening), nine of its `{x|y}` signs
are settled by a blind shape plate (`sign_check_2711/`, section at the end): `transcription_0175r_plate2711.txt`,
first choices `transcription_0175r_plate2711_first.txt`, decryption `decryption_0175r_plate2711.txt`. The text runs on from c. 174v and goes
on to c. 175v; it starts and ends in mid sentence.

Marks: a plain word is verbatim from the signs (word division, apostrophes, accents and punctuation are editorial;
u/v as sense requires). `{word}` = probable: one sign (or one doubled/dropped sign) away from the signs, or a code
known from context only; each is justified below. `[word]` = restored by sense, two or more signs away.
`‹...›` = unresolved. Codes are expanded: `30` che, `53` non, `39` questo, `59` quanto, `61` quale, `68` come,
`73` ancor, `78` Francia, `35` Vostra Excellentia, `L` et, `L^10` papa (frozen); `L^o` imperatore and `55` bene are
context-only values of `key.tsv` and are therefore counted as probable.

## Text

e certo che po più guadagnar che a [Perpignano] o in Fiandra, massimamente havendo l'armata turchesca, il {timor}
della quale importa un mondo; et {queste} lettre dice che sono state {gratissime} al re, et che ha {risposto} che si
portara di modo che fara {noto} a tutto il mondo presto presto quanto sia la grandezza et il poter suo, et che
mandara a far {genti} alla {Mirandola}. Mi ha scritto costui sempre che l'animo et l'inclinatione del papa et il core
sono volti al re, et che con lo {imperatore} va doppiamente; et che Farnese ‹[#2]de› ito con animo di far il
parentado, et a ‹fordarsi› nel secreto con ‹ello› ‹le› al {qual} il papa crede persuader con {ragioni} tanto che
s'habbia a {contentar} che ei pigli con sua bona gratia Milano, promettendogli dar l'adito et l'aiuto alle cose di
Toscana et del {regno}; et che se Farnese po appuntar questo col re, verra poi al imperatore et {accettara} Milano
pagando denari con tutte le conditioni che gliel vora dar lo {imperatore}, {ben} tentara prima d'haverlo {libero}
‹da›, non potendolo {pigliar} in ogni guisa, con speranza di {liberarselo} poi con l'aiuto di Francia. Et questi mi
dice esser li dissegni del papa, li quali non finisco di creder in tutto, ma credo {bene} che habbia cosi strette
pratiche con il re quanto {forsi} con lo {imperatore}, come {ella} vedera per la copia d'una {lettera} della
moglie di Pierluigi scritta al [fratello], [pervenutami] in mano per ottima via, quale sara con questa, et ancor certi
{pochi} avisi di Francia. Di questo che ella dice desiderar tanto di {sapere}, che se {dica} a Roma della sua ita in
{Inghilterra}, le dico che il medemo mi scrive che il papa {è} avisato che Vostra Excellentia è stata {mandata} per
dar conto della ‹[96]› et dira questo re che se l'{imperatore} haveva denari haveria seguitata la ‹[96]›, che pero
{prega} quella maesta a prepararsi di aiutarlo de denari et {genti} o de denari ‹al…›

## Count (Daniel's rule: words read by sense)

Words are counted after splitting at apostrophes (`l'animo` = 2) and with each code as one word.

| | words | share |
|---|---|---|
| sure (verbatim) | 297 | 87.4% |
| probable `{}` | 32 | 9.4% |
| restored `[]` | 3 | 0.9% |
| unresolved `‹›` | 8 | 2.4% |
| **all** | **340** | |
| **read by sense** (sure + probable + restored) | **332** | **97.6%** |

About 1,450 plain letters (over 300). By Daniel's rule (95% of words read by sense) c. 175r passes, with 87.4% sure (86.2% before the plate of 27 Nov).
The 8 unresolved: `[#2]de` (F08), `fordarsi`, `ello`, `le` (F08-F09), `da` (F15), the code `96` twice (F24, F25),
and `al…` (F26, runs on to c. 175v). Context suggests `96` = *impresa* ("dar conto della impresa"; "haveria seguitata
la impresa"); not counted.

Signs left out of the reading (the check below shows them): F07 an `s` after "al re"; F12 an `L` (et) inside
"col re"; F15 an `a` after "pigliar"; F23 an `s` in "è s avisato". They are read as slips; none of them is
counted as read.

## Probable and restored words, with the signs

| line | signs give | reading | why |
|---|---|---|---|
| F01 | palpigaano | [Perpignano] | two signs off (al/er, a/n); a place where the king could "gain"; Perpignan was besieged by the French in 1542. Restored only |
| F02 | timopr | {timor} | one extra p |
| F03 | dueste | {queste} | d for q (cipher q/d look-alike) |
| F03 | gratissi-d-e | {gratissime} | plate of 25 Nov gave q (= d) for the sign; sense only, as in the patch of PR #975 |
| F03 | hariscposto | {risposto} | one extra c |
| F04 | notu | {noto} | u for o |
| F05 | sentiallamil | {genti} | s for g (cipher f/t) |
| F05-06 | milandola | {Mirandola} | l for r |
| F07 | L^o | {imperatore} | the arbiter read the superscript as an open v (L^r) with L^o as the alternative; the blind plate of 27 Nov chose L^o, as sense wanted; L^o is a context-only code, so the word stays probable |
| F09 | qoal | {qual} | o for u (cipher b/h, open question in the arbitration; the plate of 27 Nov did not settle it, see below) |
| F09-10 | ragiuni | {ragioni} | u for o |
| F10 | consentar | {contentar} | s for t |
| F12 | resno | {regno} | s for g (cipher f; the plate of 27 Nov chose f over t, so the signs give "resno" and the word stays probable) |
| F13 | afettara | {accettara} | f for cc (cipher 5) |
| F14 | [L^o] | {imperatore} | context-only code |
| F14 | beatentara | {ben} tentara | a for n |
| F14-15 | libepo da | {libero} ‹da› | p for r; `da` unresolved |
| F15 | pigliara | {pigliar} | one extra a (left out) |
| F15-16 | libeparselu | {liberarselo} | p for r, u for o |
| F18 | [55] | {bene} | context-only code |
| F18 | fopsi | {forsi} | p for r |
| F18 | [L^o] | {imperatore} | context-only code |
| F18 | alla | {ella} | a for e |
| F19 | lettpa | {lettera} | p for er |
| F20 | praterllo | [fratello] | p for f and an extra r: two departures |
| F20 | persanutati | [pervenutami] | three departures (s/v, a/e, t/m); "pervenutami in mano per ottima via" |
| F21 | pocai | {pochi} | a for h |
| F22 | sapeer | {sapere} | e and r swapped |
| F22 | dipa | {dica} | p for c |
| F22-23 | ingailterra | {Inghilterra} | a for h |
| F23 | esauisato | {è} avisato | one extra s (left out) |
| F24 | mandala | {mandata} | l for t |
| F24 | [L^o] | {imperatore} | context-only code |
| F25 | presa | {prega} | s for g |
| F26 | uentio | {genti} o | the arbiter marks {h|t}: with t the signs give "genti o" verbatim. The plate answer was t, but its t and h examples were faulty (see below), so the word stays probable |

## Check

The unmarked words were aligned letter by letter with `decryption_0175r_arb.txt` (a read-only snippet in the
manner of `scripts/check_repairs.py`): no unmarked word holds a letter the signs do not give; the only departures
outside marks are the four signs left out listed above.

## Blind shape plate of 27 Nov 2026 (`sign_check_2711/`)

Eleven of the arbitration's doubtful signs went on a blind shape plate for Brice Dudout. Each question framed one
sign. The options were shown only as shapes, each with two real examples from this hand taken at secure places.
Letter values were never shown, and three controls were hidden among the questions. The selection rule, with the
effect of every answer, was hashed before any thumbnail existed (initial `0f169b25…af86`). Amendment 1 reframed four
boxes after the contact sheet and before the plate was delivered (`REGLE-SELECTION.md` sha256 `374b97b4…71fc2`).
The Estense images stay private (CC BY-NC-SA), so no thumbnail or crop is included. The folder holds the rule, the
answers as exported (sha256 `4bfd283d…90d4`), the revealed key (`key-revealed-cle-PRIVEE.json`, sha256
`09d7d750…49d3`, boxes in pixels of the 1900 px leaf) and `results.tsv`.

Controls: 3/3 (K1 b, K2 e, K3 `27`). These answers are applied in `transcription_0175r_plate2711.txt`: F01 e
(Fiandra) and S (confirmed), F07 `L^o` and `17` (confirmed), F08 e (parentado), F12 e and f, F18 e (pratiche) and
a (con). Four words become verbatim: **293 → 297 sure (86.2% → 87.4%)**. Read by sense is unchanged at
97.6%.
Not applied: F09 `{b|h}` (qual). The answer named h, but the remark says the two options look the same ("they are
b's"). That is not one conclusive shape, so the doubt is kept. Two plate defects are on record: to the reader, the
h examples looked like b (q01), and one t example also held an f (q12). F26 (`{h|t}`, genti) used the same t and h
examples. Its answer was t, but because of these faulty examples it is not applied: the sign stays `{h|t}` and
*genti* stays probable. Brice Dudout's answers give an opinion on shape, not a reading. The key and the readings of the other
leaves are LcCompany/WAINUT's.
