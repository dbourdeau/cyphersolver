# R1854 — "Mantova enciphered letters": four cipher letters to Gianfrancesco Gonzaga, 1428–1430

Status: read in part (22 Sept 2026); written up at docs/r1854.html. Four of five images read (P2–P5, 3 letters + a verso); P1 (Pandolfo Malatesta,
22 April 1428) not read. Key: recovered for P2, P3 (from the contemporary gloss), P4/P5; none for P1.
Catalogue #152 "Unknown sender to unknown recipient" (Mantova State Archive).

DECODE R1854 "Mantova enciphered letters", 5 images, status "Partially decrypted", graphic signs, no metadata (no
sender, date, language, shelfmark). Key record R1853 "Mantova keys" (14 images) = the Gonzaga chancery cipher
register of c. 1401–1420 (folio 1: "Zifra cum Malatesta dni Pandulfi", "Zifra nova cum fratribus de Malatestis",
"Zifra ultima cum Karolo de Malatestis"; later folios keys of 1406–1419). Images are not public domain: kept
git-ignored in `decode/`; no page image is published.

## What the five images are

Four letters (and one verso), all to Gianfrancesco Gonzaga, lord of Mantua; each carries an archivist's date and
place at the top and a stamped number (23, 24, 26 …). Tokens measured with `docs/_check_profile.py --measure`.

| image | date / place | sender | language | cipher | signs | state |
|---|---|---|---|---|---|---|
| P1 (I8411) | Rome, 22 Apr 1428 | Pandolfo Malatesta, archbishop of Patras (signed) | Latin clear + 3 cipher runs | letter-like signs, unknown system | 262 (`p1v2.txt`) | not read |
| P2 (I8412) | Rome, 9 Aug 1428 | unnamed Gonzaga agent (lozenge mark) | Latin | homophonic + nulls + 2 codes | 1,802 (`p2v3.txt`) | read, 0.966 |
| P3 (I8413) | Forlì, 6 Nov 1428 | "Ricc(ardus?) de Mutiliana" | Italian, clear + runs | homophonic + nulls + 3 name codes, interlinear decipherment | 905 (`p3_signs.txt`) | read (at the time; re-deciphered), 0.972 |
| P4 (I8414) | Rome, 13 Feb 1430 | Francesco de' Cattanei | Latin | homophonic + "et"/"con"/"-rum" signs | 1,566 (`p4v2.txt`) | read, 0.967 |
| P5 (I8415) | Rome, 21 Feb 1430 (verso, image upside down) | Francesco de' Cattanei | Latin | same as P4 | 202 (`p5v2.txt`) | read, 1.0 |

Readings: `reading_p2.md`, `reading_p3.md`, `reading_p4.md` (P4 + P5). Total 4,737 cipher signs; read as sense
about 4,337 (P2 1,740 + P3 880 + P4 1,515 + P5 202) = 0.916; P1's 262 signs all unread.

## Method

- P2: ciphertext-only. `solve.py` (homophonic annealer on the shared `lang/` Latin model, with frequency prior,
  optional costed nulls) after fixing Δ = q and `17` = u from contact (Δ precedes 17 in 21 of 29 cases). Then per-sign
  and per-occurrence rescoring (`refine.py`, `occ.py`) and glyph splits confirmed in the image: bold ∇ = s, thin dotted
  ∇̇ = null; tailed circle = p, plain circle = h; ᵹ = x vs bold 8 = f. Syllable signs 3 = con, S = et, 8t = rum.
  Nulls K, W, #, Y, 19, wq, M, O, F, 20, D, dotted ∇. Codes ARW (= cardinalis, 2×) and ARO (1×, unread).
- P4/P5: ciphertext-only anneal gave Latin at once ("sollicitabo bullam", "galeotam"); a subagent second pass then
  checked every sign against the image: 209 edits, look-alikes split (slanted b = i vs rounded = o; η vs 9; ⊢-o = q;
  o†o = x; Λ-type d), `key4_v2.txt`.
- P3: key taken from the contemporary interlinear gloss (30 sign values, each attested 2–56 times), rare signs from
  context; signs transcribed by a subagent (`p3_signs.txt`), decoded to `p3_decoded.txt`. Name codes glossed.
- P1: see Remaining gaps.

## Content in brief

