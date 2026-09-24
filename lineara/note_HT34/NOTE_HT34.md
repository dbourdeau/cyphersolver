# HT 34 and the values of the Linear A fraction signs H and A

*Draft research note, 23 September 2026. Daniel Bourdeau (cyphersolver project). Not submitted.*

## Summary

Corazza, Ferrara, Montecchi, Tamburini and Valério (2021) assigned H = 1/16 and A = 1/24 on structural grounds, and
Corazza (2024) keeps both as tentative. Line 3 of Haghia Triada tablet HT 34 (HM 22) is at odds with both values.

- It writes the amount **2 H K**. Under the descending order that the same authors take as a premise, that requires
  H > K. None of their admissible values of H exceeds K = 1/10.
- With their other values held fixed, no typologically attested value of H makes the line descending without
  duplicating an attested compound notation. That breaks their own Constraint 3.
- The tablet's settlement lines, as Younger reads them, also require F ≤ A. With A = 1/24 and F = 1/8 that fails.

The note does not propose new values. It asks for HT 34.3 to be re-examined, and for the decisive sequence on the
new Knossos handle KN Zg 58 to be taken into account (Kanta et al. 2025).

## 1. The proposal

Corazza et al. (2021) fixed J 1/2, E 1/4 and F 1/8. By constraint search and optimality metrics they fixed
B 1/5, D 1/6, K 1/10, L2 1/20, L3 1/30, L4 1/40 and L6 1/60. Among their 28 best solutions, H and A range over
1/16 to 1/84. They chose H = 1/16 and A = 1/24 for their low denominators and because 16 and 24 divide 240.
Corazza (2024, ch. 5) keeps "A = 1/24?, H = 1/16?". Both works state as a premise that fractions are written
cumulatively and "in order of decreasing value from left to right" (2021, pp. 1–2; 2024, ch. 5, p. 84). They also
state that one value is not written by both a sign and a combination (Constraint 3).

## 2. The reading of HT 34.3

HT 34 is a page tablet from the Villa Magazine at Haghia Triada (GORILA I, 64–65). Line .3 has a ligature
(*525, E+[·]) followed by **2 H K**. Three sources were consulted:

- the GORILA drawing;
- G. Douros's transcription as distributed by lineara.xyz;
- the SigLA database (Salgarella and Castellan).

All three agree on the order of the fraction signs. In SigLA's record, A706 (H) precedes A708 (K) on the same
line. In the drawing, the hooked sign H stands to the left of the T-shaped K. The published photograph is too
worn to add anything. Younger's commentary reads the line the same way ("E+[•] 2 H K").

## 3. The argument

**Order.** If 2 H K is one amount written largest first, then H > K = 1/10. Every value of H among Corazza et
al.'s best solutions (1/16, 1/24, 1/32, 1/36, 1/48, 1/64, 1/72, 1/84) is below 1/10.

**No admissible repair.** Hold the other published values fixed and search their own list of typologically
attested values. The only values of H that make line .3 descend are 1/3, 2/5, 3/20 and 3/10. Each is already
written by an attested compound under their values:

- D D = 1/3
- B B = 2/5
- K L2 = 3/20
- E L2 = 3/10

Constraint 3 therefore excludes all four. Freeing K as well gives a few thin solution families (K = 1/12 or 1/16),
too few to recommend. The search is in `lineara/fraction_constraints.py`.

**Settlement lines.** Younger reads lines .6–.7 as a settlement:

- SA+MU+KU 100, PA₃ 70, KI-RO 30 (a 7 after the 30 is erased; digital texts print 37);
- then E+KA K and PU F, which settle the items E+[·] 2 H K (.3) and QA₂+[?]+PU A (.4).

If PU F is the unsettled part of the item A, then F ≤ A. With A = 1/24 the remainder exceeds the item. This
argument rests on Younger's back-reference reading and is weaker than the order argument.

**Scale of the evidence.** Across the corpus, 29 undamaged adjacent pairs of fraction signs occur within single
entries. The 2021 values contradict three of them:

| Pair | Where | Status |
|---|---|---|
| H K | HT 34 | firm reading |
| A B | KH 86 | GORILA and SigLA read A B B; Corazza et al. read A A |
| E J | ZA 8 | already flagged by them as doubtful |

The older values (B = 1/3) fail on KH 9 (E B), which the 2021 values fix.

The three exceptions fall under three different commodity contexts: grain, cyperus, and none. HT 34's is the only
pair in the corpus containing both H and K. A commodity-specific value for H, such as a grain unit, therefore
cannot be tested and does not explain the exception.

The literature check covered the works citing the 2021 paper and Corazza (2024). E. Salgarella, *Writing in Bronze
Age Crete* (Cambridge 2025), is closed access and has not been checked for a discussion of HT 34.

## 4. What could give way

1. HT 34.3 is a scribal inversion, like the doubtful E J cases.
2. 2 H K is not a single amount. Younger's reading, in which 2 H was delivered and K is outstanding, still writes
   it as one.
3. H and A are larger than the published values: between 1/10 and 1/2, and then not a unit fraction already
   covered by a compound. Alternatively, K is smaller than 1/10.

Only option 3 touches the published system, and it touches only the two values its authors mark as tentative.
B, D and the L series are unaffected.

## 5. New evidence to come

Kanta, Nakassis, Palaima and Perna (2025) report that Face δ of the ivory handle KN Zg 58, from the Anetaki cult
centre at Knossos, records six different fraction signs in sequence. They say this gives "a different sequence of
values than those suggested until now", but the sequence itself is reserved for the final publication. That
sequence, and a photograph or autopsy of HT 34.3, would decide between the options above.

## Requests

- A photograph of HT 34 (HM 22), line 3, at a resolution that settles the order and identity of the signs after
  the numeral 2.
- The KN Zg 58 fraction sequence, when published, compared with the ranking implied by HT 34.

## References

- Corazza, M., Ferrara, S., Montecchi, B., Tamburini, F. and Valério, M. 2021. The mathematical values of fraction
  signs in the Linear A script: a computational, statistical and typological approach. *Journal of Archaeological
  Science* 125, 105214. https://doi.org/10.1016/j.jas.2020.105214
- Corazza, M. 2024. *Computational methods for undeciphered scripts*. Bologna University Press.
  https://doi.org/10.30682/9791254774038
- Godart, L. and Olivier, J.-P. 1976–1985. *Recueil des inscriptions en linéaire A* (GORILA), vol. I, 64–65.
- Kanta, A., Nakassis, D., Palaima, T. G. and Perna, M. 2025. An archaeological and epigraphical overview of some
  inscriptions found in the Cult Center of the city of Knossos (Anetaki plot). *Ariadne* 27–43.
  https://doi.org/10.26248/ariadne.vi.1841
- Salgarella, E. and Castellan, S. SigLA: the signs of Linear A. https://sigla.phis.me/
- Younger, J. G. Linear A texts in phonetic transcription and commentary, HT 34.

## Reproduce

`python lineara/fraction_order.py` and `python lineara/fraction_constraints.py`. The order pairs and every tested
value set are in `fraction_order_results.json` and `fraction_constraints_results.json`.
