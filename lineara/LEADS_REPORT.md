# Linear A: three leads followed up

23 September 2026, fifth pass. Scripts and outputs are in `reading/`. No lexical meaning and no language is claimed.

## 1. Is the HT 34 fraction point already in the literature?

Checked:

- **Every work citing Corazza et al. 2021** (OpenAlex, 18 works; Semantic Scholar, 7). None revises the fraction values.
- **The INSCRIBE team's own later account**, M. Corazza, *Computational methods for undeciphered scripts* (Bologna University Press 2024, open access), chapter 5. It repeats the values and still marks two as tentative: "A = 1/24?, H = 1/16?". It says they stem from "considerations that do not stem directly from the property of the system itself". HT 34 is not discussed. The chapter also records that B = 1/5 and D = 1/6 were already proposed by Cash and Cash (2012) and Montecchi (2013), the latter from a proportion on KH 7a.

**Result:** the HT 34 counterexample ("2 H K" written in that order, so H > K; no typologically attested H above 1/10 is free under the system's own one-value-one-notation rule) is not addressed in any source reachable online. It stays a counterexample to the two values their authors call tentative, not a new system. Not checked: Salgarella 2025 (not open), and Schrijver 2014, which predates the 2021 values.

## 2. The proposed language affiliations, tested against chance

`reading/lang_test.py`, output in `reading/lang_test_output.txt` and `lang_test_results.json`.

**Method.** Every lexicon word is spelled by fixed Linear B rules, set before any result was seen:

- open syllables;
- word-final consonants dropped;
- s, r, m and n before a consonant dropped; other consonants before a consonant written with the next vowel;
- l = r, and voicing ignored;
- geminates, long vowels and tones collapsed.

The rules reproduce Linear B practice: *Knossos* → ko-no-so, *Phaistos* → pa-i-to. Exact matches with the 491 Linear A word types of three or more signs are counted. Each lexicon is also scored against a null made of its own syllables shuffled across its words, with word lengths kept. Real words beat that null even in unrelated languages. The test that decides is therefore family against controls: the matches are split in proportion to the null expectations, and the question is whether the family's share exceeds its expectation (binomial test).

| Lexicon | Kind | Forms of 3+ syllables | Matches with Linear A | Per 1000 | Own-syllable null | Ratio |
|---|---|---:|---:|---:|---:|---:|
| Luwian (Melchert 1993) | proposed | 540 | 1 | 1.9 | 1.86 | 0.5 |
| Akkadian (Wiktionary) | proposed | 336 | 3 | 8.9 | 1.42 | 2.1 |
| Ugaritic (Wiktionary) | proposed | 288 | 4 | 13.9 | 1.22 | 3.3 |
| Etruscan (Wiktionary) | proposed | 27 | 0 | 0 | 0.08 | untestable |
| Ancient Greek (60,000 entries) | not proposed | 28,606 | 27 | 0.9 | 12.0 | 2.3 |
| Sumerian | not proposed | 40 | 0 | 0 | 0.15 | untestable |
| Hawaiian | control | 1,106 | 4 | 3.6 | 1.95 | 2.1 |
| Maori | control | 1,484 | 4 | 2.7 | 2.87 | 1.4 |
| Samoan / Tongan | control | 271 / 146 | 0 / 0 | 0 | 0.41 / 0.27 | |
| Yoruba | control | 2,447 | 7 | 2.9 | 3.28 | 2.1 |

**Family against controls.** The controls together run at 1.7× their null.

| Family | Ratio to its null | p (exceeds controls) | After correcting for 3 families |
|---|---:|---:|---:|
| Semitic (Akkadian, Ugaritic) | 2.65 | 0.23 | 0.69 |
| Anatolian (Luwian) | 0.54 | 0.95 | 1 |
| Tyrsenian (Etruscan) | untestable | | |

No proposed family matches Linear A better than languages that cannot be related to it. The matches themselves come as easily from the controls as from the candidates:

- E-KU-RU is Akkadian *eqlum* "field", and also Yoruba *eguru* "sandstone";
- A-KA-TA is Greek *akantha* and Yoruba *akata* "panther";
- A-TA-NA is Ugaritic *ḫatana* "to marry" and Māori *atanga* "interface".

**Positive control and power.** The same spelling rules applied to Greek against the whole Linear B vocabulary (4,164 types) give 13.1 matches per 1,000 lemmas, 3.2× their null. That is fewer per 1,000 than Yoruba gets against Linear B (21.7, 2.9×). At the candidate lexicons' sizes, and against 491 random Linear B types (the size of the Linear A target), a relationship as close as Greek to Linear B would give only 0.4–0.8 exact matches.

**What follows:**

1. Look-alike word lists cannot establish Minoan's affiliation. The method cannot even tell the language of Linear B apart from Yoruba. Semitic, Luwian or other readings built on matched word shapes (KU-RO = *kull*, and the like) are not evidence.
2. Within that limited power, nothing favours Semitic or Luwian. The small Semitic excess (7 matches) is within the control range.
3. KU-RO, KI-RO and PO-TO-KU-RO, the three words whose sense is fixed by arithmetic, get no same-spelled word of fitting meaning in any candidate. Control languages supply look-alikes of the wrong meaning (Yoruba *kuro*, Tongan *kulo*, Hawaiian *kilo*), just as a candidate would.

Limits: Hurrian has no open lexicon (Richter's *Bibliographisches Glossar*, 2012, is not open access), and the Etruscan and Sumerian lists are too small. The spelling rules are one fixed choice. Other choices (different treatment of clusters, ḫ as zero) would move individual matches, but not the power problem.

## 3. Linear A words in the Linear B record

`reading/names_lb.py`, output in `reading/names_lb_output.txt` and `names_lb_results.json`.

The comparison vocabulary is every word type of three or more signs in the linearb.xyz Linear B corpus: 4,164 types, 1,639 attested only on Crete and 2,260 only on the mainland. Each carries its Chadwick and Ventris (1973) category via the tiripode lexicon. Linear A sign values are shuffled within frequency bins, 2,000 times, as the null.

| | Real | Null mean | p |
|---|---:|---:|---:|
| All exact matches | 13 | 2.8 | 0.0005 |
| Place names | 3 | 0.17 | 0.001 |
| Personal names | 3 | 0.72 | 0.04 |
| Other glossed words | 3 | 0.42 | 0.01 |
| Words not in the glossary | 4 | 1.46 | 0.06 |

The two groups divide by site:

- **Names, all on Crete.** Every matched name is a Linear B word attested only on Crete (Knossos): place names PA-I-TO, SU-KI-RI-TA and SE-TO-I-JA, and personal names DA-I-PI-TA (Zakros ZA 8, ZA 10a), I-TA-JA (HT 28a) and KI-DA-RO (HT 47a, HT 117a). Half (51.3%) of Linear B names of three or more signs are Crete-only, so six of six falls out by chance with p = 0.018. Two further Knossos words not in the glossary behave like names in Linear A lists: TA-NA-TI (HT 7a, HT 10b, HT 49a, HT 98a) and PA-RA-NE (HT 115a/b).
- **Common words, on the mainland.** The Linear B words attested only on the mainland are Greek common words at Pylos: ma-te-re "mother", i-ja-te "physician", da-ma-te, a-ka-ta, a-ro-te. They are what the language test predicts from chance look-alikes of Greek.

**Result:** the only Linear A vocabulary that survives into Linear B is names, and it survives only at Knossos. Shared names at Knossos are known from individual cases. The contribution here is to show they exceed chance, and to name the concentration.

## Where this leaves decipherment

The three leads narrow the field without opening it:

- the fraction system has two values that one tablet contradicts;
- the most-cited language proposals do no better than controls, and the method they rest on cannot identify a language at all;
- Minoan onomastics continued at Mycenaean Knossos.

A decipherment of the language still needs a bilingual text or a much larger corpus.

# Second round, 23 September 2026

## 4. New inscriptions

The longest Linear A text now known is on an ivory sceptre from the Anetaki cult centre at Knossos, found in 2024:
the ring KN Zg 57 and the handle KN Zg 58, about 119 signs. The only publication so far is Kanta, Nakassis,
Palaima and Perna, *Ariadne* (2025) 27–43, which is open access. It gives no sign-by-sign transcription, and its
photograph is too small to read the signs. The full edition is announced as Kanta (ed.), *Anetaki II*,
forthcoming.

The working corpus has a partial KNZg57a (17 tokens) and empty records for KNZg57b and KNZg58, so nothing can be
added yet. The article does describe what the text contains:

- **KN Zg 57 (ring):** a religious inventory with no numerals. It lists 12 animals, vessels (amphorae, a rhyton,
  a tripod), textiles and hides, often with a syllabogram in ligature. It also has six sign groups and the
  logograms GRA, "far" and OLIV, few of them paralleled elsewhere.
- **KN Zg 58 (handle):** an account with numerals. Its Face δ gives **six different fraction signs in sequence**,
  which the authors say orders the values differently from all published proposals. That bears directly on the
  HT 34 point (section 1). The sequence is withheld until the final publication.

## 5. Cross-tablet record linkage

`reading/prosopography.py`, output in `prosopography_output.txt` and `prosopography_results.json`.

The administrative texts contain 479 labelled entries with 364 distinct entry words. Of those words, 54 recur on
two or more records. Record pairs sharing three or more entry words: **4, against a null of 0.11 (max 3 in 1,000
runs, p 0.001)**. The recurrences are real series, not shared common words. They are sparse, though: the
Haghia Triada archive does not survive as a network of repeated names.

**HT 86a/b, HT 95a/b: two headings over the same people.** Five men (DA-ME, DI-DE-RU, KU-NI-SU, MI-NU-TE, SA-RU)
receive grain on all four texts, but under different heading terms:

- HT 86a splits them between A-KA-RU (KU-NI-SU, SA-RU, DI-DE-RU, 20 each) and A-DU (DA-ME, MI-NU-TE, 20 each);
- HT 95b puts all five, with QE-RA₂-U, under A-DU at 10 each: exactly half of HT 86a;
- HT 95a (heading DA-DU-MA-TA) gives 10 each, with SA-RU at 20.

A-KA-RU and A-DU are therefore categories of the same transaction applied to the same individuals, not persons
or places. This agrees with A-DU's heading role found in section 03 of the page. What the two categories mean
is not settled by this series.

**HT 9, two faces of one list: PA₃ marks a partial amount.** HT 9a lists a wine account (SA-RO … VIN) with KU-RO
31¾ and ends with PA₃. HT 9b opens with PA₃ and repeats the same names with KU-RO 24. For every one of the six
shared names, the PA₃ amount is equal to or smaller than the recto amount:

| Name | Recto | Verso |
|---|---:|---:|
| PA-DE | 5¾ | 3 |
| *306-TU | 10 | 8 |
| DI-NA-U | 4 | 4 |
| QE-PU | 2 | 2 |
| *324-DI-RA | 2½ | 2 |
| TA-I-AROM | 2½ | 2 |

On HT 34, PA₃ 70 stands between SA+MU+KU 100 and KI-RO 30. Both documents fit PA₃ = the delivered part,
KI-RO = the part still owed. That is Younger's suggestion, now supported on two tablets. The HT 9 pattern alone
is weak evidence (four strict inequalities out of six).

**KI-RO lists count persons.** Every word that stands in a KI-RO section (HT 88, HT 94b, HT 117a) carries exactly 1.
The same words elsewhere carry varied amounts: KU-PA₃-NU 109 on HT 1, SA-RU 20 of grain on HT 86. The KI-RO lists
are lists of individuals owed or missing, one each.

## 6. Kober's test: do endings track position?

`reading/kober.py`, output in `kober_output.txt` and `kober_results.json`.

Word tokens with a known function (heading, entry label, in-list, formula, sealing) were grouped into families
with the same stem and different endings. The statistic is the conditional mutual information between ending and
function, given the stem, against 5,000 within-stem permutations.

| Families | Families | Tokens | Real | Null mean | p |
|---|---:|---:|---:|---:|---:|
| Final sign varies | 49 | 153 | 48.6 | 46.2 | 0.20 |
| Initial A- / JA- / none varies | 12 | 56 | 9.0 | 6.4 | 0.07 |

**No inflection is recovered.** Final signs do not predict position once each stem's own mix is allowed for. The
initial A-/JA- leans toward headings, as in A-KA-RU, A-PA-RA-NE and A-RI-JA against the bare forms in entries.
It stays short of significance, and ZA 10a (TA-NA-TE / A-TA-NA-TE, both entries) remains a counterexample.

Across the whole vocabulary some final signs lean strongly:

- -KA toward sealings (χ² 129);
- -TE toward formula words (24);
- -RU and -TU toward entries (74% and 79%).

These are distributions of particular words, not evidence of case endings. A Kober grid needs more attestations
per stem than Linear A provides: the largest family has 9 tokens.

## Where the second round leaves things

- **Fractions:** a ready draft (`note_HT34/NOTE_HT34.md`) and two unsent requests (`note_HT34/REQUESTS.md`). The
  decisive evidence is a photograph of HT 34.3 and the KN Zg 58 sequence, both outside this project's reach.
- **Accounting vocabulary:** A-DU and A-KA-RU are transaction categories over the same persons, PA₃ marks a
  delivered part (two tablets), and KI-RO lists count individuals. These are functional, not lexical, meanings.
- **Grammar:** not recoverable at this corpus size by Kober's method.
- **New text:** the Anetaki sceptre is the only substantial addition, and it awaits publication.

# Third round, 23 September 2026

## 7. Names across sites

`reading/prosopography.py` (`cross_site`), output in `cross_site_output.txt` and `cross_site_results.json`.

There are 479 labelled administrative entries: 337 from Haghia Triada, 60 Zakros, 26 Khania, and fewer
elsewhere. **Only 10 entry words occur at two or more sites, against 33.5 expected** if the same entries were
shuffled across sites, keeping each entry's site (P(null ≤ 10) = 0.0005). Linear A entry vocabulary is strongly
local. That is what personal names in separate archives look like.

The words that do cross sites are mostly recurring administrative words, not names:

- A-DU: Haghia Triada, and Tylissos (TY 3a, with oil);
- DA-RE: seven records at Haghia Triada, Palaikastro (PK 3, 72) and Khania (KH 104, grain);
- KU-PA, SA-MA and SI+CYP.

That fits DA-RE, like A-DU, being a transaction term rather than a person. Its uses at HT (men, grain, entries of
1 to 16½) and PK 3 (72) point the same way. Only PA-JA-RE (HT 8b, 29, 88; ZA 10b) and MA-KA-I-TA (PK 1, ZA 5b)
look like the same individual's name, or a common name, at two sites.

## 8. Fraction values by commodity

`reading/fraction_commodity.py`, output in `fraction_commodity_output.txt`.

Each of the 30 adjacent fraction pairs was tagged with the commodity governing its entry and scored against the
2021 values. The three violations fall under three different contexts:

- HT 34 H K: on a grain tablet, strictly under the unidentified *525;
- KH 86 A B: cyperus;
- ZA 8 E J: no commodity.

Every other pair in those contexts is consistent: cyperus 7 of 8, grain 2 of 3. HT 34's is the only pair in the
corpus containing both H and K, and no other grain pair involves either sign. Commodity-specific fraction units
therefore cannot be tested with the present corpus, and nothing in it favours them. HT 34 cannot be explained away
as a grain unit.

## 9. Hurrian

An open lexicon was found: E. Laroche, *Glossaire de la langue hourrite* (1980), OCR text on the Internet
Archive. Its copyright status is unclear, so it is used here only as a local, git-ignored cache for counting;
nothing from it is republished. The parse yields 612 headwords, 294 of three or more syllables after Linear B
spelling.

Against Linear A there is **1 match (A-PA-KI = *abalgi*) against 0.9 expected, p 0.6**. The result is the same
whether the OCR's plain h is dropped or read as ḫ = k. In the family test, Hurro-Urartian gives 1.1× its null
against the controls' 1.7× (p 0.79).

All four proposed families are now tested: Semitic, Anatolian, Hurro-Urartian and Tyrsenian. None matches
Linear A better than the controls. After correcting for four families, the smallest p-value is 0.86 (Semitic).

## 10. Salgarella, *Writing in Bronze Age Crete* (2025)

Closed access: a Cambridge Element with no open repository copy (OpenAlex) and no public table of contents.
Whether it discusses HT 34 or the fraction values cannot be checked without buying it or borrowing a library copy.
This is the one open item before the HT 34 note can be called new with confidence.

# Fourth round: Eteocretan and Pre-Greek, 23 September 2026

## 11. Eteocretan

`reading/eteocretan.py`, output in `eteocretan_output.txt` and `eteocretan_results.json`.

**Texts.** R. A. Brown's transcriptions of the five certain inscriptions, which follow autopsy and agree with
Duhoux 1982 on readings:

- Dreros 1 and 2: Eteocretan parts only, e.g. *et isalabre komn men inai isaluria lmo*; *tuprmēriēia*;
- Praisos 1–3.

The disputed Psychro (Epioi) stone is scored separately. In all, 193 syllables once spelled the Linear B way.
Praisos 2 and 3 have no word division, so Linear A words are sought *inside* each unbroken stretch.

| Test | Linear A in Eteocretan | Null (values shuffled) | p | Unrelated-language samples of the same size |
|---|---|---:|---:|---|
| Words of 3+ signs (491 types) | **0** | 0.39 | 1 | Hawaiian 2.7, Maori 1.2, Yoruba 1.8 |
| Words of 2 signs or more (783 types) | 14 | 15.2 | 0.70 | 16.6, 14.8, 12.8 |

**Positive control.** A sample of 491 Linear B word types was searched the same way in about 200 syllables of
Greek:

- in a neutral text (Iliad 1.1–7, Odyssey 1.1–4), 2 matches against 0.38 (p 0.06): a-na-ka, po-ru-to;
- in a text naming Cretans (Odyssey 19.172–177, Strabo 10.475), 3 against 0.45 (p 0.012).

A relationship as close as Linear B to Greek therefore yields only about 2–3 matches in a text this short, and
the design barely detects it.

**Result.** No Linear A word of three or more signs occurs in the Eteocretan inscriptions. That is fewer than
random word lists from unrelated languages produce. If Linear A stood to Eteocretan as Linear B stands to Greek,
about 2–3 matches would be expected, and 0 has a probability of roughly 0.05–0.15. The corpus weakly disfavours a
close Minoan–Eteocretan identity and cannot test a distant one. The Psychro stone has no 3-sign match.

## 12. Pre-Greek

An open list was found: Ancient Greek entries whose Wiktionary etymology derives or borrows them from Pre-Greek
(source code qsb-grc, mostly following Beekes and Furnée). The full Kaikki extract (68,196 entries) was streamed
and the 1,600 such entries kept. The test is `reading/pregreek.py`, output in `pregreek_output.txt` and
`pregreek_results.json`.

The comparison is made within Greek, which holds Greek phonology and word-building constant. Pre-Greek lemmas are
set against ordinary Greek lemmas, sampled to the same word-length distribution: Pre-Greek words are shorter,
averaging 3.0 syllables against 4.2, and length alone changes the chance of an exact match.

| | Matches with Linear A (3+ signs) | Ordinary Greek, length-matched | p |
|---|---:|---:|---:|
| Lemmas | 6 of 1,054 | 2.62 | 0.04 |
| Lemmas, proper names removed on both sides | 5 | 2.55 | 0.10 |
| Stems (Greek ending removed) | 1 of 366 | 1.17 | 0.70 |

The matches are:

- A-KA-TA / *ákantha* "thorny plant";
- A-KI-RO / *ankhílōps*, an eye swelling;
- A-RI-PA / *alíbas* "corpse";
- KI-DA-RO / *kídalon* "onion";
- PA-I-TO / Phaistos;
- PA-TA-NE / *patánē* "flat dish".

None of the Linear A words stands in a context that fits the Greek meaning. KI-DA-RO and PA-TA-NE are personal
names in KI-RO lists, and KI-DA-RO is also a personal name in Linear B at Knossos.

The syllable distributions tell the same story. Measured as Jensen–Shannon divergence from Linear A's syllable
frequencies (0 = identical; Linear A against itself 0.026):

| Lexicon | Divergence from Linear A |
|---|---:|
| Hurrian | 0.174 |
| Akkadian | 0.196 |
| Ugaritic | 0.208 |
| Luwian | 0.209 |
| Samoan | 0.233 |
| Yoruba | 0.234 |
| Pre-Greek | 0.262 |
| Maori | 0.262 |
| ordinary Greek | 0.268 |
| Hawaiian | 0.287 |

Pre-Greek is no closer in sound than ordinary Greek or Māori. The nearer languages (Hurrian, Akkadian) are the
ones whose word matches did not beat the controls, so closeness of syllable inventory alone identifies nothing.

**Result.** There is no reliable lexical link between Linear A and the Pre-Greek substrate as Wiktionary records
it. A weak excess (p 0.04) disappears once the one shared place name is set aside (p 0.10), and the matched words
do not fit their Linear A contexts.

## Where the language question stands

Every comparison open to this project has now been run under one set of rules with controls:

- **Proposed families:** Semitic, Anatolian, Hurro-Urartian and Tyrsenian.
- **The likely descendant:** Eteocretan.
- **The known contact vocabulary:** Pre-Greek.

None identifies Minoan. The positive controls show why. Even Greek against Linear B, the one known relationship,
is barely detectable by word matching at these corpus sizes, so failure to match is weak evidence against any
single hypothesis, and success would be weak evidence for one. The language will be identified, if at all, by new
texts: the full edition of the Knossos sceptre (KN Zg 57–58), further long inscriptions, or a bilingual.

# Fifth round, 23 September 2026

## 13. The Salgarella file

The file supplied, "Drawing Lines: the palaeography of Linear A and Linear B" (E. Salgarella, *Kadmos*), deals with
sign variants and the passage of sign shapes from Linear A to Linear B. It does not discuss fractions, HT 34 or
Corazza et al. 2021, so it neither anticipates nor contradicts the HT 34 point. *Writing in Bronze Age Crete*
(2025) remains the one unchecked source.

## 14. DAMOS

The DAMOS word search (damos.hf.uio.no, CC BY-NC-SA 4.0) was queried for every common word of three or more signs:
10,198 tokens and 4,162 types, against 4,164 in linearb.xyz. It widens nothing, but it independently reproduces 12
of the 13 Linear A = Linear B matches (A-KA-TA is not a full word there) and the split by site. Its line contexts
show the shared names used the same way in both scripts, as entries in lists of individuals with small counts:

- TA-NA-TI: KN Uf 311 "ta-na-ti, DA 1"; in Linear A, HT 7a "TA-NA-TI 1" in a list of men;
- I-TA-JA: KN Ap 769 "i-ta-ja MUL 1";
- PA-RA-NE: KN Vc 7616 "pa-ra-ne 1";
- DA-I-PI-TA: KN Bk 799;
- KI-DA-RO: KN E 842, with grain.

Details are in `reading/names_damos_results.json`.

## 15. Cretan Hieroglyphic

Younger's Hieroglyphic Lexicon (365 sign groups) and his grids of sign values were recovered from archived pages.
Read with the values CHIC assigns by *shape* (grid 1, certain and probable), only 20 groups are fully readable. They
match Linear A words no more than chance: 3 against 2.2 (A-JA, RU-SA, SA-RO; p 0.38), and none of three or more
signs.

With Younger's own grid 2 added, 17 groups match against 11.1 (p 0.04), and two of three or more signs (A-KI-RO,
A-SA-SA-RA; p 0.07). But grid 2 was partly built by matching Hieroglyphic groups to Linear A words (KU₂-RO₃ "total",
the Arkhanes formula), so that excess is circular.

**Result:** continuity from Hieroglyphic to Linear A in vocabulary cannot yet be tested independently. It needs sign
values fixed without word comparisons. Code: `reading/chic.py`.

## 16. Errata for the digital editions

`errata.py` compares SigLA and lineara.xyz word by word and classifies 44 disagreements, written up in `ERRATA.md`:

| Kind | Count |
|---|---:|
| One-sign substitutions | 15 |
| One sign added or missing | 11 |
| Different word division | 6 |
| Other | 9 |
| No counterpart | 3 |

The corpus-level problems are the HT 34 KI-RO figure (37 for 30), the duplicate KH101 record, and the empty or
untransliterated sceptre records KNZg57b and KNZg58. Systematic patterns:

- JA against PA3 (HT 115a, HT 117a);
- *28B against I at Zakros (four texts);
- VIR joined to the following word (four texts).

Three disagreements touch results of this project:

- PH Wa 32 is SU-KI-**RA**-TA in SigLA, so the Sybrita match rests on the GORILA reading RI;
- HT 122a is PA-**RI**-NE in SigLA (one of the Pre-Greek look-alikes);
- HT 95b is DA-**ZA** in SigLA (the HT 86/95 series still holds on the other tablets).

Draft issue text for both projects is at the end of `ERRATA.md`; nothing has been posted.

# Sixth round: dependence on disputed readings, 23 September 2026

`reading/sigla_sensitivity.py`, output in `sigla_sensitivity_output.txt` and `sigla_sensitivity_results.json`.

The Linear A vocabulary was rebuilt with SigLA's reading in place of lineara.xyz's for the 17 disagreements of a
definite kind that could be applied: 8 substitutions, 6 added or missing signs and 3 word divisions. Eleven word
types then drop out and thirteen come in, among them SU-KI-RA-TA for SU-KI-RI-TA, PA-RI-NE, DA-ZA and TE-PA₃-RE.

| Result | lineara.xyz readings | SigLA readings |
|---|---|---|
| Exact Linear A = Linear B matches (3+ signs) | 13 (null 2.8, p 0.001) | 12 (null 2.7, p 0.001) |
| Names among them, all Crete-only | 6 of 6 (p 0.018) | 5 of 5 (p 0.036) |
| NeuroDecipher list matches | 6 | 5 |
| Pre-Greek lemma matches | 6 | 6 (PA-TA-NE survives on HT 94b) |
| Language-family matches | unchanged | unchanged |

Only one result moves: the Sybrita match (SU-KI-RI-TA) depends on the GORILA reading of PH Wa 32. The conclusions
stand on either edition.

**Fraction order in SigLA.** Every document that supplies an adjacent fraction pair was looked up in SigLA, with the
signs' order read from their positions: left to right on a line, or top to bottom in a stack. None of the pairs
SigLA records is reversed:

- in the same order: HT 34 H K (left to right), KH 86 A B, the E F pairs of HT 8b, 16 and 50a, and HT 93a J H;
  HT 51b J F and HT 120 J A are stacked, larger above;
- not directly adjacent in SigLA: HT 129 and HT 32;
- not recorded in SigLA: most Khania documents and ZA 8.

The HT 34 counterexample therefore holds on both editions, and SigLA supports the A B B reading of KH 86 against the
A A of Corazza et al.

# Seventh round: name shapes, sites, ration proportions, scribal variants, 23 September 2026

## 17. Knossos personal names look like Linear A names

`reading/name_shapes.py`, output in `name_shapes_output.txt` and `name_shapes_results.json`.

Exact matches give only six shared names. This test compares the *shape* of whole name stocks:

- 358 Linear A list names (entry labels, recurrent transaction words excluded);
- 637 Linear B personal names attested only at Knossos;
- 339 attested only at Pylos.

Names are classed as personal names by the Ventris–Chadwick glossary. The statistic is D = JSD(Linear A, Pylos) −
JSD(Linear A, Knossos) over syllable distributions. The null shuffles the site labels between the Knossos and
Pylos names, keeping group sizes, 5,000 times.

| Test | All syllables | First syllables | Last syllables |
|---|---|---|---|
| Personal names | D 0.062, p 0.0002 | D 0.144, p 0.0002 | D 0.151, p 0.0002 |
| Names without a Greek etymology in the glossary (520 / 224) | D 0.054, p 0.0002 | D 0.152, p 0.0002 | D 0.173, p 0.0002 |
| Exact shared names removed | D 0.060, p 0.0003 | D 0.141, p 0.0003 | D 0.149, p 0.0003 |
| **Control: non-name vocabulary** (279 / 345) | D 0.005, p 0.32 | D 0.010, p 0.27 | D −0.004, p 0.48 |

Knossos personal names are markedly closer in shape to Linear A names than Pylos personal names are, on every
measure, with or without the exact matches. The Knossos and Pylos common vocabulary shows no difference, so this is
not a Knossos spelling convention. The effect holds for each Linear A archive separately:

| Linear A site | Names | p (Knossos closer) |
|---|---:|---:|
| Haghia Triada | 233 | 0.0005 |
| Zakros | 52 | 0.001 |
| Khania | 25 | 0.002 |

**Result:** a Minoan-shaped component runs through the Knossos onomasticon, well beyond the few names shared
exactly. The exact shared names themselves come mostly from Haghia Triada (5 names), with one each from Zakros,
Prassa and Phaistos. Non-Greek names at Knossos have long been noted; the measurement against Pylos, with a
common-vocabulary control, is new here.

## 18. Ration proportions as fraction evidence

`reading/fraction_ratios.py`. The only tablet in the corpus with repeated "n persons, then a commodity amount"
pairs is KH 7a: VIR 10 with CYP+D J, and VIR 4 with CYP+D B. That gives 1/20 per person in both entries, consistent
with J = ½ and B = ⅕. This replicates Montecchi (2013). No second proportion exists, same-entry pairs included, so
ration arithmetic offers nothing further on H or A.

## 19. Scribal hands and sign variants

`reading/scribes_variants.py`. SigLA's variant field is empty for about 90% of attestations. The coded variants
are editorial sub-types, not handwriting forms. Only three signs can be tested, and the overall association with
scribe attributions is not significant (p 0.32). Scribal palaeography would need image-based comparison of SigLA's
sign drawings. The candidate-hand scores the script prints for unattributed tablets are driven by the empty field
and carry no information.

# Eighth round: ten further hypotheses, 23 September 2026

`reading/hypotheses10.py`, output in `hypotheses10_output.txt` and `hypotheses10_results.json`. The follow-up checks
reported below were run inline and are recorded here.

| # | Hypothesis | Result | Verdict |
|---|---|---|---|
| H1 | Vowel harmony within Linear A words | same-vowel neighbours 27.5% against a within-corpus shuffle of 28.2% (p 0.72). Linear B shows 27.8% against 22.7% (p 0.001), the echo-vowel spelling of clusters (ko-no-so) | **Not supported.** Linear A lacks Linear B's cluster-spelling signature: fewer consonant clusters in Minoan words, or a different convention |
| H2 | Words start with bare A- more in Linear A than Linear B; more in Knossos names than Pylos names | 12.5% against 11.3% (p 0.18); 16.2% against 18.0% (p 0.78) | **Not supported** |
| H3 | Linear A is o-poor; Knossos names share it | Linear A 2.8% o-syllables against Linear B 26% (p 0.0005). Whole Knossos names 27% against Pylos 26% (no difference), but **inside the word** 12.3% against 16.5% (p 0.002) | **Supported inside the word:** Knossos name stems lean toward Linear A's o-deficit; Greek-inflected endings mask it |
| H4 | Signs Linear B did not keep were rare in Linear A | kept signs median 49 attestations, dropped median 2 (p 0.0002) | **Supported:** the Mycenaean adaptation dropped the rare signs |
| H5 | Which syllables make Knossos names Linear A-like | final -so (6.8% against 1.5%) and -zo significant after correction, but rare in Linear A names; first syllables qa, ku, i, wi at Linear A-like rates, not significant singly. The name-shape effect survives removing all final -u (-eus) names (p 0.0005) | **Partly:** no single syllable carries it; it is spread across the stock. The excess -so is the Pre-Greek place-name suffix (-ssos) |
| H6 | Minoan-looking names concentrate in particular Knossos series | mean Linear A-likeness by series (D, V, A, B, C, L, S, U, X, F) does not differ (p 0.72) | **Not supported:** spread across record types |
| H7 | The formula prefix (JA-/A-/none) depends on site | chi² 6.6 (p 0.64), 20 observations | **Not supported** (small sample) |
| H8 | Recurring names keep the same commodity | 5 of 22 against 2.9 expected (p 0.15) | **Not supported** |
| H9 | Transaction words go with particular commodities | token level p 0.004, but by record only p 0.20 (57 record-level pairs; SA-RA₂ with grain in 10 of 18) | **Not supported** once repeated entries on one tablet are counted once |
| H10 | Word endings agree with the entry's commodity | only 4 stem families (9 tokens) qualify | **Untestable** |

**What the round adds.**

- **H3:** Knossos personal names lean toward Linear A's o-deficit inside the word (p 0.002). That independently
  supports the name-shape result of round 7.
- **H4:** a quantitative statement of the Mycenaean adaptation. The Linear A syllabograms that Linear B dropped
  were rare ones.
- **H1:** Linear A words lack the same-vowel neighbours that Linear B's spelling of Greek clusters creates, so
  Minoan words probably had fewer consonant clusters, or Linear A spelled them differently.
- **Negatives:** the rest are negative or untestable, and are recorded so they are not rerun as open leads.

# Ninth round: fifty hypotheses in ten batches, 23 September 2026

`reading/batches.py`, output in `batches_output.txt` and `batches_results.json`. Each hypothesis was tested against a
permutation or resampling null. Benjamini–Hochberg was then applied at a 5% false-discovery rate across the 49
testable hypotheses (one was untestable): **29 survive.** The Class column separates new observations
from results that are expected by construction or already known.

| ID | Hypothesis | p | Survives correction | Class |
|---|---|---:|---|---|
| A1 | Totals balance more often on single-commodity tablets | 0.3303 | no | not supported |
| A2 | Totals are round (multiples of 10) more often than entries | 0.8231 | no | not supported |
| A3 | Entries within a list are written in descending order of size | 0.0005 | yes | new |
| A4 | Quantities >= 10 follow Benford's law (p here = evidence AGAINST Benford) | 0.0005 | yes | expected |
| A5 | Larger totals are more often wrong | 0.3688 | no | not supported |
| B1 | Persons (VIR) are never counted in fractions, unlike goods | 0.0005 | yes | expected |
| B2 | Larger fraction values (Corazza) are used more often | 0.0015 | yes | expected |
| B3 | Haghia Triada and Khania use different fraction repertoires | 0.0005 | yes | new |
| B4 | The combination K L2 belongs to cyperus | 0.1284 | no | not supported |
| B5 | Totals carry fractions more often than entries | 0.956 | no | not supported |
| C1 | Signs prefer particular positions in the word (initial, medial, final) | 0.0033 | yes | expected |
| C2 | Reduplication (the same sign twice in a row) is more common than chance | 0.9221 | no | not supported |
| C3 | Neighbouring syllables share a consonant more than chance | 1.0 | no | not supported |
| C4 | Word-final syllables have a different vowel mix | 0.0005 | yes | new |
| C5 | The next sign is more predictable than chance (lower conditional entropy) | 0.0033 | yes | expected |
| D1 | Reduplicated names are commoner at Knossos than Pylos | 0.8986 | no | not supported |
| D2 | Knossos names are closer in length to Linear A names than Pylos names | 0.0005 | yes | robustness |
| D3 | Typical Linear A name endings (ti, na, ja, ta, re, ra, ru, te) are commoner at Knossos | 0.3608 | no | not supported |
| D4 | Knossos place names are more Linear A-like than Knossos personal names | 0.0625 | no | not supported |
| D5 | Names in the early Room of the Chariot Tablets are more Linear A-like | 0.8391 | no | not supported |
| E1 | Heading words are longer than entry words | 0.7311 | no | not supported |
| E2 | Tablets by the same scribe share more vocabulary | 0.004 | yes | new |
| E3 | Words shared between sites are shorter than site-specific words | 0.0005 | yes | expected |
| E4 | KU-RO closes its section (no further entries follow) | 0.014 | yes | expected |
| E5 | Single signs on sealings are abbreviations of word beginnings (closer to initial than final signs) | 0.0005 | yes | quantified |
| F1 | Religious (formula) words are longer than administrative words | 0.0005 | yes | known qualitatively |
| F2 | The religious vocabulary overlaps the administrative less than chance | 0.0005 | yes | known qualitatively |
| F3 | Words beginning JA- belong to the religious register | 0.0005 | yes | known qualitatively |
| F4 | Words beginning U- belong to the religious register | 0.003 | yes | known qualitatively |
| F5 | Religious and administrative words differ in vowel mix | 0.0125 | yes | known qualitatively |
| G1 | Knossos Linear B uses syllables at rates closer to Linear A than Pylos does | 0.002 | yes | new |
| G2 | Knossos uses the special signs (pa3, ra2, ta2, pu2...) more than Pylos | 1.0 | no | not supported |
| G3 | Logograms Linear B kept were commoner in Linear A than numbered ones it did not | 0.0005 | yes | expected (cf. H4 of round 8) |
| G4 | Undeciphered Linear B signs (*18, *47, *56...) are commoner at Knossos | 0.0005 | yes | new |
| G5 | Knossos names with undeciphered signs are more Linear A-like | 0.954 | no | not supported |
| H1 | Knossos names are more Linear A-like than Thebes names | – | untestable |  |
| H2 | Knossos names are more Linear A-like than non-Pylian mainland names | 0.0085 | yes | robustness |
| H3 | Knossos names are closer to Linear A names in syllable pairs too | 0.002 | yes | robustness |
| H4 | The Knossos name effect survives matching word lengths | 0.0005 | yes | robustness |
| H5 | Linear A religious words also resemble Knossos names more than Pylos names | 0.0005 | yes | new |
| I1 | Middle Minoan and Late Minoan texts use syllables differently | 0.01 | yes | new (small MM sample) |
| I2 | Words are longer in Late Minoan texts than Middle Minoan | 0.8796 | no | not supported |
| I3 | o-syllables were commoner earlier (Middle Minoan) than later | 0.4508 | no | not supported |
| I4 | Sites farther apart differ more in syllable use (Mantel test) | 0.7822 | no | not supported |
| I5 | Khania differs more from Haghia Triada than Zakros does | 0.1249 | no | not supported |
| J1 | Amount sizes depend on the commodity | 0.0005 | yes | expected |
| J2 | In lists of men, each named entry is usually a single person (1) | 0.997 | no | not supported |
| J3 | Amounts in KI-RO sections are smaller than elsewhere | 0.0005 | yes | new |
| J4 | Amounts entered with SA-RA2 are larger than other grain and cyperus amounts | 0.3183 | no | not supported |
| J5 | Even amounts are commoner than odd ones (rationing in pairs) | 0.0005 | yes | new |

**Checks run inline, all confirmed:**

- **J5 (even amounts)** holds with every multiple of 5 excluded: 415 of 637 even (65%, p 0.0002).
- **A3 (largest first)** holds with each list's first number dropped (97 lists, τ 0.12, p 0.004).
- **C3 (shared consonants)**, tested the other way round after the fact: neighbouring syllables *avoid* sharing a
  consonant (4.1% against 6.8%, p 0.0005). Linear B shows the same (p 0.003), so this is a property of the spelling,
  not specifically Minoan.

**What the round adds.**

- **The Knossos evidence widens beyond names.**
  - Knossos Linear B as a whole uses syllables at rates closer to Linear A than Pylos does (G1, p 0.002).
  - Undeciphered Linear B signs (\*18, \*47, \*56 and others) are about three times as common in Knossos words
    as in Pylos words (G4: 5.1% against 1.8%, p 0.0005). This fits the view that they wrote Minoan sounds.
  - Linear A's *religious* words, not only its list names, are closer to Knossos names than to Pylos names (H5).
    The resemblance is therefore to Minoan word shapes generally.
  - It holds against the non-Pylian mainland (H2), in syllable pairs (H3) and at matched lengths (H4).
- **New bookkeeping observations:**
  - scribes tended to list larger amounts first (A3);
  - even amounts are preferred beyond round numbers (J5), which suggests halves or pairs as working units;
  - amounts in KI-RO sections are smaller (J3), consistent with KI-RO as a deficit;
  - Haghia Triada and Khania use different fraction repertoires (B3), a regional difference in metrology;
  - tablets by the same scribe share vocabulary (E2), which supports the scribe attributions or offices by
    subject.
- **Quantified:** single signs on sealings match word *beginnings* rather than endings (E5), supporting their
  reading as abbreviations.
- **Not supported, and so recorded:** reduplicated names, typical Linear A endings at Knossos, particular
  Knossos deposits, the special signs pa3/ra2 at Knossos, distance decay between sites, change in word length or
  o-use over time, SA-RA2 amounts, and K L2 tied to cyperus. One test was untestable: Thebes has only 8 names.

# Tenth round: twenty-five further hypotheses, 23 September 2026

`reading/batches2.py`, output in `batches2_output.txt` and `batches2_results.json`. The conventions are the same as the
ninth round. Benjamini–Hochberg at 5% across the 25 tests leaves **13 supported**.

| ID | Hypothesis | p | Survives correction | Class |
|---|---|---:|---|---|
| K1 | At Knossos, words with undeciphered signs are more often personal names | 0.4113 | no | not supported |
| K2 | Knossos-only words are more Linear A-like than words shared by Knossos and Pylos | 0.0005 | yes | new |
| K3 | At Knossos, names follow Linear A syllable rates more closely than common words | 0.002 | yes | new |
| K4 | Cretan place names in Linear B are more Linear A-like than mainland place names | 0.0055 | yes | new |
| K5 | Knossos adjectives in -jo/-ja are built on Linear A words (stem + suffix) | 0.5934 | no | not supported |
| L1 | Largest-first listing holds outside Haghia Triada too | 0.2369 | no | not supported |
| L2 | The even-amount preference is stronger for grain than for men | 0.8716 | no | not supported |
| L3 | Amounts on the same tablet are doubles of each other more than chance | 0.0145 | yes | new |
| L4 | KI-RO entries are mostly single units (1) | 0.0005 | yes | confirms |
| L5 | Liquids (wine, oil) take fractions more often than dry goods | 0.7446 | no | not supported |
| M1 | Words ending -TI are entry labels (names) rather than headings | 0.0525 | no | not supported |
| M2 | Words beginning A- are headings rather than entry labels | 0.0005 | yes | new (population-level) |
| M3 | Words ending -JA belong to the religious register | 0.0125 | yes | new |
| M4 | The first and last syllables of a word share their vowel more than chance | 0.7666 | no | not supported |
| M5 | Long words are compounds of attested shorter words more than chance | 0.1996 | no | not supported |
| N1 | Roundels and nodules carry different signs | 0.0005 | yes | new (27 roundel signs) |
| N2 | Sealing signs are the first signs of the commonest administrative words | 0.049 | no | not supported |
| N3 | Religious inscriptions use word dividers more than tablets | 0.0035 | yes | new |
| N4 | After a KU-RO total, the next line opens with a new commodity | 0.5622 | no | not supported |
| N5 | Peak-sanctuary inscriptions share vocabulary with each other more than with other religious objects | 0.0005 | yes | expected (formula) |
| O1 | Knossos words are Linear A words plus one final syllable more often than Pylos words | 0.0005 | yes | new |
| O2 | Knossos names contain Linear A words as stems (plus a Greek ending) beyond chance | 0.007 | yes | new (mostly 2-sign stems) |
| O3 | Cretan place names in Linear B recur in Linear A (as words or stems) more than mainland ones | 0.1124 | no | not supported |
| O4 | Linear A and Linear B use their shared syllables at correlated rates | 0.001 | yes | expected |
| O5 | Pylos names end in -o (Greek o-stems) more often than Knossos names | 1.0 | no | not supported |

**What the round adds.**

- **Minoan stems with Greek endings at Knossos.**
  - Knossos-only Linear B words are a Linear A word plus one final syllable more than twice as often as Pylos words
    (O1: 7.8% against 3.4%, p 0.0005).
  - Among Knossos personal names this exceeds the value-shuffle null (O2, p 0.007). The added endings are
    typically Greek (-no, -ro, -ko, -to): for example a-da-ra-ro on A-DA-RA, sa-ma-ti-ja on SA-MA-TI, ja-sa-ro on JA-SA.
  - 53 of the 56 stems are two-sign words, so single cases prove nothing. The claim is only the excess over chance.
- **The Knossos trace, sharpened:**
  - Knossos-only words are more Linear A-like than words shared with Pylos (K2).
  - At Knossos, names follow Linear A syllable rates more closely than common words do (K3).
  - Cretan place names in Linear B are more Linear A-like than mainland place names (K4).
- **The A- heading question.** Across the corpus, words beginning A- are headings about twice as often as entry
  labels are (M2: 20% against 9%, p 0.0005). The second pass's tentative idea holds as a tendency, although ZA 10a
  shows it is not a rule.
- **Bookkeeping:**
  - KI-RO entries are mostly single units (L4: 25 of 32), consistent with KI-RO lists of owed or missing persons;
  - amounts on one tablet are exact doubles of each other more than chance (L3, p 0.015), which fits the
    even-amount preference of round 9.
- **Register:**
  - words ending -JA lean religious (M3);
  - religious inscriptions use word dividers more (N3);
  - peak-sanctuary inscriptions share vocabulary, as the formula predicts (N5).
- **Not supported:**
  - undeciphered-sign words at Knossos being names in particular (K1);
  - Knossos -jo/-ja adjectives built on Linear A stems (K5);
  - largest-first listing outside Haghia Triada (L1, so a Haghia Triada habit);
  - a stronger even-amount preference for grain (L2);
  - fractions for liquids (L5);
  - -TI names (M1, p 0.053);
  - vowel echo between first and last syllables (M4);
  - compound words (M5);
  - sealing signs as initials of the commonest words (N2, p 0.049 before correction);
  - new commodity after KU-RO (N4);
  - Cretan place names recurring in Linear A (O3).
- **A reversal worth noting (O5):** Knossos names end in -o *more* often than Pylos names (63% against 52%). So the
  final-syllable closeness of round 7 comes from Pylos's many -eus names, not from Knossos endings; the stem-based
  measures (first syllables, internal o-deficit, stems) carry the Minoan signal.

# Eleventh round: ten follow-ups tested hard, 23 September 2026

`reading/vigorous.py`, results in `reading/vigorous_results.json` and `reading/vigorous_output.txt`.

The ten hypotheses build on results that had already held up. Each has a prediction stated before the data were
touched, one primary test with its own null, and at least one robustness check: held-out data, a second null, a
stricter subset, or a control that should fail. Benjamini–Hochberg at 5% runs across the ten primary tests. A
hypothesis counts as supported only if it survives the correction *and* its robustness checks agree.

| # | Hypothesis | primary p | BH 5% | robustness | verdict |
|---|---|---|---|---|---|
| V1 | A model trained on Linear A names against 70% of the Pylos names rates Knossos names as more Minoan than the held-out Pylos names | 0.0025 (AUC 0.59; label-shuffle null 0.50) | yes | common-word control AUC 0.53, interval crosses 0.5 | **supported** |
| V2 | Undeciphered Linear B signs are used at Knossos at rates tracking Linear A frequencies more than at Pylos | 0.082 (rho 0.62 vs 0.33) | no | only 15 signs | not supported |
| V3 | The Linear A stems of Knossos names are Linear A *names* more often than same-length Linear A words | 0.88 (37% vs 44%) | no | Pylos stems 36% | **refuted** |
| V4 | The Knossos stem excess holds for 3+-sign stems, and against Thebes, Mycenae and Tiryns | 0.021 (0.61% vs 0.08%) | yes | against other mainland sites 7.8% vs 6.4%, p 0.17 | **mixed** |
| V5 | Within a stem, the A- form is a heading more often than the bare form | 0.50 (3 vs 2 of 8 pairs) | no | too few pairs | not supported |
| V6 | KI-RO stands on personnel (VIR) tablets more than other tablets with totals | 0.99 (1/12 vs 11/29) | no | opposite direction | **refuted** |
| V7 | The amounts on a tablet share a common divisor above 1 more often than chance | 0.0005 (10.7% vs 5.1%) | yes | without all-tens tablets p 0.021; within-site shuffle p 0.001 | **supported** |
| V8 | Largest-first listing holds scribe by scribe at Haghia Triada | 0.035 (7 of 8 scribes) | no | Scribe 1 the exception | suggestive |
| V9 | Linear A religious words resemble Knossos names more than Pylos names, with the libation-formula words removed | 0.0005 (154 words) | yes | first syllables p 0.0005 | **supported** |
| V10 | Under the published fraction values, attested pairs break largest-first far less than under random reassignments | 0.022 (2 vs 12.5) | yes | circular: the values were partly set by this premise | not counted |

**What the round adds.**

- **The Knossos name result predicts out of sample (V1).** A model that never saw a Knossos name, and never saw the
  Pylos names it was tested on, still ranks Knossos names as more Minoan (AUC 0.59, p 0.0025 against a label
  shuffle). The same model does not separate common words at the two sites (AUC 0.53). This is the strongest check
  yet on the name-shape finding of round 7: it cannot be an artefact of fitting.
- **The religious-word resemblance is not the formula (V9).** With the libation-formula words (A-TA-I-*301-WA-JA,
  JA-SA-SA-RA-ME, U-NA-KA-NA-SI, I-PI-NA-MA, SI-RU-TE, DI-KI-TE and the rest) removed, 154 religious words remain
  closer to Knossos names than to Pylos names (p 0.0005, first syllables likewise). The resemblance is to Minoan
  word shapes in general, as the ninth round suggested.
- **Tablets have a working unit (V7).** Amounts on one tablet share a common divisor above 1 about twice as often
  as amounts shuffled between tablets (10.7% against 5.1%). The shuffle keeps each amount, so the general preference
  for even amounts cannot produce this; the effect survives with all-tens tablets removed (p 0.021) and with amounts
  shuffled only within their site (p 0.001). Most such tablets are all-even (divisor 2: 11 tablets), so some lists
  were kept in pairs or halves.
- **The stem result needs a caveat (V3, V4).**
  - Restricted to stems of three or more signs, Knossos still beats Pylos (0.61% against 0.08%, p 0.021), so the
    two-sign worry of round 10 does not explain it away.
  - Against Thebes, Mycenae and Tiryns the Knossos excess is small and not significant (7.8% against 6.4%, p 0.17).
    Part of the round-10 contrast is Pylos being low, not only Knossos being high.
  - The Linear A words that serve as stems are not especially Linear A names (V3). The stems look like Linear A
    words in general.
- **Refuted or not supported:**
  - KI-RO is *rarer* on personnel tablets (V6: 1 of 12 KI-RO tablets carry VIR, against 11 of 29 other tablets
    with totals). The round-10 reading of KI-RO lists as owed persons is not supported. The all-ones entries are
    more likely single items or animals.
  - The paired A- test has only eight pairs and splits 3 to 2 (V5).
  - The undeciphered-sign correlation points the right way but 15 signs are too few (V2, p 0.08).
  - Largest-first holds in 7 of 8 Haghia Triada scribes (V8, p 0.035), just short of the correction.
- **V10 is not evidence.** The published fraction values produce only two order breaks (H K on HT 34 and A B)
  where random values produce 12.5 on average. Corazza et al. used the descending-order premise in setting some of
  those values, so the agreement is partly built in. The test is kept to show that it was run.

# Twelfth round: ten more follow-ups tested hard, 24 September 2026

`reading/vigorous2.py`, results in `reading/vigorous2_results.json` and `reading/vigorous2_output.txt`.

Same rules as the eleventh round. Each hypothesis was stated before its test ran and has one primary test with its
own null plus robustness checks. Benjamini–Hochberg at 5% runs across the ten. A hypothesis counts as supported
only when the robustness checks agree with the primary test. Three of the checks (the W2 variant without Knossos,
the neutral model in W4, the Pylos comparison in W10) were added after the first run, when the first results
raised the worry each one addresses. They are reported as checks, not as new primary tests.

| # | Hypothesis | primary p | BH 5% | robustness | verdict |
|---|---|---|---|---|---|
| W1 | The V1 model rates Knossos names above Thebes/Mycenae/Tiryns names it never saw | 0.074 (AUC 0.57, 46 mainland names) | no | Pylos-free model AUC 0.58, p 0.033 | suggestive |
| W2 | A model trained on Linear A names from sites other than Haghia Triada still separates Knossos from Pylos names | 0.0033 (AUC 0.61, 130 names) | yes | HT-only model 0.59, p 0.0033; without Knossos Linear A names 0.61, p 0.0033 | **supported** |
| W3 | Names in the earliest Knossos deposit (Room of Chariot Tablets) are more Minoan than later Knossos names | 0.94 (AUC 0.44) | no | RCT-any 0.43, p 0.97; JSD tests point the same way | **refuted** |
| W4 | Knossos words written with undeciphered signs are Linear A-like in their other syllables | 0.015 (AUC 0.58, 73 words) | yes | neutral reference model: Knossos 0.56, p 0.027; Pylos 0.55, p 0.17 (29 words) | **supported** (site contrast open) |
| W5 | The internal o-deficit holds against Thebes/Mycenae/Tiryns names | 0.097 (12.3% vs 16.7%) | no | against Pylos p 0.0045 (replicated) | suggestive |
| W6 | A model trained on Linear A *religious* words picks out Knossos names out of sample | 0.0033 (AUC 0.60, 183 words) | yes | formula words removed: 0.61, p 0.0033 | **supported** |
| W7 | Common-divisor tablets are single-commodity lists more often | 0.49 (15/19 vs 120/159) | no | without all-tens tablets p 0.55 | not supported |
| W8 | KI-RO stands on produce tablets more than other total tablets | 0.80 (4/12 vs 12/29) | no | Haghia Triada only p 0.79 | not supported |
| W9 | Largest-first at Haghia Triada holds without the scribe who wrote most lists (Scribe 9) | 0.0135 (mean tau 0.17, 46 lists) | yes | every leave-one-scribe-out p ≤ 0.013; all scribes p 0.0015 | **supported** |
| W10 | Linear A words used as stems of Knossos words are attested at more Linear A sites | 0.0085 (1.27 vs 1.16 sites) | yes | Pylos stems 1.25 (p 0.13); Knossos vs Pylos stems p 0.47 | **mixed** (not Knossos-specific) |

**What the round adds.**

- **The name result does not depend on one Linear A site (W2).** Haghia Triada supplies most Linear A names. A
  model trained only on the 130 names from the other eleven sites, or only on those from Haghia Triada, separates
  Knossos from Pylos names equally well (AUC 0.61 and 0.59). The effect also survives with the Linear A names found
  at Knossos removed from training, so it is not Knossian material recognising itself.
- **Religious words alone carry the signal (W6).** A model that never saw a Linear A list name, trained only on
  religious words, still ranks Knossos names above held-out Pylos names (AUC 0.60), and does so equally well with
  the libation formula removed. The Minoan shape is a property of the language's words in general, not of its
  naming habits. This supports the ninth- and eleventh-round findings from an independent direction.
- **Undeciphered signs sit in Minoan-shaped words (W4).** With the undeciphered signs removed, the remaining
  syllables of the 73 Knossos words that use them are more Linear A-like than ordinary Knossos words (neutral
  reference, p 0.027). Pylos shows a similar but non-significant tendency on only 29 words. The data support "these
  signs write Minoan words" but cannot say whether that is special to Knossos.
- **Largest-first is a shared Haghia Triada practice (W9).** A within-list order shuffle keeps each list's amounts
  and removes only the order. Largest-first then survives the removal of any single scribe (every p ≤ 0.013). This
  answers the V8 worry: the habit is not one scribe's.
- **Two results are narrower than hoped:**
  - Against Thebes, Mycenae and Tiryns (only 46 names), Knossos names are more Minoan in the same direction but not
    significantly (W1, p 0.074; with a Pylos-free model p 0.033). The o-deficit also points the same way but is
    not significant (W5, p 0.097). The Knossos–mainland contrast is clear against Pylos and suggestive elsewhere,
    limited by the small mainland name stock.
  - The stems that link Linear A to Linear B favour widespread Linear A words, but Pylos stems do too (W10). This
    is a property of stem-matching in general, likely because common words match more easily, and is not evidence
    for Knossos.
- **A refutation worth noting (W3).** Names in the Room of Chariot Tablets, the earliest Knossos archive
  (LM II–IIIA1), are *not* more Minoan than names in the later deposits; if anything they are less so (AUC 0.44).
  The RCT tablets deal with chariots, armour and men. A plausible reading is that this archive records a newer,
  more Greek-named military group, while Minoan names persist in the later, wider administration. That is an
  interpretation, not a test.
- **Bookkeeping follow-ups failed:** common-divisor tablets are not especially single-commodity lists (W7), and
  KI-RO is not especially on produce tablets (W8). KI-RO's commodity profile stays unexplained.

# Thirteenth round: ten hypotheses aimed at reading the script, 24 September 2026

`reading/decipher10.py`, results in `reading/decipher10_results.json` and `reading/decipher10_output.txt`; the
per-row analysis is in `reading/decipher10_rows.txt` and `reading/decipher10_rows.json`.

The earlier rounds mostly characterised Linear A. This round aims at reading it: sound values, inflection, the
identity of shared undeciphered signs, and word meanings. Each hypothesis has a prediction stated before its test
ran and one primary test with its own null. Where the method can be run on Linear B, which is deciphered, it is:
a method that fails on Linear B cannot be trusted on Linear A. Benjamini–Hochberg at 5% runs across the ten.

| # | Hypothesis | primary p | BH 5% | Linear B control / robustness | verdict |
|---|---|---|---|---|---|
| Y1 | Linear A signs sharing a Linear B consonant have more similar contexts than other signs | 0.0005 (diff 0.075, 48 signs) | yes | Linear B 0.051, p 0.0035; see the checks below | **supported** |
| Y2 | When two Linear A words differ only in the final sign, the finals share a consonant (Kober's bridge) | 0.082 (12.9% vs 7.8%, 62 pairs) | no | Linear B 18.7% vs 7.1%, p 0.002 | suggestive (underpowered) |
| Y3 | Stems take two or more finals more often than with finals reassigned | 0.28 (46 vs 44.8 stems) | no | Linear B 636 vs 613, p 0.002 | not supported |
| Y4 | A hidden sign's consonant row or vowel column is predicted from context | 0.020 (Bonferroni over the two parts) | no | vowel 42% vs 20% (p 0.01), consonant 15% vs 7% (p 0.09); Linear B vowel 53%, consonant 8.5% | suggestive (vowels) |
| Y5 | Context-predicted values turn unread-sign words into Linear B words more than random values | 0.35 (10 vs 8.7 matches, 15 signs) | no | — | not supported |
| Y6 | Linear A words with *34, *47, *49, *86 share neighbours with Linear B words holding the same sign | 0.15 (2 vs 0.75 words) | no | no exact word matches | not supported (21 words) |
| Y7 | The syllable ligatured to a commodity sign begins a word on the same tablet (acrophony) | 0.37 (14/169 vs 12.7) | no | non-initial position 20 vs 14.6, p 0.08 | not supported |
| Y8 | More words are bound to a single commodity than chance allows | 0.047 (2 pairs vs 0.4) | no | KU-RO–VIR, SA-RA2–OLE | not supported after correction |
| Y9 | Linear A words on a commodity's tablets resemble the Linear B words for it | 0.43 (4 vs 3.4) | no | KU-PA-ZU/ku-pa-ro (CYP) among them | not supported |
| Y10 | A- is a prefix: pairs A-X / X commoner than chance | 0.56 (11 vs 11.0) | no | I- 8 vs 4.9, p 0.10 | **refuted** |

**What the round adds.**

- **The Linear B consonant rows are real sound classes in Linear A (Y1).** Signs that Linear B puts in the same
  consonant row (NA, NE, NI, NU; RA, RE, RI, RO, RU; and so on) keep more similar company in Linear A words than
  signs in different rows. This is a test of the sound values that does not depend on any Linear A word being
  known. The effect is at least as large in Linear A as in Linear B itself (0.075 against 0.051). It survives every
  check:
  - with the neighbours that share the sign's own consonant removed, so it is not consonant harmony or
    reduplication (0.081, p 0.0005);
  - with the pure-vowel row and the word-boundary features removed, so it is not the vowels' word-initial habit
    (0.067, p 0.0005);
  - at Haghia Triada alone (0.102, p 0.0005) and at the other sites alone (0.045, p 0.0045).

  This supports the convention of reading Linear A with Linear B values. The 2,000-shuffle test of round 1 showed
  that the values produce real words; this shows that the rows of the grid behave as sound classes, a separate
  and stronger line of evidence.
- **Which rows cohere (exploratory, `decipher10_rows.txt`).** In Linear A the Q, N and R rows and the pure vowels
  hang together most strongly; T, S and M hardly at all. The **Z row (ZA, ZU) is the one row that does not cohere
  at all**, and ZU fits its row worst of all 48 signs. Linear B's Z series is among its least certain values (a
  sibilant or affricate, /ts/ or /dz/), so this is where a different Minoan value is most likely. The nearest rows
  for ZU (D, T, P, K) are too close together to propose a replacement.
- **Vowels can be recovered from context (Y4).** With a known sign hidden, its vowel is predicted correctly 42% of
  the time against 20% by chance (p 0.01), close to the 53% the same method reaches on Linear B. Consonants are
  not recovered in either script, so the method cannot yet place an unread sign. Its value predictions for *301,
  *118, *21F and the rest (Y5) produce no more Linear B words than random values. The predictions are recorded in
  the results file, but they are not readings.
- **No evidence that A- is a prefix (Y10).** Pairs such as A-SA-SA-RA-ME / SA-SA-RA-ME or A-KA-RU / KA-RU occur
  exactly as often as random initial signs would produce (11 against 11.0). The idea of a prefix A- rests on
  examples that chance explains. The heading preference of A- words (round 10) stands. It may reflect particular
  words rather than a morpheme.
- **Inflection is not visible at this corpus size (Y2, Y3).** In Linear B the same tests detect inflection
  easily. In Linear A, final alternations lean towards sharing a consonant (12.9% against 7.8%) but are not
  significant on 62 pairs, and stems take multiple endings no more than chance. Either Linear A inflected little
  at word ends, or 959 word types are too few. Linear B, with 5,000 types, shows the effect clearly.
- **Word meanings: nothing new survives (Y6–Y9).** The shared undeciphered signs are too rare to identify across
  scripts (21 Linear A words). Acrophony does not appear in the commodity ligatures. Only two word–commodity bonds
  stand out (KU-RO with men, SA-RA2 with oil), and they do not survive the correction. Close matches to Linear B
  commodity words, such as KU-PA-ZU on a cyperus tablet against Linear B ku-pa-ro, are no commoner than chance.

# Fourteenth round: ten more hypotheses on sound values and vowels, 24 September 2026

`reading/decipher10b.py`, results in `reading/decipher10b_results.json` and `reading/decipher10b_output.txt`.

This round builds on the thirteenth round's positive result (the Linear B consonant rows behave as sound classes
in Linear A) and its open ends (the Z row, value recovery, vowels). The rules are the same: a prediction stated
before the test ran, one primary test, a Linear B control wherever possible, and Benjamini–Hochberg at 5% across
the ten. **None of the ten survives the correction.** The Linear A vs Linear B contrast in Z5 and Z6 was added
after the first run and is exploratory.

