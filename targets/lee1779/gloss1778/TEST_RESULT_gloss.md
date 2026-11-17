# Held-out test on 71 groups glossed at the time in Arthur Lee's letters of 1778-79: result (14 November 2026)

Worker: Claude (Opus 5.5). Look-up helper: one separate Opus 5.5 agent. No Sonnet or Haiku. No person has checked any of this against the images.

## Timeline and hashes

| Step | Time (EST) | File | sha256 |
|---|---|---|---|
| Plan written, rule files hashed | 20:41 | TEST_PLAN_gloss.md | (hashes of the frozen files inside it) |
| Numbers transcribed by me from the images | 20:42 | groups_numbers.tsv | 91a522e5b307a740b13f48adcf7987aa2ad153393c26bc484f84a5b67262ebfc |
| Blind look-up frozen by the helper | 21:12:13 | lookup_blind.tsv | 3f2f368b3ebfea8f8daed25fbbe5a8faf6f46d357b1bfaa544152fa4ccd2ccb0 |
| Glosses written, scored | 21:14:59 | glosses.tsv / scored.tsv | 3d8f29aa…cdb123 / 2ea54757…20ee4 |

## How well the blinding held

- **The look-up was blind; the transcription of the figures was not.** Before writing the plan I had already read the finder's table (`cipher_pages_refetch.tsv`), which gives every group with its gloss. I then read the figures from the images (1000 px, glosses visible above them). My reading of the figures could therefore lean toward the finder's; in fact it repeated the finder's three misreadings (below).
- **The helper was given only the figures, the rule and the dictionary scans.** It was told not to open the finder's files, the National Archives images, or the package's key, decoding, readings or notes. It reports that it opened none of them, saw only file names in folder listings, and froze its table before I wrote any gloss into a file. I changed nothing in its table after the freeze.
- **The rule was not wholly independent of this test set.** When the package chose the 1776 printing and the counting rule, three of these groups, as printed by Tomokiyo, were among its 19 anchors: channels 82,b,V; Congress 99,a,XVII; loan 229,a,XXXVII. These account for 6 of the 71 occurrences.

## Result: as written in the plan, the test FAILS the pass mark

| Look-up | Same | Other form | One off | Different | Hits | Share |
|---|---|---|---|---|---|---|
| **Real rule (1776)** | 40 | 14 | 3 | 14 | **54 of 71** | **76%** (mark: 80%) |
| Real rule, without the 6 anchor occurrences | | | | | 48 of 65 | 74% |
| C1 page +1 | | | | | 0 of 71 | 0% |
| C2 page −1 | | | | | 0 of 71 | 0% |
| C3 other column | | | | | 0 of 71 | 0% |
| C5 1781 printing | | | | | 0 of 71 | 0% |
| C4 1773 printing (an edition comparison, not held to the 10% mark) | | | | | 44 of 71 | 62% |

- **The controls all pass.** The four true controls give 0 hits each. The 1773 printing scores below 1776, as the plan required.
- **The real rule falls short.** It gets 54 of 71, three short of the 57 needed.
- **How the control hits were scored.** By machine: a hit is a headword equal to the gloss's base word, or that word plus at most two letters. This is slightly lenient, so the true control counts can only be lower. The real-rule column was scored by hand.

## Second look at the 17 misses (after the freeze; the score above is not changed)

Each of these was rechecked on the letter image and, where one exists, on the 1776 dictionary page image.

**My transcription slips (3).** The clerk's figure 4 looks like "1" with a hook. I, like the finder, read 347 as 317, 40 as 140, and probably 243 as 240. The frozen rule gives the right word at the corrected positions, checked by me on the 1776 page images:
- **id 9:** 347,a,XXVI is *Sorry* (26th entry on p.347). Glossed "sorry".
- **id 28:** 40,a,III-s is *Affair* (3rd entry on p.40). Glossed "affairs".
- **id 71:** 243,a,XVII is *Minister* (17th entry on p.243). Glossed "Minister". The last figure on the image is ambiguous between 0, 2 and 3. Tomokiyo already prints 243,a,XVII = minister.

With these three corrected the count would be 57 of 71 (80.3%). That is exactly the mark, but it is reached after looking, so it is not a pass of the test as planned.

