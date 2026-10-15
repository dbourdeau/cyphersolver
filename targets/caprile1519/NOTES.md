# Giuliano Caprile (Eger) to Bonaventura Pistofilo, 9 March 1519: the 1519 two-tier cipher (catalogue 157, R1128) — NOTES

Status: in progress (written up in docs/caprile1519.html as attempted, not solved; R1128 not read; the key is still rebuildable from the 1882 sibling decipherments)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. This folder held the whole
Caprile/Cistarelli file (ASMo Ungheria b. 4, DECODE R1128–R1139) with three ciphers. It now keeps the **1519 two-tier
cipher**: R1128, the only 1519 letter with no decipherment, and its siblings R1129–R1135 (same cipher, deciphered in
1882 or interlined) as key material. The 1520–21 homophonic sign cipher (R1136, R1138, R1139, Vestigia 1920, 1921) is a
different cipher, with its own page ([`targets/caprile1520/`](../caprile1520/), docs/caprile1520.html), and so is
Alfonso Cistarelli's figure cipher (R1137, [`targets/cistarelli1520/`](../cistarelli1520/), docs/cistarelli1520.html).
Shared material stays here: `decode/` (DECODE record pages R1126–R1140), `vestigia/` (search results and record JSONs),
the generic annealers `anneal.py` and `fastanneal.py` (also imported by the other two folders), `knownkeys.py` (known-keys
test for R1128 and R1137), and the images (`img/`, git-ignored; main checkout `targets/caprile1519/img/`).

Left to do: transcribe R1132 (8 pp.) against 6b and R1131 against 5b, refit the 1519 table (the factorised rebuild from
R1130/R1133 failed, `syl_fact.py`), then R1128.

