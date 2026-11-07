# Pieter Battier to Gaspar Fagel, Madrid, 1686–1688

Status: in progress (21 Oct 2026; 23 Oct r2n: the located passages read on the scans, six decoded, not read): WAINUT's passages in seven 1687 letters (PR #65, #67; 67R lines 1-3 are in both) wait on an eye check of 158 machine-read key rows.
**22 Oct 2026, reading audit** (George Lasry's test): the 4 December 1687 (92L) and 12 February 1688 (100R) cipher blocks have holes in most sentences and are now *decoded, not read* in profile.json, as the strict screen already said. fraction_read 55% -> about 49% (estimated; the two letters' 482 tokens no longer count).


**22-23 Oct 2026, re-read (REREAD_BRIEF, batch b17).** 4 Dec 1687 and 12 Feb 1688 read as whole letters:
`readings/1687-12-04_reading.md`, `readings/1688-02-12_reading.md` (with `_en.md`, `_corrections.tsv`; log
`readings/1687-12-04_1688-02-12_reread_log.md`). The cipher blocks were re-read on the NA scans and every doubtful group
looked up on the key scans: 12:908 Turcken (not getwist), 3:352 by, 11:403 Secreet, 8:48 minste, 14:455 voordragen,
11:678 soo; 99R's last cipher line ("Gravinne van Soissons") and 100L's cipher line (11:784 de Coninginne) were missing
from the token files. No decipherment sheets on scans 90-94 or 98-102. _check_reading.py cannot score Battier's Dutch
(modern word list: 0.09 and 0.06); explicit holes only: 0.96 and 0.94. fraction_read about 0.61 (estimated).


