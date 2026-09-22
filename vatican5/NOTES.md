# Vatican Challenge Part 5 (MysteryTwister) — solved by Simon Klee

> **Status update, 20 September 2026.** Simon Klee recovered the key and a candidate plaintext, published
> [“The Farnese letter”](https://simonklee.dk/farnese-letter), and received MysteryTwister's acceptance. The result
> has been reviewed here and is accepted as a solution: independent half-text recoveries, synthetic and shuffled
> controls, checks against the manuscript, and historical corroboration support it. Some damaged passages remain
> editorially uncertain. See [`SOLUTION.md`](SOLUTION.md) and [`key.md`](key.md).
>
> The investigation below is retained as an audit trail, but its final diagnosis is **superseded**. In particular,
> `4` is `o` rather than a null; `9` is the null; and the core is a mixed one-/two-digit monoalphabetic key, not the
> proposed Antonio Elio polyphonic-syllabic design.

Ciphertext: ASV Segr. Stato Spagna 1A/2 (Farnese → nuncio Poggio, Rome 15 Apr 1542), transcript
`ASV_i1025_SdS_Spain_IA-2.txt` from the MysteryTwister challenge (G. Lasry, 2019). 6553 digit tokens,
dots on some digits (`^.`), a few uncertain readings (`?`).

## Established facts (statistical)

| finding | evidence |
|---|---|
| digit **4 is a null / word separator** | bias-corrected I(x;y \| middle=4) = 0.030, identical to Italian across-word-boundary MI (0.028); every other digit 0.08–0.17 (letter-like). Only 482 of ~1100 word ends are marked. |
| 7 is *not* a null | I(x;y \| 7) = 0.153 |
| 8 and 5 never end words (5 and 16 of 482) | → consonant groups; 7, 0, 3 dominate word-final position (161/103/79) → vowel-carrying |
| top bigrams 80/57/27/03/73 are 3–5 % of all bigrams | far too frequent for 2-digit syllable codes → mostly single-digit polyphonic letters |
| dotted digits are mainly 7^ (107), 2^ (39), 0^ (33); the digit after a dot is 2/0/7/5 (~36 each) | matches Meister key no.1 mechanics (dot on the *preceding* digit selects a syllable series; 4 syllables) |
| Meister 1906 keys nos. 1–4 (pp. 176–177) as printed do not fit | tested |
| Lasry–Megyesi–Kopal 2021 §5.5: S1/IA-2 unsolved, "another key" than IA-1 | their 2-letters-per-digit polyphonic SA failed |

## Tools

* `parse5.py` — tokenizer; `mi3.py` — bias-corrected MI diagnostics; `sepwords.py d` — segments between digit *d*;
  `fitfreq.py` — fit letter groups to overall / word-initial / word-final marginals; `dots2.py` — dotted contexts.
* `build_it_lm.py` — period-Italian corpus from Nuntiaturberichte OCR (`nb_*.txt`, not in repo) → `it_ngrams.json`,
  `it_words.json`; `export_native.py` / `export_native_sp.py` → `lm5.bin` / `lm5sp.bin` (dense 5-gram tables).
* `native/Program5.cs` → `vsolve.exe` (C# 5, build with `csc.exe /o+ /platform:x64`): lattice/beam-Viterbi solver
  with simulated annealing + greedy sweeps over a key of polyphonic single digits, dotted singles, after-dot singles,
  2-digit and dotted 3-digit codes. Objective = 5-gram LM + KL(letter freq) + MDL code penalty + dictionary word
  coverage (`--wcoef`). See `--help`-less option list at top of `Main`.
* `make_syn.py`, `make_syn1.py` — synthetic ciphers (Meister key-2 / key-1 style) with known keys for testing;
  `syn_fix.py`, `syn1_fix.py` — `--fix` spec of the true key; `lmscore.py`, `wordscore.py`, `wordcov.py` — evaluate a decode.

## Lessons

* Fixed-length chunking split dotted 3-digit codes → true keys scored −8000 nats worse than garbage. Chunk
  boundaries now avoid dotted positions and a penalised skip transition exists.
* On a key-1-style synthetic the pure LM objective is **not identifiable** (a wrong key scores as well as the truth);
  dictionary coverage (words ≥5 letters, top-5000) separates them cleanly (0.52 vs 0.21).

## 2026-09-15 session (resumed)

* Dot mechanics re-derived from Meister p.176-177: key no.2 ("Cifra ultima con Mons. Poggio mandata per il
  Montepulciano") puts the dotted codes on 8x/0x (ta te ti to, qua que qui, che chi non, N.S., S.Mta), but in IA-2
  the digit after a dotted digit is 2/0/7/5 (~36 each) and the dotted digits are 7/2/0 → key-1 *type* (dot on the
  antecedent selects a 4-syllable series; dot on the digit itself another series), with {7,2,0,5} as the four
  "vowel" digits. Key 2 as printed rejected (trigram LL −49047).
* Key no.3 (Piacenza/Dandino 1545) has **Nulla 4** — same null as IA-2 — and vowel digits 2 5 7 9 0. Tested:
  trigram LL −44038 (search optima −39659, random best −45545) → rejected; the null coincidence is just that.
* New objective `bigramfit.py` / `trigramfit.py`: exact multinomial likelihood of the digit bi/trigram counts under a
  grouped Italian letter model (4 = boundary, dotted contexts excluded), SA over partitions of 21 letters into 9
  digits. Result: 24 runs → 24 different partitions with scores within 500 nats of each other (−39659 … −40157),
  Rand index vs best ≈ 0.85 (chance level). **The polyphonic single-digit model is not identifiable on this text**
  — consistent with the earlier 5-gram lattice failure and with Lasry–Megyesi–Kopal's failure.
* `decode_poly.py` — trigram Viterbi decode for any "d=letters" key; `consensus.py` — compare partitions.
* Hypotheses left: (a) plaintext not Italian (transcript tags some cleartext "SP" = Spanish) — being tested with a
  Don Quijote trigram model (`trigramfit_es.py`); (b) most digits belong to 2-digit syllable codes (key-2 style)
  so the letter model is wrong; (c) transcription noise.
* **Decisive diagnostics (2026-09-15):** synthetic control (`syn_tri.py`: 7000 Italian letters, random key-1-style
  polyphonic key, 45 % word ends marked with 4) → the trigram partition SA recovers the true key (2/3 runs exact up to
  b/z; score −40932 vs truth −40994). On the real cipher: 24 Italian runs and 12 Spanish runs (`trigramfit_es.py`,
  Don Quijote model) all fail to converge (Rand ≈ 0.87 = chance). **So IA-2 is not a plain polyphonic
  single-digit cipher in Italian or Spanish**; the digit stream must contain substantial multi-digit code content
  (key-2-style syllabary with other numbering), which no letter-level model can identify. Next attack would be a
  mixed model with explicit 2-digit syllable codes seeded by the key-2 layout (cX/dX/lX/mX/nX/rX/sX series) and
  dotted 4-series on {2,0,7,5}; the old C# lattice solver had this class but no structural prior.

## 2026-09-15, third attempt: the two-digit-syllable prior also fails

New structural lead from re-reading Meister key no. 1: there the dot sits on the *antecedent* and selects a
four-member syllable series, so the digits that *follow* a dot are the series slots (a, e, i, o). In IA-2
those following digits are {2, 0, 7, 5}, which would make them the vowel slots and predict that much of the
text is two-digit syllables of the form (consonant lead)(vowel from {2,0,7,5}).

Tested directly, segmenting on the null 4:

| prediction | observed |
|---|---|
| {2,0,7,5} concentrated at alternate positions | even positions 0.587, odd positions 0.582 — no difference |
| word segments mostly even length | 280 even against 201 odd — no preference |

So the syllables are not laid out as fixed two-digit units in a regular phase. Together with the earlier
results (Meister keys 1-3 rejected by likelihood; trigram partition search recovers synthetic keys of the
polyphonic design but fails on the real text in both Italian and Spanish) the picture is of a
**variable-length code** mixing one- and two-digit groups, very likely with heavy nomenclature — which is
exactly the case no letter-level model can identify, and is consistent with Lasry, Megyesi and Kopal having
left it unsolved.

Remaining idea, untested: the fraction of the text that is nomenclature (arbitrary groups for words and
names) may simply be too large for any statistical attack, in which case the cipher needs the key itself
rather than cryptanalysis.

## 2026-09-15, fourth attempt: the model class is now excluded by a matched control

### A real structural finding first

Italian words end in a vowel about 97% of the time, so word-final enrichment (final rate divided by
overall rate) should separate vowel-bearing digits from consonant ones. Measured over the 481 segments
delimited by the null 4:

```
  1: 1.79   7: 1.76   3: 1.52   0: 1.49  |  6: 1.01  |  9: 0.64   2: 0.58   5: 0.25   8: 0.08
```

Digit 8 ends a word at one twelfth of its overall rate; digits 1, 7, 3, 0 are all enriched. And the
frequency masses of that split match Italian independently, to three decimals:

| group | cipher mass | Italian target |
|---|---|---|
| {7, 0, 3, 1} | 0.476 | all five vowels, 0.479 |
| {8, 5, 2, 6, 9} | 0.524 | all consonants, 0.521 |

Two independent signals agreeing. **The vowel-bearing digits are {7, 0, 3, 1}.** This is the first
positive structural result on the cipher beyond the null.

### The constrained search, and why it still fails

`vc.py` repeats the trigram partition search with vowels restricted to {7,0,3,1} and consonants to
{8,5,2,6,9}, cutting the space from 9^21 to 4^5 x 5^16 and removing vowel/consonant confusions. 24 runs:
still 24 different keys, mean Rand index against the best **0.861** where chance *in the same constrained
space* is **0.799**. The runs do not even agree on which vowel sits on which digit.

### The matched control settles it

`vc_syn.py` builds a synthetic ciphertext with exactly the structure the real one is believed to have --
real Italian plaintext, same 21-letter alphabet, same vowel/consonant digit split, same polyphony (16
consonants over 5 digits), same null density, same length of 6553 digits -- and runs the identical search.

```
TRUE KEY   7=i 0=o 3=u 1=ae 8=cdgv  5=fhr 2=lst 6=bpq 9=mnz
BEST RUN   7=i 0=o 3=u 1=ae 8=cdgvz 5=fhr 2=lst 6=bpq 9=mn
```

Recovery of the true key: **0.97** (one letter misplaced), and the search even beat the true key's own
likelihood, so it found the optimum. Agreement between independent runs: 0.90. Replicated on a second
seed: recovery 0.93, agreement 0.89.

| | agreement between runs | recovers a key? |
|---|---|---|
| synthetic, same design | 0.90 | **yes, 0.97** |
| real ciphertext | 0.86 (chance 0.80) | no |

**So the method works at this polyphony, this length and this alphabet. The real ciphertext is therefore
not a polyphonic single-digit substitution of Italian.** This is no longer "we could not find the key"; it
is "no key of this kind exists to find".

### Where that leaves it

The word-final evidence says parts of the text behave like Italian letters with a vowel/consonant
structure. The failure of every letter-level model says parts of it do not. The reading that fits both is a
**mixed cipher**: polyphonic single digits for letters, interleaved with multi-digit groups for syllables,
words and names, and no marking to say which is which. Only about 6% of positions carry dots, far too few
to be the code markers, and the searches already exclude dotted contexts.

That is precisely the construction no statistical attack can resolve, and it explains why Lasry, Megyesi
and Kopal left this one unsolved while reading the rest of the collection. The route in is the key or a
matching plaintext in the Farnese correspondence, not cryptanalysis.

Reproduce: `python vc.py <seed>` (constrained search), `python vc_read.py consensus` (convergence),
`python vc_syn.py <seed>` (the matched control).

### The mixed lattice model, with the constraint, also fails

The C# lattice solver (`native/vsolve.exe`) already supports `--null`, `--vowdig` and `--consdig`, so the new
structural finding could be fed straight in: `--null=4 --vowdig=7031 --consdig=85269 --wcoef=3`. No previous
run had the right values. Four seeds, 120k iterations each.

The decodes *look* far better than anything before — real 16th-century vocabulary, `cosa`, `con la`, `et`,
`regno`, `imperatrice`, `figlia`, `signore`, `chiesa` — instead of the `che/non/per` loops the earlier runs
collapsed into. That appearance is worthless, and here is why.

**Dictionary coverage cannot judge itself.** The solver optimises coverage directly (`--wcoef`), so it will
manufacture Italian-looking words from any key. Calibrated at minlen 5 / top 5000:

| text | coverage |
|---|---|
| genuine Italian prose | **0.248** |
| constrained runs (vcn_1..4) | 0.204 – 0.232 |
| an earlier unconstrained run (nat_c4) | **0.279** |

An earlier run scored *higher than real Italian*. The metric is gameable and every "promising" coverage
number in this project's history should be read in that light.

**Convergence is the test the solver does not optimise, and it fails it.** Across the four constrained runs:

* only 1 to 3 of the 10 digits carry identical letter sets in any pair;
* pairwise Rand index over letter groupings 0.84 – 0.87, against the 0.80 chance level for this space;
* the runs disagree about which vowel sits on which digit (7 = i, i, a, i; 0 = a/u, e, i, a).

So the mixed model with polyphonic singles plus two- and three-digit codes is no more identifiable than the
pure letter model. The vowel-bearing *set* {7,0,3,1} is solid; the individual assignments are not
recoverable from 6553 digits at this ambiguity.

### Status

Unsolved, and now for a documented reason rather than for want of trying. Four model classes tested, two of
them against matched synthetic controls that the same code solves correctly. The cipher needs its key, or a
matching plaintext in the Farnese correspondence.

## 2026-09-15, fifth attempt: the level is settled, and so is why this one resisted

Resumed with a directive to solve it. It is still not solved. But the session produced the first
positive structural results since the vowel set, a third independent confirmation of that set, and -
more usefully - an explanation of why the sibling cipher fell and this one did not.

### The finding that matters most is not cryptanalytic

Part 4 of the same challenge series is ASV Portugal IA-1, and it was solved. Compare the two
transcripts as delivered:

| transcript | single spaces between digits | **double spaces** |
|---|---|---|
| Portugal IA-1 (Part 4, solved) | 7603 | **3210** |
| Spain IA-2 (Part 5, this one) | 6412 | **6** |

The Portugal transcriber recorded the scribe's word division; the Spain transcriber did not. The
division exists on the parchment - sixteenth-century chancery clerks grouped their cipher digits -
but it is absent from the only transcript in circulation. Every attack mounted here and, presumably,
by everyone else has been run on a stream with its word boundaries deleted. That is a large part of
the difficulty asymmetry between Part 4 and Part 5, and it is fixable only from the images.

### One key, not several

A page-by-page comparison of digit distributions against the document mean gives chi-squared between
3.4 and 12.6 on 9 degrees of freedom across the six substantial pages. Nothing approaches
significance, so the whole of ff. 70r-73v is in a single key. The "mixed keys" explanation for the
failure is excluded.

### Three structural results, each against a control

**Segment lengths prefer even.** The stretches between the null 4 run 278 even against 202 odd,
chi-squared 12.0 on 1 df. The fourth attempt looked at this and recorded "no preference"; that was
wrong, and it matters, because it is the signature of two-digit units.

**There is a real two-digit phase.** Inside those stretches the digit distribution at even offsets
differs from the one at odd offsets: chi-squared 39.4, against a null of 8.3 +- 4.1 built by
shuffling each segment, z = +7.6. Digit 9 sits at even offsets 1.60 times as often as odd, digit 8 at
0.84.

**Doubled digits are suppressed without exception.** All ten, and some severely - 00 occurs 6 times
against 117 expected, 44 twice against 35, 99 twice against 21. Six ordered pairs are suppressed
below an eighth of expectation; 400 shuffles of the same digits produce a mean of 0.01 such pairs and
never more than 1.

### The word-final units, and a third confirmation of the vowel set

Scanning every n-gram for enrichment immediately before a null gives two dominant word endings:

| unit | occurrences | before a null | p |
|---|---|---|---|
| **27** | 265 | 86 | 7.4 x 10^-33 |
| **80** | 349 | 82 | 4.2 x 10^-21 |
| 73 | 222 | 38 | 9.8 x 10^-7 |
| 37 | 73 | 17 | 1.7 x 10^-5 |

Every enriched ending terminates in a digit from {7, 0, 3, 1}. Italian ends about 97% of its words in
a vowel, so this is a third independent line - after word-final enrichment of single digits and after
the frequency masses - agreeing that those digits are the vowel-bearing ones. **{7, 0, 3} is now solid
on all three.**

### But the level is not letters, and that is now demonstrable

If each digit stood for one letter, the alternation of vowel-digits and consonant-digits would have to
look like the alternation of vowels and consonants in Italian. It does not:

| | cipher | period Italian |
|---|---|---|
| vowel share | 0.475 | 0.464 |
| mean vowel run | 1.604 | 1.301 |
| mean consonant run | 1.769 | 1.504 |
| consonant runs of 3 or more | **0.183** | **0.059** |

The share matches and the runs do not. Runs three times too long are what you get when letters are
sometimes written as two digits of the same class.

Worse for the letter model, the three tests disagree about which digits are the vowels. Frequency mass
picks {7,0,3,1}; a search over all subsets for the best match to Italian's run profile picks
{0,2,3,7}; the final-digit distribution picks {7,0,3,6}. All three agree on {7,0,3} and contradict
each other on the fourth. **No single letter-level assignment satisfies all three**, which is what one
expects when the units are not letters.

### The repetition says codebook

| | real | shuffle of its own digits |
|---|---|---|
| repeated 7-grams | **441** | 5 |
| repeated 8-grams | **244** | 0 |

And greedy byte-pair encoding, which lets the text name its own units, separates the real text from
both controls - compression gain +1.6% for the cipher, **-8.2% for genuine Italian pushed through a
polyphonic single-digit cipher of the believed design**, -14.0% for a shuffle. The units BPE recovers
are 15% one digit, 32% two, 29% three: a variable-length nomenclator, not a fixed grid.

### Arithmetic that now hangs together

6068 non-null digits over 480 segments is 12.64 digits per segment. If units average two digits that
is about 3000 units; at roughly 2.3 units per word that is about 1300 words of some 4.6 letters, which
is ordinary Italian and consistent with four folios. The null therefore marks about 37% of word ends,
not all of them - which is why the segments are far too long to be words.

### Status

Not solved. The model is now pinned much more tightly than before: **a variable-length syllabic code,
mostly two-digit units over vowel-bearing digits {7,0,3}+ and consonant-bearing {8,5,2,6,9}-, with 27
and 80 as the dominant word-final units and 4 as an intermittent word null.** What is missing is not
another search. It is the word division, which exists in the manuscript and was dropped in
transcription, or the key, or a matching plaintext.

New files: `phase.py` (parity and phase), `escape.py` (suppressed pairs, after Lasry's dictionary
escape in the sibling cipher), `units2.py` (unit inventory), `bpe.py` (unsupervised units with
controls), `cvtest.py` (the vowel/consonant run test).

## 2026-09-15, the cipher family is identified

A source hunt run alongside the statistics found the literature that settles what this cipher is.
It is not solved, but it is no longer unidentified, and every structural measurement above turns out
to be a match for a documented design.

### It is an Antonio Elio polyphonic-syllabic cipher

Antonio Elio (1506-1576), known in his own lifetime as *Antonio delle Zifre*, was cipher secretary to
**Paul III** - the pope whose cardinal-nephew and Secretary of State, Alessandro Farnese, wrote this
letter. Lasry, Simonetta and Biermann, "Antonio Elio 'Cipher' and his Polyphonic-Syllabic Cipher",
HistoCrypt 2025, describe the design he invented for that chancery:

* **syllabic** - most symbols encode consonant-vowel syllables, with a few for other clusters or
  short words (*gno*, *nd*, *che*)
* **polyphonic** - every syllable symbol has two meanings, and the second is selected by **a dot on
  the preceding symbol**. The dots are not applied consistently, so decipherment is often
  non-deterministic even for a secretary holding the key
* **compound symbols** - some plaintext elements are encoded by pairs, so **any symbol may be either
  stand-alone or half of a pair**
* **h and any doubled letter are dropped before encryption** - *hoggi* is reduced to *ogi*

### Every measurement above matches it

| measured here | Elio's documented design |
|---|---|
| all ten doubled digits suppressed, 00 at 6 against 117 expected | doubled letters dropped before encryption |
| dotted digits are 7/2/0 and the digit *after* a dot is 2/0/7/5 | the dot sits on the **antecedent** and selects the alternate meaning |
| word-final units are two digits, 27 and 80, p < 10^-20 | consonant-vowel syllables as units |
| BPE units 15% one digit, 32% two, 29% three; even-length preference real but only 58/42 | any symbol may be stand-alone or half of a compound |
| consonant runs three times too long for letters | the level is syllables, not letters |

The doubling rule is not merely inferred. Meister prints the Farnese chancery's own written
instruction at p.223: **"Scrivasi stretto et senza duplicare le consonanti quando occorrono dittioni
che la ricerchino"** - write tightly and without doubling the consonants where the words call for
them. The same page also says other names may be abbreviated **"con il segno della nulla in fine
della lettera o sillaba"**, with the null at the end of a letter or syllable. That reframes the null:
**4 is an abbreviation and syllable marker, not a word separator**, which is why the stretches between
nulls average 12.6 digits and never looked like words.

### The published state of the art

Lasry, Megyesi and Kopal, "Deciphering papal ciphers from the 16th to the 18th Century",
*Cryptologia* 45:6 (2021), worked this exact corpus. Two statements matter:

> "A polyphonic cipher described in Meister (1906, 176/2) was used by Mons. Poggio, the papal nuncio
> to Spain at the same period; however, attempts to decipher the ciphertexts using that key did not
> produce any result."

> "The scheme appears to be a **variable-length polyphonic cipher**, which is a unique case in the
> Vatican collections ... The ciphertexts in the second part (**IA-2**) seem to belong to another key."

So the one published key naming Poggio is on record as tested and excluded, IA-2 is flagged as a
different key again, and their description of the scheme - variable-length polyphonic - is what the
run-length, phase and BPE work here arrived at independently.

The 2025 Elio paper is blunter about the prospects:

> "Ciphertext-only cryptanalysis for such a cipher would be extremely difficult and nearly
> impossible, even with modern computing, without prior knowledge of the principles of its complex
> design."

And even **with** matching plaintext-ciphertext segments in hand, recovering the key of the 1540
Elio cipher took three expert cryptanalysts "two full days of intensive work" to make initial
inroads, and many further hours to finish.

### The plaintext is unpublished, but its neighbours are not

No edition, calendar or regesta prints Farnese to Poggio of 15 April 1542. The Spanish nunciature of
this period has no published series at all: *Monumenta Hispaniae Vaticana* stops in 1486, Olarra's
index starts in 1556, Serrano covers 1566-72. *Nuntiaturberichte aus Deutschland* I/7 prints Poggio
but jumps from December 1541 to July 1543, with Cardauns noting the 1542 correspondence survives
"nur fragmentarisch". *Concilium Tridentinum* IV prints Farnese to Poggio on 5 February and 4 June
1542 but has nothing from April; its two April 1542 Farnese letters go to the nuncio in France.
Pastor prints exactly two Farnese-Poggio letters, of February 1541 and August 1542.

What exists, uncatalogued in print:

* **Naples, Archivio di Stato, Carte Farnesiane 723** - a Farnese to Poggio letter of **12 April
  1542**, three days before this one and in the same courier cycle
* **AAV, Lettere de' Principi 14 A** - Farnese to Poggio register copies, ff. 1-129 covering to 4
  June 1542; this is where Ehses took his texts
* **BAV, Chigi L III 65** - the Farnese to Poggio originals, 348 ff. Folio calibration from the
  editions puts 23 Nov 1541 at f.153 and 29 June 1542 at ff.191-195, so **15 April 1542 should sit at
  roughly ff. 165-190**

Cardauns repeatedly notes that these registers carry contemporary interlinear decipherments. A clear
copy may simply exist.

### Status

Unsolved, and now for a fully documented reason. The cipher is identified as an Elio
polyphonic-syllabic design of the Farnese chancery; five model classes have been excluded here, two
against matched synthetic controls the same code solves correctly; the published specialists state
that ciphertext-only attack on this family is near-impossible; and the transcript in circulation has
lost the word division its solved sibling's transcript preserved. The routes in are the key from
Chigi M II 49, the word division from the manuscript images, or the clear copy from Chigi L III 65 or
Lettere de' Principi 14 A.

### The last structural question, answered: there is no grid

If the text sat on a fixed two-digit grid it could be cut into units and attacked as a substitution
over about a hundred symbols with three thousand tokens, which is tractable. `gphase.py` tests that
directly, in the three ways the null could behave:

| phasing | chi-squared, even vs odd | shuffle null | z |
|---|---|---|---|
| A - null counted, absolute index | 6.8 | 9.0 +- 4.2 | **-0.53** |
| B - null deleted, global index | 4.3 | 8.0 +- 4.0 | **-0.93** |
| C - null deleted, per cleartext run | 4.3 | 8.0 +- 4.0 | **-0.93** |
| D - phase restarts at every null (the earlier test) | 39.4 | 8.3 +- 4.1 | +7.6 |

All three global phasings sit **below** their shuffle nulls. There is no fixed two-digit grid anywhere
in the text. The only phase signal is the local one that restarts at each null, and it is modest and
driven mostly by digit 9.

So the units are genuinely variable-length, which is precisely what Elio's compound symbols predict -
"any symbol may be either a stand-alone symbol or part of a pair". Without a segmentation there is no
unit inventory; without a unit inventory there is no substitution to attack; and the polyphony doubles
every unit's meaning on top of that.

### A parsing correction

The transcript carries three distinct marks above digits, not one: **dot 175, comma 23, dash 4**, plus
13 slashes and 11 question marks that are transcriber annotations. There are **no below-marks at all**,
although the challenge describes the notation for them. Earlier passes here conflated comma-above with
dot-above. It does not change the conclusions - both concentrate on the same carriers, 7 then 0 and 2 -
but the dots are on {7, 2, 0} at 88% and carry no phase information, so they are distinct codes rather
than segmentation markers.

### Final status

Not solved, and now closed off from every direction that can be tested from the transcript. The
remaining routes all need material that is not online: the key from Chigi M II 49, the word division
from the manuscript images (DECODE record 92 holds them behind a login), or the clear register copy
from Chigi L III 65 ff. ~165-190, Lettere de' Principi 14 A, or Naples Carte Farnesiane 723.

### The image route, probed and closed

DECODE record 92 is confirmed to be this document: name `ASV_i1025_SdS_Spain_IA-2`, 8 pages, status
non-decrypted, first image `069v.jpg`. Its file server exposes images at
`/decrypt-custom/filesrv/?file=...`, and the eight thumbnails are fetchable without a login.

Everything above thumbnail size is not. `TH_IMG_R92_I69x_Px.jpg` returns a real JPEG at **200 x 256**;
every other prefix tried - bare, `MD_`, `LG_`, `FULL_`, `OR_` - returns the same 986 x 568 PNG
placeholder of identical byte length, and the size parameters `w`, `size` and `thumb` are ignored.

At 200 x 256 a folio of roughly 25 lines gives each line about 8 pixels. The digits are texture, not
glyphs; no transcription is possible and the word division cannot be verified at that resolution. What
the thumbnails do show is that **069v is ordinary cleartext prose** while 070r onward are dense cipher,
which matches the transcript's own structure.

So the images exist, are catalogued, and are one login away - but not reachable from here.

### A matched control of the Elio design, and what it says

`elio_syn.py` builds a synthetic to Elio's documented rules - h and doubled letters dropped,
consonant-vowel syllables as two-digit codes on a systematic grid, single digits for the rest,
polyphonic dot on the antecedent, intermittent null - at the real length of 6549 digits, and measures
both with the same code. Three seeds, real text scored with vowels {7,0,3}:

| | synth 1 | synth 2 | synth 3 | **real** |
|---|---|---|---|---|
| vowel share | 0.494 | 0.488 | 0.503 | 0.442 |
| mean vowel run | 1.303 | 1.495 | 1.308 | **1.510** |
| mean consonant run | 1.333 | 1.569 | 1.294 | **1.907** |
| consonant runs >= 3 | 0.039 | 0.105 | 0.020 | **0.226** |
| repeated 7-grams | 187 | 275 | 176 | **441** |

The first version of this script also produced a useful failure: with *arbitrary* digit pairs as
syllable codes, every digit becomes vowel-bearing and the consonant class vanishes entirely. Since the
real text has a clean vowel class on three independent tests, **the two-digit codes cannot be
arbitrary pairs** - they must sit on a systematic consonant-then-vowel grid, which is also what
Meister's keys of this family look like (da de do = 49 69 89; na ne ni no = 24 26 28 29). That is a
constraint on the key obtained from a control rather than from a guess.

But the control does **not** reproduce the real text. The real text has markedly longer consonant runs
and roughly twice the repetition of a pure syllabary. The repetition gap is the informative one: 441
repeated 7-grams against 176-275. A syllabary alone does not repeat that much. **Substantial
nomenclature content - fixed codes for recurring words and names - is the natural explanation**, and
it matches Lasry's description of the sibling cipher, where some digits open dictionary entries while
others carry letters and syllables.

Honest limit: the synthetic's parameters (the fraction of text taken by syllable codes, the null
placement, the number of codes) are guesses, so the mismatch is suggestive rather than decisive. What
it does establish is that the syllabic layer alone cannot account for this text, which is a further
reason no statistical attack will read it - nomenclature codes for names and words are unrecoverable
from a single letter, whatever the method.

## 2026-09-15, sixth session: sources verified from the page scans, and a unit-level attack

### What the scans and papers add

* **Meister pp. 176-178 and 222-224 read from the Internet Archive scans** (leaves 191-193 and 237-239 of
  `diegeheimschrift00meis`), not from the OCR in `meister_p176.txt`. Key no. 1 (given to Montepulciano,
  1539-42): singles Ac=8 eu=6 id=4 ot=2 bfg=7 ln=5 prz=3 ms=0, et unnumbered; da de do = 49 69 89; na ne
  ni no = 24 26 28 29; che chi non = 94 9 92; ta te ti = 96 98 99; qua que qui = 82 84 86; sa se si so =
  ·8 ·6 ·4 ·2 (dot on the antecedent); ra re ri ro = 8· 6· 4· 2· (dot on the digit); Nulla 1; "pongasi la
  nulla al fine di ogni parola". Key no. 2 (the last cipher with Poggio, sent via Montepulciano, 1538-42) as
  in `test_meister_key.py`, with the single for bc printed as "or" (a misprint) and no null at all. The
  earlier readings stand; nothing in the tests changes.
* **The letter is dated in its own cleartext**: line 192 of the transcript, "Da Roma alli XV. di Aprile
  1542". Line 9 says Montepulciano left Rome on the 25th [of March] carrying letters. Key no. 2 is the one
  "mandata per il Montepulciano", so the historical fit of key 2 to this letter is exact, and its digit
  structure still does not fit the ciphertext (the dotted codes there are ·8x; here the digit after a dot
  is 2/0/7/5 and 8 follows a dot fewer than a dozen times).
* **Lasry, Megyesi, Kopal 2021, read in full** (diva-portal PDF, text extracted). Three facts not in the
  earlier notes: (1) the key clustering by digit frequency put S1 (this volume) in the same cluster as
  Segr. Stato Spagna 6/I and 6/II; (2) the key of S6 was recovered from matching plaintext, tested with the
  automated polyphonic key recovery, and printed as Table 18; (3) but S6 is dated 16 January 1568 to 30
  May 1570 (DECODE records 93 and 94, Cardinal Alessandrino to the nuncio), a generation later, a plain
  single-digit polyphonic cipher with 0 as null and X0Y nomenclature (Figure 20 sample decoded). It is a
  design relative, not this key. The IA-1 sibling in this volume is DECODE record 91: 5 pages, ff. 62v-66v,
  non-decrypted, transcript behind the login.
* **The volume**: the challenge PDF quotes the archive note "Lett. Orig. e cifre del card. Farnese al
  nunzio, 4 oct 1539 - 24 nov. 1548, ff. 7-123". So Spagna 1A holds nine years of Farnese-to-Poggio
  cipher, of which DECODE transcribed 13 pages. More text in this key exists on paper.
* **Elio's two reconstructed keys** (HistoCrypt 2025, Figures 5 and 7, extracted from the PDF). The 1535-37
  Guidiccioni key for the Spanish nunciature: single symbols for every letter (some doubled), CV syllable
  series for c d n p r s t only, a nomenclature of about 30 words. The 1540 key: vowel singles plus a
  full CV syllabary with polyphonic pairs selected by a dot. These are the two documented Farnese
  chancery designs closest in date to April 1542; both are syllabaries with letter singles, which is the
  model class used below.
* MysteryTwister status page: Part 5 still unsolved, 0 solvers; Part 4 solved by 2.
* DigiVatLib returns 404 for Chig.M.II.49 and Chig.L.III.65; neither is digitised.
* Cellsior (2026) published an AI attempt on this cipher that reached nothing and says so.

### The unit level, measured directly

Digit 8 is followed by 0/2/7/9/1 in 85% of cases and precedes 4 or 6 fewer than a dozen times in 824:
it is a pair prefix. Digit 3 is preceded by 0 or 7 in 73% of cases: it is a pair suffix. That is the
shape of a syllable table, not of letters.

`segem.py`: unigram EM over units of one or two digits (nulls split; Dirichlet prior for sparsity)
converges to **41 unit types over 3643 tokens** and is stable under the prior (39-43 types across
settings). The inventory: 80 316, 57 281, 6 275, 27 251, 03 231, 9 213, 5 193, 73 187, 1 139, 7 138,
82 114, 8 90, 35 85, 0 82, 52 77, 06 65, 89 64, 75 63, 2 59, 08 59, 37 55, 72 52, 05 49, 38 47, 67 46,
26 42, 81 41, 28 41, 87 32, 25 31, 97 28, 59 28, 3 26, 29 26, 36 24, 01 24, 78 20, 50 15, 90 15, 60 12,
20 7. Word-final units: 27 (86 of 251), 80 (83 of 316), 73, 57, 6, 03. Word-initial: 9, 7, 73, 57, 03,
27, 05, 06. Top unit bigram 57|82 at 47.

Dots against these boundaries: 92 on a unit's last digit, 91 on a unit's first digit, 17 on singles.
The three commonest dotted forms are 27 with the dot on the 7 (48), 27 with the dot on the 2 (29), and
57 with the dot on the 7 (29). Read with Elio's rule, a dot on the last digit of a unit marks the
antecedent of the next unit.

### Matched control, then the real text

`synk2.py` writes a synthetic in the key-2 family renumbered at random, with null 4 after 40% of words,
no code containing 4, five vowel singles, polyphonic consonant-group singles, eight CV series as digit
pairs in prefix blocks, dotted variants for ta/qua/che, two nomenclature codes, 6554 digits of held-out
period Italian. On it the EM segmentation recovers unit boundaries with precision 0.94 and recall 0.87
(72% of units exactly).

`usolve.py` then maps each unit type to a letter, a polyphonic letter pair, a CV syllable, che/chi/qua/
que/qui/gn-, et or non, and anneals the mapping under the no-space 5-gram LM (`lmns.py`, cipher
orthography: no h except ch, no doubled consonants, built from eight Nuntiaturberichte volumes) with a
per-letter bonus of 1.0 nat, below the held-out cost of 1.89, so predictable strings cannot be spammed
(with the bonus at 1.89 every unit became "nostrosignore").

### Result: the two-stage attack fails, and the control says why

| run | score | key recovered | agreement between seeds |
|---|---|---|---|
| synthetic 1, three seeds | -7222 to -7293 | 2%, 6%, 12% of tokens | 0.16 to 0.41 |
| synthetic 2, one seed | -7604 | 16% | |
| real text, three seeds | -7513 to -7696 | | 0.24 to 0.35 |

`oracle.py` explains it. On synthetic 1 the true plaintext scores **-5035** under the same objective, but the
best fixed mapping from the EM units to plaintext elements scores **-11850**, worse than what the annealer
found. Only 68% of the EM tokens have any consistent right answer: the single digits double as halves of
pairs in this design (as they do in Meister's key 2), so a segmentation fixed before the key is known is
wrong for a third of the tokens, and that alone destroys the language-model signal. The search did its job;
the ceiling is the segmentation.

Two objective pitfalls met on the way, recorded so they are not met again: with a per-letter bonus equal to
the held-out cost the annealer maps every unit to a long predictable word ("nostrosignore"); with a raw
OCR corpus the letter i becomes an attractor through Roman-numeral runs (0.3% of tokens, enough).

So segmentation and key must be solved together. That is the class of `native/Program5.cs`, which earlier
sessions ran to non-convergence on this text after it had recovered synthetic keys of the same design. The
present session's contribution is therefore negative on the cryptanalysis and positive on the record:
the design family is pinned to the Farnese chancery syllabic ciphers of 1535-1542, the unit inventory is
measured, the historically matching printed key (Meister no. 2) is verified from the scan and excluded on
structure, and the one recovered relative (S6) is dated 1568-70 and unrelated.

### What would move it

1. **Register with DECODE** (de-crypt.org, free for researchers) and download from record 92 the eight
   400 dpi images, from record 91 the IA-1 transcript (the sibling letter in this volume, 5 pages), and
   from records 93-94 `s6key.txt`. The images restore the word division the transcript lost and settle the
   dot placements; IA-1 doubles the text in the same chancery hand and probably the same key family.
   This session could not do it: creating accounts is outside its remit.
2. Order the folios around ff. 62-73 of Segr. Stato Spagna 1A (the archive note gives ff. 7-123 of
   Farnese-to-nuncio cipher, 1539-1548): more ciphertext in the same keys, and possibly a decipher.
3. The clear copies: BAV Chigi L III 65 ff. ~165-190, AAV Lettere de' Principi 14 A, Naples Carte
   Farnesiane 723 (12 April 1542). Neither Chigi manuscript is on DigiVatLib.

New files: `segem.py` (EM segmentation), `lmns.py` (no-space LM in cipher orthography), `synk2.py`
(key-2-family synthetic), `usolve.py` (unit-level annealer), `uscompare.py` (convergence), `oracle.py`
(ceiling). Corpus and LM caches are gitignored; rebuild with `python build_it_lm.py` after fetching the
eight `nb_*.txt` volumes listed in the session transcript from archive.org (`nuntiaturberich0{0,3,4,5,6,8,9}romgoog`,
`nuntiaturberich10romgoog`, file `<id>_djvu.txt`).

### 2026-09-16: DECODE access obtained; Lasry on separators

Daniel now has a DECODE account. `decode/MANIFEST.md` lists the exact files of records 92, 91, 93, 94 (names read from
the public RecordsView pages), `decode/fetch_decode.py` downloads them with a browser session cookie,
`decode/compare_transcripts.py` aligns the DECODE transcription with the MysteryTwister text digit by digit and mark
by mark, and `decode/crop_lines.py` cuts a page image into 2x line strips.

George Lasry (e-mail, 16 Sep 2026) states that the Challenge 5 documents carry **no visual separators** between
logical tokens, unlike other collections, and that recognising variable-length tokens is the point of the challenge.
This removes route (b) of "Final status" above: the images cannot restore a word division that the manuscript never
had. They remain worth having for dot placement, the uncertain digits, the 069v cleartext frame, and the IA-1
sibling (record 91). The statistical result that digit 4 behaves as a null / word separator stands and is the only
segmentation signal on offer.

## 2026-09-18: the DECODE images and the IA-1 sibling, used

Downloaded from DECODE (Daniel's account): record 92 (the eight 400-dpi page images, the transcription, the address
leaf) and record 91 (IA-1: five page images, its transcription, four document images). Images live in `decode/` and
`img/` and are git-ignored (Vatican copyright); only derived text is kept.

### What the downloads are

* **DECODE's R92 transcription `DOC_R92_D1633_1633.txt` is byte-identical to the MysteryTwister text.** No second
  transcription exists; the images are the only new evidence.
* `DOC_R92_D1211_1211.png` is the address leaf: "Al Rev.mo mons. come fratello il vesc.o di Tropea Nuntio di N.S."
  (Poggio was bishop of Tropea), endorsed "Roma 1542, dal Card.le Farnese". 073v closes "Da Roma alli XV di Aprile
  1542 ... Come fratello Il Car. Farnese".
* The four R91 document images are cleartext Farnese letters of summer 1542 ("dup.to di 7 d'Agosto"; legations of
  Contarini to the Emperor and Sadoleto to France). No key sheet, no decipherment.
* The faint writing between the cipher lines (e.g. 070v) is **show-through** of the recto cleartext: mirrored, it
  reads "dar notitia ... circa la materia della ..." and "per questa causa principali è stato mandato" from 070r.
  There is no interlinear decipherment.

### IA-1 (R91) is a different key and a different design

| | IA-2 (this) | Spain IA-1 (R91) | Portugal IA-1 (Part 4, solved) |
|---|---|---|---|
| digits | 6552 | 2956 | 10934 |
| doubled digits vs chance | **0.30** | 0.88 | 0.57 |
| commonest digits | 7 .18, 0 .13, 8 .13, 5 .13 | 8 .19, 1 .16, 6 .12, 2 .12 | 2 .28, 1 .16, 4 .14 |
| digit 1 | .03 | .16 | .16 |

IA-1 (a December letter on the Nuremberg diet and Buda, 1541) has no doubling suppression, and its wide gaps (185
groups of 2-12 digits) are not word division. Lasry–Megyesi–Kopal's "another key" is confirmed; nothing transfers.

### The image-verified transcript

Seven page agents re-read every cipher line of 070r-073r against the 400-dpi images (`decode/reread/*.txt`, one
file per page, every disagreement listed with the image reading). `decode/build_reread.py` assembles them into
**`IA-2_reread.txt`** (parse5 format).

* 151 digit positions touched (2.3%): 62 substitutions, 39 insertions, 22 deletions. The largest single fault:
  on 071v the transcriber **copied four groups twice** (l.4 `5 7 2 7 4 .`, l.5 `. 2 7 4`, l.9 `5 0 3 8 2 7`, l.20
  `6 3 4 0`). 072v l.3 has `6 0 8 0` struck through in the MS (removed); 073r l.10 and l.16 have struck glyphs.
* Commonest confusion: the flat-topped 3 against the z-shaped 2 and the barred 7, and an L-shaped glyph read as 1
  in some places and 2 in others.
* Dots: of the 202 transcribed dots nearly all are confirmed over the stated digit; a handful moved, ~20 added, a
  few absent (flourishes). 222 dots now. 52 `?` remain, mostly at the binding fold of 071v and under blots.
* **Baseline dots** (" . " between digits) exist on 071r-073r only, ~90 of them; parse5 always dropped them. The
  digit before one is 4 or 9 in half the cases. Too sparse to be word division (Lasry is right); they read like
  clause punctuation.

**None of the structural statistics moves.** Doubles, the dot carriers (7 96, 2 41, 0 29), the digit after a dot
(7/2/0/5), the dot bigrams (27·, 57·, 40·; ·72, ·27, ·70, ·05), the vowel set and the unit inventory are what the
earlier sessions measured on the old text. The transcript was sound; the images confirm it rather than change it.

### A new exclusion: no renumbering of the printed Farnese keys

A doubled digit stays doubled under any relabelling of a key, so the doubled-digit rate is a key-family invariant.
Italian (cipher orthography, h and double letters dropped, null after 37% of words) encoded with each printed key:

| encoding | doubled digits | / chance |
|---|---|---|
| Meister key 1 (Montepulciano 1539-42) | 9.7% | 0.82 |
| Meister key 2 ("mandata per il Montepulciano") | 7.8% | 0.63 |
| random polyphonic single digits | 6.4% | 0.48 |
| **IA-2** | **3.6%** | **0.30** |

Key 2 would put ~510 doubles in 6552 digits; IA-2 has 233, a gap of about 12 standard deviations. So IA-2 is not
key 1 or key 2 renumbered, and not any single-digit polyphonic design: its key was built so the same digit almost
never has to be written twice. Only 7, 5 and 8 double at all (81, 63, 36); 0, 4, 6, 9, 1 essentially never.
That is what disjoint prefix/suffix classes in a syllabary give, with 7/5/8 the digits that serve on both sides.

### Status

Not solved. The DECODE material is exhausted: the images give a better transcript (dittographies removed, dots
checked, struck digits identified) but no separators, no decipherment and no key, and IA-1 is another key. The
routes are unchanged: the key (Chigi M II 49), or the clear copy (Chigi L III 65 ff. ~165-190, Lettere de'
Principi 14 A, Naples Carte Farnesiane 723), or more ciphertext in the same key from Segr. Stato Spagna 1A ff.
7-123 (1539-48), which DECODE does not hold.

### DECODE searched for further material (2026-09-18)

Public `RecordsList?cmd=search&search=` queries: Farnese (7 hits, only R91/R92 before 1579), Poggio 0, Montepulciano 0,
Tropea 0, Chigi 0, Paolo III 0, Spagna/Spain/SdS_Spain (Vatican Spain dossiers start 1566 after IA), years 1538-1548
(Florence ASFi keys 1541-43 = Medici, Bavarian keys, Simancas 1543 = Charles V, Venice 1545-46: no papal item).
Nothing else from the Farnese chancery of Paul III is catalogued. The only unexamined papal keys are the four undated
Camera Apostolica doss. 393 records (R23, R202, R203, R204; Latin/Italian), a long shot worth one look by hand.

The four Camera Apostolica records were fetched and read (images in `img/`, git-ignored). They are the **Avignon
keys of Gabriele de Lavinde, c. 1379** ("Ego Gabriel de Lavinde ... d(omi)no n(ost)ro p(a)p(e) Clemente", the
antipope Clement VII): monoalphabetic symbol alphabets with a few nulls, and small nomenclators of letter-pair codes
(Papa, Cardinales, Rex Francie, Imperator, Florentini ...), plus one Occitan note of 1400-ish dated at Avignon. No
digits, no syllabary, 160 years too early. Irrelevant to IA-2. DECODE now holds nothing further for this cipher.
