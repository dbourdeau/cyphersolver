# Parallel session's work on the same slips (28-29 Oct 2026)

A second session worked this target at the same time (from catalogue leads 1307/1312) and handed its results over
unpushed (its branch `writeup-visconti1446`, 0148c6e1c). What was merged into this folder:

- `../texts/f110_transcription.tsv`, `f110_alignment.md`, `f110_en.md`, `f110_copy1597.md`, and the f. 110 reading
  (via `../texts/import_f110.py`): its pass 2 of f. 110, aligned with the 19th-c. copy in BnF ital. 1597.
- `../texts/f136_copy1597.md` (copy of f. 136 in ital. 1597, canvas 157) and its own f. 136 alignment
  (`f136_transcription_peer.tsv`, `f136_alignment_peer.md`); `f158_copy1597.md` (a different clear letter, not f. 158).
- `key.md` (DECODE R1857 image 17, a second copy of the R5323 key) and `working_key.md` (its corrections).
- `WORKLOG.md` (every step it took, failures included), `NOTES_peer.md`, `slips.tsv` (survey of ital. 1584 and 1583:
  which slips have contemporary decipherments and later copies), `lattice.py` (an LM beam decoder that failed its
  control on f. 136) and `measure.py`. The scripts refer to that session's file names (`texts/f136_transcription.tsv`
  etc.) and are kept as a record, not rerun here.

Not merged: its readings of ff. 130, 154 and 158 (this folder's are fuller) and its site page.
