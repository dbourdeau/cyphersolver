#!/usr/bin/env python3
"""Mark check for target 2346 (Griffoli). Standard library only.

    python scripts/check_marks.py

1. Rebuilds decryption_<doc>.txt from transcription_<doc>.txt and key.tsv for k316, c315, c25; fails if any differs.
2. Runs `reading.py check`: every marked reading line must resolve to the mechanical decryption; prints word counts.
Exit 1 on a stale decryption file or on any unmarked departure.
"""
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
for d in ['k316', 'c315', 'c25']:
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / f'transcription_{d}.txt'), str(ROOT / 'key.tsv')],
                         capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / f'decryption_{d}.txt').read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n') != have.replace('\r\n', '\n'):
        print(f'FAIL decryption_{d}.txt is not what decrypt.py gives from transcription_{d}.txt and key.tsv')
        sys.exit(1)
    print(f'decryption_{d}.txt: rebuilt, identical', flush=True)
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode)
