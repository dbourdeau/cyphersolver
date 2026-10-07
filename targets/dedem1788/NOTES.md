# Van Dedem (Constantinople) ciphers 1788–1799 — DECODE R1895, R2120, R2122, R2131

Status: attempted, open (R2120 found read at the time; R2122, R2131 partly read after the code layout was established on 4 Oct 2026, see "Second pass"; R1895 unread)

Catalogue entry 225. F.G. van Dedem tot de Gelder, Dutch ambassador at Constantinople, to Grand Pensionary
L.P. van de Spiegel (NA 3.01.26 inv. 212: R2120, R2122, R2131) and to the Agent van Staat M. van der Goes
(NA 2.01.08 inv. 346: R1895). Images fetched with the DECODE cookie (git-ignored in `img/`).

## What each record is

| Record | DECODE date | What it is | State |
|---|---|---|---|
| R2120 | 1788-10-11 | Two cipher pages of the despatch signed Pera, 22 Dec 1788 (DECODE date is wrong). The same two pages are photographed again in R2121 (P5 = R2120 P1, P1 = R2120 P2). | **Read at the time**: R2121 pp. 2–4 is the full clear decipherment ("Missive van den Heer van Dedem … 22 December 1788"): the Porte's proposed loan of 7–8 million, secured on the revenues of Morea, Negropont, Salonica, Volos, Urfan, Cara Agatz, Damascus, Sorien and Rodosto and the tribute of Jenischeher; Dedem suggests the Levant Directors or Hope & Co. take it up. Transcribed: `tx/R2121_cipher.txt`, `tx/R2121_clear.txt`. |
| R2122 | 1789-01-15 | "Duplicaat", Pera 15 Jan 1789: two cipher blocks (258 groups) in a clear letter. | Unread. `tx/R2122_cipher.txt`. |
| R2131 | 1793-02-09 | One cipher paragraph of 50 groups (framed by 701 … 301) in a clear letter. | Unread. `tx/R2131_cipher.txt`. |
| R1895 | 1799-08-26 | No. XVIII, "Duplicaat", to the Burger Agent: 2–3-digit groups with superscript marks (×, ″, ¯, ~); P1 is an unrelated clear page signed Schimmelpenninck. | Unread; a different (Croiset-style marked) system from the 1788–93 code. |

## The 1788–93 code

- Numbers 2–3839, one group ≈ one Dutch or French word, **heavily homophonic** ("de" 36× in R2121's clear, no
  group more than 11×; 541/641/841/941 all frequent). Not alphabetical in any test (welke≈2888, landen≈1277, als≈17). [Superseded 4 Oct 2026: alphabetical within 500-group blocks once the groups are re-indexed by column; see "Second pass".]
- Fixed opener 2504 2604 2704 (R2120, R2122, R2053) and 701 801 … 301 401 501 601 frames (R1947, R2131): nulls/indicators.
- The same code is used in the deciphered R1947 (8 Nov 1789, French annex + solution) and R2053 (1 Dec 1789,
  French + solution), both transcribed here (`tx/R1947_*`, `tx/R2053_*`).

## What was tried

1. Keys: the undated Fagel key series (DECODE R2842–R2852, "Cijffers zonder bestemming, ongedateerd–1793") are
   large alphabetical Dutch codebooks (R2843: the a–ad words alone reach 600+ codes), not this code. No other
   DECODE key record for the Turkish legation.
2. Crib alignment: R2121 (629 groups, Dutch), R1947 (498, French), R2053 (196, French). Only 58% of R2122's and
   52% of R2131's groups occur anywhere in the cribs at all, and French/Dutch cribs share only 17% of groups.
   Hard-EM and leave-one-out word aligners (`walign.py`, `walign2.py`) converge to near-diagonal paths with no
   consistent group→word values; a "hundreds digit is a dummy" reduction (`walign3.py`) did not produce a
   consistent key either. No reliable code values, so no reading of R2122/R2131 is offered.

## What would move it

