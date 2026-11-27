# Matignon's Cipher-1, 1584: BnF fr. 15568 ff. 151r-152r (catalogue 2840) and fr. 15567 f. 24 (catalogue 2838)

Status: in progress. ff. 151r-152r are read in part (strict share 0.544). f. 24 is decoded, not read (0.409). The
siblings fr. 15567 f. 54 (decoded, not read, 0.530) and fr. 3255 f. 85 (already deciphered interlinearly in the
period) were tested on 17 Nov 2026 and fail the bar (see Remaining gaps). **No person has checked this work.** The
transcriptions, arbitrations, readings and reviews were made by Claude Opus 5.5 (Claude Code) for Brice Dudout.

**17 Nov 2026, after Daniel's review of PR #709:**
- **Interlinear glosses on f. 151r.** They are in letters, in a period hand, and were missed in the first pass. Over
  l. 1, "f∴soi" stands over Y s W 3h 7 (decoded *fesoi*, read {besoin}); the writer's f is confirmed. Over l. 3:
  - "…o[m]iacen" stands over c 3h 8 7 4 c e n (decoded *comiacen*);
  - a second gloss begins with the *que* sign "ꝗ", then r, c, …, a; it stands over Dp f c a 3 4 z M (decoded
    *que rcyuau t*);
  - "a ue" (Daniel reads "a ne") stands over 4 □.

  The glosses agree with the key wherever they can be compared. The one over □ suggests □ = *ue* or *ne*, giving
  "tient a[ue]c d'eux" (?) on f. 151r l. 3. This does not fit the other four occurrences of □ (f. 151r l. 17
  twice, f. 151v ll. 2, 13), so □ stays open in `key.tsv`. `plaintext.location` is now `interlinear`, partial.
- **read_share by the strict rule** (sure words only): 0.544 (377/693). Sure + probable + restored: 0.668, given once.
  23 "sure" words that differed from the decode (*lailer* -> laisser, *siuand* -> si quand, *paieste* -> majesté …)
  are now marked {probable} in `texts/reading_marked.txt` (`reading.md`, Strict counts).
- **Frozen key and measure scripts committed**: `holdout/key_frozen.tsv` (sha256 913f766d…461b, as in PREREG-B),
  `holdout/run_measure.sh`, `retest_C/run_measure_C.sh` and the SHA files of the four PREREGs. The scripts keep the
  absolute paths of the working folder (an external disk) in which they were run.
- **One key, one entry.** Tomokiyo places fr. 15567 ff. 24 and 54 and fr. 3255 f. 85 in this cipher, so f. 24
  (catalogue 2838) joins this folder: `f24/`. A third pre-registered single test was run there, on a new document,
  with `key.tsv` unchanged. Ll. 2-10 gave 387 labels, from two blind passes arbitrated on the image without a key.
  **Result: 294/385 = 76.4%; shuffled keys max 27.8%. The 0.85 bar is NOT met** (max + 0.30 is met). The result is
  the same as test 2 (76.7%), so on fresh text this key reaches about three quarters of signs in sense runs. The
  shortfall is not chance: shuffled keys reach at most 35%. It comes from unvalued signs and from transcription noise
  on similar shapes.
- Corrected: the letter of ff. 151-152 is **from** Matignon's side. The docket on f. 153 names him; the PR description
  had "to".

## Document
- BnF, Manuscrits, Français 15568 (Harlay 329 (8), 1584 April-December), ff. 151r, 151v, 152r; Gallica ark
  btv1b9063927n, view = folio + 8 (view 159 right = f. 151r, view 160 left = f. 151v, view 160 right = f. 152r,
  view 161 = f. 153, address). Source gallica.bnf.fr / BnF.
- Address/endorsement f. 153: "M. le mar[esch]al de Matignon … 1584" (month word doubtful, "juing"?). Writer side:
  Matignon (with Omont and Tomokiyo). f. 151r 33 cipher lines (a few interlinear glosses); f. 151v 30 lines;
  f. 152r 7 lines: 70 lines, 2 998 signs. No clear text. A contemporary decipherer glossed a few words of f. 151r ll. 1 and 3 between the lines. There is no decipherment on the neighbouring leaves (views 157-164).

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
- Reading (`reading.md`, `texts/reading_marked.txt`): first count sure 395, probable 61, restored 3, unresolved 230 of 689 words, 66.6% by sense; recounted 17 Nov
  (strict rule): sure 377, probable 84, restored 2, unresolved 230 of 693, strict 0.544 → **read in part**. ⊖ + # + read as *le roy de Navarre* (probable).

