# R2242 — Prince Frederick of Orange to the Hereditary Prince, London, 7 May 1795 (KHA, Koning Willem I, XVIII-3)

Status: read (3 Oct 2026: 994/1,037 tokens = 95.9% read as sense, strict measure; meets the read bar. The open tokens are
single word signs with no key material and two ink blots. Key: partial, the square complete, word signs open.)

DECODE R2242 ("KHA_A35_KWI_inr.XVIII-3_Prince_Frederick_to_Heredary_Prince_1795-05-07"), Non-decrypted,
4 pp., authentication-required images IMG_R2242_I15891–I15894 (photographs of photocopies, sideways; git-ignored
in `img/`). DECODE's note: not signed; the first lines point to Prince Frederick (Willem George Frederik,
1774–1799) writing to his elder brother; the cipher part "seems to be written by somebody else, originating
from a letter sent under cover to his banker"; the cipher "seems to point to a link with the Rassemblement de
Osnabrück"; the record asks for a pointer to R1892.

## System: the R1892 key, unchanged

Each letter is a vertical pair of digits 1–6 (top over bottom), monoalphabetic, plus graphic word signs. The key
recovered ciphertext-only for R1892 (`../r1892/NOTES.md`) reads this letter as it stands, which confirms that
DECODE's pointer is right: the same cipher, in Dutch here. `apply.py` is R1892's with the circle-with-dot sign
rendered DE, as in R1892.

