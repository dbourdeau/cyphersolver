# François van Aerssen to Johan van Oldenbarnevelt, Paris, 25 May 1601

Status: read in part as a two-letter record; key recovered based on adjacent plaintext.
25 May meets the read bar: 59/61 (96.7%) cipher tokens have values attested in contemporary decipherments.
The sibling of 2 June has 9/11 (81.8%), below the bar. Combined: 68/72 (94.4%), excluding contextual guesses.
The key remains partial. Decipherment by **Feyseel Nur (with Claude and Codex)**,
4 October 2026.

## Sources and scope

- Nationaal Archief, **3.01.14 (Oldenbarnevelt), inv. 2019, scan 57**, left page, top: Aerssen, Dutch agent
  in Paris, to Oldenbarnevelt, **25 May 1601**. Two cipher runs (36 + 25 tokens) inside clear French.
  No contemporary decipherment is reported. This edition covers the cipher and its
  clear context, not the entire letter.
- Same inventory, **scans 50–51**, 11 May, and **62–63**, 28 May: interlinear decipherments used to rebuild
  the key. These are training witnesses, not newly deciphered targets.
- Same inventory, **scans 42–43**, 30 April: tokens transcribed before the separate **list A, scan 46,
  right page**, entries 1–19, was opened. List A is now also attestation.
- Same inventory, **scan 66**, right page, 2 June: 11 cipher tokens, no contemporary decipherment reported.
- Archive: https://www.nationaalarchief.nl/onderzoeken/archief/3.01.14/invnr/2019
  Images: Nationaal Archief, CC0; crops of scans 57, 46 and 43, each credited by scan.

The transcriptions were made by LLMs from the Nationaal Archief scans and checked against
the images used to reconstruct the key: the interlinear glosses and list A. Both Codex reviews
are preserved verbatim.
The initial review precedes the glyph corrections; the recount accepts those corrections.
Exact original model versions, session dates and transcription authorship are not established by the files.

## Prior work

The prior-art search covered De Leeuw (2000), DECODE, Tomokiyo, editions and the
Nationaal Archief digitised series. `evidence/prior_art.txt` records edition searches and corrections. Haak's *Johan van Oldenbarnevelt.
Bescheiden*, RGP GS **80** (1934), prints Aerssen letters of 1598–1601, but none between **19 April and
23 June 1601**. The 25 May and 2 June letters were not found in Van Deventer, volume II (1862).
Veenendaal's later volumes omit Aerssen's correspondence. Nouaillac's partly undeciphered 11 May 1601
letter is **to Valcke**, a different letter from the Oldenbarnevelt training witness.
No prior reading was found in the searched sources; this does not prove that no unpublished reading exists.
The DECODE search was inconclusive even on controls. Restricted books and the old Legatie-archief 611/612
key locations remain unchecked. No DECODE identifier is established here.

## Method and glyph corrections

The matching README outcome is **key recovered based on adjacent plaintext**: key rebuilt from interlinear
glosses and a decipherment sheet in the same file, then applied to the undeciphered target. There was no
existing 25 May decipherment to transcribe; this was not a ciphertext-only attack.
The syllabic nomenclator uses numbers, letter-shaped and Greek-like signs, modified by bars, strokes and ticks,
for syllables, letters and names. Alternative values can reflect unresolved glyph distinctions, not proved
polyphony. Dots separate tokens. The differing 1598 key is not pooled into the 1601 measure.

- **qF = po** is the foot-barred q in the target and 30 April A10/A16 (*pour resister*, *pour affermir*).
  **qT = qui** is the through-stroked q of 11 May M11u. Source label q_ conflated these shapes; the transcriptions
  distinguish them. q^ remains separate. The qF (foot bar) versus qT (stroke through the descender)
  distinction was checked visually on scans 43, 57 and the 11 May scan.
- The target's Queen code is corrected to **plain 42**, with three attestations: 11 May, 28 May, list A12.
- **theta = f** is singly attested. The B-like sign of 28 May is not silently equated with theta.
- Repository grades: H primary key, C known plaintext, M uncertain, I inferred. No H primary-key claim is
  made here. Attested values are C; theta's glyph uncertainty and minority alternatives remain M.
  The source's frequency grades (H ≥3, C 2, M 1) survive only in key.tsv's **legacy_support** column,
  to reproduce the historical validation bands. List A is a decipherment, not a key sheet.

## Reading: 25 May 1601

Brackets mark cipher spans; braces retain unestablished name codes. Spacing, accents and punctuation are editorial.

> … l'Agent d'Angleterre m'a asseuré qu'on renoue la negotiation de la paix; et que je ne doibz
> [douter de l'effort de {47'} pour y disposer la Royne d'Angleterre et l'obtenir par toutevoye].
> Sans me vouloir anatomiser ce, [toutevoye il est interessé au parti de feu {45'}], et par la
> delation de M. l'Ambassadeur de Nevill, que depuis a esté mis dans la tour.

English: The English agent assured me that the peace negotiation is being resumed, and that I must not
 doubt the effort of {47'} to bring the Queen of England to it and obtain it by all means. Without wishing
 to dissect this: nevertheless he is implicated in the party of the late {45'}, and by the denunciation
 of the ambassador Neville, who has since been put in the Tower.

The pronoun's referent and the attachment of the denunciation clause remain uncertain. *Par toute voye*
is a plausible spacing. **45' = Essex is grade I**, inferred from *feu {45'}* and Neville in the Tower;
it remains a gap in the public reading and reveal. **47' is unidentified**.

## Historical context, not decoded identification

The report falls among Anglo-Spanish peace feelers after Boulogne (1600).
Essex was executed on 25 February 1601; Sir Henry Neville, English ambassador in Paris, was implicated
and sent to the Tower. Ralph Winwood, Neville's secretary, was then the English agent in Paris.
This contextual identification of the unnamed *Agent d'Angleterre* is not proven by the cipher,
does not identify 47', and supplies no key attestation for 45'.

## Sibling: 2 June 1601

> D'ailleurs [La Bauderie, ambassadeur du Roy a {88'}] m'a adverty qu'un Escossois nommé
> Stadt ou Stalwalter tient ordinaire correspondance avec les Archiducqs …

English: Moreover, La Bauderie, the King's ambassador at {88'}, informed me that a Scot named
Stadt or Stalwalter maintains regular correspondence with the Archdukes …

