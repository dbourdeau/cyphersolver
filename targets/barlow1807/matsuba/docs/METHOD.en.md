# Method and limits

## Transcription
First reading: Claude read the images by eye (`data/tr1_before_corrections.txt`). Two rounds of correction followed.

1. Disagreements with other readers and failing words were looked at in the image and corrected (42 lines of diff). These rest on Claude's eye alone.
2. Failing and uncertain words were looked at in line crops, giving 38 candidate corrections, which two separate models (Claude Sonnet, OpenAI Codex) judged independently in a **two-choice test without plaintext**. The question was only "is the number between these neighbours A or B", and which was the first reading was hidden.

   | Group | Result |
   |---|---|
   | 38 candidates | Both models chose the new value 8, both the old value 15, only Sonnet the new value 2, only Codex the new value 8, no agreement 5 |
   | 80 sampled agreed tokens | Chose the original value: Sonnet 80, Codex 79 |
   | 10 planted errors (choice against a similar-looking number) | Chose correctly: Sonnet 10, Codex 10 |
   | Question about dot marks | YES on 8 candidates: Sonnet 7, Codex 6; on 6 controls: 0 for both |

   Only the 8 places where both models agreed were changed. The rest were left. Where both chose the old value, the word is often wrong but the pen wrote it so (taken as the writer's slips). Contextual guesses were supported only 8 times in 38, so corrections from context should not be trusted. Everything is in `data/image_check.tsv`.
   In addition, a 75 where both models saw dots (in the word efforts) was marked `~75`, and 48,45 changed to 4845 (Sonnet and Codex both read 4845 in their second readings).

Only the Sonnet answers from the run with question numbers burned into the images are used; two earlier runs failed (images were not displayed because of an image limit, and some answers had been written unseen).

## Second readings
Claude Sonnet: all 19 pages, three bands per page read one at a time. Ten pages (p15 p16 p17 p03 p05 p07 p09 p11 p19 p14) were read after correction round 1 and nine after round 2. Overall 93.3% (values, of 3,915), names 93.1%.

OpenAI Codex (codex-cli 0.163.0-alpha.10.2, gpt-6-astra, reasoning high, three bands at 2048 px, run from an empty folder, no commands executed): all 19 pages. A usage limit delayed p14 and p19. 91.0% in values against the first reading before corrections (of 3,925), 91.3% after (of 3,927).

How compared: the closing point of a word can look like 0 or 1, so three-digit readings keep their first two digits; four digits are split in two against a missed comma (same treatment on both readings). Unnormalised agreement is lower. Per-page values come from `src/agreement.py` (lowest: Sonnet p16 87.7%, Codex p12 83.5%).

Limits on independence:
- Sonnet belongs to the same Claude family as the first reader.
- Codex's 91.3% is measured after corrections made on seeing disagreements, so it is not independent. The independent figure is 91.0%.
- Range seen: the lines of all 33 failing words and of the uncertain words were looked at (the line of word 504 only in the two-choice test, not by the first reader). Of the agreed tokens only the 90 sampled were checked; the rest rest on agreement of the two readings.

## Counting words
`data/reading.txt` holds the reading word by word. A word passes if the reading is an English word and the letters by the key are a subsequence of its spelling (subsequence because vowels are omitted). Words marked ? and codes do not pass.

Relaxations (all raise the figures): u=v, i=j; doubled letters count once; 10 and 12 may be skipped; 19 is a or e; 56 is y or w (duty, piety and what, with). These were set by looking at how the key is used, and some were added after the reading was made. The dictionary is wordfreq, /usr/share/dict/words and a short list (revd, buchanan, mussulmans, irremidiable, judgement, chimerical); a form minus its last letter is allowed.

**Both per-word and per-token figures are given.** The catalogue's standard ("95% of tokens make sense") is per token. But in this letter the per-word count was measured first (89.8%, then 92.9% after corrections), and the per-token figure was added afterwards (96.7%). Codex's two-choice answers then put three places back, giving 92.4% per word and 96.3% per token. Per token, in a word that is read but where one or two tokens do not fit, only those tokens fail (if more than a third of the word's tokens do not fit, the whole word fails; the 2 and the one third were set to keep this to words saved by an isolated slip).

The reading was made by fitting words to context, so the subsequence test is loose by nature. The only check that does not depend on the reading is the control.

## Controls
Letter values were shuffled 1000 times and the number of number-words whose skeleton (vowels removed) equals that of one of the top 40,000 English words was compared (`src/control.py`). A second shuffle moved only the signs with few occurrences (the 32 seen 12 times or fewer). Neither reached the real key in any run.

## Calibration
None. No contemporary decipherment or edition was found. Whether another copy (the letter says "Quadruplicate", so more should exist) survives in the Grenville papers was not checked.

## Comparison with the earlier reading
See `docs/COMPARISON.en.md`.

## Other limits
- Images are 1102 px wide; nothing larger was found.
- All key values were set from context. There is no independent key.
- The values of word codes 4087, 5089 and 4600 are unknown.