**A possible transcription slip (1).**
- **id 39:** 233,b,IX is *Magnetism*; glossed "negotiation".
  - The figure may be 253, read as 233 (5 for 3).
  - On p.253b the OCR puts Neglect at entry 1 and Neighbour at about entry 14. Negotiation would fall at about entry 9.
  - There is no 1776 image of p.253 here, so this is unverified.

**Look-up failures, not disagreements (4).** No 1776 image exists here for these pages, and the OCR has no text at the line:
- **id 14:** 300,b,IX, glossed "quarrel". 1773 has *Quarryman* at that line.
- **ids 52 and 61:** 96,b,XX, glossed "concluded" and "conclude". 1773 has *Conclude*.
- **id 69:** 364,b,XXIII-g, glossed "supplying". 1773 has *Supporter*, and 1776 has Supporter one line below.

These need the 1776 page images, which were not downloaded under this brief.

**The writer's slips (4).**
- **id 18:** 426,b,XXXVI (*Your*), glossed "you", in "or to you". The same group is glossed "your" twice in the same letter, and *You* is 426,b,XXVIII (id 35). Either Lee or his clerk wrote the "your" group, or the decipherer glossed it by the sense.
- **id 21:** 361,b,XXX-s, glossed "succours". The rule gives *Succourer*. *Succour, s.* is the entry above (29th). Lee is one entry off.
- **id 62:** 356,a,XXIX-d, glossed "stipulated". The rule gives *Stipulation*. *Stipulate* is the 28th entry, and in August 1778 Lee wrote 356,a,XXVIII for "stipulate", with the numeral overwritten. Lee is one entry off in 1779.
- **id 17:** 333,b,XXIV, glossed "service". The rule gives *Serviceable*. *Service, s.* is the entry above. This is one entry off; it could be Lee's slip, or a run-over line on that page counted differently. Not settled.

**The decipherer's wording (1).**
- **id 54:** 339,b,XXXVII-g, glossed "redeeming". The rule gives *Sink*, so the group reads "sinking all or great part of the paper".
  - Sinking and redeeming paper money mean the same here.
  - The helper marked this look-up doubtful (an OCR gap; it is Sink or the entry after).
  - *Redeem* is on p.307b, nowhere near.

**Real disagreements, unexplained (4).**
- **id 48:** 163,a,VII-a, glossed "Florida". The figures are clear on the image. The rule gives *Fit, s.*, doubtful because the headword is in the binding. *Florid* is not near that place in 1776.
- **id 59:** 255,a,XX, glossed "a noble". The rule gives *No, ad.*; *Nobility* is at 21, and *Noble* is about two entries further down. No image of that page.
- **ids 64 and 65:** 359,b,XXXI and 63,a,XXVI, under the decipherer's phrase "Treaty of Alliance", which runs over three groups. The rule gives *Subcelestial* and *Bethink*, which make no sense here. On the image the 63,a,XXVI numeral is corrected.

## Findings for later (the rule is not changed)

1. **The clerk's figure 4.** It is easily misread as 1, and the package's own transcription of the 1779-80 letter book should be checked for the same slip.
2. **Getting the remaining look-ups.** The 1776 page images for pp.96, 253, 255, 300, 359 and 364 would settle five of the open look-ups. They are free on the Internet Archive.
3. **Lee's counting.** He is sometimes one entry off (361b, 356a, perhaps 333b). The direction is not consistent, so this does not suggest a different counting rule.

## The repository's validation check

- **What it scores.** `docs/_validate.py` scores `validation.tsv`, which pairs the target's own cipher tokens with our reading of them. It measures that reading against a letter n-gram model, against random keys, and against keys fitted to shuffled text.
- **Why the glossed groups are not a fit.** They are other letters, and their readings are the 1778 decipherer's, not a reading of this target. Adding them to `validation.tsv` would mix two texts and would test the language model's view of the decipherer's words, not our look-up rule. A word-level code with about 1.4 occurrences per group also stays underdetermined to a letter model however many groups are added.
- **Decision.** I did not supply them as input. The verdict stays "underdetermined". The held-out test is recorded as evidence beside it instead.
