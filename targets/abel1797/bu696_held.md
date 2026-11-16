# Bue 696 (Paris, 29 Oct - 24 Dec 1797): what this folder holds

HStA Stuttgart, A 16 a Bue 696, Bild 7-9, 29-31, 44, 50: Abel's reports to Duke Frederick II with ciphered words
and passages, each with the decipherment of the time written above the line in another hand.

No transcription of these passages is in the folder. The contributor (Brice Dudout, PR #563) transcribed 116
glossed words token by token and built the keys K1/K2 from them; of those files only the SHA-256 values were
delivered (`frozen/GEL-CLE.sha256`, `frozen/GEL-CLE-K2.sha256`):

| file named in frozen/GEL-CLE.sha256 | what it is, going by its name |
|---|---|
| transcription/train_pairs.tsv, transcription/train_codes.tsv, transcription/v0007.txt | training pairs, code list and Bild 7 |
| transcription/holdout_v0044.tsv, holdout_v0029.tsv, holdout_v0050.tsv | Bild 44, 29 and 50, held out for the first test |

What the folder records about Bue 696 (from `validation.txt`, `NOTES.md`, `profile.json`):

- Protocol v1 (key from 1797, Bild 44, 50 and 29 held out): characters 0.895, words 0.621 (the word bar of 0.75
  missed); best of 200 control keys 0.204 / 0.034. Not validated.
- K2 (all of Bue 696, 116 words) on Bue 702 Bild 16: characters 0.863, words 0.367. Not validated.
- The values learnt from Bue 696 are in `key.tsv` (K3 = K2 plus the votes of Bue 702 Bild 16).
- Bild 50: a later pencil gloss "Georgi" is wrong, the key reads "albert" and the clear paragraph that follows is
  about Albert (contributor's observation; not checked on the image in the integration check).

To supply the texts: the contributor's six transcription files (their hashes are frozen, so a copy can be
verified), or a new transcription from the Landesarchiv images. NOTES.md records the image address only in
abbreviated form ("bild.php?...&originalBilddatei=..."); on 14 Nov 2026 a request rebuilt from it returned "Es
konnte keine Verbindung zum Datenbankserver hergestellt werden", so the images were not opened in this pass.
