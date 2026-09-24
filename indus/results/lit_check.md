# Literature check: have our Indus findings been published before?

Checked 23 Sept 2026, without logging in anywhere. Sources: Parpola 1994 (good English OCR from archive.org
`nkzf_deciphering-the-indus-script-by-asko-parpola-1994-...`; the scratchpad `p94/p94.txt` is Devanagari-OCR garbage,
and the page images `p94/ch6_112.png`, `ch6_113.png` were read for pp. 94-95), Fairservis 1992 OCR, Mahadevan's
harappa.com essays, open PDFs (PLOS ONE, Nature HSSC, arXiv), and web search abstracts. Parpola 1994 page numbers
are the printed ones. We could not see these, and they may hold more: Wells 2011 and 2015 (only the 2015 front
matter), Fuls 2013/2015/2020 (abstracts only), Mahadevan 1970/1986/2014, Parpola 2008 and 2015 (the Helsinki PDF and
the archive.org OCR both failed), and Kenoyer 2020 (harappa.com started refusing requests partway through the session).

Verdict key: **published** = the same claim is in print; **partly** = the idea is in print but not our measurement or
not our framing; **not found** = we found no earlier statement in the sources searched, which does not prove it is new.

| # | finding | verdict | nearest prior work | what is ours |
|---|---|---|---|---|
| F1 | 740/520 mutually exclusive; the choice is fixed per stem, like a gender/class suffix | partly | Parpola 1994 p. 94 (mutually exclusive; he says they alternate); Mahadevan, "The Arrow Sign in the Indus Script" (harappa.com, c. 1998) pp. 2, 4 (most preceding sequences exclusive, so gender: 520 = non-masc. *-(a)mpu, 740 = masc. *-(a)nru); Knorozov et al. 1981 via Parpola 1994 p. 96 (*-an masc.) | the measurement: 5 of 881 stems take both vs ~46 by chance. No count or baseline found anywhere |
| F2 | 520 restricted to a closed class: fish-final names (61%) + long-3 unit; human/object/plant stems take 740 | partly | Parpola 1994 p. 94 fig. 6.6 (fish+jar vs fish+arrow sequences; 'man' etc. only after fish+jar); Mahadevan c. 1998 p. 2 (fish+arrow pair closely bound); Mukhopadhyay 2019 fig. 9c (fish-like signs have a special affinity for M77 211) | the class split by what the last sign depicts, with rates and p-values; the long-3+520 unit; the persons vs stars reading |
| F3 | 'X-jar man' = possessor before head, against Sumerian/Elamite; + class-suffix test against Munda/Burushaski → only Dravidian passes | partly | Parpola 1994 pp. 86-89, 95-97, 125, 130 (Num+N, premodification, genitive before 'man', U never dropped before 'man'; Sumerian, Semitic, Hurrian, Elamite and Tibeto-Burman excluded on word order) | the second test (noun-class suffix) and the two-test elimination table; Parpola dismisses Munda and Burushaski on other grounds |
| F4 | opener formula 817/820/861 + stroke pair is one formula; variant depends on site and object type | partly | Parpola 1994 pp. 90-91 (position I phrase: 7 alternating initial signs closed by one or two short strokes); Yadav et al. 2010 PLoS ONE 5(3):e9506 (beginners M77 267/391/293 followed by 99/123); Wells 2011, 2015 p. 2 (sign inventories differ by site and object type) | the measured dependence of the opener variant on site and object type (permutation p < 0.001), and that it does not depend on the following name |
| F5 | short vs long strokes = two numeral systems (cf. Proto-Elamite counting vs capacity); long strokes + pot on tablets = capacity; Harappa tablets as tokens; numerals do not follow the weight system | partly (mostly published) | Parpola 1994 pp. 82, 107 (long strokes counted only on the early tablets and otherwise mean something else; 0-4 strokes + U pot on tablets = counted pots, votive); Wells 2015 ch. 4 (V+# texts on tablets = volumetric system, U ≈ 40 l); Rao 2018, Kenoyer felicitation volume (arXiv 1812.00049: tablets as ration tokens, compared with Proto-Elamite/proto-cuneiform); Meadow & Kenoyer 2000; Mukhopadhyay 2019, 2023; Fuls 2020 (different bases for long and short strokes); Bonta 2010 (fish signs = weight units) | the explicit counting-vs-capacity pairing with Proto-Elamite, and a test of the numerals against the Harappan weight ratios (not found) |
| F6 | only 6+fish (Pleiades) is statistically supported; Tamil 3/5/7 not enriched before fish | not found (as a test) | Parpola 1994 pp. 194-195 (numbers before fish restricted to 3, 4, 6, 7; 6+fish commonest = aru-min; 3+fish next = mu-m-min; 7+fish = elu-min); Mukhopadhyay 2023 (Supp. §2) disputes the readings on other grounds | the enrichment test against numeral base rates; it contradicts Parpola's 3+fish claim |
| F7 | unsupervised segmentation recovers the opener formula and binds terminals as suffixes | partly | Knorozov 1968/1981 blocks ('variables' = suffixes; Parpola 1994 pp. 95-96); Koskenniemi, Koskenniemi & Parpola (Parpola 1994 §6.4); Yadav et al. 2008 IJDL 37: 53-72 ("Segmentation of Indus texts"); Fuls 2015 App. I (automated segmentation trees); Nair 2026 arXiv 2604.17828 | a model-based segmenter that finds the formula unaided (95% boundary after the opener vs 52% elsewhere) and with a shuffled control |
| F8 | shuffled-key control for proposed keys, validated on Linear Elamite; consonant-skeleton scoring blind to a correct key; fitted keys generalise in any language | partly | Raghavendra 2026 arXiv 2608.02999 (Aug 2026: on a non-linguistic emblem corpus a Yajnadevam-style decoder reaches 61-74% held-out coverage in English, Sanskrit and Tamil; random-key and fixed-key shuffled controls; unstable keys); Sproat 2014 Language 90(2); Farmer, Sproat & Witzel 2004 | the key-vs-its-own-shuffle test, the Linear Elamite positive control, the consonant-skeleton result, and running it on the Indus corpus itself |
| F9 | copper-tablet sign = image equations; new anchors 347 = multi-headed animal, 460 = tree tablets | equations published; anchors not found | Parpola 1994 pp. 107-112, fig. 7.14 (46 groups; the same obverse text links an image on one group to a single sign on another; the motif and the sign name the same deity), pp. 233-234 (horned archer = ligature 47); Parpola 2008 (During Caspers vol.; not read); Wells 2015 fig. 6.1 (the hare replacement set) | the 347 and 460 candidates (347 rests on one text on 8 moulded copies) |
| F10 | late bar seals (Harappa 3C) use fewer arrow-ending fish names | not found | Kenoyer 2020 and Mukhopadhyay 2023 (later seals keep the same initial and terminal signs, with longer cores); Kenoyer & Meadow on bar-seal chronology | the whole finding |

## Notes, finding by finding

### F1. Jar (740) and arrow (520) are mutually exclusive, and the choice is fixed per stem

- Parpola 1994, *Deciphering the Indus Script*, §6.3, p. 94: the jar and the arrow (drawn as an upright arrow on the
  page image) are Parpola's pair of likely inflectional suffixes. They are mutually exclusive, one never directly
  before or after the other, and they alternate after many recurring sequences. The Finnish team read them as case endings in 1969
  (Parpola et al. 1969a: 18-23; 1969b: 6-8; fig. 6.8) and dropped that paradigm. Parpola's statement points the other
  way from our result: he speaks of alternation after recurring sequences, where we find that a stem almost never takes both.
- Parpola 1994 pp. 95-96: the Soviet team (Knorozov 1968; Knorozov et al. 1981) read one terminal sign as the
  Proto-Dravidian masculine suffix *-an inside a case paradigm (fig. 6.9). Parpola rejects the paradigm.
- Mahadevan, "The Arrow Sign in the Indus Script" (harappa.com essay, 5 pp.; the insight dates from August 1995,
  and the essay is usually cited as 1998/1999). p. 2: most but not all of the sequences before the jar and the arrow
  are mutually exclusive, so they are not case endings (case endings attach to the same nouns in different contexts). They are person-
  number-gender suffixes: arrow = non-masculine singular *-(a)mp(u) (Old Telugu -(a)mbu). p. 4: jar = masculine singular
  *-(a)nru. Mahadevan says the same in his harappa.com interview ("The Indus Arrow and 'Harrow' Sign"): the two are
  generally mutually exclusive, and where one occurs after a name the other never does.
- **Verdict: partly published.** The idea that the choice is fixed per name and so marks gender or class is Mahadevan's,
  stated as a qualitative observation. We found no count of stems taking both endings (our 5 of 881 against about 46
  expected by chance) and no shuffle baseline in Parpola 1994, in Mahadevan's essay, or in any statistical paper
  searched. Ours is the first measurement we found. It also settles the disagreement between Parpola ('alternate') and
  Mahadevan ('mutually exclusive before the same sequences') in Mahadevan's favour.

### F2. The arrow ending belongs to a small closed class

- Parpola 1994 p. 94, fig. 6.6 (checked on the page image): Parpola tabulates what follows 'fish + jar' (or zero)
  sequences and what follows 'fish + arrow' sequences. The 'man' sign and other framed signs follow only fish + jar;
  another group follows both. He sets fish + arrow up as its own category but does not say the arrow is confined to fish names.
- Mahadevan c. 1998, p. 2: the two endings are bound more tightly to the signs before them than case endings would
  be, and he gives the fish + arrow pair as his example.
- Ansumali Mukhopadhyay 2019, "Interrogating Indus inscriptions to unravel their mechanisms of meaning conveyance",
  *Palgrave Communications* 5: 73, fig. 9c: signs she calls fish-like (M77 65, 67, 70, 72) show a special
  affinity for the arrow (M77 211), and pincer-like signs for another phrase-final sign. The pairing is shown by examples, without rates.
- **Verdict: partly published.** The fish-arrow affinity has been noticed three times. The closed-class result is ours:
  fish-final names take 520 61% of the time and long-3 takes it 56 of 63 times, while human, object, plant, landscape
  and sky signs take it in 24 of 754 lines. So is the reading that the referent of the last sign decides the class.

### F3. 'X-jar man' word order, and Dravidian as the only family that passes both tests

- Parpola 1994 §6.1, pp. 86-89: the numeral stands before the counted noun (Num + N) wherever it occurs inside a longer
  text. Typology suggests Adj + N as well. Edzard's 1990 objection (in Sumerian accounts numerals are written before
  the noun, against the spoken order) does not apply to seal texts.
