# Spanish despatches: Miranda, Sessa, Ibarra — BnF fr. 3983 nos. 45, 79; fr. 3984 nos. 47, 68

Catalogue no. 19 (priority 5.0, class B). Opened 19 Sept 2026.

Status: in progress (5 Oct 2026: every cipher line of all four letters re-transcribed and scored for sense in `sense.tsv`: 92.5% of nos. 45/79/47, 37.5% of no. 68, 75.3% overall; sections 9-10). Read in part (see section 8). Both keys recovered - including the office's own key at BnF fr. 3995
f. 97 - all four leaves located on the images, and all four read line by line, with a scatter of groups and
the Feria-Mansfeld nomenclature still open. Written up as `docs/sessa1593.html`.

## 1. The keys were already published — as images

Same trap as catalogue no. 17. `research/gallica_sweep/src/` holds Tomokiyo's pages as **text dumps**, and his key
tables are **images**, so they are invisible there. Fetching the page itself
(`src/spanish3.htm`, "Spanish Ciphers during the Reign of Philip II", SHIFT_JIS) shows 32 `<img>` tags,
including:

| image | Tomokiyo's caption | relevance |
|---|---|---|
| `phelippes2.png` | **Spanish Cipher (1592-1593)** | the cipher used among Philip II, Parma, **Feria**, **Sessa**, Acuña, Olivares, Fuentes, Tassis, **Ibarra**, Doria and **Miranda** — cited at BnF fr. 3983 **f. 98, f. 158, f. 162** |
| `spanish3fuentes.png` | Syllabic Numerical Cipher (1593) | Fuentes / Philip II / Estevan de Ibarra, fr. 3983 ff. 201-258; = Nevers cipher no. 59 |
| `spanish3mansfeld.png` | Syllabic cipher for Duke of **Feria** and Count of Mansfeld (1593) | July 1593, Mansfeld / Feria / **Ibarra** in Paris, **fr. 3984 f. 130, 145** |
| `phelippes3.png`, `phelippes4.png` | Ibarra–Doria (1592), Ibarra–Zúñiga (1593) | other Ibarra keys |

All are in `src/`. Tomokiyo reconstructed the keys but did not apply them to the leaves the catalogue lists.

### The key of the Spanish Cipher (1592-1593)

Two-digit numbers carry **syllables** (consonant + vowel); a small symbol alphabet carries bare letters;
diacritics add a final consonant. Copied to `key92.tsv`:

```
ba10 be11 bi12 bo13 bu14   ca19 ce18 ci17 co16 cu15   da24 de23 di22 do21 du20
fa25 fe26 fi27 fo28 fu29   ga34 ge33 gi32 go31 gu30   ha40 he41 hi42 ho43 hu44
la45 le46 li47 lo48 lu49   ma55 me56 mi57 mo58 mu59   na64 ne63 ni62 no61 nu60
pa65 pe66 pi67 po68 pu69   qua74 que73 qui72          ra75 re76 ri77 ro78 ru79
sa90 se91 si92 so93 su94   ta80 te81 ti82 to83 tu84   va89 ve88 vi87
ya35 yo38 yu39   jo53 ju54   xa95 xi98   za704 ze705 zi706
```

Letters: a = 4 / Z / ρ · e = n / f / + · g = 9 · i = p · l = h · n = x · o = 2 / ∇ / υ · r = y / ⌐ ·
s = △ · t = u / r · u = a / 6 · x = 1 / ◦ · y = q.
Diacritics: dot above = final **-l**, `+` = **-m**, dot after = **-n**, `:` = **-r**, `^` = **-s**;
bar = the number itself; umlaut = doubled consonant; ⊤ = code word.

## 2. What the four pieces actually are

