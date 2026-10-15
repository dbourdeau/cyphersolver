# Laurière (Honoré Mauroy La Verrière) to the duc de Nevers, July–August 1593: Nevers key no. 57

Status: read in part. Three letters in La Verrière's own key, Tomokiyo's Nevers key no. 57 (BnF fr. 3995
ff. 102–103, endorsed "Mons^r de La Verriere … Chartres 1593 fevrier"): fr. 3625 no. 55 (Châlons, 9 Jul 1593) read in
full (85/86; identified by setsunaatto, issue 13); fr. 3625 no. 10 (Courgenay, 13 Jul 1593) reproduces the office's
interlinear decipherment in a blind test (setsunaatto, PR 15); fr. 3985 f. 58 (Poissy, 12 Aug 1593) 235 of 248
tokens (94.8%), one token under the read bar. Together 320 of 334 counted tokens (95.8%).

Split on 14 Oct 2026 from `champagne1590` under the one-key rule (George Lasry, 14 Oct 2026). Until then these letters
were filed with the Champagne news-letters of 1590–91 (catalogue item 30), which use other codes:
[`targets/champagne1590/`](../champagne1590/NOTES.md) (nos. 24/25/60, a two-digit alphabet) and
[`targets/bienvenut1590/`](../bienvenut1590/NOTES.md) (no. 23, a name code), each a different cipher with its own
page. The work below was done in the champagne1590 sessions of 21 Sept – 3 Oct 2026 and is carried over from its
NOTES; the files moved here on 14 Oct 2026. Images (git-ignored) stay in the main checkout's
`targets/champagne1590/img/` (f. 58 and the key sheet in `img/fr3985_f58/`).

Work date: 2026-09-21.

## Prior work checked

* Tomokiyo, cryptiana `code/nevers.htm` (copy in `research/gallica_siblings/src/nevers.htm`): the Nevers keys nos.
  1–70 of fr. 3995. No. 57 (fol. 102, February 1593, "Mons. de Laveriere") is Laurière's key; the first pass missed it
  because of the spelling La Verrière / Laurière. Tomokiyo names fr. 3985 f. 58 as a letter in it.
* No printed decipherment found (the items are not in the Mémoires de Nevers index in Tomokiyo's article).

## Access

Gallica IIIF: fr. 3625 f. 10r = canvas 31, f. 66r = canvas 143 (canvas = 2 × folio + 11 near the start). fr. 3985
(`btv1b90606498`) f. 58r = canvas 114. Key sheet fr. 3995 (`btv1b525085665`) canvases 196–201. Gallica throttles
(403/empty files) after about ten full-size requests; wait and retry.

## Fr. 3625 no. 55 (Laurière, Châlons, 9 July 1593) and no. 10 (Laurière, Courgenay, 13 July 1593)

No. 10 is f. 10r (canvas 31): a long letter with runs of figures (1–3 digits, some with signs: 10 54 20 17 262 25
103 …) and a few symbols, with the office's interlinear decipherment over most runs ("le Pape", "la volonté du
Pape", "maintenant"); one run near the foot ("307 ✗ 288 … 305 175 3 346") is not glossed. It was not transcribed in
this session. No. 55 was not found: the BnF item numbers of fr. 3625 are not in folio order around the July 1593
letters (f. 55r = 1 July, f. 56r = Langres, f. 61r = Châlons 9 July but signed by the Trésoriers de France in
Champagne, in clear). Canvases 13–64 and 81–200 were inspected at thumbnail size, the likely ones at page size, without finding
Laurière's hand with cipher. Open: locate no. 55 (canvases 65–80 and 201–270 not yet scanned), then transcribe no. 10
as the key source.

## Fr. 3625 no. 55 found (second pass, 21 September 2026)

The OAI item list of fr. 3625 fixes the order: no. 49 = f. 61 (Trésoriers de France, Châlons, **3** July, not 9 July:
the earlier note misread the date), no. 50 = f. 62, nos. 51–53 = ff. 63–64, so no. 55 falls at f. 66. F. 66r (canvas
143) is Laurière's letter, "Chalons ce IX juillet 1593", signed Laurière: clear French with eight cipher runs, 86 groups
(`ct_3625_55.txt`). One word of decipherment is written over the first group ("come" over 347) and "n" over one 304;
otherwise no decipherment on the leaf. Canvases 65–80 and 201–270 were also looked over at thumbnail size: no other
Laurière letter.

The key source is no. 10 (f. 10r). Its first three runs were aligned with the interlinear decipherment
(`ct_3625_10_glossed.txt`): ✗ = que, 335 = le Roy, 141 = soit, 288 = Catholique, 101 54y+ = Sa Majesté, 184y = auroit,
346 = volonté, 59 = du, XX = pape, 25 103 56nΔ = qu'aussitost. The code is syllabic and mixed (10 54 20 17 under
"parole", 262 under "de luy"), so single groups cannot be read from context alone.

