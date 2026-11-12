# Timestamps

Two stamps, each an RFC 3161 token from the Sectigo public time-stamping service over the SHA-256 of a manifest, with an OpenTimestamps proof for the same file.

| Folder | What the manifest lists | Manifest SHA-256 | Token time |
|---|---|---|---|
| `first/` | 134 work files (texts, scripts, outputs and images) of the solve and the prove-up, as they stood | `4916ac77edb84a449cf314db7818c1dbc76cc132274d84c1e90797e5025ed82b` | 11 Nov 2026 21:08:07 GMT |
| `blind_shape_test/` | the 6 files of the blind shape test | `5dccbdf7fc22f251d76b0820f3cebbd604bc91138156d05c38319ed443f67fc8` | 11 Nov 2026 21:10:37 GMT |

In each folder: `MANIFEST.sha256` (the list), `MANIFEST.sha256.tsr` (the token), `MANIFEST.sha256.tsq` (the request), `MANIFEST.sha256.ots` (OpenTimestamps, submitted 11 Nov 2026, not upgraded to a Bitcoin attestation when this folder was made), `STAMP.txt` (our note of the stamp) and `stamped/`, files byte for byte as stamped. The manifest paths begin with our work-folder names (`b56_...` the solve, `b64_...` the prove-up, `b68_...` the blind shape test).

| File in `first/stamped/` | Manifest line ends | Same text elsewhere in this folder |
|---|---|---|
| rossiA_c31_pass1.txt | b56_rossi_gosellini/tx/rossiA_c31_pass1.txt | transcription_A.txt (identical) |
| rossiB_c33_pass1.txt | b56_rossi_gosellini/tx/rossiB_c33_pass1.txt | transcription_B.txt (identical) |
| KEY_pass1.tsv | b56_rossi_gosellini/work/KEY_pass1.tsv | key.tsv (same values; counts, notes and the d value of P added) |
| READING.txt | b56_rossi_gosellini/work/READING.txt | the R lines of decryption_A.txt and decryption_B.txt (identical) |
| PLAINTEXT_GIST.txt | b56_rossi_gosellini/work/PLAINTEXT_GIST.txt | first form of reading_A.md and reading_B.md |
| R2.txt | b64_rossi_proveup/blind/R2.txt | transcription_blind.txt (identical) |
| dt_verdicts.tsv | b64_rossi_proveup/work/dt_verdicts.tsv | shape_verdicts_nonblind.tsv holds the same verdicts keyed by unit |
| strict.out | b64_rossi_proveup/work/strict.out | counts.txt reproduces its consensus figures |

`blind_shape_test/stamped/` holds all six files of that manifest: the classifier's raw labels (`blind_set_labels.tsv`), the labels as scored (`blind_set_labels_Ponly.tsv`), the two score outputs, the map from crop id to unit (`map.tsv`) and the freeze note. The 358 crops are images and are not here.

The other 126 files of the first manifest (images, scripts, logs, other outputs) are not in this folder; their lines cannot be checked from it.

## How to verify

1. Files against the manifest: `sha256sum first/stamped/READING.txt` and compare with the manifest line that ends in `work/READING.txt`; the same for the others.
2. Manifest against the token: `sha256sum first/MANIFEST.sha256` gives the hash in the table; `openssl ts -reply -in first/MANIFEST.sha256.tsr -text` shows the same hash under "Message data", the time and the signer.
3. The token's signature: `openssl ts -verify -data first/MANIFEST.sha256 -in first/MANIFEST.sha256.tsr -CAfile <Sectigo time-stamping chain>`. The chain is not in this folder; Sectigo publishes it.
4. OpenTimestamps: `ots upgrade`, then `ots verify` on the `.ots` file (needs the OpenTimestamps client and a view of the Bitcoin chain).

Done here on 12 Nov 2026: step 1 for all 14 stamped files (all match) and step 2 for both stamps (message hash equals the manifest hash; times as in the table). Not done: steps 3 and 4.

What the stamps show: that the frozen transcription, the key, the aligned reading, the blind second transcription, the shape verdicts and the blind shape labels existed by those times. They say nothing about the files written on 12 Nov 2026 for this folder (the sentences, the translation, holes.md, the per-page counts).
