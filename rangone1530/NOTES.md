# Guido Rangone to Anne de Montmorency, Venice, 10 January 1530 (BnF fr. 3070 f. 81, DECODE R4249)

Status: read in part

Catalogue item 181 (class C, "Guido Ramgone (Venise)"). DECODE R4249, "Non-decrypted", 2 pp., Italian; access
"Authentication required" (8 images fetched with the project cookie; git-ignored in `img/`).

Outcome: the cipher is a homophonic substitution with about 50 signs for Italian. The key was rebuilt
ciphertext-only from this letter and a sibling found in the same series (Rangone, 24 Dec 1529, fr. 3082 f. 42).
232 of 264 cipher signs (87.9%) read as sense. Both passages are about Cesare Fregoso, Rangone's new
brother-in-law: A says that Venice sent word to "Signor Cesare" and made him great offers while Rangone was
slighted; B names "il Fregoso" and the business he took on "con spada et cappa". The unread signs occur once
each and the two letters are all the ciphertext there is. Reading and translation: `reading.md`.

## The documents

- **A. BnF fr. 3070 f. 81r-v, no. 40** (Gallica btv1b9059934c; DECODE R4249 images 1-8): "Lettre, en italien, et
  avec chiffre, de GUIDO RANGONE ... a monsignore gran maestro de Franza ... De Venezia, il X di zenaro M.D.XXX".
  Autograph signature "S.re Guido Rangone Co. et c. di mano pp.a"; address on f. 82v "Alo Ill.mo et Ex.mo sig.r
  Mons. Gran maestro de Franza". Seven lines of cipher on f. 81r after "adesso lo diro piu brevemente che io potro.
  Mons.r", interrupted by the clear words "vida V. Ex. che tratti sono questi"; the rest is clear (news of Venice:
  the Duke of Urbino gone to Pesaro, the Count of Caiazzo dismissed, the Turkish envoy's audience, Bentivoglio
  taking possession of Milan for the Duke, the Swiss and Grisons going home, Genoa arming twelve galleys).
- **A'. Clair. 331 f. 15** (Gallica btv1b9000761d view 15): Clairambault's 18th-c. copy, headed "Vol. 134 fol. 81",
  cipher copied sign by sign, no decipherment. Tomokiyo (cryptiana `francis.htm`, Clair. 331) lists it as
  undeciphered and as the same cipher as Clair. 330 f. 206.
- **B. BnF fr. 3082 f. 42r, no. 19** (Gallica btv1b9060318p view 65; not on DECODE): Rangone to Montmorency, Venice,
  24 Dec 1529, same cipher, five cipher lines after "haura visto sua bona voluntade" and "li giorni passati con spada
  et cappa".
- **B'. Clair. 330 f. 206** (Gallica btv1b9000769q view 210): copy of B ("Vol. 143 fol. 42"), undeciphered.

Clairambault's "Vol. N" is the old Béthune volume number: Vol. 134 = fr. 3070, Vol. 143 = fr. 3082. That is how B
was found from Tomokiyo's Clair. 330 reference (the BnF catalogue does not flag fr. 3082 no. 19 as ciphered).

## Transcription

`cipher.txt` (lines with witness labels) and `tokens.txt` (signs only; 264 signs, 54 types as transcribed),
checked against both witnesses of each letter at 1.4-3x crops. The copies misread a few signs (Clair. 331 has
"M·N·8" for "M x 8", б for the looped ɕ); the originals were followed. Three look-alike pairs were split after
close inspection: the dashed "-∋" (`E`, u/v) against the plain ∋ (`E2`, i); the capital Θ of A1 (`Th`, t)
against the narrow θ (`theta`, i); the blotted star of A1 (`S`) against the blotted barred cross of B5 (`S2`).

## The system

Homophonic simple substitution, no word division, no nomenclator found. Homophones (from `key.json`):

| letter | signs | letter | signs |
|---|---|---|---|
| a | I, J, U | l | W, xi, hex |
| e | w, P, oo, S, S2 | m | X, oc, iii |
| i | L, r, theta, M, l, d, G, E2 | n | k, ob, B |
| o | 8, q | c | x, O, dv |
| u/v | Z, g, E | d | V, + |
| s | p, N | t | phi, Th |
| r | t | f | pi, e (tailed) |
| p | D2, A | g | m, # |
| b | D | h | 6 |

`vt` (in "Fre·goso") is a null. Vowels have 2 to 8 signs, consonants 1 to 3: the usual Italian homophonic design
of the 1520s.

## How it was broken