Groups of no. 55 that recur in the glossed runs of no. 10:

| No. 55 | Reading from no. 10 | Grade |
|---|---|---|
| 347 | come (gloss on no. 55 itself) | H |
| 59 ✗ (line 1) | du ... que | C |
| 25 ✗ 335 141 encores (line 5) | ... que le Roy soit encores | C |
| 26.6. 346. 59 XX (line 7) | ... la volonté du pape | C |
| 286 103 56nΔ (line 7) | ... aussitost | C |
| 304 ✗ (line 8) | ... que | C |

About 15 of 86 groups read (C). Context in clear: "Il est tres necessaire que ceulx qui ayment cest estat s'y
treuvent ... la remise seroit trop prejudiciable", "la rupture de la tresve", "faire une election d'ung a la devotion
du Roy d'Espagne". Reading the rest needs the other glossed runs of no. 10 (about ten more lines) aligned group by
group; not done in this session.

## Code table from no. 10 and the reading of no. 55 (third pass, 21 September 2026)

All glossed runs of no. 10 (seven of them, R1–R7 in `key_lauriere.txt`) were set against the words written over them.
The code is a syllabic nomenclator: most glosses cover two to five groups whose boundaries the clerk did not mark
(10 54 20 17 under "parole", 22n27 under "a la"), so only groups that fall under the same word in two places, or sit
alone under a one-word gloss, were accepted. The table has 12 entries: ✗ que, 335 le Roy, 346 volonté, 59 du, XX pape
(grade C, two or more agreeing places); 141 soit, 288 Catholique, 103 56nΔ aussitost, 101 54y+ Sa Majesté,
184y auroit, and the frequent short groups 25 (le/la/que) and 26 (a/de) (grade M).

Applied to no. 55 (86 groups): **19 groups read** (347 from the gloss on the leaf; 18 from the table), 67 open.

    l.1  come [...] du que [...] le [...] a [...]
    l.5  [...] le? que le Roy soit encores [...]
    l.7  [...] a la volonté du pape [...] aussitost [...] soit [...]
    l.8  [...] que

The French LM was not used: with about one group in five known and the rest syllabic fragments of unknown length,
there is no letter stream for it to score. No. 55 stays **read in part (fragments)**; reading it needs a better
alignment of no. 10's syllable groups (a solver that fits group boundaries to the glosses), or another glossed
Laurière letter.

## Fr. 3625 no. 55 read with key no. 57 (29 Sept 2026, issue 13)

