# Frame 278 glosses and the frame-4 name-sign booklet as checks of the key (Beling addition)

Andrew Beling, with AI agents, 11 Nov 2026 (files dated by our local record only; no external timestamp). Filed as
they ran, in their original layout, so that the scripts and SHA-256 lists work unchanged:

    python3 -I scripts/build_key.py .      # key.json from the booklet's left page
    python3 -I scripts/heldout_test.py .   # pre-registered test on the booklet's right page
    python3 -I scripts/check_0278.py .     # pre-registered test on the frame-278 gloss pairs
    shasum -a 256 -c results/key.sha256 results/frozen_inputs.sha256 results/frozen_inputs_0278.sha256

(run from this folder). `transcription/f5_cipher_as_seen.txt` is here only because `results/frozen_inputs.sha256`
lists it; our f.5 reading is not part of this addition.

## What was done

1. **Booklet, Nr. 530 frame 4** (name signs with the cipher spelling and the clear name; this folder files the
   Catalogus from frame 3; whether frame 4 is the next opening of the same booklet was not checked here). `PREREG.md` was written before any key file existed. A letter key was built from the left page only by
   position-wise majority votes (`scripts/build_key.py`, `results/key.json`, SHA-256 e638f434...) and tested once on
   the right page: 0.8659 of the clear letters matched, best of 200 shuffled keys 0.2793, margin 0.5866; the
   pre-registered bar (0.85 and margin 0.30) was met (`results/heldout_result.json`).
2. **Frame 278** ("Signatura catalogi sive clavis"). `PREREG2_frame0278.md` was written before the transcription
   files existed. 23 pairs of a cipher spelling with a legible period clear gloss (name entries such as Mylonius,
   Lampadius, Secretarii, and glossed words in the cipher passage) were decoded with the same frozen booklet key:
   0.8889 of the clear letters matched, best of 200 shuffled keys 0.4314, margin 0.4575; pass by the same bar
   (`results/check_0278_result.json`).
3. **Rescored with the envoys' worksheet key** (frame 168, the key of this folder), 13 Nov 2026, descriptive only,
   not pre-registered: `python3 -I ../../scripts/beling_build.py --frame278` gives 146/153 = 0.9542 of the clear
   letters and 18 of 23 words exact (`worksheet_rescore.txt`). The misses are the reader's c/o, q/g and one dropped
   letter (e.g. "difficultatzn"), not the key.

## Limits

- **Not blind.** As `PREREG2_frame0278.md` says, the reader had looked at frame 278 and decoded four or five names by
  eye before transcribing. The glyph readings may lean toward the key.
- The booklet key differs from the worksheet key in two letters: it has cipher m = p and p = m, where the worksheet has
  m = x and p = w (`results/key.json`; the transcription wrote the W-shaped glyph as m).
  These tests confirm the same reciprocal table from two further period sources; they do not add a new key.
- Only the legible gloss pairs were used. The name signs of frame 278 were not valued, and the glossed cipher passage
  was not read as a text.
- This fills the folder's gap "frame 278 ... not compared with KEY_v2" only for the gloss pairs. The contributor said on
  PR #524 (13 Nov 2026) that he will use frame 278, as the maintainer suggested, for a further reading of f.102,
  f.104 and f.204; that work is his and is not attempted here.
