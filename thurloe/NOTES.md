# Intercepts by the Commonwealth (Thurloe State Papers, 1653-56) — cryptiana unsolved item #9

Four undeciphered pieces printed in Birch's *Thurloe State Papers* (1742), full text on British History Online.
Ciphertexts extracted to `a_*.txt` … `d_*.txt`; analysis in `analyze.py` (`analyze_out.txt`), key trials in
`apply_keys.py` (`apply_keys_out.txt`; keys harvested from cryptiana into `keys/`), solvers `solve_a*.py`
(outputs `solve_a2_*.txt`), LMs `lm_nl.json`, `lm_fr.json` (`lm_build.py`).

| | letter | size | type | verdict |
|---|---|---|---|---|
| a | Beverning & Vande Perre → Boreel (Paris), Westminster 1 Sept 1653 NS; TSP i.435 | 136 groups, 33 distinct: letters 6-33 (25 symbols), codes 113 117 211 222 327 329 519 527 | monoalphabetic letters + small nomenclator; plaintext Dutch (or French) | **stuck** |
| b | du Gard's "new direction" enclosed to White, Brussels 10 June 1656; TSP v.78 | 22 symbols incl. letters q t y m f | cover address; too short | stuck |
| c | anon., Brussels 12 Aug 1656 → Copinger; TSP v.267 | 16 single digits (`2 3 1 4 7 4 6 4 9 7 2 3 is come … to visit the 0 9 3 7`) | a name + a 4-letter word in a 10-symbol cipher | stuck |
| d | Jo. Waddall (London) → "Vanyeare", Bruges, 22 Aug 1656; TSP v.337 | 50 groups, 29 distinct, letters 7-86 + codes 226 243 | homophonic letters + codes; English | stuck |

## What was tried
- **Key matching** (`apply_keys.py`): every 1653-60 royalist/Commonwealth key on cryptiana (Marshall 1656-58,
  Barwick-Hyde 1659-60, Stamford 1655, Butler 1656, Charles II intercepted 1655, Kingston 1658, Westrope 1655,
  Hague agent/Blake) applied to (a)-(d), scored by English/Dutch/French quadgram log-prob. Nothing readable;
  best per-quad scores -4.8…-5.4 vs. ~-3.2 for real text. (d) under the Marshall key gives "Theare is bsgngm of
  ilm sent to lie nere kgcikmd…" — noise.
- **(a) hill-climb** (`solve_a2.py`, Dutch and French quadgram LMs, bijective and homophonic modes, 8 restarts):
  best -4.71 per quad (random -6, genuine Dutch -3.0…-3.4); output fragments like "…ormellenhebelandender…"
  — suggestive of Dutch ("hebben", "-ende") but not a reading. 128 letters over 25 symbols with 8 unknown code
  groups breaking the text is below what the statistics can carry; a plain alphabetical assignment on 10-33 (any
  rotation/reversal) was also excluded (`stats_a.py`).
- **(c)** is a 10-digit cipher: "[12 symbols] is come with a great train to visit the [0 9 3 7]" (Brussels, Aug
  1656 — the arrival of Don Juan José de Austria as governor, or a visit to Charles II's court at Bruges, are the
  obvious contexts). Pattern of the name ABCDEDFDGEAB with the 4-letter word [H G B E] (shares 9,3,7). "the king"
  (k-i-n-g) would force the name to read ?n?dgdfdig?n — impossible, so the digits are not simple letters, or the
  word is not "king". Unresolvable at 16 symbols.
- **(d)**: the clear frame is rich — "There is [6] of [3] sent to lie near [7] and six [6] of [243 226] are [3] to
  strengthen [3], and [8] is so far out of favour now that [5] told me he had a greater mind to [3] him than [4]"
  — but 27 distinct letter-symbols in 50 groups with homophones cannot be pinned; cribs like "horse", "hang" fit
  many assignments equally well.

## Where the originals are
Bodleian **Rawlinson A** (Thurloe papers), volumes v (1653) and xxxviii/xli (1656) per Birch's marginal
references; not digitised. Birch's transcriptions are the only online witness.

## Verdict: STUCK
Too short for cryptanalysis, no key online. Sibling-letter route: (a) — any other 1653 Beverning/Nieupoort
despatch to Boreel with a decipherment in the Dutch Nationaal Archief (Staten-Generaal, liassen Engeland) —
not online in transcription. (b)-(d): the Bruges court's agents' ciphers of 1656 (Hyde/Nicholas with White,
Copinger, Waddall) would be in the Clarendon MSS — not online.

## Matched control (2026-09-22)

