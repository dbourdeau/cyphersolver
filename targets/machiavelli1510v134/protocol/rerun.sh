#!/bin/sh
# Re-run the single pre-registered measure (the frozen files are used as they are; their SHA-256 are in *.sha256).
set -e
H=$(cd "$(dirname "$0")/.." && pwd); D=$(mktemp -d)
cp "$H/key/KEY.tsv" "$H/key/decode.py" "$H/transcription/T_V131_final.txt" "$H/protocol/ref_V131_opere6_ocr.txt" "$H/protocol/measure.py" "$D/"
cd "$D" && python3 -I measure.py
