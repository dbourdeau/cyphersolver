# The Indus script: a structural analysis with checkable claims

Daniel Bourdeau, with Claude (Anthropic), September 2026. Working notes: `NOTES.md`; code and results in this folder.

## What this is, and what it is not

This is **not a phonetic decipherment**. No sign has a sound value that the evidence forces, and no published key
survives the tests set out below. It is a structural analysis of the kind that preceded the decipherment of
Linear B (Kober's grids before Ventris's values): a sign list, rules of combination, fixed meanings where the
material fixes them, constraints on the language, and a public test that any proposed decipherment can be run
through. Every number below is produced by a script in this folder and replicated, where marked, on an independent
sample (1,664 texts of Mahadevan's 1977 concordance that the main corpus lacks).

The prize announced by the Government of Tamil Nadu (January 2025) asks for a decipherment to the satisfaction of
experts. Commentators on it name readings that hold across hundreds of inscriptions, full sign lists, rules of
combination, worked readings others can check, and validation on unseen inscriptions. This dossier provides the
sign list, the rules and the validation framework; it does not provide readings, and says why none can yet be
validated.

## 1. Corpus

- ICIT-derived dump (indus-website): 2,543 objects, 10,253 tokens in lines of 3+ signs, 538 sign types; reading
  order established (texts stored left-to-right are mirrored; `build_corpus.py`).
- Mahadevan 1977 (M77): 2,906 texts, mapped to ICIT ids by aligning the texts both share (96% of lines agree,
  `align_m77.py`); 1,664 texts absent from the dump are used as a held-out sample (`merge_m77.py`).
- CISI vol. 1 photographs for checks; Parpola 1994 for the copper-tablet groups.

## 2. Sign list

`results/sign_list.tsv`: 252 signs with 5+ tokens (96.8% of all tokens), each with position profile, neighbours,
the ending its names take, numeral value, Fairservis's identification of the drawing, anchors and role. Roles by
share of tokens: heading signs 4.2%, endings 17.3%, stroke numerals 16.4%, name-final signs of the 520 class 8.7%,
of the 740 class 20.9%, other 29.3%. The list is not over-split: signs that look alike are four times likelier than
chance to be used alike, but merging every such pair reduces 223 common signs only to 180 (`allographs.py`).

## 3. Rules of combination (all replicated on the held-out M77 texts)

1. **Heading.** 817 / 820 / 861 + a stroke pair (or 60, or one stroke), on 12% of texts; a single formula with
   regional and genre variants (the choice of opener goes with site and object type, not with the name after it).
   An unsupervised segmenter finds it unaided (cuts after it 95% of the time).
2. **Name + ending.** 740 or 520 closes most names; they never touch; the ending is **fixed per name** (5 of 881
   names take both, against 46 by chance; M77: 4 of 385 against 26). The segmenter binds the ending to the name as a
   suffix (cuts before it 22% of the time against 52% elsewhere).
3. **Two classes.** 520 is a small closed class: names ending in a fish sign (61% of their lines; M77 61%) and one
   fixed unit (long 3 + 520); everything identified as a person, tool, plant, building or landscape takes 740 (24 of
   754 lines with 520).
4. **Second slot.** 740 + 'man' (90) on seals, 740 + 400 on the Harappa tablets. The order is **possessor first,
   head last**: 90 follows 740 112 times and opens a name-and-ending text once.
5. **Numerals.** Two stroke series (short and long) precede different signs (Jensen-Shannon 0.59 bits; M77 0.77;
   0 of 500 permutations), the split of Proto-Elamite's counting and capacity systems; the long strokes go with the
   pot on tablets (45 of 51). The numbers are not weight units (they are dominated by 3, which the 0.86 g binary-
   decimal weight series lacks).
6. **Genres.** Seals: names and titles. Harappa tablets: many copies, 9% just a number and one sign (tokens of a
   quantity), the rest repeating seal names with the tablet ending.

## 4. Fixed meanings

- **Firm: seven sign = image equations** from the Mohenjo-daro copper tablets, where a sign or text on one face
  stands for the picture on the other (341 rhinoceros; 749 and 777/778 markhor goat; 753 hare; 777 archer; the
  archer, elephant, bull texts) (`copper.py`).
- **Provisional:** 347 (a horned quadruped) with the multi-headed animal on 8 of 9 objects; 460 (three cones) with
  a tree in four different tablet texts (`anchors.py`).
- **One reading of Parpola's survives:** 6 + fish (the Pleiades) is enriched 4.8 times before the fish (p = 4e-5;
  M77 11.5 times, p = 2e-7). The rest of the numeral + fish star names are not supported (7 + fish once; the Tamil
  star numbers 3, 5, 6, 7 are rarer before the fish than elsewhere).

## 5. The language

