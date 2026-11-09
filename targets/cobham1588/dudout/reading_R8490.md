# DECODE R8490 (BL Harley MS 287 ff. 80r-80v): Cobham to Walsingham, Ostend, 5 May 1588. Cipher reading, in part

Contribution to Daniel Bourdeau's target `cobham1588` (catalogue 131). His clear-text transcription (`texts/R8490_reading.md`, 22/10) is the base and is not redone here. No DECODE image or crop is attached; cite "DECODE R8490" (https://de-crypt.org/decrypt-web/RecordsView/8490).

## Status

**Read in part: 35 of 43 cipher words read by sense = 81.4 %** (21 sure, 14 probable, 0 restored, 8 unresolved). With the 6 name codes (all glossed in period hands): 41/49 = 83.7 %. Below the 95 % rule, so the text stays "read in part". The clear text was checked only on the lines that carry cipher (80r ll. 9-12, 18-21, 31-35; 80v ll. 1-2); no figure is given for the whole letter.

## Method

1. All cipher of ff. 80r and 80v transcribed sign by sign (18 passages, 43 words + 6 codes) into `frozen/R8490_chiffre.tsv`, hashed before any decoding: SHA256 `01a80a432bc0423aac52825ec7d984d56c2fa1b2b7c541f4e122872e33d6a785`. f. 81r is blank; f. 81v has the address and endorsement only.
2. Raw decoding with the frozen f. 78r key `key_R8489_f78r.tsv`, unchanged, main value, unknown sign = "?": `frozen/R8490_decodage_cle_gelee.txt`. It already gives *the*, *not*, *it*, *ther*, *retorn*, *to*, and nearly *hostages*, *subiect*, *forwarde*, *openning*.
3. New values only in the declared derived key `frozen/cle_R8490_derivee.tsv` (SHA256 `8557ecf0…e37c`), each with its attestations and a strength A/B/C. The frozen key is not touched. Not measured against a control.
4. Codes: 22 = Sir James Croft; 27 = Dr Valentine Dale; 15 = the Duke of Parma; ◻ = the States (glosses on R8489 f. 78r); 7 = the Queen (gloss on f. 79, Daniel).
5. Classes: *sure* = every sign has a frozen value or a strength-A derived value and the word makes sense; *probable* {x} = one sign of strength B/C, unexplained or missing, sense clear; *restored* [x] = word supplied by sense (none); *unresolved* ‹…› = no word that makes sense.

