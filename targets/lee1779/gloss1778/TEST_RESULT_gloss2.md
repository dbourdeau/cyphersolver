# Second gloss test: result (second attempt, after the first test failed)

Run 14-15 November 2026 by a worker agent (Claude Opus 5.5) with two separate Opus helpers. No person has checked
any reading of the images.

## What was done, in order

| Step | Time (EST) | File | sha256 |
|---|---|---|---|
| Plan written | 14 Nov 21:58 | `TEST_PLAN_gloss2.md` | 90f118ae72287f291195306e51efab735082347d4239c7d492808c620cc6a3c6 |
| Strips cut, checked, shuffled | 14 Nov 22:00 | `strips2_bands.json`, `strips2_key.tsv` | |
| Figures transcribed blind, frozen | 14 Nov 22:09 | `transcribed2.tsv` | d4615f936b8a8db2063a817c4f0e009927b066e969b8a7541382f21a01ea7cd2 |
| Look-up done blind, frozen | 14 Nov 22:40 | `lookup2.tsv` | c650d13b29c444ad1a7e29bc3697437c9aa62b6521fd517e7e7ab08c14aad2fb |
| Mapped to ids and scored | 14 Nov 22:50 | `map2_ids.tsv`, `scored2.tsv` | |

- **Hiding the glosses.** 35 strips were cut from the 1600-pixel images (`sources/raw/lee1779_push_2026-11-15/pcc83/`
  in the project folder, not in this repository), each from just below the interlined words to just below the coded
  line, with cut lines set by hand on zoomed views and every strip checked on a contact sheet. One strip that first
  showed the bottom of "Congress", one that showed part of "Sorry" and one that showed part of "Service" were recut
  before use. In the strips as used, no letter of a gloss is visible to me; a few strips keep the tail of a
  descender (the foot of a "g" or "f") at the top edge. All 71 groups were tested.
- **Transcription helper.** Given only the 35 strips plus three seed strips from the letter book (image 0041) with known
  figures (265,a,XXX; 107,b,XXX; 102,a,XXXII; 40,a,III-s; 333,b,XXI; 108,a,IX), told nothing of the content. It read
  all seeds correctly, so its batch was accepted. It reports opening nothing outside its folder.
- **Look-up helper.** Given only the 61 distinct transcribed groups, shuffled, plus three seed groups (63,b,II Between;
  165,a,VI Floral; 333,b,XXI Servant), the rule and the 1776 page images (22 more pages of the same Internet Archive scan
  were fetched for it). It found all three seeds, counted every REAL entry on an image, and reports opening nothing
  outside the dictionary folders and its own.

## Result: as planned, the second test also FAILS

| Look-up | Same | Other form | One off | Different | Hits | Share |
|---|---:|---:|---:|---:|---:|---:|
| **Real rule (1776)** | 40 | 15 | 4 | 12 | **55 of 71** | **77.5%** (mark 80%, 57 of 71) |
| Without the six anchor occurrences | | | | | 52 of 65 | 80.0% |
| C1 page +1 | | | | | 1 of 71 | 1.4% |
| C2 page -1 | | | | | 0 of 71 | 0% |
| C3 other column | | | | | 0 of 71 | 0% |
| C5 1781 printing | | | | | 0 of 71 | 0% |

The controls meet their mark (all under 10%); the real rule does not. The one control hit is C1 at id 71, where the
transcriber read 242 for 243 and page + 1 lands on Minister. The real-rule column was scored by hand with the first
test's categories against the first test's `glosses.tsv`, unchanged; the controls by the first test's lenient machine
rule.

## Second look at the 16 misses (after the score; the score is not changed)

My own readings of the 1600-pixel images; no person has checked them.

- **Misreadings of the figures by the new transcriber (9):** id 5 (99 read 94), 37 (229 read 299), 60 (248 read 348),
  64 (259 read 354), 65 (43,a,XXIII read XXVI), 66 (99 read 22, under a smudge), 69 (364,b,XVIII read 354,b,XXIII),
  70 (246,b,XXV read XXVI, a dot over the v), 71 (243 read 242). At the figures as I read them the rule gives the
  glossed word (Congress, Loan, Motion, Of, Alliance, Congress, Supply, Money, Minister).
- **Lee one entry off (3):** id 62 356,a,XXIX-d is Stipulation, glossed "stipulated" (Stipulate is 28; Lee wrote
  356,a,XXVIII for stipulate in August 1778); id 17 333,b,XXIV is Serviceable, glossed "service" (Service is 23, or 24
  if the run-over line of Sergeant above it is counted, which Lee does not do elsewhere); id 21 361,b,XXX-s is
  Succourer, glossed "succours" (Succour, s. is 29; on the 1600-pixel image the third x carries a dot, so the clerk
  may have written XXIX).
- **The decipherer's words where the rule's word fits the sentence (3):** id 54 Sink, "sinking" the paper money,
  glossed "redeeming"; id 59 No, "She has made no motion to conclude what is stipulated in the Treaty of Alliance"
  (Spain), glossed "a noble"; id 18 Your, "more so to your worthy constituents", glossed "you".
- **Unexplained (1):** id 14 300,b,IX is Quarryman, glossed "quarrel" ("on account of your present quarrel"); the
  figures are clear on the clerk's copy; Quarrel, s. is the 4th entry (IV).

Across both tests the figures, not the rule, cause most misses: the first transcriber misread 9 of the 17 groups it
missed (three found then, six on 15 November, one of them probable), the second 9 of 16. Where the figures are read
right on the image, the rule gives the glossed word or a word that fits the sentence in 67 of 71 groups by my count
(68 if 361,b is XXIX; the others: Stipulation, Serviceable, Quarryman). That count is made after looking and is not a
test result.
