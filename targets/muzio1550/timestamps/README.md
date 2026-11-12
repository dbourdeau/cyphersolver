# Timestamps

What was stamped. `MANIFEST.sha256` lists the SHA-256 of 18 work files as they stood on 11 Nov 2026 at 21:08 UTC: the first-reader transcription, the key, the emendation list, the reading, the checks, the blind second transcription and the text sent as issue 405. The SHA-256 of the manifest itself is

    f76b80994e10953d843c087732d26b93bd0a0325ba61985f49bc67a9aaf55b4e

- `MANIFEST.sha256.tsr`: RFC 3161 token from the Sectigo public time-stamping service, time 11 Nov 2026 21:08:03 GMT, over that hash.
- `MANIFEST.sha256.ots`: OpenTimestamps proof for the same file. It was submitted on 11 Nov 2026 and had not been upgraded to a Bitcoin attestation when this folder was made.
- `stamped/`: six of the 18 files, byte for byte as stamped, so the manifest can be checked here. The other twelve (scripts, logs, work copies) are not in this folder; their lines in the manifest cannot be checked from it.

| File here | Manifest line | Later version in this folder |
|---|---|---|
| stamped/c3r_pass2.txt | b44_muzio_moonshot/tx/c3r_pass2.txt | transcription_c3r.txt (nine units corrected) |
| stamped/c5r_passage.txt | b44_muzio_moonshot/tx/c5r_passage.txt | transcription_c5.txt |
| stamped/KEY.tsv | b44_muzio_moonshot/work/KEY.tsv | key.tsv (same letter values; codes and status added) |
| stamped/EMEND.tsv | b44_muzio_moonshot/work/EMEND.tsv | emendations_c3r.tsv |
| stamped/READING_c3r.txt | b44_muzio_moonshot/work/READING_c3r.txt | reading_c3r.md |
| stamped/R2.txt | b51_muzio_blind/tx/R2.txt | transcription_c3r_blind.txt (identical) |

## How to verify

1. The files against the manifest: `sha256sum stamped/c3r_pass2.txt` and compare with the manifest line that ends in `tx/c3r_pass2.txt`; the same for the other five.
2. The manifest against the token: `sha256sum MANIFEST.sha256` gives the hash above; `openssl ts -reply -in MANIFEST.sha256.tsr -text` shows the same hash under "Message data", the time, and the signer.
3. The token's signature: `openssl ts -verify -data MANIFEST.sha256 -in MANIFEST.sha256.tsr -CAfile <Sectigo time-stamping chain>`. The chain is not in this folder; it is published by Sectigo.
4. OpenTimestamps: `ots upgrade MANIFEST.sha256.ots`, then `ots verify MANIFEST.sha256.ots` (needs the OpenTimestamps client and a view of the Bitcoin chain).

Done here on 12 Nov 2026: steps 1 and 2 (the six files match; the token's message hash equals the manifest hash; status Granted). Not done: step 3 (no chain to hand) and step 4.

What the stamp shows: that the key, the first transcription, the blind transcription and the reading of 11 Nov existed by that time. It says nothing about the corrections of 12 Nov, which are later.