- Parpola 1994 p. 95 (page image): the jar is never dropped before the terminal 'man' sign. A plain 'man' needs a closer
  specification, perhaps a genitive attribute, and that construction requires the jar. pp. 96-97: if the language prefers
  premodification, genitives stand before their heads. The jar may be a genitive or possessive marker (South Dravidian
  possessive utai-).
- Parpola 1994 p. 125: the language prefers premodification, which excludes Tibeto-Burman (N + Num). p. 130: Semitic,
  Sumerian and Hurrian put adjective and genitive attributes after the head, so they differ from the Indus order. In
  Elamite the attribute carries the head's class suffix. Munda and Burushaski are discussed in ch. 8 (pp. 137-142) on
  historical and areal grounds, not tested grammatically.
- Also relevant, but not read: Wells 2015 ch. 6 compares Dravidian morphology and syntax with the Indus texts; Fuls 2015
  App. III classifies the Indus language type; Mahadevan 2014, "Dravidian Proof of the Indus Script via the Rig Veda".
- **Verdict: partly published.** The possessor-before-head argument against Sumerian, Semitic and Elamite is Parpola's
  (1994), built on the same jar-before-'man' construction. We have not found the second half: a noun-class suffix test,
  applied against Munda and Burushaski, that leaves Dravidian as the only family passing both tests. Mahadevan's gender
  reading (F1) comes closest.

### F4. The opener formula

- Parpola 1994 pp. 90-91: a position I phrase usually starts the text and often has just two signs. Seven diagnostic
  initial signs alternate there, and the phrase ends in one of two sets, one or two short strokes (set 1) or jar ligatures
  (set 2). Parpola treats the short strokes as markers the position I structure requires.
- Yadav, Joglekar, Rao, Vahia, Adhikari & Mahadevan 2010, "Statistical analysis of the Indus script using n-grams",
  *PLoS ONE* 5(3): e9506: the three commonest text beginners (M77 267, 391, 293) are selective about what follows, and
  M77 99 and 123 most often follow them. These are almost certainly our 861/820/817 + stroke pair. The paper
  explicitly ignores site, stratigraphy and object type.
- Wells 2011, *Epigraphic Approaches to Indus Writing*, and Wells 2015, *The Archaeology and Epigraphy of Indus
  Writing*, p. 2: sign inventories differ by site and by artifact type (e.g. sign 400 is mostly on Harappa miniature
  tablets). Wells 2015 fig. 6.4: the position of sign 820 differs between text classes. Fuls (2013, 2015 App. II):
  positional preferences shift with text class.
- **Verdict: partly published.** The formula itself is Parpola's 1994 position I phrase, and Yadav et al. 2010 count it.
  We did not find the claim that it is one formula whose variant is chosen by site and object type (and not by the
  following name), or any test of that.

### F5. Two stroke systems, capacity on tablets, tokens, weights

- Parpola 1994 p. 82: repeated long strokes are numbers only in the early texts (the Harappa miniature tablets). In the
  mature script units are written with short strokes, whose count varies before particular signs such as the jar, while
  the long strokes mean something else and occur mostly in a few fixed sequences. p. 107: many tablets show 0-4 strokes
  before the U-shaped pot sign, read as counted pots (votive offerings; figs. 7.9-7.12).