| # | Hypothesis | primary p | BH 5% | Linear B control / robustness | verdict |
|---|---|---|---|---|---|
| Z1 | PA3, RA2, PU2, TA2 (and AU) sit nearest the row their Linear B value gives them | 0.071 (mean rank 0.34 of 1) | no | Linear B 0.30, p 0.0016; AU rank 1, RA2 and TA2 rank 3, PU2 6, PA3 9 of 13 | suggestive |
| Z2 | Nearest neighbours on weighted co-occurrence scores (PPMI) recover a hidden sign's consonant row | 0.44 (8% vs 7%) | no | Linear B 27% consonants, 53% vowels; Linear A vowels 33% vs 20%, p 0.07 | not supported |
| Z3 | ZA, ZU keep company with the S, T, D rows | 0.19 | no | Linear B p 0.51 | not supported |
| Z4 | Rows sharing a place of articulation have more similar signs | 0.054 | no | Linear B −0.010, p 0.64: the method fails its control | not interpretable |
| Z5 | O and U merged: within a row CO behaves like CU | 0.15 (+0.064) | no | Linear B −0.125; LA minus LB 0.19, p 0.014 (exploratory) | suggestive |
| Z6 | E and I merged: within a row CE behaves like CI | 0.048 (+0.060) | no | Linear B −0.153; LA minus LB 0.21, p 0.003 (exploratory) | suggestive |
| Z7 | Words differing in one internal sign differ by a close sound | 0.73 (37% vs 39%) | no | Linear B 36% vs 30%, p 0.003 | not supported |
| Z8 | Vowel harmony between neighbouring syllables | 0.68 (27.3% vs 27.8%) | no | Linear B 28.1% vs 22.6%, p 0.002 | **refuted** for Linear A |
| Z9 | Nearest-neighbour value predictions for unread signs yield Linear B words | 1.0 (2 vs 8.7) | no | — | not supported |
| Z10 | Vowel signs stand inside words more often in Linear A than in Linear B | 1.0 (30% vs 44%) | no | reversed; E is the exception (57% vs 27%) | **refuted** |

