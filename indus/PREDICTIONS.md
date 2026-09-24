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
