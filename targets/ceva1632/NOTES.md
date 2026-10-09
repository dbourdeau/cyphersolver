# Cardinal Barberini to Nuncio Ceva, Paris, 1632–34

ASV, i. 1025, Segretario di Stato, Francia, doss. 346.
DECODE R74–R84 (eleven ciphertexts); the catalogue entry named five of them:
R75, R77, R78, R82, R84.

Status: read (second pass 5 Oct 2026: 95.8% of cipher tokens measured, R75 96.2%, R84 95.3%; was 91.4%).

## What the catalogue expected, and what was actually there

The entry read this as a transcription job: DECODE says "Deciphered in original",
so the text was taken to have been read at the time and the work to be copying a
decipherment off the leaf.

That is only half right, and the other half changes the job:

* **George Lasry reconstructed the key of this dossier on 24 Oct 2020** and it is
  attached to every one of the eleven records (`DOC_R*_D32*.txt`, `#KEY:
  reconstructed`). So the system was already solved before this session.
* He also published aligned decipherments of **four** letters — 346:1 (R74),
  346/4 (R77), 346/5 (R78) and 346/9 (R82) — in a combined file replicated across
  the records (`DOC_R*_D322*.txt`, 29 050 bytes, identical everywhere).
* **Three of the five catalogue targets (R77, R78, R82) are therefore already
  read.** Two are not: **R75 (346-2, 25 Sept 1632, 3 128 digits)** and **R84
  (346-11, 18 Dec 1632, 2 110 digits)**. Those two carry only a raw ciphertext
  transcription and no decipherment.
* Lasry left **all 95 nomenclator elements unsolved**; every one is printed
  `<xxx>` in his readings.

So the work here is: read R75 and R84, and resolve what can be resolved of the
nomenclator.

## The system

Reconstructed by Lasry; re-derived and checked here against his four aligned
readings (`extract_gold.py` → `gold.json`, 104 line pairs, 179 distinct tokens).

| | |
|---|---|
| `6` | word separator |
| `2x` | null — no pair beginning 2 carries plaintext |
| `XY` | homophone or syllable, 61 codes (`cipher.py`) |
| `pXY` | nomenclator element: one prefix digit + a 2-digit code |

Three points that matter for decoding and that the DECODE key note gets only
partly right:

1. **`6` never occurs inside any code** — not in a key pair, not in any of the 95
   nomenclator elements. Word boundaries are therefore certain; only the
   two-versus-three-digit choice is not.
2. The note says nomenclator elements "have 4 digits starting with prefix 4".
   They are in fact **three** digits: the concatenated token stream of 346:1 is
   99.7% identical to the original transcription, with no dropped prefix. The
   prefix is 4 in 27 of the 95 elements but is also 0, 1, 3, 5, 7, 8 or 9.
3. The digit after the prefix is itself a valid key code in 91 of 95 elements, so
   the element is a prefix plus an ordinary code — which is why the parse is
   ambiguous and needed a language model.

29 of the 100 pairs are dead (`02 05 06 12 16 32 33 36 42 46 52 56 60–69 72 76 82
86 92 96 99`); meeting one forces a three-digit reading.

## Method

`decode.py` — a position-indexed beam search over the digit stream. Every `6` is
consumed as a separator; elsewhere the beam chooses between a 2-digit code, a
2-digit null and a 3-digit nomenclator element, scored by a character model.
Scoring is incremental: `lang`'s DenseLM is a flat table of log P(c | previous
order−1 chars), so each emitted character costs one lookup.

`indomain.py` — `it-cinquecento` stops around 1620 and knows nothing of this
clerk's spelling (v for u, doubled letters dropped). It is interpolated (w = 0.6)
with a model built on 7 693 characters from the dossier itself: the passages the
clerk wrote in clear, plus Lasry's plaintext of the letters not being tested.

## Calibration

