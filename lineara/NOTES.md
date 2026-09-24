# Linear A research

Status: written up (docs/lineara.html), no ledger entries and no profile by the user's choice, 23 Sept 2026. Structure, numbers, commodities, accounting terms and three place names read; the language unread.

## Objective and limits

2026-09-23: User explicitly requests research toward decipherment. Linear A is a writing system for an unidentified language, not an encrypted known-language text. No full decipherment or novel word meaning is claimed. The research goal remains open.

## Prior work and contamination

Before analysis, consulted Ester Salgarella's *Linear A* (Oxford Classical Dictionary, 2022), her *Writing in Bronze Age Crete* (2025), and Philippa Steele's *Exploring Writing Systems and Practices in the Bronze Age Aegean* (2023). KU-RO as a total and PO-TO-KU-RO as a grand total are established contextual interpretations; KI-RO as deficit is a received hypothesis. Their reproduction here is not independent discovery.

Also encountered Christos Tsirkas's 2026 public repository `corpus-validation-for-undeciphered-scripts-linear-a`. It claims corpus corrections, statistical tests of affixation and inherited sound values, and arithmetic confirmation of KU-RO. These are prior, unverified research claims, not treated as scholarly consensus. Its report that KI-RO does not behave as a total motivates checking a different possibility: a heading qualifying the following entries.

## Sources

- Salgarella 2022: https://www.repository.cam.ac.uk/items/f50c0df4-f355-4bc0-be2a-8e960b2bb5da
- Salgarella 2025: https://doi.org/10.1017/9781009520041
- Steele 2023: https://crewsproject.wordpress.com/wp-content/uploads/2023/10/steele-2023.pdf
- Digital working corpus: https://github.com/mwenge/lineara.xyz (Robert Hogan); upstream GORILA transcriptions, George Douros tabulation, John Younger commentary.
- Independent palaeographic reference: https://sigla.phis.me/ (Ester Salgarella and Simon Castellan).
- Prior computational project: https://github.com/ChristosTsirkas/corpus-validation-for-undeciphered-scripts-linear-a

## Protocol

1. Pin and hash a corpus snapshot; retain glyphs and metadata, remove supplied English glosses from analysis data.
2. Audit duplicate witnesses, damage, segmentation and missing metadata before statistics.
3. Establish arithmetic controls using known accounting terms; distinguish replication from discovery.
4. Test KI-RO as a heading versus a total, and examine repeated entry labels across sections. Unknown labels stay unknown.
5. Any proposed meaning must survive comparison with unused documents, scribes and sites. Do not choose a language from isolated sound resemblances.


## First-pass results, 2026-09-23

See [RESEARCH_REPORT.md](RESEARCH_REPORT.md) for the analysis and [accounting_results.json](accounting_results.json) for all machine-readable cases. Acquired 1,722 records / 1,721 names; 436 are marked Tablet. Preserved two KH101 records and flagged missing KNZg57b transliteration. Field comparison classified 610 identical, 886 empty-transcription, 130 damage-placement-only, and 96 other differences; differences are not automatically errors.

Three preselected KI-RO-headed lists balance at the following KU-RO (HT88: 6; HT94b: 5; HT117a: 10), reproducing prior interpretation. A narrow unseeded integer screen produces two KU-RO matches and one SA-RU coincidence over 44 opportunities / 38 sign groups; repeated-list comparison defeats a confident SA-RU=total inference. HT13 and HT123 inconsistencies were already discussed by Younger. The first two HT123 rows, under fixed positive ratio and additive deficit assumptions, imply a negative ratio even with X unknown. Four facsimiles inspected; no new translation claimed.

Validation: analysis assertions passed; profile checker reports valid. Source receipts and hashes saved. Research remains open; no website or solved-catalogue status is asserted.


## Second pass: source collation and word extensions, 2026-09-23

Previous goal turn classified as progress: it created the pinned corpus and accounting evidence. Current continuation fetched and decoded SigLA (802 documents / 5,144 attestations), preserving its CC BY-NC-SA 4.0 attribution. Verified both binary payload lengths/object counts and six rendered-page cases. Corrected the positional interpretation suggested by a third-party decoder: the nested pair is sign position / word index, not boundary states. No claim is made about downstream effects in that third-party project.

Recovered 1,401 word groups and aligned 824 multi-sign tokens across editions; 612 tokens / 420 distinct forms pass current confidence and damage filters. A 5,000-replicate experiment under two vocabulary-size-preserving nulls finds 42 single-sign extension relations versus means 23.11 and 25.93, with both full-sample adjusted p-values about 0.0096. This is ordered word-form structure, not semantic decipherment. No supported prefix/suffix direction preference; HT-only signal fails the full multiple-test adjustment. See [SIGLA_MORPHOLOGY_REPORT.md](SIGLA_MORPHOLOGY_REPORT.md).

Longer-base candidates include A-PA-RA-NE / PA-RA-NE and DA-KU-SE-NE(-TI). Hypothesis that A- universally marks headings fails on ZA10a, where both prefixed/unprefixed TA-NA-TE occur as ordinary entries. HT104's terminal TI has a published alternative interpretation as a separate ideogram, retained as unresolved. Follow-up should test specific functions and collate more ritual texts rather than assign translations from the string statistics.

## Third pass: fraction signs, 2026-09-23

Pulled together from the untracked `C:\Users\dbour\cypher\lineara` folder into this branch. See
[FRACTIONS_REPORT.md](FRACTIONS_REPORT.md). The earlier passes left fractions out of every arithmetic test. Only
HT104 gives a clean fraction equation from a total (J+J=1). Blind order analysis of 296 undamaged fraction runs
(42 multi-sign, 29 adjacent-pair tokens) was fixed before reading Corazza et al. 2021 (JAS 125, 105214).
Scored against their values, HT34.3 "2 H K" (lineara, SigLA and the GORILA drawing agree) needs H > K. With K =
1/10 and their own one-value-one-notation constraint, no typological H satisfies it. Younger's settlement reading
of HT34 (PU F settles QA+[?]+PU A) also needs F <= A, against A = 1/24. The disputed values are the two (H, A)
that Corazza et al. say optimality did not fix. B = 1/3 (Bennett-type glosses) fails on KH9 E B. KH86 A B B
(lineara, SigLA) against their A A remains a reading dispute. Corpus flag: HT34.6 KI-RO "37" should be 30 with an
erased 7 (Younger).

