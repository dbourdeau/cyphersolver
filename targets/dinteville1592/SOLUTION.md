# Dinteville to the duc de Nevers, Langres, July 1592: BnF fr. 3621 f. 130 (DECODE R9451) read; key rebuilt from f. 128

Catalogue item 183. Previous status in this repo was "attempted 21 Sept 2026, not read" (write-up `dinteville1592.html`,
updated 24 Sept). Contribution of 6 Oct 2026.

**Result: f. 130 deciphered.** 514 of 522 cipher tokens are read (98.5%, measured by `scripts/measure.py`), with no
emendations and 8 tokens open. The key comes from the sibling letter f. 128 and its contemporary interlinear
decipherment, and it reads f. 128 completely.

## Prior work

- **D. Bourdeau** (this repo, 21–24 Sept 2026): found the f. 128 crib. His alignment test failed; see below.
- **NoAutopilot/cipher-lab**, `ciphers/fr3621-dinteville-1592/` (public from 3 Oct 2026). They:
  - rebuilt a key from the f. 128 gloss, aligned to the 1882 print;
  - showed it reads f. 130 far better than shuffled keys;
  - published word fragments, judging their own result as fragments with about half the signs certain and the
    word-division gate failing.

  Every fragment they give agrees with the reading here: *demeure seul … auec les habitans*, *conseruer … en
  l'obeissance*, *oultre le … il ne se leuera*, *dehors les … seruiront … tant … leur … que a la*, *la ville et le roi*,
  *pourvoir de … retirer d'aultant qu'il i a … l'honneur*.

  Their open rows are the ones resolved here:
  - h, which they key as *u*, is *p*;
  - Δ, which they key as *a*, splits into plain Δ = *f* and Δ with a tail = *a*;
  - their "stemmed zero 0′, mostly s/p" is the pair ð+ = *s* / ð with ascender = *p*.

  This contribution completes their partial result into a continuous reading. It was reached independently: we found
  their folder only after the reading and the blind test.

## Why the earlier attempt found no key

`targets/dinteville1592/align.py` (one sign → one letter, up to three null sign-types, exact length) is sound. Two
inputs defeated it:

1. **The marks are part of the signs.** The small crosses and strokes were taken for the decipherer's marks over
   unexpanded code signs. They are diacritics that make new cipher signs:

   | sign | value | sign | value |
   |---|---|---|---|
   | ∇ | a | ∇ with a rising stroke | t |
   | Δ with a cross or tail below | a | plain Δ | f |
   | ð (o) with a cross above | s | ð with a plain ascender | p |
   | ψ | o | ψ with a cross below | null |

   Merging each pair into one sign produces the "same sign must be both *o* and *d*" contradiction.
2. **The gloss was read too literally.** The interlinear reads *Gennes* (Genoa), not *Geneve*, and the cipher spells
   *dessendre*.

`scripts/bourdeau_test.py` re-runs the original test on f. 128 line 2:

| | gloss read as *dascendre … geneve* | gloss read as *dessendre … gennes* |
|---|---|---|
| marks merged into the base sign | 0 keys | 0 keys |
| marks kept as separate signs | 0 keys | **1 key** (only the leading ‖ is a null) |

## The system

A homophonic substitution of letters, digits and signs, with diacritic variants and a few nulls. No nomenclator was
seen. The full key is in `key.tsv`; one line per sign token is used in `f128_signs.txt` and `f130_signs.txt`, whose
headers define the tokens.

| letter | signs |
|---|---|
| a | ∇, Δ+, B |
| b | ÷ |
| c | #, ξ |
| d | #, 3 |
| e | o, 1·, 1 |
| f | Δ, long-s with bar |
| g | ϙ |
| h | π |
| i/j/y | ꝑ, ⊥, 1 |
| l | 4, + |
| m | z, Z-shaped 2, Ɲ |
| n | ƒ, Ꝛ (r over a cross) |
| o | ψ, ç-hook |
| p | ð with ascender, ɧ |
| q | a |
| r | ϖ, c |
| s/x/z | □, ð with cross, Π |
| t | ∇ with stroke, ʒ, n |
| u/v | α, mʒ |

