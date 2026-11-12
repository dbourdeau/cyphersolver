"""Mark check for fuerstenberg1659. Standard library only.

    python scripts/check_marks.py

1. Rebuilds decryption_fuerstenberg1659.txt from transcription_fuerstenberg1659.txt and key_frozen.tsv and compares.
2. Runs reading.py check: every departure of the reading from the signs must be marked.
3. Runs heldout.py (prints the held-out result).
Exit 1 on a stale decryption file or on any unmarked departure.
"""
import pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / 'transcription_fuerstenberg1659.txt'),
                      str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
have = (ROOT / 'decryption_fuerstenberg1659.txt').read_text(encoding='utf-8')
if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
    print('FAIL decryption_fuerstenberg1659.txt is not what decrypt.py gives'); sys.exit(1)
print('decryption_fuerstenberg1659.txt: rebuilt, identical')
rc = subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode
subprocess.run([sys.executable, str(HERE / 'heldout.py')])
sys.exit(1 if rc else 0)