**What the round adds.**

- **The consonant-row signal is real but diffuse.** The thirteenth round showed that same-row signs are more alike
  on average. This round shows that the signal is too weak to place any single sign. Nearest neighbours recover
  27% of consonants in Linear B but only 8% in Linear A, which is chance (Z2). Value predictions for the unread
  signs, by either method, produce no more Linear B words than random values (Y5, Z9). With this corpus, context
  alone cannot assign values.
- **The special signs point the right way (Z1, p 0.07).** AU sits nearest the vowel row, and RA2 and TA2 rank
  third of 13 for their rows. PA3 does not fit the P row (9th of 13), which matters because PA3's Linear B value is
  itself uncertain. The four signs are too few to settle it.
- **A lead on the Minoan vowels (Z5, Z6, exploratory).**
  - In Linear B, the e-sign and the i-sign of one consonant row (DE/DI, KE/KI, TE/TI …) are clearly *unlike* each
    other in context, and so are the o- and u-signs. Greek uses those vowels to tell endings apart.
  - In Linear A the same pairs lean the other way: CE is more like CI than like CA or CO, and CO more like CU.
  - Compared row by row, Linear A differs from Linear B in both pairs (e/i p 0.003, o/u p 0.014).
  - This fits a Minoan vowel system in which e and o were marginal or merged with i and u. The o-deficit (2.8% of
    syllables against 26% in Linear B) points the same way, and three-vowel systems have been proposed for
    Minoan on other grounds.
  - Caveat: Linear B's contrast comes partly from Greek case endings, so the comparison may measure Greek
    morphology as much as Minoan phonology. The within-Linear A tests (Z5 p 0.15, Z6 p 0.048) do not survive the
    correction.
- **Linear A does not show Linear B's small-scale patterns.** Vowel harmony (Z8) and phonetically close spelling
  alternations (Z7) are both clear in Linear B and absent in Linear A. The Linear A alternations that exist are
  mostly different words, not spelling variants.
- **Vowel signs inside words (Z10) run the other way:** 30% of Linear A vowel-sign occurrences are word-internal
  against 44% in Linear B, where Greek -e-u and -a-i diphthongs account for many. E is the exception, internal 57%
  of the time in Linear A against 27% in Linear B.

# Fifteenth round: the vowel lead tested on fresh data, and vowel-free matching, 24 September 2026

`reading/decipher10c.py`, results in `reading/decipher10c_results.json` and `reading/decipher10c_output.txt`.

The fourteenth round's exploratory lead was that Linear A's e/i and o/u sign pairs behave more alike than Linear
B's, as they would if Minoan had marginal e and o. A1–A6 test predictions of that idea on data the lead did not
use. A7–A10 match words by consonant skeleton (vowels ignored), which such a vowel system would favour. The rules
are the same as before: a prediction stated before the test ran, one primary test, Linear B controls, and
Benjamini–Hochberg at 5% across the ten. The robustness checks for A5 and A7 were added after the first run.

| # | Hypothesis | primary p | BH 5% | control / robustness | verdict |
|---|---|---|---|---|---|
| A1 | Knossos name variants alternate e/i or o/u more than Pylos name variants | 0.11 (24% of 33 vs 0% of 9) | no | too few Pylos pairs | suggestive |
| A2 | One-vowel near matches between Linear A and Linear B words are e/i or o/u more than expected | 0.63 (16.7% vs 17.1%, 634 pairs) | no | — | **refuted** |
| A3 | Linear A internal one-vowel alternations are e/i or o/u more than expected | 0.19 (13.6% vs 9.9%, 66 pairs) | no | Linear B 17.2% vs 10.5%, p 0.0005 | not supported |
| A4 | Across rows, e-signs resemble i-signs and o-signs u-signs | 0.26 | no | Linear B −0.067 | not supported |
| A5 | Knossos names have fewer internal e-syllables than Pylos names | 0.0005 (16.4% vs 25.5%) | yes | -e-u names removed p 0.001; first syllables p 0.011; common words p 0.15 | **supported** |
| A6 | Linear A final one-vowel alternations are e/i or o/u more than expected | 0.018 (16.9% vs 10.3%, 89 pairs) | no (just) | Linear B 10.8% vs 9.3%, p 0.07 | suggestive |
| A7 | Knossos names skeleton-match Linear A words more than Pylos names, beyond exact matches | 0.005 (16.6% vs 9.9%) | yes | common words reversed (p 0.89); 3-sign p 0.051, 4+ p 0.28 | **supported** (not independent of the name-shape result) |
| A8 | Linear A religious words skeleton-match Linear B religious words more than administrative words do | 0.43 (1.6% vs 0.9%) | no | matches DA-MA-TE, U-TI-NU | not supported |
| A9 | Linear A headings skeleton-match Linear B place names more than entry words do | 0.21 (8.3% vs 4.9%) | no | — | not supported |
| A10 | Linear A entry words skeleton-match Linear B personal names more than headings do | 0.81 (28.7% vs 33.3%) | no | — | **refuted** |

**What the round adds.**

- **Knossos names also lack e (A5).** Linear A uses few e-syllables inside words (10.4%, against 24.3% in Linear
  B). Knossos personal names sit between the two (16.4%), clearly below Pylos names (25.5%, p 0.0005). The gap
  survives without the -e-u names (p 0.001) and in first syllables alone (p 0.011). The common vocabulary of the two
  sites shows no such gap (p 0.15). This parallels the o-deficit of round 7 (12.3% against 16.5%). Minoan-derived
  names at Knossos therefore carry both of Linear A's vowel shortages, e and o, while their i-share is higher
  (21.0% against 15.8%). This is independent support for a Minoan vowel system in which e and o were rare,
  whatever their phonetic value.
- **But the "merger" form of the idea is not supported.** If e and i were one sound, spellings should swap them.
  Linear A–Linear B near matches that differ in one vowel are e/i or o/u no more often than chance (A2, 634
  pairs). Within Linear A, internal alternations show no excess (A3), and neither do contexts across rows (A4).
  Final alternations lean that way (A6, p 0.018) but do not survive the correction. The better-supported
  statement is that e and o were *rare* in Minoan. It is not shown that they were *interchangeable* with i and u.
- **Vowel-free matching finds no meanings.** Skeleton matches are enriched for Knossos names (A7), which restates
  the Minoan shape of those names rather than adding to it. Religious words do not find Linear B religious
  counterparts (A8; the one clean match, DA-MA-TE, is an exact match already known). Headings do not match place
  names (A9), and entry labels do not match personal names better than headings do (A10). At three signs,
  skeleton matching is too permissive (29% of entries find some Linear B name) to separate meaning from chance.

# Sixteenth round: rare vowels, name models, and the accounting signs, 24 September 2026

`reading/decipher10d.py`, results in `reading/decipher10d_results.json` and `reading/decipher10d_output.txt`.

This round builds on the fifteenth round's result that Minoan-derived names at Knossos lack e and o as Linear A
does. It asks where Linear A's rare vowels sit, whether other Minoan words in Linear B show the same deficit,
whether a Knossos name model recognises Linear A names, and what the single signs and ligatures on the tablets are.
The rules are the same as before; the robustness checks for B2 and B10 were added after the first run.

| # | Hypothesis | primary p | BH 5% | control / robustness | verdict |
|---|---|---|---|---|---|
| B1 | e/o-signs occur in fewer distinct words per occurrence than a/i/u-signs | 0.22 | no | Linear B p 0.044 | not supported |
| B2 | e/o-signs stand word-finally more often than a/i/u-signs | 0.0015 (50% vs 34%) | yes | Linear B the same (36% vs 18%); word types p 0.0025; commonest words removed p 0.0025 | **supported** (not specific to Minoan) |
| B3 | Words with e/o-signs are attested at fewer sites (frequency held fixed) | 0.17 | no | 1.06 vs 1.11 sites | not supported |
| B4 | A Knossos name model scores Linear A entry labels above headings | 0.027 (AUC 0.56) | no | Pylos-trained model 0.48 | not supported |
| B5 | The same model scores religious words above non-label administrative words | 0.54 | no | — | not supported |
| B6 | Single signs abbreviate words on the same tablet (first sign) | 0.37 (25/429 vs 23.1) | no | non-initial matches 47 vs 32, p 0.003 | **refuted** as acrophony |
| B7 | Single signs are bound to particular commodities | 0.067 | no | NI occurs with every commodity | not supported |
| B8 | Linear A and Linear B share (commodity, syllable) ligatures beyond chance | 0.51 (2 vs 1.6) | no | shared: OLE+RA, TELA+KU | not supported |
| B9 | Knossos names begin with a pure vowel more often than Pylos names | 0.87 | no | — | **refuted** |
| B10 | Knossos-only place names and ethnics have fewer e/o-syllables than Pylos-only ones | 0.0005 (21% vs 42%) | yes | whole words p 0.0075; against Thebes/Mycenae/Tiryns p 0.013; common words 46% vs 50%, p 0.075 | **supported** |

**What the round adds.**

- **Cretan place names lack e and o too (B10).** With the Greek ending removed, place names and ethnics attested
  only at Knossos use e- or o-syllables 21% of the time, against 42% for those attested only at Pylos and 48% for
  Thebes, Mycenae and Tiryns (Linear A: 18%). The common vocabulary of the two sites differs little (46% against
  50%). Personal names (rounds 7 and 15) and place names now both carry Linear A's vowel profile at Knossos. The
  rarity of e and o is a property of Minoan words in general, visible even through Greek spelling.
- **Linear A's e and o live in endings (B2).** Half of all occurrences of e/o-signs are word-final, against a third
  for a/i/u-signs. The pattern holds counting each word once and without the commonest words. The e-signs are the
  clearest: NE 73%, ME 68%, TE 61%, RE 49% word-final. Linear B shows the same general pattern because of Greek
  endings, so this does not identify the language. It does suggest that Minoan e appeared mainly in suffixes
  (-NE, -ME, -TE, as in JA-SA-SA-RA-ME and A-DI-KI-TE-TE), which fits a language where e was marginal in roots.
- **Single signs are not abbreviations of nearby words (B6).** They match the first sign of a word on the same
  tablet no more than chance, but they match *later* signs more than chance (47 against 32). They are part of the
  vocabulary of the lists, not initials. NI stands with every commodity (B7), which fits its proposed reading as
  the fig or a generic unit, not a commodity marker.
- **No continuity in ligatures (B8), no name model transfer (B4, B5), no vowel-initial excess (B9).** A model
  trained on Knossos names against Knossos common words ranks Linear A entry labels slightly above headings
  (p 0.027, not surviving), but the same model trained at Pylos does not, so the functional reading of entry
  labels as names gets no independent support from Linear B.

# Seventeenth round: the Minoan vowel profile beyond Linear A, 24 September 2026

`reading/decipher10e.py`, results in `reading/decipher10e_results.json` and `reading/decipher10e_output.txt`.

The fifteenth and sixteenth rounds showed that Linear A, Knossos personal names and Cretan place names all lack e
and o. This round asks whether the profile appears in the other records of Minoan and its neighbours
(Pre-Greek, Eteocretan, Cretan Hieroglyphic), whether it picks out candidate languages, and how e and o behave
inside Linear A. Every language is counted through the same Linear B-style spelling. The rules are the same as
before. Several first-run problems were caught and fixed before the results below:
- the Hittite word list had been read from cuneiform headwords, which produced a meaningless profile, so it is now
  read from the romanised forms;
- the combined e/o figure for C1 and C2 is now split by vowel;
- checks were added for C8 (formula words removed, -TE alone) and C10 (internal positions only, Q row removed,
  rows without e/o signs removed).

| # | Hypothesis | primary p | BH 5% | robustness | verdict |
|---|---|---|---|---|---|
| C1 | Pre-Greek substrate words use fewer e/o vowels than length-matched Greek words | 0.0005 (46.8% vs 52.1%) | yes | stems: e 17.5% vs 28.1%, o 16.3% vs 20.6%, each p 0.0005; a 34% vs 23% | **supported** |
| C2 | Eteocretan uses fewer e/o vowels than Greek | 0.0045 (38% vs 53%) | yes | the deficit is o (10.6% vs 26.8%); e is as in Greek (27% vs 26%); 35 pieces | supported (o only; tiny corpus) |
| C3 | Hieroglyphic groups read with Linear A values have a lower e/o share than Linear B | 0.013 (36% vs 49%) | yes | but higher than Linear A (18%, p 0.0015); only 20 readable groups | inconclusive |
| C4 | Linear A's vowel profile is closer to Luwian than to Hittite | 1.0 | no | closest overall: Hittite 0.021, Hawaiian 0.027, Maori 0.027, Etruscan 0.028 | **refuted**: vowel profiles do not pick out a language |
| C5 | Knossos names without a Greek etymology have fewer e/o syllables | 0.031 (27.6% vs 33.9%) | yes | — | supported |
| C6 | Pylos names without a Greek etymology have fewer e/o syllables | 0.045 (40.1% vs 47.2%) | no | — | suggestive |
| C7 | Linear B words with undeciphered signs have fewer e/o among their readable signs | 0.021 (44.4% vs 49.2%) | yes | — | supported |
| C8 | Linear A words ending in an e-sign lean to the religious register | 0.016 (28.4% vs 20.2%) | yes | formula removed p 0.012; -TE alone 9.5% vs 4.1%, p 0.0085 | **supported** |
| C9 | Within rows Linear A favours i and u over a more than Linear B | 0.19 (8 of 12 rows) | no | — | not supported |
| C10 | Linear A e/o depend on the consonant more than Linear B e/o do | 0.001 (NMI 0.090 vs 0.020) | yes | internal only p 0.002; Q removed p 0.002; rows with e/o signs only p 0.002 | **supported** |

**What the round adds.**

- **Pre-Greek shares the profile (C1).** Beekes's Pre-Greek words, the substrate vocabulary that Greek took from
  the languages of the Aegean before it, use fewer e- and o-vowels in their stems than ordinary Greek words of the
  same length. For e the figures are 17.5% against 28.1%, for o 16.3% against 20.6%, and a is correspondingly
  higher (34% against 23%). This is the direction of Linear A (e 14.6%, o 3.2%, a 40%). It links the Aegean
  substrate in Greek to the Minoan vowel profile without depending on any single word match. One caution:
  Beekes's criteria for Pre-Greek include some vowel alternations, which could favour a in his list.
- **Eteocretan lacks o, not e (C2).** In the five short Eteocretan inscriptions, o is rare (10.6% against 26.8% in
  Greek) but e is not (27%). The corpus is tiny and its spelling uncertain, so this is only consistent with a
  Minoan descendant.
- **Linear A's e and o are consonant-conditioned (C10).** They occur mostly after Q, R, T and S (QE/QO half the
  time, R 37%, T 28%, S 19%). They are rare after P and J (7%) and absent after W and Z. The dependence is four times
  Linear B's and survives every check, including restriction to word-internal syllables. Minoan e and o may have
  been conditioned variants of other vowels after certain consonants, or confined to particular suffixes (-RE,
  -TE, -QE). This is the first structural statement about the Minoan vowel system these tests have produced.
- **Religious words end in -TE (C8).** Words ending in an e-sign are commoner in the religious register (28%
  against 20%), with or without the libation formula. The -TE ending alone doubles (9.5% against 4.1%): A-DI-KI-TE,
  DA-MA-TE, I-DA-MA-TE, A-RO-TE. DI-KI-TE and I-DA-MA-TE contain the mountain names Dikte and Ida, so -TE may mark
  place or divine epithets in dedications.
- **Non-Greek names carry the profile (C5, C7; C6 suggestive).** At Knossos, names with no Greek etymology have
  fewer e/o syllables than Greek-etymology names. Linear B words written with undeciphered signs have fewer e/o
  among their readable signs. At Pylos the non-Greek names point the same way (p 0.045).
- **Vowel profiles do not identify the language (C4).** Linear A's profile is as close to Hawaiian and Maori as to
  any proposed candidate, and closest to Hittite once the Hittite list is read correctly. A shortage of e and o is
  typologically common. It characterises Minoan but cannot choose between families. Hieroglyphic (C3) is
  inconclusive on 20 readable groups.

# Eighteenth round: twenty-five hypotheses, 24 September 2026

`reading/decipher25.py` (results in `reading/decipher25_results.json`, `reading/decipher25_output.txt`), with
robustness checks for the survivors in `reading/decipher25_checks.py` (`reading/decipher25_checks.json`).

Twenty-five hypotheses built on the supported results so far: the vowel profile and its consonant conditioning,
the Pre-Greek parallel, the -TE religious words, the consonant rows, the Knossos names, and the bookkeeping habits.
Each had a prediction stated before the test ran and one primary test; Benjamini–Hochberg at 5% runs across all
25. Five survived the correction. The checks run on them afterwards showed that two were artefacts:
- women's names end in -a (D13);
- the S/T effect rests on two-sign words (D8).

They also showed that sides a and b of one tablet had been counted as two tablets, so D20 and D22 were rerun on
whole tablets.

| # | Hypothesis | primary p | BH | check | verdict |
|---|---|---|---|---|---|
| D1 | Linear A e/o prefer coronals more than Linear B e/o | 0.001 (logOR 0.72 vs −0.25) | yes | internal syllables only p 0.001; e/o 22.5% after coronals vs 12.4% | **supported** |
| D2 | Pre-Greek stems prefer e/o after coronals more than Greek | 0.996 | no | reversed (−0.33 vs 0.02) | **refuted** |
| D3 | Knossos names prefer e/o after coronals more than Pylos names | 0.63 | no | — | not supported |
| D4 | Linear A e/o by consonant correlate with Pre-Greek more than with Greek | 0.98 | no | rho −0.62 vs 0.00 | **refuted** |
| D5 | -TE is a suffix (X-TE with X attested) | 0.83 | no | 17.6% vs 22.7% | not supported |
| D6 | -JA is a suffix | 0.44 | no | — | not supported |
| D7 | -NE is a suffix | 0.81 | no | — | not supported |
| D8 | s and t alternate | 0.001 (13 vs 3.6) | yes | top of 53 consonant pairs, but words of 3+ signs give 1 pair (U-NA-RU-KA-NA-SI/-TI); Linear B shows it too | weak (short words) |
| D9 | z and s alternate | 0.070 (2 vs 0.4) | no | — | suggestive |
| D10 | Sonorant rows cohere more than obstruent rows | 0.29 | no | — | not supported |
| D11 | Doublet signs (RA/RA2 …) differ in word position | 0.24 | no | — | not supported |
| D12 | Special signs commoner in entry labels than headings | 0.76 | no | — | not supported |
| D13 | Knossos names on women's (MUL) tablets are more Minoan-shaped | 0.002 (AUC 0.62) | yes | final syllable removed AUC 0.53, p 0.24; 36% of MUL names end in -a vs 17% | **artefact** |
| D14 | Knossos names on sheep (OVIS) tablets are more Minoan-shaped | 0.43 | no | — | not supported |
| D15 | Names beside Cretan place names are more Minoan-shaped | 0.17 | no | — | not supported |
| D16 | Hapax Knossos names are more Minoan-shaped | 0.38 | no | — | not supported |
| D17 | Common-divisor tablets cluster by scribe | 0.43 | no | — | not supported |
| D18 | Tablets sharing a heading share a commodity | 0.52 | no | 15 pairs | not supported |
| D19 | The same entry word carries similar amounts on different tablets | 0.93 | no | amounts differ *more* than chance | **refuted** |
| D20 | Recurring entry words stay with the same scribe | 0.002 (17.8% vs 6.2%) | yes | transaction terms removed 21.8% vs 6.2%; HT only 22% vs 9%; sides merged 17.6% vs 4.4%, p 0.002 | **supported** |
| D21 | Recurring entry words stay with the same commodity | 0.12 | no | — | not supported |
| D22 | Recurring entry words recur together (teams) | 0.001 (26 vs 3.2) | yes | sides merged, terms removed: 13 vs 1.5, p 0.001, carried by HT 86 + HT 95 and ZA 4 + ZA 15 | **supported** (recopied lists) |
| D23 | Pre-Greek first consonants resemble Linear A more than Greek | 1.0 | no | reversed | **refuted** |
| D24 | Linear A word lengths resemble Pre-Greek stems more than Greek | 1.0 | no | reversed | **refuted** |
| D25 | Knossos common words without a Greek etymology have fewer e/o | 0.027 (44.5% vs 52.8%) | no | — | suggestive |

**What the round adds.**

- **Minoan e and o come after coronal consonants (D1).** In Linear A, e/o follow T, D, N, R, S and Z in 22.5% of
  syllables and the other consonants in 12.4%. In Linear B the relation is slightly the other way. The effect holds
  inside the word, away from suffixes (p 0.001). Minoan e and o were likely conditioned by the preceding coronal:
  either lowered variants of i and u after dentals, or confined to dental-initial syllables.
- **The Pre-Greek parallel is limited to the vowel shortage (D2, D4, D23, D24).** Pre-Greek words lack e and o
  like Linear A (round 17), but their e/o do not prefer coronals, their consonant-by-consonant profile runs against
  Linear A's, and their first consonants and lengths are no closer to Linear A than ordinary Greek's. The shared
  shortage is real, but it is not a shared phonology in detail.
- **Persons stay with one scribe (D20).** An entry word that recurs on several tablets is written by the same
  scribe 18% of the time, against 4% if scribes were assigned at random. This holds with transaction terms
  removed, at Haghia Triada alone, and with the sides of each tablet merged. Scribes kept their own people, or
  their own sections of the administration.
- **Some lists were written twice (D22).** Groups of entry words recur together on HT 86 and HT 95 (six word
  pairs) and on ZA 4 and ZA 15, far more than chance. These are recopied or parallel lists rather than working
  teams. The HT 86/95 parallel is known. ZA 4/15 is worth checking as a second pair.
- **Two apparent results were artefacts.** Names on women's tablets at Knossos looked Minoan (D13), but only
  because women's names end in -a, which is Linear A's commonest vowel. Without the final syllable there is no
  effect. S/T alternation (D8) rests on two-sign words, where one-sign differences are near random. Among longer
  words the only case is U-NA-RU-KA-NA-SI / U-NA-RU-KA-NA-TI.
- **Not supported:**
  - suffixes -TE, -JA and -NE by the bare-stem test (D5–D7);
  - sonorant rows (D10), doublet-sign positions (D11) and special signs in names (D12);
  - sheep-tablet, place-name and hapax effects on Knossos names (D14–D16);
  - scribe, heading and commodity regularities in the accounts (D17, D18, D21).
  - Refuted: the same person does not get similar amounts on different tablets; the amounts differ more than
    chance (D19).

# Nineteenth round: twenty-five more hypotheses, 24 September 2026

`reading/decipher25b.py`, results in `reading/decipher25b_results.json` and `reading/decipher25b_output.txt`.

This round builds on the eighteenth: the coronal conditioning of Minoan e/o, persons kept by one scribe, and
recopied lists. It also rechecks earlier per-tablet results now that the two sides of a tablet (HT 9a, HT 9b) are
merged into one tablet. Each hypothesis had a prediction stated before the test ran and one primary test.
Benjamini–Hochberg at 5% runs across all 25 and leaves **12 supported**.

