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
