# Anonymous figure cipher, 28 October 1586 (BnF Clairambault 357, ff. 167-168)

Status: in progress (site page not yet updated). f. 168r (the clear copy) reads, and since the 23 Oct 2026 re-read the f. 167 interlinear part reads too (grade B).

**22 Oct 2026, reading audit** (George Lasry's test): the f. 168r clear copy of f. 167r ll. 1-30 builds sentences; the interlinear decipherment after the cross mark (f. 167r) and on f. 167v is transcribed only as fragments, with holes in most sentences: *decoded, not read*. The entry is split in two in profile.json; claim read -> read in part (about half, estimated).

**23 Oct 2026, re-read (b26):** f. 167r from the ✝ and f. 167v transcribed line by line on the full-resolution canvases (clear text, glosses, figure groups: [`texts/f167_interlinear_transcription.txt`](texts/f167_interlinear_transcription.txt)); unglossed and cut groups decoded with `key.md` (`research/reading_audit/b26_clair_dec.py`). Reading [`texts/f167_interlinear_reading.md`](texts/f167_interlinear_reading.md), English [`texts/f167_interlinear_en.md`](texts/f167_interlinear_en.md), log [`texts/f167_interlinear_reread_log.md`](texts/f167_interlinear_reread_log.md); 0.758 clean sentences (explicit holes 0.909). Corrections to the fragments below: "Cambaronne" = *l'embarquement*, "Coride" = *a la Floride* (after *le feu admiral*: Coligny's Florida venture), "Saisonne" = *vaisseaulx*, "Il se trouvera" = *Il se promectoit*; the recto's last words *et que luy* run on into the verso's *Fumée, si luy voulliez commettre cette charge soubz couleur d'autre voyage*: Fumée offers ships for an embarkation, i.e. the war in England. 73 = d confirmed. profile.json: both entries read; class read.

Catalogue item 14. Session 2026-09-18.

## Result

**The letter is read from a contemporary decipherment that is bound with it.** Tomokiyo reconstructed part of the key
(cryptiana `henryiii.htm`, "Anonymous Figure Cipher (1586)", image `henryiii_Anonymous.png`) and said "about two thirds
of the first page is not deciphered". His note does not mention either of the following, and together they cover the
whole letter:

