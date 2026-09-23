# DECODE R1874 — Alvise Mocenigo (Madrid) to the Doge and Senate, 26 October 1628

Catalogue 266 ("Unknown sender to unknown recipient", ASVe IT ASVe 0045 010 Busta 30 f. 174, undated, class C).

**Result: read at the time.** The record's 16 images hold the ciphered despatch *and* the chancery's decipherment of
it. Identified from the clear text and CSP Venice vol. 21 no. 515. Key not rebuilt here; it was rebuilt later from this
record's cipher and decipherment for the sibling R1862 (see `r1862/NOTES.md`; decipherment transcribed in full in `tx/decipherment.txt`).

## What the record is

DECODE R1874, 16 images (`IMG_R1874_I8951`–`I8966`, PNG, login; not public domain, kept git-ignored in `img/`),
DECODE transcription `DOC_R1874_D3607_3607.txt` (MEG, 29 Jan 2020, cipher digits + clear text). The DECODE record
has no date, sender or receiver.

| images | what |
|---|---|
| 8951–8954 | Despatch, first copy: clear paragraphs and numerical cipher paragraphs; margin paragraph marks (8, ‡) |
| 8955–8959 | The **decipherment**: the whole despatch written out in clear, paragraphs numbered 6, 7, 8, 9 in the margin |
| 8960–8964 | Second copy (duplicato) of the same despatch, enciphered separately; dated "Madrid li 26 Ott:re 1628" (DECODE's transcriber read 1606) |
| 8965 | Address leaf: "Ser:mo Principe", n.ro 74 |
| 8966 | A deciphered page of the next despatch (29 Oct 1628 = CSP Venice 21 no. 520: consultations on English and Dutch trade, a Jesuit's 100,000 crowns) |

Sender: Alvise Mocenigo, Venetian ambassador in Spain. Date: Madrid, 26 October 1628. Evidence: the clear text
(English repulsed at La Rochelle, Spinola lodging with his son-in-law Leganés, Monterrey at Genoa, Mirabel, Nuncio
Monti) and CSP Venice vol. 21 no. 515 (Madrid, 26 Oct 1628, Senato, Secreta, Dispacci Spagna), whose clear
opening is word for word R1874's p. 2 clear text and whose "italics deciphered" passage (Cottington's planned
journey, dropped since Buckingham's death; Endymion Porter waiting for orders; Rubens negotiating a truce with
the Dutch) is on decipherment p. 8958 ("Doveva come ho penetrato passare a questi Regni il secretario Cottington
di ordine del Re d'Inghilterra…"). CSP calendars only the England-related passages; the Italian decipherment in
the record is complete.

Prior art: Tomokiyo's Venetian page covers Busta 30 records R1870/R1872/R1873 but not R1874. CSP Venice 21 (1916)
prints the English summary of the ciphered passage about England. No publication of the rest found.

## The cipher (as far as established)

- Numerical groups written as clusters. The looped "b" is the period 6; the "s" form is a 5. DECODE transcribes
  the 5 as "13" or "21" (so DECODE "21xx"/"13xx" are 51xx/53xx), consistently enough to use as token labels.
- Groups: [5|6][1–4]?dd; after the lead digit only 0,1,2,3,4,7,8,9 occur. ~2,260 groups (DECODE transcription,
  after merging fragments and splitting run-ons, `tok.py`, `seg.py`), ~370 types, ~110 with ≥5 occurrences
  covering 84%.
- 6499 = paragraph mark (at the edges of the numbered paragraphs 6 and 7).
- ~2 plaintext letters per group (paragraph 6: 386 groups / ~760 letters; paragraph 7: 245 / ~445), so a
  syllabic/nomenclator system, not letter homophones.
- Anchor: "conte di Olivares" = 672 2133 6210 2190 62x9 637 2127, at 26/71/92% of paragraph 6's groups vs
  25/70/91% of its letters, and also in copy 2 (8963). This and the paragraph marks tie the decipherment to the
  cipher.

## What was tried (all failed as reading methods; kept for the profile)

1. Letter-level homophonic annealing (it-cinquecento 5-gram) on the DECODE groups: −2.6 to −2.9/char, gibberish.
   A synthetic control (same size, 120 homophones, Italian) is solved exactly by the same solver (−1.85), so the
   failure is the hypothesis, not the solver.
2. Dropping each prefix class as nulls; mapping only the last two digits: no improvement.
3. Syllable-inventory anneal (letters + CV syllables + short words): running when the decipherment was found; not needed.
4. Hard-EM monotone alignment against the decipherment (adapted from `balbases1677/align2.py`), with and without
   the Olivares anchors: stuck at uniform two-letter splits (consistency 0.35). A key rebuild needs a fresh,
   group-exact transcription and more anchors; not done.

## Open

- The key (syllabary/nomenclator) was not rebuilt in this target; the decipherment makes the letter readable without it. It was rebuilt later for R1862 (`r1862/`).
- The decipherment pages 8955–8959 are transcribed on DECODE only roughly (as cleartext); paragraphs 6–7 are
  re-read in `tx/para6-7.txt`.
- DECODE R1862 (Busta 27 f. 354, 1628, 4 pp., "Ser.mo Principe", same cipher) is in the same cipher; DECODE places it at Rome, so possibly another Venetian envoy;
  not examined beyond page 1.
