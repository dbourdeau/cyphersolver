# Timestamp

One stamp: an RFC 3161 token from the Sectigo public time-stamping service over the SHA-256 of a manifest, with an OpenTimestamps proof for the same file.

| What the manifest lists | Manifest SHA-256 | Token time |
|---|---|---|
| 30 work files of the reading: the frozen transcriptions, the key, the ledgers, the blind third transcription, the adjudicated reading, the date and address-leaf notes, the two page images | `4fc23d8e26e4bba488ad205c858deb15a1363edc7e4b35a22eb88ad85be64bf0` | 11 Nov 2026 21:08:11 GMT |

Here: `MANIFEST.sha256` (the list), `MANIFEST.sha256.tsr` (the token), `MANIFEST.sha256.tsq` (the request), `MANIFEST.sha256.ots` (OpenTimestamps, submitted 11 Nov 2026, not upgraded to a Bitcoin attestation when this folder was made), `STAMP.txt` (our note of the stamp) and `stamped/`, 28 of the 30 files byte for byte as stamped. The two not here are the page images (`b43_444_pass3/work/444_315r.jpg` and `444_315v.jpg`, the archive's IIIF files). Manifest paths begin with our work-folder names; each file in `stamped/` has the name at the end of its manifest line.

Check: `sha256sum MANIFEST.sha256` gives the hash above; `openssl ts -reply -in MANIFEST.sha256.tsr -text` shows the same hash as message data and the time; for each file in `stamped/`, `sha256sum` gives the hash on the manifest line that ends with its name. We did this on 12 Nov 2026: all 30 files matched on our machine (28 of them are here), and the token carries the manifest's hash. The token's signature chain and the OpenTimestamps proof were not verified.

| File in `stamped/` | What it is |
|---|---|
| p2_r.txt, p2_v.txt | pass 2, the first reader's second transcription, frozen before pass 1 was reopened and before any decoding |
| consensus_reading.txt | pass 2 with the first reading marked sign by sign |
| KEY_pass3.tsv | the key |
| units3.tsv, verdicts.tsv, worklist.txt, six_units.tsv, extent.txt, rebuild.out, verify3.out | pass 3: per-unit classes, the image verdicts on 309 flagged units, the m/n tally, the shuffled-key control |
| reading_pass3_marked.txt, plaintext_final.txt | the pass-3 reading. The second clear line and the dateline in `plaintext_final.txt` are wrong (NOTES.md, "Errors of ours") |
| LEDGER_444.tsv, literal_layer.txt, normalised_layer.txt, recount.out | the per-unit ledger of 1,521 units and the recount with the codes not read (89.94%) |
| LITERAL_CHECKS.tsv, DATE_MATRIX.tsv, ADDRESS_LEAF.md, KEY_COMPARATOR.md, nullcontrol.out | checks of single words on crops, the date scoring of 11 Nov, the address leaf, the comparison with Babbi's cipher, the solver controls |
| R3.txt, clear.txt, draft_r.txt, draft_v.txt | the blind third transcription, its reading of the clear text, and its drafts |
| reading_adjudicated.txt, still_EN.tsv | the reading after adjudication and the 145 units not read (90.42%) |

Not stamped: pass 1 (`passes/`, three files, md5 `c12bfb01...`, `6269e65e...`, `b1fabec2...` in our freeze list of 11 Nov), `adjudication.tsv` (the 138 verdicts of 11 Nov; its outcome, `still_EN.tsv`, is stamped, and `scripts/build.py` checks one against the other), and everything made on 12 Nov 2026: `transcription.txt`, `decryption.txt`, `units.tsv`, `overrides.tsv`, `dropped_signs.tsv`, `key.tsv`, `counts.txt`, `reading.md`, `translation.md`, `holes.md`, `NOTES.md`.