**Verdict.** R1128 (9 Mar 1519, seven lines of cipher and a clear postscript, about Caprile's own lawsuit) is **not
read**. Of the other 1519 letters in the same cipher, R1129–R1135 were read at the time or in 1882 (clear copies filed as
"b"/"c", or interlinear glosses). Attempted, open; the key material exists, so this is work left, not an outside block.

ASMo, Ambasciatori, Ungheria b. 4 (Caprile 1519–20 file = "b. 4/23"; 1520–21 file = "b. 4/28"; Cistarelli = "b. 4/26").
DECODE R1128–R1139 (R1137 is Cistarelli). Images fetched with the shared cookie into `img/` (git-ignored). Vestigia
(public) search results in `vestigia/search_*.json`; record JSONs `vestigia/v*.json`; images `img/v/`.

## Record map of the whole file

| DECODE | ASMo no. | Vestigia | date | DECODE status | clear copy / gloss | cipher system (entry) |
|---|---|---|---|---|---|---|
| R1128 | 1519–20 no. 1 | 1853 | 9 Mar 1519 | partial | none found; 7 cipher lines + clear postscript | 1519 two-tier (this entry) |
| R1129 | no. 3a | 1855 | 20 Apr 1519 | decrypted | 3b, 3c (V1856–1857) | 1519 two-tier (this entry, key material) |
| R1130 | no. 4a | 1858 | 1 May 1519 | decrypted | 4b, 4c (V1859–1860) | 1519 two-tier (key material) |
| R1131 | no. 5a | 1861 | 12 May 1519 | partial | 5b, 5c (V1862–1863) | 1519 two-tier (key material) |
| R1132 | no. 6a | 1864 | May 1519 | decrypted | 6b, 6c (V1865–1866) | 1519 two-tier (key material) |
| R1133 | no. 7a | 1867 | May 1519 | decrypted | 7b, 7c (V1868–1869) | 1519 two-tier (key material) |
| R1134 | no. 8a | 1870 | 12/15 Jun 1519 | partial | 8b, 8c (V1871–1872), covering pp. 1–3 only; pp. 4–5 are a second letter (Buda 15 Jun) in clear with cipher insertions, no decipherment | 1519 two-tier (key material) |
| R1135 | no. 10a | 1874 | 1519 | partial | 10b (V1875, 19th-c. copy, gaps); interlinear gloss on the leaf | 1519 two-tier (key material) |
| R1136 | no. 11 | 1876 | 8 Mar 1520 | partial | none found | 1520–21 sign cipher (caprile1520) |
| R1137 | Cistarelli no. 3 | 1904 | 25 Jul 1520 | partial | none found | two-digit numeric (cistarelli1520) |
| R1138 | 1520–21 no. 10 | 1919 | 16 Feb 1521 (DECODE 6 Feb) | partial | none found; slip | 1520–21 sign cipher (caprile1520) |
| R1139 | 1520–21 no. 13 | 1922 | 6 Apr 1521 | partial | none found; slip | 1520–21 sign cipher (caprile1520) |

## The 1519 cipher

Each cipher unit is a base glyph (7, m, n, L, t, 4, a …) with a small letter written above it. R1135's clear lines
between the cipher lines are an interlinear gloss ("questa cavalcata respondere che in vero è cosa che mo[lto]" = the
10b copy's text).

## Prior work

- ASMo inventory (`lit/asmo_ungheria.pdf`), Caprili 1519–20: "mancano quasi tutte le decifrature di dispacci, le qual
  sono state cavate solo nel 1882". The "b"/"c" items of nos. 3–8 and 10 are those 1882 decipherments (7b is a pencil
  copy beginning "Sire, quantunque io tenga per certo…"). No. 1 (R1128) has none.

## R1128 (9 Mar 1519), attempted 21 Sept and 2 Oct 2026, not read

Two-tier sign cipher of 1519 (9 lines, 183 columns in `t1519.txt`). Its clear part and no. 2 (V1854, "In un'altra mia ve
mandai in zifra…") show the subject is Caprile's own lawsuit at Rome ("le ragioni mie … l'adversario").

What the attempt established about the 1519 system (from R1133 = no. 7a against its 1882 decipherment 7c, `crib1519.md`;
full column transcription `t1133_full.txt`, 27 lines, 1327 columns, 16 % illegible in a faded band):
- The 1519 letters are copies of reports to the King of France ("Sire", "vostra maestà christianissima": the 1519
  imperial election, Joachim [Moltzan?] at the Polish court, Poncet, the Polish and Hungarian votes).
- A column (small sign above a base sign 7, m, n, a, t, 4) is **one plaintext letter, homophonic**: "oratore" =
  L/7 -/n u/7 x/7 c/7 m/n -/a. Seeded EM (`syl_em2.py`) holds c/7 = o (33×), L/7 = o (24), m/n = r (22), x/7 = t (19),
  -/n = r (13), u/7 = a (12), -/a = e (8), d/m = i (`fixed1519.json`).
- A **bracket-L sign with an inner sign is a nomenclator word**: the run [d][s][&] recurs exactly where 7c has "de
  vostra maesta" (lines 3 and 4). [d] = de, [s] = vostra, [&] = maesta. 245 of 1327 columns in R1133 are such codes.
- 1882 decipherment: 2,177 letters for R1133.

Why R1128 stays unread: 39 of its 183 columns are code words (the codebook is known for three), and only 9 of some 40
letter-column types have reliable values; a language-model anneal over R1133+R1134+R1128 with those fixed
(`ann1519.py`, `key1519_ann.json`) gives only scattered words. Next step: a second, careful transcription of R1133 and of
another 1882-paired letter (R1131/5b, R1132/6b) line by line against the decipherment, to fill the letter table and the
codebook, then R1128.

## Log

- 2026-09-21: DECODE R1126–R1140 metadata and images; Vestigia searches "Caprile" (52) and "Cistarelli" (20);
  contact sheets of every page. Literature: ASMo inventory (1882 decipherments). R1133 against 7c (`crib1519.md`,
  `t1133_full.txt`, `syl_em2.py`); R1128 anneal (`ann1519.py`) gives scattered words only.

- 2026-09-21/22 (Fantini session, `pair5/`, `pair8/`, `pairX/`): R1131/5b alignment fails (water stain; no better than shuffled). R1134 pp. 4–5 carry no interlinear gloss (corrected in the table). **R1130 against 4c shows the 1519 cipher is syllabic**: upper sign ≈ consonant, base ≈ vowel (7 none, m e, n o), bracket-L = CV syllables ([y] te, [m] re, [&] to, [s] si, [L] ra); `intertenere` = y/7 9/7 [y] c/7 [y] z/m [m]; ~20 values, held-out 16/18 vs shuffled 8.1 (`pairX/t.txt`, `plain.txt`, `key.json`). The one-letter-per-column values in `fixed1519.json` conflict with it and should be rechecked. A control-validated syllabary annealer is in `targets/jantini1517/syl_anneal.py`.

- 2026-10-02: known keys on R1128 (`knownkeys.py r1128`): the R1130/4c syllabary covers 32 % of columns and scores like a random key (LM -3.22 vs -3.24), fixed1519 covers 13 %, key1519_ann is fitted on R1128 itself (no evidence). Factorised syllabary (upper = consonant, base = vowel) trained on R1130/4c + R1133/7c (`syl_fact.py`): the base tier fits (7 none, m e, n o) but the upper tier does not, and the R1128 decode scores LM -2.92 against -2.41 for permuted tables (worse than control).

- 2026-10-14: split (one key per entry). The 1520–21 files moved to `../caprile1520/`, the R1137 files to
  `../cistarelli1520/`; `knownkeys.py` now reads `../cistarelli1520/r1137_transcription.txt`.

## Remaining gaps

- R1128 (9 Mar 1519, two-tier cipher, 183 columns, 78 column types, 39 code words) - blocker: left-open; known keys (`knownkeys.py r1128`): the R1130/4c syllabary covers 32 % of columns and scores like a random key (LM -3.22 vs -3.24), fixed1519 covers 13 %, key1519_ann is fitted on R1128 itself (no evidence); the 1882 sibling decipherments (R1129-R1135) still allow a key rebuild (R1131/R1132 against 5b/6b), so the key material exists and the gap is work, not an outside blocker; next: transcribe R1132 against 6b

## Escalation

- [x] siblings: R1126-R1140 and Vestigia files opened; 1882 b/c decipherments found for R1129-R1135 (2 Oct 2026)
- [x] clear-pages: b/c items identified as 1882 decipherments; R1135 interlinear gloss; R1128 has none
- [x] known-keys: done 2 Oct 2026 (`knownkeys.py`): the 1519 tables (pairX syllabary, fixed1519, key1519_ann) on R1128 give no signal against a random-key control; the 1520-21 key (`../caprile1520/key21.json`) is another system; Fantini's 1517-18 letters (jantini1517) are the same family but not this key
- [x] print: ASMo inventory; nothing printed for R1128
- [x] key-rebuild: seeded EM on R1133/7c (one letter per column) and R1130/4c (syllabary); factorised syllabary rebuild (failed)
- [x] retry: R1128 decoded with every 1519 table (2 Oct 2026); nothing reads. Still open as work: the key from R1131/R1132 against 5b/6b