1. Literature: DECODE Non-decrypted; Tomokiyo lists the Clair. copies as undeciphered; Lasry's `GL.htm` has no
   Rangone key; none of the keys rebuilt in this repository for 1528-29 Italians in French service (Visconti,
   Bizozola, Sormano) shares the sign set.
2. Siblings: B found through the Clairambault volume concordance. Four other Rangone letters of 1529-30 (fr. 3012
   no. 44, fr. 3013 no. 19, fr. 3034 no. 18, fr. 2980 no. 44) checked by an agent: all clear. The ciphered letter of
   Joachin de Vaux, Ferrara 13 March 1529 (fr. 3012 no. 51, view 162) uses a different Greek-letter sign set.
3. Simulated annealing (`solve.py`, then the incremental `solve2.py`) over sign→letter maps against
   `it-cinquecento` (5-gram, no spaces) with a letter-frequency penalty. Short runs gave pseudo-Italian and no
   consensus; genuine Italian of this kind scores about -1.72 per 5-gram, the short runs -2.3, so the search, not the
   model, was failing. 40 restarts of 2 million moves: one restart reached -1.97 with "malissimo satisfato di lui",
   "mandato a dirlo al signore Cesare", "il Fregoso", "una pratica di lei mi dispiacera" (`sa2_run2.log`,
   `key_fregoso.json`). Low-temperature restarts from perturbed copies of that key all return to it.
4. Sensitivity of each sign (`sens.py`): 35 signs are pinned by the text (margins 6-85 log units), the rest occur
   once or twice.
5. Hand corrections from the words: 6 = h ("ha mandato", "e hara", "ho una"), tailed `e` = f ("grande oferte"),
   D = b ("le cose ben disposte"), `vt` null, the Θ/θ, ∋/-∋ and star splits above.
6. Word-aware scoring (`spaced.py`: best segmentation under the spaced model, coordinate ascent over the rare
   signs, and brute force of pairs such as `xo`/✳ in A6 and `y`/`oc` in A1-A2): no alternative wins by more than
   noise, and with a null option the model deletes letters. These signs stay open.

## Context

Cesare Fregoso married Rangone's sister Costanza in autumn 1529. He had commanded Ravenna and Cervia for Venice
since September 1528, the towns the clear text of B is about, and in January 1530 the Venetian Senate made him
military governor of Verona at 2,500 ducats a year (DBI, "Fregoso, Cesare"). A's "grande oferte" to "Signor
Cesare" and Rangone's "vida V. Ex. che tratti sono questi" are that episode seen by the brother-in-law left out. In
October 1530 the French dismissed Rangone over his complaints that his pension had been cut.

## Remaining gaps
- A1 "a [y S] de venire" and A2 "[q y] le mie" (sign y, 2 places, plus the phrase around it: 9 signs) - blocker: too-short; y occurs twice, "me" fits A1 and fails A2, "b" fails A1, no third occurrence
- A6 "la [xo]icon[✳]uorano" (12 signs) - blocker: too-short; xo occurs once, the run has no parallel in either letter
- B3 "de [a]en" and "volse r[c d 9]a" (9 signs) - blocker: too-short; signs a, c, d, 9 occur once each and several words fit
- B4 "il f[?] da rovi[n]are" (2 signs) - blocker: too-short; the tailed sign reads f in A, makes no word here

## Escalation
- [x] siblings: B (fr. 3082 f. 42) found via Clair. 330 f. 206 and read; four other Rangone letters of 1529-30 and the Joachin cipher of 1529 checked, not this cipher
- [x] clear-pages: none; both Clairambault copies reproduce the cipher without decipherment
- [x] known-keys: Lasry GL.htm keys and the repository's Visconti, Bizozola, Sormano, Gramont keys compared by sign set; none shares it
- [x] print: Tomokiyo francis.htm (lists both copies as undeciphered), DECODE, DBI Fregoso and Rangoni lives, web search: no decipherment or edition
- [x] key-rebuild: annealing from random starts found the key; sensitivity, hand corrections and word-aware coordinate ascent extended it
- [x] retry: every open sign brute-forced singly and in pairs with the spaced model; no reading beats the others

## Files

`cipher.txt`, `tokens.txt`, `key.json` (final; `?` = unread), `key_fregoso.json` (the annealer's key before hand
corrections), `reading.md`, `solve.py`, `solve2.py`, `sens.py`, `spaced.py`, `show.py`. Images git-ignored: `img/`
(DECODE R4249), `full3082/`, `full330/`, `full331/` (Gallica natives).
