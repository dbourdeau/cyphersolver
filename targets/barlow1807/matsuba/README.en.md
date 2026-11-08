# Sir George Barlow's cipher letter to Thomas Grenville (1807)

Fort William, 12 February 1807, "Private and Confidential", "Quadruplicate". Cleveland Public Library, John G. White Collection (W q091.92-B249t2).
This is a record of recovering the key to the numbered parts of the letter and reading all 19 pages.

**Relation to earlier work: reproduced.** WAINUT published this letter first ([dbourdeau/cyphersolver#231](https://github.com/dbourdeau/cyphersolver/issues/231), 3 November 2026, read in part). This is a separate reading made without sight of that one; the transcription, key and reading were not changed after reading it. What is new here: a reading of p03, readings of the words left as holes there, and others. See `docs/COMPARISON.en.md`.

**Status: full reading.** Of 3,869 cipher tokens, 3,727 (**96.3%**, per token) read as words.
**By the stricter per-word count, 3,575 (92.4%), which is under 95%.** The difference is how a word with one wrong token is treated (23 words, apparently the writer's slips).
Both ways of counting are in "Figures" below. The per-token count was adopted after the per-word result had been seen, so please read the two together.

## What it says

An objection to the church establishment for India urged by Claudius Buchanan's *Memoir of the Expediency of an Ecclesiastical Establishment for British India*. Barlow writes that:

- toleration of Indian religions is the "main foundation" of "our eastern empire";
- if the fear spread that government meant to convert its subjects, the pledge of non-interference given by Act of the legislature would be broken and the empire's foundation endangered;
- the fear lately entertained by "our native troops on the coast" (we take this as the Vellore mutiny of 1806; that is our inference, the letter does not name it) would seem confirmed by the establishment;
- government has repeatedly restrained religious disputation in the college of Fort William (a value inferred from code 4845);
- the religious interests of the community in India are best served by placing clergymen of good character.

Full text: `data/fulltext.txt`; commentary: `docs/READING.en.md`.

## Method of the cipher

A homophonic substitution of parts of English words by two-digit numbers. Words are divided by points, and vowels are often omitted (govt, mnstrs).
Letters have several numbers (t = 44, 77, 50; n = 90, 70, 83; and others), and some numbers are nulls (11, 20, 21, 22, 2, 1, 100, 1100, 2200; 10 and 12 are sometimes null).
The four-digit 4990, 5650 and 4845 are word codes, with values inferred from context (India, British, Fort William). The values of 4087, 5089 and 4600 are unknown.
Sign table: `data/key.tsv`.

## Figures

| Item | Value |
|---|---|
| Cipher tokens (excluding words of nulls only) | 3,869 (703 words, all 19 pages) |
| Read as words, per token (only the wrong token of a slip counts as failing) | 3,727 (96.3%). Slip tokens 24, words not read 6, uncertain or code 112 (2.9%) |
| Read as words, per word (one wrong token fails the whole word) | 3,575 (92.4%). Failing 182 (4.7%), uncertain or code 112 (2.9%) |
| Control (letter values shuffled 1000 times) | 0 at or above the real key (words whose consonant skeleton matches an English word: real 516/703, shuffled mean 243.9, max 369) |
| Control (values of the 32 signs seen 12 times or fewer shuffled 1000 times) | 0 at or above the real key (real 516, mean 474.2, max 492) |
| Agreement with other readers (values) | Claude Sonnet, 19 pages, 93.3% (lowest page p16, 87.7%). OpenAI Codex, 19 pages, 91.0% (before corrections to the first reading), 91.3% (after; lowest page p12, 83.5%) |
| Calibration | None (no contemporary decipherment or edition was found) |

Both word-count figures use relaxations (u=v, i=j, doubled letters count once, 10 and 12 may be skipped, 19 is a or e, 56 is y or w). Some were added after the reading was made. All are listed in `docs/METHOD.en.md`.

## Human checking

**No person has checked this transcription.** The transcription and the reading were made by AI. Agreement between AIs does not replace human checking.

## Relation to earlier work

The earlier work is WAINUT's reading (see the top of this file, `docs/COMPARISON.en.md`, `docs/PRIOR_CHECK.en.md`). We do not claim this is the first. The original Grenville papers, the Barlow papers and part of the printed sources were not seen.

## Use of AI

Fetching the images, transcription, key recovery, controls and this text were done by AI (Anthropic Claude).
The second readings were made by Claude Sonnet and OpenAI Codex (codex-cli 0.163.0-alpha.10.2, gpt-6-astra, reasoning high) from the images alone, without the first reading or the key.
People gave the instructions and made the decision to publish.

## Contents

- `data/tr1.txt` transcription (after corrections); `data/tr1_before_corrections.txt` before.
- `data/key.txt`, `data/key.tsv` key; `data/reading.txt` word-by-word reading; `data/fulltext.txt` full text.
- `data/image_check.tsv` all two-choice image questions and answers.
- `second/` second readings (Sonnet, Codex) and the prompt.
- `src/` measuring programs (`python3 src/measure.py`, `src/control.py`, `src/agreement.py sonnet`, `src/compare.py`). Measuring needs `pip install wordfreq`.
- `docs/` METHOD, OPEN, READING, COMPARISON, PRIOR_CHECK.
- `SOURCES.en.md` source and page order.
