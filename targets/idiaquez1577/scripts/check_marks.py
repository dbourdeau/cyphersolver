"""Mark check for 754 / 1410,115. Standard library only.
    python -I scripts/check_marks.py
1. Rebuilds decryption_1410_115.txt from transcription_1410_115.txt and key_frozen.tsv and compares.
2. Checks key_frozen.tsv against key_frozen.sha256.
3. Runs reading.py check: every departure of the reading from the signs must be marked; prints the word counts.
"""
import hashlib, pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
bad = False
h = hashlib.sha256((ROOT / 'key_frozen.tsv').read_bytes()).hexdigest()
if h != (ROOT / 'key_frozen.sha256').read_text().split()[0]:
    print('FAIL key_frozen.tsv changed since it was frozen'); bad = True
for doc in ('1410_115',):
    out = subprocess.run([sys.executable, '-I', str(HERE / 'decrypt.py'), str(ROOT / f'transcription_{doc}.txt'),
                          str(ROOT / 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
        print(f'FAIL decryption_{doc}.txt is not what decrypt.py gives'); bad = True
    else:
        print(f'decryption_{doc}.txt: rebuilt, identical')
if bad:
    sys.exit(1)
sys.exit(subprocess.run([sys.executable, '-I', str(HERE / 'reading.py'), 'check']).returncode)