- **Grammar tests, no sound values needed:** a class suffix on the singular noun that separates persons from
  (star) names, and possessor-before-head order. Only Dravidian passes both outright; Indo-Aryan in part; Sumerian and
  Elamite fail the order, Munda and Burushaski the class suffix (Munda counts heavenly bodies as animate, Hoffmann
  1903). Conditional on the endings being suffixes, 90 a noun, and the fish names stars (`noun_class.py`,
  `typology.py`).
- **Registered predictions from the Dravidian model failed** (`PREDICTIONS.md`, committed before the test): no
  sign replaces 740 on the same names as a rational plural would, and the 520 names alternate slightly more, not less,
  than the 740 names. The Dravidian reading fits the structure it was built on and has not yet predicted anything new.
- **Registered predictions of a head-final name with a class suffix held** (second set): the ending follows the
  last sign (names sharing it agree 95% of the time, sharing the first sign 83%), and a non-final fish sign does not
  bring 520 (8% against 55% for fish-final names), on held-out texts. Against Sumerian and Elamite; neutral between
  Dravidian and Indo-Aryan.
- **Early Tamil names** (Tamil-Brahmi, Mahadevan 2003) share the shape of the Indus name slot (one dominant class
  suffix, a small second class, possessor first), but their minority class is women's names, not star names; the
  comparison is consistent with Dravidian without excluding Indo-Aryan (`tamil_brahmi.py`).
- **Statistical tests do not identify the language.** A key fitted to the corpus reads about 93% of it in any
  language; fitted keys even generalise to unseen texts in every language (the script's recurrent structure, not the
  language); with lexicons matched in size the ranking is inconclusive (`fit_holdout.py`, `matched_holdout.py`).
- **Outside evidence is almost nil:** the only probable Meluhhan names in cuneiform are Nanaza and Samar (three
  Irisagrig tablets, Šu-Suen 6); a full CDLI search (223 texts) adds none (`meluhha_oracc.py`).

## 6. The test any decipherment must pass

`bench.py` and the in-browser `docs/indus-bench.html`: a key is scored against its own shuffles in six languages
(vowel-aware), on the copper-tablet anchors, and on the structure above. **The test was validated on a real
decipherment**: Desset's accepted Linear Elamite key beats its shuffles (4 of 100 as good); the consonant-only
version of the test does not, and is not used. Results for published keys: Yajnadevam 2024 (Sanskrit), Fairservis
1992 and Parpola 1994 (Dravidian) do not beat their shuffles in their own language; Mahadevan and Kak give too few
signs to test; Mahadevan's reading of the endings as a gender pair is the one claim the structure supports.

## 7. What is new here, and what was known

Two literature checks (`results/lit_check.md`; the second read Mahadevan 1970/1982/1986/1998, Parpola 2015, the Wells
2006 thesis, Rao et al. 2009, Yadav et al. 2010 in full; still unread: Wells 2015 beyond a sample, Fuls's papers).
- **Known:** jar and arrow exclusive (Hunter 1934 via Mahadevan 1970; Parpola 1994: 94); the arrow mostly with fish
  (Mahadevan 1970: 22); gender reading (Mahadevan 1998); head-final order against Sumerian and Elamite (Mahadevan 1982,
  1986; Parpola 1994, 2015); separate stroke series, the Proto-Elamite multi-system model, pot + number as volume
  units, tablets as tokens (Wells 2006: 22, 161-196; Parpola 2008; Kenoyer 2020); West Asian seals following other
  rules, quantified (Rao et al. 2009); statistical restoration of deleted signs (Rao et al. 2009; Yadav et al. 2010,
  74%); sign-pair frequencies stable over the Mohenjo-daro periods (Rao and Mahadevan 1987); benchmarking decipherment
  algorithms on known decipherments (Snyder et al. 2010; Luo et al. 2019); fitted keys not identifying the language
  (Raghavendra 2026).
- **Contradicted by earlier work:** Wells (2006: 200-208) compared Indus word structure with Proto-Dravidian and
  Proto-Munda and preferred Munda, against the class-suffix test here; Mahadevan (1970: 46) found the openers in about
  the same proportions at every site, against the site effect found here.
- **Not found before:** the per-name fixedness count; the arrow class as closed (non-fish names almost never take it);
  the class-suffix test and the combined two-test argument; the numeral + fish enrichment test; the count of missing
  endings on foreign seals; grammar separated from numerals over the periods; restoration scored against real broken
  texts with intact twins; a key tested against its own shuffles, with Linear Elamite as the known-answer control; the
  registered predictions.

## 8. What would complete it

A phonetic decipherment needs evidence that ties sounds to signs, which this material does not contain: a bilingual
(an Indus text with a cuneiform version), a long text, or many more recorded Meluhhan names. Short of that, the
constraints above are what any proposal must meet: it must read the heading as one formula, the endings as a
two-class suffix fixed per name with the fish names in the second class, 'X-740 man' with the head last, the two
numeral series apart, the copper-tablet signs as their animals, and it must beat its own shuffles on texts it was
not built from, in its own language and not equally in others.
