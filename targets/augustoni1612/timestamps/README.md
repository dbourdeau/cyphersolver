# Timestamps

Two stamps, each an RFC 3161 token from the Sectigo public time-stamping service over the SHA-256 of a manifest, with an OpenTimestamps proof for the same file.

| Folder | What the manifest lists | Manifest SHA-256 | Token time |
|---|---|---|---|
| `first/` | 19 work files of the first reading: the key, the first reader's two transcriptions, the blind second transcription and its counts | `9ec388c133424ffad2a6d5076c6f56f41b0f0a7233f3f667da5c66da21f2b0dd` | 11 Nov 2026 21:08:13 GMT |
| `repair/` | 55 files of the decoder, alias, override and ledger work | `9949464c5570e2f8182abdb22f376edbc93cffc248290e419f4ad11ad4abc2e4` | 11 Nov 2026 21:22:32 GMT |

In each folder: `MANIFEST.sha256` (the list), `MANIFEST.sha256.tsr` (the token), `MANIFEST.sha256.tsq` (the request), `MANIFEST.sha256.ots` (OpenTimestamps, submitted 11 Nov 2026, not upgraded to a Bitcoin attestation when this folder was made), `STAMP.txt` (our note of the stamp) and `stamped/`, files byte for byte as stamped. Manifest paths begin with our work-folder names (`b48_...` the first solve, `b55_...` the blind reader, `b72_...` the repair); the second manifest has them as absolute paths on the machine used.

Check, from `first/` or `repair/`: `sha256sum MANIFEST.sha256` gives the hash above; `openssl ts -reply -in MANIFEST.sha256.tsr -text` shows the same hash as message data and the time; for each file in `stamped/`, `sha256sum` gives the hash on the manifest line that ends with its name. We did this on 12 Nov 2026: all 25 files match, and both tokens carry their manifest's hash. The tokens' signature chain and the OpenTimestamps proofs were not verified.

| File in `first/stamped/` | Manifest line ends | Same text elsewhere in this folder |
|---|---|---|
| KEY_aug1612.tsv | b48_moonshot_triage/KEY_aug1612.tsv | the values of `key.tsv` |
| aug_pass1.txt | b48_moonshot_triage/tx/aug_pass1.txt | the first transcription, on which the solver ran |
| aug_pass2.txt | b48_moonshot_triage/tx/aug_pass2.txt | the same reader's second transcription, not blind |
| frozen.md5 | b48_moonshot_triage/tx/frozen.md5 | md5 of the two (its third line is a file of another target) |
| aug_R2.txt | b55_augustoni_cpp/tx/aug_R2.txt | `transcription_blind.txt` (identical) |
| frozen_R2.md5 | b55_augustoni_cpp/tx/frozen_R2.md5 | md5 of the blind transcription at its freeze |
| aug_consensus_plaintext.txt | b55_augustoni_cpp/tx/aug_consensus_plaintext.txt | the first consensus reading, clear text approximate; superseded by `reading.md` |
| R2_dec_raw.out, R2_marks.tsv, R2_count.out, agree_R2_pass2.out | b55_augustoni_cpp/work/... | the blind transcription decoded, marked and counted on 11 Nov (535 of 600) |
| baseline_R2.out | b55_augustoni_cpp/work/baseline_R2.out | the shuffled-key control |

`repair/stamped/` holds 13 of the 55: `KEY.tsv`, `ALIASES.tsv`, `OVERRIDES.tsv`, `WORDS.tsv` (the contract), `contract.py` and `make_words.py` (the decoder and the word-table maker; they hold the absolute paths of our machine and do not run from here), `LEDGER_units.tsv`, `COUNTS.txt`, `DECODE_consensus.txt`, `CHECKS.txt`, the two `DIFF_` files, and `CROPS.tsv` (pixel boxes of the crops on the 2390 x 3508 page image). `scripts/build.py` reads the four contract files and the ledger from here. The other 42 files of that manifest (37 crop images, a log, two crop scripts, two input notes) and 7 files of the first manifest (two page thumbnails, a transcription of another target, a second decode output, three duplicate copies) are not in this folder; their lines cannot be checked from it.

The stamps cover the state of the work on 11 Nov 2026. `transcription.txt`, `review.tsv`, `reading.md`, `translation.md`, `holes.md` and the files `scripts/build.py` makes are of 12 Nov 2026 and are not stamped.