`eval.py`, leave-one-document-out — the nomenclator inventory offered for a
document is built from the other three only, which is the situation of R75 and
R84. Token-level agreement with Lasry's own segmentation:

| model | tokens | nomenclator recall | precision |
|---|---|---|---|
| `it-cinquecento` alone | 0.945 | 0.52 | 0.70 |
| interpolated, w = 0.6 | **0.958** | **0.70** | **0.79** |

Per letter at w = 0.6: 346:1 0.871, 346/4 0.928, 346/5 0.905, 346/9 0.951.

The figure to keep in view is the nomenclator recall. About three in ten elements
are still missed, and a missed element is not rendered as a gap — it is rendered
as two or three plausible Italian letters. Wrong readings in the text below will
be concentrated at those points.

## Control: the 1632 decipherment on the leaf

R75 carries a contemporary interlinear decipherment, and the DECODE transcriber
copied what was legible of it above each cipher line. It was used for nothing —
not the key, not the model, not the decoder — so it is an independent witness.

`control.py`, on the 24 lines where enough of the interlinear was legible:
**1 105 letters, 77.5% agreement**, ignoring word division. The last line agrees
at 100%. The residue is shared between this reading and the witness's own
illegibility: the transcriber flagged much of it `?` and `*`.

## Nomenclator elements resolved here

Aligning the reading of R75 against the interlinear shows which word of the 1632
decipherment stands where the decoder placed an element (`resolve.py`). Twenty-two
elements caught a witness fragment; six survive checking against Lasry's four
letters, where they were not fitted:

| code | reading | evidence |
|---|---|---|
| `474` | **mente** | `piena~`, `principal~`, `non sola~ per il solo proprio`, `malacomoda~`; witness fragment `met` |
| `495` | **quanto** | `e ~ al proporre arbitrare`; pairs with 498 |
| `498` | **tanto** | `che ~ in <347> quanto in <857> si sappia la cagione` |
| `830` | **Francia** | 4/4 in Lasry's letters after a feminine article: `render la ~ piu poderosa`, `valere a danno quella ~`, `hoggi la ~ in a di dar legge` |
| `854` | **guerra** | R75 interlinear, twice (`gurra`, `urrap`) |
| `149` | **piazza** | R75 interlinear, `acquisto d'una ~` |

Adding the six raised the control agreement from 0.737 to 0.775. That test is
partly circular for `854` and `149`, which came from the witness itself; the
independent evidence for `474`, `495`, `498` and `830` is their fit in the four
letters Lasry read.

`491` drew the witness fragment `goto` — "pensieri di goto natione", i.e. Sweden —
but it does not fit its four contexts in Lasry's letters, where it stands before
`unione` and after `conferito con`. Left open.

## The two letters

Rendering conventions: the cipher writes one sign for u and v (printed `v`), the
clerk drops doubled letters, and word division is his, not modern. Gaps are
unresolved nomenclator elements or transcription noise.

### R75 — 346-2, "Di Roma li 25 di Settembre 1632", 2 pp., 3 128 digits

Barberini on the consequences of the Swedish victories for the French alliance.
The argument: the victories make *l'accomodamento* easier but *l'unione* far
harder; the nuncio is to make the French court see the danger to itself.