| # | Hypothesis | primary p | BH | verdict |
|---|---|---|---|---|
| E1 | Common divisor on a tablet, sides merged | 0.030 (7.9% vs 4.4%) | no | **weakened**: V7 was p 0.0005 with sides separate |
| E2 | Doubled amounts on a tablet, sides merged | 0.001 (583 vs 492 pairs) | yes | holds |
| E3 | Same-scribe tablets share vocabulary, sides merged, terms removed | 0.004 | yes | holds |
| E4 | KI-RO rarer on VIR tablets, sides merged | 0.39 (3/11 vs 10/26) | no | **withdrawn**: V6 depended on split sides |
| E5 | e alone follows coronals more than in Linear B | 0.001 (logOR 0.81 vs −0.05) | yes | **supported**; o alone in the output file |
| E6 | Coronal pattern outside Haghia Triada | 0.001 (0.85 vs −0.25) | yes | **supported**; HT separately too |
| E7 | Coronal pattern in list names | 0.001 (0.67) | yes | **supported**; non-names too |
| E8 | Same-syllable consonant predicts e/o, the next syllable's does not | 0.001 (0.72 vs −0.23) | yes | **supported** |
| E9 | Among e, i, o, u, e/o take the place of i/u after coronals | 0.001 (0.55 vs −0.45) | yes | **supported** |
| E10 | Scribes specialise in commodities | 0.001 (χ² 90.6 vs 48.3) | yes | **supported** |
| E11 | Scribes specialise in transaction terms | 0.009 | yes | **supported** |
| E12 | Recopied lists give the same amounts | 0.57 (1 of 8) | no | not supported |
| E13 | Recurring entry words stay at one site | 0.001 (91.7% vs 71.5%) | yes | supported (expected for local archives) |
| E14 | Eteocretan shows the coronal pattern | 0.58 | no | not supported |
| E15 | Cretan place names show the coronal pattern | 0.78 | no | not supported |
| E16 | u prefers labials and velars more than in Linear B | 0.59 | no | not supported |
| E17 | e/o syllables cluster within words | 0.94 (52 vs 59.6) | no | not supported; if anything they avoid each other |
| E18 | Minoan-shaped Knossos names (stem-scored) cluster by Linear B scribe | 0.022 | yes | **supported** |
| E19 | Knossos names on VIR tablets are more Minoan-shaped (stem-scored) | 0.85 | no | not supported |
| E20 | Consonant-row cohesion with left context only | 0.0005 | yes | **supported** |
| E21 | Consonant-row cohesion with right context only | 0.079 | no | weak |
| E22 | Z row keeps company with the J row | 0.12 | no | not supported |
| E23 | Fraction use depends on the scribe | 0.046 | no | suggestive |
| E24 | KI-RO entry words recur on other tablets | 0.87 | no | not supported |
| E25 | Recopied lists keep their order | 0.23 (tau 0.30, 2 pairs) | no | not supported |

**What the round adds.**

- **The coronal rule for Minoan e/o is now secure.** It holds for e on its own (e-signs exist after nearly every
  consonant, so this is not a gap in the sign inventory). It holds outside Haghia Triada, in list names and in other
  words. Among the non-low vowels it takes the place of i/u, not of a. And it is the consonant of the same
  syllable that matters: the next syllable's consonant has no such effect (logOR −0.23). A working description:
  **in Minoan, e and o occur mainly after dental consonants (T, D, N, R, S), where other positions have i and u.**
  That looks like vowel lowering after dentals, or a script convention for a sound the Linear B values render as
  e/o. It does not carry over to Eteocretan (E14), Cretan place names in Linear B (E15) or Pre-Greek (round 18).
  It is a property of Linear A spelling itself.
- **Scribes had departments (E10, E11, E3).** Scribal hands specialise in commodities (χ² 90.6 against 48.3 by
  chance) and in transaction terms (SA-RA2, KA-PA, A-DU, DA-RE, KU-PA). Their tablets share vocabulary, and they
  keep their own persons (round 18). The Haghia Triada archive was divided by scribe and subject.
- **At Knossos, Minoan-shaped names cluster by Linear B scribe (E18).** This is scored on the stem, so the
  feminine -a artefact of D13 is avoided. Some Mycenaean scribes dealt more with the Minoan-named population than
  others; the most Minoan scribes are listed in the output file.
- **Row cohesion comes from the left (E20, E21).** A sign's consonant row is predicted by the sign *before* it
  (p 0.0005), much less by the sign after it (p 0.08). Minoan constrained which consonants could follow which.
- **Two earlier results do not survive merging the sides of tablets.**
  - The common-divisor result (round 11, V7) weakens to p 0.03 and no longer survives correction.
  - "KI-RO is rare on personnel tablets" (V6) disappears: 3 of 11 KI-RO tablets against 10 of 26 others.
  - Doubled amounts (E2) and scribe vocabulary (E3) hold.
  - Neither weakened result is on the page or in the preprint.
- **Not supported:**
  - recopied lists repeating amounts or order (E12, E25; only two pairs);
  - u after labials and velars (E16);
  - e/o clustering within words (E17 — they occur together less than chance, if anything);
  - VIR-tablet names (E19), Z with J (E22), fractions by scribe (E23) and KI-RO persons recurring (E24).

# Twentieth round: fifteen hypotheses, 24 September 2026

`reading/decipher15c.py`, results in `reading/decipher15c_results.json` and `reading/decipher15c_output.txt`.

This round tests fifteen hypotheses rather than twenty-five; weaker candidates were left out. They use the
coronal rule as a tool, and test scribal practice, where the Minoan-shaped names sit in the Linear B archives, and
what the left-context result of round 19 implies. Each had a prediction stated before the test ran and one primary
test; Benjamini–Hochberg at 5% runs across the fifteen. Four survive. After the run, a check stratified by
commodity showed that one of them (F6) is not robust.

| # | Hypothesis | primary p | BH | check | verdict |
|---|---|---|---|---|---|
| F1 | i~e and u~o alternations occur after dentals more than other vowel alternations | 0.022 (19 of 21 vs 66%) | no | R, S, T, D carry them | suggestive |
| F2 | Treating dental e/o as i/u gains more Linear A–Knossos name matches than treating non-dental ones so | 0.041 (8 vs 2) | no | Pylos names: 1 vs 2 | suggestive; see the -RU lead below |
| F3 | The rule is stronger in Late than Middle Minoan texts | 0.50 | no | only 20 Middle Minoan words | untestable |
| F4 | The rule holds in the religious texts | 0.001 (logOR 0.63 vs −0.25) | yes | formula removed, in the output file | **supported** |
| F5 | Near-identical spellings come from different scribes | 0.51 | no | — | not supported |
| F6 | Even-amount preference differs by scribe | 0.003 | yes | within-commodity shuffle p 0.12 | **not robust** (commodity) |
| F7 | Minoan-shaped Knossos names cluster by series | 0.052 | no | — | suggestive |
| F8 | Pylos names cluster by series | 0.72 | no | — | not supported |
| F9 | Neighbouring syllables avoid same-place consonants, more than Linear B | 0.004 (ratio 0.93) | yes | Linear B avoids them more (0.72) | **half supported**: avoidance yes, "more than Linear B" no |
| F10 | A vowel predicts the next consonant more than in Linear B | 1.0 | no | — | **refuted** |
| F11 | The preceding sign alone recovers a hidden sign's row | 0.56 (6% vs 6.5%) | no | — | not supported |
| F12 | Doubled amounts stand on neighbouring lines | 0.75 | no | — | not supported |
| F13 | Knossos scribes with more Minoan-shaped names use more undeciphered signs | 0.010 (rho 0.48, 23 scribes) | yes | — | **supported** |
| F14 | A total's gap equals an entry amount | 1.0 (0 of 5) | no | only 5 usable totals | untestable |
| F15 | Pylos women's-work names are more Minoan-shaped | 0.25 | no | only 1 name on Aa/Ab/Ad | untestable |

**What the round adds.**

- **The coronal rule holds in the religious texts too (F4).** It holds in the dedications on stone vessels as well
  as the tablets, so it is not a habit of the Haghia Triada accountants. It belongs to how Linear A spelled Minoan
  everywhere.
- **At Knossos, the scribes who wrote Minoan names also wrote the undeciphered signs (F13).** Across 23 Linear B
  scribes, the more Minoan-shaped a scribe's personal names, the more often that scribe uses signs Linear B never
  gave values to (rho 0.48). The undeciphered signs belonged to the Minoan part of the Knossos administration,
  which supports reading them as Minoan sounds that Greek did not need.
- **A lead: Linear A -RU = Knossos -ro (F2, exploratory).** Treating dental e/o as i/u adds eight exact matches
  between Linear A words and Knossos personal names:

  | Linear A | Knossos (Linear B) |
  |---|---|
  | DI-DE-RU | di-de-ro |
  | QA-QA-RU | qa-qa-ro |
  | KA-SA-RU | ka-sa-ro |
  | A-TI-RU | a-ti-ro |
  | SA-MA-RO | sa-ma-ru |
  | RI-KA-TA | re-ka-ta |
  | DE-SU | di-so |
  | SI-DU | se-do |

  Five of the eight are Linear A final -RU against Linear B -ro. That is what a Greek scribe would do with a
  Minoan name in -u, giving it the Greek -os ending. The count is small (p 0.04, not surviving the correction), but
  the correspondence is regular and could be tested on its own.
- **Minoan avoids neighbouring consonants of the same place (F9), but less than Greek does.** The left-context
  result of round 19 is not a dissimilation effect stronger than Linear B's. And the preceding sign alone does not
  recover a sign's row (F11).
- **Untestable on this corpus:**
  - change over time (F3: 20 Middle Minoan words);
  - scribal errors in totals (F14: 5 usable totals);
  - Pylos women's-work names (F15: the Aa/Ab/Ad tablets list women by ethnic, not personal name).

# Twenty-first round: the -u/-o lead on its own, and replications on SigLA, 24 September 2026

`reading/decipher11g.py`, results in `reading/decipher11g_results.json` and `reading/decipher11g_output.txt`.

Eleven hypotheses. The main one tests the twentieth round's -RU/-ro lead as its own hypothesis, with a proper
null and a Pylos control. The coronal rule and the consonant rows are replicated on SigLA's transcription, which
records its own sign values attestation by attestation (536 word types, 470 of them shared with lineara.xyz).
Benjamini–Hochberg at 5% runs across the eleven.

| # | Hypothesis | primary p | BH | verdict |
|---|---|---|---|---|
| G1 | Linear A -Cu words have a Knossos name X-Co more often than words in other vowels | 0.26 (5/105 vs a 8/242) | no | **not supported**: the lead does not hold |
| G2 | G1 without the R row | 0.92 (1/85) | no | not supported |
| G3 | Linear A -Ci corresponds to Knossos -Ce | 1.0 (0/166) | no | not supported |
| G4 | Knossos names on Linear A stems end in -o more often | 0.057 (41/56 vs 358/581) | no | suggestive |
| G18 | Linear A -a words match Knossos names exactly more often than -u words | 0.49 (2/247 vs 0/110) | no | not supported |
| G16 | Linear A words in -u are entry labels more often | 0.067 (69% vs 60%) | no | suggestive |
| G8 | The coronal rule holds in SigLA's transcription | 0.001 (logOR 0.82 vs −0.25) | yes | **replicated** |
| G13 | The consonant-row cohesion holds in SigLA's transcription | 0.0005 (0.079 vs 0.075 on lineara.xyz) | yes | **replicated** |
| G10 | The coronal rule holds site by site | 0.016 (6 of 6 sites positive) | no | every site positive; 0.016 is the smallest p a six-site sign test can give |
| G11 | Knossos scribes with Minoan-shaped names use more special signs | 0.86 (rho −0.25) | no | not supported |
| G14 | Knossos undeciphered-sign words follow the coronal rule | 0.71 | no | not supported |

**What the round adds.**

- **The -RU/-ro lead is withdrawn (G1, G2).** Tested on its own, Linear A words ending in -u find a Knossos name in
  -o no more often (5 of 105) than words ending in -a do (8 of 242). Without the R row there is one case. The
  eight matches of round 20 came from reading dental e/o as i/u, not from a regular -u → -o adaptation. The page
  now says so.
- **The two structural results replicate on an independent transcription (G8, G13).**
  - SigLA gives its own readings sign by sign. On its words, the coronal rule holds (logOR 0.82 against 0.72 on
    lineara.xyz and −0.25 in Linear B).
  - The consonant rows cohere just as strongly (0.079 against 0.075).
  - Neither result is an artefact of one edition.
- **The coronal rule holds at every site with enough words (G10):** Haghia Triada 0.51, Khania 1.00, Knossos 0.17,
  Palaikastro 0.74, Phaistos 1.17, Zakros 1.20, against Linear B −0.25. The weakest is Knossos, the site where
  Linear A was in contact with Linear B.
- **Suggestive, not significant:**
  - Knossos names built on Linear A stems take -o endings more often (G4, 73% against 62%);
  - Linear A words in -u are entry labels a little more often (G16).
- **Not supported:** Knossos scribes' special-sign use does not track their Minoan names (G11), and Knossos words
  with undeciphered signs do not follow the coronal rule (G14). The rule is a Linear A spelling habit that did not
  pass into Linear B.

# Twenty-second round: eight hypotheses, 24 September 2026

`reading/decipher8h.py`, results in `reading/decipher8h_results.json` and `reading/decipher8h_output.txt`.

A smaller round, because returns are falling. Five hypotheses stress-test the coronal rule from new angles; three
probe words and archives. Benjamini–Hochberg at 5% runs across the eight; four survive.

| # | Hypothesis | primary p | BH | verdict |
|---|---|---|---|---|
| H1 | The rule survives dropping its most influential sign | 0.001 (without RE: 0.37 vs −0.25) | yes | **supported** |
| H2 | The rule holds in words attested once | 0.001 (0.73, 631 words) | yes | **supported** |
| H3 | The rule holds in word-initial syllables | 0.001 (0.55 vs −0.23) | yes | **supported** |
| H4 | With consonants as the unit, coronals rank above non-coronals in e/o share | 0.17 (AUC 0.68) | no | **not supported**: the class is not clean |
| H5 | Reduplicated Linear A words are entry labels more often | 0.69 (10/17) | no | not supported |
| H6 | Reduplicated Knossos names are more Minoan-shaped | 0.95 (8 names) | no | not supported |
| H7 | Single-commodity tablets of the same commodity share vocabulary | 0.003 | yes | **supported** |
| H8 | Sealing signs match word initials from their own site | 1.0 | no | not supported (596 of 631 sealings are from Haghia Triada) |

**What the round adds.**

- **The rule is not a few words or one suffix (H1–H3).** It survives dropping RE, the sign that supports it most
  (logOR 0.37). It holds in the 631 words attested only once, so it is productive. And it holds in word-initial
  syllables, so it is not a matter of endings such as -TE or -RE.
- **But it is not a clean "dental" class (H4).** Consonant by consonant, the e/o share is high after Q (50%),
  R (37%), T (28%), S (19%) and N (17%), and low after D (12%), K (11%), J and P (7%), and zero after W and Z.
  Ranked as a class, dentals are not significantly above the rest (p 0.17). The accurate statement is narrower:
  **Minoan e/o are concentrated after R and T (with S, N, and the labiovelar Q)**, and pooled coronals show it
  strongly because R and T are frequent. D and Z do not share it. The page wording has been corrected to match.
- **Commodity vocabularies (H7).** Tablets recording the same commodity share more of their words, with
  transaction terms removed and sides merged, than tablets recording different commodities (p 0.003). The
  word-level search of round 13 found almost no single word bound to one commodity, but the vocabulary as a whole
  is organised by commodity.
- **Not supported:** reduplication does not mark names (H5, H6), and sealing signs are not local initials (H8;
  almost all sealings come from Haghia Triada, so the test has no power).

# Twenty-third round: nine hypotheses on archives and regions, 24 September 2026

`reading/decipher9i.py`, results in `reading/decipher9i_results.json` and `reading/decipher9i_output.txt`.

Nine hypotheses on questions not asked before:
- what drives the shared commodity vocabularies of round 22;
- whether Linear A at Knossos is closer to Knossos Linear B;
- where the signs that Linear B dropped are concentrated;
- regional practice.

Benjamini–Hochberg at 5% runs across the nine and leaves three. A control for I9 (non-name words) was added after
the run.

| # | Hypothesis | primary p | BH | verdict |
|---|---|---|---|---|
| I1 | Same-commodity tablets share entry labels (persons) | 0.011 | yes | **supported** |
| I2 | Same-commodity tablets share heading words | 1.0 | no | not supported (19 tablets) |
| I3 | Knossos Linear A is closer to Knossos Linear B than other Linear A is | 0.33 | no | not supported |
| I4 | The R/T e/o rule is weaker at Knossos | 0.14 (0.17 vs 0.72) | no | direction as predicted, 55 words |
| I5 | Signs with no Linear B value are commoner in religious words | 1.0 (4.3% vs 7.6%) | no | **refuted**: commoner in administrative words |
| I6 | Special signs are commoner in religious words | 0.60 | no | not supported |
| I7 | Commodity ligatures are site-specific | 0.0005 (χ² 194 vs 76) | yes | **supported** |
| I8 | Heading words travel between sites more than entry labels | 0.63 (6/135 vs 16/346) | no | not supported |
| I9 | Names at Haghia Triada differ in syllable profile from names elsewhere | 0.012 | yes | supported, but not name-specific (non-name words differ too, p 0.0005) |

**What the round adds.**

- **The commodity vocabularies are persons (I1, I2).** Same-commodity tablets share entry labels, but not headings.
  The same people recur on tablets of the same commodity: persons were attached to a product (oil, grain, wine),
  which fits the scribal departments of rounds 18–19.
- **Ligature practice was regional (I7).** The syllable attached to a commodity sign depends on the site:
  - Haghia Triada writes OLE+U, OLE+KI, OLE+MI, OLE+DI, GRA+PA and GRA+KU;
  - Tylissos uses the same oil set (OLE+KI, OLE+MI, OLE+U);
  - Khania writes OLE+TA and VIR+KA;
  - Zakros writes GRA+PA and VIN+RA.

  The oil-ligature system is shared between Haghia Triada and Tylissos, in central Crete, and differs in the west
  (Khania) and east (Zakros). This supports reading the adjuncts as local subtypes or administrative categories
  rather than universal commodity words.
- **Sites differ in vocabulary, not only in names (I9).** Haghia Triada's names differ in syllable profile from
  other sites' names (p 0.012), but its non-name words differ even more (p 0.0005). This is a regional difference in
  vocabulary, and perhaps dialect or scribal habit, not a naming pattern.
- **Signs Linear B dropped belong to the accounts (I5).** They are *commoner* in administrative words (7.6% of signs)
  than in religious words (4.3%); in the religious texts they are mostly *301. So Linear B did not drop signs that
  were religious. It dropped signs of the Minoan administrative vocabulary.
- **Not supported:**
  - Linear A at Knossos is no closer to Knossos Linear B than other Linear A is (I3);
  - the R/T rule is weaker at Knossos, as predicted, but not significantly (I4, 55 words);
  - headings do not travel between sites more than names do (I8).

# Twenty-fourth round: six hypotheses on regions and the R/T vowels, 24 September 2026

`reading/decipher6j.py`, results in `reading/decipher6j_results.json` and `reading/decipher6j_output.txt`.

Six hypotheses follow the regional results of round 23 and the R/T vowel rule. Benjamini–Hochberg at 5% runs
across the six and leaves three.

| # | Hypothesis | primary p | BH | verdict |
|---|---|---|---|---|
| J1 | Closer sites share more word types | 0.35 (rho −0.06) | no | not supported |
| J2 | Tylissos shares more vocabulary with Haghia Triada than other sites do | 1.0 (0 of 19 words) | no | **refuted** |
| J3 | Vowels after R/T are more varied (higher entropy) than after other consonants, more than in Linear B | 0.0005 | yes | **supported** |
| J4 | Unread signs are site-specific | 0.0005 (χ² 1454 vs 224) | yes | **supported** |
| J5 | Formula word variants cluster by site | 0.18 | no | not supported |
| J6 | Amounts differ by site within the same commodity | 0.0015 | yes | **supported** |

**What the round adds.**

- **A fuller vowel system after R and T (J3).** After R and T, Linear A spreads its syllables over the five vowels
  (entropy 1.52), while after other consonants it uses a narrower set (1.33). In Linear B the two are the same
  (1.53 and 1.50). Together with rounds 18–22, the picture is of a Minoan vowel system that shows all five Linear B
  vowels after R and T and behaves more like a three-vowel system (a, i, u) elsewhere.
- **Regional sign repertoires (J4).** Unread signs are strongly tied to sites:
  - *411, *409 and *311 occur only at Khania;
  - *309 only at Tylissos;
  - *323, *325 and *904 only at Haghia Triada.

  Some unread signs are local additions to the syllabary, which may be why Linear B, created in one region, never
  adopted them.
- **Regional economies or units (J6).** Within the same commodity, typical amounts differ by site. Grain entries
  are large at Haghia Triada (geometric mean 23) and small at Khania (6) and Zakros (5); wine entries are large at
  Zakros (23) and small at Haghia Triada (5). Either the sites handled goods at different scales, or they counted
  in different units.
- **Tylissos is linked to Haghia Triada in notation only (J2).** It shares Haghia Triada's oil ligatures (round
  23) but none of its 19 words. The shared practice was administrative convention, not shared personnel or
  vocabulary. Vocabulary does not fall off with distance in general (J1), and formula variants are not regional
  (J5).

# Twenty-fifth round: seven follow-ups, 24 September 2026

`reading/decipher7k.py`, results in `reading/decipher7k_results.json` and `reading/decipher7k_output.txt`.

Seven hypotheses follow up round 24: local signs, regional units, the geography of the Knossos matches, and the
R/T vowel pattern. Benjamini–Hochberg at 5% runs across the seven; one survives.

| # | Hypothesis | primary p | BH | verdict |
|---|---|---|---|---|
| K1 | Single-site unread signs stand in names more than widespread unread signs | 0.94 (15/40 vs 112/229) | no | not supported |
| K2 | Single-site unread signs stand word-finally more | 1.0 (0/40 vs 79/229) | no | **refuted**: they are never final |
| K3 | Grain entries at Haghia Triada carry fractions less often | 0.27 (12/66 vs 7/26) | no | not supported |
| K4 | Counts of men (VIR) differ by site | 0.58 (HT 20, Khania 14; 31 entries) | no | not supported, as a unit explanation predicts |
| K5 | Linear A words matching Knossos words come from sites near Knossos | 0.38 (13.8% vs 12.2%) | no | not supported |
| K6 | The richer vowel set after R/T replicates on SigLA | 0.0005 (gap 0.19 vs Linear B 0.03) | yes | **replicated** |
| K7 | It holds at Khania and at Zakros separately | 0.997 (Khania −0.21; Zakros 0.11, p 0.019) | no | holds at Zakros, **reversed at Khania** |

**What the round adds.**

- **The R/T vowel pattern replicates on SigLA (K6).** The gap is 0.19 there and 0.20 on lineara.xyz, against 0.03
  in Linear B.
- **Khania is different (K7).** Khania, in the west, puts e/o mainly after R and T like the other sites (round 21),
  but after R and T it concentrates on those vowels instead of spreading over five. Zakros, in the east, shows the
  pattern (p 0.019). With the regional signs and ligatures of rounds 23–24, Khania stands apart in both its notation
  and its vowel spelling.
- **Grain and wine, not men, differ by site (K4 with J6).** Counts of men are much the same at Haghia Triada (20)
  and Khania (14), while grain and wine amounts differ several-fold. That fits different measuring units more than
  different economies. The sample for men is small (31 entries).
- **Local signs are never word-final (K2).** The signs found at only one site occur 40 times, always at the start
  or in the middle of words; widespread unread signs are final a third of the time. The local signs belong to word
  roots, not endings. They are also not concentrated in names (K1).
