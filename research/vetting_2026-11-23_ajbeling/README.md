# Vetting, Andrew Beling (2026-11-23)

Run by Andrew Beling (ajbeling) with AI agents (Claude Opus 5.5 and two helper agents for the blind transcriptions).

## Lead 892: partly_read (corrections to the block of 29 Oct 2026)

Ferdinand I and his resident at the Porte, Giovanni Maria Malvezzi, 1550: HHStA Wien, StAbt Türkei I 8-2-22,
8-2-24, 8-3-10, 8-3-12 and 9-1-2.

- **Languages.** Three of the five items are Latin: Ferdinand's letters 8-2-24, 8-3-12 and 9-1-2. Malvezzi's
  8-2-22 and 8-3-10 are Italian. The lead says Italian for all five.
- **Decipherments of the 19th century.** Two items have one filed with them in the archive, both headed
  "Entzifferung":
  - 8-3-12 (Brno, 28 April 1550): AIS images 5-6, the whole ciphered text.
  - 9-1-2 (Augsburg, 3 October 1550): image 3, the ciphered passage.
- **Print.** The archive cites Austro-Turcica 1541-1552 (ed. Nehring, 1995) for all five items: pp. 415-418,
  418-419, 433-434, 437 and 513. That is the archive's citation. I checked two items:
  - Three Latin phrases from the decipherments, two from 8-3-12 and one from 9-1-2, each return that volume as
    HathiTrust's only full-text hit. So the edition prints their Latin, not only a summary.
  - The volume is search-only, so I could not see the page numbers of the hits.
  - I did not search the other three items.
- **Brice Dudout's 1550 test is not one of these five.** It is in `targets/huyson1547`. He calibrated the key on
  Türkei I 7-3-20 and tested it blind on Türkei I 8-3-8.
- **Still unread:**
  - 8-2-24: Latin, about 25 lines. A clear draft is filed at 8-2-10 fol. 74.
  - 8-2-22 and 8-3-10: Malvezzi's Italian letters, partly ciphered.
  - The duplicate of 8-3-12: 29 lines, not transcribed.
  - 9-1-2 itself is deciphered, but its 6 cipher lines were not decoded here.

## The test on 8-3-12 (`lead892_test/`)

The letter was deciphered long ago, so this is evidence for the vetting, not a new target. It tests whether the
upstream `targets/malvezzi1548` key reads a 1550 letter unchanged.

### Method

- The plan and its pass mark were written and hashed before decoding:
  - `PLAN_malvezzi1550.md`
  - `PLAN_malvezzi1550.md.sha256`, timestamped 05:24 UTC, 23 Nov 2026.
- Frozen key: `targets/malvezzi1548/KEY_BRIEF.md`, SHA-256 `66f98502...93fd`.
- The key describes its signs in words. Each 1550 shape was linked to a key description before decoding, in
  `sign_values_frozen_key.json`.
- Disclosure: the agent that wrote the plan had already read the opening lines of the 19th-century decipherment on
  an 800 px survey image. The two transcribers had not seen it.
- Two transcriptions of the original's 42 cipher lines were made by two separate helper agents. They saw only the
  line images and a sign sheet with codes and no values:
  - `transcription_T1.txt` and `transcription_T2.txt`.
  - They agree on 979 of 999 aligned signs (0.980).
- Decoding and scoring are mechanical:
  - Scripts are in `scripts/`. Run `python3 scripts/decode.py` and `python3 scripts/agree.py`.
  - Decodes are in `decode_T*.txt` (word level, holes in brackets) and `mechanical_T*.txt` (per line).
  - The reference is `reference_19c_decipherment.txt`, transcribed after the plan.

### Result

| | Letters matched (of 952) | Words read, no supplied letter (of 170) |
|---|---|---|
| Transcription 2 (primary) | **0.924** | 124 |
| Transcription 1 | 0.919 | 121 |

- The pass mark was 0.85, so the test passes.
- 200 keys shuffled among the sign codes score mean 0.358 and best 0.430.
- The decode builds Latin sentences from beginning to end. The key did not change between 1548 and 1550.

### Observations for the key's owner, not edits to `targets/malvezzi1548`

Every occurrence is listed in `key_gap_occurrences.json`, from transcription 2, aligned to the 19th-century text.

1. **A looped sign the key does not describe.** It has a V-shaped head over a closed loop at the foot, like a
   looped gamma. It stands for **q**:
   - aligned in A09.4 *quibus*, A15.13 *quarundam*, A19.9 *quod* and B03.14 *quemadmodum*;
   - also at A09.16 and B11.18, which the alignment left unpaired, both next to *quidem* and *que*.
2. **The figure 8 serves three values.** All three are already in the key under different headings:
   - d, 12 times;
   - mm, 3 times: B09.7 *commoda*, B10.17 *committimus*, B18.8 *summa*;
   - x, once: A09.2 *ex*.
   The same holds for the figure 7: i as a letter, and ll as the doubled-letter numeral, 4 times (A10.16
   *intelliges*, A14.9 *gallica*, A17.16 *gallie*, A20.6 *nonnulla*). A reader must tell numeral from letter by
   context.
3. **x is also written with the alpha-like sign** that the key gives as q: B05.20 *exemplo*, B17.17 *experientia*.
4. **Nulls not in the key's list:**
   - & opens three runs: A02.1, A03.10, A05.1.
   - A star at A07.13.
   - The capital B at A03.7.
   - Loose b, 10 times, is already listed as a null.

Three sign-sheet links made for this test were wrong. They are the test's errors, not the key's:

- The square-u sign is the key's "Ш-like" **g**, 12 of 12 times (*intelliges*, *gallica*, *Gonzaga* ...).
- The turned-y sign is **h**, as in DECODE's transcription of R367: *habes*, *habetur*, *hec*.
- The plain pi is g three times.

With the first two of these and the q-sign put right (post hoc, `scripts/posthoc.py`, not part of the hashed plan),
transcription 2 scores 0.940 of letters and 132 of 170 words.

### Images

Archive images are not included. The Austrian State Archives' fee schedule ("Entgelte", 28 Aug 2026, section 2,
"Publikationen") requires two things for every reproduction used in a publication, including on the web:

- "ein vollständiger Quellennachweis", a full source reference;
- "ein kostenloses Belegexemplar", a free copy of the publication sent to the archive.

It adds: "Die Verwendung von Vervielfältigungen ist entlang der Lizenz CC BY-ND erlaubt" (use of reproductions is
allowed along the lines of the CC BY-ND licence). Line crops and a sign sheet are adaptations, and the free copy has
not been arranged.

The records:

- 8-2-22: https://www.archivinformationssystem.at/detail.aspx?ID=7048237
- 8-2-24: https://www.archivinformationssystem.at/detail.aspx?ID=7048241
- 8-3-10: https://www.archivinformationssystem.at/detail.aspx?ID=7048434
- 8-3-12: https://www.archivinformationssystem.at/detail.aspx?ID=7048437
- 9-1-2: https://www.archivinformationssystem.at/detail.aspx?ID=7079699

## Routes

- What worked:
  - AIS detail pages and images, one request at a time.
  - HathiTrust full-text search in Chrome; its check page cleared on its own.
- What did not:
  - Google Books: API daily quota error, and an unusual-traffic page on the web search.
  - HathiTrust's in-volume search page did not render, so I have no page numbers.

## What is left

- 8-2-24 against its clear draft.
- 8-2-22 and 8-3-10, in Italian.
- The duplicate of 8-3-12.
- The page numbers of the hits in Austro-Turcica.
