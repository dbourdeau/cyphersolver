# The declaration before any result

> Paths and working labels removed on 13 November 2026; no number and no rule changed.

Written at 16:12 (UTC−3) on 12 November 2026, before any count on a new page.

**Credit.** The source is DECODE, records R5625 to R5659 (digit pages) and R5667 to R5686 (shape-label pages). The archive is the Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346. Use is for research only. Nobody may publish or redistribute the DECODE images.

**The transcription.** It is a machine transcription of the DECODE images, made in my pipeline. Nobody verified it. This read opens no image.

**The label of every result.** A read with our frozen key, found from the ciphertext alone; not yet checked against the published key. Each number is labelled "real" or "twin".

## 1. What is frozen

| Item | What it is | File |
| --- | --- | --- |
| The key | The "shown" letter of each of the 80 pair codes in pool "one2": 69 codes show a letter, 11 show "?" | a local file |
| The cut | H6: a lone 6, a lone 2, 80 pair codes (a local file) and escapes | a local file |
| The unit model of the cut | 30 EM steps on every segment of pool "one2" | a local file of the earlier key-free work |
| The roles | A lone 6 is a word space. A lone 2 is a null and is dropped. An escape is a gap mark. | a local file of the earlier key-free work, section 5 |
| The agreement rule | 90% or more of the starts within 100 nats give the letter, and 3 or more tokens | applied already in the "shown" column of a local file |
| The loader | Doubts and gaps become masks. A cleartext break and a page end each end a segment. | a local file of the earlier key-free work |
| The page gate | Share of 6 at most 0.10, and P5 at most 0.30 when a page has 20 or more runs | a local file of the earlier key-free work |
| The suspect rules | Rule 1: a run of 8 or fewer digits at a cleartext break. Rule 2: a row with 3 or more interior escapes that are 10% or more of its tokens. | a local file of the earlier key-free work |

- I rebuilt the unit model once from the earlier key-free work's pool "one2" input (before 16:12). Its Viterbi parse equals the earlier key-free work's saved parse on all 13 records, with no segment that differs.
- I use the "shown" column unchanged. I run no start and no EM step on a key.

## 2. How I apply them to the new pages

- **Input:** the 113 files of a local file. The earlier key-free work's loader reads all 113 files with no error (checked at 16:12). 35 pages hold cipher rows.
- **The parse:** the frozen unit model, Viterbi only. No EM step runs on new text.
- **The suspect rules:** I apply rules 1 and 2 to the new pages, as the earlier key-free work did to its new leaves. A suspect stretch becomes masks. Then the frozen model parses the stream again.
- **The page gate:** I compute it for each of the 35 pages.
  - A page that fails stays out of the one-key check, as in the earlier key-free work.
  - A page that fails is still read. `READ-digit.md` marks it.
- **The text:** the form of a local file of the earlier key-free work. A lone 6 is a space. A lone 2 is dropped. `·` marks an escape, a mask or a hidden code. `|` marks a cleartext break. `/` marks a page end.
- **No change of key, cut, role or rule.** Code 07 reads "l", as frozen (see section 6).

## 3. The measures of the read (real)

Each measure is given for each record and for all records.

- **Pair tokens:** the tokens of two digits under the frozen cut.
- **Share shown:** the pair tokens whose code shows a letter, over all pair tokens. This is the earlier key-free work's coverage measure.
- **Tokens that the key does not show,** as three separate counts:
  - escapes: a lone digit other than 6 and 2, which no code holds;
  - hidden tokens: pair tokens of the 11 codes that the rule hides;
  - masks: doubtful or unread positions and gap notes.
- **Pair types outside the key:** the key holds all 80 pair codes of the cut. So this count is 0 by construction. I report it as a check.
- **Three-digit codes:** the frozen cut has none, by construction. The key-free proxy is the earlier key-free work's P5:
  - P5 is the odd share of the runs between two 6 signs that hold no 2;
  - an odd run needs a three-digit code, a lone digit or a misread digit;
  - so P5 cannot tell these three causes apart;
  - I report the runs, the odd runs and P5, beside the earlier key-free work's values (new leaves 0.258 on 260 runs; pilot 0.130).
- **The .80 rule:** I compute the share shown on the records that fit (section 4), pooled, and on each record. If the pooled share is under .80, I propose a new fit with its price. I do not launch it without the coordinator's ruling.

## 4. The one-key check (real code counts; key-free)

This is the earlier key-free work's check (a local file, section 4) on the new records.

- **Records:** the 23 digit records. R5625 has no cipher row, so it has no token. So 22 records enter.
- **Tokens:** the frozen parse of the clean pages of each record, after the suspect rules. Pairs, lone 6 and lone 2 count. Escapes are dropped.
- **The pilot:** R74 to R78 from the earlier key-free work's pool "one2" input, with the same frozen parse.
- **Test A:** each record against the pooled pilot. The measure is bits per token under an add-0.5 unigram of the pilot. The null permutes the tokens of the record and the pilot. 999 permutations, seed 2026111451.
- **Test B:** each record against the other 21 new records (leave one out). 999 permutations.
- **The control (twin):** six one-key twins, with the seeds and the twin writer of the earlier key-free work.
  - Languages and seeds: Italian 2026111181, 2026111182 and 2026111183; Latin, French and Spanish 2026111181.
  - The template is the earlier key-free work's 13 pool "one2" records, then the 22 new records, with their sizes, masks and breaks.
  - The lone 6 and lone 2 shares come from pool "one2".
