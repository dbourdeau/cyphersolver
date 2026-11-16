# kn.sh term... : known.py, files with hits only
cd "$(dirname "$0")/../.." && for t in "$@"; do echo "== $t"; python -I -X utf8 research/archive_sweep_2026-10/known.py "$t" 2>&1 | grep -v "^==" | grep -o "^  [^:]*:\|no hits" | sort | uniq -c | head -12; done
