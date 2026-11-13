# PREREG — catalogue 1555 (Ippolito Capilupi to Ferrante Gonzaga, Estense, Autografoteca Campori, cc. 80a-80h)
Frozen 12/11/2026 BEFORE any key-building, by the Opus 5.5 agent of the Déchiffrement thread.

## State at freezing (honesty)
- Two blind transcription passes (A, B) exist for 02r 03r 04r 05r 05v 06r 06v 07r 09r; arbitration still to come.
- Two hands/systems: X = 03r, 09r (overlined 9, separators, light superscript letters by a second hand);
  Y = 02r, 04r, 05r, 05v, 06r, 06v, 07r (cursive, no overlines). Y shares the absent digit pairs 09 99 53 (73 ~0)
  of Camillo Capilupi's numeric cipher (our capilupi-ferrante-1545; WAINUT/LcCompany capilupi1545 cc. 48/49r):
  same system.
- Before this freeze, structural statistics only were computed on 03r 09r 06r 06v (digit and pair counts, odd-run
  lengths, units "odd*+even"), plus ONE vowel-skeleton test on 06r+06v (even digits as vowels: best permutation
  0=i 2=o 4=a 6=e 8=u, -1.226 vs shuffled -1.28). No other value was assigned. **05r was never used for anything.**

## Held-out portion H
- **H = all of c. 05r (Y hand), 21 lines, 919 digits (~380 units).** Never used for statistics, key-building, cribs
  or Fable. Excluded by name (`t05r`) from every build script and from any Fable package (FORBIDDEN regex on
  the 05r digit strings + check_leak.py).
- H is measured on the arbitrated transcription `transcriptions/1555/final/t05r.txt` (arbitrated with no key).

## Key format
`KEY-1555.json`: {code: plaintext}; plaintext "" = null, "[name]" = nomenclator word (cuts, not counted);
`_parse`: `units` (split each cipher segment into odd*+even units) or `longest` (longest code first).

## ONE measure (scripts/1555/measure_1555.py, frozen with this file)
- M = share of decoded characters of H covered by Italian words of length >= 3 (lexicon: words with frequency >= 3
  in work/it_nunz_clean.txt, j->i, v->u), maximum-coverage segmentation; unknown codes count as uncovered.
- Controls: 200 keys made by permuting the plaintext values among the key's letter codes (seeds 0..199), same parse.
- **PASS iff M > max(controls) AND M >= 0.60.** Otherwise FAIL: no reading is claimed for H.
- One run only: `python3 -I scripts/1555/measure_1555.py KEY-1555.json transcriptions/1555/final/t05r.txt work/it_nunz_clean.txt`,
  output copied verbatim to `MESURE-1555-H.txt`.
- Gate before the run: the key's decoding of the BUILD text must read as coherent Italian over several
  consecutive lines (checked by me and written to GATE-1555.md). If not, no measure is made and H stays untouched.

## Reading count (only if PASS)
Daniel's rule: sure / probable / restored / unresolved per word, by script; >= 95 % sure+probable on a portion
>= 300 characters for "read"; otherwise "read in part".
