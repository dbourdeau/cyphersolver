# Alonso Sánchez (Venice) to Charles V, 1522 — RAH Salazar 9/23–9/26, DECODE R9593–R9657

Status: in progress
**23 Oct 2026, r2o (Claude Opus 5.5)**: **CSP Spain 2 rechecked entry by entry** (british-history.ac.uk, nos. 380-515
with date and Salazar folio): R9593 (5 March) is not calendared; **R9594 (15 March, A. 23 ff. 73-75v) = no. 396**, which
Bergenroth abstracted from a contemporary decipherment in the Gayangos papers while calling the cipher "not extant" (it
is R9594); the other matches are as in the table below (abstracts give the gist, not the Spanish). **R9593 read sign by
sign** with Tomokiyo's key on the two DECODE images (`R9593_signs.txt`, 53 lines, 1,248 tokens, 520 code groups;
reading `R9593_reading.md`, English `_en.md`, log `R9593_reread_log.md`): Don Juan Manuel's and Geronimo Adorno's
letters sent on; the Signoria audience on the **lansquenets' passage of Val Camonica** (Andrea Gritti's officer, damage
denied); the **French have taken Caravaggio**; the Swiss at **Monza** said to be 16,000 and 4,000. Key values adopted:
`gim` = *suyos* (R9635's decipherment and four contexts here; Tomokiyo's "suquos?"), `fef` = *toda* (*todavia* here and in
R9653, *todas*); `ril` = *lansquenetes?* entered flagged (sense and slot, five contexts). About twenty groups stay open;
f. 27r ll. 26-33 and f. 27v ll. 11-13 do not build sentences. v2_score 0.614 explicit holes (27/44), plain 0.136, hole
rate 0.13; look-alikes ~2.5%: **kept decoded, not read**. The other 48 records (R9594 onward in date order) were
not reached: gap not-attempted with the list. fraction_read 0.93 -> 0.75 (reading-body words of the five letters worked,
estimated).
**23 Oct 2026, r2i (Claude Opus 5.5)**: **R9635's tear filled from its own cipher**: the ten torn words of f. 22r ll. 9-11
stand in cipher on f. 20r ll. 11-14 and read sign by sign with Tomokiyo's key (*en la dicha capitulacion. Repliqueles que
las tierras estavan en poder del señor infante, y respondieron que quien quiera que los tuviese ...*; `hec` = quiera,
`vac` = dicha, `gta` = l + `ta` = les); no second copy exists on the record or its neighbours. R9635 0.833 -> 0.913
(v2_score, explicit holes). **Every DECODE record of the Sánchez run R9593-R9657 fetched and every image opened** (52
records, 163 images; `research/reading_audit/r2i_fetch.py`, scratchpad `reread/r2i/`): two more contemporary
decipherments found and read: **R9613** (18 June 1522; clear copy ff. 206r-207v of the same record; `R9613_reading.md`,
0.99) and **R9641** (27 Oct 1522; clear copy ff. 187r-188r filed under R9642, which is the letter's duplicate cipher;
`R9641_reading.md`, 1.0; new value `vad` = duque). Both checked against their cipher with Tomokiyo's key. The other
~40 Sánchez letters carry no decipherment on DECODE (the "Inline Cleartext" flag marks clear opening/closing paragraphs
and postscripts) and were not read: gap not-attempted (sign-by-sign reading with the key, 2-15 pages each). R9654 has
no images. fraction_read 0.67 -> 0.93 on the four letters worked (estimated, plaintext words).
**23 Oct 2026, re-read (REREAD_BRIEF b23)**: **R9635 read** from its own contemporary decipherment, a clear court-hand
copy on f. 22r (DECODE image P3, right page) that no earlier pass had opened; checked against the cipher of ff. 20r-20v
with Tomokiyo's key, all checks agree (the old edition's "darian" is *pagarian*; `hec` = Inglaterra withdrawn). Reading
`R9635_reading.md` / `_en.md`, log `R9635_reread_log.md`, transcription `R9635_decifrado_f22r.txt`; 0.833 clean on
explicit holes. **R9653 stays decoded, not read**: its "illegible head paragraph" is the bleed-through of eleven
legible cipher lines on f. 299v, now read sign by sign with the foot lines (`R9653_cipher.txt`, partial reading
`R9653_reading.md`, log `R9653_reread_log.md`): the first paragraph builds sentences (letters from France of 26-27 Oct
from Saint-Germain; English ships lost on the way home, the rest driven ashore in Brittany, "nuevas sin fundamento"),
the second (Adorno, the protonotary, Juan Manuel) does not (cipher-only 0.455 on explicit holes). Proposed key values
(not yet in `key_codes.tsv`): from the decipherment `deg` visto, `feb` tanto, `gim` suyos; sense-only, for review: `tac`
tenian?, `fef` toda, `ref` Italia, `zub` Adorno. Sign values: `∝` = m, `ꞔ`/`∂` = e, `g#` = u/v, `ẗ4` = n, `q` = t, `3` = d,
bold `∞` = g; `Ꝁo`/`Lo` are s/t look-alikes. Class not read -> read in part, method read from existing decipherment,
fraction 0 -> 0.67 (estimated, plaintext words).
**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
R9635 and R9653 are **decoded, not read**: f. 20r is a table of phrase fragments between untranscribed letter runs, and
R9653's cipher gives one phrase; what reads as sentences is clear text (the Rhodes news, the Pace paragraph on f. 21),
not decipherment. Class read in part -> not read, method -> not solved (Tomokiyo's key kept as a part); 0.6 withdrawn.
The "Reading so far" line below is superseded.
Reading so far: read in part (R9635 f. 20r and R9653 f. 299r; the cipher itself was already solved by Tomokiyo 2025)

Catalogue entry "Alonso Sánchez (Venice) to Charles V, 29 ciphertexts" (Tomokiyo list, scored B).
Worked 2026-09-20.

## Prior art: the cipher was already reconstructed

**S. Tomokiyo, "Correspondence in Cipher of Imperial Ambassadors Alonso Sanchez and Juan Manuel (1522)",
<https://cryptiana.web.fc2.com/code/AlonsoSanchez.htm>, first posted 6 September 2025, last modified
9 September 2025.** Saved here as `tomokiyo/AlonsoSanchez.htm` / `.txt` / `.png`.

He reconstructed Sánchez's 1522 cipher from the contemporary decipherment attached to DECODE R9605,
after spotting `vog veg` = "en el" near the end. The article gives:

- the substitution alphabet, as a hand-drawn table (`tomokiyo/AlonsoSanchez.png`): homophones for
  a–z plus a null group, with `q`-with-double-bar as the plural ending `-s`;
- a nomenclature of ~177 three-letter codes and 17 two-letter codes (transcribed here to
  `key_codes.tsv`);
- the deciphered **opening lines only** of R9593–R9632, plus two longer passages (R9621 entire,
  R9623 last paragraph).

So the cipher itself is solved, and solved before this project touched it. That is the contamination
answer for the profile: a full reading of the system existed publicly from 6 September 2025.

Tomokiyo also reconstructed the parallel cipher of **Juan Manuel** (imperial ambassador at Rome,
DECODE R9499–R9529); that key is in the same article and in `key_codes.tsv`'s sibling section of the
saved text, not used here.

## What the catalogue entry got wrong

The catalogue entry said "RAH, Signatura 9/24 (29 items)", 1522–23, ending at the treaty of July 1523.
From the DECODE records themselves (`decode/rec*.htm`, metadata table below):

- the run is **9/23, 9/24, 9/25 and 9/26**, not 9/24 alone;
- every record in R9603–R9657 carries a 1522 date. **Nothing here reaches 1523**, so the July 1523
  treaty is outside this group;
- a third of the tail is not Sánchez at all but **Lope Hurtado de Mendoza** (R9634, R9644–R9646,
  R9648–R9650, R9652, R9656);
- almost every record has DECODE's `Inline Cleartext: Yes` — a contemporary decipherment is bound with
  the ciphertext. These letters were never really unread; they are unedited.

## Structure of the nomenclature

Codes are consonant–vowel–consonant over C1 ∈ `z y x v t s r p n m l h g f d c b` (16, running
backwards through the alphabet as the plaintext runs forwards), V ∈ `a e i o u`, C3 ∈ `b c d f g h l m n`
(9) — 720 slots, of which Tomokiyo recovered ~177. Sorting by (C1, C3, V) puts the plaintext in
alphabetical order, so an unassigned code is bracketed by its neighbours: `zid zod zud | zef zif | zog
zug | zel | zem zom | zen zun` gives a(h)un, ahun, al, allende, algun, alla, alli, antes, aqui,
aquell, arma, assi. The alphabetisation is the scribe's own and is loose at the edges (allende before
algun, cosa before concorda), so the bracket is a range, not a point.

