# ercole1547 report (24 Nov 2026, about 20:00 Brisbane)

Bottom line: key recovered from the ciphertext alone on lines 1-6; the two held-out lines decode to Italian on the
first pass; the shuffle control passes at both seeds. Per-letter figures wait for the judge. No prior key or reading found.

## Target

- Ercole II d'Este to his secretary Claudio [Ariosti], Ferrara, 8 Jan 1547 [sourced: date line on c. 16v, address on c. 17v].
- Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Ercole II d'Este, sfasc. I, cc. 16-17. Catalogue 2160.
  IIIF manifest https://edl-jarvis.cultura.gov.it/meta/iiif/89e1bdc6-a46d-4627-9770-efbd17e544fb/manifest
- Pages: 16r clear; 16v clear, then 8 cipher lines, then clear; 17r blank; 17v address [measured: all four viewed].
  No other cipher in the bifolium. The rest of the Ercole II folder in Campori was not swept for the same table (open).
- Tokens [measured, TRANSCRIPTION.tsv]: 276 signs, 160 raised marks, 13 dots = 449 tokens. 25 sign shapes, 15 marks.
  First-pass decode: 435 letters, 1 sign with no value, 2 uses of one code sign.

## Prior art (PRIOR_ART.md)

- None found: no key, decipherment, gloss or edition [sourced].
- Brice Dudout tried this letter on 5 Nov 2026 and left it "Not solved" (targets/ariosto1559/NOTES.md) [sourced].
- Not the ariosto1559 table, and not any WAINUT Este/Gonzaga key [measured: keys and one 1559 image compared].
  Same family as 1559: sign plus raised vowel figure. The figure values differ.
- Not checked: ASMo Cifrario (the original key may be there), Cremonini 2019, HathiTrust/Google Books, DECODE behind login.

## Key (KEY.tsv, frozen before the held-out decode)

- Figures give vowels, raised or on the line: 4 a, 5 e, 6 i, 7 o, 8 u. Other line vowels: S15 e, S20 a, S18 o, S08 i, S06 u/v.
- Consonant signs that take a raised figure: S01 p, S02 r, S11 t, S12 d, S13 qu, S17 s, S03 c (S24 c).
- Consonant signs that take a stroke for the vowel (/ a, \ e, I o): S14 l, S10 n, S04 m, S19 g.
- A bar over a consonant doubles it (ll, cc, ss). d with a cross after c = "he" (che). Dots carry nothing.
- Open: one code sign (S01^4s, a person, twice), one sign with a cross-stroke (line 5), raised 9 and 2 weak.
- How it was found: annealing on five structural models fixed the vowels (5 = e, 6 = i, 7 = o in every run) but did not
  converge on the consonants; one run of the refined model read "intenderete ... opera per intendere". The pattern word
  "intendere" (lines 1 and 3) then opened the rest by hand. Every attempt is in SOLVE_LOG.md.
  Caveat for the method label: "intendere" also stands in the clear lines of this letter.

## Figures

- Per letter, per line, held-out and whole page: PENDING THE JUDGE (judge/BRIEF.txt, judge/decode.txt). Not self-scored.
- Shuffle control (shuffle_out.txt) [measured]: 5,000 shuffled keys at seed 20261112 and 5,000 at seed 7.
  Held-out lines: real -2.284 per letter; shuffles mean -5.18 / -5.20, best -3.44 / -3.58; 0 of 5,000 reach the real key at either seed.
  Whole page: real -1.963; best shuffle -3.69 / -3.68; 0 of 5,000 at either seed.
- The length worry noted before solving did not come true: the control separates on 60 held-out signs.

## Gist (UNCHECKED; my reading of DECODE.txt, emendations in mind; the judge has not seen it)

Since you will have heard what has newly happened in Genoa, and the matter being of the great importance that it is, we
want you to do everything to learn as much as you can, both about the causes of that rising and about how [code sign:
a person, probably the Emperor] means to punish the presumption of [unclear] and set right the affairs of that city;
which, being the ladder of Spain into Italy, it is to be believed that [same code sign] will do everything not to let it
fall into the hands of the French. Use extraordinary diligence to inform yourself fully of everything.
[derived] The date fits the Fieschi rising at Genoa of early January 1547; that link is from general knowledge, not checked in a source.

## Open problems

1. One reader, one pass. No second transcription, no palaeographer. 11 proposed emendations are listed in SOLVE_LOG.md and are NOT applied.
2. S09 mixes two signs (figure 6 = i, and a b/f-like sign = f). A second pass should split them (Francesi, facciate).
3. Line 4 end to line 5 start ("de que so t de l i ll so t ? ri t di a re") is not read.
4. The code sign S01^4s is not resolved.
5. Bar = "ni" on S10 (ogni) against doubling elsewhere; "dillgentia", "italla" lack an i. The bar rule may be finer than stated.
6. The language model is local (work/build_lm.py), because the registry model could not be fetched (gutenberg.org 503).
7. Brice Dudout holds the neighbouring 2159 and tried this one: tell him before any filing.
8. More text in the same table would strengthen the control: Ercole II to Claudio Ariosti, Nov 1546 to Aug 1547 (ASMo, Ambasciatori Germania, b. 7; Campori folder).

## Files (/home/claude/keyless/ercole1547/)

PRIOR_ART.md, FETCH_LOG.txt, TRANSCRIPTION.tsv, SIGNS.md, FREEZE_TX.txt, SOLVE_LOG.md, KEY.tsv, FREEZE_KEY.txt,
decode_once.py, DECODE.txt, judge/BRIEF.txt, judge/decode.txt, shuffle.py, shuffle_out.txt, log/anneal_*.txt,
work/ (solver.py, solver2.py, build_lm.py, tx_short.txt, tx_build.py, the 31 MB model table), img/ (page images at
1000 px, cipher strips), ref/ (1559 comparison image and manifest).