The key is confirmed independently on page 1, where a contemporary hand wrote the clear Dutch under the four
cipher lines (a decipherment at the time, or the writer's own draft): every digit word agrees with it, and it
gives the values of a dozen word signs (below).

## The pages

- **p1 (cipher + clear under it).** "als deezen brief geleesen hebt, dan [is de zaak] genoomen en gebraaden. Zo
  het niet verandert, moeten wy niet in de Zee. Als de Erfprins iets begeert, zoo zulks maar weet: ben tot zijn
  dienst, dood of zoo te leeven, is het zelfde." The cipher continues on p3.
- **p2 (clear, dated "Den 7 Mey 1795").** "Weest zoo goed en zegt aan mijn Broer dat hij een brief van mij onder
  couvert van mijn Banquier van E… ontfangen moet hebben": money matters with the banker, a "wissel", letters
  from Hamburg that never arrived, "Robespierre"-era news; one word in cipher: 24 43 25 55 15 15 65 = **famille**.
- **p3 (17 cipher lines) and p4 (8 lines + P.S.)**, one continuous text (p3 ends "ra-", p4 begins "-tificatie").

## What the cipher says (p3–p4, Dutch; [x] = word sign with its value, | = unread sign)

Reading after the second pass of 2 Oct 2026 (values and grades in the sign tables below). The letter dates from
late May or June 1795: the ratification it speaks of is that of the Treaty of The Hague with France (16 May 1795),
carried to Paris by the extraordinary envoys De Sitter and Van Grasveld (received by the Convention 23 June 1795).

- "[de] [brief] braaden. Wat zeid men [van] onse alliansie met [Frankrijk]? Geeft [dat] ook verandering? Men heeft
  de offeciers en de trouppes [zoo] wel [uit] malkander gelegen, [daar] is [zoo] [weinig] staat op veele der
  gedimitteerde offeciers te maaken, [dat] men zig [daar] niet veel | [van] | [voor]stellen; ook is er geen
  de minste saamenhang tussen [dez]elve, zy [zijn] geheel verstrooyd en [zonder] hooft" — the émigré troops and
  dismissed officers scattered, without cohesion or leader.
- "… natuurlyk zoude | en [dat] zig [voor] | zouden toonen hebben, zig niet brilliant ge| | vreese [dat] de
  benauwtheid de politiken ook | [dat] verslappen | | er [daar] men op | vertrouwen | als aen o[ns?] [als] men
  zig [maar] niet [al] te veel openden [dat] het point der coalitie met alle [mogelyk]e | heid behandelt word."
- "Men heeft de ratificatie [van] ons met [Frankrijk] gepubliceert, of schoon de ratificatie zelver nog niet
  gekoomen was. Het was op | echte [brieven] [uit] Parys [van] onse ministers Meier en Blaauw, en nu zyn nog
  [naar] [Frankrijk] [als] ambassadeurs gesonden (interlined: [de] Sitter en [van] Grasveld) om de ratificatie van
  onse | t' oover te brengen." Blauw and Meyer were the Batavian negotiators in Paris (Gedenkstukken I no. 507).
- "[Als] [Engeland] [maar] blyft persisteeren [om] het tegenwoordig gouvernement niet te erkennen, dan [zoo] zy
  geen Robespierismus durven te introduseeren [daar] | zeer veel dispositie | is. Myn respect [daar] het behoort
  [is] het geheele geselschap nog [daar]. | Hier | omstandig antwoort. Groet myn broer."
- P.S. "Dankaert is ook [uit]landig | | | al | met hen." (Dankaert unidentified; the sign after 'landig' is under
  an ink blot.)

Decrypts: `decrypt_p1.txt`, `decrypt_p3.txt`, `decrypt_p4.txt`; transcriptions `transcription_p*.txt`
(LLM transcription from the photographs; several pairs doubtful, marked ?).

## Word signs fixed by the page-1 clear text

| sign | value | | sign | value |
|---|---|---|---|---|
| > ⊙ ▱ | als deezen brief | | ÷ | zoo |
| δ-loop | genoomen | | ɣ | zulks |
| H-bar | zo / zoo | | § | maar |
| long S | moeten | | v | tot |
| ⊙ Y | de Zee | | crossed 8 | zijn |
| > ⊙ ♁ | als de Erfprins | | ʃ | zelfde |

⊙ alone = de (R1892). The p3–p4 signs were read from context on 30 Sept and 2 Oct 2026 (tables below); twenty
single-occurrence signs stay open.

## Prior art

DECODE: Non-decrypted, no transcription or decipherment on the record. The only decipherment is the clear text on
page 1 itself. This is the first reading of pages 3–4; the key came from R1892 (this project, 21 Sept 2026).
Print (2 Oct 2026): the letter is not in Colenbrander's *Gedenkstukken* (see Escalation for the search).

## Word signs read from context (30 Sept 2026, for the Lasry quotation)

Re-read on the photographs (p3 lines 1, 13-17, p4 lines 1-2). Grades: H key/page-1 clear text, M probable, I context.

| sign | value | grade | occurrences |
|---|---|---|---|
| script L | uit | I | "[zoo] wel [uit] malkander gelegen" (p3 l3); "[uit] Parys" (p3 l16); P.S. "is ook [uit]landig" |
| flagged D-shape (a D with a hook at the top; distinct from the plain Δ of p3 l11, p4 l1, p4 l5) | van | I | "wat zeid men [van] onse alliansie" (p3 l1); "de ratificatie [van] ons met" (p3 l13); "[uit] Parys [van] onse ministers" (p3 l16) |
| φ | Frankrijk | I | "onse alliansie met [Frankrijk]" (p3 l1-2); "ratificatie van ons met [Frankrijk]" (p3 l14); "zijn nog < [Frankrijk] > ambassadeurs" (p3 l17) |
| ⊥ | om | M | "blijft persisteeren [om] het tegenwoordig gouvernement niet te erkennen" (p4 l2); R1892 p2 "<perp> op antwoord te wagten" = "[om] op antwoord te wachten" |
| > | als | H | fixed on p1; "[als] ambassadeurs" (p3 l17); "[als] | maar blijft" (p4 l1) |
| H-bar | zoo | H | fixed on p1; "de trouppes [zoo] wel [uit] malkander" |
| parallelogram | brief (here plural, brieven) | H/I | fixed on p1; "op | echte [brieven] [uit] Parys" (p3 l15) |

Line 15 re-read: 34 65 11 12 43 44 22 45 = "het was op", a small x (sign or correction mark, open), then
65 51 [3]4 11 65 = "echte" (the 34 is half under an ink blot), then the parallelogram. Line 16 opens with the script L,
45 43 52 13 44 "parys", then the flagged D-shape, "onse ministers meier en blaauw en nu".

Still open in the passage on 30 Sept ("<" and "&" adopted 2 Oct, see Second pass): "<" (p3 l17, "naar"? I), "&" (p4 l1, the subject of "maar blijft
persisteeren"; England is a guess only), the plain Δ in "van onse Δ 't oover te brengen", and the x on l15.
The p4 interlinear insertion reads 44 55 11 11 65 52 65 32 [flagged D] 41 52 43 44 33 65 15 31 "sitteren [van]
grasveld", probably two names (a Batavian envoy "Grasveld"?); not identified here.

Consequence for the date: if φ is France, "the ratification of ours with France" is the Batavian alliance with
France (Treaty of The Hague, 16 May 1795), which puts pages 3-4 after 16 May, later than the clear p2 letter of
7 May. The page and summary now say so; the Basel reading is withdrawn.

Quotation for the Lasry list (30 Sept 2026): "… men heeft de ratificatie [van] ons met [Frankrijk] gepubliceert,
of schoon de ratificatie zelver nog niet gekoomen was … maar blijft persisteeren [om] het tegenwoordig gouvernement
niet te erkennen, dan zoo zij geen Robespierismus durven te introduceeren …"

## Second pass (2 Oct 2026)

**Images.** The four DECODE photographs were not in this checkout; the rotated full-resolution copies and strips
made on 21 Sept were found in the old worktree `.worktrees/r2242/r2242/img/` (r1.png–r4.png, 3648×5472) and copied
to `img/` (git-ignored). A fresh DECODE download with the session cookie returned a 5 kB placeholder.

**Re-transcription of the two flagged lines, at full resolution.**
- p3 l1: every pair confirmed as transcribed: ⊙ ▱ 35 52 43 43 31 65 32 | 12 43 11 21 65 55 31 25 65 32 | flagged D |
  22 32 44 65 43 15 15 55 43 32 44 55 65 25 65 11 = "[de] [brief] braaden wat zeid men [van] onse alliansie met"
  (H). The "1" at the right edge is the page number.
- p4 l8: H-loop 34 55 65 52 ψ 22 25 44 11 43 32 31 55 41 13 32 11 12 22 22 52 11 41 52 22 65 11 25 13 32 35 52 22
  65 52. Corrections: the sixth pair of "woort" is 22 (the old 32 was a hooked 2), and the last is 52 (a 4
  overwritten by a 5), so "…omstandig yn t woort groet myn broer." 13 32 11 (y n t) is clearly 1 over 3 on the
  page; read "antwoort", taking the 1 as the writer's slip for 4 (M).
- Also re-read: p3 l2 end = "offeciers" (cramped at the margin, M); p4 l6 "is aet" → 55 44 34 65 11 "is het" (H,
  the 34 is clear); p3 l11 after "vertrouwen" the bracket and 43 15 44 43 65 32 22 52 ("als aen or", the 3 and 22
  underlined in the original) are confirmed; the faint interlinear "als a e n o λ" above them is a reader's
  attempt at the same pairs, not new text. Five doubtful pairs were resolved where the earlier notes gave a
  probable value (benauwtheid, zig, brilliant, echte, ministers); p1 l4 "dtenst" → 55 "dienst" (the clear text).

**Word signs, second pass** (grades: H fixed by clear text, M several contexts or a sibling agree, I one context):

| sign | value | grade | evidence |
|---|---|---|---|
| Λ | dat | M | "geeft [dat] ook verandering"; "te maaken, [dat] men zig"; "en [dat] zig"; R1892 three times ("op de volgende wyze: [dat] alle heeren officieren") |
| slashed / crossed Λ | dat | I | "vreese [dat] de benauwtheid"; "openden [dat] het point der coalitie" |
| ∞ | daar | M | "[daar] is zoo weinig staat op"; "dat men zig [daar] niet veel van … voorstellen" (daar … van); "[daar] men op … vertrouwen"; "myn respect [daar] het behoort" |
| < | naar | I | "zyn nog [naar] Frankrijk [als] ambassadeurs gesonden", the pair of > als |
| check over bar | zonder | M | "zy zijn geheel verstrooyd en [zonder] hooft" |
| crossed e | zijn | M | "zy [zijn] geheel verstrooyd"; the p1 crossed 8 = zijn is probably the same sign |
| X | weinig | I | "[daar] is zoo [weinig] staat op … te maaken" |
| crossed x | al | I | "maar niet [al] te veel" |
| & | Engeland | I | the power that "blijft persisteeren om het tegenwoordig gouvernement niet te erkennen" |
| + | mogelyk | I | "met alle [mogelyk]e …heid behandelt" |
| crossed diamond | voor | I | "niet veel … van … [voor]stellen"; "dat zig [voor] … zouden toonen hebben" |
| Y with crossbar | ik | I | "[ik] vreese dat de benauwtheid" |
| crossed Y | dez- | I | "tussen [dez]elve" (the digits give only "elve") |
| flagged D, also p3 l5 | van | M (was I) | now also "niet veel … [van] … voorstellen" and the interlinear "Sitter en [van] Grasveld" |
| inverted D with stroke (interlinear) | van | M | "[de] Sitter en [van] Grasveld": Gedenkstukken I p. 655 names the envoys Grasveld and De Sitter |

Still open (one occurrence each unless noted): T-bar and S-stroke ("niet veel [T] van [S] voorstellen", probably
"goeds" and "kan"/"hen", not adopted); square bracket (p3 l7); H with P (l8); dagger (l8); V-with-cross ("ge[V]",
l9); C-hook (l10); % (l10, p4 l4); crossed o (l10); plain Δ (p3 l11 "op [Δ] vertrouwen", p4 l1 "ratificatie van
onse [Δ]"; "Staaten" or "zyde" fit one context each, not adopted); vertical bracket (l11); crossed circle (l12,
over an ink blot); x mark (l15); Δ with tail (p4 l5); H with loop and ψ (p4 l8, "[?] hier [?] omstandig
antwoort"); S, crossed ø and ⊖ in the P.S. 20 sign tokens and 2 ink-blotted tokens.

**Measured** (`apply.py --measure`, `measure_sense.py`; both count every digit pair and word sign on p1, p3, p4,
parentheticals excluded):

| | tokens given a value | tokens read as sense (nl-modern, 13-char window > −4.3) |
|---|---|---|
| before (HEAD transcription, signs as of 30 Sept) | 982/1,031 = 95.2% | 887/1,031 = 86.0% |
| after (2 Oct transcription and signs) | 1,015/1,037 = 97.9% | 981/1,037 = 94.6% |

The sense threshold is calibrated on p1, whose decrypt the clear text under it confirms (110/111 pass), against
letter-shuffled p3/p4 controls (about 5% pass). By page after: p1 99.1%, p3 95.9%, p4 90.1%. The LM checks only that
the letters read as Dutch; a wrong word value that is still Dutch passes, so the I-grade signs inflate it slightly.
The 21 Sept profile figure (93%, 966/1,040) was counted by a scratchpad script that is gone; the two rows above are
both counted with this folder's scripts.

## Third pass (3 Oct 2026): measured against the read bar

**Measure, made stricter and fairer.** `measure_sense.py` (all switches documented in its header):
- `STRICT=1` (used for every figure below): a word-sign value graded I (context only, other words would fit)
  counts as **unread**. Only H and M values count. M now also covers a sign whose one context admits only one
  word grammatically (apply.py header). Upgraded on that rule, each with its forcing context:
  script L = uit (three contexts agree: "uit malkander", "[brieven] uit Parys", "uitlandig"); φ = Frankrijk (three
  contexts, and the printed history: alliance, ratification and envoys all "met/naar Frankrijk"); crossed Y = dez-
  ("tussen [?]elve" admits only dezelve); slashed and crossed Λ = dat (Λ variants; "ik vreese [?] de
  benauwtheid", and "[?] het point der coalitie … behandelt word" is a verb-final subordinate clause, so its
  conjunction is dat); Y with crossbar = ik (subject of first-person "vreese"); crossed x = al ("maar niet [?] te
  veel", the fixed phrase); < = naar ("gesonden [?] Frankrijk"). Still I and so counted unread: X weinig, & Engeland,
  + mogelyk, crossed diamond voor.
- Word check: a read token also passes when it lies inside an attested word of 6+ letters in the decrypt, words taken
  from the lang/ nl corpus and from Colenbrander's *Gedenkstukken* I–II (1789–1798 Dutch and French, fetched by
  `fetch_gedenkstukken.py` into git-ignored `gs_corpus/`). The nl-modern corpus is 1.5 MB, so period spellings
  (alliansie, gedimitteerde, persisteeren) failed the LM window although they are plain Dutch.
- y scored as ij for Dutch models: pair 13 is the writer's ij (zyn, myn, zy), the corpus spells ij.
- Control: the same test on letter-shuffled p3/p4 decrypts passes 8.4% of tokens (max 12.2% over 5 seeds), the
  same rate with and without the word check, so the word list adds no false passes at this word length.

**Transcription.** p3 l6 "saamendang" → 34 "saamenhang" (the pair is 3 over 4 on the image). Re-checked and left as
written: p4 l3 "persisteern" (the writer dropped an e: the image has t e e r n).

**Result** (`STRICT=1 python measure_sense.py . nl-modern transcription_p1.txt transcription_p3.txt transcription_p4.txt`):

| state | tokens read as sense, strict | same, I-grade values counted |
|---|---|---|
| HEAD transcription and the 30 Sept signs, today's measure | 941/1,037 = 90.7% | 959/1,037 = 92.5% |
| 2 Oct pass, strict, LM window only (no word check, no y→ij) | 940/1,037 = 90.6% | 981/1,037 = 94.6% (the 2 Oct figure) |
| + word check | 953/1,037 = 91.9% | |
| + forced-sign upgrades | 979/1,037 = 94.4% | |
| **3 Oct** | **994/1,037 = 95.9%** (p1 100%, p3 95.7%, p4 94.5%) | 1,000/1,037 = 96.4% |

What got it over the line: the forced-sign upgrades (+26 tokens: the signs themselves and the read letters next to
them that had no scoring window), the y→ij scoring (+15) and the word check (+13). Tokens given a value: 1,010/1,037 strict (97.4%),
1,015/1,037 with I values. The letter now meets the read bar's numbers (95% read as sense, no gap untried, what
stays open is scattered single word signs and ink blots); `outcome.class` was left "read in part" by this pass because the
class change had to reach the README row and the site. Reclassed **read** with the write-up update of 3 Oct 2026: the
letter (p1, p3, p4 are pages of one letter) is 95.9%; p3 95.7% and p4 94.5% on their own. The single word signs were
relabelled from open-codes to no-key-material: each occurs once or twice, none occurs in R1892 with a value, there is
no key sheet and the letter is not in print, so no material exists to value them.

## Remaining gaps
- signs that occur twice (plain Δ: p3 l11 and p4 l1; %: p3 l10 and p4 l4; crossed diamond, value voor at I only) - blocker: open-codes; no value fits both occurrences, retried 2 and 3 Oct 2026
- nineteen signs that occur once (T-bar, S-stroke, square bracket, H with P, dagger, V-with-cross, C-hook, crossed o, vertical bracket, x mark, Δ with tail, H with loop, ψ, P.S. S / crossed ø / ⊖, and X, &, + whose context-only values weinig / Engeland / mogelyk are counted unread) - blocker: no-key-material; a single context cannot fix a word sign, none occurs in R1892, no key sheet, not in print
- two tokens under ink blots (p3 l12 crossed circle, P.S. sign after "landig") - blocker: illegible; the photocopy is blotted at both places
- P.S. "Dankaert" unidentified - blocker: no-key-material; the name is spelled out in the square, only its identity is unknown

## Escalation
- [x] siblings: R1892 (same key) used; its signs pooled with R2242's on 2 Oct 2026 (Λ = dat confirmed by three R1892 contexts; R1892 phi, S, Y-cross, x and cross do not take R2242's values); R2236/R2237/R2239 (hereditary1796) use a different numbered word list and share no signs
- [x] clear-pages: p1 clear text under the cipher used as crib; p2 clear letter read
- [x] known-keys: R1892 key applied unchanged
- [x] print: searched 2 Oct 2026 - Colenbrander, Gedenkstukken I (1789-1795) and II (1795-1798), full text on resources.huygens.knaw.nl/retroboeken/gedenkstukken, for Grasveld, Sitter, Blaauw, Robespierismus, gebraaden, persisteeren, saamenhang, gedimitteerde, verstrooid, Banquier, rassemblement, "Prins Frederik aan", ratificatie; GS II pp. 834-841 (May-July 1795 letters) read: the letter is not printed; GS I p. 655 and p. 678 confirm the envoys De Sitter and Van Grasveld and the ministers Blauw and Meyer
- [x] key-rebuild: word signs extended from context, 30 Sept 2026 (uit, van, Frankrijk, om) and 2 Oct 2026 (dat, daar, naar, zonder, zijn, weinig, al, Engeland, mogelyk, voor, ik, dez-; flagged D and the interlinear inverted D = van)
- [x] retry: 2 Oct 2026 - p3 l1 and p4 l8 re-transcribed at full resolution and rerun with apply.py; p3 l2 end, p4 l6, p3 l11 and five doubtful pairs re-read; every unread sign retried against the extended key, R1892 and the printed context, and regraded (table above). 3 Oct 2026 - every token failing the sense test re-checked (measure_sense.py --show); p3 l6 corrected; sign grades re-examined under the forced-context rule; measured strict 95.9%