The 17 two-letter codes are the highest-frequency words: `xa` con, `ta` es, `re` hombre, `ne` muy,
`ho` que, `lu` por, `do` venecia, `ma` occorie, `ge` rompe, ...

This is the 1496 Ferdinand-and-Isabella type of Spanish cipher; the vocabulary is large for the date.

## The records

Fetched from DECODE 2026-09-20 (`decode/getrec.py`, `decode/fetch.py`, bordeaux cookie).
Images in `img/`, git-ignored; RAH material, permission needed to republish.

| DECODE | RAH Salazar | date (1522) | pp | DECODE status | decipherment bound in | author |
|---|---|---|---|---|---|---|
| R9603 | 9/24, f. 13-14 | May | 6 | Non-decrypted | Yes | Sánchez |
| R9604 | 9/24, f. 18-19 | May | 4 | Non-decrypted | Yes | Sánchez |
| R9605 | 9/24, f. 39-44 | May | 11 | Decrypted | No | Sánchez |
| R9606 | 9/24, f. 44-45 | May | 2 | Non-decrypted | No | Sánchez |
| R9607 | 9/24, f. 65-68 | May | 8 | Non-decrypted | Yes | Sánchez |
| R9608 | 9/24, f. 96-97 | — | 3 | Non-decrypted | No | Sánchez |
| R9609 | 9/24, f. 107-109 | May | 6 | Non-decrypted | Yes | Sánchez |
| R9610 | 9/24, f. 132-134 | Jun | 6 | Non-decrypted | Yes | Sánchez |
| R9611 | 9/24, f. 139 | Jun | 2 | Non-decrypted | Yes | Sánchez |
| R9612 | 9/24, f. 167-169 | Jun | 6 | Non-decrypted | Yes | Sánchez |
| R9613 | 9/24, f. 203-206 | Jun | 11 | Decrypted | Yes | Sánchez |
| R9614 | 9/24, f. 208-210 | Jun | 6 | Non-decrypted | Yes | Sánchez |
| R9615 | 9/24, f. 218-219 | Jun | 4 | Non-decrypted | Yes | Sánchez |
| R9616 | 9/24, f. 224-228 | — | 9 | Non-decrypted | Yes | Sánchez |
| R9617 | 9/24, f. 241-245 | Jun | 9 | Non-decrypted | Yes | Sánchez |
| R9618 | 9/24, f. 246 | Jun | 2 | Non-decrypted | Yes | Sánchez |
| R9619 | 9/25, f. 16-17 | 10 Jul | 3 | Non-decrypted | Yes | Sánchez |
| R9620 | 9/25, f. 24 | Jul | 2 | Non-decrypted | Yes | Sánchez |
| R9621 | 9/25, f. 56 | 19 Jul | 1 | Non-decrypted | Yes | Sánchez |
| R9622 | 9/25, f. 75 | 19 Jul | 1 | Non-decrypted | Yes | Sánchez |
| R9623 | 9/25, f. 133-134 | 19 Jul | 4 | Non-decrypted | Yes | Sánchez |
| R9624 | 9/25, f. 135-136 | — | 4 | Non-decrypted | No | Sánchez |
| R9625 | 9/25, f. 137-139 | Aug | 4 | Decrypted | Yes | Sánchez |
| R9626 | 9/25, f. 141-144 | — | 9 | Non-decrypted | Yes | Sánchez |
| R9627 | 9/25, f. 145-148 | — | 4 | Non-decrypted | No | Sánchez |
| R9628 | 9/25, f. 156-157 | — | 2 | Non-decrypted | Yes | Sánchez |
| R9629 | 9/25, f. 158-159 | Aug | 3 | Non-decrypted | Yes | Sánchez |
| R9630 | 9/25, f. 180 | Aug | 2 | Non-decrypted | Yes | Sánchez |
| R9631 | 9/25, f. 182-189 | Aug | 15 | Non-decrypted | Yes | Sánchez |
| R9632 | 9/25, f. 198-205 | Aug | 18 | Non-decrypted | Yes | Sánchez |
| R9633 | 9/26, f. 4-7 | — | 8 | Non-decrypted | Yes | Sánchez |
| R9634 | 9/26, f. 14-16 | Sep | 6 | Non-decrypted | Yes | **Lope Hurtado** |
| R9635 | 9/26, f. 20–22 | — | 5 | Non-decrypted | Yes | Sánchez |
| R9636 | 9/26, f. 68–71 | — | 7 | Non-decrypted | Yes | Sánchez |
| R9637 | 9/26, f. 76 | Oct | 1 | Non-decrypted | Yes | Sánchez? |
| R9638 | 9/26, f. 104–108 | 11 Oct | 8 | Decrypted | Yes | Sánchez |
| R9639 | 9/26, f. 111–115 | Oct | 10 | Non-decrypted | Yes | Sánchez |
| R9640 | 9/26, f. 139–141 | Oct | 6 | Non-decrypted | Yes | Sánchez? |
| R9641 | 9/26, f. 173–174 | Oct | 4 | Non-decrypted | Yes | Sánchez? |
| R9642 | 9/26, f. 184–188 | — | 8 | N/A | Yes | Sánchez? |
| R9643 | 9/26, f. 189–191 | Oct | 6 | Non-decrypted | Yes | Sánchez? |
| R9644 | 9/26, f. 237–243 | 1 Nov | 14 | Decrypted | Yes | **Lope Hurtado** |
| R9645 | 9/26, f. 243–244 | Nov | 4 | Non-decrypted | Yes | **Lope Hurtado** |
| R9646 | 9/26, f. 252 | — | 2 | Non-decrypted | Yes | **Lope Hurtado**? |
| R9647 | 9/26, f. 257–259 | — | 6 | Non-decrypted | Yes | Sánchez? |
| R9648 | 9/26, f. 260–265 | 9 Nov | 12 | Non-decrypted | Yes | **Lope Hurtado** |
| R9649 | 9/26, f. 266–268 | 9 Nov | 6 | Non-decrypted | Yes | **Lope Hurtado**? |
| R9650 | 9/26, f. 269–272 | — | 10 | Decrypted | Yes | **Lope Hurtado** |
| R9651 | 9/26, f. 276–279 | — | 8 | Non-decrypted | Yes | Sánchez? |
| R9652 | 9/26, f. 295–296 | Nov | 2 | Partially decrypted | Yes | **Lope Hurtado** |
| R9653 | 9/26, f. 299–300 | 20 Nov | 4 | Non-decrypted | Yes | Sánchez |
| R9654 | 9/26, f. 301–302 | 20 Nov | 4 | Non-decrypted | Yes | Sánchez |
| R9655 | 9/26, f. 303 | Nov | 2 | Non-decrypted | Yes | Sánchez |
| R9656 | 9/26, f. 334–335 | Nov | 4 | Non-decrypted | Yes | **Lope Hurtado** |
| R9657 | 9/26, f. 354–355 | — | 3 | Non-decrypted | No | Sánchez? |

