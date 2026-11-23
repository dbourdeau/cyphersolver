# Frozen record of the 9 May comparison

These are the files of the registered comparison as they stood on 20 November 2026, byte for byte, with the Cotton transcription it was scored against.

| File | What it is |
| --- | --- |
| [FREEZE.sha256](FREEZE.sha256) | Manifest of the plan, scorer, predictions, eligibility ledger and May inputs. SHA-256 `acac1ecba6eb90c693ecafad133483d291caf009fee4ebd81542b2014831c3a3`. Its names are paths in my working folders; [replay_registered.py](replay_registered.py) maps each to this repository. The plan it names is [../registered_plan.md](../registered_plan.md), unchanged. |
| [predictions.tsv](predictions.tsv) | The five mechanical predictions from the June row 2. |
| [eligibility.tsv](eligibility.tsv) | All 34 May groups and why each was or was not eligible. |
| [score.py](score.py) | The registered scorer, run once. |
| [result.json](result.json), [controls.tsv](controls.tsv), [outcome.tsv](outcome.tsv) | Its outputs: a miss, two exact words, all 1,000 controls. |
| [cotton/transcript_329r.txt](cotton/transcript_329r.txt), [cotton/transcript_329v.txt](cotton/transcript_329v.txt) | The independent reader's transcription of Cotton MS Caligula B VIII, f. 329r and 329v, with the time stamps written into them: 22:37:01 and 22:38:54 UTC. |
| [cotton/reference_329r.tsv](cotton/reference_329r.tsv), [cotton/reference_329v.tsv](cotton/reference_329v.tsv), [cotton/reference_combined.tsv](cotton/reference_combined.tsv) | The same text as folio, line and text tables, and the two joined, which is the file the scorer read (SHA-256 `9ad617375420ceb526d90850339932370caf5d4e6751b7731bb882e62f99aaf6`). |
| [REFERENCE_PROMPT.md](REFERENCE_PROMPT.md) | The instructions given to that reader. |
| [CROP_CHECK.md](CROP_CHECK.md) | A check that the May crops are reproducible from the archived image. |

Run `python3 -I -B replay_registered.py` from this folder. It checks the ten text files named in the manifest, then reruns `score.py` unchanged on `cotton/reference_combined.tsv` and compares `result.json` and all 1,000 controls byte for byte. The two manuscript crops named in the manifest are not included, so their two lines are reported and not checked.

On timing: the transcripts carry their own time stamps. The manifest has none of its own. 22:39:30 UTC is the modification time of `FREEZE.sha256`, `registered_plan.md` and `score.py` on my machine, and the reference tables were written at 22:40:44 UTC. Local file times are not independent proof of order. The Cotton reader was a separate agent on gpt-6.2-astra. The investigator had seen the May interlinear writing and knew the June alphabet, as the [README](../README.md) says.

The transcription is made from the Gale State Papers Online image, which stays local; only the reading is given here.

AI agents did this work; no person has checked it.