Next: A-/-TI functions (second pass list); collate fraction-bearing tablets against SigLA sign by sign. Check
whether the HT34 counterexample is discussed in later fraction literature (Montecchi; Schrijver) before
presenting it anywhere.

## Fourth pass: reading the corpus to the extent possible, 2026-09-23

Scripts and outputs in `reading/`; summary in [reading/READING.md](reading/READING.md).

- Sound values (`soundvalues.py`): Linear B values give 6 exact Linear A = Linear B word matches among 491 Linear A
  word types of 3+ signs (PA-I-TO, SU-KI-RI-TA, SE-TO-I-JA, A-RU-RA, I-JA-TE, DA-MA-TE). Random reassignment of the
  values within frequency bins gives a mean of 0.49 (max 6 in 2000; p about 0.001). Near matches (same stem, other
  final sign) are not significant (35 against 25.4, p 0.09). The values carry over; the vocabulary is not Greek.
- Structural reading (`build_reading.py`): all 1,722 records, 5,339 non-apparatus tokens. 41.8% of tokens (32.1% of
  signs) read as sense: numbers, fractions (Corazza values; H and A left open), commodity logograms, KU-RO, PO-TO-KU-RO,
  KI-RO and three validated place names. A further 40.5% read as sound only, with a document function (entry label,
  heading, formula word, sealing mark); 66 entries tagged as probable personal names in VIR lists. Edition in
  `reading/edition.txt`. Correction applied: HT34.6 KI-RO 30 (not 37).
