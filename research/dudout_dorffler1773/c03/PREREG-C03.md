# PREREG C03 — dorffler-1686 (catalogue Bourdeau 1773), written 2026-11-12 BEFORE any Fable call, any table, any 476 transcription

Supersedes the measurement part of ../PROTOCOLE-C02.md (b235a9ed…) for C03: new protocol, new hash, never retroactive.
Reason for the change of threshold (0.85 -> 0.75): both sides are noisy (the 1689 clerk's gloss is itself partial and
read by us at about 80-90 %; homophonic syllables spell German loosely); the margin over controls (+0.30) is kept.

## Split (fixed now)
- TRAINING = img. 470, 475, 467, 468 of SE/RA/2115/I/19/102 (R0003596). Only these are sent to Fable (crops of the
  cipher zones, make_crops.py) with ../working/T-train-v1.txt (SHA-256 9fa9e0ec…725307) and OPUS-ESSAI.md.
- HELD-OUT = img. 476, ENTIRE (both pages, all cipher and all gloss). Never sent to any API, never used to build or
  correct the table, never decoded before the measure. Checked before sending: FORBIDDEN regex of fable_run.py on
  every file name + check_leak.py (0 leaks, and a positive control that must be flagged).

## Order (fixed now)
1. This PREREG + measure.py + check_leak.py are hashed (SHA256SUMS) before the package is sent.
2. While Fable runs (its output unread): blind transcription of the CIPHER of 476 only, in blocks (a block = one
   continuous cipher zone between clear-text runs; ids @476L-1, @476L-2 …, @476R-1 …), file
   ../working/T476-cipher-v1.txt, frozen by SHA-256 before Fable's output is opened. The gloss of 476 is not read.
3. Table: Fable's proposal, checked by us on a sample of the TRAINING images only (alignment spot checks, see §Check),
   corrected on TRAINING evidence only, written as TABLE-C03.json and frozen by SHA-256.
4. After the table is frozen: reading of the 476 GLOSS alone (plain German, no decoding), each gloss line attached to
   the block where it physically lies; file ../working/G476-gloss-v1.txt, frozen by SHA-256.
5. ONE run: `python3 -I measure.py TABLE-C03.json T476-cipher-v1.txt G476-gloss-v1.txt`. Result recorded as it is.

## The single measure
S = 1 − Σ_b lev(D_b, G_b) / Σ_b max(|D_b|, |G_b|) over the glossed blocks b of 476, where D_b = the frozen table applied
to the block's groups (unknown or unreadable group -> '#', which never matches), G_b = the block's gloss, both
normalised (lower case, a-z only, ä/ö/ü -> a/o/u, j->i, y->i, v->u, dt->t, th->t, ck->k, tz->z, c->k, doubled letters
collapsed). Controls: 500 tables = the frozen table with its values permuted at random among its keys
(seed 20261112) — same groups, same value inventory, wrong assignment.
**PASS = S ≥ 0.75 AND S ≥ max(controls) + 0.30.** Anything else = FAIL: no PR, no reading of unglossed parts with this
table, failure documented. No second measure on 476 with a modified table.

## Check of Fable's alignment (before freezing; training images only)
At least 3 crops from at least 2 different images, ≥ 60 groups: for each, we read the image ourselves and score how
many of Fable's (word, group index) anchors we confirm. If < 70 % confirmed, the table is still frozen and measured
(the measure is the arbiter), but the check result is reported.

## Count (Daniel's 95 % rule) if PASS
- Glossed passages = "existing decipherment (partial contemporary interlinear)"; our contribution = the key and the
  reading of unglossed passages (470 left 9 lines, 468 left, 475 right, others found).
- Unglossed passages: word-by-word sheet — sure / probable {x} / restored [x] / unresolved ‹…›, each non-sure
  justified; proposed for publication only if ≥ 95 % of the words are read by the sense on a portion ≥ 300 characters.
