# Source-based review by a separate AI agent — Eckert selected readings

12 November 2026. Reviewer: separate reconciliation agent, with the proposed readings and printed parallels already visible. **This is not a blind decode or an independent key-discovery test.** I read the three reports, key extraction and decoder, reran the decoder, and visually checked the twenty local images enumerated below. I did not modify the reports, key, downloaded JSON or original images.

**Result:** the sampled source evidence supports the message-specific Book No. 2 reading of U1 and McPhail, and the four Book No. 1 substitutions in U2. The Johnston/Beauregard discrepancy is real in these witnesses. The time-table distinction is also real. No major contradictory key entry was found in this sample. This is not an audit of every entry in the partial extraction or every ordinary-English word.

## Verified source observations

| Question | Image observation and assessment |
|---|---|
| U1 Book No. 2 | The p4 second telegram contains Nestor, Midas, patenting, World, Salem, quickened, Jaunts, Peru, Wiley, Lady and Tobsy in the reported sequence. Book2 p19 directly gives Nestor/Sedgwick, Patent/Advance with the ed/ing instruction, and Peru/Army; p18 gives Midas/Kelly B.F. and Lady/H.W. Halleck; p20 gives Quicken/Detach with the suffix rule; p21 Salem/Force; p25 World/West. These independently support the core reading rather than merely matching the printed English. |
| U1 time | Book2 p1 has **Topsy = 12:30** in the P.M. column, with Viola = 12 Midnight underneath. The ledger form is Tobsy. OR I/33 p486 heads the matching telegram 12:30 p.m. on 1 February 1864. The spelling normalization should stay explicit. |
| Contrasting Book1 time | Book1 time image gives **Topsy = 12 Midnight**, Emily = 10 A.M., and Imogene = 3 P.M. Book2 instead has Imogene = 3:30 P.M. The Book2 Imogene reading agrees with the handwritten 3:30 P.M. heading on ledger p10. This is a useful warning against transferring a common code word across books. |
| U2 | Source p6 lower heading bears Beckwith and 1. The four selected mappings are directly present: Grapes/Washington on Book1 p14; Paradise/Colonel on p19; Plaster/5 on numerals; Emily/10 A.M. on the time page. The body is ordinary English. Keeping unity and the post-signature wording outside the readable message is appropriately cautious. |
| Java versus Ink | In **both** mssEC47 p17 and mssEC48 p17, Java is on the Johnston row; Ink is on the separate Beauregard row near the top. Ledger p9 has Java after Stephen and earlier has Ink Morgan Zebra. OR I/33 p559 prints Beauregard at both corresponding positions. Preserve the discrepancy; the sampled evidence does not establish which participant or editor caused it or whose troop count was historically accurate. |
| Hanover Junction | Ledger p9 ends with Cushing / Snyder Star at Cider Sulphur. Book2 numerals gives Cushing/7 and Snyder/Hundred; p22 gives Star/Infantry and Sulphur/Junction. Thus the ledger supports 700 infantry. Printed OR p559 instead has 780 Maryland Line. There is no visible extra eighty or Maryland-Line code group here. |
| Other numbers | The checked Book2 numeral table supports the construction of the reported 35,000, 46,000, 1,700 and 1,600 quantities from the constituent tokens. Alton = 1 is clear in the key; the source word represented as Allen on p9 is not silently repaired by the decoder. |
| Explicit transcript corrections | Source p9 address reads Snake **Peru** Talbot Argus, supporting the reported Pine→Peru correction. Source p10 second telegram clearly has **For Grant Tulip**, supporting restoration of Grant omitted in volunteer JSON. |
| Forage | Book2 p21 directly gives Rusty/Forage. The ledger p10 initial in the final supplies word remains sufficiently R/D-like that retaining Dusty in the literal and marking Rusty/forage as a proposed source repair is preferable to silently making Dusty a new dictionary entry. OR p559 independently prints forage. |
| Marine Brigade name | Ledger p10 has a plain **Elliotts**-like name after Spark. It should remain a manuscript spelling, not be numerically decoded and not silently rewritten to Ellet. The coordinator reports that the matching printed/indexed OR witness has Ellet’s. These are distinct witness readings. |