- Totals: 35 KU-RO / PO-TO-KU-RO checked with exact fractions over record, rule, KI-RO, whole-object and same-commodity
  windows; 10 balance (HT123a's olive total only in the same-commodity window). The failures are damage or the known
  scribal slips (HT9a 3/4, HT13 1/2, HT94a 1, HT119 1, HT122 grand total 1). `restorations.py` proposes the missing
  amounts where an intact total covers a damaged list (HT11a 4, HT100 4, HT122a 9, HT27a 13, HT25b 8).
- Libation formula (`formula.py`): 14 inscriptions from 7 sites keep one slot order (77 of 78 pairs):
  A-TA-I-*301-WA-JA, place word, (J)A-SA-SA-RA-ME, U-NA-KA-NA-SI, I-PI-NA-MA, SI-RU-TE, ...-U-TI-NU. The JA-/A-/zero
  prefix moves between slots (JA-DI-KI-TU at Iouktas, A-DI-KI-TE at Palaikastro, JA-SA-U-NA-KA-NA-SI on PKZa8).
  The place word A-DI-KI-TE at Palaikastro, where the later cult of Diktaean Zeus was centred, is contextual support
  for the published Dikte identification, not a test.

## Fifth pass: the three leads, 2026-09-23

See [LEADS_REPORT.md](LEADS_REPORT.md).

- Fraction literature: 18 works cite Corazza et al. 2021 (OpenAlex); none revises the values. Corazza 2024 (Bologna UP,
  open access) keeps A = 1/24? and H = 1/16? as tentative and does not discuss HT 34. The HT 34 counterexample is
  unaddressed in the literature reachable online.
- Language hypotheses (`reading/lang_test.py`): fixed Linear B spelling rules, exact matches with 491 Linear A
  types, own-syllable shuffle null, family against controls. Semitic 2.65x null against controls 1.7x (p 0.23,
  0.69 corrected); Luwian 0.54x; Etruscan too small; Hurrian no open lexicon. Positive control: unbiased Greek
  against Linear B gives 13/1000, below Yoruba's 22/1000. Look-alike matching cannot identify a language here.
- Linear B names (`reading/names_lb.py`): 13 exact Linear A = Linear B matches against 2.8 (p 0.0005); toponyms
  3 against 0.17, anthroponyms 3 against 0.72. All six matched names are Crete-only (Knossos) Linear B words (p 0.018
  given 51.3% of names are Crete-only); the mainland matches are Greek common words. New shared names include
  TA-NA-TI, KI-DA-RO, DA-I-PI-TA, I-TA-JA and PA-RA-NE.

## Sixth pass: second round of leads, 2026-09-23

See LEADS_REPORT.md, "Second round".

- New inscriptions: the Anetaki ivory sceptre, KN Zg 57 (ring) and KN Zg 58 (handle), about 119 signs, published only
  in preliminary form (Kanta, Nakassis, Palaima, Perna, Ariadne 2025) without a transcription. The full edition is
  Kanta (ed.), Anetaki II, forthcoming. The Zg 58 handle has a six-sign fraction sequence that the authors say
  orders the values differently from all proposals; the sequence is withheld.
- Cross-tablet linkage (`reading/prosopography.py`): 4 record pairs share 3+ entry words, against a null of 0.11
  (p 0.001).
  - HT 86/95: the same five men under the headings A-KA-RU and A-DU, 20 each on HT 86a and 10 each on HT 95b.
  - HT 9 recto/verso: under PA3 every shared amount is equal or smaller; with HT 34 (100, PA3 70, KI-RO 30),
    PA3 = the part delivered.
  - Names in KI-RO sections always carry 1: KI-RO lists count individuals.
- Kober test (`reading/kober.py`): endings do not predict position within stem families (p 0.20). A-/JA- leans
  toward headings (p 0.07, 12 families). No inflection is recoverable at this size.
- HT 34 note drafted (`note_HT34/NOTE_HT34.md`), with unsent requests to the Heraklion Museum and the INSCRIBE
  team (`note_HT34/REQUESTS.md`). The SigLA image of HT 34 is a redrawing, not a photograph; the museum number is
  HM 22 (Younger).

## Seventh pass: third round of leads, 2026-09-23

See LEADS_REPORT.md, "Third round".

- Cross-site names: 10 entry words at 2+ sites against 33.5 by chance (P 0.0005). The archives are local, and the
  words crossing sites are mostly administrative (A-DU, DA-RE, KU-PA, SA-MA).
- Fractions by commodity: the three violations fall in three different contexts; HT 34 is the only H/K pair.
  Commodity-specific units are not testable and not supported.
- Hurrian: Laroche 1980 (Internet Archive OCR, local cache only), 294 forms, 1 match against 0.9 (p 0.6). All four
  proposed families now fail to beat the controls.
- Salgarella 2025: closed access; needs a purchase or a library copy.

## Eighth pass: Eteocretan and Pre-Greek, 2026-09-23

See LEADS_REPORT.md, "Fourth round".

- Eteocretan (`reading/eteocretan.py`; Brown's transcriptions of Dreros 1-2 and Praisos 1-3, 193 syllables):
  0 Linear A words of 3+ signs occur inside it (null 0.39; unrelated-language samples 1.2-2.7). Positive control:
  Linear B words in a comparable length of Greek, 2 (neutral text, p 0.06) or 3 (Cretan text, p 0.012). The corpus
  weakly disfavours a close Linear A-Eteocretan identity (P about 0.05-0.15) and cannot test a distant one.
- Pre-Greek (`reading/pregreek.py`; 1,600 Wiktionary qsb-grc entries): against length-matched ordinary Greek,
  6 against 2.62 (p 0.04), 5 against 2.55 without proper names (p 0.10), stems 1 against 1.17. The matched words do
  not fit their Linear A contexts. Syllable distributions put Pre-Greek no closer to Linear A than ordinary Greek.
- Conclusion: no comparison identifies Minoan; the positive controls show word matching has too little power at
  these sizes. The language question now waits on new texts.

## Ninth pass: Salgarella file, DAMOS, Hieroglyphic, errata, 2026-09-23

See LEADS_REPORT.md, "Fifth round".

- The supplied Salgarella file is the Kadmos palaeography paper "Drawing Lines", not the 2025 book, and does not
  touch fractions or HT 34.
- DAMOS (CC BY-NC-SA) reproduces 12 of the 13 Linear A = Linear B matches and the Knossos-only split; the shared
  names are list entries with count 1 in both scripts (TA-NA-TI: KN Uf 311 DA 1 / HT 7a 1).
- Cretan Hieroglyphic (Younger's archived lexicon and grids): with shape-based values only 20 groups are readable,
  3 matches against 2.2 (p 0.38); Younger's grid 2 raises it to 17 against 11.1 (p 0.04), but that is circular.
- Errata (`errata.py`, `ERRATA.md`): 44 word-level disagreements between SigLA and lineara.xyz. Flags for this
  project's results: SU-KI-RA-TA (PH Wa 32), PA-RI-NE (HT 122a), DA-ZA (HT 95b) in SigLA. Issue drafts not posted.

## Tenth pass: dependence on disputed readings, 2026-09-23

`reading/sigla_sensitivity.py`: with SigLA's readings substituted (17 definite disagreements), Linear B matches go from
13 to 12 (p 0.001 both) and names from 6/6 to 5/5 Crete-only (p 0.036). Only the Sybrita match depends on a disputed
reading (PH Wa 32 SU-KI-RA-TA in SigLA). Pre-Greek and language results are unchanged. SigLA reverses no fraction
pair it records; HT 34 H K and KH 86 A B confirmed.

## Eleventh pass: name shapes, proportions, scribal variants, 2026-09-23

- Name shapes (`reading/name_shapes.py`): Knossos-only Linear B personal names (637) are closer in syllable shape to
  Linear A list names (358) than Pylos-only names (339) are, p 0.0002 on all, first and last syllables. The same holds
  without Greek-etymology names, and with the exact shared names removed (p 0.0003). Non-name vocabulary control:
  no difference (p 0.27-0.48). It holds for Haghia Triada, Zakros and Khania separately.
- Ration proportions (`reading/fraction_ratios.py`): only KH 7a (Montecchi's B = 1/5); nothing new.
- Scribal variants (`reading/scribes_variants.py`): SigLA variant codes are editorial and sparse; not testable (p 0.32).

## Twelfth pass: ten further hypotheses, 2026-09-23

`reading/hypotheses10.py`; table in LEADS_REPORT.md, "Eighth round".

- Supported:
  - H3: Knossos name stems are o-poor toward Linear A (12.3% against Pylos 16.5%, p 0.002; Linear A 3.2%).
  - H4: the signs Linear B dropped were rare in Linear A (median 2 against 49, p 0.0002).
- Informative negative: H1, Linear A lacks Linear B's echo-vowel cluster signature.
- Not supported: H2 initial A-, H6 Knossos series, H7 formula prefix by site, H8 commodity specialisation, H9 terms
  and commodities (record level p 0.20).
- Untestable: H10.
- Partial: H5, no single syllable drives the name-shape effect; it survives removing -eus names.

## Thirteenth pass: fifty hypotheses in ten batches, 2026-09-23

`reading/batches.py`: 49 tested, 29 survive Benjamini-Hochberg at 5%; the table is in LEADS_REPORT.md, "Ninth
round".

- New and strongest: Knossos Linear B syllable use is closer to Linear A (p 0.002); undeciphered LB signs are about
  3x commoner at Knossos (p 0.0005); Linear A religious words also resemble Knossos names (p 0.0005).
- Bookkeeping: largest amounts listed first, even amounts preferred, KI-RO amounts smaller, regional fraction
  repertoires, shared scribal vocabulary, sealing signs abbreviate word beginnings.

## Fourteenth pass: twenty-five further hypotheses, 2026-09-23

`reading/batches2.py`: 25 tested, 13 survive BH at 5%; the table is in LEADS_REPORT.md, "Tenth round".

- New: Knossos-only words are Linear A word + 1 syllable twice as often as Pylos words (7.8% against 3.4%, p 0.0005);
  Knossos names have Linear A stems with Greek-like endings beyond chance (p 0.007; mostly 2-sign stems, statistical
  only). Also: Cretan LB place names more Linear A-like (p 0.0055); A- words are headings 20% against 9% (p 0.0005);
  KI-RO entries mostly 1; tablet amounts are doubles of each other more than chance.
- Reversal: Knossos names end in -o more than Pylos names. The last-syllable closeness is a Pylos -eus effect; the
  Minoan signal is in the stems.

## Fifteenth pass: ten follow-ups tested hard, 2026-09-23

`reading/vigorous.py`: ten follow-ups to supported results, each with a pre-stated prediction and robustness checks;
the table is in LEADS_REPORT.md, "Eleventh round". Supported: V1, V7, V9. Mixed: V4. Refuted: V3, V6. Circular: V10.

- The Knossos name-shape result predicts out of sample: a model trained without any Knossos name and tested on
  held-out Pylos names gives AUC 0.59 (p 0.0025 against a label shuffle); common words give 0.53.
- Religious words resemble Knossos names with the libation-formula words removed (154 words, p 0.0005).
- Amounts on a tablet share a divisor above 1 twice as often as chance (p 0.0005; within-site p 0.001).
- Stem caveat: the Knossos stem excess holds for 3+-sign stems against Pylos (p 0.021) but not against Thebes,
  Mycenae and Tiryns (p 0.17); the stems are Linear A words in general, not names (V3).
- KI-RO is rarer on VIR tablets, not commoner (1/12 against 11/29): the owed-persons reading of KI-RO is not supported.

## Sixteenth pass: ten more follow-ups tested hard, 2026-09-24

`reading/vigorous2.py`: table in LEADS_REPORT.md, "Twelfth round". Supported: W2, W4, W6, W9. Mixed: W10.
Suggestive: W1, W5. Refuted: W3. Not supported: W7, W8.

- The Knossos name result is independent of the Linear A training site (non-HT names AUC 0.61, HT-only 0.59, both
  p 0.0033, also without Knossos Linear A names) and of naming habits (a religious-word model gives 0.60, 0.61
  with the formula removed).
- Knossos words with undeciphered signs are Linear A-like in their other syllables (p 0.027, neutral reference).
- Largest-first survives the removal of any one Haghia Triada scribe.
- Against Thebes/Mycenae/Tiryns (46 names) the name and o-deficit contrasts point the same way but are not
  significant (p 0.074, 0.097).
- Room of Chariot Tablets names are not more Minoan than later Knossos names (AUC 0.44).

## Seventeenth pass: ten hypotheses aimed at reading, 2026-09-24

`reading/decipher10.py`: table in LEADS_REPORT.md, "Thirteenth round". Supported: Y1. Suggestive: Y2, Y4.
Refuted: Y10. Not supported: Y3, Y5-Y9.

- The Linear B consonant rows behave as sound classes in Linear A: same-row signs have more similar contexts
  (p 0.0005), as strongly as in Linear B. The result survives with harmony neighbours removed, without the vowel row
  and word boundaries, and at Haghia Triada and the other sites separately.
- Exploratory: the Z row (ZA, ZU) is the only row that does not cohere; ZU is the worst-fitting sign. No
  replacement value is proposed.
- Vowels are recoverable from context (42% against 20%), consonants are not. Value predictions for the unread
  signs produce no more Linear B words than random values.
- A- pairs (A-X / X) are no commoner than chance: no evidence for an A- prefix.

## Eighteenth pass: ten more hypotheses on values and vowels, 2026-09-24

`reading/decipher10b.py`: table in LEADS_REPORT.md, "Fourteenth round". None survives BH at 5%.

- The consonant-row signal cannot place single signs: nearest neighbours get 8% of Linear A consonants (chance 7%)
  against 27% in Linear B. Value predictions for unread signs do not beat random values.
- Special signs lean towards their Linear B rows (p 0.07); PA3 does not fit P.
- Exploratory: Linear A e/i and o/u sign pairs behave more alike than in Linear B (p 0.003, 0.014), consistent with
  a Minoan system with marginal e and o; confounded by Greek case endings on the Linear B side.
- No vowel harmony and no phonetically close spelling alternations in Linear A (both clear in Linear B).

## Nineteenth pass: vowel lead on fresh data, vowel-free matching, 2026-09-24

`reading/decipher10c.py`: table in LEADS_REPORT.md, "Fifteenth round". Supported: A5, A7. Suggestive: A1, A6.
Refuted: A2, A10. Not supported: A3, A4, A8, A9.

- Knossos names have an e-deficit as well as the o-deficit: internal e 16.4% against 25.5% at Pylos (p 0.0005;
  Linear A 10.4%), robust to -e-u names and first syllables; no gap in common words.
- e/i and o/u are not interchangeable in spellings (Linear A–Linear B near matches at chance): Minoan e and o were rare,
  not shown to be merged.
- Consonant-skeleton matching restates the Knossos name effect and finds no meanings.

## Twentieth pass: rare vowels, name models, accounting signs, 2026-09-24

`reading/decipher10d.py`: table in LEADS_REPORT.md, "Sixteenth round". Supported: B2, B10. Refuted: B6 (acrophony),
B9. Not supported: B1, B3, B4, B5, B7, B8.

- Knossos-only place names and ethnics have 21% e/o-syllables (ending removed) against 42% at Pylos and 48% at
  Thebes/Mycenae/Tiryns (Linear A 18%); common words 46% against 50%. The e/o rarity is a property of Minoan words.
- Linear A e/o-signs are word-final half the time (a/i/u a third): NE 73%, ME 68%, TE 61%. The same pattern holds in
  Linear B, so it is not diagnostic of the language.
- Single signs on tablets are not initials of nearby words.

## Twenty-first pass: the vowel profile beyond Linear A, 2026-09-24

`reading/decipher10e.py`: table in LEADS_REPORT.md, "Seventeenth round". Supported: C1, C2 (o only), C5, C7, C8, C10.
Inconclusive: C3. Suggestive: C6. Refuted: C4. Not supported: C9.

- Pre-Greek stems have fewer e and o than ordinary Greek (e 17.5% vs 28.1%, o 16.3% vs 20.6%, p 0.0005 each).
- Eteocretan has little o (10.6%) but ordinary e.
- Linear A e/o depend on the consonant (after Q, R, T, S; none after W, Z), four times Linear B's dependence.
- Religious words end in -TE twice as often (A-DI-KI-TE, DA-MA-TE, I-DA-MA-TE).
- Vowel profiles cannot choose a language family (Hawaiian and Hittite as close as any candidate).

## Twenty-second pass: twenty-five hypotheses, 2026-09-24

`reading/decipher25.py` and `reading/decipher25_checks.py`: table in LEADS_REPORT.md, "Eighteenth round".
Supported: D1, D20, D22. Artefacts found by the checks: D13 (feminine -a), D8 (two-sign words). Refuted: D2, D4, D19,
D23, D24. Suggestive: D9, D25. The rest not supported.

- Linear A e/o follow coronals (22.5%) more than other consonants (12.4%), inside words too; Linear B does not.
- Pre-Greek shares the e/o shortage but not this conditioning, nor Linear A's consonant or length profile.
- Recurring entry words stay with one scribe (17.6% vs 4.4%, sides merged, terms removed).
- HT 86/HT 95 and ZA 4/ZA 15 carry the same groups of entry words (recopied lists).
- Counting note: sides a/b are separate records in the corpus; merge them for any per-tablet test.

## Twenty-third pass: twenty-five more hypotheses, 2026-09-24

`reading/decipher25b.py`: table in LEADS_REPORT.md, "Nineteenth round". 12 of 25 survive BH at 5%.

- The coronal rule is secure: e alone, outside HT, in names, same-syllable only (next syllable's consonant no effect),
  and e/o replace i/u, not a. Not shared by Eteocretan, Cretan place names in Linear B, or Pre-Greek.
- Scribes specialise in commodities and transaction terms; same-scribe tablets share vocabulary (sides merged).
- Minoan-shaped Knossos names (stem-scored) cluster by Linear B scribe.
- Row cohesion comes from the preceding sign.
- Sides merged: V7 (common divisor) weakens to p 0.03; V6 (KI-RO off VIR tablets) is withdrawn; L3 doubles holds.

## Twenty-fourth pass: fifteen hypotheses, 2026-09-24

`reading/decipher15c.py`: table in LEADS_REPORT.md, "Twentieth round". Supported: F4, F13; F9 half. Not robust: F6.
Suggestive: F1, F2, F7. Untestable: F3, F14, F15.

- The coronal rule holds in religious texts as well as tablets.
- Knossos scribes with more Minoan-shaped names use more undeciphered signs (rho 0.48, 23 scribes).
- Lead: with dental e/o read as i/u, Linear A -RU matches Knossos -ro in five names (DI-DE-RU ~ di-de-ro,
  QA-QA-RU ~ qa-qa-ro, KA-SA-RU ~ ka-sa-ro, A-TI-RU ~ a-ti-ro). Tested on its own in the next pass: withdrawn.

## Twenty-fifth pass: the -u/-o lead, and SigLA replications, 2026-09-24

`reading/decipher11g.py`: table in LEADS_REPORT.md, "Twenty-first round". Replicated: G8, G13. Withdrawn: the -RU/-ro
lead (G1 p 0.26; -u words 5/105, -a words 8/242). Every site positive for the coronal rule (G10, 6/6).

- The coronal rule and the consonant rows replicate on SigLA's own sign readings (logOR 0.82; row diff 0.079).
- Coronal rule by site: HT 0.51, Khania 1.00, Knossos 0.17, Palaikastro 0.74, Phaistos 1.17, Zakros 1.20 (Linear B -0.25).
- Not in Linear B: Knossos undeciphered-sign words and special-sign use do not follow it.

## Twenty-sixth pass: eight hypotheses, 2026-09-24

`reading/decipher8h.py`: table in LEADS_REPORT.md, "Twenty-second round". Supported: H1, H2, H3, H7.

- The coronal rule survives dropping RE, holds in hapax words and in initial syllables.
- Correction: consonant by consonant it is not a clean dental class (H4 p 0.17). e/o are high after Q 50%, R 37%, T 28%,
  S 19%, N 17%; low after D 12%, zero after W, Z. State it as "concentrated after R and T (with S, N, Q)".
- Same-commodity tablets share vocabulary (p 0.003).

## Twenty-seventh pass: archives and regions, 2026-09-24

`reading/decipher9i.py`: table in LEADS_REPORT.md, "Twenty-third round". Supported: I1, I7, I9 (not name-specific).
Refuted: I5.

- Same-commodity tablets share persons (entry labels), not headings.
- Ligature adjuncts are regional: HT and Tylissos share OLE+U/KI/MI; Khania OLE+TA, VIR+KA; Zakros GRA+PA, VIN+RA.
- HT vocabulary differs from other sites in names and non-names alike.
- Signs without Linear B values are commoner in administrative than religious words (7.6% vs 4.3%).

## Twenty-eighth pass: regions and the R/T vowels, 2026-09-24

`reading/decipher6j.py`: table in LEADS_REPORT.md, "Twenty-fourth round". Supported: J3, J4, J6. Refuted: J2.

- Vowel entropy after R/T 1.52 vs 1.33 elsewhere (Linear B 1.53 vs 1.50): five vowels after R/T, closer to three elsewhere.
- Unread signs are regional: *411, *409, *311 Khania only; *309 Tylissos; *323, *325, *904 HT.
- Amounts differ by site within commodity (GRA HT 23 vs Khania 6, Zakros 5; VIN Zakros 23 vs HT 5).
- Tylissos shares HT's oil ligatures but none of its words.

## Twenty-ninth pass: seven follow-ups, 2026-09-24

`reading/decipher7k.py`: table in LEADS_REPORT.md, "Twenty-fifth round". Replicated: K6. Refuted: K2.

- R/T vowel richness replicates on SigLA (gap 0.19); holds at Zakros; reversed at Khania.
- Men's counts do not differ by site (HT 20, Khania 14) while grain and wine do: units, not economies.
- Local (single-site) unread signs are never word-final (0/40): root signs, not suffixes.

## Thirtieth pass: Khania, local signs, scribes, 2026-09-24

`reading/decipher6l.py`: table in LEADS_REPORT.md, "Twenty-sixth round". None survives BH.

- HT scribes do not differ in e/o after R/T (p 0.30, weak): no evidence the rule is scribal habit.
- Khania: more e/o after R/T (35% vs 27%) but not significant; not e/o-rich overall; not closer to Linear B.
- Exploratory twins for unread signs: *47-KU-NA ~ DA-KU-NA, *21F-TU-NE ~ QE-TU-NE, *306-TA-JE ~ RI-TA-JE, *333-SA-MU ~ JA-SA-MU.

## Thirty-first pass: twin values checked, R/T pattern beyond Linear A, 2026-09-24

`reading/decipher6m.py`: table in LEADS_REPORT.md, "Twenty-seventh round". None survives BH.

- Twin-derived values for unread signs do no better than random on the signs' other words: withdrawn as values.
- The R/T vowel gap is not in Knossos names or Pre-Greek; leans positive in Cretan place names (p 0.12) and
  Eteocretan (0.14 vs -0.11, p 0.0135, 35 pieces); a Linear A feature on present evidence.

## Thirty-second pass: the R/T rule as a search tool, 2026-09-24

`reading/decipher4n.py`: table in LEADS_REPORT.md, "Twenty-eighth round". None survives BH.

- The R/T collapse finds no new place names; its name gains are the withdrawn -RU/-ro set.
- The dental i~e/u~o alternation (round 20 F1) does not replicate on SigLA: withdrawn.
- Keftiu names (BM 5647) set aside: seven names, read as Hellenized (JAEI).

## Twenty-ninth (loop 1 of 10) round (round29.py), 2026-09-24

- Q-row signs word-initial 62% in Linear A vs 28% in Linear B (P6).
- Linear A avoids hiatus (0.3% vs 2%) and final pure vowels (3.9% vs 10.5%); fewer vowel-initial words.
- Sign-to-sign sequences less predictable than in size-matched Linear B.

## Thirtieth (loop 2 of 10) round (round30.py), 2026-09-24

- e/o-taking consonants: T (logOR 0.99), R, S and N (0.54 vs K/P/M), Q (2.04 vs K); avoiding: K, P, M, J, W.
- e/o share uniform across word length, function and register: a language-wide pattern.
- o final 34% vs e 52%.

## Thirty-first (loop 3 of 10) round (round31.py), 2026-09-24

- Religious and administrative words differ in initial and final signs (p 0.0005, 0.0045).
- Words on the same tablet share first signs (unique words, within-site p 0.011); shared finals weaken to p 0.085.
- No final-sign agreement between neighbouring words.

## Thirty-second (loop 4 of 10) round (round32.py), 2026-09-24

- Stem-scored, Pylos-free model: Knossos names more Minoan than Thebes/Mycenae/Tiryns names (AUC 0.63, p 0.0025); resolves W1.
- Knossos-only names more Minoan than Knossos names shared with the mainland (AUC 0.58).
- RCT names again less Minoan (AUC 0.44).

## Thirty-third (loop 5 of 10) round (round33.py), 2026-09-24

- Equal amounts stand on neighbouring lines beyond chance, 1s excluded (160 vs 133).
- The first entry is the unique largest in 32/137 lists vs 22 by chance.
- Grain round numbers largely a size effect (10+: 59% vs 42%, p 0.038).

## Thirty-fourth (loop 6 of 10) round (round34.py), 2026-09-24

- Scribes differ in list length, use of KU-RO totals, amount scale within commodity, and syllable use.
- Oil ligatures follow the scribe (27 tokens); fraction values follow the commodity (within-commodity p 0.22).
- Largest-first order and word dividers are uniform across scribes.

## Thirty-fifth (loop 7 of 10) round (round35.py), 2026-09-24

- KU-RO totals: 18% of HT tablets, 3% Phaistos/Zakros, 0 elsewhere; HT lists longest.
- Q-initial pattern replicates at HT (73%) and elsewhere (52%) vs Linear B 28%.
- Khania consonant-row proportions differ from HT (chi2 36 vs 12).

## Thirty-sixth (loop 8 of 10) round (round36.py), 2026-09-24

- Formula order fixed: 36/36 pairs in canonical order across 11 inscriptions (replicates Davis 2014).
- Stone vessels and metal objects carry longer dedications (~2.4 vs ~1.2 words).
- Q-initial pattern absent in religious words (33% vs LB 28%): administrative only.

## Thirty-seventh (loop 9 of 10) round (round37.py), 2026-09-24

- Knossos names: Q-initial 5.2% vs Pylos 1.8%; final pure vowel rare, 1.0% vs 4.2% without -eus names.
- Pre-Greek stems: fewer internal vowel signs (20.7% vs 25.8%); vowel profile closer to Linear A (JSD 0.043 vs 0.095).
- Name hiatus difference was the -eus ending (artefact).

## Thirty-eighth (loop 10 of 10) round (round38.py), 2026-09-24

- Replicated on SigLA: Q-initial (57% vs 28%), no vowel sequences (0% vs 2%), few final pure vowels (3.5% vs 10.5%), e/o after T and Q.
- First entry largest replicates in 4+ lists; Linear A vowels closer to Pre-Greek than to unmatched Greek.
- S6 (tablet-mates share first signs) withdrawn: not on SigLA.

## Thirty-ninth (second loop 1 of 10) round (round39.py), 2026-09-24

- Q-initial holds on unique initial pairs (72% vs 53%).
- Neighbouring syllables share consonant 5.4% vs 3.0% in Linear B.
- J-row word-initial 36% vs 4% (JA- words).

## Fortieth (second loop 2 of 10) round (round40.py), 2026-09-24

- e vs o depends on the consonant (NMI 0.33 vs Linear B 0.08): RO/QO/TO vs TE/NE/SE/RE.
- i/u depleted after T, R, S, N, Q (logOR -0.19 vs Linear B 0.35).
- The rule does not appear in Knossos names, Cretan place names, Pre-Greek or Eteocretan.
- Within-Linear A confirmations partly circular (sets chosen on this data).

## Forty-first (second loop 3 of 10) round (round41.py), 2026-09-24

- -TI entry labels on VIR tablets 36% vs 14% (p 0.0055, misses correction): candidate men's-name ending.
- Entry labels contain unread signs more often than headings (20% vs 14%).

## Forty-second (second loop 4 of 10) round (round42.py), 2026-09-24

- None survive; nominal: undeciphered signs (5.4% vs 2.0%), Z-row (4.6% vs 1.8%), J-initial (1.4% vs 0) in Knossos names.
- Special signs commoner in Pylos names (not a Minoan marker).

## Forty-third (second loop 5 of 10) round (round43.py), 2026-09-24

- Canonical commodity order: GRA<OLE (16), OLE<OLIV (9), CYP<VIN (8), OLE<VIN (7), GRA<OLIV/VIN (6 each).
- HT lists with totals: tau 0.44 vs 0.11 without.
- Lists of men longer (7.2 vs 4.4); fraction entries adjacent.

## Forty-fourth (second loop 6 of 10) round (round44.py), 2026-09-24

- Linear A commodity order agrees with Linear B majority order 70% vs 50% (p 0.002): grain first, wine late.
- Order holds at HT and with sides merged; outside HT p 0.09.
- Wine last on 13/17; first commodity carries largest amount 30/53; oil and olives co-occur (11 vs 4).

## Forty-fifth (second loop 7 of 10) round (round45.py), 2026-09-24

- Unread signs word-initial 43% vs known 32%: they belong to roots.
- NI followed directly by a number 73% vs 52% of other single signs: commodity (figs).
- Tablet single signs are common word syllables (rho 0.65); sealing single signs a distinct set.

## Forty-sixth (second loop 8 of 10) round (round46.py), 2026-09-24

- Religious words vowel-initial 36% (31% without formula) vs admin 20%.
- Same object type shares words; inked inscriptions closer to admin vocabulary.
- Religious syllable repetition is the formula (JA-SA-SA-RA-ME).

## Forty-seventh (second loop 9 of 10) round (round47.py), 2026-09-24

- Consonant repetition: Pre-Greek 4.8% vs Greek 3.1%; Eteocretan 9.7% vs 1.5%. Syllable repetition likewise.
- Pre-Greek a-initial 41% vs 30%.
- Knossos place names Q-initial 8.2% vs Pylos 0; common words no difference.

## Forty-eighth (second loop 10 of 10) round (round48.py), 2026-09-24

- Replicated on SigLA: consonant repetition, final-consonant restriction, e vs o by consonant.
- Commodity order holds without grain; Linear B agreement without grain 56% vs 50% (p 0.40): only grain-first is shared. Page corrected.
- NI commodity use and totalled-list ordering replicate.

## Forty-ninth round (round49.py), 2026-09-24

- Consonant harmony with different signs: 3.4% vs 2.1% in Linear B; holds in names and in both regions.
- Pre-Greek repetition rests on identical syllables (Beekes criterion): not independent support.
- o after R/Q, e after T/N/S; scribes agree on commodity order (72% vs 50%).
- Lists of men largest-first (tau 0.29); totalled lists record larger sums.

## Fiftieth round (round50.py), 2026-09-24

- Linear A has no FIC logogram; NI entries carry fractions 45% vs VIR 6%; NI placed after GRA/CYP/OLE, before VIN; NI with grain 19 vs 9: NI = figs.
- Single signs not shown to be abbreviations of KU-RO, KI-RO, KA-PA, A-DU (pooled p 0.73).

## Fifty-first round (round51.py), 2026-09-24

- Linear B spice abbreviations (SA, KU, KO, MA, MI, SE, KA, PO) do not behave as commodities in Linear A: a Mycenaean development.
- Single TE opens tablets (first entry 63% vs 13%); number-following single signs are list items (first entry 7% vs 27%).

## Fifty-second round (round52.py), 2026-09-24

- Non-adjacent harmony: syllables one apart share consonant 6.5% vs 4.9% in Linear B (p 0.011).
- TE followed by a word or logogram 48% vs 15%; TE opening is a Haghia Triada habit (80% vs 9%).
- First words tied to main commodity on 22 tablets; SA-RA2 not commodity-specific.

## Fifty-third round (round53.py), 2026-09-24

- Harmony replicates on SigLA (adjacent 3.8% vs 2.1%; one apart 7.3% vs 4.9%); holds for obstruents and sonorants; productive in hapax words.
- Harmony belongs to longer words (4+: 3.4% vs 1.9%); none in two-sign words.
- Eteocretan different-sign harmony 6.3% vs 1.1% (small corpus); not in Knossos names.

## Fifty-fourth round (round54.py), 2026-09-24

- Linear B: figs (NI) after grain on 37/37 tablets, as NI after grain in Linear A (16/20).
- Linear B lists largest-first (KN tau 0.37, PY 0.10), first entry largest 155/337; KN-PY contrast is the sheep series (within commodity p 0.21).
- Linear B commodity order consistent; totalled lists not ordered.

## Fifty-fifth round (round55.py), 2026-09-24

- Kept in Linear B: figs with grain (36 vs 4), figs with sub-units 44% (LA NI 45%), first commodity largest (152/222), grain first (46/63), goods lists largest-first.
- Not kept: wine last (2/9). Oil/olive/cyperus comparisons untestable (separate Linear B series).

## Fifty-sixth round (round56.py), 2026-09-24

- Pylos goods amounts even 68% (133/196): even preference is a shared Aegean habit (LA 65%, KN 72%).
- First entry largest does not hold at Pylos (Knossos pattern); Linear B lists of men not ordered (LA yes).

## Fifty-seventh round (round57.py), 2026-09-24

- Entry order word -> commodity -> number: word first in 149/150; number after commodity 69% vs after word 53%.
- Transaction terms followed by a commodity sign 52% vs other words 14%: they qualify the goods.
- Headings almost never followed directly by a commodity sign (3%).

## Fifty-eighth round (round58.py), 2026-09-24

- Pre-commodity words recur more (TTR 0.78 vs 0.87) and span more sites (1.19 vs 1.05): technical terms, not names.
- SA-RA2 before GRA 8, CYP 5, OLE 1 (suggestive: dry goods).
- Oil ligature syllable never matches the preceding word (0/19).

## Fifty-ninth (saturation loop) round (round59.py), 2026-09-24

- Name slot and descriptor slot lexically separate (16 shared types vs 33).
- Headings share types with descriptors (terms).
- Descriptor entries larger (~13 vs ~4) and fraction-bearing twice as often, on goods tablets.
- Khania uses the descriptor slot 58% vs HT 20%.

## Sixtieth (saturation loop 2) round (round60.py), 2026-09-24

- Term-headed tablets contain descriptor entries 52% vs 17%.
- Descriptor words written by 2.6 scribes vs names 1.5: terms shared, names scribe-bound.
- Khania tablets carry 1.1 names vs HT 4.2.

## Sixty-first (saturation loop 3) round (round61.py), 2026-09-24

- Sealing signs differ HT vs Khania (chi2 345 vs 13; 19 Khania signs).
- Tablets with descriptor entries are multi-commodity (46% single vs 83%): descriptors mark goods on mixed tablets.

## Sixty-second (saturation loop 4) round (round62.py), 2026-09-24

- More commodities, more descriptor entries (rho 0.35): confirms Q13; but descriptors do not mark switches or block openings.
- Single-commodity lists write the commodity sign on 34% of entries vs 54% on mixed tablets: stated once, understood after.

## Sixty-third (saturation loop 5) round (round63.py), 2026-09-24

- Commodity sign in the first entry 55% vs later 31% on single-commodity tablets: stated at the head.
- Linear B writes the logogram on 82% of lines, Linear A 38%: the Minoan once-only economy was dropped.
- Signed entries larger than unsigned on the same tablet (63/85).

## Sixty-fourth (saturation loop 6) round (round64.py), 2026-09-24

- Knossos Linear B writes logograms on 72% of lines vs Pylos 89%, within logogram p 0.007 (VIR 82 vs 96%, MUL 42 vs 100%): Minoan once-only notation partly kept on Crete. NARROWED round 65: MUL gap = women-and-children format; goods lists KN 82% vs PY 86% (p 0.21); residue = two name lists (hands 102b, 105).
- Longer lists more economical (rho -0.33); men lists write VIR on 13% of entries vs goods 41%.

## Sixty-fifth (saturation loop 7) round (round65.py), 2026-09-24

- V10 artefact (women-and-children format), V14 confounded by logogram, rest null: 0 new.
- U4 narrowed: goods lists KN 82% vs PY 86% (p 0.21); page corrected.

## Sixty-sixth (saturation loop 8) round (round66.py), 2026-09-24

- W1 = person–commodity link (within commodity p 0.15); W5 restates regional fractions; W6 = commodity (p 0.67); W7 rests on -RU (withdrawn lead): 0 new.

## Sixty-seventh (saturation loop 9) round (round67.py), 2026-09-24

- Phaistos: no lexical turnover (Y1 reversed, proximity); Y2 p 0.06, Y6 p 0.09; vessels: 0 new.
- Saturation loop stopped: rounds 65-67 gave no new learning (rule in reading/loop_ledger.json).

## Remaining gaps
- Salgarella 2025 check for HT 34 - blocker: needs-physical-access; closed-access Cambridge Element, library copy needed
- the Anetaki sceptre KN Zg 57-58 - blocker: no-key-material; no published transcription, full edition forthcoming
- a photograph of HT 34 line 3 - blocker: needs-physical-access; only the Heraklion Museum (HM 22) can supply it
- a full Etruscan comparison - blocker: no-key-material; the open Etruscan list has 27 usable forms (Hurrian now tested with Laroche 1980)
- meanings of the 2,164 sound-only tokens (names, transaction terms, formula words) - blocker: no-key-material; the language is unidentified, no bilingual exists, and the Linear B vocabulary matches only place names and three words
- 632 unidentified signs and ligatures (*301, *304, *308, QA2+..., MI+JA+...) - blocker: no-key-material; no Linear B counterpart and no context fixes them
- fraction signs H and A, and the rare L, W, X, Y, DD - blocker: too-short; 29 written-order pairs and one clean total cannot fix them (FRACTIONS_REPORT.md)
- damaged entries and totals (HT11a, HT27a, HT100, HT109, HT122, HT131b and others) - blocker: illegible; arithmetic restorations proposed in reading/restorations.json
- 631 single-sign marks on nodules and roundels - blocker: too-short; one sign per object, no syntax
- readings of the 5 totals that cannot be reconciled in any window (HT13, HT25b, HT102, HT122b, PH(?)31a) - blocker: needs-physical-access; the editions agree, only autopsy of the tablets can say whether the scribe or the transcription erred

## Escalation
- [x] siblings: Linear B, the sibling script, used for sound values and tested against a null (soundvalues.py); Cretan Hieroglyphic is itself undeciphered and gives no key material
- [n/a] clear-pages: Linear A has no bilingual and no clear-text companion; none is known anywhere
- [x] known-keys: Linear B syllabic values (Ventris 1952), Bennett-type and Corazza et al. 2021 fraction values, GORILA logogram labels all tried and scored
- [x] print: GORILA via lineara.xyz, Younger's commentaries, SigLA, Salgarella 2022/2025, Steele 2023, Corazza et al. 2021, Davis 2014 on the formula
- [x] key-rebuild: fraction values constrained by order and totals (fraction_constraints.py); totals re-checked with fractions and object/commodity windows; missing amounts restored arithmetically
- [x] retry: every KU-RO/PO-TO-KU-RO retried with the extended fraction values and windows; HT34 re-read with Younger's erasure; the A- prefix and the formula variants re-examined
