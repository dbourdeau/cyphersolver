# Sforza chancery letters in cipher, ASMi cart. 1598 and 1591 (catalogue 1311; DECODE R5297-R5298, R5476-R5587)

Status: in progress. Triage done and catalogue 1311 split into sign families, ids 2628-2645 (14 Nov 2026); nothing read yet. Sibling of catalogue 1310 (`targets/sforza1597`).

## Fetched (14 Nov 2026, DECODE cookie, `fetch_all.py`)
203 records in `list1598.json`: 110 letters (record_type 1) and 93 key sheets (record_type 2). PDFs in `pdf/`, renders in
`png/`, contact sheets in `sheets/` (`sheets.py`); all git-ignored.

## What the letters are
Not one cipher. The 133 letter pages show many hands and sign families, as in cart. 1597:
- Geometric/cursive sign alphabets without word division (R5488, R5509, R5519, R5524, R5529 ...), the R5464-type homophonic letters.
- Clear letters with cipher passages (R5485 "Capo de Cremona", R5492, R5510, R5522, R5534 ...): these clear contexts are cribs.
- R5482: a code. Capital letter + superscript number (L^2, H^30, A^13, M^2, e^39, Z^19, N^17 ...) mixed with single signs and
  ligatures; signed "Idem". Needs a codebook; repetitions (H^26, A^11, A^13, M^2, L^3) are frequent.
- Several leaves are nearly all clear (R5481, R5489, R5494, R5530) or wrappers (R5490 p.2, R5512 p.2).

## 14 Nov 2026: split into sign families (`split1311.py`)
Top 3-4 lines of every letter rendered at 110 dpi (`strips.py`, sheets `strips/f00-f10.jpg`, git-ignored) and grouped by sign shapes by eye. Catalogue 1311 retired; 18 entries promoted:

| id | fam | DECODE records | hand |
|---|---|---|---|
| 2628 | A | 5488, 5528, 5579, 5581 | geometric T, III, infinity, U |
| 2629 | B | 5562, 5572, 5573, 5575-5577, 5586 | x, double-cross, 3, barred m, pp, k |
| 2630 | C | 5502-5506, 5514, 5515, 5517, 5518 | numerals 4/6/8 + crosses; clear phrases between runs |
| 2631 | D | 5495-5499, 5507 | lambda, 3, bz, L-dot, ooo |
| 2632 | E | 5520, 5523, 5535, 5537, 5541 | m-divide, infinity, pi, barred P |
| 2633 | F | 5555, 5556, 5559, 5563 | v, divide, infinity, plus |
| 2634 | G | 5516, 5519, 5522 | x, 4, 3, theta, lambda; clear passages |
| 2635 | H | 5551, 5561 | cursive ml, z3o, // |
| 2636 | I | 5500, 5553 | pseudo-Latin a b f |
| 2637 | J | 5490, 5493 | pseudo-Latin bz, rb, Z |
| 2638 | K | 5511-5513 | numeral-like 7, 5, 3, 9 |
| 2639 | L | 5564, 5565, 5582-5584 | ta, delta, square, Afk |
| 2640 | M | 5486, 5487, 5530 | bz, inverted T, infinity, lambda |
| 2641 | N | 5568, 5574 | hash, 8, inverted T |
| 2642 | O | 5524, 5529 | V, hash, 8, barred p |
| 2643 | P | 5521, 5542 | to, delta, 3n, qo |
| 2644 | Q | 5482, 5485 | code: capital + superscript number |
| 2645 | Z | 38 singletons | unmatched hands, many with clear context |

Clear or nearly clear leaves, left out: R5481, R5483, R5494, R5525, R5552, R5557, R5566, R5569, R5578. Families are by eye on strips, a proxy for keys; they may merge or split once key sheets are compared. The first split attempt was written into the stale shared checkout (ids 2464-2481) and reverted before commit; the committed ids come from origin/main (a second clash on push moved them from 2575-2592 to 2628-2645).

## Next steps
1. Largest family first: C (9 letters, clear phrases as cribs), then B and A.
2. Match families against the 93 key sheets of this box and the 115 of cart. 1597 (`keycols.py` in sforza1597).
3. Run the sforza1597 chain (signreader + CTTS + keyrefine) on the largest clean family.

## Remaining gaps
All letters unread; no key matched yet. Blocker: none external; work not yet done.

## Escalation
Not started beyond triage (siblings: cart. 1597 keys; clear passages as cribs).
