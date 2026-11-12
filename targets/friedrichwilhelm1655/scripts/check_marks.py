#!/usr/bin/env python3
"""Mark check, standard library only:  python scripts/check_marks.py
1. Rebuilds every decryption_<doc>.txt from transcription_<doc>.txt and key.tsv; fails if one differs.
2. Runs reading.py check: every line of each reading must resolve to the mechanical decryption."""
import pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent
for t in sorted(ROOT.glob('transcription_*.txt')):
    d = t.stem[len('transcription_'):]
    if 'pass' in d: continue
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(t), str(ROOT / 'key.tsv')], capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / f'decryption_{d}.txt').read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n') != have.replace('\r\n', '\n'):
        print(f'FAIL decryption_{d}.txt is stale'); sys.exit(1)
    print(f'decryption_{d}.txt: rebuilt, identical', flush=True)
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode)
