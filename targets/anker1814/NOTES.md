# anker1814: Carsten Anker (London) to Prince Christian Frederik, leaf of 28 June 1814 in the 1811 symbol cipher (Riksarkivet RA-EA-5938)

Status: read (Brice Dudout, 9 Nov 2026; key of the 1811 symbol cipher rebuilt from its decipherment of the time and validated on a held-out part, 0.950 vs best of 200 shuffled keys 0.019; leaf of 28 June 1814 read at 98.8% of cipher signs, 3 logograms restored [D.K.H.], one word unclear). New decipherment: the leaf is not in the printed edition.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Sources: **Arkivverket / Riksarkivet (Oslo)**,
RA-EA-5938 Christian Frederik, on Arkivportalen; **C. J. Anker (ed.)**, *Christian Frederik og Carsten Anker's Brevveksling 1814,
samt Uddrag af deres Breve fra 1801-13 og fra 1815-17* (Royal Danish Library, Danmarks Breve, tekster.kb.dk, public domain).
No image is included: Arkivverket gives open access but no explicit reuse licence was found.

## Documents

RA-EA-5938 (an extract of the Copenhagen royal house archive; series G = Carsten Anker's papers):
- F/Fc/L0216/0009 (13 pages): Anker's letter of **31 Dec 1811** in a symbol cipher, with interlinear glosses (p. 9) and the
  decipherment of the time (pp. 11-13). Printed in clear by C. J. Anker as no. 32 ("[i Chifre.]"). Existing; used here for the key.
- F/Fc/L0217/0002 (78 pages): the 1814 correspondence. The London dispatch of 28 June 1814 in a 4-digit code has its clears of
  the time and is printed as no. 88 (existing). **PDF p. 59**, a leaf headed "fr. 28 Junii 1814" ("ad Anker C. 101a"), mixes
  about ten lines of the symbol cipher with clear Danish and French. It has no decipherment and is not in the edition: **the
  target**.
- F/Fc/L0221/0003 and G/L0230/0005: key sheets (three symbol alphabets, among them one dated Bergen 22 Mar 1814 and a pencil card
  "KN-06"), codebooks 100-999 to 7000+, turning grilles, instructions. Not used for the reading.

## The system and the key (`key_1811.tsv`, `frozen/SIGNES-2.md`)

Homophonic substitution in symbols: a = + / big X / looped &; e = slashed circle / Z; o = dotted circle / cup; m = dotted arch /
<; logograms # = jeg, -- = Sverige. Word gaps are mostly kept. The key (36 labels) was learnt on the 1811 letter **p. 9 only**
(glossed lines, then lines aligned with the decipherment of the time p. 11 and print no. 32) and frozen before measurement.

## Validation (`validation.txt`)

A first pre-registered measurement failed: the archive's pencil card KN-06 on 8 held-out lines of the 1811 letter, 0.025 vs best
shuffled 0.018 (`frozen/PREREG.md`, `frozen/MESURE.txt`); a third of the signs have no value on the card, which is a partial
reconstruction. The second protocol (`frozen/PREREG-2.md`, hashed, declaring the failure) built the key above and measured it
once on the held-out 1811 p. 10 left column (10 lines) against the decipherment of the time: **0.950** of characters against at
best 0.019 for 200 shuffled keys (margin 0.931): **validated** (>= 0.85 and margin >= 0.30). Declared limit: print no. 32 had
been read in full before, so the held-out part was transcribed by shapes, not blind; the control at 0.019 shows the score does
not come from that.

Applicability to the leaf, fixed before decoding (`frozen/P59-APPLICABILITE.txt`): 0.937 of its signs have a value in the
1811 key against 0.369 matching the Bergen 1814 alphabet's shapes (scored generously): the 1811 alphabet.

## Reading (`reading_p59.md`, `translation_p59.md`)

252 cipher signs: 249 certain or probable = **98.8%**; restored: one logogram (3 occurrences) as [D.K.H.] = "Deres Kongelige
Høihed" (Your Royal Highness), from the clear "D. K. H.s" and "[D.K.H.]s Portrait"; one word, ‹felv›, decoded but of uncertain
sense. New shapes with values fixed by agreeing words: "4·" = u (11 words), and o, k, e once each.

Content: the match of Princess Charlotte of Wales with the Prince of Orange is "broken off for ever"; Anker revives his "old idea"
of a match with Christian Frederik, provided the prince is not bound and Norway's horizon clears; the prince's portrait will be
engraved and published in London within 8 to 14 days; "only let Your Royal Highness not bind yourself!"; Hardenberg and Anker agree.

## Prior work (re-checked 9 Nov 2026)

Nothing in this repository (no target, catalogue entry or lead for RA-EA-5938). The leaf is neither deciphered in the file nor
printed in C. J. Anker's edition (full text of 254 letters). **The project itself is known**: Christian Frederik writes of "the
intended connection with Princess Charlotte [of Wales]" in his printed letters to Anker of 24 June (no. 31), 11 Oct (no. 39) and
12 Dec 1814 (no. 43), and Anker reports on the Charlotte-Orange match on 26 Sept (no. 94). No secondary study of the project was
found in a quick search. What is new is Anker's own proposal of 28 June 1814, in cipher.

## Remaining gaps

- ‹felv› (one word, l. 9 of the leaf): decoded letter by letter, sense not established - blocker: open-codes; a second reader on the shapes (QF, EQ, LAM, XS) is the next step
- The logogram N12 restored [D.K.H.] (3 occurrences): not in the 1811 key - blocker: open-codes; the Bergen 1814 sheet's logogram list could confirm it

## Escalation

- [x] siblings: the 1811 letter with its glosses and decipherment of the time gave the key; the code dispatch of the same day is printed (no. 88)
- [x] clear-pages: decipherment of the time of the 1811 letter (pp. 11-13) used for the key and the held-out reference
- [x] known-keys: the archive's pencil card KN-06 measured (failed); the Bergen 1814 alphabet compared on the leaf (0.369, not it)
- [x] print: C. J. Anker's edition searched in full text; the leaf is not printed
- [n/a] key-rebuild: the leaf reads at 98.8% with the frozen key
- [n/a] retry: only one word is unclear