- Nulls: ψ+, # with a long stroke, ‖, and the joined a-loop sign `aP`.
- `#` stands for *c* or *d*, and `1` for *e* or *i*. Context decides both, as the period decipherer had to.

## f. 128 (no. 114, 1 Jul 1592), read in full with this key

> …[un gentilhomme de M. de Gondy venant de Florence] m'a dit auoir veu dessendre a Gennes deus millions d'or
> d'Espaigne. Il y a laissé a Besançon quarante cinq mulets chargés qui doiuent partir dans trois jours et prendre le
> chemin de Vesou[l], n'ayans que cent chevaux d'escort[e] (ink blot)

Spanish money landed at Genoa and taken up the Spanish Road through Franche-Comté. The contemporary gloss agrees
throughout ("m'a dit" over the first run).

**Independent check against print.** The full plaintext of f. 128 is printed in *Revue de Champagne et de Brie*
t. XII (1882), p. 340. The source was found by NoAutopilot/cipher-lab; see *Prior work* below. It reads: "m'a dit avoir
vu descendre à Gène 2 millions d'or d'Espaigne. Il en a laissé à Besançon 45 mulets chargés qui doivent partir dans
trois jours et prendre le chemin de Vesoul, n'ayant que cent chevaux d'escorte". Our decode matches it word for word,
including *Gennes* against the gloss-reading *Geneve*, *doiuent partir* where the gloss abbreviates, and *d'escorte*
under the blot.

The same 1882 instalment summarises only the clear text of f. 130 (4 July 1592). It covers the enemy threatening
Châteauvilain again, powder sent there, the comte de Châteauvilain to be sent back, and the Lorraine army near
Joinville. That fits the cipher's "[l'ennemi] faict estat d'y retourner et l'emporter … qui me faict les y renvoier
avec de la pouldre".

## f. 130 (no. 116, "IIIIe juillet 1592")

The cipher is given in bold. The clear text is from `clear_f130.txt`, a separate full transcription of the leaf; [?]
marks words uncertain there. Original spelling is kept; ? in the cipher marks open tokens. The clear text says Langres
asks for 200 horse and 200 foot, and Châteauvillain is blockaded. The cipher gives the reasons Dinteville did not
write in clear.

**Passage 1 (ll. 4–8).** …ce que J'ay eu auiourdhuy aduis de plusieurs endroitz que lennemy[?] faict estat dy
retourner et **l'emporter, ???? il n'y estoit pourveu, qui me faict les y renvoier avec de la pouldre.** vous
Iugerez[?] / aussi si vous plaist Monseigneur que **je demeure seul ici avec les habitans et** que la[rmée] … Lorrains[?]
se fortiffie de ce qui estoit du coste de Strasbourg **et, retournant a moi, il me seroit malaisé d'y conserver ceste
place en l'obeissance qu'[?]elle y est.** Messieurs de la Ville supplient tres humblement le Roy et vous d'y placer
deux cens chevaulx et deux cens hommes de pied…

**Passage 2 (ll. 11–16).** …Il y a plus de cinq cens chevaulx de garnison ennemye et le pais est […] soubz
contributions sur ce qu[i …] **si les forces n'y sont placées, oultre le hasart que court la ville, il ne se leuera un
denier de tailles. D'aultre costé, l'en y voi[t] le dedans si bien basti qu'il ne soit plus a craindre que le dehors;
les forces serviront tant a les contenir a leur devoir que a la deffence de la ville. Le Roi et vous m'excuserez si je
pass[?] de mot, que [?] s'il ne plaist a Sa Maiesté d'y pourvoir, de m'en retirer, d'aultant qu'il y a a perdre la vie
et l'honneur** comme[?] luy. / Je la doibs a sa Ma(jes)te…

