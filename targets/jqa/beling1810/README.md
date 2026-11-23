# Adams's despatches of 1810 (Nos. 21-29): a held-out test of `code_table.tsv`

Andrew Beling, with AI agents, 22 Nov 2026. These folders were not looked at by a person beyond what is said below.

The 1811-12 table in `../code_table.tsv` was rebuilt here without any 1810 material. Adams wrote in the same code (the = 1385) from St Petersburg in 1810. Seven of his despatches of August-October 1810 have coded passages, on NARA M35 reel 2. Six of those can be paired with a plaintext:
- No. 21 with Ford's print;
- Nos. 23, 24, 25, 27 and 28 with the decipherments made in the State Department and filed with them.

That makes them a test of the table on text it has never seen. The table, `align.py` and the clerk files are used unchanged; nothing in `..` is edited.

## Is any of it new?

The coded passages of four of these despatches are in print:
- **Ford**, *Writings of JQA* vol. 3 (1914), prints No. 21 (pp. 467-471; the coded sentence on p. 469, in italics, footnoted "Cypher"). It prints No. 23 (pp. 486-496; all seven coded passages, in italics, "Italics represent cypher") and No. 24 (pp. 503-507; all three, footnoted "Cypher"). No. 22 (pp. 475-480) has no code. Ford did not print Nos. 25-29. No. 25 appears only in a footnote extract of its clear text (p. 477).
- **No. 27**: both coded passages are printed in clear in *The United States and Russia: The Beginning of Relations, 1765-1815* (1980). Seen through the Internet Archive's full-text search of its loan copy `unitedstatesruss0000unse`, snippets only, page not seen. Romanzoff's line "more obstinate than you are aware of" is quoted in many histories. Adams's diary (*Memoirs* vol. 2) gives the same conversation.
- **ASP**: *American State Papers, Foreign Relations* vol. 3 prints none of Nos. 21-29 (OCR search of `americanstatepap_o03unit`). For vol. 5, p. 443, cited for No. 27 in a catalogue, no free OCR copy was found, and the full-text search found none of No. 27's phrases in any American State Papers item. Not seen.
- **Not found in print** (in the sources searched): Nos. 25 and 28 have their period decipherments only. No. 29 has no decipherment at all.

## Files

- `PLAN.md`, `PLAN.sha256`: the plan and pass mark, written and hashed at 22:40 EST on 22 Nov 2026, before the first run.
- `codes_1810.txt`: the 22 coded passages of Nos. 21, 23, 24, 25, 27 and 28, in the format of `../codes_ford.txt`. Each has its frame and witness, followed by our first transcription. The transcriptions are:
  - No. 21: the first rough reading.
  - Nos. 23 and 24: the source-first readings frozen before the period text was opened.
  - No. 25: the second pass, made before the witness.
  - Nos. 27 and 28: made after the period text had been read, so not blind.

  Witness texts: the period decipherments as read from frames 156-159, 169-172, 178-179 and 184. In No. 24-B, a crease hides five words; there Ford's wording is used. No. 21's witness is Ford's sentence.
- `heldout_1810.py`: the test, importing `../align.py`. `heldout_1810.txt` is its output: per passage, per despatch, pooled, the 100 shuffled tables, and the group-by-group alignment.
- `transcriptions/`: the two transcriptions of No. 21, No. 24 and No. 29, and their comparison (`compare_transcriptions.py`, `compare_no21.txt`, `compare_no24.txt`, `compare_no29.txt`). The second transcriptions of No. 24 and No. 29 were made blind by separate helper agents. They worked from the NARA images alone; no earlier transcription, table or plaintext was given. No. 21's second reading is from 22 Oct 2026, also source-only.
- `codes_1810_no24_second.txt`, `heldout_no24_second.txt`: after the registered run, No. 24 scored again on its blind second transcription. This is post hoc and not part of the pass mark.
- `decode_no29.py`, `no29_decode.txt`: No. 29 decoded with the key sheet alone (NARA M97 roll 13 frames 1056-1057, Weber WE028, as transcribed in `../../morris1813/beling/key/codebook_M97_13_transcription.csv`, unchanged), from both transcriptions. The table's value is given where it differs.
- `no29_reading.md`: No. 29 written as sentences from `no29_decode.txt` alone, by a model. It is labelled in the file as a reading made with the key sheet alone, with no plaintext witness, not checked by a person.

## Results

See `../NOTES.md`, section "Adams's despatches of 1810 (held-out test, 22 Nov 2026)".

## Images

The images are NARA microfilm M35 (Despatches from U.S. Ministers to Russia) reel 2, frames 137-189, on catalog.archives.gov. They are linked, not committed. The Massachusetts Historical Society's Adams Papers film was not used here and is not reproduced.
