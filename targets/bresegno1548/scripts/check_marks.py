#!/usr/bin/env python3
"""Mark check for bresegno1548. Standard library only.

    python scripts/check_marks.py

1. Rebuilds the decryption from transcription_c15r.txt and key.tsv and compares it with decryption_c15r.txt.
2. Runs `reading.py check`: walks the marked text of reading_c15r.md unit by unit against the signs and counts words.
Exit 1 on a stale decryption file or on any unmarked departure (or stale mark).
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / 'transcription_c15r.txt'), str(ROOT / 'key.tsv')],
                     capture_output=True, text=True, encoding='utf-8')
have = (ROOT / 'decryption_c15r.txt').read_text(encoding='utf-8')
if out.returncode or out.stdout.replace('\r\n', '\n') != have.replace('\r\n', '\n'):
    print('FAIL decryption_c15r.txt is not what decrypt.py gives from transcription_c15r.txt and key.tsv')
    sys.exit(1)
print('decryption_c15r.txt: rebuilt, identical', flush=True)
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode)
