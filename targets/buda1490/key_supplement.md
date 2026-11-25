# Key of DL 46150: supplement to key.json and key.md

Added 16 Nov 2026 by the decrypt audit (`research/decrypt_audit/`). `key.json` and `key.md` are written by
`scripts/build_key.py` and read by `measure.py` and `scripts/regrade.py` (which grades a word by whether key.json
alone gives it), so they are left as they were. This file holds what the reading uses and those two files do not
carry in a form that can be applied to `transcription/p1.txt`-`p4.txt` token by token. Nothing here is new: every
row is copied from the file named in its source column, and the counts were recounted from
`scripts/data/alignment.json` against the transcription.

## 1. Values used by the reading and absent from key.json / key.md

`key.json` accepts a value only with 2 or more aligned cases and 4% of the sign's cases, so these were left out of
it; the retry pass of 30 Oct 2026 adopted them in `measure.py` only.

| sign | value | n | where | source |
|---|---|---|---|---|
| `qA` | i | 4 | circa, ipsam, animo, additione | `measure.py` line 39 (`EXTENDED`); NOTES "Retry pass (30 Oct 2026)"; key.json `qA.aligned_counts` i: 4 |
| `qA` | t | 3 | affinitatem (spelt afinitatem), inter, debeat | `measure.py` line 39 (`EXTENDED`); NOTES "Retry pass (30 Oct 2026)"; key.json `qA.aligned_counts` t: 3 |
| `y` | code: ducenta milia | 1 | P3L02 | `measure.py` line 40 (`EXT_CODE`); NOTES "The system", code signs; key.json `y.aligned_counts` |
| `y` | code: ducentorum milium | 1 | P3L12 | `measure.py` line 40 (`EXT_CODE`); NOTES "The system", code signs; key.json `y.aligned_counts` |

`y` stands three more times with no value (once at the tt of admittendas, twice with no counterpart): open, see
NOTES "Remaining gaps".

## 2. From transcription tokens to the units the key is written in

The transcription writes one token per shape. `key.json` and `key.md` give values for units, nine of which are not
transcription tokens. The rules are those of `scripts/ext/em_align.py` lines 8-20 (`units`), with the sets
`U` = qB, qA, M, oo, ooA, ooB and `USIGN` = qB, M, oo, ooA of `scripts/dec14.py` lines 10-11; they are stated in
words in `transcription/signs.md` line 9. Applied in this order, left to right:

| tokens in the transcription | condition | unit in the key | value | n | source |
|---|---|---|---|---|---|
| `o H` | the next token is in U | `oH` | q | 23 | em_align.py line 12 |
| `H o` | none | `Ho` | p | 31 | em_align.py line 13 |
| `6 gA` or `6A gA` | none | `LL` | ll | 10 (5 and 5) | em_align.py line 14 |
| `G a` | none | `Ga` | code: affinitas | 4 | em_align.py line 15 |
| `G p` | none | `Gp` | code: non | 3 | em_align.py line 15 |
| `v e` | none | `ve` | code: Illustrissimus Princeps / Dominus (meus) | 6 | em_align.py line 16 |
| `O` | the unit before it is in USIGN | `Om` | m | 6 | em_align.py line 17 |
| `n` | the next token is in U | `nq` | q | 25 | em_align.py line 18 |
| `n` | otherwise | `ni` | i | 3 | em_align.py line 18 |

A token ending in `?` is the same sign read with doubt; `??` and a lone `?` are a sign lost to damage (14 tokens).
With these rules the 3,199 tokens of the four pages make the 3,122 units of `scripts/data/alignment.json`
(recounted 16 Nov 2026: token for token the same).

## 3. What a key table alone cannot give

- A sign with several values (`qB` u/s/f, `ooA` u/s, `3` n/g, `tp` b/a, `gA` o/t, `s` h/f, `qA` s/i/t) takes at each
  place the value the alignment with the Milan minute chose; the key does not say which.
- A code sign (`ff`, `ve`, `Tx`, `Ga`, `dt`, `dx`, `K`, `Gp`, `fo`, `y`) is printed in the reading in the case form
  and extent the minute has at that place (`ff` = Serenissimum Dominum Regem Hungarie, Serenissimus Dominus Rex,
  Serenissimo Domino Rege ...; `Ga` once "Affinitas Serenissimi Domini Regis"; `dt` once "quod ab"). The forms are
  listed in `key.json` under `values`; which one stands where comes from the minute (NOTES "The minute as evidence").
