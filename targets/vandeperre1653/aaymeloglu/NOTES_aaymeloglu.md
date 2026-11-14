# Vande Perre to de Bruyne, 1653: the Dutch cipher in Thurloe

**Alphabet recovered; five letters substantially read, two short fragments unresolved.**
Evidence reviewed 19 September 2026. The verified outbound inventory has **20 runs and 322
printed groups: 304 S, 5 C, 13 I** after the explicit repairs. These are token mapping grades,
not percentages of securely understood meaning: the unresolved strings also contain S letters.
No surviving key or target manuscript image has been located.

The cipher uses a 22-letter alphabetical substitution, printed groups read as *ee*, and word
codes. The alphabet was recovered from the digits without the English glosses; the glosses
support readings and supply five code meanings. These passages had already been read by the
contemporary translators. This work reconstructs their Dutch cipher text from Birch's print.

## The documents

**Paulus van de Perre**, Dutch ambassador in London, wrote to Johan de Bruyne (de Brune),
pensionary of Zeeland. Birch's index calls the envoy Paulus, as does the
[NNBW biography](https://www.dbnl.org/tekst/molh003nieu05_01/molh003nieu05_01_0674.php).
Thurloe's office intercepted the letters and translated the clear Dutch into English,
leaving sensitive ciphered phrases as numbers. Thomas Birch printed the translations in
*A Collection of the State Papers of John Thurloe*, vol. 1 (1742). Images below derive from
the [Internet Archive scan](https://archive.org/details/collectionofstat01thur), a public-domain
edition. They are not DECODE manuscript images.

| Runs | Printed page | Letter date |
|---|---|---|
| P431.1 | [431](https://archive.org/details/collectionofstat01thur/page/n460) | 29 August 1653 NS |
| P500.1–3 | [500](https://archive.org/details/collectionofstat01thur/page/n529) | 3 October 1653 NS |
| P522.1–5, P523.1–4 | [522](https://archive.org/details/collectionofstat01thur/page/n551), [523](https://archive.org/details/collectionofstat01thur/page/n552) | 10 October 1653 NS, dated at the conclusion on p. 523 |
| P576.1 | [576](https://archive.org/details/collectionofstat01thur/page/n605) | 4/14 November 1653; begins p. 575 |
| P582.1–6 | [582](https://archive.org/details/collectionofstat01thur/page/n611) | 11/21 November 1653 |

The longest run is 70 groups; most are one to five words. The inventory covers these verified
passages, not every possible cipher in the correspondence. British History Online omits the
numerical runs. The [reading page](https://aaymeloglu.github.io/unsolved-ciphers/vandeperre-reading.html)
shows source crops, mechanical output, Dutch and English for every run.

## The reading

[`reading.txt`](reading.txt) is generated from the unaltered printed groups in
[`transcription.txt`](transcription.txt), [`key.json`](key.json), and positional proposals in
[`repairs.json`](repairs.json). In the edited output, `[..]` marks I and `(..)` marks M.
English code labels in braces give meanings without claiming exact original Dutch wording.
Editorial supplements in the Dutch below are not silently inserted into the mechanical output.

| Runs | Reading or meaning |
|---|---|
| P431.1 | *ick segghe een cijffer*: I mean a cipher |
| P500.1 | *in een viandich land*: in a hostile country |
| P500.2 | *een redelijcke dispositie tot handelinge wert gespeurt, die wel diende waergenomen*: a reasonable disposition to negotiate is noticed, which ought to be taken up |
| P500.3 | *regeringe met impatientie op nader ordre van ons verwac[hten]*: the government await further orders from us with impatience |
| P522.1 | *de goede dispositie*: the good disposition |
| P522.2 | Literal `diemnicvndament`, unresolved; English gloss “who upon good grounds” |
| P522.3 | *wij gequalificeert eenige nadere propositie doen*: we [were] authorised to make some further proposal |
| P522.4 | Literal `tenprincipaln`; proposed *ten principal [e]n*, chiefly, and |
| P522.5 | *14 daghen*: fourteen days |
| P523.1 | 109: Major-General Harrison, glossed |
| P523.2 | Literal `ana?ptisten`; proposed *ana[ba]ptisten*, Anabaptists |
| P523.3 | 76: Denmark, glossed |
| P523.4 | 52: queen of Sweden, glossed |
| P576.1 | *ons tot voordeel gerekent*: reckoned to our advantage |
| P582.1–2 | *thien schepen* / *[Jarmuyen] geloopen*: ten ships / [at Yarmouth] run [away] |
| P582.3 | *bewaren*: to guard |
| P582.4 | Literal `ote`, unresolved |
| P582.5–6 | *gebreck* van *masten* bevonden: want of masts found (van and bevonden in clear) |

The 10 October letter says Harrison and the Anabaptists are losing influence. Colonel Wurts
presents himself as Denmark's envoy while receiving a pension from Sweden's queen. These
meanings come from the historical glosses, not a first discovery of the events.

## Key and repairs

| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | frac | 12 | 13 | 14 | 15 | 17 | 21 | 22 | 23 | 24 | 26 | 27 | 28 | 29 | 77 |
|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| a | b | c | d | e | f | g | h | ij | i | k | l | m | n | o | p | q | r | s | t | v | w | ee |

`frac` denotes Birch's fraction-like sort, read as *ij*. Printed **77** reads *ee* in
*gequalificeert* and *een cijffer*; an intentional digraph and joined **7.7** are both possible.
**57** is inferred as *ee* in *in een viandich land* (I).

The five C groups are **617**, article *de* or *die*; **115**, Yarmouth (the spelling *Jarmuyen*
is supplied); **109**, Major-General Harrison; **76**, Denmark; **52**, queen of Sweden.
**43** remains M in the key. Its positional I reading *ba* gives *anabaptisten* and agrees with
the gloss. Splitting **4.3** gives *ba* under the established alphabet; a syllable code is an
alternative. **43=b** would produce *anabptisten* and is not adopted.

Every repair is separately recorded with its reason. These include 14 (*l*) for *t* in both
instances of *dispositie*; 17 (*n*) for *u* in *gespeurt* and *gequalificeert*; 15 for 5 (*c*);
71 for 7 (*e*); 27 (*t*) for *n* in *ons* and for *s* in *schepen*; a dropped 7 in final 17
(*geloopen*); and 3 (*a*) for *ij* in *cijffer*. The first 14 of *14 daghen* is read as the
clear numeral, supported by the gloss. The print alone does not locate these defects in the
writer's cipher, interception copy, translation, or typesetting.

No distinct *u* symbol is established: 28 reads *v*, and 17 occurs where *u* is needed.
Sharing a symbol and confusion with an unprinted 16 remain possibilities.

## Method and what the controls say

The alphabet was found on 14 September 2026 by bijective simulated annealing over a 4-gram
model built from Hooft's *Nederlandsche Historien* (1642, DBNL `hoof001nede01`, not included).
Four of eight restarts converged on the same key; remaining values were read by hand.
English glosses were checked afterwards and supply the C values.

The reproducible check uses `cipherkit.corpora` id `nl`: Vondel, *Complete werken* I, and
Multatuli, *Max Havelaar*, cleaned with the repository's versioned cleaner. Fetch with
`python3 -m cipherkit.corpora fetch nl` before running the optional statistical experiments.

- `python3 vande-perre-1653/verify.py --z`: dictionary-segmentation key shuffle on all **322
  printed groups**, without repairs: **z = 18.0, p = 0.001**, 1,000 shuffles, seed 0. All non-S
  symbols are fixed boundaries. Multi-letter *ij* and *ee* are also held fixed; the 21
  single-letter S values are permuted. This is a conditional comparison against random
  relabellings, not a search-adjusted significance test or the probability that the reading
  is correct. The observed score, null mean and standard deviation are retained in
  [`evidence-audit/control-result.txt`](evidence-audit/control-result.txt).
- `python3 vande-perre-1653/solve.py`: ciphertext-only annealing and hill-climbing, default
  16 seeds, on the **archived 308-group discovery corpus**. The reported best seeds recover
  17–18 of 22 letter values (about 92% of letter tokens), confusing v/w and c/k/z. The
  reported key score is −1369.2, above the best search result −1377.5. This experiment is
  scoped to the archived corpus and is not presented as a fresh 322-group search.

The [source-review audit](further-review/README.md) preserves the discovery transcription,
key and repairs. Its `verify_review.py` reproduces the inventory extension and exact repair
costs. It is an audit snapshot, not a second current key.

## Unresolved readings

- **P522.2 `diemnicvndament`**: conjectural *die met fvndament* requires **three consecutive
  substitutions**, positions 5–7: 17→7 (*n→e*), 12→27 (*i→t*), 5→8 (*c→f*). Normalizing *v/u*
  is separate. The English gloss supports the sense but does not establish this wording.
- **P582.4 `ote`**: possibly a retained Dutch ending, *[vl]ote* or *[vlo]ote*, immediately
  after English “fleet”. The paragraph also mixes translated English with retained Dutch
  *bewaren* and *gebreck van masten bevonden*. No proposed prefix is encoded; unresolved.
- **P522.4 `tenprincipaln`**: *ten principal [e]n* requires an inserted *e*. The glosses do
  not fix the word boundary or establish that exact restoration.

## Manuscript evidence and next steps

**Bodleian MS. Rawl. A.7, old p. 47**, Van de Perre to Bruyne, **17 October 1653**, is explicitly
catalogued as a copy partly in Dutch and partly in cipher, omitted from Birch:
[item record](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820123),
[Macray col. 12, item 4](https://archive.org/details/CatalogiCodicumManuscriptorumBiblioth/page/n13/mode/1up).
Its digits have not been seen; neither calendar style nor use of this key is verified.
This is the strongest next retrieval target.

Two verified Zeeuws Archief entries offer recipient-side evidence: access 2, inventory
[3188](https://hdl.handle.net/21.12113/7EE8C3AD46AB40FC882D10532E14648A), De Brune's incoming
letters 1652–1658, and [3101.1](https://hdl.handle.net/21.12113/22565F7402054D48A6003DDC0EFA75F3),
England correspondence 1652–1656, explicitly including copies returned by the surviving
envoys after Van de Perre's death. Both public manifests had empty `items` on 19 September
2026. Their internal contents and any cipher enclosure are unverified.

The key-dispatch trail runs through 29 August (Birch 431), 5 September (442), De Bruyne's
27 September note (Macray A.6 p. 293), and the 3 October receipt/seal discussion (Birch 500).
It does not identify a surviving alphabet or code list. For the damaged October passage,
Birch literally prints **Vol. X p. 471**, but A.10 mainly covers December 1653–February 1654.
Other 10 October letters at A.6 pp. 463 and 474 make **A.6 p. 471** a plausible alternative,
not a verified correction. The November passage points to A.8 old p. 102.

De Bruyne's reverse letter of **31 October 1653 NS**, [Birch p. 552](https://archive.org/details/collectionofstat01thur/page/n581/mode/1up),
contains **118**, likely a code group but without a resolving gloss or demonstrated key.
It remains separate from the 322 outbound groups. Nearby De Witt groups are not imported.

The [evidence audit](evidence-audit/README.md) records the Birch OCR screen, all 152 retrieved
Colenbrander pages, targeted *First Dutch War* searches, catalogue evidence, source hashes
and limitations. The 1725 embassy *Verbael* remains incompletely inspected. No alternate
text resolving the damaged phrases has been identified. The
[retrieval specification](evidence-audit/ARCHIVAL-TARGETS.md) lists exact targets and reference
warnings. No archive enquiry or order has been sent.

## Other cipher and source-list scope

Satoshi Tomokiyo's [unsolved list](https://cryptiana.web.fc2.com/code/unsolved.htm) names the
Beverning and Vande Perre letter to Boreel, 1 September 1653 (Birch p. 435). It uses a different
system: letters 6–33, codes 113–527. Its 128-letter attack scored about −650 against a
calibrated Dutch band −614 to −554; recorded closed-negative 14 September 2026. It needs
more same-key text or a Dutch-side crib and is not solved by this alphabet.
[Bourdeau's Thurloe work](https://github.com/dbourdeau/cyphersolver/tree/main/thurloe) concerns
that letter and three 1656 intercepts. DECODE searches on 19 September 2026 for Perre, Bruyne,
Bruijne, Beverning, Nieupoort, Zeeland and Thurloe found no matching record.