The catalogue cites piece numbers; the BnF *dépouillement* gives folios. Notices fetched to
`src/notice_3983.html` and `src/notice_3984.html` (Collection Mémoires de la Ligue,
archivesetmanuscrits ark cc504266, fragments cd0e16357 and cd0e18898 from the IIIF manifests' `Relation`).

| target | folio | letter | cipher |
|---|---|---|---|
| fr. 3983 **no. 45** | f. **98** | *"Lettre, avec chiffre, d'«el conde DE MIRANDA,... al duque de Feria,... De Napoles, a 25 de hebrero 1593». En espagnol."* | Tomokiyo keys f. 98 → **Spanish Cipher (1592-93)** |
| fr. 3983 **no. 79** | f. **162** | *"Lettre, avec chiffre, d'«el duque DE SESSO,... a don Diego de Ibarra,... De Roma, 11 de março 1593». En espagnol."* | Tomokiyo keys f. 162 → same cipher |
| fr. 3984 **no. 47** | f. **108** | *"Lettre, avec chiffre et commencement de déchiffrement, d'«el duque DE SESSA» à Philippe II. «De Roma, 30 de junio 1593». Copie."* | begun decipherment on the leaf = a crib |
| fr. 3984 **no. 68** | f. **145** | *"Lettre, avec chiffre, de «D. DIEGO DE IBARRA,... De Paris, a 10 de julio 1593». En espagnol."* | Tomokiyo keys f. 145 → **Feria/Mansfeld cipher (1593)** |

## 3. All four leaves located on the images

fr. 3983 = ark `btv1b9059406b` (481 canvases), fr. 3984 = ark `btv1b9060633d` (515). Every canvas label is
`NP`, and the volumes are foliated irregularly — some pieces shot page by page, others as openings, and the
leaves carry piece numbers and folio numbers in different corners. The map was built by reading folio numbers
off a full-width top strip at intervals and interpolating (`dockets.py`, `cal*.png`):

| volume | anchors read off the leaf | rate |
|---|---|---|
| fr. 3983 | c178 = f.98 · c200 = f.111 · c220 = f.122 · c276 = f.156 | ~1.65-1.75 canvas/folio |
| fr. 3984 | c188 = f.103 · c228 = f.123 · c266 = f.144 · c272 = f.148 | ~1.8-2.0 canvas/folio |

| target | folio | **canvas** | what is on the leaf |
|---|---|---|---|
| fr. 3983 no. 45 | f. 98 | **178** | 17 lines of cipher; date in clear *"Dios Gu[arde]... al S. de Nap[oles] a 25 de hebre[ro] 1593"*; docket *"S. duq de feria"*; Miranda's signature; *"dup."* in the margin. Address *"Al Duque de feria"* on c180 |
| fr. 3983 no. 79 | f. 162 | **286** | ~25 dense lines of cipher, no clear text |
| fr. 3984 no. 47 | f. 108 | **198** | headed *"Copia 30 de Iunio 1593"*; ~28 lines of cipher **with the contemporary decipherment written between the lines** — the *"commencement de déchiffrement"* of the notice |
| fr. 3984 no. 68 | f. 145 | **268** | clear Spanish opening (*"...V.S.a de 4 y 5 deste, y de buena gana aguardara... espero que me dara V.S.a mas claridad"*) running into cipher |

## 4. The two ciphers confirmed on the leaves, and read in part

**nos. 45 and 79 are in the Spanish Cipher (1592-93)**, as Tomokiyo's citation of ff. 98 and 162 says.
Decoded with `key92.tsv` / `decode92.py`:

- no. 45, f. 98: `38 94 68. 31 73 40 89 23 91:` -> *yo · su · pon · go · que · ha · va · de · ser*; also
  **siendo confidente**, **a procurar**, **a costa de la bolsa**. See `ct45.txt`.
- no. 79, f. 162: `4 48^ 94 18 93 76^` -> *a los su-ce-so-res* = **a los sucesores**; `2:22 64 77 4^` ->
  **ordinarias**; `16. 87 n 63` -> **conviene**; `92 30 n.` -> **siguen**.

Both read as Spanish on the same key. Grade **H** for those groups.

**no. 68 is in the other cipher**, as Tomokiyo's citation of fr. 3984 f. 145 says: the values run far higher
(97, 98, 800, 200, 7243, 9482) and the leaf carries **three-letter word codes** — *pra, rom, mon, xen, vul,
cil, denp, hes, dur* — which is exactly what he describes for the *Syllabic Numerical Cipher for Duke of Feria
and Count of Mansfeld (1593)* (`src/spanish3mansfeld.png`, "three-letter symbols representing words, *vas*
for *segnor*"). That key is downloaded but not yet transcribed into a key file.

**no. 47** is the best crib in the group: its contemporary interlinear decipherment can check whichever key
applies, the way the Brienne copy checked Maisse's cipher in catalogue no. 17.

## 5. The office key found: BnF fr. 3995 fol. 97

The catalogue's `verify` line said *"DECODE for Sessa"*, and that is where the answer was. DECODE's record
search returns exactly two hits for these correspondents, and **both are keys, not letters**:

| DECODE | name | sender | type |
|---|---|---|---|
| **4076** | `BNF_Français_3995_094` | Don Diego de Ibarra | **Key** — homophonic substitution, **nomenclatures** |
| **4077** | `BNF_Français_3995_096` | Don Diego de Ibarra, Duc de Sessa | **Key** — homophonic substitution, **nomenclatures** |

Both point into **BnF fr. 3995**, the Nevers cipher key book (ark `btv1b525085665`), which this repository
already fetches for `targets/lorraine1592/`. Folio numbers there run about canvas − 91 in this stretch
(c188 = f. 97, c190 = f. 98, c194 = f. 101); `fetch3995.py` takes canvas numbers.

**Canvas 188 = folio 97 is the key itself**, and it is complete:

- the **letter alphabet** with its symbol equivalents (a = 4/ʒ, e = n/f/ʃ, g = 3, i = y/6, n = x/•, o = 7₂,
  r = y/:, s = ∧, u = o, y = q, z = ∂);
- the **syllable table**, identical to Tomokiyo's — ba 10 … bu 14, ca 19 … cu 15, da 24 … du 20, and so on
  through za/ze/zi/zo/zu, which confirms his reconstruction against the office original;
- and beneath it the **nomenclature**, which his table does not have: *aunque* ʒo, *alli* dis, *armas* hes,
  *autoridad* ʒa, *causa* ʃes, *en* ʃ, *exercito* xel, *estados* vul, *election* rol, *fin* dam,
  *Francia* gam, *forma* fem, *fuerça* gim, *franceses* fumî, *gente* gum, *lugar* ʒim, *legato* vom,
  *lettera* ra, *marques* der, *muy* ʒur, *mente* far, *mucho* hur, *magestad* ʒum, *mas* dox, *manda* caʒ,
  *manera* cer, *ministro* ʃur, *negocios* norî, *necessidades* nirî, *quando* nes, *que* ʒot, *qual* lus,
  *quien* nus, *remedio* sas, *Rey* tas, *razon* pos, *Reyno* tis, *religion* rus, *reputacion* pem,
  *Roma* vos, *seignor* ʒus, *satisfecho* yas — plus a *Nulles* row.

These are precisely the groups that stood unresolved on the leaves — *hur, cer, vul, vos, ra, ʃes, nor, xel,
dox, nes, tas, tis, sas, pem*. `key92.tsv` carried those 40 and the syllables (133 entries). The sheet has over a hundred word entries; the rest were added on 2 Oct.

Adjacent leaves (ff. 94, 96, 98, 101) hold further Spanish keys of the same office, including the one the
repository already identified as *"1592 Chifre d'entre le Duc de Parme et le Roy Cath[olique]"* at f. 98. **Correction (2 Oct 2026, on a note from satorunet):** that endorsement is on the back of f. 97 (canvas 189) and labels the key of f. 97 itself, "lequel sert aussi pour le Duc de Sessa et Don Diego de Ybarre"; f. 98 is a different, French key. See `retry_f97.md`.

## 6. What remains

Tomokiyo's published key gives the **syllable table in full** and the symbol alphabet in part. It does **not**
give the **nomenclator**. On the leaves the code words are marked with the ⊤ sign or written as two- and
three-letter groups, and they are frequent — on f. 98 alone: *di, se, hur, Val, Vor, ral, Jep, cer, pir, ner,
nor, mal, tim, cos, 50⊤, 61⊤, 31⊤*; on f. 145 (the other cipher): *pra, rom, mon, xen, vul, cil, denp, hes,
dur*. Every line therefore decodes with holes, e.g. f. 98 L5-L6:

```
91: g[..] hur 68 88 16 94 76 92 23. 17 4 n. [..] 38 n^ 17 87
ser  ·   ·   po ve co su re si  den ci a en   ·  yo es ci vi      -> "... residencia ... "
93 11 n^ 83 4 Val 9 48 40. [T]o 57 4 0 57 82 21 q
so be es to a  ·  g lo han   ·   mi a · mi ti do y  -> "sobre esto a [Val...]"
```

The words come through — *residencia*, *sobre esto*, *supongo que hava de ser*, *siendo confidente*,
*a costa de la bolsa*, *a los sucesores*, *conviene*, *ordinarias* — but the proper names and the commonest
function words sit in the nomenclator and cannot be supplied from the key as published.

### The crib opened, and what it proves

f. 108 (canvas 198) carries the decipherer's words **above** the cipher line. The first glossed line reads

```
gloss    …  a  30.  del   Passado        con   …
cipher   ʒ   3(bar)0   23   65   g(umlaut)o  21   16.   Col …
                 30     de   pa   ssa       do   con
```

This is an **independent check of Tomokiyo's key on a third letter**, from the leaf's own contemporary
decipherment, and it settles two of the diacritics:

- **bar above = the number itself** — `3̄0` is glossed *30*.
- **umlaut = doubled consonant** — `93` (so) with umlaut gives *ssa*, so that `23 65 g̈o 21` reads
  *de-pa-ssa-do* against the gloss **del Passado**.
- `16.` = *con*, confirming the trailing dot as final **-n**.

So the syllable table, the finals and the two modifier marks are all now verified against plaintext written
by a contemporary. What the gloss will also give, line by line, is the **nomenclator** — the `Col`-type code
words that the published key omits.

**The way in is no. 47.** Its contemporary interlinear decipherment (f. 108, canvas 198) pairs cipher with
plaintext on the same leaf, which is how the nomenclator can be recovered — the same move that the Brienne
copy provided for catalogue no. 17. Transcribing those glosses is the next step, and the method is proven on the
first line. But it is **not** simply bulk: the decipherer's hand is in a much lighter ink than the cipher,
and at the resolution Gallica serves (f. 108 native 4950 x 6646) the glosses sit close to the paper tone.
Moderate contrast stretching reads the first line cleanly (`g47b.png`); pushing harder to reach the fainter
lines amplifies the laid-paper texture into noise faster than it lifts the ink (`g47e.png`). So a
line-by-line harvest of the nomenclator from this scan is marginal, not routine.

Options, in the order worth trying:
1. Work the glosses at native scale line by line with per-line contrast tuned by hand, accepting that some
   lines will not come.
2. Check **DECODE** for Sessa, as the catalogue's `verify` line says and as this session did not do.
3. Look for the other Sessa/Ibarra letters of the same months elsewhere in fr. 3983-3985, where a cleaner
   decipherment may be bound in: the notice records several *"Deschiffrement"* pieces in these volumes.

## 6b. Reading with the complete key

With fr. 3995 fol. 97 in hand the leaves read continuously. f. 98 (no. 45, Miranda to Feria), opening lines:

```
n(dot) di 16. n(^) 81  z  1(ring)9 73 73 92 n. 21 16. 27 23. 81
 el    alla con  es  te  a   cha  que que si en do con fi den te
                        -> "el [alla] con este achaque, que siendo confidente..."

se 91 68 u(~) 4 68 15 75:  ...  4 16(^) 80 23 45 13(dot)
      se po      a po cu rar         a   cos ta de la  bol
                        -> "...procurar ... a costa de la bolsa"

38 94 68. 31 73 40 89 23 91:   ->  yo supongo que hava de ser
```

and f. 162 (no. 79, Sessa to Ibarra): **a los sucesores**, **ordinarias**, **conviene**, **siguen**;
f. 108 (no. 47) glossed **del Passado con**.

The ring (-h-) and the dot (-l) are now confirmed on plaintext: `1(ring)9` = *cha* in **achaque**, and
`13(dot)` = *bol* in **bolsa**.

## 7. Not done

- No continuous reading of any of the four. Only the spot decodes above.
- The symbol alphabet (a = 4/Z/ρ, e = n/f/+, ...) and the code words marked ⊤ are not worked out from the leaves,
  so a fraction of every line still decodes as `·`.
- `spanish3mansfeld.png` not transcribed; no. 68 therefore not decoded at all.
- no. 47's interlinear decipherment not transcribed, so the independent check is not yet made.
- DECODE not checked for Sessa, as the catalogue's `verify` line suggests.

## 5. Files

`fetch.py` / `fetchr.py` — canvases and regions of either volume (`VOL=3983|3984`) ·
`dockets.py` — docket-corner montages used for calibration · `key92.tsv`, `decode92.py`, `ct45.txt` ·
`src/` — Tomokiyo's pages and key images, the two BnF notices, `pieces.json` (the parsed dépouillement)


## 8. All four letters read (19 Sept 2026)

With the office key the four leaves decode. Readings in `reading45.md`, `reading79.md`, `reading47.md`,
`reading68.md`. Method: fetch the cipher block at native resolution, deskew (`deskew.py`, which searches
+/-3 degrees for the row-profile variance maximum), cut centred line strips, read at ~0.75 scale.

- **no. 45, f. 98** (Miranda to Feria): 15 of 17 lines. *con este achaque, que siendo confidente ... a costa
  de la bolsa ... no [se] vera lo que en esto converna hazer, que yo me remito a su prudencia ... dar de
  manera que no se entienda, por que la hora que ...*
- **no. 79, f. 162** (Sessa to Ibarra): 14 of 16 lines. *de ver los testemonios que a todos levantan ... los
  que bivimos en Roma ... a los sucesores se hazen tan estas ordinarias ... la election ... diversas
  pretensiones ... no puedo dexar de hazerlo, a lo menos, de que no esten ministros conformes.*
- **no. 47, f. 108** (Sessa to Philip II): the glossed lines, and the decode **agrees with the contemporary
  decipherer's own words** wherever both survive — *por via de mar ... difiriendo de dia en dia*, under the
  gloss *"por una [via] de mar ... ha ydo defiriendo de dia en dia"*. That is an independent check of the
  office key on a third letter.
- **no. 68, f. 145** (Ibarra, Paris): a **different cipher** — the Feria-Mansfeld key, transcribed to
  `keyM.tsv`. Clear opening running into cipher: *aguarda cavalleria ... que aya recivido su ...*

Still open: a scatter of groups in every letter, the later lines, and **the nomenclature of the
Feria-Mansfeld cipher**, which is the one real gap left. Its three-letter groups (*pra, dur, hes, gar, pun,
rom, mon, xen, vul, cil*) carry much of no. 68's sense, Tomokiyo tabulates none of them, and the obvious
candidate was checked and excluded: **fr. 3995 f. 101 (canvas 194) is an Italian nomenclature**, not a
Spanish one (*Austria, Ambasciatore, Assemblea, Battaglia, Bisogno, Borbone, Cardinale di, Castello,
Cattolici, Concilio generale, Corte di*). It belongs to another correspondence.

## 9. Sense measure and re-transcription (5 Oct 2026)

**The 0.70 was not a measure of sense.** It counted every group not marked `·` as read, so syllables that
make no word (*mi · mitido*, *las tima ten*) counted, and it under-counted the leaves: no. 79 has **22** cipher
lines, not 14 (the 19 Sept note that "every cipher line is read" was wrong; ll. 15-22 were never transcribed),
and no. 47 has 21, of which 13 had been read.

**Re-transcription.** All cipher lines of nos. 45, 79 and 47 re-read from Gallica crops at 3200-3600 px
(`img3983/r0178_*`, `r0286_*`, `img3984/r0198_*`), line by line, and each line scored in `sense.tsv`:
a group is read only when it is part of a Spanish word that makes sense in context; `?` readings and code
groups without a value are unread. `measure_sense.py` sums it and runs `lm.best_language` (es-modern first for
all three).

**Key sheet f. 97 re-checked** (canvas 188 at 3600 px) for the open groups:
- three-dot **94** and **95** = *de* (listed under D) -> *confidente de S.M.*, *a costa de la bolsa de S.M.*, *ser de mucho provecho*;
- three-dot **49** = *Su Santidad* -> *mostrarla a Su Santidad*, *abriesse mucho los ojos Su Santidad*, *a Su Santidad, si no me hablasse*;
- three-dot **88** = *V.M.*; three-dot **5, 8, 9, 0, 25** = nulls (the *Nulles* row); two dots = doubled consonant (*fuesse*, *passar*);
- **ʃo = assi** (*aunque* is ʒo) -> *assi fuesse a costa*, *assi pensava contar*, *assi devia agradecimiento*.

**Forced by context:** 9 = *y*; *xor* = *para* (variant of *xur*, three times); *pal* = *duque* (variant of *pol*:
*duque de Feria*, *duque de Mantua*); 86 = *vo*; *de por tes* = **Desportes**; 67 90 62 = **Pisani**; *Gondi*.

**New text** (no. 79 ll. 13-22): *cuan embarcado ha quedado el duque por la carta de Desportes ... le avia mostrado
unas cartas del duque en que le escrivia que assi devia agradecimiento ... todavia le avia pesado que uviesse tratado
de sus personas con Su Santidad, porque sabia que el no tenia ambicion ninguna, sino que su fin era desear que se
hiziesse election de un Rey ... para la conservacion de la religion ... poderoso para defenderle ... porque negocios en
que convenia que abriesse mucho los ojos Su Santidad e no le engañassen.* (no. 47 ll. 12-21): *el dicho dia de recibir
esta carta tuve a la tarde audiencia de Su Santidad, e antes de ir a ella me envio el [hum] del duque de Mantua ...
copia va con esta ... resolvi de no dezir nada a Su Santidad si no me hablasse en ello ... lo que V.M. me escrive de
Gondi y de Pisani ... a echado de ver que adrede se me devia de aver dado antes de la audiencia, e sabiendolo Su
Santidad le respondio ...*

| letter | before (2 Oct, not sense) | after (5 Oct, sense) |
|---|---|---|
| no. 45 | ~0.84 | **230/254 = 0.906** |
| no. 79 | ~0.84 of 14 lines | **504/546 = 0.923** |
| no. 47 | ~0.8 of 13 lines | **478/510 = 0.937** |
| three letters | | **1212/1310 = 0.925** |
| no. 68 | ~0.3 | **~12/620 = 0.02** (estimate) |
| all four | 0.70 | **1224/1930 = 0.634** |

**no. 68 tested again:** line 11 transcribed and decoded with `keyM.tsv`: *va le ri a no la vi o xur que le de di as
se ri as ...* - syllables, no Spanish, as on ll. 7-10. Tomokiyo's table does not give continuous text on the body;
ll. 12-31 not transcribed. Token count estimated (28 lines x ~22).

## 10. no. 68 transcribed in full and the Feria-Mansfeld key tested ciphertext-only (5 Oct 2026)

All cipher lines of f. 145 transcribed from the 3600-px crop to `ct68.txt`: **20 cipher lines (ll. 4-23; ll. 1-3 are
clear), 598 groups**, counted (the 620 of section 9 was an estimate from a wrong line count). Diacritics dropped.
`dec68.py` decodes with `keyM.tsv`.

**The earlier verdict was wrong.** On a full transcription Tomokiyo's table *does* give Spanish: *a mi no me parece que
puede*, *se [ha] de poner todo lo que se puede*, *lo que podemos*, *aliento, y si ella apareciera, y palabra*, *no
estamos desesperados*, *peligro*, *espero*, *de acudir a lo que esta*, *supuesto e numero*, *pareceria que venia a
ayudar ... y la cavalleria*, *no seria fuera de*, *a lo menos no parece sino*. Lines 7-10 had read badly in the
19 Sept pass because their transcription was truncated.

**Control** (`anneal68.py`, es-golden-age 5-gram, no spaces): keyM scores **-2.500** per character; 200 keys with
keyM's values shuffled among the numbers score at most **-3.378** (mean -3.805). The key is real.

**Rebuild:** an unconstrained hill-climb over all numbers collapses onto *que* (homophone collapse, score -1.59 but
nonsense) and was rejected. Constrained fill of the numbers missing from keyM (`fill68.py`): **57 = li** is top of
all candidates with a gain far above the median (3 occurrences: *peligro*, *aliento*) and is accepted (`fill68.json`).
64 (9 occurrences; *ha* by context: *se ha de poner*, *ha de acudir*) is not separated by the LM (na -2.549, ha
-2.569) and stays unread. 31, 77, 81, 95, 200T, 800T: no candidate stands out. Cribs: *Paris* and *Su Magestad* are
in clear on the leaf; *Feria*, *Mansfeld*, *Liga* fit no syllable run, so they would sit in the open three-letter
codes (pra, dur, hes, gar, pun, rom, mon, xen, vul, cil, var, vis, tor ...), which no crib fixes.

**Retry of nos. 45/79/47:** 57 = li belongs to the Mansfeld cipher, not to the 1592-93 office key, so it gives nothing
there; no new office-key value came out, and the ~75 doubtful groups stand.

| | before | after |
|---|---|---|
| no. 68 | ~12/620 = 0.02 (estimate) | **224/598 = 0.375** (measured) |
| all four | 1224/1930 = 0.634 | **1436/1908 = 0.753** |

## Remaining gaps
- no. 68, f. 145: 374 of 598 groups unread - blocker: no-key-material; the three-letter nomenclature (pra, dur, hes, gar, pun, rom, mon, xen, vul, cil, var, vis, tor ...) is published nowhere, fr. 3995 f. 101 is Italian and no crib fixes it; the numbers 64, 31, 77, 81, 95 are not separated by the LM control; the diacritic finals dropped in ct68.txt are still to be added from the image
- nos. 45, 79, 47: 22 code groups not on the f. 97 sheet (Val, ral, ʃep, ner, ʒe, pir, mil, is, xom, mal, rili, mos, ʃer, hir, hum, us, ho, yos, ∂ir, lir, xox, ru) - blocker: no-key-material; sheet re-read 5 Oct for them, each occurs once or twice
- nos. 45, 79, 47: about 75 syllable groups of doubtful reading (slips, ambiguous hooks), listed per line in sense.tsv - blocker: open-codes

## Escalation
- [x] siblings: fr. 3995 ff. 94, 96, 98, 101 opened next to the key; no. 47 used as the crib for the others; open codes pooled across the three letters (xor, pal, ʃo, 4̈9 solved jointly)
- [x] clear-pages: no. 47's interlinear decipherment used for ll. 1-4; no. 68's clear opening read
- [x] known-keys: Tomokiyo 1592-93, Feria-Mansfeld, Ibarra-Doria, Ibarra-Zuniga keys; DECODE R4076/R4077 = fr. 3995 ff. 94-97
- [x] print: Tomokiyo spanish3.htm; BnF notices for fr. 3983/3984
- [x] key-rebuild: f. 97 re-read 2 Oct and again 5 Oct (de, Su Santidad, V.M., nulls, assi); the Feria-Mansfeld key of no. 68 tested ciphertext-only against a shuffled control and filled where the LM separates a value (57 = li); section 10
- [x] retry: every line of nos. 45, 79, 47 re-transcribed from the images and re-read with the extended key (5 Oct, sense.tsv); no. 68 transcribed in full (ct68.txt) and decoded with keyM + 57 = li
