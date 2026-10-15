# Giuliano Caprile to Ferrara, 1520–1521: the 1520–21 sign cipher (catalogue 157) — NOTES

Status: in progress (written up in docs/caprile1520.html; V1921 read 97.0 %; R1139 89.7 %, R1136 66.9 % after pass 5, 3 Oct 2026; the R1136/R1139 stretches are still workable)

Split on 14 Oct 2026 from `caprile1519` under the one-key rule (George Lasry, 14 Oct 2026): one
entry per key. The old entry joined three ciphers of the same ASMo file. This folder keeps the **1520–21 homophonic sign
cipher** (R1136, R1138, R1139, Vestigia 1920, 1921). The 1519 two-tier cipher of R1128 is a different cipher, with its
own page ([`targets/caprile1519/`](../caprile1519/), docs/caprile1519.html), and so is Alfonso Cistarelli's figure cipher
of R1137 ([`targets/cistarelli1520/`](../cistarelli1520/), docs/cistarelli1520.html). Shared material stays in
`targets/caprile1519/`: the DECODE record pages (`decode/`), the Vestigia search results and record JSONs (`vestigia/`),
the generic annealers `anneal.py` and `fastanneal.py` (imported from there by `polish21.py`), and the images
(`img/`, git-ignored, in the main checkout under `targets/caprile1519/img/`).

Left to do: (1) R1139: "4 8 1 7" (L01) and "1 7" (L02) are code-like (no letter or numeral fits, pass 5) and short
stretches of L02, L04-L05, L08 remain; (2) R1136: L01 end, L02 start, L06, L10-L11 starts, limited by the doubtful sign
separations (c/CE/e, QB/8, AMP/EL, x/xp); the pass-5 table over all five letters (`lookalike21.py`) settles only CE = o
and xp = q, and the pen-shape study (pass 6, `shapes21.py`) found no shape class with a consistent value, so these
stretches need either hand-placed crops of every occurrence or more text in the same key.

**Verdict.** R1138 was deciphered by W. Somogyi (2025), with the second version of the same postscript (Vestigia 1920).
**New here: R1139 (6 Apr 1521) and R1136 (8 Mar 1520) read in part**, with a homophonic key rebuilt from Somogyi's two
printed decipherments. **V1921 (25 Feb 1521, no. 12, not on DECODE) read 97.0 %** (2 Oct 2026, `read_v1921.md`).

ASMo, Ambasciatori, Ungheria b. 4 (Caprile 1519–20 file = "b. 4/23"; 1520–21 file = "b. 4/28").

## Records in this cipher

| DECODE | ASMo no. | Vestigia | date | DECODE status | clear copy / gloss |
|---|---|---|---|---|---|
| R1136 | 1519–20 no. 11 | 1876 | 8 Mar 1520 | partial | none found |
| R1138 | 1520–21 no. 10 | 1919 | 16 Feb 1521 (DECODE 6 Feb) | partial | none on the leaf; Somogyi 2025 prints it |
| — | 1520–21 no. 11 p. 3 | 1920 | 16 Feb 1521 | not on DECODE | Somogyi 2025 prints it (second version of the R1138 postscript) |
| — | 1520–21 no. 12 | 1921 | 25 Feb 1521 | not on DECODE | none found |
| R1139 | 1520–21 no. 13 | 1922 | 6 Apr 1521 | partial | none found; slip |

The Vestigia records flagged "titkosírás" (cipher) in the 1519-21 files are exactly V1853, V1874, V1876, V1919-V1922; no
other letter uses the 1520-21 key. The full record map of the file (with the 1519 letters and Cistarelli) is in
`targets/caprile1519/NOTES.md`.

## The cipher

Continuous invented signs (φ, ψ, ÷, ss, ff, o, q, y, λ, T, ⊥, 8, *, …), no word division, no decipherment found anywhere
in the file except Somogyi's for the 16 Feb 1521 postscript. Somogyi calls it homophonic.

## Prior work

- W. Somogyi Judit, "Estei Hippolit püspöki hagyatéka Giuliano Caprili magyarországi leveleinek tükrében",
  *Scriptorium* VI (2025) 247–264 (`../caprile1519/lit/somogyi2025.pdf`, git-ignored), n. 50: prints decipherments of the 16 Feb 1521
  postscript in both versions: the slip of no. 10 (V1919 = **DECODE R1138**) and the postscript of no. 11 (V1920).
  Texts in `crib_somogyi.md`. So R1138 is already read (2025).