Generated by `decode/meta.py` into `decode/metadata.md`. "Decipherment bound in" is DECODE's
`Inline Cleartext` flag. Nine of the 55 records name **Lope Hurtado de Mendoza** as author.

## Work in this session

- Prior-art search; Tomokiyo's article found and saved.
- DECODE metadata for R9603–R9657 pulled and tabulated; shelfmark, date and authorship errors in the
  catalogue entry corrected above.
- Nomenclature transcribed to `key_codes.tsv` and its ordering verified.
- Images fetched for the 9/26 tail (R9633–R9657), the part Tomokiyo's article does not cover.
- **The c-block numerals settled.** Tomokiyo has `cob` xviii, `cub` xix, `cad` xx … `cud` xxiv, `caf`
  xxv, and leaves the rest blank. The ordering fills the run: `cef` xxvi, `cif` xxvii, `cof` xxviii,
  `cuf` xxix, and below, `cab` xv, `ceb` xvi, `cib` xvii. `cef` and `cif` are then **confirmed in
  text** (see below); this also resolves the uncertain "[xxviii?]" in his reading of R9598 as `cof`.
  Added to `key_codes.tsv`, flagged as this project's.
- **R9653 read in part** (`read_r9653.md`), a record outside Tomokiyo's range. f. 299r is a mixed
  letter: six lines of cipher at the head, some thirty lines in clear, two lines of cipher at the
  foot. The clear middle is the news of the siege of Rhodes — five assaults to 10 October, mines and
  underwater mines, twenty thousand Turks dead by the Venetians' count and fifty thousand by a
  secretary of the Signoria's, the Sultan said to have withdrawn to the mainland, and a thousand
  infantry enough to save the island. (Rhodes capitulated a month later.) The foot cipher paragraph
  reads in part "**cartas de Francia de xxvi y xxvii del passado de …**". The head paragraph is
  defeated by ink bleed from the facing leaf at the resolution DECODE serves.