## Open
- Second, independent reader for the reading_review (current: contributor's own, grade B, preliminary).
- 6 p/m, ſ with filled loop (Pr), □, 4 with stem (q or u), the group + # +.

## Remaining gaps

- f. 151r-v: sign 6 reads p or m by context. Either it is a homophone or there are two shapes that we do not
  separate. Blocker: transcription. A shape atlas of 6 / 6^ from the full-size images is needed.
- f. 151r-v: Pr (ſ with a filled loop), □, 4 with a stem (q or u), and the group + # + (read *de Navarre*, probable).
  Blocker: no key material. The gloss over □ (f. 151r l. 3) gives *ue/ne*, but this does not fit □'s other
  occurrences.
- f. 151r ll. 1-4, 10-22 and f. 151v ll. 1-6, 10-27: 230 unresolved words. Blocker: transcription. Confusable shapes
  are 6/6^, ſt/ſ, ρ/ꝩ, e/ʒ.
- f. 24: ll. 1, 11 and 12 are pass 2 only. The glosses over ll. 3-8 are not transcribed. The clear paragraph and the
  facing address leaf are not transcribed. Blocker: not attempted.
- fr. 15567 f. 54 (Tomokiyo: same cipher; last line all nulls) and fr. 3255 f. 85 ("la renprynse de Perigueux",
  d'Aubeterre): single pre-registered measures on 17 Nov 2026 with key_D unchanged. f. 54r ll. 3-12, 432 signs:
  0.743 (200 controls: max 0.347), decoded, not read (strict share 0.530, 44/83). Tomokiyo built his table partly
  from f. 54, so this test is not fully independent. fr. 3255 f. 85r ll. 1-16, 456 signs: 0.450 (max 0.425). The
  leaf carries a period interlinear decipherment (existing), and it is in another hand with sign forms absent from
  the key. Blocker: no fresh portion is left. Files: `siblings/` (see "Sibling tests E1 and E2" below).

## Sibling tests E1 and E2 (17 Nov 2026)

Files in `siblings/`, in the layout of the working folder where they were frozen:
- `PREREG-E.md` (sha256 f5542ba2…93df, in `PREREG-E.sha256`): the two portions, chosen before any transcription.
- `transcription/E_pass1.txt`, `transcription/E_pass2.txt`: the two blind passes (both leaves in each file).
- `transcription/E1_portion_final.txt` (f. 54r ll. 3-12, 432 labels) and `transcription/E2_portion_final.txt`
  (f. 85r ll. 1-16, 456 labels): arbitrated on the image without a key; the rules are at the head of each file.
- `PREREG-E2.md` (sha256 dcc633d7…b8de, in `PREREG-E2.sha256`): freezes the key, the scripts, the two passes and the
  two arbitrated portions before any decoding. In it, `../key_D.tsv` is `key.tsv` here (same sha256 eb00fd85…3404,
  also `f24/test_D/key_D.tsv`), and `../scripts/decode.py` is `scripts/decode.py` (9206a6a0…).
- `scripts/run_measure_E.sh`: the single run (E1, then E2). It keeps the absolute paths of the working folder.
- `mesure/E1_decoded.txt`, `mesure/E2_decoded.txt`: decoder output. `mesure/RESULTAT_E1.txt`, `mesure/RESULTAT_E2.txt`:
  raw output of `measure.py` (321/432 = 74.3%, max shuffled 34.7%; 205/456 = 45.0%, max shuffled 42.5%).
- `lecture/E1_reading_marked.txt`: the word-level reading of E1, made after the test (strict 44/83 = 0.530).

To check: the sha256 of the two PREREG files against the hashes above; the hash lines of `PREREG-E2.md` against the
files, with the two renames above; `python3 scripts/decode.py key.tsv siblings/transcription/E1_portion_final.txt`
gives `siblings/mesure/E1_decoded.txt` byte for byte (the same for E2); `measure.py` on the decoded files gives the
RESULTAT figures. Freeze order on the working disk (file times, CET; they are not proof): PREREG-E 13:21; passes 13:36
and 13:46; arbitrated portions 13:59:11; PREREG-E2 13:59:26; decoded files and RESULTAT 13:59:34-39. The f. 85
interlinear decipherment is recorded as that leaf's plaintext in `profile.json`. It is not transcribed here.

## Escalation

- [x] known-keys: Tomokiyo's Matignon's Cipher-1 table applied and extended. It is a different cipher from the
  Mayenne-Forget Cipher-1 (`matignon1586`), Matignon's Cipher-3 (`matignon1586c3`) and the tuple cipher
  (`matignon1586tuple`).
- [x] clear-pages: interlinear glosses on f. 151r ll. 1, 3 and f. 24 l. 1 used as checks. There is no decipherment on
  the neighbouring leaves (fr. 15568 views 157-164).
- [x] print: no printed decipherment found; Tomokiyo gives no reading.
- [x] siblings: fr. 15567 f. 54 and fr. 3255 f. 85 transcribed (two blind passes, arbitrated) and measured on 17 Nov
  2026: 0.743 and 0.450, both below 0.85.
- [x] retry: five single pre-registered tests, with three key files. A (0.876, passed) used
  `holdout/key_frozen.tsv`. C (0.767) used `retest_C/key_C.tsv`, corrected on the development lines after A. D (0.764,
  f. 24), E1 (0.743, f. 54) and E2 (0.450, f. 85) used `key_D.tsv` = `key.tsv` (= key_C + 6 = p). C, D, E1 and E2
  are re-tests after development changes. All four are below 0.85; C and D are above max + 0.30.
- [ ] second reader: no independent person has checked the transcription or the reading.

## Credits
Key: Satoshi Tomokiyo (cryptiana, "French ciphers during the Reigns of Charles IX and Henry III", Matignon's
Cipher-1 table). Images: Source gallica.bnf.fr / BnF. Transcription, extension and test: Brice Dudout with
Claude Opus 5.5 (Claude Code), 16 Nov 2026.