The upper McPhail source and printed version also differ in the unit/name near 120 men and in the explicit Hoke name. The report already handles these conservatively. A printed parallel is evidence of a related text, not a mandate to repair the cipher into identical wording.

## Required documentary update

At review time `McPhail_reading.md` still says no relevant prior-publication search has been completed for the second p10 telegram. The coordinator has since located the matching text in the indexed reproduction of **OR series I, volume XXXII, part II, p407**, and reports the variants “by the Government,” “General Ellet’s,” and “General Sherman.” That stale negative-search statement should be replaced by the positive indexed match, retaining the distinction between the manuscript’s Elliotts and the indexed Ellet’s.

**Verification boundary:** I visually checked the local primary print scans of OR I/33 pp486 and559. I have **not** visually checked an original print scan of OR I/32 part II p407. The p407 match and its exact variants above are coordinator-reported indexed-text evidence, not an independent visual certification in this review. A limited search during review did not supply a convenient p407 scan. The existing primary-source verification should not be overstated to cover that new item.

## Decoder audit and reproducibility

Ran from the repository root:

```sh
python3 -I output/eckert_book2_2026-11-12/decode_selected.py
```

Result: **112 selected key entries; 175 substitutions**. Both generated outputs were byte-identical to their pre-run contents:

| Output | SHA-256 |
|---|---|
| literal_selected.txt | `0d214e4e2deb069e824c12e7a9a69d6ce4f5e455246e06141a4b639d1a384522` |
| applied_key_ledger.tsv | `86ce3938ba52215718ea93454fe39a974f8655d95798bc75c53f6e826cfc551f` |

The code uses exact case-insensitive lexical matches plus an explicit small derived-form list. It preserves unmatched words and records the applied key page. It explicitly restores Peru and Grant only in the loaded working text, leaving downloaded JSON untouched. It does not implement route reversal, numerical expression arithmetic, or a complete grammatical reconstruction. U2 is a manually checked four-entry application and is not generated by this No. 2 script.

One maintenance caveat: the module docstring describes occurrence exclusions for the post-signature null tail, but the present implementation only has explicit heading/Baldwin exclusions. The U1 tail currently remains unchanged because those words are absent from the **partial** key. Book2 p19 actually has Nasty as a Stoneman code. If the key extraction is enlarged, explicit tail boundaries will be needed to avoid a spurious substitution there. This does **not** invalidate the current output; it limits reuse of this decoder with an expanded key. No change was made during review.

## Exact image sample

All filenames below are in `sources/raw/english_conflict_survey_2026-11-12/`; associated source URLs/manifests and original hashes remain in that directory.

- Manuscripts: `eckert19_p4.jpg`, `eckert19_p6.jpg`, `eckert19_p9.jpg`, `eckert19_p10.jpg`.
- Printed parallels: `or33_p486.jpg`, `or33_p559.jpg`.
- Book No. 1: `book1_time.jpg`, `book1_p14.jpg`, `book1_p19.jpg`, `book1_numerals.jpg`.
- Book No. 2: `book2_p1.jpg`, `book2_p17.jpg`, `book2_copy48_p17.jpg`, `book2_p18.jpg`, `book2_p19.jpg`, `book2_p20.jpg`, `book2_p21.jpg`, `book2_p22.jpg`, `book2_p25.jpg`, `book2_backrecto.jpg`.

The sample verifies the central identification, sensitive variants, key-dependent time readings, morphological rule, and numeral construction. It does not establish first-publication novelty, validate intelligence estimates as historical fact, or show that every amendment in the extant books was already present on the telegram dates.