> …le vittorie di […] e quella forza renderanno per avventura più facile […]
> quell'accomodamento, di […] ma più difficile assai […] quell'unione …
> per […] interessi **di Francia** …
> è tempo che se cominci a conoscere **quanto** sia pericolosa **alla Francia** la
> potenza d[i …] che cominciano [hor]mai a pensar a cose [grandi] et ad indrizar
> la [mira] loro a […]; consideri **quanto** sia oportuno alli vastissimi
> pens[ieri] di […] natione estendere il loro dominio sino al Mediterraneo con
> acquisto d'una **piazza**, e con **quanto** buon fonda**mente** lo possono
> sperare in una [rivoluzione] … **di Francia** … hanno **tanto** forze marittime
> e terrestri; consideri … che la vittoria […] è altret**anto** formidabile **alla
> Francia quanto** alla […] …
> [non si] sarà sempre al medesimo, darà sempre orecchie a[l] torbidi, et haverà
> chi li suggerisca; et un successor[e] … restringer in maniera che sempre non
> habbi libertà di [salvarsi] in campagna … [bisogna] cercar di compor[re gli]
> esterni, che cagioneranno e fo[men]teranno li domestici …
> [è] gia … arrivata a tal … di gloria … che può con ragion temere che la […]
> fortuna non si rivolti; cerchi dunque d'augumentarla con l'arti … pur vuol
> seguitar … indrizi le cose per intraprender **guerra** contro …
> quel[li] che sola parte manca alla gloria di […]. In somma … le congiunture
> presenti sono più contrarie alla s[ua] … quell'unione, **tanto** più deve …
> pensar a ritrovar ragioni che la persuadano.

### R84 — 346-11, "Roma li 18 di Xbre 1632", 2 pp., 2 110 digits

Written a month after Lützen (16 Nov 1632), and the whole page turns on "quella
vittoria". The first folio is largely in clear — Barberini acknowledging Ceva's
despatch of the 8th and referring him to Mons. Bichi at court — and the cipher
carries the analysis.

> ricordando a […] che si […] quella vittoria contro […] con la sua consueta
> **prudenza**, ad indur[re] … a facilitar il […] …
> […] che bollivano **in Francia** dopo la mia partenza; pure de[…] li torbidi di
> […] furono cagione che li […] concludessero la […] …
> le gelosie [che] quella potenza **di Francia** cerca di […]; e li spiriti
> inquieti […] fanno pastura su li impegni che il […] tiene con […] potenti, e si
> muovono più facil**mente** con speranza di fo[men]**mente** e diversione.
> Per stabilire et assicurar le cose […] bisogna levarsi le inimicitie esterne …
> nascerà l'alt[r]o in mano **di Francia**. Posso dire che stia […] se vo[gliono]
> ridur a termini ragionevoli le pretensioni …
> non […] entrar in […] cose, non lascierà di andar [f]acilitando le v[…] maniera
> che a lei s[i] accenna …
> la fuga di […] non so **quanto** sia a proposito con ins[o]liti rigori … **[in]
> Francia** metter in disperatione … potendo da[…] conseguenze che tengano
> disunita per un lungo pezzo **la Francia**, e sotto giogo alle esterne violenze,
> o almeno impotente a soccorrer li suoi alleati.

That last clause is the point of the despatch, and it is new: the Roman reading
of Lützen is that the danger is now a France held disunited and unable to help
her allies.

## Second pass, 5 Oct 2026: from 91.4% to 95.8%

Measured with `measure.py` (tokens excluding separator `6` and `2x` nulls; unread =
three-digit elements with no value in `cipher.NOMEN`, plus `?` noise digits that fit no
code). Before: R75 0.914, R84 0.915, overall 0.914 (2 095 tokens, 180 unread). After:
**R75 0.962, R84 0.953, overall 0.958** (2 085 tokens, 87 unread: 56 open elements, 31
noise digits). The decoder's letters at a missed element still count as read here, as
before; the independent check is the interlinear: letter agreement on the 24 controlled
lines of R75 rose from **0.775 to 0.828**.

What moved it, in order:

1. **Images.** R75 I589/I590 and R84 I639/I640 fetched at full resolution (2809 x 3706,
   `img/`, git-ignored). Both letters re-transcribed digit by digit against the DECODE
   transcription (`r75.retrans.txt`, `r84.retrans.txt`, diffs in `*.retrans_diff.txt`).
   DECODE's copy proved good: R75 3 lines / 5 digits changed, R84 7 lines / 7 digits. Gain
   small (R84 +0.005), but four blotted or dropped digits in R84 l.5, 8, 10, 17 now read
   ("pensieri torbidi", "di dividerla", "se vorà ridur").
