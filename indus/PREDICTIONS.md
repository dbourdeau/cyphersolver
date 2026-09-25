# Predictions registered before testing (23 September 2026)

Written and committed before `predict_test.py` was written or run. They follow from reading the two Indus endings
as a Dravidian rational / non-rational class pair (740 = rational singular, -an; 520 = non-rational, the fish = star
names), as in Old Tamil grammar (Mahadevan 2003, Early Tamil Epigraphy 7.23-7.24; Krishnamurti 2003). None has
been looked at in the data.

**P1 A rational plural.** Old Tamil has a human (epicene) plural suffix (-ar). If 740 is the rational singular,
some other sign should replace 740 at the end of the same names (same stem, different final sign), more often than
its frequency predicts.

**P2 No non-rational plural.** Old Tamil marks no plural on non-rational nouns ('No plural suffix occurs in the
Corpus for nouns in the neuter gender', Mahadevan 7.23.6). So the sign found under P1 should replace 740 but not
520: it should follow 740-class stems, not the fish (520) stems, beyond its share of those stems.

**P3 The stems that take 520 should not alternate with other final signs** at more than the rate of 740 stems
(non-rational nouns take no case or number marking at the end of a name in the Tamil-Brahmi corpus beyond the
single class suffix).

Test design, fixed in advance: stems = the whole line before its final sign, lines of 2+ signs, ICIT-derived
corpus for discovery, the M77 additions as the held-out check; a sign 'replaces 740' when the same stem occurs
once with 740 and once with that sign as the final sign; expected counts from the sign's frequency as a final sign,
by permutation of final signs among lines (200 permutations). P1 holds if some sign other than 520 and the second-
slot signs (400, 90, 151) replaces 740 at p < 0.01 on the discovery corpus and again (p < 0.05) on the held-out
texts; P2 holds if that sign's share of 520 stems is below its share of 740 stems; P3 holds if the share of 520
stems seen with more than one final sign is not above that of 740 stems.

## Results (added after the test; `predict_test.py`, `results/predict_test.md`)

- **P1 fails.** No sign replaces 740 on the same names beyond chance; the candidates (156 on 5 stems, 407 on 3, 154 on
  3) do so less often than permutation expects (18.5, 14.8, 8.3). No rational plural is visible.
- **P2** not testable (no P1 sign).
- **P3 fails narrowly.** 520 stems appear with more than one final sign in 10.9% of cases (19 of 175), 740 stems in
  8.0% (73 of 909).
- A seal names one holder, so no plural need appear on seals; but that is an explanation found after the result and
  is recorded as such. As registered, the Dravidian rational / non-rational model made two predictions beyond the
  data it was built on, and neither came out.

# Second set, registered before testing (23 September 2026)

From reading the Indus name as a head-final compound with a class suffix (Dravidian, and Indo-Aryan compounds too;
the head-initial alternatives, Sumerian and Elamite, predict the reverse). The last-sign association (G1, sixth
pass) was already known; the comparison with the first sign (Q1) and the non-final fish (Q2) have not been looked at.

**Q1 The head decides the class.** The ending (740 / 520) should depend more on the name's last sign than on its
first sign: mutual information between ending and last sign above that between ending and first sign, for names of
2+ signs before the ending, each against 500 permutations of the endings; and names that share their last sign should
agree in ending more often than names that share their first sign.

**Q2 A fish that is not the head does not make the class.** Names with a fish sign somewhere but not in last position
should take 520 far less often than fish-final names, and no more often than names without a fish sign, beyond a
small margin (difference to non-fish names under 10 percentage points).

Test design fixed in advance: discovery sample = the ICIT-derived corpus; held-out = the M77 additions and the texts of
the fuller ICIT-derived corpus that the ICIT-derived dump lacks (icit_full.py; local use). Q1 holds if MI(last) >
MI(first) in both samples and the last-sign MI is significant (p < 0.01) while the first-sign excess is smaller;
Q2 holds if in both samples the non-final-fish rate is under half the fish-final rate and within 10 points of the
no-fish rate.

## Results of the second set (added after the test; `predict_test2.py`, `results/predict_test2.md`)

- **Q1 holds** in both samples. Mutual information with the ending, excess over permutations: last sign 0.369 bits
  against first sign 0.113 (discovery), 0.307 against 0.052 (held out). Names sharing their last sign agree in ending
  88.6% / 95.4% of the time, names sharing their first sign 77.6% / 83.1%.
- **Q2 holds** in both samples. Taking 520: fish-final names 59.5% / 55.0%; a fish inside the name but not last 9.8% /
  8.2%; no fish 7.3% / 5.4%.
- The first correct advance prediction of this project: the class is set by the last element of the name, as in a
  head-final compound with a class suffix. It counts against head-initial languages (Sumerian, Elamite); it does not
  separate Dravidian from Indo-Aryan, whose compounds are also head-final. Q1 was partly foreseeable from the known
  last-sign association; Q2 had not been looked at.

# Third set, registered before testing (23 September 2026)

From the same reading (head-final names with a class suffix; a possessive 'X-740 man'). Neither has been looked at.

**R1 Numerals are attributes that precede what they count, inside names too.** Of stroke numerals inside names (the
text before the ending, heading removed), under 10% stand last, directly before the ending, and 90%+ are followed by a
non-numeral sign within the name.

**R2 Possessives can stack.** If 740 + a following noun is 'X's N', an internal 740 (one not in the final ending slot)
should be followed by further name material that itself closes with an ending (740 / 520) or the man sign: texts with an
internal 740 end in 740 / 520 / 90 / 400 more often than texts of the same length without one.

Test design fixed in advance: held-out texts only (M77 additions + the fuller corpus's texts not in the ICIT-derived
dump, icit_full.py). R1 holds if both thresholds are met. R2 holds if the share of ending-closed texts among texts with
an internal 740 exceeds that among length-matched texts without one, Fisher p < 0.05.

## Results of the third set (added after the test; `predict_test3.py`, `results/predict_test3.md`; held-out texts)

- **R1 fails.** Of 152 stroke numerals inside names, 40 (26.3%) stand last, right before the ending (units such as
  long 3 + 520), and 104 (68.4%) are followed by a non-numeral sign; the thresholds were under 10% and 90%+.
- **R2 fails.** Texts with an internal 740 close with an ending or the man sign in 11% (12 of 107), length-matched
  texts without one in 34%. The operationalisation was crude (some cases are 740 90 400, a doubled second slot, not a
  second possessor), but it was the registered one.
- Tally of the registered predictions: 2 held (Q1, Q2: the head decides the class), 4 failed (P1, P3, R1, R2). The
  structural reading predicts where the class is set; it has not predicted plurals, numeral placement or stacking.

# Fourth set, registered before testing (24 September 2026)

**Hypothesis T: the two name classes are two kinds of name.** If the fish signs are 'star / god' (Parpola) and the
520 class is closed around them, 520-ending names are divine or astral names, or titles made from them, shared by
many holders; 740-ending names ('X's man') are personal names, one holder each. Nobody has looked at this here.

Unit: distinct intact seals (object type SEAL; sealings and tablets left out, since one seal makes many sealings and
tablets were made in batches) of the fuller ICIT corpus (icit_full.py). Name = the text before the ending with the
heading removed (817 / 820 / 861 + 2 / 60 / 1), plus its ending 740 or 520 (a trailing 400 / 90 / 151 dropped).

**T1 Recurrence.** A 520 name recurs on another seal more often than a 740 name of the same length: stratified by
name length (1, 2, 3, 4+ signs before the ending), the pooled difference in the share of seals whose name recurs is
positive, permutation p < 0.05 (ending labels shuffled within strata, 10,000 times).

**T2 Spread.** Among names on 2+ seals, 520 names are found at 2+ sites more often than 740 names, same
stratification, permutation p < 0.05; and 520 names beat a site-shuffled null (site labels shuffled among the seals)
while 740 names do not.

Either failing counts against Hypothesis T. A length effect alone (short names recur more) does not count for it.

## Results of the fourth set (added after the test; `predict_test4.py`, `results/predict_test4.md`)

795 intact seals with a name and an ending (650 with 740, 145 with 520).

- **T1 fails.** Length-matched, 520 names recur on another seal no more than 740 names (pooled difference -2.9 points,
  p = 0.84). Recurrence is a matter of length: one-sign names recur 65-83%, four-sign names 0-2%, in both classes.
- **T2 fails.** Of recurring names, 520 names are at 2+ sites in 7 of 13 (54%), 740 names in 29 of 51 (57%); both a
  little under a site-shuffled null (62%, 63%). Neither class is local.
- Tally: 2 held (Q1, Q2), 6 failed (P1, P3, R1, R2, T1, T2). The two classes are not distinguishable as 'shared
  divine/astral names' against 'personal names' by how they recur or spread.
- Observed after the test, not registered: recurring names of both classes are spread over sites as a random
  assignment would spread them, not held in one city. A personal name borne by one family would be local; this looks
  more like a pool of names or titles in use everywhere, or like seals carried between cities. It is an observation
  for a future registered test, not a finding.

# Fifth set, registered before testing (24 September 2026)

**Hypothesis V: a recurring name marks the same holder or generation.** If the names are personal names, seals that
carry the same name were made for one person, or for people of one time, and should be found in the same level of a
site. If they are hereditary names, offices or titles, they persist across levels. Not looked at here before.

Unit as in the fourth set: distinct intact seals (type SEAL) of the fuller ICIT corpus with a name and an ending 740 /
520 (heading removed, trailing 400 / 90 / 151 dropped); identical name + ending = same name. Pairs are counted within
a site.

**V1 Period.** Seals with a known excavators' period: Mohenjo-daro Early / Intermediate / Late (field 9), Harappa
Period 3 sub-phase B / C (field 10). Among same-site pairs of seals bearing the same name, the share in the same
period exceeds the share when period labels are shuffled among the seals of that site (10,000 times), p < 0.05.

**V2 Depth.** Mohenjo-daro seals with a recorded depth (field 11): same-name pairs have a smaller median depth
difference than when depths are shuffled among the site's seals (10,000 times), p < 0.05.

Hypothesis V holds if V1 and V2 both hold. If both fail, recurring names persist across levels (names or titles
handed on); that is the alternative, and it counts for it only if the same-name pairs are also not closer than chance.

## Results of the fifth set (added after the test; `predict_test5.py`, `results/predict_test5.md`)

- **V1 fails.** 266 seals with a name and a known period (all but 8 from Mohenjo-daro); 36 same-name same-site pairs
  from 14 names. Same period: 47% (17 of 36); periods shuffled within site: 46%; p = 0.49.
- **V2 fails.** 449 Mohenjo-daro seals with a depth; 71 same-name pairs. Median depth difference 4.7 ft against 5.0 ft
  shuffled; p = 0.37.
- Tally: 2 held, 8 failed. Same-name seals are no closer in level or depth than any two seals of the site: the names
  run across Intermediate and Late Mohenjo-daro (for example 415-100+740 on five seals in both periods, 176+740 on
  four). This fits names or titles handed on, or a stock of names in use over generations, better than one holder
  per name.
- Limits: the test is weak. Mohenjo-daro's periods are coarse (each spans generations), the depths come from different
  areas of the site with different datums, and the pairs are not independent (one name gives 10 of the 36 pairs). The
  null band was 33-61%: only strong clustering could have shown.

# Sixth set, registered before testing (24 September 2026)

**Hypothesis W: sealings record local administration by holders of shared names or offices.** The previous two sets
found that recurring seal names are tied to neither one city nor one period, which fits names or titles held by many.
If sealings were impressed by such office-holders where they worked, a sealing's name should be found on seals of
the same site, and sealings should be made disproportionately by the names many seals carry. Not looked at before.

Unit: intact sealings (object type TAG) and intact seals (SEAL) of the fuller ICIT corpus with a name and an ending, as
in the fourth set.

**W1 Home.** Of sealings whose name occurs on at least one seal, the share with a same-name seal at the sealing's own
site exceeds the share when sites are shuffled among those sealings (10,000 times), p < 0.05. If instead the share is
below the shuffled one (p < 0.05 the other way), sealed goods travelled from the seal-holder's city; recorded either
way.

**W2 Common names.** Sealing names match a seal name more often than seal names match another seal, within name-length
strata (1, 2, 3, 4+ signs), permutation of the object type within strata, p < 0.05.

## Results of the sixth set (added after the test; `predict_test6.py`, `results/predict_test6.md`)

44 intact sealings with a name and an ending (Lothal 25), 795 seals.

- **W1 fails.** Of 17 sealings whose name is on a seal, none has a same-name seal at its own site (0%, against 15%
  with sites shuffled; p (away) = 0.001). But 10 of the 17 are one Lothal batch (48+740, TAG:B), almost certainly
  impressions of one seal. Checked after the test, counting each distinct sealing text once: 7 texts, none at home,
  against 10% expected from where sealings are found (p = 0.50). The registered 'away' result rests on that batch and
  is not claimed. What stands is descriptive: the matching seals are mostly at Mohenjo-daro (Lothal sealings 48+740,
  482+740, 705-33+520; Rupar 17-585+740; Dholavira 220+740), and two Mohenjo-daro sealings match seals found only
  elsewhere (590-390+740 at Harappa, Allahdino, Chanhu-daro, Dholavira; 32-760+740 at Nausharo).
- **W2 fails.** Length-matched, sealing names match a seal name no more often than seal names match another seal
  (+3.9 points, p = 0.27).
- Tally: 2 held, 10 failed. Not checked against Frenez's work on the Lothal sealings, which should be read before any
  claim about sealed goods moving between cities.

# Seventh set, registered before testing (24 September 2026)

**Hypothesis X: scribes break lines between words, and our segments are words.** If heading, name and ending are
units of the language, a seal text that runs onto a second line should be broken at a segment boundary, and tightly
bound sign pairs should not be split. Parpola used line division as segmentation evidence; not measured here.

Unit: intact seals (SEAL) of the fuller ICIT corpus with 2+ lines, lines in reading order (icit_full.py). A gap is the
position between two adjacent signs of the text; a break is a gap at a line end.

**X1 Segment boundaries.** Boundary gaps: after the heading (817 / 820 / 861 followed by 2 / 60 / 1) and before the
ending (740 / 520 as defined in the fourth set). The share of breaks falling on boundary gaps exceeds the expectation
with each text's breaks placed at random among its gaps (10,000 times), p < 0.05.

**X2 Bound pairs are not split.** Bound pairs: the 30 commonest ordered sign pairs (count 10+) with the highest PMI,
counted in single-line intact seal texts. In multi-line texts, gaps inside a bound pair are breaks less often than
other gaps of the same texts, Fisher p < 0.05.

## Results of the seventh set (added after the test; `predict_test7.py`, `results/predict_test7.md`)

66 intact multi-line seals (69 line breaks, 414 gaps), 1,541 single-line seals.

A problem found while testing: the reading order of *lines* in the fuller corpus is ambiguous. icit_full.py keeps them
as listed (an ending stands last on 34 of the 66, a heading first on 1); data/corpus.tsv reverses them (ending last on
12, heading first on 12). Neither order is right for every seal. The test was run both ways; icit_full.py keeps the
listed order as default, so earlier results are unchanged, with a switch (LINES_REVERSED) for the other.

- **X1 fails** in both orders. Breaks on a heading / ending boundary: 1 of 69 (1.4%, random 9.3%) as listed; 6 of 69
  (8.7%, random 7.8%) reversed. Most breaks fall inside the name (67 or 51 of 69). Scribes did not break seal lines at
  our segment boundaries; the line length seems set by the seal's field, not the grammar.
- **X2 holds** in both orders. Gaps inside the 30 bound pairs are never a line break: 0 of 31, against 69 of 383 other
  gaps (18%), Fisher p = 0.003. Checked after the test without the heading pairs (817-2, 861-2) and without first and
  last gaps: 0 of 21 against 55 of 262 (21%), p = 0.009.
- Tally: **3 held** (Q1, Q2, X2), 11 failed. X2 is the first sign that the high-PMI pairs (705-33, 415-100, 590-390,
  33-520, 920-60, 235-240, 32-220 ...) are units the scribes kept together, i.e. words or fixed compounds, and not only
  frequent neighbours. The small numbers (21-31 bound gaps) make it a lead to replicate on tablets and more seals, not a
  settled result.

# Eighth set, registered before testing (24 September 2026)

**Hypothesis Y: foreign names are spelled with sound signs, home names use word signs.** The seventh set found sign
pairs the scribes never split (X2), which behave like words. The West Asian Indus texts leave out the endings and use
unfamiliar sequences (gulf.py): they are thought to write foreign names. If the script mixes word signs with sound
signs, a foreign name has to be spelled by sound: it should avoid the bound pairs and use signs that combine freely.
Not looked at before.

Samples as gulf.py: intact lines of 2+ signs, West Asian (region Persian Gulf / Mesopotamia / Central Asia, or Susa,
Luristan, Tepe Yahya) against home. Nulls: 10,000 draws of home lines matched one-to-one on length.

**Y1 Bound pairs.** The 30 bound pairs of the seventh set: their share of the adjacent sign pairs in West Asian lines
is below the length-matched home draws, p < 0.05.

**Y2 Free signs.** Freedom of a sign = the residual of log(distinct left and right neighbours) regressed on log(tokens),
over home lines, for signs with 5+ home tokens. With 740, 520 and the heading signs (817, 820, 861) left out on both
sides, the mean freedom of West Asian sign tokens exceeds the length-matched home draws, p < 0.05.

Hypothesis Y holds if both hold.

## Results of the eighth set (added after the test; `predict_test8.py`, `results/predict_test8.md`)

18 West Asian lines (89 signs), 3,356 home lines.

- **Y1 fails, narrowly.** Bound pairs are 4 of 71 West Asian adjacent pairs (5.6%) against 12.7% in length-matched home
  draws; p = 0.060 against the registered 0.05. The direction is the predicted one. Two of the four are 590-390 in the
  two West Asian lines that end in 740 (416 840 60 3 220 590 390 740; 285 2 235 220 125 590 390 740), which read like
  ordinary Indus names; the other 16 lines have 2 bound pairs among 57.
- **Y2 holds.** Mean freedom of West Asian sign tokens +0.184 against +0.084 for home draws (5-95%: -0.006 to +0.171),
  p = 0.029: the foreign texts lean on signs that combine with many different neighbours.
- **Hypothesis Y fails** as registered (both parts required). Tally: 4 held (Q1, Q2, X2, Y2), 12 failed.
- What it leaves: a weak, consistent pattern (fewer bound pairs, more free signs) in the texts thought to write foreign
  names, which is what a script with sound signs spelling foreign words would show. 15 of 87 West Asian tokens are signs
  with under 5 home tokens, left out of Y2. The sample is small (18 lines), so this is a lead, not a result; it
  singles out the freest signs as the best candidates for sound values.

# Ninth set, registered before testing (24 September 2026)

**Hypothesis Z: tablets with the same text were made as one batch, at one time.** Harappa's miniature tablets repeat
the same text on many pieces (tablets.py; tokens, as Wells 2006 suggested). If a text was a batch made for one
occasion, identical tablets should lie in the same level. This is also the power check the fifth set lacked: seals
with the same name did not cluster by level (V1, V2); if batch tablets do, the method can see clustering and the seal
names really do span generations. Not looked at before.

Unit: Harappa tablets (TAB) of the fuller ICIT corpus with an intact text; same text = the identical full sign
sequence (lines joined in the listed order). Pairs are counted within one labelling scheme.

**Z1 Level.** Levels: HARP Period 3 sub-phase B / C (field 10 'B' or 'C'), and Vats's strata (field 10 'Stratum I' to
'Stratum VI'). Same-text pairs share a level more often than with levels shuffled within the scheme (10,000 times),
p < 0.05.

**Z2 Depth.** Tablets with a recorded depth: same-text pairs have a smaller median depth difference than with depths
shuffled (10,000 times), p < 0.05.

Hypothesis Z holds if both hold. For comparison, the same two statistics are reported for Harappa seals with the same
name (fifth-set unit), without a registered threshold.

## Results of the ninth set (added after the test; `predict_test9.py`, `results/predict_test9.md`)

- **Z1 holds.** 592 Harappa tablets with a level; 3,470 same-text pairs from 67 texts share a level 25% of the time,
  against 21% with levels shuffled; p = 0.0003.
- **Z2 holds.** 518 tablets with a depth; 4,600 same-text pairs from 52 texts lie a median 4.2 apart, against 5.2
  shuffled; p = 0.0001.
- **Hypothesis Z holds**: identical tablets were made together, or at least deposited together, more than chance.
  Tally, counting parts: **6 held** (Q1, Q2, X2, Y2, Z1, Z2), 12 failed.
- **What it does to the fifth set:** the effect is small (4 points in level, 1 unit in depth) and needs thousands of
  pairs to show. The seal-name test (V) had 36 and 71 pairs and a null band of 33-61%; it could not have seen an
  effect this size. V's failure is therefore no evidence that names were handed on; the earlier reading ('the names
  look handed on') is withdrawn to 'not tested with enough power'.
- Unregistered comparison: at Harappa the few same-name seal pairs do share a level (3 of 4, against 18% shuffled; depth
  1.5 against 4.3 on 5 pairs). Far too few to claim, but the opposite of the Mohenjo-daro picture.

# Tenth set, registered before testing (24 September 2026)

**Hypothesis AA: free signs are sound signs that can be added or left out (phonetic complements).** The eighth set
found that the texts thought to write foreign names lean on 'free' signs, those that combine with many different
neighbours for their frequency (Y2). In logo-syllabic scripts a sound sign added to a word sign to show its
pronunciation is optional, and it usually spells the end of the word. Not looked at before.

Names as in the fourth set (heading removed, ending 740 / 520 kept as the class), from every intact object of the
fuller ICIT corpus, distinct names only. Freedom as in Y2 (residual of log distinct neighbours on log tokens, home
lines). An insertion pair: two names with the same ending, one equal to the other with exactly one sign added.

**AA1 The optional sign is free.** Over insertion pairs, the added sign's freedom exceeds that of a sign drawn at random
from the other positions of the longer name (paired permutation: swap the added sign with a random other sign of the
same name, 10,000 times), p < 0.05. Signs without a freedom score (under 5 home tokens) and numerals are left out.

**AA2 It stands at the end of the word.** The added sign is the last sign of the name (directly before the ending) more
often than a random position of the longer name would be, p < 0.05 (exact, from each pair's 1 / length).

Hypothesis AA holds if both hold.

## Results of the tenth set (added after the test; `predict_test10.py`, `results/predict_test10.md`)

912 distinct names; 310 insertion pairs (one name = another plus one sign, same ending).

- **AA1 holds, weakly.** The added sign is freer than the other signs of the same name: +0.061 against +0.009 (236
  pairs), paired permutation p = 0.016. A small effect.
- **AA2 fails, the other way.** The added sign is the last sign of the name in 98 of 310 pairs (32%) against 44%
  expected from position alone. It is the *first* sign in 195 (63%), inside in 17. (Front position was not registered;
  it is reported, not claimed as a test.)
- **Hypothesis AA fails** as registered. Tally, counting parts: 7 held (Q1, Q2, X2, Y2, Z1, Z2, AA1), 13 failed.
- What it shows: names grow at the front. The commonest added signs are 240, 235 (the roofed fish), 176, 803, the long
  stroke 31, 220, 233, 760: fish-series signs, numerals and name-initial first elements, i.e. an attribute put before
  a head, which is the head-final compound the first held predictions (Q1, Q2) describe. That is modification, not a
  phonetic complement spelling a word's end. The optional signs being slightly freer fits attributes (they attach to
  many heads) as well as sound signs, so AA1 does not separate the two.

# Eleventh set, registered before testing (24 September 2026): replications and a known-answer control

The two leads of the last five sets are X2 (the 30 bound pairs are never split by a seal's line break) and Y2 (West
Asian texts use 'free' signs). Before either is used to shortlist sound signs they must replicate on material they were
not found on, and freedom must be shown to pick out sound signs in a script where the answer is known.

**RB Bound pairs, M77.** In the M77 texts absent from the ICIT-derived corpus (data/corpus_m77_added.tsv; Mahadevan's
own line division, signs mapped to ICIT numbers), with 2+ lines: gaps inside the 30 bound pairs of the seventh set are
line breaks less often than other gaps, Fisher p < 0.05, with lines as listed and with lines reversed (both required).

**RF1 Freedom is a property of the sign.** Freedom (as Y2) computed from home seals alone and from home tablets alone,
over signs with 5+ tokens in each: Spearman correlation > 0, p < 0.05 (permutation).

**RF2 The West Asian effect with independent freedom.** Freedom computed only from the M77-added texts; West Asian
tokens (as Y2) against length-matched home draws: higher mean freedom, p < 0.05.

**RC Linear B control.** On Linear B (DAMOS lines; words split into syllabograms, word dividers removed, word signs and
measure signs as single tokens, numerals as one token 'N'), freedom computed the same way (signs with 5+ tokens):
syllabograms have higher freedom than word signs (logograms, ideograms, measure signs), Mann-Whitney one-sided p <
0.05. If RC fails, freedom is not shown to detect sound signs and no shortlist will be drawn from it.

## Results of the eleventh set (added after the test; `predict_test11.py`, `results/predict_test11.md`)

- **RB holds.** On 362 M77 multi-line texts (Mahadevan's own line division), gaps inside the 30 bound pairs are line
  breaks 1 time in 155 (0.6%), other gaps 386 of 1,621 (23.8%); Fisher p < 0.0001, the same with lines reversed. X2
  replicates on a larger, independently lined sample. (Some M77 objects may be the seventh set's seals under another
  transcription; the seventh set had 66 multi-line seals, M77 362.)
- **RF1 holds.** Freedom from home seals and from home tablets agree: Spearman 0.34 over 100 signs, p = 0.0008. It is
  a property of the sign, though a noisy one.
- **RF2 holds.** With freedom computed from the M77 texts alone, West Asian tokens +0.217 against +0.056 for home draws,
  p = 0.001. Y2 replicates with independent scores.
- **RC holds.** In Linear B (10,885 lines, dividers removed) syllabograms are freer than word signs: +0.240 against
  -0.218, AUC 0.77, p = 0.0001. Freedom detects sound signs in a script where the answer is known. Caveat: Linear B's
  word signs stand mostly in lists before numerals; the Indus texts are not lists, so the contrast may be weaker there.
- Tally, counting parts: 11 held, 13 failed.

A shortlist was then drawn (`sound_shortlist.py`, `results/sound_shortlist.md`; derived, not a test): signs free (z > 0)
in every one of the three sources that score them (home seals, home tablets, M77), 2+ sources. On Linear B with
Knossos and Pylos as the sources the same rule selects 47 signs, 96% of them syllabograms (all of the top 20), and
misses 36 of 81 syllabograms. On the Indus corpus it selects 46 of 189 signs (numerals, openers, endings left out); 34
are free on both sides. Top: 741, 742, 745 (the jar with strokes; variants of the 740 ending, i.e. grammatical
elements, which logo-syllabic scripts usually spell by sound), 455, 365, 140, 315, 440, 125, 717, 111, 368, 480, 892.

# Twelfth set, registered before testing (24 September 2026): testing the candidate sound-sign shortlist

The shortlist (`results/sound_shortlist.md`, 46 signs) was drawn from home texts only. If its signs are sound signs:

**SL1 Foreign names are spelled with them.** Of West Asian sign tokens (740, 520, openers and numerals left out), the
share that are shortlist signs exceeds length-matched home draws (10,000), p < 0.05. Not independent of Y2 / RF2 (the
list rests on the same measure); it checks the discrete list, and a failure would count against it.

**SL2 Swapping one candidate for another gives a variant of the same name.** Substitution pairs: two distinct names
(fourth-set definition, every intact object of the fuller corpus) with the same ending and length, differing at exactly
one position. Candidate pairs: both swapped signs on the shortlist; other pairs: at least one not. Candidate pairs share
a findspot (a site where both names occur) more often than other pairs, with the labels permuted within strata of the
rarer name's object count (1, 2, 3+), 10,000 times, p < 0.05.

**SL3 The same, for object type**: candidate pairs share an object type (SEAL / TAB / TAG / other) more often, same
permutation, p < 0.05.

The shortlist is judged supported if SL2 or SL3 holds as well as SL1.

## Results of the twelfth set (added after the test; `predict_test12.py`, `results/predict_test12.md`)

- **SL1 fails.** Shortlist signs are 18 of 60 West Asian tokens (30%) against 32% in length-matched home draws
  (p = 0.63). The foreign texts' higher mean freedom (Y2, RF2) does not come from the listed signs; it must come from
  signs below the cut or from their avoiding the least free ones.
- **SL2 fails.** 4,050 substitution pairs among 912 names, 194 of them swaps between two listed signs. Candidate pairs
  share a site 46% of the time, other pairs 49% (p = 0.90).
- **SL3 fails.** Share an object type: 61% against 57% (+4.8 points, p = 0.18).
- **The shortlist is not supported.** Its commonest swaps are within the fish series (220 / 233 / 231, 798 / 803):
  signs free on one side only, which behave as name heads, not sound signs. Freedom stays a real, replicated property
  of signs (RF1, RC) and the foreign texts do lean on free signs (Y2, RF2), but cutting it into a list of 'sound signs'
  did not survive its first tests. Tally, counting parts: 11 held, 16 failed.
- If the list is revisited: a narrower cut (free on both sides only, fish series and 740-name heads left out) must be
  registered as a new list and tested on material not used to make it, not tuned on these results.

# Thirteenth set, registered before testing (24 September 2026): ten hypotheses

None of these has been looked at. Samples: **A** = the ICIT-derived corpus (data/corpus.tsv), **B** = the M77 texts
absent from it (data/corpus_m77_added.tsv), each read line by line (lines of 2+ signs); **F** = the fuller ICIT corpus
(icit_full.py, lines as listed), used where site, object type or findspot is needed. 'Names' as in the fourth set.
Grammar signs: 740, 520, 817, 820, 861, 90, 400 and the stroke numerals (numerals.NUMS). Every permutation test uses
10,000 draws; a test holds at p < 0.05, and where A and B are both named it must hold in both.

**H1 Doubling means plurality.** Signs written doubled (X X adjacent 2+ times in the sample; not numerals) mark
countable nouns, so, like counted nouns, they are preceded by a stroke numeral more often than frequency-matched
signs never written doubled (signs with 20+ tokens; labels permuted within token-count quintiles). A and B.

**H2 Compounds have a fixed order.** For ordered pairs X Y (X ≠ Y) with count 10+, the reversal ratio count(Y X) /
count(X Y) is lower for the 30 bound pairs of the seventh set than for the other pairs (difference in mean rank,
permutation of the bound label). A and B.

**H3 Diacritics modify a base sign without changing its word class.** Pairs within a graphic family (fish 219-244 as
signs.FISH; jar 740 / 741 / 742 / 745; fig signs.FIG; crab signs.CRAB; eye signs.EYE), both signs 10+ tokens, have
more similar contexts (cosine of positive-PMI left + right neighbour vectors) than random pairs matched on the two
signs' token-count quintiles. A and B.

**H4 Name signs vary with distance, grammar does not (dialects or local names).** F, home sites with 40+ intact
texts, fixed coordinates. Jensen-Shannon divergence between sites' name-sign distributions, rarefied to the smallest
site's token count (200 rarefactions), correlates with geographic distance (Mantel, Spearman, site-label permutation),
rho > 0, p < 0.05; and the same correlation for grammar signs is lower than for name signs.

**H5 Frequent signs are simpler (a law of writing systems).** Perimetric complexity (perimeter² / ink area) of each
glyph rendered from the ICIT font correlates negatively with log token count (Spearman, permutation), signs with a
glyph and 5+ tokens. A and B.

**H6 Tablets and sealings record transactions between parties.** Texts with two or more ending tokens (740 / 520) are
more frequent on tablets and sealings (TAB, TAG) than on seals, within text-length strata (3-4, 5-6, 7+ signs),
object labels permuted within strata. F, intact objects.

**H7 Names are built head-final from shorter names.** For names with 3+ signs before the ending, the name minus its
first sign (same ending) is an attested name more often than the name minus its last sign is (any ending); McNemar
one-sided, p < 0.05. A and B.

**H8 Attributes are local, heads are general.** The first sign of a 2+ sign name (attribute) carries more information
about the site than the last (head): excess mutual information with site (observed minus the mean under site
permutation among names) is higher for the first sign than for the last, p < 0.05 on the permuted difference. F.

**H9 Graphic variants are local writing habits.** The 30 candidate variant pairs of results/allographs.md, where both
signs have 10+ tokens with a home site in F: Cramér's V of site (Mohenjo-daro / Harappa / other) against which variant
is written is higher than for random sign pairs matched on token counts (mean over the set, permutation), p < 0.05.

**H10 Heads come from a smaller inventory than attributes.** Among names of 2+ signs before the ending, the entropy
of the last sign is lower than the entropy of the first sign, by more than in within-name shuffles of sign order
(p < 0.05). A and B.

## Results of the thirteenth set (added after the test; `predict_test13.py`, `results/predict_test13.md`; robustness checks after the test in `robust13.py`, `results/robust13.md`)

Five held, five failed.

- **H1 fails, narrowly, twice.** Doubled signs are preceded by a numeral more often (A 23.4% against 17.5%, p = 0.086;
  B 25.7% against 12.9%, p = 0.059). Right direction in both samples, short of the bar in both.
- **H2 fails.** Bound pairs are reversed rarely (mean ratio 0.027 A, 0.016 B), but so are most frequent pairs once
  ranked (p = 0.22, 0.41): Indus sign order is fixed generally, not specially inside bound pairs.
- **H3 holds** (context cosine within graphic families 0.117 A, 0.208 B; p = 0.0001 both). Check: without the fish
  family, A 0.056 (p = 0.12), B 0.112 (p = 0.04, 3 pairs). The result is mostly the fish series, already known to act
  as one class (Q2); for jar, fig, crab and eye it is not shown.
- **H4 fails.** Name-sign divergence vs distance: rho 0.31, p = 0.12 (6 sites, 15 pairs). Grammar signs: rho 0.45,
  p = 0.037, the reverse of the prediction: endings and numerals vary more with distance than name signs do. Six sites
  give little power; the grammar result is a lead (regional numeral or ending habits), not a finding.
- **H5 holds.** Frequent signs are graphically simpler: Spearman -0.13 (A, 221 signs, p = 0.025), -0.21 (B, 128
  signs, p = 0.010). The Indus script follows the law found in other writing systems (frequency favours simpler forms).
- **H6 fails.** Texts with two endings are not more common on tablets and sealings (4 of 948) than on seals (23 of
  1,316); tablets rarely carry endings at all.
- **H7 holds.** A long name minus its first sign is an attested name more often than minus its last (A 60 against 27,
  p = 0.0003; B 18 against 8, p = 0.038): names grow at the front from existing names, head-final. Check: without
  numeral-initial names, A 40 against 19 (p = 0.004), B 14 against 8 (p = 0.14): numerals as attributes carry part of
  it.
- **H8 holds as registered but is not robust.** First sign tells more about the site than the last (0.564 against
  0.384 bits, p = 0.0001). Checks: seals only p = 0.14; one name per site p = 0.12; both p = 0.19. The registered
  result rests on repeated texts (Harappa tablet batches); not claimed.
- **H9 fails.** Candidate graphic variants are not more site-dependent than random pairs (V 0.212, p = 0.75): the
  look-alike pairs are not regional writing habits; either distinct signs or variants used everywhere.
- **H10 holds, robustly.** The last sign of a name comes from a smaller inventory than the first (A 5.86 against 6.44
  bits, B 5.24 against 5.72; shuffle p = 0.0001 both; without numeral-initial names p = 0.0005, 0.0035). Heads are a
  more restricted class than attributes, as nouns of office or kind would be against a freer set of modifiers.

Tally, counting parts: 16 held, 21 failed (37 registered). Of the five that held, H5 and H10 are robust, H7 partly,
H3 reduces to the fish series, H8 does not survive the checks.

# Fourteenth set, registered before testing (24 September 2026): fifteen hypotheses toward the language and the sign classes

Samples and conventions as the thirteenth set (A, B, F; names; 10,000-draw permutations; p < 0.05; A and B both where
named). Picture categories are Fairservis's (results/sign_list.tsv, 'fairservis' column, letter before the dash): A
humans; C, D animals and animal parts; E plants; F sky and weather; G enclosures and structures; H weapons; I
implements; J containers; K measures and devices; L cloth and ornaments; M drums; N landscape and settlement; O
number-like forms; P affix strokes; Q fish-like signs. They are one scholar's identifications, used as an outside label,
not as readings. Head class: signs with 10+ tokens inside names (sample A) that are the name's last sign in 60%+ of
those tokens; attribute class: first sign in 60%+.

**K1 A rational class (Dravidian 'high caste' gender).** Names whose head (last sign) is a human figure (A) take 740
more often than names with any other head; Fisher one-sided. A and B.

**K2 A non-rational class.** Names whose head is a natural thing (C, D, E, F, N; fish Q left out) take 520 more often
than names whose head is a human or an artefact (A, G, H, I, J, K, L, M); Fisher one-sided. A and B.

**K3 Occupational titles.** Tools and weapons (H, I, K) stand as the head (last) rather than first more often than the
other categorised signs do: ratio last / first tokens, Fisher one-sided on the 2 x 2 of (tool, other) x (last, first).
A and B.

**K4 Attributes agree with the class (as in Indo-Aryan gender agreement; Dravidian adjectives do not agree).**
Conditional mutual information between the first sign and the ending, given the last sign, exceeds its value with
endings permuted within last-sign groups. A and B. If it fails, that fits Dravidian and counts against Indo-Aryan
agreement, without proving either.

**K5 Foreign names have no native title.** West Asian lines end in a head-class sign less often than length-matched
home draws. F.

**K6 A genitive on possessions.** Pot inscriptions (POT) that contain an ending have a further sign after it (the
740 + 90 / 400 / 151 pattern) more often than seal texts with an ending, within length strata (2-3, 4-5, 6+). F.

**K7 Titles are known everywhere.** On seals (distinct objects), head-class signs are found at more distinct sites than
attribute-class signs with a matched token count (quintiles; permutation of the class label). F.

**K8 Titles last, attributes change.** Mohenjo-daro seals, Early + Intermediate against Late: divergence (JSD,
rarefied to equal counts) of the last-sign distribution is smaller than that of the first-sign distribution, beyond
the period-label permutation. F.

**K9 Grammar signs vary with distance (replication of the H4 lead, more sites).** Home sites with 20+ intact texts and
known coordinates: Mantel rho between grammar-sign JSD (rarefied) and distance > 0. F.

**K10 Doubling marks plurality (replication of H1 on the fuller corpus).** As H1, on F's intact lines. (F overlaps A
in objects; it is a different transcription.)

**K11 Heads are drawn more elaborately (word signs).** Mean perimetric complexity (as H5) of name-final tokens exceeds
that of name-initial tokens, beyond within-name shuffles. A and B.

**K12 Free signs are simpler (sound signs are plain).** Freedom (as Y2, from the sample) correlates negatively with
complexity, both residualised on log tokens (Spearman, permutation). A and B.

**K13 Fish names are sky names (Parpola's 'fish = star').** Names with a fish head (Q category, or signs.FISH) have a
sky sign (F category) inside them more often than names with other heads; Fisher one-sided. A and B.

**K14 Places are local.** On seals, the presence of an enclosure / landscape sign (G, N; 861 left out) in a text is
more site-dependent (Cramér's V, site grouped MD / Harappa / other) than the presence of signs of other categories
matched on frequency. F.

**K15 The sign after the ending is a person ('X's man').** Names followed by 90 (Fairservis A-1 'a man') after their
ending take 740 more often than names followed by any other sign or by nothing; Fisher one-sided. A and B.

## Results of the fourteenth set (added after the test; `predict_test14.py`, `results/predict_test14.md`)

One held, fourteen failed. (K11 first stopped on a sign without a glyph; the filter was corrected to names whose
signs all have a glyph, as the registered shuffle requires, and the whole set rerun with the same seed.)

- **K1 holds**: names whose head is a human figure take 740 in 81 of 82 (A) and 29 of 29 (B), against 83% and 88%
  (p < 0.0001, p = 0.031). Narrow: the heads are almost all sign 100 (Fairservis 'a man with horns'; 73 of 82 in A, all
  29 in B), with 142 ('a man with a staff') 8 times.
- **K15 fails as registered, but points the same way**: the 'man' sign 90 after an ending follows 740 in 79 of 79 (A,
  p < 0.0001) and 17 of 17 (B, p = 0.14; too few for B alone). Across both, 96 of 96, never after 520. With K1: the
  human-figure signs go only with 740. That fits 740 as the class of persons (Mahadevan's reading of the jar as a
  masculine / rational suffix, Dravidian -an), and it is the only meaning-linked result that has held here. It is
  consistent with that reading, not proof of it: a jar sign marking 'person' could be a word as well as a suffix.
- **K2 fails** (natural heads do not take 520: 2% against 5%): the 520 class is the fish class, not 'things of nature'.
- **K3 fails** (tools as heads: A 45% against 49%; B 67% against 40%, p < 0.0001): contradictory samples.
- **K4 fails** (attribute-ending dependence given the head: A 0.146 bits, p = 0.0001; B 0.059, p = 0.34): agreement
  shows in A only. Not evidence for Indo-Aryan agreement; not clean evidence against it.
- **K5 fails** (foreign lines end in a head-class sign 22% against 24%).
- **K6 fails** (pots: 2 of 24 lines with a sign after the ending, seals 159 of 897): no genitive on pots.
- **K7 fails** (heads at 5.4 sites, attributes 5.3).
- **K8 fails narrowly** (Mohenjo-daro Early + Intermediate against Late: first signs diverge 0.466, last signs 0.260;
  p = 0.052): heads look steadier than attributes over time, short of the bar.
- **K9 fails** (grammar-sign drift with distance, 7 sites: rho 0.28, p = 0.12): the H4 lead does not replicate.
- **K10 fails** (doubling and numerals on F: 19.8% against 17.3%, p = 0.30): the H1 near-miss does not replicate.
- **K11 fails** (heads not more complex than attributes).
- **K12 fails narrowly** (free signs simpler: A rho -0.16, p = 0.010; B -0.14, p = 0.061).
- **K13 fails** (fish-headed names carry a sky sign no more often: 17% against 17%; B 6% against 15%): no support for
  'fish = star' from the company fish signs keep.
- **K14 fails** (enclosure / landscape signs are not more site-bound).

Tally, counting parts: 17 held, 35 failed (52 registered).

# Fifteenth set, registered before testing (24 September 2026): ten hypotheses on morphology and sound signs

Built on what has held: names = attributes + head + ending (Q1, Q2, H7, H10); human heads take 740 and the 'man'
sign 90 follows only 740 (K1, K15); bound pairs are words (X2, RB); foreign names lean on free signs (Y2, RF2).
Conventions as the thirteenth set (A, B, F; names; head class as K; freedom as Y2, computed within each sample;
10,000-draw permutations; p < 0.05; both A and B where named).

**N1 740 is a bound suffix, not a word.** A word can be counted; a suffix cannot. The share of 740 tokens directly
preceded by a stroke numeral is under one third of the same share for head-class signs. A and B.

**N2 520 is a bound suffix.** The same test for 520. A and B.

**N3 741 is an inflected (oblique / genitive) form of the person class.** Fairservis reads 741 as the jar with the
genitive stroke. If 'X-741 Y-740' is 'X's Y', the material after a non-final 741 up to the ending is itself an attested
name body (same ending) more often than the material after a random other non-final position in the same texts
(paired; exact sign test on discordant texts). A and B.

**N4 Rare names are spelled by sound.** Names occurring once (in the sample) have a higher mean freedom of their
non-grammar signs than names occurring 2+ times, within name-length strata (label permutation). A and B.

**N5 Bound pairs are word sign + sound complement.** In the 30 bound pairs of the seventh set, the second sign is
freer than the first more often than not (exact sign test, pairs where both are scored). A and B.

**N6 Tablets carry the names that seals carry.** Distinct tablet texts (F, TAB, 2+ signs) equal a seal name body
(the name without its ending; F seals) more often than the same tablet texts with their sign order shuffled.

**N7 Titles belong to persons.** Lines with the heading (817 / 820 / 861 + 2 / 60 / 1) end in 740 rather than 520
more often than headless lines with an ending, within length strata (4-5, 6-7, 8+ signs). Fisher / permutation. A
and B.

**N8 One set of sound signs.** The signs over-represented in West Asian texts (log ratio of their share there to their
share at home, F) are the same signs over-represented in rare names (log ratio of their share in once-only names to
their share in recurring names, sample A): Spearman > 0 over signs with 5+ tokens in both comparisons (permutation).

**N9 400 after the ending marks plural.** Names followed by 400 contain a stroke numeral before the ending more often
than names with the same ending and no 400. A and B.

**N10 The 'man' sign is a noun, not repeated after a human head.** Names whose head is a human figure (Fairservis A)
are followed by 90 less often than other 740 names. Pooled A + B (B alone is too small; decided here, before testing).

## Results of the fifteenth set (added after the test; `predict_test15.py`, `results/predict_test15.md`; check after the test `robust15.py`, `results/robust15.md`)

One held, nine failed.

- **N4 holds, and survives the check.** Names found once use freer signs than recurring names, length-matched (A
  +0.228, B +0.120; p = 0.0001, 0.0004). Checked for the obvious artefact (a repeated name repeats its own neighbours
  and so lowers its signs' freedom): with freedom from distinct lines only, +0.112 (p = 0.0002) and +0.053 (p = 0.022);
  with freedom from texts that contain no name at all, +0.097 (p = 0.002) and +0.057 (p = 0.050). Smaller, still
  there. Rare names, like foreign ones (Y2, RF2), lean on free signs: two independent signs of phonetic spelling for
  names that had no stock form. It says which kind of sign to look at for sound values; it assigns none.
- **N1 fails, narrowly.** 740 is preceded by a numeral in 6.9% (A) and 5.7% (B) of its tokens, head-class signs 18.1%
  and 10.5%: counted less than heads, but above the registered third in both samples. Not shown to be a suffix.
- **N2 fails, the other way.** 520 is preceded by a numeral in 22.4% and 21.9% of its tokens, more than the heads
  (18.1%, 10.5%). 520 is counted like a noun, not bound like a suffix: '3 + 520', '2 + 520'. The two endings do not
  behave alike: 740 is rarely counted, 520 often. Fairservis calls 520 'a point or spear'; a countable unit or object
  fits better than a class suffix.
- **N3 fails** (A: the tail after 741 is an attested name 46 of 98 times against 18 for a random position, p = 0.0001;
  B: 3 of 22 against 9, the reverse). Holds in one transcription only.
- **N5 fails** (the second sign of a bound pair is not the freer one: 12 of 30, 15 of 27).
- **N6 fails** (3 of 549 tablet texts equal a seal name body; no more than shuffled order): tablets do not carry the
  seal names.
- **N7 fails** (headed lines end in 740 83% and 81%, headless 85% and 89%): the heading is not tied to the person class.
- **N8 fails** (West Asian enrichment and rare-name enrichment do not rank signs alike, rho 0.03): the two phonetic
  tendencies do not yet point at the same individual signs; the West Asian sample (92 tokens) is too small to rank
  signs.
- **N9 fails, the other way** (names followed by 400 contain a numeral less often: 26% against 42%, 12% against 29%).
  400 is not a plural agreeing with numerals.
- **N10 fails** (human-headed 740 names are followed by 90 as often as others: 6.4% against 5.8%).

Tally, counting parts: 18 held, 44 failed (62 registered).

# Sixteenth set, registered before testing (24 September 2026): twenty-five hypotheses on the leads

Leads: rare and foreign names lean on free signs (N4, Y2, RF2); 520 is counted like a noun, 740 rarely (N2, N1);
scribes keep bound pairs whole across line breaks (X2, RB). Conventions as the thirteenth set (A, B, F; names; head
and attribute classes as K; freedom as Y2 within the sample; numerals = numerals.NUMS, 'long' = its long-stroke kind;
10,000-draw permutations; p < 0.05; both A and B where named). 'Once-only' = a name occurring once in its sample. The
candidate set C = signs in the top quartile of freedom computed from sample A's lines that contain no name (grammar
signs left out); C is fixed from A and tested elsewhere. M = the M77 multi-line texts of RB; M tests must hold with
lines as listed and reversed.

Sound-sign lead
- **P1** Per-sign enrichment in once-only names (log ratio of token share, once-only against recurring) agrees between
  A and B: Spearman > 0 over signs with 5+ name tokens in both.
- **P2** C is enriched in B's once-only names against its recurring names, more than random sign sets matched on B
  token-count quintiles.
- **P3** C is enriched in West Asian texts against home texts (F), more than matched random sets.
- **P4** C signs have higher positional entropy in B's names (first / inside / last) than matched random sets.
- **P5** Once-only names contain a non-adjacent repeated sign (numerals aside) more often than recurring names,
  length-stratified (3, 4, 5+). A and B.
- **P22** Once-only names contain a bound pair (seventh set) less often than recurring names, length-stratified. A, B.
- **P23** Once-only names end in a head-class sign less often than recurring names, length-stratified. A and B.
- **P24** C signs are graphically simpler (H5 complexity) than matched random sets (A quintiles).
- **P25 Control: the rare-name effect is not special to the Indus script.** In Linear B (DAMOS; words by the word
  dividers; freedom from lines with dividers removed, as RC), syllabograms of words occurring once are freer than those
  of recurring words, length-stratified (2, 3, 4+ syllables). If P25 holds, N4 is a general frequency effect and no
  evidence of sound spelling.

520 and 740
- **P6** Numerals directly before 520 are long-stroke more often than numerals before other signs. A and B.
- **P7** Ending lines on tablets and sealings end in 520 (rather than 740) more often than on seals, length-stratified.
  F.
- **P8** 520 is followed by more name material (a sign other than 90 / 400 / 151, not line end) more often than 740 is.
  A and B.
- **P9** Names ending 520 contain a numeral away from the ending (not the last body sign) more often than 740 names,
  length-stratified. A and B.
- **P10** Human heads (Fairservis A) are preceded by a numeral less often than other head-class signs. Pooled A + B.

Numerals and variants
- **P11** Pairs of distinct Harappa tablet texts differing at one position differ at a numeral more often than a random
  position of the pair holds a numeral. F.
- **P12** Seal name bodies differing at one position differ at a numeral less often than such tablet pairs do (Fisher).
  F.
- **P13** At Harappa, name heads are steadier than attributes between earlier and later levels (HARP 3B and Vats
  Strata IV-VII against HARP 3C and Vats I-III): JSD of first signs minus JSD of last signs > 0, label permutation. F.

Order inside names
- **P14** In 3-sign name bodies the two attribute slots hold different signs: MI(sign; slot 1 or 2) exceeds its value
  with the two attributes swapped at random per name. A and B.
- **P15** A numeral stands before the other attributes: in bodies of 3+ signs with one numeral and at least one other
  attribute before the head, the numeral is first more often than not (sign test). A and B.
- **P21** Attribute-class signs are freer than head-class signs (matched on token quintiles). A and B.

Units the scribes kept together (M, Fisher on break rates)
- **P16** Numeral + fish (signs.FISH) pairs are broken by a line less often than other gaps.
- **P17** Ending + post-ending sign (740 / 520 followed by 90 / 400 / 151) is broken less often than other gaps.
- **P18** Head + ending (the gap before 740 / 520 at a name's end) is broken less often than other gaps.
- **P19** Inside names, the gap before the head is broken more often than the other name-internal gaps (attribute and
  head are separate words).
- **P20** The gap after the heading is broken more often than other gaps (the heading is a separate word).

## Results of the sixteenth set (added after the test; `predict_test16.py`, `results/predict_test16.md`; checks after the test `robust16.py`, `results/robust16.md`)

Thirteen held, twelve failed. The control decides how the sound-sign lead is read.

**Sound-sign lead: withdrawn.**
- **P25 holds (control).** In Linear B, whose signs are all syllabic, syllabograms of words found once are freer than
  those of recurring words (+0.023, p = 0.0001; 2,440 and 1,305 word types). As registered, the rare-name effect (N4)
  is a general frequency effect of any corpus and no evidence of sound spelling. N4's phonetic reading is withdrawn.
- P1 (rare-name enrichment of individual signs agrees between A and B, rho 0.58), P2 (the candidate set C is enriched
  in B's once-only names, p = 0.036), P22 (once-only names contain fewer bound pairs, +12 points both samples) and P23
  (fewer end in a head-class sign, +12 and +15 points) hold; all four are what a frequency effect predicts (a name used
  once is built from less common pieces), so none is claimed as phonetic evidence.
- P3 fails (C is not enriched in West Asian texts, 0.030, p = 0.27), P4 fails (C not position-free), P5 fails (once-only
  names do not repeat signs more), P24 fails (C not simpler). The free-sign idea has no support left beyond the
  foreign-text effect (Y2, RF2), which P3 does not reproduce with C.

**520: counted, but in one fixed way.**
- **P6 holds**: numerals before 520 are long-stroke 92% (A) and 94% (B), against 33% and 51% before other signs. Check:
  they are almost all the long 3 (sign 33: 45 of 52 in A, 12 of 16 in B). 33-520 is one fixed expression (a bound pair
  of the seventh set). The fifteenth set's 'N2: 520 is counted like a noun' is corrected to: 520 is preceded by one
  numeral form, the long three, as a fixed unit; it is not freely counted.
- P7 fails (520 lines not commoner on tablets and sealings, the reverse), P8 fails (A 8% against 9%; B 18% against 9%),
  P9 fails (A +2.9, B +12.2 points).

**Numerals and variation.**
- **P11 holds**: distinct Harappa tablet texts that differ at one position differ at a numeral in 29% of 467 pairs,
  more than a random position (p = 0.0001).
- **P12 holds**: seal names that differ at one position differ at a numeral in 13% of 1,994 pairs, against 29% for
  tablets (p < 0.0001). Tablets vary in their numbers, seal names in their words: tablets look like records of counts.
- **P10 holds**: human heads are preceded by a numeral less often than other heads (13.0% against 18.8%, p = 0.001).
- P15 fails (a numeral stands first among the attributes in only 68 of 281 and 15 of 60; the reverse of the
  prediction: numerals stand next to the head, as R1 found).

**Order and stability inside names.**
- **P13 holds**: at Harappa the heads are steadier than the attributes between earlier and later levels (JSD first
  minus last +0.125, p = 0.032). With K8 at Mohenjo-daro (+0.206, p = 0.052), heads are the stable part of names.
- **P14 holds**: in three-sign names the two attribute slots hold different signs (MI 0.520 and 0.556 bits, p = 0.0001
  both): names have fixed slots, not free strings of modifiers.
- P21 fails (attributes are not freer than heads).

**Units kept together across line breaks (M77 multi-line texts, both line orders).**
- **P17 holds**: an ending and the sign after it (740 / 520 + 90 / 400 / 151) are split 1 of 87 and 0 of 86 times
  against 23% of other gaps.
- **P18 holds**: a head and its ending are split 1.2% and 3.9% against 25%. Check: without numeral + ending gaps,
  1.3% and 2.5%; 740 alone 1.4% and 2.8% (p < 0.0001). Scribes treated the name and its ending as one unit, as they
  would a word and its suffix; with N1 (740 counted far less than heads) it leans toward 740 being bound.
- P16 fails (numeral + fish: 12.2% as listed, p = 0.09; 2.7% reversed): short of the bar in one order.
- P19 fails (the gap between attributes and head is not a preferred break) and P20 fails (nor is the gap after the
  heading): the scribes did not break lines at word boundaries inside names, only avoided breaking the bound units.

Tally, counting parts: 31 held, 56 failed (87 registered). Of the thirteen that held here, four (P1, P2, P22, P23)
are explained by the frequency effect P25 shows, and one (P25) is the control that shows it.

# Seventeenth set, registered before testing (24 September 2026): twenty-five hypotheses on the surviving leads

Leads: tablets vary in their numbers (P11, P12); a head and its ending are one unit (P17, P18); 33-520 is a fixed
expression (P6); names have fixed slots and stable heads (P13, P14, H10); human heads take 740 (K1). Conventions as
the thirteenth set (A, B, F; names; head class as K; 10,000-draw permutations; p < 0.05; both A and B where named).
'Heading' = 817 / 820 / 861 followed by 2 / 60 / 1 at the start of a line. 'Post-ending sign' = 90 / 400 / 151 after
740 / 520. Numeral values from numerals.NUMS. Object types from F: SEAL, TAB (TAB:I incised, TAB:B moulded), TAG,
POT. Unicorn = motif field beginning 'Bull1'. Levels as K8 (Mohenjo-daro) and P13 (Harappa). F seal texts are counted
once per object.

Tablets as records of counts (F)
- **U1** Numerals on tablets have larger values than numerals on seals (mean stroke value; label permutation).
- **U2** On tablets a numeral stands at the edge of the text (first or last sign) more often than on seals, within
  text-length strata (2-3, 4-5, 6+).
- **U3** The sign after a numeral is drawn from a smaller set on tablets than on seals (entropy of the following sign,
  seals minus tablets, label permutation).
- **U4** Incised tablets (TAB:I) carry a numeral more often than moulded ones (TAB:B), length-stratified.
- **U5** Among post-ending signs, 400 is a larger share on tablets, sealings and pots than on seals.

The fixed expression 33-520 (A and B unless said)
- **U6** 33-520 ends its text (nothing after it, or only a post-ending sign) more often than 520 not after 33.
- **U7** The sign before 33-520 is a head-class sign more often than the sign before a 520 not after 33.
- **U8** Name bodies that occur with the closing 33-520 also occur with 740 more often than bodies that occur with a
  plain 520 do (pooled A + B).
- **U9** Among lines ending in 520, 33-520 is commoner on tablets and sealings than on seals (F).
- **U10** 33 | 520 is split by a line break less often than other gaps (M77 multi-line texts, both line orders).

Heads, attributes and slots
- **U11** Across space, heads are steadier than attributes: on seals, JSD of first signs between Mohenjo-daro and Harappa
  exceeds JSD of last signs, beyond site-label permutation (F).
- **U12** Heads select their attributes: MI(first sign; last sign) of 2+ sign names exceeds its value with heads
  shuffled among names. A and B.
- **U13** In three-sign-plus names, slot 2 (next to the head) is steadier over time than slot 1: JSD between earlier
  and later levels, slot 1 minus slot 2 > 0 (Mohenjo-daro and Harappa pooled, level labels permuted within site) (F).
- **U14** Human-figure signs (Fairservis A) stand last in names more often than first, compared with other categorised
  signs (Fisher on last / first counts). A and B.
- **U15** The ending is predictable from the head across transcriptions: a head-to-ending rule learned on A (majority
  ending per head with 3+ names in A) predicts B's endings for those heads with 90%+ accuracy and above the majority
  baseline (binomial p < 0.05).

The heading
- **U16** Headed names are longer (more signs before the ending) than headless names, rank test. A and B.
- **U17** Headed names use a different head inventory than headless ones (JSD beyond label permutation). A and B.
- **U18** Each opener (817, 820, 861) selects its own heads: MI(opener; head) beyond permutation. A and B.
- **U19** The heading is commoner on sealings (TAG) than on seals (F, lines of 3+ signs).
- **U20** The heading is rarer on pots than on seals (F, lines of 3+ signs).

Seals and their owners (F)
- **U21** Unicorn seals carry longer texts than other-animal seals (rank test).
- **U22** Unicorn seals carry the heading more often than other-animal seals, length-stratified.
- **U23** Names are longer in later levels, at both Mohenjo-daro and Harappa (rank test each).
- **U24** Cylinder seals (SEAL:C, SEAL:CY, the Mesopotamian form) omit the endings more often than square seals,
  length-stratified.
- **U25** The post-ending sign depends on the site: MI(site; post-ending sign) on seals exceeds site-label
  permutation (Mohenjo-daro / Harappa / other).

## Results of the seventeenth set (added after the test; `predict_test17.py`, `results/predict_test17.md`; checks after the test `robust17.py`, `results/robust17.md`)

Twelve held, thirteen failed.

**Tablets record counts of a measured commodity.**
- **U1 holds** (tablet numerals slightly larger: +0.13 strokes, p = 0.043), **U2 holds** (a numeral at the edge of a
  tablet text 11 points more often than on seals, p = 0.0001), **U3 holds** (the sign after a numeral comes from a far
  smaller set on tablets: entropy 2.70 bits lower, p = 0.0001). Check: on tablets 48% of numerals are followed by 700
  (Fairservis J-1 'container used to measure'), nearly all long-stroke (long 3 x140, long 4 x110, long 2 x94); on seals
  numeral + 700 occurs 4 times. The Harappa tablets carry 'N containers' in the long-stroke system; the seal names do
  not. (Numeral + 'pot' as a unit was noted in the earlier Parpola checks; the tablet / seal split is new here.)
- **U5 holds**: after an ending, 400 is the usual following sign off the seals (167 of 220) and rare on seals (15 of 73);
  counting each distinct text once, 78 of 101 against 14 of 71 (p < 0.0001). 400 belongs to tablets and sealings.
- U4 fails (incised and moulded tablets carry numerals alike).

**33-520 is not what was expected.**
- U6 fails narrowly (33-520 ends its text 44 of 45 and 12 of 12, against 90% and 79%; p = 0.083, 0.076), U7 fails (no
  head stands before it: 0 of 57), U8 fails (its stems do not also take 740), U9 fails (it is a seal expression, 27% of
  seal lines ending 520 against 9% on tablets and sealings), U10 untestable (2 cases in M77). 33-520 closes seal texts
  and follows non-head signs: it looks like a closing formula of its own, not a name's ending.

**Heads, attributes, prediction.**
- **U12 holds** (heads select their attributes: MI 3.38 bits in both samples, p = 0.0001 against shuffled heads).
- **U14 holds** (human signs stand last 88% and 93%, other categorised signs 45% and 42%): humans are heads.
- **U15 holds**: a head-to-ending rule learned on A predicts the ending of 483 B names at 95.0% against a majority
  baseline of 88.2% (p = 2e-7). The class rule carries across transcriptions.
- U11 fails (heads not steadier than attributes across space, p = 0.30), U13 fails (slot 2 not steadier than slot 1).

**The heading.**
- **U17 holds** (headed names use other heads: JSD 0.230, p = 0.0004; 0.346, p = 0.031).
- **U20 holds** (pots almost never carry the heading: 3 of 56 lines against 19.6% on seals, p = 0.003).
- U16 fails (headed names are shorter, not longer), U18 fails in B (openers select heads in A only), U19 fails narrowly
  (sealings 29% against 19.6%, p = 0.053).

**Seals.**
- **U21 holds** (unicorn seals carry longer texts: 4.85 against 4.25 signs, p = 0.0002) and **U22 holds** (and the
  heading more often, +5 points, p = 0.042): the unicorn seal goes with fuller, more formal texts.
- **U24 holds**: cylinder seals, the Mesopotamian form, omit the endings (18 of 19 lines). Check: the 8 cylinder seals
  found at Indus sites also all lack an ending, so it is the seal form, not only the find-place, that goes with the
  foreign kind of text.
- U23 fails (names longer in later levels at Harappa, 3.64 against 2.37, p = 0.0001, but not at Mohenjo-daro), U25
  fails (the post-ending sign does not depend on the site).

Tally, counting parts: 43 held, 69 failed (112 registered).

# Eighteenth set, registered before testing (24 September 2026): twenty-five hypotheses on the two genres

Leads: tablets record 'long-stroke N + 700' (U3); 400 after an ending belongs to tablets and sealings (U5); seals carry
names with heads, endings, the heading and the closing formula 33-520 (U6-U9, U17, U21, U22). Conventions as the
seventeenth set (F intact objects; A, B; names; head and attribute classes as K; 10,000-draw permutations; p < 0.05).
'N700' = a text containing a stroke numeral directly followed by 700. 'Count pair' = a numeral followed by a
non-numeral sign. Length strata: 2-3, 4-5, 6+ signs. Unicorn = motif 'Bull1'. Levels as U13 and U23.

What the tablets count (F tablets)
- **W1** The signs of N700 tablets other than numerals and 700 come from a smaller inventory than the signs of other
  tablets (entropy, other minus N700, object-label permutation).
- **W2** One unit per text: N700 tablets contain another count pair (numeral + a sign other than 700) less often than
  other tablets with a numeral (Fisher).
- **W3** N700 is commoner on moulded (TAB:B) than on incised (TAB:I) tablets, length-stratified.
- **W4** At Harappa the share of N700 among tablets depends on the level (MI(level; N700) beyond permutation).
- **W5** On tablets, 700 is preceded by a numeral in 80%+ of its tokens (a measure is always counted).
- **W6** Tablets with 400 carry a numeral more often than tablets without, length-stratified.
- **W7** N700 tablets carry an ending (740 / 520) less often than other tablets, length-stratified.
- **W8** N700 is a Harappa genre: Mohenjo-daro tablets are N700 less often than Harappa tablets (Fisher).
- **W9** N700 tablets carry a head-class sign (the owner or recipient) more often than other tablets,
  length-stratified.
- **W10** N700 texts are issued in batches: among distinct tablet texts, those found on 2+ tablets are N700 more often
  than those found once.

Where sealings and pots belong (F)
- **W11** Sealing (TAG) texts are closer to seal texts than to tablet texts (JSD of sign distributions, rarefied to equal
  counts; the difference beyond 1,000 bootstrap draws of the sealing tokens is > 0 in 95%+).
- **W12** Sealings carry 400 after the ending as tablets do: 400 share among post-ending signs on sealings exceeds that
  on seals (Fisher).
- **W13** Pot lines end in 740 (an owner) more often than tablet lines do, among lines with an ending (Fisher).

Numerals by genre (F)
- **W14** Long-stroke numerals on seals are mostly the 33 of 33-520: over half of seal long-stroke tokens are 33
  before 520.
- **W15** Tiered numerals (two rows) are seal numerals: their share among numerals is higher on seals than on tablets.

The closing formula 33-520 (pooled A + B unless said)
- **W16** The sign before 33-520 comes from a smaller set than the sign before a plain 520 (entropy, label permutation).
- **W17** The sign before 33-520 is an attribute-class sign more often than the sign before 740.
- **W18** Seals ending 33-520 are non-unicorn more often than other seals with an ending (F, Fisher).
- **W19** Lines ending 33-520 lack the heading more often than other lines with an ending, length-stratified.

Persons, titles and animals
- **W20** Names with a human head carry the heading more often than other names, length-stratified (pooled A + B).
- **W21** Seals with a human-headed name are unicorn seals more often than other seals with a name (F, Fisher).
- **W22** The head inventory differs between unicorn and other-animal seals (JSD beyond permutation) (F).
- **W23** Unicorn seals end in 740 rather than 520 more often than other-animal seals, length-stratified (F).
- **W24** Names followed by 90 ('man') are on unicorn seals more often than other seal names (F, Fisher).
- **W25** The heading is commoner in later levels, at both Mohenjo-daro and Harappa (Fisher each) (F).

## Results of the eighteenth set (added after the test; `predict_test18.py`, `results/predict_test18.md`; description after the test `describe18.py`, `results/describe18.md`)

Seven held, eighteen failed. (W16's printed list of preceding signs was wrong in the first run, showing the label
instead of the sign; the statistic was not affected. The script is corrected and the signs are in describe18.md.)

**The Harappa count tokens.**
- **W1 holds** (the other signs on N700 tablets come from a far smaller set: entropy 2.15 bits lower, p = 0.0001), **W2
  holds** (N700 tablets almost never hold a second count pair: 2 of 361, against 79% of other tablets with a numeral),
  **W7 holds** (N700 tablets lack endings: +45 points), **W8 holds** (352 of the 361 are from Harappa: 29% of Harappa
  tablets, 2% of Mohenjo-daro's, p = 3e-30).
- Description: 318 of the 361 are the bare texts 'long 3 + 700' (121), 'long 4 + 700' (108) and 'long 2 + 700' (89);
  the rest add a few signs (413 575 335 711 33 700 ten times). These are count tokens of two to four measures, one
  unit per piece, from Harappa. The class is very likely described in the Harappa excavation reports (Meadow and
  Kenoyer's tablets); the counts here are a check, not a discovery.
- W3 fails (moulded and incised alike), W4 fails (no change between levels), W5 fails narrowly (700 on tablets is counted
  79% of the time against the 80% bar), W6 fails the other way (tablets with 400 carry fewer numerals: 400 belongs to
  the name-bearing tablets), W9 fails the other way (N700 tablets carry fewer head signs), W10 fails (N700 texts are
  not more often duplicated).

**Sealings, pots, numerals.**
- **W11 holds**: sealing texts are closer to seal texts than to tablet texts in all 1,000 draws: sealings are seal
  impressions in content as in form.
- W12 fails (no 400 after the ending on sealings, 0 of 12): U5's '400 off the seals' is a tablet trait, not a sealing
  one.
- W13 fails (pot lines end 740 in 21 of 22, against 86% on tablets; p = 0.18).
- **W15 holds**: tiered numerals are seal numerals (11% of seal numerals, 5% of tablet numerals, p < 0.0001).
- W14 fails (only 9% of long-stroke numerals on seals are the 33 of 33-520).

**The closing formula.**
- **W16 holds**: the sign before 33-520 comes from a tiny set (entropy 2.26 bits below that before plain 520). It is 705
  (37 of 57) or 706 (15): the formula is '705 / 706 + 33 + 520', three signs, both 705-33 and 706-33 being bound
  pairs of the seventh set.
- W17 fails (no attribute before it), W18 fails (not an other-animal seal trait), W19 fails the other way (33-520 lines
  carry the heading more, not less).

**Persons, animals, levels.** W20 fails narrowly (human heads with the heading +5.4 points, p = 0.079), W21, W22, W24
fail, W23 fails narrowly (unicorn seals end 740 +6.2 points, p = 0.053), W25 fails (the heading is commoner later at
Harappa, 14% against 5%, p = 0.0006, but not at Mohenjo-daro).

Tally, counting parts: 50 held, 87 failed (137 registered).

# Nineteenth set, registered before testing (24 September 2026): published readings as predictions, and the formulas

The published keys make claims about single signs that the structure found here can test without sound values:
Fairservis 1992 (keys/fairservis1992_wide.tsv), Mahadevan 1998 / 2014 (keys/mahadevan2014.tsv), Parpola 1994
(keys/parpola1994.tsv; rebus_checks.py READINGS). Conventions as the eighteenth set (A, B, F; pooled A + B where said;
names; head class as K; Fairservis categories; 10,000-draw permutations; p < 0.05).

'Numeral-like' test: the right-neighbour distribution of a sign (counts of the sign that follows it) is compared by
cosine with the pooled right-neighbour distribution of the core numerals (NUMS signs with 20+ tokens in the sample,
the tested sign left out); the sign is numeral-like if its cosine is higher than that of 95% of the non-numeral signs in
its token-count quintile (p = rank among them). Must hold in A and B.

Readings of single signs
- **X1** (Fairservis: 700 = aḷa, a measuring container) On tablets, the numerals directly before 700 are long-stroke in
  90%+ of cases (F).
- **X2** (Fairservis: 706 = nūṟu 'hundred') 706 is numeral-like.
- **X3** (Parpola: 32 = 'space', vel, not a numeral) 32 is numeral-like. If X3 holds, it counts against Parpola's
  reading of 32.
- **X4** (Fairservis: 840 = 'number 8'; Parpola: 840 = 'rings', muruku) 840 is numeral-like. Holding favours
  Fairservis.
- **X5** (Parpola: 13 = 'hearth', cul; here a tiered 3) 13 is numeral-like. Holding counts against Parpola.
- **X6** (Fairservis: 55 = 'rain, twelve strokes'; here the numeral 12) 55 is numeral-like.
- **X7** (Fairservis: 400 = a dative 'of a person') Among post-ending signs, 400 is a larger share after 740 than after
  520 (pooled).
- **X8** (Mahadevan: 520 = non-masculine suffix) Names with a human head take 520 in under 2% of cases (pooled).
- **X9** (Mahadevan: fish names are non-masculine) Names with a fish head (signs.FISH) take 520 in 90%+ of cases
  (pooled).
- **X10** (Mahadevan: the endings are gender suffixes fixed by the noun) Of heads with 5+ names (pooled), 80%+ take
  their majority ending in 90%+ of their names.
- **X11** (Parpola: 740 = the possessive -a) 740 is followed by further name material (a sign other than 90 / 400 /
  151, not line end) in 20%+ of its tokens (pooled): a possessive is followed by what is possessed.
- **X12** (Fairservis: 90 = āḷ, 'ruler') Lines ending 740 + 90 carry the heading more often than lines ending 740
  without 90, length-stratified (pooled).
- **X13** (Fairservis: 861 = 'settlement', 2 = locative: '861 2' = 'in the town') In the heading, 2 follows 861 more
  often than it follows 817 (pooled, Fisher).
- **X14** (705 and 706 alternate in the closing formula) 705 and 706 have more similar contexts (cosine of positive-PMI
  left + right vectors, as H3) than random pairs matched on token quintiles. A and B.

The formulas and the count tokens
- **X15** The text before '705 / 706 + 33 + 520' (heading removed) is an attested name body (with 740 or 520 elsewhere)
  more often than the body minus its last sign of other lines ending in 520 (pooled, Fisher).
- **X16** Tiered numerals stand before fish signs more often than short-stroke numerals do. A and B.
- **X17** Mohenjo-daro tablets count with another unit: the commonest sign after a numeral on Mohenjo-daro tablets is not
  700 and covers 30%+ of those tokens (F).
- **X18** Harappa count tokens with the same value (2, 3 or 4) lie closer in depth than tokens with different values
  (median depth difference, value labels permuted) (F).
- **X19** On count tokens longer than 'N + 700', the signs before the numeral form a seal name body (F seals, any
  ending) more often than the same signs in shuffled order (F).
- **X20** The human head 100 is found at more sites (seals) than head-class signs of matched token count (F).
- **X21** Among fish-headed names, those with a numeral before the head take 520 more often than those without (pooled,
  length-stratified): numbered fish are the star names.
- **X22** Among post-ending signs, 90 is a larger share on seals than on tablets (F).
- **X23** The mix of values (2 / 3 / 4) on count tokens differs between moulded and incised tablets (MI beyond
  permutation) (F).
- **X24** Lines closing in '705 / 706 + 33 + 520' come from Mohenjo-daro more often than other seal lines with an
  ending (F, Fisher).
- **X25** Fish-headed names ending 740 carry the heading more often than fish-headed names ending 520,
  length-stratified (pooled).

## Results of the nineteenth set (added after the test; `predict_test19.py`, `results/predict_test19.md`)

Seven held, eighteen failed. (X14 first stopped because 706 has no tokens in B; the script now records it as not
testable in B, which fails it as registered, and the set was rerun with the same seed.)

**Published readings.**
- **X1 holds** (Fairservis, 700 a measuring container): numerals before 700 on tablets are long-stroke in 348 of 361
  (96%). The structure fits his reading of 700 as a counted measure; it does not confirm his Dravidian value aḷa.
- **X8 holds** (Mahadevan): human heads take 520 in 1 of 111 names. **X9 fails** (fish heads take 520 in only 151 of
  247, 61%): 520 is not a strict gender suffix that fish names always take. **X10 holds** (53 of 63 heads with 5+ names
  take one ending 90%+ of the time); the mixed heads are the fish series (220, 240, 233, 231, 235), 33, 400, 460, 920, 31.
  The endings are fixed by the head for most heads, but not for the fish signs: Mahadevan's gender pair fits the
  person side (740) and not the fish side.
- **X11 fails** (Parpola, 740 the possessive -a): 740 is followed by further name material in 162 of 1,822 tokens (8.9%),
  not 20%. A possessive whose possessed noun is nearly always left out (or is the 90 'man' after it) remains possible;
  a possessive in the ordinary sense is not supported.
- X2-X6 fail (706, 32, 840, 13, 55 are not 'numeral-like' by right-neighbour similarity), but the test is not sensitive:
  it does not recognise 32 as a numeral in A, although 32 is the long 2 of 89 count tokens ('32 700'). These failures
  say little about Fairservis's or Parpola's readings.
- X7 fails (400 does not prefer 740: 17 of 17 post-ending signs after 520 are 400). X12 fails. X13 is degenerate: in
  A and B the opener is followed by 2 in every headed line (179 after 861, 107 after 817).
- X14 fails as registered (705 and 706 share contexts in A, cosine 0.315, p = 0.003, but 706 does not occur in B at
  all: Mahadevan's sign list does not separate it from 705, which itself suggests one sign).

**The formulas and count tokens.**
- **X18 holds**: Harappa count tokens with the same value lie closer in depth (median difference 0.35 ft smaller,
  p = 0.037).
- **X23 holds**: moulded and incised tokens count differently (moulded mostly 3, then 2; incised 4 as often as 3; MI
  p = 0.0001): the two kinds were made for different quantities.
- **X21 holds**: fish-headed names with a numeral before the head take 520 more often (+16.2 points, p = 0.029): the
  numbered fish, Parpola's star names ('3 + fish', '6 + fish'), are the 520 side of the fish series. This is the first
  structural result that sides with Parpola's star-name reading, on the ending rather than on the sound.
- **X22 holds**: 90 after an ending is a seal sign (54 of 73 post-ending signs on seals, 35 of 207 on tablets).
- X15 fails (the text before the closing formula is not more often an attested name: 27% against 18%, p = 0.14), X16
  fails the other way (tiered numerals stand before fish less often than short ones), X17 fails (Mohenjo-daro tablets
  spread their counts over 585, 845, 407, 923 and others; no one unit), X19 fails (the prefixes on longer count tokens
  are not seal names), X20, X24, X25 fail.

Tally, counting parts: 57 held, 105 failed (162 registered).

# Twentieth set, registered before testing (24 September 2026): ten hypotheses

Conventions as the nineteenth set (A, B, F; names; Fairservis categories; M = the M77 multi-line texts, lines as
listed and reversed, both required; 10,000-draw permutations; p < 0.05).

- **Z1 Numbered fish are star names, in each transcription.** X21 (fish-headed names with a numeral before the head
  take 520 more often) holds in A and in B separately, length-stratified.
- **Z2 705 and 706 are one sign.** In A, 705 and 706 share more (left, right) neighbour frames than random sign pairs
  matched on the two signs' token-count quintiles (rank among 10,000 draws).
- **Z3 740 is the class of persons and their occupations.** Categorised heads of 740 names are human figures, weapons,
  implements or measures (Fairservis A, H, I, K) more often than categorised heads of 520 names (pooled A + B, Fisher).
- **Z4 Moulded count tokens were made in one episode per mould.** At Harappa, identical moulded count tokens (TAB:B, same
  text 'N 700') lie closer in depth than identical incised ones (TAB:I): median depth difference of same-text pairs,
  incised minus moulded > 0, type labels permuted among the tokens (F).
- **Z5 90 is a clitic.** In M, 90 begins a line less often than other signs do (share of its tokens that are
  line-initial in non-first lines, Fisher against all other tokens).
- **Z6 400 is a clitic.** The same for 400.
- **Z7 740 is a suffix.** The same for 740.
- **Z8 The value mix of count tokens replicates across excavations.** X23 (moulded and incised tokens carry different
  values) holds separately in the HARP tokens (field 9 = '3') and in Vats's (field 10 'Stratum ...') (F, MI beyond
  permutation each).
- **Z9 Names on tablets are incised.** Incised tablets (TAB:I) carry an ending (740 / 520) more often than moulded
  ones (TAB:B), length-stratified (F).
- **Z10 The head fixes the ending on seals alone.** On F seals (one name per object), 80%+ of heads with 5+ names take
  one ending in 90%+ of them.

## Results of the twentieth set (added after the test; `predict_test20.py`, `results/predict_test20.md`; check after the test `robust20.py`, `results/robust20.md`)

Six held, four failed.

- **Z1 fails**: the numbered-fish result (X21) holds in B (11 of 12 take 520 against 12 of 23, p = 0.008) but not in A
  (49 of 77 against 48 of 85, +10 points, p = 0.14). The one structural result siding with Parpola's star names is
  not replicated in the larger transcription; it is withdrawn to 'suggestive'.
- **Z2 holds**: 705 and 706 share 17 frames, nearly all before 33 after a fish or number sign (220_33, 231_33, 233_33,
  235_33, 240_33, 31_33), p = 0.0001. With M77 not separating them (X14), 705 and 706 are best treated as one sign in
  the closing formula.
- **Z3 holds**: categorised heads of 740 names are humans, weapons, implements or measures in 331 of 818 (40.5%),
  heads of 520 names in 7 of 155 (4.5%). Check without fish heads on either side: 47.4% against 21.9% of 32 (p =
  0.003). The person class holds people and the tools of trades; the other class does not.
- **Z6 holds, Z7 holds**: in M77's multi-line texts, 400 begins a line in 1-2 of 105 tokens and 740 in 3-10 of 233,
  against 19-20% for other signs. Both behave as bound forms that never start a line, as suffixes and clitics do.
  **Z5 fails** for 90 (1 of 12; too few tokens in M77 to test).
- **Z8 holds**: moulded and incised count tokens carry different values in both excavations (HARP p = 0.005, Vats
  p = 0.004), but not in the same way: in HARP the incised tokens are mostly 4, in Vats's mostly 3 and the moulded
  ones rarely 4. The quantities belong to batches or periods, not fixed to the technique.
- **Z10 holds**: on seals alone, 35 of 43 heads (81%) take one ending in 90%+ of their names; the exceptions are again
  the fish series (220, 233, 240, 231, 235), 460, 400 and 920.
- Z4 fails (identical moulded tokens do not lie closer together than identical incised ones), Z9 fails (incised
  tablets do not carry endings more often than moulded ones).

Tally, counting parts: 63 held, 109 failed (172 registered).

# Twenty-first set, registered before testing (24 September 2026): the lines that fit no template

A descriptive count (results/readable.md) found that 47% of intact lines fit none of the established templates (name +
ending, count token 'N 700', numbers only, closing formula). 'Bare line' = a line of 2+ signs that is none of these.
Hypothesis: most bare lines are names written without their suffix. Conventions as the twentieth set (A, B, F; names;
head and attribute classes as K, from A; 10,000-draw permutations; p < 0.05; A and B both where named).

Bare lines as names without the suffix
- **R1** The last sign of a bare line is a head-class sign more often than a random other sign of the same line (paired
  permutation). A and B.
- **R2** The last sign of a bare line is a sign that ends name bodies elsewhere (last body sign of some name in the
  sample) more often than a random other sign of the line. A and B.
- **R3** Bare lines equal an attested name body more often than their own sign-order shuffles. A and B.
- **R4** The adjacent pairs of bare lines occur inside name bodies more often than the pairs of shuffled bare lines. A
  and B.
- **R5** Bare lines contain a numeral more often than name lines, length-stratified (they include records, not only
  names). A and B.
- **R6** In lines ending with 400 not after an ending ('body + 400'), the part before 400 is an attested name body more
  often than when shuffled (pooled A + B).
- **R19** Bare lines are shorter than name lines with their ending removed (rank test). A and B.
- **R22** Human-figure signs in bare lines stand last in 70%+ of cases (pooled).
- **R23** Fish signs (signs.FISH) in bare lines stand last more often than first (pooled, sign test).
- **R24** Bare lines end in a jar variant (741 / 742 / 745) more often than those signs stand at a random other
  position of bare lines (pooled): a variant ending.

Bare lines by object, place and time (F)
- **R7** Bare seal lines end in a head-class sign more often than bare tablet lines.
- **R8** Bare tablet lines end in an attribute-class sign more often than bare seal lines.
- **R9** Seal lines are bare more often outside Mohenjo-daro and Harappa.
- **R10** Seal lines are bare more often in later levels, at both Mohenjo-daro and Harappa.
- **R11** Bare seal lines are on non-unicorn seals more often than seal names are.
- **R12** Bare seal lines carry the heading less often than seal names, length-stratified.
- **R18** Distinct bare tablet texts recur on 2+ tablets more often than distinct tablet name texts.
- **R25** Bare lines ending in 400 or 90 (a clitic without an ending) are on tablets more often than on seals.

Word classes and coverage
- **R13** Position classes carry across transcriptions: of signs with 10+ name tokens in both A and B, 80%+ have the
  same majority position (first / inside / last) in both.
- **R14** Classes from A (numerals; grammar signs 740, 520, 90, 400, 151, 817, 820, 861, 2; formula signs 705, 706, 33;
  head and attribute classes) cover 70%+ of B's tokens.

Counts and pots (F)
- **R15** Numerals on pots are short-stroke more often than numerals on tablets.
- **R16** The values of numbers-only pot lines differ from the values of tablet numerals (MI beyond permutation).
- **R17** 80%+ of numbers-only pot lines are a single numeral sign.
- **R20** On count tokens with other signs, the other signs follow the 'N 700' pair more often than they precede it.
- **R21** Mohenjo-daro tablets that are not count tokens carry an ending more often than Harappa ones,
  length-stratified.

## Results of the twenty-first set (added after the test; `predict_test21.py`, `results/predict_test21.md`)

Ten held, fifteen failed. Bare lines: 1,148 of 2,562 in A, 807 of 1,554 in B.

**Partly names without the suffix.**
- **R1 holds**: the last sign of a bare line is a head-class sign far more often than a random other sign (discordant
  229 / 57 in A, 142 / 43 in B; p < 0.0001 both). **R4 holds**: their adjacent pairs are pairs found inside name
  bodies (34% and 28%, p = 0.0001). **R3 holds**: a few are exact name bodies (13 of 1,148, 29 of 807; more than
  shuffled order, p = 0.003, 0.0001). The head-final order of names holds without the suffix.
- On seals the suffix-less lines have a profile: **R9** commoner outside Mohenjo-daro and Harappa (56% against 47%,
  p = 0.002), **R11** commoner on seals with other animals (25% against 20%, p = 0.016), **R12** less often headed
  (+5.9 points for names, p = 0.004). A less formal or regional way of writing names.
- But not all: **R5 holds** (bare lines carry numerals more often than names, +18 and +21 points) and R19 fails the other
  way (bare lines are longer than name bodies, 3.99 against 3.28 and 3.39 against 2.74). **R25 holds** (on tablets a
  line can close with 400 or 90 and no ending: 18% of bare tablet lines against 7% on seals). R2 fails (in A the last
  sign is no more often a name-final sign than a random sign), R6 fails (the part before a bare 400 is never a name
  body: 0 of 143), R7 and R8 fail, R10 fails (suffix-less seal lines are not later), R18 fails, R22 fails (human figures
  are last in only 42% of their bare-line tokens), R23 and R24 fail.

**Word classes do not yet cover the vocabulary.** R13 fails narrowly (35 of 46 signs, 76%, keep their majority
position between A and B; bar 80%); R14 fails (the classes from A cover 50.3% of B's tokens; bar 70%): 16 heads and 10
attributes are too few classes for most of the vocabulary.

**Pots.** **R16 holds** (pot values differ from tablet values: mostly 2 and 3, some 1 and 4; p = 0.010) and **R17 holds**
(112 of 120 numbers-only pot lines are one numeral sign): pot marks are single numbers. R15 fails (pots do not use the
short strokes more). R20 and R21 fail.

Tally, counting parts: 73 held, 124 failed (197 registered).

# Twenty-second set, registered before testing (24 September 2026): classes of the content signs

57% of sign tokens are content signs known only by position (results/readable.md), and the head / attribute classes
cover half of B (R14). A classification of the content signs, fixed here before any result is seen:

**Method.** Content signs = signs with 10+ tokens in sample A that are not numerals (numerals.NUMS), grammar signs
(740, 520, 90, 400, 151, 817, 820, 861, 2) or formula signs (705, 706, 33). Each sign's context = positive PMI of its
left and right neighbours in A's lines (line start and end as neighbours), the two halves concatenated and each row
scaled to unit length, reduced by SVD to 20 dimensions and scaled to unit length again; k-means, k = 8, 50 restarts,
seed 42. The same procedure is used wherever a clustering is named below. Conventions otherwise as the twenty-first
set (A, B, F; names; Fairservis categories; 10,000-draw permutations; p < 0.05).

Validation of the method (where the answer is known)
- **Q1** With the numerals (10+ tokens) added to the signs clustered, two numerals share a cluster at 3+ times the rate
  of two random signs.
- **Q2** On Linear B (DAMOS lines, dividers removed, signs with 10+ tokens), two signs of the same kind (syllabogram or
  word sign) share a cluster more often than under permutation of the kinds.

Transfer to the other transcription
- **Q3** Content-sign pairs in the same A cluster have more similar B contexts (cosine of positive-PMI vectors, as H3)
  than pairs in different clusters (cluster labels permuted).
- **Q12** A clustering of B made by the same method agrees with A's more than chance: pairs of signs together in both
  (among signs clustered in both) exceed permutation of B's labels.
- **Q4** The clusters differ in where their tokens stand in B's names (first / inside / last): MI beyond permutation of
  the sign-to-cluster labels.
- **Q14** At least half of the clusters have 60%+ of their B name tokens in one position.
- **Q5** The clusters differ in the ending taken by B names whose last sign they hold (MI beyond permutation).
- **Q13** Numerals, grammar and formula signs plus the A clusters cover 70%+ of B's tokens.

Meaning, objects, places
- **Q6** Cluster and Fairservis picture category are associated beyond permutation (MI over categorised content signs).
- **Q7** Human-figure signs (Fairservis A) share a cluster more often than random pairs of categorised signs.
- **Q15** Head-class signs (K) are concentrated: one cluster holds half or more of them.
- **Q8** The cluster mix of content tokens differs between seals and tablets (F, MI beyond permutation of object
  labels).
- **Q9** The cluster mix of seal content tokens differs between Mohenjo-daro and Harappa (F).
- **Q10** The clusters differ in graphic complexity (H5 measure; between-cluster variance beyond permutation).
- **Q11** The cluster mix of West Asian content tokens differs from home (F; permutation of home / foreign labels
  among lines).

## Results of the twenty-second set (added after the test; `predict_test22.py`, `results/predict_test22.md`)

Eight held, seven failed. 115 content signs clustered into 8 classes on A. Deviation from the registration: Q8, Q9 and
Q11 were run with 1,000 permutations, not 10,000 (the smallest possible p is 0.001); Q8's p = 0.0010 sits at that floor.

**The method passes on Linear B and fails on the Indus numerals.**
- **Q2 holds**: on Linear B the method separates syllabograms from word signs (95% of same-cluster pairs are of one
  kind, p = 0.0001).
- **Q1 fails**: added to the Indus clustering, the numerals do not gather (same-cluster rate 1.3 times that of random
  pairs; bar 3). On this corpus the method does not recover a class known in advance, so its clusters cannot be taken
  as word classes.

**What the clusters still do.**
- **Q3 holds** (A's clusters predict B contexts: cosine +0.028, p = 0.0001) and **Q12 holds** (a clustering of B made
  independently agrees with A's more than chance, 74 pairs, p = 0.0002): the grouping is reproducible across
  transcriptions, if weak.
- **Q5 holds** (clusters differ in the ending their names take in B, MI 0.241 bits, p = 0.004): one cluster (7) holds
  the fish series with 803, 806, 742, 745, i.e. the 520 side.
- **Q6 holds** (clusters and Fairservis picture categories are associated, MI 1.335 bits over 50 signs, p = 0.005) and
  **Q10 holds** (clusters differ in graphic complexity, p = 0.010): the contextual grouping partly follows what the
  signs depict and how they are drawn.
- **Q8 holds** (seals and tablets use the clusters differently, p = 0.001 at the floor).
- **Q13 holds**: numerals, grammar and formula signs plus the clustered signs cover 93.2% of B's tokens (the
  head / attribute classes alone covered 50%, R14). Coverage by a class is not knowledge of the class, given Q1.

**Failed.** Q4 (clusters do not differ in position in B, p = 0.36), Q14 (only 1 of 8 clusters has 60%+ of its tokens in
one position), Q7 (the human figures fall in five different clusters), Q15 (the head-class signs are spread, at most
47% in one cluster), Q9 (no difference between Mohenjo-daro and Harappa), Q11 (foreign texts not different, p = 0.09).

The content signs can be grouped reproducibly, and the groups carry some signal (ending, picture, drawing, object), but
the method fails its Indus check and the groups are not positional word classes. The 57% of content signs remain
unread and, in any validated sense, unclassified.

Tally, counting parts: 81 held, 131 failed (212 registered).

# Twenty-third set, registered before testing (24 September 2026): ligatures, and a validated classification

Two leads. (1) Fairservis 1992 identifies some signs as combinations of two others (keys/fairservis1992_raw.tsv):
154 = 151 + 740 (A-8 = A-7 + J-5), 156 = 151 + 520 (A-9 = A-7 + H-5), 555 = 550 + 482 (Q-14 = I-11 + K-1), 742 =
740 + 2 (Q-17 = J-5 + P-2), 702 = 700 + 2 (Q-15 = J-1 + P-2), 703 = 700 + 3 (Q-16 = J-1 + O-3). If a ligature is
written for the sequence of its parts, its left neighbours should resemble those of one part and its right neighbours
those of the other. (2) The twenty-second set's clustering failed its Indus check (Q1): a variant must pass that check
before its classes are used.

Conventions as the twenty-second set (A, B, F; 10,000-draw permutations or random draws; p < 0.05).

Ligatures (one hypothesis each; tested in A, and in B where the ligature and both parts have 10+ tokens, both
required; a ligature with under 10 tokens in A is not testable and fails)
- 'Left' and 'right' vectors = counts of the preceding and following sign (line start and end included). Sequence
  score of ligature L with parts X, Y = mean of cos(left(L), left(X)) and cos(right(L), right(Y)), taking the better of
  the two orders (X first or Y first). Null: the same score with X and Y replaced by random signs from X's and Y's
  token-count quintiles (10,000 draws).
- **G1** 154 behaves as 151 + 740. **G2** 156 as 151 + 520. **G3** 555 as 550 + 482. **G4** 742 as 740 + 2. **G5** 702
  as 700 + 2. **G6** 703 as 700 + 3.
- **G7 Sequence, not modification.** Across the six, the sequence score exceeds the 'modified base' score (mean of
  cos(left(L), left(X)) and cos(right(L), right(X)), X the pictorial base: 151, 151, 550, 740, 700, 700) for at least 5
  of the testable ligatures.
- **G8 The pot-with-strokes signs are counts.** Tablets carrying 702 or 703 are 1-2 signs long more often than other
  tablets without a count token (F, Fisher).

A classification that passes its own check
- **C1** Of four variants of the twenty-second set's method, tried in this fixed order, at least one passes the numeral
  check (numeral pairs share a cluster at 3+ times the rate of all pairs) on A: V1 left contexts only; V2 right
  contexts only; V3 left + right contexts plus each sign's share of first / inside / last positions in A's names (the
  three shares scaled by 0.5 and appended after the SVD step); V4 left + right as before with k = 12. The first variant
  to pass is the chosen one; C2-C5 use it and fail if none passes.
- **C2** The chosen clusters predict B contexts (as Q3).
- **C3** The chosen clusters are associated with Fairservis picture categories (as Q6).
- **C4** Human-figure signs share a chosen cluster more often than random categorised pairs (as Q7).
- **C5** The chosen clusters differ in position in B's names (as Q4).

## Results of the twenty-third set (added after the test; `predict_test23.py`, `results/predict_test23.md`)

One held, twelve failed.

**Ligatures.**
- **G3 holds**: 555 (Fairservis Q-14, tongs + carpenter's square) behaves as 550 + 482 in sequence (score 0.621
  against its matched null, p = 0.0009; A only, too rare in B). A ligature written for the sequence of its parts.
- G1 fails narrowly (154 as 151 + 740: p = 0.068), G2 fails (156 as 151 + 520: p = 0.11, 0.20), G4 fails (742 as 740 +
  2: p = 0.51). G5 and G6 are not testable (702 and 703 have 6 and 7 tokens in A), and G8 fails (3 tablets carry them).
- G7 fails on its count: all 4 testable ligatures score higher as a sequence than as a modified base sign, but the bar
  was 5 testable ligatures. The direction is consistent; the evidence is thin.

**Classification.** **C1 fails**: none of the four registered variants gathers the numerals at 3 times the base rate
(left only 2.5, right only 1.2, both + positions 2.9, k = 12 2.1). C2-C5 are therefore not tested. The lead of a
validated classification of the content signs is closed on this corpus: no contextual clustering tried here recovers
even the numerals as a class. Left contexts carry more class information than right contexts (2.5 against 1.2), which
fits the head-final structure: a sign's class shows in what precedes it.

Tally, counting parts: 82 held, 143 failed (225 registered).

# Twenty-fourth set, registered before testing (24 September 2026): reading order, numbers, and seals as owned objects

Twelve hypotheses on questions not yet asked. Conventions as before (A = data/corpus.tsv, which records each text's
direction; B = M77 additions; F = the fuller corpus, lines as listed; names; head class as K; 10,000-draw
permutations; p < 0.05; A and B both where named). 'Attested pair' = an adjacent sign pair found in single-line texts
of the sample other than the text itself.

Reading order
- **M1 The recorded direction is right.** For A's texts recorded as left-to-right (field 'direction' L/R), the share of
  their adjacent pairs that are attested pairs is higher read in the recorded order than reversed (paired sign test
  over texts).
- **M2 Left-to-right texts come from outside the two big cities** more often than right-to-left texts (A, Fisher).
- **M3 Line order in M77.** For B's multi-line texts, the pair across each line junction is an attested pair more often
  with lines as listed than reversed (sign test over junctions that differ).
- **M4 Line order in the fuller corpus.** The same on F's intact multi-line texts.

Numbers
- **M5 Compound numbers descend.** Where two stroke numerals stand side by side, the larger value comes first more often
  than the smaller (sign test). A and B.
- **M6 The tiered form is for larger numbers.** Among numerals of value 5-8, the tiered form is a larger share than
  among numerals of value 3-4. A and B.
- **M7 Numbers before fish are larger.** Numerals directly before a fish sign (signs.FISH) have a higher mean value than
  numerals directly before other signs (label permutation). A and B.
- **M8 The clitics have a fixed order.** Where 90 and 400 both follow an ending, 400 comes first more often than not
  (sign test, pooled A + B).

Seals as owned objects (F, distinct intact seals)
- **M9 One name, one emblem.** Seals bearing the same name (fourth-set definition) show the same animal (motif field,
  first word) more often than random pairs of named seals (label permutation over seals).
- **M10 One name, one seal shape.** Same-name seals share the seal type (SEAL:S square, SEAL:R rectangular, other) more
  often than random pairs.
- **M11 One name, one heading.** Same-name seals agree in having or lacking the heading more often than random pairs.
- **M12 Bar seals carry bare names.** Rectangular seals (SEAL:R) carry lines without an ending more often than square
  seals (SEAL:S), length-stratified.

## Results of the twenty-fourth set (added after the test; `predict_test24.py`, `results/predict_test24.md`)

Five held, seven failed.

**Reading order.**
- **M1 holds**: the 103 texts recorded as left-to-right read more familiarly in the recorded order than reversed (78
  against 3, p < 0.0001): the direction judgments in the ICIT-derived corpus are right.
- **M2 holds**: left-to-right texts come from outside Mohenjo-daro and Harappa twice as often (29% against 14%,
  p = 0.0001): the reversed direction belongs to the smaller places.
- **M3 holds**: in M77's multi-line texts the junction pair is attested more often with lines as listed (57 against 25,
  p = 0.0003): Mahadevan's line order is supported.
- **M4 fails, the other way**: in the fuller corpus the junction pair is attested more often with the lines *reversed*
  (13 against 3; the reverse direction would give p = 0.011). This settles the ambiguity found in the seventh set: the
  listed line order of icit_full.py is wrong for most multi-line texts, and the whole-string reversal of
  data/corpus.tsv is right. The seventh set (X1, X2) was run both ways; the later sets that parsed fuller-corpus names
  from whole texts used the listed order for the multi-line ones (about 4% of seals), so their fuller-corpus counts
  carry that small error. icit_full.py keeps its default so that past results reproduce; LINES_REVERSED = True is the
  setting to use from now on.

**Numbers.**
- **M6 holds**: the tiered form is used for larger numbers (63.5% and 66.2% of values 5-8, against 5.3% and 5.8% of
  values 3-4): a second row of strokes to keep large numbers readable.
- M5 fails the other way: side-by-side numerals put the smaller value first (149 against 55; 33 against 16).
- M7 fails the other way: numbers before fish are smaller on average (2.5 against 3.0; 2.4 against 3.0).
- M8 fails the other way, with a fixed order: where both clitics follow an ending it is always 90 then 400 (9 to 0).

**Seals as owned objects.**
- **M12 holds**: rectangular (bar) seals carry lines without an ending more often than square seals (+13.4 points,
  p = 0.0002): the bar seals, which have no animal, write names without the suffix.
- M9 fails (same-name seals do not share their animal more than chance: 68%, p = 0.32), M10 fails narrowly (same seal
  shape 82%, p = 0.078), M11 fails (the heading comes and goes on the same name).

Tally, counting parts: 87 held, 150 failed (237 registered).

# Twenty-fifth set, registered before testing (24 September 2026): affixed signs, direction, numbers, bar seals

Leads from the twenty-third and twenty-fourth sets: one ligature is a sequence of its parts (G3); left-to-right texts
belong to the smaller places (M2); side-by-side numerals put the smaller first (M5) and the tiered form is for 5-8
(M6); bar seals carry suffix-less names (M12); the fuller corpus's lines read reversed (M4), so F is read here with
icit_full.LINES_REVERSED = True. Conventions as before (A with its 'direction', 'type', 'site' and 'motif' fields; B;
F; names; head class as K; 10,000-draw permutations or draws; p < 0.05; A and B both where named). Regions: Sindh
(Mohenjo-daro, Chanhu-daro, Allahdino, Amri, Kot Diji, Lakhanjo-daro), Gujarat (Lothal, Dholavira, Surkotada,
Desalpur, Kanmer, Gola Dhoro, Rangpur), north (Harappa, Kalibangan, Banawali, Rakhigarhi, Farmana, Bhirrana, Rupar);
others left out.

Affixed signs as sequences (the twenty-third set's sequence score and null; A, and B where all three have 10+ tokens)
- **O1** 235 (fish under a caret, Fairservis Q-6) behaves as 480 + 220 or 220 + 480.
- **O2** 231 (fish with a stroke, Q-2) behaves as 220 + 1 (either order).
- **O3** 415 (comb with a stroke, Q-11) behaves as 400 + 1.
- **O4** 741 (jar with a stroke, J-6) behaves as 740 + 1.
- **O5** For all of O1-O4 that are testable, the sequence score exceeds the modified-base score.

Direction (A)
- **O6** Outside Mohenjo-daro and Harappa, left-to-right texts are a larger share in Gujarat than in the other regions
  (Fisher).
- **O7** Left-to-right lines end in an ending less often than right-to-left lines, length-stratified.
- **O8** Left-to-right seals carry an animal other than the unicorn more often than right-to-left seals.
- **O9** Left-to-right texts are shorter (rank test).
- **O23** Moulded tablets (type TAB:B) are left-to-right more often than other objects (a mould reverses the text).
- **O24** The left-to-right share differs between seals and other objects (Fisher, two-sided).

Numbers (A and B unless said)
- **O10** Side-by-side numerals mix two notations (short / long / tiered) more often than random pairings of the same
  numeral tokens would (permutation of the numeral tokens among the pair slots).
- **O11** In side-by-side pairs with the smaller value first, the second numeral is long-stroke more often than in pairs
  with the larger first (pooled).
- **O12** Long-stroke numerals stand before a container or device sign (Fairservis J or K) more often than short-stroke
  numerals do (pooled).
- **O13** Numerals before a fish sign are short-stroke more often than numerals before other signs.
- **O25** Tiered numerals stand inside names (not the name's last sign) more often than short-stroke numerals do.

Bar seals (F, lines reversed)
- **O15** Bar seals (SEAL:R) are a larger share of seals in later levels, at Mohenjo-daro and at Harappa (Fisher each).
- **O16** Bar seals come from outside the two cities more often than square seals.
- **O17** Bar-seal lines carry the heading less often than square-seal lines, length-stratified.
- **O18** Bar-seal texts are longer than square-seal texts (rank test).
- **O19** Bar-seal lines end in a head-class sign more often than a random other position of the same line (paired
  sign test, as R1).
- **O20** Bar seals are more often left-to-right than square seals (A, types 'SEAL:R' and 'SEAL:S').

Tablets (F)
- **O21** Distinct moulded-tablet texts recur on 2+ tablets more often than distinct incised-tablet texts.
- **O22** Tablets with 400 are incised more often than moulded, length-stratified.
- **O14** Among tablets with a name ending, incised ones carry 400 after it more often than moulded ones.

## Results of the twenty-fifth set (added after the test; `predict_test25.py`, `results/predict_test25.md`)

Eight held, seventeen failed. The fuller corpus was read with lines reversed (M4).

**Affixed signs are not sequences.** O1-O4 fail: the fish with a caret (235), the fish with a stroke (231), the comb with
a stroke (415) and the jar with a stroke (741) do not behave as their base followed by the added mark (p = 0.28 to
0.97); O5 fails (3 of 4 score higher as sequences, the bar was all). Only 555 (G3), a combination of two full signs,
behaved as a sequence. The added strokes and marks modify a sign inside itself; they are not suffixes written into it.

**Direction.**
- **O24 holds**: left-to-right texts are rarer on seals (2.5%) than on other objects (6.1%, p < 0.0001). **O9 holds**:
  they are shorter. **O8 holds**: left-to-right seals carry an animal other than the unicorn 59% of the time against
  20% (10 of 17, p = 0.0005). **O20 holds**: bar seals run left to right twice as often as square seals (4.3% against
  2.0%, p = 0.035). A seal is cut in mirror image; the left-to-right seals are the less formal ones, the short texts,
  the other animals and the bar seals.
- O6 fails (not a Gujarat habit: 6.2% against 6.6%), O7 fails (left-to-right lines carry endings as often), O23 fails
  narrowly (moulded tablets 5.3% against 3.8%, p = 0.096).

**Numbers: two systems for two things.**
- **O12 holds**: long-stroke numerals stand before a container or device sign (Fairservis J, K) in 37% of cases,
  short-stroke numerals in 3% (p < 0.0001). **O13 holds**: numerals before fish signs are short-stroke (64% and 66%
  against 50% and 30%). Long strokes count measures and containers (the tablets' 'N 700' is one case of it); short
  strokes go with the fish names.
- O10 fails (side-by-side numerals mix notations no more than chance), O11 fails the other way (in smaller-first pairs
  the second numeral is rarely long: 9% against 52%), O25 fails the other way (tiered numerals stand last in a name
  more often than short ones: 18% against 2%).

**Bar seals.** O15 fails narrowly: bar seals are a larger share of later seals at Mohenjo-daro (16.4% against 10.8%,
p = 0.041) and at Harappa (26.8% against 15.6%, p = 0.054), short of the bar at Harappa. O16, O17, O18, O19 fail (not
from smaller places, not less headed, not longer, their lines not more head-final).

**Tablets.** **O22 holds** (tablets with 400 are incised more often, +12.2 points, p = 0.0002) and **O14 holds** (name
tablets with an ending carry 400 after it 48.5% of the time when incised, 24.3% when moulded, p < 0.0001): 400 after
the name is a feature of the written, incised tablets. O21 fails.

Tally, counting parts: 95 held, 167 failed (262 registered).

# Twenty-sixth set, registered before testing (24 September 2026): tablet records, numbers, direction, variants

Leads: 400 after a name belongs to incised tablets (O14, O22); long strokes count containers and devices, short strokes
go with fish, tiered strokes write 5-8 and often stand last (O12, O13, M6, O25); left-to-right writing avoids seals
(O24); affixed marks modify a sign rather than add a suffix (O1-O5). Conventions as before (A with 'direction', 'type',
'site', 'motif'; B; F read with lines reversed; names; head class as K; Fairservis categories; 10,000-draw
permutations; p < 0.05; A and B both where named). 'Name tablet' = an incised tablet (TAB:I) with a 740 / 520 ending;
'with 400' = the ending directly followed by 400. Length strata: 2-3, 4-5, 6+.

Tablet records (F)
- **T1** Name tablets with 400 carry a numeral more often than name tablets without 400, length-stratified.
- **T2** On name tablets with 400 and a numeral, the numeral stands after the ending more often than before the name.
- **T3** Numerals on name tablets are long-stroke more often than numerals on seals.
- **T4** Name bodies on incised tablets are attested as seal name bodies more often than name bodies on moulded tablets.
- **T5** Name-tablet lines carry the heading less often than seal lines with an ending, length-stratified.
- **T6** Incised tablets are a larger share of Harappa tablets in later levels (HARP 3C, Vats I-III) than earlier.
- **T7** Names on name tablets end in 740 more often than names on seals.
- **T8** On tablets, a 400 not after an ending follows a head-class sign more often than a random other position of the
  same line (paired sign test).
- **T9** On name tablets with a long-stroke numeral, 50%+ of those numerals are followed by 700.
- **T10** Name tablets with 400 come from Harappa more often than other tablets do.

Numbers
- **N1** Among long-stroke numerals directly before a non-numeral sign, the value depends on the sign (MI beyond
  permutation of values). A and B.
- **N2** The values of numerals directly before a fish sign are distributed differently from those before other signs
  (MI beyond permutation). A and B.
- **N5** A long-stroke numeral + a Fairservis J or K sign ends its line more often than a short-stroke numeral + any
  sign (pooled A + B).
- **N6** Numerals on tablets are long-stroke more often than numerals on seals (F).
- **N7** Tiered numerals are directly followed by the ending (740 / 520) more often than short-stroke numerals. A and B.

Direction (A)
- **D1** Copper tablets (type TAB:C) run left to right more often than other objects.
- **D2** Objects written directly (TAB:I, TAB:C, POT, TAG) run left to right more often than carved or moulded ones
  (SEAL, TAB:B).
- **D3** Left-to-right lines carry the heading less often than right-to-left lines, length-stratified.

Affixed variants (pooled A + B)
- **V2** The jar variants 741, 742, 745 end their line in under 10% of their tokens.
- **V3** Base and affixed variant alternate in the same names: pairs of distinct names that differ only by 220 / 231,
  400 / 415 or 740 / 741 at one position are more numerous than such pairs for random sign pairs matched on the two
  signs' token-count quintiles (10,000 draws of three pairs).
- **V4** The affixed fish variants (231, 233, 235, 240) are the last sign of a name less often than the plain fish 220.

Other objects, places and time
- **X1** Names on sealings (TAG) end in 740 more often than names on seals (F).
- **X2** Copper tablets (TAB:C) carry an ending less often than seals, length-stratified (A).
- **S5** The balance of 740 and 520 among seal names differs by region (Sindh / Gujarat / north, as the twenty-fifth
  set; MI beyond permutation) (F).
- **S6** At Mohenjo-daro the share of 520 among seal names differs between earlier and later levels (Fisher, two-sided)
  (F).

## Results of the twenty-sixth set (added after the test; `predict_test26.py`, `results/predict_test26.md`)

Fifteen held, ten failed. 167 name tablets (incised, with an ending), 83 of them with 400 after the ending.

**The incised name tablets are a Harappa record of seal-holders.**
- **T10 holds**: all 83 name tablets with 400 come from Harappa (against 78% of other tablets).
- **T4 holds**: 53% of the names on incised tablets are also found on seals, against 23% of those on moulded tablets
  (p < 0.0001): the incised tablets name people who held seals.
- **T7 holds** (their names end in 740, the person class, 88.6% against 81.8% on seals, p = 0.018) and **T5 holds**
  (they carry the heading far less than seals: 22 points, p = 0.0001): names without the title formula.
- **T3 holds**: their numerals are long-stroke (68.5% against 31.9% on seals).
- T2 fails the other way: on name tablets with 400 and a number, the number stands before the ending in all 19 (none
  after). T9 fails: their long numerals are never followed by 700 (0 of 37): they count something other than the
  tokens' measure. T1 fails (400 does not make a number more likely), T6 fails the other way (incised tablets are
  earlier, not later: 64% of earlier Harappa tablets, 35% of later), T8 fails (a bare 400 does not follow a head).

**Numbers.**
- **N1 holds**: the value of a long-stroke count depends on what is counted (MI 1.14 and 0.63 bits, p = 0.0001 both):
  each unit has its usual counts.
- **N2 holds**: fish take their own numbers, overwhelmingly the pair of strokes (value 2: 211 of 300 in A, 85 of 104 in
  B), with 6 and 12 next.
- **N7 holds**: tiered numerals stand directly before the ending 10.6% and 14.6% of the time, short ones under 1%:
  a tiered number can be the head of a name.
- **N5 holds**: a long-stroke count with a container or device sign closes its line 86% of the time (short numerals
  29%).
- **N6 holds**: tablet numerals are long-stroke 69%, seal numerals 32%.

**Direction.** **D2 holds**: objects written directly (incised tablets, copper tablets, pots, tags) run left to right
7.0% of the time, carved and moulded ones 3.2% (p = 0.0001). D1 fails (no copper tablet runs left to right: 0 of 149),
D3 fails.

**Affixed variants.** **V2 holds** (the jar variants end a line only 6% of the time), **V4 holds** (the affixed fish are
the last sign of a name 19% of the time, the plain fish 35.5%: the affix makes an attribute), **V3 holds** (base and
affixed variant alternate in otherwise identical names more than random sign pairs: 220 / 231 8 pairs, 740 / 741 2,
400 / 415 0; p = 0.026, carried by the fish). The affixed forms behave as modified forms of the same sign, used in
front of a head.

**Other.** **X2 holds** (copper tablets carry endings 12 points less than seals: labels, not names). X1 fails narrowly
(sealing names 740 in 91% against 82%, p = 0.083). S5 and S6 fail: the 740 / 520 balance does not differ by region or
change at Mohenjo-daro over time.

Tally, counting parts: 110 held, 177 failed (287 registered).

# Twenty-seventh set, registered before testing (24 September 2026): the Harappa name records, numbers, labels

Leads: incised name tablets with 400 are a Harappa genre naming seal-holders, with the number before the ending (T2-T10);
each long-count unit has its usual values (N1); fish take the stroke pair (N2); affixed variants are attributes that
alternate with their base (V2-V4); direct writing runs left to right more (D2); copper tablets are labels (X2).
Conventions as the twenty-sixth set (F read with lines reversed; 'name tablet' = TAB:I with a 740 / 520 ending; A, B;
names; Fairservis categories; 10,000-draw permutations; p < 0.05; A and B both where named).

The Harappa name records (F)
- **L1** On name tablets with a number, the number is the text's first sign in more than half.
- **L2** Pairs of name tablets with the same name body and a number each carry different numbers in more than half.
- **L3** Name tablets with the same name body share a Harappa level more often than random pairs of name tablets
  (level labels permuted).
- **L4** Name bodies found both on name tablets and on seals are found on Harappa seals more often than Harappa's share
  of seal names predicts (binomial).
- **L5** On name tablets, 400 ends the text in 80%+ of cases.
- **L6** Name bodies on name tablets are shorter than name bodies on seals (rank test).
- **L7** The values of numbers on name tablets are distributed differently from those of numbers on seals (MI beyond
  permutation).
- **L8** Incised tablets without an ending end in 400 more often than moulded tablets without an ending.
- **L9** The values of numbers on name tablets are distributed differently from the values of count tokens (N 700).
- **L23** Harappa seals whose name is also on a name tablet are unicorn seals more often than other Harappa seals.
- **L24** Seal names also found on name tablets end in 740 more often than other seal names.

Numbers
- **L10** The stroke pair and a following fish (2 + a signs.FISH sign) are split by a line break less often than other
  gaps (M77 multi-line texts, both line orders).
- **L11** Fish-headed names with the stroke pair (2) inside take 520 more often than fish-headed names without a
  numeral (pooled A + B, length-stratified).
- **L12** Of long-count units (a J or K sign directly after long-stroke numerals 10+ times, pooled A + B), 80%+ have one
  value in half or more of their counts.
- **L13** Names headed by a tiered numeral (tiered numeral directly before the ending) are on seals more often than on
  tablets, relative to all names with an ending (F).
- **L14** Names headed by a tiered numeral carry the heading more often than other names, length-stratified (pooled).
- **L15** Long-stroke numerals open their line more often than short-stroke numerals. A and B.
- **L25** On seals too, long-stroke numerals stand before J / K signs more often than short-stroke numerals (F).

Affixed variants (pooled A + B)
- **L16** The fish variants 233, 235 and 240 alternate with 220 in otherwise identical names more than random sign
  pairs matched on token quintiles.
- **L17** Names whose last sign is an affixed fish (231, 233, 235, 240) take 520 less often than names ending in 220.

Direction (A)
- **L18** Incised tablets (TAB:I) run left to right more often than moulded tablets (TAB:B).
- **L19** Pots run left to right more often than seals.

Labels and other genres
- **L20** Copper-tablet texts are shorter than seal texts (A, rank test).
- **L21** Distinct copper-tablet texts recur on 2+ tablets more often than distinct seal texts (A).
- **L22** Pot texts with an ending carry a numeral less often than tablet texts with an ending, length-stratified (F).

## Results of the twenty-seventh set (added after the test; `predict_test27.py`, `results/predict_test27.md`)

Eleven held, fourteen failed.

**The Harappa name tablets are issued in identical sets.**
- L2 fails decisively: the 25 pairs of name tablets that name the same person and carry a number carry the *same*
  number, every one (0 differ). **L3 holds**: same-name tablets lie in the same level 86% of the time (p = 0.001). They
  are not a running account of deliveries but copies of one record, made together, like the count tokens (Z).
- **L5 holds**: 400 after the name ends the text in all 83 cases. **L6 holds**: the names on these tablets are shorter
  than seal names (p = 0.0001). **L9 holds**: their numbers are not the count tokens' numbers (mostly 2 and 1, against
  the tokens' 3, 4, 2).
- L1 fails (the number opens the text in 46% only), L4 fails (the named people are not significantly Harappa
  seal-holders: 7 of 22 against 19%, p = 0.11), L7 fails (the numbers are not unlike seal numbers), L8 fails the other
  way, L23 and L24 fail.
- The record: '[number] [short name]-740 400', copied several times in one batch. The format fits a tally or receipt
  issued to a named person in multiple copies; it does not say what was counted.

**Numbers.**
- **L11 holds**: fish-headed names with the stroke pair inside take 520 far more often than fish names without a numeral
  (+38.7 points, p = 0.0004). The stroke-pair fish (Parpola's 'intermediate space + fish') are the 520 side of the fish.
- **L12 holds**: the two long-count units with 10+ counts each have a usual value: 700 is counted 3 (150 of 249), 740
  is counted 2 (62 of 82).
- **L15 holds**: long-stroke numerals open their line more often than short ones (29.5% against 14.8%; 57.2% against
  20.6%). **L25 holds**: on seals too, long strokes stand before containers and devices (11.5% against 2.5%).
- L10 fails narrowly (the stroke pair before a fish is split by a line once or twice in 25-26 cases against 22%; p =
  0.055 as listed, 0.017 reversed). L13, L14 fail.

**Variants.** **L16 holds**: the fish variants 233, 235 and 240 alternate with the plain fish 220 in otherwise identical
names (31 pairs, p = 0.0001). L17 fails the other way (names ending in an affixed fish take 520 more, 72% against 63%,
not significant).

**Direction and labels.** **L19 holds**: pots run left to right 20% of the time, seals 2.5%. L18 fails narrowly
(incised 8.6% against moulded 5.3%, p = 0.053). **L21 holds**: copper-tablet texts recur (51% of distinct texts on 2+
tablets, against 4.6% of seal texts): standard labels. L20 fails (not shorter). L22 fails the other way (pot names
carry numerals more than tablet names).

Tally, counting parts: 121 held, 191 failed (312 registered).

# Twenty-eighth set, registered before testing (24 September 2026): receipts, the fish split, units, habits

Leads: the Harappa name tablets with 400 ('receipts': TAB:I, a 740 / 520 ending directly followed by 400) are issued in
identical copies of '[number] [short name]-740 400' (L2, L3, L5, L6); the stroke-pair fish take 520 (L11); each
long-count unit has its usual value, 700 counted 3 and 740 counted 2 (L12). Conventions as the twenty-seventh set (F read
with lines reversed; A, B; names; head and attribute classes as K; Fairservis categories; 10,000-draw permutations;
p < 0.05; A and B both where named).

Receipts and tokens (F)
- **E1** Receipt copies (same name body) lie closer in depth than random pairs of receipts (median depth difference).
- **E2** At Harappa, receipts come from earlier levels more often than count tokens (N 700) do.
- **E3** Receipt name bodies equal the last part of a longer seal name body more often than the same bodies in shuffled
  order do.
- **E4** Receipt name bodies are a single sign more often than seal name bodies.
- **E5** On receipts, the number's value depends on the name's last sign (MI beyond permutation).
- **E21** 70%+ of the numbers on receipts have the value 1 or 2.
- **E22** Receipt names have a human-figure head more often than seal names.
- **E23** The first signs of receipt names are distributed differently from those of seal names (MI beyond permutation).
- **E6** The pair 'long 2 + 740' (32 740) is on moulded tablets more often than on other objects, per object.
- **E7** At Harappa, tablets with '32 740' and count tokens differ in level (MI beyond permutation).
- **E8** Tablets containing '32 740' are 3 signs or fewer more often than other tablets.
- **E20** At Harappa, the count tokens' value correlates with depth (Spearman, permutation; either sign).

The fish split (pooled A + B unless said)
- **E9** Fish-headed names with the long pair (32) inside take 520 more often than fish-headed names without a numeral,
  length-stratified.
- **E10** Names ending in the plain fish (220) with no numeral in the name take 740 in 60%+ of cases.
- **E11** The short stroke pair (2) is followed by a fish sign more often than the short three (3). A and B.
- **E12** Names with the stroke pair before a fish carry the heading more often than other names, length-stratified.

Units
- **E14** On seals alone, the value of a long-stroke numeral depends on the sign after it (F, MI beyond permutation).
- **E15** The value of a short-stroke numeral depends on the sign after it. A and B.
- **E16** The value of a tiered numeral depends on the sign after it (pooled).
- **E13** Long-stroke numerals on seals stand in lines ending 520 more often than seal lines end in 520 (F).

Direction and labels (A)
- **E17** Left-to-right pot texts come from outside Mohenjo-daro and Harappa more often than right-to-left pot texts.
- **E18** Left-to-right lines contain a numeral more often than right-to-left lines, length-stratified.
- **E19** Copper-tablet lines contain a numeral less often than seal lines, length-stratified.

Two cities' habits (F seals)
- **E24** Seal names followed by 400 are from Harappa more often than other seal names.
- **E25** Harappa seal names are followed by 90 less often than Mohenjo-daro seal names.

## Results of the twenty-eighth set (added after the test; `predict_test28.py`, `results/predict_test28.md`)

Fourteen held, eleven failed. 83 receipts.

**Receipts name seal-holders by the end of their name.**
- **E3 holds**: 51 of the 83 receipt names equal the final part of a longer seal name (p = 0.0001 against shuffled
  order). **E4 holds**: 48% of receipt names are one sign, against 13% of seal names. **E23 holds**: they begin with
  different signs from seal names. A receipt names its person by the head of the seal name (and sometimes the attribute
  next to it), not by the whole name.
- **E1 holds**: copies of the same receipt lie closer in depth (median 2.3 ft against 4.3 for random pairs, p = 0.0001).
- **E21 holds**: 14 of the 19 numbers are 1 or 2. E5 fails narrowly (the number does not clearly depend on the name,
  p = 0.063). E22 fails the other way: no receipt name has a human-figure head (0 of 83, against 7.4% of seal names).
- E2 fails narrowly (receipts are earlier than tokens, 79% against 66%, p = 0.054).

**The long-2 + 740 expression is later.** **E7 holds**: at Harappa the '32 740' tablets are from later levels (9 of
11), the count tokens from earlier ones (113 of 171; p = 0.007). E6 and E8 fail (not a moulded formula, not short).
**E20 holds**: count-token values correlate with depth (Spearman 0.24, p = 0.002): larger counts lie deeper, i.e.
earlier.

**The fish.**
- **E11 holds**: the short stroke pair is followed by a fish 26% and 34% of the time, the short three 13% and 6%: the
  pair belongs with the fish.
- **E12 holds**: names containing the stroke pair + fish carry the heading far more often (+28.7 points, p = 0.0001).
  With L11 (they take 520), the numbered fish names are headed 520 names: a formal, titled class.
- E9 fails (the long pair before a fish does not raise 520 significantly; 8 cases), E10 fails the other way (plain-fish
  names without a numeral take 740 only 28% of the time: the plain fish is on the 520 side too).

**Numbers are idioms, not free counts.** **E14, E15, E16 hold**: in every notation (long on seals, short in A and B,
tiered) the value depends strongly on the sign that follows (MI 1.16-1.64 bits, p = 0.0001). Numeral + sign pairs
behave as fixed expressions, each sign with its own number, more than as quantities free to vary. **E13 holds**: long
numerals on seals stand in 520 lines more than 520 lines' share (30% against 18%).

**Other.** **E19 holds** (copper tablets carry numerals less than seals, -11.7 points, p = 0.005: labels without
counts). E17, E18 fail narrowly (p = 0.10, 0.08). E24, E25 fail (no Harappa / Mohenjo-daro habit in 400 or 90 on seals).

Tally, counting parts: 135 held, 202 failed (337 registered).

# Twenty-ninth set, registered before testing (24 September 2026): receipts, number idioms, titled names

Leads: receipts name seal-holders by the end of the seal name (E3, E4); numeral + sign pairs are idioms (E14-E16); names
with the stroke pair + fish are titled 520 names (L11, E12). Conventions as the twenty-eighth set ('receipt' = TAB:I
with 740 / 520 directly followed by 400; F read with lines reversed; A, B; names; head and attribute classes as K;
Fairservis categories; 'stroke-pair fish name' = a name containing 2 directly before a signs.FISH sign; 10,000-draw
permutations; p < 0.05; A and B both where named; length strata 2-3, 4-5, 6+).

Receipts (F)
- **J1** Receipt names equal the end of a Harappa seal name more often than Harappa's share of seal names predicts
  (binomial, over receipt names matching the end of some seal name).
- **J2** Single-sign receipt names are head-class signs in 50%+ of cases.
- **J3** Seal names ending in a receipt name end in 740 more often than other seal names.
- **J4** The number on a receipt correlates with how many copies of that receipt exist (Spearman > 0, permutation).
- **J5** Seal lines whose name ends in a receipt-name head carry the heading more often than other seal name lines,
  length-stratified.
- **J6** The Fairservis categories of receipt-name heads differ from those of seal-name heads (MI beyond permutation).

Number idioms
- **J7** A numeral and the sign after it are split by a line break less often than other gaps (M77 multi-line texts,
  both line orders).
- **J8** For signs directly after a numeral 10+ times (pooled A + B), the most common value accounts on average for
  60%+ of that sign's numerals.
- **J9** For signs after long-stroke numerals 5+ times on both tablets and seals (F), the values are more varied
  (entropy) on tablets than on seals for the majority (sign test).
- **J25** Seals carry 'numeral + 700' in under 1% of cases (F).

Titled names
- **J10** Stroke-pair fish names on seals come from Mohenjo-daro more often than other seal names (F).
- **J11** Stroke-pair fish names are on unicorn seals more often than other seal names (F).
- **J12** Stroke-pair fish names are rarer among tablet names than among seal names (F).
- **J13** The opener of the heading (817 / 820 / 861) differs between stroke-pair fish names and other headed names (MI
  beyond permutation, pooled).

Where numbers occur (F unless said)
- **J14** West Asian lines contain a numeral less often than length-matched home lines (10,000 draws).
- **J15** Cylinder-seal lines contain a numeral less often than square-seal lines, length-stratified.
- **J16** At Harappa, later count tokens are moulded more often than earlier ones.
- **J17** Tiered numerals are a larger share of numerals on Mohenjo-daro seals than on Harappa seals.
- **J18** Long-stroke numerals are a larger share of numerals on Harappa seals than on Mohenjo-daro seals.
- **J19** Bar-seal lines contain a numeral more often than square-seal lines, length-stratified.
- **J20** Unicorn-seal lines contain a numeral less often than other-animal seal lines, length-stratified.
- **J21** In seal lines the heading and a numeral occur together less often than independence predicts (Fisher).
- **J22** Names with a human-figure head contain a numeral in under 5% of cases (pooled A + B).
- **J23** Fish-headed names contain a numeral more often than other names, length-stratified (pooled).
- **J24** Names containing a tiered numeral take 520 more often than names containing a short-stroke numeral (pooled).

## Results of the twenty-ninth set (added after the test; `predict_test29.py`, `results/predict_test29.md`)

Ten held, fifteen failed. J21 is invalid by construction: the heading itself contains the stroke pair 2, which counts as
a numeral, so headed lines 'contain a numeral' almost always (248 of 262); it is recorded as failed and not interpreted.

**The receipts name Harappa's own seal-holders, who are persons.**
- **J1 holds**: of the 51 receipt names that match the end of a seal name, 39 (76%) match a Harappa seal, against
  Harappa's 17% share of seal names (p < 0.0001).
- **J3 holds**: the seal names that end in a receipt name take 740 in 53 of 54 (98%), against 81% of other seal names.
- **J2 holds**: 33 of the 40 single-sign receipt names (82%) are head-class signs.
- The system at Harappa: a person holds a seal with a full name (person class, 740); receipts made out to that person
  in several identical copies give the head of the name, a small number and 400.
- J4 fails (the number does not track the number of copies), J5 fails (the receipt heads are not titled on seals), J6
  fails (their picture categories are ordinary).

**Numbers are bound idioms.**
- **J7 holds**: in M77's multi-line texts a numeral and the sign after it are split by a line break 6.1% of the time,
  other gaps 25.6% (p < 0.0001, both orders).
- **J8 holds**: for the 42 signs that follow a numeral 10+ times, the commonest value accounts on average for 70% of
  their numerals.
- J9 fails (tablet counts are not more varied than seal numerals for the four shared units). **J25 holds**: 'numeral +
  700' is on 4 of 1,607 seals (0.25%): the measure count is a tablet formula.

**Titled fish names.** **J12 holds** (stroke-pair fish names are rarer on tablets, 7.2% against 10.7%) and **J13 holds**
(their heading opens with 861 more often: 36 of 68, against 57 of 172 other headed names; p = 0.007). J10 and J11
fail (not a Mohenjo-daro or unicorn-seal trait).

**Where numbers occur.** **J16 holds**: at Harappa, later count tokens are moulded (64%) where earlier ones were incised
(35% moulded; p = 0.0002): a shift from writing each token to casting them. **J20 holds**: seals with other animals
carry numerals more often than unicorn seals (+9.5 points, p = 0.001). J14, J15, J17, J18, J19, J22, J23, J24 fail
(J22: 34% of human-headed names contain a numeral; J24 the other way: tiered-number names take 520 less).

Tally, counting parts: 145 held, 217 failed (362 registered).

# Thirtieth set, registered before testing (24 September 2026): the Harappa system in detail

Leads: receipts name Harappa's own seal-holders, persons, by the head of the seal name (J1-J3, E3); numeral + sign
pairs are bound idioms (J7, J8); count tokens move from incised to moulded over time (J16); titled fish names take 861
(J13). Conventions as the twenty-ninth set ('receipt'; 'matching seal' = a Harappa seal whose name ends in the receipt's
name; F read with lines reversed; A, B; names; head class as K; 10,000-draw permutations; p < 0.05; length strata as
before).

Receipts and seals (F)
- **HA1** A receipt lies closer in depth to its matching seals than to random Harappa seals with a depth (median
  difference; seal assignments permuted).
- **HA2** A receipt shares its level with its matching seals more often than with random Harappa seals.
- **HA3** Half or more of the receipt heads end three or more different seal names.
- **HA4** Name tablets without 400 match the end of a Harappa seal name less often than receipts do.
- **HA5** Moulded tablets with a name match the end of a Harappa seal name less often than receipts do.
- **HA6** On receipts with a number, the number stands directly before the name body in 70%+.
- **HA10** Receipt heads are the last sign in 80%+ of their occurrences in seal names.
- **HA24** Bar-seal names at Harappa are matched by a receipt name more often than square-seal names at Harappa.
- **HA25** Harappa seal names matched by a receipt come from later levels more often than other Harappa seal names.

Number idioms (pooled A + B unless said)
- **HA7** For signs after a numeral 5+ times on both seals and tablets (F), the commonest value is the same on both for
  75%+ of them.
- **HA8** In names with one numeral, the numeral is the first sign of the name more often than a random position of
  the same name would be (paired sign test).
- **HA9** 'Numeral + fish' is directly followed by the ending more often than 'numeral + another sign'.

Tokens and time (F, Harappa)
- **HA11** Moulded count tokens carry smaller values than incised ones (mean value, label permutation).
- **HA12** Distinct moulded count-token texts come in more copies than distinct incised ones (mean copies, permutation).
- **HA13** Among incised tablets, receipts are a smaller share in later levels.

Titles (pooled A + B)
- **HA14** Names headed by 861 end in 520 more often than names headed by 817 or 820.
- **HA15** Headed stroke-pair fish names take 520 in 80%+ of cases.

Seals, direction, labels
- **HA16** Names on other-animal seals end in 520 more often than names on unicorn seals (F).
- **HA17** Names on other-animal seals are shorter than names on unicorn seals (F, rank test).
- **HA23** Bar-seal names end in 520 more often than square-seal names (F).
- **HA18** Left-to-right pot texts contain a numeral more often than right-to-left pot texts (A).
- **HA19** Left-to-right texts are 'numbers only' more often than right-to-left texts (A).
- **HA20** Copper-tablet lines carry the heading less often than seal lines (A).
- **HA21** 90%+ of copper tablets come from Mohenjo-daro (A).
- **HA22** Texts on rods, bangles and miscellaneous objects (ROD, BNGL, MISC) carry an ending less often than seal texts,
  length-stratified (F).

## Results of the thirtieth set (added after the test; `predict_test30.py`, `results/predict_test30.md`)

Nine held, sixteen failed.

**Receipts and seals.**
- **HA1 holds**: a receipt lies closer in depth to the Harappa seals whose names end in its name (median 5.5 ft) than
  to random Harappa seals (p = 0.0009): receipts and the seals of the people they name were buried near each other.
  HA2 fails narrowly (same level 50%, p = 0.056).
- **HA5 holds**: moulded tablets with a name match a Harappa seal name far less than receipts do (21.5% against 50.6%):
  the moulded name tablets are another genre. HA4 fails narrowly (incised name tablets without 400 match 36.9%, p =
  0.052).
- **HA3 holds** (half of the receipt heads end 3+ different seal names: a head is shared by several seal-holders, so a
  receipt name alone does not pick out one person). HA10 fails (receipt heads are the last sign in only 48% of their
  seal-name occurrences).
- **HA6 fails, and corrects the receipt picture**: on none of the 19 receipts with a number does the number stand
  directly before the name body; it stands inside it. The receipt's 'number' is part of the name (a numeral idiom, J7,
  J8), not a separate count. The receipt format is '[name, which may contain a numeral idiom]-740 400'.
- HA24, HA25, HA13 fail.

**Idioms.** HA7 fails narrowly (the commonest value is the same on seals and tablets for 10 of 14 shared signs, 71%,
bar 75%), HA8 fails (numerals do not open names more than chance), HA9 fails (numeral + fish is not a whole name more
than numeral + another sign).

**Tokens.** **HA11 holds**: moulded count tokens carry smaller values than incised ones (by 0.32, p = 0.0003). HA12
fails (moulded texts do not come in more copies per text).

**Titles.** HA14 fails, HA15 fails the other way: headed stroke-pair fish names take 520 in only 19% (13 of 68). The
L11 / E12 picture (stroke-pair fish take 520; they carry the heading) holds for each part separately but not for their
combination: headed stroke-pair fish names are mostly 740 names.

**Seals and labels.** **HA16 holds** (other-animal seals carry 520 names more: 24.4% against 17.3%, p = 0.040) and **HA17
holds** (their names are shorter, p = 0.0001). **HA20 holds** (no copper-tablet line carries the heading: 0 of 133,
against 20% of seal lines), **HA21 holds** (148 of 149 copper tablets are from Mohenjo-daro), **HA22 holds** (rods,
bangles and miscellaneous objects carry an ending 27 points less than seals: labels). HA23, HA18, HA19 fail.

Tally, counting parts: 154 held, 233 failed (387 registered).

# Thirty-first set, registered before testing (24 September 2026): labels, moulded names, idioms, the heading

Leads: copper tablets are Mohenjo-daro labels without the heading (HA20, HA21, L21, X2); moulded name tablets are not
receipts (HA5); the receipt number is part of the name (HA6); other-animal seals carry 520 and shorter names (HA16,
HA17). Conventions as the thirtieth set (A with 'type', 'site', 'motif', 'direction'; F read with lines reversed;
names; head and attribute classes as K; 'receipt' as before; 'moulded name tablet' = TAB:B with a 740 / 520 ending;
10,000-draw permutations; p < 0.05; length strata as before).

Copper tablets (A)
- **I1** Copper-tablet texts equal a seal name body more often than their own shuffled orders.
- **I2** Copper-tablet lines contain a fish sign less often than seal lines, length-stratified.
- **I3** Copper tablets with the same text carry the same picture (motif field) more often than random pairs of copper
  tablets.
- **I4** The first signs of copper-tablet lines are distributed differently from those of seal lines (MI beyond
  permutation).

Other-animal seals (F)
- **I5** Among non-unicorn seals, the ending depends on the animal (MI beyond permutation).
- **I6** Other-animal seals are a larger share of seals in later levels, at Mohenjo-daro and at Harappa.
- **I7** Names on other-animal seals end in a head-class sign less often than names on unicorn seals.

Moulded name tablets (F)
- **I8** Moulded name tablets end in 520 more often than receipts.
- **I9** Moulded name tablets carry the heading more often than receipts.
- **I10** Distinct moulded name-tablet texts recur on 2+ tablets more often than distinct receipt texts.
- **I11** Moulded name-tablet names contain a fish sign more often than seal names.
- **I12** At Harappa, moulded name tablets come from later levels more often than receipts.
- **I23** Moulded name tablets run left to right more often than seals (A, types TAB:B and SEAL).

Receipts (F)
- **I13** Receipt names contain a numeral more often than seal names.
- **I14** Receipt names contain a fish sign less often than seal names.

Numeral idioms (pooled A + B)
- **I15** Two-sign name bodies are 'numeral + sign' more often than the adjacent pairs inside longer name bodies are.
- **I16** In 'numeral + sign' pairs inside names, the sign is the name's last sign more often than the second sign of
  other adjacent pairs in names is.
- **I17** For numerals directly before a fish on seals, the value depends on the site (Mohenjo-daro / Harappa; MI
  beyond permutation; F).

The heading
- **I18** For heads with 5+ headed and 5+ unheaded names (pooled), the majority ending is the same with and without the
  heading in 80%+.
- **I19** On seals the opener (817 / 820 / 861) depends on the site (Mohenjo-daro / Harappa / other; MI beyond
  permutation; F).
- **I20** Headed names are followed by 90 more often than unheaded names ending 740 (pooled).
- **I21** 861-headed seal names come from Mohenjo-daro more often than 817-headed ones (F).
- **I25** Kalibangan seal lines carry the heading less often than Mohenjo-daro seal lines, length-stratified (F).

Tokens and pots (F)
- **I22** Incised count tokens have the value 4 more often than moulded ones.
- **I24** Pot inscriptions with a name ending come from Harappa more often than seals with a name ending do.

## Results of the thirty-first set (added after the test; `predict_test31.py`, `results/predict_test31.md`)

Fourteen held, eleven failed. (The first run stopped on a comprehension bug in I1, a filter placed after the unpacking;
it was fixed and the set rerun with the same seed.)

**Copper tablets: a vocabulary of their own, tied to the picture.**
- **I3 holds**: copper tablets with the same text carry the same picture in 92% of 586 pairs (p = 0.0001).
- I1 fails decisively: none of the 139 copper-tablet lines is a seal name body. **I4 holds**: they open with different
  signs from seal lines (p = 0.0001). **I2 holds**: they use fish signs less (-12 points).
- The copper-tablet text goes with its picture, not with the names of people: it most likely names or describes what
  is shown. This is the one place where Indus text and a known referent (the animal or scene) are paired consistently,
  the 'copper-tablet bilingual' already used as an anchor in the earlier passes (anchors.py); here it is confirmed that
  the pairing is exclusive and repeatable.

**Moulded name tablets and receipts are different genres.**
- **I8 holds** (moulded name tablets end in 520 in 18.7%, receipts in 1 of 83), **I9 holds** (they carry the heading
  7%, receipts never), **I12 holds** (they are later at Harappa: 51% against 21%), **I23 holds** (they run left to right
  5.4% against 2.5% of seals: moulded, so reversed). I10, I11 fail.
- **I14 holds**: receipt names contain a fish sign far less often than seal names (15.7% against 46.1%). Receipts name
  persons (740, no fish); moulded name tablets carry the fuller, titled, fish-bearing names. I13 fails the other way
  (receipt names hold numerals less often, 22.9% against 47.3%).

**Numeral idioms.** **I15 holds** (a two-sign name is 'numeral + sign' more often than pairs inside longer names: 17.3%
against 14.2%) and **I16 holds** (the idiom's sign closes the name 45.4% of the time, other pairs' second sign 36.5%):
a numeral idiom is often a whole name or its head. I17 fails.

**The heading.** **I18 holds**: for all 14 heads with 5+ headed and 5+ unheaded names, the majority ending is the same
with and without the heading. The heading is outside the name's grammar. **I25 holds**: Kalibangan seal lines carry the
heading less than Mohenjo-daro's (-14.7 points, p = 0.012): a regional habit. I19, I20, I21 fail.

**Other.** **I7 holds** (names on other-animal seals end in a head-class sign less often: 30% against 40%). **I22 holds**
(incised count tokens are 4 in 42%, moulded in 22%). I5, I6, I24 fail.

Tally, counting parts: 168 held, 244 failed (412 registered).

# Thirty-second set, registered before testing (24 September 2026): pictures as outside labels for meaning

Lead: copper-tablet texts go with their picture (I3: same text, same picture in 92% of pairs) and are never seal names
(I1). The picture is an outside label of what a text refers to. Data: A (data/corpus.tsv), field 'motif', first part
before ':' = the picture (copper TAB:C: Hare, Elep, Anth, Comp, Gaur, Goat, Loop, Rhin, Bull1, Tigr, Buff, Othr;
moulded TAB:B: Bull1, Mult, Gavi, Phyt, Scene, Bult, Cros, Gaur, Fish, Zebu ...; seals: Bull1, Gaur, Zebu, Elep, Rhin,
Buff, Tigr, Goat ...). 'Label' = the full text of a copper or moulded tablet with a picture (not 'Othr' or blank);
'marker' of a picture = a sign in 75%+ of that picture's labels and in 25% or fewer of the other pictures' labels of
the same object type. Anchors from the sign list: 341 rhinoceros, 749 and 778 goat, 753 hare (copper); 347
multi-headed animal, 460 tree / plant, 645 cross, 318 gharial (moulded, provisional). 10,000-draw permutations;
p < 0.05.

Copper labels
- **CT1** Half or more of the copper pictures with 4+ labelled tablets have a marker.
- **CT2** Half or more of those pictures have at most two distinct label texts.
- **CT3** Across distinct copper label texts, the last sign has lower entropy than the first sign, beyond within-text
  shuffles (a shared final element).
- **CT4** Copper labels of animal pictures (Hare, Elep, Gaur, Goat, Rhin, Tigr, Buff, Bull1) end in 740 more often than
  labels of other pictures (Anth, Comp, Loop).
- **CT5** The anchor signs occur in the labels of their own picture more often than in other copper labels (pooled
  over 341 / Rhin, 749 and 778 / Goat, 753 / Hare; permutation of pictures among labels).
- **CT11** Labels of the anthropomorph picture (Anth) contain a human-figure sign (Fairservis A) more often than other
  copper labels.
- **CT12** Two labels of the same picture differ by exactly one sign more often than two labels of different pictures.
- **CT13** Labels of the same picture share their first sign more often than their last sign.
- **CT21** Labels of composite pictures (Comp) are longer than other copper labels (rank test).
- **CT22** In copper labels, 740 is preceded by a head-class sign as often as in seal texts or more (Fisher, one-sided
  for more).

Moulded labels
- **CT7** Moulded tablets with the same text carry the same picture more often than random pairs.
- **CT8** Moulded labels of the same picture share a sign more often than labels of different pictures.
- **CT9** The provisional moulded anchors occur in the labels of their picture more often than in other moulded labels
  (pooled over 347 / Mult, 460 / Phyt, 645 / Cros, 318 / Gavi).
- **CT17** Moulded labels of the fish picture contain a fish sign more often than other moulded labels.
- **CT18** Moulded tablets with a picture carry an ending less often than moulded tablets without one.
- **CT19** Distinct moulded texts with a picture recur on 2+ tablets more often than distinct moulded texts without one.

Across object types
- **CT6** The copper anchor signs occur on seals of their own animal more often than on other seals (pooled over 341 /
  Rhin, 749 and 778 / Goat; permutation of animals among seals).
- **CT10** Copper labels and moulded labels share more vocabulary with each other than copper labels with seal texts
  (JSD of sign distributions, rarefied to the copper token count; 1,000 draws, 95%+).
- **CT14** Seals of an animal that also has copper labels (Elep, Gaur, Goat, Rhin, Tigr, Buff) carry a sign of that
  animal's copper labels more often than seals of the other such animals carry it (pooled, permutation).
- **CT15** Seal texts containing a copper anchor sign are on non-unicorn seals more often than other seal texts.
- **CT16** The hare anchor 753 occurs on fewer than 2 seals.
- **CT20** Copper labels of non-animal pictures (Anth, Comp, Loop) end in 520 more often than animal labels.
- **CT23** Copper labels are shorter than moulded labels (rank test).
- **CT24** Moulded tablets with the unicorn picture carry a unicorn-seal name more often than moulded tablets with other
  pictures do.
- **CT25** Where a pictured moulded tablet's text equals a seal name body, the seal shows the same animal more often
  than random seal pairs would.

## Results of the thirty-second set (added after the test; `predict_test32.py`, `results/predict_test32.md`)

Eight held, seventeen failed. 64 copper labels with a picture, 209 moulded labels, 1,181 seals with a picture (A).

**Correction to the sign list.** CT5 fails with a count of zero: the 'firm' copper-tablet equations of
results/sign_list.md (341 rhinoceros, 749 and 778 goat, 753 hare) never occur in the copper labels of their own
picture in data/corpus.tsv. They were taken from Parpola's drawings, where the pictorial sign is on the reverse; in the
ICIT-derived texts the picture is the motif and these signs are not in the text. They are withdrawn as text-based
anchors (CT6, CT15 fail for the same reason; CT16 holds only because 753 never occurs at all). The moulded-tablet
anchors, by contrast, hold (**CT9**: 31 anchor-in-own-picture cases, p = 0.0001).

**Copper labels: picture-specific names.**
- **CT1 holds**: most copper pictures with 4+ labels have marker signs of their own: hare 705, 321, 235; elephant 923,
  706; goat 3, 421, 176, 100, 790; anthropomorph 61, 806, 850, 900; loop 220, 415 (composite and gaur none).
- **CT2 holds** (most pictures have one or two distinct texts: hare 1, anthropomorph 1, elephant 2, goat 2, loop 2).
- **CT3 holds** (the last sign of distinct labels has 1.26 bits less entropy than the first, p = 0.0002: labels share a
  final element) and **CT22 holds** (in copper labels the sign before 740 is a head-class sign in 34 of 36 cases, on
  seals in 43%): the labels are built like names, attribute + head + ending, and name something specific to each
  picture. They are not seal names (I1).
- CT4 fails the other way (animal labels end in 740 less often than non-animal ones: 26% against 62%), CT20 fails (no
  copper label ends in 520), CT11, CT12, CT13, CT21, CT23 fail.

**Moulded labels.** **CT7 holds**: moulded tablets with the same text carry the same picture in 95% of 590 pairs
(p = 0.0001), and **CT8 holds** (same-picture labels share a sign 61.8% against 42.8%). CT17, CT18 (the other way:
pictured moulded tablets carry an ending more), CT19 fail.

**No link across object types.** CT6, CT10, CT14, CT24, CT25 fail: seals of an animal do not carry that animal's copper
label signs more than other seals (91 of 157, p = 0.68); pictured moulded names are not the names on seals with the
same animal; copper labels are not closer to moulded labels than to seals in vocabulary. Each object type pairs its
own texts with its own pictures.

Tally, counting parts: 176 held, 261 failed (437 registered).

# Thirty-third set, registered before testing (24 September 2026): picture markers across label genres

Leads: copper labels are picture-specific names with marker signs (CT1: hare 705 321 235, elephant 923 706, goat 3 421
176 100 790, anthropomorph 61 806 850 900, loop 220 415); moulded tablets pair text and picture (CT7, 95%); nothing
links object types (CT14). Conventions as the thirty-second set (A with its 'motif' field; 'label', 'marker' as
there; 'head' of a label = the sign before 740 / 520 if it has one, else its last sign; Fairservis categories; head
class as K; rebus/copper_tablets.tsv for Parpola's groups; 10,000-draw permutations; p < 0.05).

Copper labels
- **PL1** The label head depends on the picture (MI beyond permutation of pictures).
- **PL2** Labels of two animal pictures share a sign more often than an animal label and a non-animal label do (pair
  counts, pictures permuted).
- **PL3** In Parpola's copper groups, groups with identical texts (the 'link' column) show the same reverse image in
  80%+ of linked pairs.
- **PL4** Copper markers are rarer on seals than the other signs of copper labels (mean seal token count, permutation of
  the marker label among copper-label signs).
- **PL5** No copper marker is a Fairservis animal sign (category C or D).
- **PL6** Label length varies less within pictures than between them (between-picture variance share, permutation).
- **PL7** Copper markers are head-class signs more often than the other copper-label signs.
- **PL23** 90%+ of copper labels are one line.

Moulded labels
- **PL8** Half or more of the moulded pictures with 4+ labels have a marker.
- **PL9** Plant-picture labels (Phyt) contain a Fairservis plant sign (E) more often than other moulded labels.
- **PL10** Scene labels are longer than other moulded labels (rank test).
- **PL11** The moulded label head depends on the picture (MI beyond permutation).
- **PL12** Moulded labels of two animal pictures share a sign more often than an animal label and a non-animal (plant,
  scene, cross, multi-headed) label do.
- **PL13** Copper gaur labels share a sign with moulded gaur labels more often than with other moulded labels.
- **PL14** 90%+ of moulded labels come from Harappa.
- **PL22** Pictured moulded tablets contain a numeral less often than moulded tablets without a picture.
- **PL24** Pictured moulded tablets run left to right more often than moulded tablets without a picture.
- **PL25** Two moulded labels of the same picture differ by exactly one sign more often than two of different pictures.
- **PL21** Pictured moulded labels carry the heading less often than seal texts.

Seals
- **PL15** Half or more of the non-unicorn seal animals with 10+ seals have a loose marker (a sign in 30%+ of their seal
  texts and 10% or fewer of other animals' seal texts).
- **PL16** Seal texts of the same animal share a sign more often than seal texts of different animals (non-unicorn
  seals; animals permuted).
- **PL17** Elephant seals contain 923 or 706 more often than other seals.
- **PL18** Goat seals contain a goat copper marker (3, 421, 176, 100, 790) more often than other seals.
- **PL19** Seals with a composite or anthropomorphic picture contain an anthropomorph copper marker (61, 806, 850, 900)
  more often than other seals.
- **PL20** Gaur seals contain a sign of the copper gaur labels more often than other seals.

## Results of the thirty-third set (added after the test; `predict_test33.py`, `results/predict_test33.md`)

Eight held, seventeen failed. Deviation from the registration: PL2, PL12 and PL16 were run with 1,000 permutations,
not 10,000 (pairwise statistics over up to 30,000 pairs); the smallest possible p is 0.001.

**The picture-text link stays inside the label genres.**
- **PL1 holds** (the copper label's head depends on its picture: MI 2.25 bits over 64 labels, p = 0.0001) and **PL11
  holds** (the same for moulded labels: MI 2.78 bits over 207, p = 0.0001). **PL6 holds** (copper labels of one
  picture have one length: 76% of length variance lies between pictures) and **PL23 holds** (every copper label is one
  line). **PL25 holds** (same-picture moulded labels differ by one sign more often, 1.6% against 0.7%), **PL12 holds**
  (moulded animal labels share signs more, p = 0.013), **PL21 holds** (moulded labels carry the heading less than seals,
  9.8% against 20.3%). **PL5 holds** (no copper marker is an animal-category sign: the labels do not draw the animal).
- **Nothing crosses to the seals.** PL17 fails (0 of 28 elephant seals carry 923 or 706), PL18 fails (0 of 9 goat seals
  carry a goat marker), PL19, PL20 fail, PL15 fails (of six seal animals only the rhinoceros has a loose marker, 820),
  PL16 fails (seal texts of the same animal do not share signs more, p = 0.38). The texts on seals are not about the
  animal on the seal; the label texts on copper and moulded tablets are.
- PL2 fails (copper animal labels do not share signs more), PL4 fails (markers are not rare on seals), PL7 fails, PL8
  fails (only 4 of 11 moulded pictures have a marker: fish 400, unicorn 2 520 240, crs 630, cross 590 235 645 240 90
  104), PL9, PL10, PL13, PL14 (79% of moulded labels from Harappa), PL22 (the other way), PL24 fail.

**Parpola's equations explained.** PL3 fails as registered (no linked pair shares a reverse image), but it shows how
the equations were made: of Parpola's 10 linked copper groups, 8 pair a group whose reverse is an image with a group
whose reverse is a single sign, over the same obverse inscription (hare with 753, markhor with 749, rhinoceros with 341,
goat with 777 / 778). The sign stands in for the picture on the reverse. That is a real substitution, of reverse for
reverse, not a sign inside the text; the withdrawal in CT5 stands as 'not a text anchor', and the equations stand as
Parpola's reverse-side substitutions.

Tally, counting parts: 184 held, 278 failed (462 registered).

# Thirty-fourth set, registered before testing (24 September 2026): labels against names, and the labels' dates

Leads: copper and moulded labels name what is pictured, with picture-specific heads (PL1, PL11), and nothing links them
to the seals of the same animal (PL15-PL20). Conventions as the thirty-third set (A with 'motif'; 'label', 'label head'
as there; copper = TAB:C, moulded = TAB:B with a picture; F read with lines reversed, its motif field 18 and levels as
before; names; head class as K; Fairservis categories; 10,000-draw permutations; p < 0.05).

Labels and names (A)
- **LB1** Copper label heads, where they occur in seal names, stand first more often than last.
- **LB2** Moulded label heads, where they occur in seal names, stand first more often than last.
- **LB3** Copper label heads are rarer on seals than the heads of seal names (mean seal token count, permutation).
- **LB4** Moulded labels are closer to seal texts in vocabulary than copper labels are (JSD, both rarefied to the copper
  token count; 1,000 draws, 95%+).
- **LB18** Seal names containing a copper label head end in 520 more often than other seal names.
- **LB19** Seal names containing a moulded label head end in 520 more often than other seal names.
- **LB20** Labels contain the stroke pair before a fish less often than seal texts.

Label grammar (A)
- **LB5** Copper labels end in 740 more often than moulded labels.
- **LB11** Moulded labels with the unicorn picture end in 520 more often than other moulded labels.
- **LB12** Moulded unicorn labels contain the stroke pair before a fish more often than other moulded labels.
- **LB13** Moulded labels of the multi-headed animal (Mult) contain 347 in half or more.
- **LB14** Moulded labels of the gharial (Gavi) contain 318 in 30% or more.
- **LB15** Moulded plant labels (Phyt) end in 740 less often than moulded animal labels.
- **LB16** Moulded scene labels contain a human-figure sign more often than other moulded labels.
- **LB17** Copper anthropomorph labels (Anth) end in 740 more often than copper animal labels.
- **LB21** Where a copper label contains a numeral, it is the first sign in half or more.
- **LB22** Where a moulded label contains a numeral, it is the first sign in half or more.
- **LB23** The closing formula 705 / 706 + 33 + 520 occurs in at most one label.
- **LB24** 2% or fewer of labels have 400 after an ending.
- **LB25** 2% or fewer of labels have 90 after an ending.

Dates and findspots (F)
- **LB6** At Mohenjo-daro, copper tablets come from later levels more often than seals.
- **LB7** At Harappa, the picture mix of pictured moulded tablets differs between earlier and later levels (MI beyond
  permutation).
- **LB8** Copper tablets with the same picture share a Mohenjo-daro level more often than random pairs.
- **LB9** Pictured moulded tablets with the same picture share a Harappa level more often than random pairs.
- **LB10** Pictured moulded tablets with the same text lie closer in depth than random pairs of pictured moulded
  tablets (median difference).

## Results of the thirty-fourth set (added after the test; `predict_test34.py`, `results/predict_test34.md`)

Nine held, sixteen failed. Deviation: LB10 was run with 1,000 random draws, not 10,000.

**Two held results rest on one text each.**
- **LB11 and LB12 hold** (moulded unicorn labels end in 520 and carry the stroke pair + fish: 31 of 39 each, against 4%
  and 2% of other moulded labels). Checked after the test: 29 of the 39 are one Harappa moulded text, '501 405 2 240
  520', in 29 copies. The result is one text, not a pattern across texts: that batch of unicorn tablets carries a
  titled fish name of the 520 class. It is suggestive (the titled fish name as the name that goes with the unicorn on
  these tablets) and no more.
- **LB17 holds** (copper anthropomorph labels end in 740, 10 of 10, against 26% of animal labels), but all 10 carry the
  same text, '806 845 61 407 850 900 740'. One text of the person class labelling the human-like figure: consistent
  with 740 as the person class (K1, Z3), from a single text.

**Labels against names.**
- **LB4 holds**: moulded labels are closer to seal texts in vocabulary than copper labels are (1,000 of 1,000 draws):
  the Harappa moulded labels use the name vocabulary, the Mohenjo-daro copper labels their own.
- LB1 and LB2 fail the other way: label heads, where they occur in seal names, stand last far more often than first
  (copper 121 against 12; moulded 464 against 239): the label heads are name heads, not attributes. LB3, LB18, LB19
  fail (LB18 the other way: seal names with a copper label head are rarely 520 names, 4.8%). LB20 fails the other way
  (labels carry the stroke-pair fish more, 12.5% against 7.6%: the unicorn batch).
- LB5, LB13 (347 in 23% of multi-headed animal labels), LB15, LB16, LB21, LB22 fail; **LB14 holds** (318 in 35% of
  gharial labels). **LB23 holds** (the seal closing formula is on one label only). LB24 and LB25 fail: 400 (12%) and
  90 (7%) do follow endings on labels.

**Dates and findspots.**
- **LB7 holds**: the pictures on Harappa moulded tablets change between earlier and later levels (MI 0.31, p = 0.0001).
  **LB9 holds** (same-picture moulded tablets share a level, 58%, p = 0.002) and **LB10 holds** (same-text pictured
  tablets lie closer in depth, median 3.0 ft, p = 0.001). The moulded label tablets were made picture by picture, in
  batches, at particular times.
- LB6 fails (copper tablets are not later than seals at Mohenjo-daro), LB8 fails (4 pairs).

Tally, counting parts: 193 held, 294 failed (487 registered).

# Thirty-fifth set, registered before testing (24 September 2026): the core findings, city by city

The strongest results so far mostly pool every site. This set asks whether each holds separately at Mohenjo-daro and at
Harappa, the two cities with enough texts to act as independent replication samples, and whether rules learned in one
city predict the other. Data: F, intact objects, lines reversed (M4); A for direction (SR19). Each hypothesis holds only
if it holds at both cities (p < 0.05 each, or the stated threshold each); a city with under 20 cases for a test makes
the hypothesis fail as untestable there. Names, head class (K, from A), Fairservis categories, numerals and notations
as before; 10,000-draw permutations.

Grammar of names
- **SR1** The last sign carries more information about the ending than the first: MI(last; ending) minus MI(first;
  ending) exceeds its value with endings permuted.
- **SR2** The last sign of a name comes from a smaller inventory than the first, beyond within-name shuffles.
- **SR3** Human-figure heads take 740 more often than other heads.
- **SR4** A head-to-ending rule learned in one city (majority ending per head with 3+ names) predicts the other city's
  endings for those heads at 90%+ and above the majority baseline (binomial), in both directions.
- **SR7** A long name minus its first sign is an attested name more often than minus its last (McNemar).
- **SR8** The affixed fish (231, 233, 235, 240) are a name's last sign less often than the plain fish 220.
- **SR16** 80%+ of heads with 5+ names take one ending in 90%+ of them.
- **SR17** Categorised heads of 740 names are humans, weapons, implements or measures (A, H, I, K) more often than
  categorised heads of 520 names, fish heads left out.
- **SR15** For heads with 5+ headed and 5+ unheaded names, the majority ending is the same with and without the heading
  in 80%+.

Units kept whole (multi-line texts of all object types)
- **SR5** The 30 highest-PMI pairs (count 10+) of the *other* city's single-line texts are split by a line break less
  often than other gaps.
- **SR6** A numeral and the sign after it are split by a line break less often than other gaps.

Numbers
- **SR9** The short stroke pair is followed by a fish more often than the short three.
- **SR10** Among values 5-8 the tiered form is a larger share than among values 3-4.
- **SR11** Long-stroke numerals stand before a container or device sign (Fairservis J, K) more often than short ones.
- **SR12** The value of a numeral depends on the sign after it (MI beyond permutation).
- **SR20** Long-stroke numerals open their line more often than short ones.
- **SR13** Tablet texts differing at one position differ at a numeral more often than seal names differing at one
  position do.

Objects and signs
- **SR14** Unicorn seals carry longer texts than other-animal seals (rank test).
- **SR18** Frequent signs are graphically simpler (Spearman of complexity against log token count, negative).
- **SR19** Left-to-right texts are rarer on seals than on other objects (A).

## Results of the thirty-fifth set (added after the test; `predict_test35.py`, `results/predict_test35.md`)

Ten held, ten failed. This set is the robustness check of the core findings: each had to hold at Mohenjo-daro and at
Harappa separately.

**Findings that hold in both cities** (the project's most robust results):
- **SR1** the last sign of a name carries more information about the ending than the first (p = 0.0001 in both);
- **SR2** name heads come from a smaller inventory than first signs (p = 0.0001, 0.0006);
- **SR3** human-figure heads take 740 without exception (53 of 53 at Mohenjo-daro, 26 of 26 at Harappa);
- **SR16** the head fixes the ending (85% and 88% of heads with 5+ names);
- **SR8** the affixed fish are attributes (last in 14% and 28% of cases, the plain fish 33% and 45%);
- **SR10** tiered numerals write 5-8 (60% and 64% of those values, against 5% and 3% of 3-4);
- **SR11** long-stroke numerals count containers and devices (10% against 4%; 75% against 4%);
- **SR12** the number depends on the sign that follows (MI 1.29 and 0.96 bits);
- **SR20** long-stroke numerals open their line (20% against 13%; 62% against 31%);
- **SR18** frequent signs are graphically simpler (Spearman -0.15 and -0.16).

**Near miss.** SR4: the head-to-ending rule learned at Harappa predicts Mohenjo-daro at 93.2% (baseline 83.7%), but the
rule learned at Mohenjo-daro predicts Harappa at 88.6% (baseline 79.0%), under the registered 90%. The rule transfers
well above chance in both directions (p < 1e-7) and misses the bar in one.

**Harappa only** (the pooled results were carried by Harappa): SR9 (the stroke pair before fish: 41.5% against 5.3% at
Harappa, 23.0% against 15.4% at Mohenjo-daro, p = 0.09), SR13 (tablets vary at numerals: 28.7% at Harappa; Mohenjo-daro's
27 tablet variant pairs never do), SR14 (unicorn seals carry longer texts: p = 0.0007 at Harappa, 0.11 at Mohenjo-daro),
SR19 (seals avoid left-to-right writing: p = 0.0002 at Harappa, 0.083 at Mohenjo-daro). These are Harappa habits, not
general rules of the script, until shown elsewhere.

**Not testable per city** (too few cases in at least one city): SR5 and SR6 (multi-line texts are few; the bound-pair
and numeral-idiom line-break results rest on M77's line division), SR7 (Harappa 16 discordant names, though p = 0.038),
SR15 (headed names are rare at Harappa), SR17 (non-fish 520 heads are few in each city).

Tally, counting parts: 203 held, 304 failed (507 registered).

# Thirty-sixth set, registered before testing (24 September 2026): the core findings beyond the two cities and over time

The thirty-fifth set found ten findings that hold at Mohenjo-daro and at Harappa separately, and four that hold at
Harappa only. Here they meet a third sample: all other home sites pooled ('other sites': every site except Mohenjo-daro,
Harappa and the West Asian finds), and Mohenjo-daro's earlier (Early + Intermediate) and later (Late) levels taken
separately. Data F, intact objects, lines reversed; A for direction (OS19). Tests, statistics and thresholds are those
of the thirty-fifth set's hypothesis with the same number; a sample with under 20 cases fails the hypothesis as
untestable. 10,000-draw permutations; p < 0.05.

The ten core findings at the other sites
- **OS1** (as SR1) the last sign carries more information about the ending than the first.
- **OS2** (as SR2) heads come from a smaller inventory than first signs.
- **OS3** (as SR3) human-figure heads take 740 more often than other heads.
- **OS16** (as SR16) 80%+ of heads with 5+ names fix their ending.
- **OS8** (as SR8) affixed fish are a name's last sign less often than the plain fish.
- **OS10** (as SR10) the tiered form is for 5-8.
- **OS11** (as SR11) long-stroke numerals stand before container and device signs.
- **OS12** (as SR12) the number depends on the following sign.
- **OS20** (as SR20) long-stroke numerals open their line.
- **OS18** (as SR18) frequent signs are simpler.

Transfer
- **OS4** The head-to-ending rule learned at Mohenjo-daro and Harappa together predicts the other sites' endings for
  those heads at 90%+ and above the majority baseline (binomial).

The Harappa habits at the other sites
- **OS9** (as SR9) the stroke pair is followed by a fish more often than the short three.
- **OS13** (as SR13) tablet variants differ at a numeral more often than seal-name variants.
- **OS14** (as SR14) unicorn seals carry longer texts than other-animal seals.
- **OS19** (as SR19) left-to-right texts are rarer on seals than on other objects (A).

Over time at Mohenjo-daro (each finding must hold in the earlier and in the later levels)
- **OT1** (as SR1) the last sign decides the ending.
- **OT3** (as SR3) human-figure heads take 740.
- **OT16** (as SR16) the head fixes the ending.
- **OT11** (as SR11) long strokes count containers and devices.
- **OT12** (as SR12) the number depends on the following sign.

## Results of the thirty-sixth set (added after the test; `predict_test36.py`, `results/predict_test36.md`)

Nine held, eleven failed. Other sites: 491 objects (Kalibangan 102, Lothal 101, Dholavira 87, Chanhu-daro 53, Nausharo
29, others); Mohenjo-daro earlier 348, later 258 objects.

**At the other sites (a third sample), seven of the ten core findings hold**: OS1 (the last sign decides the ending,
p = 0.043), OS8 (affixed fish are attributes, p = 0.027), OS10 (tiered for 5-8, 71% against 19%), OS11 (long strokes
count containers, 9.1% against 0.7%), OS12 (the number depends on the sign, p = 0.0001), OS20 (long numbers open lines,
40% against 13%), OS18 (frequent signs simpler, Spearman -0.31). OS2 fails (heads a smaller inventory: +0.13 bits,
p = 0.22) and OS3, OS16 are not testable (10 human heads; 9 heads with 5+ names).

**The head rule does not transfer to the smaller sites.** OS4 fails clearly: the head-to-ending rule learned at
Mohenjo-daro and Harappa predicts the other sites' endings at 81.2%, below their majority baseline of 83.3% (p = 0.79).
That the last sign decides the ending holds at the other sites (OS1), but which ending a given head takes is not the
same there: the head-ending pairings are local to the two cities, or the names are different ones.

**Harappa habits.** **OS14 holds** at the other sites (unicorn seals carry longer texts, p = 0.0001): it is Mohenjo-daro
that lacks it, not a Harappa peculiarity. OS9, OS19 fail (the stroke pair + fish and seals avoiding left-to-right are
Harappa habits), OS13 is not testable (2 tablet variant pairs).

**Over time at Mohenjo-daro.** Only **OT12 holds** in both earlier and later levels (the number depends on the sign:
MI 1.39 and 1.68). OT1 holds in the earlier levels (p = 0.003) and narrowly misses in the later (p = 0.062); OT3,
OT16, OT11 lack power in at least one period (4 to 15 human heads, 6 to 8 heads with 5+ names, 60 long numerals).

Tally, counting parts: 212 held, 315 failed (527 registered).

# Thirty-seventh set, registered before testing (24 September 2026): regional name habits (round 1 of 10)

Lead: the head-to-ending rule does not carry from the two cities to the other sites (OS4). Regions: Sindh (Mohenjo-daro,
Chanhu-daro, Allahdino, Amri, Kot Diji, Lakhanjo-daro, Nausharo), north (Harappa, Kalibangan, Banawali, Rakhigarhi,
Farmana, Bhirrana, Rupar), Gujarat (Lothal, Dholavira, Surkotada, Desalpur, Kanmer, Gola Dhoro, Rangpur). F, intact
objects, lines reversed; names as before; seal names are the first name on each seal. 10,000-draw permutations; p < 0.05.
Helpers in rtools.py.

- **RG1** The head of seal names depends on the region (MI beyond permutation).
- **RG2** The first sign of seal names depends on the region.
- **RG3** Gujarat seal names are shorter than Sindh seal names (rank test).
- **RG4** Gujarat seal lines carry the heading less often than Sindh seal lines, length-stratified.
- **RG5** 30%+ of Gujarat seal names have a head never seen as a head at Mohenjo-daro or Harappa.
- **RG6** At least three head signs with 5+ names each occur as heads in one region only.
- **RG7** The notation of numerals (short / long / tiered) depends on the region.
- **RG8** Kalibangan seal names end in 520 more often than Harappa seal names.
- **RG9** Dholavira texts are longer than the texts of the other Gujarat sites (rank test).
- **RG10** Chanhu-daro seal names share their head with Mohenjo-daro seal names (head seen at Mohenjo-daro) more often
  than Lothal seal names do (Sindh neighbours against a distant site).

## Results of the thirty-seventh set (added after the test; `predict_test37.py`, `results/predict_test37.md`)

Two held, eight failed. Names look alike across regions: the head (RG1, p = 0.12) and the first sign (RG2, p = 0.34) do
not depend on the region, Gujarat names are not shorter (RG3), not less headed (RG4), and only 15% have a head unseen in
the two cities (RG5). Kalibangan is not a 520 site (RG8), Dholavira texts are not longer (RG9), Chanhu-daro does not share
Mohenjo-daro's heads more than Lothal does (RG10). **RG6 holds**: four heads with 5+ names occur only in Sindh (222, 455,
927, 255). **RG7 holds**: the numeral notation depends on the region (p = 0.0001), the one regional difference that is
general. So the OS4 failure is not a different stock of names in the smaller sites; it is the head-ending pairings that
vary. Tally, counting parts: 214 held, 323 failed (537 registered).

# Thirty-eighth set, registered before testing (24 September 2026): the longest texts (round 2 of 10)

Lines of 8+ signs ('long') against lines of 5-7 ('middle'); pooled A + B unless said; F for objects and sites.
10,000-draw permutations; p < 0.05.

- **LT1** Long lines contain two or more ending tokens (740 / 520) more often than middle lines.
- **LT2** In long lines with an ending before the end, the material after the first ending itself closes with an ending
  (740 / 520, optionally + 90 / 400 / 151) in half or more.
- **LT3** Long lines contain a numeral more often than middle lines.
- **LT4** Long lines are on objects other than seals more often than middle lines (F).
- **LT5** Long lines carry the heading more often than middle lines.
- **LT6** Long lines can be split into two parts each attested as a whole line elsewhere more often than their own
  sign-order shuffles can.
- **LT7** Distinct long texts recur on 2+ objects less often than distinct middle texts (F).
- **LT8** Long lines end in an ending (with or without 90 / 400 / 151) less often than middle lines.
- **LT9** Signs rare in the corpus (5 or fewer tokens in A + B) make up a larger share of the tokens of long lines than
  of middle lines.
- **LT10** Long lines come from Mohenjo-daro more often than middle lines (F).

## Results of the thirty-eighth set (added after the test; `predict_test38.py`, `results/predict_test38.md`)

Three held, seven failed. 210 long lines (8+ signs), 1,215 middle lines (5-7). Deviation: LT6 used 1,000 shuffles.
**LT1 holds** (two or more endings: 7.1% of long lines against 1.1%), **LT3 holds** (a numeral: 79% against 69%),
**LT7 holds** (distinct long texts recur less: 2.9% against 6.6%). But long lines are not two texts joined: none of 210
splits into two lines attested elsewhere (LT6), and after a first ending the rest closes with an ending in only 30%
(LT2). Long lines are not off the seals (LT4 the other way), not titled (LT5 the other way), end in an ending as often
as middle lines (LT8), use rare signs no more (LT9) and are not a Mohenjo-daro trait (LT10). Long lines are single,
longer, more often numbered compositions, a few of them with a second name. Tally, counting parts: 217 held, 330 failed
(547 registered).

# Thirty-ninth set, registered before testing (24 September 2026): Harappa over time (round 3 of 10)

Harappa objects of F (intact, lines reversed) with a level: earlier = HARP 3B and Vats Strata IV-VII, later = HARP 3C
and Vats Strata I-III (as before). 'Both periods' = the test holds in the earlier and in the later objects separately;
under 20 cases in either makes it fail as untestable. 10,000-draw permutations; p < 0.05.

- **HT1** (as SR1, both periods) the last sign carries more information about the ending than the first.
- **HT2** (as SR11, both periods) long-stroke numerals stand before container and device signs more than short ones.
- **HT3** (as SR12, both periods) the number depends on the following sign.
- **HT4** (as SR10, both periods) the tiered form is for 5-8.
- **HT5** Receipts are a larger share of tablets in the earlier levels than in the later.
- **HT6** Count-token values (long 2 / 3 / 4 before 700) are larger in the earlier levels (mean, label permutation).
- **HT7** The share of 520 among names differs between the periods (Fisher, two-sided).
- **HT8** (as SR9, both periods) the stroke pair is followed by a fish more often than the short three.
- **HT9** The left-to-right share differs between the periods (A is undated; F lines reversed carry no direction, so
  direction is taken from A objects matched to F by CISI number; Fisher, two-sided).
- **HT10** The head of names depends on the period (MI beyond permutation).

## Results of the thirty-ninth set (added after the test; `predict_test39.py`, `results/predict_test39.md`)

Seven held, three failed. Harappa objects with a level: earlier 465, later 346.
**Stable across time**: HT1 (the last sign decides the ending: p = 0.047 earlier, 0.0001 later), HT2 (long strokes count
containers: 79% and 64% against 8% and 0%), HT3 (the number depends on the sign: MI 1.01 and 1.16). **What changes**:
HT5 (receipts are 11.5% of earlier tablets, 5.7% of later), HT6 (earlier count tokens count more, +0.27), HT9 (left-to-
right writing 7.9% earlier, 3.8% later), HT10 (the head signs of names change, MI 0.31, p = 0.013). HT7 fails (the 520
share is stable, 16.6% against 15.8%). HT4 and HT8 lack cases per period (12-15 tiered numerals of 5-8; 16-23 short
threes). At Harappa the grammar and the number system are stable while the administration (receipts, count sizes),
the writing direction and the particular names change. Tally, counting parts: 224 held, 333 failed (557 registered).

# Fortieth set, registered before testing (24 September 2026): the core findings in Mahadevan's transcription (round 4 of 10)

Findings tested so far on F, A or pooled samples, now on B alone (the M77 texts absent from A; Mahadevan's own
transcription). Tests and thresholds as the thirty-fifth set's hypothesis named. 10,000-draw permutations; p < 0.05;
under 20 cases fails as untestable.

- **MB1** (as SR10) the tiered form is for 5-8.
- **MB2** (as SR11) long-stroke numerals stand before container and device signs more than short ones.
- **MB3** (as SR20) long-stroke numerals open their line more than short ones.
- **MB4** (as SR8) the affixed fish are a name's last sign less often than the plain fish.
- **MB5** (as SR16) 80%+ of heads with 5+ names fix their ending.
- **MB6** (as SR12) the number depends on the following sign.
- **MB7** (as SR1) the last sign carries more information about the ending than the first.
- **MB8** (as LT1) lines of 8+ signs hold two or more endings more often than lines of 5-7.
- **MB9** (as L16) the fish variants 233, 235, 240 alternate with 220 in otherwise identical names more than matched
  random sign pairs.
- **MB10** (as J8) for signs after a numeral 10+ times, the commonest value accounts on average for 60%+ of their
  numerals.

## Results of the fortieth set (added after the test; `predict_test40.py`, `results/predict_test40.md`)

Nine held, one failed. On Mahadevan's transcription alone (1,554 lines, 544 names) the core findings replicate: MB1
(tiered for 5-8: 66% against 6%), MB2 (long strokes before containers and devices: 56% against 3%), MB3 (long numbers
open lines: 57% against 21%), MB4 (affixed fish last 13% against 31%), MB5 (28 of 33 heads fix their ending), MB6 (the
number depends on the sign, MI 1.05), MB7 (the last sign decides the ending, +0.26 bits), MB9 (fish variants alternate
with 220, p = 0.001), MB10 (the commonest value covers 67% of a sign's numerals). MB8 fails narrowly (two endings in 3
of 42 long lines against 5 of 306, p = 0.060). The core of the name grammar and the number system does not depend on
the transcription. Tally, counting parts: 233 held, 334 failed (567 registered).

# Forty-first set, registered before testing (24 September 2026): repeated and doubled signs (round 5 of 10)

'Double' = two adjacent identical signs, numerals left out (the samples split joined doubles, signs.SPLIT, so A and B
count them alike). A, B, F (lines reversed); names as before. 10,000-draw permutations; p < 0.05.

- **DB1** Doubles occur more often than within-line shuffles produce. A and B.
- **DB2** A doubled sign stands inside a name (not as its last sign) more often than single tokens of the same signs do
  (pooled A + B).
- **DB3** Names ending in a double take the same ending as names ending in the single sign, for 80%+ of signs with 3+
  names of each kind (pooled).
- **DB4** A name body containing a double is also attested with the single sign in its place more often than a random
  sign replaced by its own double would be (pooled; bodies with a double, permutation of positions).
- **DB5** Tablet lines contain a double more often than seal lines, length-stratified (F).
- **DB6** A name body repeats a sign non-adjacently less often than within-name shuffles produce. A and B.
- **DB7** Lines with a double are shorter than lines without, among lines with a name (rank test, pooled).
- **DB8** A double is split by a line break less often than other gaps (M77 multi-line texts, both line orders).
- **DB9** Harappa lines contain a double more often than Mohenjo-daro lines, length-stratified (F).
- **DB10** The three commonest doubled signs account for 60%+ of all doubles (pooled).

## Results of the forty-first set (added after the test; `predict_test41.py`, `results/predict_test41.md`)

Three held, seven failed. Doubling is deliberate (DB1: 118 doubles in A, 80 in B, both above every shuffle, p = 0.001
on 1,000 shuffles) and name bodies avoid repeating a sign at a distance (DB6: 13 of 775 bodies in A, 6 of 224 in B,
p = 0.001 and 0.017), so a repeat is either adjacent or absent. DB3 holds but on one sign only (832, the only sign with
3+ names of each kind); it is not evidence. The rest fail: doubled tokens are not more often inside the name (DB2, 62%
against 65%); no body with a double is attested with the single sign instead (DB4, 0 against 4 discordant); tablets
and seals double alike (DB5); lines with a double are longer, not shorter (DB7, mean 5.5 against 4.6); line breaks do
not avoid doubles (DB8, 5 of 36, p = 0.17); Harappa does not double more (DB9); doubles are spread over many signs
(DB10, 615 alone is 90 of 198, the top three 57%). Doubling is one sign's habit (615, the 'jar-pair') plus a thin
scatter; a double is its own unit, never a variant spelling of the single sign. Deviations: DB1 and DB6 used 1,000
shuffles; DB4 was run as a paired sign test (removing a sign of the double against removing a random other sign of the
same body) rather than a permutation of positions. Tally, counting parts: 236 held, 341 failed (577 registered).

# Forty-second set, registered before testing (24 September 2026): sign order inside the name (round 6 of 10)

Name bodies as before (name_of, pooled A + B unless stated); numerals kept. 'Pair' = two signs in one body, any
distance, ordered by which comes first; pairs co-occurring in 5+ bodies. 10,000-draw permutations; p < 0.05.

- **OR1** For 70%+ of pairs one order holds in 90%+ of their bodies (pooled).
- **OR2** The dominant orders are transitive: among triples whose three pairs all qualify, cyclic triples are fewer
  than the 25% random orientation gives (binomial).
- **OR3** A sign's relative position in the body (0 first, 1 last) is more fixed than within-body shuffles make it:
  summed within-sign variance of relative position lower than in 1,000 shuffles.
- **OR4** Dominant orders agree between A and B for 85%+ of pairs that qualify in both.
- **OR5** Dominant orders agree between Mohenjo-daro and Harappa (F names) for 80%+ of pairs qualifying in both
  (3+ bodies each).
- **OR6** A recurrent prefix (body minus its last sign, 3+ bodies) combines with more distinct last signs than when
  last signs are shuffled among bodies of the same length.
- **OR7** Names grow at the front: of 3-sign bodies with exactly one attested 2-sign sub-body (same ending) made by
  dropping the first or the last sign, the attested one is the tail (first sign dropped) more than half the time.
- **OR8** In bodies of 4+ signs, an attested shorter body (same ending) is found as the final segment more often than
  as the initial segment (paired sign test).
- **OR9** The sign just before the last sign carries more information about the last sign than the first sign does
  (bodies of 3+; MI of the adjacent sign higher, and significant).
- **OR10** Pairs occurring in both orders are more common among signs in the first two positions than in the last two
  (distinct pairs, bodies of 4+; Fisher).

## Results of the forty-second set (added after the test; `predict_test42.py`, `results/predict_test42.md`)

Eight held, two failed. Order inside the name is a ranking, not a set of fixed pairs: only 49% of pairs keep one order
90%+ of the time (OR1 fails), yet the dominant orders are almost perfectly transitive (OR2: 38 cyclic of 749 triples,
5% against 25%) and each sign keeps a relative place (OR3, p = 0.001). The ranking is the same in both transcriptions
(OR4: 25 of 26 pairs) and in both cities (OR5: 67 of 75). Names are built right to left from the head: a recurrent
prefix combines with more heads than chance (OR6, p = 0.039), a 3-sign body sheds its first sign to give an attested
name far more often than its last (OR7: 76 against 29), and a long body ends in an attested name far more often than it
begins with one (OR8: 239 against 29). The adjacent sign predicts the head better than the first sign (OR9: 3.69
against 3.24 bits). Order is not looser at the front (OR10: 11.6% reversible in both places). Caveat: OR7 and OR8
partly follow from the head-final rule (a prefix lacks a head, so it is rarely a whole name); the new content is OR2,
OR3 and OR6. Deviations: OR3 used 1,000 shuffles; OR10 counted adjacent pairs; bodies counted as distinct names.
Tally, counting parts: 244 held, 343 failed (587 registered).

# Forty-third set, registered before testing (24 September 2026): the slot ranking (round 7 of 10)

A sign's rank = its mean relative position (0 first, 1 last) in distinct name bodies of 2+ signs, signs with 5+ such
tokens. 'Follows the ranking' = an adjacent pair whose earlier sign has the lower rank (pairs with equal-rounded ranks
left out). 10,000-draw permutations; p < 0.05.

- **SK1** Ranks from A predict the order of 85%+ of adjacent pairs in B's distinct bodies.
- **SK2** Ranks from Mohenjo-daro names predict 80%+ of adjacent pairs in Harappa names (F).
- **SK3** Ranks from seal names predict 75%+ of adjacent pairs in names on tablets and other objects (F).
- **SK4** Rank tercile depends on Fairservis category (MI, permutation over signs).
- **SK5** Numerals stand earlier in the body than other signs (relative position, bodies of 3+, rank test).
- **SK6** Frequent signs rank later (Spearman between token count and rank positive, permutation).
- **SK7** Bodies with an adjacent pair against the ranking by 0.2+ are more often attested once (single object) than
  bodies without one (pooled A + B; Fisher).
- **SK8** Ranks from 3-sign bodies correlate with ranks from 4+-sign bodies (Spearman 0.6+, significant).
- **SK9** Ranks under ending 740 correlate with ranks under 520 (Spearman 0.6+, significant; 5+ tokens under each).
- **SK10** Seal names follow the ranking more often than names on other objects (adjacent pairs, ranks from all F
  names; Fisher).

## Results of the forty-third set (added after the test; `predict_test43.py`, `results/predict_test43.md`)

Three held, seven failed. A single scalar rank (mean relative position, 117 signs) predicts only about 70% of adjacent
pairs out of sample: A to B 70% (SK1), Mohenjo-daro to Harappa 71% (SK2), seals to other objects 74% (SK3), all under
their thresholds and well above chance. So the transitive ordering found in the forty-second set is not captured by one
number per sign; order is partly pair-specific. The rank is stable across body length (SK8: Spearman 0.71) but only
moderately across endings (SK9: 0.49, significant but under 0.6). Bodies that break the rank are mostly one-off names
(SK7: 92% against 81% attested once), consistent with inversions being rare variants or errors. Frequent signs rank
slightly later (SK6: 0.16, p = 0.043). Rank does not follow Fairservis category (SK4), numerals are not early (SK5, mean
0.50 both), and seals keep the rank no better than other objects (SK10, 70% against 76%). Tally, counting parts: 247
held, 350 failed (597 registered).

# Forty-fourth set, registered before testing (24 September 2026): lines without a name (round 8 of 10)

'Non-name line' = a line of 2+ signs with no 740 or 520 anywhere; 'name line' = a line for which name_of gives a name.
Head class from classes(A). A, B pooled unless F is named. 10,000-draw permutations; p < 0.05.

- **NN1** Non-name lines end in a head-class sign less often than name bodies do.
- **NN2** Non-name lines are more often off seals than name lines, length-stratified (F).
- **NN3** On seals, the motif depends on whether the line is a name line or a non-name line (A, MI, permutation).
- **NN4** Non-name lines carry a numeral more often than name lines.
- **NN5** Non-name lines of 3+ signs contain an attested name body (2+ signs) as a contiguous run more often than
  within-line shuffles do.
- **NN6** Non-name lines are shorter than name lines (rank test).
- **NN7** Distinct non-name texts recur on 2+ objects more often than distinct name texts (F; Fisher).
- **NN8** Non-name lines open with a heading (817, 820, 861) less often than name lines.
- **NN9** Harappa has a larger share of non-name lines than Mohenjo-daro, length-stratified (F).
- **NN10** The five commonest last signs of non-name lines cover 50%+ of them.

## Results of the forty-fourth set (added after the test; `predict_test44.py`, `results/predict_test44.md`)

Seven held, three failed. Half the lines (2,019 of 3,914 in A + B) have no ending, and they are not names that lost it:
they end in a head-class sign 18% of the time against 42% for name bodies (NN1). They are shorter (NN6: 3.4 against
4.6 signs), carry numerals more (NN4: 60% against 44%), sit off the seals more (NN2: +9.4 points, length-stratified),
are commoner at Harappa (NN9: +7.8 points) and are headed slightly less (NN8: 12% against 14%). About a fifth of those
of 3+ signs contain an attested name body, more than shuffles give (NN5: 249 of 1,200, p = 0.001), so names are also
cited inside other formulas. They do not recur more (NN7: 14.5% both), the seal motif does not track them (NN3), and
their last signs are spread (NN10: top five 700, 400, 390, 156, 405 cover 38%). Reading: a second genre of short
counting or tagging formulas, mostly on tablets and at Harappa, that can embed a name without its ending. NN2 and NN9
overlap with the known tablet/receipt findings. Deviation: NN5 used 1,000 shuffles. Tally, counting parts: 254 held,
353 failed (607 registered).

# Forty-fifth set, registered before testing (24 September 2026): names inside the other formulas (round 9 of 10)

Non-name lines as in the forty-fourth set. 'Embedded body' = the longest contiguous run (2+ signs) of a non-name line
that is an attested name body (A + B pooled; ties to the rightmost). 10,000-draw permutations; p < 0.05.

- **EM1** The sign right after an embedded body is 400, 90, 151 or 700 in 30%+ of cases where a sign follows.
- **EM2** 2-sign bodies that are embedded are commoner as names than 2-sign bodies that are never embedded (rank test on
  name counts).
- **EM3** Embedded bodies seen 2+ times are followed by 2+ different signs (or line end) in 50%+ of cases.
- **EM4** Non-name lines with an embedded body are off seals more often than other non-name lines, length-stratified
  (F).
- **EM5** Harappa non-name lines embed a body less often than Mohenjo-daro ones, length-stratified (F).
- **EM6** Where an embedded body has something before it, the sign just before is a numeral or a heading (817, 820,
  861) in 40%+ of cases.
- **EM7** In lines with a numeral, the numeral is the first sign more often in non-name lines than in name lines.
- **EM8** The first sign depends on the line kind (non-name against name lines; MI, permutation).
- **EM9** 2-sign non-name lines are numeral + sign more often than 2-sign name bodies are.
- **EM10** Non-name lines ending in 400 have an embedded body directly before the 400 in 30%+ of cases.

## Results of the forty-fifth set (added after the test; `predict_test45.py`, `results/predict_test45.md`)

Six held, four failed. 300 of 2,019 non-name lines embed an attested name body. The embedded names are the common ones
(EM2: 2-sign bodies used as names 3.4 times on average against 1.7 for those never embedded) and combine freely with
what follows (EM3: 40 of 53 have 2+ different followers). Embedding lines sit off the seals (EM4: +10 points,
length-stratified). The formula genre is number-first: a numeral opens 47% of non-name lines that have one, against 24%
of name lines (EM7); half of 2-sign non-name lines are numeral + sign against 17% of 2-sign bodies (EM9); the first sign
alone separates the two kinds (EM8, p = 0.0001). What follows an embedded name is not a post-name or container sign
(EM1: 12%; commonest 845, 151, 156), what precedes it is not mostly a number or heading (EM6: 28%), Harappa does not
embed less (EM5), and 400 in non-name lines never follows a name body (EM10: 0 of 170; it follows 156, 158, 892, 137),
so 400 there is a different use from the post-name 400 of the receipts. Tally, counting parts: 260 held, 357 failed
(617 registered).

# Forty-sixth set, registered before testing (24 September 2026): replicating rounds 5-9 on held-out data (round 10 of 10)

Each test repeats a finding of the forty-first to forty-fifth sets on data not used to find it: B alone (Mahadevan's
transcription), or 'other sites' = F objects from sites other than Mohenjo-daro and Harappa. Definitions and tests as
in the original sets; head class and ranks from A. 10,000-draw permutations (1,000 where the original used 1,000).

- **RP1** (DB1) Doubles exceed within-line shuffles at other sites.
- **RP2** (DB6) Name bodies avoid non-adjacent repeats at other sites (bodies of 3+).
- **RP3** (OR2) Dominant orders are transitive in B alone (pairs in 3+ bodies): cyclic triples under 25%.
- **RP4** (OR7) Names grow at the front in B alone.
- **RP5** (OR8) Long bodies end in an attested name more than they begin with one, in B alone.
- **RP6** (SK7) In B, bodies against the A ranking are more often one-off names.
- **RP7** (NN1) In B, non-name lines end in a head-class sign less often than name bodies.
- **RP8** (NN4) At other sites, non-name lines carry a numeral more often than name lines.
- **RP9** (EM7) At other sites, a numeral is first more often in non-name lines than in name lines (lines with one).
- **RP10** (EM9) In B, 2-sign non-name lines are numeral + sign more often than 2-sign name bodies.

## Results of the forty-sixth set (added after the test; `predict_test46.py`, `results/predict_test46.md`)

Nine held, one failed. At the smaller sites (529 objects, 548 lines) doubling is above shuffles (RP1: 18 doubles,
p = 0.02) and names avoid distant repeats (RP2: 1 of 93 bodies, p = 0.014); non-name lines carry more numerals (RP8:
70% against 56%) and open with them more (RP9: 39% against 22%). In Mahadevan's transcription alone the order findings
hold: transitive orders (RP3: 2 cyclic of 94 triples), names growing at the front (RP4: 18 against 4) and ending in a
known name (RP5: 52 against 5); non-name lines rarely end in a head sign (RP7: 14% against 46%) and 2-sign ones are
counts (RP10: 52% against 16%). The one failure is the weakest earlier finding: bodies that break the A ranking are not
more often one-off names in B (RP6: 78% against 82%), so SK7 does not replicate and should be treated as unconfirmed.
Caveat: B is a second transcription of largely the same objects, so it guards against transcription choices, not
against the sample; the other-site tests are the independent ones. Tally, counting parts: 269 held, 358 failed (627
registered).

# Forty-seventh set, registered before testing (24 September 2026): inside the number-first formulas (second loop, round 1 of 10)

'Formula' = a non-name line (2+ signs, no 740 or 520), as in the forty-fourth set. A + B pooled unless F is named.
Numeral value and kind from numerals.NUMS. 10,000-draw permutations; p < 0.05.

- **FI1** In formulas, the numeral kind (short, long, tiered) depends on the sign that follows (MI, permutation).
- **FI2** The last sign of a formula depends on whether it opens with a numeral (MI, permutation).
- **FI3** Formulas opening with a numeral are shorter than other formulas (rank test).
- **FI4** (numeral value, next sign) pairs in formulas are idiomatic: fewer distinct pairs than when numerals are
  shuffled among formula numeral slots.
- **FI5** 20%+ of formulas with a numeral share their non-numeral residue with another formula carrying a different
  numeral value.
- **FI6** In formulas, 90%+ of numerals stand directly before a non-numeral sign.
- **FI7** Harappa formulas open with a numeral more often than Mohenjo-daro formulas, length-stratified (F).
- **FI8** Tablet formulas open with a numeral more often than seal formulas, length-stratified (F).
- **FI9** 10%+ of formula tokens (numerals left out) are signs never seen in a name body.
- **FI10** Formulas found on 2+ objects are shorter than formulas found on one (F, distinct texts, rank test).

## Results of the forty-seventh set (added after the test; `predict_test47.py`, `results/predict_test47.md`)

Nine held, one failed. The formulas have the number grammar of the count tokens: the numeral kind depends on the next
sign (FI1, MI 0.73 bits), (value, sign) pairs are idioms (FI4: 293 distinct pairs among 1,138, fewer than any shuffle),
and 39% of formulas with a numeral recur with a different number and the same residue (FI5), the shape of a tally
entry. Numeral-first formulas are short (FI3: 2.6 against 3.7 signs) and end differently (FI2). Numeral-first is the
Harappa and tablet habit (FI7: +26.5 points; FI8: +23.2, both length-stratified). 11% of formula tokens are signs never
seen in a name (FI9), and formulas repeated on several objects are shorter (FI10: 3.0 against 3.9). Only 76% of
numerals stand directly before a non-numeral sign (FI6 fails); the rest end the line or stand next to another numeral.
Tally, counting parts: 278 held, 359 failed (637 registered).

# Forty-eighth set, registered before testing (24 September 2026): objects with more than one line (loop 2, round 2)

F objects (intact, lines reversed); 'multi-line' = 2+ lines. Line kinds: name line (name_of), formula (non-name line),
other. 10,000-draw permutations; p < 0.05. Random-pair baselines draw lines from different objects.

- **ML1** A name line and a formula share an object more often than when line kinds are shuffled among the lines of
  multi-line objects (keeping each object's line count).
- **ML2** Formulas sharing an object with a name line carry a numeral more often than formulas on one-line objects.
- **ML3** Two lines of one object share a sign more often than two lines from different multi-line objects.
- **ML4** Lines of multi-line objects are shorter than lines of one-line objects (rank test).
- **ML5** Two name lines on one object share their ending more often than name lines paired across objects.
- **ML6** Two name lines on one object share their last body sign more often than name lines paired across objects.
- **ML7** Formulas on multi-line objects open with a numeral more often than formulas on one-line objects,
  length-stratified.
- **ML8** A larger share of Mohenjo-daro objects than Harappa objects is multi-line.
- **ML9** Multi-line objects recur as identical texts on 2+ objects more often than one-line objects of the same type
  class (tablets only; Fisher).
- **ML10** Where one line of a two-line object carries a numeral, the other carries one less often than when lines are
  paired across two-line objects.

## Results of the forty-eighth set (added after the test; `predict_test48.py`, `results/predict_test48.md`)

Four held, six failed. Multi-line objects are rare among intact F objects (78 of 3,681), so most tests are thin. A name
line and a formula share an object more often than shuffled line kinds give (ML1: 36 of 78, p = 0.0004), and multi-line
objects are a Mohenjo-daro habit (ML8: 3.4% against 0.6% at Harappa); their lines are a little shorter (ML4: 3.4
against 3.7). On two-line objects a numeral tends to sit in one line only (ML10: 16 of 50 partners with a numeral,
p = 0.0497, borderline). Failures: the formula beside a name is not more often a count (ML2: 47% against 68%, the
other way), lines of one object do not share signs (ML3), too few objects carry two names (ML5, ML6: 3 pairs, not
testable), multi-line formulas do not open with numbers more (ML7), and only 3 multi-line tablet texts exist (ML9).
Bug fix before recording: the first ML10 run shuffled the partner lines among themselves, which leaves the count
unchanged (p = 1.0); the recorded test draws each partner from all lines of two-line objects, as registered. Tally,
counting parts: 282 held, 365 failed (647 registered).

# Forty-ninth set, registered before testing (24 September 2026): the tally entries (loop 2, round 3)

F formula lines with a numeral (non-name lines, intact objects, lines reversed). Residue = the line with its numerals
removed (non-empty); value = sum of numeral values. 'Tally group' = a residue seen with 2+ different values; 'tally
formula' = a formula in one. 10,000-draw permutations; p < 0.05.

- **TL1** Values inside a tally group span a narrower range than same-size draws from all formula values.
- **TL2** A larger share of numeral formulas are tally formulas at Harappa than at Mohenjo-daro.
- **TL3** 80%+ of tally groups have a residue of 1 or 2 signs.
- **TL4** Tally residues contain a sign never seen in a name body more often than residues of other numeral formulas.
- **TL5** Formula values 1-12 grow rarer as they grow larger (Spearman between value and count negative, significant).
- **TL6** The value depends on the residue (tally groups with 5+ formulas; MI, permutation).
- **TL7** Tally formulas are on tablets more often than other numeral formulas.
- **TL8** All members of a tally group come from one site more often than when sites are shuffled among tally formulas.
- **TL9** In 80%+ of tally groups the numeral stands in the same position (first sign or not) in every member.
- **TL10** Tally groups contain two consecutive values more often than same-size draws from all formula values.

## Results of the forty-ninth set (added after the test; `predict_test49.py`, `results/predict_test49.md`)

Six held, four failed, with a large caveat: of the 619 tally formulas in 34 groups, 401 are the known count tokens
(numeral + 700, Harappa tablets, values 2-4), so TL1 (narrow value range, p = 0.0001), TL2 (Harappa 76% against 19%)
and TL7 (tablets 76% against 28%) mostly restate that finding. The other groups are small: 156 (44, mostly 3), 861 (31,
Harappa tablets, 3), 390 (24, seals, 3-8), 405 (10), 817 390 (10). What is new: tallied items are 1-2 signs (TL3: 32 of
34), each item has its own typical count (TL6, MI 0.55 bits, p = 0.0001), and counts fall off steeply above 4 (TL5:
89, 307, 369, 195, 69, 50, 31, 18, 9, 1, 1, 8 for 1-12). Failures: tallied items are ordinary signs, not formula-only
ones (TL4: 3% against 42%); groups span sites rather than staying at one (TL8: 4 of 34); the numeral moves (TL9: 68%);
groups do not favour consecutive values (TL10). Tally, counting parts: 288 held, 369 failed (657 registered).

# Fiftieth set, registered before testing (24 September 2026): numbers on seals against numbers on tablets (loop 2, round 4)

F formula lines with a numeral on seals (SEAL types) and on tablets (TAB types). Value = sum of numeral values in the
line; kind from numerals. Embedded body as in the forty-fifth set. 10,000-draw permutations; p < 0.05.

- **SC1** Seal values are larger than tablet values (rank test).
- **SC2** Seal numerals are tiered more often than tablet numerals.
- **SC3** The sign after a numeral depends on seal against tablet (MI, permutation).
- **SC4** Seal numeral formulas are longer than tablet numeral formulas (rank test).
- **SC5** On seals (A), the motif depends on whether the line carries a numeral (MI, permutation).
- **SC6** Among seals, numeral formulas are commoner at Mohenjo-daro than at Harappa.
- **SC7** Where 390 follows a numeral, the value is 3 or more in 90%+ of cases (F, all objects).
- **SC8** Seal numeral formulas open with a heading (817, 820, 861) more often than tablet numeral formulas.
- **SC9** Seal numeral formulas embed an attested name body more often than tablet numeral formulas.
- **SC10** Seal values are more varied than tablet values (entropy difference, permutation of the seal/tablet label).

## Results of the fiftieth set (added after the test; `predict_test50.py`, `results/predict_test50.md`)

Eight held, two failed. Numbers on seals and on tablets are two practices. Seal counts are larger (SC1: mean 4.0
against 3.1), use the tiered form (SC2: 12% against 1%), vary more (SC10: 3.1 against 1.9 bits), count different signs
(SC3, MI 0.68 bits), sit in longer formulas (SC4: 4.3 against 2.7 signs), open with a heading (SC8: 24% against 5%) and
cite a name more often (SC9: 14% against 8%). 390 after a numeral takes 3 or more in 95% of cases, commonly 5-6 (SC7).
Seal counts are not tied to the animal motif (SC5) and are as common on Mohenjo-daro seals as on Harappa seals (SC6:
24% and 25%). Caveat: tablet numerals are dominated by the 700 count tokens (values 2-4), which drives SC1, SC2 and
SC10. Tally, counting parts: 296 held, 371 failed (667 registered).

# Fifty-first set, registered before testing (24 September 2026): the seal count formulas (loop 2, round 5)

'Seal count' = an F seal formula (non-name line) with a numeral; 'counted sign' = the non-numeral sign right after a
numeral; value = the run of numerals before it. Head class from classes(A). 10,000-draw permutations; p < 0.05.

- **CT1** 30%+ of seal counts are exactly heading (817, 820, 861) + numeral(s) + one sign.
- **CT2** Counted signs on seals are head-class signs less often than name bodies' last signs are.
- **CT3** 60%+ of signs counted 5+ times on seals take 3+ different values.
- **CT4** 70%+ of signs counted 3+ times on seals also occur in name bodies.
- **CT5** Longer seal counts carry larger values (Spearman, permutation).
- **CT6** Headed seal counts carry larger values than unheaded ones (rank test).
- **CT7** The counted sign ends the line in 40%+ of seal counts.
- **CT8** Seal counts are on square seals (SEAL:S) more often than seal name lines are.
- **CT9** The counted sign depends on Mohenjo-daro against Harappa (seal counts; MI, permutation).
- **CT10** Under 50% of counted-sign tokens on seals are of signs also counted on tablets.

## Results of the fifty-first set (added after the test; `predict_test51.py`, `results/predict_test51.md`)

Four held, six failed. The counted sign on a seal is usually not a head sign (CT2: 20% against 42% of name heads), is
also an ordinary name sign (CT4: 37 of 42), takes many values (CT3: 14 of 21; 390 and 405 run 2-9, 220 and 151 up to
12), and closes the line about half the time (CT7: 48%). There is no fixed template (CT1: heading + number + sign in
8%), value does not grow with length (CT5) or heading (CT6: headed 3.4 against 3.9), seal counts are not more often on
square seals (CT8: 79% against 86%, the other way), the cities do not clearly count different things (CT9, p = 0.095),
and seals mostly count the same signs tablets count (CT10: 62%). So the same signs are counted on both media; what
differs (fiftieth set) is the range and the notation. Tally, counting parts: 300 held, 377 failed (677 registered).

# Fifty-second set, registered before testing (24 September 2026): where the order is free (loop 2, round 6)

Ranks as in the forty-third set, computed on A and applied to B's distinct name bodies unless stated; rank terciles over
ranked signs. 'Reversible pair' = two signs attested adjacent in both orders among distinct bodies (A + B). Fish
signs from signs.FISH. 10,000-draw permutations; p < 0.05.

- **PO1** In B, adjacent pairs across terciles follow the A rank more often than pairs within a tercile.
- **PO2** In B, adjacent pairs within the early tercile follow the rank no better than chance (two-sided binomial
  p >= 0.05).
- **PO3** 30%+ of reversible pairs include a numeral.
- **PO4** Reversible pairs are within one Fairservis category more often than non-reversible adjacent pairs.
- **PO5** For reversible pairs, the two orders take different endings more often than when endings are shuffled among
  bodies.
- **PO6** For reversible pairs, the two orders come from different cities more often than when sites are shuffled
  among the bodies (F names).
- **PO7** Frequent signs have more variable positions (Spearman between token count and positional SD, permutation).
- **PO8** Bodies with an inversion (against the rank by 0.2+) are longer than bodies without (rank test, A + B).
- **PO9** 40%+ of inverted adjacent pairs include a numeral or a fish sign.
- **PO10** Dominant pairwise orders from A predict B's adjacent pairs better than the scalar A rank on the pairs both
  cover (sign test on discordant pairs).

## Results of the fifty-second set (added after the test; `predict_test52.py`, `results/predict_test52.md`)

Seven held, three failed. The ordering is pairwise, not scalar: dominant pair orders from A predict B's adjacent pairs
far better than the scalar rank where they disagree (PO10: 66 against 12). The rank works between slots and less within
them (PO1: 74% against 62%), though the early slot is not free (PO2: 25 of 35 follow the rank, p = 0.017). Of 81 pairs
attested in both orders, 42% involve a numeral (PO3), and they are more often of one Fairservis category (PO4: 11%
against 2%; categories are known for few signs). Inversions sit in long names (PO8: 5.6 against 3.7 signs) and 47% of
inverted pairs involve a numeral or fish sign (PO9); frequent signs move more (PO7, borderline p = 0.048). The order is
not set by the ending (PO5, p = 0.07) or by the city (PO6: 7 of 52). Reading: a fixed skeleton (slots and pair
precedences), with numerals and fish attributes floating inside long names. Deviation: PO6 used 1,000 shuffles. Tally,
counting parts: 307 held, 380 failed (687 registered).

# Fifty-third set, registered before testing (24 September 2026): how predictable each genre is (loop 2, round 7)

Genres: name lines (name_of) and formulas (non-name lines), A + B unless F is named. 'Repeat rate' of a set of lines =
share of its adjacent-pair tokens whose pair occurs in 2+ lines of the set. Genre comparisons shuffle the genre labels
among lines (1,000 shuffles for repeat rates, 10,000 otherwise); p < 0.05.

- **EN1** Formulas have a higher repeat rate than name lines.
- **EN2** Formulas use fewer distinct signs than name lines at equal token counts (in 95%+ of 1,000 equal-size
  subsamples).
- **EN3** Signs attested once in A + B are commoner per token in name lines than in formulas.
- **EN4** First signs are more varied (entropy) in name lines than in formulas.
- **EN5** Name bodies' last signs are less varied (entropy) than formulas' last signs.
- **EN6** Harappa lines have a higher repeat rate than Mohenjo-daro lines (F).
- **EN7** Tablet lines have a higher repeat rate than seal lines (F).
- **EN8** The rank-frequency (Zipf) slope is steeper for formulas than for name lines (log-log least squares over
  ranks 1-50).
- **EN9** The sign sets of Mohenjo-daro and Harappa overlap more (Jaccard) for name lines than for formulas (F).
- **EN10** Long lines (8+) have a lower repeat rate than lines of 3-5 signs.

## Results of the fifty-third set (added after the test; `predict_test53.py`, `results/predict_test53.md`)

Two held, eight failed, and the failures mostly point the other way: name lines, not formulas, are the formulaic
genre. Name lines repeat their adjacent pairs more (EN1: 0.85 against 0.72), use fewer distinct signs at equal token
counts (EN2: formulas had fewer in 0 of 1,000 subsamples) and hold fewer once-attested signs (EN3: 0.7% against 1.3%
per token); their sign frequencies are more skewed (EN8: slope -0.81 against -0.69). First and last signs are about as
varied in both (EN4, EN5), and name and formula sign sets overlap across the cities about equally (EN9, p = 0.064).
Harappa lines (EN6: 0.79 against 0.73) and tablet lines (EN7: 0.88 against 0.70) repeat their pairs more. EN10 (long
lines repeat less: 0.69 against 0.79) fails on its permutation because the shuffled groups keep line counts, not token
counts, so the smaller long-line group is penalised under the null as well; the design was size-confounded. Reading:
the formula genre is the open, varied one (many signs, many rare ones), the name genre the closed, repetitive one.
Tally, counting parts: 309 held, 388 failed (697 registered).

# Fifty-fourth set, registered before testing (24 September 2026): signs used only in formulas (loop 2, round 8)

'Formula-only sign' = a non-numeral sign in a formula (non-name line) that never occurs in a name body (A + B pooled).
'Shared sign' = a non-numeral formula sign that does occur in a name body. Token-level comparisons within formulas
unless stated. 10,000-draw permutations; p < 0.05.

- **FO1** Formula-only tokens are last in their formula more often than shared tokens.
- **FO2** Formula-only tokens follow a numeral more often than shared tokens.
- **FO3** Formula-only signs have fewer tokens in A + B than shared signs (rank test over signs).
- **FO4** Formulas with a formula-only sign are off seals more often, length-stratified (F).
- **FO5** Among signs with 2-5 tokens in F, formula-only signs are found at one site only more often than shared signs.
- **FO6** Formulas with a formula-only sign are shorter than other formulas (rank test).
- **FO7** Formula-only tokens are on objects other than seals and tablets more often than shared tokens (F).
- **FO8** Of signs formula-only in A that occur in B, 80%+ are absent from B's name bodies.
- **FO9** Formula-only tokens are preceded by a heading (817, 820, 861) more often than shared tokens.
- **FO10** Formulas with a formula-only sign carry no numeral more often than other formulas.

## Results of the fifty-fourth set (added after the test; `predict_test54.py`, `results/predict_test54.md`)

Five held, five failed. 173 signs occur in formulas but never in a name body; they are rare (FO3: mean 3.6 tokens
against 45), hold as a class in the other transcription (FO8: 19 of 23 of A's formula-only signs are absent from B's
name bodies), close their formula more often (FO1: 43% against 34%), appear in formulas without a numeral (FO10: 50%
against 37%) and are a little commoner on objects other than seals and tablets (FO7: 12% against 9%). They are not
counted items (FO2: 20% against 21% after a numeral), not headed (FO9), not local to one site (FO5), and their formulas
are longer, not shorter (FO6: 4.0 against 3.2). Against expectation they sit on seals more, not less (FO4: -15.3
points, length-stratified). Reading: a long tail of rare, line-final labels in longer uncounted seal formulas, which
is what makes the formula genre open. Tally, counting parts: 314 held, 393 failed (707 registered).

# Fifty-fifth set, registered before testing (24 September 2026): other endings on seals (loop 2, round 9)

'Uncounted seal formula' = an F seal line of 2+ signs with no 740/520 and no numeral. 'Candidate ending' = a sign last
in 10+ such lines. Positions and names from A + B pooled unless stated. Head class from classes(A). 10,000-draw
permutations; p < 0.05.

- **EH1** 50%+ of candidate endings stand last in 70%+ of their A + B tokens.
- **EH2** In uncounted seal formulas ending in a candidate, the sign before it is head-class more often than signs at
  other non-final positions.
- **EH3** In 15%+ of uncounted seal formulas ending in a candidate, the rest of the line is an attested name body.
- **EH4** 10+ name bodies are attested both before 740/520 and before a candidate ending.
- **EH5** The candidate ending depends on the sign before it (MI, permutation).
- **EH6** Seal lines ending in a candidate are shorter than seal name lines (rank test).
- **EH7** Under 5% of candidate tokens (A + B) are directly followed by 740 or 520.
- **EH8** Among seal lines, those ending in a candidate are commoner at Mohenjo-daro than at Harappa.
- **EH9** 70%+ of candidates stand last in 50%+ of their B tokens.
- **EH10** Five or fewer candidates cover 50%+ of the last signs of uncounted seal formulas.

## Results of the fifty-fifth set (added after the test; `predict_test55.py`, `results/predict_test55.md`)

Six held, four failed. Eight signs close 10+ uncounted seal formulas: 400, 151, 527, 156, 390, 615, 368, 154. Five of
them are line-final signs (EH1: 400 91%, 151 85%, 527 83%, 156 80%, 154 78% of their tokens are last), and they behave
like name endings: the sign before them is a head more often than other positions (EH2: 14% against 4%), the rest of
the line is an attested name body in 22% (EH3), 42 bodies occur both before 740/520 and before a candidate (EH4), and
the ending depends on the preceding sign (EH5, p = 0.0001). Their lines are short (EH6: 3.2 against 5.2 signs). The
candidates are not a closed set: 390, 615 and 368 are ordinary body signs that often precede 740/520 (EH7: 18%
followed by an ending), 154 is never final in B (EH9: 5 of 8), and the five commonest cover only 33% of these lines
(EH10). Nor are they a Mohenjo-daro habit (EH8). Caveat: 400 and 151 are the known post-name signs, so 'body + 400'
may be a name with the ending left out rather than a new ending; 527, 156 and 154 are the new candidates. Tally,
counting parts: 320 held, 397 failed (717 registered).

# Fifty-sixth set, registered before testing (24 September 2026): replicating loop 2 on held-out data (loop 2, round 10)

Each test repeats a finding of the forty-seventh to fifty-fifth sets on B alone (Mahadevan's transcription) or on 'other
sites' (F objects outside Mohenjo-daro and Harappa). Definitions as in the original sets, computed within the held-out
data. 10,000-draw permutations unless the original used 1,000.

- **RQ1** (FI5) In B, 20%+ of formulas with a numeral share their residue with a formula of another value.
- **RQ2** (FI1) At other sites, the numeral kind in formulas depends on the next sign (MI).
- **RQ3** (FI8) At other sites, tablet formulas open with a numeral more often than seal formulas.
- **RQ4** (SC2) At other sites, seal numerals are tiered more often than tablet numerals.
- **RQ5** (SC8) At other sites, seal numeral formulas open with a heading more often than tablet ones.
- **RQ6** (PO10) Dominant pair orders from B predict A's adjacent pairs better than B's scalar rank.
- **RQ7** (EN1, reversed) In B, name lines have a higher repeat rate than formulas (1,000 shuffles).
- **RQ8** (EN2, reversed) In B, formulas use more distinct signs than name lines at equal token counts (95%+ of 1,000
  subsamples).
- **RQ9** (FO1) In B, formula-only tokens (signs never in B's name bodies) are last in their formula more often than
  shared tokens.
- **RQ10** (EH4) In B, 5+ name bodies are attested both before 740/520 and before 400, 151, 527, 156 or 154.

## Results of the fifty-sixth set (added after the test; `predict_test56.py`, `results/predict_test56.md`)

Six held, four failed. Replicated: formulas recur with only the number changed in B (RQ1: 48%); the numeral kind
depends on the next sign at the smaller sites (RQ2, p = 0.0001); pairwise precedence beats the scalar rank in the
reverse direction, B to A (RQ6: 82 against 15); names are the repetitive genre and formulas the open one in B (RQ7:
0.79 against 0.71; RQ8: 1,000 of 1,000 subsamples); and 15 B bodies occur both before 740/520 and before one of the
other closers (RQ10). Not replicated: the seal/tablet contrasts at the smaller sites (RQ3-RQ5) point the same way but
rest on 9 tablet numerals, too few to test; and formula-only signs do not close their formula more often in B (RQ9:
37% against 39%), so FO1 is unconfirmed. Tally, counting parts: 326 held, 401 failed (727 registered).

# Fifty-seventh set, registered before testing (24 September 2026): the other closers (loop 3, round 1)

'Closers' = 400, 151 (post-name signs) and 527, 156, 154 (new candidates, fifty-fifth set). 'Closer line' = a line of
2+ signs with no 740/520 whose last sign is a closer and whose remainder is an attested name body. 'Regular line' = a
name line (name_of). A + B pooled unless F is named. Head class from classes(A). 10,000-draw permutations; p < 0.05.

- **CL1** Bodies seen in 400-closer lines are attested as 'body + ending + 400' more often than other name bodies are.
- **CL2** 400-closer lines are on seals more often than lines with 'ending + 400' (F).
- **CL3** Bodies of 400-closer lines take 740 in their regular lines more often than name bodies overall.
- **CL4** Bodies before 527, 156 or 154 are shorter than name bodies before 740/520 (rank test).
- **CL5** Closer lines ending in 527, 156 or 154 are commoner at Harappa than at Mohenjo-daro (F, share of lines).
- **CL6** 70%+ of closer lines have 2 or 3 signs.
- **CL7** Under 10% of closer tokens are directly followed by 740 or 520.
- **CL8** 20%+ of 527, 156 and 154 tokens directly follow 740 or 520.
- **CL9** Closer lines open with a heading less often than regular lines.
- **CL10** 50%+ of the signs standing before a closer (types with 2+ such tokens) are head-class.

## Results of the fifty-seventh set (added after the test; `predict_test57.py`, `results/predict_test57.md`)

Two held, eight failed, and the set deflates the fifty-fifth. Requiring the remainder to be an attested name body
leaves only 73 closer lines in A + B, nearly all 151 (29) and 156 (28), and only 3 with 400, so the 'ending left out
before 400' idea cannot be tested (CL1-CL3). Closer lines are short (CL6: 86% of 2-3 signs) because their 'bodies' are
mostly one sign (CL4: mean 1.3 against 3.1): 'X 151' and 'X 156' pairs, not names with another ending. The closers are
not post-name signs (CL8: 527, 156, 154 follow an ending in 1% of tokens), they precede 740/520 in 21% of tokens (CL7),
the sign before them is usually not a head (CL10: 4 of 18), and they are not a Harappa habit (CL5) or unheaded (CL9).
The fifty-fifth set's alternative endings should be read as short sign pairs; only 400 and 151 as post-name signs remain
from before. Tally, counting parts: 328 held, 409 failed (737 registered).

# Fifty-eighth set, registered before testing (24 September 2026): the fish signs (loop 3, round 2)

Fish signs = signs.FISH (220 plain and its variants). Names from A + B pooled unless F is named; 'body tokens' = signs
inside name bodies. 10,000-draw permutations (1,000 for within-body shuffles); p < 0.05.

- **FS1** Two different fish signs stand adjacent in bodies more often than within-body shuffles give.
- **FS2** In adjacent fish pairs of different signs, 220 is second more often than first (sign test).
- **FS3** Fish tokens are more frequent per token in name bodies than in formulas.
- **FS4** Bodies ending in a fish sign are more varied in their ending (entropy) than bodies ending in a non-fish sign
  (label permutation).
- **FS5** Fish tokens in bodies are preceded by a numeral more often than other body tokens.
- **FS6** Which fish sign is used depends on the preceding sign (body tokens with one; MI, permutation).
- **FS7** Which fish sign is used depends on the following sign (MI, permutation).
- **FS8** Which fish sign is used depends on the city (F names, Mohenjo-daro against Harappa; MI, permutation).
- **FS9** Fish tokens are a smaller share of name-body tokens at Harappa than at Mohenjo-daro (F).
- **FS10** Fish tokens in formulas are last more often than other formula tokens.

## Results of the fifty-eighth set (added after the test; `predict_test58.py`, `results/predict_test58.md`)

Seven held, three failed. Fish signs are a name-internal series: 16% of body tokens against 7% of formula tokens (FS3).
Different fish stand side by side more than shuffles give (FS1: 174 pairs, p = 0.001), with no fixed order between the
plain fish and its variants (FS2: 220 second 30, first 28). A fish is counted more often than other body signs (FS5: 21%
after a numeral against 10%), and which fish is written depends on both neighbours (FS6: MI 0.97 bits; FS7: 0.87 bits)
and a little on the city (FS8: 0.05 bits, p = 0.0001). Fish-final bodies take either ending (FS4: entropy 0.96 against
0.38 bits), restating the mixed fish heads of earlier sets. Harappa does not use fewer fish (FS9) and fish do not close
formulas (FS10). Reading: the fish series behaves like a set of qualifiers in names, chosen by context, often counted,
and stackable. Tally, counting parts: 335 held, 412 failed (747 registered).

# Fifty-ninth set, registered before testing (24 September 2026): the headings (loop 3, round 3)

'Heading' = 817, 820 or 861 as the first sign of a line; 'headed line' = a line of 2+ signs opening with one. Name lines
(name_of) and formulas (non-name lines). A + B pooled unless F is named. 10,000-draw permutations; p < 0.05.

- **HD1** The heading sign depends on the genre (name line against formula; MI, permutation).
- **HD2** Among headed formulas, those opening with 861 carry a numeral more often than those opening with 817.
- **HD3** Headed name lines are longer than unheaded name lines (rank test).
- **HD4** 50%+ of headed lines have a numeral as their second sign.
- **HD5** Seal lines are headed more often than tablet lines, length-stratified (F).
- **HD6** The heading sign depends on the city (F, Mohenjo-daro against Harappa; MI, permutation).
- **HD7** 30%+ of name bodies in headed name lines are also attested in unheaded name lines.
- **HD8** Headed name lines take 740 more often than unheaded name lines.
- **HD9** 90%+ of 817, 820 and 861 tokens are line-first.
- **HD10** 80%+ of numerals directly after a heading are of the short kind.

## Results of the fifty-ninth set (added after the test; `predict_test59.py`, `results/predict_test59.md`)

Six held, four failed. 515 headed lines (861 229, 820 158, 817 128). The heading is nearly always followed by a stroke
numeral, almost always 2 (HD4: 83% have a numeral second; HD10: 98% of those short, 402 of 429 are 2), so 'heading + 2'
is one unit. It is a seal feature (HD5: +14.4 points over tablets, length-stratified) and optional: 31% of headed name
bodies are also attested without it (HD7). The heading sign depends weakly on genre (HD1: 0.015 bits, p = 0.004) but
not on the city (HD6) or the ending (HD8: 740 in 84% against 86%). HD3 (headed name lines longer: 5.6 against 4.4)
holds only because the heading unit adds two signs; the bodies themselves are about as long. HD2 is confounded the same
way (the 2 after the heading counts as a numeral: 89% against 98%). 25% of 817/820/861 tokens are not line-first (HD9
fails), so these signs also occur inside lines. Tally, counting parts: 341 held, 416 failed (757 registered).

# Sixtieth set, registered before testing (24 September 2026): are rare signs variants? (loop 3, round 4)

'Rare sign' = a non-numeral sign with 2-5 tokens in the sample; 'common sign' = 20+ tokens. 'Frame' of a token =
(previous sign, next sign), '#' at line ends. 'Best match' of a rare sign = the common sign sharing most of its frames
(ties to the commoner), if any. A + B pooled unless stated. p < 0.05.

- **VR1** 60%+ of rare-sign tokens stand in a frame also attested with a common sign.
- **VR2** For rare signs with a best match in both A and B, the match is the same for 50%+.
- **VR3** A rare sign's majority position (last in a name body or not) equals its best match's for 80%+ of rare signs
  in name bodies.
- **VR4** A rare sign and its best match share their majority ending for 70%+ of pairs where both end names.
- **VR5** Rare-sign tokens are off seals more often than common-sign tokens (F).
- **VR6** Rare-sign tokens are in formulas more often than common-sign tokens (among name lines and formulas).
- **VR7** A rare sign and its best match share a Fairservis category for 30%+ of pairs with both categorised.
- **VR8** Rare-sign tokens are line-final more often than common-sign tokens.
- **VR9** For 10%+ of lines holding one rare sign, replacing it with its best match gives an attested line.
- **VR10** The best match is among the 20 commonest signs for 50%+ of rare signs with a match.

## Results of the sixtieth set (added after the test; `predict_test60.py`, `results/predict_test60.md`)

Four held, six failed; the variant hypothesis is not supported. The held tests have no null and are expected by
chance: rare-sign tokens mostly sit in frames also used by a common sign (VR1: 76%), the best match is usually a very
common sign (VR10: 73% in the top 20), and swapping in the match gives an attested line 13% of the time (VR9). The tests
that would show a real variant relation fail: the best match differs between A and B (VR2: 3 of 13 agree), does not
share the rare sign's position (VR3: 69%) or ending (VR4: 58%), and rarely shares its category (VR7: 1 of 4). Rare
signs are commoner in formulas (VR6: 57% against 42%) but not off the seals (VR5, the other way) and not line-final
(VR8: 14% against 26%). With 2-5 tokens per sign, frame matching cannot recover variants; rare signs stay unassigned.
Tally, counting parts: 345 held, 422 failed (767 registered).

# Sixty-first set, registered before testing (24 September 2026): recurring units inside names (loop 3, round 5)

'Unit' = an adjacent sign pair found in 5+ distinct name bodies (A + B pooled unless stated). 1,000 within-body shuffles
where a null is needed; p < 0.05.

- **SG1** Units cover more body tokens than the same count of recurring pairs does in within-body shuffles (coverage =
  share of body tokens inside a pair recurring in 5+ bodies).
- **SG2** In bodies of 3+, unit tokens end the body more often than they start it (sign test).
- **SG3** 90%+ of units are never attested adjacent in the reverse order.
- **SG4** 70%+ of units present in F names at Mohenjo-daro or Harappa are present at both.
- **SG5** 60%+ of A's units (5+ bodies in A) recur in 3+ of B's bodies.
- **SG6** The mean share of a unit's first sign followed by its commonest follower (among its body tokens) is 0.5+.
- **SG7** 30%+ of units contain a numeral.
- **SG8** 20%+ of units contain a fish sign.
- **SG9** 60%+ of units found in long bodies (5+) are also found in bodies of 3-4.
- **SG10** 30%+ of units are also attested as whole 2-sign bodies.

## Results of the sixty-first set (added after the test; `predict_test61.py`, `results/predict_test61.md`)

Seven held, three failed. 103 adjacent pairs recur in 5+ distinct name bodies, and they cover 46% of body tokens, more
than recurring pairs cover in shuffled bodies (SG1, p = 0.001). Units sit at the end of the name more than the start
(SG2: 326 against 207, partly the head-final rule), are shared by both cities (SG4: 78 of 102), are reused between short
and long names (SG9: 95 of 102), stand alone as whole 2-sign names about half the time (SG10: 48 of 103), and a third
contain a numeral (SG7: 35) and nearly half a fish sign (SG8: 47). They are not rigid: 30% also occur reversed (SG3:
73 of 103 never reversed), a unit's first sign does not strongly call its second (SG6: 0.45), and only 29% of A's units
recur 3+ times in B (SG5), which is smaller and splits some compounds differently, so the unit inventory depends on the
transcription. Reading: names are largely assembled from a stock of about a hundred two-sign units, many of them
number + item or fish + item, that also serve as short names on their own. Tally, counting parts: 352 held, 425 failed
(777 registered).

# Sixty-second set, registered before testing (24 September 2026): sign classes from context (loop 3, round 6)

Context vector of a sign = positive PMI of its left and right neighbours (predict_test13.contexts, line ends marked);
similarity = cosine. Signs with 20+ tokens in the sample (A + B pooled unless stated). Classes: fish (signs.FISH),
numerals (numerals.NUMS), head class (classes(A)). Class-cohesion nulls draw random sign sets of the same size from the
same frequency quintiles (10,000 draws); p < 0.05.

- **DC1** Fish signs are more similar to each other (mean pairwise cosine) than random matched sets.
- **DC2** Numerals are more similar to each other than random matched sets.
- **DC3** Head-class signs are more similar to each other than random matched sets.
- **DC4** Pairwise similarities in A and in B correlate (Spearman 0.5+, signs with 20+ tokens in each).
- **DC5** Pairwise similarities at Mohenjo-daro and at Harappa correlate (Spearman 0.4+, F lines, 20+ tokens at each).
- **DC6** Pairs of signs in one Fairservis category are more similar than pairs across categories (rank test).
- **DC7** The nearest neighbour of 50%+ of fish signs is a fish sign.
- **DC8** The nearest neighbour of 70%+ of numerals is a numeral.
- **DC9** The nearest neighbour of 50%+ of head-class signs is head-class.
- **DC10** A sign's nearest neighbour in A is its nearest neighbour in B for 30%+ of signs.

## Results of the sixty-second set (added after the test; `predict_test62.py`, `results/predict_test62.md`)

Five held, five failed. Context vectors (neighbour PMI, 115 signs with 20+ tokens) recover the known classes as
groups: fish signs (DC1: mean cosine 0.16, p = 0.0001), numerals (DC2: p = 0.008) and head-class signs (DC3: p =
0.0002) are each more alike than frequency-matched random sets, and signs that look alike (same Fairservis category)
share contexts more than signs that do not (DC6: 0.07 against 0.04, p = 0.0001; the fish series contributes). A fish's
nearest neighbour is another fish for 6 of 8 (DC7), but not a numeral's (DC8: 5 of 13) or a head's (DC9: 7 of 15).
Similarities are only moderately stable: A against B Spearman 0.44 (DC4, under 0.5) and Mohenjo-daro against Harappa
0.39 (DC5, under 0.4), both significant; nearest neighbours rarely agree across transcriptions (DC10: 7 of 63).
Reading: context supports broad classes (fish, numerals, heads, look-alike families) but not sign-level identities.
Tally, counting parts: 357 held, 430 failed (787 registered).

# Sixty-third set, registered before testing (24 September 2026): sign 700 and counted signs (loop 3, round 7)

F lines unless stated. 'Count token' = a line of numeral(s) + 700 only. Value = sum of the numerals directly before 700.
Counted signs and kinds as in the fifty-first set. 10,000-draw permutations; p < 0.05.

- **CN1** Count tokens are on moulded tablets (TAB:B) more often than on incised tablets (TAB:I) (two-sided Fisher).
- **CN2** The value of a count token depends on the tablet type (TAB:B against TAB:I; MI, permutation).
- **CN3** 50%+ of distinct count-token texts are found on 2+ objects.
- **CN4** 80%+ of 700 tokens directly follow a numeral.
- **CN5** 50%+ of 700 tokens not after a numeral stand inside name bodies.
- **CN6** Where 700 stands inside a name body, it is the last body sign in 50%+ of cases.
- **CN7** 80%+ of lines with 700 700 are Harappa tablets.
- **CN8** 60%+ of signs counted 5+ times (all objects, A + B) are always counted with one numeral kind.
- **CN9** 95%+ of values before 700 are 2, 3 or 4.
- **CN10** 60%+ of Mohenjo-daro 700 tokens stand inside name bodies.

## Results of the sixty-third set (added after the test; `predict_test63.py`, `results/predict_test63.md`)

Three held, seven failed. 700 is almost only a count sign: values before it are 2-4 in 98% (CN9: 94, 147, 123), the
common count texts (32 700, 33 700, 34 700) are each on around 100 objects (CN3), and the value differs slightly between
moulded and incised tablets (CN2: 0.03 bits, p = 0.003). Count tokens are commoner on incised than moulded tablets
(CN1: 30% against 20%, the reverse of the prediction). 700 is not a name sign anywhere: only 5 of 155 uncounted 700s are
inside a name body (CN5, CN6), 1 of 26 at Mohenjo-daro (CN10). The uncounted 700s are mostly Harappa tablets and potsherd
graffiti, and 66 of them stand first before a numeral ('700 33', '700 32', '700 34'): the count token written in the
other direction relative to the F line order, not an uncounted 700. Also: 700 700 is not a Harappa tablet form (CN7:
4 of 19), and most counted signs take more than one numeral kind (CN8: 15 of 74 take one). Tally, counting parts: 360
held, 437 failed (797 registered).

# Sixty-fourth set, registered before testing (24 September 2026): lines running the other way (loop 3, round 8)

F lines (intact, reversed order as in M4). 'Reversed count token' = 700 followed only by numerals; 'normal count token'
= numerals followed by 700. 'Reversed name line' = a line of 3+ signs whose first sign is 740 or 520 and whose last is
neither. A's 'direction' field joined by CISI number where needed. 10,000-draw permutations; p < 0.05.

- **DR1** Reversed count tokens are a larger share of count tokens on moulded tablets (TAB:B) than on incised (TAB:I).
- **DR2** Objects with a reversed count token have direction 'L/R' in A more often than objects with a normal one.
- **DR3** Reversed name lines are 2%+ of F lines containing 740 or 520.
- **DR4** Reversed name lines are off seals more often than normal name lines.
- **DR5** 30%+ of reversed name lines, read backwards, give an attested name body.
- **DR6** 90%+ of reversed count tokens are from Harappa.
- **DR7** Potsherd graffiti (POT types) carry reversed forms (count or name) at a higher line share than seals.
- **DR8** The value of a count token does not depend on its direction (MI permutation p >= 0.05).
- **DR9** In A, 'L/R' lines end in 740/520 less often than other lines.
- **DR10** At most 10% of A seals with a direction entry are 'L/R'.

## Results of the sixty-fourth set (added after the test; `predict_test64.py`, `results/predict_test64.md`)

Six held, four failed. 68 of 401 count tokens run '700 + numeral' against the usual order, 67 of them from Harappa
(DR6), and they are concentrated on moulded tablets (DR1: 24% of TAB:B count tokens against 9% of TAB:I), which fits a
mould or impression being recorded in mirror image rather than a scribal choice; potsherd graffiti also carry more
reversed forms than seals (DR7: 1.6% against 0.1%). The count value does not change with direction (DR8, p = 0.12). The
catalogue's direction field does not flag these objects (DR2: 9% against 8% 'L/R'), though 'L/R' lines in A end in
740/520 less often (DR9: 32% against 43%), and 'L/R' is rare on seals (DR10: 37 of 1,469). Names almost never run
backwards (DR3: 3 of 1,619 lines, none giving an attested body), so the reversal is a count-token and tablet
phenomenon. Caveat: whether the TAB:B reversal is in the objects or in how impressions were entered in ICIT cannot be
told from the data. Tally, counting parts: 366 held, 441 failed (807 registered).

# Sixty-fifth set, registered before testing (24 September 2026): moulded against incised tablets (loop 3, round 9)

F objects of type TAB:B (moulded) and TAB:I (incised); 'text' = the object's lines joined; motif from the ICIT record
(field 18). Formula-only signs as in the fifty-fourth set. 10,000-draw permutations; p < 0.05.

- **MT1** Distinct TAB:B texts recur on 2+ objects more often than distinct TAB:I texts.
- **MT2** TAB:B texts are shorter than TAB:I texts (rank test).
- **MT3** TAB:B lines are name lines less often than TAB:I lines, length-stratified.
- **MT4** 80%+ of TAB:B objects are from Harappa.
- **MT5** TAB:B objects have a motif recorded more often than TAB:I objects.
- **MT6** Among TAB:B objects with a motif, the text depends on the motif (MI, permutation).
- **MT7** Pairs of TAB:B objects with the same text share their motif more often than pairs across texts
  (permutation of motifs among objects).
- **MT8** TAB:B lines carry a numeral more often than TAB:I lines, length-stratified.
- **MT9** TAB:B texts contain a formula-only sign less often than TAB:I texts.
- **MT10** TAB:B lines repeat a line found on a seal more often than TAB:I lines.

## Results of the sixty-fifth set (added after the test; `predict_test65.py`, `results/predict_test65.md`)

Four held, six failed. Moulded tablets (TAB:B, 780) are a Harappa product (MT4: 86%) and carry a picture far more often
than incised tablets (MT5: 42% against 17%). Their text goes with the picture (MT6: MI 3.6 bits over 328 objects,
p = 0.0001) and objects with the same text share the picture (MT7: 531 same-text pairs with the same motif, p = 0.0001):
text and image were designed together on the mould. Otherwise moulded texts are not more repetitive (MT1: 33% against
36%), not shorter (MT2: 3.5 against 2.7 signs, the other way), not poorer in names (MT3), not richer in numerals (MT8),
not more stereotyped in signs (MT9), and they repeat seal lines less (MT10: 20% against 41%). Bug fix before recording:
the ICIT motif field holds the string 'None' where no motif is recorded; the first run counted it as a motif (MT5 100%
both, MT6/MT7 over all objects). The recorded run treats 'None' as no motif. Earlier sets that read this field may be
affected; flagged for an audit. Tally, counting parts: 370 held, 447 failed (817 registered).

Audit, 24 September 2026: the earlier sets that read the motif field (seventeenth, eighteenth, twenty-first,
twenty-fourth, twenty-seventh, twenty-ninth to thirty-first, thirty-fourth to thirty-sixth, thirty-ninth, fortieth)
already excluded 'None' (and '-') at every point where having a motif mattered; their other uses only ask for Bull1
(unicorn), which 'None' cannot match, and the fortieth passes no motif at all. The corpus-A motif field (`signs.load`)
never holds 'None'. All twelve scripts were rerun with their own seeds and 'None' mapped to no motif: output
identical to the unpatched run in every case, and identical to the recorded results except one permutation p-value
in the twenty-seventh set (L16, 0.0001 to 0.0002, unrelated to motifs; still holds). No verdict changes; the tally
stands.

# Sixty-sixth set, registered before testing (24 September 2026): replicating loop 3 on held-out data (loop 3, round 10)

Each test repeats a finding of the fifty-seventh to sixty-fifth sets on data not used to find it: B alone, other sites
(F outside Mohenjo-daro and Harappa), incised tablets (TAB:I), or A's own line order. Definitions as in the originals,
computed within the held-out data; thresholds scaled only where stated. p < 0.05.

- **RX1** (FS1) In B, different fish stand adjacent more often than within-body shuffles give (1,000 shuffles).
- **RX2** (FS5) In B, fish body tokens follow a numeral more often than other body tokens.
- **RX3** (FS6) In B, which fish is used depends on the preceding sign (MI).
- **RX4** (SG1) In B, units (pairs in 3+ distinct bodies) cover more body tokens than in within-body shuffles (1,000).
- **RX5** (SG10) In B, 30%+ of units are also whole 2-sign bodies.
- **RX6** (DC1) In B, fish signs (10+ tokens) are more alike in context than frequency-matched random sets.
- **RX7** (HD7) In B, 30%+ of headed name bodies are also attested unheaded.
- **RX8** (HD5) At other sites, seal lines are headed more often than tablet and other lines, length-stratified.
- **RX9** (MT7) On incised tablets with a motif, same-text pairs share the motif more than shuffled motifs give.
- **RX10** (DR1) In A's line order, the '700 + numeral' form is a larger share of count tokens on TAB:B than on TAB:I.

## Results of the sixty-sixth set (added after the test; `predict_test66.py`, `results/predict_test66.md`)

Seven held, three failed. The fish findings replicate in Mahadevan's transcription: different fish stack (RX1: 43
pairs, p = 0.001), fish are counted more (RX2: 12% against 8%), the preceding sign picks the fish (RX3, p = 0.0001), and
fish signs share contexts (RX6: 5 signs, p = 0.0001). Two-sign units cover more of B's bodies than shuffles give (RX4:
0.36, p = 0.001) and half stand alone as names (RX5: 18 of 38). Same text, same picture holds on incised tablets too
(RX9: 114 pairs, p = 0.0001), so it is not a moulding artefact. Not replicated: the optional heading in B (RX7: 22%
under 30%); headed seal lines at the smaller sites (RX8: -8.7 points, the other way); and reversed count tokens in A
(RX10: none of A's 30 count tokens is reversed). A's transcription appears to normalise direction, so the TAB:B
reversal of the sixty-fourth set may be an ICIT data-entry pattern rather than a feature of the objects. Tally,
counting parts: 377 held, 450 failed (827 registered).

# Sixty-seventh set, registered before testing (24 September 2026): seal text and seal picture

F seals (SEAL types) with a motif recorded (ICIT field 18; '' and 'None' = no motif). 'Motif' = the field up to its
first ':' (Bull1:I -> Bull1); same-text tests use the full field. Names via names_in. 10,000-draw permutations
(shuffling motifs among the objects tested); p < 0.05.

- **TP1** Seals with identical texts share the motif more often than when motifs are shuffled.
- **TP2** The name's last body sign depends on the motif (MI).
- **TP3** The name ending depends on the motif (MI).
- **TP4** Line-length stratum depends on the motif (MI).
- **TP5** Texts found on both a seal and a tablet carry the same motif on both more often than when tablet motifs are
  shuffled.
- **TP6** Seals with a motif other than the commonest one carry a numeral more often than seals with the commonest.
- **TP7** 20%+ of signs with 10+ seal tokens have half or more of those tokens on one motif other than the commonest.
- **TP8** TP2 holds within Mohenjo-daro alone.
- **TP9** TP2 holds within Harappa alone.
- **TP10** The first sign of the seal line depends on the motif (MI).

## Results of the sixty-seventh set (added after the test; `predict_test67.py`, `results/predict_test67.md`)

Four held, six failed; on seals the text-picture link is weak, unlike on tablets. 1,303 seals have a motif, 981 of them
the 'unicorn' (Bull1). Identical seal texts do not clearly share the picture (TP1: 24 pairs, p = 0.07), no frequent
sign belongs to a non-unicorn picture (TP7: 0 of 96), the ending is independent of the picture (TP3), and non-unicorn
seals do not count more (TP6). The name's head depends on the picture over all seals (TP2: p = 0.02) but not within
Mohenjo-daro (TP8: p = 0.15) or Harappa (TP9: p = 0.35), so TP2 is likely a site mix effect. Line length (TP4, p =
0.0001) and first sign (TP10, p = 0.016) depend weakly on the picture. Texts found on both a seal and a tablet carry
the same picture on both more often than chance (TP5: 46 matches over 74 tablets, p = 0.006), so a shared text brings
its picture with it across media. Reading: seal pictures are largely independent of the name; the tablet pairing
(sixty-fifth set) is a tablet practice that reuses seal text-picture combinations. Tally, counting parts: 381 held,
456 failed (837 registered).

# Sixty-eighth set, registered before testing (24 September 2026): tablets that copy seal texts

F lines. 'Copied line' = a tablet (TAB types) line of 2+ signs identical to a line on some seal; 'copied seal' = a seal
with a line that some tablet copies. Motifs as in the sixty-seventh set ('None' = no motif; Bull1 = unicorn).
10,000-draw permutations; p < 0.05.

- **CP1** Copied tablet lines are name lines more often than other tablet lines, length-stratified.
- **CP2** Copied seal lines recur on more seals than uncopied seal lines (rank test on seal counts).
- **CP3** 80%+ of copied tablet lines are from Harappa.
- **CP4** A copied tablet line comes from the same site as a seal bearing it more often than when tablet sites are
  shuffled.
- **CP5** Tablets with a copied line have a motif recorded more often than other tablets.
- **CP6** Copied seal lines are shorter than uncopied seal lines (rank test).
- **CP7** Among seals with a motif, copied seals carry the unicorn less often than uncopied seals.
- **CP8** Exact copies are at least twice as common as near copies (tablet lines one substitution away from a seal
  line and not identical to any).
- **CP9** Copied tablet lines carry a numeral less often than other tablet lines.
- **CP10** Copied seal name lines end in 740 more often than uncopied seal name lines.

## Results of the sixty-eighth set (added after the test; `predict_test68.py`, `results/predict_test68.md`)

Five held, four failed, one uninformative. 388 of 1,494 tablet lines match a seal line exactly, but 229 of them are the
count tokens 33 700 and 34 700, each of which also occurs on 1-3 seals; the rest are a few short Harappa names (176
740 400 x36, 3 156 x22, 415 220 520 x16, 840 32 740 x9). So 'copying' is mostly shared short formulas, not tablets
reproducing seals. With that in mind: copied lines are Harappa lines (CP3: 94%) from the same site as a seal bearing
them (CP4: 322 of 388, p = 0.0001), copied seal texts are short (CP6: 2.6 against 4.8 signs) and recur on more seals
(CP2), and copied tablet lines are names more often, length-stratified (CP1: +9.4 points). Tablets with a copied line
have a picture less often (CP5: 20% against 41%), carry numerals more (CP9: 73%, the count tokens), and copied seals
are not less often unicorns (CP7) nor more often 740 (CP10). CP8 (exact copies twice near copies: 388 against 433)
fails but is uninformative, since short lines are one substitution from many others. This set also qualifies the
sixty-seventh set's TP5: a shared text keeping its picture rests on few, short texts. Tally, counting parts: 386 held,
461 failed (847 registered).

# Sixty-ninth set, registered before testing (24 September 2026): twenty hypotheses on names as names

F objects (intact, lines reversed) for site tests; A + B pooled otherwise. Names via name_of / names_in; 'body' = the
name without ending; 'city' = Mohenjo-daro or Harappa; 'other sites' = neither. Units as in the sixty-first set (pairs
in 5+ distinct bodies). Site nulls shuffle sites among the name tokens tested. 10,000-draw permutations; p < 0.05.

Where names occur
- **AM1** Identical name bodies (2+ signs) occur at both cities less often than when sites are shuffled among name
  tokens (names are local).
- **AM2** Seals with identical full texts come from one site more often than shuffled.
- **AM3** When a long body (4+) ends in another attested body, that shorter body is attested at the long one's site
  more often than shuffled.
- **AM4** A name body embedded in a formula is attested as a name at the formula's site more often than shuffled.
- **AM5** Harappa name bodies are shorter than Mohenjo-daro name bodies (rank test, F).
- **AM6** 80%+ of heads (last body signs) of names at other sites are also heads at Mohenjo-daro or Harappa.
The two endings
- **AM7** Bodies attested with both 740 and 520 have both forms at one site more often than shuffled.
- **AM8** 520 names are off seals more often than 740 names (F).
- **AM9** Among bodies with both endings, the 520 form is off seals more often than the 740 form (paired sign test).
- **AM10** 520 names are a larger share of names at Harappa than at Mohenjo-daro (F).
Counted things inside names
- **AM11** 80%+ of numerals directly before a fish sign in name bodies have value 1-3.
- **AM12** The value before a fish depends on which fish (MI, permutation).
- **AM13** Names with a numeral inside the body are a larger share at Mohenjo-daro than at Harappa (F).
The stock of names
- **AM14** 70%+ of distinct name bodies are attested on one object only.
- **AM15** Bodies on 3+ objects are shorter than bodies on one (rank test).
- **AM16** 70%+ of one-off bodies of 3+ signs contain a unit.
- **AM17** The 20 commonest first body signs combine with more distinct heads than frequency-matched signs do at
  other positions (count of distinct following-heads, permutation over matched signs).
- **AM18** Unicorn seals (Bull1) are whole-name lines (the line is a name line) more often than other-motif seals.
- **AM19** A body's ending is predicted by its head better than by its first sign (MI, bodies of 2+).
- **AM20** Names at other sites are shorter than names at the two cities (rank test, F).

## Results of the sixty-ninth set (added after the test; `predict_test69.py`, `results/predict_test69.md`)

Thirteen held, seven failed. The name stock looks like personal names. 81% of distinct names are on one object only
(AM14), the repeated ones are short (AM15: 2.4 against 4.0 signs), and 72% of the one-off names of 3+ signs are built
with at least one stock unit (AM16). Names are local: fewer bodies occur at both cities than site-shuffles give (AM1: 32,
p = 0.0001), repeated seal texts stay at one site (AM2: 30 of 76, p = 0.0002), and names cited inside formulas are
attested as names at the formula's own site (AM4: 99 of 149, p = 0.013). But a long name and the shorter name it ends in
are not found together (AM3: p = 0.83), so the 'name ending in a name' pattern is not a local family or patronymic
link. The cities differ: Harappa names are shorter (AM5: 2.9 against 3.6 signs), use 520 a little more (AM10: 18%
against 14%, p = 0.043) and contain numerals less (AM13: 34% against 41%). Counted fish are small numbers, mostly 2
(AM11: 82% are 1-3; 121 of 200 are 2), and each fish variant has its own typical count (AM12, p = 0.0001). Unicorn
seals carry a text that is only a name more often than other seals (AM18: 52% against 41%). The head predicts the
ending better than the first sign (AM19: 0.45 against 0.22 bits), restating the head-final rule. Failures: the two
endings rarely alternate on one body (AM7: 10 bodies) and 520 is not an off-seal form (AM8, AM9, the other way); the
heads of the smaller sites are not all city heads (AM6: 79%); common openers are not especially productive (AM17);
small-site names are not shorter (AM20). Tally, counting parts: 399 held, 468 failed (867 registered).

# Seventieth set, registered before testing (24 September 2026): twenty hypotheses on the local name stocks

F name tokens (names_in; site, object type, ICIT record) unless stated; 'city' = Mohenjo-daro or Harappa. 'Name' =
(body, ending); 'one-off' = on one object. Units as in the sixty-first set; motif as in the sixty-seventh ('None' = no
motif). Harappa period via rtools.level. Site/label nulls shuffle labels among the tokens tested. 10,000-draw
permutations (1,000 where stated); p < 0.05.

Time and place
- **PN1** At Harappa, a name on 2+ dated objects keeps to one period more often than when periods are shuffled.
- **PN2** Distinct opening pairs (first two body signs) are shared by the two cities more often than distinct closing
  pairs (last two).
- **PN3** Within one site, seals with identical texts share the motif more often than when motifs are shuffled within
  the site.
- **PN4** The ten names on the most objects have 60%+ of their tokens at Harappa.
- **PN5** Unit sharing is local: one-off names at one city share units with other one-offs of the same city more than
  when city labels are shuffled among one-off names (1,000 shuffles).
Length and content
- **PN6** Names with a numeral in the body are longer (rank test).
- **PN7** Names with a fish sign are longer (rank test).
- **PN8** Names with a numeral + fish pair are a larger share at Mohenjo-daro than at Harappa.
- **PN9** At Harappa, 520 names are shorter than 740 names (rank test).
- **PN10** Bodies with a doubled sign are a larger share at Mohenjo-daro than at Harappa.
- **PN11** 520 names contain a fish more often than 740 names.
Object and name
- **PN12** Names off the seals are shorter than names on seals (rank test).
- **PN13** Distinct seal names are one-off more often than distinct names off seals.
- **PN14** Tablet names are also attested on a seal more often than potsherd names are.
- **PN15** At Harappa, tablet names are shorter than seal names (rank test).
- **PN16** Names with the heading unit are one-off more often than unheaded names (A + B lines).
Inside the one-off names
- **PN17** In 70%+ of one-off names of 2+ signs, the head also heads 5+ distinct names.
- **PN18** In one-off names of 3+, the first sign is rare (5 or fewer tokens in F) more often than the head is.
- **PN19** Harappa heads are less varied than Mohenjo-daro heads (entropy, label permutation).
- **PN20** A larger share of distinct names repeats (2+ objects) at Harappa than at Mohenjo-daro.

## Results of the seventieth set (added after the test; `predict_test70.py`, `results/predict_test70.md`)

Twelve held, eight failed. The strongest new result is PN11: 74% of 520 names contain a fish sign against 37% of 740
names (171 of 230 against 452 of 1,228), so the 520 ending goes with fish-series names. Name stocks are local down to
their parts: one-off names share stock units with one-offs of their own city more than city-shuffles give (PN5: p =
0.003), and within one site identical seal texts share their picture (PN3: 16 pairs, p = 0.009; across sites the
sixty-seventh set's TP1 was p = 0.07). Seal names are the individual ones: 86% of names on seals are one-off against
54% off seals (PN13), seal names are longer than names elsewhere (PN12: 3.7 against 2.8), also at Harappa alone (PN15),
and Harappa repeats its names more (PN20: 35% against 20%). Inside one-off names, the head is a common head (PN17:
82% head 5+ names) and the rare part stands first (PN18: rare first sign 14% against rare head 6%): an individual
element in front of a common head. Counted fish are a little more Mohenjo-daran (PN8: 13% against 10%, p = 0.049).
PN6 and PN7 (names with a numeral or fish are longer) hold but follow largely from the extra sign. Failures: repeated
Harappa names do not keep to one period (PN1: 20 of 44), opening pairs travel between cities less than closing pairs
(PN2: 10% against 19%, the reverse), the commonest names are not mostly Harappan (PN4: 57%), 520 names are not shorter
at Harappa (PN9), doubles are not Mohenjo-daran (PN10), tablet names are not more often seal names than pot names are
(PN14), headed names are not more often unique (PN16, p = 0.057), and Harappa heads are not less varied (PN19).
Tally, counting parts: 411 held, 476 failed (887 registered).

# Seventy-first set, registered before testing (24 September 2026): why 520 goes with fish (twenty hypotheses)

Names = name_of over A + B lines (tokens) unless stated; head = last body sign; fish = signs.FISH; roof fish = 235,
236. 'Fish name' = a body with a fish sign. F for site tests. 10,000-draw permutations; p < 0.05.

Is the fish itself the trigger?
- **EF1** Among names whose head is not a fish, those with a fish elsewhere in the body take 520 more often.
- **EF2** EF1 holds stratified by head (heads of 5+ names; stratified permutation).
- **EF3** EF1 holds stratified by body length.
- **EF4** Among non-fish-headed fish names, the fish stands nearer the end in 520 names than in 740 names (rank test
  on signs between the last fish and the end).
- **EF5** Among names with exactly one fish, the 520 share depends on which fish (MI).
- **EF6** Roof-fish names take 520 more often than other fish names.
- **EF7** Names with 2+ fish take 520 more often than names with exactly one.
- **EF8** Fish names where a numeral stands right before the fish take 520 more often than other fish names.
Does the ending switch with the fish?
- **EF9** Removing one fish from a 520 body gives an attested 740 name more often than an attested 520 name (sign test
  over distinct 520 bodies).
- **EF10** The body before 520 without its fish signs is shorter than the body before 740 without its fish signs.
- **EF11** 60%+ of non-fish heads taking 520 in half or more of their 5+ names stand next to a fish in some body.
Replication
- **EF12** In B alone, fish names are a larger share of 520 names than of 740 names.
- **EF13** At Harappa alone (F), the same.
- **EF14** At Mohenjo-daro alone (F), the same.
- **EF15** At other sites (F), the same.
- **EF16** EF1 holds in B alone.
What else goes with 520
- **EF17** 520 is followed by 400 less often than 740 is (lines).
- **EF18** 520 names open with the heading unit less often than 740 names.
- **EF19** Seal 520 names are on unicorn seals less often than seal 740 names (F, motif recorded).
- **EF20** Distinct 520 fish names are one-off less often than distinct 740 fish names (A + B counts).

## Results of the seventy-first set (added after the test; `predict_test71.py`, `results/predict_test71.md`)

Twelve held, eight failed. The fish-520 link replicates everywhere it can be tested with numbers: B alone (EF12: 73%
against 30%), Harappa (EF13: 82% against 34%), Mohenjo-daro (EF14: 76% against 38%); at the smaller sites it does not
(EF15: 45% against 40%, 33 names). But it runs through the head: 151 of the 273 520 names are fish-headed, and the fish
effect does not survive stratifying by head (EF2: +0.7 points, p = 0.16), although a fish elsewhere in the body raises
520 slightly overall (EF1: 9.6% against 6.4%; EF3 by length: +3.6 points; EF16 in B: 9% against 5%). So 520 is chiefly
the ending of fish-headed names, and the fish heads divide: 220 (62 of 99 take 520), 240 (44 of 65), 233 (28 of 32) lean
520, while 222 takes 740 in all 21 (post-test breakdown; EF5: fish variant and ending, p = 0.009). The sign before the
fish matters too, descriptively: stroke 2 + fish ends in 520 in 31 of 34 names and 415 + fish in 26 of 33, while stroke 3
+ fish ends in 740 in 9 of 11 and 235 + fish in 22 of 26. These counts include repeats (501 405 2 240 520 x29) and were
not registered; they are leads for the next set. Also: counted fish raise 520 (EF8: 34% against 24%); 520 bodies are
shorter once fish are removed (EF10: 2.2 against 2.7); 520 is followed by 400 less often (EF17: 35% against 50%) and is
rarer on unicorn seals (EF19: 73% against 80%). Failed: nearer fish (EF4), roof fish (EF6, the other way: 14% against
30%), more fish (EF7, p = 0.08), fish removal switching to 740 (EF9: 4 against 9), heading unit (EF18) and repeat rate
(EF20). EF11 held on only two heads (33, 70) and is not evidence. Tally, counting parts: 423 held, 484 failed (907
registered).

# Seventy-second set, registered before testing (24 September 2026): does the ending agree with the number? (twenty hypotheses)

Lead from the seventy-first set (post-test, unregistered): stroke 2 + fish -> 520, stroke 3 + fish -> 740. Here all
counts are over DISTINCT names (body, ending) from A + B unless stated; F tests use distinct names per site. 'Counted
head' = a body whose last sign is not a numeral and is directly preceded by a numeral run; value = the run's sum.
Fish = signs.FISH. 10,000-draw permutations; p < 0.05.

The fish case
- **NA1** Counted fish heads with value 2 take 520 more often than those with value 3 or more.
- **NA2** Counted fish heads with value 2 take 520 more often than those with value 1.
- **NA3** Counted fish heads with value 2 take 520 more often than uncounted fish heads.
- **NA4** NA1 holds in B alone.
- **NA5** NA1 holds at Harappa (F).
- **NA6** NA1 holds at Mohenjo-daro (F).
Beyond fish
- **NA7** Over all counted heads, value 2 takes 520 more often than other values.
- **NA8** NA7 holds stratified by head (heads counted with 2 and with another value).
- **NA9** The ending depends on the value before the head (MI over counted heads; values 1, 2, 3, 4+).
- **NA10** Control: a numeral inside the body but not before the head does not predict the ending (value 2 against
  other, p >= 0.05).
- **NA11** For heads seen both counted with 2 and uncounted, the 2 form takes 520 more often (sign test over heads).
- **NA12** For heads seen both counted with 3 and uncounted, the 3 form takes 740 more often (sign test over heads).
- **NA13** The numeral kind before the head (short, long, tiered) predicts the ending (MI).
Other neighbours
- **NA14** Fish heads after 415 take 520 more often than fish heads after other signs.
- **NA15** Fish heads after 235 take 740 more often than fish heads after other signs.
- **NA16** For fish heads, the sign before the head adds information about the ending beyond the head (conditional MI,
  shuffling the preceding sign within head groups).
- **NA17** The same for non-fish heads.
Checks
- **NA18** 90%+ of numerals directly before a fish head are of the short kind.
- **NA19** 2 + fish + 520 occurs in 3+ distinct names at each city (F).
- **NA20** In formulas, fish after stroke 2 are line-final more often than fish after stroke 3 (tokens).

## Results of the seventy-second set (added after the test; `predict_test72.py`, `results/predict_test72.md`)

Two held, eighteen failed: the number-agreement lead does not survive counting distinct names. Only 29 distinct names
have a counted fish head (values 2: 9, 3: 6, 6: 4, others 1-2 each). Value 2 takes 520 in 6 of 9 against 7 of 17 for
3+ (NA1, p = 0.21), no better than value 1 (NA2) or uncounted fish heads (NA3: 67% against 63%); nothing replicates in
B (NA4: no value-2 case), at Harappa (NA5) or at Mohenjo-daro (NA6), or in both cities (NA19: 4 and 2 bodies). Over
all heads the value does not set the ending (NA7: 16% against 11%; NA8 within heads +10 points, p = 0.10; NA9: MI p =
0.74; NA11, NA12: 3-1 and 2-0 heads) and neither does the notation (NA13). The seventy-first set's '31 of 34' came from
repeated seals (501 405 2 240 520 x29 and a few others). Withdrawn. The 415/235 + fish leads also fail on distinct names
(NA14: 10 of 12, p = 0.09; NA15: 6 of 10, p = 0.12), and before a fish head the numeral is short-kind only half the
time (NA18: 15 of 29). What held: a numeral elsewhere in the body does not predict the ending (NA10, control), and for
non-fish heads the sign before the head adds a little information about the ending beyond the head (NA17: 0.034 bits,
p = 0.001); for fish heads it does not (NA16). Lesson recorded: token counts over repeated seals can manufacture
patterns; distinct-name counts are the check. Tally, counting parts: 425 held, 502 failed (927 registered).

# Seventy-third set, registered before testing (24 September 2026): the findings recounted on distinct texts (twenty hypotheses)

After the seventy-second set showed that repeated seals can manufacture a pattern, twenty earlier findings are
re-tested with every line, name or text counted once. 'Distinct lines' = the set of line tuples in A + B; 'distinct
names' = the set of (body, ending); F tests use distinct (site, line) or distinct object texts as stated. Tests and
thresholds as in the original sets. 10,000-draw permutations (1,000 where the original used 1,000); p < 0.05.

Names
- **DN1** (core) The head carries information about the ending (MI over distinct names).
- **DN2** (core) 80%+ of heads with 5+ distinct names take one ending in 80%+ of them.
- **DN3** (seventy-first) Among fish-headed distinct names, the ending depends on which fish (MI).
- **DN4** (fifty-eighth FS5) Fish body tokens follow a numeral more often than other body tokens (distinct names).
- **DN5** (fifty-eighth FS6) Which fish is written depends on the preceding sign (distinct names).
- **DN6** (forty-first DB6) Distinct bodies of 3+ avoid non-adjacent repeats against within-body shuffles.
- **DN7** (seventy-first EF17) On distinct lines, 520 is followed by 400 less often than 740.
Numbers
- **DN8** (core) On distinct lines, numerals of value 5-8 are tiered more often than numerals of value 1-4.
- **DN9** (core) On distinct lines, the numeral kind depends on the next sign (MI).
- **DN10** (core) On distinct lines, long numerals open the line more often than short ones.
- **DN11** (forty-seventh FI4) On distinct formulas, (value, next sign) pairs are fewer than with shuffled numerals.
- **DN12** (forty-seventh FI5) 20%+ of distinct numeral formulas share their residue with one of another value.
Genres
- **DN13** (forty-fifth EM7) On distinct lines with a numeral, it is first more often in formulas than in name lines.
- **DN14** (fifty-third EN1, reversed) Distinct name lines repeat their adjacent pairs more than distinct formulas (1,000).
- **DN15** (forty-first DB1) Distinct lines hold more doubles than within-line shuffles (1,000).
Seals and tablets (F, distinct (site, line))
- **DN16** (fiftieth SC1) Seal numeral-formula values are larger than tablet ones (rank test).
- **DN17** (fiftieth SC2) Seal numerals are tiered more often than tablet numerals.
- **DN18** (forty-seventh FI7) Harappa formulas open with a numeral more often than Mohenjo-daro ones, length-stratified.
- **DN19** (sixty-ninth AM18) Over distinct seal texts with a motif, unicorn texts are pure names more often.
- **DN20** (seventy-first EF19) Over distinct seal name texts with a motif, 520 names are unicorn less often.

## Results of the seventy-third set (added after the test; `predict_test73.py`, `results/predict_test73.md`)

Sixteen held, four failed. Counting each line once (2,722 distinct of 4,116) and each name once (1,089 of 1,895), the
core stands: the head sets the ending (DN1: 0.45 bits) and 46 of 52 heads fix theirs (DN2); the tiered form is for 5-8
(DN8: 64% against 1%); the next sign sets the numeral kind (DN9); long numerals open lines (DN10: 28% against 11%);
(value, sign) pairs are idioms (DN11). The newer findings also survive: which fish head decides the ending (DN3, p =
0.002), fish are counted more (DN4: 23% against 12%) and chosen by their neighbour (DN5), names avoid distant repeats
(DN6) and doubling is deliberate (DN15); formulas are number-first (DN13: 31% against 22%) and names the repetitive
genre (DN14: 0.78 against 0.59); seal numerals are tiered more (DN17: 11% against 3%); Harappa formulas open with a
number more (DN18: +5.9 points, down from +26.5, so most of that effect was repeated tablets); unicorn seals carry
pure names (DN19: 53% against 40%). Weakened to non-significance: 520 not followed by 400 (DN7: 29% against 34%),
formulas recurring with only the number changed (DN12: 16%, under 20%, was 39%, carried by the count tokens), seal
values larger than tablet values (DN16: p = 0.056), and 520 less often unicorn (DN20: p = 0.07). These four earlier
findings (EF17, FI5, SC1, EF19) should be treated as repeat-inflated. Tally, counting parts: 441 held, 506 failed (947
registered).

# Seventy-fourth set, registered before testing (24 September 2026): heads as roles, openers as persons (twenty hypotheses)

Idea from the sixty-ninth and seventieth sets: a name = an individual first element + a common head, like 'X the
potter'. All counts over DISTINCT names (A + B) or distinct (site, name) in F. Head = last body sign; opener = first
body sign of bodies of 2+. Fairservis categories from cat_of. 10,000-draw permutations; p < 0.05.

Heads are shared, openers are particular
- **HR1** Head types seen at either city are seen at both more often than opener types (F).
- **HR2** Per sign with 5+ distinct names in the role, distinct partners per name is higher for heads (openers per
  head) than for openers (heads per opener) (rank test).
- **HR3** The ten commonest heads cover a larger share of distinct names than the ten commonest openers.
- **HR4** In B alone, HR3 holds.
- **HR5** 80%+ of heads of tablet names are also heads of seal names; openers of tablet names are seal openers less
  often than that (F; Fisher over types).
- **HR6** In one-off names, head types are shared by the two cities more often than opener types (F).
- **HR7** 20%+ of openers of one-off names occur in that one name only.
Heads and openers combine freely
- **HR8** In 2-sign bodies, opener and head are independent (MI permutation p >= 0.05).
- **HR9** In bodies of 3+, first and last signs are independent (p >= 0.05).
- **HR10** Given the head, the opener adds no information about the ending (conditional MI, p >= 0.05).
- **HR11** Long bodies (4+) share their head with a 2-sign body more often than they share their opener with one
  (paired sign test).
What heads are
- **HR12** Head types are counted in formulas (directly after a numeral) more often than opener types (types used
  mainly in one role; Fisher).
- **HR13** Role (head against opener) depends on Fairservis category (MI over types).
- **HR14** The ending depends on the head's category (MI over names with a categorised head).
- **HR15** 40%+ of distinct 520 names have a fish head.
- **HR16** At most 10% of non-fish heads with 5+ names take 520 in the majority.
- **HR17** Fish are openers more often than heads (share of fish among opener tokens against head tokens).
- **HR18** Headed names (heading unit) have a different head distribution from unheaded names (MI).
- **HR19** Distinct 740 names are longer than distinct 520 names (rank test).
- **HR20** The ten commonest heads are all at both cities (F).

## Results of the seventy-fourth set (added after the test; `predict_test74.py`, `results/predict_test74.md`)

Twelve held, eight failed; all counts over distinct names. The 'common head + particular opener' model gets real
support. Heads are the shared part: head types occur at both cities more often than opener types (HR1: 49% against
34%; HR6 in one-off names: 42% against 30%), the ten commonest heads (760, 100, 33, 220, 798, 176, 32, 390, 690, 900)
are all at both cities (HR20), and they cover more names than the ten commonest openers (HR3: 423 against 346 of 982;
HR4 in B: 131 against 104 of 266). Long names keep a known head far more often than a known opener (HR11: 161 against
39). The ending belongs to the head: given the head, the opener adds nothing (HR10: p = 0.87), and the ending depends on
the head's shape category (HR14, p = 0.0001). 520 is the fish-head ending: 41% of distinct 520 names are fish-headed
(HR15) and only 2 of 46 common non-fish heads take 520 in the majority (HR16). Fish are more often openers than heads
(HR17: 16% against 10%). In 2-sign names the opener and head combine without detectable preference (HR8: p = 0.88), but
in longer names first and last are linked (HR9: p = 0.002), and HR8/HR10 are null results with limited power. Not
supported: heads taking more varied partners (HR2, p = 0.09), openers being unique to one name (HR7: 11%), heads being
counted in formulas more than openers (HR12), role following category (HR13, p = 0.08), tablet heads being seal heads
more than openers (HR5: 76% against 74%), titled names having their own heads (HR18), 740 names being longer (HR19).
Tally, counting parts: 453 held, 514 failed (967 registered).

# Seventy-fifth set, registered before testing (24 September 2026): how the name is put together (twenty hypotheses)

Distinct names (A + B) and distinct (site, type, name) in F, as in the seventy-fourth set. In a body of 3 signs:
opener, middle, head. Motif as in the sixty-seventh set. 10,000-draw permutations; p < 0.05.

Constituents
- **QS1** In 3-sign bodies the middle sign tells more about the head than about the opener (MI middle-head higher,
  and significant).
- **QS2** In 3-sign bodies, (middle, head) is an attested 2-sign body more often than (opener, middle) (sign test).
- **QS3** In 4-sign bodies, the last two signs are an attested 2-sign body more often than the first two (sign test).
- **QS4** The middle sign of 3-sign bodies is a numeral or fish in 40%+.
- **QS5** In bodies of 3+, numerals stand directly before the head more often than first (sign test on counts).
- **QS6** B alone: QS1 holds.
- **QS7** B alone: QS3 holds.
Role or place
- **QS8** Within Mohenjo-daro seals, the head depends on the motif (MI, distinct names).
- **QS9** Within Mohenjo-daro seals, the opener depends on the motif.
- **QS10** At Harappa, the head depends on the object class (seal against tablet; MI).
- **QS11** Opener types at the smaller sites are also city openers less often than their head types are city heads.
- **QS12** At Harappa, head types dated to both periods are a larger share than opener types.
- **QS13** Pairs of names sharing an opener but not a head are from the same site more often than when sites are
  shuffled (F).
- **QS14** Pairs sharing a head but not an opener are not from the same site more than shuffled (p >= 0.05).
What heads are
- **QS15** Heads that are also counted in formulas have more distinct names than heads never counted (rank test).
- **QS16** 50%+ of the ten commonest heads are also attested as 1-sign names.
- **QS17** 80%+ of signs attested as 1-sign names (with 3+ longer names) stand last in most of their longer names.
- **QS18** Receipt names (ending + 400) end in a top-10 head more often than other names (distinct lines).
- **QS19** Names cited in formulas end in a top-10 head more often than names in general.
- **QS20** In 3-sign bodies, fish stand in the middle more often than first or last.

## Results of the seventy-fifth set (added after the test; `predict_test75.py`, `results/predict_test75.md`)

Nine held, eleven failed. The constituent structure is clear and replicates in B: names are [opener [middle head]].
In 3-sign bodies the middle sign is tied to the head more than to the opener (QS1: 4.18 against 3.63 bits; QS6 in B:
3.98, p = 0.0001, against 3.33, p = 0.48; heads have fewer types, so the comparison is conservative); (middle, head)
is an attested 2-sign name far more often than (opener, middle) (QS2: 74 against 31); in 4-sign bodies the last two
signs form a name far more often than the first two (QS3: 55 against 19; QS7 in B: 14 against 1). Numerals stand
directly before the head more than first (QS5: 126 against 91): the count belongs to the head. The common heads are
also the counted things and stand alone as names: heads counted in formulas head four times as many names (QS15:
10.0 against 2.5), all ten commonest heads are also 1-sign names (QS16), and names cited inside formulas end in a
top-10 head more often (QS19: 50% against 43%). What failed: fish sit first more than in the middle (QS20: 63, 43, 17)
and the middle is not mainly numerals or fish (QS4: 36%); motifs do not track head or opener at Mohenjo-daro (QS8,
QS9); Harappa seals and tablets name the same heads (QS10); small-site openers are city openers as often as heads are
(QS11); heads do not outlast openers across Harappa periods (QS12, p = 0.13); pairs sharing an opener are only
borderline local (QS13, p = 0.058) and pairs sharing a head are local too (QS14 fails, p = 0.021), so opener and head
cannot be told apart as person against place; receipts do not favour common heads (QS18); and most 1-sign names are
not mainly heads in longer names (QS17: 25 of 69). Tally, counting parts: 462 held, 525 failed (987 registered).

# Seventy-sixth set, registered before testing (24 September 2026): the name as a noun phrase (twenty hypotheses)

From the seventy-fifth set: name = [opener [middle head]], the numeral stands before the head, and common heads are
the counted things of the formulas. Distinct names and distinct lines (A + B) unless stated. 'Modifier' = a non-head,
non-numeral body sign; 'counted head' = head directly after a numeral run (value, kind as before); 'formula-counted
sign' = sign directly after a numeral in a distinct formula. Categories from cat_of. 10,000-draw permutations; p < 0.05.

Heads select
- **NP1** The modifier directly before the head depends on the head's category (MI over distinct names).
- **NP2** The value before a counted head depends on the head (MI).
- **NP3** For signs counted in both names and formulas, the commonest numeral kind is the same in both for 70%+.
- **NP4** For signs counted in both, the commonest value is the same in both for 50%+.
- **NP5** Numeral values before heads in names are smaller than before signs in formulas (rank test).
- **NP6** Fish heads are counted more often than non-fish heads.
- **NP7** Counted heads are also 1-sign names more often than uncounted heads (types).
Modifiers
- **NP8** Adjacent modifier pairs keep one order: under 20% of such pairs are attested reversed.
- **NP9** Modifiers stand before the numeral rather than between numeral and head: 'mod N head' is commoner than
  'N mod head' (counts over bodies).
- **NP10** Slot (opener against middle in 3-sign bodies) depends on the sign (MI).
- **NP11** Under 5% of bodies hold two separate numeral runs.
- **NP12** Counted heads have more distinct modifiers per name than uncounted heads (rank test, heads with 3+ names).
Formulas share the grammar
- **NP13** In formulas, a numeral is followed by a sign that heads names more often than a random formula token is a
  name head (tokens).
- **NP14** Formula residues of two signs end in a name head more often than they begin with one.
- **NP15** Numeral-first names have a formula-counted head more often than other names.
Replication
- **NP16** B: NP2 holds.
- **NP17** B: NP13 holds.
- **NP18** Harappa (F distinct names): NP2 holds.
- **NP19** Mohenjo-daro (F distinct names): NP2 holds.
- **NP20** B: NP9 holds.

## Results of the seventy-sixth set (added after the test; `predict_test76.py`, `results/predict_test76.md`)

Eight held, twelve failed. Inside the name, the head governs: the modifier before the head depends on the head's shape
category (NP1, p = 0.0001), and the number before the head depends on the head (NP2: 1.30 bits, p = 0.0001), which
replicates in B (NP16, p = 0.02), at Harappa (NP18, p = 0.003) and at Mohenjo-daro (NP19, p = 0.0002). Fish heads are
counted more than other heads (NP6: 26% against 15%). Modifiers keep one order (NP8: 10% of pairs reversed) and opener
and middle slots use different signs (NP10, p = 0.0001). But the bridge from names to formulas does not hold: signs
counted in both take different numeral kinds (NP3: 17 of 37 agree) and different typical values (NP4: 13 of 37); names
do not count smaller (NP5); formulas do not count name heads more than their other tokens are name heads (NP13: 67%
against 65%; NP17 in B: 65% against 61%); two-sign formula residues are not head-final (NP14: 86 against 81); and
number-first names do not favour formula-counted heads (NP15). So the seventy-fifth set's 'common heads are the counted
things of the formulas' (QS15) is mostly frequency: two thirds of all formula tokens are name-head signs. The number
comes before a modifier more often than after it (NP9: 'N mod head' 124 against 'mod N head' 100; NP20 in B: 28
against 14), suggesting [N [mod head]] rather than [mod [N head]]. 7% of names hold two numeral runs (NP11), and
counted heads do not take more modifiers (NP12); counted heads standing alone is borderline (NP7, p = 0.057). Tally,
counting parts: 470 held, 537 failed (1007 registered).

# Seventy-seventh set, registered before testing (24 September 2026): numbers that are part of names, and two systems (twenty hypotheses)

Distinct names and distinct lines (A + B) unless stated. Counted head, value and kind as in the seventy-second set;
formulas = non-name lines. 'N mod head' = body ending numeral, non-numeral, head; 'mod N head' = non-numeral, numeral,
head. 10,000-draw permutations (1,000 where stated); p < 0.05.

Fixed numbers in names
- **LX1** For heads counted in 3+ distinct names, the commonest value's mean share is 0.7+.
- **LX2** For signs counted 3+ times in both, the commonest-value share is higher in names than in formulas (sign test).
- **LX3** (value, head) pairs recur across distinct bodies more often than when values are shuffled among counted names.
- **LX4** The two commonest values cover 70%+ of name numeral runs.
- **LX5** Name values and formula values differ in distribution (MI with a genre label).
- **LX6** In 'N mod head' names, the value tells more about the head than about the modifier (MI higher and
  significant).
- **LX7** For 30%+ of (value, head) pairs in counted names, 'N head' is also an attested 2-sign body.
- **LX8** Name numeral runs are value 2 or 3 more often than formula numeral runs.
Two systems sharing signs
- **LX9** 20%+ of sign types with 3+ name tokens never occur in formulas.
- **LX10** Name and formula lines share adjacent-pair types less than when genre labels are shuffled among lines (1,000).
- **LX11** They share (numeral, sign) pair types less than when labels are shuffled (1,000).
- **LX12** For signs with 10+ tokens in each genre, left-neighbour distributions differ between genres more than when
  labels are shuffled (mean Jensen-Shannon divergence, 1,000).
- **LX13** The sign after a numeral ends the line more often in formulas than in name lines.
The number before the phrase
- **LX14** In 'N mod head' names, (mod, head) is an attested 2-sign body in 30%+.
- **LX15** In 'mod N head' names, (N, head) is an attested 2-sign body in 30%+.
- **LX16** The modifier in 'N mod head' is a fish more often than in 'mod N head'.
- **LX17** 'N mod head' names take 520 more often than 'mod N head' names.
- **LX18** Harappa and Mohenjo-daro differ in the share of 'N mod head' among these two shapes (two-sided, F).
Replication
- **LX19** B: LX1 holds.
- **LX20** B: LX10 holds (1,000).

## Results of the seventy-seventh set (added after the test; `predict_test77.py`, `results/predict_test77.md`)

Nine held, eleven failed. Numbers in names are not fixed parts of the name: a head's commonest value covers only 60% of
its counted names (LX1; B: 49%, LX19), names are not more fixed than formulas (LX2: 6 against 4), (value, head) pairs
do not recur across bodies more than chance (LX3), and name values are spread (LX4: 2 x49, 3 x36, 1 x26, 7 x20; LX8
values 2-3 less common in names than in formulas: 49% against 58%). The number goes with the modifier as much as the
head (LX6: 0.91 against 0.88 bits). But the phrase shape is supported: in 'N mod head' the (mod, head) part is itself an
attested name in 49% (LX14), more than (N, head) is in 'mod N head' (LX15: 28%), and the modifier inside the number is
a fish more often (LX16: 38% against 23%), so 'N [fish head]' is a common build. Names and formulas are two systems
sharing a sign set: they share fewer adjacent-pair types (LX10: 447; B, LX20: 146) and (numeral, sign) types (LX11: 96)
than label-shuffled lines give, the same sign keeps different company in each (LX12: mean JSD 0.40 over 66 signs), the
counted item closes formulas but not names (LX13: 47% against 14%), and value distributions differ (LX5, p = 0.002).
Yet only 10% of common name signs are absent from formulas (LX9). Not supported: 520 in 'N mod head' (LX17) and a city
difference in the shape (LX18: 59% against 54%). Bug fix before recording: the first LX18 run deduplicated on (site,
shape) instead of (site, name), leaving 4 items; the recorded run counts distinct (site, name). Tally, counting parts:
479 held, 548 failed (1027 registered).

# Seventy-eighth set, registered before testing (24 September 2026): the grammar of the formulas (twenty hypotheses)

Distinct formula lines (non-name lines, A + B) unless stated. In a formula with a numeral: 'pre' = the signs before the
first numeral run (may be empty), 'item' = the sign right after a numeral run, 'value' = that run's sum. Name bodies
and heads from distinct names. F tests use distinct (site, type, line). 10,000-draw permutations; p < 0.05.

The part before the number
- **FG1** In 20%+ of formulas with a non-empty pre, the pre is an attested name body.
- **FG2** The pre's last sign is a name head more often than the item is (sign test over formulas with both).
- **FG3** The item depends on the pre's last sign (MI).
- **FG4** 50%+ of pres found in 2+ formulas occur with 2+ different items.
- **FG5** Pres' last signs are name heads for 60%+ of formulas with a pre.
- **FG6** Seal formulas have a non-empty pre more often than tablet formulas (F).
- **FG7** Seal pres are attested name bodies more often than tablet pres (F).
The counted item
- **FG8** The value depends on the item (MI).
- **FG9** Items are formula-only signs more often than pre signs are (tokens).
- **FG10** Where a sign follows the item, it is 400, 90, 151 or a numeral in 30%+.
- **FG11** Three items account for 50%+ of items directly before a line-final 400.
- **FG12** 50%+ of items counted in 3+ formulas take 3+ values.
- **FG13** (value, item) types at either city are at both in 30%+ (F).
Lists
- **FG14** In formulas with two numeral runs, the two items differ in 90%+.
- **FG15** In such formulas, the first value is larger than the second more often than smaller (sign test).
- **FG16** Item pairs (first, second) recur in 2+ formulas more often than when second items are shuffled.
Replication
- **FG17** B: FG2 holds.
- **FG18** B: FG3 holds.
- **FG19** Harappa (F): FG8 holds.
- **FG20** Mohenjo-daro (F): FG8 holds.

## Results of the seventy-eighth set (added after the test; `predict_test78.py`, `results/predict_test78.md`)

Twelve held, eight failed; distinct lines throughout. Of 725 numeral formulas, 499 have signs before the first number
(a 'pre'). The pre works as a header: it selects the counted item (FG3: 3.35 bits, p = 0.0001; FG18 in B, p = 0.019),
a repeated pre occurs with several items (FG4: 40 of 50), 23% of pres are attested name bodies (FG1), and seal formulas
have a pre more often than tablet formulas (FG6: 72% against 62%). The item sets the count (FG8, p = 0.0001; FG19
Harappa, p = 0.02; FG20 Mohenjo-daro, p = 0.0001), items are formula-only signs more often than pre signs (FG9: 13%
against 8%), and most items take several values (FG12: 34 of 63). Two-count formulas list different items (FG14: 57 of
58). So the formula reads as [header] [N item] ([N item]): a header, often a name, followed by counted items. Not
supported: pre-final signs are not name heads more than items are (FG2: 76 against 86; FG17 in B: 25 against 27), and
FG5 (68% of pres end in a name head) is close to the base rate (two thirds of formula tokens are head signs); seal
headers are not names more than tablet headers (FG7); items are not closed off by 400/90/151 (FG10: 18%; what follows is
615, 390, 527, 405); items before a final 400 are few in number (22) and varied (FG11); cities share few (value, item)
types (FG13: 17%); lists do not run large to small (FG15) and item pairs do not recur (FG16: 1). Tally, counting parts:
491 held, 556 failed (1047 registered).

# Seventy-ninth set, registered before testing (24 September 2026): formulas as records (twenty hypotheses)

From the seventy-eighth set: formula = [header] [N item] ([N item]). Parse, header ('pre'), item and value as there.
'Name header' = a header that is an attested name body; 'numeral-first' = empty header; 'heading header' = a header
that is only 817, 820 or 861. Distinct formula lines (A + B) or distinct (site, type, line) in F. Motif as in the
sixty-seventh set. 10,000-draw permutations; p < 0.05.

Who
- **AR1** Name headers are attested as seal names at the formula's own site more often than when formula sites are
  shuffled (F).
- **AR2** Under name headers, the item depends on the header's last sign (MI).
- **AR3** Items under name headers differ from items under other headers (MI with a label).
- **AR4** Name-header formulas are on seals more often than other formulas (F).
- **AR5** Name headers are shorter than names in general (rank test).
- **AR6** Name headers' own ending (in their name lines) is 740 more often than names' in general.
- **AR7** 30%+ of headers are heading signs only.
- **AR8** 80%+ of headers have 1 or 2 signs.
- **AR9** Under 50% of header-final sign types are also used as items.
What
- **AR10** Items in headed formulas are formula-only signs more often than items in numeral-first formulas.
- **AR11** Items in numeral-first formulas are less varied (entropy, label permutation) than items in headed formulas.
- **AR12** Under heading headers the item is a name head more often than under name headers.
- **AR13** On seals, the motif depends on the item (distinct seal formulas, MI).
Entries
- **AR14** (header, item) pairs recur on 2+ distinct lines more often than when items are shuffled.
- **AR15** For (header, item) pairs on 2+ lines, the values differ in 70%+.
- **AR16** Headed formulas carry larger values than numeral-first formulas (rank test).
- **AR17** Numeral-first formulas are a larger share of formulas at Harappa than at Mohenjo-daro (F).
Replication
- **AR18** B: AR2 holds.
- **AR19** B: AR14 holds.
- **AR20** The item distribution differs between Harappa and Mohenjo-daro headed formulas (F, MI).

## Results of the seventy-ninth set (added after the test; `predict_test79.py`, `results/predict_test79.md`)

Four held, sixteen failed: the 'formulas are records of named agents' reading does not survive. The name headers are
almost all single signs that happen also to be 1-sign names (AR5: mean length 1.18 against 3.72), so the
seventy-eighth set's '23% of headers are names' mostly counts common single signs, not names. Named headers are not
seal names at their own site (AR1: 7 of 79, p = 0.77), do not select their item (AR2, p = 0.15; AR18 in B, p = 0.74),
count the same things as other headers (AR3), are not more on seals (AR4) and are not a 740 class (AR6). (header, item)
entries do not recur beyond chance (AR14, p = 0.085; AR19 in B) and repeated entries change their value in only 47%
(AR15). Headed and numeral-first formulas count equally varied things (AR11), the same kinds of things (AR10, AR12),
with the same values (AR16); the motif does not follow the item (AR13); header signs are also items half the time
(AR9: 65 of 128), and headings alone are 27% of headers (AR7). What holds: headers are short (AR8: 81% of 1-2 signs),
numeral-first formulas are a Harappa form (AR17: 49% against 28%), and the cities count different items (AR20, p =
0.0001). The seventy-eighth set's header-item selection (FG3) stands as a sign-level association, but it is not an
agent-and-goods record in any testable sense. Tally, counting parts: 495 held, 572 failed (1067 registered).

# Eightieth set, registered before testing (24 September 2026): is the ending a case or a class? (twenty hypotheses)

Two readings of 740/520 make opposite predictions. Case: the same head changes ending with context (object, what
follows, site). Class (like grammatical gender): each head has a fixed ending and context does not matter. Distinct
name lines (A + B) or distinct (site, type, line) in F; heads with names under both endings for the within-head tests.
Stratified permutations by head (two-sided where marked); 10,000 draws; p < 0.05.

Case predictions (each holds if the context effect is significant within heads)
- **CG1** Seal against off-seal changes the ending within heads (F, two-sided).
- **CG2** Whether 400 follows the ending changes it within heads (two-sided).
- **CG3** Whether the line opens with the heading unit changes it within heads (two-sided).
- **CG4** Mohenjo-daro against Harappa changes it within heads (F, two-sided).
- **CG5** Whether any sign follows the ending changes it within heads (two-sided).
- **CG6** Being counted (numeral before the head) changes it within heads (two-sided).
Class predictions
- **CG7** 80%+ of heads with 5+ distinct names take one ending in 90%+ of them.
- **CG8** B alone: CG7 holds.
- **CG9** Harappa alone (F): CG7 holds.
- **CG10** Mohenjo-daro alone (F): CG7 holds.
- **CG11** Under 2% of distinct bodies are attested with both endings.
- **CG12** 80%+ of heads taking 520 in the majority (3+ names) are fish signs.
- **CG13** Heads attested with both endings are fish more often than heads with one ending.
Agreement (a class would show concord)
- **CG14** The opener's own majority ending as a head matches the name's ending more than when endings are shuffled.
- **CG15** The same for the sign just before the head.
- **CG16** Within fish heads, the ending follows the majority ending of the sign before the fish (as a head elsewhere).
- **CG17** Two names in one line share their ending more often than random pairs of names.
Controls
- **CG18** Names cited inside formulas have the same 740 share (in their name lines) as other names (p >= 0.05).
- **CG19** Seal names and tablet names with the same head have the same ending share (F; stratified, p >= 0.05).
- **CG20** B alone: CG2 (the 400 context) has no within-head effect (p >= 0.05).

## Results of the eightieth set (added after the test; `predict_test80.py`, `results/predict_test80.md`)

Eleven held, nine failed. The answer is mostly 'class', with one context that forces 740. Class: 43 of 52 heads with
5+ distinct names take one ending in 90%+ (CG7), and this holds in B (CG8: 19 of 23), at Harappa (CG9: 13 of 16) and at
Mohenjo-daro (CG10: 28 of 35); only 19 of 1,070 bodies occur with both endings (CG11); the heads that waver are fish
far more often (CG13: 5 of 15 against 3 of 162). The 520 class is not only fish, though: of 11 heads taking 520 in the
majority, 5 are fish (220, 233, 235, 231, 240) and the rest are 1, 175, 382, 70, 33, 72 (CG12 fails). There is no
concord: the opener's or the pre-head sign's own class does not match the name's ending (CG14, CG15), a fish head does
not take its neighbour's class (CG16), and two names in one line do not agree more than chance (CG17). Context mostly
does not matter: not the heading (CG3), the city (CG4), counting (CG6), nor seal against tablet (CG19 control, p =
0.11; CG1 seal against any off-seal object is p = 0.037, borderline). The one strong context is what follows the
ending: within heads that take both endings, a following sign goes with 740 (CG5: -60 points, p = 0.0002; CG2 for 400
alone: p = 0.021; CG20 in B: p = 0.14). Post-test count on distinct lines: 740 is followed by 400 (114), 90 (69) and
151 (8); 520 by 400 only (10) and never by 90 or 151. So the post-name signs attach to 740: '740 90' and '740 151' are
collocations, not a case alternation of the head. Names cited in formulas are 740 less often (CG18: 72% against 87%),
so citation is not neutral. Tally, counting parts: 506 held, 581 failed (1087 registered).

# Eighty-first set, registered before testing (24 September 2026): what the two classes are (twenty hypotheses)

From the eightieth set: each head belongs to a 740 class or a 520 class. 'Class' of a head = its majority ending over
distinct names (A + B), heads with 3+ distinct names; ties left out. 'Fish' = signs.FISH. '740 90' and '740 151' =
lines where 90 or 151 follows 740. Distinct names and lines; F distinct (site, type, line). Context vectors and
categories as in the sixty-second set. 10,000-draw permutations; p < 0.05.

What the 520 class shares
- **KC1** 520-class names contain a numeral more often than 740-class names, stratified by fish head.
- **KC2** Non-fish 520-class heads are counted (numeral directly before) more often than non-fish 740-class heads.
- **KC3** Non-fish 520-class names hold a fish modifier more often than 740-class names with non-fish heads.
- **KC4** Non-fish 520-class heads are more alike in context to the fish signs (mean cosine) than 740-class heads are
  (rank test).
- **KC5** Class depends on shape category (MI over head types).
- **KC6** 520-class heads have fewer tokens than 740-class heads (rank test over types).
- **KC7** 520-class heads are also formula items more often than 740-class heads (types).
- **KC8** In formulas, 520-class heads are counted with larger values than 740-class heads (rank test).
- **KC9** 520-class heads are preceded by a numeral or fish more often than 740-class heads (distinct names).
- **KC10** Class assignments from A + B agree with F's majority for 90%+ of heads with 5+ names in both.
- **KC11** For 740-class heads, names with a fish before the head still take 740 in 90%+.
- **KC12** 520-class names are a larger share at Harappa than at Mohenjo-daro (F distinct names).
What 90 and 151 are
- **KC13** Among 740 lines, whether 90 follows depends on the head (MI).
- **KC14** Among 740 lines, whether 400 follows depends on the head (MI).
- **KC15** Heads with a '740 90' line and heads with a '740 400' line overlap less than when the follower labels are
  shuffled (Jaccard).
- **KC16** '740 90' lines are on seals more often than other 740 lines (F).
- **KC17** '740 90' lines are at Mohenjo-daro more often than other 740 lines (F).
- **KC18** '740 90' bodies are longer than other 740 bodies (rank test).
Replication
- **KC19** B: KC13 holds.
- **KC20** B: KC3 holds.

## Results of the eighty-first set (added after the test; `predict_test81.py`, `results/predict_test81.md`)

Ten held, ten failed. The 520 class has 11 heads: the fish 220, 231, 233, 235, 240, the numerals 1 and 33 (so '... 1
520' and '... 3 520' put 520 directly after a number, as if 520 were itself counted), and 175, 382, 70, 72. The
classes are stable: the A + B class of every head with 5+ names agrees with F (KC10: 47 of 47), a fish before a
740-class head never moves it (KC11: 156 of 156), and class follows shape category a little (KC5, p = 0.049). 520-class
names take fish modifiers even when the head is not a fish (KC3: 58% against 39%; KC20 in B: 60% against 34%), and
contain numerals more often, stratified by fish head (KC1: +21.5 points, p = 0.023). But non-fish 520 heads are counted
less, not more (KC2: 5% against 16%; the numeral heads 1 and 33 cannot themselves be counted), are no closer to the fish
in context (KC4, p = 0.064), are not rarer (KC6), not formula items more (KC7), not counted higher (KC8: lower, 2.6
against 3.9), not preceded by numerals or fish more (KC9), and not commoner at Harappa (KC12). 90 and 400 after 740 are
selected by the head (KC13: p = 0.0001; KC19 in B: p = 0.0002; KC14: p = 0.006) and by different heads (KC15: Jaccard
0.13, p = 0.0001), so they are two distinct suffix-like signs, each tied to its own set of heads. '740 90' is not a seal,
Mohenjo-daro or long-name form (KC16-KC18). Tally, counting parts: 516 held, 591 failed (1107 registered).

# Eighty-second set, registered before testing (24 September 2026): counted 520 and the suffixes 90, 400, 151 (twenty hypotheses)

Distinct lines (A + B) and distinct (site, type, line) in F unless stated. 'N 520' = 520 directly after a numeral.
'Suffix line' = a name line whose ending is followed by 90, 400 or 151; heads from name_of. Categories from cat_of.
10,000-draw permutations; p < 0.05.

520 after a number
- **PS1** 'N 520' is line-final in 80%+ of its tokens.
- **PS2** Two values cover 80%+ of the numbers before 520.
- **PS3** Lines with 'N 520' are on tablets more often than other lines with 520 (F).
- **PS4** The sign before the numeral in 'N 520' is a fish in 30%+.
- **PS5** 520 tokens follow a numeral more often than 740 tokens do.
The suffixes
- **PS6** 90 follows 740 or 520 in 90%+ of its tokens.
- **PS7** 400 follows 740 or 520 in under 50% of its tokens.
- **PS8** 151 follows 740 or 520 in under 50% of its tokens.
- **PS9** Among heads with a suffix line, 80%+ take only one of 90 and 400.
- **PS10** '740 151' heads overlap with '740 90' heads more than with '740 400' heads (Jaccard).
- **PS11** Among 740 lines, whether 90 follows depends on the head's category (MI).
- **PS12** 90-line heads are counted less often than 400-line heads (distinct names).
- **PS13** 400 suffix lines are on tablets more often than 90 suffix lines (F).
- **PS14** 400 suffix lines are at Harappa more often than 90 suffix lines (F).
- **PS15** 90-line bodies hold a fish less often than 400-line bodies.
- **PS16** Heads with a suffix line are among the 20 commonest heads more often than other heads.
- **PS17** 90-suffix names are one-off (one object) more often than 400-suffix names (F).
- **PS18** '520 400' heads are fish in 50%+.
Replication
- **PS19** B: PS6 holds.
- **PS20** B: 90 heads and 400 heads overlap less than when suffixes are shuffled (Jaccard).

## Results of the eighty-second set (added after the test; `predict_test82.py`, `results/predict_test82.md`)

Thirteen held, seven failed. '520 after a number' is one fixed phrase, not general counting: 55 distinct tokens, 93%
line-final (PS1), 48 of them after 33 (value 3, PS2), and (post-test count) the sign before the number is 705 in 32 and
706 in 14, so '705/706 33 520' accounts for 46 of 55. 520 follows a number far more often than 740 does (PS5: 27%
against 7%) only because of this phrase; no fish is ever counted with it (PS4) and it is not a tablet form (PS3). The
suffixes after the ending are three different signs with different jobs. 400 is the tablet and Harappa suffix (PS13:
80% of 400 suffix lines on tablets against 21% of 90 lines; PS14: 76% at Harappa against 25%) and has other uses (PS7:
46% of 400 tokens follow an ending). 90 is the seal suffix of individual names: 90-suffixed names are one-off far more
often (PS17: 76% against 49%), and 90 bodies hold fish more, not less (PS15 fails: 55% against 32%). 151 behaves like a
variant of 90 (PS10: its heads overlap with 90's, Jaccard 0.31, against 0.05 with 400's) but is mostly used elsewhere
(PS8: 13% after an ending). A head takes one suffix (PS9: 60 of 72), 90 and 400 take different heads (PS20 in B: Jaccard
0.03, p = 0.0001), the head's shape category predicts 90 (PS11, p = 0.0001), and suffixes go with common heads (PS16:
24% against 3%). Not supported: 90 being only a suffix (PS6: 67%; PS19 in B: 51%), 90 heads being counted less (PS12),
and '520 400' heads being fish (PS18: 4 of 10). Tally, counting parts: 529 held, 598 failed (1127 registered).

# Eighty-third set, registered before testing (24 September 2026): what the suffixes do (twenty hypotheses)

From the eighty-second set: 400 is the Harappa tablet suffix, 90 (and 151) the seal suffix of one-off names. Suffix
lines as there. F distinct (site, type, line) unless stated; motif as in the sixty-seventh set; Harappa period via
rtools.level. 10,000-draw permutations; p < 0.05.

400 on tablets: receipts for seal owners?
- **SF1** Name bodies in 400 tablet lines are attested on seals more often than bodies in other tablet name lines.
- **SF2** They are attested on seals at the same site more often than when their sites are shuffled.
- **SF3** 400 tablet lines are incised (TAB:I) more often than other tablet name lines.
- **SF4** At Harappa, 400 tablet lines are from the earlier period more often than other tablet name lines.
- **SF5** 400 tablet texts recur on 2+ objects more often than other tablet name texts.
- **SF6** Three heads cover 50%+ of distinct 400 lines.
- **SF7** 400 tablets carry a picture less often than other tablets with a name.
- **SF8** 30%+ of 400-suffixed bodies are also attested without a suffix.
- **SF9** Where they are, the unsuffixed form is on a seal in 50%+.
- **SF10** At Harappa, 90%+ of 400 lines are on tablets.
- **SF11** At Mohenjo-daro, 50%+ of 400 lines are on seals.
90 on seals: the owner's name?
- **SF12** Seal lines with 90 open with the heading unit less often than other seal name lines.
- **SF13** Seal lines with 90 are on unicorn seals more often than other seal name lines.
- **SF14** 90 seal names contain a numeral less often than other seal names.
- **SF15** 30%+ of 90-suffixed bodies are also attested without a suffix.
- **SF16** At the smaller sites, 70%+ of 90 lines are on seals.
- **SF17** 70%+ of 151 suffix lines are on seals.
Both
- **SF18** 95%+ of suffix lines are the only line on their object.
- **SF19** Heads of 90 lines and of 400 lines overlap in at most 20% of their types (F).
- **SF20** In A's own rows, 400 suffix lines are on tablets more often than 90 suffix lines.

## Results of the eighty-third set (added after the test; `predict_test83.py`, `results/predict_test83.md`)

Nine held, eleven failed. 400 marks a Harappa tablet entry: at Harappa 97% of 400 lines are on tablets (SF10; at
Mohenjo-daro only 38% of its 21 are on seals, SF11), and in A's own rows 87% against 30% for 90 (SF20). 400 tablets are
incised more often (SF3: 52% against 21% of other tablet name lines; object counts), belong to the earlier Harappa
period more often (SF4: 72% against 56%), and carry a picture less often (SF7: 34% against 57%). The suffix is added to
names that exist without it (SF8: 39% of 400 bodies), and the bare form is a seal name in 58% (SF9). But the entries are
not tied to seal owners: 400 tablet bodies are no more often seal names than other tablet names (SF1: 24% against
22%), nor at the same site (SF2, p = 0.098); they do not recur more (SF5) and are spread over many heads (SF6: top three
32, 176, 817 cover 23%). 90 is not a clear 'owner' mark: 90 seal lines are not less headed (SF12), not more on
unicorns (SF13), not less counted (SF14), are added to names attested bare in only 21% (SF15), and at the smaller sites
and for 151 the suffix is not a seal form (SF16: 38%; SF17: 4 of 8). Suffix lines stand alone on their object (SF18:
97%) and 90 and 400 serve different heads (SF19: 11 of 65 types shared). Tally, counting parts: 538 held, 609 failed
(1147 registered).

# Eighty-fourth set, registered before testing (24 September 2026): how the writing changed at Harappa (twenty hypotheses)

Harappa objects with a period (rtools.level: E earlier, L later). Distinct (period, type, line) unless stated; 'name
line', 'formula', suffixes, heading unit, fish, tiered as before. Two-sided Fisher where marked '(two-sided)', else one-
sided in the stated direction; ranks as before. 10,000-draw permutations; p < 0.05.

- **PE1** The share of name lines among lines differs between periods (two-sided).
- **PE2** Formulas open with a numeral in different shares (two-sided).
- **PE3** Later name bodies are longer (rank test).
- **PE4** The 520 share of names differs (two-sided).
- **PE5** The share of names with a fish differs (two-sided).
- **PE6** The heading-unit share of name lines differs (two-sided).
- **PE7** 90 follows the ending more often later.
- **PE8** 400 follows the ending more often earlier.
- **PE9** The tiered share of numerals differs (two-sided).
- **PE10** 20%+ of later sign types are not attested earlier.
- **PE11** 50%+ of head types are found in both periods.
- **PE12** 90%+ of heads with 3+ names in each period keep their class (majority ending).
- **PE13** Dominant adjacent-pair orders in names agree across periods for 85%+ of pairs seen in both.
- **PE14** Count tokens (numerals + 700) are a larger share of lines earlier.
- **PE15** The share of lines with a double differs (two-sided).
- **PE16** Later lines are longer (rank test).
- **PE17** Seals are a larger share of objects later (objects).
- **PE18** Moulded tablets are a larger share of tablets later (objects).
- **PE19** Tablets carry a picture more often later (objects).
- **PE20** Formulas with a numeral have a header more often later.

## Results of the eighty-fourth set (added after the test; `predict_test84.py`, `results/predict_test84.md`)

Nine held, eleven failed. At Harappa (811 dated objects; 253 earlier and 239 later distinct lines) the writing grows
longer and more formal over time: later name bodies are longer (PE3: 3.4 against 2.7 signs) and lines are longer (PE16:
4.1 against 3.5), the heading unit becomes commoner in names (PE6: 17% against 6%), and the 400 receipt suffix fades
(PE8: 28% earlier against 18% later). The media shift: seals are a larger share of objects later (PE17: 29% against
17%) and moulded tablets replace incised ones (PE18: 65% against 36% of tablets). The grammar does not change: the
share of names (PE1), numeral-first formulas (PE2), 520 (PE4), fish names (PE5), tiered numerals (PE9), count tokens
(PE14), doubles (PE15) and headers (PE20) are all stable, and heads keep their class (PE12: 8 of 8) and pairs their
order (PE13: 3 of 3), though both of these rest on very few cases. 38% of later sign types are not attested earlier
(PE10), but with ~250 lines per period that has no null and is expected from sampling. Head types are less than half
shared between periods (PE11: 42%), 90 does not grow (PE7) and tablet pictures grow only slightly (PE19, p = 0.09).
Tally, counting parts: 547 held, 620 failed (1167 registered).

# Eighty-fifth set, registered before testing (24 September 2026): one grammar, two cities? (twenty hypotheses)

F distinct (site, line) and distinct (site, name) for Mohenjo-daro (MD) and Harappa (H). Shared-grammar tests are run
within each city; difference tests are two-sided Fisher unless a rank test is named. Definitions as in the sets cited.
10,000-draw permutations; p < 0.05.

Shared grammar
- **CS1** Heads with 3+ names in both cities have the same class in 90%+.
- **CS2** MD: in 4-sign bodies the last two signs form an attested 2-sign body more often than the first two.
- **CS3** H: the same.
- **CS4** MD: numerals of value 5-8 are tiered more often than those of 1-4.
- **CS5** H: the same.
- **CS6** MD: the numeral kind depends on the next sign (MI).
- **CS7** H: the same.
- **CS8** MD: distinct 520 names hold a fish more often than distinct 740 names.
- **CS9** H: the same.
- **CS10** MD: heads of '740 90' and '740 400' lines overlap less than with shuffled suffixes.
- **CS11** Dominant pair orders in names agree between the cities for 85%+ of pairs seen in 3+ bodies at each.
Local habits
- **CS12** The 520 share of names differs.
- **CS13** Name body length differs (rank test).
- **CS14** The heading-unit share of name lines differs.
- **CS15** The share of name lines with a suffix differs.
- **CS16** The share of formulas among lines differs.
- **CS17** The tiered share of numerals differs.
- **CS18** The share of lines with a double differs.
- **CS19** The counted item in numeral formulas depends on the city (MI).
- **CS20** The two cities' five commonest heads share at most three.

## Results of the eighty-fifth set (added after the test; `predict_test85.py`, `results/predict_test85.md`)

Sixteen held, four failed. One grammar, two local styles. Shared, tested within each city on distinct lines and names:
head classes (CS1: 29 of 32 heads the same class), right-branching names (CS2 MD: 19 against 9; CS3 H: 12 against 2),
the tiered form for 5-8 (CS4 MD: 57% against 1%; CS5 H: 61% against 3%), the next sign setting the numeral kind (CS6,
CS7: 0.71 and 0.75 bits), the fish-520 link (CS8 MD: 76% against 44%; CS9 H: 67% against 34%) and pair order (CS11: 67
of 75). Local: Mohenjo-daro names are longer (CS13: 3.9 against 3.1) and headed twice as often (CS14: 21% against 10%);
Harappa suffixes its names nearly three times as often (CS15: 28% against 10%, the 400 receipts) and writes more
formulas (CS16: 47% against 40%); the cities count different items (CS19, p = 0.002) and share three of their five
commonest heads (CS20: 100, 220, 760; MD adds 33, 923, H adds 176, 32). Not different: the 520 share (CS12), tiered share
(CS17) and doubling (CS18). At Mohenjo-daro alone the 90/400 head split is not significant (CS10: 54 lines, p = 0.49).
Tally, counting parts: 563 held, 624 failed (1187 registered).

# Eighty-sixth set, registered before testing (24 September 2026): recent findings on held-out data (twenty hypotheses)

Findings of the seventy-fourth to eighty-fifth sets re-tested on data they were not found on: the smaller sites (F
outside Mohenjo-daro and Harappa, 'OS'), Mahadevan's transcription alone (B), or the fuller corpus F as a whole.
Distinct lines and names throughout; definitions as in the original sets. 10,000-draw permutations; p < 0.05.

Smaller sites
- **HO1** (QS2) In 3-sign bodies, (middle, head) is an attested A + B body more often than (opener, middle).
- **HO2** (EF, distinct) 520 names hold a fish more often than 740 names.
- **HO3** (CG7) 80%+ of heads with 3+ names take one ending in 90%+.
- **HO4** (KC10) For heads with 2+ OS names and an A + B class, the OS majority ending equals that class in 90%+.
- **HO5** (core) Numerals of value 5-8 are tiered more often than those of 1-4.
- **HO6** (core) The numeral kind depends on the next sign (MI).
- **HO7** (FG3) In numeral formulas with a header, the item depends on the header's last sign (MI).
- **HO8** (HR20) 50%+ of OS names end in one of the ten commonest A + B heads.
Mahadevan's transcription
- **HO9** (NP1) The modifier before the head depends on the head's category (MI).
- **HO10** (CG11) Under 2% of bodies are attested with both endings.
- **HO11** (PS9) Among heads with a suffix line, 80%+ take only one of 90 and 400.
- **HO12** (FG8) In formulas, the value depends on the item (MI).
- **HO13** (LX11) Names and formulas share fewer (numeral, sign) types than label-shuffled lines (1,000).
- **HO14** (DN14) Name lines repeat adjacent pairs more than formulas (1,000).
The fuller corpus
- **HO15** (NP20, observed direction) 'N mod head' is commoner than 'mod N head'.
- **HO16** (FG3) The item depends on the header's last sign (MI).
- **HO17** (KC15) '740 90' heads and '740 400' heads overlap less than with shuffled suffixes.
- **HO18** (QS1) The middle sign of 3-sign bodies tells more about the head than about the opener.
- **HO19** (PS2) 80%+ of distinct 'N 520' lines are '705/706 33 520'.
- **HO20** (CG7) 80%+ of heads with 5+ names take one ending in 90%+.

## Results of the eighty-sixth set (added after the test; `predict_test86.py`, `results/predict_test86.md`)

Twelve held, eight failed, with a clear split. The number system travels everywhere: at the smaller sites (457
distinct lines) the tiered form is for 5-8 (HO5: 59% against 5%) and the next sign sets the numeral kind (HO6, p =
0.0003). The name grammar does not travel to the smaller sites: no right-branching signal (HO1: 4 against 4), no
fish-520 link (HO2: 48% against 38%, p = 0.20), heads less fixed in class (HO3: 11 of 17), classes matching A + B only
89% (HO4, just under 90%), and only a third of names ending in a common city head (HO8: 33%). In Mahadevan's
transcription the recent name findings hold: head selects modifier (HO9), bodies keep their ending (HO10: 5 of 314),
one suffix per head (HO11: 34 of 36), the item sets the count (HO12), names and formulas count differently (HO13) and
names are the repetitive genre (HO14). In the fuller corpus: 90 and 400 take different heads (HO17), the middle leans
on the head (HO18), 'N 520' is the 705/706 33 520 phrase (HO19: 37 of 45) and classes are fixed (HO20: 41 of 49). Not
confirmed in F: the header selecting the item (HO16, p = 0.13; FG3 rested on A + B) and 'N mod head' outnumbering 'mod
N head' (HO15: 98 against 92). Reading: the two cities share one name grammar and one number system; the smaller sites
share the number system but write names differently (or too few survive to show the pattern). Tally, counting parts:
575 held, 632 failed (1207 registered).

# Eighty-seventh set, registered before testing (24 September 2026): regional name systems (twenty hypotheses)

The eighty-sixth set found the name grammar does not show at the smaller sites. Regions from rtools.region: Sindh
(Mohenjo-daro, Chanhu-daro, ...), north (Harappa, Kalibangan, ...), Gujarat (Lothal, Dholavira, ...). F distinct
(site, name) and (site, line). 'City top-10 heads' from A + B. Units as in the sixty-first set. 10,000-draw
permutations; p < 0.05; two-sided where marked.

Gujarat
- **RS1** Gujarat 520 names hold a fish more often than Gujarat 740 names.
- **RS2** Gujarat names end in a city top-10 head less often than Mohenjo-daro names.
- **RS3** Gujarat head types overlap more with Mohenjo-daro's than with Harappa's (Jaccard).
- **RS4** The Gujarat 520 share differs from the two cities' (two-sided).
- **RS5** Gujarat names are shorter than Mohenjo-daro names (rank test).
- **RS6** Gujarat name lines have the heading unit less often than Mohenjo-daro's.
- **RS7** Formulas are a larger share of lines in Gujarat than at Mohenjo-daro.
- **RS8** 10%+ of Gujarat sign types occur at neither city.
- **RS9** In Gujarat, 50%+ of numerals of value 5-8 are tiered.
- **RS10** Lothal and Dholavira share head types less (Jaccard) than Mohenjo-daro and Harappa do.
- **RS11** Under 10% of Dholavira names end in 520.
North and Sindh outside the cities
- **RS12** Kalibangan head types overlap more with Harappa's than with Mohenjo-daro's.
- **RS13** Chanhu-daro head types overlap more with Mohenjo-daro's than with Harappa's.
- **RS14** Chanhu-daro names end in a Mohenjo-daro top-10 head more often than Gujarat names do.
- **RS15** Kalibangan names are shorter than Harappa names (rank test).
- **RS16** Kalibangan name lines have the heading unit less often than Harappa's.
All regions
- **RS17** The head depends on the region (MI over distinct (region, name)).
- **RS18** The ending depends on the region (MI).
- **RS19** The first sign of formulas depends on the region (MI).
- **RS20** 50%+ of small-site names of 3+ signs contain a unit.

## Results of the eighty-seventh set (added after the test; `predict_test87.py`, `results/predict_test87.md`)

Four held, sixteen failed, and the failures mostly say 'no regional difference'. Gujarat's 64 distinct names end in a
common city head exactly as often as Mohenjo-daro's (RS2: 41% and 41%), overlap equally with both cities' heads (RS3:
0.22 and 0.22), and do not differ in 520 share (RS4), length (RS5, p = 0.06) or heading (RS6); only 6% of Gujarat sign
types are absent from both cities (RS8). Kalibangan and Chanhu-daro do not lean to their nearer city (RS12, RS13, RS14
the other way), and Kalibangan names are like Harappa's in length (RS15) and heading (RS16). Over all regions the
head, the ending and the formula opening do not depend on region (RS17-RS19: p = 0.20, 0.21, 0.18). What held: Gujarat
writes more formulas (RS7: 51% against 40%), uses the tiered form for 5-8 (RS9: 7 of 12), Lothal and Dholavira share
fewer head types than the two cities (RS10: 0.26 against 0.47, expected with fewer names), and 63% of small-site names
of 3+ signs contain a city unit (RS20). Not confirmed: fish-520 in Gujarat (RS1: 5 of 15) and Dholavira avoiding 520
(RS11: 25%). This revises the eighty-sixth set's reading: the smaller sites use the same name stock and the same
units; the grammar tests failed there because 160 names are too few, not because the system differs. Tally, counting
parts: 579 held, 648 failed (1227 registered).

# Eighty-eighth set, registered before testing (24 September 2026): lines with two names (twenty hypotheses)

'Two-name line' = a distinct line (A + B) with exactly two ending tokens (740/520), each with a non-empty segment
before it. First segment = the signs before the first ending (heading unit removed); second segment = the signs after
the first ending (and any 400/90/151 right after it) up to the second ending. 'One-name line' = a name line with one
ending. F for object and site tests. 10,000-draw permutations; p < 0.05.

- **TN1** Two-name lines are 2%+ of distinct lines with an ending.
- **TN2** Both segments are attested name bodies in 30%+ of two-name lines.
- **TN3** The second segment is shorter than the first more often than longer (sign test).
- **TN4** The two segments share their last sign more often than random pairs of name bodies.
- **TN5** They share their first sign more often than random pairs.
- **TN6** Two-name lines are on seals less often than one-name lines (F).
- **TN7** Two-name lines are at Mohenjo-daro more often than one-name lines (F).
- **TN8** The first ending is 740 in 90%+.
- **TN9** A 400, 90 or 151 follows the first ending in 20%+.
- **TN10** Two-name lines open with the heading unit more often than one-name lines.
- **TN11** The second segment ends in a top-10 head more often than the first (sign test).
- **TN12** The second segment is one sign in 30%+.
- **TN13** Second segments recur across two-name lines more often than first segments.
- **TN14** Second-segment last signs are formula items more often than first-segment last signs.
- **TN15** Two-name lines contain a numeral more often than one-name lines.
- **TN16** The numeral stands in the second segment more often than the first (sign test over lines with one).
- **TN17** 30%+ of second segments are also attested as a whole one-name line's body.
- **TN18** 30%+ of first segments are.
- **TN19** B: TN3 holds.
- **TN20** B: TN12 holds.

## Results of the eighty-eighth set (added after the test; `predict_test88.py`, `results/predict_test88.md`)

Three held, seventeen failed; the 'two names in a line' reading is not supported. Only 23 distinct lines have two
endings with a segment before each (TN1: 1.6%, under 2%), 16 of 18 located ones at Mohenjo-daro (TN7: 89% against
53%). Their parts do not look like two names: both segments are attested bodies in only 2 of 23 (TN2), the first
segment stands alone as a name in only 4 (TN18), the two never share a head (TN4: 0), the first ending is not always
740 (TN8: 78%), no suffix ever separates them (TN9: 0), and none is headed (TN10: 0 against 17%). Only the second
segment is sometimes a known name (TN17: 10 of 23; TN20 in B: 3 of 7 are one sign). The other tests fail on 23 cases.
Reading: a medial 740 or 520 is mostly not the end of a first name but part of a longer compound (an inner '... 740 ...'
element), with the true name at the end; the long lines that looked like two names (thirty-eighth set, LT1) are better
read as long single names at Mohenjo-daro. Tally, counting parts: 582 held, 665 failed (1247 registered).

# Eighty-ninth set, registered before testing (24 September 2026): the three heading signs (twenty hypotheses)

'Heading' = 817, 820 or 861 as the first sign of a line of 2+ signs; 'headed name line' = a headed line that is a name
line. Distinct lines (A + B) unless stated; F distinct (site, type, line) and objects for site, type and motif tests.
Motif as in the sixty-seventh set. 10,000-draw permutations; p < 0.05.

What chooses the heading sign
- **HS1** The heading sign depends on the head of the name that follows (MI).
- **HS2** It depends on the city (F, MI).
- **HS3** It depends on seal against tablet (F, MI).
- **HS4** 861-headed lines are formulas more often than 817-headed lines.
- **HS5** 90%+ of 817 headings are followed by 2.
- **HS6** 90%+ of 820 headings are followed by 2.
- **HS7** 90%+ of 861 headings are followed by 2.
- **HS8** The sign after the heading (2 against other) depends on the heading sign (MI).
- **HS9** The same body follows 2+ different heading signs in 20%+ of bodies seen headed 2+ times.
Where heading signs occur otherwise
- **HS10** 50%+ of non-initial 817/820/861 tokens directly follow a numeral.
- **HS11** Under 2% of lines hold two heading-sign tokens.
What headed names are
- **HS12** At Mohenjo-daro, headed name bodies are longer than unheaded ones (rank test).
- **HS13** Headed names take 740 as often as unheaded names (two-sided p >= 0.05).
- **HS14** Headed names hold a fish less often than unheaded names.
- **HS15** At Mohenjo-daro, headed name lines carry a suffix less often than unheaded ones.
- **HS16** Headed seals carry the unicorn more often than unheaded seals (F objects).
- **HS17** Headed names are one-off (one object) more often than unheaded names (F).
- **HS18** 95%+ of headed lines are the only line on their object (F).
Replication
- **HS19** B: HS1 holds.
- **HS20** B: HS7 holds.

## Results of the eighty-ninth set (added after the test; `predict_test89.py`, `results/predict_test89.md`)

Eight held, twelve failed. 419 distinct headed lines (861 x174, 820 x142, 817 x103). The three heading signs are
interchangeable in front of names: a body seen headed twice is found after two different heading signs in 20 of 22
(HS9), and the choice depends on neither the name's head (HS1, p = 0.77; HS19 in B, p = 0.78), the city (HS2) nor
seal against tablet (HS3). What differs is the sign that follows (HS8, p = 0.0001; post-test counts): 817 and 861 take 2
(87%, 86%) or 368 (7, 11), while 820 takes 2 (56%), 60 (22) or 1 (14), so 820 goes with a wider set of stroke signs
(HS5-HS7 fail their 90% threshold; HS20 in B: 84% for 861). 861 heads formulas more than 817 does (HS4: 47% against
31%). The heading unit stands at the start of a line on its own object (HS18: 97%; HS11: 1% of lines hold two heading
signs); inside a line these signs are rarely counted (HS10: 10%). Headed names keep their ending class (HS13: 82%
against 86% 740, p = 0.11), carry a suffix less (HS15 at Mohenjo-daro: 6% against 12%) and sit on unicorn seals a
little more (HS16: 80% against 74%, p = 0.045). Against expectation, headed names at Mohenjo-daro are shorter, not
longer (HS12: 3.0 against 4.0 signs, so the heading takes the place of part of the name), hold fish more (HS14: 51%
against 42%) and repeat more (HS17: 70% one-off against 84%). Tally, counting parts: 590 held, 677 failed (1267
registered).

# Ninetieth set, registered before testing (24 September 2026): the minor media (twenty hypotheses)

F object types beyond seals and tablets: potsherd graffiti (POT:T:g), stamped potsherds (POT:T:s), copper tablets
(TAB:C), bangles (BNGL), tags (TAG, TAG:L). 'Seal lines' = lines on SEAL types. Distinct (type, line) unless stated.
City top-10 heads from A + B; formula-only signs as in the fifty-fourth set. 10,000-draw permutations; p < 0.05.

Graffiti
- **MM1** Graffiti lines are shorter than seal lines (rank test).
- **MM2** Graffiti lines hold a numeral more often than seal lines.
- **MM3** Graffiti lines are count tokens (numerals + 700) more often than seal lines.
- **MM4** Graffiti names end in a top-10 head more often than seal names.
- **MM5** Graffiti tokens are formula-only signs more often than seal tokens.
- **MM6** Graffiti numerals are of the short kind more often than seal numerals.
- **MM7** At Harappa, graffiti are count tokens more often than graffiti elsewhere.
Stamped pots and tags
- **MM8** 30%+ of stamped-pot lines also occur on a seal.
- **MM9** Stamped-pot lines occur on a seal more often than graffiti lines do.
- **MM10** 30%+ of tag lines also occur on a seal.
Copper tablets
- **MM11** 30%+ of distinct copper-tablet texts are on 2+ copper tablets.
- **MM12** Copper-tablet lines are name lines less often than seal lines.
- **MM13** 90%+ of copper tablets are from Mohenjo-daro.
- **MM14** Under 10% of copper-tablet lines also occur on a seal.
Bangles
- **MM15** 80%+ of bangle lines have 3 signs or fewer.
- **MM16** Bangle lines are formulas more often than seal lines.
All media
- **MM17** Line length depends on the medium (MI over length strata; seal, TAB:I, TAB:B, TAB:C, graffiti, bangle).
- **MM18** The last sign depends on the medium (MI).
- **MM19** The first sign depends on the medium (MI).
- **MM20** The 520 share of names differs between seals and all non-seal media (two-sided).

## Results of the ninetieth set (added after the test; `predict_test90.py`, `results/predict_test90.md`)

Twelve held, eight failed. Each medium has its own kind of text (length, first sign and last sign all depend on the
medium: MM17-MM19, p = 0.0001). Copper tablets are a Mohenjo-daro genre (MM13: 197 of 198) of repeated texts (MM11: 51%
of distinct texts on 2+ tablets) that are rarely names (MM12: 35% against 49% of seal lines) and almost never seal
texts (MM14: 2 of 68): copper tablets carry their own fixed labels. Bangles carry very short texts (MM15: 90% of 3
signs or fewer), mostly formulas (MM16: 65%). Potsherd graffiti are short (MM1: 2.1 against 4.7 signs); count tokens
are rare there (MM3: 2 of 127, more than on seals but negligible), and graffiti are not more numerical (MM2), do not
name common heads (MM4), do not use formula-only signs more (MM5) and use fewer stroke numerals (MM6: 33% against 57%).
Stamped potsherds and tags are not impressions of known seal texts (MM8: 5 of 27; MM10: 3 of 26), and stamped pots copy
seals no more than graffiti do (MM9), so the stamps that made them are mostly not among the surviving seals. Names on
seals take 520 twice as often as names on other media (MM20: 18% against 9%, p = 0.0002), so the 520 class is a seal
feature. Tally, counting parts: 602 held, 685 failed (1287 registered).

# Ninety-first set, registered before testing (24 September 2026): endings in mid-line (twenty hypotheses)

From the eighty-eighth set: a 740 or 520 inside a line is mostly not the end of a first name. 'Medial ending' = a 740/520
token that is neither the last sign nor directly followed only by 400, 90 or 151 at line end. Distinct lines (A + B)
unless stated; F distinct (site, type, line) and objects for site, type and repeat tests. Head class from classes(A).
10,000-draw permutations; p < 0.05.

- **MX1** 85%+ of medial endings are 740.
- **MX2** 70%+ of lines with a medial ending are from Mohenjo-daro (F).
- **MX3** The sign before a medial ending is head-class less often than the sign before a final ending.
- **MX4** In lines that also end in a name, the segment after the medial ending is an attested body more often than
  the segment before it (sign test).
- **MX5** Medial endings follow a numeral more often than final endings do.
- **MX6** The sign after a medial ending is a fish in 20%+.
- **MX7** The sign after a medial ending depends on the sign before it (MI).
- **MX8** For 50%+ of medial endings, 'sign before + ending' is also a whole 1-sign-body name.
- **MX9** 70%+ of lines with a medial ending also end in a name.
- **MX10** 70%+ of lines with a medial ending are on seals (F).
- **MX11** Lines with a medial ending open with the heading unit less often than name lines without one.
- **MX12** 80%+ of segments before the first medial ending have 1 or 2 signs.
- **MX13** The sign before a medial ending recurs (2+ lines) in 30%+ of medial-ending lines.
- **MX14** The final ending of medial-ending lines is 740 at the name-line rate (two-sided p >= 0.05).
- **MX15** Under 10% of medial endings are directly followed by a numeral.
- **MX16** Lines with a medial ending hold a numeral more often than other name lines.
- **MX17** Medial 520s follow a fish in 50%+.
- **MX18** Medial-ending texts are on one object only more often than other name texts (F).
- **MX19** B: MX1 holds.
- **MX20** B: MX4 holds.

## Results of the ninety-first set (added after the test; `predict_test91.py`, `results/predict_test91.md`)

Ten held, ten failed. 184 distinct lines have a mid-line ending (187 tokens), 87% of them 740 (MX1; MX19 in B: 88%).
The eighty-eighth set's 'part of a long compound' reading is revised: the medial ending usually closes a real short
name and something else follows. The sign plus ending before it is itself a whole 1-sign name in 66% (MX8), the sign
recurs (MX13: 72%; 176 x22, 220 x15, 233 x8, 100 x7, 240 x6), and it is a head-class sign less often than before a final
ending (MX3: 27% against 38%). Only 13% of these lines also end in a name (MX9 fails); the tail is short (post-test:
1-3 signs in 83%) and often a numeral (MX15: 17% of medial endings are followed by one; commonest followers 1, 679,
621, 32, 90), sometimes a second headed entry ('... 520 32 861 2 ...'). The before and after signs form fixed phrases
(MX7, p = 0.0001). These lines are seal texts (MX10: 75%), rarely headed (MX11: 7% against 17%), unique (MX18: 91% on one
object) and spread over both cities (MX2: 62% Mohenjo-daro). Not supported: fish after the ending (MX6), numerals
before it (MX5), a name after it (MX4, MX20: 6-2 and 2-0), a short first element (MX12: 49%), extra numerals (MX16) and
fish before medial 520 (MX17: 10 of 24). Reading: 'short name + ending + short tail', a name followed by an
annotation, mostly on one-off seals. Tally, counting parts: 612 held, 695 failed (1307 registered).

# Ninety-second set, registered before testing (24 September 2026): the jar signs 700, 705, 706 (twenty hypotheses)

700 is the count sign (numeral + 700); 705 and 706 sit in the fixed phrase '705/706 33 520' (eighty-second set).
Distinct lines (A + B) unless stated; context vectors as in the sixty-second set (signs with 5+ tokens); categories
from cat_of. 10,000-draw permutations; p < 0.05.

- **CF1** 705 and 706 are more alike in context than frequency-matched random pairs.
- **CF2** 700 is more alike in context to 705 and 706 than frequency-matched random signs are.
- **CF3** 50%+ of 705 and 706 tokens are directly followed by a numeral.
- **CF4** 60%+ of those numerals are 33 (long 3).
- **CF5** Numerals after 705/706 are of the long kind more often than numerals after other signs.
- **CF6** Under 10% of 705/706 tokens directly follow a numeral (705/706 are not counted; they are followed by the
  count, 700 is preceded by it).
- **CF7** 50%+ of lines with 705 or 706 end in 520.
- **CF8** 70%+ of 705/706 lines are on seals (F).
- **CF9** 705/706 lines are a larger share of lines at Mohenjo-daro than at Harappa (F).
- **CF10** 80%+ of 700 lines are on tablets (F).
- **CF11** 705 and 706 are free variants: the sign before does not depend on which (MI p >= 0.05).
- **CF12** After '705/706 + numeral', the next sign is 520 in 50%+.
- **CF13** In '705/706 + numeral + 520', the value is 3 in 80%+.
- **CF14** 60%+ of 705/706 lines are name lines.
- **CF15** Under 5% of 700 tokens stand inside a name body.
- **CF16** 705/706 account for 30%+ of signs directly before 33.
- **CF17** B: CF3 holds.
- **CF18** B: CF4 holds.
- **CF19** F: CF13 holds.
- **CF20** 705 and 706 have the same shape category as 700.

## Results of the ninety-second set (added after the test; `predict_test92.py`, `results/predict_test92.md`)

Eleven held, nine failed. '705/706 33' is a fixed pair: 95% of numerals after 705/706 are 33 (CF4; CF18 in B: 36 of
36), 97% of them are long-kind against 25% after other signs (CF5), and 75% of the signs directly before 33 are 705 or
706 (CF16: 705 x88, 706 x29). The 520 that sometimes follows always comes with value 3 (CF13: 46 of 46; CF19 in F: 37
of 37). 705 and 706 are free variants: they share context far more than chance (CF1: cosine 0.40, p = 0.0006) and the
sign before them does not choose between them (CF11, p = 0.81). Their lines are seal texts (CF8: 73%) and commoner at
Mohenjo-daro (CF9: 8.6% against 5.4% of lines). They are not a family with the count sign 700: 700 does not share their
context (CF2, p = 0.87), 700 lines are not mostly tablets (CF10: 59%), 700 is inside a name body in 11% of distinct cases
(CF15), and the shapes are catalogued differently (CF20: 700 J, 706 I, 705 none). Also not supported: 705/706 never
counted (CF6: 13% follow a numeral), their lines ending in 520 (CF7: 21%; CF12: 38% after the count) or being names
(CF14: 52%), and CF3 in B (41%). Reading: '705/706 33' behaves like one lexical unit (a 'three-X' compound written with
the long 3), often closed by 520 as a name, not like a count of jars. Tally, counting parts: 623 held, 704 failed (1327
registered).

# Ninety-third set, registered before testing (24 September 2026): frozen numbers and real counts (twenty hypotheses)

The ninety-second set found '705/706 33' to be a fixed unit. Over distinct lines (A + B): for each sign X counted 5+
times (directly after a numeral run), 'value share' = the share of its counts that take its commonest value. 'Frozen' =
value share 0.9+; 'variable' = under 0.6. 10,000-draw permutations; p < 0.05.

- **FZ1** 20%+ of signs counted 5+ times are frozen.
- **FZ2** Frozen pairs are in name lines more often than variable pairs (tokens).
- **FZ3** Frozen pairs use the long kind more often than variable pairs.
- **FZ4** Frozen signs are counted more often (share of their tokens after a numeral) than variable signs (rank test).
- **FZ5** Frozen pairs are followed by an ending more often than variable pairs.
- **FZ6** Variable pairs are in formulas more often than frozen pairs.
- **FZ7** Variable pairs are line-final more often than frozen pairs.
- **FZ8** Frozen pairs are at Mohenjo-daro more often than variable pairs (F).
- **FZ9** Variable pairs are on tablets more often than frozen pairs (F).
- **FZ10** A frozen sign's value is the same in A and in B for 90%+ of frozen signs counted 3+ times in B.
- **FZ11** Frozen signs are counted with value 3 more often than variable signs are.
- **FZ12** Frozen pairs recur in 2+ distinct lines more often than variable (value, sign) pairs.
- **FZ13** The sign before a frozen pair is a heading sign less often than the sign before a variable pair.
- **FZ14** The numeral of a frozen pair is preceded by a non-numeral more often than that of a variable pair.
- **FZ15** Value share depends on the numeral kind of the sign's commonest count (MI over signs, kind against frozen).
- **FZ16** Signs counted mostly by long strokes have higher value shares than signs counted mostly by short strokes
  (rank test).
- **FZ17** 700 is variable (value share under 0.6).
- **FZ18** Frozen signs are also name heads more often than variable signs.
- **FZ19** B: FZ2 holds.
- **FZ20** F: FZ1 holds.

## Results of the ninety-third set (added after the test; `predict_test93.py`, `results/predict_test93.md`)

Four held, sixteen failed: frozen numerals before a sign are rare, so counts are mostly real counts. Of 66 signs
counted 5+ times, only 4 always take one value (FZ1: 236 = 2, 632 = 2, 717 = 2, 923 = 3; FZ20 in F: 3 of 62), 36 are
variable, and 700 is variable (FZ17: value share 0.59). The four frozen pairs keep their value in B (FZ10: 4 of 4), are
all at Mohenjo-daro (FZ8: 14 of 14 located tokens) and are written with long strokes more (FZ3: 67% against 41%). They
are not a class otherwise: not more in names (FZ2, FZ19), not more name-final (FZ5), not always counted (FZ4), not more
often 3 (FZ11), not heads more (FZ18); variable counts are not more in formulas (FZ6) or line-final (FZ7, p = 0.06) or on
tablets (FZ9); notation does not predict frozenness (FZ15, FZ16). Note: the '705/706 33' unit of the ninety-second set
is not in this count because there the numeral follows the sign; the frozen pattern shows up on both sides of a sign
but only for a handful of Mohenjo-daro signs. Tally, counting parts: 627 held, 720 failed (1347 registered).

# Ninety-fourth set, registered before testing (24 September 2026): copper tablets and their pictures (twenty hypotheses)

F copper tablets (TAB:C, 198, nearly all Mohenjo-daro). Motif = the ICIT field up to ':' ('', 'None', '-', 'Unknown' =
none; 'Othr' kept as a category). Text = the tablet's lines joined. Seal lines and seal motifs as in the sixty-seventh
set. 10,000-draw permutations; p < 0.05.

Text and picture
- **CU1** Copper tablets with the same text share the motif more often than when motifs are shuffled.
- **CU2** The text depends on the motif (MI over tablets with a motif).
- **CU3** For motifs on 5+ tablets, the commonest text covers 50%+ of that motif's tablets on average.
- **CU4** 80%+ of texts on 2+ tablets with a motif have one motif.
- **CU5** 80%+ of anthropomorph (Anth) tablets carry one text.
- **CU6** 80%+ of hare tablets carry one text.
- **CU7** Tablets whose text repeats have a motif more often than tablets with a unique text.
- **CU8** Text length depends on the motif (MI).
- **CU9** Copper and seal texts for the same animal share sign types more than texts for different animals
  (mean Jaccard, animals on both, permutation of copper motifs).
The copper texts
- **CU10** 60 or fewer distinct texts among the copper tablets.
- **CU11** 20%+ of copper tokens are signs never on seals.
- **CU12** 40%+ of copper lines hold a numeral.
- **CU13** Copper numerals are long-kind more often than seal numerals.
- **CU14** Copper lines open with a heading sign less often than seal lines.
- **CU15** Under 40% of copper lines end in 740.
- **CU16** Copper tablets with an animal motif are name lines more often than those with 'Othr'.
- **CU17** 'Othr' tablets have more distinct texts per tablet than animal-motif tablets.
- **CU18** 5 or fewer copper tablets have two lines.
- **CU19** Copper text heads (last signs) are shared by tablets of one motif more than when motifs are shuffled.
- **CU20** Copper texts share fewer adjacent-pair types with seal texts than label-shuffled lines do (1,000).

## Results of the ninety-fourth set (added after the test; `predict_test94.py`, `results/predict_test94.md`)

Thirteen held, seven failed. On copper tablets text and picture are bound: same-text tablets share the picture (CU1:
545 pairs, p = 0.0001), the picture predicts the text (CU2: 2.6 bits), its length (CU8) and its last sign (CU19), and
each picture has a dominant text (CU3: mean share 0.65). All 10 anthropomorph tablets carry '806 845 61 407 850 900
740' (CU5) and all 12 hare tablets '235 705 33 845 407 321 407' (CU6); both labels share 845 and 407, and the hare label
contains the fixed unit '705 33' of the ninety-second set. A text is not always tied to one picture (CU4: 10 of 15).
Copper labels count (CU12: 44% of lines hold a numeral), with long strokes more than seals (CU13: 51% against 32%), are
almost never headed (CU14: 1% against 19%), are one line (CU18: 2 two-line tablets) and share fewer adjacent pairs with
seal texts than chance (CU20), but they use the seal sign set (CU11: 4% of tokens not on seals). The same animal's
copper and seal texts share signs slightly more than different animals' do (CU9: +0.010 Jaccard, p = 0.025), a weak
link across media. Not supported: few distinct labels (CU10: 70 texts for 198 tablets), 740 rare (CU15: 44%), animal
tablets carrying names (CU16: the other way, 36% against 79% for 'Othr'), 'Othr' being more varied (CU17), repeated
labels having pictures more (CU7). Tally, counting parts: 640 held, 727 failed (1367 registered).

# Ninety-fifth set, registered before testing (24 September 2026): the single stroke '1' (twenty hypotheses)

Sign '1' (value 1, short) keeps turning up outside counting: after the heading 820, after mid-line 740, as a 520-class
head. Distinct lines (A + B) unless stated; comparisons against the short numerals '2' and '3' (their tokens). F for
object and site tests. 10,000-draw permutations; p < 0.05.

- **ON1** '1' is directly followed by a non-numeral less often than '2' and '3'.
- **ON2** '1' is line-final more often than '2' and '3'.
- **ON3** '1' directly follows 740 or 520 more often than '2' and '3'.
- **ON4** 90%+ of 'heading + 1' are '820 1'.
- **ON5** 70%+ of '1' tokens are preceded by a non-numeral.
- **ON6** The sign before '1' is a name head more often than the sign before '2' or '3'.
- **ON7** Bodies ending in '1' take 520 more often than bodies ending in another numeral.
- **ON8** Five signs cover 50%+ of the non-numerals after '1'.
- **ON9** '1' tokens are on seals more often than '2' and '3' tokens (F).
- **ON10** '1' is a larger share of numeral tokens at Mohenjo-daro than at Harappa (F).
- **ON11** '1' stands inside a name body more often than '2' and '3'.
- **ON12** Under 5% of '1' tokens begin a line.
- **ON13** '1' stands next to another numeral less often than '2' and '3'.
- **ON14** After a medial 740, '1' is followed by the line end within two signs in 70%+.
- **ON15** The sign after '1' depends on the sign before it (MI).
- **ON16** Lines with '1' are on one object only more often than lines with '2' or '3' (F).
- **ON17** Signs counted with '1' and signs counted with '2' overlap in at most 30% of their types.
- **ON18** B: ON2 holds.
- **ON19** B: ON3 holds.
- **ON20** In formulas, 50%+ of '1' tokens directly precede a non-numeral.

## Results of the ninety-fifth set (added after the test; `predict_test95.py`, `results/predict_test95.md`)

Seven held, thirteen failed: '1' is mostly an ordinary count, with two special uses. Special: '1' directly follows an
ending 21 times against never for '2' or '3' (ON3: 13% against 0%), and there it opens a short tail that ends the line
within two signs (ON14: 16 of 21); and after a heading only 820 takes '1' (ON4: 14 of 14). Otherwise '1' behaves like
the other strokes: it counts in formulas (ON20: 65% before a sign), follows a word (ON5: 82%), sits in fixed phrases
like any sign (ON15), and counts a different set of things from '2' (ON17: 23% shared types). It is not less often
before a sign (ON1, p = 0.06), not more line-final (ON2, p = 0.07; ON18 in B), not after heads more (ON6, the other
way), not a 520 head beyond 3 bodies (ON7), not a seal or Mohenjo-daro sign (ON9, ON10), not a name sign (ON11), and
not rarer next to numerals (ON13). In B '1' is rare (25 tokens) and the post-ending use is barely present (ON19: 1),
so the post-ending '1' depends on the ICIT transcription. Tally, counting parts: 647 held, 740 failed (1387 registered).

# Ninety-sixth set, registered before testing (24 September 2026): how the copper labels are built (twenty hypotheses)

Copper tablets (TAB:C) with motif as in the ninety-fourth set. Seen before registering (descriptive listing): labels
per picture, e.g. anthropomorph '806 845 61 407 850 900 740', hare '235 705 33 845 407 321 407', elephant '706 33 923
740 (1)', tiger '798 240 845 61 407', 'Loop' '415 220 845 407', 'Othr' '503 615 752 740' x28, buffalo '255 435 690
740 900 (1) 3 42x'. Distinct texts unless stated; seals and their motifs from F. p < 0.05.

- **LB1** 70%+ of distinct copper texts containing 407 have 845 before it.
- **LB2** 70%+ of copper tablets with '845 ... 407' have an animal or figure motif (not 'Othr', not none).
- **LB3** 90%+ of copper tablets with '705/706 33' have an animal or figure motif.
- **LB4** The elephant label '706 33 923 740' also occurs on a seal.
- **LB5** The 'Othr' label '503 615 752 740' occurs on 5+ seals.
- **LB6** Seals bearing a copper label's text carry that copper tablet's motif in 50%+ (seals with a motif).
- **LB7** 50%+ of signs on 3+ copper tablets have 80%+ of their copper tokens under one motif.
- **LB8** 30%+ of all 845 tokens are on copper tablets.
- **LB9** 20%+ of all 407 tokens are on copper tablets.
- **LB10** Copper lines have '1' directly after 740 more often than seal lines do.
- **LB11** Copper lines with 740 have signs after it more often than seal name lines with 740.
- **LB12** For motifs on 3+ tablets, the commonest label is repeated identically in 60%+ of that motif's tablets on average.
- **LB13** At most two identical labels occur under two or more different motifs.
- **LB14** Copper lines are longer than seal lines (rank test).
- **LB15** 15%+ of distinct copper texts end in 407.
- **LB16** 80%+ of copper tokens of 421, 422, 423, 424 directly follow 3.
- **LB17** 30%+ of copper tablets with no motif carry a text also found on a copper tablet with a motif.
- **LB18** Copper texts found on seals are found on Mohenjo-daro seals more often than Harappa seals.
- **LB19** The anthropomorph label occurs on no seal.
- **LB20** The one-sign copper labels (777, 782) occur on no seal.

## Results of the ninety-sixth set (added after the test; `predict_test96.py`, `results/predict_test96.md`)

Eight held, twelve failed. Copper labels are a vocabulary of their own: 82% of all 845 tokens (LB8: 40 of 49) and 61% of
all 407 tokens (LB9: 76 of 124) are on copper tablets; the labels are copied whole within a picture (LB12: mean 0.63);
'845 ... 407' goes with animal or figure pictures (LB2: 29 of 40); 16% of distinct labels end in 407 (LB15); '3 42x' is a
fixed unit (LB16: 421-424 follow 3 in 11 of 11). The labels almost never occur on seals: not the anthropomorph label
(LB19), not the elephant label (LB4), not the 'Othr' label '503 615 752 740' (LB5: 0; its 28 copies are all copper, so
the seventieth set's 'commonest names' list included copper labels), and only one copper text occurs on any seal (LB6,
LB18). Not supported: 845 always before 407 (LB1: 6 of 16), '705/706 33' only with animals (LB3: 84%), signs bound to
one picture (LB7: 12 of 54), one label per picture (LB13: 5 labels under two or more motifs), copper tails after 740
(LB10, LB11: 24% against 13%, p = 0.06), longer labels (LB14), pictureless tablets repeating pictured labels (LB17: 28%),
and 777/782 being copper-only (LB20: one seal token). Caveat for earlier sets: name counts over F include copper
labels, which inflate repeat counts for a few names (503 615 752 740, 806 845 61 407 850 900 740). Tally, counting
parts: 655 held, 752 failed (1407 registered).

# Ninety-seventh set, registered before testing (24 September 2026): the name findings without copper tablets (twenty hypotheses)

The ninety-sixth set found that name counts over F include copper-tablet labels (e.g. '503 615 752 740' x28, all
copper). Twenty name findings that used F are re-tested with copper tablets (TAB:C) removed. Definitions, tests and
thresholds as in the sets cited; object counts where the original used them. 10,000-draw permutations (1,000 where
the original used 1,000); p < 0.05.

- **XC1** (AM1) Fewer bodies occur at both cities than when sites are shuffled among name tokens.
- **XC2** (AM14) 70%+ of distinct names are on one object only.
- **XC3** (AM15) Bodies on 3+ objects are shorter than bodies on one.
- **XC4** (AM5) Harappa name bodies are shorter than Mohenjo-daro ones.
- **XC5** (AM10) 520 names are a larger share at Harappa than at Mohenjo-daro.
- **XC6** (AM13) Bodies with a numeral are a larger share at Mohenjo-daro than at Harappa.
- **XC7** (PN11) 520 names hold a fish more often than 740 names (name tokens).
- **XC8** (PN13) Distinct seal names are one-off more often than distinct names off seals.
- **XC9** (PN17) In 70%+ of one-off names of 2+ signs, the head heads 5+ distinct names.
- **XC10** (PN18) In one-off names of 3+, the first sign is rare (5 or fewer tokens) more often than the head.
- **XC11** (PN20) A larger share of distinct names repeats at Harappa than at Mohenjo-daro.
- **XC12** (PN5) One-off names share units with one-offs of their own city more than when city labels are shuffled
  (1,000).
- **XC13** (HR1) Head types are seen at both cities more often than opener types.
- **XC14** (HR6) The same within one-off names.
- **XC15** (CS13) Mohenjo-daro distinct names are longer than Harappa's (two-sided rank).
- **XC16** (CS14) Mohenjo-daro name lines carry the heading unit more often than Harappa's (distinct lines).
- **XC17** (CS15) Harappa name lines carry a suffix more often than Mohenjo-daro's (distinct lines).
- **XC18** (MM20) Seal names take 520 more often than names on other objects (distinct).
- **XC19** (CG10) At Mohenjo-daro, 80%+ of heads with 5+ distinct names take one ending in 90%+.
- **XC20** (CG9) The same at Harappa.

## Results of the ninety-seventh set (added after the test; `predict_test97.py`, `results/predict_test97.md`)

Eighteen held, two failed: the name findings survive removing the copper tablets (198 objects). Names stay local (XC1:
31 bodies at both cities, p = 0.0001), 82% one-off (XC2), repeated names short (XC3), Harappa names shorter (XC4: 2.9
against 3.6) and less often counted (XC6: 34% against 44%), 520 names fish names (XC7: 74% against 38%), seal names
one-off (XC8: 86% against 56%), one-off names = rare opener + common head (XC9: 82%; XC10: 14% against 6%), Harappa
repeating names (XC11: 35% against 18%), city-local units (XC12), heads shared and openers local (XC13, XC14), the city
styles (XC15-XC17: Mohenjo-daro longer and headed, Harappa suffixed), and 520 as a seal class (XC18: 18% against 9%).
Two do not survive: Harappa's larger 520 share (XC5: 18% against 16%, p = 0.24; the sixty-ninth set's AM10 was already
borderline at p = 0.043, and copper labels had added Mohenjo-daro 740 names), and the Mohenjo-daro fixed-class count
falls just under its threshold (XC19: 27 of 34, 79%; Harappa XC20: 13 of 16). Tally, counting parts: 673 held, 754
failed (1427 registered).

# Ninety-eighth set, registered before testing (24 September 2026): picture labels across media (twenty hypotheses)

Copper labels (ninety-fourth to ninety-sixth sets) against moulded (TAB:B) and incised (TAB:I) tablets and seals.
Motif as in the ninety-fourth set ('Othr' kept). Text = an object's lines joined. Dated Harappa objects via
rtools.level. 10,000-draw permutations (1,000 where marked); p < 0.05.

Across media
- **XM1** For pictures on both copper and moulded tablets, copper labels share signs with moulded texts of the same
  picture more than of other pictures (mean Jaccard difference, permutation of moulded motifs, 1,000).
- **XM2** The same for incised tablets (1,000).
- **XM3** At most one identical text occurs both on copper and on a moulded tablet.
- **XM4** 30%+ of moulded-tablet motif types also occur on copper.
- **XM5** Copper labels and moulded texts share fewer adjacent-pair types than label-shuffled lines (1,000).
Moulded and incised tablets as picture labels
- **XM6** For moulded motifs on 5+ tablets, the commonest text covers 50%+ on average.
- **XM7** 80%+ of repeated moulded texts with a motif have one motif.
- **XM8** Incised tablets with the same text share the motif more often than when motifs are shuffled.
- **XM9** 90%+ of moulded tablets with a motif are from Harappa.
- **XM10** Moulded tablets with a motif carry a numeral less often than moulded tablets without.
- **XM11** 60%+ of moulded texts with a motif have 1-3 signs.
- **XM12** 'Mult' moulded tablets have longer texts than other moulded tablets with a motif (rank test).
- **XM13** A moulded text-picture pair seen on 2+ dated objects spans both periods in 30%+.
- **XM14** Unicorns are a smaller share of tablet motifs than of seal motifs.
The copper words elsewhere
- **XM15** 50%+ of 845 tokens off copper are on tablets.
- **XM16** 50%+ of 407 tokens off copper are on seals.
- **XM17** Off copper, 845 and 407 share a line more often than chance.
- **XM18** 30%+ of 407 tokens off copper are line-final.
- **XM19** 70%+ of 845 tokens off copper are from Mohenjo-daro.
- **XM20** Off copper, 407 directly follows 845 less often than on copper.

## Results of the ninety-eighth set (added after the test; `predict_test98.py`, `results/predict_test98.md`)

Ten held, ten failed. Picture labels do not carry across media: for the seven pictures found on both copper and moulded
tablets, the copper label shares no more signs with moulded texts of the same picture than of others (XM1: +0.001,
p = 0.41; XM2 incised: p = 0.24); no text occurs on both copper and a mould (XM3: 0); the two media share fewer
adjacent pairs than chance (XM5); and only a quarter of moulded picture types occur on copper (XM4: 7 of 28). Within
each medium the text still follows the picture (XM8 on incised tablets: 114 pairs, p = 0.0001), though moulded
pictures are less tied to one text than copper ones (XM6: mean 0.45; XM7: 75%). Moulded picture tablets count less
than moulded tablets without a picture (XM10: 44% against 57%), and some text-picture pairs span both Harappa periods
(XM13: 7 of 19). Tablet pictures are rarely unicorns (XM14: 11% against 77% on seals). The copper words: off copper, 845
is rare (9 tokens, none on tablets: XM15 fails) but when it occurs 407 is in the same line in 5 of 9 (XM17: 56% against
1%); off-copper 407 is mostly on seals (XM16: 67%) and line-final half the time (XM18); and '845 407' is tighter on copper
(XM20: 25% against 10%). Not supported: moulded pictures all at Harappa (XM9: 77%), short moulded labels (XM11: 44%),
longer 'Mult' texts (XM12), 845 off copper at Mohenjo-daro (XM19: 6 of 9). Tally, counting parts: 683 held, 764
failed (1447 registered).

# Ninety-ninth set, registered before testing (24 September 2026): position specialists (twenty hypotheses)

Distinct lines (A + B) of 2+ signs, copper lines excluded where F is used. For each sign with 10+ tokens: 'initial
share' = share of its tokens that are line-first, 'final share' = line-last. 'Initial specialist' = initial share
0.7+; 'final specialist' = final share 0.7+; 'medial' otherwise. Numerals excluded from the specialist sets.
10,000-draw permutations; p < 0.05.

- **PZ1** Specialists (initial or final) are 20%+ of signs with 10+ tokens.
- **PZ2** Final specialists outnumber initial specialists.
- **PZ3** Initial specialists have more distinct right neighbours per token than medial signs (rank test).
- **PZ4** Final specialists have more distinct left neighbours per token than medial signs (rank test).
- **PZ5** Final specialists are name heads or endings in 70%+.
- **PZ6** Initial specialists include the three heading signs.
- **PZ7** Initial specialists are followed by a numeral more often than medial signs are (tokens).
- **PZ8** Final specialists are preceded by a numeral more often than medial signs are.
- **PZ9** Specialist status agrees between A and B for 80%+ of signs with 10+ tokens in each.
- **PZ10** Specialist status agrees between Mohenjo-daro and Harappa (F) for 70%+ of signs with 10+ tokens at each.
- **PZ11** Final specialists are on tablets more often than medial signs (F tokens).
- **PZ12** Initial specialists are on seals more often than medial signs (F tokens).
- **PZ13** Final specialists are commoner signs than medial signs (rank test on tokens).
- **PZ14** Initial specialists are rarer than medial signs (rank test).
- **PZ15** Lines with an initial specialist are longer than lines without (rank test).
- **PZ16** Lines ending in a final specialist are shorter than lines ending otherwise (rank test).
- **PZ17** The final specialists' final share is higher in formulas than in name lines (pooled tokens).
- **PZ18** 50%+ of final specialists are in the 520 class or are post-name signs (400, 90, 151) or the endings.
- **PZ19** Medial signs are the fish and numeral-adjacent signs: fish are medial in 80%+ of fish types with 10+ tokens.
- **PZ20** B: PZ2 holds.

## Results of the ninety-ninth set (added after the test; `predict_test99.py`, `results/predict_test99.md`)

Nine held, eleven failed. Of 138 non-numeral signs with 10+ tokens, 21 keep one end of the line in 70%+ of tokens
(PZ1: 15%, under 20%): 7 openers (491, 545, 692, 817, 853, 861, 880) and 14 closers (151, 154, 156, 161, 226, 241, 400,
426, 520, 527, 565, 621, 679, 740) (PZ2; PZ20 in B: 6 against 2). Positions are very stable: the same role in A and B
for 62 of 67 signs (PZ9) and at Mohenjo-daro and Harappa for 46 of 51 (PZ10). Openers are followed by a numeral (PZ7:
64% against 13%), i.e. they are heading-type signs, and lines that open with one are longer (PZ15: 5.1 against 4.3);
820 is not among them (it also occurs inside lines), so PZ6 fails. Openers are seal signs (PZ12: 69% against 60%) and
closers tablet signs (PZ11: 39% against 33%). The closers are mostly not name heads (PZ5: 5 of 14) nor 520-class or
suffix signs (PZ18: 4 of 14); besides 740, 520 and 400 they are formula closers (151, 154, 156, 527, 565, 621, 679),
several of which the ninety-first set found in the tails after a mid-line name. Fish are inside signs (PZ19: 8 of 10).
Not supported: openers or closers combining more freely (PZ3, PZ4), closers after numbers (PZ8, the other way),
frequency differences (PZ13, PZ14), shorter closed lines (PZ16), and closers being more final in formulas (PZ17).
Tally, counting parts: 692 held, 775 failed (1467 registered).

# Hundredth set, registered before testing (24 September 2026): variant forms of one sign (twenty hypotheses)

Candidate variant pairs are looked for three ways: by context (cosine of neighbour PMI vectors, sixty-second set,
signs with 10+ tokens in A + B), by catalogue number (signs whose numbers differ by 1, a proxy for shape families in
the ICIT numbering), and known cases (705/706, fish 220/240/233, headings 817/820/861). Site and period from F without
copper. Random baselines draw frequency-matched pairs (10,000, or 1,000 where marked); p < 0.05.

Context twins
- **AL1** The 30 most context-similar pairs differ more in Mohenjo-daro share than random matched pairs.
- **AL2** They co-occur in one line less often than random matched pairs.
- **AL3** They share a Fairservis category more often than random pairs.
- **AL4** They differ more in Harappa period share than random matched pairs.
- **AL5** 5+ of them have one member 80%+ at one city and the other 80%+ at the other.
Known variants
- **AL6** 705 and 706 differ in Mohenjo-daro share (two-sided).
- **AL7** 705 and 706 differ in Harappa period share (two-sided).
- **AL8** 220 and 240 differ in Mohenjo-daro share (two-sided).
- **AL9** 220 and 233 differ in Mohenjo-daro share (two-sided).
- **AL10** 817, 820 and 861 differ by Harappa period (MI).
City-only signs
- **AL11** 10+ signs have 5+ tokens at Mohenjo-daro and none at Harappa.
- **AL12** For such Mohenjo-daro-only signs, the nearest context neighbour is mostly a Harappa sign (50%+ of its F tokens
  at Harappa) in 30%+.
- **AL13** 5+ signs have 5+ tokens in A and none in B.
Neighbouring catalogue numbers
- **AL14** The 30 most context-similar pairs have catalogue numbers within 5 more often than random pairs.
- **AL15** Pairs with numbers differing by 1 are more context-similar than random pairs (rank test).
- **AL16** Pairs with numbers differing by 1 share a line less often than random pairs (1,000).
- **AL17** Pairs with numbers differing by 1 differ more in Mohenjo-daro share than random pairs (1,000).
- **AL18** 10+ number-adjacent pairs have context cosine 0.3+.
- **AL19** B: AL15 holds (contexts from B, signs with 5+ tokens).
- **AL20** F without copper: AL15 holds.

## Results of the hundredth set (added after the test; `predict_test100.py`, `results/predict_test100.md`)

Eight held, twelve failed. Signs next to each other in the catalogue numbering behave alike: pairs whose numbers differ
by 1 are far more context-similar than random pairs (AL15: 0.17 against 0.04; AL19 in B, p = 0.0006; AL20 in F, p =
0.0002), and 12 of the 30 most context-similar pairs have numbers within 5 (AL14, p = 0.001). Since the catalogue
groups signs by shape, shape families share function. The strongest candidates for variant forms of one sign are
435/436 (cosine 0.73), 526/527 (0.61), 336/337 (0.57), 554/555 and 705/706 (AL18: 5 pairs at 0.3+, under the
threshold of 10). But these twins are not regional or period variants: they are not split by city (AL1, AL5: only 347/95
and 636/773) or period (AL4), they co-occur in lines like random pairs (AL2, AL16), and 705/706 are spread alike over
cities and periods (AL6, AL7), as are 220/240 (AL8) and the headings over periods (AL10). The one city split is 233,
commoner at Mohenjo-daro than 220 (AL9: 67% against 53%). Mohenjo-daro has 13 signs with 5+ tokens never seen at
Harappa (AL11), and half of them have a nearest context neighbour that is Harappan (AL12: 6 of 12), a weak sign of local
spellings. 57 signs with 5+ tokens in A never occur in B (AL13): Mahadevan's list merges many of ICIT's signs, which
should be kept in mind for every 'B replication'. AL3 is uninformative (few categorised signs among the pairs).
Tally, counting parts: 700 held, 787 failed (1487 registered).

# Hundred-and-first set, registered before testing (24 September 2026): recent findings on held-out data (twenty hypotheses)

Findings of the eighty-ninth to hundredth sets, found on A + B distinct lines, re-tested on the fuller corpus without
copper tablets (F', distinct lines) and on B alone (bearing in mind that B merges some of A's signs). Definitions as in
the sets cited. 10,000-draw permutations; p < 0.05.

F' (fuller corpus, no copper)
- **RR1** (MX1) 85%+ of medial endings are 740.
- **RR2** (MX8) For 50%+ of medial endings, 'sign before + ending' is a whole 1-sign-body name (F' names).
- **RR3** (MX13) The sign before a medial ending recurs in 30%+ of medial-ending lines.
- **RR4** (HS9) 20%+ of bodies headed 2+ times follow 2+ different heading signs.
- **RR5** (HS8) The sign after the heading (2 or other) depends on the heading sign (MI).
- **RR6** (HS4) 861-headed lines are formulas more often than 817-headed lines.
- **RR7** (ON3) '1' follows 740/520 more often than '2' and '3' do.
- **RR8** (ON4) 90%+ of 'heading + 1' are '820 1'.
- **RR9** (PZ7) Opener specialists are followed by a numeral more often than medial signs.
- **RR10** (PZ12) Opener specialists are on seals more often than medial signs.
- **RR11** (CF4) 60%+ of numerals after 705/706 are 33.
- **RR12** (CF11) 705 and 706 are free variants: the sign before does not choose between them (p >= 0.05).
- **RR13** (FZ10) 3 or more of the frozen pairs 236 = 2, 632 = 2, 717 = 2, 923 = 3 keep their value as the commonest.
- **RR14** (AL15) Signs with numbers differing by 1 are more context-similar than random pairs.
B alone
- **RR15** (HS9) 20%+ of bodies headed 2+ times follow 2+ different heading signs.
- **RR16** (ON4) 90%+ of 'heading + 1' are '820 1'.
- **RR17** (PZ7) Opener specialists are followed by a numeral more often than medial signs.
- **RR18** (MX8) For 50%+ of medial endings, 'sign before + ending' is a whole 1-sign-body name.
- **RR19** (HS4) 861-headed lines are formulas more often than 817-headed lines.
- **RR20** (CF11) 705 and 706 are free variants (p >= 0.05).

## Results of the hundred-and-first set (added after the test; `predict_test101.py`, `results/predict_test101.md`)

Fifteen held, five failed. On the fuller corpus without copper (2,217 distinct lines) nearly everything recent
replicates: medial endings are 740 (RR1: 88%) and close a 1-sign name (RR2: 57%) with a recurring element (RR3: 61%);
heading signs are interchangeable before the same body (RR4: 15 of 17) and differ in the stroke that follows (RR5, p =
0.0001); '1' follows an ending where '2' and '3' never do (RR7: 17 against 0) and only 820 takes '1' after a heading (RR8:
11 of 11); openers precede numerals (RR9: 53% against 16%); numerals after 705/706 are 33 (RR11: 92%) and 705/706 are free
variants (RR12); the four frozen counts keep their values (RR13: 4 of 4); catalogue neighbours share contexts (RR14, p
= 0.03). Not replicated in F': 861 heading formulas more than 817 (RR6: 42% against 36%, p = 0.19) and openers being seal
signs (RR10). In B several tests are degenerate: B has no 817 lines (RR19), writes 705 and 706 as one sign (RR20 holds
trivially), and has only 1 and 3 cases for RR15 and RR16; openers do not precede numerals in B (RR17) and 'X 740' before a
medial ending is a name in 48% (RR18, just under 50%). Tally, counting parts: 715 held, 792 failed (1507 registered).

# Hundred-and-second set, registered before testing (24 September 2026): shape blocks and what they do (twenty hypotheses)

The hundredth set found that catalogue neighbours behave alike. 'Block' = the catalogue number's hundreds digit
(0-9; block 0 holds most stroke numerals). Non-numeral signs only unless stated. Roles (opener, closer, medial) as in the
ninety-ninth set; classes as in the eighty-first; categories from cat_of. Distinct lines and names (A + B) unless
stated. 10,000-draw permutations; p < 0.05.

- **SB1** Positional role depends on block (MI over signs with 10+ tokens).
- **SB2** Name-line share of a sign's tokens depends on block (MI over tokens: block against name/formula).
- **SB3** Being counted (directly after a numeral) depends on block (MI over tokens).
- **SB4** A head's class depends on block (MI over classed heads).
- **SB5** Seal against tablet depends on block (F tokens without copper, MI).
- **SB6** Mohenjo-daro against Harappa depends on block (F tokens, MI).
- **SB7** Two blocks cover 50%+ of name-head tokens.
- **SB8** 80%+ of block-2 fish signs with 10+ tokens are medial (not specialists).
- **SB9** Block-7 tokens are counted more often than other non-numeral tokens.
- **SB10** Block-8 signs are specialists (opener or closer) more often than other signs.
- **SB11** Block-1 tokens are the last body sign more often than other body tokens.
- **SB12** Adjacent signs are from the same block less often than in within-line shuffles (1,000).
- **SB13** Opener and head of 2+-sign bodies are from different blocks more often than when heads are shuffled.
- **SB14** The ending depends on the head's block (MI over distinct names).
- **SB15** A block's majority role (opener, closer, medial) is the same in A and B for 80%+ of blocks.
- **SB16** Fairservis category predicts positional role (MI over categorised signs).
- **SB17** Fairservis category predicts being counted (MI over tokens of categorised signs).
- **SB18** Block-3 tokens are in formulas more often than other non-numeral tokens.
- **SB19** Block-5 tokens are the last body sign more often than block-3 tokens.
- **SB20** Block-9 signs have fewer tokens than other signs (rank test).

## Results of the hundred-and-second set (added after the test; `predict_test102.py`, `results/predict_test102.md`)

Eleven held, nine failed. The catalogue's hundreds block (a rough shape family) carries information about use: genre
(SB2: name against formula, p = 0.0001), being counted (SB3), a head's class (SB4: 0.25 bits over 70 heads, p = 0.002),
the ending (SB14, p = 0.0001), seal against tablet (SB5), and city (SB6), all weak but significant. Block 1 signs are
name heads (SB11: 63% last in the body against 31%) and block 3 signs are formula signs (SB18: 58% against 38%); fish
(block 2) are medial (SB8: 8 of 10); the category also predicts counting (SB17). But the block does not fix position
(SB1, p = 0.06; SB16 by category, p = 0.07), heads are spread over four blocks (SB7: blocks 7, 1, 2, 4 about equal),
block 7 is counted less, not more (SB9: 11% against 17%), block 8 is not the ends (SB10), block 5 heads less than block
3 (SB19, reverse), and block 9 is not rarer (SB20). Same-block signs stand next to each other more, not less, than
shuffles give (SB12: 928 adjacent pairs, the reverse of the prediction; e.g. fish beside fish), and opener and head are
not from different blocks more than chance (SB13). SB15 (block roles agree in A and B, 7 of 7) holds trivially since
every block's majority role is 'medial'. Tally, counting parts: 726 held, 801 failed (1527 registered).

# Hundred-and-third set, registered before testing (24 September 2026): the formula closers (twenty hypotheses)

'Closers' = the ninety-ninth set's final specialists other than 740, 520 and 400: 151, 154, 156, 161, 226, 241, 426,
527, 565, 621, 679. 'Closer line' = a distinct line (A + B) of 2+ signs ending in a closer. Name bodies, heads and
embedding as before; F without copper for object and site tests; motif as in the sixty-seventh set. 10,000-draw
permutations; p < 0.05.

- **FX1** 80%+ of closer lines are formulas (no 740/520).
- **FX2** 20%+ of closer tokens directly follow a numeral.
- **FX3** 10%+ of closer tokens directly follow 740 or 520.
- **FX4** Closer lines are shorter than other formulas (rank test).
- **FX5** 60%+ of closer tokens are on seals (F).
- **FX6** Closer lines are a larger share of lines at Mohenjo-daro than at Harappa (F).
- **FX7** The sign before a closer depends on which closer (MI).
- **FX8** Under 3% of lines hold two different closers.
- **FX9** Closer lines embed an attested name body more often than other formulas.
- **FX10** Closer lines open with a heading sign more often than other formulas.
- **FX11** Closer lines hold a numeral less often than other formulas.
- **FX12** 50%+ of 156 tokens directly follow a numeral.
- **FX13** The sign before a closer is a name head in 50%+.
- **FX14** Closers' left-neighbour sets overlap little: mean pairwise Jaccard 0.2 or less (closers with 5+ tokens).
- **FX15** Closer texts recur on 2+ objects more often than other formula texts (F).
- **FX16** Seal closer lines are on unicorn seals less often than other seal lines (F).
- **FX17** 5+ of the closers have 5+ tokens in B.
- **FX18** B: FX1 holds.
- **FX19** F without copper: FX1 holds.
- **FX20** 80%+ of closer lines have 2-4 signs.

## Results of the hundred-and-third set (added after the test; `predict_test103.py`, `results/predict_test103.md`)

Eleven held, nine failed. 284 distinct lines end in one of the 11 closers (151, 154, 156, 161, 226, 241, 426, 527, 565,
621, 679). 80% of them have no 740/520 (FX1; FX18 in B: 81%; FX19 in F: 82%), yet they are not short counting formulas:
they are seal texts (FX5: 80% of closer tokens on seals), commoner at Mohenjo-daro (FX6: 12% against 7% of lines),
longer than other formulas (FX4 fails: 4.3 against 3.7 signs; FX20: only 58% have 2-4 signs), and the sign before the
closer is a name-head sign in 67% (FX13). Each closer has its own set of preceding signs (FX7: 2.2 bits, p = 0.0001;
FX14: mean Jaccard 0.07 between closers), and a line never holds two (FX8: 3 of 2,722). 12% of closer tokens follow
740/520 directly (FX3). They do not differ from other formulas in citing names (FX9), heading (FX10), numerals (FX11)
or recurrence (FX15, the other way), 156 is counted in only 33% (FX12), and they are not less often on unicorns (FX16).
Reading: a second family of seal inscriptions at Mohenjo-daro, 'name-like body + closer' in place of 'body + 740/520',
with each closer taking its own heads. This partly restores the fifty-fifth set's alternative-closer idea (withdrawn in
the fifty-seventh set, which required the remainder to be an attested name body): the bodies before closers are
name-like in their heads but mostly not attested names. Tally, counting parts: 737 held, 810 failed (1547 registered).

# Hundred-and-fourth set, registered before testing (24 September 2026): line templates (twenty hypotheses)

Each distinct line becomes a role string: H = heading sign (817, 820, 861) in first place; N = a numeral run; E = 740
or 520; S = 400, 90 or 151 directly after E; C = a closer (hundred-and-third set); F = a fish sign; X = any other sign,
with runs of X merged into one X. 'Template' = that string. Distinct lines (A + B) unless stated; F without copper for
object, site and period tests. 10,000-draw permutations; p < 0.05.

- **TP1** The ten commonest templates cover 50%+ of distinct lines.
- **TP2** The template depends on seal against tablet (MI, F).
- **TP3** The template depends on the city (MI, F).
- **TP4** A's and B's five commonest templates share 4+.
- **TP5** 'XE' is the commonest template on seals (F).
- **TP6** 'NX' is the commonest template on tablets (F).
- **TP7** 90%+ of templates starting with H continue with N.
- **TP8** In 90%+ of lines containing E, E is followed only by S or the line end.
- **TP9** 50%+ of lines with C have the template 'XC'.
- **TP10** Template entropy is higher at Mohenjo-daro than at Harappa (label permutation).
- **TP11** Template entropy is higher on seals than on tablets.
- **TP12** Copper lines use fewer distinct templates per line than seal lines.
- **TP13** In 'NX' lines the numeral value is 2-4 in 70%+.
- **TP14** Under 2% of lines hold both E and C.
- **TP15** Under 10% of lines hold two or more N segments.
- **TP16** At Harappa the template does not depend on the period (MI p >= 0.05).
- **TP17** 80%+ of graffiti lines have no E.
- **TP18** F without copper: TP1 holds.
- **TP19** B: TP1 holds.
- **TP20** 70%+ of F lines with a template starting 'HN' and containing E are from Mohenjo-daro.

## Results of the hundred-and-fourth set (added after the test; `predict_test104.py`, `results/predict_test104.md`)

Nine held, eleven failed. Reduced to role strings, 2,722 distinct lines use 391 templates; the commonest are X (344),
XE (252), XNX (155), NX (131), XNXE (88), HNXE (80), XC (77), XES (67), HNX (64), XN (63), FXE (52), NXE (51). The ten
commonest cover 49% (TP1, just under half; TP18 in F: 51%; TP19 in B: 54%), and A's and B's top five share four (TP4).
Templates depend on medium (TP2) and city (TP3); Mohenjo-daro and seals use a wider range of them (TP10: +0.67 bits;
TP11: +1.30 bits). Lines rarely hold two numbers (TP15: 8%), and graffiti are rarely names (TP17: 86% without E). Not
supported: 'XE' leading on seals and 'NX' on tablets (TP5, TP6: plain 'X' leads both, since distinct lines collapse the
repeated count tokens); 'H' always followed by N (TP7: 82%); E always final (TP8: 87%; the mid-line endings of the
ninety-first set); 'XC' as the closer template (TP9: 22%; closers take many shapes); copper using fewer templates (TP12,
reverse: fixed labels are few lines, not few shapes); 'NX' being 2-4 counts (TP13: 65%); E and C excluding each other
(TP14: 65 lines, 2.4%); templates stable over Harappa periods (TP16: p = 0.0001, they change); and headed names being
Mohenjo-daran (TP20: 68%, just under). Tally, counting parts: 746 held, 821 failed (1567 registered).

# Hundred-and-fifth set, registered before testing (24 September 2026): closer inscriptions against name inscriptions (twenty hypotheses)

From the hundred-and-third set: 'closer lines' end in one of 151, 154, 156, 161, 226, 241, 426, 527, 565, 621, 679 and
mostly have no 740/520. 'Closer body' = the signs before the closer (heading unit removed); 'name body' as before.
Distinct lines and bodies (A + B); F without copper for site, object, motif tests. Units as in the sixty-first set.
10,000-draw permutations; p < 0.05.

- **CB1** Closer bodies (2+ signs) end in a sign that also heads names in 60%+.
- **CB2** 20%+ of closer bodies are also attested name bodies.
- **CB3** Closer bodies are shorter than name bodies (rank test).
- **CB4** Closer bodies of 2+ signs contain a unit as often as name bodies (two-sided p >= 0.05).
- **CB5** The last body sign before a closer depends on the closer (MI).
- **CB6** Heads shared by closer bodies and name bodies take 740 in 90%+ of their names.
- **CB7** Closer lines carry the heading unit less often than name lines.
- **CB8** Closer seal lines are on unicorn seals as often as name seal lines (two-sided p >= 0.05).
- **CB9** Closer lines at Mohenjo-daro are a larger share of seal inscriptions than at Harappa (F seals).
- **CB10** Closer bodies hold a fish less often than name bodies.
- **CB11** Closer bodies hold a numeral as often as name bodies (two-sided p >= 0.05).
- **CB12** The opener of closer bodies depends on the closer (MI).
- **CB13** Closer bodies share openers with name bodies in 60%+ of closer-body opener types.
- **CB14** Closer-line texts are on one object only more often than name-line texts (F).
- **CB15** Closer lines are commoner in the earlier Harappa period (F, Harappa seals and tablets with a period).
- **CB16** 156 and 527 lines differ in site (two-sided).
- **CB17** The sign before the closer is a 520-class head less often than the sign before 520 in names.
- **CB18** In 12%+ of closer lines a 740/520 stands directly before the closer (name + closer).
- **CB19** B: CB5 holds.
- **CB20** B: CB1 holds.

## Results of the hundred-and-fifth set (added after the test; `predict_test105.py`, `results/predict_test105.md`)

Thirteen held, seven failed. Closer inscriptions are a sister type of the name inscriptions on the same seals. Their
bodies end in signs that also head names (CB1: 75%), use the name openers (CB13: 71% of opener types), count like names
(CB11: 46% against 47%), are one-off (CB14: 87% against 81%), are rarely headed (CB7: 12% against 17%) and sit on the
same animals (CB8: 81% against 80% unicorn). Each closer selects both its heads (CB5: 2.2 bits; CB19 in B, p = 0.0001) and
its openers (CB12, p = 0.001). But the bodies are not the attested names (CB2: 14%), are shorter (CB3: 3.2 against 3.7),
use the recurring name units less (CB4: 41% against 61%), hold fish less (CB10: 33% against 44%), and almost never
follow a 520-class head (CB17: 7% against 85% for 520 names), so closers pair with the 740 side of the head inventory
(CB6: 32 of 39 shared heads are 740-class, 82%, under 90%). 13% of closer lines are 'name + ending + closer' (CB18).
Revision of the hundred-and-third set: as a share of seal inscriptions, closers are as common at Harappa as at
Mohenjo-daro (CB9: 19% and 20%; FX6 compared all lines, where Harappa's many tablets dilute the share). Not supported:
earlier date (CB15), a site split between 156 and 527 (CB16), and CB1 in B (CB20: 47%). Tally, counting parts: 759
held, 828 failed (1587 registered).

# Hundred-and-sixth set, registered before testing (24 September 2026): bare lines (twenty hypotheses)

'Bare line' = a distinct line (A + B) whose template (hundred-and-fourth set) is 'X': 2+ signs with no heading in first
place, no numeral, no 740/520, no closer, no fish. Seen before registering: 344 such lines, mostly 2-3 signs, commonest
last signs 400 (50), 368 (17), 595 (16), 390 (16), 615 (10). Name lines, bodies, heads and openers as before; roles as
in the ninety-ninth set; F without copper for object, site and period tests. 10,000-draw permutations; p < 0.05.

- **XL1** Bare lines are shorter than name lines (rank test).
- **XL2** 10%+ of bare lines end in 400.
- **XL3** In 30%+ of bare lines ending in 400, the signs before 400 are an attested name body.
- **XL4** Bare lines are on tablets more often than name lines (F).
- **XL5** Bare lines are a larger share of lines at Harappa than at Mohenjo-daro (F).
- **XL6** The last sign of a bare line is a name head in 50%+.
- **XL7** The first sign of a bare line is a name opener in 50%+.
- **XL8** 20%+ of 2-sign bare lines are attested 2-sign name bodies.
- **XL9** Bare texts recur on 2+ objects more often than name texts (F).
- **XL10** Bare lines are on potsherds more often than name lines (F).
- **XL11** Bare-line tokens are formula-only signs more often than name-line tokens.
- **XL12** 30%+ of bare lines end in a final specialist.
- **XL13** 10%+ of bare lines end in 368 or 595.
- **XL14** 368 directly follows a name-head sign in 60%+ of its tokens.
- **XL15** 595 is line-final in 60%+ of its tokens.
- **XL16** Bare seal texts are one-off more often than name seal texts (F).
- **XL17** At Harappa, bare lines are commoner in the earlier period (F).
- **XL18** Bare lines end in 400 more often at Harappa than at Mohenjo-daro (F).
- **XL19** B: XL1 holds.
- **XL20** B: XL8 holds.

## Results of the hundred-and-sixth set (added after the test; `predict_test106.py`, `results/predict_test106.md`)

Ten held, ten failed. The 344 bare lines (no heading, numeral, ending, closer or fish) are short (XL1: 2.9 against 5.0
signs; XL19 in B: 2.7 against 4.4) and built like names without an ending: they start with a name opener in 76% (XL7)
and end in a name head in 70% (XL6). But they are not the attested names with the ending dropped: only 7% of 2-sign
bare lines are attested name bodies (XL8; XL20 in B: 7%), and bare '... 400' lines are not 'name + 400' (XL3: 3 of 50).
They are a practical genre: on tablets (XL4: 32% against 23%) and potsherds (XL10: 9% against 2%) more than names,
somewhat commoner at Harappa (XL5: 15% against 12%), and they hold formula-only signs (XL11: 11% of tokens against
0.1% in name lines). 15% end in 400 (XL2), and 368 follows a name-head sign in 68% of its tokens (XL14). Not supported:
recurring more (XL9), one-off seal texts (XL16), an earlier date (XL17), 400 as a Harappa bare-line ending (XL18), and
the stricter closer tests (XL12: 15%; XL13: 10%, just under; XL15: 595 line-final in 38%). Tally, counting parts: 769
held, 838 failed (1607 registered).

# Hundred-and-seventh set, registered before testing (24 September 2026): sets 102-106 on held-out data (twenty hypotheses)

Findings of the hundred-and-second to hundred-and-sixth sets, found on A + B distinct lines, re-tested on F without
copper (F', distinct lines), the smaller sites (OS, F' outside Mohenjo-daro and Harappa) and B. Definitions as in the
sets cited (closers, bodies, blocks, templates, bare lines). 10,000-draw permutations (1,000 where marked); p < 0.05.

F'
- **RH1** (SB11) Block-1 body tokens are the last body sign more often than other body tokens.
- **RH2** (SB18) Block-3 tokens are in formulas more often than other non-numeral tokens.
- **RH3** (SB12, observed direction) Adjacent signs share a block more often than in within-line shuffles (1,000).
- **RH4** (FX13) 50%+ of closer tokens follow a name-head sign.
- **RH5** (FX7) The sign before a closer depends on the closer (MI).
- **RH6** (FX8) Under 3% of lines hold two different closers.
- **RH7** (CB10) Closer bodies hold a fish less often than name bodies.
- **RH8** (CB17) Closers follow a 520-class head less often than 520 does.
- **RH9** (TP15) Under 10% of lines hold 2+ numeral segments.
- **RH10** (TP4) F's five commonest templates share 4+ with A + B's.
- **RH11** (XL1) Bare lines are shorter than name lines.
- **RH12** (XL6) 50%+ of bare lines end in a name head.
- **RH13** (XL7) 50%+ of bare lines start with a name opener.
- **RH14** (XL11) Bare-line tokens are formula-only signs more often than name-line tokens.
- **RH15** (XL14) 60%+ of 368 tokens follow a name-head sign.
Smaller sites
- **RH16** (CB9) Closer lines are 10%+ of seal inscriptions (closer or name lines on seals).
- **RH17** (XL1) Bare lines are shorter than name lines.
- **RH18** (XL7) 50%+ of bare lines start with a name opener.
B
- **RH19** (SB11) Block-1 body tokens are the last body sign more often than other body tokens.
- **RH20** (CB10) Closer bodies hold a fish less often than name bodies.

## Results of the hundred-and-seventh set (added after the test; `predict_test107.py`, `results/predict_test107.md`)

All twenty held. On the fuller corpus without copper (2,116 distinct lines): block 1 is a head block (RH1: 49% against
27%) and block 3 a formula block (RH2: 61% against 39%); same-family signs cluster (RH3, p = 0.001); closers follow
name-head signs (RH4: 66%), each with its own partners (RH5, p = 0.0001), one per line (RH6: 2 lines), with fewer fish
(RH7: 35% against 44%) and almost never after a 520-class head (RH8: 7% against 83%); lines rarely hold two numbers (RH9:
8%); four of the top five templates are the same (RH10); bare lines are short (RH11), name-shaped (RH12: 57% end in a
head; RH13: 61% start with an opener) and full of formula-only signs (RH14: 20% of tokens against 0.1%); 368 follows a
head (RH15: 66%). At the smaller sites closer inscriptions are a quarter of seal inscriptions (RH16: 42 of 168), and
bare lines are short (RH17) and name-shaped (RH18: 63%). In B, block 1 heads (RH19: 51% against 33%) and closer bodies
avoid fish (RH20: 26% against 40%). Tally, counting parts: 789 held, 838 failed (1627 registered).

# Hundred-and-eighth set, registered before testing (24 September 2026): the four genres as systems (twenty hypotheses)

Genre of a distinct line (A + B): 'name' (name_of gives a name), 'closer' (ends in a closer, no 740/520), 'count' (a
formula with a numeral), 'bare' (template X), else 'other'. F without copper for object, site and period tests.
'Genre-specific sign' = a non-numeral sign with 10+ tokens, 70%+ of them in one genre. 10,000-draw permutations; p < 0.05.

- **GS1** 30%+ of signs with 10+ tokens are genre-specific.
- **GS2** Genre-specific signs exist for all four genres.
- **GS3** Genre depends on object type (MI; seal, TAB:I, TAB:B, potsherd, other).
- **GS4** Genre depends on the city (MI).
- **GS5** At Harappa, genre depends on the period (MI).
- **GS6** Name and closer lines share sign types more than name and count lines do (Jaccard over types).
- **GS7** Bare and count lines share sign types more than bare and name lines do.
- **GS8** Line length depends on genre (MI over length strata).
- **GS9** Genre depends on the first sign (MI over first signs with 5+ lines).
- **GS10** Genre depends on the last sign more than on the first sign (MI larger, both significant).
- **GS11** On objects with 2+ lines, the lines' genres agree more often than when genres are shuffled among those lines
  (F).
- **GS12** Seals carry names or closers in 70%+ of their lines (F).
- **GS13** Incised tablets carry counts or bare lines more often than moulded tablets (F).
- **GS14** Potsherd lines are bare or count lines in 70%+ (F).
- **GS15** Genre shares at the smaller sites match the two cities' (MI site-group against genre p >= 0.05).
- **GS16** Genre-specific signs are rarer (fewer tokens) than shared signs (rank test).
- **GS17** Count-specific signs are block 3 or block 1 more often than other genre-specific signs.
- **GS18** B: GS1 holds.
- **GS19** B: GS8 holds.
- **GS20** F': GS1 holds.

## Results of the hundred-and-eighth set (added after the test; `predict_test108.py`, `results/predict_test108.md`)

Seven held, thirteen failed, and the failures are informative: the genres are frames, not vocabularies. Of 2,722
distinct lines, 1,233 are names, 605 counts, 344 bare, 228 closer lines, 312 other. Only 15% of signs with 10+ tokens
keep 70% of their tokens in one genre (GS1; B 9%, GS18; F' 27%, GS20), almost all of them name signs; there is one
count-specific sign and no bare-specific sign (GS2). Closer lines share fewer sign types with names than counts do
(GS6: Jaccard 0.32 against 0.43), and bare lines are nearer counts than names (GS7: 0.45 against 0.39). What decides the
genre is the frame: the last sign carries far more information about it than the first (GS10: 1.34 against 0.39
bits), length differs by genre (GS8; GS19 in B), and object (GS3) and city (GS4) shift the mix slightly. Genre does not
change between Harappa periods (GS5), lines on one object do not share a genre (GS11: 15 of 76), seals are 59% names or
closers (GS12, under 70%), incised and moulded tablets carry counts and bare lines alike (GS13), potsherds are only 48%
bare or count (GS14), the smaller sites' mix differs (GS15, p = 0.0001), and genre signs are not rarer (GS16).
Tally, counting parts: 796 held, 851 failed (1647 registered).

# Hundred-and-ninth set, registered before testing (24 September 2026): the bare-line closers (twenty hypotheses)

Bare lines (hundred-and-sixth set) end most often in 400, 368, 595, 390 and 615. Here each is looked at across all
distinct lines (A + B) unless stated. 'Bare 400' = 400 not directly after 740/520. Name heads as before; F without
copper (F') for object and site tests, F with copper where stated. 10,000-draw permutations; p < 0.05.

- **BC1** 50%+ of 368 tokens are line-final.
- **BC2** 50%+ of 390 tokens directly follow a numeral.
- **BC3** 30%+ of 595 tokens directly follow 95.
- **BC4** 30%+ of 615 tokens stand next to another 615.
- **BC5** 50%+ of bare-400 tokens directly follow a name-head sign.
- **BC6** 60%+ of bare-400 lines are on tablets (F').
- **BC7** 70%+ of 368 lines are on seals (F').
- **BC8** The signs before 368 and before 740 overlap little (Jaccard 0.3 or less).
- **BC9** 10%+ of 368 tokens directly follow a heading sign.
- **BC10** 90%+ of the numerals directly before 390 are worth 3 or more.
- **BC11** 70%+ of 390 lines are on seals (F').
- **BC12** 70%+ of 615 tokens are medial (neither first nor last).
- **BC13** Lines with 615 hold a numeral more often than other lines.
- **BC14** Four signs cover 40%+ of the signs directly before bare 400.
- **BC15** The signs before bare 400 and before '740 400' overlap little (Jaccard 0.3 or less).
- **BC16** 30%+ of 595 tokens are on copper tablets (F with copper).
- **BC17** 368 lines are a larger share of lines at Mohenjo-daro than at Harappa (F').
- **BC18** B: BC1 holds.
- **BC19** B: BC4 holds.
- **BC20** F': BC12 holds.

## Results of the hundred-and-ninth set (added after the test; `predict_test109.py`, `results/predict_test109.md`)

Eight held, twelve failed. The bare-line closers are not one class; each has its own use. 368 is a seal sign (BC7: 82%
of its lines) that follows a heading sign in 28% of tokens (BC9; the '817/861 + 368' heading variant of the
eighty-ninth set) and otherwise takes words 740 does not take (BC8: Jaccard 0.14); it is line-final in only 34% (BC1;
B 42%, BC18) and not Mohenjo-daran (BC17). 390 is a seal sign (BC11: 81%) counted with 3 or more when counted (BC10: 61
of 67), though it follows a numeral in only 30% of tokens (BC2). 615 is the doubled sign (BC4: 75% next to another 615;
BC19 in B: 72%), medial in 61% (BC12; F' 64%, BC20), and not more numerical (BC13). Bare 400 is a different 400 from the
post-name 400: they follow almost disjoint sets of signs (BC15: Jaccard 0.09); bare 400 follows many signs (BC14: top
four 156, 90, 158, 400 cover 22%), a name head in 45% (BC5), and is on tablets in only half its lines (BC6). 595 does not
follow 95 (BC3) and is not a copper word (BC16: 12%). Tally, counting parts: 804 held, 863 failed (1667 registered).

# Hundred-and-tenth set, registered before testing (24 September 2026): sets 108-109 on held-out data (twenty hypotheses)

Findings of the hundred-and-eighth and hundred-and-ninth sets (found on A + B distinct lines) re-tested on F without
copper (F', distinct lines), the smaller sites (OS) and B. Genres and definitions as in those sets. 10,000-draw
permutations; p < 0.05.

Genres as frames
- **RG1** F': bare lines share more sign types with counts than with names (GS7).
- **RG2** F': the last sign tells the genre more than the first (GS10).
- **RG3** F': the first sign tells the genre (GS9).
- **RG4** B: GS10 holds.
- **RG5** B: GS7 holds.
- **RG6** OS: GS10 holds.
- **RG7** OS: under 30% of signs with 5+ tokens are genre-specific (shared vocabulary).
- **RG8** F': the genre sets the length (GS8).
- **RG9** OS: GS8 holds.
The closers
- **RG10** F': 30%+ of 615 tokens stand next to 615 (BC4).
- **RG11** F': the signs before 368 and before 740 overlap at Jaccard 0.3 or less (BC8).
- **RG12** F': 10%+ of 368 tokens follow a heading sign (BC9).
- **RG13** F': 90%+ of numerals before 390 are worth 3+ (BC10).
- **RG14** F': the signs before bare 400 and before '740 400' overlap at 0.3 or less (BC15).
- **RG15** B: BC8 holds.
- **RG16** B: BC15 holds.
- **RG17** B: BC10 holds.
- **RG18** B: BC9 holds.
- **RG19** OS: 70%+ of 390 lines are on seals (BC11).
- **RG20** OS: 30%+ of 615 tokens stand next to 615 (BC4).

## Results of the hundred-and-tenth set (added after the test; `predict_test110.py`, `results/predict_test110.md`)

Eighteen held, two failed. The genres-as-frames findings replicate: the last sign tells the genre far more than the
first in F' (RG2: 1.30 against 0.39 bits), B (RG4: 1.36 against 0.56) and the smaller sites (RG6: 1.28 against 0.39);
the first sign still tells something (RG3); genre sets line length in F' and at the smaller sites (RG8, RG9); the
smaller sites also share one vocabulary across genres (RG7: 25% genre-specific); and bare lines are nearer counts than
names in F' (RG1: 0.39 against 0.34), though not in B (RG5: 0.56 against 0.56). The closer findings replicate too: 615
is the doubled sign (RG10: 74%; RG20 small sites: 6 of 9), 368 takes other words than 740 (RG11: 0.12; RG15 in B: 0.10)
and follows a heading in about 30% (RG12, RG18), 390 is counted 3+ (RG13: 93% in F'; RG17 in B: 83%, under 90%) and is a
seal sign at the smaller sites (RG19: 78%), and the two uses of 400 have almost disjoint predecessors (RG14: 0.08; RG16
in B: 0.12). Tally, counting parts: 822 held, 865 failed (1687 registered).

# Hundred-and-eleventh set, registered before testing (24 September 2026): one sign, many genres (twenty hypotheses)

The genres share one vocabulary (hundred-and-eighth set). If a sign keeps its function across genres, its behaviour
should carry over. Genres as in the hundred-and-eighth set; distinct lines (A + B). For a sign: 'relative position'
= mean of i/(len-1) over its tokens in lines of 2+; 'right company' = its right-neighbour distribution. Signs with 5+
tokens in each genre compared. Correlations are Spearman with permutation p; 10,000 draws; p < 0.05.

Position carries over
- **OG1** Relative positions in names and in counts correlate (Spearman 0.3+, significant).
- **OG2** Relative positions in names and in closer lines correlate (0.3+).
- **OG3** Relative positions in names and in bare lines correlate (0.3+).
- **OG4** Relative positions in counts and in bare lines correlate (0.3+).
- **OG5** Name heads (last body sign in 50%+ of name tokens) are line-final in bare lines more often than other signs.
- **OG6** Name openers (first body sign in 50%+ of name tokens) are line-first in counts more often than other signs.
Company carries over
- **OG7** A sign's right company in names is closer (Jensen-Shannon) to its right company in counts than to a random
  other sign's company in counts (sign test over signs).
- **OG8** The same for left company.
- **OG9** Adjacent pairs found in names recur in counts more often than pairs made by shuffling names' signs (1,000).
- **OG10** Units (sixty-first set) occur in counts more often than random pairs of name signs.
- **OG11** The two members of a unit keep their order in counts in 90%+ of unit occurrences there.
Numbers carry over
- **OG12** Signs counted in both names and counts are counted with the same numeral kind in 60%+ (commonest kind).
- **OG13** The value before a sign in names correlates with its value in counts (Spearman over signs, 0.3+).
- **OG14** Fish are counted in counts as well as in names (share of fish tokens after a numeral 10%+ in counts).
Class carries over
- **OG15** 520-class heads end bare lines more often than 740-class heads do.
- **OG16** 740-class heads precede closers more often than 520-class heads do (CB17 as a class contrast).
Replication
- **OG17** B: OG1 holds.
- **OG18** B: OG9 holds.
- **OG19** F without copper: OG1 holds.
- **OG20** F without copper: OG7 holds.

## Results of the hundred-and-eleventh set (added after the test; `predict_test111.py`, `results/predict_test111.md`)

Seventeen held, three failed: signs keep their function across genres. A sign's position in the line correlates
between names and counts (OG1: 0.49; OG17 in B: 0.44; OG19 in F': 0.58), names and closer lines (OG2: 0.49), counts and
bare lines (OG4: 0.34), though only weakly between names and bare lines (OG3: 0.21, p = 0.08). A sign's right and left
company in counts is closer to its own company in names than to another sign's (OG7: 65 against 9; OG8: 62 against 15;
OG20 in F': 44 against 12). Name pairs recur in counts beyond chance (OG9; OG18 in B), the recurring name units occur in
counts (OG10: 343) in their name order (OG11: 91%), a sign's numeral kind (OG12: 52 of 78) and typical count (OG13: 0.52)
carry over from names to counts, and fish are counted in counts too (OG14: 52%). Name heads end bare lines (OG5: 54%
against 30%) and closers follow 740-class heads rather than 520-class ones (OG16: 3.8% against 1.6%). Not supported:
name openers opening counts (OG6, p = 0.057) and the 520 class ending bare lines (OG15: 4 tokens). This qualifies the
seventy-seventh set's 'two systems' (LX10-LX12): names and counts favour different pairs, but each sign keeps its own
place, company, notation and count across both, so they are two uses of one language rather than two codes.
Tally, counting parts: 839 held, 868 failed (1707 registered).

# Hundred-and-twelfth set, registered before testing (24 September 2026): the number system across genres (twenty hypotheses)

Numeral signs and their (value, kind) from numerals.NUMS; a 'run' = consecutive numeral signs, its value their sum.
Genres as in the hundred-and-eighth set. Distinct lines (A + B) unless stated; F without copper (F') for object tests.
10,000-draw permutations; p < 0.05.

- **NS1** In names, numerals of value 5-8 are tiered more often than those of 1-4.
- **NS2** The same in counts.
- **NS3** The same in closer lines.
- **NS4** Run value depends on genre (MI; values capped at 8).
- **NS5** Numeral kind depends on genre (MI).
- **NS6** In closer lines, 70%+ of numeral runs stand inside the body (not directly before the closer).
- **NS7** Value 3 is the commonest run value in names, in counts and in closer lines.
- **NS8** Runs of value 5+ are rarer in counts than in names.
- **NS9** 5%+ of runs in counts have 2+ numeral signs.
- **NS10** In 2-sign runs, the larger value comes first in 70%+.
- **NS11** Every numeral sign with 10+ tokens occurs in 2+ genres.
- **NS12** In counts, tiered numerals are on seals more often than on tablets (F').
- **NS13** In names, long numerals stand directly before the head more often than short numerals do.
- **NS14** The short stroke '2' is the commonest numeral sign.
- **NS15** Runs worth 1 are rarer than runs worth 2.
- **NS16** Runs worth 9 or more are under 5% of runs.
- **NS17** Runs worth 12 outnumber runs worth 10 and 11 together.
- **NS18** B: NS1 holds.
- **NS19** B: NS2 holds.
- **NS20** F': NS10 holds.

## Results of the hundred-and-twelfth set (added after the test; `predict_test112.py`, `results/predict_test112.md`)

Thirteen held, seven failed. One number system serves every genre: the tiered form is for 5-8 in names (NS1: 77%
against 2%; NS18 in B: 85% against 3%), counts (NS2: 52% against 1%; NS19 in B) and closer lines (NS3: 3 of 5), every
common numeral sign occurs in 2+ genres (NS11: 13 of 13), and the notation (kind) does not depend on genre (NS5, p =
0.11). Values do differ a little by genre (NS4, p = 0.0001): counts run larger than names, not smaller (NS8 fails: 22%
of runs 5+ against 16%), and seal counts are tiered more than tablet counts (NS12: 12% against 4%). The commonest value
is 2 in every genre (NS7 fails for 3); '2' is the commonest numeral sign (NS14: 668), runs worth 1 are rarer than 2
(NS15), runs of 9+ are about 5% (NS16), and 12 stands out (NS17: 36 runs against 7 for 10 and 11), but all 36 are the
single sign 55, so this is one sign, not a counting base. 17% of count runs have 2+ signs (NS9). NS10/NS20 (larger part
first) fail at 26%, but post-test inspection shows the 'smaller first' pairs are mostly a heading's '2' followed by a
numeral ('861 2 31', '861 2 4'), not compound numbers, so the order of compound numerals is untested. Also not
supported: closer-line numbers inside the body (NS6: 58%) and long numerals before the head (NS13: 34% against 40%).
Tally, counting parts: 852 held, 875 failed (1727 registered).

# Hundred-and-thirteenth set, registered before testing (24 September 2026): sets 111-112 on held-out data (twenty hypotheses)

Findings of the hundred-and-eleventh and hundred-and-twelfth sets re-tested on F without copper (F'), the smaller sites
(OS, F' outside the two cities) and B, plus a corrected compound-numeral test that leaves out runs directly after a
heading sign (the confound found in the hundred-and-twelfth set). Definitions as in those sets. 10,000-draw
permutations (1,000 where the original used 1,000); p < 0.05.

- **RO1** OS: positions in names and counts correlate (OG1; Spearman 0.3+, significant; signs with 3+ tokens in each).
- **RO2** OS: a sign's right company in counts is closer to its own name company than to another sign's (OG7).
- **RO3** F': positions in names and closer lines correlate (OG2).
- **RO4** F': positions in counts and bare lines correlate (OG4).
- **RO5** F': name heads end bare lines more often than other signs (OG5).
- **RO6** F': name pairs recur in counts beyond name-shuffled pairs (OG9, 1,000).
- **RO7** F': recurring name units occur in counts beyond random name-sign pairs (OG10).
- **RO8** F': 60%+ of signs counted in names and counts keep their commonest numeral kind (OG12).
- **RO9** F': a sign's mean count in names and counts correlates (OG13; 0.3+).
- **RO10** F': closers follow 740-class heads more than 520-class heads (OG16).
- **RO11** B: OG7 holds.
- **RO12** B: OG13 holds.
- **RO13** F': in names, 5-8 is tiered more than 1-4 (NS1).
- **RO14** F': in counts, the same (NS2).
- **RO15** F': every numeral sign with 10+ tokens occurs in 2+ genres (NS11).
- **RO16** F': the numeral kind does not depend on genre (MI p >= 0.05; NS5).
- **RO17** A + B: in 2-sign runs of unequal value not directly after a heading sign, the larger value comes first in
  70%+.
- **RO18** F': RO17 holds.
- **RO19** B: '2' is the commonest numeral sign (NS14).
- **RO20** F': runs worth 12 outnumber runs worth 10 and 11 together (NS17).

## Results of the hundred-and-thirteenth set (added after the test; `predict_test113.py`, `results/predict_test113.md`)

Seventeen held, three failed. 'One sign, many genres' replicates widely: sign positions correlate between names and
counts at the smaller sites (RO1: 0.55) and between names and closers (RO3: 0.53) and counts and bare lines (RO4: 0.37)
in F'; a sign keeps its company across genres at the smaller sites (RO2: 18 against 5) and in B (RO11: 27 against 7);
name heads end bare lines (RO5: 58% against 30%); name pairs and units recur in counts (RO6, RO7); notation carries over
(RO8: 63%); closers follow the 740 class (RO10). A sign's typical count carries over in B (RO12: 0.93 over 8 signs) but
not in F' (RO9: 0.04 over 21 signs), so OG13 is only partly confirmed. The number system is the same across genres in
F' (RO13, RO14: tiered for 5-8; RO15: all 14 common numerals in 2+ genres; RO16: notation independent of genre, p =
0.25), '2' is the commonest numeral in B (RO19), and 12 (the sign 55) stands out in F' too (RO20: 27 against 6).
Corrected compound test: even with heading-led runs removed, 2-sign numeral runs put the smaller value first (RO17: 24%
larger first; RO18 in F': 31%), so the prediction fails and the order 'small then large' is the observed pattern; it is
not yet clear whether the small first element (often '2' or '1') is a numeral or a stroke with another role.
Tally, counting parts: 869 held, 878 failed (1747 registered).

# Hundred-and-fourteenth set, registered before testing (24 September 2026): small-then-large numeral runs (twenty hypotheses)

Seen before registering (A + B distinct lines): 158 two-sign numeral runs not directly after a heading sign, commonest
'2 32' (17), '2 3' (11), '31 2' (10), '2 4' (8), '33 33' (8), '1 3', '1 4' (7 each); 28 are line-initial; the sign after
is often 220, 390, 405. 'Small-first run' = a 2-sign run whose first value is smaller; '2 N run' = a run '2' + numeral.
Runs as in the hundred-and-twelfth set; heading signs 817, 820, 861. 10,000-draw permutations; p < 0.05.

- **SR1** 70%+ of small-first runs start with '2' or '1'.
- **SR2** '2 N' runs are line-initial more often than other numeral runs.
- **SR3** Five signs cover 50%+ of the signs after '2 N' runs.
- **SR4** For 50%+ of '2 N X' (X a non-numeral), 'N X' is attested elsewhere without the leading '2'.
- **SR5** The '2' prefix stands before long numerals more often than numerals in general are long.
- **SR6** 70%+ of lines with a '2 N' run are on seals (F without copper).
- **SR7** '2 N' lines are a larger share of lines at Mohenjo-daro than at Harappa (F without copper).
- **SR8** Runs of two identical numerals are 10%+ of 2-sign runs.
- **SR9** Large-first runs are followed by a non-numeral as often as small-first runs (two-sided p >= 0.05).
- **SR10** 30%+ of '1 N' runs directly follow 740 or 520.
- **SR11** Small-first runs are line-initial more often than large-first runs.
- **SR12** In '2 N' runs, N is worth 3+ in 80%+.
- **SR13** In '2 N X', X's commonest count elsewhere equals N's value more often than N + 2.
- **SR14** The signs X after unheaded '2 N' runs overlap with the signs after 'heading 2 N' more than with random signs
  (Jaccard against frequency-matched random sets).
- **SR15** Runs of 3+ numeral signs are under 3% of runs.
- **SR16** B: SR1 holds.
- **SR17** B: SR2 holds.
- **SR18** F without copper: SR1 holds.
- **SR19** F without copper: SR4 holds.
- **SR20** F without copper: SR14 holds.

## Results of the hundred-and-fourteenth set (added after the test; `predict_test114.py`, `results/predict_test114.md`)

Eleven held, nine failed. The small first stroke in 'small-then-large' runs is not part of the number. In '2 N X', the
'N X' is attested without the '2' in 85% (SR4; SR19 in F': 83%), and X's usual count elsewhere equals N in 27 cases and
N + 2 in none (SR13): the '2' is a prefix, not an addend. The signs counted after '2 N' overlap with those counted after
'heading + 2 + N' more than random signs do (SR14: p = 0.018; SR20 in F': p = 0.045), so an unheaded '2 N' behaves like
the heading unit's '2' without its heading sign. '2 N' lines are seal lines (SR6: 40 of 45) and a little commoner at
Mohenjo-daro (SR7: 2.4% against 1.2%); they count a few items, mainly 220 and 390 (SR3: top five 58%). Most small-first
runs start with '2' or '1' (SR1: 71%; just under 70% in B, SR16: 65%, and F', SR18: 69%). Numeral runs are short (SR15:
1% of 3+ signs). Not supported: '2 N' opening lines (SR2, SR17: they are mostly mid-line), '2' preferring long numerals
(SR5), doubled numerals being common (SR8: 9%), '1 N' after an ending (SR10: 26%), small-first runs opening lines (SR11),
and N being 3+ (SR12: 61%). Large-first and small-first runs are both followed by a counted sign (SR9). Tally, counting
parts: 880 held, 887 failed (1767 registered).

# Hundred-and-fifteenth set, registered before testing (24 September 2026): structural predictions of published proposals (twenty hypotheses)

Each hypothesis is a structural consequence of a published view, stated so the data can contradict it; none tests a
proposed sound value. Views (from memory of the literature, to be checked against the sources): Parpola 1994 (fish
signs as 'star/god' words, numeral + fish as named star groups such as 'six' and 'seven' stars, theophoric personal
names); Mahadevan 1977 and Parpola (740 and 520 as grammatical suffixes, suffixes stack after the ending); Farmer,
Sproat and Witzel 2004 (a non-linguistic sign system: many singletons, short texts, little repetition); Rao et al.
2009 and Yadav et al. 2010 (language-like sequential structure, text segmentable into frequent pairs). Distinct lines
(A + B) unless stated; F without copper (F') for objects and sites. 10,000-draw permutations (1,000 where marked); p < 0.05.

Parpola: fish
- **PR1** Values 6 and 7 are a larger share of the numbers directly before a fish than before other signs.
- **PR2** 70%+ of distinct names with a numeral + fish pair are on one object only (F').
- **PR3** 10+ minimal pairs exist: distinct name bodies that differ only by swapping one fish sign for another.
- **PR4** Numeral + fish names are on seals in 80%+ (F').
- **PR5** Fish-final names occur at both cities as often as other names (two-sided p >= 0.05; F', distinct bodies).
Mahadevan and Parpola: suffixes
- **PR6** Under 2% of 740 tokens are line-initial.
- **PR7** 400, 90 and 151 directly precede 740 in under 5% of their adjacencies with 740.
Farmer, Sproat and Witzel
- **PR8** 20%+ of sign types in F (with copper) occur once.
- **PR9** Mean line length is under 5 signs (F', distinct lines).
- **PR10** Non-adjacent repetition of a sign within a line is rarer than in within-line shuffles (all lines, 1,000).
Rao et al. and Yadav et al.
- **PR11** Adjacent-sign mutual information is at least twice its mean under within-line shuffles.
- **PR12** Conditional entropy of the next sign given the previous is under 80% of the unigram entropy.
- **PR13** The rank-frequency slope over ranks 1-100 is between -1.3 and -0.7.
- **PR14** The 50 commonest adjacent pairs cover 30%+ of adjacent-pair tokens.
- **PR15** 50%+ of adjacent-pair types occur once.
Order of number and noun
- **PR16** 'Numeral + non-numeral' adjacencies outnumber 'non-numeral + numeral' by 1.5 to 1 or more.
Replication
- **PR17** B: PR11 holds.
- **PR18** F': PR12 holds.
- **PR19** B: PR8 holds (B's sign types).
- **PR20** F': PR1 holds.

## Results of the hundred-and-fifteenth set (added after the test; `predict_test115.py`, `results/predict_test115.md`)

Eleven held, nine failed. These test structural consequences only, under this project's sign identifications and
numeral values (ICIT numbering), which may not match each author's; the views are summarised from memory and should
be checked against the sources before citing. Parpola (fish): numbers before a fish are 6 or 7 less often, not more,
than before other signs (PR1: 4% against 9%; PR20 in F': 4% against 9%), so the 'six stars / seven stars' pattern does
not show here (fish are mostly counted 2, sixty-ninth set); numeral + fish names are one-off (PR2: 93%) and fish
variants make many minimal pairs (PR3: 111), consistent with distinct words in personal names, but they are on seals in
only 68% (PR4) and fish-final names occur at both cities more often than other names (PR5: 13% against 5%, the reverse
of 'as local as others'). Mahadevan and Parpola (suffixes): 740 almost never begins a line (PR6: 9 of 1,218) and
400/90/151 almost never precede it (PR7: 9 of 219), consistent with 740 as a suffix and suffixes stacking after it.
Farmer, Sproat and Witzel: a third of sign types are singletons (PR8: 33% in F; B only 12%, PR19, as B merges rare
signs), lines are short (PR9: 4.3), and non-adjacent repeats are rarer than chance (PR10); these fit their view but
also fit short name-like texts. Rao and Yadav (language-like order): the next sign is well predicted (PR12: conditional
entropy 52% of unigram; PR18 F': 49%, though plug-in estimates on this few tokens understate conditional entropy), the
frequency curve is Zipf-like (PR13: slope -0.90), and pair types are mostly singletons (PR15: 65%); but adjacent MI is
only 1.5 times its shuffled value (PR11; PR17 in B: 1.35), under the 2x threshold, and the top 50 pairs cover 25%
(PR14). 'Number before noun' holds only 1.2 to 1 (PR16), because numerals also follow 705/706 and headings. Neither the
linguistic nor the non-linguistic view is decided by these tests. Tally, counting parts: 891 held, 896 failed (1787
registered).

# Hundred-and-sixteenth set, registered before testing (24 September 2026): sets 114-115 on held-out data (twenty hypotheses)

Findings of the hundred-and-fourteenth and hundred-and-fifteenth sets re-tested on F without copper (F'), the smaller
sites (OS) and B. Definitions as in those sets. 10,000-draw permutations (1,000 where marked); p < 0.05.

The '2' prefix
- **HX1** F': in '2 N X', X's commonest count elsewhere equals N more often than N + 2 (SR13).
- **HX2** B: 'N X' is attested without the '2' for 50%+ of '2 N X' (SR4).
- **HX3** B: SR13 holds.
- **HX4** OS: 70%+ of lines with a '2 N' run are on seals (SR6).
- **HX5** F': runs of 3+ numeral signs are under 3% (SR15).
- **HX6** B: SR15 holds.
- **HX7** F': five signs cover 50%+ of the signs after '2 N' runs (SR3).
Published proposals
- **HX8** F': 10+ minimal pairs of bodies differ by one fish sign (PR3).
- **HX9** B: 5+ such minimal pairs.
- **HX10** F': under 2% of 740 tokens are line-initial (PR6).
- **HX11** B: PR6 holds.
- **HX12** F': 400/90/151 precede 740 in under 5% of their adjacencies with it (PR7).
- **HX13** B: PR7 holds.
- **HX14** B: non-adjacent repeats are rarer than in within-line shuffles (PR10, 1,000).
- **HX15** OS: PR10 holds (1,000).
- **HX16** F': the rank-frequency slope over ranks 1-100 is between -1.3 and -0.7 (PR13).
- **HX17** B: PR13 holds (ranks 1-100 or all if fewer).
- **HX18** F': 50%+ of adjacent-pair types occur once (PR15).
- **HX19** B: conditional entropy of the next sign is under 80% of the unigram entropy (PR12).
- **HX20** OS: 70%+ of distinct numeral + fish names are on one object (PR2).

## Results of the hundred-and-sixteenth set (added after the test; `predict_test116.py`, `results/predict_test116.md`)

Nineteen held, one failed. The '2' prefix replicates: in F' X's usual count equals N 17 times and N + 2 never (HX1; B: 4
and 0, HX3), 'N X' exists without the '2' in B (HX2: 11 of 13), '2 N' lines are seal lines at the smaller sites (HX4: 6
of 8), '2 N' counts few things (HX7: 390, 220 cover most), and numeral runs are short (HX5, HX6). The structural
predictions replicate: fish-variant minimal pairs (HX8: 73 in F'; HX9: 32 in B), 740 almost never line-initial (HX10,
HX11), suffixes after the ending in B (HX13: 2 of 72; F' 9 of 175 = 5.1%, just over the 5% line, HX12), fewer distant
repeats than chance (HX14 in B; HX15 at the smaller sites), a Zipf-like curve (HX16: -0.92; HX17: -0.83), mostly unique
pair types (HX18: 70%), predictable next signs in B (HX19: ratio 0.47, with the plug-in caveat), and one-off numeral +
fish names at the smaller sites (HX20: 21 of 22). Tally, counting parts: 910 held, 897 failed (1807 registered).

# Hundred-and-seventeenth set, registered before testing (24 September 2026): the lines no genre claims (fifteen hypotheses)

Opening a self-directed loop (test, learn, propose) aimed at the gaps left by the hundred-and-sixteenth set. 312 of 2,722
distinct lines (A + B) are 'other' in the hundred-and-eighth set's genres. Seen before registering: their commonest
templates are FX (35), XFX (23), XEX (22), XCX (21), XF (21), HX (14). Sub-kinds: 'fish bare' = no H, N, E, C but a
fish; 'name + tail' = contains E with signs after it that are not only a suffix; 'closer + tail' = contains a closer
with signs after it; 'heading + word' = template starting H not followed by N. F' = F without copper. p < 0.05.

- **OT1** Fish-bare lines end in a name head in 50%+.
- **OT2** Fish-bare lines start with a name opener in 50%+.
- **OT3** Fish-bare lines are on tablets or potsherds more often than name lines (F').
- **OT4** 80%+ of name + tail lines have a tail of 1-3 signs.
- **OT5** 80%+ of closer + tail lines have 1-2 signs after the closer.
- **OT6** The sign right after a mid-line closer is a numeral or 400/90/151 in 40%+.
- **OT7** 40%+ of heading + word lines have 368 as their second sign.
- **OT8** Counting fish-bare lines as bare, name + tail as names, closer + tail as closer lines and heading + word as
  headed names or formulas, under 5% of lines remain unassigned.
- **OT9** The first tail sign after a mid-line ending is a closer, a numeral or 400/90/151 in 50%+.
- **OT10** Closers followed by a tail are 151 or 156 more often than line-final closers are.
- **OT11** Fish-bare lines hold a formula-only sign less often than bare lines.
- **OT12** 'Other' lines are seal lines more often than bare lines are (F').
- **OT13** 'Other' texts are one-off more often than name texts (F').
- **OT14** B: OT8 holds.
- **OT15** F': OT8 holds.

## Results of the hundred-and-seventeenth set (added after the test; `predict_test117.py`, `results/predict_test117.md`)

Nine held, six failed. The 312 'other' lines are extensions of the known genres: 160 are names with a short tail (OT4:
89% of tails 1-3 signs), 100 are bare lines that contain a fish (OT1: 79% end in a name head; OT2: 85% start with a name
opener; OT3: more on tablets and potsherds than names, 37% against 25%), 31 are closer lines with a short tail (OT5: 94%
1-2 signs), and 18 are headed lines with a word after the heading (mostly '820 60', not 368: OT7 fails). Only 3 of
2,722 lines stay unassigned (OT8: '740 400', '740 90', '861 2 740 90'; OT14 in B: 2 of 973; OT15 in F': 89 of 2,217,
4%). The key new observation: the sign after a mid-line closer is 400 in 25 of 31 cases (OT6: 81% numerals or
suffixes), so closers take the same 400 suffix as the 740 ending; this makes the closers look like endings rather
than formula words (to be tested next). Name tails start with 1, 679, 621, 565, 90, 32, but that is not mostly
counts, closers or suffixes (OT9: 47%). Not supported: 151/156 as the tail-taking closers (OT10), fish-bare lines using
fewer formula-only signs (OT11), 'other' lines on seals more than bare lines (OT12), and 'other' texts being one-off
(OT13, the other way). Tally, counting parts: 919 held, 903 failed (1822 registered).

# Hundred-and-eighteenth set, registered before testing (24 September 2026): are the closers endings? (fifteen hypotheses)

Lead from the hundred-and-seventeenth set: 25 of 31 closer lines with a tail add 400 after the closer, as '740 400'.
Closers as in the hundred-and-third set. Distinct lines (A + B) unless stated; F' = F without copper; 'body' = signs
before the closer or ending (heading unit removed). p < 0.05; two-sided where marked.

- **CE1** 80%+ of 400s directly after a closer are line-final.
- **CE2** 'Closer 400' lines are on tablets more often than closer lines without 400 (F').
- **CE3** 'Closer 400' lines are at Harappa more often than closer lines without 400 (F').
- **CE4** 90 directly follows a closer in under 3 distinct lines (90 belongs to 740).
- **CE5** In lines with both 740 and a closer, 740 directly precedes the closer in 50%+.
- **CE6** Over heads with 5+ distinct lines, a head's closer share and its 740 share correlate negatively (Spearman
  -0.3 or lower).
- **CE7** 5+ bodies are attested both before 740 and before a closer.
- **CE8** 10+ distinct lines end '740 + closer'.
- **CE9** The body's last sign is counted (numeral before it) as often before closers as before 740 (two-sided p >= 0.05).
- **CE10** The share of closer lines with 400 after the closer is within a factor of 2 of the share of 740 lines with
  400 after 740.
- **CE11** B: CE1 holds.
- **CE12** F': CE2 holds.
- **CE13** 20%+ of bodies before 'closer 400' are attested before '740 400' or 740.
- **CE14** At the smaller sites, 3+ distinct lines have 'closer 400'.
- **CE15** Where a closer's tail is not 400, its first sign is a numeral in 50%+.

## Results of the hundred-and-eighteenth set (added after the test; `predict_test118.py`, `results/predict_test118.md`)

Thirteen held, two failed: the closers behave as endings. The same body takes either 740 or a closer (CE7: 40 bodies),
and over 74 heads a head's closer share and its 740 share replace each other (CE6: Spearman 0.79 against the 740
share); a closer's head is counted as often as 740's (CE9: 14% against 16%). Closers take the 400 suffix at the same rate
as 740 (CE10: 9.1% against 10.1% of lines), line-final (CE1: 31 of 32; CE11 in B: 14 of 15), and 'closer 400' is, like
'740 400', a Harappa tablet form (CE2: 76% on tablets against 9%; CE3: 90% Harappa against 27%); 25% of 'closer 400'
bodies also occur before 740 (CE13). 90 never follows a closer (CE4: 0), so 90 belongs to 740 alone. A closer can also
stand after 740 ('740 + closer', CE8: 34 lines; CE5: in 54% of lines with both, 740 directly precedes the closer), so the
closers are a set of endings that either replace 740 or stack after it. Not supported: 'closer 400' at the smaller sites
(CE14: 1 line) and non-400 closer tails being counts (CE15: 32%). CE12 repeats CE2 on the same data (registered in error
as a separate F' test) and is not independent evidence. Tally, counting parts: 932 held, 905 failed (1837 registered).

# Hundred-and-nineteenth set, registered before testing (24 September 2026): the ending slot as a paradigm (fifteen hypotheses)

From the hundred-and-eighteenth set: the ending slot holds 740, 520 or a closer (CL), and a closer can also stack
after 740. 'Filler' = 740, 520 or a closer at the end of a body (heading unit removed); 'stack' = 740 or 520 directly
followed by a closer. Distinct lines (A + B) unless stated; F' = F without copper. p < 0.05.

- **EP1** 'Closer + 740' is under 10% of the adjacencies between a closer and 740 (the order is 740 then closer).
- **EP2** Closers stack after 740 at least three times as often as after 520 (distinct lines).
- **EP3** Which closer is used depends on whether 740 stands before it or a head does (MI).
- **EP4** Bodies before '740 + closer' are longer than bodies before a closer alone (rank test).
- **EP5** Lines with the heading unit have 740 before their closer more often than other closer lines.
- **EP6** 80%+ of '740 + closer' lines are on seals (F').
- **EP7** '740 + closer' lines are at Mohenjo-daro more often than closer-alone lines (F').
- **EP8** 5+ bodies are attested with 3+ different fillers (740, 520 or particular closers).
- **EP9** The filler is predicted by the head more than by the city (MI head > MI city, F' lines at the two cities).
- **EP10** 70%+ of the 11 closers appear directly after 740 at least once.
- **EP11** '740 + closer + 400' occurs in 2 or fewer distinct lines (no double suffix).
- **EP12** Closer choice depends on the city (MI, F').
- **EP13** Closer choice depends on seal against tablet (MI, F').
- **EP14** B: EP1 holds.
- **EP15** B: 5+ bodies occur before both 740 and a closer.

## Results of the hundred-and-nineteenth set (added after the test; `predict_test119.py`, `results/predict_test119.md`)

Nine held, six failed. The ending slot behaves as a paradigm. The order is fixed: 740 then closer (EP1: 3 of 40 the other
way; EP14 in B: 0 of 12), closers stack after 740 and hardly after 520 (EP2: 37 lines against 4), a subset of closers
stacks (EP3: 151, 161, 527, 565, 621, 679 follow 740; EP10: 6 of 11), and nothing follows '740 + closer' (EP11: no
'740 + closer + 400'). 26 bodies are attested with three or more different fillers (EP8), and 13 bodies take both 740
and a closer in B (EP15). The head chooses the filler, the city barely (EP9: 1.06 against 0.02 bits); the city shifts
closer choice a little (EP12, p = 0.006), the medium not significantly (EP13, p = 0.07). Stacked names are not longer
(EP4), not headed more (EP5), not more on seals (EP6: 79%, just under 80%) or at Mohenjo-daro (EP7). Model: body +
{740 | 520 | closer | 740 + stacking closer} + optional 400 (not after a stacked closer) or 90 (after 740 only).
Tally, counting parts: 941 held, 911 failed (1852 registered).

# Hundred-and-twentieth set, registered before testing (24 September 2026): two kinds of closer (fifteen hypotheses)

From the hundred-and-nineteenth set: six closers are seen after 740 ('stacking': 151, 161, 527, 565, 621, 679) and five
are not ('plain': 154, 156, 226, 241, 426). Bodies, classes and heads as before; distinct lines (A + B) unless stated;
F' = F without copper. p < 0.05.

- **SK1** Plain closers' bodies also occur before 740 more often than stacking closers' bodies (closer directly after the
  body).
- **SK2** 25%+ of stacking-closer tokens directly follow 740.
- **SK3** F': plain closers directly follow 740 in 1 distinct line or none.
- **SK4** Plain closers follow a 520-class head more often than stacking closers do.
- **SK5** Stacking-closer lines are on tablets more often than plain-closer lines (F').
- **SK6** Plain closers take 400 after them more often than stacking closers.
- **SK7** The closer kind depends on the city (F', Fisher two-sided).
- **SK8** When no 740 intervenes, 90%+ of classed heads before stacking closers are 740-class.
- **SK9** Under 80% of classed heads before plain closers are 740-class.
- **SK10** Plain closers' heads are counted (numeral before) more often than stacking closers' heads.
- **SK11** Bodies before stacking closers are attested 740 names more often than bodies before plain closers.
- **SK12** B: SK1 holds.
- **SK13** F': stacking closers follow 740 in 25%+ of tokens (SK2).
- **SK14** F': SK11 holds.
- **SK15** The first sign of name tails (after a mid-line ending) is a stacking closer at least three times as often as a
  plain closer.

## Results of the hundred-and-twentieth set (added after the test; `predict_test120.py`, `results/predict_test120.md`)

Three held, twelve failed: the split into stacking and plain closers is real only in the property that defined it.
Plain closers never follow 740 in F' either (SK3: 0 lines), every closer that begins a tail after a mid-line ending is a
stacking one (SK15: 41 against 0), and plain closers take 400 a little more often (SK6: 13% against 6%). Otherwise the two
kinds are alike: their bodies are attested 740 names equally often (SK1, SK11, SK12, SK14: about 20% both), their heads
are 740-class alike (SK8: 84%; SK9: 90%) and rarely 520-class (SK4), they are counted alike (SK10), sit on tablets alike
(SK5), and do not split by city (SK7, p = 0.07). Only 18% of stacking tokens follow 740 (SK2; SK13 in F'), so stacking is
an option, not the rule. Reading: one set of closers in the ending slot, six of which may also be added after 740.
Tally, counting parts: 944 held, 923 failed (1867 registered).

# Hundred-and-twenty-first set, registered before testing (24 September 2026): what else marks the 520 class (twelve hypotheses)

Classes as in the eighty-first set (520 class: fish 220, 231, 233, 235, 240; numerals 1, 33; and 175, 382, 70, 72).
Distinct names (A + B) unless stated. 'Left neighbours' of a sign = the set of signs seen directly before it in bodies.
10,000-draw permutations; p < 0.05.

- **C5A** The non-fish 520 heads (175, 382, 70, 72) are directly preceded by a fish more often than 740-class heads are.
- **C5B** 520 names open with a fish more often than 740 names do.
- **C5C** The value before the head depends on the head's class (MI over counted heads).
- **C5D** In F (all objects), 90 directly follows 520 in at most one distinct line.
- **C5E** The five commonest 520 bodies account for 20%+ of 520 name tokens (A + B tokens).
- **C5F** The left neighbours of 520-class heads overlap with the left neighbours of fish signs more than those of
  740-class heads do (mean Jaccard, heads with 3+ neighbours).
- **C5G** The fish head 222 (always 740) and the fish head 220 (mostly 520) have left-neighbour sets overlapping at
  Jaccard 0.3 or less.
- **C5H** Counted fish heads take 520 more often than uncounted fish heads (distinct names).
- **C5I** 40%+ of distinct 520 lines have a fish directly before 520.
- **C5J** Within fish heads, the class depends on the sign before the fish (MI, distinct names).
- **C5K** B: C5B holds.
- **C5L** B: C5I holds.

## Results of the hundred-and-twenty-first set (added after the test; `predict_test121.py`, `results/predict_test121.md`)

Four held, eight failed: nothing in the context explains the 520 class beyond the head itself. 43% of distinct 520
lines have a fish directly before 520 (C5I; B 40%, just under, C5L), 90 never follows 520 (C5D: 0 in all of F), the 520
names are dominated by a few repeated ones (C5E: 26% are 501 405 2 240, 415 220, 233, 240, 705 33), and the fish heads
222 (always 740) and 220 (mostly 520) take different words before them (C5G: Jaccard 0.13). But 520 names do not open
with fish more (C5B, C5K), the non-fish 520 heads are not preceded by fish more (C5A, p = 0.06) nor keep fish company
(C5F), the count does not depend on the class (C5C), counted fish heads do not take 520 more on distinct names (C5H,
the other way), and the sign before a fish head does not choose its class (C5J, p = 0.15). Reading: class membership
is a property of each head, learned per word, not derived from its neighbours; the internal evidence on this question
is exhausted. Tally, counting parts: 948 held, 931 failed (1879 registered).

# Hundred-and-twenty-second set, registered before testing (24 September 2026): the model as a predictor (fifteen hypotheses)

The structural findings are turned into predictions on held-out data. Distinct lines (A + B) are split 80/20 at random
(seed fixed in the script); models are fitted on the 80% and scored on the 20%. Genres as in the hundred-and-eighth set;
classes, units and templates as before. Cross-entropy in bits per sign with add-one smoothing over the training
vocabulary plus one unknown. Thresholds as stated.

- **GM1** From the preceding sign, the head of a held-out name is predicted (top-1) 10+ points better than by the
  commonest head.
- **GM2** The ending of a held-out name is predicted from its head (the head's training majority) with 85%+ accuracy,
  over names whose head was seen in training.
- **GM3** The ending is predicted from the head 10+ points better than from the opener.
- **GM4** The genre of a held-out line is predicted from its last sign with 80%+ accuracy (last signs seen in training).
- **GM5** The last sign predicts genre 20+ points better than the first sign.
- **GM6** 45%+ of held-out lines fall in the training set's ten commonest templates.
- **GM7** A bigram model has at least 1 bit per sign lower cross-entropy than a unigram model on held-out lines.
- **GM8** A two-sign-context model (with backoff to bigram) beats the bigram model by 0.2+ bits per sign.
- **GM9** 60%+ of held-out name bodies of 3+ signs contain a unit found in training.
- **GM10** 90%+ of held-out name heads were seen as heads in training.
- **GM11** 70%+ of held-out openers (bodies of 2+) were seen as openers in training.
- **GM12** Trained on Mohenjo-daro names (F without copper), the head predicts Harappa endings with 85%+ accuracy.
- **GM13** Trained on A's names, the head predicts B's endings with 85%+ accuracy.
- **GM14** B (80/20 split): GM4 holds.
- **GM15** F without copper (80/20 split): GM7 holds.

## Results of the hundred-and-twenty-second set (added after the test; `predict_test122.py`, `results/predict_test122.md`)

Twelve held, three failed. As predictors on held-out lines (80/20 split): the sign before the head predicts the head
38% of the time against 7% for the commonest head (GM1); the head predicts the ending 90% of the time (GM2), across
cities (GM12: Mohenjo-daro to Harappa 92%) and transcriptions (GM13: A to B 93%), but the opener alone gets 82% (GM3
fails) because 740 is the ending of about 85% of names, so the head adds only about 5-8 points over always guessing
740. The last sign predicts genre far better than the first (GM5: 77% against 44%) but under 80% (GM4; B 69%, GM14).
Order carries real information: a bigram model saves 1.8 bits per sign over unigrams (GM7: 8.21 to 6.38; GM15 in F':
8.23 to 6.75), and two signs of context save a further 0.6 (GM8: 5.80). The inventories generalise: 48% of test lines
fall in the training top-10 templates (GM6), 65% of test bodies contain a training unit (GM9), 95% of test heads (GM10)
and 88% of openers (GM11) were already seen. Tally, counting parts: 960 held, 934 failed (1894 registered).

# Hundred-and-twenty-third set, registered before testing (24 September 2026): does structure improve prediction? (twelve hypotheses)

Same 80/20 split and cross-entropy (bits per sign) as the hundred-and-twenty-second set (its baseline bigram 6.38 bits).
'Role' of a sign: numeral kind, heading (first-position 817/820/861), ending (740/520), suffix (400/90/151 after an
ending), closer, fish, or other. Interpolation weights are fitted on a slice of the training data only. Thresholds as
stated.

- **BM1** Interpolating the sign bigram with a role-bigram model (P(role|previous role) x P(sign|role)) lowers held-out
  cross-entropy by 0.1+ bits.
- **BM2** Genre-specific bigrams (genre read from the line's last sign) lower it by 0.1+ bits.
- **BM3** A position-aware unigram (first, middle, last) beats the plain unigram by 0.5+ bits.
- **BM4** The bigram read in the recorded direction beats the same model read in reverse by 0.05+ bits.
- **BM5** Knowing the ending raises head prediction from the preceding sign by 5+ points (names).
- **BM6** For heads with 5+ training names, the ending is predicted with 95%+ accuracy.
- **BM7** A 'no-repeat' adjustment (halving the probability of a sign already used two or more places back in the
  line) lowers cross-entropy by 0.02+ bits.
- **BM8** The trigram gain over bigram is larger for name lines than for count lines.
- **BM9** A bigram trained on Mohenjo-daro lines is 0.3+ bits worse on Harappa lines than one trained on other
  Harappa lines (F without copper, same training size).
- **BM10** A bigram trained on names is 1+ bit worse on count lines than on held-out names.
- **BM11** A bigram trained on A is within 1 bit of B-trained on held-out B lines (same training size).
- **BM12** Adding the role model (BM1) helps more on the smaller sites' lines than on the cities' held-out lines.

## Results of the hundred-and-twenty-third set (added after the test; `predict_test123.py`, `results/predict_test123.md`)

Seven held, five failed. The structural findings improve prediction of held-out lines. Adding the role model (numeral
kind, heading, ending, suffix, closer, fish, other) to the sign bigram cuts cross-entropy from 6.38 to 5.86 bits per sign
(BM1), more on the smaller sites (BM12: 0.60 against 0.53); genre-specific bigrams cut it to 6.17 (BM2); and position in
the line alone (first, middle, next-to-last, last) gives 5.43 bits, better than the plain bigram and 0.9 bits better
than the unigram (BM3). Names carry longer dependencies than counts (BM8: trigram gain 0.74 against 0.65) and a
name-trained model does 2 bits worse on counts (BM10: 5.52 against 7.55), so the genres are different sequence types
on one vocabulary. A-trained models are within 1 bit of B-trained ones on B (BM11: 6.82 against 5.96). Not supported:
knowing the ending barely helps predict the head (BM5: 38% to 42%); common heads predict the ending at 90%, not 95%
(BM6); penalising repeats does not help (BM7); a Mohenjo-daro model is only 0.14 bits worse on Harappa than a Harappa
one (BM9, under 0.3). BM4 was ill-posed: a smoothed bigram scores almost identically forwards and backwards, so it cannot
detect reading direction (6.384 both). Next: combine position, roles and bigrams in one model. Tally, counting parts:
967 held, 939 failed (1906 registered).

# Hundred-and-twenty-fourth set, registered before testing (24 September 2026): one combined model (ten hypotheses)

Components from the hundred-and-twenty-second and -third sets, fitted on the same 80% training lines: bigram,
role model, position unigram (first, middle, next-to-last, last), two-sign-context model. The combined model is a
linear interpolation whose weights are chosen on a held-back slice of the training data only (coarse grid). Scores are
held-out cross-entropy in bits per sign (previous best single component: position unigram 5.43).

- **CM1** The combined model beats the best single component by 0.3+ bits.
- **CM2** The combined model scores under 5.0 bits per sign.
- **CM3** Adding genre-specific bigrams to the combination gains 0.05+ bits.
- **CM4** Adding a position-bucketed bigram (previous sign and position class) gains 0.05+ bits.
- **CM5** Trained on A + B, the combined model scores under 5.5 bits on F-without-copper lines absent from A + B.
- **CM6** On B alone (80/20), the combined model beats B's bigram by 0.5+ bits.
- **CM7** Dropping the role model from the combination costs 0.1+ bits.
- **CM8** Dropping the position unigram costs 0.2+ bits.
- **CM9** Dropping the two-sign-context model costs 0.1+ bits.
- **CM10** Relative position in five buckets beats the four-way position class by 0.1+ bits (as a unigram).

## Results of the hundred-and-twenty-fourth set (added after the test; `predict_test124.py`, `results/predict_test124.md`)

Five held, five failed. The best held-out model of the sign sequence is simple: position in the line (first, middle,
next-to-last, last) plus two signs of context, weighted 0.62 and 0.37, gives 4.92 bits per sign (CM1: 0.51 better than
the best single part; CM2: under 5), against 8.21 for the unigram and 6.38 for the bigram. Both parts matter (CM8:
dropping position costs 0.34; CM9: dropping context costs 0.50), and the same model gains 1.2 bits over the bigram on B
(CM6: 5.90 to 4.73). Once position and context are in, the role classes, genre and a position-aware bigram add nothing
(CM7: 0.00; CM3: 0.004; CM4: 0.000): what the structural rules capture is mostly where a sign stands and what stands
next to it. Finer position buckets do worse (CM10), and the model is 5.69 bits, not under 5.5, on the 413 F lines that
A + B lack (CM5), about 0.8 bits worse than on its own held-out lines. Benchmark: 4.9 bits per sign in-sample held-out,
5.7 on new lines; any model claiming more structure should beat these. Tally, counting parts: 972 held, 944 failed
(1916 registered).

# Hundred-and-twenty-fifth set, registered before testing (24 September 2026): beating the benchmark (ten hypotheses)

Benchmark (hundred-and-twenty-fourth set): position class + two-sign context, 4.92 bits per sign on held-out A + B lines,
5.69 on new F lines. Same split and weight-fitting on a training slice. Each hypothesis states a structural claim and its
predictive test.

- **BB1** Lines are anchored at their end: a unigram by distance from the end (0, 1, 2, 3+) beats one by distance
  from the start (0, 1, 2, 3+) by 0.1+ bits.
- **BB2** Replacing the four-way position class with distance-from-end (4 buckets) in the benchmark gains 0.05+ bits.
- **BB3** Absolute-discount (Kneser-Ney style) smoothing of the bigram beats add-one by 0.5+ bits.
- **BB4** Using that bigram in the benchmark instead of the add-one bigram inside the context model gains 0.1+ bits.
- **BB5** Backing off unknown and rare signs (fewer than 3 training tokens) to their catalogue block improves the
  benchmark on new F lines by 0.1+ bits.
- **BB6** Adding a line-length-conditioned position unigram (length 2, 3, 4, 5+ by position) gains 0.05+ bits.
- **BB7** Adding a 'next-to-last given last' reverse term is not possible left to right; instead, adding a unigram
  conditioned on the first sign of the line gains 0.05+ bits.
- **BB8** The best of these models scores under 4.8 bits per sign on held-out A + B lines.
- **BB9** The best model scores under 5.5 bits on new F lines.
- **BB10** The best model's gain over the benchmark on B (80/20) is positive.

## Results of the hundred-and-twenty-fifth set (added after the test; `predict_test125.py`, `results/predict_test125.md`)

Six held, four failed. Two structural facts and a better benchmark. Lines are anchored at their end: knowing how far a
sign is from the end predicts it 0.57 bits better than knowing how far it is from the start (BB1: 5.46 against 6.02).
Shape families carry over to unseen signs: backing off rare and unknown signs to their catalogue block improves new F
lines from 5.69 to 5.44 bits (BB5). Better smoothing (absolute discounting) lowers the bigram from 6.38 to 4.99 (BB3) and
the benchmark from 4.92 to 4.68 (BB4); with an extra end-distance term the best model reaches 4.66 bits per sign on
held-out A + B lines (BB8) and improves B too (BB10: 4.71 to 4.52). Line length, the first sign and a finer
end-distance term add nothing once position and context are in (BB2, BB6, BB7), and new F lines stay at 5.64 (BB9, not
under 5.5). New benchmark: 4.66 bits per sign held-out, 5.44 on new lines with block backoff. Tally, counting parts: 978
held, 948 failed (1926 registered).

# Hundred-and-twenty-sixth set, registered before testing (24 September 2026): is the line composed from the end? (nine hypotheses)

From the hundred-and-twenty-fifth set: lines are anchored at their end. Here: does knowledge flow backwards from the
end? Distinct lines (A + B) unless stated; same 80/20 split; best-model machinery of that set (discounted smoothing,
position and context terms, weights fitted on a training slice). p < 0.05 where tested.

- **RL1** Modelling lines end-to-start (reversed, with distance-from-start of the reversed line) beats the best
  start-to-end model by 0.05+ bits per sign.
- **RL2** The third-from-last sign is predicted from the last two (top-1, training counts) better than the third sign is
  from the first two, by 5+ points (lines of 4+).
- **RL3** B: RL2 holds.
- **RL4** F without copper: RL2 holds.
- **RL5** In name lines, per-position entropy (over distinct lines of 4+) is lowest at the last position and highest at
  the first.
- **RL6** Per-position entropy counted from the end rises over the last three positions (last < second-last <
  third-last).
- **RL7** In count lines (formulas with a numeral), the last position also has the lowest entropy.
- **RL8** Given the last sign, the second-last is predicted (top-1) better than the second sign given the first, by 5+
  points (lines of 3+).
- **RL9** B: RL8 holds.

## Results of the hundred-and-twenty-sixth set (added after the test; `predict_test126.py`, `results/predict_test126.md`)

Four held, five failed. The end anchoring is the ending itself plus the head: in names the last position has an entropy
of 1.41 bits against 5.6-6.2 at every position from the start (RL5), and the last two signs (head + ending) predict the
third-from-last far better than the first two predict the third (RL2: 36% against 23%; RL3 in B: 42% against 16%; RL4
in F': 31% against 22%), in line with the right-branching names found earlier. But reading end-to-start does not predict
better overall (RL1: 4.662 against 4.659), entropy does not keep falling toward the end beyond the last sign (RL6: 4.41,
6.43, 6.34), count lines are not end-fixed (RL7: last 5.56), and the last sign alone predicts its neighbour worse than
the first predicts the second (RL8: 25% against 33%; RL9 in B), because the last sign is usually 740, which says little
about what comes before it. Reading: no new mechanism; the line's end is fixed by its ending and the (head, ending)
pair selects the modifier. Tally, counting parts: 982 held, 953 failed (1935 registered).

# Hundred-and-twenty-seventh set, registered before testing (24 September 2026): the rare signs (ten hypotheses)

'Rare sign' = a non-numeral sign with 1-3 tokens in the distinct lines of the sample; 'common' = 20+. 'Frame-mates' of a
rare token = common signs seen in the same (previous, next) frame elsewhere. Blocks and catalogue numbers as in the
hundred-and-second set. Distinct lines (A + B) unless stated; F' = F without copper. 10,000-draw permutations (1,000
where marked); p < 0.05.

- **RA1** Frame-mates share the rare sign's block more often than random common signs do.
- **RA2** Frame-mates have catalogue numbers within 10 of the rare sign more often than random common signs do.
- **RA3** Rare-sign tokens are medial (neither first nor last) more often than common-sign tokens.
- **RA4** Rare signs stand next to another rare sign more often than within-line shuffles give (1,000).
- **RA5** Lines with a rare sign are longer than lines without (rank test).
- **RA6** Rare-sign tokens are at Mohenjo-daro more often than common-sign tokens (F').
- **RA7** 50%+ of rare signs have a common sign whose catalogue number differs by 1.
- **RA8** Under 5% of rare-sign tokens stand in the ending slot (directly before 740/520 at the line end, or as a
  closer).
- **RA9** B: RA1 holds.
- **RA10** F': RA4 holds (1,000).

## Results of the hundred-and-twenty-seventh set (added after the test; `predict_test127.py`, `results/predict_test127.md`)

Three held, seven failed. 304 signs have 1-3 tokens. The common signs found in the same frames as a rare sign belong to
its catalogue block (RA1: p = 0.003) and to its catalogue neighbourhood of +/-10 (RA2: p = 0.0001) more often than
random common signs do, so rare signs tend to stand where a sign of the same shape family would stand, weak support for
'rare sign = variant or compound of a family member' (not replicated in B: RA9, p = 0.07, where many rare signs are
merged). Lines with a rare sign are longer (RA5: 4.9 against 4.3). Otherwise rare signs behave like common ones: not
more medial (RA3, the other way), not clustered (RA4; RA10 in F'), not more Mohenjo-daran (RA6: 64% both), not usually
next to a common sign in the numbering (RA7: 16%), and 14% of their tokens stand in the ending slot as heads before an
ending or closer (RA8). Tally, counting parts: 985 held, 960 failed (1945 registered).

# Hundred-and-twenty-eighth set, registered before testing (24 September 2026): forbidden pairs and a family grammar (ten hypotheses)

Distinct lines (A + B) unless stated. 'Common' = non-numeral signs with 20+ tokens. Expected adjacency count of a pair =
(left count x right count) / total adjacencies. A 'gap' = a pair of common signs with expected 5+ and observed 0; an
'excess' pair = observed 5+ and at least 5 times expected. Blocks as before. 1,000 within-line shuffles where marked;
p < 0.05.

- **FA1** There are at least twice as many gaps as in within-line shuffles (mean over 1,000).
- **FA2** 50%+ of excess pairs involve an ending (740/520), a suffix (400/90/151) or a numeral.
- **FA3** 20%+ of common non-ending signs never directly precede 740.
- **FA4** Signs that precede 740 and signs that directly follow a numeral overlap at Jaccard 0.3 or less.
- **FA5** Block-level adjacency (block of left sign, block of right sign) carries mutual information beyond within-line
  shuffles (1,000).
- **FA6** Block-level adjacency MI is 20%+ of sign-level adjacency MI.
- **FA7** Gap pairs are same-block less often than excess pairs are.
- **FA8** B: FA1 holds.
- **FA9** F without copper: FA5 holds.
- **FA10** 30%+ of gaps involve a heading sign or a numeral.

## Results of the hundred-and-twenty-eighth set (added after the test; `predict_test128.py`, `results/predict_test128.md`)

Five held, five failed. The script has forbidden pairs: 20 pairs of common signs that chance would put together 5+
times never occur, 17 times more than in shuffled lines (FA1; B: 2 against 0.1, FA8). Examples: the fish 220, 240 never
directly before 390, and 233, 235, 240 never directly before 400; 125, 350 and 415 never directly before 740 (415 goes
before a fish instead). 26% of common non-ending signs never stand before 740 at all (FA3). Shape families have a weak
grammar of their own (FA5: block MI 0.13 bits, p = 0.001; FA9 in F'), but it is only 5% of the sign-level order
information (FA6), so order is mostly a matter of particular signs, not families. The strongest pairs are mostly not
grammatical-role pairs (FA2: 18% involve an ending, suffix or numeral; e.g. 176-100, 140-920, 142-615), the signs before
740 and after numerals overlap more than predicted (FA4: 0.36), gaps are not especially cross-family (FA7) and do not
mostly involve headings or numerals (FA10: 15%). Tally, counting parts: 990 held, 965 failed (1955 registered).

# Hundred-and-twenty-ninth set, registered before testing (24 September 2026): the strong pairs as compounds (ten hypotheses)

'Excess pairs' as in the hundred-and-twenty-eighth set (105 pairs, observed 5+ and 5x expected, A + B distinct lines).
Genres as in the hundred-and-eighth set; units as in the sixty-first; F' = F without copper. p < 0.05.

- **CW1** For 80%+ of excess pairs, the reverse order makes up under 5% of their combined adjacencies.
- **CW2** For 50%+ of excess pairs, the right member follows the left in 50%+ of the left member's tokens.
- **CW3** 60%+ of excess pairs occur in two or more genres.
- **CW4** 60%+ of excess pairs occur at both cities (F').
- **CW5** 70%+ of excess pairs occur twice or more in B.
- **CW6** 50%+ of excess pairs share a (previous, next) frame with some single common sign (they fill a one-sign slot).
- **CW7** 60%+ of excess pairs are units (pairs in 5+ distinct name bodies).
- **CW8** Under 20% of excess pairs contain 740 or 520.
- **CW9** 20%+ of excess pairs chain with another (one's right member is another's left member).
- **CW10** 60%+ of excess pairs occur in F' lines that are absent from A + B.

## Results of the hundred-and-twenty-ninth set (added after the test; `predict_test129.py`, `results/predict_test129.md`)

Six held, four failed. The 105 strong pairs are shared collocations, not fixed compounds. They cross genres (CW3: 70%),
are shared by the cities (CW4: 76%), recur in B (CW5: 87%), rarely include an ending (CW8: 12%), and nearly all chain
into longer sequences with other strong pairs (CW9: 91%). But their order is not rigid (CW1: 73% keep one order under 5%
reversal), the left member does not usually call the right (CW2: 10%), fewer than half are the name units (CW7: 39%), and
under half turn up again in the F lines that A + B lack (CW10: 41%). CW6 (99% share a frame with a single sign) holds
but is weak, since short frames such as line boundaries are shared by almost everything. Reading: frequent but loose
collocations that string together, consistent with the pairwise-precedence picture of earlier sets rather than a
lexicon of two-sign words. Tally, counting parts: 996 held, 969 failed (1965 registered).

# Hundred-and-thirtieth set, registered before testing (24 September 2026): material and size (twelve hypotheses)

Two ICIT record fields not used before: field 13 'material' (Steatite 1,846, Clay 495, Faience 425, Copper 218, ...;
'-' = missing) and field 31, read here as the object's main dimension in millimetres (seal median 26, tablet median
18; '0' = missing). The reading of field 31 as size is an inference from its values, not documented here. F objects
with the field present; genres, heading unit, motif as before. 10,000-draw permutations; p < 0.05; two-sided where marked.

- **MS1** On seals, text length correlates with size (Spearman 0.2+, significant).
- **MS2** Seals with the heading unit are larger than seals without (rank test).
- **MS3** Unicorn seals are larger than seals with other motifs (rank test).
- **MS4** Seals with a name line and seals with a closer line differ in size (two-sided rank).
- **MS5** Faience objects carry shorter texts than steatite objects (rank test).
- **MS6** Among tablets, genre depends on material (MI).
- **MS7** 50%+ of moulded tablets (TAB:B) with a material recorded are faience.
- **MS8** The 520 share of names differs between steatite and other materials (two-sided).
- **MS9** Seal size differs between Mohenjo-daro and Harappa (two-sided rank).
- **MS10** At Harappa, later seals are larger than earlier seals (rank test).
- **MS11** Among all objects with a size, count lines are on smaller objects than name lines (rank test).
- **MS12** Seals with a numeral formula are larger than seals with only a name (rank test).

## Results of the hundred-and-thirtieth set (added after the test; `predict_test130.py`, `results/predict_test130.md`)

Nine held, three failed. Two new variables (material, field 13; main dimension, field 31, read as millimetres) open a
physical side. Bigger seals carry longer texts (MS1: Spearman 0.42 over 1,545 seals), seals with the heading unit are
bigger (MS2: 28.1 against 26.9 mm), seals with a closer line are smaller than seals with a name line (MS4: medians 24.9
against 26.7), and Harappa's later seals are much bigger than its earlier ones (MS10: 29.9 against 23.2 mm), matching the
longer later texts of the eighty-fourth set. Faience objects carry shorter texts than steatite ones (MS5: 3.2 against
4.2 signs), moulded tablets are mostly faience (MS7: 409 of 590), tablet genre depends on material (MS6, p = 0.0001),
and names on steatite take 520 twice as often as names on other materials (MS8: 17% against 9%; steatite = seals, as
in the ninetieth set). Count lines sit on slightly smaller objects than name lines (MS11). Not supported: unicorn seals
larger (MS3, p = 0.14), different seal sizes between the cities (MS9: both median 26.7 mm), and counting seals being
larger (MS12, the other way). Tally, counting parts: 1005 held, 972 failed (1977 registered).

# Hundred-and-thirty-first set, registered before testing (24 September 2026): size beyond text length, and seal shapes (twelve hypotheses)

Size and material as in the hundred-and-thirtieth set. Length-controlled tests permute labels within strata of total
text length (2, 3, 4, 5, 6+ signs) and compare mean size; 10,000 draws; p < 0.05. SEAL:S (square) and SEAL:R
(rectangular) are ICIT's seal types.

- **SZ1** Headed seals are bigger than unheaded ones at equal text length.
- **SZ2** Closer seals are smaller than name seals at equal text length.
- **SZ3** At Harappa, later seals are bigger than earlier ones at equal text length.
- **SZ4** Text density (signs per mm) falls as seal size grows (Spearman between size and density negative, significant).
- **SZ5** Seals with a 520 name are smaller than seals with a 740 name at equal text length.
- **SZ6** Seals from the smaller sites are smaller than seals from the two cities (rank test).
- **SZ7** Lines on rectangular seals are longer than lines on square seals (rank test).
- **SZ8** Rectangular seals have no motif more often than square seals.
- **SZ9** Rectangular seals carry count formulas more often than square seals (lines).
- **SZ10** Rectangular seals are a larger share of seals at Harappa than at Mohenjo-daro.
- **SZ11** Moulded tablets are smaller than incised tablets (rank test).
- **SZ12** Copper tablets are larger than moulded tablets (rank test).

## Results of the hundred-and-thirty-first set (added after the test; `predict_test131.py`, `results/predict_test131.md`)

Eight held, four failed. The size differences between headed and unheaded seals and between closer and name seals are
due to text length: at equal length they vanish (SZ1: p = 0.74; SZ2: p = 0.15), and 520 seals are not smaller (SZ5).
Later Harappa seals are bigger even at equal length (SZ3: +6.7 mm, p = 0.0002), so seal size grew over time in its own
right; small seals pack signs tighter (SZ4), and seals from the smaller sites are smaller (SZ6: 24.8 against 27.7 mm).
Rectangular seals (SEAL:R) are a distinct kind: 96% have no picture against 5% of square seals (SZ8), their lines are a
little longer (SZ7: 4.8 against 4.4), they carry counts more (SZ9: 25% against 18%), and they are commoner at Harappa
(SZ10: 25% against 14% of seals). Copper tablets are the largest tablets (SZ12: 31.6 against 22.9 mm); moulded tablets
are larger than incised ones, not smaller (SZ11: 22.9 against 14.7). Tally, counting parts: 1013 held, 976 failed (1989
registered).

# Hundred-and-thirty-second set, registered before testing (24 September 2026): the rectangular seals (twelve hypotheses)

From the hundred-and-thirty-first set: rectangular seals (SEAL:R) are nearly always without a picture. F objects;
genres, heading unit, formula-only signs, size and material as before; lines distinct per object type. p < 0.05;
two-sided where marked.

- **RS1** Rectangular seal lines are name lines less often than square seal lines.
- **RS2** At Harappa, rectangular seals are later more often than square seals.
- **RS3** Rectangular seals are a larger share of seals at the smaller sites than at the two cities.
- **RS4** Names on rectangular seals take 520 less often than names on square seals.
- **RS5** Rectangular seal lines carry the heading unit less often than square seal lines.
- **RS6** Rectangular seal texts are one-off (one object) less often than square seal texts.
- **RS7** Rectangular seal lines hold a formula-only sign more often than square seal lines.
- **RS8** Rectangular seals are smaller than square seals (rank test).
- **RS9** Rectangular seal lines are closer lines more often than square seal lines.
- **RS10** Rectangular seal lines are bare lines more often than square seal lines.
- **RS11** 90%+ of rectangular seals with a material recorded are steatite.
- **RS12** The first sign depends on seal shape (MI over lines).

## Results of the hundred-and-thirty-second set (added after the test; `predict_test132.py`, `results/predict_test132.md`)

Five held, seven failed. Rectangular seals (256) differ from square ones (1,312) in content but not in circumstances:
fewer of their lines are names (RS1: 39% against 50%), their names take 520 less (RS4: 11% against 19%), they use
formula-only signs more (RS7: 27% against 21%), they are steatite (RS11: 93%), and their opening sign differs (RS12, p =
0.007). They are not later (RS2, p = 0.054), not more provincial (RS3), not less headed (RS5), not more repeated (RS6),
not smaller (RS8: larger, 29.3 against 26.7 mm), and do not carry more closers (RS9) or bare lines (RS10). Their genre
mix: names 101, counts 65, other 44, closers 25, bare 21 lines. Reading: a pictureless steatite seal type used a little
more for counts and formula words, not a separate period or region. Tally, counting parts: 1018 held, 983 failed (2001
registered).

# Hundred-and-thirty-third set, registered before testing (24 September 2026): the physical findings within each city (ten hypotheses)

Findings of the hundred-and-thirtieth to hundred-and-thirty-second sets (all F) re-tested inside Mohenjo-daro and
Harappa separately, and at the smaller sites where numbers allow. Size (field 31) and material (field 13) as before.
p < 0.05.

- **PH1** Mohenjo-daro: seal size correlates with text length (Spearman 0.2+, significant).
- **PH2** Harappa: the same.
- **PH3** Smaller sites: the same.
- **PH4** Mohenjo-daro: rectangular seals have no motif more often than square seals.
- **PH5** Harappa: the same.
- **PH6** Mohenjo-daro: names on steatite take 520 more often than names on other materials.
- **PH7** Harappa: the same.
- **PH8** Harappa: moulded tablets with a material are mostly faience (50%+).
- **PH9** Mohenjo-daro: faience objects carry shorter texts than steatite ones (rank test).
- **PH10** Harappa: the same.

## Results of the hundred-and-thirty-third set (added after the test; `predict_test133.py`, `results/predict_test133.md`)

Nine held, one failed. Inside each city the physical findings stand: bigger seals carry longer texts at Mohenjo-daro
(PH1: 0.40), Harappa (PH2: 0.49) and the smaller sites (PH3: 0.37); rectangular seals are pictureless at Mohenjo-daro
(PH4: 98% against 3%) and Harappa (PH5: 88% against 5%); Harappa's moulded tablets are mostly faience (PH8: 75%); faience
texts are shorter at both cities (PH9, PH10). The 520-steatite link holds at Mohenjo-daro (PH6: 17% against 3%) but not at
Harappa (PH7: 14% both), and at Mohenjo-daro the non-steatite names are mostly copper-tablet labels, which are almost all
740; so the hundred-and-thirtieth set's MS8 mainly reflects copper labels, not a steatite preference. Tally, counting
parts: 1027 held, 984 failed (2011 registered).

# Hundred-and-thirty-fourth set, registered before testing (24 September 2026): our genres against ICIT's text codes (ten hypotheses)

ICIT field 25 holds a text code per object (SS, SC, VN, MT, IT, SP, LP, NU, TS, LC, 2L, MS, ...), apparently the
database's own classification of the inscription; it is derived from the texts, so agreement is a validation of our
genres against an independent classifier, not new evidence about the script. Seen before registering: VN lines are
almost all our counts, NU lines are mostly potsherd graffiti. Lines of F objects; genres as in the hundred-and-eighth
set. Thresholds as stated.

- **IC1** Normalised agreement: MI(field 25, genre) / H(genre) is 0.3+.
- **IC2** 90%+ of VN lines are our counts.
- **IC3** 70%+ of LP, IT, SP and MT lines together are our names.
- **IC4** 80%+ of NU lines are made of numerals only.
- **IC5** 80%+ of TS lines are single signs.
- **IC6** 60%+ of LC lines are our counts.
- **IC7** 90%+ of 2L objects have two or more lines.
- **IC8** No single ICIT code holds 50%+ of our closer lines (the closer inscriptions are not an ICIT category).
- **IC9** 50%+ of our bare lines are coded SC.
- **IC10** No single genre holds 70%+ of SS lines.

## Results of the hundred-and-thirty-fourth set (added after the test; `predict_test134.py`, `results/predict_test134.md`)

All ten held. Our genres match ICIT's own text codes (field 25), a classification made independently of this project:
the mutual information is 38% of the genre entropy (IC1); VN lines are our counts (IC2: 95%), LP/IT/SP/MT lines our names
(IC3: 78%), NU lines numerals only (IC4: 86%), TS lines single signs (IC5: 99%), LC lines counts (IC6: 68%), 2L objects
two-lined (IC7: 97%), and our bare lines are mostly ICIT's SC (IC9: 67%). The closer inscriptions are not one of ICIT's
categories (IC8: spread over SS, IT, SP), and ICIT's SS is a mixed bag of our genres (IC10). This validates the genre
system against an outside classifier and marks the closer inscriptions as this project's addition. Tally, counting
parts: 1037 held, 984 failed (2021 registered).

# Hundred-and-thirty-fifth set, registered before testing (24 September 2026): does a proposed reading respect the structure? (ten hypotheses)

The ICIT dump used here carries, for 1,727 of 3,681 intact objects, a romanised reading (field 35, e.g. '235 740' ->
'amam', '590 390 740' -> 'varan') and a gloss (field 36) from a Sanskrit-based decipherment whose source is not
identified in this project. These tests ask only whether those readings respect structure found here; they say nothing
about whether the decipherment is right, and they do not endorse or reject its author. Readings are compared as
lower-case letter strings. 10,000-draw permutations; p < 0.05.

- **RD1** Readings of single-line texts ending in 740 share their final letter more often than readings of texts ending
  in other non-numeral signs (share of the commonest final letter).
- **RD2** The reading's final letter depends on whether the text ends in 740 or 520 (MI, permutation).
- **RD3** Identical texts receive identical readings in 95%+ of pairs.
- **RD4** Reading length in letters correlates with text length in signs (Spearman 0.5+, significant).
- **RD5** Texts sharing their first sign share the reading's first letter more often than random text pairs.
- **RD6** Texts sharing their last sign share the reading's last two letters more often than random text pairs.
- **RD7** Letters per sign vary little: coefficient of variation under 0.5 over texts of 2+ signs.
- **RD8** Among 2-sign texts 'X 740', 60%+ of readings end in the same two letters.
- **RD9** Texts that differ only in the heading sign (817/820/861 before the same rest) get readings that differ only
  in their first part (the rest of the reading identical) in 50%+ of pairs.
- **RD10** Count tokens (numeral + 700) with the same numeral get the same reading in 90%+.

## Results of the hundred-and-thirty-fifth set (added after the test; `predict_test135.py`, `results/predict_test135.md`)

Eight held, two failed, after a data fix: most field 35 values are cross-references ('ref:212.1' etc., pointing to
another object's reading), which the first run wrongly treated as readings (RD1 then showed 'f' as the commonest
'final letter'); the recorded run keeps only actual readings (1,653 single-line texts). The stored readings behave as
a sign-by-sign phonetic substitution: reading length tracks text length closely (RD4: Spearman 0.89) at a steady 1.8
letters per sign (RD7: CV 0.23), texts sharing a first sign share the reading's first letter (RD5: 0.93 against 0.12 by
chance) and texts sharing a last sign share its last letters (RD6: 0.58 against 0.11), and identical texts, heading
variants and count tokens read consistently (RD3, RD9, RD10, but on only 2-5 cases each). The two endings are read
differently (RD2, p = 0.0001). But the reading does not treat 740 as a fixed suffix: texts ending in 740 end in a, m or n
with no dominant sound (RD1: share 0.35 against 0.80 for other final signs), and 'X 740' readings do not end alike
(RD8: 47%). Since 740 is the most rigidly positioned sign in the script (almost never line-initial, fixed class per head,
followed only by suffixes), a reading that gives it a variable sound conflicts with the structure. This is a
consistency check only; it does not test the decipherment's correctness, and its source is not identified here.
Tally, counting parts: 1045 held, 986 failed (2031 registered).

# Hundred-and-thirty-sixth set, registered before testing (24 September 2026): the West Asian texts against the later grammar (ten hypotheses)

First of the external directions listed after the loop end. The West Asian texts (gulf.py's sample: F objects from the
Persian Gulf, Mesopotamia, Central Asia, or Susa / Luristan / Tepe Yahya; about 18 intact lines) were earlier found to
leave out the endings and use unfamiliar sequences (thought to write non-Indus names: Hunter 1932, Parpola 1994,
Laursen 2010, as summarised in gulf.py). Here they are tested against grammar found since. 'Home' = F without copper,
Indus-region sites, lines of 2+ signs, length-matched where stated. Small sample; p < 0.05.

- **WA1** West Asian lines end in the ending slot (740, 520 or a closer) less often than home lines of 2-8 signs.
- **WA2** No West Asian line ends in a closer.
- **WA3** 30%+ of West Asian first signs are never openers of home names.
- **WA4** Under 80% of West Asian last signs are home name heads (against 95% for held-out home names).
- **WA5** West Asian lines of 3+ signs contain a home name unit less often than home lines of 3+.
- **WA6** Under the benchmark model trained on home lines (hundred-and-twenty-fifth set), West Asian lines score 6.5+
  bits per sign (home new lines: about 5.4).
- **WA7** West Asian lines hold a numeral less often than home lines.
- **WA8** West Asian lines hold a fish sign as often as home lines (two-sided p >= 0.05).
- **WA9** The West Asian lines that end in 740 have a 740-class home head before it.
- **WA10** West Asian lines are longer than home lines (rank test).

## Results of the hundred-and-thirty-sixth set (added after the test; `predict_test136.py`, `results/predict_test136.md`)

Seven held, three failed (18 West Asian lines, so all effects are rough). The West Asian texts break the home grammar in
the ways foreign names should: they rarely end in the ending slot (WA1: 17% against 57%), start with signs that never
open home names in 39% (WA3), end in a home head in only 67% (WA4, against 95% for held-out home names), rarely contain
a home name unit (WA5: 20% against 50%), and the home benchmark model finds them hard to predict (WA6: 6.52 bits per
sign against about 5.4 for new home lines). They use fish signs as often as home texts (WA8), and the two lines that
end in 740 do so after 390, a regular 740-class head (WA9). One line ends in a closer (WA2 fails: '3 426'), and they
are not significantly longer (WA10). The new observation is WA7, the reverse of the prediction: 14 of 18 West Asian
lines contain a numeral sign against 56% at home, often inside the line ('924 1 319 31 55 2 150 416', '91 32 1 33',
'415 803 1 717 354'), so in texts thought to spell foreign names the stroke signs are used heavily, as if for sound
rather than count. This supports, weakly, the long-standing proposal that some stroke signs had phonetic (rebus)
values, and it is a lead for the language-type and decipherment tests that follow. Tally, counting parts: 1052 held,
989 failed (2041 registered).

# Hundred-and-thirty-seventh set, registered before testing (24 September 2026): sign shapes (ten hypotheses)

Second external direction: the glyphs themselves. Each sign is rendered from the ICIT webfont (sk_indus_script, the
codepoints in data/glyphs.tsv) at a fixed size and binarised. 'Shape similarity' of two signs = the best intersection-
over-union over shifts (cross-correlation); 'containment' of sign C in sign R = the best share of C's ink covered by
R's ink over shifts. 'Compound' = a rare sign (1-3 tokens in A + B distinct lines) that contains a common sign (20+
tokens) at 0.8+ with at least 20% more ink. Context similarity as in the sixty-second set. Random baselines are
frequency-matched where stated; p < 0.05. The font's drawings are one designer's normalised forms, not the originals.

- **SH1** Rare signs are compounds of a common sign more often than common signs contain another common sign.
- **SH2** A compound's base sign appears among its frame-mates (hundred-and-twenty-seventh set) more often than chance.
- **SH3** Shape similarity correlates with context similarity over pairs of common signs (Spearman, permutation).
- **SH4** Signs whose catalogue numbers differ by 1 are more similar in shape than random pairs (rank test).
- **SH5** The five candidate free variants (435/436, 526/527, 336/337, 554/555, 705/706) are more similar in shape than
  95% of random common-sign pairs, on average.
- **SH6** Fish signs are more similar in shape to each other than random matched sets.
- **SH7** Non-fish 520-class heads are more similar in shape to the fish than 740-class heads are (rank test).
- **SH8** The eleven closers are more similar in shape to each other than random matched sets.
- **SH9** Rare signs have more ink (a complexity proxy) than common signs (rank test).
- **SH10** A compound stands in its base sign's usual position class (first, middle, last) in 60%+ of its tokens.

## Results of the hundred-and-thirty-seventh set (added after the test; `predict_test137.py`, `results/predict_test137.md`)

Five held, five failed, on glyphs rendered from the ICIT webfont (normalised modern drawings, a limit on all of this).
The catalogue numbering does group signs by shape: neighbours by number look alike (SH4: IoU 0.37 against 0.19), which
confirms the reading of blocks as shape families used in earlier sets. The five candidate free variants look alike
(SH5: IoU 0.57 against 0.30 for the top 5% of random pairs), fish signs look alike (SH6, p = 0.001), and the eleven
closers look alike too (SH8: p = 0.01), so the endings found here form a shape family, not just a positional class.
Rare signs have more ink than common ones (SH9). But shape overall does not predict use: shape and context similarity
do not correlate over 1,500 pairs of common signs (SH3: 0.005), the non-fish 520 heads do not look like fish (SH7), and
the compound test gives nothing: rare signs contain a common sign no more often than common signs do (SH1: 17% against
11%, p = 0.13, with many 'bases' being the small sign 90, a sign of a crude method), the base is not among the
compound's frame-mates (SH2) and compounds do not keep the base's position (SH10). Tally, counting parts: 1057 held,
994 failed (2051 registered).

# Hundred-and-thirty-eighth set, registered before testing (24 September 2026): Parpola's, Mahadevan's and Knorozov's structural claims (ten hypotheses)

Third external direction: published decipherment claims, taken from the OCR text of Parpola 1994 (Deciphering the
Indus script, pp. ~180-200 and ch. 6; checked in the text, not from memory). Claims used: (a) Parpola: numeral + fish
sequences read as Dravidian star names; '6 + fish' (aru-min, Pleiades) is 'the most frequent sequence', '3 + fish'
(mu-m-min) 'next in frequency', and a large seal carries the sole text '7 + fish' (elu-min, Ursa Major); fish + fish
is an intensifying repetition; the sequences Num + fish 'belong together syntactically'. (b) Parpola, discussing the
Soviet team (Knorozov et al.): the frequent final sign ('jar', here 740) behaves as a case marker with a general
possessive function ('the possession of X' on seals), attributes precede the noun, and some prefixed signs are
optional. (c) Knorozov et al. as reported by Parpola: a stroke after the 'jar' marks the dative. Mapped onto ICIT
signs: fish = signs.FISH, 740 = the 'jar'; numeral values from numerals.NUMS. Runs directly after a heading sign are
left out (the confound found in the hundred-and-twelfth set). Distinct lines (A + B) unless stated. p < 0.05.

- **PA1** Value 6 is the commonest value of a numeral run directly before a fish.
- **PA2** Value 3 is the second commonest.
- **PA3** At least one object in F has as its whole text a numeral worth 7 followed by a fish.
- **PA4** Identical fish signs stand doubled (fish x + fish x) in 5+ distinct lines.
- **PA5** In name bodies holding both a numeral and a later fish, the numeral stands directly before a fish in 90%+.
- **PA6** 740 is line-final (allowing a following 400/90/151) more often on seals than on tablets (possession labels).
- **PA7** In 30%+ of 3+-sign bodies, dropping the opener leaves an attested body (optional prefixed signs).
- **PA8** Where a stroke '1' follows 740, the line ends within one more sign in 50%+ (a final case marker).
- **PA9** The roof fish (235, 236) is a name head (last body sign) at least as often as the plain fish 220 (two-sided
  p >= 0.05 counts as holding).
- **PA10** Fish are counted (numeral directly before) with value 6 or 7 in 20%+ of counted fish in F (Parpola's star
  groups as the common readings).

## Results of the hundred-and-thirty-eighth set (added after the test; `predict_test138.py`, `results/predict_test138.md`)

Three held, seven failed. Parpola's fish claims, checked on ICIT's transcription: the commonest numeral before a fish
is 2 (113 of 195 distinct lines, with heading-led runs already removed), not 6 (8 cases, sign 16 'three over three'),
so PA1 and PA10 fail (6 or 7 in 5% of counted fish in F); 3 + fish is second (PA2: 28), the sole-text seal '7 + fish'
exists (PA3: object 1070.1, '17 220'), and doubled fish occur (PA4: 8 lines). The difference with Parpola's 'most
frequent sequence' may come from sign identification (whether a given six-stroke form is recorded as one numeral sign
or as strokes of another value) or from his corpus (the 1982 concordance) against ICIT's; this set cannot tell which,
but in ICIT's data the pattern is 'two fish', not 'six fish'. The numeral stands directly before a later fish in 86% of
bodies (PA5, under 90%). The claims carried over from the Soviet team fail in their stated form: 740 is line-final on
seals no more than on tablets (PA6: 87% against 91%), prefixed signs are dropped in only 15% of bodies (PA7), a stroke
after 740 ends the line in only 6 of 18 cases (PA8), and the roof fish heads names far less than the plain fish (PA9:
7% against 28%; it acts as a modifier, not a separate star word). Tally, counting parts: 1060 held, 1001 failed (2061
registered).

# Hundred-and-thirty-ninth set, registered before testing (24 September 2026): a second transcription, Parpola's CISI (ten hypotheses)

Fifth external direction: a second corpus edition. The open digitisation of CISI (mayig/indus-valley-script-corpus,
MIT licence, commit ad2f1e2; `cisi.py` writes `data/cisi_mayig.tsv` and `data/cisi_signs.tsv`) covers Mohenjo-daro
M-1 to M-184: 179 sides, all joined to ICIT records by CISI number (field 1), 163 to intact F objects. Signs are
Parpola's numbers, mapped to ICIT glyphs only through the repository's own Mahadevan equivalents and
`data/icit_m77_map.tsv` (no alignment on these texts; 164 of the 182 Parpola signs used get an ICIT candidate).
A position 'agrees' when the ICIT glyph is among the Parpola sign's candidates. Sides containing P000 (damage) are
left out; an object's CISI text is its sides' lines concatenated; position-level tests use objects with one line in
both editions and equal length. Numeral values: R.NUMS of the mapped glyph. Distinct objects throughout. p < 0.05.

- **CS1** The two editions give the same number of signs for 70%+ of joined objects.
- **CS2** On equal-length single-line objects, 80%+ of positions agree.
- **CS3** Where ICIT has a numeral directly before a fish, CISI has a numeral of the same value there in 80%+
  (the '6 + fish' question of the hundred-and-thirty-eighth set is not one of transcription).
- **CS4** In CISI's own text of these objects, value 2 is the commonest numeral directly before a fish, as in ICIT.
- **CS5** The last sign agrees (same ICIT candidate) in 90%+ of joined single-line objects.
- **CS6** The jar (P324 = 740) is the commonest last sign of CISI lines, as 740 is in ICIT.
- **CS7** Positions CISI marks uncertain (uncertainty > 0) or damaged disagree more often than clear positions
  (Fisher).
- **CS8** Disagreements fall on rare signs: aligned positions whose ICIT glyph has fewer than 20 tokens in A disagree
  more often than the rest (Fisher).
- **CS9** CISI uses no more distinct signs over these objects than ICIT does over the same objects (Parpola's
  inclusive allographs).
- **CS10** The ending paradigm holds in CISI's text: of CISI lines whose last sign maps to 740 or 520 or a closer,
  the sign before it maps to a sign attested before that ending in the rest of ICIT (A + B minus these objects) in
  80%+.

## Results of the hundred-and-thirty-ninth set (added after the test; `predict_test139.py`, `results/predict_test139.md`)

Nine held, one failed. 157 joined intact objects (sides with P000 left out). The two editions agree closely on these
Mohenjo-daro seals: the same length in 96% (CS1), 92% of positions on 143 single-line objects (CS2), the last sign in
98% (CS5), the jar P324 the commonest last sign (CS6: 71 of 157). The ending paradigm holds in Parpola's text: the sign
before an ending is one ICIT attests there in 88% (CS10). CISI uses fewer distinct signs (CS9: 176 against 215;
Parpola's inclusive allographs). Disagreements fall on rare signs (CS8: 23% against 5%), not on the positions the
digitiser marked uncertain or damaged (CS7 fails, 9.5% against 8.2%); the commonest are P230/798, P201/65 and
P364/806, splits between near-identical signs.

**The '6 + fish' question.** CS3 and CS4 hold: the counted fish agree between editions (23 of 28), and in Parpola's
own CISI text of these objects the counts before a fish are 2 (13), 1, 3 (2 each), 14, 8, 4; no 6. The rarity of
'6 + fish' found in the hundred-and-thirty-eighth set is therefore not a matter of ICIT's sign identification, at
least on the 157 Mohenjo-daro seals CISI's digitisation covers; Parpola's 'most frequent sequence' must rest on
counting sequences rather than distinct texts, or on other sites, or on a wider sense of 'six'. Caveat: the
M77-to-ICIT half of the sign map was learned by alignment on the whole corpus, which includes these objects, so
agreement rates are an upper bound; the numeral and fish identities (P122 = 2, P126 = 6, P050 = 220) are not in
doubt. Tally, counting parts: 1069 held, 1002 failed (2071 registered).

# Hundred-and-fortieth set, registered before testing (24 September 2026): find spots inside Mohenjo-daro (ten hypotheses)

Sixth external direction: archaeological context. Periods and depths were used before (V1, V2, K8, U23, LB6-LB10);
the find spot inside the city was not. ICIT fields for Mohenjo-daro: 4 = area (DKG. (S), DKG. (N), DKC, HRA, HRB,
VSA, SD ...), 5 = block and house ('9VI' = block 9, house VI) or street, 6 = room/findspot. Intact F objects at
Mohenjo-daro (1,416). Major area = DK / HR / VS / SD / L / MN. Sub-area = field 4 with the generic values ('DK-',
'HR-', 'VS-', 'DKG', '--') left out. House = sub-area + field 5 where field 5 ends in a Roman numeral (618 objects in
176 houses). Names from R.names_in, genre from predict_test108.genre; one text per object (first line). Pair tests
compare the share of pairs in the same place against 1,000 permutations of the place labels over the objects in the
test; MI tests as rtools (1,000 permutations). p < 0.05.

- **FS1** Seals with the same whole text are found in the same sub-area more often than chance.
- **FS2** Seals whose names share a head (last body sign) are found in the same sub-area more often than chance.
- **FS3** Seals from the same house share at least one non-numeral sign more often than seals from different houses
  of the same sub-area (household vocabulary; permutation of house labels within sub-area).
- **FS4** The genre mix of seals (name / closer / count / bare / other) differs between major areas DK and HR (MI).
- **FS5** Copper tablets have a different sub-area distribution from seals (MI of type against sub-area).
- **FS6** Copper tablets with the same text are found in the same sub-area more often than chance.
- **FS7** Among seal names ending 740 or 520, the ending depends on sub-area (MI).
- **FS8** The seal motif (unicorn against other) depends on sub-area (MI).
- **FS9** Long seal texts (5+ signs) depend on sub-area (MI).
- **FS10** Seals found in streets and lanes (field 5 naming a street or lane) are names less often than seals found
  in houses (lost in public places versus kept at home; Fisher).

## Results of the hundred-and-fortieth set (added after the test; `predict_test140.py`, `results/predict_test140.md`)

One held, nine failed. 1,000 Mohenjo-daro seals with text, 800 with a sub-area, 502 in an identified house. Inside
the city, what a seal says does not follow where it was found: same-text seals are not significantly co-located
(FS1: 40 pairs, 40% in the same sub-area against 26%, p = 0.075), same-head names are not (FS2), seals from one house
share signs no more than seals from neighbouring houses (FS3: +0.012), and the genre mix (FS4), the 740/520 ending
(FS7), the unicorn motif (FS8) and text length (FS9) do not depend on the area. Street and lane finds are names as
often as house finds (FS10 fails: 57% against 51%). Copper tablets, by contrast, cluster (FS5 holds, MI 0.048, p =
0.0001): checked after the test, VS-A has 15 copper tablets against 44 seals (25%), the SD/L citadel mounds 7 against
19, DK-G North none against 87 seals and DK-G South 25 against 376. Identical copper texts are not co-located (FS6),
so the clustering is of the object type (workshops or deposits), not of texts. Reading: seals circulated and were lost
across the city independently of their text; a seal text is not tied to a neighbourhood or household in any way these
records can detect. Limits: sub-areas are excavation units, not social units, and the house labels are the
excavators'. Tally, counting parts: 1070 held, 1011 failed (2081 registered).

# Hundred-and-forty-first set, registered before testing (24 September 2026): language type from sign order (ten hypotheses)

Second external direction: typology. Head-final names, a suffix-like ending slot and the absence of concord are
established (Q1, H7, CG). These ten tests take order correlates the earlier sets did not run. The family expectations
come from standard typology (Dravidian: numeral before noun, genitive before the possessed, rigid agglutinative
suffix chains, plural suffix optional; Indo-Aryan: the same orders with obligatory number; Sumerian: noun before
numeral, genitive after the possessed, plural by reduplication) and are stated from general knowledge, not a
checked source: each result is an order fact first and a family indication second. Markers M = 740, 520, the closers
CL, 400, 90. Heads = last body signs of names. Distinct lines (A + B), distinct names. p < 0.05.

- **TY1** Numeral before the counted sign: in name bodies, numeral runs with a lexical (non-numeral, non-marker)
  sign directly after them outnumber runs with a lexical sign directly before and none after, by 2 to 1 or more.
- **TY2** Preposed genitive: where 740 stands inside a line and a lexical sign follows it, that sign is a head more
  often than lexical signs in other interior positions are (Fisher), and in 50%+.
- **TY3** Rigid marker order: of lines with two different markers, 95%+ have them in the majority order for their pair.
- **TY4** Reduplication exists: 1%+ of distinct lines have a non-numeral, non-marker sign doubled.
- **TY5** Reduplication marks nouns: the doubled sign's second copy is the name head in 50%+ of doubled cases.
- **TY6** Agglutinative chains: of lines ending in a marker, 1%+ have three or more markers after the last lexical
  sign.
- **TY7** Markers close the whole name, not its parts: 740 or 520 stands inside a name body (not last) in 2% or fewer
  of distinct names with 3+ body signs.
- **TY8** Openers are lexical, not a closed prefix class: the ten commonest openers of 3+-sign bodies cover less than
  50% of those bodies.
- **TY9** The counted sign is a head: in name bodies where a numeral run is directly followed by a lexical sign, that
  sign is the body's last sign (the head) in 50%+.
- **TY10** No number agreement: among names whose head is directly preceded by a numeral run, the ending (740 / 520
  / closer / none) does not depend on value 1 against 2+ (two-sided Fisher on 740 against the rest, p >= 0.05 holds).

## Results of the hundred-and-forty-first set (added after the test; `predict_test141.py`, `results/predict_test141.md`)

Four held, six failed. Deviation, fixed before recording: the first run counted numerals among the 'markers' after
the last lexical sign in TY6 (61 lines); counted as registered (markers only) it is 12 of 1,645 and fails.

What held: **numerals come before the counted sign** (TY1: 472 runs with a lexical sign after them against 106 with
one only before), the order of Dravidian and Indo-Aryan and against the noun-numeral order of Sumerian; **doubled
lexical signs exist** (TY4: 125 of 2,722 lines, 5%, but 58 of them are sign 615); **openers are an open class** (TY8:
the ten commonest cover 37% of 3+-sign bodies), so the front of a name is lexical, not a prefix paradigm; and **no
number agreement** (TY10: after a counted head the ending is 740 in 88% with value 1 and 87% with 2+).

What failed: no preposed genitive after an inner 740 (TY2: the sign after it is a head less often than other interior
signs, 62% against 79%); marker order is mostly but not fully rigid (TY3: 87%; 740/90 80:8 and 740 before 400 131:10
are the loose pairs); doubled signs are not heads (TY5: 11 of 36), so no Sumerian-type plural reduplication; no long
suffix chains (TY6: two markers at most in all but 12 lines), a fixed slot rather than open agglutination; 740 or 520
inside a body in 3% of 3+ names (TY7, over 2%); and the counted sign is the head in only 37% (TY9): numeral +
sign is usually a modifier inside the name, not the name's head.

Typology, as far as order can show it: numeral-first, head-final, no number or class agreement, a short and closed
ending slot. That fits a Dravidian-like or Indo-Aryan-like order and not Sumerian's, but none of it separates
Dravidian from Indo-Aryan, and the family expectations were stated from general knowledge. Tally, counting parts:
1074 held, 1017 failed (2091 registered).

# Hundred-and-forty-second set, registered before testing (24 September 2026): line breaks as word boundaries (eight hypotheses)

Parpola used line division as evidence for segmentation; it was never measured here. Sample: distinct intact F texts
with two or more non-empty lines (77). The order of lines is not reliable (the pair '31 32' stands first on some
objects and last on others), so every hypothesis is tested twice, with the lines as listed and reversed, and holds
only if it holds both ways. Chance: each junction is moved to a uniformly drawn interior position of the same
concatenated text (10,000 draws; one-sided p). Units U = predict_test61.units of name bodies (pairs in 5+ bodies);
bound pairs = predict_test8.bound_pairs (30 highest-PMI pairs). Markers M = 740, 520, closers CL, 400, 90. Genre as
predict_test108. p < 0.05.

- **LK1** Junctions split a unit pair less often than chance.
- **LK2** Junctions split a bound pair less often than chance.
- **LK3** Lines are well-formed texts on their own (genre name, closer, count or bare) more often than the segments
  of random cuts.
- **LK4** Lines end in a marker more often than random segments do.
- **LK5** Junctions separate a numeral from the sign after it less often than chance.
- **LK6** Two-line texts of 4+ signs are unbalanced (lines differ by 2+ signs) in 50%+ (syntax over layout).
- **LK7** 20%+ of multi-line texts have a line made only of numerals (a separate count line).
- **LK8** Where one line of a two-line text is a name (ends 740/520), the other line is not a name in 70%+ (the lines
  are separate fields, not one name wrapped).

## Results of the hundred-and-forty-second set (added after the test; `predict_test142.py`, `results/predict_test142.md`)

Six held, two failed. 77 multi-line texts, 81 junctions; every chance comparison run with the lines as listed and
reversed. **Line breaks respect the units found by statistics alone.** No junction splits a bound pair (LK2: 0
against about 5 by chance, either order), junctions split a name unit 4 times as listed and never reversed against
8-9 by chance (LK1), each line is a well-formed text on its own (LK3: 120 lines against 79 and 94) and lines end in a
marker twice as often as random segments (LK4: 64 against 32 and 52). Lines are unbalanced in 70% of two-line texts
(LK6), so the break follows the syntax, not the space. Where one line is a name, the other is not a name in 42 of 43
(LK8): the second line is a separate field (a closer such as 621, a title-like 790 / 930 / 817, or strokes like
'31 32'), not a wrapped name. Failed: numerals are separated from the next sign no less than chance (LK5: 7 against
10, few cases) and numeral-only lines are 13% (LK7). This is the first check of the segmentation from outside the
sign statistics: the scribes' own line breaks fall where the units say word boundaries are. Tally, counting parts:
1080 held, 1019 failed (2099 registered).

Correction (added after recording, same day): the registration said line division 'was never measured here'; that
came from a stale remark in the seventh set's text. Line breaks were tested before: X1/X2 (seventh set: the 30 bound
pairs never split, 0 of 31; heading/ending boundaries no more than random), RB, U10 and J7 (M77 multi-line texts).
LK2 is therefore a replication of X2 on F. New here: LK1 (name units), LK3 (each line a well-formed text), LK4 (lines
end in markers; X1 measured heading/ending boundaries, not line ends), LK6 and LK8. LK5 fails on F where J7 held on
M77 (numeral + next sign split 6.1%): the two samples disagree, with few cases in F (7 junctions).

# Hundred-and-forty-third set, registered before testing (24 September 2026): numerals used for their sound (six hypotheses)

The West Asian texts use strokes heavily (set 136), the sign after a numeral is usually not the name head (TY9) and
'2 + fish' dominates beyond what counting explains (PA1). If numerals also served for their sound (Parpola's
homophone argument), numerals inside names should behave partly like ordinary signs. Distinct lines (A + B) and
distinct names; numeral runs as predict_test112.runs, values as R.NUMS; lexical = not a numeral and not a marker (740,
520, closers, 400, 90). A run 'counts' when a lexical sign follows it in the body; it is a 'head' when it ends the
body. Frames are (previous, next) signs in the line, '#' at the line edges. MI tests as rtools (permutation).
p < 0.05.

- **NP1** Numeral tokens in names stand in frames that also host a lexical sign more often than numeral tokens in
  count texts (genre 'count') do (Fisher).
- **NP2** Of minimal pairs of distinct equal-length name bodies differing at one position that holds a numeral in at
  least one of them, 30%+ have a lexical sign in the other.
- **NP3** The value of a numeral run in a name depends on whether it counts or is the head (MI).
- **NP4** Before a fish, the value depends on which fish follows (lexicalised numeral + fish words; MI).
- **NP5** Before other lexical signs with 5+ counted occurrences, the value depends on the sign (MI).
- **NP6** 5%+ of names that contain a numeral have a numeral run as their head.

## Results of the hundred-and-forty-third set (added after the test; `predict_test143.py`, `results/predict_test143.md`)

Five held, one failed. **Numerals behave partly like words, not only like counts.** In minimal pairs of name bodies,
a numeral alternates with a lexical sign in 935 of 1,008 pairs (NP2) and with another numeral in only 63. Caveat, noted
after the test: NP2 was registered without a chance baseline. Numerals are 16.6% of body tokens, so a pure 'any sign
can replace any sign' model would give about 17% numeral partners; the observed 6% is lower. The numeral position is
therefore not a closed count slot where values swap for values, but the alternation may be 'count present / count
absent' constructions rather than rebus spellings. The value depends on its role (NP3: heads against counting runs,
MI 0.087, p = 0.0001), on which fish follows (NP4: MI 0.35, p = 0.008) and on which other sign follows (NP5: 19
signs, MI 1.10, p = 0.0001): numeral + sign pairs are lexicalised, fixed words rather than free counts. Numerals are
the head of 23% of names that contain one (NP6: 119 of 509, mostly the long pair 32 before 740, e.g. '15 32 740',
'14 32 740'), a numeral standing where a noun stands. Failed: numeral tokens in names do not share frames with
lexical signs more than numerals in count texts do (NP1: 47% against 50%). Reading: consistent with numerals as
words or word parts (number words used in names, or phonetic values) and against a purely arithmetic use inside
names; it does not yet show a phonetic value, because lexicalised numeral compounds (as in Parpola's star names) give
the same pattern. Tally, counting parts: 1085 held, 1020 failed (2105 registered).

# Hundred-and-forty-fourth set, registered before testing (24 September 2026): does the ending slot change over time? (eight hypotheses)

Name length and first/last-sign drift were tested across levels (K8, U23), the ending paradigm never. Levels: early /
late as predict_test18.level (Mohenjo-daro Early + Intermediate against Late, field 9; Harappa 3B against 3C and Vats
strata), F objects without copper tablets, one text per object and level (distinct (text, site, level)). Harappa fine
periods from field 8 (3A = 1, 3B = 2, 3C and 3C-n = 3, 4 = 4, 5 = 5; 'Period 3', '3B/C' left out). Differences are
late minus early, with the level labels permuted within site (10,000 draws, two-sided). p < 0.05.

- **TM1** The share of 520 among names ending 740 or 520 changes between early and late.
- **TM2** The share of closer-genre texts changes.
- **TM3** The share of names with 400 or 90 after the ending changes.
- **TM4** The share of 740 names followed by a stacking closer changes.
- **TM5** Heads with 3+ names in both levels keep their majority ending (740 or 520) in 90%+ (a stable lexical class).
- **TM6** Heads first seen in the late level take 740 at the same rate as older heads (two-sided p >= 0.05 holds:
  the paradigm is productive).
- **TM7** At Harappa, the 520 share has a monotone trend over the fine periods (Spearman with period, permutation).
- **TM8** The share of count-genre texts changes.

## Results of the hundred-and-forty-fourth set (added after the test; `predict_test144.py`, `results/predict_test144.md`)

None held, eight failed. Deviation, fixed before recording: the first run took TM4's 740 texts from name_of, which
drops texts ending in a stacking closer other than 151; rerun on texts where 740 is followed only by markers (the
registered sense). Result unchanged (fails).

1,029 distinct (text, site, level) at Mohenjo-daro and Harappa. **The ending slot does not change between early and
late levels**: the 520 share (TM1: 16.1% against 14.3%), closer texts (TM2: 8.6% against 8.3%), 400/90 after the
ending (TM3: 21% against 16%, p = 0.16), stacking closers (TM4: 2.8% against 2.4%) and count texts (TM8: 19% against
18%) are flat, and there is no trend over Harappa's fine periods (TM7: 520 share 4/26, 25/125, 1/5, 0/3). Heads keep
their majority ending in 17 of 19 (TM5, just under 90%). **TM6 fails the informative way**: heads first seen in the
late level take 740 in 34 of 34 names, against 83% for heads already attested (p = 0.007). New names are made with 740;
the 520 class does not grow. This is the diachronic form of the finding that the 520 class is lexical: 740 is the
productive default, 520 a closed set of old heads. Reading: the ending slot is a stable convention over the period the
levels cover (generations, not centuries of language change); if it wrote grammatical endings, the grammar did not
move in that span. Tally, counting parts: 1085 held, 1028 failed (2113 registered).

# Hundred-and-forty-fifth set, registered before testing (24 September 2026): Mahadevan 2014, the 'merchant of the city' phrase (eight hypotheses)

First external direction, follow-up. Claims taken from the text of Mahadevan 2014 (Dravidian Proof of the Indus
Script via the Rig Veda, Bulletin of the Indus Research Centre 4; read in the PDF, Section I and Section III
notes), not from memory. His gender reading of the endings was tested before (X8-X10) and is not repeated. Claims:
(a) the four-sign sequence A B C D (WOLF, HOOK, CROSSROADS, JAR = ICIT 255 435 690 740, as mapped in the eighth
pass) 'can occur as a complete text, also more often as part of longer inscriptions'; (b) it is 'an integral
linguistic unit', subdivided into AB and CD, with AB 'an attribute qualifying CD', C the root and D its suffix;
(c) the Indus texts 'consist mostly of word signs depicting names and titles'; (d) the JAR-BEARER sign (M015 = ICIT
154-158) and the BEARER (M012 = ICIT 151) are names (a seer; a dynasty). Distinct lines (A + B); F for sites. p < 0.05.

- **MH1** ABCD is a complete text in at least one distinct line, and more of its distinct lines are longer texts
  than complete texts.
- **MH2** The phrase splits AB | CD: AB occurs without CD, and CD without AB, each in 3+ distinct lines.
- **MH3** AB qualifies other heads: AB directly before a head other than 690, followed by 740, in 3+ distinct lines.
- **MH4** The junction B-C (435-690) is the weakest of the three (lowest PMI over distinct lines).
- **MH5** Inside longer texts, ABCD is final (followed only by markers or nothing) in 80%+.
- **MH6** The bearer signs (151, 154-158) are name heads (last body sign before 740 or 520) in 50%+ of their tokens
  in distinct lines.
- **MH7** 'Mostly names and titles': 50%+ of distinct seal lines in F are names (genre 'name') or closers.
- **MH8** As a title ('merchant of the city') the phrase occurs at 2+ sites in F and after 5+ different preceding
  signs.

## Results of the hundred-and-forty-fifth set (added after the test; `predict_test145.py`, `results/predict_test145.md`)

Four held, four failed. The phrase 255 435 690 740 is in 22 distinct lines. Held: it is a complete text once and
part of a longer text 21 times (MH1); it splits into AB and CD, each recurring without the other (MH2: AB alone 20,
CD alone 12); seal lines are mostly names or closers (MH7: 59%); and the phrase occurs at three sites (Mohenjo-daro
21, Harappa 5, Kalibangan 1) after 9 different preceding signs (MH8), as a title or a name part used by many.
Failed: AB never qualifies another head before 740 (MH3: 0), so 'AB is an attribute of CD' is not shown by AB
modifying anything else; instead AB's other partner is a bearer closer ('255 435 156', '255 435 154', '255 435 156
400'), so AB is a unit that takes either 690 740 or a closer. The B-C junction is not weaker than A-B (MH4: PMI 4.96
against 4.98; the weak junction is C-D, 1.87, because 740 is everywhere), the phrase ends the text in 76% (MH5, just
under 80%; it is followed by counts '900 1 3 42x' or a second name on the rest), and the bearer signs he reads as
names (151, 154-158) are almost never name heads (MH6: 1 of 196): they are closers, as the grammar already had them.
Reading: Mahadevan's phrase is a real recurring unit across sites, but its internal structure is AB + (CD or closer),
not attribute + suffixed root, and his bearer readings conflict with how the bearer signs are used. Tally, counting
parts: 1089 held, 1032 failed (2121 registered).

# Hundred-and-forty-sixth set, registered before testing (24 September 2026): scribal workshops (nine hypotheses)

H9 found the candidate graphic variants no more site-dependent than random pairs. This set asks the same inside
cities, in time, by medium and inside one object, and uses the CISI allograph feature vectors (set 139). Variant pairs:
the candidate pairs of results/allographs.md with 5+ tokens on each side in F. Places: Mohenjo-daro sub-area and house
as the hundred-and-fortieth set; Harappa field 4 (excavation unit, '--' left out). Tokens are sign occurrences on F
objects. Pooled statistics sum MI (variant against place) over pairs; chance permutes the variant labels within each
pair (2,000 draws). CISI features: the full feature vector after the three default features, per Parpola sign.
p < 0.05.

- **WS1** At Mohenjo-daro the variant chosen depends on the sub-area.
- **WS2** At Harappa the variant chosen depends on the excavation unit.
- **WS3** At Mohenjo-daro, two tokens of one pair from the same house share the variant more often than two tokens
  from different houses of the same sub-area.
- **WS4** The variant depends on the level (early / late, predict_test18.level; permuted within pair and site).
- **WS5** The variant depends on the object type (seal / tablet / other).
- **WS6** On one object, two tokens of one pair use the same variant more often than chance.
- **WS7** Different objects with the same text use the same variant more often than random pairs of objects that
  both carry that pair.
- **WS8** In CISI, the allograph feature vector of a Parpola sign depends on the Mohenjo-daro sub-area.
- **WS9** In CISI, two tokens of one Parpola sign on one object share the feature vector more often than two tokens on
  different objects.

## Results of the hundred-and-forty-sixth set (added after the test; `predict_test146.py`, `results/predict_test146.md`)

Five held, four failed. 29 candidate variant pairs, 2,768 tokens in F; `cisi.py` now also stores the CISI allograph
features (column 'features'; set 139 reproduces unchanged). Held: the variant depends on the Mohenjo-daro sub-area
(WS1: p = 0.008) and on the medium (WS5: seal / tablet / other, p = 0.0005); tokens on one object agree more than
chance (WS6: 77 pairs, +0.074, p = 0.049), different objects with the same text agree more (WS7: +0.135, p =
0.0005), and in CISI two tokens of one Parpola sign on one object share their allograph features far more than tokens
on different objects (WS9: +0.40, p = 0.0005, but only 12 same-object pairs). Failed: no Harappa unit effect (WS2),
no house effect (WS3), no change over levels (WS4), no CISI allograph effect by sub-area (WS8).

Caveats, noted after the test: (1) several candidate pairs are different fish (220~233, 235~240, 220~231) whose
choice may be lexical, so WS1 and WS5 can reflect vocabulary by area and by medium rather than hands; (2) many
same-text objects are moulded or stamped copies, so WS7 is partly mechanical; (3) WS6 is borderline. What survives
is consistent with writing habit at the level of the object and the maker (one hand, one form; copies keep the form)
and a weaker area effect at Mohenjo-daro, with no trace of households and no drift in time. Tally, counting parts:
1094 held, 1036 failed (2130 registered).

# Hundred-and-forty-seventh to hundred-and-fifty-first sets, registered together before testing any of them (24 September 2026)

Five sets, registered in one commit and tested one after another. Common conventions: distinct lines (A + B) unless
stated; F objects without copper tablets unless stated; names = R.name_of (body, ending); head = last body sign;
closers CL; markers M = 740, 520, CL, 400, 90; lexical = not a numeral and not a marker. p < 0.05.

## Hundred-and-forty-seventh set: how many names existed (capture-recapture; seven hypotheses)

The structure never separated personal names from titles. Two cities are treated as two independent catches of the
name population: Mohenjo-daro seals and Harappa seals in F (1,279 seals between them). A whole name is (body,
ending). Chapman's bias-corrected Lincoln-Petersen estimate N = (n1 + 1)(n2 + 1)/(m + 1) - 1 over distinct names per
city; Chao1 = S + f1^2 / (2 f2) over the number of seals carrying each name.

- **CR1** The Lincoln-Petersen estimate of whole names is at least 3 times the number of distinct names observed in the
  two cities (a large population, as personal names would give).
- **CR2** Chao1 over whole names (both cities pooled) is at least 2 times the observed number.
- **CR3** For heads, the Lincoln-Petersen estimate is at most 1.5 times the observed number of distinct heads (heads are
  a closed vocabulary, nearly all seen).
- **CR4** 60%+ of distinct whole names are on exactly one seal.
- **CR5** Names found in both cities end in 520 more often than names found in one (Fisher).
- **CR6** Names found in both cities have shorter bodies than names found in one (rank test).
- **CR7** Chao1 over heads is at most 1.5 times the observed number of distinct heads.

## Hundred-and-forty-eighth set: productivity of the endings (seven hypotheses)

TM6 found that new late heads all take 740. Productivity (Baayen): P = hapax heads / names, where a hapax head is a head
seen in exactly one distinct name. Closer names: distinct lines ending in a closer (optionally + 400) with 1+ sign
before it and no 740/520; their 'head' is the sign before the closer. Chance for P differences: ending labels
permuted over names (10,000 draws, one-sided).

- **PV1** P for 740 names is higher than for 520 names.
- **PV2** Hapax heads take 740 more often than other heads (Fisher, 740 against 520).
- **PV3** Rarefied to the number of 520 names, 740 names show more distinct heads than 520 names in 95%+ of 1,000
  draws.
- **PV4** P for closer names is lower than for 740 names.
- **PV5** 740 name bodies are longer than 520 name bodies (rank test).
- **PV6** Heads seen at one site only (F) take 740 more often than heads seen at two or more sites (Fisher).
- **PV7** Of hapax heads of 740 names, 50%+ are rare signs (fewer than 10 tokens in A + B).

## Hundred-and-forty-ninth set: a closer as a head and its ending in one sign (five hypotheses)

From set 145: '255 435' takes '690 740' or a bearer closer. A stem is the part of a line before a closer (closer
lines as PV) or before the head of a 740 or 520 name; stems must be non-empty.

- **CF1** Closer stems are also attested as stem + X + 740 in a larger share than 520-name stems are (Fisher).
- **CF2** For stems attested both ways, the commonest X of each closer covers 50%+ of that closer's stems (pooled over
  closers with 3+ such stems).
- **CF3** That share is higher than when closer labels are permuted among the stems (1,000 draws).
- **CF4** For the bearer closers (154, 156), X = 690 in 50%+ of their stems attested both ways.
- **CF5** Closer stems are as long as 740 bodies minus the head (rank test, two-sided p >= 0.05 holds).

## Hundred-and-fiftieth set: numeral compounds as a shared vocabulary (five hypotheses)

From set 143: numeral + sign pairs are fixed. Compound = the last numeral of a run + the lexical sign after it, with
3+ distinct lines. Controls: lexical + lexical bigrams, each compound matched to the bigram(s) nearest in distinct-line
frequency (ties: all, averaged). Sites and object types from F (all objects).

- **NC1** Compounds occur at more sites than matched bigrams (paired sign test).
- **NC2** Compounds occur on more object types (seal / tablet / other) than matched bigrams (paired sign test).
- **NC3** A larger share of compounds than of matched bigrams occurs at both Mohenjo-daro and Harappa.
- **NC4** Compounds recur at the smaller sites (outside Mohenjo-daro and Harappa) more often than matched bigrams.
- **NC5** For lexical signs counted at both Mohenjo-daro and Harappa, the commonest numeral value before them is the
  same in both cities in 70%+.

## Hundred-and-fifty-first set: copper tablets by area (five hypotheses)

From set 140: copper tablets cluster by area. Mohenjo-daro copper tablets in F with a sub-area (65 of 197; small).
Picture = field 18 ('None' = no picture). Pair tests as the hundred-and-fortieth set (1,000 permutations).

- **CU1** The picture depends on the sub-area (MI).
- **CU2** Having a picture depends on the sub-area (MI).
- **CU3** Same-picture copper tablets share a sub-area more often than chance.
- **CU4** Copper tablets from the same sub-area share a sign more often than tablets from different sub-areas.
- **CU5** Copper tablets from the same sub-area share a level (early / late) more often than chance.

## Results of the hundred-and-forty-seventh set (added after the test; `predict_test147.py`, `results/predict_test147.md`)

Five held, two failed. 1,279 Mohenjo-daro and Harappa seals; 475 and 130 distinct names, 20 in both cities.
**Whole names are a large, open population; heads are a small, closed one.** The Lincoln-Petersen estimate of whole
names is about 2,970 (CR1: 5.1 times the 585 seen) and Chao1 about 5,540 (CR2: 9.5 times; 536 names on one seal, 29
on two); 92% of names are on exactly one seal (CR4). Heads are nearly all seen: Lincoln-Petersen 147 against 129
observed (CR3: 1.14 times), Chao1 216 (CR7 fails, 1.68 times, just over 1.5). The 20 names found in both cities are
short (CR6: mean body 1.75 signs against 4.08), mostly a head alone + ending ('176 740', '388 740', '705 33 520'), and
are 520 names no more often than others (CR5 fails: 20% against 18%).

Reading: this is the pattern of personal names (or individual holders) built from a finite stock of name elements:
thousands of distinct combinations, each on one seal, over a closed vocabulary of about 150-220 heads; the names
shared between cities are the short ones any combinatorial system repeats by chance or convention. It counts against
the names being a small set of titles or offices, which would recur across seals and cities. Caveats: Lincoln-Petersen
assumes the two cities sample one population with equal catchability; local name fashions (different heads
preferred in each city) reduce the overlap and inflate the estimate, so the numbers are upper-side estimates. The
order of magnitude (thousands against hundreds) is the result. Tally, counting parts: 1099 held, 1038 failed (2137
registered).

## Results of the hundred-and-forty-eighth set (added after the test; `predict_test148.py`, `results/predict_test148.md`)

Three held, four failed. Names: 740 926, 520 163, closer 226; hapax heads (one distinct name in the whole pool; the
registered wording, not Baayen's per-ending count) 91. **The 520 class is narrow; 740 takes the rare and local
heads.** At equal size 740 names always show more distinct heads than the 163 520 names, which use only 26 (PV3:
1,000 of 1,000); heads found at one site only take 740 in 93% against 84% (PV6, p = 0.006); and 77% of hapax heads of
740 names are rare signs (PV7). Baayen's P does not separate the endings (PV1: 0.066 against 0.043, p = 0.18; PV2: 90%
against 85%, p = 0.17): hapax heads are too few (91) for the test to have power. Closer 'heads' (the sign before the
closer) are more varied than 740 heads (PV4 fails the other way, 0.102), a sign that the sign before a closer is not a
head in the same sense. 740 and 520 bodies are the same length (PV5). Reading, with TM6 (all new late heads take 740):
740 is the open ending that new, rare and local heads go to; 520 is a small fixed set of widespread heads. The
productivity measure itself is underpowered here. Tally, counting parts: 1102 held, 1042 failed (2144 registered).

## Results of the hundred-and-forty-ninth set (added after the test; `predict_test149.py`, `results/predict_test149.md`)

One held, four failed. **A closer is not a fused head + 740.** Closer stems are no more often attested as stem + X +
740 than 520 stems are (CF1: 16% against 21%). Of 49 stems attested both ways, a closer's commonest X covers only 39%
(CF2), no better than closer labels shuffled (CF3: p = 0.07); the bearer closers 154 and 156 alternate with X = 900
(7), 752 (4), 760 (3) and only 3 times with 690 (CF4: 14%), so the '255 435 156' / '255 435 690 740' alternation of set
145 is one case, not a rule. What holds: the part before a closer is as long as a 740 body minus its head (CF5: 3.02
against 2.97), i.e. a closer takes the place of head + ending in length, without replacing any particular head.
Reading: closers fill the slot of a whole head + ending but are their own words (as the alternative-closer sets had
them, each with its own heads), not abbreviations of a titled noun; it gives no support to reading the bearer signs
as 'merchant' or any other specific head. Tally, counting parts: 1103 held, 1046 failed (2149 registered).

## Results of the hundred-and-fiftieth set (added after the test; `predict_test150.py`, `results/predict_test150.md`)

One held, four failed. 112 numeral compounds (3+ distinct lines), each matched to lexical bigrams of the nearest
frequency. Compounds reach more sites than matched bigrams (NC1: 2.58 against 2.19, 76 higher, 33 lower, p <
0.0001), but they are not on more object types (NC2), not more often in both cities (NC3: 0.62 against 0.59) and not
significantly more at the smaller sites (NC4: 0.55 against 0.40; the sign test loses power on fractional matched
means). **The value before a given sign is not the same in the two cities** (NC5 fails: the commonest value agrees for
27 of 69 signs counted in both, 39%; for example 390 takes 6 at Mohenjo-daro and 3 at Harappa, 125 takes 2 and 13,
760 takes 1 and 6; the fish 235 and 240 take 2 in both). Reading, with set 143: numeral + sign pairs are fixed within
each city but the fixing differs between cities, so they are not a shared vocabulary of number words (star names,
measures) across the civilisation; the exceptions are the stroke-pair fish '2 235' / '2 240', which are the same
everywhere. That fits local naming customs (or local counting conventions) more than common words. Tally, counting
parts: 1104 held, 1050 failed (2154 registered).

## Results of the hundred-and-fifty-first set (added after the test; `predict_test151.py`, `results/predict_test151.md`)

Three held, two failed; small sample (65 copper tablets with a sub-area). The picture depends on the area (CU1: MI
1.13 bits over 63 tablets, p = 0.0001), and so does having a picture at all (CU2: p = 0.005); same-picture tablets
share an area more than chance (CU3: 21% against 15%, p = 0.04). Checked after the test: DK-G South has mostly
text-only tablets (16 of 25) and no animal picture except one tiger; VS-A has the animal set (elephant 3, gaur, hare,
anthropomorph, composite, loop); the SD/L citadel mounds carry anthropomorphs, composites, hare and gaur. Texts do
not cluster by area (CU4: shared signs -0.04) and the tablets of one area are not from one level (CU5: 0.487 against
0.487, 25 tablets with a level). Reading: copper tablets were made or kept as picture sets in particular parts of the
city (text-only ones in DK-G South, the animal series in VS-A and on the citadel), across levels; their texts vary
within each set. This adds a place to the copper tablets' picture-set organisation (LB, CT sets) but says nothing new
about the texts. Tally, counting parts: 1107 held, 1052 failed (2159 registered).

# Hundred-and-fifty-second to hundred-and-fifty-sixth sets, registered together before testing any of them (24 September 2026)

Five sets that check and build on the hundred-and-forty-seventh set (names: a large open population over a closed
stock of heads). Conventions as sets 147-151. p < 0.05.

## Hundred-and-fifty-second set: the capture-recapture method on Linear B (six hypotheses)

Control on a read script. Data: DAMOS (CC BY-NC-SA; `scratchpad/linb`, collected 23 Sept), Knossos and Pylos
documents, clean complete word tokens. Word classes from the Tiripode lexicon definitions (exact word forms):
persons = definition names 'anthroponym' and not 'occupation', 'title', 'anthroponym or', 'or anthroponym',
'anthroponym?'; titles = definition names 'occupation' or 'title' and not 'anthroponym'. Catches: the distinct words
of each class at Knossos and at Pylos. Chapman's Lincoln-Petersen as set 147; 'on one document' over both sites.

- **LC1** Persons: the Lincoln-Petersen estimate is at least 3 times the observed number of distinct persons.
- **LC2** Titles: the estimate is at most 1.5 times the observed number.
- **LC3** Persons are shared between the sites less than titles are (share of the smaller site's words also at the
  other site; Fisher).
- **LC4** 60%+ of persons are on exactly one document.
- **LC5** Titles are on exactly one document less often than persons are (Fisher).
- **LC6** On the three measures (estimate / observed, shared share, one-document share) the Indus names of set 147
  (5.1, 20 of 130 = 15%, 92%) are each closer to Linear B persons than to Linear B titles.

## Hundred-and-fifty-third set: capture-recapture inside one city (five hypotheses)

Set 147's estimate could be inflated by local fashion between cities. Catches inside one city, seals only (F):
Mohenjo-daro DK against HR areas (major area as set 140), Mohenjo-daro early against late (predict_test18.level),
Harappa early against late.

- **WC1** Whole names, Mohenjo-daro DK against HR: estimate at least 3 times observed.
- **WC2** Whole names, Mohenjo-daro early against late: estimate at least 3 times observed.
- **WC3** Heads, Mohenjo-daro DK against HR: estimate at most 1.5 times observed.
- **WC4** Heads, Mohenjo-daro early against late: estimate at most 1.5 times observed.
- **WC5** Whole names, Harappa early against late: estimate at least 3 times observed.

## Hundred-and-fifty-fourth set: same name, same person? (six hypotheses)

Whole names on two or more seals in F (all sites). Long = body of 3+ signs (a name of four or more signs with its
ending); short = body of one sign. Pairs of seals carrying the same name.

- **SP1** Long-name pairs are from the same site more often than short-name pairs (Fisher).
- **SP2** Among same-site Mohenjo-daro pairs with sub-areas, long-name pairs share the sub-area more often than
  short-name pairs (Fisher).
- **SP3** Long-name pairs share the level (early / late) more often than short-name pairs (Fisher).
- **SP4** Long-name pairs at Mohenjo-daro share a sub-area more often than chance (pair permutation as set 140).
- **SP5** Short-name pairs at Mohenjo-daro do not (p >= 0.05 holds).
- **SP6** Long-name pairs carry the same motif (field 18) more often than short-name pairs (Fisher).

## Hundred-and-fifty-fifth set: names from two interchangeable elements? (four hypotheses)

Dithematic personal-name systems (Greek, Germanic, Sanskrit) compose names from one pool of elements in either order.
Two-sign name bodies (opener + head), distinct names (A + B).

- **DT1** Of heads with 3+ two-sign names, 50%+ also occur as the opener of a two-sign name.
- **DT2** Reversed pairs (a b and b a both attested as two-sign bodies) are at least as many as when heads are shuffled
  among the bodies (1,000 draws; holds if the observed count is at or above the median).
- **DT3** Opener and head combine freely: their MI is not above shuffles (p >= 0.05 holds).
- **DT4** 70%+ of middle-sign types of three-sign bodies are also attested as an opener or a head.

## Hundred-and-fifty-sixth set: numerals in names as birth-order or clan numbers (four hypotheses)

Numeral runs as predict_test112.runs; value R.NUMS.

- **BO1** Numeral runs in name bodies are worth 4 or less more often than runs in count texts (Fisher).
- **BO2** Runs that open a name body are worth 4 or less in 80%+.
- **BO3** The value of name-opening runs depends on the city (Mohenjo-daro against Harappa, F; MI).
- **BO4** 5+ pairs of distinct names differ only in the value of a name-opening run (e.g. '2 X Y 740' and
  '3 X Y 740').

## Results of the hundred-and-fifty-second set (added after the test; `predict_test152.py`, `results/predict_test152.md`)

Five held, one failed. **The capture-recapture method separates personal names from titles on a read script, and
the Indus names fall with the personal names.** Linear B (DAMOS, Knossos and Pylos): 992 attested persons (Knossos 649,
Pylos 419, both 76) give an estimate of 3,544, 3.6 times the observed (LC1); 43 titles and occupations (Knossos 16,
Pylos 35, both 8) give 67, 1.56 times (LC2 fails narrowly against 1.5). Persons are shared between the palaces less
than titles (LC3: 18% against 50%, p = 0.005) and are on one document more often (LC4: 71%; LC5: titles 51%, p =
0.006). On all three measures the Indus names of set 147 are closer to Linear B persons than to titles (LC6: estimate
ratio 5.1 against 3.6 / 1.6; shared 15% against 18% / 50%; one object 92% against 71% / 51%).

Noted after the test: the Indus heads of set 147 (estimate 1.14 times observed, 50 of 64 Harappa heads also at
Mohenjo-daro, 78%) have the profile of Linear B titles, not persons, which fits heads as a closed vocabulary of name
elements or titles. Caveats: the Linear B classes come from one lexicon's definitions (Tiripode, exact forms), the two
palaces differ in date as well as place, and Indus objects are seals, not administrative documents; the comparison is
of profiles, not a test of identity. With this control, set 147's reading (Indus names behave as personal names) is
calibrated rather than only suggestive. Tally, counting parts: 1112 held, 1053 failed (2165 registered).

Qualified by the hundred-and-fifty-eighth set (added later the same day): Ur III personal names have the
*title-like* profile and only whole Ur III legends are open, so the profile measures how individual a whole text is,
not personhood. Read LC6 as 'Indus seal texts are individual compositions, like Linear B person names and Ur III
whole legends'.

## Results of the hundred-and-fifty-third set (added after the test; `predict_test153.py`, `results/predict_test153.md`)

Five held, none failed. **Set 147's result does not depend on comparing two cities.** Inside Mohenjo-daro, DK against
HR areas: 351 and 79 names, 8 shared, estimate 3,128 (WC1: 7.4 times observed); early against late: 136 and 115, 11
shared, estimate 1,323 (WC2: 5.5 times); at Harappa early against late: 37 and 54, 1 shared, estimate 1,044 (WC5; one
recapture, so the figure itself is unstable, but the overlap is as low as a large population gives). Heads stay closed
inside the city: 1.15 times observed between areas (WC3: 35 of 44 HR heads also in DK) and 1.13 times between levels
(WC4). Caveat: the level splits compare generations, so their overlap also measures turnover of names over time; the
area split (WC1) is the cleaner check and gives the same answer. Tally, counting parts: 1117 held, 1053 failed (2170
registered).

## Results of the hundred-and-fifty-fourth set (added after the test; `predict_test154.py`, `results/predict_test154.md`)

One held, five failed; the set is underpowered. Only 14 long names (body 3+) recur on two or more seals (28 seal
pairs, 6 with Mohenjo-daro sub-areas), against 26 short names (107 pairs). Long-name pairs are from the same site
somewhat more often (SP1: 61% against 41%, p = 0.051), but not from the same sub-area (SP2: 2 of 6), level (SP3: 5 of
8) or motif (SP6: 19% against 14%), and are not co-located beyond chance (SP4: 6 pairs). Short-name pairs are not
co-located either (SP5 holds, p = 0.10). Reading: with so few repeated long names, same-name seals cannot be tied to
one owner; that 92% of names are on a single seal (set 147) is itself the main fact, and it fits one seal per
person. Tally, counting parts: 1118 held, 1058 failed (2176 registered).

## Results of the hundred-and-fifty-fifth set (added after the test; `predict_test155.py`, `results/predict_test155.md`)

Four held, none failed, with two caveats. 242 distinct two-sign bodies, 199 three-sign bodies. Heads also open
names (DT1: 20 of 31 heads with 3+ two-sign names, 65%); middle signs of three-sign bodies come from the same pool as
openers and heads (DT4: 66 of 76, 87%); reversed pairs occur (DT2: 6 against a shuffled median of 2). **Caveats noted
after the test:** (1) DT3 is ill-posed: on distinct bodies every (opener, head) pair is unique, while shuffles create
repeated pairs and so raise MI; p = 1.0 is that artefact, not evidence of free combination. It is counted as held
under the registered rule but carries no weight. (2) The six reversed pairs are almost all fish pairs (220 235, 220
240, 235 240, 233 803, 235 803, 240 806): the known free order of stacked fish (set 67 and after), not a general
reversibility; sign order is otherwise fixed (H2). Reading: name elements are drawn from one shared pool used in
every position, which is a feature of dithematic personal-name systems, but the order is fixed except among fish, so
it is not the Greek/Germanic kind where the two elements swap freely. Tally, counting parts: 1122 held, 1058 failed
(2180 registered).

## Results of the hundred-and-fifty-sixth set (added after the test; `predict_test156.py`, `results/predict_test156.md`)

Three held, one failed; weak. Name numerals are small slightly more often than count-text numerals (BO1: 83% against
78%, p = 0.025; 2 dominates, 252 of 594), name-opening runs are worth 4 or less in 83% (BO2), and 29 pairs of names
differ only in the opening value (BO4). But the opening value does not depend on the city (BO3: p = 0.12), and the
BO4 pairs are almost all a numeral + one head ('2 / 3 / 4 / 6 + 220 740 or 520', '2 / 3 / 4 + 840 740', '3 / 4 / 5 / 8
+ 900 740'): the count-a-sign construction, which a birth-order name and a counted noun would both produce. Reading:
the numbers inside names are small, and a name can vary only in its number, which is compatible with numbered
persons (birth order, clan or rank) but equally with 'N of X' counts; this set cannot separate the two. Tally,
counting parts: 1125 held, 1059 failed (2184 registered).

# Hundred-and-fifty-seventh set, registered before testing (24 September 2026): which kinds of text are names, which titles? (seven hypotheses)

The capture-recapture profile separated persons from titles on Linear B (set 152: persons estimate/observed 3.57,
shared 0.18, on one document 0.71; titles 1.56, 0.50, 0.51). Here each kind of Indus text gets the same three
measures. Catches: Mohenjo-daro against Harappa (F, objects without copper unless stated). Units: 740 names and 520
names = whole names (body, ending) on seals; closer texts = whole distinct lines of genre 'closer' on seals; count
texts = whole distinct lines of genre 'count' on any object; copper texts = whole texts of Mohenjo-daro copper tablets,
catches DK against the other major areas (copper tablets are almost all from Mohenjo-daro). A kind is person-like when
it is nearer the Linear B persons than the titles on 2+ of the 3 measures, title-like when nearer the titles on 2+.
p < 0.05.

- **GC1** 740 names are person-like.
- **GC2** 520 names are title-like.
- **GC3** Closer texts are title-like.
- **GC4** Count texts are title-like.
- **GC5** Copper-tablet texts are title-like.
- **GC6** 520 names are shared between the cities more often than 740 names (share of the smaller city's names; Fisher).
- **GC7** Closer texts are shared between the cities more often than 740 names (Fisher).

## Results of the hundred-and-fifty-seventh set (added after the test; `predict_test157.py`, `results/predict_test157.md`)

Two held, five failed. Profiles (estimate/observed, shared, on one object): 740 names 5.13, 0.15, 0.92; 520 names
4.08, 0.17, 0.91; closer texts 5.25, 0.12, 0.93; count texts 8.75, 0.06, 0.87; copper-tablet texts 1.47, 0.54, 0.51
(Linear B persons 3.57, 0.18, 0.71; titles 1.56, 0.50, 0.51). Held: 740 names are person-like (GC1) and copper texts
title-like (GC5: a closed set of labels, repeated across areas, as the tablet sets of sets 33-34 showed). Failed:
520 names (GC2), closer texts (GC3) and count texts (GC4) are all person-like too, and 520 names and closers are
shared between the cities no more than 740 names (GC6: 17% against 15%; GC7: 12.5%).

**What this changes.** Every seal genre, and the count texts, has the open profile. Count texts are combinations of
numbers and commodity signs, not people, so the profile measures an open, combinatorial set of texts, not persons as
such. Set 147 and 152 still stand as far as they go: seal names are an open population of combinations over a closed
stock of elements, and in that respect they differ from titles and from the fixed label sets of the copper tablets.
But 'personal names' is one reading of that openness, not the only one; any system that composes texts freely (names,
descriptions, counts) gives it. What the 520 / closer tests add: 520 names and closer texts are not a small shared
set of titles or divine names either; they are as varied and as local as 740 names. Tally, counting parts: 1127 held,
1064 failed (2191 registered).

# Hundred-and-fifty-eighth set, registered before testing (24 September 2026): Ur III seal legends as a read control (seven hypotheses)

A second read control, this time of the same genre: Mesopotamian seal legends. Data: ORACC epsd2/admin/ur3 JSON
export (CC0; `ur3_seals.py` streams the 562 MB zip and keeps the 'seal N' surfaces: 22,179 texts, 70,367 seal lines,
lemmas with part of speech, in `data/ur3_seals.tsv`). A legend = the lemma sequence of one seal surface; distinct
legends stand for distinct seals (one seal rolled on many tablets gives one legend). Catches: Umma against Girsu
(provenience). Owner = the PN on line 1; title = an N lemma on a later line other than dumu (child), arad (servant),
lugal (king); father = the PN after dumu. Profiles as set 157 against the Linear B persons and titles.
Indus side for UR5-UR7: F seals at Mohenjo-daro and Harappa. p < 0.05.

- **UR1** Ur III owner names are person-like.
- **UR2** Ur III titles are title-like.
- **UR3** Ur III whole legends are person-like (open, as whole Indus texts were in set 157).
- **UR4** Ur III fathers are person-like.
- **UR5** Indus seals with two names (two name units, in one line or two) are at least half as common as Ur III legends
  with two or more PNs (the filiation format).
- **UR6** Indus seals with a post-name field (a closer, 400 or 90 after the ending, or a separate non-name line) are
  within a factor of 2 of the share of Ur III legends with a title.
- **UR7** Both title stocks are closed: the ten commonest Ur III titles cover 60%+ of titled legends, and the ten
  commonest Indus post-name signs (closers, 400, 90, or the last sign of a separate non-name line) cover 60%+ of Indus
  seals with a post-name field.

## Results of the hundred-and-fifty-eighth set (added after the test; `predict_test158.py`, `results/predict_test158.md`)

Three held, four failed. 22,402 Ur III seal surfaces, 6,521 distinct legends (Umma 2,307, Girsu 1,612 ...).
Profiles (estimate/observed, shared, in one legend): owners 2.04, 0.31, 0.57; fathers 1.91, 0.34, 0.56; titles 1.19,
0.61, 0.38; whole legends 17.51, 0.03, 0.99. **Ur III personal names have the title-like profile** (UR1 and UR4
fail): Sumerian names are a limited stock borne by many people (the same Lu-Nanna or Ur-Lamma in both cities), so
owners and fathers recur across Umma and Girsu. Titles are closed (UR2 holds), and only the whole legend (name + title
+ father) is open (UR3 holds). Indus seals almost never carry two names (UR5 fails: 1.6% against 65% of Ur III legends
with two PNs) or a post-name field (UR6 fails: 13% against 71% with a title); both title stocks are closed (UR7 holds:
top ten cover 80% and 79%; Indus 90, 400, 842, 790, 151, 60, 621 ...).

**This qualifies sets 147, 152 and 157.** The capture-recapture profile does not detect personal names as such: in
Linear B, persons are open; in Ur III, persons are closed and only whole legends are open. What the profile measures
is how individual a whole text is. An Indus seal text (5.1, 15%, 92%) is as individual as a whole Ur III legend,
though it is one name unit, not name + title + father. Two readings fit: (a) Indus names are drawn from a far larger,
more compositional stock than Sumerian names (as Greek names are); or (b) an Indus seal text packs into one name unit
what a Mesopotamian legend spreads over fields (name, office, filiation), the opener and middle elements carrying
title or lineage. The seal format itself differs from Mesopotamia's: no filiation line, rarely a title field. Set
152's 'Indus names behave as personal names' should be read as 'Indus seal texts are individual compositions, as
Linear B person names and Ur III whole legends are'. Tally, counting parts: 1130 held, 1068 failed (2198 registered).

# Hundred-and-fifty-ninth and hundred-and-sixtieth sets, registered together before testing (24 September 2026): twenty hypotheses from the controls and the literature

Built from this project's results (sets 142-158) and from others' claims: Fuls 2024 (IJAS 14(1): 3-16; sign 1 not a
word divider against Wells 2011's partial divider for signs 1 and 2; mean word length about 1.7 signs; Indus as
scripta continua), Fuls 2022/2023 (text classes), and the Ur III and Linear B controls. Profiles, catches and
person-like / title-like as sets 152, 157 and 158. Conventions as sets 147-151. p < 0.05.

## Hundred-and-fifty-ninth set: the packed-legend reading and the word-divider question (ten hypotheses)

Set 158 left two readings: Indus names come from a large stock, or one Indus name packs name + office / lineage.
If the second, the opener (first sign of a 3+-sign body) would carry office or lineage.

- **PL1** Openers of 3+-sign name bodies on seals have the title-like profile (Mohenjo-daro against Harappa).
- **PL2** The name core (body minus opener) of the same names has the person-like profile.
- **PL3** 50%+ of the smaller city's openers also occur in the other city.
- **PL4** On seals with a motif, the opener tells more about the motif than the head does: permutation z of
  MI(opener, motif) above that of MI(head, motif) (1,000 permutations each; names with 3+-sign bodies).
- **PL5** The post-name signs of set 158 (closers, 400, 90 after an ending) have the title-like profile.
- **PL6** Wells's divider, sign 1: for inner tokens of sign 1, both the part before and the part after are attested as
  complete distinct lines elsewhere more often than for inner tokens of other signs with 20+ inner tokens (Fisher).
- **PL7** The same for sign 2.
- **PL8** Line junctions (set 142's 77 multi-line texts) stand next to sign 1 or 2 more often than random cut points
  (10,000 draws; both line orders).
- **PL9** Fuls's word length: chaining adjacent unit pairs (predict_test61.units) into words, with unlinked signs as
  one-sign words, the mean word length in name bodies lies between 1.5 and 2.0 signs.
- **PL10** Seal pairs sharing an opener are in the same city (Mohenjo-daro / Harappa) more often than seal pairs
  sharing a head (Fisher).

## Hundred-and-sixtieth set: the new findings on independent samples (ten hypotheses)

B = Mahadevan's M77 texts absent from ICIT (signs.load(only_m77=True); sites by M77 block: Mohenjo-daro 465 lines,
Harappa 409). Linear B and Ur III as sets 152 and 158.

- **RP1** In B, at the size of the 520 names, 740 names show more distinct heads in 95%+ of 1,000 draws (PV3).
- **RP2** In B, for signs counted in both cities, the commonest value before them agrees in under 70% (NC5's locality).
- **RP3** In B, whole names, Mohenjo-daro against Harappa: estimate at least 3 times observed (set 147).
- **RP4** In B, heads: estimate at most 1.5 times observed.
- **RP5** Harappa moulded tablets (TAB:B, TAB:I; F), whole texts, early against late: title-like (closed sets, as
  copper tablets in GC5).
- **RP6** Linear B inside Knossos, persons, series D (the sheep tablets) against all other series: person-like.
- **RP7** The same split, titles: title-like.
- **RP8** Ur III owners, Umma against Nippur: title-like (UR1 with a third city).
- **RP9** Ur III whole legends, Umma against Nippur: person-like (UR3).
- **RP10** Indus names on seals, Gujarat (Lothal, Dholavira) against Mohenjo-daro: estimate at least 3 times observed.

## Results of the hundred-and-fifty-ninth set (added after the test; `predict_test159.py`, `results/predict_test159.md`)

Five held, five failed. **The packed-legend reading gains support.** Openers of 3+-sign names have the title-like
profile (PL1: estimate/observed 1.37, shared 0.63, on one seal 0.57), and 33 of the smaller city's 52 openers
also occur in the other (PL3: 63%), while the name cores (body minus opener + ending) are strongly person-like (PL2:
8.86, 0.08, 0.95). On seals with a motif, the opener carries more information about the picture than the head does
(PL4: permutation z 2.53 against 0.95; MI 1.73 against 1.29 bits, 508 names). So an Indus name of three or more signs
looks like a shared, closed first element that goes with the seal's emblem, plus an individual core: the shape of
'office or lineage + personal name', packed into one unit rather than set on separate lines as in Ur III legends.
Same-opener seals are not more often in one city than same-head seals (PL10: 67% against 69%), so the opener is not
a local lineage mark. PL5 holds but is degenerate (after-ending closers, 400 and 90 are 2-3 sign types per city) and
carries no weight.

**Fuls 2024 is supported on word dividers.** Signs 1 and 2 do not behave as dividers: the text on both sides of an
inner sign 1 is a complete text elsewhere no more often than around other signs (PL6: 4.2% against 4.0%), for sign 2
far less (PL7: 0.3%, sign 2 is bound to what follows), and line breaks do not fall next to them (PL8: 7 and 1 against
10 and 9). Wells's partial divider reading fails. Fuls's word length of about 1.7 is not matched by this project's
unit chaining (PL9: 1.36 signs per word with units from 5+ bodies; the figure depends on the unit threshold).
Tally, counting parts: 1135 held, 1073 failed (2208 registered).

Withdrawn in part by the hundred-and-sixty-first set (added later the same day): openness grows with unit length
(1-sign names are title-like), so PL1/PL2 mostly compare single signs with multi-sign units; the shared openers are
frequent signs and numerals. Only a weak motif link (PL4) remains of the office + name reading.

## Results of the hundred-and-sixtieth set (added after the test; `predict_test160.py`, `results/predict_test160.md`)

Eight held, two failed. **The new findings replicate on independent samples.** In Mahadevan's M77 additions (B,
Mohenjo-daro against Harappa), the 520 class is narrow (RP1: 9 heads in 29 names; 740 always more at equal size),
numeral values before a given sign are local (RP2: same commonest value for 18 of 35 signs, 51%), whole names are open
(RP3: 5.98 times observed) and heads closed (RP4: 1.21 times). Gujarat seals against Mohenjo-daro give the same open
profile (RP10: 4.62). The controls hold on new splits: Linear B persons are person-like inside Knossos too (RP6: D
series against the rest, 3.01, 0.22, 0.80), and in Ur III owners are title-like (recurring) and whole legends open
between Umma and Nippur as between Umma and Girsu (RP8: 2.09, 0.31, 0.61; RP9: 37.1, 0.02, 0.99). Failed: RP7 is
degenerate (no title word occurs in the D series, so there was nothing to test); Harappa moulded tablets (RP5: 1.99,
0.34, 0.69) fall between the profiles and are classed person-like by one measure's margin (shared 0.34, equidistant):
they are neither a fully closed label set like the copper tablets nor as open as seal names. Tally, counting parts:
1143 held, 1075 failed (2218 registered).

# Hundred-and-sixty-first and hundred-and-sixty-second sets, registered together before testing (24 September 2026): the office + name reading, twenty hypotheses

Set 159 found openers of 3+-sign names title-like and motif-linked, cores person-like. These twenty tests probe that
reading from other sides and control for length. Definitions: names as R.name_of; opener = first body sign of a
3+-sign body; core = (body minus opener, ending); shared opener = an opener attested on seals at both Mohenjo-daro
and Harappa in F (set 159: 33 signs); heading = a line whose first signs are 817, 820 or 861 followed by 2, 60 or 1
(the prefix R.name_of strips). Profiles and person-like / title-like as sets 157-159. F objects; seals unless stated.
p < 0.05.

## Hundred-and-sixty-first set: the opener as an office (ten hypotheses)

- **OF1** Length control: names with a 2-sign body are person-like (openness is not only a matter of length).
- **OF2** Names with a 1-sign body (head + ending) are title-like.
- **OF3** Set 159's PL4 holds within 3-sign bodies and within 4+-sign bodies separately (opener z above head z in both).
- **OF4** Openers with 5+ names on seals with a motif have a majority motif covering a larger share of their names
  than heads with 5+ such names do (pooled majority counts; Fisher).
- **OF5** Seals without a picture (motif 'None') carry a 3+-sign name with a shared opener less often than pictured
  seals do (Fisher).
- **OF6** Heading and opener exclude each other: names under a heading have a shared opener less often than names
  without one (3+-sign bodies; Fisher).
- **OF7** Cores recombine with openers: the number of cores attested with 2+ different openers is at least the median
  when openers are shuffled among the 3+-sign names (1,000 draws).
- **OF8** Across levels (early / late, both cities), openers are shared more than cores (share of the smaller level's
  units also in the other; Fisher).
- **OF9** West Asian names (as set 136) carry a shared opener less often than home names with 3+-sign bodies (Fisher).
- **OF10** Copper-tablet texts contain a shared opener as their first sign less often than seal names with 3+-sign
  bodies do (Fisher).

## Hundred-and-sixty-second set: the office + name reading, further checks (ten hypotheses)

- **MX1** Rare motifs concentrate openers: over motifs other than the unicorn with 10+ names of 3+ signs, the mean share
  of the commonest opener is above the unicorn's share at the same sample size in 95%+ of 1,000 draws.
- **MX2** In B (M77 additions), openers are title-like (Mohenjo-daro against Harappa).
- **MX3** In B, cores are person-like.
- **MX4** 50%+ of the openers of 3+-sign names on Harappa moulded tablets are shared openers.
- **MX5** The ending (740 / 520) is better predicted by the head than by the opener (permutation z of MI, head above
  opener; 3+-sign names).
- **MX6** Among 3+-sign names on seals, seals with a shared opener are larger (field 31) than seals with another
  opener (rank test).
- **MX7** For shared openers with names in both cities, the commonest motif is the same in both cities in 60%+.
- **MX8** Tags (sealings) carry a shared opener on their 3+-sign names more often than seals do (Fisher).
- **MX9** At Mohenjo-daro, seals sharing a shared opener share a sub-area more often than chance (pair test as set
  140).
- **MX10** The share of 3+-sign names with a shared opener differs between early and late levels (site-stratified
  permutation as TM, two-sided).

## Results of the hundred-and-sixty-first set (added after the test; `predict_test161.py`, `results/predict_test161.md`)

Five held, five failed. **This set largely withdraws set 159's 'office + name' reading.** The length controls show
that openness grows with unit length: 1-sign names are title-like (OF2: 1.29, 0.69, 0.62), 2-sign names only just
person-like (OF1: 3.04, 0.24, 0.82). An opener is a single sign drawn from the sign inventory, so its closed,
title-like profile (PL1) is nearly automatic, and the core's openness (PL2) follows from its length. The 33 'shared
openers' are mostly frequent signs, several of them numerals (3, 31, 32, 33, 55) or common signs (700, 820, 861, 920):
copper-tablet texts begin with one as often as seal names do (OF10: 56% against 57%), pictureless seals carry them as
often as pictured seals (OF5: 17% against 19%), the two West Asian names are no different (OF9), and names under a
heading have them more, not less (OF6 fails the other way: 82% against 53%). The motif link is weak once length is
split: opener z 0.98 against head z -0.08 in 3-sign names, 2.03 against 1.93 in 4+-sign names (OF3 holds on the
registered rule but the margin is small), and openers are not more motif-specific than heads (OF4: 35% against 31%).
What holds: openers last across levels far more than cores (OF8: 48% against 4%, as single signs do against
multi-sign units) and cores recombine with openers at the shuffled maximum (OF7: 36, range 33-36), i.e. openers
attach freely to cores. Reading: set 159's PL1/PL2 contrast is mostly an artefact of comparing single signs with
multi-sign units; PL4's motif link survives only weakly. Tally, counting parts: 1148 held, 1080 failed (2228
registered).

## Results of the hundred-and-sixty-second set (added after the test; `predict_test162.py`, `results/predict_test162.md`)

Six held, four failed. The direct tests of an office-emblem reading fail: a shared opener does not go with the same
commonest motif in both cities (MX7: 5 of 33, 15%), rare motifs do not concentrate openers (MX1: gaur and zebu, top
opener share 0.14, beat the unicorn in 32% of draws), shared-opener seals are not larger (MX6: 29.3 against 29.1 mm)
and do not cluster in one quarter of Mohenjo-daro (MX9). The head, not the opener, sets the ending (MX5: z 22.7
against 1.1), as the paradigm already had it. In B, openers are again title-like and cores person-like (MX2: 1.54,
0.47, 0.59; MX3: 10.85, 0.04, 0.86), but set 161 showed that contrast is mostly single sign against multi-sign unit,
so the replication carries the same caveat. Two new facts, both about the 33 frequent 'shared openers' rather than
about offices: they begin 90% of the 3+-sign names on tags (sealings, mostly Lothal and Kalibangan) against 57% on
seals (MX8, p = 0.002), and 53% of those on Harappa moulded tablets (MX4); and names beginning with one become more
common from early to late levels (MX10: +0.26, p = 0.0003), a drift towards a smaller set of standard name openings
over time. Tally, counting parts: 1154 held, 1084 failed (2238 registered).

# Hundred-and-sixty-third and hundred-and-sixty-fourth sets, registered together before testing (24 September 2026): twenty hypotheses

## Hundred-and-sixty-third set: length-matched and shuffled baselines for the capture-recapture profiles (ten hypotheses)

Set 161 showed openness grows with unit length, so the comparisons of sets 147, 152, 157 and 158 need length matching
and a chance baseline. Length: Indus names by total signs (body + ending); Linear B persons by syllables (hyphen
count + 1); Ur III legends by lemmas. Shuffled baseline: within each catch, the units (signs, syllables, lemmas) are
shuffled among that catch's items keeping each item's length (1,000 draws); 'excess' = real shared count / mean
shuffled shared count. Catches as before (Indus Mohenjo-daro / Harappa seals; Linear B Knossos / Pylos; Ur III Umma /
Girsu). p < 0.05.

- **LM1** At 3 units, the Indus name estimate/observed ratio is within a factor of 2 of the Linear B person ratio.
- **LM2** The same at 4 units.
- **LM3** Indus 2-sign names (head + ending) have an estimate/observed ratio within a factor of 2 of Ur III owners.
- **LM4** Indus 3-sign whole seal lines and Ur III 3-lemma legends are both person-like.
- **LM5** Real Indus names recur between the cities more than shuffled names (shared count above 95% of shuffles).
- **LM6** Real Linear B persons recur between the palaces more than syllable-shuffled persons.
- **LM7** Real Ur III legends recur between the cities more than lemma-shuffled legends.
- **LM8** The recurrence excess of Indus 520 names is larger than that of 740 names.
- **LM9** The recurrence excess of Indus names is smaller than that of Ur III owners (Indus names recur less, beyond
  combinatorics, than Sumerian names).
- **LM10** The shared share falls with length both for Indus names (lengths 2-6) and for Linear B persons (2-5
  syllables): Spearman negative in both.

## Hundred-and-sixty-fourth set: standardisation over time and the seal types (ten hypotheses)

From set 162: names beginning with a frequent ('shared') opener rise from early to late (MX10) and dominate sealings.
Definitions as sets 161-162; levels as predict_test18.level; seals in F.

- **TS1** MX10 holds at Mohenjo-daro alone (late share above early, Fisher).
- **TS2** MX10 holds at Harappa alone.
- **TS3** The rise is carried by numeral openers: the share of 3+-sign names opening with a numeral rises (site-
  stratified, one-sided p < 0.05) while the share opening with a non-numeral shared opener does not (p >= 0.05).
- **TS4** Late names recur more: the share of distinct names on 2+ seals is higher late than early (Fisher).
- **TS5** Late names are less open: with the two cities as catches inside each level, the late estimate/observed
  ratio is below the early one.
- **TS6** Rectangular seals (SEAL:R) are later than square seals (SEAL:S) (site-stratified share late).
- **TS7** 3+-sign names on rectangular seals begin with a shared opener more often than those on square seals.
- **TS8** MX10 holds on square seals alone (site-stratified, one-sided p < 0.05).
- **TS9** Tag (sealing) texts are shorter than seal texts (rank test, per object).
- **TS10** At Lothal and at Kalibangan separately, 70%+ of tag names of 3+ signs begin with a shared opener.

## Results of the hundred-and-sixty-third set (added after the test; `predict_test163.py`, `results/predict_test163.md`)

Nine held, one failed. **Length-matched, the Indus names still match Linear B persons.** At 3 units the Indus name
estimate/observed is 3.04 against 3.67 for 3-syllable Linear B persons (LM1, quotient 0.83), at 4 units 2.95 against
3.38 (LM2, 0.87). Indus head + ending names (2 signs) come out closer to Ur III owner names (LM3: 1.29 against 2.04),
and 3-unit texts are open in both Indus lines and Ur III legends (LM4: 5.49 and 18.06). Sharing falls with length in
both scripts (LM10: Spearman -0.87 and -1.00), so length matters, but at equal length the Indus names and Linear B
person names have the same profile: set 152's comparison survives the length control that set 161 applied to the
openers. **Real names recur far beyond combinatorics**: 20 Indus names are in both cities against 0.8 when signs are
shuffled within each city (LM5, excess 25), as Linear B persons recur 33 times beyond syllable shuffles (LM6) and Ur
III legends 3 times beyond lemma shuffles (LM7). So the shared names are real repeated names, not accidental
combinations. 520 names recur more beyond combinatorics than 740 names (LM8: excess 50 against 19), fitting the 520
class as a narrow set of widespread names. LM9 fails by construction (Ur III owner names are single lemmas, so
shuffling cannot change them; excess 1). Tally, counting parts: 1163 held, 1085 failed (2248 registered).

## Results of the hundred-and-sixty-fourth set (added after the test; `predict_test164.py`, `results/predict_test164.md`)

Five held, five failed. **Name openings standardise over time at Mohenjo-daro.** Long names beginning with one of the
33 frequent openers go from 39% early to 66% late there (TS1, p = 0.0004); Harappa is already at 75% early and 88% late
(TS2 fails, n.s.). The rise holds on square seals alone (TS8: +0.23, p = 0.0007), so it is not only the later spread
of rectangular seals, though rectangular seals are indeed later (TS6: +0.15, p = 0.007) and use the frequent openers
more (TS7: 77% against 57%). It is not carried by numerals (TS3 fails: numeral openers -0.02; the non-numeral
frequent openers +0.29), and checked after the test it is spread over several openers (late Mohenjo-daro: 32, 692,
920, 806, 803, 503, 798, 61; early: 920, 240, 140, 803). Whole names do not recur more in late levels (TS4: 4.8%
against 5.3%), and the late name population is only slightly less open (TS5: 7.7 against 10.1 times observed, on 2
and 4 recaptures, weak). Sealings are not shorter than seals (TS9); Lothal's 13 long sealing names all begin with a
frequent opener, Kalibangan has one (TS10 fails for lack of data). Reading: over the levels Mohenjo-daro's seal names
converge on the openings Harappa already used, while the names themselves stay individual: a spreading convention
for how names begin, not fewer names. Tally, counting parts: 1168 held, 1090 failed (2258 registered).

# Hundred-and-sixty-fifth and hundred-and-sixty-sixth sets, registered together before testing (24 September 2026): twenty hypotheses

Conventions as sets 161-164. JSD = Jensen-Shannon divergence (bits); permutation tests shuffle the level labels
among Mohenjo-daro seals (1,000 draws). 'Harappa' = all Harappa seals in F unless a level is named. p < 0.05.

## Hundred-and-sixty-fifth set: does Mohenjo-daro converge on Harappa? (ten hypotheses)

- **CV1** The openers that rise at Mohenjo-daro are those common at Harappa early: Spearman of Harappa-early opener
  frequency against the Mohenjo-daro late-minus-early share change is positive (permutation of MD level labels).
- **CV2** Heads: JSD(Mohenjo-daro late, Harappa) is below JSD(Mohenjo-daro early, Harappa), beyond permutation.
- **CV3** All signs on seals: the same.
- **CV4** Mean name-body length at Mohenjo-daro late is closer to Harappa's than early is, beyond permutation.
- **CV5** The share of long-stroke numerals (R.NUMS kind) at Mohenjo-daro late is closer to Harappa's than early is,
  beyond permutation.
- **CV6** The share of bare lines (genre 'bare', no ending) on Mohenjo-daro seals rises from early to late (one-sided
  Fisher).
- **CV7** Harappa does not move towards Mohenjo-daro: JSD(Harappa late, Mohenjo-daro early) is not below
  JSD(Harappa early, Mohenjo-daro early) beyond permutation of Harappa level labels (p >= 0.05 holds).
- **CV8** CV3 holds on square seals alone.
- **CV9** Gujarat seals (Lothal, Dholavira): the opener distribution is closer to Harappa's than to Mohenjo-daro's
  (JSD).
- **CV10** Kalibangan seals: the opener distribution is closer to Harappa's than to Mohenjo-daro's (JSD).

## Hundred-and-sixty-sixth set: the names that recur (ten hypotheses)

- **RN1** Of the names found in both cities, 50%+ have a fish head (signs.FISH).
- **RN2** Names on 2+ seals (anywhere in F) are 520 names more often than names on one seal (Fisher).
- **RN3** 520 names occur at more sites than 740 names on the same number of seals (each 520 name against the mean of
  740 names with its seal count; sign test).
- **RN4** At least 3 names occur at 3 or more sites.
- **RN5** Name sharing between sites falls with distance: over site pairs among sites with 10+ names and approximate
  coordinates (in the script, from general sources), Spearman of shared-name share against distance is negative,
  permutation p < 0.05.
- **RN6** Names found in both cities are on unicorn seals more often than names found in one (Fisher).
- **RN7** Two seals with the same name carry the same motif more often than random pairs of seals (Fisher).
- **RN8** Recurring 520 names also occur on tablets more often than recurring 740 names do (Fisher).
- **RN9** Linear B persons found at both palaces are shorter (syllables) than persons found at one (rank test), as
  Indus shared names are (CR6).
- **RN10** Ur III owner names found in both Umma and Girsu are shorter (characters) than those found in one (rank
  test).

## Results of the hundred-and-sixty-fifth set (added after the test; `predict_test165.py`, `results/predict_test165.md`)

Three held, seven failed. **Mohenjo-daro does not converge on Harappa in general.** Over 512 Mohenjo-daro seals with a
level (287 early, 225 late) against 279 Harappa seals, the heads (CV2: JSD 0.282 early, 0.286 late), the whole sign
distribution (CV3: 0.143 and 0.143; CV8 on square seals: 0.148 and 0.153) and the numeral notation (CV5) do not move
towards Harappa; the openers that rise at Mohenjo-daro are not specifically those common at early Harappa (CV1:
Spearman 0.16, p = 0.13); bare lines do not rise (CV6). Only the mean name length moves slightly towards Harappa's
(CV4: 3.63 to 3.76 against 3.73, p = 0.048), and Harappa does not move towards early Mohenjo-daro (CV7 holds, as
registered). Gujarat openers are not closer to Harappa (CV9); Kalibangan's are marginally (CV10, only 11 openers).
**This corrects set 164's reading**: the rise of frequent openers at Mohenjo-daro is a local change in how names
begin, not convergence on Harappa; 'converge on Harappa's openings' in set 164 should read 'shift towards frequent
openings, which Harappa also used'. Tally, counting parts: 1171 held, 1097 failed (2268 registered).

## Results of the hundred-and-sixty-sixth set (added after the test; `predict_test166.py`, `results/predict_test166.md`)

Two held, eight failed. Fifteen names occur at three or more sites (RN4 holds), e.g. '590 390 740' at five sites
(Allahdino, Chanhu-daro, Dholavira, Harappa, Mohenjo-daro), '13 840 740' at four, and the closing formulas '705 / 706
33 520' at three; but the names shared between the two cities are almost never fish names (RN1: 1 of 20), recurring
names are 520 names no more often than single ones (RN2: 19% against 18%), and **520 names reach fewer sites than 740
names on the same number of seals, not more** (RN3 fails the other way: 15 more, 111 fewer). With LM8, the 520 names
recur beyond combinatorics because they are short and few, not because they travel. Name sharing does not fall with
distance over the five sites with 10+ names (RN5: Spearman 0.05), shared names are not especially on unicorn seals
(RN6), and **seals with the same name carry the same motif no more often than random seals** (RN7: 12% against 11%):
a name is not tied to its seal's animal. Recurring 520 names are not more on tablets (RN8). The controls split: Ur III
owner names shared by Umma and Girsu are shorter (RN10: 8.1 against 9.2 characters, p = 0.0001), as Indus shared
names are (CR6), while Linear B shared persons are not (RN9). Tally, counting parts: 1173 held, 1105 failed (2278
registered).

# Hundred-and-sixty-seventh and hundred-and-sixty-eighth sets, registered together before testing (24 September 2026): twenty hypotheses building on the write-up

Conventions as sets 161-166. p < 0.05.

## Hundred-and-sixty-seventh set: administration, survival and scribal hands (ten hypotheses)

- **AD1** How many seal texts existed: Lincoln-Petersen (Chapman) over distinct texts, seals (SEAL) against sealings
  (TAG) as two catches in F, is at least 3 times the number of distinct seal texts observed.
- **AD2** At Lothal, 50% or fewer of the distinct sealing texts are found on any seal in F (most sealing seals lost).
- **AD3** The openers that rise at Mohenjo-daro (late minus early share) are those common on sealings: Spearman of
  sealing opener frequency against the change is positive (permutation of MD level labels, 1,000 draws).
- **AD4** In two-line seal texts with a name line, the other line ends in a closer, 400, 90 or another post-name sign
  of set 158's list in 50%+.
- **AD5** In those texts the non-name line is shorter than the name line (paired sign test).
- **AD6** Non-name lines recur on more seals than name lines do (share of distinct line texts on 2+ seals; Fisher).
- **AD7** A scribe's hand: on objects carrying tokens of two different variant pairs (set 146), the two variant choices
  are correlated beyond chance (pooled agreement against permutation of choices within pair, 1,000 draws).
- **AD8** Numeral compounds (set 150) on Mohenjo-daro seals share a sub-area more often than chance when two seals
  carry the same compound (pair test as set 140).
- **AD9** In West Asian lines, stroke signs stand before signs never counted at home more often than home strokes
  do (Fisher): strokes used for sound, not number.
- **AD10** West Asian stroke runs are worth 1 or 2 more often than home stroke runs (Fisher).

## Hundred-and-sixty-eighth set: controls on published claims and on the count texts (ten hypotheses)

- **CT1** Counting every object (copies included, F), the commonest numeral + fish value is still 2, not 6.
- **CT2** In M77 (all its texts, Mahadevan's transcription), the commonest numeral + fish value is 2.
- **CT3** Linear B (DAMOS): for commodity logograms entered with a number at both Knossos and Pylos (5+ entries each),
  the commonest quantity differs between the palaces for 50%+ (real counts are local too, the control for NC5).
- **CT4** Linear B commodity entries (logogram + quantity, as units) have the person-like (open) profile between
  Knossos and Pylos, as Indus count texts do.
- **CT5** Indus seal lines of 5-7 signs contain a repeated sign at least half as often as Ur III legends of 5-7
  lemmas contain a repeated lemma (against Farmer, Sproat and Witzel's 'too little repetition').
- **CT6** Indus lines of 5-7 signs repeat a sign less often than shuffled lines of the same lengths drawn from the
  corpus sign frequencies (repetition avoidance; 1,000 draws).
- **CT7** Ur III legends of 5-7 lemmas repeat a lemma more often than lemma-shuffled legends (1,000 draws).
- **CT8** The copper-tablet picture signs (749, 341, 753, 777) are name heads (directly before 740 or 520) in 50%+ of
  their occurrences in names.
- **CT9** Names headed by one of them take 740 in 90%+.
- **CT10** 90%+ of copper-tablet sign tokens are signs also used in seal names (one script and vocabulary, not a
  separate label code).

## Results of the hundred-and-sixty-seventh set (added after the test; `predict_test167.py`, `results/predict_test167.md`)

Four held, six failed. **Most seals are lost.** Of 42 distinct sealing texts only 6 are on a surviving seal; with seals
and sealings as two catches the estimate is about 9,100 seal texts against 1,485 known (AD1, 6.1 times), and at
Lothal 2 of 12 sealing texts match a known seal (AD2). Caveat: the sealings come mostly from Lothal and Kalibangan,
whose seals are thinly represented, so the estimate is inflated by geography; the direction (most seals not found)
is the result. In two-line seal texts the non-name line is shorter than the name line (AD5: 31 against 7) but it is
not a title field of closers (AD4: 16 of 40 end in a post-name sign, several of them numerals) and does not recur more
(AD6). The openers that rise at Mohenjo-daro are not the sealing openers (AD3), numeral compounds are not local inside
the city (AD8), and a scribe's hand across different variant pairs is not shown (AD7: p = 0.059, close). AD9 holds
but is ill-posed, noted after the test: 'never counted at home' was defined from the home runs themselves, so the home
rate is 0 by construction; what stands is descriptive: 5 of 16 West Asian stroke runs stand before signs never counted
anywhere in the Indus homeland, which fits strokes used for sound in foreign names (set 136) but on few cases. West
Asian stroke runs are not smaller (AD10). Tally, counting parts: 1177 held, 1111 failed (2288 registered).

## Results of the hundred-and-sixty-eighth set (added after the test; `predict_test168.py`, `results/predict_test168.md`)

Six held, four failed. **Parpola's '6 + fish' is not recovered by counting copies or by Mahadevan's transcription**:
with every object and copy counted the commonest numeral + fish is 2 (CT1: 117, then 3: 31, 6: 9), and in M77's
full transcription (mapped through the alignment) also 2 (CT2: 123, then 3: 24, 6: 12). With set 139 (Parpola's own
CISI text), three transcriptions and two ways of counting agree against 'the most frequent sequence'.

**Two controls change how earlier results should be read.** (1) Real texts avoid repetition: Indus seal lines of 5-7
signs repeat a sign in 9.5% against 28% for shuffled lines (CT6), but Ur III seal legends of 5-7 lemmas do the same,
13.4% against 34% (CT7 fails the registered direction). Repetition below chance is ordinary for real texts, and the
Indus rate is close to the Sumerian one (CT5): against Farmer, Sproat and Witzel's claim that Indus texts repeat too
little to be writing. (2) Linear B commodity counts differ between Knossos and Pylos for 8 of 17 logograms (CT3: 47%,
just under the bar) and Linear B entries (logogram + quantity) have the open profile (CT4: 3.24, 0.20, 0.63), as
Indus count texts do. So the locality of Indus numeral compounds (set 150: values differ between the cities for 61%
of signs) is of the size real counts show, and does not need a local naming custom; set 150's 'local naming customs'
is withdrawn to 'local, as counts are'.

**The picture signs are copper-tablet words.** 749, 341 and 753 occur only on copper tablets and 777 on one seal
besides, so they never head a seal name (CT8, CT9: no cases, failed as registered). Copper-tablet texts otherwise
use the seal vocabulary (CT10: 94% of tokens). Tally, counting parts: 1183 held, 1115 failed (2298 registered).

# Hundred-and-sixty-ninth and hundred-and-seventieth sets, registered together before testing (24 September 2026): twenty hypotheses

## Hundred-and-sixty-ninth set: writing-system statistics against two read scripts (ten hypotheses)

Set 168 showed same-genre controls can settle claims about 'what kind of writing' (Farmer, Sproat and Witzel; Rao et
al. 2009; Fuls 2023/2024 on entropic redundancy). Here the Indus signs are placed between known levels at a matched
sample size. Units: Indus signs (distinct lines of F); Linear B signs (syllabograms of words plus logograms, DAMOS
clean lines); Linear B words (whole syllabic words); Ur III lemmas (distinct seal legends). Each statistic is the mean
over 100 random samples of whole lines/legends accumulated to 5,000 tokens. 'Between' means strictly between the Linear
B sign value and the Linear B word value. p not used; point comparisons of the means.

- **WR1** Distinct types at 5,000 tokens: Indus lies between Linear B signs and Linear B words.
- **WR2** Share of types seen once (hapax share): Indus between.
- **WR3** Bigram conditional entropy H(next | previous), within lines: Indus between.
- **WR4** Share of tokens covered by the ten commonest types: Indus between.
- **WR5** Unigram entropy divided by log2 of the number of types: Indus between.
- **WR6** On a log scale, Indus types lie closer to Linear B signs than to Linear B words (more sign-like).
- **WR7** Indus types at 5,000 tokens are fewer than Ur III lemma types.
- **WR8** Adjacent doubled units (x x) per token: Indus between Linear B signs and Linear B words.
- **WR9** H(next | previous) / H(unit): Indus between Linear B signs and Linear B words.
- **WR10** The single commonest Indus sign (740) covers a larger share of tokens than the commonest Linear B sign does.

## Hundred-and-seventieth set: follow-ups on content (ten hypotheses)

- **C1** In '2 + fish' (set 138's counting), the numeral is the short pair (sign 2) in 80%+ of distinct lines.
- **C2** '2 + fish' makes up the whole name body before an ending (2 fish + 740/520) in 50%+ of its occurrences in
  names.
- **C3** The non-name line of two-line seals (set 167) contains a numeral in 50%+.
- **C4** Harappa count texts (a long-stroke numeral + 700 as the whole text) take values that depend on the excavation
  unit (field 4; MI, permutation).
- **C5** Signs found only on copper tablets (2+ tokens) are Fairservis animal or human pictures more often than other
  signs with a Fairservis identification (Fisher).
- **C6** Left-to-right texts of 2+ signs are attested, reversed, among right-to-left texts more often than as written
  (count of texts with a reversed match against those with a direct match).
- **C7** Sealing texts that match a seal are shorter than sealing texts that do not (rank test).
- **C8** West Asian lines use signs rare at home (fewer than 5 home tokens) more often than home lines do (tokens;
  Fisher).
- **C9** The heading (817, 820 or 861 followed by 2, 60 or 1) opens copper-tablet texts less often than seal lines
  (Fisher).
- **C10** Names on sealings end in 740 more often than names on seals (Fisher).

## Results of the hundred-and-sixty-ninth set (added after the test; `predict_test169.py`, `results/predict_test169.md`)

Seven held, three failed. At 5,000 tokens (means of 100 samples): Indus signs 495 types, hapax share 0.41, H(next|prev)
3.12 bits; Linear B signs 198, 0.26, 3.96; Linear B words 2,128, 0.71, 1.11; Ur III lemmas 1,057, 0.67, 2.92.
**The Indus signs sit between a syllabary-with-logograms and a vocabulary of words, nearer the signs**: types, hapax
share and conditional entropy fall between Linear B signs and words (WR1-WR3), the type count is closer to the signs
on a log scale (WR6: 0.92 against 1.46), and far below Ur III words (WR7), as a logo-syllabic script with a few hundred
signs would be (Fuls 2023 reaches the same class from entropic redundancy). Predictability relative to entropy is
between too (WR9: 0.45 against 0.63 and 0.11), and one sign (740) dominates more than any Linear B sign (WR10: 10%
against 4%). Failed: top-ten coverage (WR4: 0.32, above both), normalised entropy (WR5: 0.78, below both) and doubling
(WR8: 0.014, above both) are not between; on those three, and on WR9 and the commonest-unit share, the Indus signs
resemble the Ur III seal legends (top ten 0.49, normalised entropy 0.70, predictability 0.42, commonest 16%): the
concentration and repetitiveness of a short formulaic seal genre, not of a script type. Caveat: Linear B is
administrative text, a different genre from seals; the comparison places the sign inventory, not the language.
Tally, counting parts: 1190 held, 1118 failed (2308 registered).

## Results of the hundred-and-seventieth set (added after the test; `predict_test170.py`, `results/predict_test170.md`)

Four held, six failed. **'2 + fish' is two things.** Of 113 distinct lines, 60 write the 2 as the short pair (sign 2)
and 51 as the long pair (sign 32), which Parpola does not read as a number but as 'space' (*vēḷ*), long pair + fish
being his *vēḷ-mīn*, Venus (C1 fails at 53%). Leaving the long pair out, short 2 + fish (60) is still far commoner than
6 + fish (8), so sets 138, 139 and 168 stand, but part of the '2 + fish' count is Parpola's Venus compound. '2 + fish'
is never a whole name body on its own (C2: 0 of 73). The non-name line of two-line seals is not mostly a count (C3:
38%). **Harappa count tokens vary by excavation unit** (C4: MI 0.29 bits, p = 0.0001; long 3, 4 and 2 + 700), batches
made and kept locally, as the Linear B counts of set 168 are local. **The heading never opens a copper-tablet text**
(C9: 0 of 198 against 16% of seal lines): the tablets are labels without the seal's heading. Sealing texts that match a
known seal are shorter (C7: 3.5 against 4.8 signs), as common short names would be, and foreign lines use signs rare
at home three times as often (C8: 16% against 5%). Failed: sealing names are 740 names only slightly more (C10: 91%
against 82%, p = 0.08); C5 had no case (none of the seven copper-only signs, 341, 597, 749, 753, 781, 782, 957, has a
Fairservis identification); and C6 fails in a way that settles a point: left-to-right lines match right-to-left
lines as stored (46) and almost never reversed (2). ICIT stores every text in reading order, so left-to-right texts
are the same texts written in the other direction, not reversals. Tally, counting parts: 1194 held, 1124 failed (2318
registered).

# Hundred-and-seventy-first set, registered before testing (24 September 2026): the structure of names across candidate languages (ten hypotheses)

The owner asked for language tests built on the structure rules. Name lists (`lang_names.py`; sources outside the
repository): Indus = distinct name bodies on seals (F), without the ending, 2+ signs; Ur III = seal-owner names
(ORACC, CC0), PN forms split into signs; Old Tamil = Sangam poets (Wikipedia list, Tamil script), the last word of
each name (the personal name, honorific included) split into aksharas; Sanskrit = Monier-Williams entries 'N. of a man
/ woman', split into syllables (C*V) and into compound members; Linear B = DAMOS persons, syllabograms. A Prakrit
list could not be built cleanly (EIAD tags names only in its headers; the donor formula gives 13 words); Prakrit is
left out and Sanskrit stands for Indo-Aryan. Names with 2+ elements only. For each list: T_first and T_last = distinct
first and last elements, rarefied to 400 names (mean of 500 draws); R = T_last / T_first (R < 1: the last element
comes from the smaller, closed set). Length = elements per name; JSD over lengths 2-8+. Caveats registered with the
set: the sources differ by up to two millennia from the Indus texts; Tamil names carry the honorific -ār; Monier-
Williams gives stems of all periods; aksharas and syllables are not Indus signs.

- **LN1** Ur III owner names close their first element: R > 1 (Ur-, Lu-, Nin-, the divine determinative).
- **LN2** Indus name bodies close their last element: R < 1.
- **LN3** Old Tamil names: R < 1.
- **LN4** Sanskrit names (syllables): R < 1.
- **LN5** Linear B persons: R < 1.
- **LN6** On a log scale the Indus R is closer to the Old Tamil R than to the Sanskrit (syllable) R.
- **LN7** The Indus length distribution is closer (JSD) to Old Tamil akshara lengths than to Sanskrit syllable lengths.
- **LN8** The Indus length distribution is closer to Old Tamil than to Ur III sign lengths.
- **LN9** Sanskrit compound names (2+ members) close their last member: member-level R < 1 (-datta, -deva, -mitra ...).
- **LN10** The Indus R is within a factor of 2 of the Sanskrit member-level R (Indus signs behave like name members).

## Results of the hundred-and-seventy-first set (added after the test; `predict_test171.py`, `results/predict_test171.md`)

Six held, four failed. **Sumerian names close their first element, Indus names their last** (LN1: Ur III R 1.41, 107
first types against 151 last at 400 names; LN2: Indus R 0.71, 146 against 103): a second, independent exclusion of a
Sumerian-type name structure, measured on name lists rather than on word order. Linear B persons close the last
element too (LN5: 0.84), and Sanskrit compound names are close to even at the member level (LN9: 0.97); the Indus R
is within a factor of 2 of the Sanskrit member R (LN10: 0.73), consistent with Indus signs behaving like name
members. **Dravidian and Indo-Aryan are not separated.** The Old Tamil list (Sangam poets) closes its last element
far more (LN3: R 0.20) because nearly every name ends in the honorific -ār, and its names are long (6.2 aksharas),
so the Indus R is nearer the Sanskrit syllable R (LN6 fails: 0.43 against 1.27 on a log scale), and the Indus length
distribution is nearer Sanskrit syllables (LN7 fails: JSD 0.08 against 0.25) and even Ur III signs (LN8 fails) than
Old Tamil. Sanskrit names at the syllable level do not close their last syllable (LN4: 1.09), because Monier-Williams
gives stems without case endings. Reading: the name lists confirm the head-final, closed-last name structure that
separates Indus from Sumerian, but the available Dravidian list (literary names with an honorific) is not comparable
enough to rank Dravidian against Indo-Aryan; see the follow-up set. Tally, counting parts: 1200 held, 1128 failed
(2328 registered).

# Hundred-and-seventy-second set, registered before testing (24 September 2026): the Tamil comparison repaired, and the ending profile (six hypotheses)

Set 171's Old Tamil list failed as a comparator because the Sangam names carry the honorific -ār. Here the honorific
is removed by a fixed rule written before testing: a final 'ார்' (-ār) is replaced by the pulli '்' on the preceding
consonant (muṭavaṉār > muṭavaṉ, the plain -aṉ form); other names are kept as they are. 'Final element' of a full
name: Indus = the ending (740 or 520, R.names_in); Old Tamil = the last akshara of the core; Sanskrit = the last
syllable of the Monier-Williams stem; Linear B = the last syllabogram. Rarefaction and JSD as set 171.

- **LT1** Old Tamil name cores close their last element: R < 1.
- **LT2** On a log scale the Indus R is closer to the Old Tamil core R than to the Sanskrit syllable R.
- **LT3** The Indus body length distribution is closer (JSD) to Old Tamil cores than to Sanskrit syllables.
- **LT4** The mean length of Old Tamil cores (aksharas) is within 1 of the Indus body mean (signs).
- **LT5** The share of names whose final element is the commonest one is closer between Indus and Old Tamil cores than
  between Indus and Sanskrit stems.
- **LT6** Linear B persons' commonest final syllabogram covers a smaller share of names than 740 does of Indus names.

## Results of the hundred-and-seventy-second set (added after the test; `predict_test172.py`, `results/predict_test172.md`)

Three held, three failed. With the honorific removed (464 of 542 names), Old Tamil name cores still close their last
element strongly (LT1: R 0.30), more than the Indus names (0.71), so the Indus R stays nearer the Sanskrit syllable R
(LT2 fails), and the Indus body lengths stay nearer Sanskrit syllables (LT3 fails: JSD 0.08 against 0.11); Tamil cores
are longer (LT4 fails: 5.4 aksharas against 4.3 signs). **One feature is Tamil-like: the dominant name ending.** 82% of
Indus names end in 740, and 67% of Old Tamil name cores end in -ṉ (the masculine personal suffix -aṉ), against 8% for
the commonest final syllable of Sanskrit stems (LT5) and 13% for Linear B (LT6). That puts a number on Mahadevan's
740 = -aṉ argument. It is not decisive: Monier-Williams gives uninflected stems, and an inflected Indo-Aryan name
list (Prakrit donors in the genitive -sa, not obtainable cleanly here) would also be concentrated on one ending.
Summary of sets 171-172: name structure excludes a Sumerian-type language a second time (first element closed there,
last element closed here); between Dravidian and Indo-Aryan the name lists available do not decide, with lengths and
closure nearer Sanskrit and the dominant masculine-type ending nearer Tamil. Tally, counting parts: 1203 held, 1131
failed (2334 registered).

# Hundred-and-seventy-third set, registered before testing (24 September 2026): early Prakrit donor names as an Indo-Aryan comparator (ten hypotheses)

The owner asked for further tests with material that can be obtained. New source: H. Lüders, *A List of Brahmi
Inscriptions from the Earliest Times to about A.D. 400* (Ep. Ind. X appendix, 1912; OCR at the Internet Archive),
parsed by `lang_names.pra_luders`: 'Gift of [titles] Name' in entries marked Prakrit, the site taken from the
references (Bhilsa Topes = Sanchi, Bharhut, Mathura ...) and, where an entry names none, from the last site named
before it (the list runs site by site): 374 names, Sanchi 310, Bharhut 43; names lower-cased, macrons lost in the
OCR, some OCR errors kept. Elements = aksharas (split after each vowel a e i o u, trailing consonants joined to the
last). This is South Asian, Indo-Aryan, personal names on donated objects, c. 200 BCE-400 CE: closer in time, place
and genre to the Indus seals than Monier-Williams. Profiles as sets 152/157 (Linear B person / title benchmarks);
R, JSD and rarefaction (to the smaller list) as sets 171-172; Old Tamil = the honorific-removed cores of set 172.

- **PK1** Prakrit donor names, Sanchi against Bharhut, are person-like.
- **PK2** At 3 and at 4 units, the Indus name estimate/observed ratio is within a factor of 2 of the Prakrit one (both
  lengths, where both have 20+ names per catch; otherwise at all lengths pooled).
- **PK3** Prakrit donor names close the last element: R < 1.
- **PK4** On a log scale the Indus R is closer to the Prakrit R than to the Old Tamil core R.
- **PK5** The Indus body length distribution is closer (JSD) to Prakrit akshara lengths than to Old Tamil cores.
- **PK6** Prakrit names end in a closed stock of compound heads: the ten commonest final two-akshara endings (-guta,
  -mita, -dina, -rakhita ...) cover 30%+ of names.
- **PK7** The ten commonest Indus heads cover a share of Indus names within 0.15 of PK6's share.
- **PK8** Names found at both Sanchi and Bharhut are shorter than names found at one (rank test), as Indus shared names
  are (CR6).
- **PK9** Real Prakrit names recur between Sanchi and Bharhut more than akshara-shuffled names (above 95% of 1,000
  shuffles), as Indus names do (LM5).
- **PK10** The final two-akshara endings (compound heads) have the title-like profile between Sanchi and Bharhut, as
  Indus heads do.

## Results of the hundred-and-seventy-third set (added after the test; `predict_test173.py`, `results/predict_test173.md`)

Seven held, three failed. 374 Prakrit donor names from Lüders 1912 (Sanchi 260, Bharhut 39 distinct). **Indus names
are built like early Prakrit donor names.** The Prakrit names are person-like between Sanchi and Bharhut (PK1: 5.91,
0.13, 0.85) and as open as the Indus names (PK2: 5.07 against 5.91; the per-length check was not possible, Bharhut
being too small), and they recur between the sites beyond combinatorics (PK9: 5 against 0.2). The Indus closure R and
length distribution are nearer the Prakrit names than the Old Tamil cores (PK4: log distance 0.39 against 0.89; PK5:
JSD 0.055 against 0.110). Prakrit names end in a stock of compound heads, -rakhita, -guta, -data, -dina, -mita, -deva,
-giri, -pālita (PK6: the top ten cover 41%), and the ten commonest Indus heads cover almost exactly the same share of
Indus names (PK7: 43%): the 'modifier + stock head' build of names like Dhama-rakhita or Naga-dina matches the Indus
'opener + head' build. Failed: Prakrit names do not close the last akshara (PK3: R 1.05; the heads are two aksharas
long, so the last akshara alone is not a closed set), shared names are not shorter (PK8: 5 names only) and the
two-akshara heads are not title-like between the sites (PK10: 2.54, 0.32, 0.69; with 39 Bharhut names the catches are
small).

**What this does and does not show.** Together with set 172 it turns the dominant-ending argument around: Prakrit donor
names also carry one near-universal ending (the genitive -sa of the donation formula), so an Indus ending on 82% of
names fits an Indo-Aryan donor-style formula as well as the Tamil masculine -aṉ. On name structure the Indus names
resemble early Indo-Aryan donor names more than the literary Old Tamil names available here. It does not decide the
language: the Tamil list is literary and of another genre, no Tamil-Brahmi donor-name list could be built (the only
digital copy of Mahadevan 2003 is unusable OCR), aksharas are not Indus signs, and a Dravidian naming system of the
same 'modifier + stock head' kind would give the same statistics. Tally, counting parts: 1210 held, 1134 failed (2344
registered).

# Hundred-and-seventy-fourth set, registered before testing (24 September 2026): the matching Dravidian comparator, Tamil names from donation records (ten hypotheses)

The fair counterpart to set 173: Tamil personal names from records of donations, taken from English scholarly
translations as the Prakrit names were taken from Lüders's English summaries. Source: the DHARMA Tamil corpora
(erc-dharma tfa-pallava, tfa-sii, tfa-tamilnadu, tfa-pandya, tfa-cirkali, tfa-kotumpalur, tfa-uttiramerur; CC BY 4.0;
Pallava to later periods, c. 7th-16th centuries, so further from the Indus period than the Prakrit list), parsed by
`lang_names.tam_records`: capitalised words with Tamil diacritics ending in a personal suffix, place-name endings
excluded (1,402 distinct; some titles and places remain). Elements = aksharas (vowels a ā i ī u ū e ē ai o ō au;
trailing consonants joined to the last). Catches: the SII corpus against the Pallava corpus. Prakrit = set 173's list.
Methods as set 173.

- **TD1** Tamil record names are person-like (SII against Pallava).
- **TD2** The Indus estimate/observed ratio is within a factor of 2 of the Tamil record names' (pooled).
- **TD3** Tamil record names close the last element: R < 1.
- **TD4** On a log scale the Indus R is closer to the Prakrit R than to the Tamil record R.
- **TD5** The Indus body length distribution is closer (JSD) to the Prakrit names than to the Tamil record names.
- **TD6** The ten commonest final two-akshara endings of Tamil record names cover a share within 0.15 of the Indus
  top-ten head share (43%).
- **TD7** The Indus top-ten head share is closer to the Prakrit share (41%) than to the Tamil record share.
- **TD8** The commonest final akshara of Tamil record names (expected -ṉ) covers a share closer to 740's 82% of Indus
  names than the commonest final akshara of the Prakrit names does.
- **TD9** Real Tamil record names recur between the catches more than akshara-shuffled names (above 95% of 1,000).
- **TD10** Of TD4, TD5 and TD7, at least two favour the Prakrit names (name structure nearer Indo-Aryan donor names
  than Dravidian donor names).

## Results of the hundred-and-seventy-fourth set (added after the test; `predict_test174.py`, `results/predict_test174.md`)

Seven held, three failed. 1,396 distinct Tamil names from the DHARMA donation records (SII 522, Pallava 477). They are
person-like (TD1: 7.20, 0.07, 0.75), as open as the Indus names (TD2: quotient 0.70) and recur beyond combinatorics
(TD9: 35 against 0.5), like the Prakrit donor names: the genre behaves the same in both languages.

**The two comparators split the evidence.** Nearer the Prakrit (Indo-Aryan) donor names: the closure of the last
element (TD4: log distance 0.37 against 0.79; Tamil record names do not close their last akshara, TD3: R 1.60) and,
the clearest difference, the stock of compound heads: the ten commonest Indus heads cover 43% of names, the Prakrit
compound heads (-rakhita, -guta, -dina ...) 35% of distinct names, the Tamil two-akshara endings only 16% (TD6 fails,
TD7 holds). Nearer the Tamil names: the length distribution, almost identical (TD5 fails: JSD 0.009 against 0.056;
means 4.27 signs, 4.46 and 3.61 aksharas), and the dominance of one ending (TD8: 740 on 82%, Tamil -ṉ on 47%, the
commonest Prakrit stem ending on 23%). TD10 holds by its registered rule (two of three comparisons favour Prakrit),
but with the length result pointing strongly the other way the honest reading is a split, not a verdict.

Caveats: the Tamil records are 7th-16th century (the Prakrit list 200 BCE-400 CE), and many of their names are
Sanskrit-derived royal or religious names; the Prakrit names are stems without the case ending while the Tamil ones
carry the suffix; aksharas are not Indus signs; both lists carry extraction noise. Summary of sets 171-174: a
Sumerian-type name structure is excluded; between Indo-Aryan and Dravidian, Indus names share the 'modifier + stock
head' build of early Prakrit donor names and the length and single dominant suffix of Tamil names; the language is
not decided by name structure. Tally, counting parts: 1217 held, 1137 failed (2354 registered).

# Hundred-and-seventy-fifth set, registered before testing (24 September 2026): contemporary Tamil-Brahmi donor names (ten hypotheses)

The owner found and supplied the route to a contemporary Dravidian donor list: the page scans of I. Mahadevan, *Early
Tamil Epigraphy* (2003) at the Internet Archive. Its Appendix II (Index to Personal Names, pp. 656-658) was
transcribed by eye from the scans (107 full names from the cave-bed donor inscriptions, c. 2nd century BCE - 4th
century CE; the OCR is unusable). Personal name = the last word of each full name (hyphens and paragogic joins
removed), as the Prakrit list takes the donor's own name; aksharas as set 174. This is the same period, region and
genre as the Prakrit donor names of set 173. The list is small, so no capture-recapture; structure tests only, with
rarefaction to the smallest list. Prakrit = set 173's names; Tamil records = set 174's.

- **TB1** Tamil-Brahmi names close the last element: R < 1.
- **TB2** On a log scale the Indus R is closer to the Prakrit R than to the Tamil-Brahmi R.
- **TB3** The Indus body length distribution is closer (JSD) to the Prakrit names than to the Tamil-Brahmi names.
- **TB4** The ten commonest final two-akshara endings of Tamil-Brahmi names cover a share within 0.15 of the Indus
  top-ten head share.
- **TB5** The Indus top-ten head share is closer to the Prakrit share than to the Tamil-Brahmi share.
- **TB6** The commonest final akshara of Tamil-Brahmi names (expected -ṉ) covers a share closer to 740's share of Indus
  names than the commonest final of the Prakrit names does.
- **TB7** The mean Tamil-Brahmi name length (aksharas) is within 1 of the Indus body mean (signs).
- **TB8** Of TB2, TB3 and TB5, at least two favour the Prakrit names.
- **TB9** Tamil naming is stable over time: the -ṉ share of Tamil-Brahmi names is within 0.15 of the Tamil record
  names' share (set 174).
- **TB10** At the same period the two languages' donor names are distinguishable on the dominant final: the
  Tamil-Brahmi and Prakrit commonest-final shares differ by more than 0.2.

## Results of the hundred-and-seventy-fifth set (added after the test; `predict_test175.py`, `results/predict_test175.md`)

Seven held, three failed. 104 Tamil-Brahmi donor names (the owner located the page scans; the index was transcribed by
eye and checked against a second copy the owner supplied), 305 Prakrit, 628 Indus, rarefied to 104. **At the same
period and in the same genre, the structure statistics of Indus names sit with the Prakrit names.** Closure: Indus R
0.83, Prakrit 0.90, Tamil-Brahmi 1.45 (TB2: log distance 0.08 against 0.56; Tamil-Brahmi names do not close their last
akshara, TB1 fails); length: JSD 0.056 against 0.153 (TB3; Tamil-Brahmi names are short, 3.0 aksharas against 4.3
Indus signs, TB7 fails); stock of heads: Indus 43%, Prakrit 35%, Tamil-Brahmi 30% (TB5; TB4 holds, Tamil-Brahmi within
0.15 too). TB8 holds, three of three. **The one Tamil-like feature is the dominant ending** (TB6: 740 on 82% of Indus
names, -ṉ on 73% of Tamil-Brahmi names, the commonest Prakrit stem ending on 23%), and the two languages differ clearly
on it (TB10: 0.73 against 0.23). But that contrast is partly made by the sources: the Tamil-Brahmi names are given with
their personal suffix -aṉ, while Lüders's summaries give Prakrit names as stems without the case ending (-o, -sa)
that every Prakrit donor name carries in the inscriptions. Tamil naming is not stable in this measure between the
Tamil-Brahmi and the later records (TB9 fails: 0.73 against 0.47).

Reading, with caveats: on name structure (closure, length, stock heads) the Indus names resemble early Prakrit donor
names more than contemporary Tamil-Brahmi donor names; on the dominant suffix they resemble Tamil, but the source
format makes that comparison unfair to Prakrit. This is not a language identification. The Tamil-Brahmi list is
small (104), aksharas are not Indus signs (if Indus signs are word signs, lengths are not comparable at all), several
Tamil-Brahmi donors bear Prakrit names themselves (Kasapaṉ, Cantirananti, Sapamitā), so South Asian donor naming
crossed languages, and the Indus texts are some two thousand years older than either list. Tally, counting parts:
1224 held, 1140 failed (2364 registered).

# Hundred-and-seventy-sixth set, registered before testing (24 September 2026): decipherment loop 1, structure and roles (eight hypotheses)

The owner set a standing goal: loops of registered tests toward decipherment, with a progress metric measured each
loop (`progress.py`, `PROGRESS.md`). Baseline: S 4.712 bits per sign held out (24.9% of unigram entropy explained),
R 56.2% of tokens with a tested role, M 16.6% anchored, P 0 sound values, L 4 families open. Loop 1 aims at S and R.
New model components, each added to the baseline mixture (tri + pos + end, discounted) with weights fitted on a
development split of the training lines only (as set 125), evaluated on progress.py's fixed test split:
- role: P(sign | left-context role of the previous token: numeral, ending, closer, marker, heading sign, other);
- cls: P(sign | distributional class of the previous sign), 30 classes by k-means on next-sign distributions of
  signs with 10+ training tokens (rarer signs in one class), fitted on training lines only;
- nval: after a numeral run, P(sign | value bucket of the run: 1, 2, 3, 4, 5-8, 9+); elsewhere the unigram.
Role extension: 'name modifier' = body signs before the head in lines parsed as names (R.name_of), from the tested
head-final name grammar (H7, DT1-DT4).

- **LP1** Adding 'role' lowers S by 0.03 bits or more.
- **LP2** Adding 'cls' lowers S by 0.03 or more.
- **LP3** Adding 'nval' lowers S by 0.02 or more.
- **LP4** The best combination of the three lowers S by 0.05 or more (the model in progress.py is then updated).
- **LP5** Adding the 'name modifier' role raises R above 70%.
- **LP6** The modifier role is stable: signs that are modifiers in the training lines stand inside name bodies
  (modifier or head) in 80%+ of their tokens in the test lines.
- **LP7** Heads are a stable class too: signs that are heads in training stand as heads in 50%+ of their test tokens
  that sit in name bodies.
- **LP8** The loop's S gain holds on B alone (M77 additions, own 80/20 split): the best combination beats the baseline
  mixture there.

## Results of the hundred-and-seventy-sixth set (added after the test; `predict_test176.py`, `results/predict_test176.md`)

Three held, five failed. **Structure (S) does not move**: the role, class and numeral-value components each get zero
weight in the fitted mixture (LP1-LP4: 4.712 bits with or without them); the trigram with position and distance from
the end already carries what they encode. LP8 holds only on a tie (B: 4.562 both ways) and adds nothing. **Roles (R)
move**: counting body signs before the head of a parsed name as modifiers, from the tested head-final name grammar,
lifts R from 56.2% to 72.9% as measured by progress.py (LP5's quick count, 76.9%, counted some tokens twice). The
role is positional, not a fixed property of the sign: training modifiers stay inside name bodies only 57% of the time
in the test lines (LP6 fails), while training heads stay heads 88% of the time (LP7). The metric's R now includes the
modifier role, read as 'the job of this token is fixed by its slot'. Tally, counting parts: 1227 held, 1145 failed (2372
registered).

# Hundred-and-seventy-seventh set, registered before testing (24 September 2026): decipherment loop 2, longer contexts, new picture anchors, bare-line roles (eight hypotheses)

Metric after loop 1: S 4.712, R 72.9%, M 16.6%, P 0, L 4. Loop 2 aims at S with a variable-order model (texts repeat
long formulas that a trigram cannot see), at M with the two provisional picture anchors of the eleventh pass, tested on
objects not used to propose them, and at R with the bare lines (names written without the ending, twenty-first set).
VO model: interpolated Witten-Bell n-gram of order 1-5 over signs with line-start padding, unknown signs uniform;
evaluated on progress.py's fixed split, alone and as an extra component of the loop-1 EM mixture. 'New objects' = F
objects whose CISI number is not among A's objects. Motif codes: multi-headed animal 'Mult'; tree / plant 'Phyt',
'Pipal', 'Plant' (field 18 or 19).

- **VP1** The VO model alone reaches S at least 0.05 bits below the baseline mixture (4.712).
- **VP2** As an extra mixture component it lowers S by 0.05 or more.
- **VP3** The same VO model predicts the lines read backwards (right to left in reading order) at least 0.05 bits
  worse than forwards (the constraint sits on the endings, which forwards the model sees last).
- **VP4** New objects carrying sign 347 carry the multi-headed animal in 50%+ (anchor 347 = multi-headed animal).
- **VP5** New objects carrying sign 460 carry a tree / plant picture in 50%+ (anchor 460 = tree).
- **VP6** At least one of VP4-VP5 holds with 3+ new objects (else M cannot move this loop).
- **VP7** Bare lines of 2+ signs (genre 'bare') have a last sign attested as a name head in 50%+ (they are names
  without the ending), which licenses head / modifier roles for them.
- **VP8** With those bare-line roles R rises by 3 points or more.

## Results of the hundred-and-seventy-seventh set (added after the test; `predict_test177.py`, `results/predict_test177.md`)

Two held, six failed. **S does not move.** A variable-order (Witten-Bell, order 5) model is worse alone (VP1: 5.595
bits) and adds only 0.005 inside the mixture (VP2: 4.707, weight 0.13), short of the registered 0.05, so the metric's
model is unchanged: the repeated formulas are already captured by the trigram with position and end distance. Reading
the lines backwards costs no more than forwards (VP3: 5.586 against 5.595). **M cannot move by this route**: the
provisional picture anchors cannot be tested on objects that were not used to propose them (VP4: no new object carries
347; VP5: two carry 460, neither with a plant). **R moves**: bare lines end in a sign attested as a name head in 70%
(VP7), which licenses head and modifier roles for them, and R rises from 72.9% to 81.1% (VP8). Tally, counting parts:
1229 held, 1151 failed (2380 registered).

# Hundred-and-seventy-eighth set, registered before testing (24 September 2026): decipherment loop 3, meanings from depiction checked by use (seven hypotheses)

Metric after loop 2: S 4.712, R 81.1%, M 16.6%, P 0, L 4. S and R are near what internal modelling reaches; loop 3
aims at meaning. A sign's depiction (Fairservis 1992's identifications, 'sure' or 'likely', keys/fairservis1992_raw.tsv;
categories A humans, C/D animals, E plants, H weapons, I implements, Q fish-like) becomes a class-level meaning anchor
only if it predicts how the sign is used, tested on B (Mahadevan's M77 additions, not used in the earlier finding
that 740 heads are people and trades, set 20). Names in B via R.name_of; a class needs 10+ B names headed by its signs,
else its test fails as untestable. Adoption rule, registered now: every class whose test holds enters a new metric
component M+ ('share of tokens whose sign has a depiction-class meaning confirmed by use'); M itself is unchanged.

- **DC1** Names in B headed by a human-figure sign take 740 in 90%+.
- **DC2** Names in B headed by a weapon or implement take 740 in 90%+.
- **DC3** Names in B headed by a fish-like sign take 520 more often than other names (Fisher).
- **DC4** Names in B headed by an animal sign take 740 in 90%+.
- **DC5** Names in B headed by a plant sign take 740 in 90%+.
- **DC6** In B, the depiction category of the head predicts the ending beyond permutation (MI).
- **DC7** At least two classes pass (M+ above 0).

## Results of the hundred-and-seventy-eighth set (added after the test; `predict_test178.py`, `results/predict_test178.md`)

Six held, one failed. On B (Mahadevan's additions, independent of the earlier finding), what a head sign depicts
predicts the ending (DC6: MI 0.20 bits over 129 names, p = 0.0001): names headed by human figures take 740 in 25 of 25
(DC1), by weapons or implements 27 of 29 (DC2), by plants 25 of 25 (DC5), and by fish-like signs 520 in 40% against 8%
(DC3, p < 0.0001). No B name is headed by an animal sign (DC4 fails, untestable). Under the registered rule the four
classes enter M+, which is 41.4% of tokens (M strict stays 16.6%). Caveat, noted after the test: 740 is the default
ending (about 88% of names), so 'takes 740' is weak evidence class by class (25 of 25 against an 88% base has p about
0.04); the clear evidence is the fish class and the overall MI. What M+ says is that the depicted category of a name's
head is part of how the script works (fish names form their own ending class), not that any word is read. Tally,
counting parts: 1235 held, 1152 failed (2387 registered).

# Hundred-and-seventy-ninth set, registered before testing (24 September 2026): decipherment loop 4, sound values from substitution (seven hypotheses)

Metric after loop 3: S 4.712, R 81.1%, M 16.6% (M+ 41.4%), P 0, L 4. Loop 4 aims at P. Test: in a script that writes
sound, signs that replace each other in the same slot of otherwise identical words should often sound alike, so a
correct key gives substitutable sign pairs more similar values than a shuffled key does. Substitution pairs: minimal
pairs of distinct name bodies (A + B, R.name_of) of equal length differing at one position, both signs lexical (not
numerals, endings, closers, 400, 90), each sign pair weighted by the number of frames it appears in. Similarity of two
values = 1 - Levenshtein distance / longer length on the consonant skeleton (bench.skel) plus the vowels. Chance = the
key's values shuffled among its keyed signs (1,000 draws, one-sided p). Keys: Fairservis 1992 (Dravidian), Parpola 1994
(Dravidian), Yajnadevam 2024 (Sanskrit, xlits.csv), Mahadevan 2014, Kak 1988. Control with a known answer: Linear B
(DAMOS lexicon words; syllabograms with their standard values, minimal pairs of distinct words). Rule for P: a key's
signs count toward P only if it passes on A-names and on B-names separately and the Linear B control passes.

- **SP1** Linear B: substitutable syllabograms have more similar values than shuffled values (the method can see sound).
- **SP2** Fairservis's key passes (p < 0.05, 10+ keyed pairs).
- **SP3** Parpola's key passes.
- **SP4** Yajnadevam's key passes.
- **SP5** Mahadevan's 2014 key passes.
- **SP6** Kak's 1988 key passes.
- **SP7** At least one key passes on both A-names and B-names separately (the P rule).

## Results of the hundred-and-seventy-ninth set (added after the test; `predict_test179.py`, `results/predict_test179.md`)

One held, six failed. **The method can see sound**: in Linear B, syllabograms that replace each other in minimal pairs
of words have more similar standard values than shuffled values (SP1: 2,111 pairs, 0.256 against 0.213, p = 0.001).
**No published Indus key passes**: Fairservis (SP2: 676 pairs, p = 0.10), Parpola (SP3: 48, p = 0.16), Yajnadevam
(SP4: 3,570, p = 0.08); Mahadevan's and Kak's keys cover almost no substitution pairs (SP5, SP6). Two keys pass on A's
names and fail on B's (Fairservis p = 0.04 then 0.54; Yajnadevam p = 0.03 then 0.39): Yajnadevam's key was fitted to the
indus-website corpus from which A derives, so an A-only pass followed by a B failure is the signature of fitting, not of
true values. SP7 fails; P stays 0. The test is kept as a tool: any proposed sound key must pass it on both samples.
Tally, counting parts: 1236 held, 1158 failed (2394 registered).

# Hundred-and-eightieth set, registered before testing (24 September 2026): decipherment loop 5, which language's words for the pictures make substitutes sound alike? (seven hypotheses)

Metric after loop 4: S 4.712, R 81.1%, M 16.6% (M+ 41.4%), P 0, L 4. Loop 4 validated a sound test on Linear B
(substitutable signs sound alike under the true values). Loop 5 applies the rebus principle: in a logo-syllabic script
a sign's value is the word for what it depicts, in the true language. Depiction keys: for each sign Fairservis
identifies ('sure'/'likely'), the concept is the first word of his identification after articles and number words
(automatic, no hand fixes; 'combination' entries skipped); each language's value is the first glossary entry whose
sense begins with that concept: Dravidian = DEDR entry meanings (dedr_entry_v11), Sanskrit = Monier-Williams
(bench.lexicon_mw), Sumerian = ePSD2 (sux_gloss.tsv, guide word and senses). Substitution pairs, similarity and
shuffle test as set 179, run on A-names and B-names separately.

- **DK1** The Dravidian depiction key passes on A and on B (p < 0.05 each, 10+ keyed pairs each).
- **DK2** The Sanskrit depiction key passes on A and on B.
- **DK3** The Sumerian depiction key passes on A and on B.
- **DK4** On all pairs pooled, the Dravidian key's excess similarity (observed minus shuffled mean) is larger than the
  Sanskrit key's.
- **DK5** The Dravidian key's excess is larger than the Sumerian key's.
- **DK6** At least one language passes on both samples (a P candidate; P itself needs a second, independent test).
- **DK7** The three keys cover 10+ substitution pairs each (the test has power).

## Results of the hundred-and-eightieth set (added after the test; `predict_test180.py`, `results/predict_test180.md`)

Two held, five failed. No depiction key passes on both samples (DK6): Dravidian passes on A only (DK1: p = 0.046, then
0.62 on B), Sumerian on A only (DK3: p = 0.004, then 0.054), Sanskrit on neither (DK2). The Dravidian excess is above
the Sanskrit one (DK4: 0.017 against -0.008) and below the Sumerian one (DK5: 0.019); the test had power (DK7: 283-504
pairs). **Caveat that empties the comparison, noted after the test:** the registered lookup (first glossary entry whose
sense begins with the concept) chose obscure words: 'man' became Monier-Williams agredadus and a DEDR form anmu·ṛo·n,
not the ordinary words (nara, puruṣa; āḷ, maṉ). The keys therefore measure lookup noise as much as language, and no
language inference is drawn. The next loop repeats the test with a lookup that prefers the basic word. Tally, counting
parts: 1238 held, 1163 failed (2401 registered).

# Hundred-and-eighty-first set, registered before testing (24 September 2026): decipherment loop 6, a world-wide language search by rebus substitution (eight hypotheses)

Loop 5's depiction keys failed on lookup noise. Loop 6 replaces the lookup with basic vocabulary and replaces the three
hand-picked languages with every language that can be scored. Depiction map (fixed now, before any language is
scored): signs.FISH -> FISH; noun_class.HUMAN -> PERSON; signs.CRAB -> CRAB; signs.FIG -> FIG; and each sign Fairservis
identifies ('sure'/'likely') whose identification (before '=>') contains, first in this order, one of: woman ->
WOMAN, bow -> BOW, arrow -> ARROW, pot / jar / container -> POT, tree -> TREE, sun -> SUN, moon / crescent -> MOON,
rain -> RAIN (PRECIPITATION), mountain -> MOUNTAIN, river -> RIVER, drum -> DRUM, comb -> COMB, shield -> SHIELD,
sickle -> SICKLE, fence -> FENCE, roof / cover -> ROOF, grain -> GRAIN, leaf / pipal -> LEAF, duck -> DUCK, bee ->
BEE, spear -> SPEAR, axe -> AXE, basket -> BASKET, wheel -> WHEEL, man -> PERSON. Words: CLICS4 (clics4/cldf
forms, the first form of each language for each concept), compared as IPA segment strings (normalised Levenshtein
over segments). Substitution pairs as set 179 on A and on B names; pairs whose two signs map to the same concept are
left out (every language 'matches' them); chance = the language's words shuffled among the concepts (200 draws); z =
(observed - shuffled mean) / shuffled sd. Languages scored: those with words for 12+ of the mapped concepts and 30+
usable pairs. Families from CLICS4's Family_Name; Indo-Aryan = Indo-European languages of South Asia (longitude
66-92, latitude 6-36).

- **LS1** Dravidian languages have a mean percentile rank of 0.75 or more among all scored languages.
- **LS2** Indo-Aryan languages have a mean percentile rank of 0.75 or more.
- **LS3** The Dravidian mean z is above the Indo-Aryan mean z.
- **LS4** Among families with 5+ scored languages, Dravidian has the highest mean z.
- **LS5** The median z over all languages is below 0.5 (the test does not reward every language).
- **LS6** Scores are stable: Spearman between per-language z on A-pairs and on B-pairs is 0.3 or more.
- **LS7** The top-ranked language has z >= 2 on A-pairs and on B-pairs separately (a P candidate).
- **LS8** Control: with the concepts shuffled among the signs (20 shuffled maps), Dravidian's mean percentile falls
  below its real value in 19 of 20 (any Dravidian lead depends on the depictions).

## Results of the hundred-and-eighty-first set (added after the test; `predict_test181.py`, `results/predict_test181.md`)

Four held, four failed. 83 signs mapped to 23 depicted concepts; 100 concept pairs among substitutable signs; 503
CLICS4 languages scored. **No language signal.** Dravidian (Kannada, Malayalam, Tamil, Telugu) and Indo-Aryan
(Bengali, Hindi; Northern Pashto caught by the region filter) both sit at the 44th percentile (LS1, LS2 fail), Dravidian
slightly above Indo-Aryan in mean z (LS3: -0.22 against -0.41, both below zero). No family stands out (LS4: best Uralic
0.33), and the median z is -0.14 (LS5 holds: the test does not reward every language). The top languages (Ao Chungli
z 3.12, Embera, Lower Sorbian, Dargwa dialects, Hungarian) are what the maximum of 503 draws gives by chance (about 3):
LS7 'holds' (Ao Chungli A z 2.53, B z 2.08) but is a multiple-comparison artefact, not a P candidate. LS6's high
stability (0.79) reflects that A and B share most concept pairs, so the two samples are not independent at this level.
The shuffled-map control (LS8) puts Dravidian at 0 or near it in most shuffles, below its real 0.44 in 15 of 20, short of
the registered 19. Reading: basic words for what the signs depict, in any of 503 languages, do not make substitutable
Indus signs sound alike. Either the substitutions are not phonetic (signs alternate as words, not as sounds), or the
depictions are misidentified, or the language is not represented; a simple rebus reading of the depicted signs is not
supported. P stays 0; L unchanged (no family excluded, none favoured). Tally, counting parts: 1242 held, 1167 failed
(2409 registered).

# Hundred-and-eighty-second set, registered before testing (24 September 2026): decipherment loop 7, are substitutions semantic? (eight hypotheses)

Metric after loop 6: S 4.712, R 81.1%, M 16.6% (M+ 41.4%), P 0, L 4. Loop 6 found no phonetic signal in substitutions
under any language's words. Loop 7 asks whether substitutions are semantic instead: signs replacing each other because
they depict the same kind of thing, as word signs would. Categories: Fairservis letter (A humans, C/D animals, E
plants, F sky, G structures, H weapons, I implements, J containers, K measures, L cloth/ornaments, M drums, N landscape,
Q fish-like), with signs.FISH as Q and noun_class.HUMAN as A. Substitution pairs as set 179 (A + B names, lexical signs,
weighted by frames); chance = categories shuffled among the identified signs (1,000 draws).

- **SE1** Substitution pairs of two identified signs are same-category more often than chance.
- **SE2** SE1 holds with the fish series left out.
- **SE3** SE1 holds on B's names alone.
- **SE4** Human-figure signs' identified substitution partners are human figures in 30%+ of pair weight.
- **SE5** Same-category pairs are 40%+ of identified-pair weight.
- **SE6** Leave-one-out: an identified sign's category is the majority category of its identified partners (3+
  partners) in 50%+ of such signs, above the shuffled rate (95th percentile).
- **SE7** If SE6 holds, unidentified signs with 3+ identified partners and a 60%+ majority get that category; M+ rises
  by 2 points or more (adoption rule, registered now).
- **SE8** Signs that substitute across categories are rarer than within, even among signs of the same position class
  (heads only): same-category share among head-slot substitutions above chance.

## Results of the hundred-and-eighty-second set (added after the test; `predict_test182.py`, `results/predict_test182.md`)

One held, seven failed. **Substitutions are not semantic either.** Substitutable signs share a depicted category more
than chance only because the fish signs replace one another (SE1: 0.168 against 0.112, p = 0.024; without the fish
series 0.095 against 0.109, SE2 fails; B alone p = 0.066, SE3). Human figures almost never replace human figures (SE4:
1 of 138 pair weight), same-category pairs are a sixth of the total (SE5), a sign's partners do not predict its
category (SE6: 0.22 leave-one-out against a shuffled 95th percentile of 0.29), so no category could be inferred for
unidentified signs (SE7), and head-slot substitutions are not category-bound (SE8). Reading, with loop 6: the slots of
Indus names take signs without regard either to how their depicted words sound (in 503 languages) or to what they
depict, except that fish signs form a family. Either Fairservis's identifications are largely wrong, or the name
elements work like arbitrary name parts (as personal-name elements do in many naming systems), or both. M+ and P do
not move. Tally, counting parts: 1243 held, 1174 failed (2417 registered).

# Hundred-and-eighty-third set, registered before testing (24 September 2026): decipherment loop 8, are the depiction identifications coherent? (eight hypotheses)

Metric after loop 7: S 4.712, R 81.1%, M 16.6% (M+ 41.4%), P 0, L 4. Loops 6-7 found that substitutions follow neither
the sound of the depicted words nor the depicted category (except fish). Loop 8 asks whether the identifications are
the weak link. If a category is a real depiction class, its signs should look alike (shape) and be used alike
(context). Shapes: set 137's font renderings and mean pairwise IoU against 1,000 random sign sets of the same size;
contexts: set 62's context similarity (signs with 20+ tokens) against random pairs. Categories as set 182 (Fairservis
letters; signs.FISH; noun_class.HUMAN).

- **DI1** Human-figure signs (noun_class.HUMAN) form a shape family (p < 0.05).
- **DI2** Fairservis's A signs not in HUMAN still look like the HUMAN signs more than random signs do (mean best IoU).
- **DI3** Weapons and implements (H, I) form a shape family.
- **DI4** Control: the fish series forms a shape family (as SH6).
- **DI5** Human-figure signs are used alike: mean context similarity of HUMAN pairs above random pairs (p < 0.05).
- **DI6** Weapons and implements are used alike.
- **DI7** Across categories with 3+ signs, shape cohesion and context cohesion correlate (Spearman > 0).
- **DI8** The fish series is used alike (context), the known positive case.

## Results of the hundred-and-eighty-third set (added after the test; `predict_test183.py`, `results/predict_test183.md`)

Five held, three failed. **The identification groups are coherent in shape**: human figures (DI1: mean IoU 0.38, p =
0.001), weapons and implements (DI3: 0.23, p = 0.004) and the fish (DI4: 0.32, p = 0.001) each form a visual family.
(DI2 had no case: Fairservis's A signs are all in HUMAN.) **But only some groups are used alike**: the fish strongly
(DI8: context similarity 0.16, p = 0.001), weapons and implements weakly (DI6: 0.06, p = 0.04), human figures not at all
(DI5: 0.05 over 7 signs, p = 0.27); across categories, looking alike does not go with being used alike (DI7: Spearman
-0.07). Reading, with loops 6-7: the depictions are not simply wrong (the groups are visually real), but a shared
picture does not mean a shared use, except for the fish, which behave as one family of variants of a single word or
class; human-figure signs behave as distinct name elements. What a sign depicts is therefore a weak guide to its
reading beyond the fish class. Metric unchanged. Tally, counting parts: 1248 held, 1177 failed (2425 registered).

# Hundred-and-eighty-fourth set, registered before testing (24 September 2026): decipherment loop 9, is the cage a grammatical affix? (seven hypotheses)

Metric after loop 8: S 4.712, R 81.1%, M 16.6% (M+ 41.4%), P 0, L 4. Two of the closers (226, 241) are fish drawn
inside a 'cage' of four small strokes. If the cage is a grammatical marker that attaches to many signs, that is a
compositional rule inside the signs, the kind of structure a decipherment builds on. Caged / base pairs from Parpola's
sign list (CISI digitisation, cisi.p2icit; 'caged by four small vertical strokes'): 226/220, 232 and 153/231, 236/235,
241/240, 144/142, 393/tree family (390, 392, 405, 406, 407, 409, 48, 64), 895/892, 466/A family (465, 467, 468, 471,
472, 474), 804/leaf-tree (803, 838), 878/877, 689/71. Distinct lines of A + B unless stated. 'Final' = last sign of the
line, or followed only by 400 / 90. Fisher tests pool the tokens of all caged signs against all their bases.

- **CG1** Caged signs are line-final more often than their bases.
- **CG2** Caged signs are followed by 740 or 520 less often than their bases (the cage takes the place of the ending).
- **CG3** The effect is not only the fish: CG1 holds for the non-fish pairs pooled.
- **CG4** Caged and base signs share their preceding signs (cosine of preceding-sign distributions, pooled pairs) more
  than random sign pairs of similar frequency do (the cage attaches to the same stems).
- **CG5** CG1 holds on B alone.
- **CG6** Caged signs are used as closers: 60%+ of their tokens are line-final with no 740 / 520 anywhere after them.
- **CG7** If CG1, CG2 and CG6 hold, R gains a 'caged marker' role for caged tokens not already counted (adoption rule).

## Results of the hundred-and-eighty-fourth set (added after the test; `predict_test184.py`, `results/predict_test184.md`)

Five held, one failed (CG7 is the adoption rule). **The cage works like a grammatical affix drawn around a sign.**
Caged signs (a sign inside four small strokes; 92 tokens) end the line in 73% against 20% for their plain bases (CG1,
p < 0.0001), are never followed by 740 or 520 (CG2: 0 of 92 against 16%), attach to the same stems as their bases
(CG4: cosine of preceding signs 0.43 against 0.09 for random partners, p = 0.001), and behave as closers (CG6: 73%
final with no ending after them). It replicates on B (CG5: 82% against 28%). The cage turns a name's head into a
closing form that stands in place of the ending: morphology written inside the sign. Limit: outside the fish, caged
signs are too few (17 tokens) to confirm the rule (CG3: 47% against 35%, n.s.), so it is established for the caged fish
and suggested for the rest. Under CG7 the caged signs not already among the closers get a 'caged marker' role in R.
Tally, counting parts: 1253 held, 1178 failed (2431 registered).

# Hundred-and-eighty-fifth set, registered before testing (24 September 2026): decipherment loop 10, do the other fish marks work as affixes? (seven hypotheses)

Metric after loop 9: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4. Loop 9 found the cage works as a grammatical affix.
Loop 10 asks the same of the other marks added to the fish: plain 220; stroke in the body 231; horizontal bar 233;
caret-shaped 'roof' hat 235; whiskers 240 (Parpola's list via the CISI digitisation). Outside the fish these marks are
too rare to test (1-18 tokens). Names via R.name_of on distinct lines; A and B (M77 additions) separately.

- **MF1** In A, the variant predicts its slot in the name (head against modifier) beyond permutation (MI).
- **MF2** MF1 holds on B.
- **MF3** The roof fish 235 stands directly before another fish sign more often than the plain fish does (Fisher,
  A + B): the hat marks an attribute.
- **MF4** Names headed by the whisker fish 240 take 520 more often than names headed by the plain fish 220 (Fisher,
  A + B).
- **MF5** The direction of each variant's head-slot difference from the plain fish is the same in A and in B for all
  four marked variants.
- **MF6** On B, the value of a numeral run before a fish depends on the variant (MI; NP4's result on a new sample).
- **MF7** The variant depends on the preceding sign beyond permutation (MI), in A and in B (the mark agrees with its
  context, as inflection would).

## Results of the hundred-and-eighty-fifth set (added after the test; `predict_test185.py`, `results/predict_test185.md`)

Five held, two failed. **The marks added to the fish change its job.** The variant predicts whether the fish is a
name's head or a modifier, in A (MF1: MI 0.036, p = 0.0001) and B (MF2: 0.074, p = 0.0007). The roof-hat fish 235
stands directly before another fish in 40% against 15% for the plain fish (MF3, p < 0.0001): the hat marks an
attribute. The bar (233), roof (235) and whisker (240) fish are less often heads than the plain fish 220 in both
samples (A -0.11 / -0.21 / -0.18; B -0.21 / -0.29 / -0.24); MF5 fails only on the stroke fish 231, whose difference is
near zero with opposite signs (-0.03, +0.01). The variant agrees with its context: it depends on the preceding sign in
both samples (MF7: MI 0.79 and 1.02, p = 0.0001) and, on B, on the counted value before it (MF6: p = 0.012, NP4
replicated on a new sample). Whisker-fish names do not take 520 more than plain-fish names (MF4). Reading, with loop
9: the fish family is one word written with a small set of marks that change its grammatical job, the plain fish as
head, the marked fish as attributive or derived forms, the caged fish as a closing form; morphology inside the signs.
Roles already cover these tokens, so the metric does not move. Tally, counting parts: 1258 held, 1180 failed (2438
registered).

# Hundred-and-eighty-sixth set, registered before testing (24 September 2026): decipherment loop 11, the strokes inside the jar (eight hypotheses)

Standing goal (owner, 24 Sept): loops until 20 in a row make no progress (PROGRESS.md stopping rule). Metric after loop
10: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4; no-progress streak 0. Loops 9-10 found marks that change a sign's
grammatical job (the cage; the fish marks). Loop 11 asks the same of the jar: 740 (plain), 741 (one stroke inside),
742 (two), 745 (three), per Parpola's list (P324-P327 via the CISI digitisation). Distinct lines; A and B separately
where stated. 'Final' = last sign or followed only by 400 / 90.

- **JV1** Stroked jars (741, 742, 745) are final less often than the plain jar (A; Fisher).
- **JV2** JV1 holds on B.
- **JV3** Stroked jars are directly followed by 740 or 520 more often than the plain jar is (A + B): a stroked jar can
  be a head that takes the ending.
- **JV4** Stroked jars are preceded by a numeral less often than the plain jar (the strokes inside do the counting).
- **JV5** The inner strokes are graded: across 740, 741, 742, 745, the share final falls (or rises) monotonically with
  the stroke count (Spearman |rho| = 1 over the four points).
- **JV6** The stroked jars are relatively more frequent on tablets than on seals, compared with the plain jar (F;
  Fisher).
- **JV7** 741 and '740 1' (the jar followed by a single stroke) stand in the same frames more than random sign pairs of
  similar frequency (the stroke inside = a stroke after).
- **JV8** Progress rule: at least one of JV1/JV3 holds with a same-direction replication on B.

## Results of the hundred-and-eighty-sixth set (added after the test; `predict_test186.py`, `results/predict_test186.md`)

Five held, three failed. **The strokes inside the jar turn the ending into a name element.** The plain jar 740 ends
the line in 88% of its tokens; the stroked jars 741, 742, 745 in 3% (JV1, A) and 14% (JV2, B). They are occasionally
followed by an ending themselves (JV3: 1.0% against 0.1%, p = 0.02) and are preceded by a numeral less often (JV4:
4.2% against 7.1%). They belong to seals more than the plain jar does (JV6 fails the other way: 20% on tablets
against 42%). The three stroke counts are not graded (JV5: final 0.86, 0.07, 0.12, 0.06), and 741 does not stand where
'740 1' stands (JV7: no shared frame), so the inner stroke is not a stroke written after the jar. Reading, with loops
9-10: a third mark that changes a sign's job, here turning the commonest ending into an internal element of the
name; the script marks grammatical function by strokes and cages drawn onto a base sign. JV8 (progress rule) holds:
new and replicated on B. Tally, counting parts: 1263 held, 1183 failed (2446 registered).

# Hundred-and-eighty-seventh set, registered before testing (24 September 2026): decipherment loop 12, doubling and brackets (seven hypotheses)

Metric after loop 11: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4; streak 0. An automatic sweep of Parpola's list for
'base + mark' pairs (a marked sign whose description begins with a base sign's description) finds few pairs beyond
those already tested: cage (8), stroke (the jar, 3), bracket (2: 101-103/100, 905/904-927), hatching (1: 924/923).
Loop 12 tests the other visible device, doubling (a lexical sign written twice in a row, TY4: 5% of lines, mostly 615),
and the brackets. Distinct lines; A and B separately.

- **DB1** A lexical sign written doubled (x x) ends the line (or stands before 400 / 90) less often than the same sign
  written once, pooled over signs doubled 3+ times (A; Fisher).
- **DB2** DB1 holds on B.
- **DB3** Doubled pairs are followed by 740 / 520 less often than the single sign is (A + B).
- **DB4** Doubled pairs stand at the start of the line more often than the single sign (A + B): doubling marks the
  opening element.
- **DB5** The doubled 615 has a different set of following signs from the single 615 (JSD above the 95th percentile of
  random splits of 615 tokens).
- **DB6** Bracketed signs (101/103, 905) are final more often than their bases (100; 904, 927) (A + B).
- **DB7** Progress rule: at least one of DB1, DB3, DB4 holds in A with the same direction in B.

## Results of the hundred-and-eighty-seventh set (added after the test; `predict_test187.py`, `results/predict_test187.md`)

Three held, four failed. Signs doubled 3+ times: 220, 390, 615, 700, 790, 809, 820, 892 (147 doubled tokens, 1,323
single). **Doubled signs sit at the edges of texts.** They end the line more often than the single sign, not less
(DB1 and DB2 fail the other way: 41% against 21% in A, 34% against 26% in B) and open it more often (DB4: 36% against
29%, same direction in A and B), and they take the ending as often as single signs (DB3). The doubled 615 is followed
by different signs from the single 615 (DB5: JSD 0.58 against a random-split 95th percentile of 0.36). Brackets do not
change position (DB6, 23 tokens). Reading: doubling is a distinct form, not just emphasis: a doubled sign tends to
stand as a text's first or last element (short texts made of a doubled sign and little else), consistent with a
plural, collective or total. DB7 holds (DB4 new and replicated in direction on B): progress, streak 0. Tally, counting
parts: 1266 held, 1187 failed (2453 registered).

# Hundred-and-eighty-eighth set, registered before testing (24 September 2026): decipherment loop 13, more training text for S (five hypotheses)

Metric after loop 12: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4; streak 0. S has not moved in twelve loops:
richer model components added nothing. Loop 13 adds data instead. The fuller ICIT export (F) holds distinct lines that
are not among progress.py's lines (A + B); adding them to the training lines (never to the fixed test lines, and
excluding any F line identical to a test line) is a legitimate improvement of the same benchmark. Model as
progress.py (tri + pos + end, discounted; weights fitted on a development split of the training lines).

- **SX1** Training on progress.py's training lines plus F's extra distinct lines lowers S by 0.03 bits or more (the
  metric's training data is then extended).
- **SX2** Adding only F's extra seal lines lowers S by 0.01 or more.
- **SX3** With the extra lines, the share of test tokens unseen in training falls by 0.5 points or more.
- **SX4** The gain is not only from copper tablets: adding F's extra lines without copper tablets lowers S by 0.02 or
  more.
- **SX5** Progress rule: SX1 holds.

## Results of the hundred-and-eighty-eighth set (added after the test; `predict_test188.py`, `results/predict_test188.md`)

None held, five failed. Adding F's 432 extra distinct lines to the 2,177 training lines makes S slightly worse, not
better (SX1: 4.712 to 4.719; seals only 4.723, SX2; without copper 4.717, SX4), though it cuts the unseen test signs
from 2.05% to 1.58% (SX3, short of 0.5 points). The extra lines apparently follow different transcription habits (F
is the fuller export, with fragmentary and variant readings that A's cleaning left out), so more text of that kind
does not help the benchmark. No progress this loop: streak 1. Tally, counting parts: 1266 held, 1192 failed (2458
registered).

# Hundred-and-eighty-ninth set, registered before testing (24 September 2026): decipherment loop 14, strokes inside the U (seven hypotheses)

Metric after loop 13: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4; streak 1. Loop 11 found that strokes inside the
jar change its job. Parpola's list has the same device on the U: plain U 700 (P310, the measure container of the count
tokens); U with a long vertical stroke inside 704 / 705 / 706 (P316; 705 / 706 are the signs of the closing formula
'705 33 520'); U with two or three short strokes inside 702 / 703 (P311, P312). Distinct lines; A and B separately.

- **UI1** The plain U 700 is directly preceded by a numeral more often than the stroked U 705 / 706 (A; Fisher).
- **UI2** UI1 holds on B.
- **UI3** 705 / 706 are directly followed by the long 3 (33) more often than 700 is (A + B).
- **UI4** 700 ends the line (or stands before 400 / 90) more often than 705 / 706 (A).
- **UI5** UI4 holds on B.
- **UI6** The short-stroked U 702 / 703 are preceded by a numeral less often than 700 (A + B; 17 tokens, weak).
- **UI7** Progress rule: UI1 with UI2, or UI4 with UI5 (the inner-stroke device generalises from the jar to the U).

## Results of the hundred-and-eighty-ninth set (added after the test; `predict_test189.py`, `results/predict_test189.md`)

Seven held, none failed. **The inner-stroke device generalises from the jar to the U.** The plain U 700 is a counted
unit that ends the text: preceded by a numeral in 45% against 13% for the U with a long stroke inside (705 / 706)
(UI1; B 30% against 10%, UI2) and final in 45% against 3% (UI4; B 43% against 8%, UI5). The stroked U opens the closing
formula: followed by the long 3 in 49% against 0% for the plain U (UI3). The U with two or three short strokes inside
(702 / 703) is almost never counted (UI6: 1 of 18 against 37%). Reading, with loop 11: strokes drawn inside a container
sign (jar, U) turn it into a different word or form, a productive graphic device of the script: the plain container
counts or ends, the stroked container is a name element or the head of the closing formula. This is structural
knowledge any reading must reproduce (a reading of 700 as a measure or container must give 705 / 706 a related word
that heads the closing formula). Progress (new, replicated on B): streak 0. Tally, counting parts: 1273 held, 1192
failed (2465 registered).

# Hundred-and-ninetieth set, registered before testing (24 September 2026): decipherment loop 15, the leaf family (six hypotheses)

Metric after loop 14: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4; streak 0. Loops 9-14 found marks and inner
strokes that change a sign's job. The leaf shape in Parpola's list carries several attachments: a small diamond on top
(817, 824, 856, 861: the heading signs), a tree at the bottom (803, 838), a stroke inside (808, 809, 830, 832), a hatched
square inside (810, 812, 814), a diagonal stroke inside (831). Positions: initial, medial, final (last sign or before
400 / 90) and name head (directly before 740 / 520). Distinct lines; A and B separately.

- **LF1** In A, the attachment predicts the position class (initial / medial / head / final) beyond permutation (MI).
- **LF2** LF1 holds on B.
- **LF3** Leaf + stroke inside is a name head more often than leaf + tree (A + B; Fisher).
- **LF4** Leaf + tree stands medially (not initial, not head, not final) more often than leaf + stroke inside (A + B).
- **LF5** Leaf + diamond (the heading) is line-initial in 60%+ (A + B; a replication check of the known heading).
- **LF6** Progress rule: LF1 and LF2 both hold, or LF3 holds with the same direction in A and in B separately.

## Results of the hundred-and-ninetieth set (added after the test; `predict_test190.py`, `results/predict_test190.md`)

Four held, two failed. The leaf's attachment predicts the position class in A (LF1: MI 0.22, p = 0.0001) and B (LF2:
0.20, p = 0.0001), and the diamond-topped leaves (the heading) open the line in 75% (LF5). The stroke-inside leaf is not
more often a head than the tree leaf (LF3: 13% against 15%), nor the tree leaf more medial (LF4: 49% against 38%, p =
0.10). **Check after the test**: with the diamond leaves (the already-known heading) left out, the attachment still
predicts position in A (MI 0.14, p = 0.0006, 161 tokens) but not in B (MI 0.15, p = 0.10, 77 tokens). LF6 holds by its
registered rule, but on the independent sample the signal is carried by the known heading, so this loop is counted
conservatively as no progress: streak 1. Tally, counting parts: 1277 held, 1194 failed (2471 registered).

# Hundred-and-ninety-first set, registered before testing (24 September 2026): decipherment loop 16, a parser for the whole grammar (six hypotheses)

Metric after loop 15: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), P 0, L 4; streak 1. A new component, G = share of distinct
lines fully parsed by one explicit grammar built from the registered findings: LINE = [HEADING] NAME [POST] | COUNT |
CLOSER-LINE | FORMULA | BARE | NUMBERS. HEADING = 817 / 820 / 861 + 2 / 60 / 1 (set 45 and after); NAME = BODY
ENDING, BODY = one or more lexical signs or numerals, ENDING = 740 | 520 | a closer | a caged sign (set 184) | 740 + a
stacking closer; POST = any of 400, 90 after the ending; COUNT = a numeral run + at most two signs (count tokens, set
38 and after); CLOSER-LINE = lexical signs + a closer; FORMULA = 705 / 706 + 33 + 520 (set 35); BARE = 2+ lexical
signs whose last sign is attested as a name head (set 177); NUMBERS = numerals only. Set 35 parsed 53% of lines with
fewer rules. Grammar fixed on A's knowledge; B is the check.

- **GR1** G on A's distinct lines is 70% or more.
- **GR2** G on B's distinct lines is within 10 points of G on A (the grammar is not fitted to A).
- **GR3** G on F's extra lines (not in A or B) is 60% or more.
- **GR4** Each rule is needed: dropping any single rule costs 1+ point of G on A (the rules with that effect listed).
- **GR5** Unparsed lines are longer than parsed lines (rank test): what remains is the long texts.
- **GR6** Progress rule: GR1 and GR2 hold (G enters the metric).

## Results of the hundred-and-ninety-first set (added after the test; `predict_test191.py`, `results/predict_test191.md`, `grammar.py`)

Four held, two failed. One explicit grammar (heading, name body + ending/closer/caged sign/stacked closer, post-ending
marker, count, closing formula, bare name, numerals) parses 80.5% of the distinct A lines (GR1) and 71.6% of B with heads
learned from A only (GR2). It covers only 56.0% of the 389 extra F lines (GR3 fails). Not every rule pays its way
(GR4 fails): dropping the heading or the formula costs nothing measurable, while the bare-name (15.7 points), post-ending
(10.0) and closer (7.2) rules carry most of the coverage. The unparsed lines are the longer ones (GR5: 4.86 against 4.55
signs, p = 0.04): names followed by counts ('X 740 900 1 3 423'), '740 1 ...' sequences and 'X 400' pairs. GR6 holds;
G enters the metric at 80.2% (A lines as progress.py counts them) and 72.3% (B). Progress: streak 0. Tally, counting
parts: 1281 held, 1196 failed (2477 registered).

# Hundred-and-ninety-second set, registered before testing (24 September 2026): decipherment loop 17, rules for what the grammar leaves (seven hypotheses)

Metric after loop 16: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), G 80.2% (B 72.3%), P 0, L 4; streak 0. Five new rules for
`grammar.py`, written from the unparsed A lines only (B stays the check): SHORT = a heading (817 / 820 / 861 + 2 / 60 /
1) alone or with one lexical sign; ONE = a single lexical sign + a post-ending marker (400, 90); U = a body ending in a
numeral + 700 (set 189: plain 700 is the counted, final U); OPEN = 705 / 706 + a body without the rest of the formula
(set 189: 705 / 706 heads the closing formula); SEQ = a line that splits into two consecutive units that each parse
(name, count, bare name, formula, short heading), the first of two or more signs. A grammar can reach any coverage by
accepting everything, so each line is also scored after shuffling its signs (20 shuffles, fixed seed): the grammar
should parse real lines far more often than shuffled ones.

- **SQ1** The extended grammar raises G on A by 5 points or more.
- **SQ2** It raises G on B by 3 points or more.
- **SQ3** The margin (G on real lines minus G on shuffled lines) rises on B: the gain is structure, not permissiveness.
- **SQ4** Each new rule, added alone, raises coverage of real B lines more than of shuffled B lines (all five).
- **SQ5** G on F's extra lines rises by 5 points or more (GR3 was 56.0%).
- **SQ6** In SEQ lines, the first unit ends with 740 / 520 / a closer / a caged sign more often than the same position
  in shuffled lines that SEQ parses (the split falls after an ending).
- **SQ7** Progress rule: SQ2 and SQ3 hold (G rises on the independent sample without losing specificity).

## Results of the hundred-and-ninety-second set (added after the test; `predict_test192.py`, `results/predict_test192.md`, `grammar.py` EXT_RULES)

Three held, four failed. (A bug that stopped the ONE rule from firing, the post-ending marker being stripped first, was
fixed before the result was recorded; it changes no verdict.) The extension raises G on A from 80.2% to 88.5% (SQ1), on B
from 72.3% to 80.9% (SQ2) and on F's extra lines from 57.1% to 66.3% (SQ5), but it parses shuffled B lines even more
readily (41.6% to 55.5%), so the margin over shuffled lines falls from 30.7 to 25.5 points (SQ3 fails). SEQ is the
permissive rule (real +5.5, shuffled +11.8; SQ4 fails), and its split does not fall after an ending more often than in
shuffled lines (SQ6 fails, 66% against 75%). SHORT, ONE and U are specific (real +1.4/+0.6/+0.4 against shuffled
+0.3/+0.3/+0.1); OPEN is not. The progress rule fails: no progress, streak 1. **Check after the test**: the base
grammar's bare-name rule is barely specific either (dropping it costs 26.8 points on real B lines and 25.3 on shuffled
ones): a line of lexical signs ending in one of 177 attested heads is accepted almost regardless of order. G as defined
overstates what the grammar captures; its real content is the margin (A 43.3, B 30.7 points). Tally, counting parts:
1284 held, 1200 failed (2484 registered).

# Hundred-and-ninety-third set, registered before testing (24 September 2026): decipherment loop 18, a specific grammar (six hypotheses)

Metric after loop 17: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), G 80.2% (B 72.3%), P 0, L 4; streak 1. Set 192 showed G
rewards permissive rules; the metric's grammar component becomes **G margin** = share of real lines parsed minus share
of the same lines parsed after shuffling their signs (20 shuffles, seed 192). Base margins: A 43.3, B 30.7 points.
Grammar G2, designed on A only: the base rules plus SHORT, ONE and U from set 192 (specific there), no SEQ, no OPEN,
and BARE limited to heads seen 5+ times as a name head in A and more often as a head than as a modifier. On A its
margin is 46.2 (designed there, so not a test).

- **SP1** G2's margin on B exceeds the base grammar's by 1.5 points or more.
- **SP2** G2's margin on F's extra lines exceeds the base grammar's.
- **SP3** G2 parses fewer shuffled B lines than the base grammar (it is stricter where it matters).
- **SP4** Lines that G2 drops from BARE (parsed by the base, not by G2) are more often unique to one object than lines
  G2 keeps as BARE (one-object share, A + B; the dropped lines are the idiosyncratic ones).
- **SP5** The share of B lines parsed by G2 stays 60% or more (the grammar still covers most of the corpus).
- **SP6** Progress rule: SP1 and SP2 hold (G margin enters the metric and rises on both independent samples).

## Results of the hundred-and-ninety-third set (added after the test; `predict_test193.py`, `results/predict_test193.md`, `grammar.py` parse2)

Four held, two failed. The stricter grammar G2 (base rules + SHORT, ONE, U; BARE only for heads seen 5+ times and
more often as heads than as modifiers) raises the margin over shuffled lines on B from 30.7 to 34.7 points (SP1) and
on F's extra lines from 17.0 to 17.3 (SP2, a small rise), and halves the shuffled B lines it accepts (41.6% to 21.4%;
SP3). The bare lines it drops are not more often single-object lines than those it keeps (SP4 fails: 85% against 91%),
and it covers only 56.2% of B (SP5 fails: the strictness costs a third of the bare lines). The progress rule holds
(SP6): the G margin enters the metric at A 46.2, B 34.7 points. Progress: streak 0. The low F margin (17 points) says
the extra F lines (mostly short, damaged or tablet lines) carry little order the grammar knows. Tally, counting parts:
1288 held, 1202 failed (2490 registered).

# Hundred-and-ninety-fourth set, registered before testing (24 September 2026): decipherment loop 19, graphic families as context (six hypotheses)

Metric after loop 18: S 4.712, R 81.3%, M 16.6% (M+ 41.4%), G margin A 46.2 / B 34.7, P 0, L 4; streak 0. Loops 9-14
found graphic devices (cage, inner strokes, fish marks) that change a sign's job while it keeps its base shape. If
marked variants share contexts, the S model should gain from seeing the previous two signs by their graphic family.
Family = ICIT decade block (g // 10: 740-745 jars, 700-706 U's, the fish in 220-240). New component `ftri`: a trigram
over the families of the two previous signs, predicting the sign (`famlm.py`), mixed with the set-125 model (tri, pos,
end; weights fitted on the training lines' own dev split). A design run on the training lines only gave 4.740 -> 4.731.

- **FB1** S on the fixed test lines improves by 0.005 bits or more.
- **FB2** Replication on B: trained on A's distinct lines, tested on the B lines not in A, the family model also gains.
- **FB3** Random families (the signs regrouped at random into groups of the same sizes, 20 draws, seed 194) gain less
  than the decade families in at least 19 of 20 draws (fixed test).
- **FB4** Decade families gain more than the coarser hundred blocks (g // 100) as families.
- **FB5** The weight fitted to `ftri` is nonzero on both the fixed split and the A->B run.
- **FB6** Progress rule: FB1 and FB2 hold (S improves and the gain replicates on B).

## Results of the hundred-and-ninety-fourth set (added after the test; `predict_test194.py`, `results/predict_test194.md`, `famlm.py`)

All six held. Seeing the two previous signs by their graphic family (ICIT decade block) improves S for the first time
since the metric began: 4.7124 -> 4.6973 bits/sign on the fixed test (FB1, gain 0.015). Trained on A and tested on the
new B lines the gain is larger, 5.259 -> 5.237 (FB2). Random families of the same sizes gain nothing (-0.002 to +0.0004;
the decade families beat all 20 draws, FB3), nor do the coarse hundred blocks (-0.001, FB4); the family component gets
weight 0.08 in both runs (FB5). So graphic variants share contexts: the variant marks (cage, strokes, fish marks) sit on
a base sign whose grammatical environment carries over, which fits the morphographic reading of loops 9-14. S enters the
metric at 4.697. Progress: streak 0. Tally, counting parts: 1294 held, 1202 failed (2496 registered).

# Hundred-and-ninety-fifth set, registered before testing (24 September 2026): decipherment loop 20, the L bench against the world's languages (six hypotheses)

Metric after loop 19: S 4.697, R 81.3%, M 16.6% (M+ 41.4%), G margin A 46.2 / B 34.7, P 0, L 4; streak 0. The owner
asked for an L bench that narrows the language explicitly, with typology-matched decoys (Turkish, Japanese, Basque,
Burushaski ...) rather than only Sanskrit and shuffled keys. L as a count of open families cannot move without a whole
family falling, so a graded component is added: **L world** = share of the world's language groups whose typology is
incompatible with the Indus profile. The profile uses only structure established here without sound values:
suffixing (the ending follows the name; WALS 26A = 2 or 3), possessor/modifier before head (head-final names; 86A = 1,
87A = 1), numeral before the counted sign (89A = 1), case suffixes (post-ending markers after the ending; 51A = 1 or
6), and, as a separate weaker variant, a two-way class ending (740 / 520; 30A = 2+). A language is assessed when 3+
profile features are coded; a genus is compatible if any assessed member is. Data: WALS (CLDF, CC-BY 4.0;
`data/wals_profile.tsv`) and, as the independent replication, Grambank (CLDF, CC-BY 4.0): GB024 = 1/3 (Num-N), GB065 =
1/3 (possessor first), GB193 = 1/3 (property word first), class variant = any of GB051/052/053/054/192 present,
assessed with 2+ coded, grouped by Glottolog family. Disclosed before testing: a design run on WALS gave 80.9% of 444
genera excluded (core) and 82.0% (with class); some Grambank codes of the South Asian candidates were looked at
(Tamil/Telugu GB053 = 0; Hindi GB321 = 0, Marathi 1): database codes do not split Dravidian from Indo-Aryan on class
assignment, so no hypothesis below relies on that.

- **LW1** Grambank replication: the core profile excludes 50% or more of the Glottolog families assessed.
- **LW2** Every assessed Dravidian and Indo-Aryan language is compatible with the core profile in both databases.
- **LW3** The core profile does not separate the two candidates: Dravidian and Indo-Aryan compatibility rates are
  equal in both databases (this test cannot choose between them).
- **LW4** With the class variant, Turkish, Japanese and Basque are excluded in Grambank, while every assessed Dravidian
  and Indo-Aryan language is kept.
- **LW5** Families compatible with core + class in Grambank are 10% or fewer of the families assessed.
- **LW6** Progress rule: LW1 and LW2 hold (L world enters the metric, replicated in an independent database).

## Results of the hundred-and-ninety-fifth set (added after the test; `predict_test195.py`, `results/predict_test195.md`, `lbench.py`)

One held, five failed. The narrowing replicates in the independent database: the core profile (suffixing, modifier
and possessor before the head, numeral before the counted sign, case suffixes) excludes 80.9% of 444 WALS genera and
56.0% of 300 Grambank (Glottolog) families (LW1). But the profile as coded is too strict to keep every candidate
language (LW2 fails): Assamese, Oriya and Sinhala are coded 'no dominant order' of numeral and noun (89A = 3), Urdu
'no case affixes' (51A = 9, its case markers counted as words), and Toda has the numeral after the noun (GB024 = 2).
The candidates' rates therefore differ slightly (LW3 fails: WALS Dravidian 1.00, Indic 0.81; Grambank 0.97 against
1.00), from coding and outliers, not from a family-level difference. The class variant removes Turkish, Japanese and
Basque but also genderless members of both candidate families (LW4 fails): Brahui, Toda, Kodava and others on the
Dravidian side, the eastern Indo-Aryan languages (Magahi, Maithili, Odia) on the other. Core + class leaves 72 of 289
families (24.9%; LW5 fails). The progress rule fails: streak 1. Reading: the world typology narrows the field to about
a fifth of the genera, and within that fifth the Indus profile does not separate Dravidian from Indo-Aryan, as
expected. Tally, counting parts: 1295 held, 1207 failed (2502 registered).

# Hundred-and-ninety-sixth set, registered before testing (24 September 2026): decipherment loop 21, the L bench repaired and the class signal by place and time (seven hypotheses)

Metric after loop 20: S 4.697, R 81.3%, M 16.6% (M+ 41.4%), G margin A 46.2 / B 34.7, P 0, L 4; streak 1. Set 195's
profile was coded too strictly (a language with 'no dominant order' was counted against the profile, although the
Indus order does not contradict it) and required every language to fit, where one outlier (Toda) is enough to fail.
Fixed here before looking: **tolerant profile** = 86A, 87A, 89A value 3 also compatible, 51A dropped (whether 400 / 90
are case suffixes or words is not settled); Grambank GB024/065/193 as before; compatibility judged per genus (WALS)
and per family (Grambank): a group is compatible if most of its assessed languages are. Set 178 found that names
with human, tool and plant heads take 740 and fish-headed names lean to 520 (DC3). The owner asked whether such
signals hold across places and periods (a multilingual or layered society would show breaks). Places: Mohenjo-daro,
Harappa, all other sites. Periods at Harappa (ICIT field 8): early = Period 1-3B (without the ambiguous 3B/C), late =
Period 3C and after.

- **LT1** Tolerant WALS profile: the Dravidian and Indic genera are both compatible.
- **LT2** Tolerant Grambank profile: Dravidian and Indo-European (its Indo-Aryan members judged as one group) both
  compatible, and 50% or more of the families assessed are excluded.
- **LT3** Tolerant WALS profile excludes 70% or more of the genera assessed.
- **LT4** Fish-headed names take 520 more often than other identified-head names at Mohenjo-daro.
- **LT5** The same at Harappa.
- **LT6** The same at the other sites taken together.
- **LT7** The same in both early and late Harappa (the direction holds in both; one-sided p < 0.05 in at least one).
- **LT8** Progress rule: LT1, LT2 and LT3 hold (L world enters the metric), or LT4-LT7 all hold (a new finding that
  replicates across independent subsets).

## Results of the hundred-and-ninety-sixth set (added after the test; `predict_test196.py`, `results/predict_test196.md`, `lbench.py`)

All eight held (the heading says seven; there are eight). With the tolerant profile fixed before looking (86A/87A/89A
'no dominant order' compatible, 51A dropped, majority rule per group), the Dravidian and Indic genera are compatible in
WALS (LT1), Dravidian and Indo-European (all 16 Indo-Aryan languages) in Grambank, where 68.3% of families are excluded
(LT2), and 81.3% of 422 WALS genera are excluded (LT3). Among the compatible genera are Turkic, Mongolic, Tungusic,
Japanese, Korean, Burushaski, Munda, Kartvelian, Uralic branches and Quechuan: the typology narrows the field to a
fifth of the world but cannot choose inside it. The fish-name / 520 signal holds separately at Mohenjo-daro (52%
against 2%), Harappa (48% against 2%) and the other sites together (36% against 7%; LT4-LT6), and in both early and
late Harappa in direction (LT7; early has only 9 identified-head names, late p < 0.0001). No break by place or time:
one grammatical system across the Indus world, as far as this signal can show. Note for L: human-, tool- and
plant-headed names all take 740 and only fish heads lean to 520 (set 178), so the class split is 'fish/star names
against the rest'. That fits a Dravidian rational/non-rational reading (a tool-headed name such as 'bowman' names a
person) and equally a Sanskrit-type gender reading (star names are mostly feminine there); it does not separate the
two. Progress: streak 0; L world enters the metric at 81.3% (WALS) / 68.3% (Grambank). Tally, counting parts: 1303
held, 1207 failed (2510 registered).

# Hundred-and-ninety-seventh set, registered before testing (24 September 2026): decipherment loop 22, name structure against typology-matched decoys (five hypotheses)

Metric after loop 21: S 4.697, R 81.3%, M 16.6% (M+ 41.4%), G margin A 46.2 / B 34.7, P 0, L 4, L world 81.3% (WALS) /
68.3% (Grambank); streak 0. The typology leaves about a fifth of the world's genera, including Turkic and Japanese.
Sets 171-175 compared Indus name structure only with the candidates (Prakrit, Tamil) and excluded languages
(Sumerian, Linear B Greek). Here two decoys from inside the compatible fifth join: Japanese given names (JMnedict,
masc/fem entries, morae; 20,081) and Turkish given names (2009 counts, 100+ bearers, syllables; 12,764; many are
Arabic/Persian loans, a known weakness). Measures as set 175, all rarefied to the same sample size: R (distinct last
elements / distinct first elements), length distribution (JSD), share of the ten commonest final pairs against the
Indus ten commonest heads, and dominant final element share against 740's share. Distances: |log ratio| for R, JSD,
absolute differences for the shares; languages ranked per measure; overall = mean rank. Languages: Tamil-Brahmi,
Prakrit, Japanese, Turkish, and the controls Ur III Sumerian owners and Linear B persons.

- **DN1** The language nearest the Indus names overall is a candidate (Tamil-Brahmi or Prakrit).
- **DN2** Both candidates rank nearer than both decoys (Japanese, Turkish).
- **DN3** Both controls (Sumerian, Linear B) rank below both candidates.
- **DN4** The nearest language is the same when the Indus names are split at random into two halves (seed 197).
- **DN5** Progress rule: DN1 and DN4 hold (a nearest language that replicates across halves).

## Results of the hundred-and-ninety-seventh set (added after the test; `predict_test197.py`, `results/predict_test197.md`)

All five held. Rarefied to 104 names each, the Indus name structure (R 0.83, head share 0.43, dominant ending 0.82) is
nearest the Prakrit donor names (mean rank 1.00: R 0.90, head share 0.35), then Tamil-Brahmi (2.75), then the decoy
Japanese (3.25), Linear B (3.75), Ur III Sumerian (4.50) and Turkish (5.75) (DN1-DN3). The order of the first two is
the same in two random halves of the Indus names (DN4). **Caveats.** (1) Genre: the two candidates are inscriptional
donor names, the decoys dictionary lists of modern given names, so part of the gap may be genre; against that, the Ur
III seal-owner names, the closest genre match (seal legends), rank fifth. (2) No language matches the dominant ending:
740 ends 82% of Indus names, no language's commonest final element exceeds 23%, so 740 is a separate morpheme, not a
name-final syllable, and that measure mostly ranks noise. (3) As in set 175, the name structure leans Indo-Aryan in R
and head share while the candidates stay close together; this does not choose between them. What it adds for L: the
typology-matched decoys inside the compatible fifth (Japanese, Turkish) fit the Indus names worse than both South Asian
candidates. Progress by the registered rule: streak 0. Tally, counting parts: 1308 held, 1207 failed (2515 registered).

**Qualified by set 198**: with genre held to name lists on both sides, the decoy Japanese ranks nearest; the
candidate advantage above was genre.

# Hundred-and-ninety-eighth set, registered before testing (24 September 2026): decipherment loop 23, the genre control for set 197 (five hypotheses)

Metric after loop 22: S 4.697, R 81.3%, M 16.6% (M+ 41.4%), G margin A 46.2 / B 34.7, P 0, L 4, L world 81.3% / 68.3%;
streak 0. Set 197 put the candidates' inscriptional donor names nearest the Indus names and the decoys' modern
given-name lists further off, which genre alone could do. Here genre is held to name lists on both sides: candidates
= Sanskrit names from Monier-Williams ('N. of a man / woman', syllables, as set 171) and Old Tamil names from the
Sangam poets list (grapheme clusters, as set 171); decoys = Japanese and Turkish given names as set 197. Same four
measures, rarefaction, distances and mean-rank rule as set 197.

- **GC1** With genre held to lists, at least one candidate list ranks nearer the Indus names than both decoys.
- **GC2** Both candidate lists rank nearer than both decoys.
- **GC3** Sanskrit (dictionary) names rank nearer than Japanese (dictionary) names.
- **GC4** The nearest of the four is the same in both random halves of the Indus names (seed 198).
- **GC5** Progress rule: GC1 and GC4 hold (the candidate advantage survives the genre control and replicates).

## Results of the hundred-and-ninety-eighth set (added after the test; `predict_test198.py`, `results/predict_test198.md`)

One held, four failed. (The first run stopped on a sampling error, the rarefaction size exceeding one half of the Indus
names; the size was capped at the smaller half, the same size for every comparison as registered, and rerun: 309.) With
genre held to name lists on both sides, the order is Japanese (mean rank 1.50), Sanskrit from Monier-Williams (2.00),
the Sangam poets' names (3.00), Turkish (3.50) (GC1-GC3 fail), the same in both halves (GC4). **This overturns the
language reading of set 197**: the candidates' advantage there came from genre (inscriptional donor names against
dictionary lists), not language. Name-structure statistics of this kind do not discriminate between languages inside
the compatible fifth; the typology-matched decoy Japanese fits as well as or better than the candidates. The progress
rule fails: streak 1. Set 197 stays recorded as held by its rule, qualified by this control. Tally, counting parts:
1309 held, 1211 failed (2520 registered).

# Hundred-and-ninety-ninth set, registered before testing (24 September 2026): decipherment loop 24, a longer family context for S (five hypotheses)

Metric after loop 23: S 4.697 (model tri + pos + end + ftri), R 81.3%, M 16.6% (M+ 41.4%), G margin A 46.2 / B 34.7,
P 0, L 4, L world 81.3% / 68.3%; streak 1 (stopping rule now 10 consecutive loops without progress). Set 194's family
trigram helped; a design run on the training lines' own split shows a family 4-gram (the families of the previous
three signs, interpolated with the family trigram) doing better (4.732 -> 4.724), and a family-by-distance-from-end
component adding nothing. New component `f4` in famlm.py; model tri + pos + end + f4.

- **F41** S on the fixed test improves over 4.697 by 0.003 bits or more.
- **F42** Replication A -> B (trained on A, tested on B's new lines): tri+pos+end+f4 beats tri+pos+end+ftri.
- **F43** Random families (20 draws of the same sizes, seed 199) used in f4 gain less than the decade families in 19+.
- **F44** f4 gets a nonzero weight on both runs.
- **F45** Progress rule: F41 and F42 hold.

## Results of the hundred-and-ninety-ninth set (added after the test; `predict_test199.py`, `results/predict_test199.md`, `famlm.py` f4)

All five held. The family 4-gram context lowers S on the fixed test from 4.6973 to 4.6842 (F41, gain 0.013), and the
gain replicates trained on A and tested on B's new lines (5.2349 -> 5.2249; F42). Over the set-125 model the decade
families now gain 0.030 bits, random families of the same sizes at most 0.002 (20 of 20; F43); f4 gets weight 0.09 and
0.08 (F44). (The A->B figure for the ftri model, 5.2349, differs from set 194's 5.2372 because famlm.py now also counts
the 4-gram table while fitting; the comparison here is within one run.) S enters the metric at 4.684. Progress: streak
0. Tally, counting parts: 1314 held, 1211 failed (2525 registered).

# Two-hundredth set, registered before testing (24 September 2026): decipherment loop 25, picture anchors frozen and tested on unseen tablets (six hypotheses)

Metric after loop 24: S 4.685, SIGN top-1 36.2%, WORD top-10 3.0%; prize tiers V (checked meaning) 0.008%, C gate 1 of
3 methods, U (vault) 0; streak 0. The only language-free bilingual evidence is text + picture on the same tablet (NOTES
second and third passes: copper-tablet texts go with their images; seal texts do not). Tier 1 asks for meanings
checked against outside evidence, tier 3 for values frozen before being tried on unseen texts. Here: all tablets
(ICIT TAB:C copper, TAB:B moulded, TAB:I incised) with a specific motif (ICIT field 18; 'Othr', 'Unknown', 'None'
left out; motif classes = the code before ':'). Objects are grouped by their full text, and whole text groups are
split at random into a design half and a vault half (seed 200), so no mould copy crosses the split. On the design
half a sign becomes a **picture anchor** if it occurs on 3+ objects in 2+ distinct texts and 80%+ of those objects
carry one motif. On the vault half each object carrying an anchor gets the anchors' majority motif as its predicted
picture. Null: motifs shuffled among the design text groups, anchors rebuilt, 1,000 times.

- **PB1** Vault accuracy exceeds the permutation null (p < 0.01).
- **PB2** 20% or more of vault objects carry at least one anchor.
- **PB3** On copper tablets alone (anchors from design copper tablets, tested on vault copper tablets), accuracy also
  beats its null (p < 0.05).
- **PB4** On seals (SEAL:S) the same procedure does not beat its null (replicating the second pass: seal texts do not
  name the animal).
- **PB5** Accuracy on vault objects is 50% or more.
- **PB6** Progress rule: PB1 holds. Then the anchor signs whose vault predictions are right more often than not enter
  V (checked meaning), and U counts the vault tokens they read.

## Results of the two-hundredth set (added after the test; `predict_test200.py`, `results/predict_test200.md`)

One held, five failed. 474 pictured tablets (218 distinct texts; bas-relief bull, multi-headed animal, gharial, tree,
fish ...). Anchors fixed on half of the text groups (8 signs: 142, 240, 405, 520 = one-horned bull; 167, 741 =
multi-headed animal; 440 = gharial; 463 = tree) predict the picture of 1 of 38 unseen tablets (2.6%; permutation p =
0.40; PB1, PB5 fail); only 17% of unseen tablets carry an anchor (PB2 fails); copper tablets alone have too few
distinct texts to test (PB3 fails). Seal texts again predict nothing beyond their null (PB4 holds). **Reading:** the
text-picture pairing on tablets is a property of whole texts repeated with their scene (mould copies of one text with
one picture), not of signs: no sign carries its picture into a new text. For tier 1 this means the tablets fix
meanings only at the level of a whole text, and the four copper-tablet anchor signs rest on the drawing of the sign,
not on a pairing that generalises. No progress: streak 1. Prize tiers unchanged (V 0.008%, C 1 of 3, U 0). Tally,
counting parts: 1315 held, 1216 failed (2531 registered).

# Two-hundred-and-first set, registered before testing (24 September 2026): decipherment loop 26, phrase-level picture anchors; graphic against learned families (seven hypotheses)

Metric after loop 25: S 4.685; prize tiers V 0.008%, C 1 of 3, U 0; streak 1. Set 200: single signs do not carry a
tablet's picture into a new text. Two independent questions, tested together.

(A) Phrases. Same tablets, motifs and text-group split as set 200. An unseen tablet is matched to the design text
groups with which it shares the most adjacent sign pairs (at least one); its predicted picture is the majority motif
of those groups. Null: motifs shuffled among design text groups, 1,000 times.

- **PH1** Vault accuracy beats the null (p < 0.05), split seed 200.
- **PH2** The same with a second split (seed 201).
- **PH3** 30% or more of unseen tablets share a pair with some design text.

(B) Graphic families. Set 194/199's family context helps S and random families do not. Is the gain graphic, or would
any sensible sign classes do? Classes learned from contexts (k-means on left/right neighbour distributions of the
training lines, k = 40, 80, 150, seed 0) replace the decade families in f4. A design run on the training lines' own
split gave 4.725 for decade families against 4.736-4.747 for learned classes.

- **GF1** On the fixed test, decade families give lower S than each of the three learned class sets.
- **GF2** Trained on A and tested on B's new lines, decade families beat each learned set too.
- **GF3** Families that are decade-block and learned-class pairs do no better than decade families alone (fixed test).
- **GF4** Progress rule for the loop: PH1 and PH2 hold, or GF1 and GF2 hold.

## Results of the two-hundred-and-first set (added after the test; `predict_test201.py`, `results/predict_test201.md`, `famlm.learned_classes`)

All seven held. **(A) Phrases carry pictures where single signs do not.** An unseen tablet matched to the design texts
with which it shares the most adjacent sign pairs gets its picture right in 26 of 106 cases (24.5%; permutation p =
0.001; PH1), and 21 of 113 on a second split (18.6%; p = 0.03; PH2); 49% of unseen tablets share a pair (PH3).
Post hoc, the right predictions come mostly from 706 33 923 740 -> elephant (8 of 8 across both splits; partly
near-duplicate texts that differ by a final stroke), 806 158 -> tree (6 of 6; 806 is the leaf-in-oval sign), 233 520
-> gaur (3 of 3), 752 740 and 861 2 -> tree, 840 32 / 32 740 -> scene; 740 400 is ambiguous (gharial 7 of 19, bull 5
of 8). **(B) The S gain is graphic.** Decade families give 4.6849 on the fixed test against 4.712-4.718 for classes
learned from contexts (GF1), 5.223 against 5.263-5.271 A -> B (GF2), and pairing them with learned classes makes S
worse (4.705; GF3). Progress (GF4): streak 0. Prize tiers: V strict unchanged (0.008%); tier 3 gains a
picture-vault line: phrase-level picture prediction on unseen tablets 24.5% / 18.6% (nulls p = 0.001 / 0.03).
Tally, counting parts: 1322 held, 1216 failed (2538 registered).

# Two-hundred-and-second set, registered before testing (24 September 2026): decipherment loop 27, sharper phrase matching and phrases on seals (six hypotheses)

Metric after loop 26: S 4.685; prize tiers V 0.008%, C 1 of 3, U 0 (picture vault 24.5% / 18.6%); streak 0. Set 201's
matcher counted shared adjacent pairs equally. Here (A) a weighted matcher: shared pairs and shared triples between
an unseen tablet and each design text group, each weighted by log(D / d), D design groups, d groups containing it
(rare phrases count more; triples also count); prediction = the motif of the best-scoring group (ties: majority).
Same objects, motifs and split rule as sets 200-201; nulls as there (1,000 shuffles of motifs among design groups).
(B) Seals (SEAL:S, motif classes as set 200) with set 201's plain pair matcher.

- **WM1** Weighted matching beats set 201's accuracy on split 200 (24.5%) and on split 201 (18.6%).
- **WM2** Weighted matching beats its null on a new split (seed 202, p < 0.05).
- **WM3** Weighted matching beats its null on splits 200 and 201 (p < 0.05 each).
- **WM4** On seals, phrase matching does beat the majority-class rate (unicorn) on unseen seals.
- **WM5** On seals, phrase matching beats its null (p < 0.05, 300 shuffles).
- **WM6** Progress rule: WM1 and WM2 hold (a better picture vault that replicates on a new split).

## Results of the two-hundred-and-second set (added after the test; `predict_test202.py`, `results/predict_test202.md`)

One held, five failed. Weighting shared pairs and triples by rarity does not improve the picture vault (23.6% on split
200, was 24.5%; 19.5% on split 201, was 18.6%; WM1 fails), though both still beat their nulls (WM3). On a new split
(seed 202) it does not: 19 of 184 (10.3%), p = 0.16 (WM2 fails). **This weakens set 201**: the phrase-picture effect
holds on two splits of three and depends on which text groups fall in the vault (chiefly the elephant and tree
phrases). Phrase matching on seals does worse than always guessing the one-horned bull (72.2% against 78.4%; WM4) and
does not beat its null (p = 0.11; WM5). No progress: streak 1. Set 201's picture-vault line in the prize tiers is
marked 'split-dependent' until an estimate over many splits is made. Tally, counting parts: 1323 held, 1221 failed
(2544 registered).

# Two-hundred-and-third set, registered before testing (24 September 2026): decipherment loop 28, the picture vault without split luck (five hypotheses)

Metric after loop 27: S 4.685; prize tiers V 0.008%, C 1 of 3, U 0; streak 1. Set 201's phrase-picture effect held on
two random splits and failed on a third (set 202). Estimated here without split luck. Same tablets and motifs as
sets 200-202; set 201's plain pair matcher. Leave-one-out: each text group is predicted from all the other groups
(its own mould copies left out with it). **Text families**: texts that become identical when numerals are removed
from both ends are one family, and a family is left out whole. Null: motifs shuffled among text groups (families),
500 times, leave-one-out recomputed.

- **LO1** Leave-one-out accuracy over text groups beats its null (p < 0.01).
- **LO2** Leave-one-family-out (near duplicates left out together) beats its null (p < 0.05).
- **LO3** With every text containing 923 (the elephant phrase) removed, leave-one-family-out still beats its null
  (p < 0.05).
- **LO4** Over 50 random half splits by family (seeds 300-349), the matcher's accuracy exceeds its null median in 40
  or more.
- **LO5** Progress rule: LO1 and LO2 hold (a picture vault that does not depend on the split or on mould variants).

## Results of the two-hundred-and-third set (added after the test; `predict_test203.py`, `results/predict_test203.md`)

One held, four failed. Leave-one-out over the 218 text groups predicts 60 of 356 matched tablets' pictures (16.9%; p
= 0.052; LO1 fails); with near duplicates left out together (205 families) 48 of 352 (13.6%; p = 0.14; LO2 fails);
without the elephant phrase 14.1% (p = 0.13; LO3 fails). Over 50 random family splits the matcher beats its null
median in 49 (median accuracy 14.0%, range 5.6-34.8%; LO4 holds). **Reading:** there is a consistent but weak tendency
for shared phrases to go with the same picture; set 201's p = 0.001 was a favourable split. The tablets do not yet
give a picture vault that a panel would accept. No progress: streak 2. Prize tier 3's picture line is corrected to
'weak: leave-one-out 16.9% (p = 0.05), 13.6% with near duplicates together (p = 0.14)'. Tally, counting parts: 1324
held, 1225 failed (2549 registered).

# Two-hundred-and-fourth set, registered before testing (24 September 2026): decipherment loop 29, the Tamil Nadu graffiti as writing; a two-direction SIGN model (eight hypotheses)

Metric after loop 28: S 4.685, SIGN top-1 36.2%; prize tiers V 0.008%, C 1 of 3, U 0; streak 2. (A) The prize was
announced beside the Tamil Nadu Department of Archaeology's claim that ~90% of south Indian graffiti marks have Indus
parallels (Rajan and Sivanantham 2025; 2026 vol. II, a concordance of composite graffiti signs by sherd, elements in
prefix / stem / suffix slots). Without a sign mapping, a language-free fingerprint can still be compared: writing
places co-occurring signs in a consistent order. Data: the vol. II concordance (Table 6.1, extracted by table
reading; scratchpad, not redistributed), deduplicated by (sherd, composite number); an element's order = its slot
(prefix-3 ... suffix-3). Order consistency = for element pairs co-occurring in 3+ composites, the share of their
co-occurrences in the pair's majority order, pooled. Indus: the same measure on distinct lines (A+B), pairs 3+.
(B) Summing a right-to-left model's line log-probability with the left-to-right one in the SIGN task; a design run
gave 37.8% -> 38.6% top-1 on the training lines' own split.

- **TG1** Graffiti order consistency is 80% or more.
- **TG2** Graffiti order consistency is within 10 points of the Indus lines'.
- **TG3** Elements prefer slots: element x first/last position MI beats 1,000 within-composite shuffles (p < 0.01).
- **TG4** TG1 holds separately at the two largest sites (KLD, TKP).
- **TG5** The commonest final element's share in graffiti composites is within 10 points of the commonest final
  sign's share in Indus lines.
- **SB1** Two-direction SIGN top-1 on the fixed test beats the forward model by 0.5 points or more.
- **SB2** The same trained on A and tested on B's new lines (first 300 lines).
- **SB3** Progress rule: TG1 and TG4 hold (a replicated finding about the graffiti), or SB1 and SB2 hold.

## Results of the two-hundred-and-fourth set (added after the test; `predict_test204.py`, `results/predict_test204.md`, `graffiti.py`)

Four held, four failed. **(A) The Tamil Nadu graffiti.** 1,589 composite graffiti signs on 1,453 sherds (vol. II
concordance). Co-occurring elements keep a consistent order in 70.5% of 2,012 co-occurrences (TG1 fails), against
88.0% for Indus lines (TG2 fails), and the same at Keeladi (73.0%) and Thulukarpatti (70.9%) (TG4 fails, but the
figure replicates across sites). Elements do prefer slots (MI 0.24 bits, p = 0.0001; TG3). The commonest final element
(39.0, a stroke) ends 14% of composites against 740's 31.7% of Indus lines (TG5 fails). **Reading:** by a
language-free order fingerprint the graffiti composites are markedly less ordered than Indus texts, at both large
sites; the slot layout is the authors' analysis, so this bears on their composites as recorded, and says nothing
about individual shape parallels. It does not support treating the graffiti as a continuation of Indus writing. **(B)
Two-direction SIGN model.** Summing a right-to-left model's line log-probability lifts SIGN top-1 from 36.2% to 38.2%
on the fixed test (SB1) and from 29.9% to 31.8% A -> B (SB2). Adopted in prizebench; the metric run gives SIGN top-1
37.9%, top-5 60.0%. Progress (SB3): streak 0. Tally, counting parts: 1328 held, 1229 failed (2557 registered).

# Two-hundred-and-fifth set, registered before testing (24 September 2026): decipherment loop 30, a key scorer that passes the Linear B gate; two-direction WORD (six hypotheses)

Metric after loop 29: S 4.685, SIGN top-1 37.9%, WORD top-10 3.0%; prize tiers V 0.008%, C 1 of 3 (the key bench's
dictionary-parse score fails the Linear B gate: `linb_control.md`), U 0; streak 0. (A) A different scorer: decode a
line with the key, join the values without word dividers (as the Indus script has none), and score the string by a
character n-gram language model of the claimed language (per-character log-probability, add-0.5 smoothed, trained on
the language's word list with word boundaries). Linear B data as `linb_control.py` (DAMOS lines of 3+ syllabic signs,
standard values; Greek forms adjusted to Linear B spelling: l > r, final s/n/r dropped). The n-gram order (2-5) is
chosen on the odd-numbered lines; the gate is judged on the even-numbered lines against 100 shuffled keys (values
permuted among signs of similar frequency, bench.shuffles). Specificity: the same scorer with a Sanskrit model
(Monier-Williams headwords, SLP1 lowercased). (B) The WORD task with the two-direction model of set 204.

- **GA1** With the Greek model, Ventris's key beats 95 or more of 100 shuffles on the even lines.
- **GA2** With the Sanskrit model, Ventris's key does not beat 95 of 100 shuffles (the scorer is language-specific).
- **GA3** Ventris's key's margin over the shuffle median is larger with the Greek model than with the Sanskrit one.
- **GA4** Two-direction WORD top-10 on the fixed test beats the forward model by 1 point or more.
- **GA5** The same A -> B (trained on A, B's new lines, first 300).
- **GA6** Progress rule: GA1 and GA2 hold (a key scorer that passes the gate and is language-specific), or GA4 and GA5.

## Results of the two-hundred-and-fifth set (added after the test; `predict_test205.py`, `results/predict_test205.md`, `lmkey.py`)

Four held, two failed. **A key scorer that passes the Linear B gate.** Decoded lines joined without dividers and scored
by a character n-gram model of Greek (Linear B spelling) separate Ventris's values from shuffled keys: on the design
(odd) lines every order from 3 to 5 puts the real key above all 100 shuffles (order 5 chosen); on the held-out even
lines the real key scores -4.247 bits/char against shuffles -4.730 to -4.473 (median -4.565), 0 of 100 as good (GA1).
With a Sanskrit model the real key is not distinguished (9 of 100 shuffles as good; GA2) and its margin is a sixth of
the Greek one (0.054 against 0.318 bits/char; GA3). This is the first key-scoring method in the folder that recovers
a known answer and is language-specific; the dictionary-parse key bench does not (`linb_control.md`). Prize tier 2:
C = 2 of 4 methods passed. The two-direction WORD model gains on the fixed test (top-10 3.0% -> 3.9%) but not A -> B
(2.5% both; GA4, GA5 fail). Progress (GA6): streak 0. Next: the published Indus keys through this scorer. Tally,
counting parts: 1332 held, 1231 failed (2563 registered).

# Two-hundred-and-sixth set, registered before testing (24 September 2026): decipherment loop 31, the published keys through the validated scorer (five hypotheses)

Metric after loop 30: prize tiers V 0.008%, C 2 of 4 (the character-LM key scorer of set 205 passes the Linear B gate
and is language-specific), U 0; streak 0. The published Indus keys (keys/*.tsv on ICIT ids: Fairservis 1992,
Mahadevan 2014, Parpola 1994, Kak 1988; Yajnadevam 2024 xlits.csv) go through that scorer: every distinct line (A +
B) decoded, values joined without dividers, scored per character by an order-5 character model (the order chosen on
Linear B) of each language: Sanskrit (Monier-Williams headwords), Dravidian (DEDR forms, all languages), Sumerian
(ePSD2 citation forms); keys' values and all word lists reduced to plain lowercase a-z (diacritics stripped) so the
three languages are scored alike. Each key against 100 of its own shuffles (values permuted among signs of similar
frequency, bench.shuffles, band 10).

- **KY1** At least one published key beats 95 or more of its 100 shuffles in its claimed language.
- **KY2** Every key that passes KY1 also fails to beat 95 of 100 shuffles in both other languages (it is specific).
- **KY3** For most keys (majority), the margin over the shuffle median is largest in the claimed language.
- **KY4** Positive check that the reduction to a-z does not break the gate: Ventris's Linear B key, Greek model trained
  on the same reduced forms, still beats 95 of 100 shuffles on the even lines.
- **KY5** Progress rule: KY1 and KY2 hold (a published key reads its language as specifically as Ventris's reads
  Greek). If KY1 fails, the folder records that no published key passes a gate-validated test.

## Results of the two-hundred-and-sixth set (added after the test; `predict_test206.py`, `results/predict_test206.md`)

Four held, one failed. Through the gate-validated character-LM scorer (the reduction to plain a-z keeps the Linear B
gate: Ventris's key 0 of 100 shuffles as good; KY4), the substantial published keys do not read their claimed
language better than their own shuffles: Fairservis 1992 (97 signs, Dravidian) 12 of 100 shuffles as good;
Yajnadevam 2024 (681 signs, Sanskrit) 7 of 100; Parpola 1994 (30 signs, Dravidian) and Mahadevan 2014 (5 signs,
Dravidian) score worse than most of their shuffles (99 of 100). Only Kak 1988 (7 signs, Sanskrit) beats 100 of 100
(KY1) and not in Dravidian or Sumerian (KY2); the claimed language gives the largest margin for 2 of 5 keys (KY3
fails). **Check after the test**: with 1,000 shuffles Kak's key gives p = 0.03 in Sanskrit and 0.13 in Sumerian, and
with its one value 740 = sa removed it gives nothing (254 of 1,000 shuffles as good): the pass rests entirely on
putting 'sa' on the line-final ending sign, which any suffixing language with a common -sa ending rewards. Counted
conservatively as no progress: streak 1. For the prize tiers: no published key passes a gate-validated test on the
strength of its readings. Tally, counting parts: 1336 held, 1232 failed (2568 registered).

# Two-hundred-and-seventh set, registered before testing (24 September 2026): decipherment loop 32, blind key fitting on Linear B as a language-identification gate (six hypotheses)

Metric after loop 31: prize tiers V 0.008%, C 2 of 4, U 0; streak 1. No published key reads its language through the
validated scorer (set 206). The defensible comparison (owner's note) gives every candidate language the same freedom:
fit sign values to each language and see which fits unseen text best. It must first work on a known script. Linear B
lines as set 205; for each language (Greek in Linear B spelling, Sanskrit MW, Dravidian DEDR, Sumerian ePSD2; plain
a-z), the value inventory = its 90 commonest consonant(s)+vowel units; every sign gets one value (many signs may share
one); values fitted by annealing (30,000 steps, order-3 character model of the language, `keyfit.py`) on the odd
lines, then the fitted key scored on the even lines by the order-5 model. Control: the same fit and scoring on lines
whose signs are shuffled within each line (seed 0). Gain = held-out score on real lines minus on shuffled lines.

- **KF1** Greek has the largest gain of the four languages (seed 1).
- **KF2** Greek's gain exceeds the next language's by 0.05 bits/char or more.
- **KF3** The fitted Greek key gives Ventris's value (plain a-z) to 20% or more of the 30 commonest signs.
- **KF4** With a second seed (2), Greek again has the largest gain.
- **KF5** Every language's gain is positive (real order carries something any model can use).
- **KF6** Progress rule: KF1 and KF4 hold (blind fitting identifies the known language; a gate for tier 2 and L).

## Results of the two-hundred-and-seventh set (added after the test; `predict_test207.py`, `results/predict_test207.md`, `keyfit.py`)

One held, five failed. Fitted blind, with the same freedom for every language, Linear B fits **Sanskrit** best:
held-out gain over the shuffled-line control Sanskrit 0.361, Dravidian 0.197, Sumerian 0.195, Greek 0.024 bits/char
(seed 1; KF1, KF2 fail); seed 2 Sanskrit 0.328, Dravidian 0.247, Greek 0.216, Sumerian 0.157 (KF4 fails). The fitted
Greek key gives Ventris's value to 0 of the 30 commonest signs (KF3 fails). Every language gains from real order
(KF5). **Reading:** free key fitting rewards the most accommodating language model (a large lexicon of regular
consonant-vowel syllables), not the right language, even on a script whose answer is known. This is the trap in
measured form: a claim that the Indus script 'fits Dravidian' or 'fits Sanskrit' after fitting values freely is not
evidence for either, since the same procedure makes Mycenaean Greek look like Sanskrit. Prize tier 2: blind fitting
recorded as failing the gate (2 of 5 methods pass). No progress: streak 2. Tally, counting parts: 1337 held, 1237
failed (2574 registered).

# Two-hundred-and-eighth set, registered before testing (24 September 2026): decipherment loop 33, graphic families from Parpola's descriptions (five hypotheses)

Metric after loop 32: S 4.685, SIGN top-1 37.9%; prize tiers V 0.008%, C 2 of 5, U 0; streak 2. The only S gains came
from reading context by graphic family (ICIT decade blocks; sets 194, 199, 201), and learned classes do not do it. A
second, independent definition of graphic family: ICIT -> M77 -> the CISI description (mayig digitisation) -> its
first shape noun (`descfam.py`: 73 families, 350 signs, 95% of tokens; e.g. stroke, person, leaf, fish, tree, jar).
Signs without a description keep their own id.

- **DF1** Description families in place of decade families (f4) beat random families of the same sizes (20 draws, seed
  208) in 19 or more, fixed test.
- **DF2** Adding the description-family 4-gram as a second family component to the model with decade f4 lowers S on
  the fixed test by 0.003 bits or more.
- **DF3** The same A -> B.
- **DF4** Description families beat learned classes (k = 80, as set 201) on the fixed test.
- **DF5** Progress rule: DF2 and DF3 hold.

## Results of the two-hundred-and-eighth set (added after the test; `predict_test208.py`, `results/predict_test208.md`, `descfam.py`, `famlm.M4`)

Two held, three failed. Families defined independently, from the first shape noun of Parpola's CISI descriptions
(stroke, person, leaf, fish, tree, jar ...), also improve S over the set-125 model (4.7124 -> 4.6966, gain 0.016),
while random families of the same sizes gain at most 0.0004 (20 of 20; DF1), and they beat classes learned from
contexts (4.6966 against 4.7141; DF4). So the graphic-family effect replicates with a definition not made here. They
carry nothing beyond the decade families: added as a second component, S is unchanged (4.6842 -> 4.6845; DF2 fails)
and A -> B worse (DF3 fails); the decade blocks already capture the variants (ICIT numbers variants next to their
base sign). No progress by the rule: streak 3. Tally, counting parts: 1339 held, 1240 failed (2579 registered).

# Two-hundred-and-ninth set, registered before testing (24 September 2026): decipherment loop 34, roles in closer lines (five hypotheses)

Metric after loop 33: R 81.3% (2,245 tokens without a role: 1,034 in count lines, 790 other, 408 in closer lines);
streak 3. Sets 118-120 found the closers acting as alternative endings. If so, the body before a closer is a name
body like the body before 740 / 520: its last sign a name head, the rest modifiers. Tested before adopting the role.
Closer lines = lines whose genre (predict_test108.genre) is 'closer'; the closer = the line's last closer sign
(predict_test103.CL); the body = the signs before it, numerals excepted. Name heads = signs seen directly before 740
or 520 in A's distinct lines.

- **RL1** In A's closer lines, the sign directly before the closer is a known name head more often than the other
  body signs of those lines (one-sided Fisher p < 0.05).
- **RL2** The same in B's new lines (heads from A).
- **RL3** The sign before a closer is a known name head at least half as often as the sign before 740 / 520 in B.
- **RL4** Body signs before a closer (not the last) are known name modifiers (seen in A name bodies before their head)
  more often than chance draws of signs matched on frequency (B, p < 0.05).
- **RL5** Progress rule: RL1 and RL2 hold; then closer-line bodies get the roles name head / name modifier in R.

## Results of the two-hundred-and-ninth set (added after the test; `predict_test209.py`, `results/predict_test209.md`)

One held, four failed. In closer lines the sign directly before the closer is a known name head no more often than
the other body signs: A 72% against 77% (p = 0.88; RL1), B 64% against 67% (RL2). It is a head less often than the
sign before 740 / 520 (64% against 87% in B), though more than half as often (RL3). The earlier body signs are known
modifiers no more often than frequency-matched signs (RL4). The known-head set (183 signs) is large enough that most
common signs belong to it, so the test has little power; closer-line bodies do not show the name-body pattern beyond
that. No roles adopted; R stays 81.3%. No progress: streak 4. Tally, counting parts: 1340 held, 1244 failed (2584
registered).

# Two-hundred-and-tenth set, registered before testing (24 September 2026): decipherment loop 35, discounted family context (four hypotheses)

Metric after loop 34: S 4.685 (tri + pos + end + f4), SIGN top-1 37.9%; streak 4. The family components interpolate
with count/(count + 2) weights. Absolute discounting (Kneser-Ney style: subtract D from each seen count, give the mass
to the lower order in proportion to the number of distinct followers) usually does better on sparse contexts. New
component f4k: the family 4-gram discounted onto the discounted family trigram, onto the family bigram; D = 0.5,
chosen on the training lines' own split (design: 4.7247 -> 4.7187; D 0.75 4.7199, D 0.9 4.7318).

- **DK1** S on the fixed test: tri + pos + end + f4k beats tri + pos + end + f4 by 0.003 bits or more.
- **DK2** The same A -> B (trained on A, tested on B's new lines).
- **DK3** SIGN top-1 on the fixed test (two-direction, as prizebench) does not fall with f4k in place of f4.
- **DK4** Progress rule: DK1 and DK2 hold (f4k enters the model).

# Two-hundred-and-eleventh set, registered before testing (24 September 2026): decipherment loop 36, a discounted sign trigram (four hypotheses)

Metric after loop 35: S 4.675 (tri + pos + end + f4k); streak 0 (loop 35 counted as progress). The sign trigram of
the set-125 model interpolates with count/(count + 2) weights onto the Kneser-Ney bigram. New component trik: the
trigram absolutely discounted (D = 0.75, chosen on the training lines' own split: 4.7169 -> 4.6763; D 0.5 4.6923,
D 0.9 4.6895) onto the same bigram; model trik + pos + end + f4k.

- **TK1** S on the fixed test beats tri + pos + end + f4k by 0.01 bits or more.
- **TK2** The same A -> B.
- **TK3** SIGN top-1 on the fixed test (two-direction) does not fall.
- **TK4** Progress rule: TK1 and TK2 hold (trik replaces tri).

## Results of the two-hundred-and-tenth set (added after the test; `predict_test210.py`, `results/predict_test210.md`, `famlm.py` f4k)

All four held. Absolute discounting of the family 4-gram (D = 0.5) lowers S on the fixed test from 4.6849 to 4.6753
(gain 0.0096; DK1) and A -> B from 5.2226 to 5.2162 (DK2); SIGN top-1 does not fall (37.8% -> 38.2%; DK3). f4k
enters the model; the metric run gives S 4.675, SIGN top-1 38.3%, top-5 60.6%. Progress: streak 0. Tally, counting
parts: 1344 held, 1244 failed (2588 registered).

# Two-hundred-and-twelfth set, registered before testing (24 September 2026): decipherment loop 37, lighter smoothing of the count components (four hypotheses)

Metric after loop 36: S 4.635 (trik + pos + end + f4k), SIGN top-1 39.6% (test run); streak 0. The position, end
and family-bigram components are add-one smoothed over the whole sign vocabulary (~560), heavy for contexts seen a few
dozen times. Add-k with k = 0.3 (chosen on the training lines' own split: 4.6772 -> 4.6643; k 0.1 4.6697, 0.03
4.6846, 0.01 4.6948) replaces add-one in those components (M2.sm).

- **SM1** S on the fixed test improves by 0.005 bits or more.
- **SM2** The same A -> B.
- **SM3** SIGN top-1 on the fixed test does not fall.
- **SM4** Progress rule: SM1 and SM2 hold (k = 0.3 adopted).

## Results of the two-hundred-and-eleventh set (added after the test; `predict_test211.py`, `results/predict_test211.md`, `famlm.py` trik)

All four held. Discounting the sign trigram (D = 0.75) onto the Kneser-Ney bigram lowers S on the fixed test from
4.6753 to 4.6354 (gain 0.040, the largest single gain of the loops; TK1) and A -> B from 5.2146 to 5.2070 (TK2);
SIGN top-1 rises from 38.2% to 39.6% (TK3). trik replaces tri; the metric run gives S 4.635 (26.1% of the unigram
entropy explained), SIGN 39.7% / 61.8%, WORD top-10 3.4%. Progress: streak 0. Tally, counting parts: 1348 held,
1244 failed (2592 registered).

# Two-hundred-and-thirteenth set, registered before testing (24 September 2026): decipherment loop 38, the line's opening sign as context (four hypotheses)

Metric after loop 36: S 4.635 (trik + pos + end + f4k); streak 0; loop 37 (smoothing) pending. Set 125 tried a
component conditioned on the line's first sign and did not keep it; with the new model a design run on the training
lines' own split gives trik + pos + end + f4k 4.6772 -> + first 4.6621 (a discounted sign 4-gram 4.6845, + start
4.6763, + len 4.6835: not kept). The heading and the name openers (sets 45, 161) make the first sign a plausible cue
for the rest of the line.

- **FS1** S on the fixed test with + first beats the model without it by 0.005 bits or more.
- **FS2** The same A -> B.
- **FS3** SIGN top-1 on the fixed test does not fall.
- **FS4** Progress rule: FS1 and FS2 hold (first enters the model).

## Results of the two-hundred-and-twelfth set (added after the test; `predict_test212.py`, `results/predict_test212.md`)

One held, three failed. Add-0.3 smoothing of the count components lowers S on the fixed test (4.6354 -> 4.6284; SM1)
but raises it A -> B (5.1927 -> 5.2177; SM2 fails) and lowers SIGN top-1 (39.7% -> 39.2%; SM3 fails): lighter
smoothing overfits the contexts of one sample, and B's new lines have more unseen ones. Not adopted (famlm.M3.K
stays 1). No progress: streak 1. Tally, counting parts: 1349 held, 1247 failed (2596 registered).

## Results of the two-hundred-and-thirteenth set (added after the test; `predict_test213.py`, `results/predict_test213.md`)

All four held. A component conditioned on the line's opening sign lowers S on the fixed test from 4.6354 to 4.6097
(gain 0.026; FS1) and A -> B from 5.1927 to 5.1557 (gain 0.037; FS2); SIGN top-1 holds (39.7% -> 39.8%; FS3). The
first sign carries information about the whole line, as the heading and name-opener findings imply (the position
component's weight falls to zero beside it). first enters the model; the metric run gives S 4.610 (26.5% explained),
SIGN 39.8% / 62.1%, WORD top-10 3.9%. Progress: streak 0. Tally, counting parts: 1353 held, 1247 failed (2600
registered).

**Withdrawn after set 223 (leak).** The 'first' component (set 125's) counts, for every position, the signs of lines
that open with the line's first sign, including position 0 itself: the first sign is predicted from a context that is
the first sign. With position 0 given no such conditioning, 'first' gets weight 0 and S is exactly the model without
it (4.6354). The S gain here, and those of firstpos (set 214) and first2 (set 217, which conditions position 1 on
itself), were artefacts of the leak. 'first' is removed from the model; S returns to 4.635 (set 211).

# Two-hundred-and-fourteenth set, registered before testing (24 September 2026): decipherment loop 39, opening sign by position (four hypotheses)

Metric after loop 38: S 4.610 (trik + pos + end + f4k + first); streak 0. A design run on the training lines' own
split: conditioning on the opening sign and the position class together (firstpos: first sign x first / middle /
last-but-one / last) in place of first gives 4.6690 -> 4.6513; the opening sign's graphic family adds nothing
(4.6695).

- **FP1** S on the fixed test with firstpos in place of first beats the current model by 0.005 bits or more.
- **FP2** The same A -> B.
- **FP3** SIGN top-1 on the fixed test does not fall.
- **FP4** Progress rule: FP1 and FP2 hold (firstpos replaces first).

## Results of the two-hundred-and-fourteenth set (added after the test; `predict_test214.py`, `results/predict_test214.md`, `famlm.py` firstpos)

Three held, one failed. Conditioning on the opening sign and the position class together lowers S on the fixed test
from 4.6097 to 4.5915 (FP1) and A -> B from 5.1544 to 5.1471 (FP2), but SIGN top-1 does not rise (39.8% -> 39.7%;
FP3 fails). The metric run with firstpos gives S 4.594 but SIGN 39.7% / 61.7% and WORD top-10 3.4%, below loop 38's
39.8% / 62.1% / 3.9%. The prize bench ranks the prediction tasks above S, so firstpos is **not adopted** (the model
stays with first) and the loop is counted conservatively as no progress: streak 1. Tally, counting parts: 1356 held,
1248 failed (2604 registered).

# Two-hundred-and-fifteenth set, registered before testing (24 September 2026): decipherment loop 40, the sign before a count (five hypotheses)

Metric after loop 39: R 81.3% (1,034 unroled tokens in count lines); streak 1. Count lines (genre 'count') often put
signs before the numeral run: '104 4 390', '125 861 2 4 390', 'x N x' is the second commonest shape (59 lines). If
the slot before a count is a label for what or whose the count is, it should be filled from a restricted set. Unit:
the sign directly before the first numeral run of a count line (not at position 0 excluded; numerals not counted).
Null: the same lines with their non-numeral signs shuffled among the non-numeral positions (numerals stay), 1,000
times; statistic = share of pre-count tokens taken by the ten commonest pre-count signs.

- **CT1** In A's distinct count lines the pre-count slot is more concentrated than in its shuffles (p < 0.01).
- **CT2** The same in B's new count lines (p < 0.05).
- **CT3** The ten commonest pre-count signs of A cover 40% or more of B's pre-count tokens.
- **CT4** Pre-count signs are name heads (seen before 740 / 520 in A) less often than the counted sign after the
  numerals (B): the label slot is not the counted-thing slot.
- **CT5** Progress rule: CT1 and CT2 hold; then the sign directly before a count gets the role 'count label' in R.

## Results of the two-hundred-and-fifteenth set (added after the test; `predict_test215.py`, `results/predict_test215.md`)

Four held, one failed. The slot directly before a count is filled from a restricted set: the ten commonest pre-count
signs take 51.9% of 270 tokens in A (shuffles p = 0.001; CT1) and 58.3% of 199 in B (p = 0.001; CT2), and A's ten
cover 42.7% of B's (CT3). Pre-count signs are name heads about as often as counted signs (69% against 73%; CT4 fails).
**Check after the test**: the commonest pre-count signs are the heading signs 861, 820, 817 (and 60), whose second
element 2 is read as a numeral; with those lines left out the slot is still restricted, but less (A p = 0.036, B p =
0.013). Heading tokens already have a role; the new role 'count label' adds the other pre-count signs: R rises from
81.3% to 84.2% (344 tokens). Progress (CT5): streak 0. Tally, counting parts: 1360 held, 1249 failed (2609
registered).

# Two-hundred-and-sixteenth set, registered before testing (24 September 2026): decipherment loop 41, the count label in the grammar (four hypotheses)

Metric after loop 40: R 84.2%, G margin A 46.2 / B 34.7; streak 0. A grammar rule for set 215's finding: LABEL-COUNT
= one of A's ten commonest pre-count signs + a line that G2 parses as a count. Design on A: margin 46.2 -> 46.6.

- **GL1** G2 + LABEL-COUNT raises the margin over shuffled lines on B (any rise).
- **GL2** It raises coverage of real B lines more than of shuffled B lines.
- **GL3** It raises the margin on F's extra lines (any rise).
- **GL4** Progress rule: GL1 and GL2 hold (the G margin component rises on the independent sample).

# Two-hundred-and-seventeenth set, registered before testing (24 September 2026): decipherment loop 42, the line's first two signs as context (four hypotheses)

Metric after loop 41 (pending measurement): S 4.610 (trik + pos + end + f4k + first), SIGN top-1 39.8%. Component
first2: every sign after the first conditioned on the line's first two signs, interpolated (count/(count + 3)) onto
first; replaces first. Design on the training lines' own split: 4.6690 -> 4.6334. Loop 39 showed S can improve while
the prize tasks slip, so the progress rule now also requires SIGN not to fall.

- **F21** S on the fixed test beats the current model by 0.01 bits or more.
- **F22** The same A -> B.
- **F23** SIGN top-1 on the fixed test does not fall.
- **F24** Progress rule: F21, F22 and F23 hold (first2 replaces first).

## Results of the two-hundred-and-sixteenth set (added after the test; `predict_test216.py`, `results/predict_test216.md`, `grammar.parse3`)

All four held. The LABEL-COUNT rule (one of A's ten commonest pre-count signs + a count) raises the margin over
shuffled lines on B from 34.75 to 35.13 points (GL1), real B coverage more than shuffled (+0.75 against +0.37; GL2),
and the margin on F's extra lines from 17.34 to 17.92 (GL3). Adopted in the metric's G margin. Progress: streak 0.
Tally, counting parts: 1364 held, 1249 failed (2613 registered).

## Results of the two-hundred-and-seventeenth set (added after the test; `predict_test217.py`, `results/predict_test217.md`, `famlm.py` first2)

Two held, two failed. Conditioning on the line's first two signs lowers S on the fixed test from 4.6097 to 4.5725
(F21) and A -> B from 5.1544 to 5.1338 (F22), but SIGN top-1 falls from 39.8% to 38.5% (F23 fails): when the hidden
sign is one of the first two, the component conditions on the candidate itself and rewards candidates that make
familiar openings rather than the right sign. By the rule registered for this loop (SIGN must not fall) it is not
adopted: no progress, streak 1. Tally, counting parts: 1366 held, 1251 failed (2617 registered).

# Two-hundred-and-eighteenth set, registered before testing (24 September 2026): decipherment loop 43, discounted position and end components (four hypotheses)

Metric after loop 42: S 4.610 (trik + pos + end + f4k + first), SIGN top-1 39.8%; streak 1. The position and
distance-from-end components are add-one smoothed over the vocabulary; lighter add-k overfit (set 212). Absolute
discounting onto the unigram (D = 0.5; the unigram add-0.5) is the principled alternative: posk, endk. Design on the
training lines' own split: 4.6690 -> 4.6163 (D 0.75 the same). (An LSTM component was also tried in design and made
things worse at this data size; not registered.)

- **PK1** S on the fixed test with posk + endk in place of pos + end beats the current model by 0.01 bits or more.
- **PK2** The same A -> B.
- **PK3** SIGN top-1 on the fixed test does not fall.
- **PK4** Progress rule: PK1, PK2 and PK3 hold.

## Results of the two-hundred-and-eighteenth set (added after the test; `predict_test218.py`, `results/predict_test218.md`, `famlm.py` posk / endk)

Two held, two failed. Discounting the position and distance-from-end components onto the unigram lowers S on the
fixed test from 4.6097 to 4.5706 (PK1) and A -> B from 5.1544 to 5.1224 (PK2), but SIGN top-1 falls from 39.8% to
39.5% (PK3 fails), so by the registered rule it is not adopted: no progress, streak 2. As in sets 214 and 217, S keeps
improving while the SIGN task stays near 39-40%: better calibrated probabilities do not change which candidate ranks
first. Tally, counting parts: 1368 held, 1253 failed (2621 registered).

# Two-hundred-and-nineteenth set, registered before testing (24 September 2026): decipherment loop 44, what follows a count (four hypotheses)

Metric after loop 43: R 84.2% (unroled: count lines 690 tokens, 'other' lines 790); streak 2. In count lines the
signs after the counted sign (the first sign after the numeral run) have no role: 'N x x x' (11 lines in A), 'x N x x
x' (14). If a count is followed by the name of its owner or place, the last sign of that tail should be a known name
head. Tail = the signs after the counted sign, when there are 2+. Known heads = signs seen directly before 740 / 520
in A. Null: frequency-matched draws (the 20 nearest signs in frequency rank), 1,000 times.

- **AF1** In A's count lines, the last sign of the tail is a known name head more often than frequency-matched draws
  (p < 0.05).
- **AF2** The same in B's new count lines (heads from A).
- **AF3** The tail's other signs are known name modifiers more often than frequency-matched draws (B).
- **AF4** Progress rule: AF1 and AF2 hold; then the tail's last sign gets 'name head' and the rest 'name modifier' in R.

## Results of the two-hundred-and-nineteenth set (added after the test; `predict_test219.py`, `results/predict_test219.md`)

None held. The tail after a count's counted sign (100 tails in A, 62 in B) ends in a known name head no more often
than frequency-matched signs (A 70%, p = 0.32; B 76%, p = 0.67; AF1, AF2), and its other signs are known modifiers no
more often than chance (AF3). As with the closer lines (set 209), the known-head and known-modifier sets are so large
that the commonest signs belong to them; no name structure is shown in count tails. No roles added. No progress:
streak 3. Tally, counting parts: 1368 held, 1257 failed (2625 registered).

# Two-hundred-and-twentieth set, registered before testing (24 September 2026): decipherment loop 45, no prefixes in the L profile (five hypotheses)

Metric after loop 44: L world 81.3% of WALS genera / 68.3% of Grambank families excluded (tolerant profile, set 196);
streak 3. The profile allowed WALS 26A 'weakly suffixing' (3), which admits languages with productive prefixes. The
Indus names show no closed set of prefixes: what stands before a head comes from an open set (sets 141, 176; section
11 of the write-up), and no sign class sits obligatorily before heads the way possessor prefixes do. Strict profile:
WALS 26A = 2 only (strongly suffixing), other tolerant features as set 196; Grambank: tolerant profile plus GB431 = 0
(no prefix marking the possessed noun). Majority rule per group as set 196. Burushaski (26A = 3; possessor prefixes
on inalienable nouns) is the open candidate family most affected.

- **LS1** Strict WALS profile excludes more genera than 81.3% and keeps the Dravidian and Indic genera.
- **LS2** Grambank with GB431 = 0 excludes more families than 68.3% and keeps Dravidian and Indo-European.
- **LS3** Burushaski is excluded by both.
- **LS4** Munda is kept by the strict WALS profile (26A = 2 for Mundari), so the change is not aimed at one family.
- **LS5** Progress rule: LS1 and LS2 hold (L world rises in both databases); if LS3 also holds, Burushaski leaves the
  open families (L 4 -> 3) with the caveat that the evidence is the absence of a prefix class in names.

## Results of the two-hundred-and-twentieth set (added after the test; `predict_test220.py`, `results/predict_test220.md`, `lbench.world_strict`)

Four held, one failed. Requiring the strongly suffixing type (no productive prefixes), as the Indus names show no
prefix class, raises the share of WALS genera excluded from 81.3% to 85.1% (LS1) and, with no possessor prefix on the
possessed noun, the share of Grambank families excluded from 68.3% to 77.0% (LS2); the Dravidian, Indic /
Indo-European and Munda groups are kept (LS4). Burushaski is excluded by WALS (26A weakly suffixing) but not by
Grambank (GB431 coded absent), so it stays open (LS3 fails; L stays 4). L world enters the metric at 85.1% / 77.0%.
Caveat: the evidence is the absence of a prefix class in short name texts. Progress: streak 0. Tally, counting parts:
1372 held, 1258 failed (2630 registered).

# Two-hundred-and-twenty-first set, registered before testing (24 September 2026): decipherment loop 46, doubling at the edges in the grammar (four hypotheses)

Metric after loop 45: G margin A 46.6 / B 35.1; streak 0. Set 187: doubled signs stand at text edges. Rule EDGE-DOUBLE:
a line whose first two (or last two) signs are one non-numeral sign doubled is accepted if the rest parses (G2 +
LABEL-COUNT). Design on A: margin 50.53 -> 51.16 (15 more lines).

- **ED1** The rule raises the B margin over shuffled lines (any rise).
- **ED2** It raises coverage of real B lines more than of shuffled B lines.
- **ED3** It raises the margin on F's extra lines.
- **ED4** Progress rule: ED1 and ED2 hold.

## Results of the two-hundred-and-twenty-first set (added after the test; `predict_test221.py`, `results/predict_test221.md`, `grammar.parse4`)

All four held. EDGE-DOUBLE (a doubled non-numeral sign at either edge, the rest parsing) raises the margin over
shuffled lines on B from 35.13 to 35.92 points (ED1), real B coverage more than shuffled (+1.04 against +0.25; ED2),
and the margin on F's extra lines from 17.92 to 18.43 (ED3). Adopted in the metric's G margin. Progress: streak 0.
Tally, counting parts: 1376 held, 1258 failed (2634 registered).

# Two-hundred-and-twenty-second set, registered before testing (24 September 2026): decipherment loop 47, a caged sign with its marker (four hypotheses)

Metric after loop 46: G margin A 47.2 / B 35.9; streak 0. Set 184 found caged signs replace the ending; a caged (or
closer) sign followed only by 400 / 90 is then an ending with its post-ending marker, a line the grammar still
rejects ('226 400', '236 400'). Rule CAGED-POST. Design on A: margin 51.16 -> 51.28 (a sign + final long stroke
rule was also tried in design and lowered the margin; not registered).

- **CP1** The rule raises the B margin (any rise).
- **CP2** It raises real B coverage more than shuffled.
- **CP3** It raises the F margin.
- **CP4** Progress rule: CP1 and CP2 hold.

## Results of the two-hundred-and-twenty-second set (added after the test; `predict_test222.py`, `results/predict_test222.md`, `grammar.parse5`)

Three held, one failed. CAGED-POST (a caged or closer sign followed only by 400 / 90) raises the B margin slightly,
35.92 -> 36.02 points (CP1), real B coverage more than shuffled (+0.22 against +0.12; CP2); the F margin is unchanged
(CP3 fails). A small gain, adopted in the metric's G margin. Progress: streak 0. Tally, counting parts: 1379 held,
1259 failed (2638 registered).

# Two-hundred-and-twenty-third set, registered before testing (24 September 2026): decipherment loop 48, a second unit after a mid-line ending (four hypotheses)

Metric after loop 47: R 84.2%; streak 0. Many lines of no genre continue after a name's ending: '176 740 220', '176
740 590 892 352 297 400'. Sets 209 and 219 tested 'is the last sign a known head' and lacked power (most common signs
are known heads). Sharper statistic: a sign's head propensity = the share of its A occurrences directly before 740 /
520. Unit: the tail after a mid-line 740 or 520 (the ending not last, not followed only by 400 / 90 or a closer), with
400 / 90 dropped, of 1+ lexical signs. Null: frequency-matched draws (20 nearest in rank), 1,000 times; statistic =
mean head propensity of the tail's last signs.

- **SU1** In A the tail's last sign has higher head propensity than frequency-matched draws (p < 0.05).
- **SU2** The same in B's new lines (propensities from A).
- **SU3** In B the tail's other signs have lower head propensity than its last sign.
- **SU4** Progress rule: SU1 and SU2 hold; then tail last sign = 'name head', other tail signs = 'name modifier' in R.

## Results of the two-hundred-and-twenty-third set (added after the test; `predict_test223.py`, `results/predict_test223.md`)

One held, three failed. The tail after a mid-line 740 / 520 does not end like a name: in A the last tail sign's
mean head propensity is 0.073, below every one of 1,000 frequency-matched draws (so SU1, which predicted higher,
fails with p = 1.0); in B 0.126, p = 0.67 (SU2 fails); the other tail signs are slightly less head-like than the last
(SU3). **Reading:** what follows a finished name is not a second name; its signs avoid the head slot, as epithets,
titles or closers would. Not turned into a role (the registered direction failed). No progress: streak 1. Tally,
counting parts: 1380 held, 1262 failed (2642 registered).

# Two-hundred-and-twenty-fourth set, registered before testing (24 September 2026): decipherment loop 49, weighting the two directions in SIGN (three hypotheses)

Metric after the correction: S 4.635, SIGN top-1 39.7% / top-5 61.8% (forward + backward log-probabilities, equal
weight); streak 1. A design run on 300 lines of the training lines' own split: forward weight 0.3 / 0.4 / 0.5 / 0.6 /
0.7 gives 39.8 / 40.1 / 40.2 / 40.3 / 40.4% top-1. Registered: weight 0.7 on the forward model.

- **WD1** SIGN top-1 on the fixed test with weight 0.7 beats equal weights by 0.3 points or more.
- **WD2** The same A -> B (first 300 B lines).
- **WD3** Progress rule: WD1 and WD2 hold (the SIGN tier rises and the gain replicates).

## Results of the two-hundred-and-twenty-fourth set (added after the test; `predict_test224.py`, `results/predict_test224.md`)

None held. Weighting the forward model 0.7 lowers SIGN top-1 on the fixed test (39.8% -> 39.2%; WD1) and A -> B
(33.0% -> 31.9%; WD2): the design-run difference (0.2 points on 300 lines) was noise, and equal weights stay. No
progress: streak 2. Tally, counting parts: 1380 held, 1265 failed (2645 registered).

# Two-hundred-and-twenty-fifth set, registered before testing (24 September 2026): decipherment loop 50, the post-name tail replicated on F (three hypotheses)

Metric: S 4.635, R 84.2%; streak 2. Set 223 found, against its registered direction, that in A the last sign of a
tail after a mid-line 740 / 520 has lower head propensity than any of 1,000 frequency-matched draws (0.073); in B the
direction was the same but weak (0.126). F's extra lines (not in A or B) were not looked at. Registered now in the
observed direction: tails after a finished name are not name-like.

- **TL1** In F's extra lines, the tail's last sign has lower head propensity (from A) than frequency-matched draws
  (one-sided p < 0.05, 1,000 draws).
- **TL2** In F, the tail signs overall (all positions) have lower head propensity than frequency-matched draws.
- **TL3** Progress rule: TL1 holds (A's finding replicates on unseen lines); then the tail signs after a mid-line
  ending get the role 'post-name element' in R.

## Results of the two-hundred-and-twenty-fifth set (added after the test; `predict_test225.py`, `results/predict_test225.md`)

None held. F's extra lines give only 20 tails after a mid-line ending; their last signs' head propensity (0.119) is
not lower than frequency-matched draws (p = 0.38; TL1), nor are the tail signs overall (TL2). Set 223's A result
does not replicate on B (weak) or F (too few, no effect); it is left as an A-only observation, and no role is added.
No progress: streak 3. Tally, counting parts: 1380 held, 1268 failed (2648 registered).

# Two-hundred-and-twenty-sixth set, registered before testing (24 September 2026): decipherment loop 51, Parpola's description families used alike? (four hypotheses)

Metric: M+ 41.4% (numerals, copper-tablet anchors, and Fairservis depiction classes human / tool / plant / fish
confirmed by use, set 178); streak 3. Set 183 found that of Fairservis's depiction groups only fish (and tools weakly)
are used alike. Parpola's CISI descriptions give independent, larger depiction families (descfam.py: person 36 signs,
leaf, fish, tree, jar ...). Use coherence as set 183 (predict_test62.sims context similarity, signs seen 20+ times;
mean pairwise similarity within the family against 1,000 random groups of the same size), computed on A's lines and
on B's lines separately, for every description family with 3+ qualifying members in each.

- **UA1** At least one description family other than fish is used alike in both A and B (p < 0.05 each).
- **UA2** The 'person' family is used alike in both.
- **UA3** The fish family is used alike in both (replicating set 183 with Parpola's family).
- **UA4** Progress rule: UA1 holds; the families that pass both enter M+ (their tokens counted as meaning classes).

## Results of the two-hundred-and-twenty-sixth set (added after the test; `predict_test226.py`, `results/predict_test226.md`)

One held, three failed. Of Parpola's description families with enough frequent members, only the fish family is used
alike in both samples (A mean similarity 0.203, p = 0.001; B 0.254, p = 0.001; UA3), replicating set 183 with an
independent grouping. Strokes (A p = 0.02, B 0.07), leaves (A 0.03, B 0.09) and the jar (B 0.03 only) reach it in one
sample; the person family in neither (UA2). No new class enters M+ (UA1, UA4 fail). The fish remain the one depiction
family whose members behave as one class. No progress: streak 4. Tally, counting parts: 1381 held, 1271 failed (2652
registered).

# Two-hundred-and-twenty-seventh set, registered before testing (24 September 2026): decipherment loop 52, one grammar across sites (five hypotheses)

Metric: G margin A 47.3 / B 36.0; tier 4 (archaeological consistency) has the fish / 520 signal holding at every site
and period (set 196); streak 4. A stronger consistency test: the grammar (grammar.parse5: G2 + LABEL-COUNT +
EDGE-DOUBLE + CAGED-POST) with its learned parts (name heads, head statistics, count labels) taken from one site's
distinct lines only, scored on another site's distinct lines as a margin over shuffled lines (grammar.margin). Sites
from F (ICIT field 3): Mohenjo-daro, Harappa, other sites together.

- **CS1** Learned on Mohenjo-daro, the margin on Harappa lines is 25 points or more.
- **CS2** Learned on Harappa, the margin on Mohenjo-daro lines is 25 points or more.
- **CS3** Learned on Mohenjo-daro + Harappa, the margin on the other sites is 20 points or more.
- **CS4** The cross-site margins are within 10 points of the within-site margins (the learned site's own lines).
- **CS5** Progress rule: CS1, CS2 and CS3 hold (one grammar serves every site: a tier-4 finding).

## Results of the two-hundred-and-twenty-seventh set (added after the test; `predict_test227.py`, `results/predict_test227.md`)

All five held. The grammar with its learned parts taken from one site parses another site's lines far better than
shuffled lines, and nearly as well as its own: learned on Mohenjo-daro (1,186 distinct lines), the margin on Harappa
is 43.8 points against 44.8 at home (CS1); learned on Harappa (777), 46.1 on Mohenjo-daro against 44.6 at home (CS2);
learned on both cities, 36.1 on the other sites together (457 lines; 46.0 at home; CS3). All cross-site margins are
within 10 points of the within-site ones (CS4). **Reading:** one grammatical system, with the same heads, endings,
count labels and devices, serves the two cities and the smaller sites: a tier-4 (archaeological consistency) finding
that any reading must respect. Progress (a new finding that replicates across independent samples): streak 0. Tally,
counting parts: 1386 held, 1271 failed (2657 registered).

# Two-hundred-and-twenty-eighth set, registered before testing (24 September 2026): decipherment loop 53, one grammar across object types and periods (five hypotheses)

Metric: G margin A 47.3 / B 36.0; set 227 found one grammar across sites; streak 0. The same test across object types
(F: seals 1,530 distinct lines, tablets 578) and across time at Harappa (ICIT period, as set 196: early 83 lines, late
282). Grammar and learned parts as set 227.

- **OT1** Learned on seals, the margin on tablet lines is 20 points or more.
- **OT2** Learned on tablets, the margin on seal lines is 20 points or more.
- **OT3** Learned on late Harappa, the margin on early Harappa lines is 20 points or more.
- **OT4** The seal -> tablet margin is lower than the seal -> seal (within) margin by 5 points or more (tablets are a
  different genre, sets 69, 157).
- **OT5** Progress rule: OT1 and OT3 hold (the grammar holds across object type and time).

## Results of the two-hundred-and-twenty-eighth set (added after the test; `predict_test228.py`, `results/predict_test228.md`)

All five held. The grammar learned on seals parses tablet lines with a margin of 43.6 points over shuffled lines
(OT1), learned on tablets it parses seals at 48.1 (OT2), and learned on late Harappa it parses the early levels at
27.0 (83 lines; OT3). Tablets sit 5.2 points below seals under the seal grammar (48.8 against 43.6; OT4), in line
with their being a different genre. With set 227: one grammatical system across sites, object types and periods, the
early Harappa lines included. Progress: streak 0. Tally, counting parts: 1391 held, 1271 failed (2662 registered).

# Two-hundred-and-twenty-ninth set, registered before testing (24 September 2026): decipherment loop 54, the graphic devices in each city (five hypotheses)

Metric: streak 0; tier 4 has one grammar across sites, object types and periods (sets 227-228). The graphic devices
were found on pooled data. Per city (F, distinct lines of Mohenjo-daro and of Harappa, separately):

- **GD1** Caged signs (set 184) are followed by 740 / 520 in 5% of cases or fewer at Mohenjo-daro, and less often
  than their uncaged base signs are (the ten signs of CAGED against all other lexical signs).
- **GD2** The same at Harappa.
- **GD3** Stroked jars (741, 742, 745) end the line (only 400 / 90 after them) less often than the plain jar 740, at
  Mohenjo-daro (one-sided Fisher p < 0.05).
- **GD4** The same at Harappa.
- **GD5** Progress rule: GD1-GD4 all hold (the device system is shared by both cities: a tier-4 finding).

## Results of the two-hundred-and-twenty-ninth set (added after the test; `predict_test229.py`, `results/predict_test229.md`)

All five held. In each city separately, caged signs are never followed by 740 / 520 (Mohenjo-daro 0 of 52,
Harappa 0 of 16, against 16.1% and 16.8% for other lexical signs; GD1, GD2), and the stroked jars almost never end a
line where the plain jar usually does (Mohenjo-daro 2 of 118 against 487 of 558; Harappa 4 of 43 against 289 of 323;
GD3, GD4). The two cities share the device system as well as the grammar (sets 227-228). Progress: streak 0. Tally,
counting parts: 1396 held, 1271 failed (2667 registered).

# Two-hundred-and-thirtieth set, registered before testing (24 September 2026): decipherment loop 55, the class signal on seals and tablets (three hypotheses)

Streak 0. Set 196 found fish-headed names take 520 more often than other identified-head names at every site and
period. Across object types (F: SEAL* against TAB*), separately, with set 196's test (depiction classes of set 178,
one-sided Fisher):

- **FT1** On seals, fish-headed names take 520 more often than other identified-head names (p < 0.05).
- **FT2** On tablets, the same (p < 0.05).
- **FT3** Progress rule: FT1 and FT2 hold (the class signal is shared by both object types: tier 4).

## Results of the two-hundred-and-thirtieth set (added after the test; `predict_test230.py`, `results/predict_test230.md`)

All three held. Fish-headed names take 520 far more often than other identified-head names on seals (60 of 120
against 4 of 156; FT1) and on tablets (14 of 33 against 1 of 47; FT2). With set 196 (sites, periods): the class
signal holds across places, periods and object types. Progress: streak 0. Tally, counting parts: 1399 held, 1271
failed (2670 registered).

# Two-hundred-and-thirty-first set, registered before testing (24 September 2026): decipherment loop 56, the count-label slot in each city (three hypotheses)

Streak 0. Set 215 found the slot before a count restricted in A and in B. Per city (F distinct count lines of
Mohenjo-daro and of Harappa), with set 215's statistic and shuffle null (1,000 shuffles of non-numeral signs within
lines):

- **CC1** At Mohenjo-daro the pre-count slot is more concentrated than in shuffled lines (p < 0.05).
- **CC2** The same at Harappa.
- **CC3** Progress rule: CC1 and CC2 hold (the count label is shared by both cities: tier 4).

## Results of the two-hundred-and-thirty-first set (added after the test; `predict_test231.py`, `results/predict_test231.md`)

All three held. The slot before a count is restricted in each city: Mohenjo-daro top-ten share 51.0% of 151
pre-count tokens (p = 0.001; CC1), Harappa 58.8% of 102 (p = 0.002; CC2). Counted as progress like sets 229-230; from
the next loop on, per-subset replications of findings already made no longer count as progress under the stopping
rule (they are consistency evidence, not new findings). Streak 0. Tally, counting parts: 1402 held, 1271 failed (2673
registered).

# Two-hundred-and-thirty-second set, registered before testing (24 September 2026): decipherment loop 57, does the ending follow the graphic family? (four hypotheses)

Streak 0. A name's ending (740 / 520 / closer / caged / other) is chosen by its head (sets 103-120), and fish-family
heads lean to 520 (sets 178, 196). New question: do heads of the same graphic family (ICIT decade block, famlm.fam)
choose endings alike beyond the fish? Statistic: over heads with 5+ names, the mean within-family share of the
family's modal ending, weighted by names; null: heads regrouped at random into groups of the same sizes, 1,000
times. Names from distinct lines (R.name_of), ending = the name's ending sign class.

- **FE1** In A, heads' endings are more homogeneous within graphic families than in random groupings (p < 0.05).
- **FE2** The same in B (families and heads as in B's names).
- **FE3** With the fish block (heads 219-240) left out, FE1 and FE2 still hold (p < 0.05 each).
- **FE4** Progress rule: FE3 holds (a new finding beyond the fish, replicated on B).

## Results of the two-hundred-and-thirty-second set (added after the test; `predict_test232.py`, `results/predict_test232.md`)

None held. Heads of one graphic family do not choose endings more alike than random groupings of heads: A modal-ending
share 0.877 (49 heads, 10 families with 2+ heads), p = 0.94 (FE1); B 0.925, p = 0.80 (FE2); without the fish block
p = 0.97 and 0.93 (FE3). With 740 ending most names the statistic sits near its ceiling, so the test has little power;
beyond the fish, no family-level ending class is shown. No progress: streak 1. Tally, counting parts: 1402 held, 1275
failed (2677 registered).

# Two-hundred-and-thirty-third set, registered before testing (24 September 2026): decipherment loop 58, texts whose referent the picture fixes (four hypotheses)

Streak 1. Tier 1 (V) counts sign tokens read as sense and checked against outside evidence; it is 0.008% (four
copper-tablet picture signs). Sets 200-203: on tablets the picture goes with the whole text, not with single signs.
Mould copies are one design repeated and prove nothing, but copper tablets (TAB:C) and incised tablets (TAB:I) are
made one by one. Criterion: a text written on 3+ individually made pictured objects (TAB:C, TAB:I; motif as set 200)
whose modal picture is on 80%+ of them has its **referent fixed by the picture** (not a reading). Null: pictures
shuffled among all those objects, 1,000 times.

- **RF1** More text groups meet the criterion than in 95% of shuffles.
- **RF2** At least three distinct texts meet it.
- **RF3** Every text meeting it pairs with a picture no other qualifying text pairs with, or the shared pictures are
  listed (a label is specific to its scene).
- **RF4** Progress rule: RF1 and RF2 hold; then V gains a line 'referent fixed by the picture': the share of sign
  tokens (distinct lines) in qualifying texts, reported beside the strict V.

## Results of the two-hundred-and-thirty-third set (added after the test; `predict_test233.py`, `results/predict_test233.md`, `prizebench.referent_fixed`)

Three held, one failed. Eleven texts are written on 3+ individually made pictured objects (copper and incised tablets)
with one picture on 80%+ of them; no shuffle of the pictures gives as many (p = 0.001; RF1, RF2): the hare text 235
705 33 845 407 321 407, the archer (anthropomorph) text 806 845 61 407 850 900 740, the elephant text 706 33 923 740
(+/- a final stroke), the goat text 3 421 176 100 740 790, the loop text 415 220 845 407, a gharial text 605 760 740
400, a fish text 27 32 740 400, and three texts with the bull (415 578 32 824; 33 700; 176 740 400). Two pictures are
shared (the elephant variants, three bull texts; RF3 fails). Their referent is fixed by the picture, which is outside
evidence, though they are not read. Tier 1 gains a line beside the strict V: referent fixed by the picture, 0.38% of
sign tokens (11 texts). Progress: streak 0. Tally, counting parts: 1405 held, 1276 failed (2681 registered).

# Two-hundred-and-thirty-fourth set, registered before testing (25 September 2026): decipherment loop 59, a Linear B control for the picture-referent method (four hypotheses)

Streak 0. Set 233's method (a unit written with the same picture on 80%+ of its 3+ occurrences has its referent fixed
by the picture) needs a positive control (tier 2). In Linear B the pictures are the ideograms and the known answers are
the commodity words. Units = syllabic word types; picture of a line = its first non-measure ideogram (measure and
fraction signs T, M, Z, S, N, L, P, O, X, V, Q and syllabic adjuncts of one or two letters left out); a word qualifies
if it occurs in 3+ lines with an ideogram and 80%+ of them carry one ideogram. Known pairs, fixed here and not looked
at before (a few others, ka-ko / AES, ti-ri-po / *201VAS, si-to / GRA, e-ra-wo / OLE, ku-ru-so / AUR, ku-pa-ro, me-ri,
were glanced at in an earlier design check and are excluded): a-mo / ROTA (wheels), i-qo / EQU (horse), pa-ka-na /
*233 (swords), e-ke-a / *254 (spears), sa-sa-ma / SA (sesame), ko-ri-ja-do-no / KO (coriander), i-qi-ja / BIG
(chariot).

- **LR1** The method recovers 3 or more of the 7 known pairs (the word qualifies with its known ideogram).
- **LR2** It qualifies more word types than with ideograms shuffled among lines (95% of 1,000 shuffles).
- **LR3** No known word qualifies with a wrong ideogram.
- **LR4** Progress rule: LR1 and LR2 hold (the method passes a known-answer control: gate 3 of 6).

## Results of the two-hundred-and-thirty-fourth set (added after the test; `predict_test234.py`, `results/predict_test234.md`)

One held, three failed. On Linear B the picture-referent method qualifies 143 word types, against a shuffle median of
2 (95th percentile 6; LR2), so co-occurrence with a single picture is far from chance. By the registered answer key it
recovers none of the 7 known pairs (LR1 fails) and gives 'wrong' ideograms for three (LR3 fails): pa-ka-na -> PUG,
ko-ri-ja-do-no -> AROM, i-qi-ja -> CAPS. **Check after the test**: the key was written in the wrong ideogram
convention (Bennett numbers *233, *254 and the adjunct KO, where DAMOS names the ideograms PUG 'dagger / sword', AROM
'aromatic', CAPS 'chariot box'); by DAMOS's own names those three are correct referents. The registered verdict stands
(no progress: streak 1); a fresh registration with the key in DAMOS naming is the proper next step. a-mo, i-qo,
e-ke-a and sa-sa-ma do not qualify (too few lines, or mixed pictures). Tally, counting parts: 1406 held, 1279 failed
(2685 registered).

# Two-hundred-and-thirty-fifth set, registered before testing (25 September 2026): decipherment loop 60, the Linear B referent control with a key in DAMOS naming (three hypotheses)

Streak 1. Set 234's answer key used the wrong ideogram convention. A fresh key, in DAMOS's own ideogram names, of word
types not looked at before: a-mo-ta / ROTA (wheels), e-ra-wa / OLIV (olives), ko-wa / MUL (girls, counted with the
women), pa-we-a / *146 (cloths). Method and line picture exactly as set 234 (predict_test234.qualify).

- **LD1** The method recovers 2 or more of the 4 pairs.
- **LD2** None of the 4 qualifies with another ideogram.
- **LD3** Progress rule: LD1 holds (with set 234's LR2, the method passes a known-answer control: gate 3 of 6).

## Results of the two-hundred-and-thirty-fifth set (added after the test; `predict_test235.py`, `results/predict_test235.md`)

All three held. With the key in DAMOS's ideogram naming, the picture-referent method recovers a-mo-ta -> ROTA (wheels)
and ko-wa -> MUL (girls, counted with the women) (LD1); e-ra-wa and pa-we-a do not qualify, and no key word qualifies
with a wrong ideogram (LD2). With set 234 (143 qualifying words against 2 by chance, and three further correct
referents under DAMOS naming), the method passes a known-answer control: prize tier 2 rises to 3 of 6 methods, and the
tier-1 line 'referent fixed by the picture' (set 233) now rests on a gated method. Progress: streak 0. Tally, counting
parts: 1409 held, 1279 failed (2688 registered).

# Two-hundred-and-thirty-sixth set, registered before testing (25 September 2026): decipherment loop 61, the short lines of no genre (four hypotheses)

Streak 0. Lines that predict_test108.genre calls 'other' hold 790 unroled tokens; the commonest shapes are two and
three lexical signs ('x x' 37 lines, 'x x x' 25 in A + B). If they are bare names, their last sign should be head-like.
Statistic as set 223: mean head propensity (share of a sign's A occurrences directly before 740 / 520) of the last
sign, against frequency-matched draws (20 nearest in rank), 1,000 times. Lines: 'other'-genre lines of 2-3 signs, all
lexical (no numerals, endings, closers, 400 / 90).

- **OB1** In A the last sign is more head-like than frequency-matched draws (p < 0.05).
- **OB2** The same in B's new lines (propensities from A).
- **OB3** The first sign of these lines is less head-like than the last (A and B).
- **OB4** Progress rule: OB1 and OB2 hold; then these lines' last sign = 'name head', the rest 'name modifier' in R.

## Results of the two-hundred-and-thirty-sixth set (added after the test; `predict_test236.py`, `results/predict_test236.md`)

None held. In the short all-lexical lines of no genre, the last sign is not more head-like than frequency-matched
signs in A (24 lines, mean propensity 0.100, p = 0.81; OB1); in B it nearly is (45 lines, 0.186, p = 0.051; OB2), and
the first sign is not less head-like than the last (OB3). These lines do not behave as bare names; no roles added. No
progress: streak 1. Tally, counting parts: 1409 held, 1283 failed (2692 registered).

# Two-hundred-and-thirty-seventh set, registered before testing (25 September 2026): decipherment loop 62, the referent method at phrase level (four hypotheses)

Streak 1. The picture-referent method passed its Linear B control at word level (sets 234-235: word types recurring
across lines with one ideogram). Set 233 applied it to whole Indus texts. At the level where it was validated: units =
adjacent sign pairs (numerals included), counted once per object, on individually made pictured tablets (TAB:C,
TAB:I); a pair qualifies if it is on 3+ such objects, in 2+ distinct texts, with one picture on 80%+ of them. Null:
pictures shuffled among objects, 1,000 times.

- **PL1** More pairs qualify than in 95% of shuffles.
- **PL2** At least three qualifying pairs occur in 2+ distinct texts (not one text's copies).
- **PL3** The qualifying pairs occur on seals or other objects not used to find them (reported: how many tokens).
- **PL4** Progress rule: PL1 and PL2 hold; the tokens of qualifying pairs on the tablets used are added to the tier-1
  referent line (their occurrences elsewhere are reported, not counted).

## Results of the two-hundred-and-thirty-seventh set (added after the test; `predict_test237.py`, `results/predict_test237.md`, `prizebench.referent_fixed`)

All four held. At the level where the method passed its Linear B control, 11 adjacent sign pairs recur on 3+
individually made pictured tablets in 2+ distinct texts with one picture on 80%+ of them, against a shuffle median of
0 (95th percentile 3; PL1, PL2): 95 595, 595 1, 1 142 = one-horned bull; 176 740 = bull; 706 33, 33 923, 923 740, 740 1
= elephant; 32 740 = fish; 705 33 = hare; 240 740 = the S590 motif. Several come from near-duplicate texts (the
elephant text and its variant with a final stroke), so the gain is thinner than the count. The pairs occur 275 times on
other lines (PL3; reported, not counted). Counting their tokens on the tablets used raises the tier-1 referent line
from 0.38% to 0.61% of sign tokens. Progress: streak 0. Tally, counting parts: 1413 held, 1283 failed (2696
registered).

# Two-hundred-and-thirty-eighth set, registered before testing (25 September 2026): decipherment loop 63, the referent method on seals (three hypotheses)

Streak 0. Seals are carved one by one and carry a field animal; sign-level tests found seal texts independent of the
animal (second pass, set 200 PB4). The phrase-level referent method (set 237) applied to seals (SEAL:S, SEAL:R;
motif classes as set 200): pairs on 3+ seals in 2+ distinct texts with one animal on 80%+; the one-horned bull's base
rate is absorbed by the shuffle null (animals shuffled among seals, 1,000 times).

- **SR1** More pairs qualify than in 95% of shuffles.
- **SR2** Excluding the one-horned bull (Bull1), more pairs qualify for the other animals than in 95% of shuffles.
- **SR3** Progress rule: SR2 holds (a seal phrase fixes a non-default animal; tier 1).

## Results of the two-hundred-and-thirty-eighth set (added after the test; `predict_test238.py`, `results/predict_test238.md`)

One held, two failed. On seals, 189 sign pairs recur on 3+ seals in 2+ texts with one animal on 80%+ of them, above
the shuffle 95th percentile of 176 (SR1), but every one goes with the one-horned bull, the default animal; for the
other animals no pair qualifies, as in the shuffles (SR2 fails). Seal phrases do not fix a non-default animal: seal
texts do not name their animal, as the sign-level tests found. The slight excess with the one-horned bull fits the
one-horned-bull seals' texts differing somewhat from the others. No progress: streak 1. Tally, counting parts: 1414
held, 1285 failed (2699 registered).

# Two-hundred-and-thirty-ninth set, registered before testing (25 September 2026): decipherment loop 64, a longer family context (four hypotheses)

Streak 1. The discounted family 4-gram (f4k, set 210) helps S; a family 5-gram discounted onto it (f5k, D = 0.5)
gave 4.6772 -> 4.6722 in a design run on the training lines' own split. Model trik + pos + end + f5k.

- **F51** S on the fixed test beats the current model by 0.003 bits or more.
- **F52** The same A -> B.
- **F53** SIGN top-1 on the fixed test does not fall.
- **F54** Progress rule: F51, F52 and F53 hold.

## Results of the two-hundred-and-thirty-ninth set (added after the test; `predict_test239.py`, `results/predict_test239.md`, `famlm.py` f5k)

One held, three failed. The family 5-gram lowers S on the fixed test slightly (4.6354 -> 4.6312; F51) but raises it
A -> B (5.1927 -> 5.2014; F52 fails), and SIGN top-1 falls by less than 0.05 points (both 39.7% rounded; F53 fails):
the longer family context overfits. Not adopted. No progress: streak 2. Tally, counting parts: 1415 held, 1288 failed
(2702 registered).

# Two-hundred-and-fortieth set, registered before testing (25 September 2026): decipherment loop 65, the pictures check the grammar (three hypotheses)

Streak 2. If the grammatical analysis is right, grammatical signs (the endings 740 / 520, the post-ending markers 400
/ 90, closers, caged signs, numerals) carry no referent of their own, while lexical signs do. On pictured tablets, sign
pairs containing a grammatical sign should then go with more different pictures than pairs of two lexical signs.
Statistic: per pair recurring on 3+ objects, distinct pictures / occurrences; one-sided Mann-Whitney (rank test),
grammatical against lexical pairs. Disclosed: a design look at the individually made tablets (TAB:C, TAB:I) showed the
most picture-diverse pairs are ending / marker pairs (740 400, 740 90, 690 740, 100 740); the registered test there is
not independent of that look. The moulded tablets (TAB:B) were not looked at and are the test.

- **GV1** On the individually made tablets, grammatical pairs have higher picture diversity than lexical pairs (p < 0.05).
- **GV2** On the moulded tablets (TAB:B), the same (p < 0.05).
- **GV3** Progress rule: GV2 holds (the pictures independently confirm the grammar / lexicon split: tier 1 / 4).

## Results of the two-hundred-and-fortieth set (added after the test; `predict_test240.py`, `results/predict_test240.md`)

Two held, one failed. On the moulded tablets (TAB:B), not looked at before, sign pairs containing a grammatical sign
(ending, post-ending marker, closer, caged sign, numeral) go with more different pictures than pairs of two lexical
signs: 0.45 against 0.28 distinct pictures per occurrence (44 and 32 pairs; p = 0.001; GV2). On the individually
made tablets the direction is the same but weak (0.37 against 0.33, p = 0.29; GV1 fails). **Reading:** outside
evidence, the pictures, confirms the grammatical analysis from the other side: the signs the grammar calls endings,
markers and numerals carry no referent of their own, while pairs of content signs stay with one picture. Progress (a
new finding on an unseen sample): streak 0. Tally, counting parts: 1417 held, 1289 failed (2705 registered).

# Two-hundred-and-forty-first set, registered before testing (25 September 2026): decipherment loop 66, the pictures judge the closers and the count labels (four hypotheses)

Streak 0. Set 240: on moulded tablets grammatical pairs go with more pictures than lexical pairs. The same measure
(distinct pictures per occurrence of sign pairs recurring on 3+ moulded tablets, TAB:B) judges two grammatical claims
not checked from outside: the closers (predict_test103.CL) as alternative endings (sets 118-120), and the count-label
signs (set 215: A's ten commonest pre-count signs). Comparison group: pairs of two lexical signs (as set 240).

- **JC1** Pairs containing a closer (and no other grammatical sign) are more picture-diverse than lexical pairs
  (one-sided rank test, p < 0.05): the closers are grammatical.
- **JC2** Pairs containing a count-label sign (and no other grammatical sign) are more picture-diverse than lexical
  pairs (p < 0.05).
- **JC3** Pairs containing 740 or 520 are more picture-diverse than lexical pairs (replicating set 240 for the endings
  alone).
- **JC4** Progress rule: JC1 holds (outside evidence confirms the closers are grammatical, a claim so far internal).

## Results of the two-hundred-and-forty-first set (added after the test; `predict_test241.py`, `results/predict_test241.md`)

One held, three failed. (The first run stopped on an empty group; a guard reporting 'too few to test' was added.) No
closer pair recurs on 3+ moulded tablets, so the closers cannot be judged this way (JC1 fails). Count-label pairs are
less picture-diverse than lexical pairs, not more (0.16 against 0.30, 4 pairs; JC2 fails): if anything the label slot
holds content words, not grammar (not registered in that direction; noted). Pairs with 740 / 520 alone are more
picture-diverse (0.45 against 0.30, p = 0.011; JC3), replicating set 240 for the endings. No progress: streak 1. Tally,
counting parts: 1418 held, 1292 failed (2710 registered).

# Two-hundred-and-forty-second set, registered before testing (25 September 2026): decipherment loop 67, are the count labels content words? (three hypotheses)

Streak 1. Set 241 saw (4 pairs, not in the registered direction) count-label pairs on moulded tablets less
picture-diverse than lexical pairs. Registered now in that direction, on the samples not used there: the individually
made pictured tablets (TAB:C, TAB:I) and, as a second sample, seals (SEAL:S, SEAL:R, their field animal as picture).
Pairs containing one of A's ten commonest pre-count signs and no other grammatical sign, against pairs containing
740 / 520; picture diversity as set 240 (pairs on 3+ objects).

- **CL1** On the individually made tablets, count-label pairs are less picture-diverse than ending pairs (one-sided
  rank test, p < 0.05).
- **CL2** On seals, the same.
- **CL3** Progress rule: CL1 or CL2 holds with the other in the same direction (the count label is a content slot).

## Results of the two-hundred-and-forty-second set (added after the test; `predict_test242.py`, `results/predict_test242.md`)

None held. On the individually made tablets only 3 count-label pairs recur (mean diversity 0.25 against 0.40 for
ending pairs, not significant; CL1); on seals count-label and ending pairs are alike (0.39 against 0.37; CL2). Set
241's hint that the label slot holds content words does not replicate; the question stays open. No progress: streak
2. Tally, counting parts: 1418 held, 1295 failed (2713 registered).

# Two-hundred-and-forty-third set, registered before testing (25 September 2026): decipherment loop 68, referent phrases on moulded tablets (three hypotheses)

Streak 2. The phrase-level referent method (set 237) requires 2+ distinct texts per qualifying pair; on moulded
tablets (TAB:B) copies of one mould are one text, so distinct texts are independent designs and the requirement makes
them usable. Pairs on 3+ moulded tablets in 2+ distinct texts with one picture on 80%+; null: pictures shuffled among
objects, 1,000 times.

- **MR1** More pairs qualify than in 95% of shuffles.
- **MR2** At least three qualifying pairs are not already qualifying on the individually made tablets (set 237).
- **MR3** Progress rule: MR1 and MR2 hold; the new pairs' tokens on the moulded tablets used are added to the tier-1
  referent line.

## Results of the two-hundred-and-forty-third set (added after the test; `predict_test243.py`, `results/predict_test243.md`, `prizebench.referent_fixed`)

All three held. On the moulded tablets (308 pictured objects), 8 sign pairs recur in 2+ distinct texts (independent
designs) with one picture on 80%+, against a shuffle median of 0 (95th percentile 1; MR1), all new (MR2): 590 407,
255 436, 436 690, 440 740 = gharial; 806 158, 752 740, 798 740 = tree; 2 240 = one-horned bull. The tree phrase 806
158 contains the leaf sign 806, as the earlier notes proposed. The tier-1 referent line rises from 0.61% to 0.84% of
sign tokens. Progress: streak 0. Tally, counting parts: 1421 held, 1295 failed (2716 registered).

# Two-hundred-and-forty-fourth set, registered before testing (25 September 2026): decipherment loop 69, do fish names float free of the pictures? (three hypotheses)

Streak 0. Set 240: grammatical pairs go with many pictures, lexical pairs with one. Fish-headed names take the 520
class (sets 178, 196, 230) and are read by Parpola as star / deity names. If they name beings rather than depict the
scene, pairs containing a fish sign (FISH, signs.py) should be more picture-diverse than other lexical pairs. Measure
as set 240 (pairs on 3+ objects; distinct pictures per occurrence); comparison: pairs of two non-fish lexical signs.

- **FF1** On moulded tablets (TAB:B), fish pairs (no grammatical sign) are more picture-diverse than other lexical pairs
  (one-sided rank test, p < 0.05).
- **FF2** On the individually made tablets (TAB:C, TAB:I), the same direction.
- **FF3** Progress rule: FF1 holds with FF2 in the same direction.

## Results of the two-hundred-and-forty-fourth set (added after the test; `predict_test244.py`, `results/predict_test244.md`)

None held. Pairs with a fish sign are more picture-diverse than other lexical pairs in both samples, moulded tablets
(0.35 against 0.26; 8 and 24 pairs; p = 0.16; FF1) and individually made tablets (0.43 against 0.30; 6 and 17; p =
0.11; FF2), but neither is significant: the direction fits fish-headed names naming beings rather than the scene, the
samples are too small to show it. No progress: streak 1. Tally, counting parts: 1421 held, 1298 failed (2719
registered).

# Two-hundred-and-forty-fifth set, registered before testing (25 September 2026): decipherment loop 70, fish names and seal animals (two hypotheses)

Streak 1. Set 244 found fish pairs more picture-diverse than other lexical pairs on both tablet samples, not
significantly. Seals are a larger, unseen sample for this question (field animal as picture; SEAL:S, SEAL:R), with set
244's measure and comparison.

- **FS1** On seals, pairs with a fish sign (no grammatical sign) are more animal-diverse than other lexical pairs
  (one-sided rank test, p < 0.05).
- **FS2** Progress rule: FS1 holds (fish-headed names float free of the picture, replicated on an unseen sample).

## Results of the two-hundred-and-forty-fifth set (added after the test; `predict_test245.py`, `results/predict_test245.md`)

None held. On seals: - 67 against 64 pairs; means 0.39 and 0.40; rank difference +0.1; p = 0.4943. (FS1 fails). Seal animals are dominated by the one-horned bull, so pair diversity there is low
for fish and non-fish pairs alike; the tablet direction of set 244 does not replicate on seals. No progress: streak 2.
Tally, counting parts: 1421 held, 1300 failed (2721 registered).

# Two-hundred-and-forty-sixth set, registered before testing (25 September 2026): decipherment loop 71, phrases tied to what the object was for (three hypotheses)

Streak 2. Tier 1 names the object's function as outside evidence. The picture-referent method (validated on Linear B,
sets 234-235) with the object's class as the 'picture': seal, tablet, pottery (POT*), tag / sealing (TAG*), other.
Units: adjacent sign pairs on 3+ objects in 2+ distinct texts; a pair qualifies for a class if 80%+ of its objects
are of that class. Null: object classes shuffled among objects (F, all inscribed objects with text), 1,000 times.
Seals and tablets are the default classes; the question is the minority classes.

- **OF1** More pairs qualify for pottery, tags or other objects together than in 95% of shuffles.
- **OF2** At least two pairs qualify for pottery.
- **OF3** Progress rule: OF1 holds (phrases tied to an object's function; tier 1 evidence, reported beside V).

## Results of the two-hundred-and-forty-sixth set (added after the test; `predict_test246.py`, `results/predict_test246.md`)

Two held, one failed. Five sign pairs recur in 2+ distinct texts on 3+ objects of one minority class, against a
shuffle median of 0 (95th percentile 1; OF1): four on tags / sealings (2 48, 705 500, 55 220, 1 55) and one on pottery
(32 999); only one for pottery (OF2 fails). Caveat: tags carry seal impressions, so tag-only phrases may be the texts
of seals not recovered rather than words for the tag's function. Reported beside the tier-1 V line, not added to it.
Progress by the registered rule: streak 0. Tally, counting parts: 1423 held, 1301 failed (2724 registered).

**Withdrawn after set 247**: the four tag pairs are repeated impressions of two Lothal seals, counted as distinct
texts through partial transcriptions; only the pottery pair 32 999 remains, which does not meet the rule. No progress.

# Two-hundred-and-forty-seventh set, registered before testing (25 September 2026): decipherment loop 72, phrases tied to a site: toponym candidates (three hypotheses)

Streak 0. A place name or local title would recur at one site. The picture-referent method (validated on Linear B)
with the find site as the 'picture': units = adjacent sign pairs on 3+ objects in 2+ distinct texts (F, all inscribed
objects); a pair qualifies for a site if 80%+ of its objects come from it. Mohenjo-daro and Harappa are the default
sites; the question is the others (Dholavira, Lothal, Kalibangan, Chanhu-daro, ...). Null: sites shuffled among
objects, 1,000 times.

- **TS1** More pairs qualify for sites other than Mohenjo-daro and Harappa than in 95% of shuffles.
- **TS2** Qualifying pairs are found for at least two different minority sites.
- **TS3** Progress rule: TS1 holds (site-bound phrases: toponym or local-title candidates, checkable by find site).

## Results of the two-hundred-and-forty-seventh set (added after the test; `predict_test247.py`, `results/predict_test247.md`)

Two held, one failed. Four pairs are bound to a minority site, all Lothal (TS1 holds by its rule; TS2 fails, one
site): 2 48, 55 220, 705 500, 1 55. **Check after the test**: all four come from the Lothal sealings, many impressions
of two seals, 817 2 48 740 and 705 500 741 1 55 220 740 90, and the '2+ distinct texts' requirement was met only by
partial transcriptions of the same impressions (817 2 48 against 817 2 48 740). They are repeated impressions, not
toponyms or local titles. The same four pairs made set 246's 'tag' result. **Both sets' progress is withdrawn**:
set 246 (loop 71) keeps only its single pottery pair (32 999), which does not meet its rule, and set 247 (loop 72)
shows nothing. No progress: loop 71 streak 3, loop 72 streak 4. Lesson: distinct-text requirements must merge
transcriptions that are sub-strings of one another (the same object text read in part). Tally, counting parts: 1425
held, 1302 failed (2727 registered).

# Two-hundred-and-forty-eighth set, registered before testing (25 September 2026): decipherment loop 73, the grammar as a prior in the SIGN task (three hypotheses)

Streak 4. The grammar (grammar.parse5, learned parts from the training lines) parses real lines far more often than
shuffled ones. In the SIGN task each candidate's two-direction log-probability gets a bonus of lambda bits if the line
with the candidate parses. Design run on 300 lines of the training lines' own split: lambda 0 / 1 / 2 / 4 gives 40.1 /
40.4 / 40.7 / 40.6% top-1. Registered: lambda = 2.

- **GP1** SIGN top-1 on the fixed test with the grammar prior beats the task without it by 0.3 points or more.
- **GP2** The same A -> B (first 300 B lines; grammar learned from A).
- **GP3** Progress rule: GP1 and GP2 hold (the grammar prior enters the SIGN task; tier 7).

## Results of the two-hundred-and-forty-eighth set (added after the test; `predict_test248.py`, `results/predict_test248.md`)

One held, two failed. A 2-bit bonus for candidates that leave the line parseable raises SIGN top-1 only from 39.8% to
40.0% on the fixed test (below the registered 0.3 points; GP1 fails) and from 33.0% to 33.1% A -> B (GP2). The
grammar and the n-gram model largely know the same things. Not adopted. No progress: streak 5. Tally, counting parts:
1426 held, 1304 failed (2730 registered).

# Two-hundred-and-forty-ninth set, registered before testing (25 September 2026): decipherment loop 74, the marker 400 without an ending (three hypotheses)

Streak 5. 400 gets the role 'post-ending marker' only after an ending or closer. It also follows lexical signs
directly ('131 400', '137 400', '226 400', 'x x 400'). If such lines are names with the ending left out, the sign
before 400 should be head-like. Statistic as sets 223 / 236: mean head propensity of the sign directly before a 400
that follows a lexical sign (not an ending, closer, caged sign or numeral), against frequency-matched draws, 1,000
times.

- **ZF1** In A the sign before such a 400 is more head-like than frequency-matched draws (p < 0.05).
- **ZF2** The same in B's new lines.
- **ZF3** Progress rule: ZF1 and ZF2 hold; then that sign gets 'name head' and the 400 'post-ending marker' in R.

## Results of the two-hundred-and-forty-ninth set (added after the test; `predict_test249.py`, `results/predict_test249.md`)

None held. The sign directly before a 400 that follows no ending is not head-like: A - 77 tokens; mean propensity 0.084; p = 1.0000. (ZF1); B 27 tokens, mean
propensity 0.098, p = 0.92 (ZF2). Lines like '131 400' are not names with the ending left out; 400 after a lexical
sign stays unexplained. No progress: streak 6. Tally, counting parts: 1426 held, 1307 failed (2733 registered).

# Two-hundred-and-fiftieth set, registered before testing (25 September 2026): decipherment loop 75, a rule for 400 after a non-head (three hypotheses)

Streak 6. Set 249 found (in A, against its registered direction) that the sign before a 400 that follows no ending is
less head-like than chance. Grammar rule LOW-POST: a line of 1-2 lexical signs + 400 whose sign before 400 has head
propensity (A) below 0.05 (3+ occurrences). Design on A: margin 51.28 -> 51.51.

- **LP1** parse5 + LOW-POST raises the B margin (any rise) and real B coverage more than shuffled.
- **LP2** It raises the F margin.
- **LP3** Progress rule: LP1 holds.

## Results of the two-hundred-and-fiftieth set (added after the test; `predict_test250.py`, `results/predict_test250.md`, `grammar.parse6`)

All three held. LOW-POST (1-2 lexical signs + 400, the sign before 400 of low head propensity) raises the B margin
from 36.02 to 36.27 points, real B coverage more than shuffled (+0.37 against +0.13; LP1), and the F margin from 18.43
to 18.52 (LP2). A small gain, adopted in the metric's G margin: lines like '131 400' are a construction of their own,
a non-head sign with the marker. Progress: streak 0. Tally, counting parts: 1429 held, 1307 failed (2736 registered).

# Two-hundred-and-fifty-first set, registered before testing (25 September 2026): decipherment loop 76, two small rules (three hypotheses)

Streak 0. From the A lines the grammar still misses: SINGLE-DOUBLE, one lexical sign + a doubled lexical sign ('117
615 615', '142 615 615'; set 187's edge doubling when the rest is a single sign); 550-END, lexical signs + 550 + 525 /
526 ('220 550 525', '233 550 526'). Design on A: margin 51.51 -> 51.62 and 51.68.

- **TR1** parse6 + both rules raises the B margin (any rise) and real B coverage more than shuffled.
- **TR2** It raises the F margin.
- **TR3** Progress rule: TR1 holds.

## Results of the two-hundred-and-fifty-first set (added after the test; `predict_test251.py`, `results/predict_test251.md`, `grammar.parse7`)

None held. SINGLE-DOUBLE and 550-END do not generalise: B - margin 36.27 -> 36.08; real +0.15, shuffled +0.34 points. (TR1 fails); F margin 18.52 -> 18.37 (TR2 fails). The A
gains were fitted to A's lines. Not adopted. No progress: streak 1. Tally, counting parts: 1429 held, 1310 failed
(2739 registered).

# Two-hundred-and-fifty-second set, registered before testing (25 September 2026): decipherment loop 77, does a sign's drawing match the object's picture? (six hypotheses)

Streak 1. Owner's question: can checked meaning (tier 1, strict V) grow? A sign-level check: a sign that depicts X on
an object that shows X. Drawing classes fixed now from the descriptions, before any sign-picture count: PLANT = Parpola
description families leaf, leave, half-leave, tree, plant, branching, plus Fairservis 'plant'; FISH = signs.FISH;
PERSON = families person, people, plus Fairservis 'human'; ANIMAL = families deer, animal, cow', cat', plus Fairservis
'animal'. Matching pictures: PLANT - Phyt, Pipal; FISH - Fish; PERSON - Anth; ANIMAL - any quadruped motif (Bult,
Bull, Bull1, Bull2, Gaur, Goat, Elep, Rhin, Hare, Buff, Zebu, Tigr, Mult). Unit: distinct text (part-texts merged as
predict_test237.merged) with its modal picture; statistic: share of matching-picture texts that contain a class sign
against the share among other pictured texts (one-sided Fisher). Two independent samples: individually made tablets
(TAB:C, TAB:I) and moulded tablets (TAB:B).

- **PC1** PLANT signs are more frequent in tree / pipal texts, in both samples (p < 0.05 each).
- **PC2** FISH signs in fish texts, both samples.
- **PC3** PERSON signs in anthropomorph texts, both samples.
- **PC4** ANIMAL signs in quadruped texts, both samples.
- **PC5** At least one class holds in one sample and in the other at p < 0.10 (reported).
- **PC6** Progress rule: any of PC1-PC4 holds; the signs of that class enter strict V as depiction-checked meanings
  (their tokens counted, as the copper-tablet anchors are).

## Results of the two-hundred-and-fifty-second set (added after the test; `predict_test252.py`, `results/predict_test252.md`)

None held. A sign's drawing does not match the picture on its object. Fish signs are, if anything, rarer on texts with
a fish picture (individually made 1 of 12 against 21 of 61; moulded 1 of 6 against 28 of 121; PC2); human-figure and
animal signs show no match either (PC3, PC4); plant signs come closest, on moulded tablets only (10 of 19 tree texts
against 34 of 108, p = 0.066; the individually made tablets have 2 tree texts; PC1). **Reading:** the texts do not
name what the object shows by drawing it; the text-picture link found in sets 233-243 is lexical (a whole text or
phrase goes with a picture), not pictographic. This closes the most direct route to sign-level checked meaning with
the material at hand: strict V stays 0.008%. No progress: streak 2. Tally, counting parts: 1429 held, 1316 failed
(2745 registered).

# Two-hundred-and-fifty-third set, registered before testing (25 September 2026): decipherment loop 78, the main findings on the damaged texts (six hypotheses)

Streak 2. The full ICIT export was in use all along (correction of 25 Sept); the analyses used only its clean texts.
Sample D (`damaged.py`): the legible runs of 2+ signs in the 1,999 damaged texts, cut at gaps, runs found intact inside
any clean text dropped as copies: 435 runs, 1,501 signs, 427 objects, never used by any test so far. Only relations
inside a run are used (an open end means the neighbour is unknown). Re-tests:

- **DM1** Order is predictable: bits per interior sign under the clean-data model (famlm, MODEL, trained on all clean
  distinct lines) are lower for D runs than for the same runs shuffled within themselves (20 shuffles, paired sign test
  over runs, p < 0.05).
- **DM2** The cage: caged signs with a following sign inside the run are followed by 740 / 520 in 5% of cases or fewer.
- **DM3** Stroked jars (741, 742, 745) are followed by another sign inside the run more often than the plain jar 740
  (one-sided Fisher p < 0.05).
- **DM4** Fish heads take 520 more often than other identified heads (sign directly before 740 / 520 inside a run;
  set 178 depiction classes; one-sided Fisher p < 0.05).
- **DM5** Signs directly before a numeral run inside a run are concentrated like the count label (top-ten share above
  95% of 1,000 within-run shuffles).
- **DM6** Progress rule: none of these moves a bench component; all holding is consistency evidence on a new sample,
  recorded as such (no progress unless a component moves).

## Results of the two-hundred-and-fifty-third set (added after the test; `predict_test253.py`, `results/predict_test253.md`, `damaged.py`)

Five held, one failed (by design). On sample D (435 independent legible runs of the damaged texts, 1,501 signs, never
used before): order is predictable, real runs beating their shuffles under the clean-data model in 219 of 299 runs (p
= 2e-16; DM1); caged signs are not followed by 740 / 520 (0 of 3, too few to weigh; DM2); stroked jars are followed by
another sign far more often than the plain jar (32 of 39 against 29 of 90; DM3); fish heads take 520 (5 of 9 against 0
of 24; DM4); the slot before a count is concentrated (43.3% against a shuffle 95th percentile of 38.0%; DM5). The main
findings replicate on a third independent sample. Consistency evidence only (DM6): no bench component moves, streak
3. Of the damaged texts' 1,177 legible runs, 742 are copies of clean texts, which is why D is small. Tally, counting
parts: 1434 held, 1317 failed (2751 registered).

# Two-hundred-and-fifty-fourth set, registered before testing (25 September 2026): decipherment loop 79, the referent method with the pictured fragments (three hypotheses)

Streak 3. The tier-1 referent line (0.76%) counts texts and sign pairs whose picture is fixed on individually made
tablets (TAB:C, TAB:I) and across distinct moulded designs (TAB:B), clean texts only. The damaged tablets with a
picture add their legible runs: each damaged object contributes its runs joined by a separator, so no pair crosses a
gap. Qualification exactly as sets 237 / 243 with part-texts merged (predict_test237.merged, qual); nulls: pictures
shuffled among objects, 1,000 times, per pool.

- **RD1** With the fragments added, more pairs qualify in each pool than in 95% of its shuffles.
- **RD2** At least three pairs qualify that did not qualify with clean texts alone (both pools together).
- **RD3** Progress rule: RD1 and RD2 hold and the tier-1 referent line (computed as before on the clean distinct lines,
  now with the enlarged pair lists) rises.

## Results of the two-hundred-and-fifty-fourth set (added after the test; `predict_test254.py`, `results/predict_test254.md`, `prizebench.referent_fixed`)

All three held. Adding the pictured damaged tablets (31 individually made, 51 moulded; legible runs only, no pair
across a gap) leaves the referent pairs far above their shuffle nulls in both pools (RD1) and adds 4 pairs (RD2): 636
740 and 240 636 = bull, 740 790 = goat (individually made), 318 920 = gharial (moulded). The script's own line
(0.88% -> 0.96%) marked pairs on any tablet line; computed as the bench does it (each pool's pairs on its own tablets,
'as before' in RD3), the tier-1 referent line rises from 0.76% to 0.79% (27 texts and pairs). Progress: streak 0.
Tally, counting parts: 1437 held, 1317 failed (2754 registered).

# Two-hundred-and-fifty-fifth set, registered before testing (25 September 2026): decipherment loop 80, blind restoration of illegible signs checked on the CISI photographs (four hypotheses)

Streak 0. A check against outside evidence that needs no language: the SIGN model predicts each illegible sign (ICIT
000) that stands alone inside a line with intact edges and legible neighbours (79 cases), and the predictions are
checked on Parpola's photographs (CISI vol. 1, Collections in India, 1987; the owner's scan). Protocol: (1) the
predictions (top 5 of the 150 commonest clean signs, two-direction model, trained on all clean distinct lines) are
written to `results/restoration_predictions.tsv` by `restore.py` without being displayed, and committed, so their hash
fixes them before any photograph is read; (2) the photographs are read for the gap sign and recorded in
`results/restoration_readings.tsv` (ICIT number, or 'illegible') without the predictions in view; (3) a script compares
them. Only objects whose photograph is in CISI vol. 1 and whose gap sign is legible on it count.

- **RS1** Top-1 predictions match the photo reading in 25% or more of the readable cases (at least 10 readable).
- **RS2** Top-5 predictions contain the photo reading in 50% or more.
- **RS3** Top-1 beats the frequency baseline (the commonest clean sign) on the same cases.
- **RS4** Progress rule: RS1 and RS3 hold (frozen predictions confirmed by outside evidence; tier 3 gains its first
  line, 'blind restorations confirmed').

## Results of the two-hundred-and-fifty-fifth set (added after the test; `predict_test255.py`, `results/predict_test255.md`, `results/restoration_readings.tsv`)

All four failed, for lack of evidence rather than by a wrong prediction. Of the 79 gaps, 15 are on objects in CISI
vol. 1; 14 were examined on the owner's scan (H-28's page was not located), including 400-dpi crops of M-61 and M-62.
None of the gap signs can be identified: the objects are broken across the text (M-167, M-168), worn (K-31, L-78,
M-477, C-33), corroded (C-40), overlapped (K-88) or too small in the photograph (H-246, H-291), which is why ICIT
marks them illegible from the same plates. With no readable case the frozen predictions were never compared with
anything (RS1-RS3 need 10 readable), and they stay unread and committed for a later check on better photographs or
the objects. The scan's resolution, not the model, is the blocker. Progress: none (streak 1). Tally, counting parts:
1437 held, 1321 failed (2758 registered).

# Two-hundred-and-fifty-sixth set, registered before testing (25 September 2026): decipherment loop 81, WORD task with names composed by the head-final grammar (four hypotheses)

Streak 1. The WORD task (tier 6) ranks only name bodies seen whole in training, so at most 54 of the 232 held-out
names can be found (measured before registering; composing modifier sequences and heads seen 3+ times raises that
ceiling to 82, also measured). The ranking itself has not been run. Candidates: the training bodies plus every
modifier sequence (a body minus its head, seen 3+ times) joined to every head seen 3+ times; control: the same parts
head first. Same model (MODEL), same split, scored on the whole line as in `prizebench.word_task` (`predict_test256.py`).

- **WR1** WORD top-10 rises by 1 point or more with the composed names (from the seen-only ranking in the same run).
- **WR2** At least 3 test names never seen whole in training reach the top 10.
- **WR3** Head-final composition beats the head-first control, both in top-10 hits and in never-seen hits.
- **WR4** Progress rule: WR1 and WR3 hold (the WORD component then uses composed candidates).

## Results of the two-hundred-and-fifty-sixth set (added after the test; `predict_test256.py`, `results/predict_test256.md`)

All four failed. 2,657 names composed from 39 modifier sequences and 73 heads (each seen 3+ times) join the 895 seen
bodies; the same 8 of 232 held-out names reach the top 10 with or without them, and with the head-first control (2,762
candidates) as well. No composed name reaches any top 10 (WR2), so the grammar's head-final shape, which holds as
structure (sets 176-177), gives the model no purchase on which unseen names occur: the scorer's context around the body
(heading, ending) is too weak to prefer a rare new body over frequent seen ones. The WORD task stays bounded by
seen bodies. Progress: none (streak 2). Tally, counting parts: 1437 held, 1325 failed (2762 registered).

# Two-hundred-and-fifty-seventh set, registered before testing (25 September 2026): decipherment loop 82, an infill component for the SIGN task (four hypotheses)

Streak 2. The SIGN task (tier 7) scores a hidden sign as a product of a left-to-right and a right-to-left model (set
204); neither sees both neighbours at once. The infill probability p(c | left, right), counted on the training lines
with line edges as neighbours and smoothed toward the sign's frequency, is added with weight alpha, chosen on a
development split of the training lines only (alpha in 0-3), then applied once to the fixed test lines
(`predict_test257.py`). Not measured before registering.

- **IF1** SIGN top-1 rises by 0.5 point or more on the test lines.
- **IF2** SIGN top-5 does not fall.
- **IF3** The development split gives the infill a positive weight (alpha > 0).
- **IF4** Progress rule: IF1 and IF2 hold (the SIGN task then uses the infill scorer).

## Results of the two-hundred-and-fifty-seventh set (added after the test; `predict_test257.py`, `results/predict_test257.md`)

Two held, two failed. The development split gives the infill a small weight (alpha 0.25: top-1 40.7% -> 40.9%; larger
weights hurt), IF3 holds. On the 2,340 test signs top-1 falls 39.9% -> 39.4% (IF1 fails) and top-5 rises 61.8% ->
62.2% (IF2 holds). The two-direction model (set 204) already carries what the immediate neighbours say; counting the
exact left-right frame adds noise on 3,000 lines. (The two-direction baseline here, 39.9%, differs from the bench's
39.7% only by tie order among equal scores.) Progress: none (streak 3). Tally, counting parts: 1439 held, 1327 failed
(2766 registered).

# Two-hundred-and-fifty-eighth set, registered before testing (25 September 2026): decipherment loop 83, the frozen restorations against Parpola's own transcription (three hypotheses)

Streak 3. Set 255 could not read the gap signs on the CISI vol. 1 photographs. Parpola's own transcription (the CISI
digitisation, `cisi.py`, M-1 to M-184) covers 4 of the 79 gaps: M-167 is illegible there too (P000), M-168 is absent,
and two carry a reading: M-62 position 2 = P310 = ICIT 700 (no uncertainty marked; ICIT reads the line 551 ??? 550 741
32 226, Parpola 550 700 550 741 2 226) and M-61 position 6 = P251 = ICIT 81 / 82 / 958 (90% uncertainty). These
readings were looked up before registering; the frozen predictions (`results/restoration_predictions.tsv`, committed
in 002427952) are still unread (`predict_test258.py`).

- **RC1** M-62: ICIT 700 is in the top 5.
- **RC2** M-61: one of ICIT 81 / 82 / 958 is in the top 5.
- **RC3** Progress rule: not applicable; two cases are consistency evidence only (set 255 required 10). Recorded as failing.

## Results of the two-hundred-and-fifty-eighth set (added after the test; `predict_test258.py`, `results/predict_test258.md`)

All three failed. Opened for the first time, the frozen predictions miss both of Parpola's readings: M-62's gap is 700
in CISI (certain), predicted 840 60 2 233 3; M-61's is 81 / 82 / 958 (uncertain), predicted 585 923 740 798 176. Two
cases prove little either way (at the SIGN task's 62% top-5, missing both happens about 1 time in 7), but the only outside
check the restoration predictions have met is a miss. The M-62 line also shows how the transcriptions differ elsewhere
(ICIT 551 ... 32, Parpola 550 ... 2): gap filling inherits transcription noise. Progress: none (streak 4). Tally,
counting parts: 1439 held, 1330 failed (2769 registered).

# Two-hundred-and-fifty-ninth set, registered before testing (25 September 2026): decipherment loop 84, an anti-cache for non-adjacent repeats (four hypotheses)

Streak 4. Signs repeat non-adjacently inside a line less often than shuffles produce (DB6, DN6, HX14), which the
n-gram model cannot see beyond its window. At each sign position the probability of a sign already written earlier in
the line (other than the immediately preceding sign) is multiplied by gamma and the distribution renormalised. A
design run on the training lines' own split gave 4.6772 -> 4.6736 at gamma 0.5 (0.4: 4.6737, 0.3: 4.6745); gamma is
fixed at 0.5 (`predict_test259.py`). For SIGN, a candidate written elsewhere in the line, not adjacent, takes log gamma.

- **AC1** S on the fixed test falls by 0.002 bits or more.
- **AC2** The same A -> B (any fall).
- **AC3** SIGN top-1 does not fall.
- **AC4** Progress rule: AC1, AC2 and AC3 hold.

## Results of the two-hundred-and-fifty-ninth set (added after the test; `predict_test259.py`, `results/predict_test259.md`)

All four failed. The anti-cache that helped on the design split (0.0036 bits) raises S on the fixed test (4.6354 ->
4.6369), raises it more A -> B (5.1927 -> 5.2104) and lowers SIGN top-1 (39.7% -> 39.6%). The avoidance of
non-adjacent repeats is real as a corpus statistic (DB6, DN6, HX14) but too weak and uneven to predict with: repeated
signs that do occur (numerals, doubled heads, 740 in stacked endings) are penalised with the rest. Second design-split
gain that did not survive (after f5k, set 239): design runs on the training split overstate small S gains. Progress:
none (streak 5). Tally, counting parts: 1439 held, 1334 failed (2773 registered).

# Two-hundred-and-sixtieth set, registered before testing (25 September 2026): decipherment loop 85, a head + modifier frame before closers (four hypotheses)

Streak 5. The roles component leaves 1,901 tokens unassigned; 408 are in closer lines, where the sign before the closer
was found to be a name head (FX13 67%, CB1), but `progress.roles` never gave it a role. If closer lines share the name's
head-final frame, the pre-closer sign is head-class and the signs before it behave as modifiers. Head class H = signs
heading 5+ A names more often than they modify (as parse2). Closer lines: genre 'closer', 3+ signs, heading unit set
aside; lexical signs only (`predict_test260.py`). Not measured before registering.

- **CH1** A: the pre-closer sign is head-class more often than the earlier body signs (Fisher one-sided, p < 0.05).
- **CH2** B (M77 additions, heads from A): the same.
- **CH3** A: earlier body signs are head-class no more than name modifiers are, plus 10 points.
- **CH4** Progress rule: CH1-CH3 hold; `roles` then gives pre-closer signs 'name head' and earlier body signs 'name modifier'.

## Results of the two-hundred-and-sixtieth set (added after the test; `predict_test260.py`, `results/predict_test260.md`)

Two held, two failed. On A the sign before a closer is head-class more often than the earlier body signs (25 of 96,
26%, against 24 of 233, 10%; p = 0.0004; CH1), and the earlier signs are head-class about as rarely as name modifiers
(10% against 7%; CH3). On B the difference is gone (7 of 48, 15%, against 16 of 121, 13%; p = 0.5; CH2 fails). With
the strict head class (5+ heads, more often head than modifier) only a quarter of pre-closer signs qualify, far below
FX13's 67% (any sign that ever heads a name): closers take mostly their own preceding signs (FX7), not the 740 heads.
The name frame does not transfer to closer lines on the evidence of B; `roles` unchanged. Progress: none (streak 6).
Tally, counting parts: 1441 held, 1336 failed (2777 registered).

# Two-hundred-and-sixty-first set, registered before testing (25 September 2026): decipherment loop 86, three grammar rules for unparsed lines (four hypotheses)

Streak 6. LOW-POST's grammar (parse6) leaves 831 of 2,722 A lines unparsed; 53 of them end in 740, blocked by a caged
sign, a 400 / 90 or a second ending inside the line (looked at before registering; margins not measured). Three rules,
each scored by the G margin over within-line shuffles (`predict_test261.py`): CAGE-OPEN (a caged sign opens the line and
the rest parses as a name), MID-POST (1-3 lexical signs, 400 / 90, then a rest that parses), NAME-NAME (a name followed
by a second name). SEQ (set 192) showed that splitting rules can parse shuffles as well as real lines; the margin
decides.

- **GR1** CAGE-OPEN raises the margin on A by 0.3 point or more and raises it on B.
- **GR2** MID-POST, the same.
- **GR3** NAME-NAME, the same.
- **GR4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-first set (added after the test; `predict_test261.py`, `results/predict_test261.md`, `grammar.parse8`)

Two held, two failed. CAGE-OPEN raises the G margin on A (47.6 -> 47.9) and on B (36.3 -> 36.5): a caged sign opening a
line before a name (226 31 740, 232 48 740, 466 705 760 740) is a real frame, not a shuffle artefact, and fits set 184
(the cage marks a unit in place of the ending): a caged unit can stand before a name as well as alone. MID-POST (A 47.2,
B 35.9) and NAME-NAME (A 47.3, B 36.9) lower the A margin: splitting rules parse shuffled lines as readily as real ones
(as SEQ did in set 192). The grammar becomes parse8 = parse6 + CAGE-OPEN; `progress.grammar_margin` uses it. Progress:
G margin rises (streak 0). Tally, counting parts: 1443 held, 1338 failed (2781 registered).

# Two-hundred-and-sixty-second set, registered before testing (25 September 2026): decipherment loop 87, three more grammar rules for unparsed lines (four hypotheses)

Streak 0. Same method as set 261, on the lines parse8 leaves unparsed (their last signs include 400, 368, 31, 407, 2,
220, 615, 595; many are two-sign lines whose last sign heads names too rarely for G2's bare rule). Rules, each scored by
the G margin on A and B (`predict_test262.py`): END-PRONE (lexical body + a sign ending 50%+ of its 5+ A occurrences),
CLOSER-740 (lexical body + closer + 740), TWO-BARE (two lexical signs, the second a name head at least once in A).
Margins not measured before registering.

- **GE1** END-PRONE raises the margin on A by 0.3 point or more and raises it on B.
- **GE2** CLOSER-740, the same.
- **GE3** TWO-BARE, the same.
- **GE4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-second set (added after the test; `predict_test262.py`, `results/predict_test262.md`, `grammar.parse9`)

Two held, two failed. Ten signs end half or more of their 5+ A occurrences without being endings or closers (405 407
526 298 215 423 64 137 136 155). END-PRONE (lexical body + one of them) raises the A margin 47.94 -> 48.31 and the B
margin 36.47 -> 36.48: GE1 holds as registered, but the B replication is 0.01 point, so the rule is adopted as weak (on
B the end-prone signs close as many shuffled lines as real ones). CLOSER-740 lowers both margins (47.83, 36.37) and
TWO-BARE raises B (36.59) but A only 0.02 point: both rejected. The grammar becomes parse9 = parse8 + END-PRONE (the
end-prone set learned from A); `progress.grammar_margin` uses it. Progress: G margin A rises (streak 0). Tally, counting
parts: 1445 held, 1340 failed (2785 registered).

# Two-hundred-and-sixty-third set, registered before testing (25 September 2026): decipherment loop 88, three more grammar rules for unparsed lines (four hypotheses)

Streak 0. Same method as sets 261-262, on the lines parse9 leaves unparsed (`predict_test263.py`): NUM-END (1-2 lexical
signs, then a numeral run ending the line: a label written after its count), BODY-400 (3+ lexical signs + 400; LOW-POST
covers only 1-2), HEADING-BODY (the heading unit, then any lexical body). Margins not measured before registering.

- **GN1** NUM-END raises the margin on A by 0.3 point or more and raises it on B.
- **GN2** BODY-400, the same.
- **GN3** HEADING-BODY, the same.
- **GN4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-third set (added after the test; `predict_test263.py`, `results/predict_test263.md`, `grammar.parse10`)

Three held, one failed. BODY-400 (3+ lexical signs + 400) raises the margin A 48.31 -> 48.66, B 36.48 -> 36.65: 400
closes a longer body as it closes one or two signs (LOW-POST, set 250), so 400 is a line-final marker in its own right
and not only a post-ending sign. HEADING-BODY (heading unit + lexical body) raises A to 48.85, B to 36.75: the heading
opens lines without a name ending too. Together A 49.21, B 36.92 (GN4). NUM-END (a label written after its count)
lowers both margins (46.68, 34.75): numerals do not close lines after a label; the order is count then label (set 215).
The grammar becomes parse10; `progress.grammar_margin` uses it. Progress: G margin rises (streak 0). Tally, counting
parts: 1448 held, 1341 failed (2789 registered).

# Two-hundred-and-sixty-fourth set, registered before testing (25 September 2026): decipherment loop 89, three more grammar rules for unparsed lines (four hypotheses)

Streak 0. Same method (sets 261-263), on the 774 A lines parse10 leaves unparsed, mostly all-lexical lines of 2-4 signs
and short count-like lines (`predict_test264.py`): LABEL-ANY (any lexical sign + numeral run + 0-2 lexical signs; the
LABEL-COUNT rule allows only A's ten commonest labels), NAME-TAIL (a name + exactly one lexical sign), OPEN-PRONE (2+
lexical signs, the first opening 50%+ of its 5+ A occurrences, the last heading an A name at least once). Margins not
measured before registering.

- **GL1** LABEL-ANY raises the margin on A by 0.3 point or more and raises it on B.
- **GL2** NAME-TAIL, the same.
- **GL3** OPEN-PRONE, the same.
- **GL4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-fourth set (added after the test; `predict_test264.py`, `results/predict_test264.md`, `grammar.parse11`)

Two held, two failed. OPEN-PRONE (2+ lexical signs, the first an opening-prone sign, the last a name head) raises the
margin A 49.21 -> 49.64, B 36.92 -> 37.39: short lexical lines are framed at both edges, an opening sign and a head,
even without an ending. LABEL-ANY lowers both margins (47.73, 35.27): only the frequent labels stand before counts (as
set 215 found), and NAME-TAIL lowers them sharply (43.90, 33.16): nothing but 400 / 90 follows a name. The grammar
becomes parse11; `progress.grammar_margin` uses it. Progress: G margin rises (streak 0). Tally, counting parts: 1450
held, 1343 failed (2793 registered).

# Two-hundred-and-sixty-fifth set, registered before testing (25 September 2026): decipherment loop 90, three more grammar rules for unparsed lines (four hypotheses)

Streak 0. Same method (sets 261-264), on the lines parse11 leaves unparsed; some end in heading signs (820, 861), as if
read the wrong way (`predict_test265.py`): REVERSED (the line read backwards parses: a direction slip in writing or in
the transcription; shuffles are as likely to parse backwards as forwards, so only real reversed lines raise the
margin), BARE-2 (2+ lexical signs, the last heading 2+ A names and heading more often than modifying; G2's bare rule
needs 5+ and TWO-BARE, 1+, failed in set 262), ENDP-POST (lexical body + an end-prone sign + 400 / 90). Margins not
measured before registering.

- **GV1** REVERSED raises the margin on A by 0.3 point or more and raises it on B.
- **GV2** BARE-2, the same.
- **GV3** ENDP-POST, the same.
- **GV4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-fifth set (added after the test; `predict_test265.py`, `results/predict_test265.md`)

All four failed. REVERSED (accept a line if it parses read backwards) lowers the margin sharply (A 49.64 -> 32.04, B
37.39 -> 21.07): read backwards, shuffled lines parse far more often than real ones, so real lines almost never parse
in reverse. The grammar is strongly directional, which confirms the corpus's reading order, and no direction slips are
recoverable this way. BARE-2 lowers both margins slightly (49.52, 37.32); ENDP-POST parses no new line (49.64, 37.39).
Progress: none (streak 1). Tally, counting parts: 1450 held, 1347 failed (2797 registered).

# Two-hundred-and-sixty-sixth set, registered before testing (25 September 2026): decipherment loop 91, three more grammar rules for unparsed lines (four hypotheses)

Streak 1. Same method (sets 261-265), on the lines parse11 leaves unparsed (`predict_test266.py`): COUNT-3 (a numeral
run, then exactly 3 lexical signs; COUNT allows at most 2), HEAD-COUNT (the heading unit, then a count), CAGE-MID (1+
lexical signs, a caged sign, then a name: CAGE-OPEN, set 261, with material before the cage). Margins not measured
before registering.

- **GW1** COUNT-3 raises the margin on A by 0.3 point or more and raises it on B.
- **GW2** HEAD-COUNT, the same.
- **GW3** CAGE-MID, the same.
- **GW4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-sixth set (added after the test; `predict_test266.py`, `results/predict_test266.md`)

All four failed. COUNT-3 lowers both margins (A 49.41, B 37.04): a count takes at most two signs after it, as COUNT
already says. HEAD-COUNT parses no line the grammar does not already parse (the heading before a count is covered).
CAGE-MID raises A by 0.10 and B by 0.01 point, below the threshold: the cage opens lines, and rarely stands inside them.
Progress: none (streak 2). Tally, counting parts: 1450 held, 1351 failed (2801 registered).

# Two-hundred-and-sixty-seventh set, registered before testing (25 September 2026): decipherment loop 92, roles from the new grammar rules (four hypotheses)

Streak 2. Sets 262-264 added frames whose edge signs have a fixed job the roles component does not count: end-prone
signs close lines (END-PRONE), opening-prone signs open them (OPEN-PRONE), 400 closes a lexical body (BODY-400). The
sign sets were learned from A; the roles are adopted only if the behaviour replicates on B's new lines
(`predict_test267.py`; `progress.roles(edges=True)`: line-final end-prone sign = 'end-prone closer', line-initial
opening-prone sign = 'opener', line-final 400 = 'line-final 400', each only where no earlier role applies).

- **RL1** B: the end-prone signs end 50%+ of their occurrences.
- **RL2** B: the opening-prone signs open 50%+ of their occurrences.
- **RL3** B: 400 is line-final in 80%+ of its occurrences.
- **RL4** Progress rule: RL1-RL3 hold and R rises; `roles` then uses the edge roles.

## Results of the two-hundred-and-sixty-seventh set (added after the test; `predict_test267.py`, `results/predict_test267.md`, `progress.roles(edges=True)`)

All four held. The edge behaviours learned from A replicate on B's new lines: the 10 end-prone signs end 53% of their
122 B occurrences (RL1), the 36 opening-prone signs open 61% of their 344 (RL2), and 400 is line-final in 89% of its
92 (RL3). Given roles where no earlier role applies (end-prone closer 56 tokens, opener 135, line-final 400 40), R rises
84.2% -> 86.1%. (A first run read the baseline as 84.5% because the 400 role was not switched off with the option;
fixed before recording.) Progress: R rises (streak 0). Tally, counting parts: 1454 held, 1351 failed (2805 registered).

# Two-hundred-and-sixty-eighth set, registered before testing (25 September 2026): decipherment loop 93, a grammar prior for the SIGN task (four hypotheses)

Streak 0. The grammar (parse11, sets 250-264) and the SIGN model (set 204) have been built separately. Here each SIGN
candidate gains alpha (in log-probability) if the line it completes parses; the grammar's frames and sign sets are
learned from the training lines only, and alpha (0-3) is chosen on a development split of them, then applied once to
the fixed test lines (`predict_test268.py`). Not measured before registering.

- **GP1** SIGN top-1 rises by 0.5 point or more on the test lines.
- **GP2** SIGN top-5 does not fall.
- **GP3** The development split gives the grammar prior a positive weight (alpha > 0).
- **GP4** Progress rule: GP1 and GP2 hold (the SIGN task then uses the grammar prior).

## Results of the two-hundred-and-sixty-eighth set (added after the test; `predict_test268.py`, `results/predict_test268.md`)

Two held, two failed. The development split takes the largest grammar-prior weight offered (alpha 3: top-1 40.7% ->
41.0%; GP3), but on the 2,340 test signs top-1 moves 39.9% -> 39.8% (GP1 fails) and top-5 61.8% -> 62.1% (GP2 holds).
The grammar's frames are edge and ending constraints the two-direction model already encodes (its position and end
components); knowing that a line parses adds nothing at the top rank. Third SIGN component in a row to fail (sets 257,
259, 268): the SIGN task is near what these data give a local model. (A first run ended without writing its report;
rerun unchanged.) Progress: none (streak 1). Tally, counting parts: 1456 held, 1353 failed (2809 registered).

# Two-hundred-and-sixty-ninth set, registered before testing (25 September 2026): decipherment loop 94, three numeral rules for unparsed lines (four hypotheses)

Streak 1. Same method (sets 261-266), on the 734 A lines parse11 leaves unparsed, many with a numeral inside
(`predict_test269.py`): NUM-INFIX (1 lexical sign, a numeral run, then a sign that heads an A name), OPEN-NUM (an
opening-prone sign, a numeral run, 0-1 lexical signs), MULTI-COUNT (2+ consecutive count units, each a numeral run + 1
lexical sign). Margins not measured before registering.

- **GX1** NUM-INFIX raises the margin on A by 0.3 point or more and raises it on B.
- **GX2** OPEN-NUM, the same.
- **GX3** MULTI-COUNT, the same.
- **GX4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-sixty-ninth set (added after the test; `predict_test269.py`, `results/predict_test269.md`)

All four failed. NUM-INFIX lowers both margins (A 49.48, B 37.09); OPEN-NUM raises A by 0.15 but lowers B (37.34);
MULTI-COUNT lowers A (49.54) though it raises B (37.53). None meets both conditions. The numerals inside the remaining
short lines do not follow a frame that shuffled lines lack. Progress: none (streak 2). Tally, counting parts: 1456
held, 1357 failed (2813 registered).

# Two-hundred-and-seventieth set, registered before testing (25 September 2026): decipherment loop 95, head roles inside the new frames (five hypotheses)

Streak 2. Two frames adopted today end in a lexical sign whose job is not yet a role: the last sign of an OPEN-PRONE
line (set 264) and the sign before 400 in a BODY-400 line (set 263). If each is a name head, it is head-class (H:
heads 5+ A names, more often head than modifier) more often than the signs before it (opener excluded). Set 260's
closer-line version held on A and failed on B; B decides (`predict_test270.py`). Not measured before registering.

- **RH1** A OPEN-PRONE: the last sign is head-class more often than the earlier signs (Fisher one-sided, p < 0.05).
- **RH2** B OPEN-PRONE: the same.
- **RH3** A BODY-400: the sign before 400 is head-class more often than the earlier signs.
- **RH4** B BODY-400: the same.
- **RH5** Progress rule: a frame that holds on A and B gives that sign the 'name head' role in `progress.roles`.

## Results of the two-hundred-and-seventieth set (added after the test; `predict_test270.py`, `results/predict_test270.md`)

One held, four failed. OPEN-PRONE lines of 3+ signs are few (A 16, B 21): the last sign is head-class on B (8 of 21
against 2 of 39 earlier signs, p = 0.002; RH2) but not on A (2 of 16 against 2 of 29, p = 0.45; RH1 fails). In
BODY-400 lines the sign before 400 is never head-class (A 0 of 12, B 0 of 4; RH3, RH4 fail): as LOW-POST (set 250)
found for short lines, 400 follows signs that are not name heads, so a lexical body + 400 is not a name. No new role.
Progress: none (streak 3). Tally, counting parts: 1457 held, 1361 failed (2818 registered).

# Two-hundred-and-seventy-first set, registered before testing (25 September 2026): decipherment loop 96, two-sign lines (four hypotheses)

Streak 3. The largest group of lines parse11 leaves unparsed is two-sign lexical lines whose signs have headed names (54
'h h' in A); BARE-2 and TWO-BARE (sets 262, 265) failed with loose head tests. Stricter frames (`predict_test271.py`;
strict head H = heads 5+ A names, more often head than modifier): HH-STRICT (two strict heads), OPEN-H (opening-prone
sign + strict head), H-LOW (strict head + a low-head-propensity sign, LOW-POST's set). Margins not measured before
registering.

- **GY1** HH-STRICT raises the margin on A by 0.3 point or more and raises it on B.
- **GY2** OPEN-H, the same.
- **GY3** H-LOW, the same.
- **GY4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-seventy-first set (added after the test; `predict_test271.py`, `results/predict_test271.md`)

All four failed. HH-STRICT and OPEN-H parse no line the grammar does not already parse: a two-sign line ending in a
strict head is already a bare name (G2), so the unparsed 'h h' lines end in signs that head names only occasionally.
H-LOW lowers both margins (A 49.56, B 37.32). The two-sign lines left over have no frame shuffles lack. Progress: none
(streak 4). Tally, counting parts: 1457 held, 1365 failed (2822 registered).

# Two-hundred-and-seventy-second set, registered before testing (25 September 2026): decipherment loop 97, modified Kneser-Ney discounts for the sign trigram (four hypotheses)

Streak 4. The sign trigram (trik, set 211) uses one absolute discount, D = 0.75. Modified Kneser-Ney (Chen & Goodman
1998) uses three, D1, D2 and D3+ for counts 1, 2 and 3+, estimated from the training trigrams' count-of-counts; it is
the standard improvement on small data. Component trimk replaces trik (`predict_test272.py`). No design run.

- **MK1** S on the fixed test falls by 0.002 bits or more.
- **MK2** The same A -> B (any fall).
- **MK3** SIGN top-1 does not fall.
- **MK4** Progress rule: MK1, MK2 and MK3 hold (trimk then replaces trik in MODEL).

## Results of the two-hundred-and-seventy-second set (added after the test; `predict_test272.py`, `results/predict_test272.md`)

All four failed. The count-of-counts estimates are D1 0.786, D2 1.225, D3+ 1.224, close to the single D = 0.75 for the
singletons that dominate; with them S on the fixed test is 4.6357 against 4.6354 (MK1), A -> B worsens (5.1927 ->
5.2145; MK2) and SIGN top-1 falls 39.7% -> 39.6% (MK3). The trigram's smoothing is not where S can be gained. Progress:
none (streak 5). Tally, counting parts: 1457 held, 1369 failed (2826 registered).

# Two-hundred-and-seventy-third set, registered before testing (25 September 2026): decipherment loop 98, names with material around them (four hypotheses)

Streak 5. Among the lines parse11 leaves unparsed, 266 contain an ending, closer, cage or 400 / 90 inside; several are
a name followed by a count (176 740 1 832, 121 740 1 31 240 520) or a short unit + 90 before a name (17 585 90 680 740).
NAME-NAME, NAME-TAIL and MID-POST (sets 261, 264) failed as broad splits; narrower frames (`predict_test273.py`):
NAME-COUNT (a name, then a count: numeral run + 0-2 lexical signs), PRE-NAME (1-2 lexical signs, 400 / 90, then a name),
TWO-400 (two lexical signs + 400; LOW-POST requires a low-head-propensity sign). Margins not measured before registering.

- **GZ1** NAME-COUNT raises the margin on A by 0.3 point or more and raises it on B.
- **GZ2** PRE-NAME, the same.
- **GZ3** TWO-400, the same.
- **GZ4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-seventy-third set (added after the test; `predict_test273.py`, `results/predict_test273.md`)

All four failed. NAME-COUNT lowers both margins (A 47.19, B 36.07): a count after a name is a shuffle pattern, not a
frame. PRE-NAME lowers both (49.29, 37.09). TWO-400 raises A by 0.27 point (49.91) and B by 0.19 (37.58): real, small,
and below the registered 0.3 threshold, so not adopted; it extends LOW-POST (set 250) and BODY-400 (set 263) to any
two-sign body. Progress: none (streak 6). Tally, counting parts: 1457 held, 1373 failed (2830 registered).

# Two-hundred-and-seventy-fourth set, registered before testing (25 September 2026): decipherment loop 99, a two-direction scorer for the WORD task (three hypotheses)

Streak 6. The SIGN task gained from scoring both reading directions (set 204); the WORD task (tier 6) still scores a
candidate body with the left-to-right model only. Here each candidate is scored by the sum of the left-to-right model
and the right-to-left model on the reversed line; candidates, split and model unchanged (`predict_test274.py`). Not
measured before registering.

- **WB1** WORD top-10 rises by 1 point or more.
- **WB2** WORD top-1 does not fall.
- **WB3** Progress rule: WB1 and WB2 hold (the WORD task then uses the two-direction scorer).

## Results of the two-hundred-and-seventy-fourth set (added after the test; `predict_test274.py`, `results/predict_test274.md`)

One held, two failed. Scoring both reading directions puts 10 of the 232 held-out names in the top 10 instead of 8
(3.4% -> 4.3%), 0.86 point, below the registered 1-point rise (WB1 fails); top-1 stays 0 (WB2 holds). The direction of
the gain matches the SIGN task's (set 204), but two names are too few to adopt the scorer: the WORD task is bounded by
the 54 test names seen whole in training (set 256). Progress: none (streak 7). Tally, counting parts: 1458 held, 1375
failed (2833 registered).

# Two-hundred-and-seventy-fifth set, registered before testing (25 September 2026): decipherment loop 100, end-prone signs as alternative name endings (three hypotheses)

Streak 7. Ten lexical signs end half or more of their lines (set 262: 405 407 526 298 215 423 64 137 136 155), and they
replicate on B (set 267). If they are endings like 740 / 520, the body before them is a name body: an attested body
before 740 / 520 in A lines. The contrast is the body before a line-final 400, which is not a name (set 270: never
head-class). Lexical bodies only (`predict_test275.py`). Not measured before registering.

- **EP1** A: bodies before an end-prone sign are attested name bodies more often than bodies before 400 (Fisher one-sided, p < 0.05).
- **EP2** B: the same, name bodies from A.
- **EP3** Progress rule: EP1 and EP2 hold (a new finding, replicated: the end-prone signs close name bodies).

## Results of the two-hundred-and-seventy-fifth set (added after the test; `predict_test275.py`, `results/predict_test275.md`)

All three failed. Distinct lines of a lexical body + an end-prone sign are few (A 15, B 21), and their bodies are almost
never attested name bodies (A 1 of 15, B 0 of 21), no more often than the bodies before 400 (A 1 of 40, B 1 of 18). The
end-prone signs close lines of their own kind; they are not a further ending slot in the name paradigm (740 / 520 /
closers). Their role stays 'end-prone closer' (set 267). Progress: none (streak 8). Tally, counting parts: 1458 held,
1378 failed (2836 registered).

# Two-hundred-and-seventy-sixth set, registered before testing (25 September 2026): decipherment loop 101, the slot after the counted sign (three hypotheses)

Streak 8. 597 tokens in count lines have no role; many stand right after the counted sign (numeral run + counted sign
+ X). The slot before a count is restricted (count label, set 215); if the slot after the counted sign is restricted
too it has a job (a unit or qualifier of the count). Entropy of X against 1,000 random same-size samples of the lexical
tokens of the same count lines (`predict_test276.py`). Not measured before registering.

- **CC1** A: the slot's entropy is below 95% of the random samples.
- **CC2** B: the same.
- **CC3** Progress rule: CC1 and CC2 hold; `roles` then gives X the role 'count complement'.

## Results of the two-hundred-and-seventy-sixth set (added after the test; `predict_test276.py`, `results/predict_test276.md`)

All three failed. The sign after the counted sign has an entropy of 5.82 bits on A (149 tokens) against a null median of
5.95 (p = 0.16) and 5.26 on B (112 tokens) against 5.39 (p = 0.20): slightly below chance in both, not significantly.
Unlike the slot before a count (set 215), the slot after the counted sign is open: whatever follows a count is the start
of the next unit, not a qualifier of the count. No new role. Progress: none (streak 9). Tally, counting parts: 1458
held, 1381 failed (2839 registered).

# Two-hundred-and-seventy-seventh set, registered before testing (25 September 2026): decipherment loop 102, final markers opening a line (four hypotheses)

Streak 9. CAGE-OPEN (set 261: a caged sign opens a line before a name) is the one opening frame that raised the margin.
If other final markers can likewise stand as a unit before a name, lines open with them too (`predict_test277.py`):
CLOSER-OPEN (a closer sign, then a name), POST-OPEN (400 / 90, then a name), ENDING-OPEN (740 / 520, then a name).
Margins not measured before registering.

- **GO1** CLOSER-OPEN raises the margin on A by 0.3 point or more and raises it on B.
- **GO2** POST-OPEN, the same.
- **GO3** ENDING-OPEN, the same.
- **GO4** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the two-hundred-and-seventy-seventh set (added after the test; `predict_test277.py`, `results/predict_test277.md`)

All four failed. A closer (A 49.53, B 37.20), 400 / 90 (48.91, 36.82) or 740 / 520 (48.32, 36.23) opening a line before
a name lowers both margins: of the final markers only the caged sign also opens lines (CAGE-OPEN, set 261), which fits
the cage being a unit of its own (set 184) rather than a line-final marker. Progress: none (streak 10). The stopping
rule (10 consecutive loops without progress) is met with this loop. Tally, counting parts: 1458 held, 1385 failed
(2843 registered).

# Two-hundred-and-seventy-eighth set, registered before testing (25 September 2026): decipherment loop 103, a SIGN ensemble over two family maps (three hypotheses)

New run of the loop (owner's goal of 25 Sept, stop after 10 consecutive loops without progress); streak 0. The family
components can use the ICIT decade blocks or Parpola's description families (set 208: both work for S, no gain from
using both in one model). Here the two-direction SIGN scores of the two models are averaged with equal weight, no
tuning (`predict_test278.py`). Not measured before registering.

- **SE1** SIGN top-1 rises by 0.5 point or more.
- **SE2** SIGN top-5 does not fall.
- **SE3** Progress rule: SE1 and SE2 hold (the SIGN task then uses the ensemble).

## Results of the two-hundred-and-seventy-eighth set (added after the test; `predict_test278.py`, `results/predict_test278.md`)

All three failed. Averaging the two-direction SIGN scores of the decade-family and description-family models lowers
top-1 (39.8% -> 39.5%) and top-5 (61.9% -> 61.7%): the two family maps carry the same information (as for S, set 208),
and the description families are the weaker of the two. Progress: none (streak 1 of the new run). Tally, counting
parts: 1458 held, 1388 failed (2846 registered).

# Two-hundred-and-seventy-ninth set, registered before testing (25 September 2026): decipherment loop 104, the heading unit (five hypotheses)

Streak 1. The heading (817 / 820 / 861 + 2 / 60 / 1, set 161) is a two-sign unit, but `progress.roles` gives the role
only to its first sign (the second is counted as a numeral when it is 2 or 1, and gets nothing when it is 60). And in
HEADING-BODY lines (heading + lexical body without an ending, set 263) the last sign may be a name head, as in names.
(`predict_test279.py`; `progress.roles(head2=True)` gives the second heading sign the role 'heading' where no earlier
role applies.) Not measured before registering.

- **HU1** B: 817 / 820 / 861 opening a line of 3+ signs are followed by 2 / 60 / 1 in 80%+.
- **HU2** A HEADING-BODY lines: the last sign is head-class more often than the earlier body signs (Fisher one-sided, p < 0.05).
- **HU3** B: the same.
- **HU4** Progress rule (unit): HU1 holds and R rises with the second heading sign given its role.
- **HU5** Progress rule (head): HU2 and HU3 hold; the last sign then gets the role 'name head'.

## Results of the two-hundred-and-seventy-ninth set (added after the test; `predict_test279.py`, `results/predict_test279.md`, `progress.roles(head2=True)`)

Two held, three failed. On B, 88 of the 106 lines of 3+ signs that open with 817 / 820 / 861 continue with 2 / 60 / 1
(83%; HU1): the heading is a two-sign unit there too, and giving its second sign the role raises R 86.11% -> 86.27%
(HU4; a small, bookkeeping-sized gain: the tokens were mostly 60, which had no role). In HEADING-BODY lines the last
sign is not a name head (A 5 of 29 against 7 of 51 earlier signs, p = 0.45; B 1 of 11 against 1 of 22, p = 0.56; HU2,
HU3, HU5 fail): a heading + body without an ending is not a name. Progress: R rises (streak 0). Tally, counting parts:
1460 held, 1391 failed (2851 registered).

# Two-hundred-and-eightieth set, registered before testing (25 September 2026): decipherment loop 105, the object type as context (four hypotheses)

Streak 0. Line length and genre depend on the medium (MM17, set 106), and copper tablets carry their own labels; the
model never sees the medium. Each line is prefixed with a pseudo-sign for its object class from the full ICIT records
(seal, tablet, tag, pot, other; 'unk' for the 32% of lines the records do not give, mostly M77 additions; commonest
class for a line on several), so the contexts at the line start include it; the pseudo-sign is not scored
(`predict_test280.py`). This uses what a reader of any inscription knows: the object it is on. Not measured before
registering.

- **TY1** S on the fixed test falls by 0.005 bits or more.
- **TY2** The same A -> B (any fall).
- **TY3** SIGN top-1 (with the prefix) does not fall.
- **TY4** Progress rule: TY1, TY2 and TY3 hold (S and SIGN then condition on the object class).

## Results of the two-hundred-and-eightieth set (added after the test; `predict_test280.py`, `results/predict_test280.md`)

All four failed. The object-class prefix raises S on the fixed test (4.6354 -> 4.6748), raises it much more A -> B
(5.1927 -> 5.3304) and lowers SIGN top-1 (39.7% -> 39.5%). The prefix takes a context slot: the start contexts of the
trigram and family components are split six ways, and each class sees too few lines; A -> B suffers most because most
B lines have no class in the records ('unk'), a start context the A lines rarely give. What the medium changes (length,
genre) the position and end components already see. Progress: none (streak 1). Tally, counting parts: 1460 held, 1395
failed (2855 registered).

# Two-hundred-and-eighty-first set, registered before testing (25 September 2026): decipherment loop 106, edge doubles as a role (four hypotheses)

Streak 1. EDGE-DOUBLE (set 221) put a doubled non-numeral sign at either edge into the grammar, and doubling at text
edges was found in loop 14 (sets 186-189), but the doubled signs have no role: 74 such tokens are unassigned (58 are
615, looked up before registering). If doubling is an edge device, adjacent doubled pairs stand at an edge more often
than the edge's share of pair positions (2 of n - 1 per line), on A and on B (`predict_test281.py`;
`progress.roles(dbl=True)`: role 'edge double' where no earlier role applies).

- **ED1** A: doubled non-numeral pairs (lines of 4+) stand at a line edge more often than chance (binomial, p < 0.05).
- **ED2** B: the same.
- **ED3** R rises with the edge-double role.
- **ED4** Progress rule: ED1-ED3 hold.

## Results of the two-hundred-and-eighty-first set (added after the test; `predict_test281.py`, `results/predict_test281.md`)

Two held, two failed. On A, 51 of 82 doubled non-numeral pairs stand at a line edge (62%) against 43% expected
(p = 0.0004; ED1); on B, 40 of 72 (56%) against 46% (p = 0.061; ED2 fails). The role would raise R 86.27% -> 86.89%
(ED3), but without B's replication it is not adopted. The edge preference of doubling is weaker on the M77 additions
than on A. Progress: none (streak 2). Tally, counting parts: 1462 held, 1397 failed (2859 registered).

# Two-hundred-and-eighty-second set, registered before testing (25 September 2026): decipherment loop 107, the frozen restorations against Mahadevan 1977 (four hypotheses)

Streak 2. Set 255's photographic check was not feasible and set 258 found only two gaps read by Parpola. Mahadevan's
1977 concordance (M77, in the outside-data folder, mapped to ICIT through data/icit_m77_map.tsv) is a transcription of
its own: `m77_gaps.py` aligns each of the 79 gap lines with the M77 lines of the same length whose other signs agree (at
most one mismatch in lines of 5+) and takes M77's sign at the gap when all aligned lines give the same legible sign
(`results/restoration_m77.tsv`: 23 read, 12 conflicting, 3 illegible in M77 too, 41 unmatched). Short lines can match
another object with the same frame, so only gap lines of 4+ signs count (about 15). The M77 readings were looked at
before registering; the frozen predictions (002427952) are still unread. Caveats: ICIT and M77 are not wholly
independent transcriptions, and two worklist objects share one text. Criteria as set 255 (`predict_test282.py`).

- **MR1** Top-1 predictions match the M77 reading in 25% or more of the cases (at least 10 cases).
- **MR2** Top-5 predictions contain it in 50% or more.
- **MR3** Top-1 beats the frequency baseline (the commonest sign) on the same cases.
- **MR4** Progress rule: MR1 and MR3 hold (tier 3 gains its first line, 'blind restorations confirmed against M77').

## Results of the two-hundred-and-eighty-second set (added after the test; `predict_test282.py`, `results/predict_test282.md`, `m77_gaps.py`, `results/restoration_m77.tsv`)

All four held as registered, and the set is withdrawn on audit. The frozen top-1 prediction equals Mahadevan's 1977
reading in 12 of the 15 gaps (top-5 13; the frequency baseline 740 3). But 8 of the 15 completed lines are distinct
lines of the training data (copies of the same text, or the M77 text itself as an addition): the model had seen them,
and M77's 'reading' may be the copy's, so these cases are circular. The registration should have excluded them; tier
3 counts only texts never used to fix the model. On the 7 clean cases the top-1 prediction matches 4 (H-1042 231,
H-1816 717, M-168 741, 255 13 744 [892] 740) and top-5 5, against 0 for the baseline; 7 cases are below the registered
minimum of 10. Encouraging, not evidence: no progress (streak 3). Lesson: any restoration check must drop gap lines
whose completion is a training line. Tally, counting parts: 1466 held, 1397 failed (2863 registered; this set's four
'held' are withdrawn in the text).

# Two-hundred-and-eighty-third set, registered before testing (25 September 2026): decipherment loop 108, the M77 restoration check without copies (four hypotheses)

Streak 3. Set 282 was withdrawn because 8 of its 15 completed gap lines were training lines. Here the same 15 cases
(gap lines of 4+ signs with an agreed legible M77 reading, `results/restoration_m77.tsv`) are predicted afresh, each by
the two-direction SIGN model retrained on the distinct lines minus every copy of the gap line: a line of the same length
agreeing on all other positions but at most one (the alignment's own criterion), or a line containing the whole gap line
with any sign in the gap as a contiguous run (`predict_test283.py`). What remains is what the model learned from other
texts. The predictions are made and compared inside the script. The M77 readings and set 282's (leaky) predictions are
known; these new predictions are not. Criteria as set 255.

- **MC1** Top-1 matches the M77 reading in 25% or more of the 15 cases.
- **MC2** Top-5 contains it in 50% or more.
- **MC3** Top-1 beats the frequency baseline (the commonest sign).
- **MC4** Progress rule: MC1 and MC3 hold (tier 3 gains its first line, 'blind restorations confirmed against M77, copies excluded').

## Results of the two-hundred-and-eighty-third set (added after the test; `predict_test283.py`, `results/predict_test283.md`)

All four held, narrowly. With every copy of the gap line removed from training (0-17 lines per case), the model's top-1
restoration equals Mahadevan's 1977 reading in 4 of 15 cases (27%; MC1: H-1816 717, M-168 741, M-636 861, H-1035 255),
its top 5 contain it in 9 (60%; MC2), and the frequency baseline (740) gets 3 (MC3). Caveats: the margin over the
baseline is one case; M-2109 and M-2111 carry one text (14 distinct texts: 4 against 2); ICIT and M77 are not wholly
independent transcriptions; and M77's reading is of this object only as far as the alignment identifies it (lines of
4+ signs). What it shows: a model that never saw the text restores an illegible sign as another scholar read it in a
quarter of cases, from context alone. Tier 3 gets a sign-level line (not meaning). Progress: streak 0. Tally, counting
parts: 1470 held, 1397 failed (2867 registered).

# Two-hundred-and-eighty-fourth set, registered before testing (25 September 2026): decipherment loop 109, the copy-free restoration check on new cases (four hypotheses)

Streak 0. Set 283 met its rule narrowly on 15 cases. Replication on cases it did not use: ICIT lines of 4+ signs with
exactly one illegible sign at any position (broken edges allowed), outside set 255's worklist, whose aligned M77 lines
agree on one legible sign. The count (34 cases) was looked up before registering; no prediction has been made for them.
Same procedure as set 283: model retrained without copies of each gap line, top 5 of the 150 commonest signs
(`predict_test284.py`).

- **MN1** Top-1 matches the M77 reading in 25% or more of the new cases (10+).
- **MN2** Top-5 contains it in 50% or more.
- **MN3** Top-1 beats the frequency baseline.
- **MN4** Progress rule: MN1 and MN3 hold on the new cases (the tier 3 line then counts both samples).

## Results of the two-hundred-and-eighty-fourth set (added after the test; `predict_test284.py`, `results/predict_test284.md`, `results/restoration_m77_new.tsv`)

All four held. On 34 new gaps (33 distinct texts) read by M77 and not used in set 283, the copy-free model's top-1
equals M77's sign in 17 (50%; MN1), its top 5 contain it in 23 (68%; MN2), the frequency baseline (740) in 3 (MN3).
Most models lost one copy (the other transcription of the same object); common short texts lost up to 48. Caveat on
difficulty: this sample allows gaps at line edges, and 10 of the 17 hits fill structural slots the grammar predicts
(861 / 817 before 2 at a line start: C-7, H-383, M-1832, M-454, M-1300, K-419; 740 or 527 at a line end: M-55, M-220,
M-845, M-1971); the frequency baseline, 740 everywhere, does not model the heading slot, so it understates the easy
cases. The 7 lexical hits (590 twice, 13 twice on one text, 803, 3, 741) are the harder part. Tier 3's sign-level line
now reads top-1 21 of 49 (43%), top-5 32 of 49. Progress: the tier 3 line replicates on new cases (streak 0). Tally,
counting parts: 1474 held, 1397 failed (2871 registered).

# Two-hundred-and-eighty-fifth set, registered before testing (25 September 2026): decipherment loop 110, the tier 3 restorations against a context baseline (four hypotheses)

Streak 0. Sets 283-284 beat the frequency baseline (740 everywhere), which cannot see structural slots: 10 of set 284's
17 hits are heading or ending slots. A stricter baseline, per case on the same copy-free training lines: the commonest
sign seen between the gap's two neighbours (line edges as neighbours), else after the left neighbour, else before the
right neighbour, else the commonest sign. Lexical cases: M77's sign is not a heading sign, 740 / 520 / 400 / 90 or a
closer (`predict_test285.py`, the 49 cases with the predictions already recorded). A validation, not a progress test:
if CB1 fails the tier 3 line is downgraded.

- **CB1** The model's top-1 beats the context baseline's on the 49 cases.
- **CB2** The same on the lexical cases.
- **CB3** The model's top-1 is right in 20% or more of the lexical cases.
- **CB4** Progress rule: none (validation; recorded as failing).

## Results of the two-hundred-and-eighty-fifth set (added after the test; `predict_test285.py`, `results/predict_test285.md`)

Three held; CB4 is the non-progress rule. Against a context baseline built on the same copy-free training lines, the
model's top-1 wins narrowly: 21 against 19 of the 49 cases (CB1), 10 against 7 of the 29 lexical cases (CB2), and it is
right in 34% of the lexical cases (CB3). The tier 3 line stands, but most of what the model restores a plain neighbour
rule restores too: the Indus texts are formulaic enough that the sign between two known neighbours is often the one
seen there before. The PROGRESS tier 3 cell now gives both baselines. Progress: none (validation; streak 1). Tally,
counting parts: 1477 held, 1398 failed (2875 registered).

# Two-hundred-and-eighty-sixth set, registered before testing (25 September 2026): decipherment loop 111, damaged-text runs as extra training text (four hypotheses)

Streak 1. Sample D (damaged.py, set 253) holds 435 legible runs of damaged texts, 1,501 signs not in any clean line. Set
188's extra clean lines did not lower S by its 0.03 threshold; D is new text and was left out because its runs have
cut edges. Here a cut start is marked with the pseudo-sign '<cut>' and a cut end with '<cutend>', so the runs add
interior contexts without false line starts or ends; the test lines are unchanged (`predict_test286.py`). Not measured
before registering.

- **DX1** S on the fixed test falls by 0.005 bits or more.
- **DX2** The same A -> B (any fall).
- **DX3** SIGN top-1 does not fall.
- **DX4** Progress rule: DX1, DX2 and DX3 hold (training then includes the marked runs).

# Two-hundred-and-eighty-seventh set, registered before testing (25 September 2026): decipherment loop 112, the referent method's criteria calibrated by false-discovery rate (four hypotheses)

Owner's request (25 Sept): expand the picture-referent method (tier 1's only line with a positive control) over the
next loops. Its criteria (3+ objects, 80%+ one picture, 2+ distinct texts for pairs) were fixed in set 233 and never
calibrated. `referents.py` makes them parameters (k objects, share s) and reproduces the current line (k 3, s 0.8: 27
units, 0.79%). For each of four criteria, (3, 0.8), (3, 0.67), (2, 1.0) and (2, 0.67), qualifying units are counted on
the real pictures and on 100 shuffles within each pool; FDR = mean shuffled count / real count. Rule fixed now: the
criterion with FDR <= 10% and the largest coverage is chosen; the Linear B control (set 235's four words) is re-run with
it (`predict_test287.py`). Not measured before registering.

- **RX1** The current criterion has FDR <= 10%.
- **RX2** A looser criterion with FDR <= 10% raises the coverage.
- **RX3** Linear B with the chosen criterion recovers 2+ of the 4 control words, none with a wrong ideogram.
- **RX4** Progress rule: RX2 and RX3 hold (`prizebench.referent_fixed` then uses the chosen criterion).

## Results of the two-hundred-and-eighty-seventh set (added after the test; `predict_test287.py`, `results/predict_test287.md`, `referents.py`, `prizebench.referent_fixed`)

All four held. False-discovery rates against 100 picture shuffles: k 3, s 0.8 (the old criterion) 27 units, shuffled
mean 0.7, FDR 2.5% (RX1); k 3, s 0.67 38 units, FDR 5.5%; k 2, s 1.0 30 units, FDR 11.4%; k 2, s 0.67 55 units, shuffled
mean 5.2, FDR 9.4%, coverage 1.38% (chosen by the registered rule; RX2). With the chosen criterion the Linear B control
still recovers a-mo-ta (ROTA, wheel) and ko-wa (MUL, woman), none with a wrong ideogram (RX3). About 5 of the 55 units
are expected to be chance; the old 27 are almost all real. `prizebench.referent_fixed` now uses k 2, s 0.67 (the old
line is referent_fixed(DL, 3, 0.8)). Progress: the tier 1 referent line rises 0.79% -> 1.38% (streak 0). Tally,
counting parts: 1481 held, 1398 failed (2879 registered).

# Two-hundred-and-eighty-eighth set, registered before testing (25 September 2026): decipherment loop 113, single signs and 3-sign runs as referent units (four hypotheses)

Streak 0. The referent method counts whole texts and adjacent sign pairs (sets 233-287). A referent may sit in one sign
(a noun written with one sign) or need three. With set 287's criterion (2+ objects in 2+ distinct texts, 67%+ one
picture) and its false-discovery rule (FDR against 100 picture shuffles <= 10%), unit sets (2), (1, 2), (2, 3) and
(1, 2, 3) are compared (`predict_test288.py`; `referents.units(ns=...)`). The single-sign units are listed. Not
measured before registering.

- **RN1** Adding single signs keeps FDR <= 10% and raises the coverage.
- **RN2** Adding 3-sign runs keeps FDR <= 10% and raises the coverage.
- **RN3** The unit set with FDR <= 10% and the largest coverage beats pairs alone.
- **RN4** Progress rule: RN3 holds (the referent line then uses the chosen unit set).

## Results of the two-hundred-and-eighty-eighth set (added after the test; `predict_test288.py`, `results/predict_test288.md`)

Three held, one failed. With set 287's criterion: pairs alone 55 units (FDR 9.4%, 1.38%); + single signs 88 (FDR 10.8%,
1.65%; RN1 fails the 10% rule); + 3-sign runs 68 (FDR 9.8%, 1.46%; RN2); all three 101 (FDR 10.8%). The registered rule
chooses pairs + 3-sign runs (RN3): the referent line rises 1.38% -> 1.46%. The 33 single-sign candidates, though over
the FDR line as a set, show the locality found in set 243: 806 goes with the human figure on individually made tablets
and with plants on moulded ones; the gharial (Gavi) and plant (Phyt) signs are all on moulded tablets, the bull (Bult)
signs on individually made ones. `prizebench.referent_fixed` now uses ns (2, 3). Progress: tier 1 referent line rises
(streak 0). Tally, counting parts: 1484 held, 1399 failed (2883 registered).

## Results of the two-hundred-and-eighty-sixth set (added after the test; `predict_test286.py`, `results/predict_test286.md`)

One held, three failed. The 435 marked runs (1,501 signs) raise S on the fixed test (4.6354 -> 4.6712; DX1) and A -> B
(5.1938 -> 5.2105; DX2); SIGN top-1 rises slightly (39.6% -> 39.8%; DX3). The cut markers take probability mass and
split contexts, and short runs add more edge contexts than interior ones; damaged texts do not help the model, as clean
extra lines did not (set 188). (Recorded after loops 112-113, which ran meanwhile; the streak after loop 111 was 2.)
Tally, counting parts: 1485 held, 1402 failed (2887 registered).

# Two-hundred-and-eighty-ninth set, registered before testing (25 September 2026): decipherment loop 114, the picture vault with referent units (four hypotheses)

Streak 0. Tier 3 needs meaning checked on texts not used to fix it. The picture vault of sets 201-203 (sign-level
anchors, leave-one-out) reached 16.9% (p = 0.05). Here, with the calibrated referent units (sets 287-288: sign pairs and
3-sign runs, 2+ objects in 2+ distinct texts, 67%+ one picture): each pictured tablet is held out, units are learned
from the other objects of its pool excluding every object with the same text (merged part-texts), and the units in the
held-out text vote for its picture. Accuracy on the objects that get a prediction, against 200 shuffles of the pictures
within each pool (`predict_test289.py`). Not measured before registering.

- **PV1** Pooled accuracy is above the 95th percentile of the shuffles.
- **PV2** Pooled accuracy is 30% or more.
- **PV3** Each pool (individually made, moulded) is above its shuffle median.
- **PV4** Progress rule: PV1 and PV2 hold (tier 3 gains a picture-vault line for referents).

## Results of the two-hundred-and-eighty-ninth set (added after the test; `predict_test289.py`, `results/predict_test289.md`)

Two held, two failed. Held out one text at a time, the referent units predict the picture of 74 of the 556 pictured
tablets and are right on 26 (35.1%; PV2; the sign-level vault of sets 201-203 reached 16.9%): individually made 11 of
39 (28.2%, shuffle median 21.4%), moulded 15 of 35 (42.9%, shuffle median 0%) (PV3). But the pooled accuracy is not
above the shuffles' 95th percentile (53.8%; p = 0.19; PV1 fails): with shuffled pictures few units qualify, so the
shuffles make only a few predictions and their accuracy swings widely. The registered statistic was poorly chosen
(accuracy on a varying number of predictions); the number of correct predictions is the stable one. Not rescored here;
a new registered set will test it. Progress: none (streak 1). Tally, counting parts: 1487 held, 1404 failed (2891
registered).

# Two-hundred-and-ninetieth set, registered before testing (25 September 2026): decipherment loop 115, the picture vault by correct predictions, with a Linear B control (three hypotheses)

Streak 1. Set 289's accuracy statistic was unstable (shuffles make few predictions). The stable statistic is the number
of correct predictions, which counts both how many held-out objects the units reach and how often they are right. The
real count (26) is known from set 289; its shuffle distribution is not. Control: the same leave-one-out vault on Linear
B (each DAMOS line's ideogram from its words, units from the other lines without copies of the same word list, same
criterion), against 20 shuffles of the ideograms (`predict_test290.py`).

- **VH1** Indus: the number of correct predictions is above the 95th percentile of 200 shuffles.
- **VH2** Linear B control: the number of correct predictions is above all 20 shuffles.
- **VH3** Progress rule: VH1 and VH2 hold (tier 3 gains a picture-vault line for referents).

## Results of the two-hundred-and-ninetieth set (added after the test; `predict_test290.py`, `results/predict_test290.md`)

All three held. Scored by correct predictions, the picture vault is well above chance: 26 held-out tablets get the
right picture from referent units learned on other texts (copies excluded), against a shuffle median of 1 and a 95th
percentile of 7 (p = 0.005, the floor for 200 shuffles; VH1). The same procedure on Linear B gets 710 of 1,716 DAMOS
lines' ideograms right against a shuffle maximum of 22 (VH2): the vault works as a positive control. Scope: 74 of 556
pictured tablets get a prediction; the units are local to their pool (set 243); the check is referent-level (the text
names what the picture shows), not a reading. Tier 3's picture-vault cell is updated. Progress: streak 0. Tally,
counting parts: 1490 held, 1404 failed (2894 registered).

# Two-hundred-and-ninety-first set, registered before testing (25 September 2026): decipherment loop 116, the referent method on seals, non-default animals (four hypotheses)

Streak 0. Set 238 (strict criterion) found seal phrases only for the one-horned bull, the default animal on 77% of
seals. With the calibrated criterion (set 287: 2+ seals in 2+ distinct texts, 67%+ one animal; pairs and 3-sign runs,
set 288), units labelled with any other animal are counted, and their FDR estimated from 100 shuffles of the animals
among the 1,274 pictured seals (`predict_test291.py`). Tags (59, 44 bull) and SEAL:C (16) are too small to test apart.
Not measured before registering.

- **SN1** Non-default seal units exist with FDR <= 10%.
- **SN2** There are more of them than the shuffles' 95th percentile.
- **SN3** They mark seal tokens (coverage beyond the tablets).
- **SN4** Progress rule: SN1 and SN2 hold (seal units join the referent line).

## Results of the two-hundred-and-ninety-first set (added after the test; `predict_test291.py`, `results/predict_test291.md`)

One held, three failed. With the calibrated criterion the 1,274 pictured seals give 5 units labelled with an animal
other than the one-horned bull (2 233 235, 415 803, 415 803 1, 550 1, 803 1, all gaur), against 2.2 in shuffles (FDR
43%, SN1 fails; 95th percentile 7, SN2 fails); they would mark 11 tokens (SN3). Set 238's result stands with the looser
criterion: seal texts do not name their animal. The referent method's reach is the tablets, where the text and the
picture were made for each other. Progress: none (streak 1). Tally, counting parts: 1491 held, 1407 failed (2898
registered).

# Two-hundred-and-ninety-second set, registered before testing (25 September 2026): decipherment loop 117, skip-pairs as referent units (three hypotheses)

Streak 1. A referent word written with a variable inner sign (an inflection, a numeral, a variant) escapes contiguous
pairs and runs. Skip-pairs (A _ B: two signs one position apart, any sign between) are added to the pairs and 3-sign
runs (set 288) under set 287's criterion; FDR against 100 picture shuffles (`predict_test292.py`; `referents.grams_of`).
Not measured before registering.

- **SK1** With skip-pairs the FDR stays at or below 10%.
- **SK2** The coverage rises.
- **SK3** Progress rule: SK1 and SK2 hold (skip-pairs join the referent units).

## Results of the two-hundred-and-ninety-second set (added after the test; `predict_test292.py`, `results/predict_test292.md`)

One held, two failed. Skip-pairs add 22 units (90 against 68) and raise coverage 1.46% -> 1.65% (SK2), but the shuffles
give 9.2 on average, FDR 10.2%, just over the registered 10% (SK1, SK3 fail): the extra units are about as noisy as the
single signs of set 288. Not adopted. Progress: none (streak 2). Tally, counting parts: 1492 held, 1409 failed (2901
registered).

# Two-hundred-and-ninety-third set, registered before testing (25 September 2026): decipherment loop 118, where referent units sit in a text (three hypotheses)

Streak 2. If the referent units are words for the pictured thing, they may hold a fixed place in the text (leading it,
or in the name head's place at the end). Relative start position (0 first, 1 last) of each occurrence of a qualifying
referent unit (set 288) against other units recurring on 2+ objects in 2+ texts, per pool; Mann-Whitney two-sided;
direction not predicted (`predict_test293.py`). Not measured before registering.

- **RP1** Individually made tablets: the positions differ (p < 0.05).
- **RP2** Moulded tablets: they differ in the same direction.
- **RP3** Progress rule: RP1 and RP2 hold (a new finding, replicated across the two pools).

## Results of the two-hundred-and-ninety-third set (added after the test; `predict_test293.py`, `results/predict_test293.md`)

All three failed. Referent units sit at about the same relative position as other recurring units: individually made
0.62 against 0.57 (p = 0.49), moulded 0.55 against 0.58 (p = 0.46), in opposite directions. The word for the pictured
thing has no fixed slot in the tablet texts; it is part of the text wherever the text's grammar puts it. Progress: none
(streak 3). Tally, counting parts: 1492 held, 1412 failed (2904 registered).

# Two-hundred-and-ninety-fourth set, registered before testing (25 September 2026): decipherment loop 119, the picture vault with all unit kinds (three hypotheses)

Streak 3. Single signs (set 288) and skip-pairs (set 292) failed the 10% FDR rule as referent units, but the vault
(set 290) checks units on held-out tablets against shuffles, which controls false units by itself. Here the vault votes
with single signs, pairs, 3-sign runs and skip-pairs (`predict_test294.py`). Not measured before registering.

- **VX1** More than set 290's 26 correct predictions, with p < 0.05 against 200 shuffles.
- **VX2** Accuracy on the predicted objects is 30% or more.
- **VX3** Progress rule: VX1 holds (the tier 3 vault line counts more held-out tablets).

## Results of the two-hundred-and-ninety-fourth set (added after the test; `predict_test294.py`, `results/predict_test294.md`)

All three held. Voting with single signs, pairs, 3-sign runs and skip-pairs, the vault reaches 191 held-out tablets
(against 74) and gets 64 pictures right (33.5%; VX1, VX2), against a shuffle median of 4 and a 95th percentile of 14
(p = 0.005, the floor for 200 shuffles). The unit kinds that failed the 10% FDR rule as a list still predict held-out
pictures far above chance: the held-out check is the stronger test. The tier 3 vault cell now reads 64 tablets.
Progress: streak 0. Tally, counting parts: 1495 held, 1412 failed (2907 registered).

# Two-hundred-and-ninety-fifth set, registered before testing (25 September 2026): decipherment loop 120, the picture vault with single-object units (three hypotheses)

Streak 0. Set 294's vault lets a unit vote when it stands on 2+ other objects in 2+ texts with 67%+ one picture. Here a
unit seen on a single other object (a different text) may also vote, with that object's picture; the shuffles still
guard against noise (`predict_test295.py`). Not measured before registering.

- **VK1** More than set 294's 64 correct predictions, with p < 0.05 against 200 shuffles.
- **VK2** Accuracy on the predicted objects is 25% or more.
- **VK3** Progress rule: VK1 holds.

## Results of the two-hundred-and-ninety-fifth set (added after the test; `predict_test295.py`, `results/predict_test295.md`)

Two held as registered, one failed; progress withdrawn on audit. Letting a unit vote from a single other object, the
vault predicts 325 held-out tablets and gets 81 right (VK1 holds: more than 64, p = 0.005), but accuracy falls to 24.9%
(VK2 fails) and the shuffle median rises from 4 to 28: the excess over chance falls from +60 (set 294) to +53. The
added predictions are right by chance about as often as by referent. The rule compared raw counts; it should have
compared the excess over the shuffle median. The tier 3 line stays at set 294's (64 of 191). Lesson: score a vault by
correct predictions minus the shuffle median. Progress: none (streak 1). Tally, counting parts: 1497 held, 1413 failed
(2910 registered).

# Two-hundred-and-ninety-sixth set, registered before testing (25 September 2026): decipherment loop 121, the picture vault with weighted votes (three hypotheses)

Streak 1. Set 294's vault gives every qualifying unit one vote. Here a unit votes with weight share * log2(1 + n), its
picture's share among the n other objects that carry it, so well-supported, pure units outweigh weak ones. Units and
criterion as set 294. Scored by the excess of correct predictions over the shuffle median (set 295's lesson; set 294:
+60) (`predict_test296.py`). Not measured before registering.

- **VW1** The excess over the shuffle median is above +60, with p < 0.05 against 200 shuffles.
- **VW2** Accuracy on the predicted objects is above 33.5%.
- **VW3** Progress rule: VW1 holds (the tier 3 vault line rises).

## Results of the two-hundred-and-ninety-sixth set (added after the test; `predict_test296.py`, `results/predict_test296.md`)

All three failed. Weighting each unit's vote by its purity and support gets 61 of 191 held-out pictures right (31.9%),
excess +56 over the shuffle median of 5, below set 294's +60 with one vote per unit (VW1, VW2 fail). The widely
supported units are the common signs and pairs, which are the least specific; up-weighting them pulls votes toward the
frequent pictures. (The registered script had a string-quoting error, fixed in 2d4bd2c15 before the run; the test
itself is unchanged.) Progress: none (streak 2). Tally, counting parts: 1497 held, 1416 failed (2913 registered).

# Two-hundred-and-ninety-seventh set, registered before testing (25 September 2026): decipherment loop 122, the picture vault with specificity-weighted votes (three hypotheses)

Streak 2. Set 296's support weighting favoured common, unspecific units and did worse. Here each qualifying unit votes
with weight 1 / n (n = other objects carrying it), so rare, specific units count more; otherwise as set 294, scored by
the excess over the shuffle median (`predict_test297.py`). Not measured before registering.

- **VS1** The excess over the shuffle median is above +60, with p < 0.05 against 200 shuffles.
- **VS2** Accuracy on the predicted objects is above 33.5%.
- **VS3** Progress rule: VS1 holds (the tier 3 vault line rises).

## Results of the two-hundred-and-ninety-seventh set (added after the test; `predict_test297.py`, `results/predict_test297.md`)

All three failed. Weighting votes by specificity (1 / n) gets 62 of 191 held-out pictures right (32.5%), excess +57
over the shuffle median of 5, against set 294's +60 (VS1, VS2 fail). Neither support (set 296, +56) nor specificity
weighting beats one vote per unit: the vault's limit is which tablets carry a known unit, not how the votes are
weighed. Progress: none (streak 3). Tally, counting parts: 1497 held, 1419 failed (2916 registered).

# Two-hundred-and-ninety-eighth set, registered before testing (25 September 2026): decipherment loop 123, the picture vault with a cross-pool fallback (three hypotheses)

Streak 3. The vault's limit is reach: a held-out tablet needs a unit known in its own pool. Referent labels are mostly
local to a pool (set 243), but some may travel. Here a tablet whose own pool gives no vote takes the votes of the other
pool's units (set 294's units and criterion otherwise), scored by the excess over the shuffle median
(`predict_test298.py`). Not measured before registering.

- **VC1** The excess over the shuffle median is above +60, with p < 0.05 against 200 shuffles.
- **VC2** More than 191 held-out tablets get a prediction.
- **VC3** Progress rule: VC1 holds (the tier 3 vault line rises).

## Results of the two-hundred-and-ninety-eighth set (added after the test; `predict_test298.py`, `results/predict_test298.md`)

All three held. With the other pool's units as a fallback, the vault predicts 295 held-out tablets (VC2) and gets 70
right (23.7%) against a shuffle median of 6: excess +64, above set 294's +60 (p = 0.005; VC1). The gain is small: the
104 tablets reached only through the other pool add about 4 correct predictions beyond chance, so the labels mostly do
not travel between pools (as set 243 found), though a few do. Tier 3's vault cell now includes this line. Progress:
the vault excess rises (streak 0). Tally, counting parts: 1500 held, 1419 failed (2919 registered).

# Two-hundred-and-ninety-ninth set, registered before testing (25 September 2026): decipherment loop 124, referents across sites (three hypotheses)

Streak 0. The vault holds out one text at a time inside a pool. A stronger test, closer to new excavations: learn the
referent units on one city's moulded tablets and predict the pictures on the other city's (Harappa 235 moulded tablets,
Mohenjo-daro 61; fragment runs included; copies of a text excluded), both directions, against 200 shuffles of the
pictures in the learning city (`predict_test299.py`). The individually made pool is not used: its Mohenjo-daro tablets
are copper and its Harappa tablets incised, which set 243 found do not share labels. Not measured before registering.

- **XS1** Harappa -> Mohenjo-daro: correct predictions above the shuffles (p < 0.05).
- **XS2** Mohenjo-daro -> Harappa: the same.
- **XS3** Progress rule: XS1 and XS2 hold (referents travel between cities; tier 3 gains a cross-site line).

## Results of the two-hundred-and-ninety-ninth set (added after the test; `predict_test299.py`, `results/predict_test299.md`)

All three held as registered; withdrawn on audit. Harappa -> Mohenjo-daro gives 1 correct prediction of 25 (shuffle
median 0, p = 0.025) and Mohenjo-daro -> Harappa 22 of 215 (median 5, p = 0.005). But 17 of the 22 predict 'Mult', the
code for a tablet with several pictures (a genre, not a referent), and 3 test texts are part or whole of a Mohenjo-daro
text, a leak the identical-text exclusion misses; 2 clean referent hits remain. Referents do not travel between the
cities. The registration should have excluded the catch-all codes (Mult, Scene, Comp) and part-texts. The audit of the
in-pool vault (set 294) shows its hits are referents (bull 30, plant 20, fish 7; Mult 2), so that line stands, resting
on three pictures. Progress: none (streak 1). Tally, counting parts: 1503 held, 1419 failed (2922 registered; this
set's three 'held' are withdrawn in the text).

# Three-hundredth set, registered before testing (25 September 2026): decipherment loop 125, referent units over sign families (three hypotheses)

Streak 1. If one word is written with graphic variants of a sign, exact-sign units split it and each part may fall
short of the criterion. Texts are mapped to Parpola's description families (descfam, set 208; unmapped signs keep their
id) before the units (pairs, 3-sign runs) are formed; set 287's criterion and FDR rule; coverage on the real tokens
(`predict_test300.py`). Not measured before registering.

- **FV1** Family units keep FDR at or below 10%.
- **FV2** Coverage rises above the sign units' 1.46%.
- **FV3** Progress rule: FV1 and FV2 hold (the referent line uses family units).

## Results of the three-hundredth set (added after the test; `predict_test300.py`, `results/predict_test300.md`)

One held, two failed. Over description families the method finds 74 units (sign units 68) and they would mark 2.87% of
tokens (FV2), but the shuffles give 8.5 on average, FDR 11.5%, over the registered 10% (FV1, FV3 fail): a family unit
matches more texts, by chance as well as by variant spelling. Not adopted. Progress: none (streak 2). Tally, counting
parts: 1504 held, 1421 failed (2925 registered).

# Three-hundred-and-first set, registered before testing (25 September 2026): decipherment loop 126, the picture vault with sign-family units (three hypotheses)

Streak 2. Family units failed the 10% FDR rule as a list (set 300) but, as with single signs (set 294), the vault checks
units on held-out tablets. Here set 298's vault (all unit kinds, cross-pool fallback) also votes with every unit kind
formed over Parpola's description families (`predict_test301.py`). Not measured before registering.

- **VF1** The excess over the shuffle median is above +64 (set 298), with p < 0.05 against 200 shuffles.
- **VF2** Accuracy on the predicted objects is at least set 298's 23.7%.
- **VF3** Progress rule: VF1 holds (the tier 3 vault line rises).

## Results of the three-hundred-and-first set (added after the test; `predict_test301.py`, `results/predict_test301.md`)

All three failed. With family units the vault reaches 386 held-out tablets and gets 72 right, but the shuffle median
rises to 9: excess +63 against set 298's +64 (VF1), accuracy 18.7% (VF2). The family units reach more tablets without
adding referent knowledge: variant-spelling does not explain the tablets the sign units miss. Progress: none (streak 3).
Tally, counting parts: 1504 held, 1424 failed (2928 registered).

# Three-hundred-and-second set, registered before testing (25 September 2026): decipherment loop 127, the picture vault without catch-all votes (three hypotheses)

Streak 3. Set 299's audit found that the codes Mult, Scene and Comp (several pictures, a scene, a composite) name a
genre of tablet, not a thing. Here a unit whose qualifying picture is one of them does not vote, so the vote falls to
units naming one thing; set 298's vault otherwise, all tablets remain targets (`predict_test302.py`). Not measured
before registering.

- **VG1** The excess over the shuffle median is above +64 (set 298), with p < 0.05 against 200 shuffles.
- **VG2** Accuracy on the predicted objects is at least 23.7%.
- **VG3** Progress rule: VG1 holds (the tier 3 vault line rises).

## Results of the three-hundred-and-second set (added after the test; `predict_test302.py`, `results/predict_test302.md`)

All three failed. Without catch-all votes the vault gets 68 of 292 held-out pictures right (23.3%), shuffle median 5:
excess +63 against set 298's +64. Removing the Mult / Scene / Comp votes costs as many right predictions as it saves;
the vault line is unchanged, and it can be stated without the catch-all codes at almost no cost. Progress: none
(streak 4). Tally, counting parts: 1504 held, 1427 failed (2931 registered).

# Three-hundred-and-third set, registered before testing (25 September 2026): decipherment loop 128, single signs as referent units under a stricter criterion (three hypotheses)

Streak 4. Single signs failed at set 287's loose criterion (set 288: FDR 10.8%) because common signs pick up chance
associations. Here single signs must meet the stricter criterion (3+ objects in 2+ texts, 80%+ one picture), while pairs
and 3-sign runs keep 2+ / 67%+; combined FDR against 100 picture shuffles (`predict_test303.py`). Not measured before
registering.

- **SS1** The combined FDR is at or below 10%.
- **SS2** Coverage rises above 1.46%.
- **SS3** Progress rule: SS1 and SS2 hold (strict single signs join the referent units).

## Results of the three-hundred-and-third set (added after the test; `predict_test303.py`, `results/predict_test303.md`)

All three held. Single signs under the stricter criterion (3+ objects in 2+ texts, 80%+ one picture) add 17 units
beside the pairs and 3-sign runs: combined 85 units, shuffle mean 7.8, FDR 9.1% (SS1); coverage 1.46% -> 1.62% (SS2).
The single signs: on individually made tablets 171, 226, 636, 797, 824, 840 (bull, Bult), 4 (pipal), 790 (goat), 923
(elephant); on moulded tablets 17, 318, 440, 503 (gharial), 463, 752 (plant), 405 (Bull1), 167 (Mult). They stay local
to their pool. `prizebench.referent_fixed` adds them. Progress: referent line rises (streak 0). Tally, counting parts:
1507 held, 1427 failed (2934 registered).

# Three-hundred-and-fourth set, registered before testing (25 September 2026): decipherment loop 129, skip-pairs and family units under the stricter criterion (three hypotheses)

Streak 0. Skip-pairs (set 292, FDR 10.2%) and family units (set 300, FDR 11.5%) failed narrowly at the loose criterion;
single signs passed at the stricter one (set 303). Each is added, under the stricter criterion (3+ objects in 2+ texts,
80%+ one picture), to set 303's units; combined FDR against 100 picture shuffles; coverage on the real tokens
(`predict_test304.py`). Not measured before registering.

- **SF1** Strict skip-pairs: FDR at or below 10% and coverage above set 303's.
- **SF2** Strict family units (pairs and 3-sign runs over description families): the same.
- **SF3** Progress rule: SF1 or SF2 holds (the passing kind joins the referent units; if both, the larger coverage).

## Results of the three-hundred-and-fourth set (added after the test; `predict_test304.py`, `results/predict_test304.md`)

All three held. Under the stricter criterion, skip-pairs added to set 303's units give 96 units, FDR 7.6%, coverage
1.70% (SF1); family units (pairs and 3-sign runs over description families) give 108 units, FDR 9.6%, coverage 1.80%
(SF2). The registered rule takes the larger coverage: family units join (`prizebench.referent_fixed`), and the referent
line rises 1.62% -> 1.80%. Skip-pairs and family units together were not tested. Progress: streak 0. Tally, counting
parts: 1510 held, 1427 failed (2937 registered).

# Three-hundred-and-fifth set, registered before testing (25 September 2026): decipherment loop 130, strict skip-pairs with the family units (two hypotheses)

Streak 0. Set 304 found strict skip-pairs and strict family units each passing and adopted the family units. Here the
strict skip-pairs are added to them; combined FDR against 100 picture shuffles (`predict_test305.py`). Not measured
before registering.

- **SB1** The combined FDR is at or below 10% and coverage rises above 1.80%.
- **SB2** Progress rule: SB1 holds (strict skip-pairs join the referent units).

## Results of the three-hundred-and-fifth set (added after the test; `predict_test305.py`, `results/predict_test305.md`)

Both held. Strict skip-pairs added to set 304's units give 119 units, FDR 8.3% (below either kind's alone: the
stricter units are cleaner), coverage 1.80% -> 1.87%. `prizebench.referent_fixed` now uses them. Progress: referent
line rises (streak 0). Tally, counting parts: 1512 held, 1427 failed (2939 registered).

# Three-hundred-and-sixth set, registered before testing (25 September 2026): decipherment loop 131, family single signs and skip-pairs under the stricter criterion (two hypotheses)

Streak 0. Sets 303-305 admitted single signs, family pairs / 3-sign runs and skip-pairs under the stricter criterion.
The two remaining family kinds, single family signs and family skip-pairs, are added (3+ objects in 2+ texts, 80%+);
combined FDR against 100 picture shuffles (`predict_test306.py`). Not measured before registering.

- **FS1** The combined FDR is at or below 10% and coverage rises above 1.87%.
- **FS2** Progress rule: FS1 holds (they join the referent units).

## Results of the three-hundred-and-sixth set (added after the test; `predict_test306.py`, `results/predict_test306.md`)

Both held. Strict family single signs and family skip-pairs added to set 305's units give 136 units, FDR 6.7%, coverage
1.87% -> 1.89% (FS1): a small step, the unit grid under the strict criterion is now complete. `prizebench.referent_fixed`
uses them. Progress: referent line rises, small (streak 0). Tally, counting parts: 1514 held, 1427 failed (2941
registered).

# Three-hundred-and-seventh set, registered before testing (25 September 2026): decipherment loop 132, the strict-tier units at an intermediate criterion (two hypotheses)

Streak 0. After set 306 the combined FDR is 6.7%, below the 10% rule. The unit kinds admitted under the stricter
criterion (single signs, skip-pairs and the four family kinds) are tried at an intermediate one (3+ objects in 2+ texts,
67%+ one picture); pairs and 3-sign runs keep 2+ / 67%+. Combined FDR against 100 picture shuffles
(`predict_test307.py`). Not measured before registering.

- **MI1** The combined FDR is at or below 10% and coverage rises above 1.89%.
- **MI2** Progress rule: MI1 holds (the intermediate criterion replaces 80%+ for these kinds).

## Results of the three-hundred-and-seventh set (added after the test; `predict_test307.py`, `results/predict_test307.md`)

Both held. With single signs, skip-pairs and the four family kinds at 3+ objects and 67%+ (pairs and 3-sign runs
unchanged), the method finds 185 units, FDR 7.8%, coverage 1.89% -> 2.28% (MI1). Caution: sets 287-307 tuned the
criteria step by step against the same kind of FDR estimate; each step passed its own test, but the sequence as a whole
needs an independent check (next set). Progress: referent line rises (streak 0). Tally, counting parts: 1516 held, 1427
failed (2943 registered).

# Three-hundred-and-eighth set, registered before testing (25 September 2026): decipherment loop 133, a split-half check of the tuned referent configuration (three hypotheses)

Streak 0. Sets 287-307 tuned the referent criteria step by step against the same FDR estimate. Independent check: each
pool's distinct texts are split at random into halves (seed 308); set 307's configuration learns units on one half and
the other half is scored: the share of (unit, held-out object) matches whose picture is the unit's label, against 1,000
shuffles of the held-out pictures; both directions (`predict_test308.py`). A validation: a failure downgrades the tuned
line; no progress either way. Not measured before registering.

- **SH1** Half 1 -> half 2: matches above the shuffles (p < 0.05).
- **SH2** Half 2 -> half 1: the same.
- **SH3** Progress rule: none (validation; recorded as failing).

## Results of the three-hundred-and-eighth set (added after the test; `predict_test308.py`, `results/predict_test308.md`)

One held, two failed. Learned on half the texts, set 307's configuration finds 91 units, and 80 of their 384 matches on
the other half carry the unit's picture (21%, p = 0.002; SH1); the other way, 70 units, 62 of 246 (25%, p = 0.058;
SH2 fails). The tuned line is not confirmed independently in both directions, and its held-out precision is low: the
2.28% is downgraded, as registered, to an unconfirmed upper figure (PROGRESS tier 1 cell). The step-by-step tuning of
sets 287-307 found real signal (one direction clearly significant) but its precision is far below the in-sample
purity (67%+). Next: the same split-half check on the earlier configurations, to find the largest one confirmed both
ways. Progress: none (streak 1). Tally, counting parts: 1517 held, 1429 failed (2946 registered).

# Three-hundred-and-ninth set, registered before testing (25 September 2026): decipherment loop 134, which referent configuration survives a split-half check (three hypotheses)

Streak 1. Set 308's single split was mixed for the tuned configuration. Each configuration adopted since set 233 (C0
original, C1 set 287, C2 set 288, C3 set 303, C4 set 304, C5 set 305, C6 set 306, C7 set 307) is checked on five random
half-splits (seeds 3091-3095), both directions, the real held-out matches summed over the ten split-directions against
200 joint shuffles of the held-out pictures; confirmed if p < 0.05 (`predict_test309.py`). Rule fixed now: the referent
line is set to the largest confirmed configuration (it can only stay or fall; no progress either way). Not measured
before registering.

- **SL1** C0, the original criterion, is confirmed.
- **SL2** C7, the tuned configuration, is confirmed.
- **SL3** Progress rule: none (a correction; the referent line is set to the largest confirmed configuration).

## Results of the three-hundred-and-ninth set (added after the test; `predict_test309.py`, `results/predict_test309.md`)

Two held; SL3 is the non-progress rule. Pooled over five random half-splits in both directions, every configuration is
confirmed (SL1, SL2): C1 62 of 222 held-out matches right (28%, p = 0.010), C2 70 of 241 (29%, p = 0.020), C3 136 of 576
(24%), C4 223 of 851 (26%), C5 252 of 908 (28%), C6 314 of 1,184 (27%), C7 578 of 2,539 (23%) (p = 0.005 from C3 on).
Set 308's single split was an unlucky draw. The 2.28% referent line (C7) is restored as confirmed; the caveat is its
precision: about a quarter of held-out matches carry the unit's picture, against the 67%+ purity required in sample.
The units are real associations, not reliable word meanings. Progress: none (correction; streak 2). Tally, counting
parts: 1519 held, 1430 failed (2949 registered).

# Three-hundred-and-tenth set, registered before testing (25 September 2026): decipherment loop 135, split-half precision of the referent method on Linear B (three hypotheses)

Streak 2. Set 309 found the Indus referent units' held-out precision low (C0 44%, C1 28%, C7 23%). Is that low for the
method? The same split-half check on Linear B (DAMOS lines, words and ideograms; five half-splits of the distinct word
lists, both directions) at C0-like (3+ lines, 80%+) and C1-like (2+, 67%+) criteria gives the yardstick
(`predict_test310.py`). No progress either way. Not measured before registering.

- **LP1** Linear B's C0-like held-out precision is above the Indus C0 figure (44%).
- **LP2** Linear B's C1-like precision is above the Indus C1 figure (28%).
- **LP3** Progress rule: none (a yardstick; recorded as failing).

## Results of the three-hundred-and-tenth set (added after the test; `predict_test310.py`, `results/predict_test310.md`)

Two held; LP3 is the non-progress rule. On Linear B the same split-half check gives held-out precision of 96% (8,661 of
8,993 matches, C0-like) and 95% (9,673 of 10,175, C1-like), against the Indus 44% (C0) and 28% (C1). Linear B is the
easy case the method was built for: an administrative line names its commodity next to the ideogram. The Indus
tablets' texts are tied to their pictures far more loosely: the referent units are real (sets 290, 309) but a unit
predicts its picture on a new tablet only a quarter to under half of the time. Stated in the PROGRESS tier 1 cell.
Progress: none (streak 3). Tally, counting parts: 1521 held, 1431 failed (2952 registered).

# Three-hundred-and-eleventh set, registered before testing (25 September 2026): decipherment loop 136, tags and SEAL:C as referent pools (three hypotheses)

Streak 3. The referent method uses two tablet pools. Two small pictured pools are added with set 307's configuration:
tags (TAG and subtypes, 59 clean objects, mostly Bull1 and elephant) and SEAL:C / SEAL:CY (16, 13 gaur). Combined FDR
against 100 picture shuffles; coverage on the real tokens (`predict_test311.py`). Not measured before registering.

- **TP1** The combined FDR is at or below 10%.
- **TP2** Coverage rises above 2.28%.
- **TP3** Progress rule: TP1 and TP2 hold (the new pools join).

## Results of the three-hundred-and-eleventh set (added after the test; `predict_test311.py`, `results/predict_test311.md`)

One held, two failed. Tags (94 objects with fragments) and SEAL:C / SEAL:CY (28) add 89 units and would raise coverage to
3.28% (TP2), but the combined FDR rises to 33.7% (TP1 fails): in a pool dominated by one picture (Bull1 on tags, gaur on
SEAL:C) almost any recurring unit meets the share criterion by chance, as seals showed (sets 238, 291). Not adopted.
Progress: none (streak 4). Tally, counting parts: 1522 held, 1433 failed (2955 registered).

# Three-hundred-and-twelfth set, registered before testing (25 September 2026): decipherment loop 137, 4-sign runs as referent units (two hypotheses)

Streak 4. 4-sign runs (3+ objects in 2+ texts, 67%+ one picture) are added to set 307's units; combined FDR against 100
picture shuffles (`predict_test312.py`). Not measured before registering.

- **F41** The combined FDR is at or below 10% and coverage rises above 2.28%.
- **F42** Progress rule: F41 holds (4-sign runs join).

## Results of the three-hundred-and-twelfth set (added after the test; `predict_test312.py`, `results/predict_test312.md`)

Both held. 4-sign runs add 4 units (189), FDR 7.2%, coverage 2.28% -> 2.29%: progress by the registered rule, minimal in
size; longer runs recur too rarely to add much. `prizebench.referent_fixed` includes them. Progress: streak 0. Tally,
counting parts: 1524 held, 1433 failed (2957 registered).

# Three-hundred-and-thirteenth set, registered before testing (25 September 2026): decipherment loop 138, referent units before an ending (three hypotheses)

Streak 0. Referent units have no fixed position in the text (set 293), but they may have a fixed grammatical slot: if
they name the pictured thing as a name body does, they stand directly before an ending (740 / 520) more often than other
recurring units; or less, if they are labels outside the name. Per pool, the share of occurrences directly followed by
740 / 520 (units containing an ending excluded), referent units against other units recurring on 2+ objects in 2+
texts; Fisher two-sided; direction not predicted (`predict_test313.py`). Not measured before registering.

- **RE1** Individually made tablets: the shares differ (p < 0.05).
- **RE2** Moulded tablets: they differ in the same direction.
- **RE3** Progress rule: RE1 and RE2 hold (a new finding, replicated across pools).

## Results of the three-hundred-and-thirteenth set (added after the test; `predict_test313.py`, `results/predict_test313.md`)

All three failed. Referent units are followed by 740 / 520 in 10% of occurrences on individually made tablets against
24% for other recurring units (p = 0.12), and in 26% against 16% on moulded tablets (p = 0.38): opposite directions,
neither significant. The referent units hold no fixed grammatical slot relative to the endings, as they hold no fixed
position (set 293). Progress: none (streak 1). Tally, counting parts: 1524 held, 1436 failed (2960 registered).

# Three-hundred-and-fourteenth set, registered before testing (25 September 2026): decipherment loop 139, restoration of lines with two illegible signs (three hypotheses)

Streak 1. Tier 3's restoration line (sets 283-285) uses single gaps. Lines with two illegible signs that M77 reads
(13 lines, 26 signs; counted before registering, no prediction made) are new cases: for each, the two-direction model
is retrained without copies of the line and the pair is chosen jointly over the 60 commonest signs; each gap sign is
compared with M77, and with set 285's context baseline applied to each gap (`predict_test314.py`).

- **MT1** The model is right on 25% or more of the gap signs (10+ signs).
- **MT2** The model beats the context baseline.
- **MT3** Progress rule: MT1 and MT2 hold (the tier 3 restoration line gains these cases).

## Results of the three-hundred-and-fourteenth set (added after the test; `predict_test314.py`, `results/predict_test314.md`)

All three held. On 13 lines with two illegible signs read by M77 (26 signs), the copy-free model chooses both signs
jointly and matches M77 on 8 (31%; MT1): K-43 60, M-1077 415, M-1386 760 and 740, M-1498 100, H-1103 892, H-779 400, and
740 in the last line; the context baseline matches 4 (MT2). The tier 3 restoration line now counts 29 of 75 signs (39%)
against a context baseline of 23. Progress: streak 0. Tally, counting parts: 1527 held, 1436 failed (2963 registered).

# Three-hundred-and-fifteenth set, registered before testing (25 September 2026): decipherment loop 140, pictographic referent signs (three hypotheses)

Streak 0. Tier 1's strict line counts four copper-tablet signs whose shape is the animal pictured on the same tablet.
The referent method now finds single signs tied to a picture (set 303: e.g. 923 with the elephant, 17 / 318 / 440 / 503
with the gharial). Where Parpola's CISI description of such a sign names the thing in its picture, the sign is a
pictograph checked against iconography, like the copper anchors. Loop 77 found sign shapes generally unrelated to the
pictures, so this is a hard test. Single-sign referents at 3+ objects, 67%+ (both pools); keyword lists per picture
code fixed in the script; matches against 1,000 shuffles of the pictures among these signs (`predict_test315.py`). No
description was looked at before registering.

- **PA1** Two or more single-sign referents are described as the thing in their picture, above the shuffles' 95th percentile.
- **PA2** The matches include a sign not already an anchor (749, 341, 753, 777).
- **PA3** Progress rule: PA1 and PA2 hold (the matching signs join ANCHORS; V strict rises).

## Results of the three-hundred-and-fifteenth set (added after the test; `predict_test315.py`, `results/predict_test315.md`)

One held, two failed. Of 29 single-sign referents (24 with a CISI description), one is described as the thing in its
picture: 752, "u with decorated branching at top", with plants (Phyt) on moulded tablets; the shuffles give up to 2 (p
= 0.70; PA1 fails). The elephant sign 923 is "right parenthesis drawn in outline", the gharial signs are strokes,
triangles and a tree (407), the goat sign 790 a leaf or diamond. As loop 77 found for pictures and sign shapes in
general, the referent signs do not depict their referents: the tablets write a word for the pictured thing, not its
drawing. No new anchor. Progress: none (streak 1). Tally, counting parts: 1528 held, 1438 failed (2966 registered).

# Three-hundred-and-sixteenth set, registered before testing (25 September 2026): decipherment loop 141, one word per referent (three hypotheses)

Streak 1. The referent signs are not drawings of their pictures (loop 77, set 315); if they write a word for the
pictured thing, the several units tied to one picture are overlapping pieces of that word and share signs. Within each
pool, the share of unit pairs sharing a sign among same-picture pairs minus that among different-picture pairs, against
1,000 shuffles of the unit labels (`predict_test316.py`). Not measured before registering.

- **OW1** Individually made tablets: same-picture units share signs more than chance (p < 0.05).
- **OW2** Moulded tablets: the same.
- **OW3** Progress rule: OW1 and OW2 hold (a new finding, replicated across pools).

## Results of the three-hundred-and-sixteenth set (added after the test; `predict_test316.py`, `results/predict_test316.md`)

All three held as registered; withdrawn on audit. Same-picture unit pairs share a sign far more often than
different-picture pairs in both pools (individually made 54 of 147 against 71 of 843, moulded 16 of 125 against 6 of
310; p = 0.001 each). But a unit nested in another (a pair inside a 3-sign run of the same phrase) shares signs and
picture by construction. Without nested pairs: individually made 17 of 110 against 71 of 843 (p = 0.035), moulded 3 of
112 against 4 of 308 (p = 0.12). Some support for one word per referent on the individually made tablets, none on the
moulded ones. The registration should have excluded nested units. Progress: none (streak 2). Tally, counting parts:
1531 held, 1438 failed (2969 registered; this set's three 'held' are withdrawn in the text).

# Three-hundred-and-seventeenth set, registered before testing (25 September 2026): decipherment loop 142, WORD with a body-frequency prior (three hypotheses)

Streak 2. The two-direction WORD scorer (set 274) reached 4.3% top-10, below the 1-point threshold over the bench's
3.4%. Here the score adds beta * log(1 + training count of the body), with beta chosen on a development split of the
training lines (0, 0.5, 1, 2) and applied once to the fixed test lines (`predict_test317.py`). Not measured before
registering.

- **WP1** WORD top-10 is 1 point or more above 3.4%.
- **WP2** The prior takes weight on the development split (beta > 0).
- **WP3** Progress rule: WP1 holds (the WORD task then uses this scorer).

## Results of the three-hundred-and-seventeenth set (added after the test; `predict_test317.py`, `results/predict_test317.md`)

All three failed. On the development split every beta gives 4 of 218 names in the top 10, so the rule keeps beta 0
(WP2 fails); on the test lines the two-direction scorer stays at 10 of 232 (4.3%; WP1 fails). The model's line
probability already carries the body's frequency. The WORD task is capped by the 54 test names seen whole in training.
Progress: none (streak 3). Tally, counting parts: 1531 held, 1441 failed (2972 registered).

# Three-hundred-and-eighteenth set, registered before testing (25 September 2026): decipherment loop 143, BODY-90 and SHORT-90 (three hypotheses)

Streak 3. BODY-400 (set 263) found 400 closing a longer lexical body; 90 stands where 400 does after endings. Rules
(`predict_test318.py`, on top of parse11): BODY-90 (3+ lexical signs + 90), SHORT-90 (1-2 lexical signs + 90). Scored
by the G margin on A and B. Not measured before registering.

- **G91** BODY-90 raises the margin on A by 0.3 point or more and raises it on B.
- **G92** SHORT-90, the same.
- **G93** Progress rule: the rules that hold, together, raise the margin on A (0.3+) and on B; they then join the grammar.

## Results of the three-hundred-and-eighteenth set (added after the test; `predict_test318.py`, `results/predict_test318.md`)

All three failed. BODY-90 (A 49.65, B 37.36) and SHORT-90 (49.62, 37.36) leave the margins practically unchanged: 90
closes lexical bodies too rarely to form a frame; unlike 400 (sets 250, 263), it is a post-ending marker only.
Progress: none (streak 4). Tally, counting parts: 1531 held, 1444 failed (2975 registered).

# Three-hundred-and-nineteenth set, registered before testing (25 September 2026): decipherment loop 144, tablet referents on seals (three hypotheses)

Streak 4. Referents do not travel between tablet types or cities (sets 243, 299), and seal texts do not name their
animal (sets 238, 291). A direct cross-medium check: tablet referent units whose picture is an animal also shown on
seals (elephant, rhinoceros, goat, bull, gaur, zebu, buffalo, tiger; the tablet code Bult counted as the bull) are
looked for in seal texts; the seals carrying them should show that animal more often than chance (1,000 shuffles of
the seal animals) (`predict_test319.py`). Not measured before registering.

- **SM1** Seals carrying a tablet referent unit show its animal more often than chance (p < 0.05).
- **SM2** At least one matched unit names an animal other than the default bull.
- **SM3** Progress rule: SM1 holds (a new finding: referents travel from tablets to seals).

## Results of the three-hundred-and-nineteenth set (added after the test; `predict_test319.py`, `results/predict_test319.md`)

One held, two failed. 35 tablet referent units carry an animal also shown on seals (bull, elephant, gaur, goat, rhino;
11 not the bull; SM2); they occur 491 times in seal texts, and 304 of those seals show the unit's animal, against a
shuffle median of 310 (p = 0.78; SM1 fails). Tablet referents do not travel to seals, in keeping with sets 238, 243,
291 and 299: the referent labels are local to the tablets that carry them. Progress: none (streak 5). Tally, counting
parts: 1532 held, 1446 failed (2978 registered).

# Three-hundred-and-twentieth set, registered before testing (25 September 2026): decipherment loop 145, SIGN with 250 candidates (three hypotheses)

Streak 5. The SIGN task ranks the 150 commonest training signs, so a hidden rarer sign can never be ranked first. With
250 candidates the model can reach them, at the cost of more competitors (`predict_test320.py`). Not measured before
registering.

- **SC1** SIGN top-1 rises by 0.1 point or more.
- **SC2** SIGN top-5 does not fall.
- **SC3** Progress rule: SC1 and SC2 hold (the SIGN task uses 250 candidates).

## Results of the three-hundred-and-twentieth set (added after the test; `predict_test320.py`, `results/predict_test320.md`)

One held, two failed. With 250 candidates SIGN top-1 falls 39.79% -> 39.62% (SC1 fails) and top-5 rises 61.92% ->
62.35% (SC2): the rare signs it can now reach are won back less often than they displace the right common sign at the
top. The 150-candidate task stands. Progress: none (streak 6). Tally, counting parts: 1533 held, 1448 failed (2981
registered).

# Three-hundred-and-twenty-first set, registered before testing (25 September 2026): decipherment loop 146, referent units over picture classes (two hypotheses)

Streak 6. The ICIT picture codes split one referent across codes (Bult, Bull1, Bull, Bull2 are all bulls), which can
keep a word's evidence below the share criterion. Codes are merged into classes fixed now (bovine: Bult Bull1 Bull Bull2
Zebu Gaur Buff; plant: Phyt Pipal; others unchanged) and set 312's configuration is re-run with them; combined FDR
against 100 shuffles of the classes (`predict_test321.py`). Coarser classes also make chance matches easier, which the
FDR measures. Not measured before registering.

- **PC1** The combined FDR is at or below 10% and coverage rises above 2.29%.
- **PC2** Progress rule: PC1 holds (the referent line uses the picture classes).

## Results of the three-hundred-and-twenty-first set (added after the test; `predict_test321.py`, `results/predict_test321.md`)

Both failed. With picture classes (bovine, plant merged) the configuration finds 239 units and would mark 2.84%, but the
FDR rises to 12.4% (PC1 fails): the merged bovine class covers most individually made tablets, so a unit reaches the
share criterion by chance as easily as on a seal pool dominated by the bull (sets 291, 311). The fine codes stay.
Progress: none (streak 7). Tally, counting parts: 1533 held, 1450 failed (2983 registered).

# Three-hundred-and-twenty-second set, registered before testing (25 September 2026): decipherment loop 147, the referent pools without catch-all objects (two hypotheses)

Streak 7. Tablets coded Mult, Scene or Comp (several pictures, a scene, a composite) name no single thing (set 299) and
dilute the share of every unit they carry. They are removed from both pools before set 312's configuration is run;
combined FDR against 100 picture shuffles (`predict_test322.py`). Not measured before registering.

- **PX1** The combined FDR is at or below 10% and coverage rises above 2.29%.
- **PX2** Progress rule: PX1 holds (the referent pools drop the catch-all objects).

## Results of the three-hundred-and-twenty-second set (added after the test; `predict_test322.py`, `results/predict_test322.md`)

Both failed. Without the 104 catch-all tablets the configuration finds 182 units, FDR 10.2%, coverage 2.28% against
2.29% (PX1 fails): the units the catch-all objects diluted are balanced by those they supported. The pools stay as
they are. Progress: none (streak 8). Tally, counting parts: 1533 held, 1452 failed (2985 registered).

# Three-hundred-and-twenty-third set, registered before testing (25 September 2026): decipherment loop 148, the picture vault with the tier 1 configuration (two hypotheses)

Streak 8. The vault (sets 290-298) votes with loosely chosen unit kinds; tier 1 now uses a calibrated configuration
(set 312: pairs and 3-sign runs at 2+ / 67%+; single signs, skip-pairs, 4-sign runs and the family kinds at 3+ / 67%+).
Here the vault votes with exactly that configuration, learned without copies of the held-out text, with set 298's
cross-pool fallback; scored by the excess over the shuffle median (`predict_test323.py`). Not measured before
registering.

- **VT1** The excess over the shuffle median is above +64 (set 298), with p < 0.05 against 200 shuffles.
- **VT2** Progress rule: VT1 holds (the tier 3 vault line rises).

## Results of the three-hundred-and-twenty-third set (added after the test; `predict_test323.py`, `results/predict_test323.md`)

Both failed. Voting with the calibrated tier 1 configuration (64 correct of 373 predicted (17.2%); shuffles median 8, 95th percentile 20; p = 0.005), the vault's
excess over the shuffle median is +56, below set 298's +64 with the loose unit kinds (VT1 fails): the configuration's
family and 4-sign units reach more held-out tablets (373) but less accurately (17.2%). Progress: none (streak 9). Tally, counting parts: 1533
held, 1454 failed (2987 registered).

# Three-hundred-and-twenty-fourth set, registered before testing (25 September 2026): decipherment loop 149, a back-off picture vault (two hypotheses)

Streak 9. The loose vault (set 298) is more accurate where it votes; the tier 1 configuration (set 323) reaches more
tablets less accurately. Back-off: the loose units vote first (own pool, then the other pool); a tablet left without a
vote takes the tier 1 configuration's votes (own pool, then the other). Excess over the shuffle median
(`predict_test324.py`). Not measured before registering.

- **VB1** The excess over the shuffle median is above +64 (set 298), with p < 0.05 against 200 shuffles.
- **VB2** Progress rule: VB1 holds (the tier 3 vault line rises).

## Results of the three-hundred-and-twenty-fourth set (added after the test; `predict_test324.py`, `results/predict_test324.md`)

Both failed. The back-off vault gets 72 of 385 held-out pictures right (18.7%), shuffle median 9: excess +63 against
set 298's +64 (VB1 fails). The tier 1 configuration's extra reach adds predictions right about as often as by chance.
Progress: none (streak 10). The owner's stopping rule (10 consecutive loops without progress) is met with this loop,
ending the run begun at loop 103. Tally, counting parts: 1533 held, 1456 failed (2989 registered).

# Three-hundred-and-twenty-fifth set, registered before testing (25 September 2026): decipherment loop 150, a base-rate criterion for referent units (four hypotheses)

Owner's goal (25 Sept): continue until another 10 loops without progress, focused on the referent line; streak 0.
The fixed share criterion (67%+) treats every picture alike, although 2 of 3 is weak for the commonest picture (bull)
and strong for a rare one (gharial). Base-rate criterion: a unit on 2+ objects in 2+ distinct texts takes its most
common picture m when a binomial test against m's share in the pool gives P < alpha; all unit kinds of set 312, whole
texts as before; alpha from 0.001-0.05 chosen by the FDR rule (<= 10%, 100 picture shuffles, largest coverage); the
Linear B control re-run with it (`predict_test325.py`). Not measured before registering.

- **RB1** An alpha with FDR <= 10% gives coverage above 2.29% (set 312).
- **RB2** Linear B with that alpha recovers 2+ of the 4 control words, none wrong.
- **RB3** The chosen alpha keeps FDR <= 10%.
- **RB4** Progress rule: RB1, RB2 and RB3 hold (the referent line uses the base-rate criterion).

## Results of the three-hundred-and-twenty-fifth set (added after the test; `predict_test325.py`, `results/predict_test325.md`)

All four held. With the base-rate criterion: alpha 0.001 286 units, FDR 0.6%, coverage 3.91%; 0.005 368, 3.1%, 4.66%;
0.01 388, 5.7%, 4.79%; 0.02 434, 10.5%, 5.04%; 0.05 493, 24.2%, 5.33%. The rule chooses alpha 0.01 (RB1, RB3): the
referent line rises 2.29% -> 4.79%; the Linear B control recovers a-mo-ta and ko-wa, none wrong (RB2). The fixed 67%
share discarded strong evidence for rare pictures (two gharial objects of two is P = 0.0025 at a 5% base rate) and
admitted weak evidence for the commonest. Even alpha 0.001 (FDR 0.6%) reaches 3.91%. A jump this size needs the
split-half check of set 309 (next set). `prizebench.referent_fixed` uses alpha 0.01. Progress: streak 0. Tally,
counting parts: 1537 held, 1456 failed (2993 registered).

# Three-hundred-and-twenty-sixth set, registered before testing (25 September 2026): decipherment loop 151, split-half check of the base-rate configuration (three hypotheses)

Streak 0. Set 325 doubled the referent line with a base-rate criterion. Independent check as set 309: five random
half-splits, both directions, the real held-out matches (held-out objects carrying the unit's picture) against 200 joint
shuffles; held-out precision compared with set 309's C7, 23% (`predict_test326.py`). A validation: a failure of BV1
downgrades the line; no progress either way. Not measured before registering.

- **BV1** The base-rate configuration is confirmed on the five split-halves (p < 0.05).
- **BV2** Its held-out precision is at least 23%.
- **BV3** Progress rule: none (validation; recorded as failing).

## Results of the three-hundred-and-twenty-sixth set (added after the test; `predict_test326.py`, `results/predict_test326.md`)

One held, two failed (BV3 is the non-progress rule). On five split-halves both ways the base-rate configuration's
units match 1,275 of 9,406 held-out objects' pictures, against a shuffle median of 631 (p = 0.005; BV1): the line is
confirmed. Held-out precision is 14%, below C7's 23% (BV2 fails): the base-rate criterion reaches far more text, but a
unit's picture holds on a new tablet about twice as often as chance, not reliably. The 4.79% line stands with that
precision stated in the tier 1 cell. Progress: none (streak 1). Tally, counting parts: 1538 held, 1458 failed (2996
registered).

# Three-hundred-and-twenty-seventh set, registered before testing (25 September 2026): decipherment loop 152, referent pools by tablet type (two hypotheses)

Streak 1. Referents do not travel between tablet types (set 243), and copper and incised tablets carry different
pictures, yet they share one 'individually made' pool whose base rates mix them. The base-rate configuration (set 325,
alpha 0.01) is run with copper (TAB:C) and incised (TAB:I) as separate pools beside the moulded pool; combined FDR
against 100 picture shuffles (`predict_test327.py`). Not measured before registering.

- **TY1** The combined FDR is at or below 10% and coverage rises above 4.79%.
- **TY2** Progress rule: TY1 holds (the referent pools are split by tablet type).

## Results of the three-hundred-and-twenty-seventh set (added after the test; `predict_test327.py`, `results/predict_test327.md`)

Both failed. With copper (76 objects), incised (121) and moulded (359) as separate pools, the base-rate configuration
finds 328 units (against 388), FDR 5.3%, coverage 4.37% against 4.79% (TY1 fails): a unit shared by copper and incised
tablets loses its support when the pools are split, and the purer base rates do not make up for it. Progress: none
(streak 2). Tally, counting parts: 1538 held, 1460 failed (2998 registered).

# Three-hundred-and-twenty-eighth set, registered before testing (25 September 2026): decipherment loop 153, one pool for all pictured tablets (two hypotheses)

Streak 2. Splitting pools lost support (set 327). The reverse: individually made and moulded tablets in one pool (base
rates over all; part-texts merged across the pool), base-rate configuration of set 325; combined FDR against 100
picture shuffles (`predict_test328.py`). Referent labels are mostly pool-local (set 243), so mixing may only add noise;
the FDR decides. Not measured before registering.

- **MP1** The combined FDR is at or below 10% and coverage rises above 4.79%.
- **MP2** Progress rule: MP1 holds (one pool for all pictured tablets).

## Results of the three-hundred-and-twenty-eighth set (added after the test; `predict_test328.py`, `results/predict_test328.md`)

Both held. With all 556 pictured tablets in one pool, the base-rate configuration finds 431 units, FDR 7.0%, coverage
4.79% -> 5.43% (MP1): pooling gives shared words the support they lacked in each pool, and the shuffles show it does
not bring in more chance units than the rule allows. `prizebench.referent_fixed` now uses one pool. The held-out
precision of this configuration has not been measured (set 326's 14% was for two pools). Progress: streak 0. Tally,
counting parts: 1540 held, 1460 failed (3000 registered).

# Three-hundred-and-twenty-ninth set, registered before testing (25 September 2026): decipherment loop 154, seals and tags in the one pool (three hypotheses)

Streak 0. Seals and tags failed as referent pools under the fixed share because one animal dominates them (sets 238,
291, 311). The base-rate test (set 325) corrects exactly that: a unit for the one-horned bull needs a share well above
the bull's 77%. Pictured seals (SEAL:S, SEAL:R, SEAL, SEAL:C, SEAL:CY) and tags join set 328's single pool; combined FDR
against 100 picture shuffles; coverage on the real tokens (`predict_test329.py`). Not measured before registering.

- **SP1** The combined FDR is at or below 10%.
- **SP2** Coverage rises above 5.43%.
- **SP3** Progress rule: SP1 and SP2 hold (seals and tags join the referent pool).

## Results of the three-hundred-and-twenty-ninth set (added after the test; `predict_test329.py`, `results/predict_test329.md`)

One held, two failed. With 1,669 pictured seals and tags added (2,225 objects), the base-rate configuration at alpha
0.01 finds 540 units and would mark 30.47% of tokens (SP2), but the FDR is 19.3% (SP1 fails): with so many seal texts,
chance associations pass alpha 0.01 too often. The seal units cover common phrases, which is why coverage leaps. A
stricter alpha for the combined pool is the next test. Progress: none (streak 1). Tally, counting parts: 1541 held,
1462 failed (3003 registered).

# Three-hundred-and-thirtieth set, registered before testing (25 September 2026): decipherment loop 155, the combined pool at stricter alphas (four hypotheses)

Streak 1. Seals and tags in the one pool reached 30.5% but FDR 19.3% at alpha 0.01 (set 329). Stricter alphas (0.0001,
0.0005, 0.001, 0.002, 0.005): the alpha with FDR <= 10% and the largest coverage is chosen; the Linear B control is
re-run with it (`predict_test330.py`). Caveat registered now: a unit tied to the one-horned bull (Bull1) across
hundreds of seals may mark a seal type, not a word for the bull; coverage without Bull1 units is reported beside it.
Not measured before registering.

- **SA1** An alpha with FDR <= 10% gives coverage above 5.43%.
- **SA2** Without Bull1 units that alpha still covers more than 5.43%.
- **SA3** Linear B with that alpha recovers 2+ of the 4 control words, none wrong.
- **SA4** Progress rule: SA1 and SA3 hold (the referent line uses the combined pool at that alpha; SA2 reported as the caveat).

## Results of the three-hundred-and-thirtieth set (added after the test; `predict_test330.py`, `results/predict_test330.md`)

All four held. With tablets, seals and tags in one pool: alpha 0.0001 258 units, FDR 0.8%, coverage 18.48% (6.02%
without Bull1 units); 0.0005 321, 2.0%, 20.01% (6.81%); 0.001 347, 4.7%, 20.97% (7.24%); 0.002 390, 7.3%, 23.52% (7.53%);
0.005 483, 14.3%, 29.31%. The rule chooses alpha 0.002 (SA1); the Linear B control passes (SA3); without Bull1 units
the line is 7.53%, still above 5.43% (SA2). Most of the gain is units whose picture is the one-horned bull on seals:
a phrase far commoner on bull seals than their 77% share predicts. That association is real (FDR 7.3%), but it may
mark a type of seal (a workshop, a class of owner) rather than a word for the bull; set 238 saw the same slight excess.
The PROGRESS tier 1 cell gives both figures. `prizebench.referent_fixed` builds the pool as the test does (a first
version merged part-texts twice and gave 27.0%; fixed before recording). Progress: streak 0. Tally, counting parts:
1545 held, 1462 failed (3007 registered).

# Three-hundred-and-thirty-first set, registered before testing (25 September 2026): decipherment loop 156, split-half check of the combined referent pool (four hypotheses)

Streak 0. Set 330 raised the referent line to 23.5% (7.5% without the default-bull units). Independent check as sets
309 and 326: five random half-splits of the distinct texts, both directions, held-out matches against 200 joint
shuffles, for all units and for the non-Bull1 units separately (`predict_test331.py`). A validation: a failure downgrades
the matching figure; no progress either way. Not measured before registering.

- **CV1** All units are confirmed on the five split-halves (p < 0.05).
- **CV2** The units not labelled Bull1 are confirmed (p < 0.05).
- **CV3** The non-Bull1 units' held-out precision is at least 14% (set 326).
- **CV4** Progress rule: none (validation; recorded as failing).

## Results of the three-hundred-and-thirty-first set (added after the test; `predict_test331.py`, `results/predict_test331.md`)

Two held, two failed (CV4 is the non-progress rule). On five split-halves both ways, all units of the combined pool
match 14,867 of 29,790 held-out objects' pictures (50%) against a shuffle median of 12,869 (p = 0.005; CV1): most
matches are bull units on bull seals, right about as often as the bull's base rate plus a margin. The units for other
pictures match 958 of 8,946 (11%) against a median of 242 (p = 0.005; CV2): four times chance, but below set 326's 14%
(CV3 fails). Both figures of the line stand, confirmed; their precision is low. Progress: none (streak 1). Tally,
counting parts: 1547 held, 1464 failed (3011 registered).

# Three-hundred-and-thirty-second set, registered before testing (25 September 2026): decipherment loop 157, the combined pool at intermediate alphas (four hypotheses)

Streak 1. Set 330 chose alpha 0.002 (FDR 7.3%); 0.005 gave 14.3%. Intermediate alphas 0.0025, 0.003 and 0.004 under the
same rule (FDR <= 10%, largest coverage) and Linear B check (`predict_test332.py`). Not measured before registering.

- **SF1** An intermediate alpha with FDR <= 10% gives coverage above 23.52%.
- **SF2** Without Bull1 units it covers more than 7.53%.
- **SF3** Linear B with it recovers 2+ of the 4 control words, none wrong.
- **SF4** Progress rule: SF1 and SF3 hold (the referent line uses that alpha).

## Results of the three-hundred-and-thirty-second set (added after the test; `predict_test332.py`, `results/predict_test332.md`)

All four held. Alpha 0.0025: 412 units, FDR 8.5%, coverage 23.77% (7.85% without Bull1 units); 0.003 FDR 11.1%; 0.004
11.8%. The rule chooses 0.0025 (SF1, SF2); the Linear B control passes (SF3). A small step. (Two labels in the script
read SA1 / SA3 and its docstring named the wrong results file; corrected in text only.) `prizebench.referent_fixed`
uses alpha 0.0025. Progress: streak 0. Tally, counting parts: 1551 held, 1464 failed (3015 registered).

# Three-hundred-and-thirty-third set, registered before testing (25 September 2026): decipherment loop 158, site-stratified base rates for the referent pool (four hypotheses)

Streak 0. The combined pool's units, most of them for the default seal bull, are tested against the pool-wide share of
each picture. If picture shares differ between sites, a phrase common at a bull-heavy site passes as a bull referent.
Here a unit's expected share is the mean of its objects' own-site shares (binomial with that mean), and the FDR comes
from shuffles of the pictures within each site (`predict_test333.py`). A validation: the stratified figures replace the
current ones (23.77% / 7.85% without Bull1 units) if lower; no progress either way. Not measured before registering.

- **ST1** The site-stratified FDR is at or below 10%.
- **ST2** The stratified coverage is at least 23.77%.
- **ST3** The stratified coverage without Bull1 units is at least 7.85%.
- **ST4** Progress rule: none (validation; recorded as failing).

## Results of the three-hundred-and-thirty-third set (added after the test; `predict_test333.py`, `results/predict_test333.md`)

One held, three failed (ST4 is the non-progress rule). With each object's expected picture share taken from its own
site (50 sites) and the pictures shuffled within sites, the combined pool gives 305 units, FDR 5.8% (ST1), coverage
18.99% (ST2 fails against 23.77%) and 6.70% without Bull1 units (ST3 fails against 7.85%). Part of the unstratified
line was site composition: phrases common at a site where one animal dominates passed as referents for it. As
registered, the stratified figures replace the current ones (PROGRESS tier 1 cell; `prizebench.referent_fixed`
stratified by default). Progress: none (streak 1). Tally, counting parts: 1552 held, 1467 failed (3019 registered).

# Three-hundred-and-thirty-fourth set, registered before testing (25 September 2026): decipherment loop 159, base rates stratified by site and object class (four hypotheses)

Streak 1. In the one pool, seals are mostly bull and tablets rarely: a phrase commoner on seals than on tablets passes
as a bull referent. Set 333's site strata become (site, object class: seal, tablet, tag); expected shares and the
shuffles within strata as there (`predict_test334.py`). A validation: lower figures replace the current ones (18.99% /
6.70% without Bull1 units); no progress either way. Not measured before registering.

- **SX1** The stratified FDR is at or below 10%.
- **SX2** The stratified coverage is at least 18.99%.
- **SX3** Without Bull1 units, at least 6.70%.
- **SX4** Progress rule: none (validation; recorded as failing).

## Results of the three-hundred-and-thirty-fourth set (added after the test; `predict_test334.py`, `results/predict_test334.md`)

One held, three failed (SX4 is the non-progress rule). With strata of site and object class (71 strata), the combined
pool gives 224 units, FDR 4.6% (SX1), coverage 12.69% (SX2 fails against 18.99%) and 5.75% without Bull1 units (SX3
fails against 6.70%). Seals are mostly bull and tablets rarely: part of the site-stratified line was phrases commoner on
seals than on tablets. As registered, these figures replace the current ones (`prizebench.referent_fixed` now
stratifies by site and class). The line is still far above the tablets-only 5.43% of set 328, and the non-bull figure
above it too. Progress: none (streak 2). Tally, counting parts: 1553 held, 1470 failed (3023 registered).

# Three-hundred-and-thirty-fifth set, registered before testing (25 September 2026): decipherment loop 160, the stratified referent pool at looser alphas (four hypotheses)

Streak 2. Stratifying by site and object class (set 334) lowered the FDR to 4.6% at alpha 0.0025. Looser alphas (0.005,
0.01, 0.02) under the same strata: the alpha with FDR <= 10% (100 within-stratum shuffles) and the largest coverage is
chosen, with the Linear B control (`predict_test335.py`). Not measured before registering.

- **SL1** An alpha with FDR <= 10% gives coverage above 12.69%.
- **SL2** Without Bull1 units it covers more than 5.75%.
- **SL3** Linear B with it recovers 2+ of the 4 control words, none wrong.
- **SL4** Progress rule: SL1 and SL3 hold (the stratified referent line uses that alpha).

## Results of the three-hundred-and-thirty-fifth set (added after the test; `predict_test335.py`, `results/predict_test335.md`)

All four held. Under the site-and-class strata: alpha 0.005 296 units, FDR 8.1%, coverage 13.64% (6.84% without Bull1
units); 0.01 333, 14.6%; 0.02 398, 22.9%. The rule chooses 0.005 (SL1, SL2); the Linear B control passes (SL3). The
stratified line rises 12.69% -> 13.64%. `prizebench.referent_fixed` uses alpha 0.005 with the strata. Progress:
streak 0. Tally, counting parts: 1557 held, 1470 failed (3027 registered).

# Three-hundred-and-thirty-sixth set, registered before testing (25 September 2026): decipherment loop 161, are the seal bull units words for the bull? (three hypotheses)

Streak 0. Most of the referent line is units for the one-horned bull on seals, which may be words for the bull or marks
of a seal type (a workshop, a class of owner). The two predict differently off the seals: a word for the bull should
come with bulls on tablets too; a seal-type mark should not. Units are learned on the pictured seals alone (set 334's
stratified method, alpha 0.005); pictured tablets carrying a Bull1 unit are checked for a bull picture (Bull1, Bult,
Bull, Bull2) against 1,000 shuffles of the tablet pictures (`predict_test336.py`). Not measured before registering.

- **BW1** Tablets carrying a seal bull unit show a bull more often than chance (p < 0.05).
- **BW2** At least 10 tablets carry one (enough to test).
- **BW3** Progress rule: BW1 and BW2 hold (a new finding: the seal bull units behave as words for the bull).

## Results of the three-hundred-and-thirty-sixth set (added after the test; `predict_test336.py`, `results/predict_test336.md`)

All three failed, and the test found a flaw. Learned on the pictured seals alone (site-stratified), no unit qualifies
for the one-horned bull, so none can be carried to the tablets (BW2 fails). Inspection after the test: of the combined
pool's 27 Bull1 units, most occur on about 29 moulded tablets with the bull picture (for example 405, 501, 405 2, 240
520 and 2 _ 520 each on 29), which are probably copies of one mould design. The binomial criterion (sets 325-335)
counts each copy as an independent object, so one design weighs as 29 pieces of evidence; the picture shuffles break
the copies' shared picture and so do not correct it. The seal bull units are not shown to be words; they are largely
an artefact of mould copies. Next set: count each distinct text once. Progress: none (streak 1). Tally, counting parts:
1557 held, 1473 failed (3030 registered).

# Three-hundred-and-thirty-seventh set, registered before testing (25 September 2026): decipherment loop 162, the referent pool counted by distinct text (four hypotheses)

Streak 1. Set 336 found that the binomial criterion (sets 325-335) counts mould copies as independent objects, so one
design weighs as many observations. Correction: each distinct text (part-texts merged) is one observation, with the
majority picture and stratum of its objects; base rates, units (set 334's kinds, site-and-class strata, alpha 0.005)
and the FDR's within-stratum shuffles all over distinct texts; coverage on the real tokens as before
(`predict_test337.py`). A correction: lower figures replace the current ones (13.64%; 6.84% without Bull1 units); no
progress either way. Not measured before registering.

- **DT1** The FDR over distinct texts is at or below 10%.
- **DT2** Coverage is at least 13.64%.
- **DT3** Without Bull1 units, at least 6.84%.
- **DT4** Progress rule: none (a correction; recorded as failing).

## Results of the three-hundred-and-thirty-seventh set (added after the test; `predict_test337.py`, `results/predict_test337.md`)

All four failed. Counting each distinct text once (2,225 objects -> 1,438 distinct texts), the stratified binomial
configuration at alpha 0.005 finds 39 units (2 Bull1) and the shuffles about half as many: FDR 50.3% (DT1 fails);
coverage 1.09% (0.99% without Bull1 units). The growth of the line in sets 325-335 rested on copies counted as
independent objects. As registered, the lower figures replace the current ones: the tier 1 referent line is 1.09%,
with an FDR that no longer supports it. Two cautions: (1) signal across distinct texts exists (the split-halves of
sets 309, 326, 331 split by distinct text, and the vault excludes copies, all far above chance), so the strict
per-text binomial at alpha 0.005 may be underpowered; (2) collapsing every copy also merges independent evidence
(seals carved separately, copper tablets written one by one); only mould copies and seal impressions are true
duplicates. Next set: collapse only those. Progress: none (streak 2). Tally, counting parts: 1557 held, 1477 failed
(3034 registered).

# Three-hundred-and-thirty-eighth set, registered before testing (25 September 2026): decipherment loop 163, the referent pool with true duplicates collapsed (four hypotheses)

Streak 2. Set 337 collapsed every copy of a text, which also merges independent evidence: seals carved one by one and
tablets written by hand with the same text. Only objects from the same mould (moulded tablets, TAB:B) and seal
impressions (tags) are true duplicates. Here those are collapsed by text; seals, copper and incised tablets count as
separate objects; set 334's stratified binomial at alpha 0.005, FDR over the collapsed observations
(`predict_test338.py`). Registered now: the figure replaces set 337's 1.09% if its FDR is at or below 10% (otherwise
1.09% stands); not counted as progress, since the counting unit is re-decided after set 337. Not measured before
registering.

- **MC1** The FDR is at or below 10%.
- **MC2** Coverage is above 1.09%.
- **MC3** Without Bull1 units, above 0.99%.
- **MC4** Progress rule: none (recorded as failing).

## Results of the three-hundred-and-thirty-eighth set (added after the test; `predict_test338.py`, `results/predict_test338.md`)

Two held, two failed. With only mould copies and seal impressions collapsed (2,225 objects -> 2,002 observations), the
stratified binomial at alpha 0.005 finds 121 units (11 Bull1), coverage 3.43% (3.28% without Bull1 units; MC2, MC3),
but FDR 18.7% (MC1 fails): as registered, set 337's 1.09% stands. The bull units drop from 27 to 11 once mould copies
count once. A stricter alpha on this principled pool is the next test. Progress: none (streak 3). Tally, counting
parts: 1559 held, 1479 failed (3038 registered).

# Three-hundred-and-thirty-ninth set, registered before testing (25 September 2026): decipherment loop 164, the true-duplicate pool at stricter alphas (four hypotheses)

Streak 3. Set 338's pool (mould copies and impressions counted once, hand-made objects separately) failed the FDR at
alpha 0.005. Stricter alphas (0.0001, 0.0005, 0.001, 0.002): the alpha with FDR <= 10% and the largest coverage is
chosen, with the Linear B control (`predict_test339.py`). Not measured before registering.

- **MA1** An alpha with FDR <= 10% gives coverage above 1.09% (set 337).
- **MA2** Without Bull1 units, above 0.99%.
- **MA3** Linear B with it recovers 2+ of the 4 control words, none wrong.
- **MA4** Progress rule: MA1 and MA3 hold (the referent line uses the true-duplicate pool at that alpha).

## Results of the three-hundred-and-thirty-ninth set (added after the test; `predict_test339.py`, `results/predict_test339.md`)

All four held. On the true-duplicate pool: alpha 0.0001 62 units, FDR 0.5%, 1.49%; 0.0005 82, 2.1%, 2.28%; 0.001 93,
3.7%, 2.55%; 0.002 98, 6.8%, 2.80% (2.75% without Bull1 units). The rule chooses 0.002 (MA1, MA2); Linear B passes
(MA3). The referent line becomes 2.80%, nearly all of it for pictures other than the default bull: counting mould
copies once removes the bull question. `prizebench.referent_fixed` uses this pool. Progress: streak 0. Tally, counting
parts: 1563 held, 1479 failed (3042 registered).

# Three-hundred-and-fortieth set, registered before testing (25 September 2026): decipherment loop 165, split-half check of the true-duplicate configuration (three hypotheses)

Streak 0. Set 339's configuration (mould copies and impressions once, hand-made objects separately, site-and-class
strata, alpha 0.002) set the referent line at 2.80%. Independent check: five random half-splits of the distinct texts,
both directions, held-out matches against 200 joint shuffles; held-out precision (`predict_test340.py`). A validation:
a failure of TV1 downgrades the line; no progress either way. Not measured before registering.

- **TV1** The configuration is confirmed on the five split-halves (p < 0.05).
- **TV2** Its held-out precision is at least 14% (set 326).
- **TV3** Progress rule: none (validation; recorded as failing).

## Results of the three-hundred-and-fortieth set (added after the test; `predict_test340.py`, `results/predict_test340.md`)

One held, two failed (TV3 is the non-progress rule). On five split-halves both ways, the true-duplicate configuration's
units match 114 of 2,317 held-out observations' pictures against a shuffle median of 45 (p = 0.015; TV1): the 2.80% line
is confirmed. Held-out precision is 5% (TV2 fails): about 2.5 times chance, far below Linear B's 95% (set 310). Once
mould copies count once, what remains of the referent line is real but weak. (A first run failed on an empty stratum in
a half-split; a guard was added to predict_test334.units, c81ea3536, with no effect on earlier runs.) Progress: none
(streak 1). Tally, counting parts: 1564 held, 1481 failed (3045 registered).
