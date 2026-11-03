# capilupi1545: Camillo Capilupi to Ferrante Gonzaga, catalogue 1565

Worked 3 Nov 2026 by WAINUT with AI language-model agents viewing the images. No human palaeographer has checked it.

| Document | Status | Cipher words | As sense (A) | No restored or changed letter (C) |
|---|---|---|---|---|
| cc. 15-16, 8 May 1545 | read in part | 293 | 233 (79.5%) | 214 (73.0%) |
| c. 48, 23 Feb 1546, Camillo to Ippolito | not read | digits transcribed, first pass | | |
| c. 49r, 28 Feb 1546 | not read | digits transcribed, first pass | | |

A = verbatim words plus words with a marked repair. C = verbatim only. Both leave out 26 doubtful words, 23 code words and 11 words of signs not read. The 95% bar is not met on either count. Clear words are not counted; an earlier 89% that included them was the wrong figure. The independent check before the fixes put the count at about 204 of about 301 (68%), an estimate. The recount above is by script after the fixes. Most of the rise comes from the sign corrections of pass 3, made on crops with the sense in view (below), so it is not a blind result. Counts are from `scripts/check_marks.py c15_16`; every repair and proposal is listed in `repairs_c15_16.md`.

Catalogue 1564 is untouched. Catalogue 1570 is in `targets/vittoria1686/`.

## Images

Estense IIIF, CC BY-NC-SA, linked and not committed. Manifests at `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest`:

- cc. 15-16: 13076923-8963-45b6-ae17-9b9752e6a22e
- c. 48: ce5fb6b7-0d6e-4d7b-9eb3-72f0caf1291d
- cc. 49-50: d2db1750-d22b-43c7-afee-9e0f02e6f389

Compared and rejected as keys: Ercole fonds cc. 88-92, 0229717b-2bf9-4850-b434-9a271b2dcd3b; Ippolito cc. 80a-80h, 9c9aab5c-5ed0-4533-a6a0-7b2022ec53c7.

## The letter of 8 May 1545

**Document.** Three pages. Clear Italian and cipher alternate inside sentences, with no word division in the cipher. The docket on c. 16v is in the clear. Read on a native-size crop it runs: M. Camillo Capilupo 8 di maggio in ziffera; Del Mar. del Vasto; Del Prin.e D'oria; Del matrimonio con Ottavio; Del vicere di Napoli per li Cavalli; Della persona di V. Ecc.a; Del p[ri]orato di Barletta; Il Car. d'Agosta desidera V. Ecc.a [...] contra li protestanti; Dell'Abbadia.

**System.** A homophonic alphabet of about 37 signs, plus:

- Nulls: any sign with a subscript 8 or 9 under it is cancelled. Scoring on Italian 4-grams per letter: no marks removed -8.52, only 8 -7.86, only 9 -7.94, both -7.47. A 9 written above the stroke sign is part of that sign (I9 = p).
- Double letters written as pseudo-words: bur tt, bor ss, bar rr, mur ll, and the pair F r for cc.
- Code words: sed, ima, ulir, Lus, Quan.
- Ordered null strings: runs of signs set in order, not text. L01 after Quan: e d h i l m n o r s t u then four signs. L24: a e i o u a e i. L11: a t e i o u. v06: u e o e t a a a i i i o o e. The sentence runs on across each one. Their order owes nothing to Italian, so they check the values.

Neither neighbour table fits. The 1556 table shares only 16 of 48 sign names and scores -14.8 per letter against -10.7 for this key on the same scale. The 1560 table is a dotted syllabary with a different sign set, so it could not be applied. c. 89r in the Ercole fonds is a 1556-type table with its clear on cc. 90-91; it is not a pair for any letter here. The independent check did not test these two misfits.

**Key.** `key.tsv`. Solved from the signs by homophonic annealing on Italian 4-grams with a letter-frequency penalty (`scripts/hsolve.py`), a break from ciphertext, not from a contemporary decipherment. Control on a synthetic 39-token homophonic of the same length: accuracy 1.0 with no noise, 0.92 at 8% noise, 0.22 at 15%. The rest was fixed by hand on the concordance (`scripts/conc.py`).

