# figueroa1534: the 0.873 measurement, as frozen (added 15 Nov 2026 for the review of PR #621)

Everything needed to re-run the single pre-registered measurement of 14 Nov 2026 on AGS Estado 1379,14-18
(PARES 3615615), cipher image 06, and to check that the figure comes out byte for byte:

    sh rerun.sh          # Python 3, standard library only; about one to two minutes

`rerun.sh` first checks the SHA-256 of every file (`SHA256SUMS`), then runs the scorer and compares its output with
the output recorded on 14 Nov (`MESURE-P-ATLAS.txt`). Run here with Python 3.9.6: byte-identical.

## Files (all byte-identical copies of the frozen files; original paths in the contributor's folder in brackets)

| file | what | SHA-256 | frozen |
|---|---|---|---|
| `PREREG-ATLAS.md` [PREREG-ATLAS.md] | the pre-registration (French), written and frozen before any look at 1547 images 04 and 06 | 6d666ab4…84d1 | 14 Nov 2026 12:59 CET |
| `PREREG-ATLAS.sha256` | the freeze record as written at 12:59, with its original paths | (lists the files below) | 12:59 |
| `LABELS-FORMES.md` [working/p-atlas/] | the shape labels the three transcribers used, without values (French) | e0485fbc…513d | 12:59 |
| `K4.tsv` [working/ags1545/] | the key table: sign label, value, source (Tomokiyo/Masiá values completed by the 1545 AGS table) | a456e5bb…32ed6 | before any look at 1547 image 05 (14 Nov), unchanged since |
| `score_atlas.py` [cryptanalysis/p-atlas/] | the scorer: mechanical decode, reference window, character precision, both sets of 200 controls, verdict | 21ed80a2…baa7 | 12:59 |
| `score_k4.py` [cryptanalysis/c05/] | the earlier scorer, whole-key controls only; run as the PREREG says, its three summary lines close the record | 536a871b…58fe5 | 12:59 |
| `atlas.tsv` [working/atlas-estense/] | the shape atlas from the Estense Campori letters (labels and boxes only; the crops and plates are images and are not included) | 4ba643ea…65eb | 12:59 (`ATLAS.sha256`) |
| `img06_ARB.txt` [working/p-atlas/] | the held-out cipher image 06, arbitrated shape transcription (492 signs; pass A, pass B and arbitration by three separate blind sub-agents) | 4d7be1c3…b62eb378 | 13:23, before the clear copy was read (`T-IMG06.sha256`) |
| `clear_1547_ref_img06.txt` [working/p-atlas/] | the clear copy of the time (1379,14-18 clear images 13-16), **our transcription**, read after 13:23 | 40555165…4fb2 | used as read |
| `MESURE-P-ATLAS.txt` [working/p-atlas/] | the recorded output of the one measurement | 042c248c…6577 | 13:25 |

`targets/figueroa1534/transcriptions/1379_14-18_img06.txt` is the same transcription as `img06_ARB.txt`, laid out
like the other transcriptions (signs separated by spaces, with a header); the scorer reads the `|`-separated file.

## What the figure is

Character precision of the mechanical decode against the window of the clear copy that a local alignment picks
(Smith-Waterman +2/-1/-1, ±40 characters): LCS / decoded length = **0.873** (794 decoded characters, window of 888,
clear characters 2165-2973). Controls, 200 each, seed 744: values permuted inside letter / syllable / code / null
classes, max **0.477** (the threshold plan); values permuted over the whole key, max 0.449. Signs outside the key
4.1%. Thresholds written before: ≥ 0.85, ≥ best within-class control + 0.30, ≤ 20% outside the key: passed.
Image 06 is spent. Image 04, untouched at the time, was measured on 15 Nov under a frozen amendment (K4 0.887): see `img04/README.md`; both images are now spent.

## Declared deviation (in the PREREG itself)

Before the freeze the orchestrating agent saw on screen about 400 characters of the clear copy that very probably
match the first lines of image 06. Hence it did no transcription: pass A, pass B and the arbitration were done by
three separate sub-agents that never saw the clear copy, the values or the earlier transcriptions. The order of the
freezes rests on the contributor's record (local SHA-256 files and times), not on a public time stamp.

## Images

No image or crop is included. AGS images are marked "Prohibida la reproducción" on PARES; the files here are text
only: our own transcriptions of a 1547 document and of its shapes, our key table and our scripts. We did not
re-read the AGS terms online for this push; if Daniel or AGS read them as covering transcriptions too, the clear
file can be withdrawn and the figure re-run by anyone with PARES access from the same steps.