## 1520–21 key (R1136, R1138, R1139, V1920, V1921)

Built by monotone EM alignment (`em21.py`, `key21.py`) of the transcription (`caprile1521_transcription.txt`, labels in
`seg21/signs.md`, ligatures m+ → MT, n+ → NT in `c21_merged.txt`) against Somogyi's plaintexts of V1920 and the
capitals of V1919 (= R1138), seeded by a ciphertext-only anneal (`../caprile1519/fastanneal.py`, `f21_o4.txt`). 714 letters
aligned, 89.6 % of alignments agree with the majority value of their sign. Counts per sign in `key21_counts.json`,
majority key in `key21.json`:

a = q, T, UT · c = PHI, TH · d = PSI, r · e = y, ss, 12?, 8? · g = w, U · i = B, RC, L · l = ff, n, A? · m = z, HH ·
n = DIV, p · o = CE, QB, o-SL-o · p = EL, AMP · r = AST, x · s = MT (m+), NT (n+) · t = h, f, K? · u = LAM, a.
The lone o is mostly a null (filler between letters); 8 appears as a null after "il" in R1139 L01.
**Corrected 2 Oct 2026 (V1921):** the lone o is a homophone for h and u ("ha", "ch'à", "che"; "qui", "suo",
"quantunque"), as the EM counts already showed (o 28, h 13, u 10); oo = b ("beni"; R1139 "de[b]ito"); z+ = q and
x+ = q (crossed ligatures like m+, n+; "qui", "quantunque", "quel"); EL = f in "oficio" (as AMP = f in "Alfonso");
K = et (M); Z = x. Homophonic, as Somogyi says; no word division; no nomenclator codes seen.

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

## Log

- 2026-09-21: DECODE R1126–R1140 metadata and images; Vestigia searches "Caprile" (52) and "Cistarelli" (20);
  contact sheets of every page. Transcription of the 1520–21 cipher by a subagent. Literature: Somogyi 2025 (R1138
  read). Key from Somogyi cribs by EM; R1139 and R1136 read in part.

- 2026-09-30 (quotation list for George Lasry): R1139 second reading pass, `r1139_pass2.txt`. Signs re-checked on
  the image where the decrypt did not read; letters proposed by a beam search over `key21_counts.json` with the
  `it-cinquecento` model and checked sign by sign. Transcription corrections: L03 "custo p ss" is "custo r ss"
  (custode); L05 "q CE" in "teneva | per" is EL (p); L05 "UT PHI" in "andata" is the crossed p (n). Now continuous
  from L05 to L07: "li go fato moto deli danari del suo de[b]ito, come mi dise messere [Alfonso]. Lui m'ha
  resposto, dice [de] voler andar in Italia quando al dare …" (C/M; "Alfonso" is enciphered a-l-p-o-n-s-o, M), and
  L08-L09 "parlaremo a longo sopra ciò … vedrò quel mi dirà, e il tuto reportarò a V. Ex." (M/I). L01-L03 still
  read only in phrases.

- 2026-10-02: V1921 (no. 12) read. Six cipher runs re-checked sign by sign on `img/v/v1921_2.jpg` (4 corrections:
  z+, x+, m+ written as "m p", ff not HH); key21 values plus five new ones forced by context (lone o = h/u, oo = b,
  z+/x+/xp = q, EL = f, K = et); 161/166 signs read, 97.0 % (`read_v1921.py`). Vestigia records checked for other
  1520-21 cipher letters: none beyond R1136, R1138, R1139, V1920, V1921.

- 2026-10-02 (later): retry and known-keys steps (see Escalation); `beam21.py`, `regrade21.py`, `pass3_r1136_r1139.md`.
  The xp ligature (= q) found in R1136 L10 also reads V1921's "quantunque" (161/166).

- 2026-10-02 (pass 4): R1136 second transcription (`r1136_pass4.txt`) 66.9 %; R1139 second pass (`r1139_pass4.txt`) 88.7 %.

- 2026-10-03 (pass 5): look-alike tabulation (`lookalike21.py`: CE = o, xp = q accepted; QB/8, c/e, AMP/EL not separable), numeral test of R1139's "4 8 1 7"/"1 7" (no fit), name and Somogyi-phrase cribs (`namecrib21.py`, nothing new); R1139 89.7 %, R1136 66.9 %. Vestigia records have no summaries.