**Joins.** Every cipher run continues the grammar of the clear text on each side, as transcribed independently:
- "et | l'emporter"
- "que | je demeure"
- "habitans et | que la[rmée]"
- "Strasbourg | et retournant"
- "qu'elle est | Messieurs de la Ville"
- "l'honneur | comme luy. Je la doibs a sa Majesté"

The request in clear for "deux cens chevaulx et deux cens hommes de pied" is picked up in cipher as "si les forces n'y
sont placées".

**English.**

Passage 1: …[the enemy] means to come back and carry the place, [unless?] it were provided for, which is why I am
sending them back there with powder. … if you please, my Lord, [consider] that I am left alone here with the
townspeople, that the Lorraine army is fortifying itself on the Strasbourg side, and that if it turns back on me, it
would be hard for me to keep this place in the obedience it is in now.

Passage 2: If troops are not stationed here, then besides the danger the town runs, not a penny of taille will be
raised. On the other hand, one sees the inside so well built that only the outside is to be feared; the troops will
serve as much to keep them to their duty as to defend the town. The King and you will forgive me if I speak bluntly:
if it does not please His Majesty to provide for it, [I ask] to withdraw, since there is life and honour to be lost…

## Checks (all scripts in `scripts/`, run from that folder)

| check | result |
|---|---|
| `measure.py`: tokens whose key value gives the reading | 514/522 (98.5%); 0 emended; 8 open |
| `blind_score.py`: independent blind transcription of ll. 5, 11, 13, 15 decoded with the key | 219/225 (97.3%) of the reading reproduced |
| `verify.py`: French-lexicon score, real key | −2.00 log-p per letter; 74% of letters in dictionary words |
| `verify.py`: same, with only the f. 128 key (fixed before f. 130 was transcribed) | −2.19; 68% |
| `verify.py`: same, 30 shuffled keys | best −4.54, best 33% |
| `bourdeau_test.py` | unique key, as above |

**Blind test.** A separate agent got only the line crops and a legend of glyph shapes, with no values and no reading
(`blind/LEGEND.md`). Its transcription (`blind/blind_transcription.txt`) matches ours on 95.6% of tokens, with no
insertions or deletions, and decodes to the same French. Five of its six disagreements are one glyph, Ꝛ (r over a
cross, *n*), which the legend described poorly; the transcriber filed it under crossed ψ. It is the same glyph as the
*n* of *Besançon* and *despaigne* on f. 128.

**Context checks.**
- Every cipher run continues the grammar of the clear text around it ("et | l'emporter", "Strasbourg | et
  retournant", "l'honneur | pour luy").
- The Strasbourg Bishops' War began in 1592, with the Lorraine cardinal's troops in Lower Alsace that summer.

## Open (8 tokens)

- l. 4: the four signs after *l'emporter*. They decode to "? i u s" before *il*, so perhaps *ou s'il* / *puis*; the
  first sign is unclear.
- l. 7: one sign in *qu'[u]elle y est*.
- l. 14: the last sign of *pass[e]* (key value *r*) and the sign after *que*.
- Images are not included (BnF/DECODE). Gallica `btv1b52524472n`, views 265 (f. 128r) and 269 (f. 130r).

## Files

| file | contents |
|---|---|
| `f128_signs.txt`, `f130_signs.txt` | sign-token transcriptions |
| `key.tsv`, `key_f128.tsv` | the key, and the subset fixed on f. 128 |
| `reading_f130.tsv` | one plaintext character per token |
| `clear_f130.txt` | clear text of f. 130, a full diplomatic transcription by a separate agent; the postscript (ll. 35–45) is fragmentary |
| `blind/` | legend and blind transcription |
| `scripts/` | decode, measure, controls, the re-run of the original test |
| `data/fr_words.tsv` | French word frequencies for the lexicon control |
