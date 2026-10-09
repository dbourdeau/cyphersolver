# Giuliano Caprile (catalogue 157) and Alfonso Cistarelli (catalogue 158), Ferrarese agents in Hungary 1519–1521 — NOTES

Status: in progress (written up in docs/caprile1519.html; V1921 read 97.0 %; R1139 89.7 %, R1136 66.9 % after pass 5, 3 Oct 2026)
Left to do: (1) R1139: "4 8 1 7" (L01) and "1 7" (L02) are code-like (no letter or numeral fits, pass 5) and short stretches of L02, L04-L05, L08 remain;
(2) R1136: L01 end, L02 start, L06, L10-L11 starts, limited by the doubtful sign separations (c/CE/e, QB/8, AMP/EL,
x/xp); the pass-5 table over all five letters (`lookalike21.py`) settles only CE = o and xp = q, and the pen-shape study (pass 6, `shapes21.py`) found no shape class with a
consistent value, so these stretches need either hand-placed crops of every occurrence or more text in the same key; (3) R1128: transcribe R1132
(8 pp.) against 6b and refit the 1519 table (the factorised rebuild from R1130/R1133 failed, `syl_fact.py`); (4) R1137:
see its gap line.

**Verdict.** Catalogue 157 (Caprile, 7 records) and 158 (Cistarelli, R1137). Of Caprile's records, R1129–R1135 were
read at the time or in 1882 (clear copies filed as "b"/"c", or interlinear glosses), and R1138 was deciphered by W. Somogyi
(2025). **New here: R1139 (6 Apr 1521) and R1136 (8 Mar 1520) read in part**, with a homophonic key rebuilt from
Somogyi's two printed decipherments. R1128 (9 Mar 1519, a different "two-tier" cipher, about Caprile's own lawsuit)
is not read. **V1921 (25 Feb 1521, no. 12, not on DECODE) read 97.0 %** (2 Oct 2026, `read_v1921.md`). Cistarelli's R1137 (numeric) is read only in fragments by ciphertext-only annealing.

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
no. 12 (V1921, 25 Feb 1521, cipher phrases inside clear sentences; read 2 Oct 2026, `read_v1921.md`). The Vestigia
records flagged "titkosírás" (cipher) in the 1519-21 files are exactly V1853, V1874, V1876, V1919-V1922; no other
letter uses the 1520-21 key.

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
**Corrected 2 Oct 2026 (V1921):** the lone o is a homophone for h and u ("ha", "ch'à", "che"; "qui", "suo",
"quantunque"), as the EM counts already showed (o 28, h 13, u 10); oo = b ("beni"; R1139 "de[b]ito"); z+ = q and
x+ = q (crossed ligatures like m+, n+; "qui", "quantunque", "quel"); EL = f in "oficio" (as AMP = f in "Alfonso");
K = et (M); Z = x. R1136 has 8 oo and 3 "z t", V1920 4 and 2: not yet re-read with these values.
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

**V1921, 25 Feb 1521 (1520-21 no. 12), six cipher runs in clear sentences, read 97.0 % (161/166 signs; 88.6 % at
grade C).** "E me dicixe ha un omo qui [clear: qual oltra che fa mille pacie & da poca riputation ale cose del
patron] dice ogni cosa e revelta [clear: e ha ditto haver scritto al suo mazo che] il custode è stato quel ch'à
persuaso [..] [clear: a dire che] Agria era data d'anti il suo advento, e[t] che lo toglia in oficio [clear: … in gran
disgratia di] suo signore [clear: … a repeter il suo] sopra soi beni, quantunque siano in reg[..]". Someone at
Esztergom blames the custode of Eger for the claim that the see had been given away before Ippolito's successor
arrived; Caprile advises the Duke to reclaim Ippolito's due from the man's goods. Transcription corrected on the
image (`v1921_signs.txt`); it-cinquecento −1.79/char vs −4.12 shuffled. Details `read_v1921.md`.