- **R9635 read in part** (`read_r9635.md`), 16 Sept 1522, Salazar 9/26 f. 20–22, also outside Tomokiyo's
  range. f. 20r is a full page of cipher in a clean hand with a *patchy* contemporary decipherment
  between the lines. Read: "das cartas de vuestra magestad", "los de esta republica", "del señor
  infante", "ducados allende de los otros xviii mil", "**mas de xv mil ducados**", "todos los … mil
  ducados luego de esto", with the glosses *obligados … fuessen restituydas sus bienes*. The subject is
  the sums owed by the Signoria under the capitulation and the restitution of goods seized from
  imperial vassals — the same business R9638 (11 Oct) carries entirely in clear.
- **`cab` = xv attested**, in "ped xig cab pol9 vud+s" = *mas de xv mil ducados*. That is a third
  predicted numeral confirmed in text (with `cef`, `cif`), and none of the seven is contradicted.
- Notation settled: `pol9` = `pol` (mi) + the letter sign for **l** = *mil* (the `l` sign reads as a `g`
  in this hand); `gɣ lal` = letters *r-e* + `lal` (publica) = *republica*; the opening nulls are padded
  with the meaningless clear words *como* / *quien*, which is what Tomokiyo's "como quierr" note under
  the nulls column means.
- `decode_tokens.py` resolves a token string against the key and brackets unknown codes by their
  alphabetical neighbours.

## The letter alphabet, and why the spelled runs are still open

Tomokiyo gives the substitution alphabet only as a hand-drawn table
(`tomokiyo/AlonsoSanchez.png`). Read off at high zoom it is about thirty signs over twenty-two
letters (a b c d e f g h i l m n o p q r s t u x y z), most letters having two or three homophones:

| a | b | c | d | e | f | g | h | i | l | m |
|---|---|---|---|---|---|---|---|---|---|---|
| n, ʒf | ᵹ | z, Ә | ∞, 3, ɸ | 4, ʒ | P | ∞(bold), L | x, m∞ | a₄ | 9 | β, ✗ |

| n | o | p | q | r | s | t | u | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|
| ᶻ, ᵺ₄ | #, ǂ | a₀, tt | 8, ϙ | Ɋ | ǂ(q-crossed), ✗ₒ, P | q, Lo | m, ʃ# | o, ʑ | ʒ | A |

Two things this settles:

- **The "q with a double bar" is the letter `s`.** It is not a separate plural marker: the plural
  ending is simply the letter s written after a code group. Tomokiyo's guess ("may well be the plural
  ending -s") is right for the wrong reason.
- **`r` is a different sign** — a q with a loop — and the two are easy to confuse in this hand.

`alpha.py` holds the map in the transcription labels used for the code groups and spells a run out.
It verifies on runs taken from R9635 f. 20r: `nx#gn` = **ahora**, `ttn#n` = **nada**.

**Why the spelled runs are nevertheless not yet read continuously.** Tomokiyo transliterates the code
groups with latin labels (`zid`, `vog`, …) drawn from a set that includes `v`, which is not one of the
twenty-two plaintext letters; so the code labels and the alphabet do not share one transliteration, and
each sign has to be matched to both by eye. At the resolution DECODE serves, distinguishing the
homophone pairs — `Ɋ` (r) from `ǂ` (s), `9` (l) from `Ɋ` (r), `∞` (d) from bold `∞` (g) — is a
judgement call per occurrence. Getting it wrong silently produces plausible-looking Spanish that is not
what the page says, so the runs are left marked rather than filled in.

The way through is the one the glosses offer: collate the patchy interlinear decipherment on R9635
f. 20r word by word against the signs beneath it, which pins each homophone in *this* scribe's hand,
and then the unglossed lines and the rest of the group follow. That is edition work against a published
key, not cryptanalysis.

## R9605 gives ground truth, and it changes two things