- 2026-10-03 (pass 6): pen-shape step for QB/8, c/e/CE, AMP/EL (`shapes21.py`, sheets in `shapes21/`): automatic crops reliable for about half of QB only; QB's two forms do not follow the LM values; c is a distinct form without a consistent value; failed, stopped, percentages unchanged.

- 2026-10-11: statistical validation (`docs/_validate.py`, `validation.tsv` from `mk_validation.py`): underdetermined (V1921 alone, 161 tokens, 42 types).

- 2026-10-14: split from `caprile1519` (one key per entry). Moved here: the 1520–21 transcription, key, alignment,
  beam, regrade, look-alike, shape and V1921 files. `fraction_read` now measured over this key's letters only:
  992/1236 (80.3 %; R1139 453/505 and R1136 378/565 decoded letters inside phrases, V1921 161/166 signs).

## Remaining gaps

Blocker "left-open" is not one of the checker's outside blockers on purpose: these pieces are still workable here, and
no outside blocker (no key material, too short, illegible, physical access) honestly applies to them.

- R1136 L01-L02 stain and blot (about 6 signs, "# #" in the transcription) and R1139 L10 end - blocker: illegible; the stain covers the signs on the only image
- R1139 (6 Apr 1521), "4 8 1 7" (L01) and "1 7" (L02) - blocker: open-codes; tested as letters and as numerals (3 Oct 2026), nothing fits; likely nomenclator codes with no list
- R1139 (6 Apr 1521), other unread stretches (10 % of decoded letters) - blocker: left-open; pass 5 89.7 % (L08 "mi per Milan" added); pass 4 (`r1139_pass4.txt`, `pass3_r1136_r1139.md`): 88.7 % inside claimed phrases; L01 and L03 now read; open: numeral-like "4 8 1 7" and "1 7" (no key value) and short stretches of L02, L04-L05, L08
- R1136 (8 Mar 1520), unread stretches (33 % of decoded letters) - blocker: left-open; pass 4: second transcription at native resolution (`r1136_pass4.txt`, 11 of 12 lines changed), 66.9 % inside claimed phrases (was 59.4 %); what still stops L06, L10-L11 and the line starts is the doubtful sign separations (c/CE/e, QB/8, AMP/EL, x/xp), which a sign table over all five letters could settle; not an outside blocker
- V1921 (25 Feb 1521), 5 of 166 signs - blocker: illegible; notes: "K PHI" at the torn page edge after "in reg" (illegible); two minims "1 1" after "persuaso" have no key value (no-key-material); one QB before "Agria" probably a slip; "dicixe" and "revelta" grade M

## Escalation

- [x] siblings: R1126-R1140 and Vestigia files opened; Vestigia cipher-flagged records of the 1519-21 files are exactly V1853, V1874, V1876, V1919-V1922; the 1520-21 cipher is in R1136, R1138, R1139, V1920, V1921 only (2 Oct 2026)
- [x] clear-pages: no clear copy or gloss of R1136, R1139 or V1921 in the file; the 1882 b/c copies belong to the 1519 letters (2 Oct 2026)
- [x] known-keys: done 2 Oct 2026: key21 + V1921 values on R1139/R1136/V1921 (reads); the 1519 tables (`../caprile1519/`) are another system
- [x] print: ASMo inventory and Somogyi 2025 found; R1138 already read
- [x] key-rebuild: EM key from Somogyi cribs (89.6%); V1921 values (lone o = h/u, oo = b, z+/x+/xp = q, EL = f, K = et); pass 4 values (o+ = s, Z+/Zp = q, D = b/x, plain c = o)
- [x] retry: done 2 Oct 2026 - V1921 re-transcribed and read 97.0 %; R1139 and R1136 re-decoded with the new values (`beam21.py`), phrases checked on the crops and regraded (`pass3_r1136_r1139.md`, `regrade21.py`: R1139 83.8 %, R1136 59.4 %); pass 4 (2 Oct, later): R1136 re-transcribed and regraded 66.9 %, R1139 second pass 88.7 %; pass 5 (3 Oct) R1139 89.7 %. Still open as work, not as escalation: a full second transcription of R1136