The codebook itself (Van Dedem's legation papers, NA 1.02.04 legatie Turkije; or Croiset's lost working sheets),
or more deciphered Dutch letters in the same code: DECODE R1948–R1952 (Kroll 1784–85), R2134 (Van Haeften 1776),
R2141 (Schenck 1777) have solutions and could be transcribed as further cribs, though they may be in French.
Henk Boon, *Frederik Gijsbert baron van Dedem. Onze man in Constantinopel* (2012) was not checked.

## Second pass (4 Oct 2026, contributed by Feyseel Nur, PR #21): alphabetical within 500-group blocks

Within each block of 500 groups (thousands T, hundreds H) the code follows the alphabetical order of the Dutch/French
words once groups are re-indexed as `T·1000 + (H≥5)·500 + line·5 + (H mod 5)` (line = last two digits): entries filled
row-wise across five columns, numbered down the columns. Frequent words fill whole rows (en = 541/641/741/841/941; de =
85/185/285/385/485/86 …); e.g. 537 egter, 837 eindelijk, 541-941 en, 543 engagement, 643 engager, 644 entrer.

Evidence (OpenAI Codex's independent re-derivation, `alpha/codex_review/`): 95 re-aligned crib pairs give within-block
Spearman 0.799 for this layout, against 0.351 numeric order, 0.567 four columns, 0.645 six columns; the early unfiltered
pairs give 0.602; null (10,000 permutations, max over 7 layouts) p99.9 = 0.368. Five columns also wins globally (0.874
vs 0.828 for ten; within a block ten columns gives the same ranks). Not established: physical sheets, a single list,
the ~3150 boundary of names/titles. The first-pass "94% leave-one-out" figure leaked held-out values and is withdrawn.

Table: `alpha/dedem_alpha_table.tsv`, 354 values graded A/B/C (agrees with the first-pass table on 127 of 155 values,
moves 39 out-of-slot ones, e.g. 2748 vijftig, 1768 op, 811 deze). Readings with every word graded and the alphabetical
bracket of each unknown: `alpha/decoded_targets_v2.txt`. Codex word verdicts (S solid, P plausible, X speculative):
R2131 PORTA[S] … aan[S] [den][X] ENVOYÉ[P] verklaard[X] … heeft[P] om[S] gedurende[P] deze[P] Oorlog[S] met[S] de[S]
Franschen[X] en[S] sig[P] in[P] … neutraliteit[X] te[S] houden[P] — the neutrality reading is not established; R2122
ENVOYÉ[P] het[S] verlangen[X] en[S] van[S] PORTA[S] ontrent[P] het[S] doen[P] een[S] -er[X] negociatie[X] … Republicq[P]
niet[S] geheel[S] te[S] … ignoreren[S] (loan theme consistent with the R2121 crib). Independent witnesses: 1764 Oorlog
(R2121 #486), 1518 met (R2121 #10), 86 de (R2053 #5), 3373 Porta (R2121 #180), 3273 Porte Ottomanne (R1947 #42), 3610
envoy title (R1947 #407, R2053 #9).

## Remaining gaps

- R2122 and R2131: groups with no attested value (graded "-" or "?" in `alpha/decoded_targets_v2.txt`); the alphabetical bracket narrows each but does not fix it - blocker: open-codes; more deciphered letters in this code (DECODE R1948-R1952, R2134, R2141) would test the layout on unseen text.
- R1895 (1799, to the Burger Agent): a different, marked system - blocker: no-key-material.

## Escalation

- [x] siblings: R2121, R1947, R2053 transcribed and aligned (first pass); layout derived from them (second pass)
- [x] clear-pages: R2121's clear decipherment used as the crib
- [x] known-keys: Fagel key series R2842-R2852 compared (first pass): not this code
- [n/a] print: Boon (2012) not checked
- [x] key-rebuild: alphabetical-slot model, 354 values
- [x] retry: R2122/R2131 rerun with the slot model; Codex adversarial review