R9605 (9/24 f. 39-44, 7 May 1522) is the record Tomokiyo broke the cipher from, and its images show
why: the **cipher and the clerk's full contemporary decipherment sit on facing leaves**. Fetched here
and aligned at the end of the letter (`calibration_r9605.md`):

> *plegue adios* `nuf` `pac` `ɡɣβ4q4` `vog` `veg` `zn·β·aɥ` `nuf` = "plegue a Dios **no lo yerre en el
> camino**"

`vog veg` = *en el* is Tomokiyo's own way in, met here in situ. Two things follow that the key alone
could not give:

1. **Code groups are used for syllables, not only whole words.** `nuf` is *no* the adverb, and in the
   next breath the final syllable of *cami-no*. A reading that assumes one group = one word will
   mis-segment.
2. **The lookalike signs separate.** *camino* needs `β` = **m**; *ahora* (`nx#Ɋn`, R9635 f. 20r) needs
   `Ɋ` = **r**; the bold `∞` is **g**. All three are a "g"-shape at DECODE's resolution and they are
   the single largest source of error in the spelled runs.

This is the calibration route: align the whole of R9605's cipher against its decipherment - several
hundred signs of ground truth - to fix each homophone in this scribe's hand, then carry it to the
unglossed pages. That is the next session's work.

### The calibration begun, and a correction to the published key

Continuing the same passage of R9605 f. 44 against the clear *"la venida del visorey **con todas las
postas**, que despacho y escrivo"*:

- `xel def` = *del visorey*; `ded xof` = *veni*+*da* = *venida* — verbatim, and more code groups
  carrying syllables.
- **`va` = *despacho*, not "desponho".** Tomokiyo's table gives `va` = *desponho*, which is not a
  Spanish word; the clear reads *que despacho y escrivo* with `ho` = *que* and `va` in that slot. It
  also explains his puzzled "me desponho x-e-r-o-n que" in R9623. Corrected in `key_codes.tsv`.
- The spelled run for *escrivo* is seven signs for seven letters, fixing `z` = c, `ɡ` = r, `aɥ` = i,
  `m` = **v**, `#` = o with ground truth beneath them. This is the method working.
- `pog` = *mesmo*, `suf` = *hago*, in "y lo mesmo hago".

One check came out **inconclusive** and is recorded as such: the clear at "que fue a …" stands over
the group `cud`, which Tomokiyo reads "xxiv?". Had the clear read *xxv*, the c-block series would
shift by one. It does not settle it — the date is written over a correction and reads as something
like *xxv y xxvij*, two dates, so it cannot be matched to one group. `cab`, `cef` and `cif` do not
depend on it: each was confirmed in its own context, independently of where the run starts.

### The opening of R9605 read straight through, and the sign table it fixes

f. 39r is R9605's first cipher page and f. 42 the first page of the clerk's decipherment; they align
from the first word. Clear: *"Ya dixe a V. Mag. que el embaxador de Hungria fue respondido de los
desta republica con buenas palabras…"*. Cipher:

| cipher | plaintext |
|---|---|
| `cig` | **ya** (code) |
| `vu`·o·ɣ | **di**+x+e = *dixe* |
| `dom pud` `ho` `veg` | vuestra magestad que el |
| `vam` `vuc`·ɡ | **embaxa**+**do**+r = *embaxador* |
| `n·℔·∞` `ɡ·aɥ` | Hun-gria, spelled across the line break |
| `sa` | **fue** |
| `ɡ·ɣ·q·ao·#·&` `vu` `vuc` | r-e-s-p-o-n + **di** + **do** = *respondido* |
| `xig vum` `ɡ·ɣ lal` | de esta + r-e + **publica** = *desta republica* |
| `xa` `yuc`·n+s | con **buen**+a+s = *con buenas* |

Nothing there is a guess: the clerk's plaintext stands over every group on the facing leaf. It fixes,
against ground truth rather than by eye: `n`=a, `ɣ`=e, `ɡ`=r, `aɥ`=i, `o`=x, `#`=o, `q`=s, `ao`=p,
`&`=n, `m`=v, `z`=c, `β`=m, `ɋ`=s. (`q`=s here against Tomokiyo's alphabet column `q`=t — two similar
glyphs, the pair to watch next.) The table is carried in `alpha.py`, ground-truth values marked.

**Reading R9605 is not itself a new reading** — the Emperor's clerk deciphered it in 1522. Its value
is the sign table, which is what the genuinely unread pages of the 9/26 tail need; carrying it to
R9635 f. 20r and the rest is now mechanical rather than a matter of judgement.

## The edition pass: the model of the writing was wrong

The earlier failure here came from a wrong model of the page, now corrected. **Everything is written
in ordinary latin-looking cursive.** The two systems are told apart by shape-length and context:

- **three-letter latin trigrams are nomenclator codes** (`xig`, `vog`, `dom`, `pud`, `lig`, `nuc`),
  read straight off Tomokiyo's table;
- **single letters and short runs between them are the substitution alphabet**, where letterform and
  value differ: `n`=a, `y`=e, `g`=r, `o`/`✗`=x, `#`=o, `ao`=p, `m`=u/v, `z`=c, `β`=m, `9`=l, and the
  q-with-double-bar = s;
- three nulls open each paragraph, padded with the clear words *como* and *quien*.

