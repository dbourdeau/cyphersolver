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