- **Not supported:** fractions on grain by site (K3), and a Knossos-area origin for the Linear A words matching
  Knossos names (K5; they come from across Crete in proportion to each site's vocabulary).

# Twenty-sixth round: six hypotheses on Khania, local signs and scribes, 24 September 2026

`reading/decipher6l.py`, results in `reading/decipher6l_results.json` and `reading/decipher6l_output.txt`.

Six hypotheses; Benjamini–Hochberg at 5% across the six. **None survives.**

| # | Hypothesis | primary p | verdict |
|---|---|---|---|
| L1 | Khania uses e/o after R/T more than Haghia Triada | 0.12 (35% vs 27%) | direction as predicted, not significant |
| L2 | Khania uses e/o more overall | 0.46 (16.8% vs 16.5%) | not supported |
| L3 | Khania Linear A is closer to Linear B than Haghia Triada's | 0.41 | not supported |
| L4 | Words with a local unread sign have a twin with a known sign in that slot more often | 1.0 (2/16 vs 61/145) | **refuted**: fewer twins |
| L7 | Words with e/o after other consonants are attested outside Haghia Triada more often | 0.80 | not supported |
| L10 | Haghia Triada scribes differ in e/o after R/T | 0.30 (13%–35%, 125 syllables) | not supported |

**What the round adds.**

- **No sign that the R/T rule is a scribal habit (L10).** The four Haghia Triada scribes with enough data do not
  differ significantly in how often they write e/o after R and T. This fits the rule being part of the language.
  The test is weak (125 syllables), so it is absence of evidence, not proof.
- **Khania's difference is not a general e/o excess (L1, L2).** Khania leans towards more e/o after R/T but not
  overall, and it is no closer to Linear B (L3).
- **Candidate values for unread signs (L4, exploratory, not tested).** Words of three or more signs whose unread sign
  has a twin with a known sign in the same slot elsewhere:
  - *47-KU-NA ~ DA-KU-NA
  - *21F-TU-NE ~ QE-TU-NE
  - *306-TA-JE ~ RI-TA-JE
  - *324-DI-RA ~ ZU-DI-RA
  - *333-SA-MU ~ JA-SA-MU
  - *164-RI-DA ~ DA-RI-DA
  - *118-MI-NA ~ NE-MI-NA

  These could equally be different words. As a class, twins are rarer for local signs than for widespread ones.
  The full list is in the output file.

# Twenty-seventh round: twin values checked, and the R/T pattern beyond Linear A, 24 September 2026

`reading/decipher6m.py`, results in `reading/decipher6m_results.json` and `reading/decipher6m_output.txt`.

Six hypotheses; Benjamini–Hochberg at 5% across the six. **None survives.**

| # | Hypothesis | primary p | verdict |
|---|---|---|---|
| M1 | Twin-derived values (round 26) turn the signs' other words into attested words more than random values | 0.62 (6 vs 6.2) | **not supported**: the candidate values are withdrawn as values |
| M6 | Knossos names show the R/T vowel-entropy gap more than Pylos names | 0.87 | not supported |
| M7 | Cretan place names show it more than Pylos place names | 0.12 (0.10 vs 0.03) | direction as predicted, not significant |
| M8 | Pre-Greek stems show it more than Greek stems | 0.19 | not supported |
| M9 | Eteocretan shows it more than Greek | 0.0135 (0.14 vs −0.11) | nominal only (threshold 0.0083); 35 short pieces |
| M10 | Linear B words with the same numbered signs become attested words under the candidate values | 0.51 | not supported (only *47 is shared) |

**What the round adds.**

- **The twin values do not hold up (M1).** Substituted into the other words containing the same sign, the values
  taken from twin words turn no more of them into attested words than random values do. The round-26 list
  (*47 = DA, *21F = QE, *306 = RI and the rest) stays a list of coincidences until other evidence appears.
- **The R/T vowel pattern is a Linear A feature.** It does not show in Knossos names (M6) or in Pre-Greek (M8). It
  leans the right way in Cretan place names (M7) and in Eteocretan (M9, nominal p 0.0135), but neither survives the
  correction. Eteocretan's hint is worth noting as the only outside record that points the same way, on a corpus
  too small to carry weight.

# Twenty-eighth round: the R/T rule as a search tool, 24 September 2026

`reading/decipher4n.py`, results in `reading/decipher4n_results.json` and `reading/decipher4n_output.txt`.

Four hypotheses that use the R/T vowel rule to look for hidden matches, rewriting e/o after R and T as i/u before
comparing. Benjamini–Hochberg at 5% across the four. **None survives.**

An external lead was considered first and set aside: the Keftiu names of the Egyptian school tablet BM 5647. The
tablet gives seven names, too few to test, and a recent study reads them as Hellenized Cretan names
("Crossing the Wine-Dark Sea", Journal of Ancient Egyptian Interconnections).

| # | Hypothesis | primary p | verdict |
|---|---|---|---|
| N1 | Under the collapse, Linear A matches Knossos place names more than Pylos ones | 1.0 (no new matches at either) | not supported |
| N2 | The R/T collapse gains more Knossos name matches than a collapse after other consonants | 0.052 (6 vs 2; Pylos 0 vs 2) | not independent: the same -RU/-ro names withdrawn in round 21 |
| N3 | On SigLA, i~e and u~o alternations fall after dentals more than other alternations | 0.43 (75% vs 67%) | **not replicated**; round 20 F1 (p 0.022) does not hold on the second transcription |
| N5 | Linear A headings match Knossos place names more than entry labels do | 1.0 (0/137 vs 1/350) | not supported |

**What the round adds.** The vowel rule describes Linear A spelling but does not unlock new identifications: no
hidden place names appear, and the only name gains are the -RU/-ro set already withdrawn. The dental i~e / u~o
alternation of round 20 is withdrawn too, as it does not replicate on SigLA. The replicated vowel results remain the
e/o shortage, the e/o concentration after R and T, and the richer vowel set after R and T.

# Twenty-ninth (loop 1 of 10) round: spelling and sound patterns, 24 September 2026

`reading/round29.py`, results in `reading/round29_results.json` and `reading/round29_output.txt`.

Ten hypotheses on the spelling and sound patterns of Linear A words, each against Linear B. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| P1 | Linear A words begin with a pure vowel more often than Linear B words | 0.9925 (LA 0.238, LB 0.279) | no | **reversed**: fewer vowel-initial words |
| P2 | Linear A writes two pure vowel signs in succession more often | 1 (LA 0.003, LB 0.02) | no | **reversed**: hiatus far rarer (0.3% vs 2%) |
| P3 | o-signs are word-initial more than other signs, more so than in Linear B | 0.0005 (LA_gap 0.022, LB_gap -0.113) | yes | supported, but it reflects Greek -o endings: Linear A o-signs are initial no more than other signs (gap 0.02) |
| P4 | After an a-syllable, Linear A has I or U more often (diphthongs) | 0.062 (LA 0.0537, LB 0.039) | no | suggestive |
| P5 | Linear A words begin with a repeated syllable more often | 0.058 (LA 0.0158, LB 0.0088) | no | suggestive |
| P6 | Q-row signs are word-initial more often in Linear A | 0.0005 (LA 0.62, LB 0.277) | yes | **supported** |
| P7 | R-row signs are word-initial less often in Linear A | 0.958 (LA 0.174, LB 0.139) | no | not supported |
| P8 | Final syllables favour a over internal ones more in Linear A | 0.963 (LA_gap -0.09, LB_gap -0.053) | no | not supported |
| P9 | Linear A words end in a pure vowel sign more often | 1 (LA 0.039, LB 0.105) | no | **reversed**: final pure vowels rarer (3.9% vs 10.5%) |
| P10 | The next sign is more predictable in Linear A than in size-matched Linear B | 1 (LA_H 2.829, LB_H_subsampled 2.625) | no | **reversed**: Linear A is less predictable sign to sign |

**What the round adds.**

- **Minoan labiovelars start words (P6).** Q-row signs (QA, QE, QI) are word-initial 62% of the time in Linear A, against 28% in Linear B. It is a positional restriction on the labiovelar series, the clearest new phonotactic pattern of this round.
- **Linear A avoids vowel sequences (P2, P9).** Two pure vowel signs in a row are almost absent (0.3% of words, against 2% in Linear B), and words rarely end in a pure vowel sign (3.9% against 10.5%). Minoan words were built from CV syllables with little hiatus. Greek, by contrast, needed vowel signs for its diphthongs and endings.
- **Less vowel-initial, less predictable (P1, P10).** Fewer Linear A words begin with a pure vowel than Linear B words (24% against 28%). Sign-to-sign sequences are *less* predictable than in size-matched Linear B, so the Linear A lexicon is not more formulaic in its spelling.
- **P3 says more about Greek than Minoan.** o-signs look word-initial relative to Linear B only because Greek puts o in its endings.
- **Suggestive:** diphthong spellings after a (P4, p 0.06) and initial reduplication (P5, p 0.06).

# Thirtieth (loop 2 of 10) round: the vowel system in detail, 24 September 2026

`reading/round30.py`, results in `reading/round30_results.json` and `reading/round30_output.txt`.

Ten hypotheses on the details of the Minoan vowel pattern. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| Q1 | e/o follow T alone more than non-coronals, more than in Linear B | 0.0005 (logOR_LA 0.991, logOR_LB -0.131) | yes | **supported** |
| Q2 | e/o follow S and N more than K, P, M, more than in Linear B | 0.0005 (logOR_LA 0.537, logOR_LB -0.126) | yes | **supported** |
| Q3 | e/o follow Q more than K, more than in Linear B | 0.0005 (logOR_LA 2.043, logOR_LB 0.729) | yes | **supported** |
| Q4 | In Linear A, o is word-final more often than e | 0.998 (o_final [0.338, 71], e_final [0.5183, 328]) | no | **reversed**: o is final less often than e (34% vs 52%) |
| Q5 | a-a sequences exceed chance within Linear A words more than in Linear B | 1 (LA_ratio 1.017, LB_ratio 1.115, bootstrap p 1.0) | no | not supported |
| Q6 | High vowels co-occur within words beyond chance, more than in Linear B | 0.0495 (LA_ratio 1.006, LB_ratio 0.96, bootstrap p 0.0495) | no | nominal only (p 0.0495) |
| Q7 | e/o are commoner in Linear A words of 3+ signs than in two-sign words | 0.7401 (long 0.175, short 0.186) | no | not supported: same in short and long words |
| Q8 | e/o are commoner in entry labels than in headings | 0.1949 (entries 0.178, headings 0.159) | no | not supported |
| Q9 | e/o are commoner in religious words than in administrative words | 0.7101 (religious 0.169, admin 0.179) | no | not supported |
| Q10 | E/O are rarer among pure vowel signs, relative to CV e/o, in Linear A than in Linear B | 0.7136 (LA_gap -0.087, LB_gap -0.104) | no | not supported |

**What the round adds.**

- **The e/o rule, consonant by consonant (Q1–Q3).** T alone carries it (logOR 0.99 against −0.13 in Linear B), not only through RE and RO. S and N favour e/o over K, P and M (0.54 against −0.13). Q favours them strongly over K (2.04 against 0.73), so QE/QO far outnumber KE/KO. The consonants that take e/o in Minoan are T, R, S, N and the labiovelar Q. Those that avoid them are K, P, M, J and W.
- **The pattern runs through the whole vocabulary (Q7–Q9).** The e/o share is the same in two-sign and longer words, in names and headings, and in religious and administrative words. That is what a sound pattern of the language would look like, rather than a feature of one word class.
- **o is less tied to endings than e (Q4, reversed).** o is word-final 34% of the time, against 52% for e.
- **No vowel harmony.** Neither a-a sequences (Q5) nor high-vowel co-occurrence (Q6, nominal p 0.0495) shows it convincingly.

# Thirty-first (loop 3 of 10) round: word endings, beginnings and possible grammar, 24 September 2026

`reading/round31.py`, results in `reading/round31_results.json` and `reading/round31_output.txt`.

Ten hypotheses on word endings, beginnings and agreement. Benjamini–Hochberg at 5% across the ten. A check for S5 and S6 (unique words per tablet, shuffling within site) was added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| S1 | Final signs are associated with function (entry vs heading) | 0.1729 (chi2 23.6, null 18.1, words 319) | no | not supported |
| S2 | Final signs are associated with register | 0.0045 (chi2 59.7, null 33.9, words 649) | yes | **supported** |
| S3 | Initial signs are associated with function | 0.5317 (chi2 18.4, null 19.3, words 359) | no | not supported |
| S4 | Initial signs are associated with register | 0.0005 (chi2 84.8, null 24.7, words 620) | yes | **supported** |
| S5 | Words on the same tablet share final signs beyond chance | 0.0005 (same_final_pairs 202, null 103.9) | yes | weakened by the check (unique words, within-site: p 0.085) |
| S6 | Words on the same tablet share initial signs beyond chance | 0.0005 (same_initial_pairs 242, null 141.7) | yes | **supported**; holds under the check (p 0.011) |
| S7 | Linear A name finals resemble Knossos stem-final syllables more than Pylos ones | 0.1344 (jsd_KN 0.2073, jsd_PY 0.2501) | no | not supported |
| S8 | Two-sign endings attach to 3+ distinct stems more than chance | 0.9701 (LA_endings 8, null 8.0) | no | not supported (Linear B also shows none by this test) |
| S9 | Neighbouring words share their final sign more than chance | 0.8326 (pairs 21, null 24.18) | no | not supported |
| S10 | A heading and the next word share their final sign more than chance | 0.8661 (pairs 4, null 5.38) | no | not supported |

**What the round adds.**

- **Religious words have their own beginnings and endings (S2, S4).** Initial and final signs differ between the religious and administrative vocabularies (initials χ² 84.8 against 24.7; finals 59.7 against 33.9). This extends the known JA-/U- and -JA observations to the whole sign inventory.
- **Words on one tablet share their first sign (S6).** The pattern survives counting each word once and shuffling only among tablets of the same site (p 0.011). Lists group words that begin alike, perhaps by alphabet-like ordering or by word family. The matching finals of S5 mostly come from repeated words (p 0.085 after the check).
- **No agreement between neighbouring words (S9, S10).** Adjacent words, and headings with the words after them, share final signs no more than chance. There is no sign of case or number agreement marked by the final syllable.
- **Not supported:** role-marking finals or initials (S1, S3); a productive set of two-sign suffixes (S8, which the same test does not detect in Linear B either); Linear A name finals matching Knossos stem finals (S7).

# Thirty-second (loop 4 of 10) round: Minoan-shaped names across the Linear B archives, 24 September 2026

`reading/round32.py`, results in `reading/round32_results.json` and `reading/round32_output.txt`.

Ten hypotheses on where Minoan-shaped names sit in the Linear B archives. Every name is scored on its stem, with the final syllable removed, by a model of Linear A list names against Linear B common words, so Greek endings and the Pylos names cannot drive the result. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| U1 | Knossos names are more Minoan-shaped than Thebes/Mycenae/Tiryns names | 0.0025 (auc 0.634, n [637, 46]) | yes | **supported**: resolves round 12 W1 (was p 0.07) |
| U2 | Knossos-only names are more Minoan-shaped than Knossos names shared with the mainland | 0.0045 (auc 0.579, n [637, 131]) | yes | **supported** |
| U3 | Knossos names without a Greek etymology are more Minoan-shaped than Greek ones | 0.025 (auc 0.555, n [520, 117]) | no | nominal (p 0.025), the measure behaves as it should |
| U4 | Pylos names without a Greek etymology are more Minoan-shaped than Greek ones | 0.0875 (auc 0.544, n [224, 115]) | no | suggestive |
| U5 | Knossos theonyms are more Minoan-shaped than Pylos theonyms | 0.8976 (auc 0.281, n [8, 4]) | no | not supported (8 vs 4 theonyms) |
| U6 | Stems of Knossos ethnics are more Minoan-shaped than stems of Pylos ethnics | 0.1204 (auc 0.675, n [7, 11]) | no | suggestive (7 vs 11 ethnics) |
| U7 | Knossos names with undeciphered signs are more Minoan-shaped in their readable signs | 0.8611 (auc 0.445, n [31, 637]) | no | not supported |
| U8 | Pylos names also attested at Knossos are more Minoan-shaped than Pylos-only names | 0.5592 (auc 0.496, n [104, 339]) | no | not supported |
| U9 | Knossos names with special signs are more Minoan-shaped | 0.3783 (auc 0.516, n [36, 601]) | no | not supported |
| U10 | Room of the Chariot Tablets names are more Minoan-shaped (stem-scored) than later Knossos names | 0.9545 (auc 0.438, n [70, 454]) | no | **reversed** again (AUC 0.44) |

**What the round adds.**

- **Knossos names are more Minoan than every mainland name stock (U1).** Scored on the stem, and with a model that never used Pylos names, Knossos names beat the 46 Thebes, Mycenae and Tiryns names (AUC 0.63, p 0.0025). This removes the "Pylos only" caveat of round 12 (W1, p 0.07). The page and the preprint are updated.
- **The Greek-mainland names are the less Minoan part of Knossos (U2).** Knossos-only names are more Minoan-shaped than Knossos names that also occur on the mainland (AUC 0.58).
- **The measure behaves as it should (U3).** Knossos names without a Greek etymology score higher than Greek ones (p 0.025, not surviving the correction). Pylos points the same way (U4, p 0.09).
- **The Room of the Chariot Tablets is again less Minoan (U10).** Stem scoring gives the same result as round 12. That early archive recorded a more Greek-named group.
- **Not supported:**
  - readable parts of names with undeciphered signs (U7), and names with special signs (U9);
  - Pylos names also found at Knossos (U8);
  - theonyms and ethnics (U5, U6), too few to test.

# Thirty-third (loop 5 of 10) round: amounts, totals and fractions, 24 September 2026

`reading/round33.py`, results in `reading/round33_results.json` and `reading/round33_output.txt`.

Ten hypotheses on the bookkeeping. Benjamini–Hochberg at 5% across the ten. Checks for V1 (amounts of 10 or more only) and V17 (amounts other than 1) were added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| V1 | Grain amounts are multiples of 5 more often than other commodities' amounts | 0.0005 (GRA [0.4706, 85], other [0.1946, 221]) | yes | weakened by the check: among amounts of 10+, 59% vs 42% (p 0.038), so largely a size effect |
| V3 | Entries with J (1/2) have odd whole numbers more often | 0.5042 (with_J [0.5185, 54], no_fraction [0.5114, 1097]) | no | not supported |
| V7 | Lists with a KU-RO total are longer | 0.002 (with_total [6.6875, 32], without [4.819, 232]) | yes | supported (expected) |
| V8 | Totals balance less often on longer lists (6+ entries) | 0.8691 (long_ok [0.3684, 19], short_ok [0.2222, 9]) | no | not supported |
| V9 | Totals that do not balance fall short of the entries more often than they exceed them | 0.5927 (short 9/18, sign_test_p 0.5927) | no | not supported |
| V10 | Fractions stand on the later half of a list more often | 0.3858 (later_half [0.2224, 571], earlier_half [0.2141, 495]) | no | not supported |
| V12 | Entries with a fraction have smaller whole-number parts | 0.043 (with_fraction_mean_log [1.453, 123], without [1.6831, 1097]) | no | nominal (p 0.043) |
| V15 | Oil amounts differ in size by ligature adjunct | 0.2089 (between_SS 5.86, null 4.02, entries 63) | no | not supported |
| V16 | The first entry is the largest more often than chance | 0.017 (first_is_max 32/137, null 22.1) | yes | **supported** |
| V17 | Equal amounts stand on neighbouring lines more often than chance | 0.0005 (adjacent_equal 292, null 249.1) | yes | **supported**; holds without 1s (160 vs 133, p 0.0005) |

**What the round adds.**

- **Equal amounts are grouped (V17).** Neighbouring entries carry the same amount more often than chance, even leaving out the 1s of personnel lists (160 against 133). Scribes grouped entries of equal size, which goes with the largest-first habit.
- **The first entry is often the largest (V16).** 32 of 137 lists open with their unique largest entry, against 22 by chance. This refines the largest-first habit: the head of a list is its biggest item.
- **Totals go with longer lists (V7).** Lists that end in KU-RO have 6.7 entries on average, against 4.8 for lists without a total.
- **Grain round numbers are mostly a size effect (V1).** Grain amounts are multiples of 5 far more often (47% against 19%), but among amounts of 10 and more the difference shrinks to 59% against 42% (p 0.038).
- **Not supported:**
  - halves with odd numbers (V3);
  - longer lists balancing less often (V8), or wrong totals falling short (V9: 9 of 18);
  - fractions late in a list (V10), or oil amounts by ligature (V15);
  - smaller whole parts beside fractions is only nominal (V12, p 0.043).

# Thirty-fourth (loop 6 of 10) round: scribes and archives, 24 September 2026

`reading/round34.py`, results in `reading/round34_results.json` and `reading/round34_output.txt`.

Ten hypotheses on whether recording habits depend on the Haghia Triada scribe (tablet sides merged; scribes with three or more tablets). Benjamini–Hochberg at 5% across the ten. A within-commodity check for W4 was added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| W1 | List length differs by scribe | 0.0065 (between_SS 12.18, null 6.305, tablets 110) | yes | **supported** |
| W2 | Use of KU-RO totals differs by scribe | 0.013 (between_SS 4.223, null 2.138, tablets 110) | yes | **supported** |
| W3 | Use of word dividers differs by scribe | 0.8236 (between_SS 4.282, null 5.942, tablets 84) | no | not supported |
| W4 | The fraction values used differ by scribe | 0.0005 (chi2 239.2, null 144.4, tokens 155) | yes | not robust: within commodity p 0.22 (58 tokens) |
| W5 | Syllable use differs by scribe (transaction terms removed) | 0.013 (chi2 975.4, null 867.1, tokens 926) | yes | **supported** |
| W6 | Scribes with more tablets balance their totals more often | 1 (rho -0.4, scribes 4) | no | not testable (4 scribes) |
| W7 | Amount size differs by scribe within the same commodity | 0.001 (between_SS 124.22, null 69.28, entries 144) | yes | **supported** |
| W8 | Strictness of largest-first order differs by scribe | 0.8856 (between_SS 1.196, null 2.52, lists 43) | no | not supported: uniform across scribes |
| W9 | Oil ligature adjuncts differ by scribe | 0.001 (chi2 52.1, null 24.8, tokens 27) | yes | supported, on 27 tokens |
| W11 | Use of single signs differs by scribe | 0.083 (between_SS 0.316, null 0.214, tablets 110) | no | suggestive |

**What the round adds.**

- **Each scribe had a recognisable way of keeping lists (W1, W2, W7).** Scribes differ in how long their lists are, in whether they close them with a KU-RO total, and in the size of the amounts they record *within the same commodity*. The last means a scribe dealt with a scale of transaction, not only with a product.
- **Scribes differ in vocabulary (W5).** Their syllable use differs with transaction terms removed, which fits their keeping different people and subjects (rounds 18–23).
- **Oil ligatures follow the scribe (W9),** on only 27 tokens. With the regional result of round 23, the adjuncts look like the categories of particular offices.
- **The fraction values follow the commodity, not the scribe (W4).** The scribal difference disappears when scribes are compared within one commodity.
- **Some practice was shared by everyone:** largest-first order is equally strict for all scribes (W8), and word dividers are used alike (W3).

# Thirty-fifth (loop 7 of 10) round: variation between sites, 24 September 2026

`reading/round35.py`, results in `reading/round35_results.json` and `reading/round35_output.txt`.

Ten hypotheses on differences between sites (tablet sides merged). Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| X1 | List length differs by site | 0.0005 (between_SS 49.938, null 4.454, tablets 349) | yes | **supported** |
| X2 | Use of KU-RO totals differs by site | 0.0005 (between_SS 2.651, null 0.541, tablets 350) | yes | **supported** |
| X3 | Use of word dividers differs by site | 0.4553 (between_SS 2.349, null 2.544, tablets 212) | no | not supported |
| X5 | Fractions per entry differ by site within commodity | 0.024 (between_SS 3.88, null 1.974, entries 356) | yes | supported |
| X6 | The share of entries equal to 1 differs by site within commodity | 0.1744 (between_SS 1.771, null 1.228, entries 356) | no | not supported |
| X9 | Word length differs by site | 0.0005 (between_SS 26.12, null 5.27, words 672) | yes | **supported** |
| X10 | Use of single signs differs by site | 0.8721 (between_SS 0.059, null 0.136, tablets 349) | no | not supported |
| X11 | Q-row signs are word-initial at HT and outside HT, each more than in Linear B | 0.0005 (HT {'share': 0.731, 'n': 26, 'p': 0.0005}, other {'share': 0.52, 'n': 25, 'p': 0.0005}, LB 0.277, p (larger) 0.0005) | yes | **supported** (replication) |
| X12 | Khania uses the consonant rows in different proportions from Haghia Triada | 0.0015 (chi2 36.4, null 12.0, syllables 1152) | yes | **supported** |
| X14 | Tablets opening with a heading word differ by site | 0.7026 (between_SS 1.226, null 1.765, tablets 212) | no | not supported |

**What the round adds.**

- **Totals were a Haghia Triada habit (X2).** 18% of Haghia Triada tablets end in a KU-RO total, against 3% at Phaistos and Zakros and none at Khania, Knossos, Malia or Arkhalkhori. Haghia Triada also has the longest lists (X1). The written total belonged to one administration's practice, not to Linear A accounting in general.
- **The word-initial Q pattern replicates by region (X11).** Q-row signs are initial 73% of the time at Haghia Triada and 52% elsewhere, against 28% in Linear B.
- **Khania spells with different consonant proportions (X12)** (χ² 36 against 12 by chance). This adds to its distinct signs, ligatures and vowel spelling (rounds 23–25).
- **Word length (X9) and fraction use within a commodity (X5, p 0.024) differ by site.**
- **Shared across sites:** word dividers (X3), single signs (X10), entries of 1 (X6) and opening headings (X14).

# Thirty-sixth (loop 8 of 10) round: the religious texts, 24 September 2026

`reading/round36.py`, results in `reading/round36_results.json` and `reading/round36_output.txt`.

Ten hypotheses on the religious inscriptions (stone vessels, libation tables, metal objects, inked and other non-administrative texts). Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| Y1 | The formula words keep a fixed order across inscriptions | 0.0005 (in_order_pairs 36/36, null 17.9, inscriptions 11) | yes | **supported** (replicates Davis 2014) |
| Y2 | Religious word types are attested at 2+ sites more often than administrative ones | 0.1504 (religious [0.0613, 212], admin [0.0406, 689]) | no | not supported |
| Y3 | Religious vocabulary repeats more than administrative vocabulary of the same size | 0.7886 (type_token_religious 0.836, admin_same_size 0.822, tokens 268) | no | not supported |
| Y4 | Q-row signs are word-initial in religious words more than in Linear B | 0.3098 (religious 0.333, LB 0.277) | no | not supported: the Q pattern is administrative only |
| Y5 | Inscription length differs by object type | 0.003 (between_SS 51.66, null 12.52) | yes | **supported** |
| Y6 | Non-formula religious words are more name-shaped than formula words | 0.2399 (nonformula_mean 0.015, formula_mean -0.021, n [154, 36]) | no | not supported |
| Y7 | Same-site inscriptions share non-formula words more than cross-site ones | 1 (diff -0.0012, null -0.0, inscriptions 129) | no | not supported |
| Y8 | Religious words in -TE are attested at a single site more often | 0.6257 (TE_single_site [0.9444, 18], other [0.9272, 206]) | no | not supported |
| Y9 | Religious texts repeat word pairs more than administrative texts of the same size | 0.8262 (religious 0.087, admin_same_size 0.197) | no | not supported (religious repeat pairs less) |
| Y10 | *301 is concentrated in religious words relative to other unread signs | 0.2129 (301_religious [0.0828, 290], other_unread_religious [0.0651, 584]) | no | not supported |

**What the round adds.**

- **The formula order is fixed (Y1).** In the 11 inscriptions with two or more formula words, all 36 pairs follow the canonical order (A-TA-I-*301-WA-JA, JA-SA-SA-RA-ME, U-NA-KA-NA-SI, I-PI-NA-MA, SI-RU-TE), against 18 expected. This replicates Davis (2014) with a pre-stated test.
- **Longer dedications on stone and metal (Y5).** Stone vessels and metal objects carry about 2.4 words per inscription, clay vessels and stone objects about 1.2.
- **The word-initial Q pattern is administrative (Y4).** In religious words Q-row signs are initial 33% of the time, close to Linear B's 28%. The pattern of rounds 29 and 35 belongs to the administrative vocabulary. It may be a property of particular words (QA-, QE- names and terms) rather than of the sound system.
- **Not supported:**
  - the non-formula words of the dedications are not name-shaped (Y6), and are not shared by inscriptions from the same site (Y7);
  - -TE words are not more site-bound (Y8);
  - *301 is not concentrated in religious words beyond other unread signs (Y10);
  - religious vocabulary does not repeat more (Y3), and repeats word pairs *less* than administrative texts (Y9).

# Thirty-seventh (loop 9 of 10) round: Minoan-derived words outside Linear A, 24 September 2026

`reading/round37.py`, results in `reading/round37_results.json` and `reading/round37_output.txt`.

Ten hypotheses asking whether Minoan-derived words outside Linear A share the patterns found in this loop (word-initial Q, few vowel signs inside words or at their ends). Benjamini–Hochberg at 5% across the ten. Checks removing the Greek -eus names (spelled -e-u) were added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| Z1 | Knossos names begin with a Q-row sign more often than Pylos names | 0.0085 (target 0.0518, comparison 0.0177, n [637, 339]) | yes | **supported** |
| Z2 | Knossos names have fewer internal vowel signs than Pylos names | 0.0005 (target 0.1413, comparison 0.2655, n [637, 339]) | yes | **artefact**: -eus names; strictly internal with -e-u removed, 8.2% vs 7.5% (p 0.68) |
| Z3 | Knossos names end in a pure vowel sign less often than Pylos names | 0.0005 (target 0.0502, comparison 0.1947, n [637, 339]) | yes | **supported**; holds without -eus names (1.0% vs 4.2%, p 0.0035) |
| Z4 | Pre-Greek stems have fewer internal vowel signs than Greek stems | 0.002 (target 0.2073, comparison 0.2581, n [1143, 1143]) | yes | **supported** |
| Z5 | Eteocretan has fewer internal vowel signs than Greek | 0.6032 (target 0.5714, comparison 0.563, n [35, 119]) | no | not supported |
| Z6 | Cretan place names have fewer internal vowel signs than Pylos place names | 0.0005 (target 0.0685, comparison 0.2917, n [73, 120]) | yes | weakened by the check (p 0.053) |
| Z7 | Linear A's vowel profile is closer to Pre-Greek than to Greek | 0.0005 (jsd_LA_PreGreek 0.0433, jsd_LA_Greek 0.0951) | yes | **supported** |
| Z8 | Linear A's consonant profile is closer to Pre-Greek than to Greek | 0.9995 (jsd_LA_PreGreek 0.1281, jsd_LA_Greek 0.112) | no | not supported |
| Z9 | Knossos common words without a Greek etymology are more Linear A-like | 0.046 (auc 0.564, n [199, 80]) | no | nominal (p 0.046) |
| Z10 | Knossos tablets with undeciphered-sign words carry more Minoan-shaped names | 0.6557 (with_star_words [-0.2255, 45], without [-0.1711, 557]) | no | not supported |

**What the round adds.**

- **Knossos names share two Linear A word-shape habits (Z1, Z3).** They begin with a Q-row sign more often than Pylos names (5.2% against 1.8%). They rarely end in a pure vowel sign (5.0% against 19.5%), and still do so with the Greek -eus names removed (1.0% against 4.2%). These are the Linear A patterns of round 29 (P6, P9) turning up in Minoan names written by Greek scribes.
- **Pre-Greek words avoid vowel sequences (Z4) and share Linear A's vowel profile (Z7).** Pre-Greek stems have fewer internal vowel signs than ordinary Greek stems (20.7% against 25.8%). Their vowel profile is much closer to Linear A's than ordinary Greek's is (JSD 0.043 against 0.095). The consonant profile is not (Z8).
- **The name "hiatus" result was an artefact (Z2).** Knossos names seemed to avoid internal vowel signs (14% against 27%), but that came from Greek -eus names spelled -e-u. With them removed and only strictly internal positions counted, the difference vanishes. Cretan place names keep a weaker difference (Z6, p 0.053).
- **Not supported:** Eteocretan vowel sequences (Z5), undeciphered-sign words beside Minoan names on the same tablets (Z10), and Knossos non-Greek common words (Z9, nominal p 0.046).

# Thirty-eighth (loop 10 of 10) round: replications of the loop results, 24 September 2026

`reading/round38.py`, results in `reading/round38_results.json` and `reading/round38_output.txt`.

The last round of the loop replicates its surviving results on other data or definitions: SigLA's independent transcription, other subsets of lists, a mainland comparison, an unmatched Greek sample. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| AA1 | Q-row signs word-initial (SigLA vs Linear B) | 0.0005 (target 0.5652, comparison 0.277) | yes | **replicated** |
| AA2 | Two vowel signs in succession rarer (SigLA vs Linear B) | 0.0005 (target 0.0, comparison 0.0195) | yes | **replicated** |
| AA3 | Final pure vowel signs rarer (SigLA vs Linear B) | 0.0005 (target 0.0354, comparison 0.1054) | yes | **replicated** |
| AA4 | e/o follow T (SigLA vs Linear B) | 0.0005 (target 0.6954, comparison -0.1313) | yes | **replicated** |
| AA5 | e/o follow Q more than K (SigLA vs Linear B) | 0.001 (target 1.9811, comparison 0.7286) | yes | **replicated** |
| AA6 | Equal amounts on neighbouring lines outside Haghia Triada (1s excluded) | 0.066 (adjacent_equal 58, null 51.6, lists 74) | no | not replicated outside HT (p 0.066) |
| AA7 | The first entry is the unique largest (lists of 4+) | 0.0235 (first_is_max 22/105, null 14.4) | yes | **replicated** |
| AA9 | Tablet-mates share first signs (SigLA tablets, unique words, within-site shuffle) | 0.4478 (pairs 116, null 114.1, tablets 98) | no | **not replicated**: S6 withdrawn |
| AA10 | Knossos names begin with Q more often than Thebes/Mycenae/Tiryns names | 0.0985 (target 0.0518, comparison 0.0) | no | not significant (46 mainland names, none Q-initial) |
| AA11 | Linear A vowel profile closer to Pre-Greek than to an unmatched Greek sample | 0.0005 (jsd_PreGreek 0.0433, jsd_Greek_unmatched 0.1007) | yes | **replicated** |

**What the round adds.**

- **Linear A word shape is confirmed on SigLA (AA1–AA3).** Q-row signs start words (57% against 28% in Linear B). Two vowel signs in a row never occur (0% against 2%). Words seldom end in a pure vowel sign (3.5% against 10.5%). Minoan words, as Linear A spells them, were strings of consonant-vowel syllables without vowel sequences, and the labiovelars stood at the start.
- **The e/o consonant pattern is confirmed on SigLA (AA4, AA5).** e/o follow T (logOR 0.70 against −0.13 in Linear B) and Q rather than K (1.98 against 0.73).
- **The first entry of a list is its largest (AA7),** also in lists of four or more entries (22 of 105 against 14 by chance).
- **Linear A's vowels are closer to Pre-Greek than to Greek (AA11),** also against an unmatched Greek sample (JSD 0.043 against 0.101).
- **Withdrawn or unconfirmed:** tablet-mates sharing first signs (S6) does not replicate on SigLA. Grouped equal amounts are not confirmed outside Haghia Triada (p 0.066). The Q-initial Knossos names cannot be confirmed against the small mainland name stock.

**Summary of the loop (rounds 29–38, 100 hypotheses).** About a third survived the correction, and fewer survived the checks and replications. Four new results stand:
- **Word shape:** Linear A avoids vowel sequences and final pure vowels, and puts Q-row signs first. This replicates on SigLA, and parts of it appear in Knossos names.
- **The e/o consonant pattern, by consonant:** T, R, S, N and Q take e/o; K, P, M, J and W avoid them.
- **Minoan names beyond Pylos:** stem-scored, Knossos names are more Minoan than Thebes/Mycenae/Tiryns names.
- **Bookkeeping:** totals are a Haghia Triada habit, scribes keep their own list styles and scales, and the first entry is the largest.

Several apparent results were artefacts and are recorded as such: the -eus hiatus (Z2), shared first signs (S6), and the fraction values by scribe (W4).

# Thirty-ninth (second loop 1 of 10) round: word-shape follow-ups, 24 September 2026

`reading/round39.py`, results in `reading/round39_results.json` and `reading/round39_output.txt`.

Ten follow-ups to the word-shape results of the first loop, each against Linear B. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| BB1 | Q-initial share counting each initial sign pair once | 0.0055 (LA 0.7241, LB 0.5294) | yes | **supported** |
| BB2 | J-row signs word-initial less often | 1 (LA 0.3582, LB 0.0437) | no | **reversed**: J-initial 36% vs 4% (JA- words) |
| BB3 | W-row signs word-final less often | 0.7496 (LA 0.3571, LB 0.3341) | no | not supported |
| BB5 | Special signs word-internal more often | 0.9775 (LA 0.2857, LB 0.5165) | no | reversed: special signs are internal less often |
| BB6 | Neighbouring syllables repeat the consonant more often | 0.0005 (LA 0.054, LB 0.0298) | yes | **supported** |
| BB7 | Initial and final consonant distributions differ more | 0.999 (LA 0.1234, LB 0.1603) | no | not supported |
| BB8 | Z-row signs word-final more often | 0.2574 (LA 0.4444, LB 0.3816) | no | not supported |
| BB9 | First syllables favour a over later syllables more | 0.6422 (LA 0.0773, LB 0.085) | no | not supported |
| BB10 | Q-initial words are entry labels more often | 0.3108 (Q_initial [0.68, 25], other [0.6088, 547]) | no | not supported |
| BB11 | Final consonants more restricted than initial ones | 0.0075 (LA 0.0454, LB 0.1317) | yes | **supported** |

**What the round adds.**

- **The Q-initial pattern is not a few word families (BB1).** Counting each word-initial sign pair once, Q-row signs still start words 72% of the time, against 53% in Linear B.
- **Consonants repeat in neighbouring syllables (BB6).** 5.4% of neighbouring syllable pairs share their consonant, against 3.0% in Linear B (SA-SA, KU-KA, TA-TI and the like). Partial reduplication or consonant harmony was a feature of Minoan word shape.
- **Endings are more restricted than beginnings (BB11),** relative to Linear B. Linear A finals draw on a narrower set of consonants.
- **J-row signs start words (BB2, reversed).** J is word-initial 36% of the time in Linear A, against 4% in Linear B, through the JA- words of the religious texts and lists.
- **Not supported:** W final (BB3), Z final (BB8), a-initial (BB9), and Q-initial words as names (BB10). Special signs are internal *less* often (BB5).

# Fortieth (second loop 2 of 10) round: the e/o rule with the refined consonant sets, 24 September 2026

`reading/round40.py`, results in `reading/round40_results.json` and `reading/round40_output.txt`.

Ten hypotheses using the consonant sets of round 30: T, R, S, N, Q take e/o; K, P, M, J, W avoid them. Benjamini–Hochberg at 5% across the ten. **Caution:** the sets were chosen on Linear A data, so the within-Linear A tests (CC1, CC2, CC9, CC11) are partly circular. SigLA shares 470 word types with lineara.xyz, and Khania is part of Linear A. The informative tests are CC4, CC5 and the outside records.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| CC1 | The rule holds in first syllables | 0.0005 (target 1.481, comparison -0.124, n [760, 4866]) | yes | supported (partly circular) |
| CC2 | The rule holds in final syllables | 0.0005 (target 1.243, comparison -0.087, n [760, 4866]) | yes | supported (partly circular) |
| CC4 | i/u are depleted after the e/o-taking consonants more than in Linear B | 0.0005 (logOR_iu_LA -0.191, logOR_iu_LB 0.347) | yes | **supported** |
| CC5 | e versus o depends on the consonant more than in Linear B | 0.002 (nmi_LA 0.33, nmi_LB_subsampled 0.083) | yes | **supported** |
| CC6 | Knossos names (ending removed) show the rule more than Pylos names | 0.5867 (target -0.263, comparison -0.211, n [637, 339]) | no | not supported |
| CC7 | Cretan place names show the rule more than Pylos place names | 0.8711 (target -0.521, comparison -0.015, n [58, 119]) | no | not supported |
| CC8 | Pre-Greek stems show the rule more than Greek stems | 0.998 (target -0.351, comparison -0.011, n [1143, 1143]) | no | not supported |
| CC9 | The rule holds on SigLA's transcription | 0.0005 (target 1.437, comparison -0.138, n [536, 4866]) | yes | supported (partly circular) |
| CC10 | Eteocretan shows the rule more than Greek | 0.7061 (target -0.217, comparison 0.057, n [35, 119]) | no | not supported |
| CC11 | Khania's Linear A shows the rule | 0.0005 (target 0.976, comparison -0.138, n [68, 4866]) | yes | supported (partly circular) |

**What the round adds.**

- **e and o are each tied to particular consonants (CC5).** Within e/o syllables, whether the vowel is e or o depends on the consonant four times more than in Linear B (normalised MI 0.33 against 0.08). Linear A has RO, QO and TO but TE, NE, SE and RE, so the two vowels are not interchangeable variants of one sound. Each is attached to its own set of syllables.
- **They replace i/u (CC4).** After T, R, S, N and Q, i and u are depleted relative to K, P, M, J and W, where in Linear B they are not (logOR −0.19 against 0.35).
- **The rule does not travel.** Knossos names, Cretan place names, Pre-Greek words and Eteocretan (CC6–CC8, CC10) show no trace of it. On present evidence it is a convention of Linear A spelling, or a feature of Minoan that Greek transmission erased.
- **The within-Linear A tests** (first syllables 1.48, final syllables 1.24, SigLA 1.44, Khania 0.98, against Linear B −0.1) confirm the pattern everywhere in Linear A, but they are partly circular, because the sets were chosen on this data.

# Forty-first (second loop 3 of 10) round: Linear A list names, 24 September 2026

`reading/round41.py`, results in `reading/round41_results.json` and `reading/round41_output.txt`.

Ten hypotheses on the Linear A entry labels (list names). Benjamini–Hochberg at 5% across the ten. **None survives.**

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| DD1 | Entry labels repeat the consonant of neighbouring syllables more often | 0.6637 (entries 0.0453, others 0.0509, n [358, 222]) | no | not supported |
| DD2 | Entry labels end on a narrower set of final signs | 0.0265 (entries 3.6653, others 3.7318, n [358, 222]) | no | nominal (p 0.027) |
| DD3 | Entry labels ending in -TI stand on VIR tablets more often | 0.0055 (TI_on_VIR [0.3571, 28], other_on_VIR [0.1415, 530]) | no | suggestive: misses the corrected threshold narrowly (0.0055 vs 0.005) |
| DD4 | Entry labels contain unread signs less often than headings | 0.9865 (entries 0.2025, headings 0.1379) | no | **reversed**: entry labels contain unread signs more often (20% vs 14%) |
| DD5 | Entry labels on VIR tablets differ in syllable profile from those on tablets of goods | 0.0505 (jsd 0.1259, null 0.0978, n [49, 297]) | no | suggestive (p 0.05) |
| DD6 | Entry labels with amount 1 differ in syllable profile from those with larger amounts | 0.2804 (jsd 0.0684, null 0.0623, n [89, 244]) | no | not supported |
| DD7 | Recurring entry labels match Knossos words more often than one-off labels | 0.2329 (recurring [0.1556, 45], once [0.1086, 313]) | no | not supported |
| DD8 | Entry labels in the same list share syllables more than labels from other lists of the site | 0.2395 (mean_jaccard 0.0499, null 0.0477, lists 57) | no | not supported |
| DD9 | Two-sign entry labels stand on VIR tablets more often | 0.1909 (two_sign_on_VIR [0.1722, 209], longer_on_VIR [0.1404, 349]) | no | not supported |
| DD10 | Entry labels matching Knossos words stand on VIR tablets more often | 0.6927 (matched_on_VIR [0.1273, 55], other_on_VIR [0.144, 389]) | no | not supported |

**What the round adds.**

- **-TI may mark men's names (DD3, suggestive).** Entry labels ending in -TI stand on personnel (VIR) tablets 36% of the time, against 14% for other entry labels (p 0.0055, just above the corrected threshold). With the round-10 result that -TI words are entry labels (M1, p 0.053), -TI is a candidate ending for personal names of men. It needs more data.
- **Names carry more unread signs than headings (DD4, reversed).** 20% of entry labels contain an unread sign, against 14% of headings. Personal names used more of the rarer, local signs.
- **Not supported:**
  - names do not repeat consonants more (DD1), and their finals are only nominally more restricted (DD2);
  - names in one list do not resemble each other (DD8);
  - recurring names are not more often Knossos-attested (DD7);
  - neither two-sign names nor Knossos-matched names concentrate on personnel tablets (DD9, DD10).

# Forty-second (second loop 4 of 10) round: Linear A habits in Knossos names, 24 September 2026

`reading/round42.py`, results in `reading/round42_results.json` and `reading/round42_output.txt`.

Ten hypotheses asking whether Knossos names (against Pylos names) share the Linear A habits of this loop. Benjamini–Hochberg at 5% across the ten. **None survives.**

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| EE1 | Knossos names repeat neighbouring consonants more often | 0.2389 (KN 0.024, PY 0.0197, n [637, 339]) | no | not supported |
| EE2 | Knossos names begin with J more often | 0.019 (KN 0.0141, PY 0.0, n [637, 339]) | no | nominal (p 0.019) |
| EE3 | Knossos names contain undeciphered signs more often | 0.0095 (KN 0.0535, PY 0.0202, n [673, 346]) | no | nominal (p 0.0095) |
| EE4 | Knossos names contain special signs more often | 0.9885 (KN 0.0565, PY 0.0944, n [637, 339]) | no | **reversed**: special signs commoner in Pylos names |
| EE5 | Knossos place names repeat neighbouring consonants more often | 0.0575 (KN 0.0427, PY 0.0212, n [73, 120]) | no | suggestive |
| EE6 | Knossos names end in -ti more often | 0.1954 (KN 0.0141, PY 0.0059, n [637, 339]) | no | not supported |
| EE7 | Knossos common words repeat neighbouring consonants more often (control) | 0.081 (KN 0.0338, PY 0.023, n [279, 345]) | no | suggestive |
| EE8 | Knossos names contain Q-row signs more often | 0.2679 (KN 0.1162, PY 0.1003, n [637, 339]) | no | not supported |
| EE9 | Knossos names contain Z-row signs more often | 0.017 (KN 0.0455, PY 0.0177, n [637, 339]) | no | nominal (p 0.017) |
| EE10 | Knossos name stems end on a narrower set of consonants | 0.0985 (KN 0.2878, PY 0.3757, n [637, 339]) | no | suggestive |

**What the round adds.**

- **Nothing survives the correction, but three differences point the same way.** Knossos names contain undeciphered signs more often (5.4% against 2.0%, p 0.0095). They contain Z-row signs more often (4.6% against 1.8%, p 0.017). A few begin with J (1.4% against none at Pylos, p 0.019). Each is a Linear A trait (unread signs, the Z series, JA- words), but none is individually significant after correction.
- **Special signs are commoner in Pylos names (EE4, reversed),** so they are not a Minoan marker in Linear B.
- **Consonant repetition is only a lean:** in Knossos place names (EE5, p 0.06) and in the common-word control (EE7, p 0.08), and not in names (EE1). The -ti ending (EE6) and Q anywhere in the word (EE8) show nothing, and the final-consonant restriction only leans (EE10, p 0.10).

# Forty-third (second loop 5 of 10) round: the bookkeeping, second pass, 24 September 2026

`reading/round43.py`, results in `reading/round43_results.json` and `reading/round43_output.txt`.

Ten hypotheses on list organisation. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| FF1 | At HT, lists with a total are more strictly largest-first | 0.005 (with_total_tau [0.4389, 24], without [0.1113, 77]) | yes | **supported** |
| FF2 | Lists with a total are single-commodity more often | 0.1889 (with_total [0.7222, 18], without [0.5789, 114]) | no | not supported |
| FF3 | KI-RO stands on tablets with KU-RO more often than chance | 1 (kiro_tablets_with_kuro [0.3636, 11], others_with_kuro [1.0, 26]) | no | **invalid test**: the comparison set contained only tablets with KI-RO or KU-RO, so "others" were all KU-RO tablets |
| FF4 | The first entry is the unique largest in lists of goods | 0.0575 (first_is_max 27/122, null 20.3) | no | suggestive (p 0.058) |
| FF5 | Tablets with fractions carry a total more often | 0.9935 (with_fractions [0.0732, 123], without [0.1631, 141]) | no | reversed: tablets with fractions carry totals less often |
| FF6 | Lists of men are longer than lists of goods | 0.001 (VIR_lists [7.1538, 26], goods_lists [4.3672, 128]) | yes | **supported** |
| FF7 | Fraction entries stand on neighbouring lines more often than chance | 0.004 (adjacent 126, null 113.6) | yes | **supported** |
| FF8 | Lists that open with a heading are longer | 0.1989 (with_heading [5.1935, 93], without [4.7714, 140]) | no | not supported |
| FF9 | Multi-commodity tablets list commodities in a consistent order | 0.0005 (order_asymmetry 59, null 27.9, tablets 53) | yes | **supported** |
| FF10 | Same-commodity entries stand in blocks more often than chance | 0.069 (adjacent_same 60, null 53.3, lists 38) | no | suggestive (p 0.069) |

**What the round adds.**

- **A fixed order of commodities (FF9).** On tablets recording several commodities, they appear in a consistent order across tablets (order asymmetry 59 against 28 by chance). Grain comes before oil (16 tablets), oil before olives (9), cyperus before wine (8), oil before wine (7), and grain before olives, wine and men. Minoan scribes had a canonical sequence of goods.
- **Totalled lists are ordered lists (FF1).** At Haghia Triada, lists that end in a KU-RO total are much more strictly largest-first (Kendall tau 0.44) than lists without a total (0.11). Largest-first ordering and totalling went together as one practice.
- **Lists of men are longer (FF6)** (7.2 entries against 4.4 for goods), and **fraction entries sit together (FF7)**: entries carrying fractions stand on neighbouring lines more than chance.
- **Tablets with fractions carry totals less often (FF5, reversed),** and FF3 was an invalid test (see table).

# Forty-fourth (second loop 6 of 10) round: commodity order, persons and commodities, 24 September 2026

`reading/round44.py`, results in `reading/round44_results.json` and `reading/round44_output.txt`.

Ten hypotheses following the canonical commodity order of round 43 and the persons–commodity link. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| GG1 | The commodity order holds at Haghia Triada | 0.0005 (asymmetry 50, null 20.8, tablets 36) | yes | **supported** |
| GG2 | The commodity order holds outside Haghia Triada | 0.094 (asymmetry 19, null 14.6, tablets 17) | no | suggestive (p 0.09, 17 tablets) |
| GG3 | Linear A commodity order agrees with Linear B order | 0.002 (agreement 0.704, null 0.5, pairs 54) | yes | **supported** |
| GG4 | The commodity order holds with tablet sides merged | 0.0005 (asymmetry 57, null 28.5, tablets 50) | yes | **supported** |
| GG5 | Same-commodity tablets share entry labels (within-site shuffle) | 0.035 (diff 0.0465, null 0.008, tablets 43) | yes | supported |
| GG8 | On tablets with both, grain amounts exceed oil amounts | 0.0106 (grain_larger 13/16, sign_test_p 0.0106) | yes | supported |
| GG9 | The first commodity carries the largest amount more often than chance | 0.0005 (first_has_max 30/53, null 17.8) | yes | **supported** (overlaps with grain being first and large) |
| GG10 | Wine stands last more often than chance | 0.0015 (VIN_last 13/17, null 6.7) | yes | **supported** |
| GG11 | Cyperus and wine stand on the same tablets beyond chance | 0.4683 (together 8, null 7.42) | no | not supported |
| GG12 | Oil and olives stand on the same tablets beyond chance | 0.0005 (together 11, null 4.13) | yes | **supported** |

**What the round adds.**

- **The order of goods carried over into Linear B (GG3).** For pairs of commodities that Linear B lists in a majority order, Linear A tablets follow the same order 70% of the time, against 50% by chance (p 0.002, 54 pairs). Both put grain before olives, cyperus, wine and oil, and wine late. The Mycenaean administration kept the Minoan sequence for listing goods, as it kept the script and the logograms.
- **The order is robust at Haghia Triada and with sides merged (GG1, GG4).** Outside Haghia Triada it points the same way on 17 tablets (GG2, p 0.09).
- **Wine last, grain first and largest (GG10, GG9, GG8).**
  - Wine is the last commodity on 13 of 17 tablets that record it.
  - The first commodity carries the tablet's largest amount on 30 of 53 tablets, against 18 by chance.
  - On tablets with both, grain amounts exceed oil amounts on 13 of 16.
  - The three overlap: grain is usually first and usually large.
- **Oil and olives go together (GG12)** (11 tablets against 4 by chance). Cyperus and wine do not (GG11).
- **Persons tied to commodities holds within sites (GG5,** p 0.035).

# Forty-fifth (second loop 7 of 10) round: the signs, 24 September 2026

`reading/round45.py`, results in `reading/round45_results.json` and `reading/round45_output.txt`.

Ten hypotheses on the signs themselves. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| HH1 | Unread signs are word-initial more often than known signs | 0.0015 (unread_initial [0.4343, 198], known_initial [0.3179, 2746]) | yes | **supported** |
| HH3 | Tablet single signs are the commonest word syllables | 0.0002 (spearman 0.654, signs 51) | yes | **supported** |
| HH4 | Single signs on sealings differ in repertoire from those on tablets | 0.0005 (chi2 633.7, null 31.9, tokens 1012) | yes | **supported** |
| HH5 | *301 is word-internal more often than other signs | 0.0625 (301_internal [0.5217, 23], other_internal [0.3471, 2921]) | no | suggestive (p 0.06) |
| HH6 | Unread signs stand next to other unread signs more than chance | 0.979 (adjacent_unread_pairs 14, null 15.99) | no | not supported |
| HH7 | Unread signs are confined to fewer word types per occurrence | 0.0395 (unread_resid [-0.1191, 26], known_resid [0.0525, 59]) | no | nominal (p 0.040) |
| HH8 | ZE is followed directly by a number more often than other single signs | 0.5397 (ZE [1.0, 1], other [0.5514, 428]) | no | untestable (ZE occurs once as a single sign on tablets; it is a sealing sign) |
| HH11 | NI is followed directly by a number more often than other single signs | 0.0015 (NI [0.7286, 70], other [0.5181, 359]) | yes | **supported** |
| HH15 | Syllable signs are associated with register | 0.0005 (chi2 135.6, null 49.7, tokens 2618) | yes | **supported** |
| HH16 | Signs Linear B uses word-finally are relatively rarer in Linear A | 0.0326 (spearman -0.272, signs 50) | no | nominal (rho -0.27, p 0.033) |

**What the round adds.**

- **Unread signs start words (HH1).** 43% of unread-sign occurrences are word-initial, against 32% for known signs. With round 25's result that local signs are never word-final, the unread signs belong to the beginnings and roots of words, not to endings. Linear B dropped signs from Minoan roots, which Greek had no use for, rather than from the grammar.
- **NI behaves like a commodity sign (HH11).** As a single sign on tablets, NI is followed directly by a number 73% of the time, against 52% for other single signs. That fits the reading of NI as "figs", the value Linear B later gave it as a logogram.
- **Single signs on tablets are common syllables; sealing signs are a separate system (HH3, HH4).** The single signs on tablets are the syllables commonest in words (rho 0.65), so they are likely abbreviations. Sealings use a very different set (χ² 634 against 32).
- **Register-specific signs (HH15).** The whole syllabary, not only the initial and final signs of round 31, is distributed differently in religious and administrative words.
- **Suggestive only:**
  - signs that Linear B uses at word ends are rarer in Linear A (HH16, rho −0.27, p 0.033), consistent with Linear B repurposing them for Greek endings;
  - unread signs are confined to fewer words (HH7), and *301 sits inside words (HH5).

# Forty-sixth (second loop 8 of 10) round: the religious and administrative vocabularies, 24 September 2026

`reading/round46.py`, results in `reading/round46_results.json` and `reading/round46_output.txt`.

Ten hypotheses comparing the religious and administrative vocabularies. Benjamini–Hochberg at 5% across the ten. Checks without the libation-formula words were added for II2 and II7 after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| II1 | Words in both registers are entry labels more often | 0.9605 (shared_words_entry [0.4167, 12], other_entry [0.6161, 560]) | no | reversed: shared words are entry labels less often |
| II2 | Religious words begin with a pure vowel more often | 0.0005 (religious 0.3579, admin 0.1982, n [190, 560]) | yes | **supported**; holds without the formula (31% vs 20%, p 0.0045) |
| II3 | Religious words repeat neighbouring consonants more often | 0.0965 (religious 0.0626, admin 0.0467, n [190, 560]) | no | not supported |
| II4 | Religious words contain Z-row signs more often | 0.7911 (religious 0.0474, admin 0.0589, n [190, 560]) | no | not supported |
| II5 | Administrative words also found in religious texts occur at more sites | 0.4318 (shared_mean_sites [1.0833, 12], other [1.0536, 560]) | no | not supported |
| II6 | Religious words are two-sign words less often | 0.028 (religious 0.3105, admin 0.3929, n [190, 560]) | no | nominal (p 0.028) |
| II7 | Religious words repeat a whole syllable more often | 0.002 (religious 0.0842, admin 0.0286, n [190, 560]) | yes | formula-driven: without the formula 4.5% vs 2.9% (p 0.22) |
| II8 | Inked inscriptions are closer to administrative texts than to stone dedications | 0.0075 (jsd_to_stone_minus_admin 0.0088, null -0.0952, n [12, 106]) | yes | supported (12 inked words) |
| II9 | Same object type shares words more than different types | 0.0005 (diff 0.031, null 0.0, inscriptions 153) | yes | **supported** |
| II10 | Religious words match Knossos words more often | 0.904 (religious 0.1105, admin 0.1446, n [190, 560]) | no | not supported |

**What the round adds.**

- **Religious words start with a vowel (II2).** 36% of religious word types begin with a pure vowel sign (A-, I-, U-, E-), against 20% of administrative words, and 31% even without the libation formula. The religious vocabulary is built on vowel-initial forms. That fits the A-, I- and U- elements proposed as prefixes in the dedications, though the round-13 test of A- as a prefix found nothing.
- **Object type organises the dedications (II9).** Inscriptions on the same type of object share words more than inscriptions on different types. Inked inscriptions are closer to the administrative vocabulary than to the stone dedications (II8, on only 12 words).
- **Syllable repetition belongs to the formula (II7).** Religious words repeat a whole syllable more often (8.4% against 2.9%) only because of formula words such as JA-SA-SA-RA-ME.
- **Not supported:**
  - the few words shared by both registers are not names (II1, reversed) and do not travel more (II5);
  - religious words do not repeat consonants (II3) or use the Z row (II4) more;
  - they do not match Knossos words more (II10), and are only nominally less often two-sign (II6).

# Forty-seventh (second loop 9 of 10) round: this loop's findings in the other records, 24 September 2026

`reading/round47.py`, results in `reading/round47_results.json` and `reading/round47_output.txt`.

Ten hypotheses taking the second loop's findings to Pre-Greek, Eteocretan and the Knossos and Pylos records. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| KK1 | Linear B commodity order agrees with Linear A more at Knossos than at Pylos | 0.2149 (KN 0.75, PY 0.667, n [27, 13]) | no | not supported (27 vs 13 tablets) |
| KK2 | Pre-Greek words repeat neighbouring consonants more often | 0.0025 (target 0.0482, comparison 0.0305, n [1143, 1143]) | yes | **supported** |
| KK3 | Pre-Greek words repeat a whole syllable more often | 0.0045 (target 0.0236, comparison 0.0096, n [1143, 1143]) | yes | **supported** |
| KK4 | Eteocretan repeats neighbouring consonants more often | 0.0015 (target 0.0972, comparison 0.0147, n [35, 119]) | yes | **supported** (short, unsegmented corpus) |
| KK5 | Eteocretan repeats a whole syllable more often | 0.003 (target 0.1429, comparison 0.0084, n [35, 119]) | yes | **supported** (short, unsegmented corpus) |
| KK6 | Pre-Greek words begin with an a-syllable more often | 0.0005 (target 0.4077, comparison 0.3036, n [1143, 1143]) | yes | **supported** |
| KK7 | Knossos place names begin with Q more often | 0.005 (target 0.0822, comparison 0.0, n [73, 120]) | yes | **supported** |
| KK8 | Knossos common words begin with Q more often | 0.5402 (target 0.0251, comparison 0.0232, n [279, 345]) | no | not supported |
| KK9 | Knossos common words repeat neighbouring consonants more often | 0.078 (target 0.0338, comparison 0.023, n [279, 345]) | no | suggestive |
| KK10 | Pre-Greek words contain Z-row syllables more often | 0.8001 (target 0.0079, comparison 0.0105, n [1143, 1143]) | no | not supported |

**What the round adds.**

- **Repetition inside words is an Aegean substrate trait (KK2–KK5).** Linear A repeats the consonant of neighbouring syllables more than Linear B (round 39). Pre-Greek words do the same (4.8% against 3.1% for Greek words of the same length) and repeat whole syllables (2.4% against 1.0%). Eteocretan shows it strongly (9.7% against 1.5%, whole syllables 14% against 0.8%). Two cautions:
  - reduplicated shapes are among the features Beekes used to recognise Pre-Greek words, so part of the Pre-Greek result may be built into the list;
  - the Eteocretan texts are short, unsegmented and repetitive.
- **Pre-Greek words begin with a-syllables (KK6)** (41% against 30%), matching Linear A's a-rich profile.
- **Q-initial belongs to names and places (KK7, KK8).** Knossos place names begin with a Q-row sign 8.2% of the time, against none at Pylos. Knossos common words do not differ from Pylos ones. With the Knossos personal names of round 37, the Q-initial habit is carried by Minoan proper names.
- **Not supported:**
  - Linear B's agreement with the Linear A commodity order is not stronger at Knossos than at Pylos (KK1, 75% against 67%, few tablets);
  - Pre-Greek does not have more Z-row syllables (KK10).

# Forty-eighth (second loop 10 of 10) round: replications of the second loop, 24 September 2026

`reading/round48.py`, results in `reading/round48_results.json` and `reading/round48_output.txt`.

The last round of the second loop replicates its surviving results on SigLA, on other subsets, or against other comparison sets. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| LL1 | Neighbouring consonant repetition (SigLA vs Linear B) | 0.0005 (target 0.0558, comparison 0.0298) | yes | **replicated** |
| LL2 | Final consonants more restricted (SigLA vs Linear B) | 0.018 (target 0.0373, comparison 0.1317) | yes | **replicated** |
| LL3 | e versus o depends on the consonant (SigLA) | 0.002 (nmi_SigLA 0.325, nmi_LB 0.094) | yes | **replicated** |
| LL4 | The commodity order holds with grain removed | 0.0035 (asymmetry 30, null 16.1, tablets 35) | yes | **replicated** |
| LL5 | Agreement with Linear B order on pairs without grain | 0.3998 (agreement 0.556, null 0.497) | no | **not replicated**: the Linear B agreement rests on grain first |
| LL6 | Unread signs word-initial more often, at HT and elsewhere | 0.044 (HT {'flagged': [0.4396, 91], 'rest': [0.3484, 1151], 'p': 0.044}, other {'flagged': [0.4259, 108], 'rest': [0.3025, 1663], 'p': 0.0065}, p (larger) 0.044) | no | not confirmed after correction (p 0.044) |
| LL7 | NI followed by a number more often, at HT and elsewhere | 0.0215 (HT {'flagged': [0.7805, 41], 'rest': [0.5871, 201], 'p': 0.0165}, other {'flagged': [0.6552, 29], 'rest': [0.4304, 158], 'p': 0.0215}, p (larger) 0.0215) | yes | **replicated** |
| LL8 | Religious words vowel-initial more often (SigLA) | 0.0725 (target 0.36, comparison 0.2115) | no | not confirmed (p 0.07) |
| LL9 | Lists with a total more strictly largest-first (5+ entries) | 0.001 (with_total_tau [0.4794, 21], without [0.1124, 62]) | yes | **replicated** |
| LL10 | Pre-Greek consonant repetition against an unmatched Greek sample | 0.001 (target 0.0482, comparison 0.0305) | yes | **replicated** |

**What the round adds.**

- **Replicated on SigLA (LL1–LL3):**
  - neighbouring syllables repeat their consonant (5.6% against 3.0% in Linear B);
  - final consonants are more restricted than initial ones;
  - the choice between e and o depends on the consonant (normalised MI 0.33 against 0.09).
- **The commodity order does not depend on grain (LL4),** but the Linear B agreement does (LL5). Without grain, Linear A's order is still consistent across tablets (asymmetry 30 against 16). Agreement with Linear B on pairs not involving grain, however, is only 56% against 50% (p 0.40). What Linear B demonstrably shares with Linear A is putting grain first. The rest of the Linear A order is not shown to have passed into Linear B. The page is corrected.
- **Also replicated:**
  - NI behaves as a commodity sign at Haghia Triada and elsewhere (LL7);
  - totalled lists are more strictly largest-first in lists of five or more (LL9, tau 0.48 against 0.11);
  - Pre-Greek consonant repetition holds against an unmatched Greek sample (LL10).
- **Not confirmed after correction:** unread signs as word-initial at each site separately (LL6, p 0.044), and vowel-initial religious words on SigLA (LL8, p 0.07).

**Summary of the second loop (rounds 39–48, 100 hypotheses).** New results that survived their checks and replications:
- **Word shape:** neighbouring syllables repeat consonants, finals are restricted, and the Q-initial habit holds (in names and place names, not common words). Pre-Greek and Eteocretan share the repetition.
- **Vowels:** e and o are each tied to their own consonants, not interchangeable.
- **Bookkeeping:**
  - a consistent order of commodities (grain first, wine last), of which Linear B demonstrably shares only grain first;
  - totalled lists ordered largest-first;
  - NI used as a commodity sign.
- **Signs:** unread signs belong to word beginnings, and sealing signs are a separate system.

Withdrawn or unconfirmed: the full Linear B continuity of the commodity order, the -TI men's ending, and several register and name tests.

# Forty-ninth round: twenty follow-ups to the strongest results, 24 September 2026

`reading/round49.py`, results in `reading/round49_results.json` and `reading/round49_output.txt`.

Twenty hypotheses following the strongest results of the two loops. Benjamini–Hochberg at 5% across all twenty.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| TT1 | Same consonant, different sign, in neighbouring syllables: Linear A vs Linear B | 0.0005 (target 0.0341, comparison 0.021, n [760, 4866]) | yes | **supported** |
| TT2 | Consonant repetition in Linear A entry labels vs Linear B | 0.0105 (target 0.0453, comparison 0.0298, n [358, 4866]) | yes | **supported** |
| TT3 | Consonant repetition at HT and elsewhere, each vs Linear B | 0.0005 (HT {'rate': 0.0538, 'p': 0.0005}, other {'rate': 0.0513, 'p': 0.0005}, LB 0.0298, p (larger) 0.0005) | yes | **supported** |
| TT4 | Pre-Greek: same consonant, different sign, vs Greek | 0.087 (target 0.0317, comparison 0.0238, n [1143, 1143]) | no | **not supported**: Pre-Greek repetition rests on identical syllables (p 0.087 without them) |
| TT11 | Repetition rates by consonant: Linear A correlates with Pre-Greek more than with Greek | 0.5808 (rho_diff -0.071, null 0.019) | no | not supported |
| TT12 | Repetition concentrated in the first two syllables, more than in Linear B | 0.6772 (target 0.0034, comparison 0.0083, n [760, 4866]) | no | not supported |
| TT13 | When the consonant repeats, the vowel changes more often than in Linear B | 0.8746 (target 0.631, comparison 0.7052, n [760, 4866]) | no | not supported |
| TT5 | o prefers R/Q and e prefers T/N/S, more than in Linear B | 0.0005 (target 0.1616, comparison -0.035, n [760, 4866]) | yes | **supported** |
| TT19 | Pre-Greek e/o choice depends on the consonant more than Greek's | 0.3653 (nmi_pre 0.032, nmi_greek 0.029) | no | not supported |
| TT16 | Eteocretan begins with a-syllables more often than Greek | 0.0155 (target 0.5143, comparison 0.2941, n [35, 119]) | yes | supported (35 short Eteocretan pieces) |
| TT17 | Pre-Greek stems end on more restricted consonants | 0.1169 (target 0.1357, comparison 0.1833, n [1143, 1143]) | no | not supported |
| TT18 | Pre-Greek words begin with a pure vowel less often | 0.0005 (target 0.2616, comparison 0.336, n [1143, 1143]) | yes | **supported** |
| TT6 | Different scribes order commodity pairs the same way | 0.003 (agreement 0.717, null 0.501, scribe_pairs 120) | yes | **supported** |
| TT21 | HT and the other sites order commodity pairs the same way | 0.2434 (agreement 0.667, null 0.489, pairs 9) | no | not supported (9 pairs) |
| TT14 | Oil comes before wine more often than not | 0.0898 (oil_first 7/9, sign_test_p 0.0898) | no | suggestive (7/9) |
| TT7 | The last entry is the unique smallest more often than chance | 0.2954 (last_is_min 22/137, null 19.4) | no | not supported |
| TT22 | Lists of men are ordered largest-first beyond chance | 0.0005 (mean_tau 0.289, null 0.002, lists 19) | yes | **supported** |
| TT15 | Scribes who total more also order more strictly largest-first | 0.026 (spearman 0.507, scribes 15) | no | nominal (p 0.026) |
| TT20 | Totalled lists record larger summed amounts | 0.002 (with_total_mean_log_sum [4.0686, 32], without [3.1733, 222]) | yes | **supported** |
| TT8 | Vowel-initial religious words are vowel + attested word more often than administrative ones | 0.9315 (target 0.1176, comparison 0.2, n [51, 80]) | no | not supported |

**What the round adds.**

- **Consonant harmony, not only reduplication (TT1–TT3).** Neighbouring syllables share a consonant with *different* signs (TA-TI, KU-KA) 3.4% of the time in Linear A, against 2.1% in Linear B. The pattern is not only repeated syllables such as SA-SA. It holds in list names (4.5% against 3.0% for all repetition) and at Haghia Triada and elsewhere separately (5.4% and 5.1% against 3.0%). Minoan words favoured the same consonant in neighbouring syllables.
- **The Pre-Greek parallel is weaker (TT4, TT11).** Without identical syllables, Pre-Greek's excess is not significant (3.2% against 2.4%, p 0.087). The consonants that repeat in Pre-Greek do not match Linear A's either. The round-47 parallel rests on reduplication, one of Beekes's own criteria, so it should not be counted as independent support.
- **Each vowel has its own consonants (TT5).** Within e/o syllables, o is commoner after R and Q and e after T, N and S (a difference of 0.16, against −0.04 in Linear B).
- **The commodity order is institutional (TT6).** Different scribes order the same pair of commodities the same way 72% of the time, against 50% by chance.
- **Largest-first extends to men (TT22),** and **totalled lists are the big ones (TT20).** Lists of men are ordered largest-first too (tau 0.29), and lists with a KU-RO total record larger sums (geometric mean about 58 against 24).
- **Pre-Greek and Eteocretan beginnings (TT18, TT16).**
  - Pre-Greek words begin with a pure vowel less often than Greek words (26% against 34%), as Linear A does against Linear B.
  - Eteocretan pieces begin with an a-syllable more often than Greek (51% against 29%), on a tiny corpus.
- **Not supported:**
  - repetition concentrated at the word start (TT12), or with a vowel change (TT13);
  - Pre-Greek e/o dependence (TT19) or final restriction (TT17);
  - site agreement on the commodity order (TT21, 9 pairs);
  - oil before wine is suggestive only (TT14, 7 of 9);
  - last entry smallest (TT7) and religious vowel prefixes (TT8).

# Fiftieth round: what single signs and NI mean, 24 September 2026

`reading/round50.py`, results in `reading/round50_results.json` and `reading/round50_output.txt`.

Eight high-value tests of what the single signs, and NI in particular, stand for. Benjamini–Hochberg at 5% across the eight.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| HV1 | NI and FIC avoid the same tablet | 1 (together 0, null 0.0, NI_tablets 55, FIC_tablets 0) | no | untestable as stated: Linear A has no FIC logogram at all |
| HV2 | Single signs and the terms they would abbreviate avoid the same tablet | 0.7286 (together 4, null 3.65, single_tokens 60) | no | not supported |
| HV3 | Single KU stands in the last entry more often than other single signs | 0.5927 (KU_last [0.1333, 15], other_last [0.1281, 359]) | no | not supported |
| HV4 | Single signs on oil tablets are oil-ligature syllables more often | 0.8786 (on_oil_tablets [0.2241, 58], elsewhere [0.283, 371]) | no | not supported |
| HV5 | NI entries carry fractions more often than VIR entries | 0.0005 (NI [0.4464, 56], VIR [0.0556, 36]) | yes | **supported** |
| HV6 | NI has a consistent place among the commodities | 0.0005 (asymmetry 53, null 17.9, tablets 43) | yes | **supported** |
| HV7 | NI stands on grain tablets more often than chance | 0.0005 (together 19, null 9.09, NI_tablets 55, GRA_tablets 61) | yes | **supported** |
| HV8 | NI amounts are listed largest-first beyond chance | 1 (mean_tau -1.0, null -0.006, lists 1) | no | untestable (one list) |

**What the round adds.**

- **NI is a commodity, and the commodity is figs (HV1, HV5–HV7).**
  - Linear A has no separate fig logogram: the FIC sign never occurs on the administrative tablets (HV1 had nothing to test). Linear B's fig logogram is the same sign as the syllable NI (*30).
  - On the Linear A tablets, NI behaves as a measured commodity. NI entries carry fractions 45% of the time, against 6% for entries of men (HV5).
  - NI has a fixed place in the order of goods: after grain (16 against 4), cyperus (19 against 0) and oil (11 against 5), and before wine (16 against 3) (HV6).
  - NI stands on grain tablets more than chance (19 against 9, HV7).

  Linear A wrote figs with NI, and fitted them into the canonical order between oil and wine, as a ration food alongside grain.
- **Single signs are not simple abbreviations of the terms (HV2–HV4).**
  - Single KI never shares a tablet with KI-RO (0 of 13), and single A never with A-DU (0 of 15). But pooled over six pairs, avoidance is not beyond chance (4 against 3.7).
  - Single KU does not stand where totals stand (HV3).
  - Single signs on oil tablets are not the oil-ligature syllables (HV4).

# Fifty-first round: single signs as commodity abbreviations, 24 September 2026

`reading/round51.py`, results in `reading/round51_results.json` and `reading/round51_output.txt`.

Eight tests of whether the syllables Linear B uses as commodity abbreviations already worked that way in Linear A. The set was fixed from Linear B before testing: SA (sesame), KU (cumin), KO (coriander), MA (fennel), MI (mint), SE (celery), KA (safflower) and PO. NI is left out, having been tested in round 50. Benjamini–Hochberg at 5% across the eight.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| CM1 | Spice-abbreviation signs are followed by numbers more often | 0.2039 (set [0.5763, 59], other [0.5067, 300]) | no | not supported |
| CM2 | Spice-abbreviation sign entries carry fractions more often | 0.6697 (set [0.0847, 59], other [0.0933, 300]) | no | not supported |
| CM3 | Spice-abbreviation signs stand on goods tablets more often | 0.2299 (set [0.4068, 59], other [0.3433, 300]) | no | not supported |
| CM4 | Number-following and fraction rates correlate across single signs | 0.8212 (spearman -0.19, signs 27) | no | not supported |
| CM5 | Single TE stands in the first entry more often | 0.0005 (TE_first [0.6296, 27], other_first [0.1295, 332]) | yes | **supported** |
| CM6 | Number-following single signs hold consistent places among commodities | 0.4793 (asymmetry 96, null 94.8, tablets 55) | no | not supported |
| CM7 | Spice-abbreviation signs co-occur on the same tablets | 0.8406 (tablets_with_2plus 5, null 6.5) | no | not supported |
| CM8 | Number-following single signs stand in the first entry less often | 0.0005 (num_first [0.0699, 186], other_first [0.2717, 173]) | yes | **supported** |

**What the round adds.**

- **The Linear B spice abbreviations are not a Linear A system (CM1–CM3, CM7).** The syllables that Linear B uses for sesame, cumin, coriander, fennel, mint, celery and safflower behave like any other single sign in Linear A:
  - they are not followed by numbers more often (58% against 51%);
  - they carry no more fractions, and are no commoner on goods tablets;
  - they do not cluster on the same tablets.

  NI (figs) is the only syllable that Linear A demonstrably uses as a commodity, so the abbreviation system for spices looks like a Mycenaean development.
- **Two kinds of single sign (CM5, CM8).**
  - Single signs followed by a number are list items: they stand in the first entry of a tablet only 7% of the time, against 27% for other single signs.
  - TE is the clearest of the other kind. It stands in the first entry 63% of the time, against 13%, so it works as a heading or opening sign.
- **No coherent commodity use across single signs (CM4, CM6).** Being followed by numbers does not go with taking fractions, and number-following single signs have no fixed place among the commodities.

# Fifty-second round: TE, first words, transaction terms, harmony, 24 September 2026

`reading/round52.py`, results in `reading/round52_results.json` and `reading/round52_output.txt`.

Ten hypotheses on the heading sign TE, first words and transaction terms, and non-adjacent consonant harmony. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| OP1 | TE-opened tablets record a single commodity more often | 0.4243 (TE [1.0, 2], other [0.6566, 166]) | no | untestable in practice (TE is the first token on only 6 tablets) |
| OP2 | TE-opened tablets carry a total more often | 1 (TE [0.0, 6], other [0.0862, 348]) | no | untestable in practice |
| OP3 | Opening with TE is tied to particular scribes | 0.5747 (chi2 12.87, null 17.44, tablets 110) | no | not supported |
| OP4 | TE opens tablets at HT and elsewhere | 0.7496 (HT {'TE_first': [0.8, 20], 'other_first': [0.0884, 181], 'p': 0.0005}, other {'TE_first': [0.1429, 7], 'other_first': [0.1788, 151], 'p': 0.7496}, p (larger) 0.) | no | Haghia Triada only: 80% vs 9% there, 14% vs 18% elsewhere |
| OP6 | The first word is associated with the main commodity | 0.004 (chi2 33.4, null 16.8, tablets 22) | yes | **supported** (22 tablets) |
| OP10 | TE is followed by a word or logogram more often than other single signs | 0.0005 (TE [0.4815, 27], other [0.1493, 402]) | yes | **supported** |
| OP14 | Transaction terms are associated with particular commodities | 0.3623 (chi2 21.7, null 20.3, pairs 72) | no | not supported (SA-RA2 occurs with every commodity) |
| OP17 | Transaction terms are associated with particular sites | 0.026 (chi2 31.4, null 16.5, pairs 44) | no | nominal (p 0.026) |
| OP19 | Syllables one apart share a consonant more often than in Linear B | 0.011 (LA 0.0653, LB 0.0492) | yes | **supported** |
| OP22 | The word after TE recurs across TE-opened tablets | 1 (repeats 0, null 0.01, TE_tablets 3) | no | untestable (3 tablets) |

**What the round adds.**

- **Harmony reaches past the next syllable (OP19).** The first and third of three syllables share a consonant 6.5% of the time in Linear A, against 4.9% in Linear B (p 0.011). Consonant harmony in Minoan words was not limited to neighbouring syllables.
- **TE introduces a word, and belongs to Haghia Triada (OP10, OP4).** TE is followed by a word or a commodity logogram 48% of the time, against 15% for other single signs, so it works as a marker placed before a heading. Its opening role is a Haghia Triada habit: there it stands in the first entry 80% of the time, elsewhere no more than other single signs. It is rarely the literal first token (6 tablets), so the tests of TE-opened tablets (OP1–OP3, OP22) had almost no data.
- **Headings go with commodities (OP6).** Among tablets whose first word recurs (A-DU, SA-RA2, SA-RO, KA-PA, JE-DI), the first word is tied to the tablet's main commodity (χ² 33 against 17). This rests on 22 tablets only.
- **Transaction terms are not commodity-specific (OP14).** SA-RA2 occurs with grain, oil, men, wine and cyperus alike. They lean towards particular sites (OP17, p 0.026), which mostly reflects Haghia Triada.

# Fifty-third round: consonant harmony in depth, 24 September 2026

`reading/round53.py`, results in `reading/round53_results.json` and `reading/round53_output.txt`.

Ten hypotheses on consonant harmony (neighbouring syllables with the same consonant and different signs). Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| HC1 | Non-adjacent harmony on SigLA vs Linear B | 0.0035 (target 0.0728, comparison 0.0492, n [536, 4866]) | yes | **replicated** |
| HC2 | Adjacent harmony (different signs) on SigLA vs Linear B | 0.0005 (target 0.0378, comparison 0.021, n [536, 4866]) | yes | **replicated** |
| HC3 | Harmony holds for obstruents and sonorants separately | 0.0225 (obstruents {'LA': 0.0405, 'LB': 0.0282, 'p': 0.0225}, sonorants {'LA': 0.0421, 'LB': 0.0222, 'p': 0.0015}, p (larger) 0.0225) | yes | **supported** |
| HC4 | Knossos names show harmony more than Pylos names | 0.1234 (target 0.0182, comparison 0.012, n [637, 339]) | no | not supported |
| HC5 | Eteocretan shows harmony more than Greek | 0.0145 (target 0.0625, comparison 0.011, n [35, 119]) | yes | supported (35 short pieces) |
| HC6 | Same consonant preferred over same place more than in Linear B | 0.0795 (target 0.2034, comparison 0.1618, n [760, 4866]) | no | suggestive (p 0.08) |
| HC7 | Harmony holds in 3-sign and 4+-sign words separately | 0.0715 (3 signs {'LA': 0.0338, 'LB': 0.0224, 'p': 0.0715}, 4+ signs {'LA': 0.0336, 'LB': 0.0185, 'p': 0.0065}, p (larger) 0.0715) | no | 4+ signs p 0.0065; 3 signs p 0.07 |
| HC8 | Harmony holds in words attested once | 0.0015 (target 0.0352, comparison 0.021, n [631, 4866]) | yes | **supported** |
| HC9 | Two-sign words share their consonant more often than in Linear B | 0.5292 (target 0.0538, comparison 0.0532, n [279, 827]) | no | not supported |
| HC10 | Words with harmony are attested at more sites | 1 (diff_mean_sites -0.098, harmonic_words 52) | no | reversed |

**What the round adds.**

- **Harmony replicates on SigLA, adjacent and one apart (HC1, HC2).** Different-sign harmony is 3.8% on SigLA against 2.1% in Linear B, and non-adjacent harmony 7.3% against 4.9%.
- **It covers the whole consonant system (HC3):** obstruents (4.1% against 2.8%) and sonorants (4.2% against 2.2%) alike.
- **It is productive (HC8).** It holds in the 631 words attested only once (3.5% against 2.1%), so it is not carried by a few frequent words.
- **It belongs to longer words (HC7, HC9).** It is clear in words of four or more signs (3.4% against 1.9%) and weaker in three-sign words (p 0.07). Two-sign words show nothing (5.4% against 5.3%). The pattern is a property of longer stems, not of short syllable pairs.
- **Eteocretan shows it (HC5)** with different signs (6.3% against 1.1% for Greek), on 35 short pieces. With round 49's qualification of the Pre-Greek result, Eteocretan is the only outside record with harmony that is not simple reduplication.
- **Not in Knossos names (HC4),** not spread across more sites (HC10, reversed). The preference for identical over merely similar consonants is only suggestive (HC6, p 0.08).

# Fifty-fourth round: Minoan bookkeeping habits in Linear B, 24 September 2026

`reading/round54.py`, results in `reading/round54_results.json` and `reading/round54_output.txt`.

Ten hypotheses asking whether the Mycenaean scribes kept the Linear A bookkeeping habits. Linear B entries are parsed from linearb.xyz (logogram followed by a whole number). Benjamini–Hochberg at 5% across the ten. After the run, two problems were found and addressed. First, the fig logogram is written NI in the transcription, so LBC6 and LBC7 were rerun reading NI as figs. Second, a within-commodity check was added for LBC3.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| LBC1 | Knossos lists are largest-first | 0.0005 (mean_tau 0.365, null 0.0, lists 251) | yes | **supported** |
| LBC2 | Pylos lists are largest-first | 0.023 (mean_tau 0.097, null -0.001, lists 86) | yes | supported |
| LBC3 | Knossos lists are more strictly largest-first than Pylos lists | 0.0005 (KN 0.365, PY 0.097) | yes | **not robust**: within commodity p 0.21; the Knossos figure is carried by sheep lists (tau 0.59, 121 lists) |
| LBC4 | The first entry is the unique largest | 0.0005 (first_is_max 155/337, null 76.6) | yes | **supported** |
| LBC5 | Equal amounts (not 1) stand next to each other beyond chance | 0.085 (adjacent_equal 71, null 63.3) | no | suggestive (p 0.085) |
| LBC6 | Figs come after grain | 1 (grain_first 0/0, sign_test_p 1.0) | no | **supported on rerun** (NI read as figs): figs after grain on 37 of 37 tablets |
| LBC7 | Figs come before wine | 1 (figs_first 0/0, sign_test_p 1.0) | no | untestable on rerun (3 tablets) |
| LBC8 | Commodities appear in a consistent order | 0.0005 (asymmetry 239, null 107.5, tablets 210) | yes | **supported** |
| LBC9 | Knossos amounts of 2+ are even more often than odd | 0 (even 1472/2037) | yes | **supported** |
| LBC10 | Lists with a total word are more strictly largest-first | 1 (with_total [-0.0678, 32], without [0.3345, 305]) | no | reversed: Linear B totalled lists are not ordered |

**What the round adds.**

- **Linear B keeps figs after grain (LBC6).** Reading the fig logogram NI, figs come after grain on all 37 Linear B tablets that record both (p < 10⁻¹¹). In Linear A, NI follows grain on 16 of 20. The place of figs after grain passed from the Minoan to the Mycenaean accounts, together with the sign used for them.
- **Linear B lists are largest-first and keep a commodity order (LBC1, LBC2, LBC4, LBC8).** Knossos lists are strongly largest-first (tau 0.37, 251 lists), Pylos lists weakly (0.10). In 155 of 337 lists the first entry is the unique largest (77 by chance). Commodities appear in a consistent order (asymmetry 239 against 108).
- **But the Knossos–Pylos contrast is content, not tradition (LBC3).** Within the same commodity the difference is not significant (p 0.21). Knossos's strong ordering comes mostly from its sheep records (tau 0.59 over 121 lists), a series Pylos barely has.
- **Even amounts dominate at Knossos (LBC9)** (72% of amounts of 2 or more). Linear A also prefers even amounts (round 9); here the sheep and grain series probably contribute.
- **Linear B totals do not mark ordered lists (LBC10, reversed),** unlike Linear A's KU-RO lists. Grouping of equal amounts is only suggestive (LBC5).

# Fifty-fifth round: Linear A bookkeeping habits kept in Linear B, 24 September 2026

`reading/round55.py`, results in `reading/round55_results.json` and `reading/round55_output.txt`.

Ten tests repeating Linear A bookkeeping findings on the Linear B tablets of Knossos and Pylos (NI read as the fig logogram). Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| C1 | Cyperus before figs | 1 (cyperus_first 0/0) | no | untestable (no Linear B tablet records both) |
| C2 | Oil before figs | 1 (oil_first 0/0) | no | untestable |
| C3 | Figs stand on grain tablets beyond chance | 0.0005 (together 36, null 4.1) | yes | **kept** |
| C4 | Fig entries carry sub-units more often than entries of men | 0.0005 (FIC [0.4419, 43], VIR [0.0, 562]) | yes | **kept** |
| C5 | Grain amounts exceed oil amounts on tablets with both | 1 (grain_larger 0/0) | no | untestable |
| C6 | The first commodity carries the largest amount | 0.0005 (first_has_max 152/222, null 100.9) | yes | **kept** |
| C7 | Wine is the last commodity | 0.7001 (VIN_last 2/9, null 2.2) | no | **not kept**: wine last on 2 of 9 |
| C8 | Oil and olives stand on the same tablets beyond chance | 1 (together 0, null 1.0) | no | untestable (oil and olives in separate series) |
| C9 | Grain is the first commodity | 0.0005 (GRA_first 46/63, null 25.6) | yes | **kept** |
| C10 | Lists of goods (not men, not sheep) are largest-first | 0.019 (mean_tau 0.122, null -0.001, lists 77) | yes | kept |

**What the round adds.**

- **Five Linear A habits reappear in Linear B.**

  | Habit | Linear A | Linear B |
  |---|---|---|
  | Figs stand with grain | 19 tablets (9 by chance) | 36 (4 by chance) |
  | Figs measured with fractions or sub-units | 45% of NI entries (men 6%) | 44% of fig entries (men 0%) |
  | The first commodity carries the largest amount | 30 of 53 | 152 of 222 (101 by chance) |
  | Grain comes first | grain before the others | 46 of 63 (26 by chance) |
  | Lists of goods run largest-first | yes (round 33) | tau 0.12, p 0.019 (men and sheep excluded) |

  The Mycenaean scribes took over the script and the logograms, and also a way of organising commodity lists: grain first and largest, figs alongside grain as a measured ration, and big items before small.
- **Wine last was not kept (C7).** Wine ends only 2 of 9 Linear B tablets that record it.
- **Untestable (C1, C2, C5, C8).** Linear B keeps cyperus, oil and olives in separate records from figs and grain, so their relative order cannot be compared.

# Fifty-sixth round: more bookkeeping comparisons between Linear A and Linear B, 24 September 2026

`reading/round56.py`, results in `reading/round56_results.json` and `reading/round56_output.txt`.

Nine further comparisons of Linear A and Linear B bookkeeping. Benjamini–Hochberg at 5% across the nine.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| D1 | Pylos goods amounts are even more often than odd | 0 (even 133/196) | yes | **supported** |
| D2 | Linear A: grain amounts exceed wine amounts | 0.0156 (grain_larger 6/6) | no | nominal (6/6, p 0.016) |
| D3 | Linear B: grain amounts exceed wine amounts | 0.5 (grain_larger 2/3) | no | not supported |
| D4 | Linear B: grain before olives | 0.1051 (grain_first 11/16) | no | suggestive (11/16) |
| D5 | Linear B: grain before men | 0.9688 (grain_first 1/5) | no | not supported |
| D6 | Pylos: the first entry is the unique largest beyond chance | 0.2029 (first_is_max 22/107, null 18.4) | no | not supported: first-entry-largest is a Knossos pattern |
| D7 | Linear A: cyperus and oil on the same tablets beyond chance | 0.988 (together 7, null 11.57) | no | reversed: cyperus and oil tend to be on different tablets |
| D8 | Linear B: cyperus and oil on the same tablets beyond chance | 1 (together 0, null 0.25) | no | not supported |
| D9 | Linear B lists of men are largest-first | 0.7006 (mean_tau -0.033, null 0.002, lists 52) | no | not supported: Linear B lists of men are not ordered |

**What the round adds.**

- **Even amounts are a shared Aegean habit (D1).** At Pylos, 68% of goods amounts of 2 or more are even (133 of 196). Linear A has 65% (round 9) and Knossos 72%. The preference for even amounts is not confined to the Knossos sheep records.
- **Two habits are Knossian or Minoan, not Mycenaean in general (D6, D9).**
  - At Pylos the first entry is not the largest (22 of 107, against 18 by chance), so the Linear B first-largest result of round 55 comes from Knossos.
  - Linear B lists of men are not ordered largest-first (tau −0.03), unlike Linear A's (round 49, tau 0.29).
- **Grain over wine and olives (D2, D4):** grain exceeds wine on all 6 Linear A tablets with both (nominal), and Linear B puts grain before olives on 11 of 16 tablets (suggestive).
- **Not supported:** cyperus with oil in either script (D7, D8); grain before men in Linear B (D5).

# Fifty-seventh round: the syntax of an entry, 24 September 2026

`reading/round57.py`, results in `reading/round57_results.json` and `reading/round57_output.txt`.

Nine hypotheses on the order of word, commodity sign and number within an entry. Benjamini–Hochberg at 5% across the nine.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| SY1 | The word precedes the commodity sign more often than not | 0 (word_first 149/150) | yes | **supported** |
| SY2 | Entry order differs by site | 0.1734 (chi2 11.1, null 4.1) | no | not supported |
| SY3 | Entry order differs by scribe | 0.097 (chi2 9.3, null 6.1, entries 61) | no | suggestive (p 0.10) |
| SY4 | Commodity-first entries are first entries more often | 1 (commodity_first_in_first_entry [0.0, 1], word_first_in_first_entry [0.3624, 149]) | no | not supported |
| SY5 | A number follows a commodity sign more often than a word | 0.0005 (after_commodity [0.6916, 454], after_word [0.5346, 911]) | yes | **supported** |
| SY6 | Linear A puts the word first less often than Linear B | 1 (LA 149/150, LB 1340/1775) | no | not interpretable: the Linear B comparison uses a rough line parser |
| SY8 | Heading words are followed by a commodity sign more often than entry labels | 1 (heading [0.0301, 166], entry_label [0.2159, 593]) | no | reversed: headings are almost never followed directly by a commodity sign (3%) |
| SY9 | Transaction terms are followed by a commodity sign more often than other words | 0.0005 (terms [0.5217, 46], other_words [0.1353, 865]) | yes | **supported** |
| SY10 | Entry labels are followed by a number more often than headings | 0.0005 (entry_label [0.7201, 593], heading [0.0663, 166]) | yes | **definitional**: "entry label" is defined by a following quantity, so not evidence |

**What the round adds.**

- **An entry is word, then commodity sign, then number (SY1, SY5).** When an entry has both a word and a commodity sign, the word comes first in 149 of 150 cases. A number follows a commodity sign directly more often than it follows a word (69% against 53%). This is the Linear B entry order (name, logogram, quantity), already fixed in Linear A. The one exception is at Zakros. The comparison with Linear B (SY6) used a rough line parser and is not interpretable.
- **Transaction terms qualify commodities (SY9).** SA-RA2, KU-PA, A-DU, KA-PA and DA-RE are followed directly by a commodity sign 52% of the time, against 14% for other words. The terms stand in the slot before the logogram, where Linear B puts descriptive words for a commodity. They describe the transaction or the goods, not a person.
- **Headings stand apart from the commodity (SY8, reversed).** Heading words are followed directly by a commodity sign only 3% of the time. Headings open a tablet and are followed by entries, not by the goods themselves.
- **SY10 is definitional.** The reading defines an entry label as a word followed by a quantity.

# Fifty-eighth round: words in the descriptor slot before a commodity sign, 24 September 2026

`reading/round58.py`, results in `reading/round58_results.json` and `reading/round58_output.txt`.

Eight hypotheses on the words standing directly before a commodity sign, the slot where Linear B puts descriptions of the goods or the people. Benjamini–Hochberg at 5% across the eight.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| DS1 | Words before a commodity sign are associated with that commodity | 0.1254 (chi2 32.9, null 24.9, pairs 29) | no | suggestive: SA-RA2 before GRA 8 and CYP 5, OLE only 1 |
| DS2 | Transaction terms before a commodity sign are associated with that commodity | 0.2004 (chi2 16.4, null 12.8, pairs 24) | no | not significant (24 pairs) |
| DS3 | Pre-commodity words end in -JA more often | 0.5152 (pre_commodity [0.0455, 110], other [0.0422, 545]) | no | not supported |
| DS4 | Pre-commodity words recur more than pre-number words | 0.001 (type_token_pre_commodity 0.78, pre_number_same_size 0.867) | yes | **supported** |
| DS5 | Pre-commodity words are attested at more sites | 0.0015 (pre_commodity_mean_sites [1.1909, 110], pre_number [1.0544, 349]) | yes | **supported** |
| DS6 | Oil ligature syllable matches the first sign of the preceding word | 1 (matches 0/19, null 1.07) | no | **refuted** (0/19) |
| DS7 | Words before VIR differ in syllable profile from words before goods | 0.0515 (jsd 0.3852, null 0.3076, n [14, 79]) | no | suggestive (p 0.052) |
| DS8 | -JA words stand before VIR more often than before goods | 1 (JA_before_VIR [0.0, 5], other_before_VIR [0.1103, 136]) | no | not supported |

**What the round adds.**

- **The pre-commodity slot holds technical vocabulary, not names (DS4, DS5).** Words directly before a commodity sign recur more than words directly before a number (type/token 0.78 against 0.87 at the same sample size), and occur at more sites (1.19 against 1.05 per word). This is the behaviour of terms, where the words before numbers behave like personal names.
- **SA-RA2 goes with dry goods (DS1, suggestive).** Directly before a commodity sign, SA-RA2 precedes grain 8 times and cyperus 5 times, and oil only once. The association is not significant on 29 pairs.
- **No acrophony in the oil ligatures (DS6).** None of 19 oil ligatures repeats the first syllable of the word before it, which closes the acrophony question from a third direction (rounds 13 and 50 being the other two).
- **No -JA descriptors (DS3, DS8).** Pre-commodity words do not end in -JA more often, and -JA words do not precede VIR.

# Fifty-ninth (saturation loop) round: the name slot and the descriptor slot, 24 September 2026

`reading/round59.py`, results in `reading/round59_results.json` and `reading/round59_output.txt`.

First round of the saturation loop (rule in `reading/loop_ledger.json`: stop after three consecutive rounds with no new learning). Ten hypotheses on the name slot (a word directly before a number) and the descriptor slot (a word directly before a commodity sign). Benjamini–Hochberg at 5% across the ten. Checks restricting N3 and N10 to tablets of goods (no VIR) were added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| N1 | The two slots are lexically separate | 0.0005 (shared_types 16, null 32.7) | yes | **new** |
| N2 | The slots differ in syllable profile | 0.2554 (jsd 0.0658, null 0.0591, n [93, 271]) | no | not supported |
| N3 | Descriptor-slot entries have larger amounts | 0.0005 (desc_mean_log [2.5671, 102], name_mean_log [1.5511, 464]) | yes | **new**; holds on goods tablets (p 0.0005) |
| N4 | Descriptor words contain unread signs less often | 0.089 (desc [0.1348, 141], name [0.1889, 487]) | no | suggestive |
| N5 | Heading words recur more than name-slot words | 0.981 (heading_ttr 0.877, name_ttr_same_size 0.839, n 203) | no | reversed |
| N6 | Heading types overlap descriptor types more than name types | 0.002 (diff 0.101, null -0.0) | yes | **new** |
| N7 | Descriptor words are shorter | 0.3623 (desc_len 2.83, name_len 2.87) | no | not supported |
| N8 | Descriptor words keep a single commodity | 0.0525 (single_commodity_share 0.417, null 0.205, words 12) | no | suggestive (p 0.053, 12 words) |
| N9 | Use of the descriptor slot differs by site | 0.0005 (chi2 37.9, null 5.1) | yes | **new** |
| N10 | Descriptor entries carry fractions more often | 0.0035 (desc [0.1844, 141], name [0.0903, 487]) | yes | **new**; holds on goods tablets (20% vs 10%, p 0.0065) |

**What the round adds.**

- **The name slot and the descriptor slot use different words (N1).** Only 16 word types occur in both, against 33 when slot labels are shuffled. Linear A lists had two distinct lexical classes: words that stand before a quantity (names) and words that stand before a commodity sign (terms).
- **Headings are terms (N6).** Heading words share types with the descriptor slot much more than with the name slot (difference 0.10).
- **Descriptor entries are bigger and more finely measured (N3, N10).** On tablets of goods, entries whose word stands before the commodity sign are larger (geometric mean about 13 against 4) and carry fractions twice as often (20% against 10%). They record quantities of goods under a term, while the name slot records smaller allocations to persons.
- **Sites use the slots differently (N9).** At Khania, 58% of such entries use the descriptor slot, against 20% at Haghia Triada, 17% at Zakros and none at Palaikastro. Khania's lists are organised by goods and terms, Haghia Triada's by persons.
- **Not supported:**
  - a different syllable profile (N2), or shorter descriptor words (N7);
  - headings do not recur more than names (N5, reversed);
  - descriptors keeping one commodity (N8, p 0.053) and fewer unread signs in descriptors (N4) are suggestive only.

# Sixtieth (saturation loop 2) round: consequences of the two word classes, 24 September 2026

`reading/round60.py`, results in `reading/round60_results.json` and `reading/round60_output.txt`.

Ten hypotheses following the name slot / descriptor slot distinction of round 59. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| P1 | Khania tablets carry fewer name-slot words than Haghia Triada tablets | 0.0005 (Khania [1.1429, 14], HT [4.2179, 78]) | yes | supported (refinement of N9, not counted as new) |
| P2 | Descriptor entries stand earlier in the list | 0.0345 (desc_mean_position [0.3969, 27], name_mean_position [0.5663, 42]) | no | nominal (p 0.035) |
| P3 | Tablets headed by a term contain descriptor entries more often | 0.0015 (term_headed [0.52, 25], other [0.1727, 110]) | yes | **new** |
| P4 | Descriptor words repeat within a tablet more than name words | 0.973 (desc 0.0, name 0.012) | no | not supported |
| P6 | Name words show harmony more than descriptor words | 0.0705 (name 0.066, desc 0.022) | no | suggestive (p 0.07) |
| P8 | Q-initial words are name-slot words more often | 0.8091 (name 0.048, desc 0.065) | no | not supported |
| P9 | Vowel-initial words are descriptor-slot words more often | 0.1 (desc 0.247, name 0.177) | no | not supported |
| P10 | Descriptor words are written by more scribes | 0.0035 (desc [2.5909, 22], name [1.4634, 41]) | yes | **new** |
| P11 | Descriptor words occur in religious texts more often | 0.0585 (desc [0.0364, 110], name [0.0086, 349]) | no | suggestive |
| P12 | Descriptor words (2+ tablets) are attested at more sites | 0.0515 (desc [1.4545, 22], name [1.1707, 41]) | no | suggestive (p 0.052) |

**What the round adds.**

- **The heading announces the kind of list (P3).** Tablets whose heading is a term (a word also used in the descriptor slot) contain descriptor entries 52% of the time, against 17% for other tablets.
- **Terms are shared, names are not (P10).** Descriptor words on two or more tablets are written by 2.6 scribes on average, name words by 1.5. The persons belonged to particular scribes (round 18); the vocabulary of goods and transactions was common to the whole archive.
- **Khania keeps goods, not persons (P1, refinement).** Khania tablets carry 1.1 name-slot words on average, against 4.2 at Haghia Triada. This follows from round 59's N9.
- **Suggestive only:**
  - descriptor entries come earlier in lists (P2, p 0.035), as larger items would under largest-first;
  - name words show more harmony (P6, p 0.07);
  - terms occur more in religious texts (P11) and at more sites (P12).

# Sixty-first (saturation loop 3) round: list types and the sealing system, 24 September 2026

`reading/round61.py`, results in `reading/round61_results.json` and `reading/round61_output.txt`.

Ten hypotheses on list types and the sealing system. Benjamini–Hochberg at 5% across the ten.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| Q1 | Term-headed tablets record larger amounts | 0.3733 (term_headed [1.9653, 22], other [1.8682, 72]) | no | not supported |
| Q2 | Term-headed tablets carry fractions more often | 0.4198 (term_headed [0.4, 25], other [0.3545, 110]) | no | not supported |
| Q4 | Sealing signs differ by site | 0.0005 (chi2 345.3, null 13.3, sites {'Haghia Triada': 596, 'Khania': 19}) | yes | **new** (19 Khania sealing signs) |
| Q5 | Sealing signs are oil-ligature syllables more often than tablet single signs | 1 (seal [0.0254, 631], tablet [0.2751, 429]) | no | reversed |
| Q7 | Khania descriptor words occur at HT more often than Khania names | 0.6932 (desc_at_HT [0.1818, 22], name_at_HT [0.1875, 16]) | no | not supported |
| Q8 | Tablets with a total carry name entries more often | 0.0435 (with_total_name_share [0.8184, 27], without [0.6755, 85]) | no | nominal (p 0.044) |
| Q10 | Descriptor entries have an amount of 1 less often | 0.0005 (desc [0.0882, 102], name [0.3254, 464]) | yes | supported (refinement of N3) |
| Q11 | At HT, sealing signs are the common word-initial signs more often than tablet single signs | 0.0005 (seal [0.7299, 596], tablet [0.4298, 242]) | yes | supported (replication of the round-9 sealing result) |
| Q12 | At HT, roundels and nodules use different signs | 0.3963 (chi2 14.0, null 14.5) | no | not supported |
| Q13 | Tablets with descriptor entries are single-commodity more often | 1 (with_desc [0.4615, 78], without [0.8333, 90]) | no | **reversed**: tablets with descriptor entries are multi-commodity (46% single vs 83%) |

**What the round adds.**

- **Sealing repertoires are regional (Q4).** Single signs on sealings differ between Haghia Triada (596) and Khania (19) far beyond chance (χ² 345 against 13). The Khania sample is small.
- **The descriptor slot marks goods on mixed tablets (Q13, reversed).** Tablets with descriptor entries record a single commodity only 46% of the time, against 83% for tablets without. A word before the commodity sign is used where several goods share a tablet, to say which entry is which.
- **Confirmations:**
  - descriptor entries are rarely single units (Q10: 9% against 33%);
  - Haghia Triada sealing signs are the common word-initial syllables (Q11: 73% against 43%), as round 9 found.
- **Not supported:**
  - term-headed tablets record no larger amounts and no more fractions (Q1, Q2);
  - sealing signs are not oil-ligature syllables (Q5);
  - roundels and nodules at Haghia Triada use the same signs (Q12).

# Sixty-second (saturation loop 4) round: the descriptor slot on mixed tablets, 24 September 2026

`reading/round62.py`, results in `reading/round62_results.json` and `reading/round62_output.txt`.

Seven hypotheses testing whether the descriptor slot marks which goods an entry concerns (following the reversal Q13 of round 61). Benjamini–Hochberg at 5% across the seven. A size check for R9 was added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| R1 | A switch of commodity carries a descriptor word more often | 0.6482 (switch [0.1838, 136], continue [0.1972, 71]) | no | not supported |
| R2 | More commodities, more descriptor entries | 0.0008 (spearman 0.345, tablets 125) | yes | **new** (pre-stated confirmation of Q13) |
| R4 | Single-commodity tablets repeat the commodity sign less | 0.0005 (single [0.3386, 79], multi [0.5381, 61]) | yes | **new** |
| R5 | KU-RO before a commodity sign on multi-commodity tablets | 0.5787 (multi [0.1429, 7], single [0.1, 30]) | no | not supported (7 totals) |
| R9 | Amounts after descriptor words are multiples of 10 more often | 0.004 (desc [0.3039, 102], name [0.1746, 464]) | yes | size effect: among amounts of 10+, 51% vs 56% (p 0.80) |
| R11 | Headings of multi-commodity tablets are terms more often | 0.7871 (multi [0.2222, 18], single [0.2759, 29]) | no | not supported |
| R13 | Descriptor entries open a commodity block more often | 0.6047 (desc_opens [0.5694, 72], other_opens [0.5787, 197]) | no | not supported |

**What the round adds.**

- **Descriptors belong to mixed tablets (R2).** Across 125 tablets, the more commodities a tablet records, the larger the share of its word entries in the descriptor slot (rho 0.35, p 0.0008). This confirms round 61's reversal with a pre-stated test.
- **But not as switch markers (R1, R13).** A descriptor is no more likely where the commodity changes from the previous entry, or at the start of a commodity block. The descriptor slot goes with mixed tablets as a whole, not with particular transitions.
- **A single-commodity list writes its commodity once (R4).** On single-commodity tablets only 34% of entries carry the commodity sign, against 54% on mixed tablets. The sign is stated once and understood for the rest of the list, and repeated where goods alternate.
- **Rounder descriptor amounts are a size effect (R9).** Among amounts of 10 and more the difference disappears.

# Sixty-third (saturation loop 5) round: the commodity sign written once and understood, 24 September 2026

`reading/round63.py`, results in `reading/round63_results.json` and `reading/round63_output.txt`.

Seven hypotheses following round 62's finding that single-commodity lists write their commodity sign once. Benjamini–Hochberg at 5% across the seven. S2 and S3 were rerun after two parsing faults were fixed (Linear B line breaks; a missing commodity median).

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| S1 | The commodity sign stands in the first entry more often | 0.001 (first_entry [0.5455, 55], later_entries [0.3125, 256]) | yes | **new** |
| S2 | Linear B writes the logogram on more entries than Linear A | 0.0005 (LB_share 0.822, LA_share 0.383, n [181, 55]) | yes | **new** |
| S3 | Sign-less entries match the preceding commodity's scale | 0.4598 (closer_to_preceding 50/98, sign_test_p 0.4598) | no | not supported |
| S4 | Commodity blocks run largest-first | 0.1184 (mean_tau 0.12, null -0.001, blocks 33) | no | not supported |
| S5 | Sign-less entries are name entries more often | 0.0005 (signless_name [0.3134, 201], signed_name [0.0, 110]) | yes | definitional (a signed entry cannot be a name entry by construction) |
| S7 | Fraction entries carry the commodity sign more often | 0.04 (with_fraction [0.5565, 239], without [0.4852, 540]) | no | nominal (p 0.04) |
| S8 | Signed entries are larger than sign-less entries on the same tablet | 0 (signed_larger 63/85, sign_test_p 0.0) | yes | **new** |

**What the round adds.**

- **The commodity is stated at the head of the list (S1).** On single-commodity tablets the commodity sign stands in the first entry 55% of the time, against 31% for later entries.
- **Linear B gave up the economy (S2).** Linear B single-commodity lists write the logogram on 82% of their lines, Linear A on 38%. Writing the commodity once and letting it carry down the list was a Minoan practice that the Mycenaean scribes did not keep: they repeated the logogram on every line.
- **The signed entry is the big one (S8).** On tablets with both, entries that carry the commodity sign are larger than those that do not, on 63 of 85 tablets. The sign goes with the principal quantity, usually the first and largest entry.
- **Understood signs do not take their scale from the previous commodity (S3),** and commodity blocks within mixed tablets are not clearly ordered (S4).

# Sixty-fourth (saturation loop 6) round: who wrote the commodity sign once, and where, 24 September 2026

`reading/round64.py`, results in `reading/round64_results.json` and `reading/round64_output.txt`.

Seven hypotheses on the once-only commodity sign ("sign share" = share of a single-commodity list's entries that carry the sign). Benjamini–Hochberg at 5% across the seven. A within-logogram check for U4 was added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| U1 | Khania lists repeat the commodity sign more | 0.1244 (Khania [0.4191, 15], HT [0.3314, 29]) | no | not supported |
| U2 | Sign share differs by scribe | 0.3303 (between_SS 0.227, null 0.191, lists 16) | no | not supported |
| U3 | Longer lists write the sign on a smaller share of entries | 0.0108 (spearman -0.328, lists 56) | yes | **new** |
| U4 | Knossos writes the logogram on fewer lines than Pylos | 0.0005 (KN 0.718, PY 0.892, n [73, 108]) | yes | **new**; holds within logogram (p 0.007) |
| U5 | Lists of men write the sign on a smaller share | 0.001 (VIR [0.1328, 7], goods [0.4132, 49]) | yes | **new** |
| U6 | KU-RO entries carry the commodity sign more often than later entries | 0.8611 (kuro_signed [0.2, 10], later_signed [0.3068, 264]) | no | not supported |
| U7 | Lists that write the sign less often are more strictly largest-first | 0.1012 (spearman -0.225, lists 32) | no | suggestive (p 0.10) |

**What the round adds.**

- **Knossos kept part of the Minoan notation (U4).** In Linear B single-logogram lists, Knossos writes the logogram on 72% of lines and Pylos on 89%. The difference holds within the same logogram (p 0.007), mainly in lists of men (82% against 96%) and women (42% against 100%). Linear A writes the sign on 38% (round 63). The Knossos scribes sit between, closer to the Mycenaean practice but still omitting the logogram on many lines.
- **Economy grows with list length (U3),** and **lists of men are the most economical (U5).** Longer lists repeat the sign less (rho −0.33). Lists of men write VIR on only 13% of entries, against 41% for goods: a personnel list states VIR once and lists names with counts.
- **Not supported:**
  - Khania repeats the sign no more than Haghia Triada (U1);
  - scribes do not differ (U2);
  - KU-RO lines do not restate the commodity (U6);
  - economical lists are not clearly more ordered (U7, p 0.10).

# Sixty-fifth (saturation loop 7) round: who kept the once-only logogram at Knossos, 24 September 2026

`reading/round65.py`, results in `reading/round65_results.json` and `reading/round65_output.txt`.

Eight hypotheses on which Knossos Linear B lists write the logogram only once ("share" = share of a single-logogram list's numbered lines that carry the logogram). Benjamini–Hochberg at 5% across the eight. Stratified checks and a look at the lists were added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| V7 | Knossos lists with more Minoan names omit the logogram more | 0.3429 (spearman -0.046, lists 25) | no | not supported |
| V8 | Scribes who omit the logogram more have more Minoan names | 0.7157 (spearman 0.257, scribes 6) | no | not supported |
| V9 | Room of the Chariot Tablets lists omit the logogram more | 0.8791 (RCT [0.9, 4], later [0.7, 59]) | no | not supported |
| V10 | Knossos lists of women omit the logogram more than lists of men | 0.0005 (MUL [0.4167, 18], VIR [0.8158, 18]) | yes | artefact: 13 of 18 MUL lists are the women-and-children format, whose girls and boys lines carry their own word |
| V13 | Knossos lists that omit the logogram contain undeciphered-sign words more often | 0.953 (omitting [0.1579, 38], full [0.2857, 35]) | no | not supported |
| V14 | Logogram omission differs by Knossos scribe | 0.0005 (between_SS 1.813, null 0.484, lists 40, groups 6) | yes | confounded: gone within logogram (p 0.20) |
| V15 | Logogram omission differs by Knossos findspot | 0.0285 (between_SS 1.394, null 0.631, lists 43, groups 7) | no | not supported after BH (p 0.029) |
| V16 | Pylos personnel lists omit the logogram more than goods lists | 0.9975 (personnel [0.9646, 33], goods [0.8597, 75]) | no | not supported |

**What the round adds.**

- **No new learning.** Both survivors fail their checks. The women lists (V10) sit at one line in three because the Knossos women tablets give girls (ko-wa) and boys (ko-wo) on their own lines; nothing is left out. The scribe difference (V14) is the logogram difference: shuffling scribes within logogram gives p 0.20.
- **Correction to round 64 (U4).** Without the women lists, Knossos writes the logogram on 82% of lines against Pylos 89% (p 0.03); on lists of goods 82% against 86% (p 0.21). What remains is two long Knossos name lists (hands 102b and 105) that state VIR once or twice for a dozen names. The page sentence is narrowed to that.
- **Not supported:** Minoan-shaped names (V7, V8), the Room of the Chariot Tablets (V9), undeciphered-sign words (V13), Pylos personnel lists (V16).

# Sixty-sixth (saturation loop 8) round: fixed allocations, fraction signs and final signs, 24 September 2026

`reading/round66.py`, results in `reading/round66_results.json` and `reading/round66_output.txt`.

Nine hypotheses on whether a recurring name or term gets a fixed amount, and on what fraction signs and word-final signs go with. Benjamini–Hochberg at 5% across the nine. Stratified checks were added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| W1 | A recurring name gets similar amounts | 0.0025 (mean_var 0.782, null 1.297, words 47) | yes | confounded: gone within site and commodity (p 0.15); the known person–commodity link |
| W2 | A recurring descriptor gets similar amounts | 0.971 (mean_var 2.391, null 1.404, words 7) | no | not supported |
| W3 | A recurring name gets exactly the same amount on two tablets | 0.7381 (words_with_repeat 10, null 11.05) | no | not supported |
| W4 | Fraction signs go with the commodity | 0.1139 (chi2 32.4, null 24.5, n 98, groups {'OLE': 19, 'VIN': 19, 'GRA': 17, 'CYP': 35, 'OLIV': 8}) | no | not supported |
| W5 | Fraction signs differ by site | 0.019 (chi2 53.3, null 30.7, n 261, groups {'Haghia Triada': 160, 'Khania': 70, 'Petras': 8, 'Phaistos': 5, 'Tylissos': 6, 'Zakros': 12}) | yes | restatement of the regional fractions (NOTES, bookkeeping summary) |
| W6 | Fraction signs differ by Haghia Triada scribe | 0.0005 (chi2 66.6, null 36.7, n 67, groups {'HT Scribe 2': 12, 'HT Scribe 8': 13, 'HT Scribe 10': 9, 'HT Scribe 1': 12, 'HT Scribe 14': 5, 'HT Scribe 5': 7, 'HT Scribe ) | yes | confounded: gone within commodity (p 0.67) |
| W7 | Final sign of name words goes with the tablet commodity | 0.0005 (chi2 322.2, null 201.6, n 181, groups {'VIR': 90, 'OLE': 10, 'VIN': 44, 'GRA': 29, 'OLIV': 8}) | yes | not robust: men vs goods null (p 0.65); goods-only p 0.037 falls to 0.11 without -RU, the withdrawn -RU lead |
| W8 | Final sign of descriptor words goes with the commodity | 0.5677 (chi2 227.7, null 232.0, n 138, groups {'OLE': 20, 'VIR': 15, 'VIN': 8, 'GRA': 61, 'CYP': 26, 'OLIV': 8}) | no | not supported |
| W9 | A recurring name stays with one commodity | 0.042 (single_commodity_words 11/25, null 5.41) | no | not supported after BH (p 0.042) |

**What the round adds.**

- **No new learning.** All four survivors fail their checks or repeat known results.
  - A recurring name does get similar amounts (W1), but only because names stay with one commodity and commodities have their own scale. Within site and commodity the effect is gone (p 0.15), and without the men lists nothing is left (p 0.60). There is no evidence of fixed rations per person.
  - Fraction signs differ by site (W5), which is the regional fraction habit already recorded. They differ by scribe (W6) only through the scribes' commodities: within commodity, p 0.67.
  - The final sign of a name goes with the tablet's commodity (W7) under a tablet-level shuffle (p 0.004). But men's lists and goods lists do not differ (p 0.65), and on goods lists the signal rests on the -RU names of grain tablets (p 0.037, then 0.11 without them). That is the -RU lead withdrawn earlier.
- **Not supported:**
  - descriptor terms do not keep a fixed amount (W2);
  - exact repeated amounts are at chance (W3);
  - fraction signs do not follow the commodity after correction (W4, p 0.11);
  - descriptor final signs are independent of the commodity (W8);
  - recurring names keep one commodity only nominally (W9, p 0.042).

# Sixty-seventh (saturation loop 9) round: change over time, and what vessels name, 24 September 2026

`reading/round67.py`, results in `reading/round67_results.json` and `reading/round67_output.txt`.

Six hypotheses on change over time, with Phaistos (Middle Minoan II, a few kilometres from Haghia Triada but some two centuries older) against the Late Minoan IB archives, and on what clay-vessel inscriptions name. Benjamini–Hochberg at 5% across the six.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| Y1 | Phaistos words occur at Haghia Triada less often | 0.974 (Phaistos [0.1154, 52], other_nonHT [0.0565, 549]) | no | reversed: Phaistos words occur at HT more often (12% vs 6%), so proximity, not time |
| Y2 | Phaistos uses signs unattested at Haghia Triada more often | 0.062 (Phaistos [0.0523, 153], other_nonHT [0.0259, 1774]) | no | suggestive (p 0.06) |
| Y3 | Phaistos lists repeat the commodity sign more | 0.8611 (Phaistos [0.2254, 3], LM_IB [0.3868, 53]) | no | not supported |
| Y4 | Phaistos lists run largest-first | 0.9025 (mean_tau -0.275, null 0.009, lists 5) | no | not supported |
| Y5 | Vessel words are name-slot words more often | 0.7636 (diff -0.0036, null -0.0012, vessel_types 63, in_name 2, in_desc 1) | no | not supported |
| Y6 | Phaistos words are shorter | 0.0905 (Phaistos [2.9423, 52], other_nonHT [3.2313, 549]) | no | suggestive (p 0.09) |

**What the round adds.**

- **No new learning.** Nothing survives. Phaistos vocabulary shows no turnover over time: its words occur at nearby Haghia Triada more often than the words of more distant sites do (12% against 6%). Phaistos may use signs unknown at Haghia Triada more often (5% against 3%, p 0.06) and have shorter words (p 0.09), but neither passes. Phaistos has only 3 single-commodity lists and 5 lists of three or more amounts, too few to date the bookkeeping habits. Clay-vessel words almost never recur in the tablets' name or descriptor slots (2 and 1 of 63 types).
- **The saturation loop stops here.** This is the third round in a row with no new learning (rounds 65, 66, 67), which meets the stop rule fixed before round 59.

# Sixty-eighth (after the loop) round: the Z row, and Linear A's sound pattern among 104 languages, 24 September 2026

`reading/round68.py`, results in `reading/round68_results.json` and `reading/round68_output.txt`.

Run after the saturation loop stopped, on the two open leads that need no new inscriptions: a scan of every consonant row for the Z signs, and a comparison of Linear A's sound pattern with 104 Eurasian languages (NorthEuraLex 4.0, CC-BY 4.0, in the git-ignored data/ folder), each respelled with Linear B's spelling rules. Benjamini–Hochberg at 5% across the eight. Checks for L1 (sample size, spelling rule, consonant set) were added after the run.

| # | Hypothesis | primary p | BH 5% | verdict |
|---|---|---|---|---|
| M1 | Another row is closer to ZA/ZU than chance | 0.3278 (best_row n, affinity 0.0979, null_max 0.0911, z_signs ['za', 'zu']) | no | not supported |
| L0 | Linear B finds Greek among its nearest languages | 0.0476 (greek_rank 5, of 104) | no | control passed weakly: Modern Greek 5th of 104 for Linear B (p 0.048); the method separates languages only coarsely |
| L1 | Linear A coronal e/o conditioning is extreme | 0.0095 (LA_cor 1.224, languages_as_high 0) | yes | **new**, narrowed: above all 104 languages on the main measure (0 of 200 size-matched draws reach it; holds with a no-echo spelling rule and without Q), but Lak passes it when only R and T are counted (1.49 against 1.44), and Linear A's bootstrap interval (0.95–1.53) overlaps Lak |
| L2 | Linear A e/o share is extreme | 0.1143 (LA_eo 0.174, languages_as_low 11) | no | not supported |
| L3 | Linear A harmony is extreme | 0.2381 (LA_harm 0.634, languages_as_high 24) | no | not supported |
| L4 | One family dominates Linear A's nearest languages | 0.6542 (max_family_count 4, null 4.02) | no | not supported |
| L5 | Languages nearer Crete are nearer Linear A | 0.8836 (spearman -0.119, languages 104) | no | not supported |
| L6 | Linear A and Linear B have different nearest languages | 0.005 (overlap 0, lb_resample_overlap 9.04) | yes | a check (Linear A and Linear B profiles differ), restating the known contrast |

**What the round adds.**

- **Linear A's consonant-conditioned e/o is at the far end of what natural languages do, but it is attested (L1).** Respelled the way Linear B spells Greek, no one of 104 Eurasian languages reaches Linear A's contrast (e/o after T, R, S, N, Q against after K, P, M, J, W; log-odds 1.22). The nearest is Lak (0.99), a Nakh-Daghestanian language of the Caucasus. The result holds on samples cut to Linear A's size and under a second spelling rule. It is narrowed, though. When only R and T are counted, Lak passes Linear A, and Linear A's bootstrap interval overlaps Lak's value. So the pattern is extreme but found in at least one natural language, and it need not be a scribal convention. Linear B's spelling of Greek does not produce it (−0.14).
- **No family or region.** Linear A's ten nearest profiles are scattered: Lak, Estonian, Mansi, Evenki, Manchu, Sami, Dargwa, Mongolian, Lezgian (L4, p 0.65), and nearness in profile does not follow distance from Crete (L5). Its e/o share (L2) and harmony (L3) are within the range of these languages. The control is weak: Linear B finds Modern Greek only 5th of 104, so the comparison can sort broad profiles but is far too coarse to identify a relative.
- **The Z row stays open (M1).** Scanning every row, ZA and ZU keep company most with N and R, but no more than random sign pairs do with their best row (p 0.33).
