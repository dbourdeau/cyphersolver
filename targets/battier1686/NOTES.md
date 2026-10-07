# Pieter Battier to Gaspar Fagel, Madrid, 1686–1688

Status: read in part; **read with known key**. Two letters pass the strict sense screen without a known contemporary decipherment:
**24 April 1687, 230/235 = 97.9% conservatively**, and 8 April 1688,
313/323 = 96.9%, or 312/323 = 96.6% conservatively. The 19 December 1686 letter is a third
validation against contemporary plaintext on 32R. The volume is not a complete decipherment.
Decipherment by **Feyseel Nur (with Claude and Codex)**; 4–5 October 2026.

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

## Remaining gaps
- 24 April 1687: surplus 8=e; partly covered 5:623 gra[tie]; gehelyk, sedert dat and soo als hy; Gastanaga's exact departure condition - blocker: open-codes; the 230/235 sense screen excludes these five positions; see codex_review/review_1687-04-24.md
- Separate decipherment sheets near 4 December 1687 and 12 February 1688 have not been checked - blocker: open-codes; comparison with nearby plaintext remains unexamined
- Focus-letter unresolved groups and sense: 12:6?0; getwist versus inferred Turck(en); Novelli/Hofmeester, gesoubconneert gouverneren and Sex.; name repairs, 81 and other emendations in semantic_adjustments.tsv - blocker: open-codes; key lookup alone does not settle the meaning or mark choices
- Unread volume letters listed individually in inv/orch_letters.tsv, including 102L and the untranscribed cipher on 95R - blocker: open-codes; not yet transcribed; workable with the same key
- States General parallel set NA 1.01.02 inv. 12588.120–125 - blocker: needs-physical-access; not digitised

## Escalation
- [x] siblings: all 109 scans inventoried; unread letters listed in inv/orch_letters.tsv are not yet transcribed; workable with the same key
- [x] clear-pages: 28R, 32R and 42R–43R compared to three validation letters; 58L–60R checked with no decipherment found for 24 April 1687; scans 107–109 visually checked with no decipherment list; 101R has an interlinear check
- [x] known-keys: Battier's named inv. 1209 key applied; DECODE R2794 shelfmark discrepancy recorded
- [x] print: De Leeuw (2000), DECODE, Tomokiyo, editions and NA digitised series searched; no Battier edition found; see evidence/prior_art.md
- [x] key-rebuild: dictionary transcription and correction overrides preserved; Codex identifies remaining variants and alphabetical reversals
- [x] retry: five focus letters re-decoded and screened for sense; unresolved readings recorded in semantic_adjustments.tsv and review_1687-04-24.md; unread letters not yet transcribed; workable with the same key

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
