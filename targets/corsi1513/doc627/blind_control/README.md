# Doc 627 control: blind test of the frozen Corsi key (w17)

Status: packet built 16 Nov 2026; blind transcription not yet done; decode NOT run.

## Purpose
The Corsi key was built from the contemporary decipherment at the foot of doc 627 (MAP CXXXVII, c.635r). This control asks: does a blind sign-by-sign transcription of 627's cipher block, decoded once with the frozen key, reproduce that decipherment, and by more than chance?

## Inputs (fixed)
- Image: /mnt/user-data/uploads/codebreaking/corsi_img/map137_A0001353.jpg, md5 d54b593af4bf28749aed6947433988a8.
- Key: /home/claude/wt_cv/targets/corsi1513/key_corsi_w17_frozen.json, sha256 5f56ad5879c6d53d9c865d52096fde97fbe831e6fcca924efe83a5247c732940.
- Reference: /home/claude/wt_cv/targets/corsi1513/doc627/decipherment_627.txt (never shown to the transcriber or the decoder).

## Packet (/tmp/corsi627_packet/)
Cipher block only (5 lines, 'q x s3 z o7 ...' to '... w x g q7'), cut by crop.py at full-res boxes y 598-905; line 5 cut at x 372 so the clear text after it is excluded. No clear lines and no decipherment are in any image (checked by eye). SHEET.md uses neutral labels S01-S42 in random order (seed 627635) with stroke-only shape words; build_sheet.py checks that no label or description holds a letter name, single-letter word or key token. The label-to-key map is private (private/LABELS_TO_KEY.tsv) and never enters the packet. Ko, L2, Ri and GR are described from earlier notes only (not checked on this page) and the sheet says so.

## Steps
1. A fresh reader with only the packet follows PROMPT.txt and writes BLIND.tsv and BLIND_NOTES.md.
2. Freeze: `sha256sum /tmp/corsi627_packet/BLIND.tsv > FREEZE_blind.txt` (plus UTC time); copy BLIND.tsv here. No edits after the freeze.
3. Decode once: `python3 -I /home/claude/corsi627_control/decode_once.py`. It refuses a rerun, a changed key or an unfrozen BLIND.tsv. The first pass is the figure of record; any emendation is listed separately and never replaces it.

## Scoring plan (set before the decode)
- Strict judge: a separate agent, given only decode_once.txt and decipherment_627.txt, aligns them and scores per letter (match / mismatch / hole), with per-line figures and the whole-block figure. No pooling with other documents. Our own 65% line binds us.
- Chance control: 5,000 shuffles at each of seeds 20261112 and 7, same method as corsi1513/blind633/shuffle.py (dictionary-cover score of the real decode vs decodes with the key values shuffled within the bare, base and vowel classes); report count >= real and max.
- Caveat for the write-up: 627 is the document the key was built from, so this is a transcription-and-key consistency check, not an independent decipherment.
