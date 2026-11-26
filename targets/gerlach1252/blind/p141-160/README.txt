gerlach1252 blind pass of pp.141-160 (24 Nov 2026): three batches, each a separate blind transcription, one decode and one strict judge.

Batches (by scan; page numbers as written, MAPPING.tsv):
  A  scans 0134-0142             = pp.141-149
  B  scans 0144-0148, 0150-0153  = pp.151-155, 157, 148a, 149a, 150a   (scan 0143 = p.150 is in blind/p138-150; scan 0149 = p.156 left out: its opening is in the 11 Nov reading)
  C  scans 0154-0163             = pp.151a-157a, 158, 159, 160
Scans 0151-0160 carry a second page sequence 148a-157a (148a on a pasted corner patch); the main sequence resumes at scan 0161 = p.158.
pp.161-170 (scans 0164-0173) are not in this pass.

Each batch folder holds: PROMPT.txt and SHEET_v2.md (the packet, images not committed: see PACKET_INDEX.txt for IIIF URLs, md5 and sha256),
FREEZE.txt (hashes frozen before any transcription), BLIND.tsv and FREEZE_blind.txt (the blind transcription as handed over, frozen before the decode),
key_frozen.tsv (= ../../key_v2.tsv byte for byte), decode_once.py and decode_once.txt (one decode, no emendation), judge/ (BRIEF.txt and decode.txt =
all the judge was given; judge.tsv, JUDGE_NOTES.txt by the judge; RECOUNT.txt = the judge figures re-added by script), shuffle.py and shuffle_out.txt.
tools/ holds the scripts that ran the steps (after_blind.py, after_judge.py, fetch.sh); their sha256 are in each FREEZE.txt. Paths inside them are those of
the working folder (/home/claude/gerlach_next), not of this repository.

PAGE-LABEL CORRECTION AFTER THE BLIND PASS (batch B, scan 0150)
The batch B blind reader wrote the page number of scan 0150 as "157a" (18 lines). MAPPING.tsv, recorded from the scans before any transcription and hashed in
FREEZE.txt, gives scan 0150 as p.157 of the main sequence, and scan 0160 (batch C) carries "157a". On the image the number at the top corner of scan 0150 is
"157", with an "a" on the triangular corner piece beside it (a patch or fold); a person has not checked this against the volume.
The label is corrected to p.157 in the files outside blind/ (transcription_p141-160.tsv, decryption_p141-160.txt, reading_p141-160.md, translation_p141-160.md)
and in NOTES.md and profile.json. Only the page label changed: every token, letter and judge mark of those 18 lines is as frozen. The files in B/ (BLIND.tsv,
decode_once.txt, judge/*) are left exactly as written and still say "157a".
