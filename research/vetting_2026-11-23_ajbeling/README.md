# Vetting, Andrew Beling (2026-11-23)

Run by Andrew Beling (ajbeling) with AI agents (Claude Opus 5.5, with three helper agents for the blind
transcriptions). An independent AI reviewer (Claude Opus 5.5) checked the package on 23 Nov 2026; its corrections are
applied here.

## Lead 892: read (supersedes the block of 29 Oct 2026, which said partly_read)

Ferdinand I and his resident at the Porte, Giovanni Maria Malvezzi, 1550: HHStA Wien, StAbt Türkei I 8-2-22,
8-2-24, 8-3-10, 8-3-12 and 9-1-2. Every ciphered passage of the five items has a decipherment or a clear text on
record, on the leaf or filed with it, so nothing in the lead is unread. The verdict rests on those decipherments, not
on our decodes. Austro-Turcica 1541-1552 (ed. Nehring, 1995) prints all five with the cipher passages in clear
(below).

| Item | Language, extent | Decipherment or clear text on record | Our decode (`lead892_test/`, `lead892_rest/`) |
|---|---|---|---|
| 8-2-22, Malvezzi to Ferdinand, 24 Mar | Italian, four cipher passages (about 46 lines) in the original, all again in the duplicate | 16th-century decipherment between the lines, on every cipher line of the images viewed | two passages (10 lines): 0.739 of the letters of my reading of the gloss, under the 0.80 pass mark |
| 8-2-24, Ferdinand to Malvezzi, 25 Mar | Latin, 26 cipher lines | clear draft at 8-2-10 fol. 74 (AIS 7048141, images 9-10); modern pencil decipherment over lines 1-3 | 0.875 of the draft's letters; pass |
| 8-3-10, Malvezzi to Ferdinand, 22 Apr | Italian, about 50 cipher lines | 16th-century decipherment between the lines throughout | fol. 160r (10 lines): 0.783 of the letters of my reading of the gloss, under the 0.80 pass mark |
| 8-3-12, Ferdinand to Malvezzi, 28 Apr | Latin, 42 lines (original) and 29 (duplicate) | 19th-century decipherment filed with it (images 5-6) | 0.924 of the decipherment's letters; pass |
| 9-1-2, Ferdinand to Malvezzi, 3 Oct | Latin, 3 cipher lines | 19th-century decipherment filed with it (image 3) | 0.911 of the decipherment's letters; pass |

- **What this block changes against the block of 29 Oct.** That block already noted, from the archive's
  descriptions, the 19th-century decipherment of 8-3-12, the clear draft of 8-2-24 and the archive's citation of
  Austro-Turcica; it had not seen any cipher. ("No decipherment" is in the lead's `status` field, not in the 29 Oct
  block.) New here: all five items seen at reading size; three of the five are Latin, not Italian as the lead says;
  the 16th-century interlinear decipherments over the cipher lines of the originals of 8-2-22 and 8-3-10 (every line on the images viewed); the
  19th-century decipherment of 9-1-2; the pencil gloss on 8-2-24; and tests of the 1548 key on all five. Verdict
  from partly_read to read.
- **Lead 2682** (vetted `read`, 16 Nov 2026) covers the rest of Türkei I Kt. 8-9 "beyond the ones in leads 891/892".
  It names 8-2-22, 8-2-24 and 8-3-10 as the overlap to match against this lead, and records from the Vienna inventory
  regests on Hungaricana that the Malvezzi cipher pieces in those boxes carry their decipherments and are printed in
  Nehring. The two leads do not duplicate each other: 892 holds these five items, 2682 the remainder; the evidence
  here, from the leaves, agrees with 2682's.
