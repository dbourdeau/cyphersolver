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