2. **One stream per letter** (`run2.py`). `run.py` decoded line by line, but codes run
   across line ends (R75 l.28/29 `5|1` = f of "fortuna"; l.25/26 "biso|gna"), so each
   wrap made `?` noise and spurious elements. 0.914 -> 0.931 with no new value.
3. **Seventeen element values** (`cipher.py`, second `NOMEN.update`). The interlinear of
   R75 was re-read at full resolution (`r75.interlinear.txt`), and every occurrence of each
   code was pooled across Lasry's four letters and R75/R84 (`ctx.py <code>`):

| code | value | evidence |
|---|---|---|
| `315` | **S.E.** (Richelieu) | interlinear 'S.E.' (l.12 'è tempo che S.E. cominci a conoscere'); 'già S.E. è arrivata a tal grado di gloria', 'manca alla gloria di S.E.', 'consideri ancora S.E. che la vittoria del Sueco…' |
| `411` | **V.S.** | 'ricordando a ~', 'pure risposto ~ adequatamente', 'di ~ de ventitre', 'non so dir a ~ d'avantaggio', 'più deve ~ pensar' |
| `938` | **Monsieur** (Gaston) | margin gloss 'Monsieur S.A.' at R75 l.21/22; 'la fuga di ~', 'accomodamento di ~ col fratello', 'torbidi di ~' |
| `988` | **negotio** | 'il principal ~ commesso a V.S.', 'il ~ dell'accomodamento', 'quel ~ et indrizzato' |
| `338` | **stato** | 'la Francia in ~ di dar legge', 'non so quanto sia ~ a proposito', 'lo ~ del negotio' |
| `441` | **bene** | interlinear 'bin' ('se ~ si agiustano'); 'al publico ~ et alla quiete', 'stimarà ~ e gradirà' |
| `481` | **però** | interlinear 'piro' (l.25); 'non si poteva ~ negare', 'non lascierà ~ di andar' |
| `493` | **questa/o** | interlinear 'questa sola parte' (l.32); 'entrar in ~ cose', 'da ~ debolezza' |
| `439` | **ancora** | interlinear (l.19, l.21 'ancora che') |
| `470` | **hor** | interlinear 'hor mai' (l.14) |
| `488` | **quale/i** | interlinear 'alla quale' (l.18); 'le cose sue, le quali in tempo di guerra' |
| `857` | **Germania** | interlinear 'Germa' (l.21): 'alla Francia quanto alla ~' |
| `334` | **Sueco** | interlinear 'del Sueco' (l.20) |
| `104` | **Svedesi** | interlinear l.13, ending '…desi', first letters blotted (the image agent read 'Spagn.li'); Swedish context: 'Goto natione… sino al Mediterraneo' |
| `129` | **Regno** | interlinear 'del Regno' (l.23) |
| `454` | **grandi** | interlinear 'cose grandi' (l.14) |
| `127` | **Imperiali** | interlinear 'a gli Imperiali' (l.15) |

   0.931 -> 0.954. Then the decoder penalty for a code known from Lasry's letters but still
   without a value was raised (`--unvalued=-5`): an unvalued element emitted a cheap space
   and beat real letters, e.g. R75 l.7 `13 24 38 95 71 49 70 38 59` 'per assicurar' had
   been read 'pera<957>mi<970>ar'. 0.954 -> 0.958 with the re-transcriptions.

Content gained: the "S.E." of R75 is Richelieu. The letter tells Ceva to make the
Cardinal see that the Swedish victory is "altrettanto formidabile alla Francia quanto
alla Germania", that S.E. has reached such glory that he must fear fortune turning, and
that the one glory he lacks is a war against the infidel. Monsieur "sarà sempre al
medesimo, darà sempre orecchie a' torbidi".

Failures and limits of this pass:

