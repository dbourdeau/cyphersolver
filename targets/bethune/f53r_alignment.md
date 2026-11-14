# f. 53r (24 Dec 1601), cipher block 1 aligned with its marginal gloss: 72, 6 and 66 fixed

Verification pass, 14 Nov 2026 (Claude Opus 5.5). Image: Gallica, BnF fr. 3484, ark btv1b52523722c, canvas 113,
full resolution (3926 × 5342 px), cut into half-lines at 0.75× and the figures re-checked at 1×.
Source gallica.bnf.fr / BnF.

The NOTES (third pass) named this block as the cheapest route to the open groups 66 and 72 and left its eight
cipher lines untranscribed. They are transcribed here and aligned with the gloss.

## The gloss (left margin, office hand, verbatim)

> Je confesse, je ne suis pas d'advis que vous pressiez sa Saincteté de me faire sçavoir sa volonté sur ce faict, ny
> que vous vous mettiez en peine de justiffier davantage la mienne, encore que sur le discours d'autruy. Il fault, nous
> confians en la prudence et cognoissance de sa Saincteté, de la sincerité avec laquelle vous avez jusques icy
> procedé, attendre ce qu'il plaira a sa Saincteté vous en ordonner.

## Transcription (labels of `key.tsv`; one pass, figures re-checked; `?` = unsure glyph)

The block opens after the clear words *"par sa responce"* (l. 2) and is marked with the same double cross as the gloss.
Clear words inside the block are in *italics*.

```
l2  6 8 n i y f m x ? Z 4 ff g ... x Cm x o 4 x: + b Z c ? g x; 72 , T 63 , r b Z
l3  ? , 6 +. x Z 3: 9 4 c f ? x 66 p + S f LS q Z g p x p: a , g a x; 72 p + c ? x Z
l4  e p ? Z q Cm LS o Z ? g Cm +  *justiffier davantage*  g u Cm Cm LS Z PH g e f
l5  Z q x; q p x f, x  *discours d'aultruy. Il fault*  n, b ? 4 ? Z ? ? g ? p g g ,
l6  T o p + LS p: x: Z d c 4 g ? x Cm p Z p +. 6 Z g g , Z ? LS b Cm x Cm p Z
l7  i: g x, S Z 72  *avez*  x, + Z a S, ? Cm + 4 q Z S Z 63 p. 61 S T S 4 . . 4
l8  PH 6 72 Z LS + o Z f LS Z 2  *Mais [ce] ...* (clear text resumes)
```

## Alignment (only the anchors that fix values; the letter values elsewhere follow `key.tsv`)

| cipher | gloss | value fixed |
|---|---|---|
| l2 `x; 72 , T 63 , r b Z` + l3 `?` | *que vous pressiez* | **72 = vous** (T = p, 63 = re as known) |
| l3 `6 +. x Z 3:` | *sa Saincteté de me faire* | **6 = Sa Sainteté**; `+.` = de; `x Z` = me; `3:` = faire |
| l3 `9 4 c f ? x` | *sçavoir* | 9 = s(c)? (low) |
| l3 `66 p + S f LS q Z` | *sa volonté* | **66 = sa**; p + S f LS q Z = volonte (as in the 10 Nov minute) |
| l3 `p: a ,` | *ce faict* | `a,` = faict confirmed |
| l3 `g a x; 72 p + c` | *ny que vous vous* | **72 = vous** again, followed by *vous* spelled out |
| l5 `n, b ...` | *nous confians* | `n,` = nous (medium) |
| l6 `x:` | *et* | confirmed |
| l6 `+. 6` | *de sa Saincteté* | **6 = Sa Sainteté** again |
| l7 `72` + clear *avez* | *vous avez* | **72 = vous** again |
| l7 `p. 61 S T S 4` | *ce qu'il pla[ira]* | p. = ce, 61 S = qu'il, T = p, S = l, 4 = a |
| l7 end `4` + l8 `PH 6 72 Z LS` | *plaira a sa Saincteté vous en* | PH doubles the a of *plaira* (= *plaira a*); **6** and **72** again; Z LS = en |

Result: **72 = vous** on four aligned occurrences, **6 (a standalone figure) = Sa Sainteté** on three, **66 = sa** on one.
This also resolves the counter-indication recorded in NOTES (the final `72` of the D1 block on f. 49v against a
footnote ending *"a luy en parler"*): with 72 = vous fixed four times here, the D1 block must run past the passage its
footnote glosses, or its tail was misread at 1.5×.

Inside a word, 6 stays the letter *a* (`6 7 1` = *ati* in *gratification*, 10 Nov), so 6 is read as Sa Sainteté only
where it stands as a word. In the 22 Nov runs the sequence `4 6 x:` (*a Sa Sainteté et*) occurs at f. 46v ll. 9 and 12,
`4 6 x: f LS 17` at l. 9 (*a Sa Sainteté et au … Aldobrandin*), in a passage that goes on in clear *"après
toutesfois en avoir conferé avec le Card.al d'Ossat"*.

## Check on a portion not used to derive the values (pre-registered, 14 Nov 2026)

Pre-registration frozen before the check (SHA-256
`285ddb07edf49f548b2064c0fa95d701850322a78d9472cda256d6111a9bd1de`): every locatable 72, standalone 6 and 66 in
the glossed blocks of f. 56r and f. 49v-50r is checked against the gloss; confirmed if n ≥ 4 and ≥ 80 % agree.

* f. 56r (two blocks; glosses *"…vous prudemment garde…"*, *"Le Roy d'Espaigne est mal pourveu d'argent…"*): no 72,
  6 or 66 found in the lines read; `7` = le Roy d'Espagne agrees with the second gloss.
* f. 50r: one 72, in `x, d, 72 63 o …` under the gloss's *"…que je vous …"*, agrees. The f. 50r gloss is cut by the
  binding, so the other groups cannot be checked there.

n = 1 (agrees): **not conclusive** under the pre-registered rule. The protocol measurement (≥ 300 signs against 200
shuffled keys) does not apply to three code groups with one to four occurrences: **not measurable**. The values rest on
the verbatim alignment above.

## Second-hand effects on the 22 Nov runs (decoded by eye from the image, not read)

With the key above and the clear frames, three runs of f. 46r give sense. They are *probable*, not sure, and the letter
stays decoded, not read:

* l. 2 `73 Z g Cm m f q Cm 4 71` = *vostre negotiation* (the first hooked m standing for *e*, plain m = g).
* l. 6 `… b + r PH Cm g o + g m 4 LS …` = *…correspondance…*, and the end of the run `m x g b 63 71` = *discretion*,
  before the clear *"que je vous ay recommandé"*.
* l. 5 `f, r 63 g o Z b …` = *le respect …*.

The hooked m standing for *e* in two of these words is a further case of the glyph merges recorded in NOTES.
