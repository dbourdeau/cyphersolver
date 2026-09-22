# Giuliano Caprile (catalogue 157) and Alfonso Cistarelli (catalogue 158), Ferrarese agents in Hungary 1519–1521 — NOTES

Status: in progress (written up in docs/caprile1519.html; R1137 and R1128 still unread, known-keys and retry steps open)

**Verdict.** Catalogue 157 (Caprile, 7 records) and 158 (Cistarelli, R1137). Of Caprile's records, R1129–R1135 were
read at the time or in 1882 (clear copies filed as "b"/"c", or interlinear glosses), and R1138 was deciphered by W. Somogyi
(2025). **New here: R1139 (6 Apr 1521) and R1136 (8 Mar 1520) read in part**, with a homophonic key rebuilt from
Somogyi's two printed decipherments. R1128 (9 Mar 1519, a different "two-tier" cipher, about Caprile's own lawsuit)
is not read. Cistarelli's R1137 (numeric) is read only in fragments by ciphertext-only annealing.

ASMo, Ambasciatori, Ungheria b. 4 (Caprile 1519–20 file = "b. 4/23"; 1520–21 file = "b. 4/28"; Cistarelli = "b. 4/26").
DECODE R1128–R1139 (R1137 is Cistarelli). Images fetched with the shared cookie into `img/` (git-ignored). Vestigia
(public) search results in `vestigia/search_*.json`; record JSONs `vestigia/v*.json`; images `img/v/`.

## Record map

| DECODE | ASMo no. | Vestigia | date | DECODE status | clear copy / gloss | cipher system |
|---|---|---|---|---|---|---|
| R1128 | 1519–20 no. 1 | 1853 | 9 Mar 1519 | partial | none found; 7 cipher lines + clear postscript | 1519 two-tier |
| R1129 | no. 3a | 1855 | 20 Apr 1519 | decrypted | 3b, 3c (V1856–1857) | 1519 two-tier |
| R1130 | no. 4a | 1858 | 1 May 1519 | decrypted | 4b, 4c (V1859–1860) | 1519 two-tier |
| R1131 | no. 5a | 1861 | 12 May 1519 | partial | 5b, 5c (V1862–1863) | 1519 two-tier |
| R1132 | no. 6a | 1864 | May 1519 | decrypted | 6b, 6c (V1865–1866) | 1519 two-tier |
| R1133 | no. 7a | 1867 | May 1519 | decrypted | 7b, 7c (V1868–1869) | 1519 two-tier |
| R1134 | no. 8a | 1870 | 12/15 Jun 1519 | partial | 8b, 8c (V1871–1872), covering pp. 1–3 only; pp. 4–5 are a second letter (Buda 15 Jun) in clear with cipher insertions, no decipherment | 1519 two-tier |
| R1135 | no. 10a | 1874 | 1519 | partial | 10b (V1875, 19th-c. copy, gaps); interlinear gloss on the leaf | 1519 two-tier |
| R1136 | no. 11 | 1876 | 8 Mar 1520 | partial | none found | 1520–21 sign cipher |
| R1137 | Cistarelli no. 3 | 1904 | 25 Jul 1520 | partial | none found | two-digit numeric |
| R1138 | 1520–21 no. 10 | 1919 | 16 Feb 1521 (DECODE 6 Feb) | partial | none found; slip | 1520–21 sign cipher |
| R1139 | 1520–21 no. 13 | 1922 | 6 Apr 1521 | partial | none found; slip | 1520–21 sign cipher |

The same 1520–21 sign cipher also occurs, not on DECODE, in 1520–21 no. 11 (V1920 p. 3, a 9-line postscript) and
no. 12 (V1921, 25 Feb 1521, cipher phrases inside clear sentences).

## Systems

- **1519 two-tier cipher**: each cipher unit is a base glyph (7, m, n, L, t, 4, a …) with a small letter written
  above it. R1135's clear lines between the cipher lines are an interlinear gloss ("questa cavalcata respondere che in
  vero è cosa che mo[lto]" = the 10b copy's text). Not yet analysed.
