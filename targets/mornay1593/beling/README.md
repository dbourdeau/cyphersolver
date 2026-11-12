# Duplessis-Mornay 1595-1612: the folded 1593 key tested, the Rohan 1594 key fits Mme de Rohan's 1597 letters but not her 1611-12 ones

Contributed by Andrew Beling, with AI agents, 11 November 2026 (round 1) and 11-12 November 2026 (round 2, section 6).
This folder adds to `targets/mornay1593/`. It changes nothing in Daniel Bourdeau's files or Brice Dudout's key.
The NOTES.md and profile.json changes that go with it are in the same pull request.

[V] = checked on the image or in output. [I] = inference.

## 1. What is here

| File | What it is |
|---|---|
| `PREREG.md` | the two tests, written before the scripts and before the vols. 7-8 transcription; Addendum 1 adds the Rohan test |
| `key/key_dudout.tsv`, `key/rohan1594_key.tsv` | the repo's keys copied unchanged (sha256 in `results/frozen_inputs.sha256`) |
| `transcription/repo/` | the repo's `lomenie1595.txt`, `duplessis1597.txt`, `ciphertext.txt`, copied unchanged |
| `transcription/v7v8_figures.tsv` | 34 new passages from vols. 7-8 (Rohan 1597: 19; Duplessis Sep 1597-Apr 1598: 15), figures only |
| `transcription/v7v8_context.tsv` | the clear words around each passage, in a separate file |
| `results/test_result.json`, `test_output.txt` | the test result |
| `results/mechanical.txt` | every passage decrypted with each key, nothing edited |
| `results/rohan1597_reading.md` | what the Rohan output suggests, with the new values it needs |
| `results/scan_shift.txt` | the exploratory scan of shifted folded keys |
| `results/frozen_inputs.sha256`, `external_inputs.sha256` | hashes frozen before the run; the language corpus (vol. 6 OCR) is outside the folder |
| `scripts/test_folded.py`, `scripts/scan_shift.py` | the test and the scan (standard library) |
| `images.txt` | the archive.org page images used; none committed |
| `CHECKS.txt` | hash check, a second run (identical), the scan |

Run from this folder: `python3 -I scripts/test_folded.py <path to mmoiresetcorre06morn_djvu.txt>` (round 1),
`python3 -I scripts/test_round2.py <same path>` and `python3 -I scripts/explore_system.py` (round 2, section 6).

## 2. Test 1: the folded 1593 key on Loménie 1595 and Duplessis 1597 [V]

Material: the repo's transcriptions, 203 numeric groups. Pre-registered pass: coverage ≥ 0.85 and ≥ 0.30 above the best
of 200 random number sets; language sign if the key beats 190 of 200 permuted keys (letter-trigram model from vol. 6).

- Coverage **0.655** (133/203); random number sets mean 0.306, best 0.616; margin **0.039**. Fails.
- Language: −3.43 per letter, beats 193 of 200 permutations (null mean −4.36, best −3.15). A "sign" by the rule.
- Pre-registered verdict: **inconclusive** (coverage fails, language sign).
- Control, the 1593 figures: coverage 1.0, −2.24 per letter, beats 200/200. The method works where the key is right.
- [I] The key does not fit. −3.43 is far from the −2.24 of real text under the same model, the output has no words
  (`mechanical.txt`: "ut [62] [110] [4]" for "du sieur ..."), and the new 1597-98 Duplessis figures (part B)
  give coverage 0.49 and no language sign (175/200). The 193/200 probably comes from frequent small numbers
  falling on frequent letters, not from a reading.
- Shifting every key number by 1-100 (exploratory): best −3.00, coverage ≤ 0.37. No lead.
- A disclosure: a rough coverage count (about 0.65) was made before PREREG.md was written; PREREG says so.

## 3. Test 2: the Rohan 1594 key on Mme de Rohan's 1597 letters [V]

While locating the vols. 7-8 figures, two letters of **Mme de Rohan to Mme Duplessis** turned up: vol. 7 LXXXII
(Feb 1597, p. 169) and CXLI (Pequigny, 4 Aug 1597, pp. 306-307). Same writer and recipient as the vol. 6 letter
from which the repo built its Rohan key; the repo had tried that key only on Loménie and Duplessis. Addendum 1 to
PREREG.md set the test before transcription.

- 50 groups (19 passages, 12 of them single name figures). Coverage **0.78** (39/50).
- Language: −2.26 per letter over 49 letters; beats **197 of 200** permutations (null mean −2.68, best −2.21).
- Pre-registered verdict: **fits**. The sample is small, and three permuted keys scored higher.
- Mechanical output [V]: "M. de vi l le [672] et de [134] me ni e"; "M. de ca r [38] [160] i s";
  "M. de c la s ti l [134] n"; "10 = le roy a faict bonne chere a 20".