* `491` (5 tokens): the interlinear plainly writes 'Goto' over it at l.16, but 'Goto'
  fails 'animi a ~ unione', 'in ~ piazza', 'considerate ~ quel fratello' in Lasry's letters;
  left open. `497` (3, often before 491), `998` (3, always before a stray `3` in R84),
  `328` (3: 'per ~ interessi', 'a ~ hanno', 'compor ~ esterni') tried, no single value fits.
* 31 noise digits remain, mostly at ink blots (R75 l.30, 31) and in R75 ll.15, 22, 23 where
  the parse is still unsure; the image check did not change those digits.
* The fraction counts letters emitted at an element the decoder missed as read, as the
  first pass did; the 0.828 interlinear agreement is the honest bound on sense for R75.

## What is open

* **The nomenclator.** After the second pass 23 elements carry a value; 56 element
  tokens of R75/R84 are still open (see Remaining gaps). A key for this dossier, if one
  survives in the ASV, would close them at a stroke.
* **Transcriptions** were re-checked against the images on 5 Oct 2026 (see Second pass);
  the residual noise sits at ink blots.
* **R74, R76, R79, R80, R81, R83** — the other six of the eleven — were read by
  Lasry and are not touched here.

## Files

| | |
|---|---|
| `decode/` | the DECODE transcriptions, key and combined decipherment |
| `cipher.py` | key, nulls, separator, the six elements read here |
| `extract_gold.py` → `gold.json` | Lasry's aligned readings, parsed |
| `streams.py` → `r75.digits`, `r84.digits` | ciphertext digit streams |
| `decode.py` | the beam-search decoder |
| `indomain.py` | the interpolated character model |
| `eval.py` | leave-one-out calibration |
| `control.py` | check against the 1632 interlinear |
| `resolve.py` | nomenclator proposals from the interlinear |
| `run.py` → `r75.read.txt`, `r84.read.txt` | the first-pass readings (line by line) |
| `img/` | full-resolution DECODE images (git-ignored) |
| `r75.retrans.txt`, `r84.retrans.txt` (+ `_diff`) | re-transcription from the images, 5 Oct 2026 |
| `r75.interlinear.txt` | the 1632 interlinear re-read at full resolution |
| `ctx.py <code>` | every context of an element across the six letters |
| `run2.py --unvalued=-5` → `r75/r84.read2.txt`, `.tokens2.json` | the second-pass readings, one stream per letter |
| `measure.py` | fraction_read |

## Remaining gaps

- 56 nomenclator tokens of R75/R84 (491 x5, 497/998/328 x3, 494/128/450/110 x2, ~40 singletons) - blocker: open-codes; pooled across all six letters, no single value fits; interlinear only on R75 and illegible at most of them
- 31 noise digits at ink blots (R75 l.30, 31) and unsure parses - blocker: illegible; checked against the full-resolution images 5 Oct 2026
- dossier key with nomenclator - blocker: needs-physical-access; none on DECODE; would need the ASV

## Escalation

- [x] siblings: all eleven records R74-R84 opened; Lasry key and four readings on them; every code pooled across the four letters + R75/R84 (ctx.py)
- [x] clear-pages: R75 interlinear 1632 decipherment re-read at full resolution (r75.interlinear.txt); margin gloss 'Monsieur S.A.'; 17 elements fixed from it and from pooled contexts
- [ ] known-keys: not done - other Barberini-period ASV nunciature keys on DECODE (e.g. Pallotto 1629 R215) not tried for the nomenclator
- [ ] print: not done - Nuntiaturberichte / Acta Nuntiaturae Gallicae for Ceva 1632-34 not searched
- [x] key-rebuild: LM beam decoder, interpolated in-domain model; whole-letter streams (run2.py); unvalued-code penalty
- [x] retry: both letters re-transcribed from the images (r75/r84.retrans.txt) and decoded again with the 23 values: 0.914 -> 0.958
