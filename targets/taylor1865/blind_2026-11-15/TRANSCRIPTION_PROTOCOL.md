# Transcription protocol and seed check (written 15 Nov 2026, before any reader started)

## Readers
Four helper readers (Claude Opus subagents), in two pairs. Each reader works blind: it is told not to open
anything in the project except its own images and its own folder, has not seen any earlier transcription,
decryption, key or the other reader's work, and is told not to decrypt.

- Pair A (vol. 196): readers A1, A2. Seed frame vol. 196 fr. 0061. Frames 0053, 0056, 0064, 0065, 0071.
- Pair B (vols. 11 and 10): readers B1, B2. Seed frame vol. 11 fr. 0039. Frames vol. 11 0044, 0045, 0046; vol. 10 0056.

Images: `sources/raw/taylor1865_open_2026-11-15/` (full NARA JPEGs, SHA256SUMS there).

## Notation
One cipher group per row: frame, telegram (dateline and addressee as the reader reads them), line, group number,
group as read. Doubtful letter: `[Y/V]`, preferred first. Illegible letter: `?`. Uncertain letter count: note it.

## Seed check (pass mark fixed now)
The seed telegrams have an established as-written transcription in the merged target (`alignment.tsv`, column of
letters as read, 12 Mar 1865 fr. 0061, 180 letters; 8 Apr 1865 fr. 0039, 61 letters). A reader's seed transcription is
compared group by group with the established as-written letters, taking each doubtful letter at the reader's
preferred form.

Pass: the same number of groups (plus or minus one) and at least 90% of letters agreeing position by position
within aligned groups. A reader that fails the seed check is rejected and its frames are read again by a new reader.
A miss is reported as a miss.

## Agreement measure (for the open frames)
Groups aligned by order within each telegram (by hand where a reader splits or joins a group). Reported per frame:
groups agreeing exactly, letters agreeing, and the list of disagreements. Each disagreement is settled by the
coordinator on the image (crop saved in `work/settle/`), or left as a two-way reading carried into the tests.
