# Linear A: fraction signs against written order and HT 34

23 September 2026, third pass. Status: in progress. No lexical reading is claimed. This pass tests a published
numerical decipherment, the values of the fraction signs, rather than the language.

## Why fractions

The first pass left fractions out of every arithmetic test. Fractions are the one part of Linear A where a
cipher-style method applies directly: the signs have numerical values, the tablets carry sums, and the
writing convention (largest value first, as with integers) gives order constraints. They also matter for any
reading of the accounts, because a wrong fraction value turns a balanced list into an apparent error.

Only 11 KU-RO records contain a fraction sign, and only one of them gives a clean equation: HT 104,
45 J + 20 J + 29 = 95, so J + J = 1 (already Bennett's argument). HT 9a and HT 13 do not balance under any value of
J (HT 13 was noted by Younger). HT 123+124a's olive total balances for every J. Totals alone cannot fix the
fraction system.

## Written order, measured blind

`fraction_order.py` collects every undamaged run of fraction signs inside one editorial entry (296 runs, 42 with
two or more signs) using sign identities only. The corpus's own English fraction glosses were not read. It
then finds the value ranking that contradicts the fewest adjacent pairs (exact search over subsets).

A first version joined adjacent entries across line breaks. That produced false pairs on HT 8b (J | J) and
HT 60 (K | E), and they were removed by treating each newline as an entry boundary. Two single-entry
exceptions remain: ZA 8.4 E J and PH 9b J J. KE Wc 2 "D | B B" is two entries, and the object may be a weight
inscribed with mina signs (Younger), so it gives no D/B evidence.

29 adjacent-pair tokens survive. They admit a zero-violation ranking only if E > J, which rests on ZA 8 alone.
The data are too sparse to rank the signs unaided. They can, however, test published value sets.

## The published values, scored

Values were then taken from the literature (read after the order data were fixed): the Bennett-type values
carried as glosses in the working corpus, and
[Corazza, Ferrara, Montecchi, Tamburini and Valério 2021](https://doi.org/10.1016/j.jas.2020.105214)
(J ½, E ¼, F ⅛, H 1/16, A 1/24, B 1/5, D 1/6, K 1/10, L2 1/20, L3 1/30, L4 1/40, L6 1/60).

| Value set | Order pairs broken | HT 34 F ≤ A |
|---|---|---|
| Bennett-type glosses (B ⅓, A ≈ H ≈ ⅙, K 1/16) | E B (KH 9, firm); A B (KH 86, disputed); E J (ZA 8, doubtful) | holds |
| Corazza et al. 2021 | **H K (HT 34, firm)**; A B (KH 86, disputed); E J (ZA 8, doubtful) | **fails** |
| Corazza et al., alternative B ⅙ / D ⅕ | same as above | fails |

KH 9 "E B" rules out B = ⅓, which is how Corazza et al. moved to B = 1/5. The sets differ on H, A and K.

### HT 34

HT 34 is a Haghia Triada page tablet. Line .3 has a ligature (*525, E+[·]) with the amount **2 H K**. Lineara
(GORILA via Douros), SigLA (A706 then A708 on one line) and the GORILA drawing all agree on the order: the hooked
H, then the T-shaped K. Under the largest-first convention, H > K. Corazza et al. allow H only values of 1/16 and
below (their 28 best solutions give H between 1/16 and 1/84), and K = 1/10. Every one of those makes line .3
ascend.

The tablet is also self-referring. Younger reads line .6 as SA+MU+KU 100, PA₃ 70, KI-RO 30: 100 − 70 = 30, with a
7 erased after the 30 (the working corpus prints "37"; the erasure is lost). The last two lines, E+KA K and PU F,
settle two earlier items: E+[·] 2 H K on .3 and QA+[?]+PU A on .4. If PU F is what remains of the item A, then F ≤ A.
Younger drew this inference himself ("F (1/8) is smaller than A"). With Corazza's A = 1/24 and F = 1/8, the
remainder exceeds the item. This test depends on Younger's back-reference reading, so it is marked interpretive.

### Can the system absorb HT 34?

`fraction_constraints.py` fixes Corazza et al.'s other values and searches their own list of typologically
attested fractions for A and H (and then K). It checks the firm order pairs, then adds the HT 34 F ≤ A test, then
the disputed KH 86 reading. Their Constraint 3 (one value, one notation) is applied optionally to attested
compound notations as well.

| Free signs | Constraint 3 on compounds | Evidence | Solutions |
|---|---|---|---|
| A, H | no | firm order | 48; H ∈ {3/20, 3/10, 1/3, 2/5} |
| A, H | **yes** | firm order | **0** |
| A, H, K | yes | firm order | 54; K ∈ {1/16, 1/12, 1/10}, H ∈ {1/12, 1/10, 3/20} |
| A, H, K | yes | firm + HT 34 F ≤ A | 3; A = 3/20, H ∈ {1/12, 1/10}, K ∈ {1/16, 1/12} |
| A, H, K | yes | + KH 86 A B | 0 |

All four H values that pass the order test collide with notations already attested under Corazza's values: D D
= ⅓, B B = ⅖, K L2 = 3/20, E L2 = 3/10. **With K = 1/10 and their own uniqueness constraint, no typologically
attested value of H allows HT 34.3 to be written largest first.** At least one of these must give way:

1. HT 34.3 is a scribal exception to the descending order, like the doubtful E J cases they already set aside;
2. "2 H K" is not one compound amount (Younger's settlement reading splits it into 2 H delivered and K
   outstanding, but still writes it as one amount);
3. K is not 1/10, or H is not below 1/16. Freeing K yields small solution families, too thin to propose values.

Corazza et al. state that optimality did not fix H and A, and that they chose H = 1/16 and A = 1/24 on
palaeographic and structural grounds. Those are the two values this test disputes. Their B, D and L-series
values are untouched by this evidence. Only 29 order pairs exist, so this is a pointed counterexample, not an
alternative system.

Literature check (fifth pass, LEADS_REPORT.md): none of the 18 works citing the 2021 paper revises the values.
Corazza's 2024 book (*Computational methods for undeciphered scripts*, ch. 5) repeats A = 1/24? and H = 1/16? as
tentative and does not discuss HT 34. Salgarella 2025 was not checked (not open access).

## Data notes for the working corpus

- HT 34.6: the corpus gives KI-RO "37"; GORILA/Younger have 30 with an erased 7. Any arithmetic on the corpus
  string reads 37.
- KH 86.2: lineara and SigLA read A B B; Corazza et al. read A A.
- ZA 8 has no fraction attestations in SigLA, so its E J cannot be cross-checked there.

## Reproduce

```
python lineara/fraction_order.py
python lineara/fraction_constraints.py
```

Output: `fraction_order_results.json`, `fraction_constraints_results.json`. The HT 34 and KH 86 GORILA drawings
come from the pinned lineara.xyz commit into the ignored `data/` cache (images © École française d'Athènes).
