"""Mark check for catalogue 2354. Standard library only.

    python scripts/check_marks.py

1. Rebuilds decryption_<doc>.txt from transcription_<doc>.txt and key_frozen.tsv and compares.
2. Runs reading.py check: every departure of reading_<doc>.md from the signs must be marked; prints the word counts.
3. Runs check_pairs.py: every glossed pair in pairs.tsv must decrypt to its gloss with key_frozen.tsv; the held-out
   comparison (heldout_24786_pairs.tsv) is printed.
Exit 1 on a stale decryption file, on any unmarked departure, or on a glossed pair the key does not give.
"""
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
bad = False
for doc in ('24793', '24800'):
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / f'transcription_{doc}.txt'),
                          str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
        print(f'FAIL decryption_{doc}.txt is not what decrypt.py gives', flush=True); bad = True
    else:
        print(f'decryption_{doc}.txt: rebuilt, identical', flush=True)
if bad:
    sys.exit(1)
rc1 = subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode
rc2 = subprocess.run([sys.executable, str(HERE / 'check_pairs.py')]).returncode
sys.exit(1 if rc1 or rc2 else 0)
