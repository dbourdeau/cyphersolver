# Philip to Ferrante Gonzaga, 25 Jun 1546, 14 Mar 1553 and the letter catalogued 16 Jun 1563 (catalogue 1561): a double-blind transcription and one pre-registered test

Status: in progress (14 Mar 1553: key confirmed on a held-out portion, read in part, 333 of 550 words sure, 60.5%; 25 Jun 1546 and the letter catalogued 1563: decoded, not read, the pre-registered test failed). Next step: a sign-level reading of 1553 against the images, and a better pre-registered test for the other two.

Brice Dudout, with Claude (AI agents), 27 Nov 2026. Builds on WAINUT's work in `../wainut/` and on Andrew Beling's in `../beling_march1553/`.

## What was done

1. **Two blind shape transcriptions per letter, then an arbitration.** Each letter was transcribed by two separate agents, A and B. They had no key, no values and no clear text. They named the signs from the project's atlas of this cipher (`sign_table` names such as `x-curl-1dot`, `six-o`, `Lambda-bar`), shown on plates cut from the 14 Nov 1549 letter, with their values removed. Signs outside the atlas were written `?description`. A third agent settled every place where A and B differed by looking at the images, again without a key. It also kept a closed list of the `?` classes it used.
   - Agreement between A and B before arbitration: 1546, 0.892 of 546 places; 1553, 0.765 of 1,402; "1563", 0.712 of 893. The "1563" leaves have heavy ink bleed-through.
   - The files are in `blind/` (A and B), `arb/*_DIFF.tsv`, `arb/*_PRE.txt`, `arb/*_ARB.txt` and `arb/*_GLOSSAIRE.md`. The reader and arbiter instructions are `CONSIGNE-AVEUGLE.md` and `CONSIGNE-ARBITRAGE.md`, in French. All of these are frozen by SHA-256: `FREEZE-*.sha256`.
   - Lines: 1546 has 23 lines (c. 5r L01-L19, c. 5v L01-L04). 1553 has 64 lines (c. 35r 15, c. 35v 18, c. 40r 23, c. 40v 8), the same as WAINUT's B01-B64. "1563" has 30 lines (c. 24r 15, c. 24v 15). WAINUT counted 44 there; the difference comes from bleed-through rows.
2. **Key.** WAINUT's `../wainut/key.tsv` was used unchanged (SHA-256 `47a2b2f3…`). Atlas names were linked to WAINUT's names through `CROSSWALK-C09.tsv`. That table was frozen before any transcription was read. It was built from how often each pair of names falls on the same aligned place in the 14 Nov 1549 letter (`compare_readings.py`; counts in `cooc_14nov1549_atlas_vs_wainut.json`), using a rule of at least 0.6, plus 7 listed manual rows. The `?` classes, `#`, and names not in the table are left as holes. A sign with dots below counts as cancelled, which is WAINUT's own rule.
3. **Pre-registration: `PREREG-C09.md`.** It was hashed before any decoding (`PREREG-C09.sha256`, `e2500565…`).
   - Held-out portion: paragraphs 4-6 of 1553 (c. 40r L08-L23 and c. 40v), scored against the matching three paragraphs of the Spanish enclosure cc. 37r-38r. The enclosure transcription is Beling's, split into paragraphs exactly as in his `calibrate.py`. These 865 letters are the same hold-out he used.
   - Metric: Levenshtein edits, with Beling's normalisation.
   - Controls: 1,000 shuffled keys, plus 1,000 shuffles of the order of the decoded tokens with the real key.
   - Threshold: no tie and no win in either control family.
   - For 1546 and "1563", which have no clear: the share of decoded letters covered by Spanish words of 4 or more letters, against the same two control families.
4. **One measurement only: `MESURE-C09.json`.** The scripts are `mesure_c09.py`, frozen, and the decodes `decode_*.txt`. To rerun from this folder (deterministic, standard library): `python3 -I mesure_c09.py .. .`, then `python3 -I lecture_1553.py .. .`

## Results

| letter | measure | real | key shuffles (best) | order shuffles (best) | ties or wins | pre-registered verdict |
|---|---|---|---|---|---|---|
| 14 Mar 1553, held-out ¶4-6 | edits / 865 letters | **176 (CER 0.204)** | 661 | 608 | 0 / 0 | **key confirmed** |
| 14 Mar 1553, ¶1-3 (secondary) | edits / 1,476 | 289 (CER 0.196) | | | | |
| 25 Jun 1546 | lexicon cover | 0.321 | 0.502 | 0.124 | 54 / 0 | failed |
| catalogued 16 Jun 1563 | lexicon cover | 0.222 | 0.438 | 0.092 | 188 / 0 | failed |

