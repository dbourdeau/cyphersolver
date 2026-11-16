# rucellai1482: notes

Status: in progress. Folder integrated 14 Nov 2026 without a page: the key has no validation figure and the gaps are workable (strict shares of sure words 25-61% per letter; see Integration check).

Catalogue 2350 and 2323 (ASF MAP LXXII 196, 200, 202, 206; and LXXII 211, which the PR calls lead 2323): Bernardo Rucellai's 1482 letters from Milan in his "HP" sign cipher. Proposed as **read in part, key partial**. No images: the ASF MAP scans are cited, not reproduced.

## Material
- Key pair: LXXII 207 (cipher) and 208 ("Decifrato della n. 207", contemporary decipherment).
- Used up for tests: 204/205 (cipher and contemporary clear, test of 6 Nov 2026) and the glosses of 201 (test of 13 Nov 2026). See validation.txt.
- Bare letters read here: 196, 200, 202, 206, 211 (no decipherment on the leaf or filed with it).

## How the key was built
1. 6 Nov 2026: letter table K_T from 207/208 by EM alignment and greedy tuning; tested once on 204 against 205: 0.6018 (best shuffled 0.2281), not validated.
2. 13 Nov 2026: second transcription pass of 207; second test on 201 against its glosses: 0.5088 (best shuffled 0.2832), not validated.
3. 14 Nov 2026: two proposals from Claude Fable 5.2 runs (lots 11 and 12; used as tools, by Brice Dudout's API runs): rule corrections on 207 (fit 0.770, then 0.778), I, the dot, l with small o, crossed equals, B tried as values.
4. 14 Nov 2026 (this proposal, K_HP_v1):
   - the q-like signs of 207 re-examined one by one at 4x: the old token "g" merged a q with barred descender (now G) and a "g" with open lower loop (now 8); against 208, G = o and 8 = e; plain q stays o, and h before e-signs;
   - the five bare letters transcribed again, blind, with the 207 convention (1320 tokens; 90 % token agreement with the earlier pass); "g" there is always the barred q, and the open-loop "g" had been written c;
   - value changes kept only if they did not lower the 207 fit and raised the Italian likelihood of held-out letters (leave-one-letter-out); I = rr and dot = tt kept from the reading (signs absent from 207);
   - fit on 207: 0.8093 (lot 12: 0.7776); lexical coverage of the four unused bare letters 0.374 against 0.122 for the best of 200 shuffled keys.

## Status and limits
- **Not validated.** No HP passage with a clear is left unused, so no fresh measurement exists for this key. The only protocol figure for the system is 0.6018 against 0.2281 (an earlier key). The figures in validation.txt are consistency checks.
- Readings: sure + probable words cover 52-66 % of the decoded letters of the cipher runs (reading/). Remaining limits: 1272 px images (b/6/t, d/b, o/Q), a nomenclator not in the key (B, ⊙, crossed equals, "e d"), ℓ° (probably "che", restored only).
- Not seen: R. M. Comanducci, *Il carteggio di Bernardo Rucellai: inventario* (Olschki 1996), pp. XXIX-XXXI and Appendix III (Rucellai's keys, printed). The key sheet of Rucellai in P. D. Gabbrielli's volume of Dieci keys (no. 14, 1484-85) belongs to another system (the "##" family).

## Prior art
No decipherment of 196, 200, 202, 206 or 211 found (catalogue vetting of 6 Nov 2026; repository searched 14 Nov 2026: no target, PR or issue on these letters except our status notes). Mallett's edition of Lorenzo's Lettere cites only 204-205.

## Remaining gaps
- Key not validated - blocker: not-attempted; the one protocol test of the system failed (0.6018 against a 0.85 bar, earlier key K_T, 204 against 205), the second too (0.5088 on the glosses of 201); K_HP_v1 has no fresh test. The routes under Escalation are still open (a further HP letter with a clear or a gloss; Comanducci 1996, Appendix III).
- Unresolved stretches - blocker: open-codes; 19, 12, 10, 10 and 17 in 196, 200, 202, 206, 211 (B, crossed equals, dotted o, "e d", l with small o) and doubtful shapes at 1272 px (b/6/t, d/b, o/Q, q/9).
- Images - blocker: needs-physical-access; the ASF server gives 1272 px at most, higher resolution needs an order to the ASF.
- Second reader - blocker: not-attempted; nobody has compared the five bare letters with the images (the integration check sampled 207 only).

## Escalation
- [ ] siblings: catalogue 2377 lists Rucellai's pieces in MAP XLVIII with glosses on about 60 pages and four filed decipherments; `targets/mediceo1483` found XLVIII 294 (Feb 1485) in another sign family ("##"), so which XLVIII pieces of 1482 are in the HP cipher is not yet known. MAP LXXII 189-215 and XLVIII have not been surveyed sign by sign (validation.txt, point 5). This is the workable route to a fresh test.
- [x] clear-pages: 208 (of 207) used for the key; 205 (of 204) and the glosses of 201 used for the two failed tests.
- [ ] known-keys: MAP LXXII 183 (the Milan embassy key of the 1490s, issue #589) compared by sign description only, see Integration check: same family of conventions, not the same key; not tried on the images. Gabbrielli's Dieci key no. 14 (1484-85) is another system (contributor).
- [ ] print: R. M. Comanducci, *Il carteggio di Bernardo Rucellai: inventario* (Olschki 1996), pp. XXIX-XXXI and Appendix III (Rucellai's keys), not seen.
- [ ] key-rebuild: after one of the above.
- [ ] retry: after one of the above.

## Integration check (14 Nov 2026)
- Second decoder, written for this check from `key/K_HP_v1.json` (pairs longest first, the two context rules, singles): identical to all six files in `decryption/` (196, 200, 202, 206, 207, 211; 1608 decoded letters).
- Fit on the training pair: 0.800 by my count (1 - Levenshtein / 535 letters of 208, letters only) against the stated 0.8093; the difference is in the normalisation. It is a fit, not a test, as the contributor says.
- The two failed tests (0.6018 and 0.5088) cannot be rerun: the transcriptions of 204, 205 and 201 and the earlier keys are not in the folder. They are published as failed, by the contributor's record.
- Strict shares, recounted from the cards in `reading/` (sure words only; probable, restored and unresolved are holes; an unresolved stretch counted as one word, so the word shares are upper bounds; clear words of the letters not counted):

  | letter | sure / all units | strict word share | sure letters / decoded letters | contributor (sure + probable letters) |
  |---|---|---|---|---|
  | 196 | 32 / 65 | 49.2% | 119 / 333 = 35.7% | 64% |
  | 200 | 16 / 40 | 40.0% | 64 / 166 = 38.6% | 66% |
  | 202 | 5 / 20 | 25.0% | 27 / 130 = 20.8% | 52% |
  | 206 | 25 / 41 | 61.0% | 100 / 188 = 53.2% | 66% |
  | 211 | 23 / 51 | 45.1% | 96 / 272 = 35.3% | 53% |

  All five are far below the 95% bar: read in part at most, and with a key that is not validated the sure words are words the key gives, not a checked reading. `python docs/_check_reading.py rucellai1482`: clean share 0.473, the raw decodings "not a reading".
- Images: the ASF viewer and its IIP server answered on 14 Nov 2026 (`.../map/riproduzione/?id=79608`, 1272 x 1778 px). LXXII 207 recto, cipher lines 0-2 (about 120 signs) compared with `transcription/lxxii207.txt`: all agree except two doubtful shapes (the sign after `6` in L01, written P, has a barred descender; the two signs after `&` in L02, written c c). The five bare letters were not sampled.
- MAP LXXII 183 (issue #589, Andrew Aymeloglu; key sheet "Cifra con Paulantonio Soderini", used in 1494) against K_HP_v1, by the sign descriptions of the two key files only: shared values for two short strokes = a, pi = o, one short stroke = u, o with a lead-in stroke = e, the n sign (= / ÷); different for 9 (null here, r in 183), looped x (u here, x = m in 183), crossed b (s here, l in 183), B (null or a name here, *che* in 183), and the null pair H P has no counterpart in 183. The Medici chancery conventions are shared; it is not the same key. No other target holds these documents (`mazzinghi1478`, `toledo1479`, `mediceo1483`, `pandolfini1514/1515` are other systems or other documents).
- Catalogue: 2350 and 2323 stay (in progress, claimed from this folder).

## 14 Nov 2026 full-texts audit: 207

207 (the key pair) was a document without texts. Its files were in the folder and are now listed: `transcription/lxxii207.txt`, `decryption/lxxii207_v1.txt`, the word table `reading/lxxii207.md`, and the contemporary decipherment `transcription/lxxii208_clear.txt` under `contemporary`. Added: `reading/lxxii207_reading.md` (208 as sentences, with the decoded letters in brackets wherever the decode differs; no word of 208 changed) and `translation_207.md` (full English; `translation.md` had only a summary for 207). State `read`, read from the decipherment of the time; 114 of 119 words of 208 as typed, 5 uncertain there.

Three places where the decode gives better sense than 208 as typed, to look at on the image of 208: *fermo* / decode *fecene* (fece ne quelli segni), *{uscissimo}* / decode *uiscriueno* (che vi scrivemo), *valere* / decode *uedere* (vedere qualche garbuglio). Also *Crediamo che questa alteratione* / decode *credaamo per*: with *per* the sentence joins the one before (non si è sentito bene, crediamo per questa alteratione). Left as typed; the image was not opened in this session.
