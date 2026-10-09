# R9241 Catherine de' Medici to Paul de Foix, 15 Jan 1563 — reading v5 (graded, 2026-10-04)

Supersedes v4. Following the adversarial review (review/review.md), every value is now either independent of this letter
(K0) or explicitly fitted on it (K1), and every reading carries a grade.

## Keys
- **K0, frozen, independent of R9241** (key_k0.json; each entry has its source). Mapping of Tomokiyo's chart of
  de Foix's 1565 cipher onto the R9241 sign names = the reviewer's independent transcription (review/published_key.json),
  plus values I verified on the 1565 letter against its own decipherment (BnF fr. 15971, Gallica btv1b105094409: cipher
  ff. 21r-22r, "Dechifré de la precedente" f. 25r, marginal decipherment f. 26r):
  - g = s (ainsi, choses, meritans), overriding the chart's d
  - f = s as well as l/u (aussi)
  - so = 50 = que ("50 f 50" = quelque; transcription note so = 50)
  - 82 = ceulx, 51 = qui ("ceulx qui se sont")
  - 37 = me or car
  - 8 = luy or m (maiesté); this is only a weak glyph match
  - ny = n (agent, monsieur, punition, Meluin) or z (chart)
- **K1, fitted on R9241 itself** (key_k1.json, with the words that motivated each value). A K1 value is called
  *replicated* if it produces dictionary words in at least 2 passages with at least 2 distinct words (v5_k1_replication.json).
  Replicated: 3=s, r=d, qs=n, Yb=u, T2=i, Z3=e, H=i, y=a, sz=m, qf=s, ch=x, ff=l, tb=r/h, Xx=b, gy=d, 2=l, Yx=p.
  Single-passage only: z=i, fh=r, Rx=m, X=s, tf=o, Fk=r, t4=r, 7x=c, 6=m.
  Several K1 values contradict K0 (r: chart m, fitted d; z: chart p, fitted i; Yb: chart l?, fitted u). The transcription
  may have merged glyphs, but I could not check the R9241 images.

## Pre-specified measure and results (v5_coverage.txt; 200 token-order shuffles, passage lengths kept)
Share of the 1,026 cipher tokens whose letters all fall in dictionary words of 4–14 letters. The decoding is a beam search
(width 48) with the same settings for real and shuffled texts.

| layer | real | shuffled mean ± sd (max) | Montaigne dict: real / shuffled |
|---|---|---|---|
| K0, grade A (unique values) | **14.0%** | 7.0 ± 1.1% (10.2%) | 5.7% / 2.3% |
| K0, grade A+B | **25.6%** | 12.7 ± 1.6% (17.1%) | 14.0% / 3.6% |
| K0 + replicated K1 (C1) | 58.5% | 20.7 ± 1.9% (26.6%) | 30.9% / 5.6% |
| K0 + all K1 (C2) | 69.6% | 24.3 ± 2.2% (30.0%) | 39.4% / 6.9% |

p = 1/201 in every row. The K1 rows are optimistic for the real text, because K1 was chosen on it.

## Text (v5_rendering.txt; word list with grades in v5_wordlist.tsv)
Notation: CAPS = A (unique under K0); {x} = B (K0, several paths); [x] = C1 (needs replicated K1 values);
[[x]] = C2 (needs single-passage K1 values); … = no word.

(1) … {ceste} [uisi] [[tation]] … ENTRE [eulx] {ques} … [estions] [dela] [paix] … [[cognois]] … {tous} [[iours]] …
[enuie] … POURL {moins} ESTRE [dela] {parties} [inten] [[tion]] … [[iuger]] AIANT FAICT … [beaulx] … [dela] [[guere]]
… [[durant]] … [trouble] … [persona] … [scauez] … [negotiation] [prend] {quelque} TRAICT … [desi] … [[laisse]]
[entendre] … [infi] [[nies]] [fois] … CEULX [peust] [[auoir]] TANT [defaueur] … [auoit] [moien] … [[sortir]]
[[prompte]] [[ment]] LARE [conciliation] [neces] [aire] ENTRE … [deux] …

(2) AUEC [ques] … [dance] [dela] … [dexte] {rite} … {espe} RITE … [tirer] … [moiens] … TOUT … [pase] …
{toutes} [fois] … FAIRE … [autre] [choses] [inon] {ceque} … ESTE … TANT [escri] …

(3) … UEOI … [aise] [defaire] … [prou] … [entendre] … [oster] [cette] [espe] RANCE

(4) … TOUTE … BIEN … FAIRE [entrer] … [quelque] … [bourse] [ment] … [deniers] … [inten] [tion] … [pourrez] …
[prendre] {quelque} [chose] … TOUTE {ceste} {sera} … [depuis] … PARTE [ment] [dudict] …

## Phrase grades (v5_phrases.json; minimum number of letter edits needed under each key)
| phrase | edits K0 | edits K0+K1rep | edits K0+K1 | grade |
|---|---|---|---|---|
| pour le moins estre de la partie | 1 | 0 | 0 | C1 |
| la negotiation prend quelque traict | 1 | 0 | 0 | C1 |
| dexterité de son esperit | 2 | 0 | 0 | C1 |
| quelque deboursement de deniers | 7 | 0 | 0 | C1 |
| et toutesfois | 1 | 0 | 0 | C1 |
| il a tousiours eu envie de / laissé entendre / la reconciliation / oster ceste esperance / en ceste visitation | 1–6 | 1–3 | 0 | C2 |
| ignorant de tout ce qui est passé ("pase") / des incommoditez ("incomoditez") / depuis le partement dudict / luy pourrez apprendre quelque chose | – | – | 1 | C3 (1 edit) |
| necessaire entre ces deux royaulmes / avecques grande abondance de langaige | – | – | 2 | C3 (2 edits) |
| faire son proufit de ce royaulme | 7 | 3 | 3 | C3: withdrawn |

No sentence reaches grade A or B. The frozen key alone gives fragments only, for example
"pour le moins estre [m]e la partie", "aiant faict", "quelque traict", "tout ce qui est pa[s]é et toutesfois",
"toute ceste sera".

## What is and is not established
- **Established.** The cipher is de Foix's (Tomokiyo's chart, unfitted: 7.8 SD; reviewer's Montaigne model: 10.7 SD).
  Under the frozen key, A and A+B word coverage is about twice the shuffled level and above every one of 200 controls.
- **Probable (C1).** The phrases in the C1 rows above.
- **Conjectural (C2/C3).** Everything else, including "abondance de langaige" and "reconciliation … entre ces deux
  royaulmes". "faire son proufit de ce royaulme" is withdrawn.
- **Unread.** About 30% of tokens are in no word even with K1; 80, 93, M, Ax and zt have no value.
- **Not shown.** That the letter was never read before.
- **Next.** Image crops of R9241, to settle the K0/K1 glyph conflicts (r, z, Yb, 3/Z3).