**9/11 = 81.8%** have gloss-attested values. `20^ = ba` is inferred from La Bauderie (only 21^ is glossed);
`88' = Bruxelles` is contextual only: both grade I and excluded. `k^ = ri` is a singly attested minority
alternative to pe, grade M. Identification with La Boderie and Brussels is a hypothesis, not a code attestation.
This sibling prevents a complete extent for the combined target although 25 May is above the bar.

## Measurement and validation

`scripts/attest.py` rebuilds support from 11 May ALIGN and 28 May SEG records plus the three explicit list-A
pairs. It writes `evidence/attestation_25may.tsv` and the reveal: **59/61 = 96.7%** attested at least once,
**58/61 = 95.1%** at least twice. Theta is the single-attestation token; both open names remain in the denominator.
Including contextual Essex gives 60/61, not the headline. Grades: C 58, M 1, I 1, unassigned 1.
Sibling: C 8, M 1, I 2. Combined supported fraction: **68/72 = 94.4%**.

30 April reproduces **281/330 = 85.2%** of list A using any listed alternative, **252/274 = 92.0%** in the
old frequency-H band. Fixed top values give **270/330 = 81.8%**. The aligner selects alternatives against the
answer, skips reference letters and absorbs mismatches; the 330-token denominator includes an ellipsis,
and A19 is incomplete. Excluding the ellipsis gives 281/329. **List A now supplies attestation evidence,
so it is no longer a clean holdout.** Frozen historical versions are not established.
Coverage is not independently established accuracy.

French word coverage is **0.838**; 2,000 order shuffles: mean **0.395**, maximum **0.667**; 2,000 key
permutations: mean **0.401**, maximum **0.726**. The controls were run with `scripts/measure.py` and `scripts/control2.py` in this folder.
The permutation script preserves the original sorting of labels across the qF/42 relabels for seeded runs.
The controls test structure, not grammatical correctness: free-gap word segmentation rewards fragments,
and key permutations vary decoded length. Further sensitivity checks are recorded in the initial review.
Both reviews assess the transcriptions and corrections; the reviews themselves are not independent image inspections.

## Remaining gaps
- 25 May code 47' - blocker: open-codes; no attested name value in the sibling letters
- 25 May code 45' - blocker: open-codes; Essex is grade I from context only, retained as a gap
- 2 June sign 20^ and code 88' - blocker: open-codes; ba and Bruxelles are contextual guesses, not attested values
- French lexicon provenance and licence before redistribution - blocker: no-key-material; upstream source documentation is missing
- Oldenbarnevelt's location for an atlas route - blocker: no-key-material; only Paris is established by the source evidence
- Independent holdout validation - blocker: no-key-material; a frozen key/transcription pair and an unused witness are needed
- Contemporary key sheet at the old Legatie-archief 611/612 locations - blocker: no-key-material; current location unresolved

## Escalation
- [x] siblings: 11 May and 28 May transcriptions used; 30 April and 2 June compared; inventory retained
- [x] clear-pages: list A examined; it deciphers 30 April, not 25 May; no target decipherment reported
- [n/a] known-keys: no contemporary key sheet available; old Legatie-archief 611/612 location unresolved
- [x] print: De Leeuw (2000), DECODE, Tomokiyo, editions and NA digitised series searched; prior_art.txt records Haak, Van Deventer and Veenendaal results and access limits
- [x] key-rebuild: qF/qT separated after visual checks and plain 42 corrected; list A adds direct support
- [x] retry: target segments remeasured with corrected key; names and the two sibling guesses remain I/open

## Files and reproduction

`transcription/`: five letters' records, list A, two token-only files. `key.tsv`: values and provenance.
`reading.txt`: edited excerpts and translations. `codex_review/`: both reviews verbatim.
`evidence/`: source inventory, prior-art notes, token support and run outputs.
The controls need a modern French word list as a JSON array at `scripts/fr_words.json` (not included; the runs used a
336,524-word list of the kind published as the npm package an-array-of-french-words). `frscore.py` adds early-modern spellings.

Run from the repository root:

```
python3 targets/aerssen1601/scripts/attest.py
python3 targets/aerssen1601/scripts/measure.py targets/aerssen1601/key.tsv targets/aerssen1601/transcription/25may1601.md --control 2000
python3 targets/aerssen1601/scripts/control2.py targets/aerssen1601/key.tsv targets/aerssen1601/transcription/25may1601.md 2000
python3 targets/aerssen1601/scripts/validate.py targets/aerssen1601/transcription/listA_1-19.txt targets/aerssen1601/transcription/30apr1601_blind.md
python3.14 targets/aerssen1601/scripts/build_page.py
python3 docs/_check_profile.py aerssen1601
python3 docs/_check_writeup.py aerssen1601
```