**Held-out test.** The annealer was trained on c. 15r only (508 letters) and frozen in `scripts/key_frozen_c15r.json`, then applied to cc. 15v-16r (685 letters). Result -7.435 per letter; 200 shuffled tables mean -10.168, best -9.326 (the check's rerun: mean -10.181, best -9.510). On the check's own scorer the frozen table gives -10.229 against shuffled tables -13.967 mean, -12.893 best, and scrambled sign order -12.824 mean, -12.283 best. The frozen table agrees with the final key on 33 of 43 signs and 87.7% of held-out tokens, so it tests the system and not every value. Limit: it was run after all pages had been read, so two shape rules and the code list were not blind. Without them, on raw pass 1, it still passes (-10.718 against -12.677 best scrambled). Four annealer runs with the sign order of c. 15r scrambled scored -12.24 to -12.63 on the held-out pages, against -10.229 for the real training.

**Independent blind check.** `VERIFY.md`, unchanged. An agent read 184 signs of c. 15v lines v01-v08 before opening any solver file: 10 differences, 5.4%. Of those, 7 were its own label failures (it used one label for q and g, and one for P and Fq), which leaves 3 of 184, 1.6%: one i against l inside a nulled sign at v02; a real solver error at v05, now fixed; and the last crossed sign of v08, where the transcription has V and the check saw a 4 with no raised 5. That last one is logged and not changed. Four new annealer seeds reproduced the frozen table 44 of 44. c. 15r, c. 15v from v09 and c. 16r had no line-by-line blind reader.

**Passes.** Pass 1 was made with no key. Pass 1b applied two logged shape rules. Pass 2 re-viewed about 40 lines on enlarged crops with the key in view (`pass2_changes.tsv`). Pass 3 (`pass3_changes.tsv`) applies the check's v05 correction and goes back to the image wherever the sense broke. Besides v05 it changed signs on 8 lines and clear text on 2. They are sign calls, but they were found by looking where the sense failed, and no blind reader has checked them:

- L12: the raised 9 stands over the stroke, with its tail sweeping left, as in r05. That stroke is I9 = p. There is no separate s, and the next sign is g. "il principe" now reads with no repair.
- L13: `n o` was one sign, K. The sign after X is blotted, with a B written above it as a correction. This gives "quali il m.". The sign n no longer exists.
- L20: the 9 belongs to F at the end of L19 and had been counted twice. "Farnese" reads with no repair.
- L07, L27, L29: signs read q are the hooked g. L23, L28: signs read q are P. L27: P is Fq. These give risponderli, imperadore, anchor, accomodava, accomodati, fussero. So "q stands for r or d" was a transcription fault in those places, not a second value.

**Corrections from the check: done.** v05 matrimonio. r04-r05 "{QUAN} [?d']Ago[s]ta desidera qui {IMA}", with one slip, r for s. The docket line "Il Car. d'Agosta desidera V. Ecc.a" gives both the phrase and {IMA} = V. Ecc.a at this place. Code words stay out of both counts. L20 "vi[e]n a la cort[e]". v17-v18 "di [g]uerra questo a[nn]o". v03 "si tratt[a]ra": the line starts tra, and the future tense follows the check. v11 clear "mi" restored. Docket gap: "vicere di Napoli" confirmed. The 19 repairs now carry marks. No correction on the check's list was found wrong on the image. One addition: the earlier passes had the start of L10 as uar; the crop has caua, so "ricer|cava" needs no repair. One disagreement stands at v08, above; it changes no word.

**Code words.** Context only unless stated.

- ima: Vostra Eccellenza, feminine agreement, fits every use; the docket line above confirms it at r05.
- sed: the Marchese del Vasto, by the docket heading and "il m. {SED}" at L13.
- ulir: the Emperor or His Majesty. Fits every use, but the Emperor is also spelled out, and the writer puts "ulir" in the clear at v14. Doubtful.
- Quan: very likely the Cardinal, at L01, r05 and the closing line. The clear line r10 has "parlai con Quan". Context only. At L11, L24, L26, v06, v12, v20, r04 and r07 it stands against a string and the sentence runs without it, so it may also be a decoy there.
- Lus: one use, not identified. Perhaps Luis de Avila; not proved.

**Five unordered strings count as not read:** L26 `ptcdi`, v12, v20 `aottundanobnasc`, r04 `datrsiloqrt`, r07 `qadqrot`. Nothing proves they are null, so they stay in the denominator as 8 words by length (45 letters). v12 looks like text: it reads "{QUAN} redeuto aer conto di cui deoe", so `aer` is printed as `[?aver]` and only `redeuto` stays unread. The tail of the L01 string, r04 and r07 were first called null by position alone.

## Historical context

From general histories, not checked in this run; please check before citing. The Diet met at Worms in spring 1545. Cardinal Alessandro Farnese came there as legate in May 1545 to treat of war against the Protestants, which fits "se Farnese non viene ben risoluto" and the "impresa di guerra". Ottavio Farnese's marriage to Margaret of Austria is the marriage in question. After the treaty of Crepy the question of the Duke of Orleans was open until his death in September 1545, which fits "le cose di monsignor d'Orliens". Ferrante Gonzaga and the Marchese del Vasto were rivals in Italy until Vasto's death in 1546.

## cc. 48 and 49r

Continuous digits inside clear Italian. `transcription_c48.txt`, `transcription_c49r.txt`, 641 digits in all, with blots and faded ink, one pass only. cc. 49v-50 were not worked. Tests in `scripts/digits.py`: no fixed pair grid; pair index of coincidence 0.0163 and 0.0145 in the two phases; 101 repeated 4-digit pairs against 25 in shuffled text (maximum 43). Groups of mixed length, or nulls, are likely. The solver stopped there and called the text too short for ciphertext-only work. **That "too short" judgement has no matched control**, so it is not a proved negative. The clear gives no crib longer than the context "ho parlato a". `reading_c48.md` holds the clear of c. 48r only.

## Prior art: open

Checked 3 Nov 2026. Three web searches by the solver (Capilupi cipher and Worms 1545; Capilupi, Truchsess, Farnese marriage; Chiesi on the Capilupi-Gonzaga correspondence) and one by the checker found no edition or decipherment of these letters. That does not clear them. Not seen: an essay by Lino Chiesi on the Capilupi-Gonzaga correspondence, cited in a paper on Ferrante Gonzaga and Julius III; one calendar entry "Camillo Capilupo, Mantuan Envoy with the Emperor", with no year in the snippet. Nothing here is claimed as new, and `first_break` is left out of the profile for that reason. This repository has no target folder for these letters at head 3c777efd5. `catalogue.json` lists entry 1565 as an open lead, with prior art open, so the line in `VERIFY.md` section 8 that it has no Capilupi is wrong. The mention in `gonzaga1590` is a different man (Giulio).

## Remaining gaps

- 26 doubtful words, listed with their signs in `repairs_c15_16.md`. Among them: L05 [?conosce], L09 [?sempre], [?fin] at L25, [?Idiaquez] (the last sign gives l, not z), [?Ispagna], [?d'accordo].
- K stands for o and also where u or v is needed (Mantoua, altroue, deue, uiene, qual-, uenirci). Two values, doubtful; those words stay marked. A homophone table might settle it.
- Z with a subscript 9 occurs five times. In three a g is wanted: before uerra at v18 and at v21, and in Ispa-na at r13. At L21 and L28 it stands where a null fits. If Z9 is a g rather than a null, [g]uerra and Ispagna need no repair. Not tested further.
- An open-ring sign at L23 and L29 (accor-o) is not settled: d fits L29, e fits L23.
- "mi" in the clear hand at v07 and v11 is not resolved. The docket order puts the viceroy of Naples at exactly this passage, so it may be an abbreviation for him. Context only.
- Word at L25 read [?fin]. Lus. Quan as a person against Quan as a decoy.
- 5 unordered strings, 8 words, above; 3 more words not read at L07 and L11.
- Blind second read of c. 15r, of c. 15v from v09, c. 16r, and of the pass 3 corrections.
- cc. 48 and 49r: not read; no matched control for "too short"; digits one pass. cc. 49v-50 not worked.
- The clear passages are a first transcription.
