# Van Dedem (Constantinople) to Van de Spiegel, 1788–1793 — DECODE R2120, R2122, R2131

**5 Nov 2026, code 2704 corrected (issue #244, EscalatorStudios).** Our key table had 2704 as "anno 2 voorige jaar" (a faded
indicator). On Nationaal Archief scan 0004 of inv. 785 the cell of "te meer" (2701), row 4, holds a faded abbreviated
entry that reads *ann.t 2 voorige Car.s*: "annuleert 2 voorige caracters", an instruction to cancel the 2 preceding
characters, not a date word. Checked on the scan (service.archief.nl render of scan 0004; the scans are not kept in the
repository); `key/kroll785_values.tsv` and `tx/R2122_decode.txt` updated (`research/reading_audit/b19_dedem_decode.py`).
No reading changes: 2504 2604 2704 stay the unread opening markers (begin des briefs, blank slot, cancel 2 preceding).
Not verified: the reporter's comparison entry 1429 on scan 0002 (the faded "einde des Briefs" mark sits on the ruled line
above the written 1430 row, but we did not settle which column it belongs to); whether the instruction really cancels
2504 and 2604 in the opener is a hypothesis, nothing in R2122 tests it (R2053 and R2121 open the same way).

**23 Oct 2026, re-read (REREAD_BRIEF, batch b19): the codebook found; R2122 and R2131 read.** The legation
inventory lists under Kroll (chargé 1784-85) **NA 1.02.20 (legatie Turkije) inv. 785**, "Sleutel geheimschrift": its six
scans on the Nationaal Archief site are the codebook itself, headed "Kroll. Un Chiffre" (500-group pages of five
columns of 100, words alphabetical across the rows, letters and syllables at the foot of each column, titles in
3001-3500, a Nota on noun and preterite forms). It is this code: the slot model below had found its layout, and its
A-grade values recur. inv. 686 (De Weiler's cipher, 1775) holds the "Berigt" on begin/einde des briefs markers and
nulls. Every group of R2122 and R2131 looked up on the scans (`key/kroll785_values.tsv`); cipher re-read on the DECODE
images (R2131: 2261 -> 2262, 311 -> 317?). Both letters now read: `tx/R2122_reading.md`, `tx/R2131_reading.md` (with
`_en.md`), log `tx/R2122_R2131_reread_log.md`. R2131: the Porte bound itself to the Prussian envoy to stay neutral in
the war with France and to make no further alliance with her. R2122: Van Dedem's demarches after the resolution of
2 October, the Porte's wish for a loan negotiation in the Republic passed to the Prussian envoy, a sharp portrait of
the English ambassador, a Swedish subsidy. About 14 groups give no sense where they stand (named in the readings).
Clean-sentence share: 0.22 / 0.20 on the checker's modern Dutch list, 0.93 / 0.80 counting explicit holes only
(period spelling). Method by part: R2120 from its contemporary decipherment; R2122/R2131 with the codebook found in the
archive. fraction_read 1.0.

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
R2120 **reads** from its contemporary clear decipherment (`tx/R2121_clear.txt`, continuous Dutch; English translation
still to be written). R2122 and R2131 are **decoded, not read**: the graded decode has holes in nearly every clause
(4 of 113 sentences clean, `docs/_check_reading.py`). Method now read from existing decipherment (R2120), parts for
the rest; the 41% firm-value figure is withdrawn as a reading figure (0.673 = R2120's share of the groups).

Status: in progress (all three letters read: R2120 from its contemporary decipherment, R2122 and R2131 with Kroll's codebook NA 1.02.20 inv. 785, 23 Oct 2026; write-up pending)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): R1895 (26 Aug 1799, to the Burger Agent
van der Goes) is in a different marked system, not this 1788–93 code, and is now its own entry, a different cipher
with its own page: `../dedem1799/` (`docs/dedem1799.html`). Its row is kept in the table below for the record.

Catalogue entry 225. F.G. van Dedem tot de Gelder, Dutch ambassador at Constantinople, to Grand Pensionary
L.P. van de Spiegel (NA 3.01.26 inv. 212: R2120, R2122, R2131) and to the Agent van Staat M. van der Goes
(NA 2.01.08 inv. 346: R1895). Images fetched with the DECODE cookie (git-ignored in `img/`).

## What each record is

| Record | DECODE date | What it is | State |
|---|---|---|---|
| R2120 | 1788-10-11 | Two cipher pages of the despatch signed Pera, 22 Dec 1788 (DECODE date is wrong). The same two pages are photographed again in R2121 (P5 = R2120 P1, P1 = R2120 P2). | **Read at the time**: R2121 pp. 2–4 is the full clear decipherment ("Missive van den Heer van Dedem … 22 December 1788"): the Porte's proposed loan of 7–8 million, secured on the revenues of Morea, Negropont, Salonica, Volos, Urfan, Cara Agatz, Damascus, Sorien and Rodosto and the tribute of Jenischeher; Dedem suggests the Levant Directors or Hope & Co. take it up. Transcribed: `tx/R2121_cipher.txt`, `tx/R2121_clear.txt`. |
| R2122 | 1789-01-15 | "Duplicaat", Pera 15 Jan 1789: two cipher blocks (258 groups) in a clear letter. | Decoded in part (second pass): 107 of 255 non-null groups with firm values. `tx/R2122_cipher.txt`. |
| R2131 | 1793-02-09 | One cipher paragraph of 50 groups (framed by 701 … 301) in a clear letter. | Decoded in part (second pass): 16 of 46 non-null groups with firm values. `tx/R2131_cipher.txt`. |
| R1895 | 1799-08-26 | No. XVIII, "Duplicaat", to the Burger Agent: 2–3-digit groups with superscript marks (×, ″, ¯, ~); P1 is an unrelated clear page signed Schimmelpenninck. | Unread; a different (Croiset-style marked) system from the 1788–93 code. |

## The 1788–93 code

- Numbers 2–3839, one group ≈ one Dutch or French word, **heavily homophonic** ("de" 36× in R2121's clear, no
  group more than 11×; 541/641/841/941 all frequent). Not alphabetical in any test (welke≈2888, landen≈1277, als≈17). [Superseded 4 Oct 2026: alphabetical within 500-group blocks once the groups are re-indexed by column; see "Second pass".]
- Fixed opener 2504 2604 2704 (R2120, R2122, R2053; begin des briefs, blank slot, "annuleert 2 voorige caracters") and 701 801 … 301 401 501 601 frames (R1947, R2131): nulls/indicators.
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
   consistent key either. No reliable code values, so no reading of R2122/R2131 is offered. [Superseded 4 Oct 2026 by the second pass below.]

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

## Outcome (21 Oct 2026)

Profile set to key recovered based on adjacent plaintext, read in part: the block-alphabetical layout was recovered
from the sibling decipherments in the same file, and 123 of the 301 non-null groups of R2122 and R2131 (41%) carry a firm
value (grades A, B, T in `alpha/decoded_targets_v2.txt`). The running reading is fragmentary; values, not sense.

## Remaining gaps

- R2122 and R2131: about 14 groups whose codebook value gives no sense where they stand (R2122: 1230, 1330 twice, 80, 760 twice, 3928, 1605, 1463, 2622; R2131: 319, 591) and 4414 (no such code) - blocker: too-short; each occurs once or twice, too few to establish another value (probably clerk slips: 319 for 314 "alle"; 760 the Nota's example number copied for a "g" character)

Closed 23 Oct 2026 (consistency pass): R2120's English translation is written (`tx/R2121_en.md`, translation wave of 23 Oct 2026); the not-attempted gap was stale.

## Escalation

- [x] siblings: R2121, R1947, R2053 transcribed and aligned (first pass); layout derived from them (second pass)
- [x] clear-pages: R2121's clear decipherment used as the crib
- [x] known-keys: Fagel key series R2842-R2852 compared (first pass): not this code
- [n/a] print: Boon (2012) not checked (not online)
- [x] key-rebuild: alphabetical-slot model, 354 values
- [x] retry: R2122/R2131 rerun with the slot model; Codex adversarial review
- [x] key from archive (23 Oct 2026): Kroll's codebook NA 1.02.20 inv. 785 found and read; R2122, R2131 decoded and read with it


## Croiset's cipher-office papers located (23 Oct 2026)

The codebooks every pass here has wanted are catalogued in the Croiset family archive, **NA 2.21.045, section A.7.b**
"Secretaris van het cijfer van de Staten-Generaal en secretaris van het cijfer van de Staat, 1789-1810"
(Samuel Egbert Croiset, 1734-1816):

- **inv. 18**: correspondence with Dutch envoys about setting cipher codes, *with letters in cipher and code tables*.
- **inv. 21**: cipher codes with notes, covering letters and instructions to envoys on keeping them secret.
- **inv. 22**: incoming letter from W.F. Röell (Louis Napoleon period).
- inv. 17: diary notes on his work.

All are `PHYSICAL` (not scanned). They can be reached through the Nationaal Archief's paid scan-on-demand service or
a reading-room visit. That is an outside blocker, but a lifted one is likely to give the key outright. Found by the sweep in
`research/nationaal_archief/`.