- **A deviation, declared now.** The real side uses the frozen unit model, fitted on pool "one2". So each twin's unit model is fitted on the twin's pool "one2" part only and applied to all its records. The earlier key-free work fitted each twin's model on the whole twin.
- **The reading, by record slot (the earlier key-free work's rule):**
  - "differs": p below 0.05 and an excess above the largest excess of the same slot in all six twins;
  - "not decided": p below 0.05 only;
  - "fits": else.
- **Power:** for each record, the share of 100 draws with a test-A p below 0.05 when a quarter of its code types get new codes (199 permutations each). Small records have low power, and the report says so.
- **The old split:** I run the same check on the earlier split of R5626 to R5651, as a report. The newer text is the main result.

## 5. The comparison with the earlier key-free work's read (records R5626 to R5651)

- **Old:** the earlier split (a local file, its cleared list). **New:** this split.
- Both go through the same frozen pipeline and the pool "one2" key.
- For each record, I give: pair tokens, the share shown and the letters equal by alignment of the two decoded texts.
- For each name, place and date in a local file of the earlier key-free work, I say whether it still reads in the new text.
- The earlier key-free work's appendix records (R5642, R5645, R5646, R5649, R5650 and R5651) used the pool "all" key. Here they use the pool "one2" key. I say so beside their rows.

## 6. The shape-label pages: structure only (real)

There is no fit on these pages. A label is local to its page. So every count of label types or repeats stays inside one page.

### 6.1 The measures

- **For each page, record and all:** tokens, doubtful tokens, label types, tokens for each type, the five commonest labels and their shares.
- **Repeated groups:** for each n from 2 to 6, the label groups that occur 2 or more times on one page. A gap or a clear mark breaks a group. A mark (`·`, `—`, `_`) holds no position and is skipped. As a reference, I give the mean count of 20 shuffles of the same page.
- **Descriptive only:** the unigram entropy and the index of coincidence of each page. The references are the digits of the digit pages and the letters of the Italian twin text.
- **Token rules:** a doubtful label `x?` counts as `x`. `[a|b?]` counts as `a`. `[?]` is a token but not a label type. `n{bar}` is its own label.

### 6.2 The one question: the digit cipher in another notation, or another system?

- **The primary measure, K95:** the smallest number of label types that hold 95% of a page's labelled tokens.
  - The digit cipher has 10 signs. So "ten-sign" means K95 of 10 or less.
  - "More signs" means K95 of 14 or more.
  - From 11 to 13, the measure does not decide.
- **The check of the pair structure, S:**
  - For each label c with 30 or more tokens on the page, and each "null" choice d (none, or a label with 20 or more tokens), I take the runs between two consecutive c that hold no d.
  - S is the smallest odd share of those runs over all choices of c and d, with 20 or more runs.
  - The digit cipher gives P5 of 0.11 to 0.27 on clean pages (the earlier key-free work). A random order gives about 0.5.
  - "Pair structure" means S of 0.30 or less, and S below the 1st percentile of 199 shuffles of the same page (seed 2026111261).
- **A positive control:** I run S on the clean digit pages, with the digits as labels. If fewer than 80% of those with 20 or more runs show pair structure, S does not inform. Then the verdict rests on K95 alone.
- **The verdict for each page:**
  - "the digit cipher in another notation": ten-sign and pair structure;
  - "another system": more signs and no pair structure;
  - "not decided": every other case, and pages with fewer than 200 labelled tokens.
- **The verdict for all:** "another system" if 75% or more of the decided pages say so. "The digit cipher" if 75% or more say that. Else "mixed or not decided".
- **A caveat:** a transcriber can split one digit shape into several labels (for example `[g|9?]`). This raises K95. The S check guards this case only in part.

### 6.3 What a fit would need

I state the letter model, the size, the twins and the price. I run no fit.

## 7. Exposure

- I read the brief, and the plan, the frozen read, the key and the code of the earlier key-free work.
- The brief sent me to the public `francia-346-leaves/README.md`. It states some results of a check against the published key:
  - code 07 stands for h in the published key, where our key reads "l";
  - 22 of our 80 pair codes are syllables (for example che, per and di), 8 are nulls and 10 are false pairs;
  - the published key has three-digit codes for words and names.
- **I use none of this.** Code 07 reads "l". The cut stays H6. No choice here depends on these facts. The three-digit measure comes from the brief and from the earlier key-free work's P5.
- I opened no key file, no grade file, no clear text, no image and nothing in the sealed decode folder.

## 8. Compute

- Local only, at most 2 workers. Before each job: fewer than 11 heavy jobs, more than 8 GB free and a 1-minute load under 28.
- No paid compute.
