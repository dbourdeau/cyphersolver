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