1. **f. 168r is a clear text**, in a secretary hand, of f. 167r from the opening ("Jay receu voz deux lettres en ung
   mesme temps dont jay faict communication a M^r de la Forest et M^r de Corbet…") down to the mark ✝ ("…qui passe
   avant ✝"). The same ✝ stands in the left margin of f. 167r at about line 30, the point where the next item begins.
2. **From that ✝ to the end** (the rest of f. 167r and all of f. 167v down to the date and the signs), the decipherer
   wrote the plaintext **between the lines**, word by word over the figure groups.

These are the "two thirds" that Tomokiyo called unread. The key agrees with both layers wherever it was checked
(see below), so the clear text is the decipherment of this ciphertext and not a separate letter.

## Source

- Gallica: Clairambault 357 = `ark:/12148/btv1b9001053r` (687 canvases, all labelled NP). The volume is titled
  "Documents originaux … XLVII Règne de Henri III, 1583-1587". The ark was found through a Gallica SRU `dc.source`
  query after a 429.
- **f. 167r = canvas 331**, **f. 167v = canvas 332** (date, signs, BnF stamp), **f. 168r = canvas 333** (the clear
  text, foliated "168", old numbers "375", "7433"). Full-resolution IIIF images (about 3400-3700 × 5700) are in `img/`,
  which is git-ignored and can be re-fetched with `python ../vasto1527/clairfetch.py btv1b9001053r img full 331,332,333`.
- Crop tools: `linecrop.py` and `stack.py` (a line at a given y, cut in three stacked parts at 1.5×).

Note that f. 167r is not solid cipher: the writer drops into clear for stretches (l. 2 ends "Bourdeaux", l. 3 reads
"tres fasché du bon terme en quoy sont voz affaires", in clear, before the figures resume), and f. 168 copies those
stretches too.

## System (Tomokiyo's table, checked and extended)

The system is a homophonic two-digit figure substitution written as a continuous stream, with a few nomenclator signs,
nulls, and 78 = vous, 81 = que, 83 = il, 92 = et. Tomokiyo's table is `henryiii_Anonymous.png`. Checks against the
interlinear glosses:

| Figures | Gloss | Reads with the key as |
|---|---|---|
| 74 24 34 28 29 72 | Guienne | g u i e n e |
| 26 43 28 82 | tres | t r e s |
| 18 37 19 35 34 25 28 19 26 | confident | c o n f i d e n t |
| 25 24 # | du Roy de Navarre | d u + sign |
| 35 24 64 87 | Fumé | f u m e (**87 = e**, not in Tomokiyo's table) |
| 92 81 | et que | et que |
| 25 28 | de | d e |

The key-based reading of the upper f. 167r also matches f. 168. For example, the run "…25 28 88 22 20 24 26 88 72 82 70
14 | 18 28 …" reads "de[s] autres pla|ce[s]", and f. 168 has "…et autres places qui vous ont esté distraictes". The line
glossed "pour ne me sembler a propos de le faire" matches f. 168 "…ne me sembler a propos de le f[aire]".

Additions to the key:
- **22** is very frequent and reads as a null in every checked word ("Guienne 22 tres", "de r 22 autres"). It could
  instead stand for the lost s of "des", which is not settled.
- **66** and 45 31 are nulls or signals (for example "C 66 35 24 64 87" = "C [null] Fumé"). 45.31.73.65.21 at the
  opening of the letter and again before D are dotted groups outside the text stream.
- **87 = e** and **71 = a** (in "visadmiral" and "tres confident").
- Nomenclator signs:

| Sign | Meaning | Status |
|---|---|---|
| # (a double-barred sign) | Roy de Navarre | glossed three times |
| D (double-stroked) | Angleterre | Tomokiyo; glossed "d'Angleterre" twice (once correcting a struck "la Royne") |
| && | Monsieur de Mayne | Tomokiyo; glossed "Monsieur du Mayne" on the verso |
| R | Navarre | glossed "Navarre" on f. 167r l. 33; probably Nérac |
| ✝ C | head of a proper-name group | before "Fumé" and elsewhere |
| ⊖ | uncertain | near "Huguenotz" in the glosses, not confirmed |
| Ω, ∞, ✝o | uncertain | Ω with Villeroy; the others stand for places or people named on the verso |

## Text

Transcribed from the images. Abbreviations are expanded silently, and [?] marks an uncertain reading. f. 168 is a
continuous clear text. The glossed part is given as the glosses read, and figures without a gloss are marked (…).

### f. 168r (= f. 167r, ll. 1-30 in cipher)

> Jay receu voz deux lettres en ung mesme temps, dont jay faict communication a M^r de la Forest et M^r de Corbet.
> Charry … estant tres fasché du bon terme en quoy sont voz affaires, et que serez rentré dedans au plustost [?].
> Indisposé d'une maladye qui ma travaillé pres de deux moys, qui a empesché vous escrire. Pendant ce temps la
> qui fut la cause que le commis a l'abbé de la Couronne [labbé written above a struck word], par le moyen se
> debvroit entendre … de M^r de Nemours [?], et remettre vingt [?] de leurs troupes [?] qui prendroit a moy
> advis, plustost par vous le mariage effectué, auquel je montroit bien avoir regret, … ne m'en retint pas de luy
> dire, comme le voyage et negotiation qu'il entreprenoit [?] estoit contraire a celle de l'an passé, seroit trouvé
> estrange non seullement de ses amys, catholiques de France, mais des princes estrangers. Sur quoy il apportoit
> tout ce qu'il pouvoit de raisons. La meilleure et plus apparente [?] estoit … de la Royne mere, dont il bailloit
> appuy a qui il vouloit, qui luy promettoit l'asseurance [?] de ne desirer faire la paix qu'a condition qu'il n'y
> auroit que la Religion catholique en France, et passa oultre, que s'il eust esté aux termes qu'il avoit
> designez avec vous, il n'eust entreprins le voyage, que chascun avoit faict son affaire, et l'avoit on laissé seul
> abandonné. Le bruit que ces jours icy [?] avoit couru par tout que voulliez venir est bien jusques a moy. …
> [au]mosnier [corrected "aon" over a struck word] cest [?] qui venoit en ce pays, … compagnye et … ressentira
> [?] richement … que me donn[e] … a pense … tout ce bruict que vous recommandiez … pour ne me sembler a propos
> de le f[aire]. Cependant ne pressé ne comprise [?] que sont les seulles causes qui vous y doivent precipiter. Je
> croy que faisant des stances [?] et autres places qui vous ont esté distraictes vous les pourrez avoir ou du
> moings faire congnoistre que vous n'y quictez rien. La poursuite ne les travaux [?] de la brouillerie du Roy de
> Navarre et de vous, que je tiens tres difficile pour la qualité que chascun de vous a prinse, luy de [protecteur?]
> … Catholiques … Huguenotz … qui passe avant. ✝

The last sentence is uncertain. The image seems to show "luy de protecteur les Catholiques … les Huguenotz", but the
word before "les Catholiques" may not be "protecteur", and the words between are not read. The sense expected is that
Navarre protects the Huguenots and the addressee the Catholics. It needs the matching cipher words decoded.

### f. 167r from the ✝ (interlinear decipherment)

> ✝ Je vous diray que j'ay esté pressé, et la seule bonne volonté d'un que vous congnoissez s'y a mis de
> pratique, au moyen de reputation, qui s'appelle [✝ C] **Fumé, visadmiral de Guienne, tres confident du Roy de
> Navarre**, bien qu'il soit catholique et loyal a moy. [Il] a donné le retour de deça pour quelque negotiation, car
> je sçay comment de ce voyage a [R = Navarre/Nérac?] et a [✝o] … Il est bien adverty. Il m'a plusieurs foys
> **proposé cette reconciliation**, qu'il dict luy estre aussy aysé et facille comme je la luy fais difficille et
> malaisée, et en … c'est bien si avant que … si vous y voullez entendre … aux … moy … ce … Il m'a quasy prié de
> la part du **Roy de Navarre** [#] la bonne proposée [?] et que [92 81] Il se trouvera [?] … mesme … la guerre
> … sy [D =] **Angleterre** … moyen a la bonne fin [?] … par ce seul moyen se faisoit … asseurance que **la Royne
> [D] d'Angleterre ne pourroit procurer** … des [⊖] … de la court …

### f. 167v (interlinear decipherment, glossed throughout)

> **Fumé**, si luy voulliez [?] commettre cette charge, … d'autre … [ai]sance [?] qu'il … voyage. Il vous
> fournira d'autant … pour Cambaronne [?] … avant [✝] envoyant … la Royne mere, le filz … admiral, a la
> Coride [?] … mais c'est pour vous a vostre service … Monsieur … Jay envoyé a [88 28 18 19 25 14 19 …]
> **Villeroy** [Ω] qui me manda que pour contenter **Monsieur du Mayne** [&&] a l'instance, prieres et requestes
> … a faict son estat a premier de sa … comme aussy se retirent les … que Il n'y a de toutes choses et mesme
> … Il ne pouvoit faire … conclure la paix et si l'on donne quelque advantage aux Huguenotz [⊖?] … l'on se
> fonde …

The verso glosses are faint in places, and this pass did not read them word by word. The words above are the ones read
with confidence.

## Content (summary)

The writer is a Catholic nobleman of the Angoumois or Saintonge (the abbey of La Couronne near Angoulême; Charry;
M^rs de la Forest and de Corbet), writing on 28 October 1586 to a League leader. The addressee is paired with the King
of Navarre as heads of the two religious parties, with Mayenne named in the third person, so the addressee is
probably Henri, duc de Guise. The writer reports:
- He has been ill for two months.
- Catherine de Médicis's negotiation with Navarre (the Saint-Brice interviews, autumn 1586) is backed by the
  promise to make peace only on condition of Catholicism alone.
- Navarre's Catholic confidant **Fumé, vice-admiral of Guyenne**, has repeatedly proposed through him a
  **reconciliation between Navarre and the addressee**.
- There is talk of the war and of what **the Queen of England** could or could not procure.
- Villeroy has written to him about satisfying Mayenne.

The sender's signs at the foot of f. 167v are not identified.

## Open

- Word-by-word decoding of the ~30 cipher lines above the ✝, to check f. 168 phrase by phrase. So far this was done
  on sample runs only, all of which agreed.
- Several uncertain words in the f. 168 transcription (ll. 2-3, 6-7, 17-19).
- The f. 167v glosses, especially the proper names at Cambaronne [?] and Coride [?], and the sender's signs.
- Identity of Fumé (a vice-admiral of Guyenne of that name, probably of the Fumée family) and of the addressee.

## Remaining gaps

Closed 23 Oct 2026: f. 167r after the cross mark and f. 167v, once read only in fragments (texts/f167_interlinear_reading.md).

- a few unglossed figure strings on f. 167r-v (under "ne pourroit procurer", "si porte bien …", the last line before the date) - blocker: illegible; strokes run together and the glosses are cut or faint
- the sender's signs at the foot of f. 167v (8 X X 8) - blocker: no-key-material

## Escalation

- [x] siblings: none found in Clair. 357 round ff. 167-168
- [x] clear-pages: f. 168r clear copy and the f. 167 interlinear found
- [x] known-keys: Tomokiyo's partial table, checked and extended
- [x] print: none found
- [x] key-rebuild: unglossed groups of the interlinear part decoded with the table (23 Oct 2026); 73 = d confirmed
- [x] retry: the verso glosses read word by word at full resolution (23 Oct 2026)
