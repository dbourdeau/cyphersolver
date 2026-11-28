# LJS 51 ff. 37v-38v: the qalam qummī and the "Pahlavi" key verse (chain 37v.12)

Images: University of Pennsylvania, LJS 51, OPenn (Penn IIIF, 2343 px, PDM 1.0).
Built on Daniel Bourdeau's transcription and by-eye key of 37v.12 (`../../keys_eye/37v.12.json`, commit 44d521b44a)
and on his `../../prior_art_2.md`.

## 1. 38v l.4 and l.6 are key verses, not alphabets of signs

The compiler writes that "the Qummī pen is not the Pahlavi". He gives the Pahlavi (l.4) and then the Qummī (l.6),
and adds that "the ẓāʾ fell out of it, the ḍād stands in for it". Both lines are in ordinary Arabic letters
(`ALPHABETS-38v.md`, three passes, frozen before any comparison).

- **l.6 = the mnemonic verse of the qalam qummī.** It is a reciprocal swap of letter pairs. al-Qalqashandī quotes it from Ibn al-Durayhim
  (*Ṣubḥ al-aʿshā* 9:230, OpenITI Shamela0009429): «كم أو حط صلا له در سع في بز خش غض ثج تدفق». Each letter in this verse is
  followed by its partner. Qalqashandī gives examples: محمد = كطكر, علي = سهف. The LJS copy reads
  كمر او حيط صلاله در سع تي برخش غض ثج تذ ق, the same verse with copying slips. Pairs: ك م, ا و, ح ط, ل ه, د ر, س ع,
  ف ي, ب ز, خ ش, غ ض, ث ج, ت ذ, ن ق (uncertain). ص stays alone because its partner ظ has dropped out.
- **l.4 = another pair verse**, which the compiler calls the "Pahlavi". Read in successive pairs it gives قد ضج زح وش كا ثه مذ سخ طت غص نع لي:
  12 disjoint pairs covering 24 distinct letters. A random string of 24 letters would have all of them distinct with p ≈ 2.4 × 10⁻⁷.
  The tail «لا اقط» is not resolved. Mrayati's analysis of the *Miftāḥ* (vol. 1 p. 163, cited in prior_art_2.md)
  names "a verse key such as قد ضج زح…" among the fixed substitutions.
- Both keys are prior art (EXISTING). LJS 51 adds the two verses side by side, the name "Pahlavi" for the second one,
  and the remark on ẓāʾ.
- *Shawq al-mustahām* (Hammer 1806) has neither a Pahlavi nor a Qummī alphabet.

## 2. Test c2: the published qummī key on the cant (frozen; hash on #1023 before measuring)

