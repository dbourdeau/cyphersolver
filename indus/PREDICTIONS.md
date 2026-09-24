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