- **Print.** Austro-Turcica 1541-1552 (ed. Nehring, Munich 1995) prints all five letters with their cipher
  passages in clear, set between /: and :/. Seen on 24 Nov 2026 by an AI agent of ours (Claude Opus 5.5) in the
  Bavarian State Library's free digital copy, https://www.digitale-sammlungen.de/en/view/bsb00150599, from the
  library's own OCR text of the scans (printed page = scan - 14); the page images were not viewed:
  - No. 155, pp. 415-418: 8-2-22 (source "f. 111r-114v, Original"). Two passages in /: :/, "De novo sonno venute
    nove de Soria ... esso meco" and "Circa l'armata del mare ... quello che Dio vorä"; our two decoded passages
    (S01-S04, E01-E06) are the start of the first and the whole of the second.
  - No. 156, pp. 418-419: 8-2-24, the letter of 25 March 1550 (source "f. 123r-v, Original; f. 74r-v,
    Dechiffrierung"), so the edition prints this letter, with its text from the draft on fol. 74 of 8-2-10, not the
    draft of 17 March. The whole cipher passage, "Quamvis tibi per proximas ... gradatim descendas", is in
    /: :/; the edition reads "alias" where we left the draft's "ats" unexpanded.
  - No. 163, pp. 433-434: 8-3-10 (source "f. 160r-161v, Original"). One passage in /: :/ from "Sir, da molti giorni
    in qua Rustan Passa" to "sei che se armano qua", which includes our fol. 160r lines (M01-M10).
  - No. 165, p. 437: 8-3-12 (source "f. 169r-v, 171r-v, Original; 170r-v, Dechiffrierung"). The whole cipher text,
    "Transmittimus ad te ... non dubitamus", in /: :/.
  - No. 193, p. 513: 9-1-2 (source "f. 166r-v, Dechiffrierung; f. 167r, Original"). "Teque gratiose requirimus ...
    certiores facere pergas" in /: :/.
  The HathiTrust phrase searches of 23 Nov (`search_log_hathitrust.md`) were made before the print was seen.
- **What our decode adds.** For the two Italian letters, nothing I can show. For 8-2-24 the decode follows the draft,
  with *Ras* where the draft has "Principem Turcarum" and the code word *zus* where it has "Transylvaniae"
  (`targets/malvezzi1548/KEY_BRIEF.md` gives *zus* as "Hungariae imperium"). For 8-3-12 the cipher reads *mentem
  dilectionis et maiestatis eius caesareae*, *traductione italica* and *negotiis istis nostris*, where the
  19th-century decipherment has *dilectissimi fratris ... suae*, *italiana* and no *istis*
  (`lead892_rest/compare_8-3-12.md`; an independent reviewer confirmed all three on the image). In No. 165 the
  edition prints *mentem dilectionis et Maiestatis eius Caesareae*, *traductiones Italica*, *Drogutum*, *indutiarum*
  and *Teudes* as the cipher has them, and *negotiis nostris* without *istis*.

## The key used, and whose it is

All tests use Daniel Bourdeau's `targets/malvezzi1548/KEY_BRIEF.md` (from DECODE R367/R386), unedited: SHA-256
`66f98502297ed3ff111122bae75b21c309325b8adc1f4cc8c37d9fcd8c7793fd`, the same as upstream. They do not use Brice
Dudout's K-C01 (`targets/huyson1547/key_KC01.json`, SHA-256 `c53e36e5...d873127`). The key describes its signs in
words; the links from those words to the 1550 sign shapes (`lead892_test/sign_values_frozen_key.json`) are ours,
frozen before any decoding, and some were wrong (listed below: square u = g, turned y = h, pi with feet = g, among
others). Scores are of "KEY_BRIEF plus our links".

What the tests show: with those links the key beats every one of 200 shuffled keys on all five items (an independent
reviewer re-ran 2,000 with another seed and code: best shuffled 0.414-0.511); it reads the three Latin letters above
their pass marks; the two Italian samples fall below the pass mark against my own reading of the glosses. The 1550
copies also use signs the brief does not list: a looped q, & and a star as nulls, alpha for x.

## The tests on the other four items (`lead892_rest/`)

- Plan and pass marks written and hashed before any transcription was decoded or any witness transcribed:
  `PLAN_malvezzi_rest.md`, `.sha256` (15:19 UTC, 23 Nov 2026). The key and our sign links are those of the 8-3-12
  test, unchanged. Times written inside the plan, the transcription and witness headers of this round are wrong (I
  wrote them later than the files were made): the plan was hashed at 10:19 Eastern, T1 saved 10:24 (Latin) and 10:41
  (Italian), T2 10:39, the witnesses 10:42-10:43, the scores 10:45.
- Transcriptions: T1 by the orchestrating agent (not blind: it knew the key and had seen the witnesses; said in the
  file); T2 by a separate helper agent that saw only the line images and the sign sheet with codes. T2 is the primary.
  Agreement T1/T2 (`results/agreement.txt`): 8-2-24 0.951, 9-1-2 0.857, 8-3-10 0.876, 8-2-22 0.897; part of the
  difference is naming (T1 wrote the reversed c as `c` and a d-like sign as `3?`, T2 as unlisted signs). An
  independent reviewer's own transcription of 8-2-24 lines P04-P08 agrees 0.943 with T2 and 0.933 with T1.
- Witnesses (`witness/`), transcribed after the plan: the clear draft of 8-2-24; the 19th-century decipherment of
  9-1-2 (read before the plan; disclosed there); the interlinear glosses of 8-3-10 and 8-2-22, which are a weak
  witness (fast cursive between dense lines; guesses marked).
- Run `python3 scripts/score.py` and `python3 scripts/agree.py` (they use `../lead892_test/scripts`). The aligner needs numpy.

| Item | Witness letters | T2, letters (pass mark) | T1 | 200 shuffled keys, mean / best | Words read, T2 |
|---|---|---|---|---|---|
| 8-2-24 | 973 | **0.875** (0.85): pass | 0.878 | 0.355 / 0.428 | 111 / 178 |
| 9-1-2 | 90 | **0.911** (0.85): pass | 0.922 | 0.390 / 0.478 | 8 / 14 |
| 8-3-10, fol. 160r | 511 | **0.783** (0.80): miss | 0.773 | 0.362 / 0.433 | 52 / 116 |
| 8-2-22, two passages | 452 | **0.739** (0.80): miss | 0.715 | 0.335 / 0.392 | 47 / 104 |

The two Latin letters pass. The two Italian samples miss the pass mark I set, although the decodes build the same
Italian sentences as the glosses (`results/decode_8-3-10_T2_primary.txt`: *sir da molti giorni in qua [Rustan]
passa si e fatto tanto arrogante superbo ...*) and stand far above the shuffled keys. The misses come from the sign
links in Malvezzi's hand (his reversed 6 is written like a d and was not on the sheet), the gloss read by me, and
code words (*Ras*, *ki*, *ka*, *zos*) set against glossed words. They are reported as misses. The secondary scores
(the three sign links learned on 8-3-12) change little: 0.793 and 0.741.

Sign-sheet links (ours) that these four items show to be wrong, as on 8-3-12 (not edits to the key): the inverted-V
sign that the transcribers coded `lam` is often the key's caret **f** (*fuit*, *flumio*, *firma*), though `lam` also
stands for h (*hoc*, P08), so the two shapes are not cleanly separated; the pi with feet is **g**
(*regno*, *agere*); the 8-shaped circle on a stem coded `qo` is often **d** (*concedendo*, *quondam*); the reversed c
is **b**.

## The test on 8-3-12 (`lead892_test/`)

The letter was deciphered long ago, so this is evidence for the vetting, not a new target. It tests whether Daniel
Bourdeau's `targets/malvezzi1548` key brief, with our sign links, reads a 1550 letter.

### Method

- The plan and its pass mark were written and hashed before decoding:
  - `PLAN_malvezzi1550.md`
  - `PLAN_malvezzi1550.md.sha256`, timestamped 05:24 UTC, 23 Nov 2026.
- Frozen key: `targets/malvezzi1548/KEY_BRIEF.md`, SHA-256 `66f98502...93fd`.
- The key describes its signs in words. Each 1550 shape was linked to a key description before decoding, in
  `sign_values_frozen_key.json`. The plan quotes its hash as "50a3a583...1cb37"; the file's hash is
  `50a3a58369d51c5e02bc36dfbd619282e694aaa86c1d89c3a0161b1e13bcf127`. The fragment in the plan is a slip; the file
  (00:23 Eastern) is older than the plan (00:24) and was not changed after. The plan's "about 00:45 Eastern" is also
  wrong: the file was written at 00:24.
- Disclosure: the agent that wrote the plan had already read the opening lines of the 19th-century decipherment on
  an 800 px survey image. The two transcribers had not seen it.
- Two transcriptions of the original's 42 cipher lines were made by two separate helper agents. They saw only the
  line images and a sign sheet with codes and no values:
  - `transcription_T1.txt` and `transcription_T2.txt`.
  - They agree on 979 of 999 aligned signs (0.980). That is agreement between our own two helpers, both working
    from the same sign sheet; an independent reviewer's own blind transcription of lines A01-A10 agrees 0.927 with
    T1 and 0.923 with T2, mostly on signs one of us marked as doubtful.
- Decoding and scoring are mechanical:
  - Scripts are in `scripts/`. Run `python3 scripts/decode.py` and `python3 scripts/agree.py` (the aligner needs numpy).
  - Decodes are in `decode_T*.txt` (word level, holes in brackets) and `mechanical_T*.txt` (per line).
  - The reference is `reference_19c_decipherment.txt`, transcribed after the plan.

### Result

| | Letters matched (of 952) | Words read, no supplied letter (of 170) |
|---|---|---|
| Transcription 2 (primary) | **0.924** | 124 |
| Transcription 1 | 0.919 | 121 |

- The pass mark was 0.85, so the test passes.
- 200 keys shuffled among the sign codes score mean 0.358 and best 0.430.
- The decode builds Latin sentences from beginning to end. The 1548 key brief, with our links, reads this 1550
  letter; the letter also uses signs the brief does not list (below).

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

Conditions of the images: they are from the Austrian State Archives' public archive information system
(Haus-, Hof- und Staatsarchiv, Türkei I 8-2-22, 8-2-24, 8-3-10, 8-3-12, 9-1-2, and 8-2-10 for the draft), read
without sign-in by AI agents working for Andrew Beling, one image at a time. Since 1 September 2026 the archive
allows its reproductions to be published under CC BY-ND with a full source reference and a deposit copy; its terms
say nothing about AI readers or automated access. Nobody at the archive was asked; Andrew Beling decided on the use
himself. No image is in the repository. `lead892_rest/scripts/line_boxes.py` gives the pixel boxes of every line
used, so the crops can be remade from the archive's images.

The records:

- 8-2-22: https://www.archivinformationssystem.at/detail.aspx?ID=7048237
- 8-2-24: https://www.archivinformationssystem.at/detail.aspx?ID=7048241 (clear draft: 8-2-10, https://www.archivinformationssystem.at/detail.aspx?ID=7048141, images 9-10)
- 8-3-10: https://www.archivinformationssystem.at/detail.aspx?ID=7048434
- 8-3-12: https://www.archivinformationssystem.at/detail.aspx?ID=7048437
- 9-1-2: https://www.archivinformationssystem.at/detail.aspx?ID=7079699

## Routes

- What worked:
  - AIS detail pages and images, one request at a time.
  - HathiTrust full-text search in Chrome; its check page cleared on its own.
- What did not:
  - Google Books: API daily quota error, and an unusual-traffic page on the web search.
  - HathiTrust's in-volume search page did not render, so I had no page numbers; the Bavarian State Library's
    digital copy (24 Nov) gave them.

## What is left

- Nothing in lead 892 is unread. Not transcribed by us: the other two cipher passages of 8-2-22 and the duplicate
  (images 5-8), fol. 160v-161r of 8-3-10, and the duplicate of 8-3-12; each original passage carries a decipherment
  between the lines or filed with it.
- A word-by-word comparison of the edition with the decodes (only the points named above were compared), and the
  edition's page images (only the library's OCR text was read).
- An independent AI review was made on 23 Nov 2026 and its corrections applied; no person has reviewed the package.