Verified on R9605 f. 39r l. 1 against the clerk's plaintext on the facing leaf: `cig vu·o·y n dom pud
ho veg` = "Ya dixe a vuestra magestad que el", with `vu`(di)+`o`(x)+`y`(e) = *dixe*.

With that, R9635 f. 20r reads. The edition is `edition/r9635_f20r.md`; ll. 2-3 run continuously:

> `lig vog vom nuf gad lel` ao-y-g-`xig`-g `nuc` … `xa pac`+s `xig vum` g-y-`lal`
> = **"pues en esto no se puede perder nada … con los de esta republica"**

Two things in that sentence are new. **`lel` = *puede***, a code Tomokiyo never recovered, bracketed
between `lal` *publica* and `lol` *pudi* and fixed by sense. And *perder* is written p-e-r + `xig`
(*de*) + r — a code group used mid-word for a syllable, the pattern R9605 showed with *cami* +
`nuf`(*no*) = *camino*.

Coverage of the page: ll. 2-3 continuous, plus the passages at ll. 6, 7, 14, 22; l. 1 partly; about a
third in all. The remaining lines are the same work at the same zoom, cryptanalytically unremarkable,
and are left untranscribed rather than filled in by inference.

## What is left

The other 27 records. Most of them have a contemporary decipherment bound in — though R9635 shows the
glossing can be patchy — so the work there is transcription and edition, not cryptanalysis: the cipher is Tomokiyo's, and this folder's key file is
enough to check any passage. The Lope Hurtado de Mendoza letters are **not** in Sánchez's cipher — see below.

## Lope Hurtado de Mendoza writes in a third cipher

R9648 (9/26 f. 260–265, 9 Nov 1522) is Lope Hurtado to Charles V, and mixes clear and cipher inline
within the sentence, in the same general style. But his code groups take finals that Sánchez's key
does not have. Sánchez's third position is strictly C3 ∈ `b c d f g h l m n`; Lope Hurtado's leaf
gives `tep`, `tap`, and groups ending in `z`. Juan Manuel's Rome cipher, by contrast, does use
`p r s t z` as finals (`jap` papa, `jir`, `jus`, `boz`, `qat`).

So Lope Hurtado's key is a third member of the same family, not Sánchez's. Whether it is Juan
Manuel's own is not settled here: none of the groups legible on f. 260v (`ton`, `tep`, `tap`, `xul`,
`xild`, `zar`, `xurzun`) has a value in Tomokiyo's Juan Manuel table either, but that table is itself
only a partial recovery, so absence does not decide it. The nine Lope Hurtado records deserve
their own target.

f. 260r opens in clear: "La carta de V. M[agestad] recebi de xxvj de octubre; don Juan era ya ydo
quando yo llegue aqui; yo yua para el duque a Mariño donde estaua, para hazer con el lo que V. M. me
embio a mandar que hiziese con don Juan si aqui estouiera; y el duque vino a su S[eñoria] con las
cartas de V. M., y bolui con el, que le tope en el camino. Parecele que yo deuia residir aqui
continuamente para seruir mejor a V. M. …" — the same letters of 26 October that R9653's foot cipher
paragraph reports arriving at Venice.

## Calendared in CSP Spain 2 (Bergenroth 1866)

Checked 2026-09-21. Text from british-history.ac.uk, *Calendar of State Papers, Spain*, vol. 2 (1509-1525),
pages pp380-386 to pp510-519, fetched and grepped for "Alonso Sanchez" and "Salazar. A. 23-26". Bergenroth's
source line (date, "M. Re. Ac. d. Hist. Salazar. A. n. ff.") sits before each entry number. His "A. 24-26" =
RAH signatura 9/24-9/26. Matches by volume, folio and date:

| DECODE | Salazar ff. | CSP no. (page) | CSP date, ref | note |
|---|---|---|---|---|
| R9613 | 9/24 f. 203-206 | 429 (p. 435) | 18 June 1522, A.24 ff. 203-206 | exact |
| R9616/R9617 | 9/24 f. 224-228 / 241-245 | 439 (p. 443) | 26 and 30 June, A.24 f. 229; cipher copy ff. 241-250 | letter to Gattinara |
| R9619 | 9/25 f. 16-17 | 444? (p. 449) | 10 July, A.25 ff. 20-22 | date matches, folio near |
| R9621/R9622 | 9/25 f. 56 / 75 | 447? (p. 451) | 19 July, A.25 ff. 58-60 | date matches, folio near |
| R9627 | 9/25 f. 145-148 | 462 (p. 467) | 7 Aug, A.25 ff. 145-148 | exact |
| R9631 | 9/25 f. 182-189 | 470 (p. 473) | 27 Aug, A.25 ff. 182-190 | exact; the long Pace-reception despatch, 15 pp |
| R9632 | 9/25 f. 198-205 | 473 (p. 479) | 31 Aug, A.25 ff. 202-206 | overlap |
| **R9635** | 9/26 f. 20-22 | **476 (p. 482)** | 16 Sept, A.26 ff. 20-22 | exact |
| R9636 | 9/26 f. 68-71 | 482 (p. 484) | 3 Oct, A.26 ff. 68-72 | exact |
| R9638 | 9/26 f. 104-108 | 487 (p. 491) | 11 Oct, A.26 ff. 107-109 | overlap, same date |
| R9639 | 9/26 f. 111-115 | 488 (p. 491); 489 is its cipher duplicate (A.26 [f.] 116) | 15 Oct, A.26 ff. 111-121 | exact |
| R9643 | 9/26 f. 189-191 | 491 (p. 497) | 23 Oct, A.26 ff. 189-192 | exact |
| R9642 | 9/26 f. 184-188 | 495? | 28 Oct, A.26 f. 187 | the heading is 494's (Lannoy abstract, f. 187); probable |
| R9651 | 9/26 f. 276-279 | 500 (p. 502) | 8 and 13 Nov, A.26 ff. 276-280 | exact |

Other 1522 Sánchez entries outside this folder's records: 367, 380, 382, 389 (A.21-22), 396-397 (A.23, March),
450 and 464 (Pascual de Gayangos papers, not Salazar), 436 (C. 71), 471 (abstract), 515 (Adorno and Sánchez,
28 Dec, A.26 f. 413). **Not calendared:** the whole May-June 9/24 run R9603-R9612 and R9614-R9615, R9618,
R9620, R9623-R9626, R9628-R9630, R9633, R9637, R9640-R9641, R9647, and **R9653-R9655 (20 Nov)**. The Lope
Hurtado records match his own entries (475 = R9634, A.26 ff. 14-18; 497 = R9644, ff. 237-241).

Every Sánchez entry says "Autograph in cipher. Contemporary deciphering." So for these fourteen the content
has been in print in English since 1866, abstracted from the court decipherments. They are abstracts, not
transcriptions: no Spanish text and no code values.

**No. 476 against R9635.** Bergenroth: Sánchez asked the Venetians to pay the 20,000 ducats due under the
truce of 1 Sept 1521 "together with the 18,000 ducats left unpaid last year"; they asked that their towns be
delivered to them first; Richard Pace gave him the enclosed memoir and asks for letters to the Pope and to
Don Juan; news from Constantinople. This **confirms** `cob pol9` = xviii mil ("ducados allende de los otros
xviii mil") and the Pace paragraph of f. 21. It **corrects the gloss's subject**: *fuessen restituydas sus
tierras* (f. 21) is the Venetians' condition that their towns be restored, not goods of imperial vassals as
suggested on f. 20r above. It **fills** the gist of the unread lines (the 20,000-ducat instalment, the
Constantinople news) but does not supply the words, and "mas de xv mil ducados" is not in the abstract.
The new-reading claim for R9635 is therefore reduced to the Spanish text and the code values, not the content.

Closed items (moved out of Remaining gaps):
- R9635 f. 22r tear across ll. 9-11 - closed 23 Oct 2026 (r2i): filled from the cipher of f. 20r ll. 11-14, read sign by sign

## Remaining gaps
- R9653 cipher, second paragraph (f. 299v ll. 7-12) and single groups of the first, decoded, not read - blocker: no-key-material; xug, zi, tac, lud, qef, sob, ca, nu absent from Tomokiyo's table, single contexts, no decipherment bound or imaged
- R9653 second copy (f. 300v) and R9654 (ff. 301-302, same date) - blocker: needs-physical-access; f. 300v only as faint bleed-through, R9654 not imaged on DECODE (rechecked 23 Oct 2026)
- R9635 four uncertain words of the decipherment ([?bastar], [?tenido], [?Menorami], [?Lucerna]) - blocker: illegible; cramped court hand at DECODE's resolution
- R9613 and R9641: three and two uncertain words of their decipherments ([?nescia], [?nemora], [?sus pagos]; [?conversacion], [?vera]) - blocker: illegible; fast cursive at DECODE's resolution
- R9593 (5 March 1522) f. 27r ll. 26-33, f. 27v ll. 11-13 and about twenty open code groups (xe, vub, lud, fug, la, lif, ni, fu, sag, nif, ram, tag, zom, fag, pil, dug, nad, mug, tem, nog, ca, ce) - blocker: no-key-material; read sign by sign 23 Oct 2026 (r2o), groups absent from the published key and mostly met once, no decipherment bound or imaged, not in CSP Spain 2
- the other Sánchez records of 9/23-9/26, 48 records (some duplicates: R9626/R9627, R9628/R9629; R9625 and R9638 mostly clear): R9594, R9595, R9596, R9597, R9598, R9599, R9600, R9601, R9602, R9603, R9604, R9606, R9607, R9608, R9609, R9610, R9611, R9612, R9614, R9615, R9616, R9617, R9618, R9619, R9620, R9621, R9622, R9623, R9624, R9625, R9626, R9627, R9628, R9629, R9630, R9631, R9632, R9633, R9636, R9637, R9638, R9639, R9640, R9643, R9647, R9651, R9655, R9657 - blocker: not-attempted; no decipherment imaged (r2i); R9594 is next in date order (5 pp., = CSP 396, whose decipherment is in the Gayangos papers); each readable sign by sign with the key as R9593 was
- Lope Hurtado records R9634, R9644-R9646, R9648-R9650, R9652, R9656 - blocker: no-key-material; a third cipher, finals p/z absent from Sánchez's key; groups not in Tomokiyo's Juan Manuel table (see the lopehurtado1522 target)

## Escalation
- [x] siblings: R9603-R9657 metadata tabulated; R9605 facing decipherment aligned; R9648 examined
- [x] clear-pages: R9605 clerk's decipherment aligned as ground truth; R9635 interlinear glosses used
- [x] known-keys: Tomokiyo 2025 Sánchez key; Juan Manuel key compared for the Lope Hurtado leaves
- [x] print: done 2026-09-21 — Bergenroth CSP Spain vol. 2 (1866) grepped by Salazar folio; 14 of the DECODE records here are calendared as "Autograph in cipher. Contemporary deciphering" (English abstracts made from the bound decipherments). R9635 = no. 476 confirms the reading; the May 9/24 run and R9653 are not calendared. See "Calendared in CSP Spain 2" below
- [x] key-rebuild: c-block numerals by alphabetical bracket (cab, cef, cif confirmed), lel = puede, va = despacho; sign table from R9605
- [x] retry: 23 Oct 2026 (b23) — every DECODE image reopened (R9635's f. 22r decipherment found, R9653's f. 299v cipher found); R9653 re-read sign by sign and regraded (still decoded, not read); R9635 read
- [x] print: redone 23 Oct 2026 (r2o) - CSP Spain 2 entry by entry (nos. 380-515): R9593 not calendared, R9594 = no. 396 (decipherment in the Gayangos papers, cipher called not extant)
- [x] key-rebuild: 23 Oct 2026 (r2o) - gim = suyos and fef = toda adopted on every occurrence; ril = lansquenetes? flagged
- [x] retry: 23 Oct 2026 (r2o) - R9593 read sign by sign on line crops at 2-3.5x (decoded, not read, 0.614)
- [x] retry: 23 Oct 2026 (r2i) - R9635 tear read in the cipher of f. 20r; all 52 Sánchez records of R9593-R9657 fetched and every image opened; decipherments of R9613 (ff. 206-207) and R9641 (ff. 187-188, under R9642) found and read

## R9607 read in part, and the key measured on a held-out passage, 12 Nov 2026 (Brice Dudout)

DECODE lot 1 (R9594, R9607, R9616, R9617, R9626, R9631, R9632, R9633, R9636, R9639, R9651; 55 images) was triaged
(`dudout/TRIAGE_lot1.md`): R9616/R9617 are one letter in two copies, R9626 has its copy in R9627, DECODE serves R9632's
P2 twice (one opening missing), R9636 and R9651 are mixed with full clear passages, R9594 (= CSP 396) has a surviving
contemporary decipherment; only R9607 and R9633 are uncalendared. Before any decoding, a PREREG was frozen by SHA-256
with one measure on a held-out passage, R9632 f. 200r ll. 7-25 (386 tokens transcribed blind, R9632 used for no key
adjustment): this folder's key, unchanged, scores 593 decoded characters at -2.471 per character (4-gram, Don Quijote)
against 400 controls (permuted keys and token shuffles) with mean -3.106 and best -2.766, z = 5.68: PASS on the pre-set
thresholds (`dudout/protocol/`). R9607 (14 May 1522, 9/24 ff. 65r-67v, 146 cipher lines, no decipherment imaged) was then
transcribed blind by sign shape, frozen, decoded with the key unchanged and read by sense: 1,121 sure, 116 probable,
2 restored, 316 unresolved of 1,555 words = 79.5 %, read in part (`dudout/R9607_reading.md`, `_text_es.md`, `_en.md`):
Venice arming galleys after the French defeat, French soldiers from Milan at Padua, Cremona, Lautrec and Prospero
Colonna, Sánchez's demand that the Signoria declare itself released from its French capitulation, the Turk's fleet
reported from Corfu, the Hungarian ambassador's departure. Tomokiyo's printed opening line agrees. Most unresolved words
are spelled runs mis-transcribed on look-alike signs; 63 code groups absent from the key are listed there, none added.
For the gap list: R9607 moves from not-attempted to read in part; the other ten lot-1 records are triaged, not read.

## Lot 2 triaged, R9610 read in part, R9607 re-checked, 12 Nov 2026 (Brice Dudout)

DECODE lot 2 (17 records, 43 images) was triaged (`dudout/TRIAGE_lot2.md`): every Sánchez letter in it is uncalendared
and carries no imaged decipherment, except R9624, marked "triplicada", a third copy of the 7 Aug letter (R9626/R9627,
CSP 462); R9628 is a copy of R9629; R9612 is mixed with long clear passages; R9623 is dated in clear 7 [?] Aug (not
19 July) and calls itself a triplicate, and its last paragraph, given by Tomokiyo as decrypted, is in clear in the
letter; R9657 is not Sánchez but Lope Hurtado de Mendoza, in another cipher. R9606, R9637 and R9655 have no image
online. A second PREREG (`dudout/protocol/PREREG_lot2.md`) was frozen before decoding: key unchanged, nothing added, so
no new measure. R9610 (2 June 1522, 9/24 ff. 132r-134r, 130 cipher lines) was transcribed blind, frozen, decoded with
the key unchanged and read by sense: 691 sure, 211 probable, 2 restored, 233 unresolved of 1,137 words = 79.3 %, read
in part (`dudout/R9610_reading.md`, `_text_es.md`, `_en.md`); 96 of the unresolved read only after correcting a sign
label and are not counted. Content: 24,000 ducats sent by the Viceroy of Naples for Prospero Colonna through Venetian
lands with an escort from Verona, safe-conducts for the Viceroy, the King of France's letters from Lyon (he blames
Lautrec and sends the Admiral), Lautrec leaving for France, Cremona, the Turk's ambassador as a spy and the Turk arming
a hundred sails, the Turks before Knin. R9607's unresolved runs were re-checked by a rule frozen in that PREREG:
5 words accepted, 79.5 % -> 79.9 %, still read in part (`dudout/R9607_recheck.md`). Proposed codes, none added:
dud = vino, sod = govierno, lud = presente, cid = xxii. For the gap list: R9610 moves from not-attempted to read in part.