- P2 (Rome, 9 Aug 1428): marriage negotiations reported through ser Vittorio and Giovanni de Orlandis: a countess
  (comitissa) agrees to the match of her daughter; the subjects object that the lord of Mantua is too far away and
  "Carolus est nimis iuvenis ad talia" (Carlo Gonzaga, b. 1417); Antonio Colonna and the cousins of domina Palma.
- P3 (Forlì, 6 Nov 1428): the governor of Forlì secretly favours the marquess's sons; the pope is said to be with
  them; an enterprise with the lord Malatesta and the count of Urbino would make the lord of Mantua a great lord;
  Guidantonio of Urbino in secret contact with Giovanni de Ramberto.
- P4 (Rome, 13 Feb 1430): Cattanei's news: Carlo (Malatesta?) on a marriage alliance with King Louis (of Anjou); a
  galley of Giovanni de Orlandis took a Catalan ship, lost at Gaeta (5,000 ducats); Castile presses Aragon; an envoy
  of the lords of Rimini left empty-handed; the archbishop of Patras offered the temporal lordship (of Patras) to the
  Venetians with the pope's licence, and the cardinals answered it was better lost than given to Venice; Niccolò da
  Tolentino's chancellor; the abbot's excommunication lifted; six Bolognese citizens expected.
- P5 (Rome, 21 Feb 1430): the Rimini envoys Astorgio and Bartolomeo appeared before the commissaries with a mandate
  and authenticated copies of bulls; "credo parum iuvabit"; in clear "denarios non habeo pro expensis".

## Remaining gaps
- P1 (Pandolfo Malatesta, Rome 22 Apr 1428), 262 signs in 3 runs - blocker: no-key-material; not a monoalphabetic or homophonic substitution in Latin or Italian (solver controls pass on synthetic text with 12% noise); none of the register's Malatesta keys fits; the likely key material is Pandolfo's own ciphered letter of 1 Mar 1438 with its contemporary translation (ASMn AG b. 1081 c. 159-160 and b. 840 c. 95, Falcioni 2015), whose ciphertext is not online and not printed
- P2 code ARO (1×, "in filium [ARO]") and ~60 signs in doubtful spans - blocker: too-short; single occurrence, no sibling letter in this cipher
- P3 signs Z (2×) and fk (1×) - blocker: too-short; no gloss over them, two and one occurrences
- P4 L04 "leonebi … re[∂]bs", L14 "a-mhi", L20 "debert onorio" - blocker: illegible; signs re-read at 10-13x, 786-px scan, values not fixable from single occurrences

## Escalation
- [x] siblings: R1853 (register, 14 images) read for keys; all other Mantova records on DECODE opened (R7858-R7888 = Archivio Gonzaga E.I.2 b. 423, 16th-17th c. keys; R7888-R7890 = 1395 Armanini); none for 1428-30
- [x] clear-pages: P3's interlinear gloss is the contemporary decipherment (used as key source); P5 is the verso of Cattanei's second letter, not a clear copy
- [x] known-keys: register keys "cum Malatesta dni Pandulfi", "nova cum fratribus de Malatestis", "ultima / prima cum Karolo de Malatestis", "Ziffra nova" 1417 tried on P1: values do not fit (seeded anneal -4.2/char)
- [x] print: web search (Pandolfo Malatesta, Gonzaga, cifra, 1428); Treccani DBI; Falcioni 2015 (Pandolfo and the council of Ferrara) found: prints the 1438 plaintext only
- [x] key-rebuild: P2 and P4 keys rebuilt ciphertext-only and extended by per-sign and per-occurrence rescoring; P3 key completed from context; P1 annealed under 12 hypotheses (Latin, Italian, modern Italian, costed nulls, vowel classes, separators as spaces, word/line/global reversal, split and merged digraphs)
- [x] retry (2): P1 tested for digraphic (pair IC 0.005), periodic/polyalphabetic (flat column IC, periods 2-8) and transposed text (vowel alternation 0.713 > 200 shuffles: linear substituted text); annealed in Spanish, Catalan, French, German, Portuguese and order-3 Latin/Italian with 150 restarts; syllable-aware anneal (signs as letters, 27 syllables/word signs or nulls, solve_syl.py): no reading
- [x] retry: P1 re-transcribed sign by sign by a second pass (`p1v2.txt`, 262 signs, 3 runs) and re-solved: no reading; P4 open spots re-read at 10-13x