- **1553.** On the same 865 held-out letters and with the same key, WAINUT's single blind pass needed 621 edits (Beling's figure, `../beling_march1553/paragraphs.tsv`), and Beling's fitted table needed 487. The double-blind transcription needs 176. The key is unchanged; the gain comes from the transcription.
  - It also shows that the Spanish sheets cc. 37r-38r follow the cipher passages almost letter for letter: the residual 20% is mostly our sign errors and holes. Beling left open whether they are a draft, an extract or a decipherment. They are at least a full clear text of these six passages.
- **1546 and "1563".** Both failed the pre-registered test, so both stay **decoded, not read**. The failure is the metric's: the coverage score of shuffled keys reaches 0.50. Shuffles that move the long code values of key.tsv (`sumagestad`, `franceses`, `reydefrancia`, `embaxador`) onto frequent signs create many dictionary words. The order-shuffle family is beaten with no tie, but by the pre-registered rule both families had to be beaten.
  - In the unrepaired decodes, some runs can be seen without being read: in 1546 `artilleria`, `Nauarra`, `Lombardia dos mil infantes`, `galeras … de Sicilia`; in "1563" `Embaxador Figueroa`, `don Antonio de Biuero`, `ciento y cinquenta mil`. WAINUT's datings stand: the "1563" letter is earlier than January 1556.

## Reading of 1553 (read in part)

`reading_1553.md` gives the six passages, and `translation_1553_en.md` gives them in English. The word classes follow the project's rule:
- A word is **sure** when the letters decoded from the signs give it, with only the project's spelling fold (`compare_readings.py` norm). It is written in the cipher's own spelling.
- Every other word is **[restored]** from the enclosure and never counted as sure.
- No word is {probable}: no value was supplied from sense.
- No word is ‹unresolved›: the enclosure covers every passage.

The count is made by `lecture_1553.py` (output `lecture_1553_auto.txt`): **333 of 550 words sure (60.5%), 1,085 letters.** That is below the 95% read bar, so the 1553 letter is **read in part**.

## Hostile reading (our own)

- **The "sure" words of 1553 depend on the enclosure for word division.** Their letters come from the signs, but the alignment that cuts them into words was made with the clear text. The match was made after the measurement. A count made from the signs alone against the images, without the enclosure, has not been done.
- **The enclosure confirms only what it covers.** Where the cipher and the enclosure differ in wording (¶1 `hauer des rematido` against `havernos remitido`), our count calls the word restored, although the cipher may simply differ there.
- **The crosswalk depends on values indirectly.** It comes from the 14 Nov 1549 alignment, which pairs places by value similarity. It uses nothing from the three letters, but it is not a pure shape crosswalk.
- **The readers were not fully independent of each other's conventions.** The instructions for 1553 and "1563" named some habits of this hand (ſ = `S`, ∂ = `theta`, `xo|x-stroke-o`), taken from reader B's 1546 report. Arbitration was done by one agent per letter, and no person checked it.
- **The test for 1546 and "1563" was badly designed.** The two failures are reported as failures. No second measurement was run: a better metric would need a new pre-registration.
- **The line cutting may be wrong in places.** 1546 and 1553 were cut by projection. "1563" was cut at fixed peaks, with one manual fix (c. 24v L13-L15), so lines may be missing among the bleed-through. Only 30 lines were found there against WAINUT's 44.
- **Prior art.** WAINUT transcribed and decoded all three letters first, and found the dating of "1563". Beling identified the enclosure. Neither the key nor the enclosure is ours. What is ours here is the transcription, the crosswalk and the test.

## Can catalogue 1561 be closed?

**No.**
- 1553 is read in part (60.5% sure).
- 1546 and "1563" are decoded, not read: their pre-registered test failed.

The entry can move from "decoded, not read" to "read in part" for 14 Mar 1553 only.

## Credits

- **WAINUT (GitHub LcCompany):** key.tsv (the table of the Imperial Cipher of 1544-1554 recovered from the contemporary decipherments of Philip's letters), the first transcription and decoding of these three letters, and the dating of the letter catalogued 1563 (addressed to Ferrante, who died in 1557, so before January 1556).
- **Andrew Beling, with AI agents:** the identification of the Spanish enclosure cc. 37r-38r, its transcription and paragraph split, the scoring code, and the baseline of 621 edits reused here.
- **The project (Daniel Bourdeau):** the sign atlas and sign names of the 14 Nov 1549 letter, and `compare_readings.py`.
- **Satoshi Tomokiyo and María José Bertomeu Masiá** for the published key of this cipher, as credited in `../NOTES.md`.
- **Brice Dudout, with Claude (AI agents):** the double-blind transcriptions and arbitration, the crosswalk, the pre-registration and the measurement, and the 1553 reading.

Images: Biblioteca Estense Universitaria, Modena (Lodovico Media Library, CC BY-NC-SA). None is included here.

AI agents did this work. Brice Dudout has not yet checked the readings against the images.
