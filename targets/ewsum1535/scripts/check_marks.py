"""Mark check for catalogue 2533 (Ewsum). Standard library only.

    python scripts/check_marks.py

1. Rebuilds decryption_ewsum.txt from transcription_ewsum.txt and key_frozen.tsv and compares.
2. Runs reading.py check: every departure of reading_ewsum.md from the signs must be marked; prints the word counts.
Exit 1 on a stale decryption file or on any unmarked departure.
"""
import pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / 'transcription_ewsum.txt'),
                      str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
have = (ROOT / 'decryption_ewsum.txt').read_text(encoding='utf-8')
if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
    print('FAIL decryption_ewsum.txt is not what decrypt.py gives'); sys.exit(1)
print('decryption_ewsum.txt: rebuilt, identical', flush=True)
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode)