Polyvalent signs, decided word by word: Λ (A) = t in *the, not, kept, to, ther, these, treat(s), subiect, action, brother, retorn*, = s in *is, hostages, surti, send, Bruges, desire, restrain*; one broad caret = a (*treats*, C). γ (Y) = r in *ther* ("their" in Cobham's spelling). d = o everywhere (*of, to, openning, brother*; strength A). The letter d is written ∞ or a small closed o (O: *forwarde, send, Breda*), a sign distinct from d and c at 1:1.

## Word table

| id | folio, line | signs | reading | class | note |
|---|---|---|---|---|---|
| C01 | 80r l. 9 | c V N 8 S | ‹…› | unresolved | "ornc?"; S (barred long s) unknown |
| C02a | 80r l. 10 | X # | {in} | probable | X = i, # = n (C) |
| C02b | | A h 7 | the | sure | |
| C02c | | ◻ | [the States] | code | f. 78r gloss |
| C02d | | L U N 8 7 A | ‹…ances› | unresolved | "[ex]pances" would need ◻ = ex-, against the f. 78r gloss |
| C03a | 80r l. 12 | N c A | not | sure | |
| C03b | | B 7 | be | sure | B = b (A) |
| C03c | | w E L A | {kept} | probable | ϕ = p (C, one attestation) |
| C03d | | A h 7 | the | sure | |
| C03e | | h c u 7 N | haven | sure | c = a (A) |
| C03f | | I A | is | sure | |
| C03g | | X d + c u 8 7 | ‹…› | unresolved | |
| C04 | 80r l. 18 | h c A A U G E A | hostages | sure | "Touching hostages" |
| C05a | 80r l. 19 | 7 | [the Queen] | code | |
| C05b | | A R | to | sure | R = o (A) |
| C05c | | D 7 Y N O E | ‹…› | unresolved | the verb |
| C05d | | A h 7 Y | ther | sure | = their |
| C05e | | A u V A I | surti | sure | = surety |
| C05f | | A R | to | sure | |
| C05g | | A h 7 A | these | sure | |
| C05h | | A c V M 7 A | {termes} | probable | c = e (C) |
| C06 | 80r l. 20 | A V 7 A T A | {treats} | probable | A = a (C), T = t (B) |
| C07a | 80r l. 21 | A V 7 A T | {treat} | probable | |
| C07b | | d F | of | sure | |
| C07c | | B V 7 O Q | {Breda} | probable | O = d (A), Q = a (B); b-r-e-d-a letter by letter |
| C08 | 80r l. 21 | A u B I 7 8 A | subiect | sure | singular |
| C09 | 80r l. 31 | F c V W v V O 7 | {forwarde} | probable | v = a (C) |
| C10 | 80r l. 31 | c X A I R N | {action} | probable | X = c (C) |
| C11a | 80r l. 32 | A 7 N O | send | sure | |
| C11b | | A d | to | sure | |
| C11c | | B V u G E A | {Bruges} | probable | only the last sign in doubt (looped caret) |
| C11d | | 27 | [Dr Dale] | code | |
| C12a | 80r l. 32-33 | d P 7 N – N I N G | openning | sure | split at line end |
| C12b | | d F | of | sure | |
| C12c | | A h 7 | the | sure | |
| C12d | | B R c w 7 A | ‹bookes› | unresolved | signs spell b-o-o-k-e-s; sense not established |
| C13a | 80r l. 33 | A d N | ‹…› | unresolved | |
| C13b | | d F | of | sure | |
| C13c | | X c V I w 7 | ‹…› | unresolved | place name? |
| C14 | 80r l. 34 | B V d A 7 V | {brother} | probable | h not written |
| C14b | | 15 | [the Duke of Parma] | code | |
| C15 | 80r l. 34 | V Q I N A L c V A | ‹…› | unresolved | perhaps a place in -port |
| C16 | 80r l. 35 | h c u 7 N | {haven} | probable | small second sign |
| C17a | 80v l. 1 | 22 | [Sir James Croft] | code | |
| C17b | | v 7 A I v V | {desire} | probable | 1st and 5th signs unexplained |
| C17c | | A c | to | sure | |
| C17d | | V 7 A c V N | retorn | sure | f. 78r: *retorne* |
| C18 | 80v l. 2 | V j A A V Q I N B 8 | {restrain[ed]} | probable | j = e (C), Q = a (B); ending "B 8" unexplained |

Count: 43 cipher words = 21 sure + 14 probable + 8 unresolved; 35/43 = 81.4 %. Codes 6/6. Total 41/49 = 83.7 %.

## Cipher passages in context

Clear text from Daniel's transcription; cipher in *italics*; {x} probable; ‹…› unresolved; [x] code.

- 80r ll. 9-12: "…to drawe our forces from *‹…›*, hoping theym *{in} the [States] ‹…ances›*, for what chaunces so ever yow bestowe … yt will *not be {kept}, the haven is ‹…›*."
- 80r ll. 18-21: "Touching *hostages*, yt ys honorable for *[the Queen] to ‹…› ther surti to these {termes}*, as usuall yn all *{treats}* … at the *{treat} of {Breda}* … and the *subiect* ther were delivered Julio Romeo, Cristophero Mondragon, Mor Daussy…"
- 80r ll. 31-35: "*[22: Sir James Croft]* is so *{forwarde}* yn the *{action}* that he promised Q[ueen] to *send to {Bruges} [27: Dr Dale]* to begyn the *openning of the ‹bookes?›*, which myght bee to the *‹…› of ‹…›*, that a *{brother}* about *[15: the Duke of Parma]*, who promised the mayor *‹…›* a *{haven}* to open."
- 80v ll. 1-2: "*[22: Sir James Croft] hath a {desire} to retorne* from theym, yf he be not more *{restrain[ed]}*."

## New compared with the existing reading

- 22 and 27 applied: Croft promised the Queen "to send to Bruges Dr Dale"; Croft "hath a desire to return from them, if he be not more restrained". History (Dale sent to Parma in 1588) is a sense check only, not proof.
- *Bruges* (previously b-u-i-e-s, unread), *kept* (previously unread), *Breda* letter by letter (b-r-e-d-a, previously b-r-e-d-d), *subiect* singular (previously *subiects*), *termes*.
- Sign distinctions: O (small closed o = d) ≠ ∞; R (= o) ≠ T (barred t = t); d = o throughout.
- Still unresolved: l. 9 (place forces are drawn from), l. 10 "…ances", l. 12 state of the haven, l. 19 the verb, l. 33 two words (a place?), l. 34 the mayor of ‹…›.