`verification/PREREG_c2.json` and `MANIFEST_c2_v1.sha256` (dd9d0f46…). The test applied the 13-pair key as published, with
no tuning, to the 90 cant letters (Daniel's corrected plaintext), against 200 random pair-swaps.

| | log-likelihood (4-gram) | words in lexicon |
|---|---|---|
| qummī key | **−309.4** (rank 1/200) | **0.48** (rank 1/200) |
| best of 200 controls | −387.4 | 0.30 |
| mean of controls | −502.4 | 0.08 |

**Verdict under the frozen criterion: FAIL**, because the lexicon share of 0.48 is below the 0.70 threshold. The protocol foresaw this case: the
decoded text may be the Sasanian cant itself rather than plain Arabic. The decoded text is:

دمخت بالخاجاه ليله عبوا دلقي / وضاع ييس حشيشي وزضدوا علقي / واضحيت قيري مزفت ضاق با خلقي / لا شي اكش ولا ازفت ولا القي

Read after the measurement, descriptive only:
- The four hemistichs now rhyme in **-لقي** (دلقي، علقي، خلقي، القي). The rhyme of the qummī text was -هنف.
- Arabic words appear: ليله, وضاع, حشيشي, ضاق, خلقي, لا شي, ولا.
- The compiler's word list after «هذا باللغة الساسانية» (38r l.12-38v l.2) contains **اكش** next to اكل ("to eat"). اكش is a
  word of the decoded verse. It also has دمخنث, close to the decoded first word دمخت, and عبواسر, close to عبوا.

So the cant as the compiler wrote it on 38r appears still to be in qummī letters. The key turns it into Sasanian cant
mixed with Arabic. The words cannot be checked for sense without a glossary such as Bosworth 1976, which we could not consult.

## 3. Test c: free substitution (frozen, MANIFEST_c_v1.sha256 fdd8c85b…)

Simulated annealing of a free simple substitution on the same 90 letters, using the 4-gram model of al-Ḥillī and Ibn Nubāta, against 200 shuffled controls run with the same budget.

| | log-likelihood | words in lexicon |
|---|---|---|
| cant | **−258.9** (rank 1/200, z = 3.8) | 0.52 |
| best control | −263.7 | 0.65 |

**Verdict: FAIL.** The lexicon share is below the best control and below 0.70.

The anneal was never shown the qummī key, yet it found ا↔و, ف→ي and ه→ل on its own. These are the qummī pairs of the most frequent letters. Its decoding agrees with the c2 decoding on 46 of 90 letters (51 %) and shows the same «لا … ولا … ولا» frame (`verification/POST_c_vs_c2.txt`, written after the measurement). This is independent support for the qummī layer, not a validation. The ten fixed tables built by reading l.4 and l.6 as ordered alphabets score ≤ 0.09 on the lexicon: the pair reading is the right one.

The manifests list the files under the local folder layout (`gel/`, `transcriptions/`, `donnees/`, `scripts/`). Here they sit under `verification/` with the same contents and hashes.

## 3b. Test c3: the "Pahlavi" key of l.4 as a named negative control (frozen, `verification/c3/MANIFEST_c3_v1.sha256` 08eb2021…, posted on #1023 at 19:45:37Z)

- Same 4-gram model, same lexicon and the same 200 random involutions as c2 (seed 20261129; the run checks that the qummī figures and the control maxima equal c2's: they do).
- Decided before freezing: the frozen l.4 reads ضح, not ضج, so ح sits in two pairs. Three reciprocal readings are tested (emended ضج; frozen ضح with زح dropped; frozen زح with ضح dropped) and the criterion uses the best one. The tail «لا اقط» is left out of the key (its letters are all already paired); uncovered letters stay unchanged.
- Prediction: best Pahlavi log-likelihood ≤ qummī − 39.0 (half the c2 gap to the best control) AND lexicon share ≤ qummī − 0.20 (≤ 6 of 23 words).
- Result (one run, 2026-11-28T19:46:18Z, `verification/c3/RESULT_c3.json`): best Pahlavi LL −547.1 (rank 160/200, below the undecoded cant at −450.0), 0/23 words in the lexicon, no glossary word. qummī: −309.4, 11/23, اكش. **Prediction confirmed.** A key of the same type from the same page does not produce the c2 signal.
- Lexicon words under the qummī key (point 4 of the review): ليله وضاع ييس ضاق با خلقي لا شي ولا ولا القي; content words only: 6 of 18.
- Descriptive, after the run: attestation of the 23 decoded forms in *Lisān al-ʿArab* and *Tāj al-ʿarūs* (OpenITI), `verification/c3/ARGOT-ATTESTATIONS-c2.md`. اكش occurs in neither, which fits a cant word that the compiler glosses اكل. A form attested in Arabic says nothing of its sense in the cant.

## 4. The verses in print

None of the 23 cant words occurs in Abū Dulaf's *Sāsāniyya* as al-Thaʿālibī quotes it in the *Yatīma*, whether in
qummī letters or decoded. The only shared words are common Arabic ones: ضاق, لا, ولا. No run of four words matches, so the
verses are not identified. al-Ḥillī's *Sāsāniyya* is absent from both OpenITI versions of his dīwān. Bosworth, *The Mediaeval Islamic
Underworld* II (1976), was not available.

## Files

`ALPHABETS-38v.md` (frozen transcription), `ANALYSE-l4-l6.md`, `verification/` (protocols, manifests, results, scripts).