- Reading [I] (`results/rohan1597_reading.md`): **M. de Villeroy et de Lomenie**, **M. de Cargrois**,
  **M. de Chastillon**, "envers le roy", if 672 = roy, 134 = lo, 38 = g, 160 = ro. 134 is needed twice and gives a
  known name both times. "Chastillon" is one sign off: 111 is printed "la" in 1594 [V, vol. 6 p. 83].
- The Rohan key on part A and B (a repeat of the repo's step 5): no fit again (64/200 and 5/200).

## 4. Vols. 7-8 transcription [V]

All bare figures found by searching the vol. 7 and vol. 8 OCR for runs of figures, then read on the page images:
Rohan pp. 169, 306-307 (vol. 7); Duplessis to his wife, vol. 7 pp. 335 (27 Sep 1597) and 347 (Oct 1597),
vol. 8 pp. 197 (20 Mar 1598), 261 (1 Apr 1598) and 307 (11 Apr 1598). The editors printed letters among some
figures ("pt", "v", "T"); they are kept as written and not counted as groups. The name code "81 63" recurs
in vol. 8; round 2 transcribed all twelve places (`transcription/v8_namecode.tsv`). The repo's C3 (vol. 7 p. 125) was checked against the
image and is right; the OCR's "93" there is wrong.

Vols. 9-12: see section 6. The OCR search can miss runs it garbled.

## 5. Open (after round 2; see section 6)

- The 1595-98 Duplessis/Loménie system: not read. Neither the folded 1593 key nor the Rohan key fits. Round 2 found no
  clear copy of any passage, but did find cribs for Loménie's letter (section 6.4).
- Rohan 1597: R1 and R18 still unread; 672, 134, 160 have no second occurrence; 38 has one (vol. 9, R20), and the
  pre-registered test does not support it.
- Rohan 1611-12 (vol. 11): a different table; unread.
- Dates: LXXXII ends "Des isles de Mons, ce 27 febvrier 1597" in the OCR (not checked on the image); CXLI "De Pequigny, ce 4 aoust 1597" (OCR, same).

## 6. Round 2 (11-12 Nov 2026)

Pre-registration `PREREG_round2.md`, written after an OCR survey of vols. 9-12 and before any vols. 9-12 page image was
read (its first hash, with a timestamp, is in `results/prereg_round2_initial.sha256`; it was not changed afterwards).
Inputs frozen in `results/frozen_inputs_round2.sha256`. One run of `scripts/test_round2.py`; a second run is identical
(`CHECKS.txt`). Everything in 6.3-6.5 beyond the test numbers is exploratory.

### 6.1 New files

| File | What it is |
|---|---|
| `transcription/v9v12_figures.tsv`, `v9v12_context.tsv` | every bare-figure passage found in vols. 9-12: 16 Duplessis (1599, 30 groups), 43 Rohan (1599 and 1611-12, 88 groups), 3 unsigned (1612, 9 groups) |
| `transcription/v8_namecode.tsv` | the twelve places of the name code 81 63 in vol. 8, with context (one is round 1's M8) |
| `scripts/find_figures.py` | the OCR search used to find candidate figures (hits must be read on the image) |
| `scripts/test_round2.py`, `results/round2_result.json`, `round2_mechanical.txt` | Tests 3 and 4 and the extras |
| `scripts/explore_system.py`, `results/explore_system.txt` | exploratory structure of the Duplessis/Loménie figures |

### 6.2 What vols. 9-12 contain [V on the images unless marked]

- Vol. 9, Duplessis to his wife, Jan-Mar 1599 (CXXIII-CXXXIX): the name code **153 63** (five places; cf. 81 63 in
  1598), **33** alone (eight places, a man in the sale of "les Boues"), and three short runs: 88 32 24 70 (a person),
  40 9 64 18 ("j'ai tiré de ... en confession, que sa matiere est le regule"), 58 166 32 19 ("La ... m'y faict plus
  penser que tout"). The OCR misread two of these (24 as "il\.", 40 as "l\o").
- Vol. 9, CLXIX, **Mme de Rohan to Duplessis**, La Rochelle 30 Oct 1599, p. 297: "pour M. de 121. 174. 38. 143."
- Vol. 11, **Mme de Rohan to Duplessis**, Nov 1611 - Mar 1612 (CXCII, CXCVII, CC with a postscript of 4 Dec 1611,
  CCXXXII): 42 passages, 84 groups, mostly single figures used as names (77, 115, 26, 110, 39, 221, 81, 28, 29, 11,
  105, 227, 18, 113) and eight runs of 3-10 figures. The OCR of both scans gave 110 or 115 where the image has 113.
- Vol. 11, CCXLII, unsigned letter to Duplessis, Paris 25 Jul 1612: 16 75 90 28; 77 12 90; 16 75.
- Vols. 10 and 12: no figures found. This rests on the OCR search only (both scans for vol. 10, one for vol. 12); a run
  the OCR garbled beyond recognition could be missed.
- Vol. 8, 81 63: twelve places, Duplessis to his wife, 18 Mar - 11 Apr 1598, all read on the images
  (`v8_namecode.tsv`). Contexts: "si 81 63 disoit vrai, il nous tireroit de beaucoup des importunités", "la drogue de
  81 63", "M. 81 63 nous traisne tousjours". With vol. 9 ("si M. 153 63 dict vrai", "sa matiere est le regule ... l'or
  s'y noye") the person looks like an alchemist or empiric whose promised result would clear the family's debts [I].
- Correction to round 1 [V]: M7-M9 (p. 197) are in letter LXXXII (Angers, 21 Mar 1598 by the OCR date line), not LXXXI
  (p. 195, a short letter of 20 Mar with no figures). `v7v8_figures.tsv` is left unchanged because it is hashed; the
  correction is recorded in `v8_namecode.tsv` and here.

### 6.3 Test 3: the 1594 Rohan key on Mme de Rohan's later figures [V]

- All new Rohan groups (88; 1599 and 1611-12): coverage **0.568** (50/88), language **−2.69** per letter over 64
  letters, beats **85 of 200** permuted keys (null mean −2.67, best −2.19). Pre-registered verdict: **does not fit**.
- 1611-12 alone: coverage 0.56, beats 87/200. Runs of two or more groups alone: coverage 0.62, beats 126/200.
- Mechanical output (`round2_mechanical.txt`): "que pe so l re r" (R28, after "desseing de"), "pe re u r" (R57, after
  "promesse de"), "[123] s p po [164] n ci s" (R47). No French. The coverage comes mostly from single small figures that
  are names in these letters, so it means little.
- [I] By 1611 Mme de Rohan wrote to Duplessis (his wife had died in 1606) with another table. A few letter values
  could be shared (57, 58, 59 often fall where an s would fit; 58 ends R40 and R58), but nothing reads.

### 6.4 Test 4: the four values inferred in round 1 [V]

Only 38 recurs in a run (R20, 1599); 672, 134 and 160 do not occur again. The extended key scores −2.695 against
−2.695 for the base key; it beats 130 of 200 controls with random values on the four figures. Pre-registered verdict:
**not supported**. [I] The test had almost no power: one group in one four-group run. Read with the key, R20 is
"M. de la vi [38] ne", and 38 = g gives "M. de La Vigne", a man named in a letter about marriages; the name is not identified, so this is neither a confirmation nor a refutation.

R1 ("d'escrire pour le [100] c [35] u que [66]") and R18 ("plus de son u u r", i.e. 28 14 54) remain unread. R18 ends
like R57 of 1612 (148 158 14 54), but the 1611-12 table is different, so this proves nothing.

### 6.5 The 1595-99 Duplessis/Loménie system (exploratory)

Clear sources searched: archive.org (all 12 vols., both scans where they exist), the 1625 edition (tome II,
archive.org `ned-kbn-all-00003389-001`, OCR), web searches (no published decipherment, no printed key). The Mornay
papers are in archives (Nantes BM, fonds Dugast-Matifeux DM2/92-94; AN 402AP; the Institut / BnF), not online. **No
clear copy of any ciphered passage was found**, so no key was built and nothing was tested.

What the structure shows (`results/explore_system.txt`; 334 groups, 112 distinct):
- Loménie 1595 is not like the Duplessis letters: 23 of its 95 groups are x10 codes (810 x9, 910 x5, 410 x4, 610,
  210, 510, 710), against 4 of 239 in Duplessis's letters of 1595-99. Treat them as two systems until shown otherwise [I].
- Repeats: "810 44 109 27 32 10" (L1, L6), "810 62 110 4" (L2, L4), "40 9 64" (1598 M9 "40 9 64 33", 1599 D5
  "40 9 64 18"), "40 25" (M10, M13), "153 63" and "81 63" (names).
- Cribs for Loménie's letter, overlooked so far: (a) the editors' note under it, vol. 6 p. 181: "Au dos est escrit :
  Pour la dame de Querveno. Cela regardoit le desseing du sieur de Camor, de se saisir de M. de Mercœur, et le mener à
  Rennes avec la dame de K."; (b) the king's own letter of the same day, vol. 6 CVI, "escrite en chiffre" and printed
  in clear (also in the 1625 edition), on the same affair: "... non seulement ladite ville sera asseurée pour celui qui
  me doit faire ce service; mais telle autre ville de mon pays de Bretagne qu'il aura agreable ...".
- So [I]: L4 "feut la resolution du sieur 810 62 110 4" is very likely "du sieur de Camor" (810 = de, as in the Rohan
  1594 word series), and L6 "lui promettre telle 77 99 108 102 107 410 910 810 44 109 27 32 10 et vaudra pour l'estat
  de colonnel de la cavallerie legere dudict pays" likely ends "... de Bretagne", which makes "810 44 109 27 32 10" =
  "de Bretagne" in L1 too. These are two cribs, not a key: they do not fix whether groups are letters or syllables, and
  L2 "en 810 62 110 4" does not read well as "en de Camor". No further reading is offered.
- The best next step is archival: the original of the king's cipher letter CVI (24 Feb 1595), or Loménie's original,
  in the Mornay papers; either would give a key for the 1595 system.
