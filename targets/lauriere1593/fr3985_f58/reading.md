# BnF fr. 3985 f. 58: La Verrière to Nevers, Poissy, 12 August 1593

Session of 2 October 2026. This is the letter Tomokiyo (cryptiana `code/nevers.htm`, entry for key no. 57) names as using
Laurière's/La Verrière's key: "a letter from Laveriere to the Duke of Nevers, Poissy, 12 August 1593 (BnF fr.3985
fol.58)". No other target reads it; `targets/nevers1593` works other items of the same volume.

## Access

Gallica `btv1b90606498` (fr. 3985, microfilm, 485 canvases, all labelled NP). **f. 58r = canvas 114** (pencil "58" top
right, docket "12 d'aoust 1593"), f. 58v = canvas 115 (address only: "A Monseigneur / Monseigneur le duc de
Nivernois"). Canvas 112 is f. 56 (Revol? 12 Aug, Gerzy), 116 is f. 59. Full size 4719 × 6676, fetched through IIIF
`full/full/0/native.jpg` with no throttling (two requests). The key sheet f. 103r (fr. 3995, `btv1b525085665` canvas
200) was fetched again at full size to read the whole word list (`words57.tsv`; key57.txt only had the words of
nos. 10 and 55). Images (full canvases c114_full.jpg, c115_full.jpg, the deskewed c114_deskew.jpg, key_c200.jpg, all crops) are in `../img/fr3985_f58/`, git-ignored.

## The leaf

One page in La Verrière's hand, signed "Laverriere", "A Poissy ce xij aoust 1593". Clear French with **two cipher
passages**: run A, nine lines in the middle (page lines 11–19, 223 cipher tokens), and run B, short pieces in lines
21–24 (25 tokens). **The office's interlinear decipherment is written over almost every cipher line**, in a lighter
ink and a different hand, so the letter was read at the time. The cipher is key no. 57 exactly as in nos. 10 and 55:
two signs per letter, syllables row + 14 × vowel, words 99–353, overbarred places and v/z syllables, name signs.

Files: `ct.txt` (transcription of every run in the sign names of `../check_3625_10.py`, with the gloss as G lines),
`clear.txt` (the clear text), `words57.tsv` (key word list 99–353 and the province/town table, read off f. 103r),
`decode58.py` (applies the key, prints key value / reading per run, counts, runs the LM check).

## Result

**Run A reads; run B in part. 235 of 248 cipher tokens (94.8%) read as sense** (run A 219/223 = 98.2%, run B 16/25),
measured with `decode58.py`; token counts exclude Laverrière's own clear words inside the runs and two groups he
struck through. First pass (2 Oct): 222/248 (89.5%). French LM (`fr-1600-letters`) on the run A reading −1.66 per
character; `lm.best_language` puts French first (fr-1600-letters −1.69, fr-modern −1.97, Latin −2.58). Just under the
95% bar: the letter stays *read in part*.

### Second pass (3 Oct 2026): what changed and how

* **Images.** Gallica's maximum for this canvas is the 4719 × 6676 image already fetched (`info.json`), so there is no
  higher resolution to get. The cipher block was fetched again as nine lossless IIIF PNG regions (no JPEG artefacts),
  deskewed, and read with autocontrast and an unsharp mask. The microfilm is greyscale, so channel separation does not
  apply.
* **Name panel, f. 103v (fr. 3995 canvas 201), read at full resolution.** It lists "Mr le prince de Conty" (an R crossed
  with an x), "Mr de Montmorency" (o‡o), "Mr le Cardinal de Bourbon" (a hooked cross) and "Le duc de Lorraine" (H with a
  tall l), the four signs on f. 58. They are now grade H from the key, not C from the gloss. Montmorency is singular
  on the panel ("Mr de Montmorency"), not "Messieurs". The panel also gives Revol, Fresne, Sancy, La Force, Villeroy and
  others (not used in the cipher here).
* **The writer's caret (p) is a tall λ like his lam (a).** With that, A3 `caret sigma ddag plus` after *est* is
  **p-o-r-t**: "Madame d'Angoulesme est port[ée] du tout a la maison de [M. de Montmorency]" (grade I; the office
  wrote "a m…"). The same caret gives *princi-*.
* A4: the sign between *pa* and *l* is a cursive beta: *pall* (principall). A7: the undecided sign in *monsieur* is a
  zig (i); a struck 20 follows it. A8: the sign after beta in *de la* is lam. A6: `34 ye plus` is *lieu*, the plus
  standing for perp as in A8 *aucung* (the gloss reads *lieu*).
* **B1** `om 29_ ? PAPE`: the second sign is 29 with a bar, the province number **L'Espaigne ou Espagnols**, as in
  no. 10: "a [Espagnols] [?] [Pape]"; the office wrote "aux Esp… au Pape". One sign still open.
* **B3**: the bar over 252 is a flourish; 252 = *lettre*: "qu'il y a lettre[s] [du] [Pape] pour atanter a la
  personne du [Cardinal de Bourbon], et disent avoir les lettres". The clear "avoir les lettres" confirms it (grade I).
* **B4** `28 25 [303 struck] 202 LORRAINE`: the last sign is the duke of Lorraine (H). 28 25 202 = "te que font": no
  sense.
* **B2** is `6 lam 340`, not 344 as read in the first pass.

### Run A (after "… ce qui l'empesche c'est")

> pour le fait du [prince de Conty], qui desire de ritirer, mais il ne sait a qui le confier, estant la personne qui
> luy est de plus d'importance. Madame d'Angoulesme est port[ée] du tout a la maison de [M. de Montmorency], et le
> principall appuy qu'il ait, soit des catholiques, soit de ceux de la religion, soit de ceste maison, *qui
> s'acorderoit fort bien pour cela*, s'il y avoit quelque remuement. Vola pourquoy il desire faire election d'ung
> fidelle serviteur et [340] le lieu ou il le pourra mettre, *et point* l'oter, instruire, gagner monsieur de la
> Trimouille, pour ne donner aucung soubs son[…] a ceux de la religion, *estans tous* de nature defians.

(*italics* = Laverrière's own clear words inside the run.) The office's gloss agrees word for word except where noted
below. Tomokiyo's note on the entry (a Japanese comment in the page source) names the phrase **17 9 70 26 17 32 ω q n s
= "de nature defians"** as the one that let him identify the key, with **304 = pour** at the start. Both are here: the
phrase is the last group of run A (`17 9 70 26 17 32 om venus pi`) and 304 is its first figure.

### Run B (lines 21–24)

> … ny eust grand propos, et a [Espagnols] [?] [Pape] ce tiennent le plus empeschés [6 lam 340] … et ce [28 25 202]
> [duc de Lorraine] de ces … dict qu'il y a lettre[s] [du] [Pape] pour atanter a la personne du [Cardinal de Bourbon],
> et disent avoir les lettres, et je ne croys qu'il amenera.

### Key changes and slips

* Word list completed: `words57.tsv` has every word 99–353, the overbarred 200–203 and the province/town numbers, read
  off f. 103r. New values used here: 159 donnee, 160 desire, 183 estre, 200̄ plus, 243 importance, 245 instruire,
  252 lettre, 300 personne, 309 quoy, 327 serviteur, 344 tout; province 29̄ Espagnols.
* **183 = estre** stands where the sense and the gloss need *estant* ("183 n t"). Grade I.
* **340** reads "taboure" on the sheet (T column, between 339 trompette and 341 tient; re-read from a lossless crop),
  and the office also glossed *tabour*. In A6 the sense wants a verb like *trouver* ("faire election d'ung fidelle
  serviteur et [trouver] le lieu ou il le pourra mettre, et point l'oter"), but no reading of the sheet gives it. Left
  open.
  Third pass (3 Oct): the figure is a clear 340 on the lossless crop. Cotgrave 1611 gives *Tabourer* "to drumme;
  also, to rap, knocke, or thumpe … at a wooden window, doore", and Nicot 1606 has only the noun. Neither fits. Of the
  key words one digit away, only 348 *voir* (and, more weakly, 341 *tenir*) makes the sentence grammatical: "et
  *voir* le lieu ou il le pourra mettre". This is a conjecture (grade I), not counted, because the office also read
  *tabour* and nothing else supports a slip. B2 `6 lam 340` and B4 `28 25 202` give no sense with any neighbouring
  number.
* Writer's slips, each forced by context and agreeing with the gloss: `8 2 22` ma-*ca*-me for *madame* (3 = da);
  `caret 44 venus 30` p-*co*-n-ci for *princi-* (40 = ri); `334 tri` son-t for *soit* (335); `22 17 eps 20` *me*-delle
  for *fidelle* (32 = fi); `57` without its bar for *vo* in *vola*; `29_ sigma yi plus` a-*ve*-o-i-t for *avoit*.
* The scroll sign stands for *b* in *soub[s]* and for *u* in *ou* ("ou il le pourra"). On the key sheet itself the
  row-2 u sign (Vs) is a blotted scroll close to the row-3 b sign (xi), so the two cannot be told apart on this page.

### Where key and office differ

* A8 `lam 16 perp inf` is *a ceux* on the key; the office wrote *a cause*. Both give sense ("pour ne donner aucung
  [ombrage?] soubs son[…] a ceux / a cause de la religion"); the figures are *ceux*.
* A6 `Ep 20 sigma mu 42 f venus`: key "e-le-o-c-ti-o-n", office *election*; the sigma (o) is probably a second c.
* A7 the office's *gagner* over `5 varpi 23 plus` (ga-g-ne-t).
* A3 the office's "a m…" over `caret sigma ddag plus` (port).

## Open (13 tokens)

* A2 two signs inside *s..t* (*sait*): a blot and a 2-shaped sign that matches neither an a nor an i sign. Blocker:
  illegible.
* A4 the three middle signs of *c…e* (*ceste*), written `1 5 4`; no key value gives -est-. Blocker: illegible (shapes
  certain, value not).
* A6 340 "taboure": no sense. Blocker: open-codes (the sheet's value is certain, the intended word is not).
* B1 the sign after 29̄ (gloss "au"): one sign. Blocker: illegible.
* B2 `6 lam 340` (gloss "la plu…") and B4 `28 25 202` ("te que font"). Blocker: open-codes; the key values give no
  sense and the gloss does not resolve them.

The original is not digitised in colour: a colour scan or the manuscript itself (BnF) is the outside step that could
settle the illegible signs.

## Context

Poissy, 12 Aug 1593, the fortnight after Henri IV's abjuration (25 July) and during the truce talks; the conference
was moving between Mantes and Andrésy. La Verrière reports to Nevers (who was preparing his embassy to Rome) on the
young prince de Conty, who wants to *retirer* someone but has no one to entrust it to; Madame d'Angoulême
(Diane de France) is wholly with the Montmorency house, his chief support among both Catholics and Protestants; hence
he wants to choose a faithful servant and to win over M. de La Trémoille, the Huguenot leader. Run B reports something
[letters?] of the Pope for an attempt on the person of the Cardinal de Bourbon (Charles de Bourbon-Vendôme). The clear
text deals with Revol, Fresne, Sancy, and the rest of a payment of 1000 écus.