- **1520–21 sign cipher**: continuous invented signs (φ, ψ, ÷, ss, ff, o, q, y, λ, T, ⊥, 8, *, …), no word
  division, no decipherment found anywhere in the file.
- **Cistarelli**: two-digit groups, mostly ending in 5 or 0 (25 95 70 15 80 55 …), with a few other signs (f, k, u),
  mixed with clear text. No gloss.

## Prior work

- ASMo inventory (`lit/asmo_ungheria.pdf`), Caprili 1519–20: "mancano quasi tutte le decifrature di dispacci, le qual
  sono state cavate solo nel 1882". The "b"/"c" items of nos. 3–8 and 10 are those 1882 decipherments (7b is a pencil
  copy beginning "Sire, quantunque io tenga per certo…"). No. 1 (R1128) has none.
- W. Somogyi Judit, "Estei Hippolit püspöki hagyatéka Giuliano Caprili magyarországi leveleinek tükrében",
  *Scriptorium* VI (2025) 247–264 (`lit/somogyi2025.pdf`), n. 50: prints decipherments of the 16 Feb 1521
  postscript in both versions: the slip of no. 10 (V1919 = **DECODE R1138**) and the postscript of no. 11 (V1920).
  She calls the system homophonic. Texts in `crib_somogyi.md`. So R1138 is already read (2025).

## 1520–21 key (R1136, R1138, R1139, V1920, V1921)

Built by monotone EM alignment (`em21.py`, `key21.py`) of the transcription (`caprile1521_transcription.txt`, labels in
`seg21/signs.md`, ligatures m+ → MT, n+ → NT in `c21_merged.txt`) against Somogyi's plaintexts of V1920 and the
capitals of V1919 (= R1138), seeded by a ciphertext-only anneal (`fastanneal.py`, `f21_o4.txt`). 714 letters
aligned, 89.6 % of alignments agree with the majority value of their sign. Counts per sign in `key21_counts.json`,
majority key in `key21.json`:

a = q, T, UT · c = PHI, TH · d = PSI, r · e = y, ss, 12?, 8? · g = w, U · i = B, RC, L · l = ff, n, A? · m = z, HH ·
n = DIV, p · o = CE, QB, o-SL-o · p = EL, AMP · r = AST, x · s = MT (m+), NT (n+) · t = h, f, K? · u = LAM, a.
The lone o is mostly a null (filler between letters); 8 appears as a null after "il" in R1139 L01.
Homophonic, as Somogyi says; no word division; no nomenclator codes seen.

## Readings (gist; raw decrypt in `decrypt21_raw.txt`)

Grades as in README: C = likely, M = possible. Transcription errors leave many letters wrong; only the phrases below
are claimed.

**R1139, slip of 6 Apr 1521 (1520–21 no. 13), 9 cipher lines, read in part.** "Post: il custode … io scrissi … è
tornato governator de[l] … ogni cosa … è tenuto Agria … in castello … la venuta … in Italia … li scritti … vedendo io …
deli danari del suo … come mi disse … lui m'ha resposto dice de voler andar in Italia quando al dare … Milan … parlaremo a
longo sopra ciò … per andar … el mi dirà …" (C for the quoted phrases). Subject: the castellan/custode of Eger, the
governor's return, money of the late bishop, and someone's wish to go to Italy — the Hippolito estate business of
Somogyi's article.

**R1136, 8 Mar 1520 (1519–20 no. 11), 12 cipher lines, read in part.** "e la susseguente matina … il custode … questo
episcopato … il custode … governator … Lactantio … tesoro … in gran … conclusi … congrega[tione] … ogni episcopa[to] …
in questo modo … poco spensi … Excellentia … al custode … de Ungaria sopra il suo … secondo … tornato … intendere …
[s]pensier suo … tal debito" (C/M). Subject: Eger see, its custode and governor, money and debts, the day after a
meeting ("la susseguente matina"), written as Ippolito was leaving Hungary (he crossed the border 7 Mar 1520).

