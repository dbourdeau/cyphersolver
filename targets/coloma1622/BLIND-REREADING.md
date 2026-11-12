# Blind re-readings and new code values, 9-11 Nov 2026 (follow-up to PR #279)

The key `key.tsv` (CLE_C04, SHA-256 714f70ba...) and `validation.txt` are unchanged: no new measurement was made, and the key
stays partial by our protocol. What changed is the reading of the letter: two code values held by a contemporary clear,
proposals of a text-only machine run, and two blind sheets of sign shapes answered by Brice Dudout on the BNE images.
No image, crop or thumbnail is reproduced here.

## 1. Two values held by a contemporary clear (9 Nov)
BNE MSS/18428 (Mirabel to Gondomar, lead 1271) has a bound contemporary clear copy (fol. 31) of a letter in the same system.
Used as learning text only (no measurement): **141 = ELLO** ("cabo dellos") and **318 = OFICIO** ("los offos que convendran
hazer"). In this letter: "de ‹141›os" -> "de ello" (certain) and "oficios" restored -> certain.

## 2. Proposals of a text-only machine run (11 Nov)
A Claude Fable 5.2 run (API, text only, it saw no image) was given the frozen transcription, the key and our reading. Its
proposals, marked as such in `reading.md`:
- values from clears we already had: + = i after que (Feria Rosetta, "que aqui"), sa = al (RES/227/128, 4 places);
- the **order of the nomenclator**: code numbers follow the alphabet of their values. On the 37 code values held by a
  contemporary clear, Kendall tau 0.750 against at most 0.463 for 200 shuffled controls; a non-circular check: 14 of the 16
  values that we had placed by sense alone on 5 Nov fall in the alphabetical window of their code (shuffled codes: mean 5.3,
  max 11). The two outside (30 TERMI, 35 CORRESPONDENCIA) are replaced by window values: **30 = ALLA** (allanar, allanado),
  **35 = AMISTAD**;
- values by sense inside the window (one place each unless said): **48 TRATA** (2 places), **52 CRISTIAN** (2), 127 DIFICULTAD,
  40 BAJO, 264 HONRA, 295 MANDA, 53 CARDENAL (2), and the group L/54/y = "religion catolica romana"; "bo" (= la in C04, held by
  no clear, one place in the whole file) moved from certain to unresolved.
Only the values of the first bullet rest on a contemporary clear. The rest is sense plus the order, partly circular (the run
says so), and a value with one place cannot be tested. Values at one place stay **restored**; values at two places or more,
or a near spelling, are **probable**, as the class rule at the head of the word table says (the "literal rule").

## 3. Blind sheet FL2-C (11 Nov): the signs these proposals depended on
Format of the earlier sheet M16 (PR #279): for each question, the line with one sign boxed, next to reference shapes cut from
the same letter (RES/227/122; for MSS/18428 p. 44, from that page); Brice Dudout picks the shape he sees; no value, decoding or
gloss is shown; questions in random order (seeds 202611111 / 202611112); "none / other shape", "illegible", a remark per question.
15 questions = 13 points + **2 controls** (faz, xa). Sheet `planche.html` da35c553...; private shape-to-reading map bd4b16d2...
(never loaded by the page); answers 46924224...; integration rule 6adc16e1... (written before the map was applied to the answers).
- Controls 2/2.
- With the proposals: the sign in 1r.16 is _A_ (so _L_ is free for RELIGION in 1v.24); "fa" in 1r.18 is fa; in MSS/18428 p. 44
  the looped fi is the que ligature.
- Against them: 1r.10 is 79, not 84 ("este" stays restored); 1v.10 "a barred 4 under an erased circle", not z ("hizo" not
  settled there); 1v.05 fu, not the ligature fuz; 1v.26 xo, not +.
- "None", remark kept, nothing integrated: "0 barred"; "fov, not fvo (looks like shape 3)"; "shape 2 with an e in the middle";
  "xo with a v above"; "o with a cross". These are new marked signs, not in the key.

## 4. Blind sheet FS1 (11 Nov): four conjectures by sense on restored words
Rule `REGLE-INTEGRATION` **29231542e4f12607fd45f91b342c8fc18fc263418ac13da4763deccfd459e75b**, hashed before the sheet was built.
Base: the reading of section 2 under the literal rule (SHA cd373647..., 380/421 = 90.3%). Sheet `planche.html` fbbb418a...,
private map fa693d21..., builder planche_core.py 7f1d5d1e..., applier appliquer.py e92b1d3d...; seeds 202611113 / 202611114.
Answers (Brice Dudout, 11 Nov 2026 17:02 UTC) **391e2f24fb0f23e5a493a9e43a3c56834bdef159e95ae567ff7e149ad2d2483c**.
6 questions = 4 conjectures + 2 controls; each answer applies to that one place only; a word confirmed counts at best probable;
one failed control and nothing is integrated.

| q | place | sign | shape seen | effect |
|---|---|---|---|---|
| K1 | 1v.15 | for (control) | for | OK |
| K2 | 1v.15 | 94 (control) | 94 | OK |
| S1 | 1v.10 | z? or 4 | 4 | "{hízo}sele novedad" (as "lo hizo" 1r.07: 81 4 61 sor) |
| S2 | 1v.05 | fro or for | for | "lo {deseaba}" |
| S3 | 1v.14 | 68 or 88 | 88 | "{bastaría}" (was [gustaría]) |
| S4 | 1v.18 | 94 or 84 | 84 | "queriendo {este} Rey" (was [deste]) |

Declared: the S3 conjecture came from a zoom made before the rule (to place the boxes), so it is not blind; the blind answer decided.

**Position bias, declared.** After the shuffle (seed 202611114; the shuffle was checked in planche_core.py), the six expected
shapes (4 conjectures + 2 controls) all fell in position "shape 3" (chance about 0.14%), and all six answers are "shape 3".
On this sheet the controls therefore cannot tell a reading of the shape from an answer by position. Asked afterwards, Brice
Dudout confirmed that he chose each answer by the shape, not by its place. We keep the result on that confirmation, and the
builder is to be fixed so that the target never sits at the same position on every question.

## Count (Daniel Bourdeau's rule)
| stage | words | certain | probable | restored | unresolved | certain + probable |
|---|---|---|---|---|---|---|
| PR #279 as merged (5 Nov, sheet M16) | 425 | 338 | 37 | 29 | 21 | 375 = 88.2% |
| after sections 1-2, prudent count | 421 | 337 | 37 | 41 | 6 | 374 = 88.8% |
| after sections 1-2, literal rule | 421 | 337 | 43 | 35 | 6 | 380 = 90.3% |
| after FS1 (this version) | 421 | 337 | 47 | 31 | 6 | **384 = 91.2%** (98.6% with restored) |

FL2-C moves no word in or out of certain + probable (its confirmations are on words already counted; its refusals leave words
restored). All counts are by the same script on the same letter, with the check that the word table covers the frozen
transcription in order. The word total moves from 425 to 421 because some groups are segmented differently ("a que aqui" ->
"aqui", "no veda" + surplus -> "novedad", "‹141›os recibiendole" -> "ello ofreciendole", "‹48› vale este" -> "trataba este").

**The literal rule against the M16 pre-registration.** Six words differ between the two rows of sections 1-2. Three of them
are the xe words (acomodarse, deseando, conservase: xe confirmed on M16 where xer = se is expected, three places): the M16
pre-registration kept them restored, the class rule of the word table makes them probable as a near spelling. The other
three are machine proposals held at two places (trata and trataba for code 48; cristianos for code 52). Under the
prudent count the present version would be 378/421 = 89.8%. Either way: **read in part**, under 95%.

## Declared limits
- No new key test; the key is not validated (C02 0.761 and H5 0.814 partial; C01 and H3 failed; see `validation.txt`).
- Words unblocked by a sheet count at best as probable, never certain.
- Most new code values are machine proposals by sense and order; the shapes, not the proposals, decided on the sheets.
- One reader of the shapes (Brice Dudout); AI agents transcribed and read. No palaeographer checked the letter.