**23 Oct 2026, triage of the unread volume letters (batch r2j).** All scans of the letters listed "not read" in
`inv/orch_letters.tsv` fetched full size (35-36, 54-88, 93-106; scan 99 would not download) and contact-sheeted. Every
letter is Battier's to Fagel in the same volume and the same number system, so all belong to this target. **No cipher**
in 10 Apr 1687 (56R-58L), 11/22 May 1687 (60R-65R, with French and Spanish enclosures in clear), 31 Jul 1687 (70R-72L),
28 Aug 1687 enclosures (74R-77R), 9 Oct / 23 Oct / 6 Nov 1687 (82R-88L) and 25 Mar 1688 (105R-106L): closed. **Cipher
located, not read**: 2 Jan 1687 35R/36L (interlinear decipherment of the time, not transcribed), 13 Mar 1687 54R (about 8
lines) and 55R (about 5), June 1687 67L (about 6), July 1687 69L (3 lines, 34 groups), Aug 1687 73R (about 4), Sept 1687
78R (about 5) and 80R (about 7), 18 Dec 1687 93R and 94L (about 25 lines) and 94R after l. 5, 1 Jan 1688 95R (about 5),
99L (3), 26 Feb 1688 102L (two passages, about 45 groups, faint interlinear decipherment) and 11 Mar 1688 103R (about 2).
Pilot on 69L (`tokens/s069L_r2j_draft.txt`): groups transcribed and ten codes looked up on the key scans with
`research/reading_audit/b17_keylook.py` ("dat men namentlyk met dese declaratie ... afflictie en in Engelandt ...
aanhouden ..."); the third line gives no sense with the marks as read, so the marks need a second look: not read.
Draft tokens for 102L in `tokens/s102L_r2j_draft.txt`. Each passage needs its marks read group by group and most codes
looked up (the dict holds only codes used so far): workable with the key, not done in this pass.

**23 Oct 2026, the thirteen located passages (fourteen when 54R and 55R are counted separately) read on the scans (batch r2n).** Every group of 35R/36L, 54R, 55R, 67L,
69L, 73R, 78R, 80R, 93R, 94L, 94R after l. 5, 95R, 99L (scan 99 from the b17 download), 102L and 103R read on the
full-resolution NA scans (1,046 groups, `tokens/s*_r2n.txt`); about 150 codes looked up on the key scans
(`research/reading_audit/r2n_keylook.py`, `r2n_allblocks.py`), new rows in `key/dict/r2n.tsv`. 2 Jan 1687 aligned with its
interlinear decipherment of the time (30 codes agree; 10:703 rabat against the clerk's 'een'). Readings in
`readings/r2n/` (`_reading.md`, `_en.md`, log `r2n_log.md`). Read (v2_score explicit holes): 2 Jan 1687 0.78, 13 Mar 1687
54R 1.0 and 55R 1.0, July 1687 1.0, 11 Sept 1687 0.75, 18 Dec 1687 93R/94L 0.85, 1 Jan 1688 1.0, 11 Mar 1688 1.0 (Oropesa to
speak for Cogolludo, Melgar and Balbases; the Grand Master's Vienna plans and the war-council presidency; Holstein
desists). Decoded, not read: 67L, 73R, 80R, 94R after l. 5, 99L, 102L. fraction_read about 0.78 (estimated).

Status: read in part; **read with known key**. Two letters pass the strict sense screen without a known contemporary decipherment:
**24 April 1687, 230/235 = 97.9% conservatively**, and 8 April 1688,
313/323 = 96.9%, or 312/323 = 96.6% conservatively. The 19 December 1686 letter is a third
validation against contemporary plaintext on 32R. The volume is not a complete decipherment.
Decipherment by **Feyseel Nur (with Claude and Codex)**; 4–5 October 2026.

21 Oct 2026, PR #65 and #67 (WAINUT) merged: the folder key applied to passages in seven 1687 letters listed as not read
(1,389 groups, 39 uncertain; sections "Contribution by WAINUT" at the end). They are contributed readings and are not
counted in the figures above: 158 of their code values come from an unchecked machine read of the key, and the 4-gram
control is not in the repository. Adopted from them: the 2 Jan 1687 letter has interlinear decipherment
(`inv/orch_letters.tsv` corrected), and key rows 11:718 soetjens, 11:719 soetelaars (`key/dict/orch.tsv`).

## Documents and key

- Nationaal Archief **3.01.18, inv. 401**, 109 scans: Pieter Battier, Dutch envoy extraordinary
  in Madrid, to Grand Pensionary Gaspar Fagel, 1686–1688.
  https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/401
- Key: Nationaal Archief **1.10.29 (Fagel), inv. 1209**, 86 scans, headed
  “Voor den Heer Extraord. Envoye Battier”.
  https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/1209
  DECODE **R2794** holds this key but cites “inv. nr. 5345”, which is absent from the current
  1.10.29 inventory. The correct inventory number is **1209**. This is application of an
  identified key, not recovery of an unknown cipher.
- Contemporary decipherments: 5 December 1686, scan **28R** (cipher 30R, 31L);
  19 December 1686, **32R** (four numbered passages; cipher 31R, 32L);
  30 January 1687, **42R–43R** (cipher 41R, 42L, 44R); interlinear **101R**, 26 February 1688.
- The States General set, NA **1.01.02, inv. 12588.120–125**, is not digitised.
- Manuscript images: Nationaal Archief, **CC0**. The site lead is inv. 401, scan 108, right page.

No edition was found; the letters are not in DECODE.
K. M. M. de Leeuw, *Cryptology and statecraft in the Dutch Republic* (University of Amsterdam,
2000), discusses Fagel codebooks but never Battier. See `evidence/prior_art.md` for the citation.
The prior-art search covered De Leeuw (2000), DECODE, Tomokiyo, editions and the
Nationaal Archief digitised series. This is a bounded finding, not proof that no unpublished
reading exists.

The transcriptions were made by LLMs from the Nationaal Archief scans and checked against
the key images. Uncertain digits, marks and dictionary readings remain identified below.

## System

The letter table, **2–98**, has eight homophones per vowel and three per consonant
(`key/letters.py`, key scans 3–6); vowel-substitute letters are also recorded there.
A one-part alphabetical Dutch codebook repeats **99–999** in fifteen blocks, selected by
a mark above the number: none, tilde, backslash, caret, slash, e, l, r, bar, two dots,
first/second/third digit struck, c/, reversed c/. Block 13 begins at 100. The transcriptions
use `block:number`; bare 2–98 are letters. Names include Spanish councils and grandees
on key scan 59, with places on scans 78–82 (transcription series 16).

The key transcription contains **1,417 distinct dictionary codes**: the earlier count
of 1,393 plus 24 new codes in `key/dict/nw.tsv`. Its 27 rows retain scan/column references.
Three codes already occur in the repository: 15:165, 2:825 and 11:431; the preserved
24 April review identifies only the first two duplicates. Sorted TSV files retain the dictionary override order, including
`zz_corrections`. The 365 alphabetical reversals (96 touching focus tokens) are **not 365
proven misreads**: inflection, thematic lists and historical spelling can break strict order.

## Conservative results

| Letter | Cipher scans | Tokens | Key-attested | Strict sense | Generous ceiling | Verdict |
|---|---|---:|---:|---:|---:|---|
| 19 Dec 1686 | 31R, 32L | 186 | 186 | 186/186 = 100% | 100% | validation: four passages on 32R |
| 24 Apr 1687 | 58R, 59L | 235 | 234 complete mappings, including surplus e | **230/235 = 97.9%** | 99.6% legacy H+C+M | passes; no known contemporary decipherment |
| 4 Dec 1687 | 91R, 92L | 211 | 210 | 199/211 = 94.3% | 96.7% | below |
| 12 Feb 1688 | 99R, 100R | 271 | 268 | 250/271 = 92.3% | 96.7% | below |
| 8 Apr 1688 | 107R, 108L, 108R, 109L | 323 | 322 | 313/323 = 96.9% | 99.7% | passes |

These are the Codex review numbers, not the more generous original H+C totals. The strict
screen excludes unkeyed emendations and unresolved meanings in `codex_review/semantic_adjustments.tsv`;
semantic screening is judgment, not statistical confidence. Literal key attestation alone
does not establish meaningful text. The earlier estimate was roughly **55% of the cipher in inv. 401** read;
the 235-token addition has no revised volume-wide denominator. `inv/orch_letters.tsv` lists the unread
letters. Its legacy READ label means transcribed/decoded/graded, not a pass of the strict bar.

## Third validation: 19 December 1686

Scan 32R carries a contemporary numbered list 1–4 in a clerk's hand for the four
cipher passages on 31R and 32L. The key reading reproduces this decipherment across
186 tokens, apart from spelling and “niet gedaan” versus “niet afgedaen”. This is the
third validation letter, not a new reading, and strengthens the identification of
inv. 1209 as Battier's key. The list confirms **15:325 = wat** (32L, token 65) and
**12:409 = syn** (32L, token 93); the latter's legacy C grade records a contextual
mark choice, now confirmed by contemporary plaintext.

On 31R, line L05, tokens 57–59 are `8:721 = niet`, `4:294 = gedaan`, `4:696 = en`;
32L continues with “blyft alles traineren”. No separate `af` prefix token occurs in
the recorded sequence. The clerk's “afgedaen” expands the recorded key reading;
a token omitted from the cipher transcription cannot be excluded without checking
that cipher line against the image.

The clerk's list reads:

1. “van de Graef van Mansfelt, maer t' sedert het dese laetste eens gemanqueert heeft, is syn persoon weynigh geestimeert, en syn credit hier aen het hof seer geringh, en daerom oock voor hem weynigh apparentie.”
2. “maer daerom werden de publicque affaires niet afgedaen en blyft alles traineren.”
3. “maer soo men die helft vinden kost, soude haestelyck een ander Gouverneur de reys naer Vlaenderen aennemen.”
4. “soo veel impressie, dat men dan soo voorts op geen defensie gedenckt, en wat nogh meer is, men magh se oock soecken te desabuseren soo veel men kan, soo syn se soo seer gepersuadeert, dat Engelandt en den Staet de Spaensche Nederlanden par raison d'interessen sullen moeten defenderen, dat se weynigh op ander middel gedencken.”

The letter has 186 cipher tokens, all key-attested and accepted by the strict screen.
The ciphered stretches concern candidates for the Netherlands governorship and Madrid's
failure to organise defence. In the original Dutch, with editorial spacing:

> van de Graaf van Mansfeld, maar sedert het dese laatste eens gemanqueert heeft, is syn persoon
> weynigh geaestimeert, en syn credit hier aan 't hof seer geringh, en daarom ook voor hem weynigh apparentie.

> maar daarom werden de publicqe affairen niet gedaan en blyft alles traineren.

> maar soo men die helft vinden kost, soude haastelyk een ander gouverneur de reys na Vlaanderen aannemen.

> soo veel impressie, dat men dan soo voorts op geen defensie gedenckt; en wat noch meer is, men mach se
> ook soecken te desabuseren soo veel men kan, soo syn se soo seer gepersuadeert dat Engelandt en de Staat
> de Spaansche Nederlanden par raison d'interessen sullen moeten defenderen, dat se weynigh op andere middel gedenken.

The surrounding clear text explains the money request and negotiations; it is marked in
`readings/s031R_text.txt` and `s032L_text.txt`. Their provisional date headings predate the
inventory's identification of 19 December and are preserved as source history.

## Reading: 24 April 1687

Scans **58R–59L** contain **235 cipher tokens** (73 and 162). The conservative Codex
sense screen accepts **230/235 = 97.9%**. Legacy grades are H 212, C 21, M 1, I 1;
H+C is 233/235 = 99.1%, not a measure of coherent Dutch sense. Complete key-file
mappings cover 234 tokens, including the surplus e; 5:623 has only the partial `gra[..]`.
No token is 81. The review is preserved verbatim in `codex_review/review_1687-04-24.md`.

The decipherment-sheet check covered **58L–60R** before the reading: no interlinear
plaintext, numbered list or marginal passage numbers were found. 58L is the endorsement
of the 10 April letter; 59R is blank; 60L endorses the 24 April letter; 60R begins the
next letter. The small recurring 3 is on a following leaf's tab, not a passage number.
This is the second passing letter without a known contemporary decipherment; the local
check does not establish absence of a prior publication.

Gastanaga may be removed before the end of his three years or employed in Peru or
Catalonia. The exact condition of his departure remains uncertain: `gehelyk` and
`sedert dat` do not yield a secure conditional construction. The Emperor's ambassador
seeks the advantages enjoyed by his predecessor and

> beweeght hemel en aarde om weder in de Koninginne goede gra[tie] te komen

He works through a nun, the confessor and ministers. Renewed friendship with the Countess
of Soissons is intended to obtain her good offices; the plural `sy` leaves the exact
participants uncertain. Battier concludes that it appears

> Hare Majt. het quaat van den Amb. van den Keyser haar aangedaan noyt niet vergeten sal.

The final `sal` is encoded on 59L, tokens 160–162. The ambassador's identification as
Mansfeld is not established by these cipher tokens. The review qualifies the fluent
English summaries in `readings/s058R_text.txt` and `s059L_text.txt`.

The five strict exclusions are 58R:15, a surplus bare **8 = e** (possible encipherment
slip); 59L:30, **5:623 = gra[tie]**, partly covered by a pasted slip in key scan 29R,
column 1; 58R:9, **gehelyk** (possibly final -e in the key); 58R:21, **sedert dat**;
and 59L:52, **soo als hy**. The latter's relation to `by de Koningh` remains unresolved.
The screen is an editorial assessment, not a confidence probability.

## Reading: 8 April 1688

This is one of two focus letters that pass the strict sense screen without a known contemporary
decipherment: **313/323 = 96.9%**, conservatively **312/323 = 96.6%**. Visual inspection of
scans 107–109 found no decipherment list. Inv. 401 has 109 scans; the letter ends on scan 109
with the signature “Mad. den 8 April 1688”.

The reviewed reconstruction is `codex_review/april_reading.md`; it supersedes the fluent
interpretations in `readings/s108-109_text.txt`. Representative cipher clauses:

> Den Grand Maestre aan syn agent geordonneert de oude Koninginne te verseekeren …

> Ondertusschen soo formeert sich een gesworen partye tegen den selven: Connestable van Castille,
> Os[t]una en Mon[i→t]ere [Monterey?] brouwen wat met malkander.

> de Nederlandse toestemminge, gelyk in tyt van Grana is geschiedt, door syn handen niet veel sullen passeren.

The instruction to the agent and faction formation are solid within the transcription.
The Holsteyn project and Monterey's presidency ambitions are plausible; Osuna, pronoun referents
and the administrative meaning of *toestemminge* are speculative. Read **“Grana is geschiedt”**,
not “Grana's geschiedt”. Troop and money figures in the project's description are clear text.
The unfilled viceroyalty on 108L is **12:6?0**; it is not identified here.

## Other letters and validation

The 4 December 1687 and 12 February 1688 readings are retained with their token tables,
but neither passes the strict sense threshold. The reading corpus, including
29 January and the partial 26 February 1688 check, is supporting material, not a set of new
complete-reading claims. Difficult tokens in the five focus letters remain traceable through the TSV notes,
the earlier semantic adjustments and `codex_review/review_1687-04-24.md`.

The 24 April 1687 review independently re-decodes 235 positions: 233 value fields match
exactly, with two typography-only differences. This reproduces curated token choices,
not a blind validation of their marks or digits. All 27 additional key rows were reviewed
against image crops; the covered gratie ending and possible final -e in gehelyk remain open.
The contemporary-plaintext validation totals below are unchanged.

The first two validation letters contain **369** tokens (5 December 1686) and **781** (30 January 1687).
Agreement with contemporary decipherments where comparable is **1113/1132 = 98.3%**;
key-alone agreement is **94.7%**. Eighteen positions are not comparable. The source filename
`validation_1687-01-16.txt` is a legacy misdate: the inventory and validation summary identify
the letter as **30 January**. Comparison used the existing decipherments, so this is not a blind
holdout claim. The third validation, 19 December 1686, adds **four passages, 186 tokens**,
compared with the numbered decipherment on **32R**, with spelling differences and the
“gedaan”/“afgedaen” distinction above. The earlier percentages describe the first two letters
only; they are not an aggregate score for all three. In the shuffle control run with `scripts/control.py`, **72%** of spelled runs segment into Dutch,
versus mean **1.2%**, maximum **4.1%**, for **300** permuted tables. Segmentation tests structure,
not correctness of names or syntax; the fixed lexicon and names list influence this result.

## Grades and review limits

Repository grades: H = primary-key support, C = contemporary-plaintext support, M = uncertain,
I = inferred. The reading TSVs instead use H = secure key/sense, C = contextual digit/mark
choice, M = conjectural, I = unread/no sense. **Those legacy grades are preserved, not silently
converted into repository grades or used as the headline result.** Literal decoding and the
strict review screen take precedence. Context-only repairs are inferred (I), uncertain glyphs
are M; no aggregate repository-grade counts are claimed.

The alleged **81=e habit** comprises 17 occurrences: 14 contextual e, 3 retained i. The key
has **81=i**. None of the three validation letters contains 81, so they do **not** confirm this habit.
`getwist` is the key reading where the contextual interpretation proposes **Turck(en)**; that
inference remains open. The Codex review is independent **software re-decoding, not paleography**.
Shifted annotations, dictionary variants and mark choices still require image checks.

Closed items (moved out of Remaining gaps):
- Volume letters without cipher (10 Apr, 11/22 May, 31 Jul, 28 Aug enclosures, 9 Oct / 23 Oct / 6 Nov 1687, 25 Mar 1688): closed 23 Oct 2026 (r2j), contact-sheeted, clear text only

## Remaining gaps
- 24 April 1687: surplus 8=e; partly covered 5:623 gra[tie]; gehelyk, sedert dat and soo als hy; Gastanaga's exact departure condition - blocker: no-key-material; the 230/235 sense screen excludes these five positions; see codex_review/review_1687-04-24.md
- Separate decipherment sheets near 4 December 1687 and 12 February 1688 - blocker: no-key-material; checked 22 Oct 2026 (b17): scans 90-94 and 98-102 hold none
- Focus-letter unresolved groups and sense: 12:6?0; getwist versus inferred Turck(en) (settled 22 Oct 2026: 12:908 Turcken); Novelli/Hofmeester, gesoubconneert gouverneren and Sex.; name repairs, 81 and other emendations in semantic_adjustments.tsv - blocker: no-key-material; key lookup alone does not settle the meaning or mark choices
- Located passages, r2n (23 Oct 2026): read 2 Jan 1687 35R/36L, 13 Mar 1687 54R and 55R, July 1687 69L, 11 Sept 1687 78R, 18 Dec 1687 93R/94L, 1 Jan 1688 95R, 11 Mar 1688 103R; groups still open in them (35R 361 448 and the end of the 35R run, 703 against the clerk's 'een'; 54R 886; 55R 2:888 blank key row; 78R the first run 260 117 779 60; 93R/94L 888 178 883 212 256; 95R 11:861) - blocker: no-key-material; each looked up on the key scans with the mark as read (and in other blocks where the mark was unclear), no row gives sense in place (readings/r2n/r2n_log.md)
- June 1687 67L (the letter run t-e-s-m-o-g-n-e-r-e-n) and Aug 1687 73R (backslash mark on 90, stray g): decoded, not read, one sentence each - blocker: no-key-material; every group decoded and looked up, the remaining run and mark have no key value that fits
- 25 Sept 1687 80R (894, 432, 422, 379, 756), 18 Dec 1687 94R after l. 5 (406, 706, 238, 116, 653, 724, 312, 830) and Jan 1688 99L third run (886, 688, 878, 214, 154, 980): decoded, not read - blocker: no-key-material; looked up on the key scans with the marks as read, no row gives sense; 80R 9x9 is smudged (illegible)
- 26 Feb 1688 102L (420, 335, 499, 114, 603, 800, 505): decoded, not read - blocker: illegible; the key rows give no sense and the interlinear decipherment of the time that would settle them is too faint on the NA scan to read
- States General parallel set NA 1.01.02 inv. 12588.120–125 - blocker: needs-physical-access; not digitised
- 4 Dec 1687 (92L) and 12 Feb 1688 (100R) cipher blocks: closed 22-23 Oct 2026 (b17), both letters read; groups still without sense (92L 889 and a-u-t-o-r-i-s-g; 91R 11:466, 14:6ø, ø94; 99R 431 374 137 512, 604; 100L 867 826 296 765; 100R the struck groups after Madrid and after gesoubconneert, 59ø ø39) - blocker: no-key-material; each looked up on the key scans, no sense in place (readings/*_corrections.tsv)

## Escalation
- [x] siblings: all 109 scans inventoried; unread letters listed in inv/orch_letters.tsv are not yet transcribed; workable with the same key
- [x] siblings (23 Oct 2026, r2j): every letter listed not read re-checked on full-size scans: seven have no cipher (closed), thirteen passages located with their size; 69L piloted with key lookups; the rest not transcribed
- [x] clear-pages: 28R, 32R and 42R–43R compared to three validation letters; 58L–60R checked with no decipherment found for 24 April 1687; scans 107–109 visually checked with no decipherment list; 101R has an interlinear check
- [x] known-keys: Battier's named inv. 1209 key applied; DECODE R2794 shelfmark discrepancy recorded
- [x] print: De Leeuw (2000), DECODE, Tomokiyo, editions and NA digitised series searched; no Battier edition found; see evidence/prior_art.md
- [x] key-rebuild: dictionary transcription and correction overrides preserved; Codex identifies remaining variants and alphabetical reversals
- [x] retry (23 Oct 2026, r2n): the located passages (thirteen by letter, fourteen with 54R and 55R separate) read group by group on the NA scans, every code looked up on the key scans, 35R/36L aligned with its interlinear; eight read, six decoded, not read with the blocker named (readings/r2n/r2n_log.md)
- [x] retry: 22-23 Oct 2026 (b17) 92L, 91R, 99R, 100R re-read on the NA scans group by group and every doubtful group checked on the key scans; two untranscribed cipher runs added; 4 Dec 1687 and 12 Feb 1688 read (readings/1687-12-04_1688-02-12_reread_log.md). Earlier: five focus letters re-decoded and screened for sense; unresolved readings recorded in semantic_adjustments.tsv and review_1687-04-24.md; unread letters not yet transcribed; workable with the same key

## Files and reproduction

- `key/letters.py`, `key/dict/*.tsv`, `key/colindex*.txt`: transcribed key and column locators.
- `tokens/`: line-labelled cipher tokens; `readings/`: legacy graded tables and texts.
- `codex_review/`: review.md, audit_notes.md, april_reading.md, metrics.tsv and semantic_adjustments.tsv copied verbatim; review_1687-04-24.md preserves the second passing letter's review verbatim.
- `scripts/decode.py`: key-only decoding; run `python3 targets/battier1686/scripts/decode.py targets/battier1686/tokens/s031R.txt`.
  Do not use `--write` on preserved readings: it overwrites grades.
- `scripts/measure.py`: legacy grade totals, **not** the conservative review's semantic screen.
- `scripts/control.py`: permutation control used for the reported results; requires the original
  OpenTaal word list via `BATTIER_OPENTAAL=/path/to/opentaal.txt`. The lexicon is not bundled.
- `scripts/build_reveal.py`: decodes the continuous 59-token passage on 31R and compares it to the reading table.
- `scripts/build_site.py`: scoped use of the repository builder for this page and shared indexes;
  does not rewrite other target pages or their replay files.

The thesis PDF and full manuscript scans are not included.
No DECODE letter update is applicable: the letters have no DECODE records; the R2794 key
shelfmark correction is documented here without making an external edit.

## Contribution by WAINUT (21 Oct 2026)

WAINUT (a Dutch AI company, https://github.com/WAINUTAI) applied this folder's key to one passage of a letter that
`inv/orch_letters.tsv` lists without a decipherment, and checked one row of the key transcription. The key
transcription, the column index, the token grammar and `scripts/decode.py` are this folder's; nothing above has been
changed. Number groups were transcribed with Google Gemini (gemini-4-argon) and the analysis was done with AI
language-model agents. The three cipher lines below and every key row used for them were then checked visually
against the full-resolution NA scans, group by group, in two separate passes. Files are in `wainut/`;
`wainut/check_67R.py` reproduces every number in this section (standard library, paths relative to the folder).

**1. Scan 67R, cipher lines 1-3 (letter of June 1687).** `inv/orch_letters.tsv` lists the letter 1687-06/07, scans
66R-68L, cipher on 67L and 67R, no contemporary decipherment, not transcribed. It is signed on 68L "Madrid den 19
[or 10] Juny 1687", so it is a June letter. Scan:
https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/401/file/NL-HaNA_3.01.18_401_0067

`wainut/tokens_s067R_L01-03.txt` gives the 45 tokens of the first cipher passage in this folder's grammar: 21 cipher
letters and 24 codes. Battier writes 8 as a struck o (2ø = 28, ø56 = 856, øø5 = 885). Of the codes, 16 are in
`key/dict`. The other 8 were looked up in the key through `key/colindex.txt` and checked on the key scans; they are in
`wainut/key_rows.tsv` in the `key/dict` layout: 11:695 soo seer (s59L1), 6:490 jnkomen (s34R1), 5:273 geduyrigh
(s27R3), 11:721 soigneuslyke (s59L1), 3:126 borse (s17R3), 12:784 total (s64L1), 11:172 ruïne (s56R1) and the open
885 (below). Key scans: https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/1209/file/NL-HaNA_1.10.29_1209_0059
(change the last four digits for scans 12, 17, 27, 34, 55, 56 and 64).

The key decode, with the clear text around it:

> [Daer is geen apparentie, dat de Hr. Gastañaga geremoveert worden sal, eer syn tyt uyt is, soo hy geen considerabele
> faute begaet, offe een ander groot accident daer tusschen komt, niet tegenstaende] soo seer veel klaghten te hem
> inkomen, als of 'r anders niet daede, als geduyrighe despences en (885) noch soigneuslyke borse te maken tot totale
> ruïne van de Spaansche Nederlanden; [men kan hem sonder waer anders te placeren niet wel wechjagen]

That is: so many complaints come in against Gastañaga, as if he did nothing but run up expenses and carefully fill his
purse, to the total ruin of the Spanish Netherlands; but he cannot be removed without being placed elsewhere.
`wainut/s067R_L01-03.tsv` grades the 45 tokens H 41, M 3, I 1 (repository grades). M: 13:171 veel (the strike on the
last digit is faint), 6:490 jnkomen (the mark looks like an e; 4:490 is Wismar) and 12:784 total (no strike seen beyond
the struck-o 8; block 12 from "tot total-e ruïne"). I: 885 carries a single dot, which is none of the fifteen marks;
1:885 argh and 10:885 regulier both give poor sense, so it is left open. "te hem" may stand for "tegen hem".

No interlinear, marginal or separate decipherment was found on 66R, 67R or 68L, and there is no `s067*` file in
`tokens/` or `readings/`. The States General set (1.01.02 inv. 12588.120-125) was not checked.

**Control.** With the key rotated by one row (letter n read as the letter of n+1, code b:n as b:n+1), the same tokens
give "soo verre veele klaghtigh w te bedde qit jngekomen alsmen offe l andermaal niet alleen fuu / za alsmen
geduyrigheyt ufinuowoan ende arghlistigh nochtans Soissons / borse der Cooplieden te bedde gemaakt tot hier totaliter i
ruïneux van achteren dese de Geestelyckheyt". The letter runs (hem, daede, edespences) lose all sense. For the codes the
control is weak, because in an alphabetical one-part code the next row is often a related word (total/totaliter,
ruïne/ruïneux).

**2. Key row 11:719.** `key/dict/orch.tsv` has `11:719 soetjens (key s59L1)`. On key scan 59L, column 1, the rows run
716 Soetheyt, 717 Soetelyke, 718 Soetjens, 719 Soetelaars, 720 Soigneus, 721 Soigneuslyke. The last digit of 718 is the
key's looped 8, which can be taken for a 9; 719 has a plain 9. On this evidence the entries would be 11:718 soetjens and
11:719 soetelaars. Neither code occurs in `tokens/`, so no reading changes. Scan:
https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/1209/file/NL-HaNA_1.10.29_1209_0059

**3. Single machine pass (method control).** A single Gemini pass on pages this folder already has gives the same
number for 64 of 73 tokens on 58R (88%) and 154 of 162 on 59L (95%), but the same decoded value for only 52 (71%) and
126 (78%), because marks are missed or confused (e read as c, struck digits missed). On 67R lines 1-3 it agrees with
the checked transcription on 39 of 45 numbers (87%) and 34 of 45 values (76%). This is why every token of the
reading above was checked on the scan, and why no machine-only transcription is offered as a reading. The passes are
in `wainut/machine_pass/` (58R, 59L and 67R lines 1-3).

Files: `wainut/tokens_s067R_L01-03.txt`, `s067R_L01-03.tsv`, `s067R_L01-03_text.txt` (reading with English gist),
`key_rows.tsv`, `check_67R.py` (run `python3 targets/battier1686/wainut/check_67R.py`), `machine_pass/` (method
control only).

## Further contribution by WAINUT (21 Oct 2026)

This builds on #65 (the "Contribution by WAINUT" section above). It applies the folder's key (NA 1.10.29 inv. 1209) to the
1687 letters that `inv/orch_letters.tsv` lists as "not read", and adds one correction to that inventory. Files are in
`wainut/r24_1687/`.

**Readings.** Every group below was checked by eye on the NA scans of 3.01.18 inv. 401 (scan numbers as in this folder).
Codes are decoded with `key/letters.py` and `key/dict/*.tsv` first; codes not in `key/dict` come from
`wainut/r24_1687/key_rows_machine.tsv` (a machine read of the code book, marked `*` in the script output).

| letter | cipher pages | groups | uncertain | state |
|---|---|---|---|---|
| 16 Jan 1687 | 38L, 38R, 39L | 207 | 11 | nearly complete |
| 13 Feb 1687 | 45R, 46L, 46R | 272 | 11 | nearly complete |
| 27 Feb 1687 | 47R-50L | 575 | 8 | nearly complete |
| 13 Mar 1687 | 55L only (54R, 55R not read) | 66 | 1 | partial |
| 10 Jun 1687 | 67R (lines 1-3 as in #65; 67L not read) | 152 | 6 | partial |
| 20 Nov 1687 | 89R | 60 | 1 | complete |
| 18 Dec 1687 | 94R lines 1-5 (rest of 93R-95L not read) | 57 | 1 | partial |
| | | **1,389** | **39** | |

The running text with Battier's clear text around the cipher is in `wainut/r24_1687/readings_1687.txt`. In short:
16 Jan: Montalto was offered the government of the Spanish Netherlands by those who lead the King, and declined only for
lack of money; Cramprich (named in the clear text) presses to keep Castañaga. 13 Feb: Castañaga is told he will not be removed
before his three years are out; Oropeza runs everything without the title of first minister; Lira acts as if he cared little for his post.
27 Feb: Oropeza stays vague on remittances to the Netherlands; Spain will not turn the truce into a peace that cedes
what France took after Nijmegen, unless the Emperor settles; the Pope could persuade them, as Oropeza's confessor is a
Jesuit. 13 Mar: the French ambassador asks Spain at least to leave the Augsburg league. 10 Jun: the Countess of Soissons
recommends her son, serving in Hungary, for the government of the Spanish Netherlands. 20 Nov: some have tried to stop the Admirant of
Castille, to please the President of Castille. 18 Dec: Battier has the envoy of Syne Hoogheyt (key 8:439, between
437 "Prince v. Orange" and 438 "de Princesse") press Lira on behalf of the French refugees.

Open points: in the 16 Jan letter, 12:118 is "Stówinge" on key scan 60R (a noun), so the person who "solicits for himself"
is unresolved; the tail of 39L has about five groups without clear sense. On 67R line 5, 103 carries the mark read as e
elsewhere, yet neither 2:103 nor 6:103 gives sense; it is left open.

**Correction to `inv/orch_letters.tsv`.** The letter of 2 Jan 1687 (35R, 36L) is listed with contemporary decipherment
"no". The scans show heavy interlinear decipherment over the cipher on 35R and 36L. A spot check of the first cipher line,
937\ 7.15 463 431 374 703, gives "dat is te seggen in [10:703 rabat]" against the interlinear "dat is te seggen in een".
This letter is therefore not new, and no reading of it is offered here.

**Method and control.** The number groups were transcribed by three independent machine vision passes and then corrected
by eye on full-resolution crops; every group in the table was looked at on the scan. On the eye-checked tokens, each of the
seven letters scores higher under the true key than under any of 20 row-shifted keys and 200 shuffled keys (Dutch letter
4-gram model; this control needs an external model and is not included). A second check of about 265 groups on freshly
downloaded scans found no digit misreading. Machine-only passages of these and later letters (69L, 73R, 78R, 80R, 95R, 99L,
103R) are not offered as readings. The States General copies (1.01.02 inv. 12588.120-125) were not checked, and a short web
search found no edition of these dispatches.

Files: `wainut/r24_1687/tokens/s*.txt` (checked tokens with per-group notes), `readings_1687.txt`,
`key_rows_machine.tsv`, `check_1687.py` (run `python3 targets/battier1686/wainut/r24_1687/check_1687.py`; it prints the
decoded lines, the counts in the table and the inventory line for 2 Jan 1687).