`control.py` → `control_out.txt` (40 trials per cell, 895 s). Synthetic ciphertexts copy (a)'s layout exactly:
three passages with the same sequence of letter runs and 3-digit code groups (66 + 47 + 15 = 128 letter tokens,
8 code groups replacing whole words, skipped by the solver). The climber is `solve_a2.py`'s code unchanged
(8 restarts, fixed 60,000 iterations each instead of a wall-clock slice). Plaintext is held-out text (last 20%
of the `lang/` corpus), the quadgram LM is built as `lm_build.py` does from the other 80%: Dutch `nl-gutenberg`,
French `fr-gutenberg`, English `en-1640s-history` (period English). Two designs: *bij* = one-to-one substitution
(~20-21 distinct symbols), mode bij; *homo* = homophonic with exactly 25 distinct symbols, as (a), mode homo
with LAM 0.5 / MAXH 2 (the settings of the `*_homo2` runs that gave the best −4.71; the defaults collapse onto
e/n). Recovered = ≥ 80% of the 128 letter tokens right.

| cell | recovered ≥ 80% | ≥ 50% | median accuracy | best score/quad, range |
|---|---|---|---|---|
| Dutch, bij | **39/40** | 40/40 | 0.98 | −4.60 … −3.84 |
| Dutch, homo (25 symbols) | **26/40** | 35/40 | 0.84 | −4.67 … −3.76 |
| French, bij | **40/40** | 40/40 | 0.98 | −4.50 … −3.90 |
| French, homo | **24/40** | 36/40 | 0.85 | −4.44 … −3.84 |
| English, bij | **36/40** | 37/40 | 0.98 | −5.30 … −3.91 |
| English, homo | **17/40** | 27/40 | 0.73 | −4.75 … −3.83 |

What it means: the control succeeds, so (a) is **not** too short for this method. 128 letters with 8 code gaps
are enough for the hill-climb to read a Dutch or French simple substitution almost always and a 25-symbol
homophonic one about 60% of the time. The negative on (a) is therefore meaningful, and the scores say how. The
fair comparison is the homo mode (a bij key cannot fit 25 symbols with ≤ 26 letters and ~21 in use): (a)'s best
is −4.71 in Dutch and −4.57 in French, below all 40 Dutch controls (worst −4.67) and all 40 French controls
(worst −4.44); only in English (−4.68) does it sit inside the control range (−4.75 … −3.83), at its bottom end.
(Caveat: the target runs used `lm_nl.json`/`lm_fr.json`/`beale/en_lm.json`, the controls LMs rebuilt the same way
from the `lang/` corpora, so the per-quad scores compare closely but not exactly.) A Dutch or French letter
cipher of this layout with up to two symbols per letter would have scored higher and would very likely have been
read. So one of the assumptions is wrong: the figures 6-33 are not a plain or lightly homophonic letter cipher of
Dutch/French text (syllables or word-signs among them, nulls, more homophones, or a different language), or
Birch's printed transcription is corrupt. Letters (b)-(d) were not
put through the control: (b) 22 and (c) 16 symbols are below any statistical attack, (d) has 50 groups with 29
distinct symbols (fewer than two occurrences per symbol).

## Remaining gaps

- (a) Beverning 1653, 136 groups - blocker: no-key-material; the matched control shows the text is long enough for
  the solver, and it still fails, so the system is not the one modelled; the key or a deciphered sibling despatch
  (Nationaal Archief, Staten-Generaal liassen Engeland) is needed. The 8 code groups need the new code Boreel sent.
- (b) du Gard 1656, 27 tokens - blocker: too-short; a cover address, no key online.
- (c) Brussels 1656, 16 digits - blocker: too-short; a name and a 4-letter word.
- (d) Waddall 1656, 50 groups / 29 distinct homophonic symbols - blocker: too-short; cribs fit many assignments; key in the Clarendon MSS, not online.

## Escalation

- [n/a] siblings: the sibling route (a deciphered Beverning/Nieupoort despatch to Boreel in the Nationaal Archief, Staten-Generaal liassen Engeland) is not online in transcription or images.
- [n/a] clear-pages: no images, only Birch's 1742 print; the originals (Bodleian Rawlinson A) are not digitised.
- [x] known-keys: every 1653-60 royalist/Commonwealth key on cryptiana applied to (a)-(d) (apply_keys.py).
- [x] print: Birch's TSP and cryptiana (Tomokiyo lists it as undeciphered) checked.
- [x] key-rebuild: hill-climb on (a) in Dutch/French/English, bijective and homophonic; alphabetical-key search; matched control run.
- [x] retry: nothing reads, so nothing to regrade; (c) and (d) cribs retried.
