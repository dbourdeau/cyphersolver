# Van Spaen's Vienna code, 1807

This local evidence draft contains two blind-read held-out dispatches, the training witness, three recorded tests, and the evidence for individual candidate values. Start with the [findings and archival sources](NOTES.md). The [reader's tables](TABLES.md) identify the manuscripts, symbol conventions and data files.

## Verify the evidence

From the folder containing this directory, run the following command. Within the directory, use the same command with the folder prefix removed. Python 3.9 or later and its standard library are sufficient.

```sh
python3 -I -B vienna_contribution/verify.py
```

The verifier checks the bundle inventory and historical hashes, rebuilds all four position tables, derives the candidate key from the two archived alignment paths, and replays the January and two March evaluations. It compares every row of the original predictions, matched occurrences, shuffled control scores and support tables. The two fitted training alignments are archived inputs to this check. It does not refit their parameters. The replay has access to the sealed reference files from the outset and cannot independently verify what an investigator saw at the time of the historical run. It creates and discards its own temporary directory and leaves the evidence files untouched. The March result lines should give 32/43 and 48/61, with the best of 1,000 shuffled tables scoring 16 and 20 respectively. The January miss should give 2/5, with 226 controls equal or better.

## Provenance and paths

The original protocols, timestamped commitments, candidate key, reader transcriptions, reference texts and machine outputs are byte-for-byte copies. Their filenames retain the dates of the working project. [PATH_MAP.tsv](PATH_MAP.tsv) maps each original workspace-relative path to its path here. The five plan and prediction manifests retain their original paths. The two reference seals name files relative to [references](references). The verifier resolves these names without access to the original workspace.

Three entries in the 21 March training plan are hashes of local source-image crops. The bundle retains their commitment lines and identifies each as “image checksum only” in the path map. Those image bytes are external to this evidence draft. The original scans are in the Nationaal Archief inventory cited in the notes. The single-reader French transcription of the training body and the two separately sealed held-out transcriptions are included.

[SHA256SUMS](SHA256SUMS) inventories every bundle file apart from the list itself. The independently recorded No. 26 and No. 21 prediction-manifest hashes are, respectively, a2e1f6a8782149f6ef15bdc80ed3307bd0080a8db2a375d9aa590bb9239f464f and 8742edc42017879cd87a2fa5d8fa1b160625f2f0c5fc3181b1a84825d62db91c. Local timestamped records document ordering; no third-party timestamp authority was used.

AI agents did this work; no person has checked it.