- Wells 2015, ch. 4, "Tablets, Pots and the Volumetric System of Harappa" (the V+# texts on Harappa tablets), as
  reported by Rao 2018: the U sign is a volumetric measure of about 40 litres.
- Rao 2018, "The Indus Script and Economics: A Role for Indus Seals and Tablets in Rationing and Administration of
  Labor", in *Walking with the Unicorn* (Kenoyer felicitation volume; arXiv 1812.00049): the Meadow & Kenoyer 2000
  Harappa tablets were ration tokens, like Proto-Elamite and proto-cuneiform ration tablets (numeral + measure/commodity).
- Ansumali Mukhopadhyay 2019 (above): long and short strokes form 22 numeral signs, with a separate metrological
  class, and the repetition compared to Proto-Elamite cumulative-additive notation. Mukhopadhyay 2023, *HSSC* 10
  (s41599-023-02320-7): 2, 3, 4 or 6 long strokes + rimless jar on two-sided tablets, read as license-fee slabs rather
  than transaction quantities.
- Fuls 2020, "Ancient Writing and Modern Technologies: Structural Analysis of Numerical Indus Inscriptions", *Studies on
  Indus Script* (National Fund for Mohenjodaro): 57-90. Abstract only: long and short strokes carry different bases or
  units. Bonta 2010: fish signs = weight units (minas).
- **Verdict: mostly published, in pieces.** Parpola separates short from long strokes functionally. Wells, Rao and
  Mukhopadhyay treat long strokes + pot on tablets as a volume or quantity. Meadow & Kenoyer and Rao treat the tablets as
  tokens and compare them with Proto-Elamite. Two things we did not find: the framing as two numeral systems that
  precede different signs, set against the Proto-Elamite counting and capacity systems (Rao compares formats, not systems),
  and a test showing the numerals do not follow the Harappan weight ratios. Bonta's weight reading goes against the second.

### F6. Numeral + fish star names

- Parpola 1994 pp. 194-195: the numbers attested before the fish are restricted to 3, 4, 6 and 7. 6 + fish, the commonest,
  = Old Tamil aru-min (the Pleiades); 3 + fish, next in frequency, = mu-m-min (Mrgasirsa); 7 + fish = elu-min (Ursa
  Major). He rejects Kinnier Wilson's 1987 reading of fish rations.
- Mukhopadhyay 2023 (Supplementary §2) argues against these readings from script-internal patterns, but runs no
  enrichment test.
- **Verdict: not found as a test.** No one appears to have tested which numeral + fish pairs occur more than the
  numeral base rates predict. Our result backs Parpola on 6 + fish and goes against him on 3 + fish.

### F7. Segmentation

- Knorozov et al. (1968-81), summarised in Parpola 1994 pp. 95-96: texts divided into blocks of constants,
  semivariables and variables, with the variables (the terminal signs) as gender and case suffixes. Parpola 1994 §5.3
  (segmentation) and §6.4 (the Koskenniemi, Koskenniemi & Parpola computer grammar).
- Yadav, Vahia, Mahadevan & Joglekar 2008, "Segmentation of Indus texts", *IJDL* 37: 53-72: frequent n-grams segment 88% of
  texts. Fuls 2015, Wells 2015 App. I: automated multivariate segmentation trees. Nair 2026 (arXiv 2604.17828)
  replicates a statistical segmentation.
- **Verdict: partly published.** Frequency-based and hand segmentations already isolate the opening phrase and treat the
  terminal signs as bound morphemes. What we add is an unsupervised model that recovers both unaided, with a sign-shuffle control.

### F8. Testing decipherment keys

- Raghavendra 2026, "On the Non-Specificity of Statistical Measures Used in Script Decipherment", arXiv 2608.02999
  (August 2026): on a purpose-built non-linguistic emblem corpus, a reconstruction of the Yajnadevam 2024 Sanskrit method reaches
  high coverage in English, Sanskrit and Tamil. Grouped held-out coverage stays at 61-74%, random keys and fixed-key
  shuffles are the controls, and bootstrap keys agree on only 9% of sign values. It is the closest prior work to our
  "fitted keys generalise in any language".
- Sproat 2014, "A statistical comparison of written language and nonlinguistic symbol systems", *Language* 90(2);
  Farmer, Sproat & Witzel 2004, *EJVS* 11(2): the statistical measures do not tell language from non-language.
  Nair 2026 (arXiv 2604.17828): non-linguistic baselines.
- **Verdict: partly published, and very recently.** The point that dictionary coverage and held-out fit do not identify a
  key was made one month ago by Raghavendra (2026), on a synthetic corpus. We did not find: testing a key against
  shuffled versions of itself, a Linear Elamite positive control, the result that consonant-skeleton scoring cannot
  detect even a correct key, or the generalisation test on the real Indus corpus. Our profile.json should record the
  date for the contamination question.

### F9. Copper tablets and new anchors

- Parpola 1994 pp. 109-112, fig. 7.14: 46 prototype groups. An identical obverse inscription links an iconographic
  motif on the reverse of one group (A2, B1, B5, B7, B9, B10, B19) with an inscription on the reverse of another (C4, C1,
  A11, C2, C5, A7, C6). That inscription is usually a single pictogram, and one sign (C5/C6) goes with two motifs,
  the markhor and the horned archer. Motif and sign seem to denote the same deity. pp. 233-234: ligature 47 = the
  horned archer. Our `copper.md` T1 equations are these links, redrawn.
- Parpola 2008, "Copper tablets from Mohenjo-daro and the study of the Indus script" (During Caspers memorial volume):
  the full study, not read (the Helsinki repository asks for cookies). Wells 2015 fig. 6.1: the 'hare eating grass'
  replacement set.
- 347 (multi-headed animal moulded tablets) and 460 (tree tablets): no earlier proposal found. Parpola 1994 p. 218 fig.
  12.9 describes M-489 with a three-headed animal but does not equate it with a sign.
- **Verdict: the equations are published (Parpola 1994, 2008); the two anchors were not found.** 347 rests on one text in 8
  moulded copies plus one seal, so it is one data point, not eight.

### F10. Late bar seals

- Kenoyer 2020, "Origin and development of the Indus script: insights from Harappa and other sites" (as reported by
  Mukhopadhyay 2023): inscriptions get longer over time, while initial and terminal signs stay the same. We found
  nothing on the fish + arrow share in Period 3C or on bar seals.
- **Verdict: not found.**

## Sources we could reach

- Parpola 1994, CUP: archive.org `nkzf_deciphering-the-indus-script-by-asko-parpola-1994-new-york-cambridge-university-press` (_djvu.txt).
- Mahadevan, "The Arrow Sign in the Indus Script": harappa.com/arrow/1.html to 5 (pages 1-5); interview: harappa.com/content/arrow-sign.
- Yadav et al. 2010: journals.plos.org/plosone/article?id=10.1371/journal.pone.0009506.
- Ansumali Mukhopadhyay 2019: doi 10.1057/s41599-019-0274-1; 2023: nature.com/articles/s41599-023-02320-7.
- Rao 2018: arxiv.org/abs/1812.00049. Nair 2026: arxiv.org/abs/2604.17828. Raghavendra 2026: arxiv.org/abs/2608.02999.
- Wells 2015 front matter: archaeopress.com sample PDF 9781784910464. Fuls publication list: epigraphica.de/indus/menueindus.htm.

## Second pass (full texts)

Checked 23-24 Sept 2026, no logins. Texts saved in the session scratchpad `lit2/`. Numbering in this section follows
the second-pass brief, which differs from the table above:
F1 jar/arrow fixed per name (measured); F2 arrow = closed class of fish-final names; F3 head-final 'X-jar man' +
noun-class-suffix test leaving only Dravidian; F4 heading-formula variant depends on site and object type; F5 short
vs long stroke numerals as two systems (counting vs capacity, Proto-Elamite), numerals not following the weights,
Harappa tablets as tokens; F6 numeral + fish enrichment test (only 6 + fish); F7 unsupervised segmentation binding
terminals as suffixes; F8 foreign names on Gulf/West Asian seals omit the Indus endings (quantified); F9 grammar stable
over periods while numeral use changes; F10 restoring broken texts from grammar, scored on intact duplicates;
F11 a decipherment-evaluation test validated on a real decipherment.

### Mahadevan 1986, "Towards a grammar of the Indus texts: 'intelligible to the eye, if not to the ears'", *Tamil Civilization* 4(3-4): 15-30

Full text read (OCR text layer of the RMRL digital-library flipbook, rmrl.in, id `Towards a grammar of the Indus
texts_1986b`; printed page = flipbook page + 14).

- p. 21 (rule III.2): signs split into root morphemes (406 signs, mean frequency 25) and suffixes (10 basic signs,
  3 ligatures, 1 modifier; mean frequency 250), from positional statistics. p. 21 rule 4: attributes, numerals
  included, precede the substantive. **F3 (order half), F7 (qualitative).**
- pp. 21-23 (rule 5): the three superscript short-stroke signs (M77 87, 99, 123) are case markers closing the
  'introductory' phrase. The choice among them is governed by the preceding substantive: some substantives take any
  of the three, some only two, some only one. He reads the introductory phrase as a place name (palace/temple, city,
  crossroads) + locative/genitive marker. **F4: the nearest earlier statement, and it points the other way** — the
  variant is said to depend on the preceding sign, not on site or object type. No test by site or object.
- p. 24 (rule 6): the script distinguishes long from short vertical strokes, and upper- from middle-register short
  strokes, in meaning and function; initial short strokes are numerals or variants of long strokes. **F5 (partly):
  two stroke classes named, but not as two numeral systems, and no Proto-Elamite or capacity reading.**
- pp. 24-26 (rule 7): the five frequent terminal signs (jar, arrow and others) are *not* number/gender/case morphs
  but nominal suffixes in name formation (after Hunter 1934), themselves substantive ideograms; they attach only to
  personal nouns. The chart (p. 28) puts jar (M77 342) and arrow (M77 211) together in class C, 'primary nominal
  suffixes'. **F1: no statement that the choice is fixed per stem; at this date Mahadevan rejects the gender reading
  he adopted in 1998.** pp. 25-26 (rule 8): the four-stroke enclosure replaces the nominal suffix (plural marker).
- p. 27 (rule 9): text = optional introductory phrase (attribute + substantive + case marker) + substantive phrase
  (attributes + substantive + 1-3 nominal suffixes). **F7: the same segmentation, by hand.**
- Nothing on F2, F6, F8, F9, F10, F11.

### Rao (Mythili R.) & Mahadevan 1987, "Archaeological context of Indus texts at Mohenjodaro", *Journal of the Institute of Asian Studies* (Madras), c. pp. 26-56

Full text read (RMRL flipbook `Archaeological context of Indus texts at Mohenjodaro_1987`; conference paper of June 1985).

- p. 34 (result 3.i-iii) and Statements 6 and 8: the 18 commonest sign pairs, including the opener pairs M77
  267-099, 391-099 and 293-123, tabulated by locus, level and object type at Mohenjo-daro. Some pairs are much
  rarer at Mohenjo-daro than at Harappa; the two commonest terminal pairs are rarer on seals and commoner on sealings
  and ivory rods, and absent from copper tablets. p. 35 (iv): some pairs are over-represented on copper tablets.
  p. 36 (conclusion i): one sign's apparent site preference is really an object-type preference.
  **F4: partly anticipated as description** — pair frequencies vary with site and object type, and object type is
  separated from site for one sign. No statement that the opener formula's variant is chosen by site and object type,
  and no test.
- p. 35 (result 3.vi): no significant change in the relative frequencies of the frequent sign pairs across the Early,
  Middle and Late periods of DK-G, which they take as confirming the stability of language and script at
  Mohenjo-daro. **F9: the stability half is stated here (Mohenjo-daro only, frequent pairs, no numeral analysis).**
- p. 37 (conclusion iv): the distribution of the jar, arrow and related terminals does not support reading them as
  number, gender or case suffixes (promised a separate paper). **F1: contrary to the gender reading; no count.**

### Mahadevan 1970, "Dravidian parallels in proto-Indian script", *Journal of Tamil Studies* 2(1) (separately paginated reprint, 1-c. 120)

Full text read (RMRL flipbook `Dravidian Parallels in Proto Indian Script_1970`; printed page = flipbook page - 4).
The same passages recur in "Method of parallelisms" (1973, RMRL), §3.1.

- p. 18 (§1.23): **Hunter (1934) had already claimed that the sequences before the jar and before the arrow are
  mutually exclusive**; Mahadevan says Hunter was mistaken, since several sequences (he cites a fish pair) take either.
  p. 20 (§1.28): the shared preceding sequences make it unlikely the two mark mutually exclusive grammatical
  categories, and the fish signs, which take the arrow often, are unlikely to be feminine. p. 20 (§1.29): counts of
  blocks ending in each sign (Kondratov 146 vs 48; Finnish 873 vs 146 occurrences). **F1: the claim is Hunter's
  (1934, qualitative) and was disputed in 1970; Mahadevan reversed himself by 1998. Nobody counted stems taking both.**
- p. 22 (§1.40): the arrow "occurs mostly" in the fish + arrow digram and with the other fish signs; p. 26 (§2.8):
  jar or arrow is almost always added to fish signs. The 1973 version (§3.1) adds that the fish signs take the arrow
  more often than the jar. **F2: the fish-arrow association is stated plainly here (qualitative, no rates); the
  closed-class claim — that non-fish stems almost never take the arrow — is not.**
- pp. 29-30 (§2.17-2.20): numerals before fish: a constant numeral in a block is a homophone, a variable one a true
  number; the numbered fish are phratry numbers (4, 6, 7), not constellations; the long-stroke 3 + fish is a special
  case. **F6: a reading of the same pairs, no enrichment test.**
- pp. 43-46 (§3.1-3.6): the three 'introductory' signs (about 15% of inscriptions) with their stroke suffixes are
  place names (Temple, Citadel, City) + locative/possessive; the choice of stroke depends on the introductory sign
  (p. 45: one of the three never takes a given stroke). **p. 46 (§3.6): he rules out one sign per city because "the
  proportion of the occurrences of these symbols is approximately the same on the seals recovered from various
  sites".** **F4: an explicit earlier claim of *no* site dependence (qualitative, seals only). Our measured site and
  object-type dependence contradicts it.**
- p. 71 (§5.2-5.3): the 'cup' sign on Harappa votive tablets is preceded by one to four long strokes; he rejects
  counts of offerings (the number never exceeds four) and reads phratry numbers. **F5: the Harappa tablet
  long-stroke + cup texts are discussed but read as clan numbers, not capacity or tokens.**
- pp. 61-62 (§4.24-4.26): numerals + hand signs; earlier readings as measures or ordinals rejected.

### Mahadevan 1982, "Terminal ideograms in the Indus script", in Possehl (ed.), *Harappan Civilization*, 311-317

Read (RMRL flipbook). p. 311, point 4: the frequent terminal signs are "too closely related to their antecedent signs"
in all contexts to be case endings; the relation is semantic, not grammatical. Point 6: the language is not Sumerian
or West Asian, which put the attribute after the substantive; numerals before the counted noun prove the reverse
order. **F1 (qualitative per-stem binding, read as semantic), F3 (the order half only).**

### Mahadevan 1998, "Phonetic value of the 'arrow' sign in the Indus script", *Journal of the Institute of Asian Studies* 15(2)

Read (RMRL flipbook); the same text as the harappa.com essay reported in the first pass. p. 70: most, not all,
sequences before jar and arrow are mutually exclusive, so they are not case markers. Adds nothing to the first pass.

### Ganesan, Subramanian, Suresh Babu & Mahadevan 2010, "The Indus script: text and context. A statistical-positional analysis of significant text segments" (World Classical Tamil Conference, Coimbatore)

Full text read (RMRL flipbook). pp. 3-4 (§6.1-6.2): sign frequencies by site and by object type; for signs that
look site-specific, object type is the main cause (miniature tablets at Harappa); copper tablets only at
Mohenjo-daro. p. 5 (§7.1.2): the commonest initial pair is mostly on seals and sealings, never on copper tablets, with
an affinity to Mohenjo-daro and the unicorn; the commonest final pair is mostly on miniature tablets and sealings,
with an affinity to Harappa. §7.1.7: text segments have no special affinity to field symbols, except on copper tablets.
**F4: the closest descriptive precedent** — they show one opener pair's affinity to site and object type, and
separate site from object type. They do not treat the opener as one formula whose variant is chosen by site and object
type, run no test, and do not check independence from the following name. No stratigraphy (§5.3), so nothing on F9.

### Parpola 2008, "Is the Indus script indeed not a writing system?", in *Airāvati* (Mahadevan felicitation volume), Chennai: Varalaaru.com, 111-131

Full text read (harappa.com/script/indus-writing.pdf; text layer). A point-by-point reply to Farmer, Sproat & Witzel 2004.

- p. 116: numbers 1-4 alternate before the U-shaped pot on the Harappa bifacial tablets (UUU on H-764 = 3 + U), so
  the strokes are numeral attributes. p. 122: the Harappa tablets had an economic and ritual function; many identical
  copies from one spot; perhaps receipts for offerings/dues paid to a temple, or amulets given in exchange. **F5: the
  'tablets as receipts/tokens' idea is here (a suggestion, with a Kerala analogy); no capacity system, no
  Proto-Elamite pairing, nothing on weights.**
- p. 124: sequences recur in fixed order across sites; some signs limited to text ends, others to beginnings.
- **p. 125: Indus sign sequences are uniform across South Asia, but seals from the Near East carry both native and
  non-Harappan sequences (in step with seal shape: square = Indus, round = Gulf, cylinder = Mesopotamia); a round
  Gulf seal (BM 120228) has five common Indus signs in unique sequences, including a doubled sign never doubled in the
  Indus Valley. He reads this as Harappan agents in the Gulf and Mesopotamia writing their adopted local names in
  Indus signs.** (Also Parpola 1994 fig. 8.6.) **F8: the idea that Gulf/West Asian seals write foreign names in Indus
  signs is Parpola's (1994, 2008). He does not say or count that these texts lack the Indus terminal endings; the
  quantified omission is ours.**
- Nothing on F1-F4, F6, F7, F9-F11.

### Kenoyer & Meadow 2010, "Inscribed objects from Harappa excavations 1986-2007", CISI 3.1, introductory chapter (cited here by the offprint's own pages 1-15)

Full text read (harappa.com PDF, text layer).

- p. 6: square seals with animal + script from late 3A, script-only square seals from 3B, long rectangular
  (bar) seals only in 3C; incised steatite tablets and moulded tablets from mid-3B into 3C, not the earliest levels
  (correcting Vats). p. 6 n. 8: the same 'numerical' sign series recur on moulded tablets from different moulds.
  p. 8: "the Indus script did not appear fully formed and remain unchanged for more than 700 years" — changes in
  sign style and in the objects carrying signs; no script use in the Late Harappan period.
- p. 13 (conclusions): seal forms evolve over time; "whether there were parallel changes in the script needs to be
  investigated in detail"; earlier studies lumped all periods; the assumption of uniformity (Parpola 1994) will
  probably need revision.
- **F9: they pose the question (does the script change by period?) and expect change; they do not test it. Our
  result — grammar stable, numeral use changing — answers their question. With Rao & Mahadevan 1987 (p. 35: sign-pair
  frequencies stable across Mohenjo-daro periods) this is the prior work on F9.** **F5: tablets' chronology and
  duplicate numeral series, no function argued here** (the token reading is Meadow & Kenoyer 2000 / Rao 2018).

### Rao, Yadav, Vahia, Joglekar, Adhikari & Mahadevan 2009, "A Markov model of the Indus script", *PNAS* 106(33): 13685-13690

Full text read (PMC2721819, HTML).

- 'Filling in missing signs' (Results; Fig. 4C-E; SI Table S1): a first-order Markov model trained on the complete
  texts (EBUDS, 1,548 lines) restores missing signs by the most probable explanation. Scored by deleting signs from
  complete inscriptions: about 74% of deleted signs predicted correctly in cross-validation (details in Yadav et al.
  2010). Real damaged texts (from Parpola 1994 and M77) are also filled in, including one with an unknown number of
  missing signs; the outputs are compared with the closest intact texts in the corpus. **F10: restoring broken texts
  from sequence statistics, with an accuracy score, is published (2009-2010).** What differs in ours: the model is the
  grammar (heading/stem/ending slots), not a bigram chain, and it is scored on genuinely broken texts against their
  intact duplicates rather than on artificial deletions.
- 'Testing the likelihood' (Table 2): the complete West Asian Indus texts (from M77) have median likelihood about
  6.4e-13, about 100,000 times lower than held-out Indus Valley texts, because of sign pairs never found in the
  Valley; read as a different language or content, following Parpola's observation of unusual combinations.
  **F8: the West Asian texts' departure from Indus grammar is already quantified (by likelihood).** Not found: that
  the departure is specifically the missing terminal endings (jar/arrow), or a count of endings on foreign vs Valley
  seals.
- Nothing on F1-F7, F9, F11.

### Yadav, Joglekar, Rao, Vahia, Adhikari & Mahadevan 2010, "Statistical analysis of the Indus script using n-grams", *PLoS ONE* 5(3): e9506

Full text read (PMC2841631). (Also relevant to F4, reported in the first pass.)

- 'Restoring illegible signs' (Figs. 11-12; Table 5; Fig. 14): bigram model with Viterbi search restores deleted
  signs (random single deletions; all examples in Fig. 11 recovered) and proposes readings for the doubtfully read
  signs of M77 (Fig. 12). Cross-validation sensitivity 74%. **F10: published, as above; scored on artificial
  deletions, not on intact duplicates.**
- Materials and Methods: the corpus drops duplicates, damaged texts and multi-line texts, and "variations due to the
  archaeological context of the sites, stratigraphy, and type of object ... are, at present, not taken into
  account". **F4, F9: explicitly not studied.** Text enders 342 (jar), 176, 211 (arrow) and beginners 267, 391, 293
  followed by 99/123 are profiled by bigram probabilities, not by stem (F1/F2 not addressed).

### Tamburini 2025, "On automatic decipherment of lost ancient scripts relying on combinatorial optimisation and coupled simulated annealing", *Frontiers in AI* 8: 1581129

Full text read (PMC12162589). Surveys and extends the benchmark tradition in which decipherment *methods* are
validated on real decipherments: Snyder, Barzilay & Knight 2010 (Ugaritic/Hebrew), Berg-Kirkpatrick & Klein 2011,
Luo, Cao & Barzilay 2019 (Ugaritic, Linear B/Greek), Luo et al. 2021 (Gothic, Ugaritic, and a language-closeness
measure that identifies the right relative, then applied to Iberian); adds Phoenician/Ugaritic and Luvian/Hittite
benchmarks. **F11: validating on known decipherments is standard for decipherment *algorithms*; Luo et al. 2021's
closeness measure is the nearest thing to a validated *evaluation* test. None of these tests a proposed key against
shuffled versions of itself, or uses Linear Elamite as the positive control.** Mentions the Indus only for Rao et al.
2009/2010 (entropy) and Palaniappan & Adhikari 2017 (sign recognition).

### Mukhopadhyay 2019, 2021, 2023 (*Humanities and Social Sciences Communications* 5: 73; 8: 193; 10: 972), full texts

All three read in full (nature.com HTML); 2019 and 2023 were partly used in the first pass.

- 2019 (s41599-019-0274-1), section on stroke signs: repeated strokes read as cumulative-additive numerals, compared
  with Egyptian, Aramaic, Proto-Elamite and Assyro-Babylonian notation. **F5: a notation comparison, not the
  counting-vs-capacity pairing.** No site, period, West Asian or restoration analysis; nothing on F1, F3, F8-F11 beyond
  what the first pass recorded (fig. 9c, fish-like signs + arrow, F2).
- 2021 (s41599-021-00868-w, 'pīlu' elephant word): the Dravidian case rests on a loanword (Proto-Dravidian *pīl-
  borrowed into Mesopotamian and other languages) plus genetics; Munda (Witzel's 'Para-Munda', Southworth) and
  Burushaski are discussed as rival hypotheses, not tested on the script. **F3: no grammatical (noun-class suffix)
  elimination of Munda/Burushaski.**
- 2023 (s41599-023-02320-7): Gulf seals and Harappan weights in the Dilmun customs house (after Parpola 2018,
  Laursen 2010) support a tax/licensing reading; she argues the numerals on seals and two-sided tablets are licence
  slabs and did *not* record quantities of commodities in standard containers. **F5: argues against the capacity
  reading; no test of numerals against the weight ratios. F8: Gulf seals discussed for function only, not their
  texts. F9: 'poor chronological control' cited as an obstacle; no period analysis.**

### Two further items found in this pass

- **Venkatesh & Farghaly 2023, "Statistical models for identifying missing and unclear signs of the Indus script",
  *Journal of Emerging Investigators* 6** (full text read, emerginginvestigators.org PDF). n-gram models (n = 2-7)
  plus positional probabilities on the ICIT corpus fill in single missing signs; scored on signs deliberately deleted
  from complete held-out texts (Hit@1 about 35%, Hit@10 about 63%), then applied to about 100 real damaged texts.
  Notes that 820, 861, 817 and 920 dominate text beginnings. **F10: a third restoration study, again scored on
  artificial deletions, not on intact duplicates.**
- **Recchia & Louwerse 2016 [online 2015], "Archaeology through computational linguistics: inscription statistics
  predict excavation sites of Indus Valley artifacts", *Cognitive Science* 40(8): 2065-2080** (abstract only; the
  Wiley full text sits behind a bot check, not bypassed). Sign co-occurrence statistics recover the relative
  locations of sites and are used to assign four sealings of unknown provenance to sites. **F4: shows that
  inscriptions carry site-specific statistics overall; not about the opener formula.**

### Vidale 2007, "The collapse melts down: a reply to Farmer, Sproat & Witzel", *East and West* 57(1-4): 333-366

Full text read (archive.org `mvidale-the-collapse-melts-down-2007`, OCR of the JSTOR PDF; pages from the item's page map).

- p. 352: the relatively many unique signs on seals from Indus enclaves in Mesopotamia, the Gulf, the Iranian plateau
  and Bactria (citing Parpola 1994, Vidale 2005) show scribes adapting the script to new linguistic settings.
  **F8: qualitative, about unique signs, not endings.**
- p. 362: Dilmun seals need only 40-45 signs, against about 400 for the Indus script; p. 345-346 Proto-Elamite at
  Tepe Yahya (80 signs on 27 tablets) as a comparison of sign counts. **F5: Proto-Elamite cited for sign inventory, not
  numeral systems.**
- p. 364-365 (programme): study the palaeography and development of the script through time on the Harappa and
  Nausharo stratigraphy, separating diachronic from synchronic variation; keep corpora by medium (seals, moulded
  tablets, faience tablets, pottery pre-/post-firing, metal tools) and compare "possible numerals in this medium"
  across media. **F9 and F5: proposed as future work, not done.**
- Nothing on F1-F4, F6, F7, F10, F11.

### Kenoyer 2020, "Origin and development of the Indus script: insights from Harappa and other sites", in *Studies on Indus Script* (Karachi: National Fund for Mohenjodaro), 217-236

Full text read (harappa.com PDF, text layer; the first pass had only Mukhopadhyay's report of it). Fuls 2020 is in the
same volume but is not on harappa.com.

- pp. 218-219: regional and chronological changes in the kinds of symbols and their uses "suggest that there were
  significant changes in the writing system over time"; the details cannot be understood before decipherment.
- pp. 220-223 (Table 2): four stages; for each Harappa period, the objects and the look of the script (3A: 1-3 signs,
  curved placement; 3B: script-only square seals, incised and moulded tablets; 3C: long rectangular seals, 'bold, rigid,
  regular script'). **In 3C the tablets are listed under "Trade and Accounting devices", with moulded terracotta
  tokens bearing script.** p. 229: the jar sign (M77 342) and the pair 342 + 347 already occur on Period 1-2 pottery.
- **F9: change is claimed for media, carving style and placement, not for the grammar; no statement that headings and
  endings stay stable, and no numeral-by-period analysis.** (The claim attributed to Kenoyer 2020 in the first pass,
  via Mukhopadhyay 2023, that later seals keep the same initial and terminal signs with longer cores, is not in this
  paper's text; it may come from the 2020 talk.) **F5: tablets as trade/accounting devices and script-bearing tokens,
  stated as a classification; no capacity or Proto-Elamite argument.**

### Rao, Yadav, Vahia, Joglekar, Adhikari & Mahadevan 2010, "Entropy, the Indus script, and language: a reply to R. Sproat", *Computational Linguistics* 36(4): 795-805

Full text read (author's HTML at homes.cs.washington.edu/~rao/IndusCompLing.html). A Bayesian 'weight of evidence'
framing of the entropy results; lists properties shared with linguistic scripts; cites the restoration work (Rao et al.
2009b; Yadav et al. 2010). No calibration of any test on a known decipherment. **Nothing new on F1-F11** beyond the
restoration papers already listed under F10.

### Wells 2015, *The Archaeology and Epigraphy of Indus Writing* (Archaeopress) — front matter only

Still not readable beyond the Archaeopress sample (pp. i-2). What the sample adds: Preface pp. viii-ix: "marked
regional differences in sign uses and artifact inventories"; future work should define regional differences in text
structure; the corpus is "demonstrably affected by spatial and temporal variation". Introduction p. 1: most researchers
wrongly treat the corpus as homogeneous. The lists of figures and tables show what the body covers, so these chapters
are the ones to check if the book becomes available: Fig. 3.8 and 3.15 (initial-cluster terminal markers, i.e. the
stroke pair, by initial cluster), Fig. AI.9 (segmentation by artefact type; Fuls's Appendix I), Ch. 4 Tables 4.1-4.2
(Harappa volumetric units from the Purana Qila pots), Ch. 5 Tables 5.1-5.3 (right-adjacent collocations of short-linear,
short-stacked and long-linear strokes, i.e. which stroke system precedes which signs — **the nearest thing to F5's
two-system claim, unread**), Fig. 5.2 (economic texts in three ancient scripts vs Indus), Fig. 5.5 (fish + numeral
associations, **F6, unread**), Fig. 6.21 (Proto-Dravidian verb endings and signs). The 2006 thesis (below) is the
earlier version of chapters 3-6.

### F8 background from Parpola 1994 (first-pass OCR, re-read for this point)

Parpola 1994 §8.2, pp. 131-132: quotes **Hunter 1932 (JRAS: 469)** — the round seals found in Mesopotamia show sign
sequences unparalleled in the Indus Valley, the square seals found there show normal Mohenjo-daro sequences, so the
round ones are "in a different language", made for Sumerian- or Semitic-speaking people of Indus descent. Parpola adds
two examples: the Kish square seal's text recurs in the Valley; the round BM seal's five common signs form pairs
attested nowhere else, with the commonest sign (the jar) doubled only here. He proposes the hybrid texts as a future
test of any decipherment (they should read as Near Eastern names). **F8: the observation that West Asian round seals
depart from Indus sequences goes back to Hunter 1932; Rao et al. 2009 quantified the departure by likelihood. The
specific, counted claim that these texts lack the Indus terminal endings is not in any of these.**

### Parpola 2015, *The Roots of Hinduism* (OUP), chapters 5, 14, 16, 17, 21

Read in full for those chapters (pp. 25-32, 163-172, 187-219, 266-294) by fresh OCR (easyocr) of the page images in
archive.org `rootsofhinduismearlyaryansandtheinduscivilizationaskoparpolaoup_757_i` (the item's own text layer is
Devanagari-OCR garbage; the other copy, `rootsofhinduisme0000parp`, is lending-only). Printed page numbers.

- **F8** p. 163: one language wrote the Indus script, since its sequences repeat across the realm; "only in the West
  Asian Indus seals" are clearly different sequences found (another language: Sumerian/Akkadian, early West Semitic
  in the Gulf); p. 164 fig. 14.1: the round BM 120228 seal, five common signs in a unique order. p. 213: counts the
  Gulf-type seals with inscriptions (28: 12 Mesopotamia, 3 Iran incl. one with Linear Elamite, 9 Gulf, 5 Lower Indus)
  and notes the square seals from Nippur and Kish carry native sequences. Same idea as Hunter 1932 / Parpola 1994,
  2008; no count of endings.
- **F3** p. 165: Burushaski, Tibeto-Burman and Munda are set aside because they are small, marginal minority
  languages with no recognised loans in the Rigveda, and Witzel's 'Para-Munda' etymologies are rejected (after Osada
  2006); p. 286: "in Dravidian languages the qualifier precedes the qualified" used to read a text. **No grammatical
  (noun-class suffix) test against Munda or Burushaski.**
- **F6** pp. 274-275: numerals are "mutually interchangeable before specific signs, including the simple fish sign";
  6 + fish = aru-min (Pleiades), 7 + fish = elu-min (Ursa Major; the whole text of seal H-9, fig. 21.8); pp. 288-291:
  two long strokes + fish = vel-min (Venus). pp. 196-198 (ch. 16): the Pleiades head the Vedic naksatra list, of
  Harappan origin. **Readings only; no enrichment test.** (The 3 + fish reading of 1994 is not repeated here.)
- **F5** pp. 268, 270-271: on the Harappa tablets the U sign alone or after 1-4 strokes (UUU = 3) stands for pots of
  offerings; two Harappa tablets read "four pots of fish" (H-1191, H-1192). **Offerings, not capacity units; nothing
  on weights, Proto-Elamite or two stroke systems.**
- p. 266: logosyllabic scripts mark grammar minimally, so no Linear-B-style grid is possible. pp. 282-283: the copper
  tablets link reverse motif and single sign (as in 1994).
- Nothing on F1, F2, F4, F7, F9, F10, F11 beyond what 1994 already says.

### Wells 2006, *Epigraphic Approaches to Indus Writing* (PhD thesis, Harvard; revised as the 2011 Oxbow/ASPR monograph)

Read for chapters 3 (end), 4, 5 and 6 (pp. 93-108, 129-210) by fresh OCR (easyocr) of the page images in archive.org
`epigraphicapproachestoinduswritingbryankennethwellsphd.thesis_230_Z` (its own text layer is Devanagari-OCR garbage).
Thesis page numbers (printed page = PDF page - 11). The 2011 book is this thesis revised; page numbers will differ.
The 2015 book was not available (see above).

- **F4** p. 108, 133: sign inventories correlate between Mohenjo-daro and Harappa only for square seals; differences
  between sites are largely differences of artefact type, so site and artefact type must both be used to classify
  texts. pp. 134-135 (Table 4.4): his five text types are distributed unevenly by site and artefact type. pp. 138-141
  (Table 4.5, 4.6): the opening 'Initial Cluster' ends in an 'Initial Cluster Terminal Marker' (ICTM: signs 1, 2 or 60
  in his numbering, i.e. the stroke pair and its alternants); the pairing of initial sign with ICTM is strongly
  non-random ("a strong preference for certain signs to locate exclusively with others"); ICTM positions tabulated.
  p. 154: the fish sign is initial far more often at Harappa. **Closest earlier work on the heading formula: the
  opener + marker unit and its internal pairings are Wells's; site/object-type effects are shown for inventories and
  text types. Not found: that the opener variant itself depends on site and object type, tested, and independent of
  the following name.**
- **F7** p. 141 (with pp. 192-195): long texts follow a fixed order of clusters — Initial Cluster, ICTM, 741/742/745,
  Ovals, Fish & Numbers, Bonded Clusters, Terminal Markers, Post-Terminals; pp. 135-137: single-segment texts are the
  building blocks of longer texts. A hand-built slot grammar with the terminals as a slot; no unsupervised model.
  (Fuls's automated segmentation appears only in Wells 2015 App. I.)
- **F1/F2** p. 151: jar (740), 390, 407, 405 and arrow (520) share the Terminal Marker slot and are logographs.
  pp. 198-200 (Table 6.1): only 20.5% of jar occurrences take a post-terminal affix (mostly signs 400, 90); affixes are
  optional and restricted. **No per-stem analysis of jar vs arrow, and no fish/arrow class claim.**
- **F5** p. 101 and pp. 148-149: Harappa tablets (TAB) may be ration chits or a form of money (citing Wells 1999: 35);
  sign 700 (the U pot) + 2-5 long strokes relates to "a possible system of Indus volumetric measures"; sign 700
  prefers particular numerals, and signs 31-34 do not have the same values in V + number texts as elsewhere.
  pp. 161-172: four numeral sets (short linear, long linear, short stacked, special); explicit comparison with
  Proto-Elamite and proto-cuneiform, whose numerals belong to several metrological systems chosen by the counted noun
  (p. 166: Proto-Elamite 14 numerals in at least 5 groups); p. 171-172: working out which Indus numerals belong to which
  measuring system is "beyond the scope" of the thesis. p. 179 (Fig. 5.7): long strokes cluster on rectangular seals and
  pottery, short strokes on seals; p. 181: short stacked and short linear strokes are "two distinct set[s] of numerals".
  p. 196: the three stroke series count differently (short linear 1-7, stacked 2-10, long linear 1-7 and 9); two
  counting systems for different purposes is judged possible but less likely than stacking to save space. p. 178:
  numerals prefer particular signs, "not surprising given" the standard weights and vessel sizes — assumed, not tested.
  **F5 is largely anticipated here: separate stroke systems, the Proto-Elamite/proto-cuneiform multi-system model,
  volumetric V + number texts on Harappa tablets, tablets as ration chits. What remains ours: assigning short vs long
  strokes to counting vs capacity specifically, and the test against the Harappan weight ratios.**
- **F6** p. 176 (Fig. 5.6) and p. 178: a table of which numerals stand right-adjacent to which signs, fish signs
  included; numerals "have a preference for certain signs". Raw co-occurrence counts, no enrichment test against
  numeral base rates, nothing on 6 + fish specifically.
- **F9** pp. 102-105: singletons and variants of the jar sign (740a-f) plotted by phase at Mohenjo-daro DK-G and
  Harappa Mound F; graphic variants shift over time while graphemes keep constant proportions. pp. 156-157: enclosed
  signs vary by phase and correlate with mean text length. **Palaeographic change by period is Wells's; nothing on the
  stability of headings/endings or on numeral use by period.**
- **F3 — the thesis argues the opposite of our result.** pp. 186-191: candidates narrowed to Proto-Dravidian,
  Proto/Para-Munda and 'Language X'. pp. 200-207: Indus word structure compared with Proto-Dravidian (McAlpin 1981;
  p. 201 gives the PDr masculine *-anṟ(e) vs non-masculine *-ay/*-i noun classes) and Proto-Munda (Anderson 2001).
  p. 205: the Indus pattern "effectively eliminates PDr"; p. 207-208: the prefixing/infixing needed for initial
  clusters fits Proto-Munda better; conclusion: only Proto-/Para-Munda and X remain; p. 184, 194: he prefers
  verb-initial (VSO/VOS) syntax. **So a morphological elimination test between Dravidian and Munda was done in 2006,
  with the opposite verdict and without a gender/class-suffix test on the jar/arrow endings.** (Wells 2015 ch. 6 is
  titled "Proto-Dravidian and the Indus script", so he appears to have changed his view; unread.)
- **F11** p. 208-210, 'Tests of decipherment': any decipherment must give a two-syllable word for 'hare' fitting the
  copper-tablet replacement set, and must read a Dholavira place name in the signboard sequence that recurs on
  Mohenjo-daro bronze implements and a tag. **Criteria for checking a decipherment, not a test validated on a known
  decipherment.**
- Nothing on F8 or F10.
- Addendum (ch. 1, pp. 20-22, OCR'd last): tablets (bas-relief, incised, copper) repeat identical texts, which
  "suggests ... that they are tokens of some sort"; copper tablets are essentially Mohenjo-daro only, incised and
  bas-relief tablets Harappa, so their uses were site-specific. **F5: the token reading of the tablets is already
  Wells 2006 p. 22 (and 1999).**

### Second-pass summary by finding

| # | earlier statements found in this pass | what still looks new |
|---|---|---|
| F1 | Hunter 1934 claimed the stems before jar and arrow are mutually exclusive (reported and disputed by Mahadevan 1970 pp. 18, 20); Mahadevan 1982 p. 311 (terminals bound to their antecedents); Mahadevan 1986 pp. 24-26 and Rao & Mahadevan 1987 p. 37 argue *against* gender/case readings; Mahadevan 1998 for them | the count (5 of 881 stems vs ~46 by chance) and the baseline |
| F2 | Mahadevan 1970 p. 22 (arrow "occurs mostly" with fish signs), p. 26; 1973 §3.1 (fish take the arrow more often than the jar) | the closed-class claim (non-fish stems almost never take it), with rates |
| F3 | order half: Mahadevan 1982 p. 311, 1986 p. 21; Parpola 2015 p. 286. Munda/Burushaski set aside on non-grammatical grounds (Parpola 2015 p. 165). **Wells 2006 pp. 200-208 ran a Dravidian-vs-Proto-Munda morphology comparison and eliminated Dravidian** | the noun-class-suffix test and the two-test elimination leaving Dravidian; it contradicts Wells 2006 |
| F4 | Mahadevan 1970 p. 46 (opener proportions "approximately the same" across sites — the opposite claim); Mahadevan 1986 pp. 21-23 (variant governed by the preceding sign); Rao & Mahadevan 1987 pp. 34-36 and Ganesan et al. 2010 p. 5 (opener pairs tabulated by site and object type, descriptively); Wells 2006 pp. 133-141 (initial cluster + marker, site/type effects on inventories); Recchia & Louwerse 2016 (site-predictive statistics) | the tested dependence of the opener variant on site and object type, independent of the following name |
| F5 | Wells 2006 pp. 22, 101, 148-149, 161-196 (four numeral series, Proto-Elamite/proto-cuneiform multi-system model, V + number = volumetric, tablets as tokens/ration chits; two counting systems considered and judged less likely); Parpola 2008 p. 122 (tablets as receipts); Kenoyer 2020 pp. 221-222 (tablets as trade/accounting devices, tokens); Mahadevan 1986 p. 24 (long vs short strokes functionally distinct) | short = counting vs long = capacity as a stated pairing, and the weight-ratio test |
| F6 | Mahadevan 1970 pp. 29-30 (numbered fish = phratries 4, 6, 7); Parpola 2015 pp. 274-275, 288-291 (6, 7, 'two long strokes' + fish as stars); Wells 2006 p. 176 (numeral-sign co-occurrence table) | the enrichment test |
| F7 | Mahadevan 1986 pp. 21, 27 (root vs suffix classes; intro phrase + substantive phrase); Wells 2006 p. 141 (fixed slot order) | an unsupervised model recovering it, with a shuffle control |
| F8 | Hunter 1932: 469; Parpola 1994 pp. 131-132, 2008 p. 125, 2015 pp. 163-164, 213; Vidale 2007 p. 352; **Rao et al. 2009 PNAS Table 2 (West Asian texts ~10^5 times less likely under the Valley model)** | that the difference is the missing terminal endings, counted |
| F9 | Rao & Mahadevan 1987 p. 35 (sign-pair frequencies stable across Mohenjo-daro periods); Wells 2006 pp. 102-105, 156-157 (palaeographic and enclosure change by phase); Kenoyer & Meadow 2010 pp. 6-8, 13 and Kenoyer 2020 pp. 218-223 (change in media and carving; call for period study); Vidale 2007 pp. 364-365 (proposed) | grammar stable while numeral use changes, measured |
| F10 | **Rao et al. 2009 PNAS (Markov restoration, ~74% on deletions); Yadav et al. 2010 (bigram restoration, 74% sensitivity); Venkatesh & Farghaly 2023 (Hit@1 ~35%)** | grammar-based restoration scored against intact duplicates |
| F11 | decipherment algorithms benchmarked on real decipherments (Snyder et al. 2010, Luo et al. 2019, 2021, Tamburini 2025); Wells 2006 pp. 208-210 (criteria a decipherment must meet) | a key-vs-shuffled-key test validated on Linear Elamite |

Still unread after this pass: Wells 2011 (the thesis read instead) and Wells 2015 beyond the sample (Chs. 3-6 and
Fuls's appendices are the ones to get); all of Fuls's papers (2010, 2012 on vessel volumes, 2013 Epigrafika, 2020 in
*Studies on Indus Script*): Academia/ResearchGate return 403 and the blog copy is script-rendered; Recchia & Louwerse
2016 beyond the abstract (Wiley bot check, not bypassed); Rao et al. 2009 *Science* (not needed: entropy only);
Mahadevan 2014.