**R1139 and R1136, pass 3 (2 Oct 2026, `pass3_r1136_r1139.md`).** Re-decoded with the V1921 values: R1139 83.8 % of
decoded letters inside claimed phrases (L05-L08 continuous, "debito" now at key values), R1136 59.4 % ("transferse a
Buda il custode", "in oficio questo episcopato, et a epso custode", "dicono esser conclusi", "potrà far al custo[d]e
per questa via de Ungaria sopra il suo", "in questo loco niente", "tal debito"). Mostly grade M.

**R1139 and R1136, pass 4 (2 Oct 2026, later).** Second transcriptions at native resolution (`r1139_pass4.txt`,
`r1136_pass4.txt`); new values o+ = s, Z+/Zp = q, D = b/x, plain c = o, σ = h. R1139 88.7 % (L01 "il custode, quando a
Buda, come i' scrisi, è tornato gubernator de …"; L03 "credo dia ogni ato e qualche cosa a le ma[n] di [l]o custode;
per anchora si n'è in-|trato"); R1136 66.9 % ("Lactantio, ho inteso, qual …", "congregati … Bachiensis, che ogni
episcopa[to]", "l'altro in titolo, et a questo modo excluderà …"). Details in `pass3_r1136_r1139.md`.

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

- 2026-09-21/22 (Fantini session, `pair5/`, `pair8/`, `pairX/`): R1131/5b alignment fails (water stain; no better than shuffled). R1134 pp. 4–5 carry no interlinear gloss (corrected in the table). **R1130 against 4c shows the 1519 cipher is syllabic**: upper sign ≈ consonant, base ≈ vowel (7 none, m e, n o), bracket-L = CV syllables ([y] te, [m] re, [&] to, [s] si, [L] ra); `intertenere` = y/7 9/7 [y] c/7 [y] z/m [m]; ~20 values, held-out 16/18 vs shuffled 8.1 (`pairX/t.txt`, `plain.txt`, `key.json`). The one-letter-per-column values in `fixed1519.json` conflict with it and should be rechecked. A control-validated syllabary annealer is in `targets/jantini1517/syl_anneal.py`.

- 2026-09-21: DECODE R1126–R1140 metadata and images; Vestigia searches "Caprile" (52) and "Cistarelli" (20);
  contact sheets of every page. Transcriptions of R1137 and of the 1520–21 cipher by two agents. Literature: ASMo
  inventory (1882 decipherments), Somogyi 2025 (R1138 read). Key from Somogyi cribs by EM; R1139 and R1136 read in part;
  R1137 ciphertext-only anneal gives fragments.

- 2026-09-30 (quotation list for George Lasry): R1139 second reading pass, `r1139_pass2.txt`. Signs re-checked on
  the image where the decrypt did not read; letters proposed by a beam search over `key21_counts.json` with the
  `it-cinquecento` model and checked sign by sign. Transcription corrections: L03 "custo p ss" is "custo r ss"
  (custode); L05 "q CE" in "teneva | per" is EL (p); L05 "UT PHI" in "andata" is the crossed p (n). Now continuous
  from L05 to L07: "li go fato moto deli danari del suo de[b]ito, come mi dise messere [Alfonso]. Lui m'ha
  resposto, dice [de] voler andar in Italia quando al dare …" (C/M; "Alfonso" is enciphered a-l-p-o-n-s-o, M), and
  L08-L09 "parlaremo a longo sopra ciò … vedrò quel mi dirà, e il tuto reportarò a V. Ex." (M/I). L01-L03 still
  read only in phrases. Page §03 updated.

- 2026-10-03 (pass 6): pen-shape step for QB/8, c/e/CE, AMP/EL (`shapes21.py`, sheets in `shapes21/`): automatic crops reliable for about half of QB only; QB's two forms do not follow the LM values; c is a distinct form without a consistent value; failed, stopped, percentages unchanged.

- 2026-10-03 (pass 5): look-alike tabulation (`lookalike21.py`: CE = o, xp = q accepted; QB/8, c/e, AMP/EL not separable), numeral test of R1139's "4 8 1 7"/"1 7" (no fit), name and Somogyi-phrase cribs (`namecrib21.py`, nothing new); R1139 89.7 %, R1136 66.9 %. Vestigia records have no summaries.

- 2026-10-02 (pass 4): R1136 second transcription (`r1136_pass4.txt`) 66.9 %; R1139 second pass (`r1139_pass4.txt`) 88.7 %; R1128 factorised syllabary from R1130/R1133 (`syl_fact.py`) fails against a permuted control; R1137 spot-check of L04-L07 (13/92 groups disagree) and crib test (`r1137_crib.py`: cribs no better than controls).

- 2026-10-02 (later): retry and known-keys steps (see Escalation); `beam21.py`, `regrade21.py`, `knownkeys.py`, `pass3_r1136_r1139.md`. The xp ligature (= q) found in R1136 L10 also reads V1921's "quantunque" (161/166).

- 2026-10-02: V1921 (no. 12) read. Six cipher runs re-checked sign by sign on `img/v/v1921_2.jpg` (4 corrections:
  z+, x+, m+ written as "m p", ff not HH); key21 values plus five new ones forced by context (lone o = h/u, oo = b,
  z+/x+/xp = q, EL = f, K = et); 161/166 signs read, 97.0 % (`read_v1921.py`). Vestigia records checked for other
  1520-21 cipher letters: none beyond R1136, R1138, R1139, V1920, V1921.

## Remaining gaps

Blocker "left-open" is not one of the checker's outside blockers on purpose: these pieces are still workable here, and
no outside blocker (no key material, too short, illegible, physical access) honestly applies to them.

- R1136 L01-L02 stain and blot (about 6 signs, "# #" in the transcription) and R1139 L10 end - blocker: illegible; the stain covers the signs on the only image
- R1139 (6 Apr 1521), "4 8 1 7" (L01) and "1 7" (L02) - blocker: open-codes; tested as letters and as numerals (3 Oct 2026), nothing fits; likely nomenclator codes with no list
- R1139 (6 Apr 1521), other unread stretches (10 % of decoded letters) - blocker: left-open; pass 5 89.7 % (L08 "mi per Milan" added); pass 4 (`r1139_pass4.txt`, `pass3_r1136_r1139.md`): 88.7 % inside claimed phrases; L01 and L03 now read; open: numeral-like "4 8 1 7" and "1 7" (no key value) and short stretches of L02, L04-L05, L08
- R1136 (8 Mar 1520), unread stretches (33 % of decoded letters) - blocker: left-open; pass 4: second transcription at native resolution (`r1136_pass4.txt`, 11 of 12 lines changed), 66.9 % inside claimed phrases (was 59.4 %); what still stops L06, L10-L11 and the line starts is the doubtful sign separations (c/CE/e, QB/8, AMP/EL, x/xp), which a sign table over all five letters could settle; not an outside blocker
- V1921 (25 Feb 1521), 5 of 166 signs - blocker: illegible; notes: "K PHI" at the torn page edge after "in reg" (illegible); two minims "1 1" after "persuaso" have no key value (no-key-material); one QB before "Agria" probably a slip; "dicixe" and "revelta" grade M
- R1137 Cistarelli, 584 two-digit groups - blocker: needs-physical-access; the only image (DECODE, whole spread at 3240 px, digits about 25 px, faded) does not settle the digit readings: a second reading of P2 L04-L07 against the image disagrees with `r1137_transcription.txt` on 13 of 92 groups (14 %: 8/9 as in 85/95, 4/9, 0/5/6, 80/86, and where a group starts), and the single "0"/"5" groups may be halves of groups; no key exists anywhere (series, archive, correspondent, decade; DECODE has no Este/ASMo key 1490-1550); ciphertext-only anneal (order 5, 20 restarts) and crib placement (`r1137_crib.py`, `r1137_crib_out.txt`: custode, Agria, Alfonso, debito, Buda, episcopato against six control words, with a word-level rerank) do not separate cribs from controls (mean gain -169 vs -172, word scores -3.00 to -3.25 for both); my judgement, not proven, is that transcription noise is what stops the solve, so a better photograph from ASMo (b. 4/26 no. 3) is the next step
- R1128 (9 Mar 1519, two-tier cipher, 183 columns, 78 column types, 39 code words) - blocker: left-open; known keys (`knownkeys.py r1128`): the R1130/4c syllabary covers 32 % of columns and scores like a random key (LM -3.22 vs -3.24), fixed1519 covers 13 %, key1519_ann is fitted on R1128 itself (no evidence); the 1882 sibling decipherments (R1129-R1135) still allow a key rebuild (R1131/R1132 against 5b/6b), so the key material exists and the gap is work, not an outside blocker. 2 Oct (later): factorised syllabary (upper = consonant, base = vowel) trained on R1130/4c + R1133/7c (`syl_fact.py`): the base tier fits (7 none, m e, n o) but the upper tier does not, and the R1128 decode scores LM -2.92 against -2.41 for permuted tables (worse than control); next: transcribe R1132 against 6b

## Escalation

- [x] siblings: R1126-R1140 and Vestigia files opened; 1882 b/c decipherments found for R1129-R1135; Vestigia cipher-flagged records of the 1519-21 files are exactly V1853, V1874, V1876, V1919-V1922 (2 Oct 2026)
- [x] clear-pages: b/c items identified as 1882 decipherments; R1135 interlinear gloss; R1137 P1/P3 clear text, P4 address (2 Oct 2026)
- [x] known-keys: done 2 Oct 2026 (`knownkeys.py`): key21 + V1921 values on R1139/R1136/V1921 (reads); the 1519 tables (pairX syllabary, fixed1519, key1519_ann) on R1128 (no signal against a random-key control); R1137 is numeric and no numeric key of the series, archive (DECODE ASMo/Este 1490-1550: none), correspondent (Bonzagni 1512-14, Ippolito's Eger household) or decade (Sadoleto 1482, Maffeo 1489) exists, so none could be applied
- [x] print: ASMo inventory and Somogyi 2025 found; R1138 already read
- [x] key-rebuild: EM key from Somogyi cribs (89.6%); seeded EM on R1133/7c for 1519 system; V1921 values (lone o = h/u, oo = b, z+/x+/xp = q, EL = f, K = et)
- [x] retry: done 2 Oct 2026 - V1921 re-transcribed and read 97.0 %; R1139 and R1136 re-decoded with the new values (`beam21.py`), phrases checked on the crops and regraded (`pass3_r1136_r1139.md`, `regrade21.py`: R1139 83.8 %, R1136 59.4 %); R1137 anneal rerun with a shuffled control; pass 4 (2 Oct, later): R1136 re-transcribed and regraded 66.9 %, R1139 second pass 88.7 %, R1128 factorised rebuild (failed), R1137 transcription spot-check (14 % disagreement) and crib test (cribs = controls). Still open as work, not as escalation: a full second transcription of R1136 and R1137, and the R1128 key from the 1882 siblings
