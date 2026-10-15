# Antoine de Bordeaux, French resident in London: two ciphers of 1653-54 — item A read 2026-09-18

Cryptiana, *Ciphers Early in the Reign of Louis XIV*, §3 "Correspondence Intercepted in England (1653)"
(`louisxiv0.htm#SEC3`). Two items:

| | document | DECODE | status here |
|---|---|---|---|
| A | Bordeaux → [Brienne], 30 May 1653 NS; BL Add MS 4200 f. 88 (Thurloe's papers), 7 pp.; duplicates of the opening (f. ?, R8393) and the ending (R8391); English worksheets R8386, R8388, R8389 | R8390 | **read 2026-09-18** with the English key sheet R7537 + page images; see *Result* below |
| B | Mazarin → Bordeaux, 22 June 1654, copy; BnF Mélanges de Colbert 11 ff. 479-481 | R9482 | **solved by George Lasry, 19 Feb 2025**; key published on cryptiana (`louisxiv_0mazarin.png`); the ciphertext itself is not accessible here |

## Item A: the 1653 letter

**Ciphertext.** Tomokiyo's provisional transcription (`louisxiv_bordeaux.txt`, Shift-JIS) normalised into
`ciphertext.txt`: 63 lines, **810 tokens, 156 distinct symbols**, ending in the cleartext "on n'a point icy".
Symbol classes (`analysis` in this file's history; counts in tokens):

| class | distinct | tokens | most frequent |
|---|---|---|---|
| graphic / letter signs (u, x, d, ll, m, p, q, h, φ, λ, θ, ff, …) | 24 | 227 | u 47, x 29, d 28, ll 28, m 24, p 14, q 12 |
| plain numbers (0-45; ten stray ones 53-99) | 42 | 198 | 32 ×38, 33 ×33, 15 ×14, 25 ×12, 9 ×11, 17 ×11 |
| numbers with prime (4'-99', clustered 25'-75') | 33 | 168 | 43' ×23, 39' ×17, 63' ×17, 53' ×12, 54' ×10, 64' ×9 |
| numbers with two dots (5¨-99¨) | 40 | 156 | 20¨ ×31, 97¨ ×11, 85¨ ×9, 73¨ ×9, 74¨ ×9 |
| numbers with overbar (25‾-96‾) + 332, 344, 396‾ | 14+3 | 37 | 96‾ ×12, 94‾ ×8, 86‾ ×3 |
| 4- (4 with a stroke) | 1 | 25 | |

IC over tokens 0.019; the graphic signs are frequent enough to be letters (u, x, d, ll, m ≈ 3-6 % each), and
"x p" (×14), "x u" (×9), "m u" (×7), "q u" (×4) are probably compound glyphs. Repeated bigrams are few
(ll 20¨ ×7, u 33 ×8, 4- 33 ×5, 32 39' ×5).

**What the cipher is.** The office that issued it (Brienne's secretariat) used one design throughout 1651-54,
known from two recovered keys on cryptiana: Brienne's Cipher 2 to d'Estrades (1651: letters = numbers 3-24 +
graphic signs; syllables BA 27 … GU 64 then HA 1_ … VV 62_ in a second, marked series) and Lasry's key for
item B (1654: letters = graphic signs; syllables BA 59‾ … JE 99‾ then JO 3¨ … VO 50¨, with DES, EST, ESTRE,
FAIRE, FAIT, ON, OU, TANT embedded alphabetically). In both, **consecutive numbers run through the CV syllabary
in alphabetical order, the series changing at 100, with a few gaps and a few function words in place**. The
1653 letter has the same ingredients (letters as graphic signs and low plain numbers; three marked series),
so the working hypothesis was: prime and two-dot series = the syllabary in order; overbar series (and the
three-digit groups) = nomenclature. The 1654 key does not read the 1653 text (its two-dot series stops at 61;
here 73¨-99¨ carry 60 tokens), so the keys differ.

**Plaintext search (negative).** Birch printed twelve Bordeaux → Brienne despatches of 1653 in French from
the Saint-Germain letter-book (Thurloe SP i, 5 June to 8 Jan 1654) and Guizot printed sixty more of 1653-58
from AE Corr. pol. Angleterre (*Histoire de la République d'Angleterre*, 1854, t. II appendix, used here as
`guizot_docs_raw.txt`); **30 May 1653 is in neither**. No English decrypt of it is in Thurloe SP i for May-June
1653 (all intercepted letters there checked). Wallis's Bodleian collection of decipherments ends with a French
letter of 4 April 1653, so he did not do this one; the frequency tables in Add MS 4200 (R8386-9) are an
unfinished English attack. **Lead:** DECODE **R7537 = BL Add MS 32263 f. 1**, the Deciphering Branch's key
volume (Willes papers, "cipher-keys 1653-1850", not digitised), catalogued as a numerical simple-substitution
key of **1653, London, receiver "Mr. Bordeaux"**. That is almost certainly the English reconstruction of this
cipher; it needs a DECODE login or a BL order.

**Ciphertext-only attack with matched controls.** `lm.py`: spaceless 6-gram French model on 5.3 M letters
(Chaulnes corpus + Guizot's Bordeaux despatches). `solver.py`: simulated annealing over (i) a free homophonic
map for letter symbols (nulls forbidden after v1 collapsed into nulls), (ii) a **monotone alignment** of the
ordered syllable slots onto the alphabetical unit list (90 CV syllables + 40 function words), moved by single
re-seatings and block shifts, (iii) overbar tokens as unknown words cutting the text into 36 segments.
`make_control.py`: a Bordeaux despatch of 28 June 1654 enciphered with a random key of the assumed design,
same symbol inventory, 810 tokens. Design A = syllables over prime then two-dot series; design B = prime
numbers are letter homophones, syllables in the two-dot series only.

| run | true key | solver best (per seed) | tokens recovered |
|---|---|---|---|
| control 1, design A | -839 | -846 / -2941 | **99.3 %** / 20 % |
| control 2, design A | -841 | -839 / -868 / -2866 / -2704 | **99.9 %** / **99.3 %** / 11 % / 34 % |
| control 1, no alphabetical constraint | -839 | -2002 | 0.7 % |
| control 4, design B (90 letter symbols) | -650 | -1824 / -1464 / -2001 | 26 % / 9 % / 16 % |
| control 5, design A, 10 % of diacritics misread | -1180.6 | -2808 / -2962 | 52 % / 9 % |
| **real, design A**, order prime→dots, 7 seeds | ? | -2768 … -3004 | — |
| real, design A, order dots→prime, 7 seeds | ? | -2768 … -2962 | — |
| real, design A, plain>45 first, 7 seeds | ? | -2953 … -3366 | — |
| real, design A, syllables only (no words), 9 seeds | ? | -3174 … -3881 | — |
| real, design B, 4 seeds | ? | -1913 … -2030 | degenerate (e s t n salad) |
| real, unconstrained, 3 seeds | ? | -1610 … -1996 | degenerate (POUR FAIRE FAIT salad) |

Reading: the alphabetical-syllabary prior makes an 810-token cipher of this family solvable ciphertext-only
(three of six clean control seeds land on the true key to within 30 nats), which is itself a result worth
keeping. But every design-A run on the real text stops at the control's *failed*-seed level (-2770 to -3400),
21 seeds over three series orders and two unit lists, and inspection shows word salad rather than partial
French. Since the same solver solves its controls, the real cipher does not fit design A as posed: most
likely the prime series is not (only) syllables, or the transcription's diacritics are not reliable enough
to preserve the order: control 5 shows that misreading one diacritic in ten already drops the solver to 52 % and 9 % on two seeds, with scores in the real cipher's band, so a *provisional* transcription is enough to explain the failure on its own. Design B, which would put ~90 homophones on 24
letters, is beyond ciphertext-only reach at this length even in a clean control. **No reading is reported.**

**Ways in (as of 2026-09-16; (1) done 2026-09-18, see Result).** (1) DECODE login: the page images of R8390 (to fix the diacritics, which decide the whole
structure), and R7537, the 1653 English key for "Mr. Bordeaux". (2) The plaintext: the Saint-Germain
letter-book Birch quoted (now BnF, fonds Saint-Germain français) or AE Corr. pol. Angleterre 62 for 30 May
1653; either would give the key by alignment. (3) A second letter in the same cipher (Bordeaux's despatches
of April-July 1653 were routinely intercepted).

## Result (2026-09-18): item A read

DECODE access came through (session cookie; images local and git-ignored). **R7537 (BL Add MS 32263 f. 1)** is headed
"To Mr. Bordeaux French M.r at London 1653 / Key & Calculation / Discovered Aug. 20th 1832" (the year reads 1832; the sheet is
printed ledger paper numbered 2801-3000, so a later Deciphering Branch working, not a 1653 original). It is a worksheet:
a left column of candidate letters per number, and boxes of settled values. Transcribed in `key7537.txt`. It confirms the design A
hypothesis exactly: **plain 15-37 = a-z; the prime, two-dot and overbar series are alphabetical CV syllabaries with words
embedded** (prime: pa 25' … pu, pour 31', par 32', qui 38', que 39', ra 42' … se 53' … te 63' … ve 73' … vous 79';
two-dot: da 19¨ … du, dans 24¨, et 28¨, estre, estat 32¨, fa 37¨ … fu, fort 42¨, ge 49¨ … ha 60¨ … hu, ja-ju 66¨-70¨, il,
la 73¨ … lu, les, leur 79¨, leurs 83¨, ma 84¨ …, na 96¨ … nu 100¨; overbar: ba 83‾ … bu, bien, bon, ca 93‾ … cu 97‾).
Graphic signs (from the sheet's "Principal" list and context): u=n, m=e, a=r, x=o, **x p=a** (compound), p=p, ꝺ=u, **∂=n**,
q=i, ll=r, 4-/4=s, ≠=g, h=p, H/e=z, 9=i, φ=y, λ=s, θ=i, ω=n, o=x, y=p, ff=t, 〃=n, )=n; plain homophones above 37
(38=et, 43=re, 54=si, 97=ne, …) are the syllable numbers written without their mark. Context-derived additions are in
`key_guess.txt`; `key_work.txt` = both; `apply_key.py key_work.txt` decodes `ct2.txt`.

**Why the solver failed.** Checking the page images (`ct2.txt`, 21 corrections, one of them the 52' in *commissaires* restored from the duplicate R8393) showed that Tomokiyo's "d" merges two glyphs,
ꝺ = u and ∂ = n; tokens are dropped (line 2 lost 76¨ and 27); marks are lost (97¨→97, 96¨→96‾, 74'/79'); and the cipher
clerk himself often omits the diacritic (plain 38/43/45/54/97 for the marked syllables). The design was right. What broke the
solver was the transcription plus the clerk's own slips, as control 5 predicted.

**Content** (`plaintext_1653.txt`): the Council heard the Bordeaux (Ormée) deputies through two commissioners before
Cromwell ("le General") gave Bordeaux his audience; the treaty agreed after the Parliament's resolutions is still unsigned;
England may help Bordeaux indirectly, so Brienne should hold back the offer of French mediation; English fear that a France
rid of sedition would back the Stuart party could push Cromwell against French interests. The letter continues in clear
(ff. 89v-90: news of the fleet off Scotland).

**Still open:** name codes 25‾, 28‾ (probably Charles II / the Stuart court), 43‾ (the Bordelais?), 332, 344, 396‾; the rare
tokens 6¨, 10, 30', 35', 68', 98, 14', 46¨ (context: "la [France?]"); "fort" at 42¨ where context wants "faire".
R8392 has **no images** on DECODE (0 attached, checked logged-in). R8391 (f. 92 frequency count, which lists d and ∂ as separate signs; ff. 93-93v a duplicate of the ending that agrees
token for token, so 68' and 24 are genuine) and R8393 (duplicate of lines 1-9) checked; R8386-9 not yet used.

## Item B: the 1654 copy

Lasry's key (cryptiana image, dated 19 Feb 2025): 24 graphic letter signs; syllables 59‾ BA … 99‾ JE, then
3¨ JO … 50¨ VO in alphabetical order (BE, BI, BU are the "unknown" 61‾-63‾); nomenclature DES 70‾, EST 77‾,
ESTRE 78‾, FAIRE 79‾, FAIT 80‾, OU 20¨, ON 21¨, VA 47¨, VE 48¨, VO 50¨, TANT 61¨, and one code for a person.
DECODE still marks R9482 "Non-decrypted". Mélanges de Colbert 11 is not on Gallica (checked by SRU); the
BnF catalogue (`cc95411w`) lists f. 479 "Copie d'une lettre chiffrée, adressée par le cardinal Mazarin à
Antoine de Bordeaux de Neufville … 1654" and f. 474 a "Mémoire des lettres à deschiffrer" for d'Effiat.
Nothing to solve here without the images; the item should be marked solved (Lasry) in DECODE and in the
cryptiana list is already so marked. Chéruel's *Lettres de Mazarin* vi has other letters of 22 June 1654 but
not this one (Tomokiyo).

## Files

`ciphertext.txt` (normalised tokens) · `lm.py`, `lm6.pkl`, `corpus_fr.txt`, `guizot_docs_raw.txt` ·
`solver.py` (`--order`, `--primeletters`, `--nowords`, `--truth/--truthscore`) · `make_control.py <seed> [A|B]
[noise]` · `control*.txt`, `control*_key.txt`, `control*_plain.txt` · `run_*.txt` (all runs above).

## Corrections

- 30 Sept 2026: the English paraphrase of the first cipher sentence on docs/bordeaux1653.html is corrected; the
  French reading (`plaintext_1653.txt`) is unchanged. The sentence is "Ce n'est pas que si nos affaires estoyent
  plus florissantes nous n'eussions sujet de tesmoigner quelque mescontentement de la reception qui a esté faite aux
  deputez de Bordeaux". After "ce n'est pas que", the lone "ne" of "n'eussions" is a full negation (classical use,
  as in "ce n'est pas que je ne l'estime"). So it means "not that, were our affairs more flourishing, we would lack
  cause to show some displeasure": France has the grievance but, weakened by the Fronde, cannot afford to show it,
  which is why the rumour of his recall is false. The page had "Even if our affairs were more flourishing, we would
  still have reason to show some displeasure", which makes the grievance independent of France's position. The
  paraphrase now reads "Not that, were our affairs more flourishing, we would lack cause to show some displeasure
  at the reception given to the deputies of Bordeaux". Section 05 ("What it says") gains one sentence on the point.

## Assumptions for George's review (14 Oct 2026)

- Credit: George's 2025 solution is of item B (Mazarin to Bordeaux, 22 June 1654, R9482), a different key that does
  not read item A. He is therefore no longer credited with a prior solution of this entry, whose only document is
  item A (1653). He keeps a "pointer" credit because his item-B key showed the design (syllabary numbered in
  alphabetical order, series changing at 100) that the item-A solver used as its hypothesis. If he prefers no credit
  at all on item A, the pointer can be dropped.
- Item B has no entry of its own here: its ciphertext is not accessible (Mélanges de Colbert 11 is not on Gallica),
  and the solution is his.