**R1137 (Cistarelli, 25 Jul 1520), 584 numeric groups + 83 signs, fragments only.** Ciphertext-only anneal
(`fastanneal.py`, `refine37*.py`, outputs `f37_*.txt`, `r37*.txt`) gives a partly consistent key (e = 0, 25; a = 86,
80; o = 70, 10; i = 45; t = 95; r = 85, 84; s = 90, 15; n = 65, y; l = 55; p = 75; u = 96; m = 60; d = 20; c = 30) and
phrases such as "lettere per", "sempre", "presto", "saria meglio", "non se poteria", "dua milla", "questi altri",
"Antonio" (M). Not a reading; the transcription (`r1137_transcription.txt`, one reader) needs checking.

**R1128 (9 Mar 1519), attempted 21 Sept 2026, not read.** Two-tier sign cipher of 1519 (9 lines, 183 columns in
`t1519.txt`). Its clear part and no. 2 (V1854, "In un'altra mia ve mandai in zifra…") show the subject is Caprile's own
lawsuit at Rome ("le ragioni mie … l'adversario").

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

- 2026-09-21/22 (Fantini session, `pair5/`, `pair8/`, `pairX/`): R1131/5b alignment fails (water stain; no better than shuffled). R1134 pp. 4–5 carry no interlinear gloss (corrected in the table). **R1130 against 4c shows the 1519 cipher is syllabic**: upper sign ≈ consonant, base ≈ vowel (7 none, m e, n o), bracket-L = CV syllables ([y] te, [m] re, [&] to, [s] si, [L] ra); `intertenere` = y/7 9/7 [y] c/7 [y] z/m [m]; ~20 values, held-out 16/18 vs shuffled 8.1 (`pairX/t.txt`, `plain.txt`, `key.json`). The one-letter-per-column values in `fixed1519.json` conflict with it and should be rechecked. A control-validated syllabary annealer is in `jantini1517/syl_anneal.py`.

- 2026-09-21: DECODE R1126–R1140 metadata and images; Vestigia searches "Caprile" (52) and "Cistarelli" (20);
  contact sheets of every page. Transcriptions of R1137 and of the 1520–21 cipher by two agents. Literature: ASMo
  inventory (1882 decipherments), Somogyi 2025 (R1138 read). Key from Somogyi cribs by EM; R1139 and R1136 read in part;
  R1137 ciphertext-only anneal gives fragments.

## Remaining gaps

- R1139 and R1136 (1520-21 sign cipher), unread stretches - blocker: illegible; notes: transcription errors leave many letters wrong; single-reader transcription not re-checked
- R1137 Cistarelli, 584 numeric groups - blocker: not-attempted; only a ciphertext-only anneal on one unchecked transcription; no crib or clear copy searched beyond the Vestigia file
- R1128 (9 Mar 1519, two-tier cipher) - blocker: not-attempted; letter table and codebook incomplete; notes name the next step (careful transcription of R1133/R1131/R1132 against the 1882 decipherments) as not done

## Escalation

- [x] siblings: R1126-R1140 and Vestigia files opened; 1882 b/c decipherments found for R1129-R1135
- [x] clear-pages: b/c items identified as 1882 decipherments; R1135 interlinear gloss
- [ ] known-keys: not done - 1520-21 key not tried on R1137; other Ferrarese Hungary keys (Buda 1489, Sadoleto) not tried on R1137
- [x] print: ASMo inventory and Somogyi 2025 found; R1138 already read
- [x] key-rebuild: EM key from Somogyi cribs (89.6%); seeded EM on R1133/7c for 1519 system
- [ ] retry: not done - second transcription of R1136/R1139 and rerun; transcribe R1131/R1132 against 5b/6b to fill the 1519 table, then R1128
