# BnF fr. 3621 no. 97: the re-read (22 Sept 2026)

Charles III of Lorraine to the comte de Vaudémont, Nancy, 18 June 1592 (fol. 109, Gallica canvas f227,
DECODE R9449). This replaces section 5 of `no97_reading.md` as the reading of record. Transcription and
word grades: `no97_reread.txt`; measurement: `../measure_reread.py`.

## 1. What the re-read changed: the system is a reciprocal pair cipher

Going back to the page with the 18 Sept decode beside it showed that the key was not 44 free symbols
at all. Laid out as pairs, the 18 Sept values already said so: glyph *a* = i and glyph *i* = a, *o* = r and
*r* = o, *q* = d and *d* = q, *n* = s and *s* = n. Every letter of the hand stands for its partner in eleven
fixed pairs:

    a<->i   b<->p   c<->f   d<->q   e<->t   g<->u   l<->y   m<->z   n<->s   o<->r   h<->x

(22 letters, the whole alphabet of the period). Plus:

* **two dots under a letter double it**: ṇ = ss (*promesses*, *assister*, *passer*), c̤ = ff (*affin*),
  c̈ = tt (*remettre*);
* the looped æ is a **null**, used as a word divider (*peu · d'execution*, *belles · promesses*);
* a small set of **special signs** (λ, Θ, ꝗ, m̄, π, γ, capital E, t with a low bar, reversed 3, a figure-4
  form); Θ = s is secure (*chemins*, *audits*); the rest are open;
* **figures for syllables and words**, at least some syllabic: **31 = "ma"** (*com-31-nder*, *de-31-nde*,
  *me 31-nde*, *31 resolution*), **139 = "vous"** (*chemins, 139 tiendres*; *et 139 ne manquies*),
  **145 = "me"** (*affin que 141 ne 145 delaisent*).

The two transcription merges that did most of the damage in the 18 Sept decode:

* the transcription's **c** was two glyphs, the secretary **e** (→ t) and **c** (→ f). The old key had
  to send it to t, so every f in the letter was lost (*intiniment*, *satistait*); five plain letters
  (b f g x z) had no cipher value at all, as the page write-up noticed;
* its **B** was two glyphs, the beta-like **b** (→ p) and the looped secretary **h** (→ x): *du peu* but
  *ceulx* and *d'execution*.

Correcting those two, and reading the dotted and doubled forms as doublings, turns most of the 18 Sept
"connective tissue" into plain French with no further guessing.

## 2. The reading

Graded words in `no97_reread.txt`; here rendered as running text. `[?]` = not read; `[word]` = doubtful.
Line numbers follow the manuscript (L19 is clear).

> L00 [?] j'ay esté [?] infiniment [?] mal satisfait [?] du peu d'execution [?] vous
> L01 [57] [?] et ceulx de la [98] [?] ont, de tant de belles promesses [141] [?] avoient fait,
> L02 [l'?] de me assister et de [122] [123] [?] pionniers [?] et [?] munitions [?] [dressera]
> L03 [?ien] fait. Vous [?] le faire l'entendre [?] clairement ausdits [57] [?], et les de-
> L04 -putés de [?] [98], et vous ne [manquiés] à me [?] [demander] [?] [141] [?] conno-
> L05 -issent le juste mescontentement [?]. Vous [?] dois avoir l'[137] [?]. Il [?] f-
> L06 -auldra [?] de prudence, affin [que] [141] [?] ne me delaissent [?] tout à cou-
> L07 -p [?] et de munitions et chevaulx [?] [121] [?] et aultres commoditez [?]
> (clear:) aussi si Dieu nous fault la grace de prendre Chasteauvillain
> L08 [?] [57] me [?] demande [?] la plaine. I-
> L09 -l fauldra [?] le remettre [13] ou le [?] luy [?] dire. Vous [?] escrire [?] afin de [?]
> L10 recepvoir mon commandement [?]. Ne [?] mettre [?] quelq[u'un] qui, pour y comma-
> L11 -nder et conserver la plaine [?] quant à ne vous, ceulx de [88] [?] [?] pour fa-
> L12 -ire [?] passer [?] les [?] leur [?] ses promesses ne me [?] induiront [et re-]
> L13 [-solument] [?ien] [?] le fera [?] le [?] des [?] ... apres l'effect [?] de
> L14 Chasteau[v]ilains. Me [ne fais] [es] de ramener mon armée [droites] [?] quartiers de
> L15 la Faulche [?] et me preadvertir [?] jour. Vous me [?] [pour] [?] me ma-
> L16 -nde [?] chemins. Vous tiendrés [?] s'il ne vous [?] fault, pour tant faire paroistre ausd-
> L17 -its de [88] ma resolution [146] [?ien] le peu de moien que [?] secours. Vous me promet[tés] par de-
> L18 -là pour [?] le [?] Chasteau[v]ilain, ainsy vous l'on avoit [?] promis [?]
> (clear:) et de la ilz pourroient tascher de remedier, ou bien juger le peu de suiect qui me doibt occasionner
> L20 [asseurté?] ses promesses [?] faire [?] passer oultre [?] [103] [?]

The substance, where it reads: the Duke has been *infinitely ill satisfied with the little execution*
of what was promised; certain people (57, "ceux de la 98") had *so many fine promises* made to help him
with (122, 123), pioneers and munitions; he wants it made plain to them and to the deputies of 98, and
asks his son not to fail to demand of them … that they recognise *le juste mescontentement*; *il fauldra
[user] de prudence, affin que 141 ne me delaissent tout à coup*, both for munitions, horses and other
supplies. After the clear line on taking Chasteauvillain: someone must be put there *pour y commander et
conserver la plaine*; he means *de ramener mon armée … ès quartiers de la Faulche*, wants to be
*préadverti* of the day; *vous tiendrés [les] chemins*; he sets out *ma resolution … le peu de moien que
[j'ai] de secours*, what *l'on avoit promis* about Chasteauvillain, and whether to *passer oultre*.

## 3. Measured

`python measure_reread.py` (rule in the script's docstring: a cipher token is read if the word it
belongs to is graded H or C):

| | tokens | read | share |
|---|---|---|---|
| all cipher tokens (letter signs, specials, nulls, figures) | 1,105 | 790 | **0.715** |
| letter signs only | 1,067 | 769 | 0.721 |
| nomenclator figures (139, 145, 31 assigned) | 38 | 21 | 0.553 |
| **before**: same words, 18 Sept key and tokens decode them identically | 1,105 | 449 | 0.406 |

Four emendations among the read words (the key decode differs from the reading): two omitted *v* in
*Chasteau(v)ilain(s)*, *q(u)e*, and *promesses* where the page has a special sign in the word.

The "before" figure is lower than the 18 Sept estimate of ~70% coherent because it demands that the old
decode give the word exactly, not that a reader recognise it through *intiniment* and *satistait*.

## 4. What is not read (315 tokens)

* **Special signs** with no settled value: λ (11), m̄ (9), U (8), E (4), π (4), γ (5), ꝗ, t with a low
  bar, the figure-4 form, reversed 3 in some places. Most unread words contain one. Several may be
  nulls (m̄ and λ stand between whole words), but that is not proved.
* **Eleven figures** (57, 98, 141, 122, 123, 13, 137, 88, 146, 121, 103; 17 tokens).
* **Four runs** where the glyph sequence does not decode to French under the pair key even with the
  specials set aside: L12 *i t G y B G r J c r o* (after *passer*), L13 middle (*des … apres*), L18
  *pour [?] le [?] Chasteauvilain*, L20 *m'a d...te*. These need a second look at higher magnification
  than the IIIF 1:1 crops, or they hide more special signs.
