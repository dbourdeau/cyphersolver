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
