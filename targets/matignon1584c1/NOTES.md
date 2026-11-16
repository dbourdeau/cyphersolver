# Matignon's Cipher-1, 1584 — BnF fr. 15568 ff. 151r-152r (catalogue 2840) 

**State: read in part.** Tomokiyo's table ("Matignon's Cipher-1", cryptiana `henryiii.htm`, reconstructed from
fr. 15567 ff. 24, 54) was applied to the letter of fr. 15568 ff. 151r-152r, extended on f. 151r (development
portion) and then tested **once** on a held-out portion it had never seen: f. 152r (seven lines) plus the last
line of f. 151v, 302 signs.

## Document
- BnF, Manuscrits, Français 15568 (Harlay 329 (8), 1584 April-December), ff. 151r, 151v, 152r; Gallica ark
  btv1b9063927n, view = folio + 8 (view 159 right = f. 151r, view 160 left = f. 151v, view 160 right = f. 152r,
  view 161 = f. 153, address). Source gallica.bnf.fr / BnF.
- Address/endorsement f. 153: "M. le mar[esch]al de Matignon … 1584" (month word doubtful, "juing"?). Writer side:
  Matignon (with Omont and Tomokiyo). f. 151r 33 cipher lines (a few interlinear glosses); f. 151v 30 lines;
  f. 152r 7 lines: 70 lines, 2 998 signs. No clear text, no contemporary decipherment on the neighbouring leaves (views 157-164).

## Key
`key.tsv`: Tomokiyo's table plus values set on f. 151r: double long s (ſſ) = t, 6 with a cap = m/p, ρ-like sign = b,
g-with-tail (ℊʒ) = z (ilz), diamond with long tail = *que*, barred theta (⊖) = *le roy* (Tomokiyo's code sign),
4 with long stem = q (development guess; the held-out text suggests u/v instead), ≋ and // null.
Open: ſ with a filled loop (2 tokens in the portion), the group "+tt" after ⊖ (probably a code, *de Navarre*?).
Observed after the test (not in the frozen key): two shapes of 6 (p and m) and two of Y (f and a looped b-form).

## Test (pre-registered, single run, 16 Nov 2026)
- Held-out portion chosen and frozen (SHA-256) before any transcription; transcribed twice from differently cut
  crops, 4 disagreements settled on the image; key frozen (SHA-256) before decoding it.
- Statistic: Daniel's sense-run rule (`targets/matignon1586c3/f276/scripts/measure.py`, fr-1600-letters, mincount 20).
- **Result: 262 of 299 signs (87.6%) read in sense runs; 200 shuffled keys: median 3.3%, max 32.1%.**
  Thresholds fixed beforehand: ≥ 0.85 and ≥ max control + 0.30 (0.621): both met.

## Reading of the held-out portion (word level, after the test)
Sure 38, probable 13, restored 2, unresolved 19 of 72 words: 71% by sense → *read in part*. See
`reading_holdout.md`. Gist: the King of Navarre(?) said the King allowed him to build at the Boucau (mouth of the
Adour below Bayonne); the inhabitants of Bayonne; "soubz peine"; "faisant semblant"; "empeschement".

## Whole letter (second stage, 16 Nov 2026)
- Every line of ff. 151r-v transcribed in two independent passes (blind sub-agents for f. 151r both passes, f. 151v
  ll. 16-29 pass 1 and f. 151v pass 2; brief in `texts/BRIEF-transcripteurs.md`). Agreement before arbitration 88.6-88.8%.
- New held-out portion C = f. 151v ll. 1-9 (377 signs), chosen before transcription (`retest_C/PREREG-C-portion.md`),
  arbitrated on the image without a key (`retest_C/holdout_C_final.txt`). Development lines (rest of ff. 151r-v)
  arbitrated by sense (`scripts/arb_dev.py`, lexical coverage, ties to pass 1).
- Key corrected on development only, then frozen (`retest_C/PREREG-C2-gel.md`, `retest_C/key_C.tsv`):
  6^ = p, ω = l, λ = l, circled sign = o, # = a, small ð with crossed tail = s, A/✱ = a, Δ = b, ƶ = i, τ = d.
- **Single re-test: 287/374 = 76.7%; shuffled keys median 2.7%, max 34.5%. Bar 0.85 NOT met** (max + 0.30 met).
  Clerical slip: sign 6 lost its value in `key_C.tsv`; post-hoc non-probative rerun with 6 = p: 73.0%.
- `key.tsv` = key_C + 6 = p, used for the reading. Plain 6 reads p or m by context (prendre, province / me semble,
  mande, maison, Majesté): an unresolved homophone or two shapes we do not separate.
- Reading (`reading.md`, `texts/reading_marked.txt`): sure 395, probable 61, restored 3, unresolved 230 of 689 words,
  66.6% by sense → **read in part**. ⊖ + # + read as *le roy de Navarre* (probable).

## Open
- Second, independent reader for the reading_review (current: contributor's own, grade B, preliminary).
- 6 p/m, ſ with filled loop (Pr), □, 4 with stem (q or u), the group + # +.

## Credits
Key: Satoshi Tomokiyo (cryptiana, "French ciphers during the Reigns of Charles IX and Henry III", Matignon's
Cipher-1 table). Images: Source gallica.bnf.fr / BnF. Transcription, extension and test: Brice Dudout with
Claude Opus 5.5 (Claude Code), 16 Nov 2026.