setsunaatto (dbourdeau/cyphersolver issue 13, 29 Sept 2026) identified Tomokiyo's Nevers key no. 57 (BnF fr. 3995
ff. 102–103, Gallica `btv1b525085665` canvases 196–201) as Laurière's: the endorsement on f. 102v names "Mons^r de La
Verriere" (Honoré Mauroy La Verrière) and "Chartres 1593 fevrier", and Tomokiyo's own entry says the key is used in
a Laverrière letter to Nevers of August 1593. Design, checked here on canvas 200 (f. 103r): alphabet of two signs per
letter; syllables 1–72 = row + 14 × vowel (the sheet's own header: ba 1, be 15, bi 29, bo 43, bu 57); doubles 73–98
(92 = pr); words 99–353 in alphabetical order; provinces and towns with an overbar; name signs (XX = le Pape, the
crossed X = le Roy, Gondi, the grand duke of Tuscany). `key57.txt` has the table.

Every cipher run on f. 66r reads (`reading_3625_55.txt`, the issue's transcription; its lines 1–2 re-checked here
against the full-resolution page and against our own `ct_3625_55.txt`, group for group):

| Run | Reading |
|---|---|
| 1 (after "resouvenir", "come" over 347) | vous estes necessaire pres du Roy afin qu'il ne retarde d'ung jour son assemblée, ce que ses ennemys luy donne[r]ont tout l'empeschemen[t] qu'ilz pourront pour luy faire prandre autre dessein |
| 2 (after "Revenant a mon voiage") | [le duc de Lorraine] montre desir de traiter, mais necessaire avant que [le Roy] soit catholique |
| 2b | quoy fait une election (… "ce moquans de cela") |
| 3 (after "francoir") | s'il veult atandre la volonté du [Pape], non aussitost qu'il sera catholique, qui la traitera |
| 3b (after "et en donne sa parolle") | [le Cardinal de Gondy] pour [le grand duc de Toscane] |

The *r* of donne[r]ont and the *t* of empeschemen[t] are missing in the cipher itself. "304 9P" after "les
oreilles" is *pour* plus a clear abbreviation (9P is not on the key). The issue also tested the key on the sibling
no. 10 (13 July 1593), which has an interlinear decipherment and was not used to fit the key: 157 of 196 letters
(80%) fall in runs of four or more that match the gloss, against a shuffle control of 34 ± 6 (maximum 58).

**Why the first pass stalled:** the 12-entry table from no. 10's glosses was one group out of step from ✗ onward
(✗ is *le Roy*, not *que*; 335 *soit*; 141 *catholique*; 288 *nous*; `101 54y+` is *au-ro-i-t*, not *Sa Majesté*;
`184y` is *est-e*). `key_lauriere.txt` is kept, marked as superseded. The cipher-lab repository's test of key no. 57
(4 of 12) was made against that shifted table.

Context: the letter is from the weeks before Henri IV's abjuration (25 July 1593). Laurière urges Nevers to go to
the King so that he does not put off his assembly by a day, since his enemies will do all they can to turn him
from it. He reports that Lorraine will treat only once the King is Catholic, and that the Leaguers joke about an
election. He also asks whether the Pope's consent is to be awaited.

## No. 10 deciphered with key no. 57: the blind test and the other eight runs (setsunaatto, 30 Sept 2026)

`check_3625_10.py` scores key no. 57 against the office's interlinear decipherment of no. 10 (f. 10r). The letter
played no part in fitting the key, with one small exception: issue 13 checked which y-shaped sign is e and which is i
on run L2. With the two swapped the blind score is 152 instead of 157 (117 instead of 121 without L1), still far above
every control. Score: gloss letters falling in runs of four or more that match the decipherment. Control: the same
signs of each run in shuffled order, 2000 times.

| Set | Transcribed | Letters in runs of >= 4 | Shuffled control | Z |
|---|---|---|---|---|
| `ct_3625_10_blind.txt`, 5 runs | from crops that hide the glosses; fixed before the glosses were read | 157 / 196 (80%) | 33.8 ± 6.3 (max 58) | +19.4 |
| same, without L1 (seen when the key was first applied) | | 121 / 160 (76%) | 21.8 ± 5.0 (max 42) | +19.8 |
| `ct_3625_10_rest.txt`, the other 8 runs | with the glosses in view (weaker) | 311 / 354 (88%) | 97.7 ± 10.6 (max 129) | +20.1 |

Grades of the new values: the word numbers and 29 = *L'Espagne* are **H** (read on the key sheet); 202 = *prendre* and
320 = *sans* are **C** (the sheet lists both values of each number; the office's gloss chose); the Marquis de Pont
sign is **M** (the shape is close to the key's sign, not identical). The deciphered runs below are **H** except where
marked.

No shuffled control reaches the real score in any set. Apart from spelling and the gaps in the gloss, the two places
where key and office disagree are both in R3.
"25 29", with a bracket-shaped bar over the 29, is *que [l'Espagne]* (province 29, "L'Espaigne ou Espagnols" on the
sheet), where the office wrote *qui ne se*. Over "344 234" the office wrote *pour son*. Those figures were re-checked
on the page when the PR was merged: they are 344 234 as transcribed (the middle 4 is an open 4, not a 0), which the
sheet makes *tout hault*. But the idiom is *faire tout son effort*, so the writer most likely meant 334 (*son*) and
wrote 234: the office's *son* would then be right, and its *pour* is not in the figures. Reading: *fera tout hault
[son?] effort* (figures H, the intended word C). Among the other runs: *ne pouvoir recongnoistre le
Roy que premieremen ilz n'eusse eu la volonté du Pape, qui ne viendront jamais a c'est ... que par force*; *l'Espagne
fera tout hault effort maintenant pour anpescher que le Pape ne le resoive, qui seroit tousjours une extreme longueur
pour sortir du mal*; *que nous tenons que [le marquis de Pont] suivra le duc de Lorraine* (the sign **M**); *a l'assemblée ou elle sera tres necessaire*.

One run of no. 10 carries no gloss (after "... que nous avions despesché"): *[le grand duc de Toscane] quant [le Roy]
nous bailla par escrit (sa?) volonté* (the last sign but one, an overbarred 3, is not on the sheet). Its signs were
transcribed from the page when the PR was merged, as U1 in `ct_3625_10_rest.txt`: `TOSCANE 307 ROY 288 xi om zig eps
lam 305 175 3_ 346`. *bailla* is written with one l (b-a-i-l-a). The barred 3 is not a syllable (the overbar marks
only the v and z rows), and province 3 is Bretaigne, which gives no sense, so *sa* is a guess from context (grade I).
The Tuscany sign is taken as the contributor read it from the key's name panel (f. 103v, not re-checked here).

**Checked here before merging (30 Sept 2026).** The script reproduces the table exactly (seed 0, standard library only,
and it also runs on the cp1252 console). Our own transcription of runs L1-L3, made on 21 Sept before key no. 57 was
known (`ct_3625_10_glossed.txt`), agrees with the blind file on every figure group but one: L1 opens with 10 in ours
and 20 in theirs, and the gloss *le* supports 20. On the key sheet (f. 103r, canvas 200), 18 of the 21 word numbers
added from no. 10 stand as given (100, 122, 150, 154, 175, 185, 186, 187, 190, 211, 224, 234, 246, 279, 303, 305,
307, 320); 191, 196 and 255 were not viewed. Both duplicates are as described (202/203 in the F column and in the
overbarred block; 320 religion in R, 320 sans added in S), and province 29 is "L'Espaigne ou Espagnols". The two
header rows match the alphabet in `check_3625_10.py` letter for letter, which showed that the old alphabet line in
`key57.txt` had c and h the wrong way round (now corrected; the contributor had flagged it). Details in `key57.txt`.

## Fr. 3985 f. 58, La Verrière to Nevers, Poissy, 12 Aug 1593, deciphered with key no. 57 (2 Oct 2026)

Tomokiyo's entry for key no. 57 says the key is used in "a letter from Laveriere to the Duke of Nevers, Poissy,
12 August 1593 (BnF fr.3985 fol.58)". No target had read it (`targets/nevers1593` works other items of fr. 3985).
Gallica `btv1b90606498`: **f. 58r = canvas 114**, f. 58v = canvas 115 (address only, "Monseigneur le duc de
Nivernois"). Full write-up in `fr3985_f58/reading.md`; transcription `fr3985_f58/ct.txt`, clear text
`fr3985_f58/clear.txt`, decoder and count `fr3985_f58/decode58.py`, the whole word list of the key sheet
`fr3985_f58/words57.tsv` (read off f. 103r for this letter; key57.txt had only the words of nos. 10 and 55). Images in
`img/fr3985_f58/` (git-ignored).

The page is clear French with two cipher passages (run A, page lines 11-19; run B, lines 21-24), and **the office's
interlinear decipherment stands over almost every cipher line**: the letter was deciphered at the time. Key no. 57
applied as it stands on the sheet reads **222 of 248 cipher tokens (89.5%)** as sense: run A 207/223, run B 15/25.
French LM (`fr-1600-letters`) on the run A reading -1.72 per char; `best_language` French. Tomokiyo's own anchor
(a Japanese comment in the page source: "17(de)9(na)70(tu)26(re) 17(de)32(fi)ω(a)q*(n)n(s)", with 304 = pour at the
start) is the last group of run A and the first figure of run A here.

Run A: "pour le fait du [prince de Conty], qui desire de ritirer, mais il ne sait a qui le confier, estant la
personne qui luy est de plus d'importance. Madame d'Angoulesme est a[...] du tout a la maison de [Messieurs de
Montmorency], et le principal appuy qu'il ait, soit des catholiques, soit de ceux de la religion, soit de ceste
maison, *qui s'acorderoit fort bien pour cela*, s'il y avoit quelque remuement. Vola pourquoy il desire faire
election d'ung fidelle serviteur et tabour le [lieu?], ou il le pourra mettre, *et point*, l'oter, instruire, gagner
monsieur de la Trimouille, pour ne donner aucung soubs son[...] a ceux de la religion, *estans tous* de nature
defians." (italics = clear words inside the run). Run B: "... qu'il y a [?] du Pape pour atanter a la personne du
[Cardinal de Bourbon], et disent avoir les lettres ...".

Key changes: the full word list (160 desire, 183 estre, 200̄ plus, 243 importance, 245 instruire, 300 personne,
309 quoy, 327 serviteur, 340 tabour, ...). 183 *estre* + n t stands for *estant* (grade I). Four name signs that are not
on the f. 103r panel as checked, taken from the gloss (grade C): prince de Conty (R crossed with X), Messieurs de
Montmorency, Cardinal de Bourbon, and the B4 sign (gloss "duc de Lorraine", not read). Writer's slips forced by
context and gloss: 8 *2* 22 for madame (3), *44* for 40 in princi-, *334* for 335 soit, *22* for 32 in fidelle, 57
without its bar for vo, 29̄ for vo in avoit. The scroll sign is b in soub[s] and u in ou: the writer's xi and Vs are not
separable on this page. Key and office differ at A8 (*a ceux*, office *a cause*), A6 (e-le-o-c-ti-o-n, office
*election*) and A7 (ga-g-ne-t, office *gagner*).

Failed or open here: the word after "est" in A3 (`lam ? plus plus`, gloss "a m..."); `340 20 34 ye plus` (key "tabour
le liet", gloss "tabour le lieu", no sense established); the three middle signs of c...e (ceste) and a sign in
pa?l (principal), illegible on the microfilm; run B pieces B1 (two signs), B2 `6 lam 344` (key "la a tout", gloss
"la plus..."), the overbarred 252 (not on the sheet as read), and B4 `28 25 203 NAME` ("te que fait", gloss "pour
mo[...] du duc de Lorraine").

### Second pass on f. 58 (3 Oct 2026): 89.5% -> 94.8%

Goal set by the coordinator: 95% for f. 58 and for the target. What was done (details in `fr3985_f58/reading.md`):

* Gallica's maximum for canvas 114 is the 4719 x 6676 image already used (`info.json`). The cipher block was fetched
  again as lossless IIIF PNG regions, deskewed, contrast-stretched and sharpened (greyscale microfilm: no channels to
  separate). Images in `img/fr3985_f58/`.
* Names panel f. 103v (fr. 3995 canvas 201) read at full resolution: prince de Conty, M. de Montmorency (singular),
  Cardinal de Bourbon and duc de Lorraine are all on it. The four name signs are now grade H.
* The writer's caret (p) looks like his lam (a). A3 `caret sigma ddag plus` = *port[ée]* ("Madame d'Angoulesme est
  port[ée] du tout a la maison de [M. de Montmorency]"), grade I. Other signs settled on the enhanced image: beta in
  *principall*, zig in *monsieur*, lam in *de la*, *lieu* in A6 (plus for perp, as in *aucung*).
* Run B: 29 with a bar = province 29, *Espagnols* (B1, gloss "aux Esp… au Pape"); 252 = *lettre* (B3: "qu'il y a
  lettre[s] du [Pape] pour atanter a la personne du [Cardinal de Bourbon], et disent avoir les lettres"); the B4 sign
  is the duke of Lorraine. B2 is `6 lam 340`, not 344.
* 340 re-read on a lossless crop of the sheet: "taboure", as the office glossed. "Tabour le lieu" is not settled; the
  sense wants *trouver*, and no reading of the sheet gives it.

Count (`decode58.py`): **235 of 248 (94.8%)**, run A 219/223 (98.2%), run B 16/25. Still one token short of 95%, so the
letter stays read in part. Of the 13 open tokens, 6 are illegible signs and 7 have certain key values that give no
sense.

Other documents, before and after this pass: nos. 24/25/60 63/104 (unchanged); key no. 57 and `words57.tsv` applied
to them give no sense ("qui pi bo ni lo fi …"), because they use a different, alphabetical two-digit system. No. 55
85/86 (unchanged; the one open group is '9P', a clear abbreviation). No. 78 0/6 (unchanged; too short). **Target
overall: 370/444 (83.3%) -> 383/444 (86.3%).** Nos. 24/25/60 are what keep it under 95%: their 41 open figures have no
key and no gloss.

### Third pass on f. 58 (3 Oct 2026): dictionaries and slip test. No change in the count.

* **"Tabour(er)" in the dictionaries.** Cotgrave 1611 (archive.org `fre_b2062733`): "Tabourer. To drumme; also, to
  rap, knocke, or thumpe (as on a Drumme) at a wooden window, doore, &c." Nicot 1606 (`fre_b1887920`) has *tabour*
  and *tabourin* (the drum) and no verb sense that fits. Neither gives "et tabourer le lieu ou il le pourra mettre" a
  sense.
* **Slip test for 340 and the run B groups.** 340 is a clear 340 on the lossless crop (closed 0). Of the key words one
  digit away (300 personne, 341 tenir, 343 tous, 344 tout, 345 veult, 346 volonte, 347 vous, 348 voir, 349 voie,
  350 venir, …), only **348 *voir*** and **341 *tenir*** make A6 grammatical: "faire election d'ung fidelle serviteur
  et *voir* le lieu ou il le pourra mettre". 348 is the better reading, but the office read *tabour* and nothing else
  supports a slip, so it is recorded as a conjecture (grade I) and not counted. The character LM cannot rank the
  candidates: any common word scores alike. B2 `6 lam 340` gives no sense with any neighbour of 340 either (gloss "la
  plu…"). B4 `28 25 202` with neighbours (27 se, 203 fait, …) gives at best "et ce se que fait [duc de Lorraine]"
  ("et ce que fait …", if 28 is a slip or null), not counted.

Count after all passes: f. 58 222/248 -> 235/248 (94.8%); no. 55 85/86. Entry (14 Oct 2026): 320 of 334 (95.8%);
f. 58 alone stays under the per-document read bar.

## Files

* `ct_3625_55.txt` — no. 55's eight runs (86 groups).
* `key_lauriere.txt` — first-pass table from no. 10's glosses; superseded (one group out of step).
* `key57.txt` — Nevers key no. 57 (fr. 3995 ff. 102–103), Laurière's key.
* `reading_3625_55.txt` — no. 55 transcribed and read with key no. 57.
* `ct_3625_10_glossed.txt` — no. 10's first three runs aligned with the interlinear decipherment (first pass, 21 Sept,
  before key no. 57 was known; superseded by the two files below, and agrees with them on every figure group but one).
* `ct_3625_10_blind.txt`, `ct_3625_10_rest.txt` — all thirteen glossed runs of no. 10 in sign names, with the glosses
  (the first five transcribed blind), and the unglossed run as U1; `check_3625_10.py` scores key no. 57 against the
  glossed runs (exit 0 = pass) and prints the decipherment of U1 (rerun 14 Oct 2026: unchanged).
* `fr3985_f58/` — fr. 3985 f. 58: `ct.txt`, `clear.txt`, `words57.tsv`, `decode58.py` (rerun 14 Oct 2026: 235/248),
  `reading.md`.
* `mk_validation.py`, `validation.tsv` — f. 58 token pairs for `docs/_validate.py` (pass, 11 Oct 2026).

## Remaining gaps

- Fr. 3985 f. 58, 6 illegible tokens: two signs in s..t (sait; a blot and a 2-shaped sign), the three middle signs of c...e (ceste, written '1 5 4'), the sign after 29-bar in B1 - blocker: illegible; Gallica's maximum (4719 px, lossless PNG regions, enhanced) does not decide them; no colour scan online, needs the manuscript
- Fr. 3985 f. 58, 7 tokens with certain key values and no sense: 340 'taboure' in A6 (context wants a verb; 348 'voir' one digit away fits, conjecture only; Cotgrave/Nicot give tabourer = to drum, to rap), B2 '6 lam 340' (gloss 'la plu...'), B4 '28 25 202' ('te que font', before [duc de Lorraine]) - blocker: open-codes; the sheet's values are certain and the office gloss does not resolve them

## Escalation

- [x] siblings: fr. 3625 OAI item list walked, no. 10 found as the key source and no. 55 located at f. 66r; (2 Oct 2026) fr. 3985 f. 58, the letter Tomokiyo names for key no. 57, located (canvas 114) and deciphered (89.5%, 94.8% after the 3 Oct retry); its verso is the address only; canvases 112-120 looked over (f. 56 and f. 59 are other 12 Aug letters in clear)
- [x] clear-pages: no. 10's interlinear decipherment aligned; the two glosses on no. 55 used; (2 Oct 2026) the office's interlinear decipherment on f. 58 used to check run A word for word and to name four name signs; it does not resolve the B2/B4 groups
- [x] known-keys: Nevers keys of fr. 3995 (Tomokiyo nevers.htm) reviewed; no. 57 (La Verrière, Feb 1593) reads no. 55 in full (29 Sept 2026, issue 13); (2 Oct 2026) the whole word list of key no. 57 read off f. 103r (`fr3985_f58/words57.tsv`) to try every word number on f. 58; overbarred 252 and two name signs then off the sheet as read
- [x] print: Tomokiyo nevers.htm and GL.htm, Mémoires de Nevers index: no printed decipherment; Tomokiyo's nevers.htm gives no reading of f. 58 beyond his anchor phrase "de nature defians" and 304 = pour; Mémoires de Nevers ii is not online (targets/nevers1593/NOTES.md); (3 Oct 2026) Cotgrave 1611 and Nicot 1606 checked for tabourer: no sense fitting f. 58 A6
- [x] key-rebuild: the first-pass table from no. 10 (key_lauriere.txt) superseded by key no. 57, the writer's own sheet; the key is complete, the open tokens of f. 58 are illegible or slips
- [x] retry: the no. 10 table applied to all 86 groups of no. 55 (19 read); key no. 57 then read all 86 (29 Sept) and every run of no. 10, the unglossed one included (PR 15, 30 Sept); (3 Oct 2026) f. 58 re-read from lossless IIIF PNG regions with contrast enhancement, names panel f. 103v read at full resolution, 13 tokens settled (89.5% -> 94.8%); slip hypothesis for 340, '6 lam 340', '28 25 202' tested against every key word one digit away (348 voir fits A6, conjecture, not counted)
