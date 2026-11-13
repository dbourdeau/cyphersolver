"""Mark check for 2532 (Van Malen). Standard library only.   python scripts/check_marks.py
1. Rebuilds decryption_<doc>.txt from transcription_<doc>.txt and key_frozen.tsv and compares.
2. Runs reading.py check (every departure of reading_malen1.md from the signs must be marked; word counts)."""
import pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent; bad = False
for doc in ('malen1', 'malen2'):
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / f'transcription_{doc}.txt'), str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
        print(f'FAIL decryption_{doc}.txt is not what decrypt.py gives'); bad = True
    else: print(f'decryption_{doc}.txt: rebuilt, identical')
if bad: sys.exit(1)
sys.exit(subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode)
