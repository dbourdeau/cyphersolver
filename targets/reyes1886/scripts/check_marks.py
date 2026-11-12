#!/usr/bin/env python3
"""Mark check for target 1447.   python scripts/check_marks.py

1. Rebuilds decryption_634.txt from transcription_634.txt and key_frozen.tsv; fails if it differs.
2. Runs `reading.py check`: every marked reading line must resolve to the mechanical decryption.
"""
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / 'transcription_634.txt'),
                      str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
have = (ROOT / 'decryption_634.txt').read_text(encoding='utf-8')
if out.returncode or out.stdout.replace('\r\n', '\n') != have.replace('\r\n', '\n'):
    print('FAIL decryption_634.txt is not what decrypt.py gives from transcription_634.txt and key_frozen.tsv')
    sys.exit(1)
print('decryption_634.txt: rebuilt, identical', flush=True)
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode)
