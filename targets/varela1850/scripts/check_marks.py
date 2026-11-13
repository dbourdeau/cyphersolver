"""Mark check for catalogue 1500. Standard library only.

    python scripts/check_marks.py

1. Rebuilds decryption_varela1850.txt from transcription_varela1850.txt and key_frozen.tsv and compares.
2. Runs reading.py: every departure of the marked reading from the decryption must be marked; prints word counts.
Exit 1 on a stale decryption file or on any unmarked departure.
"""
import pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / 'transcription_varela1850.txt'),
                      str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
have = (ROOT / 'decryption_varela1850.txt').read_text(encoding='utf-8')
if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
    print('FAIL decryption_varela1850.txt is not what decrypt.py gives'); sys.exit(1)
print('decryption_varela1850.txt: rebuilt, identical')
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py')]).returncode)
