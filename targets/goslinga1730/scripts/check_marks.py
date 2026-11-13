"""Mark check for catalogue 2534. Standard library only.     python scripts/check_marks.py

1. Rebuilds decryption_goslinga1730.txt (and the held-out decryption) from the transcription and key_frozen.tsv and
   compares with the files on disk.
2. Runs reading.py check: every departure of the marked reading from the signs must be marked; prints word counts.
3. Runs build_key.py: the pairs must cover the transcription group for group and the key must have no conflicts;
   prints the held-out result.
Exit 1 on any failure.
"""
import pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
bad = False
for tr, dec in (('transcription_goslinga1730.txt', 'decryption_goslinga1730.txt'),
                ('heldout_fontainebleau1730_transcription.txt', 'heldout_fontainebleau1730_decryption.txt')):
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / tr), str(ROOT / 'key_frozen.tsv')],
                         capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / dec).read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
        print(f'FAIL {dec} is not what decrypt.py gives'); bad = True
    else:
        print(f'{dec}: rebuilt, identical')
rc1 = subprocess.run([sys.executable, str(HERE / 'reading.py'), 'check']).returncode
before = (ROOT / 'key_frozen.tsv').read_text(encoding='utf-8')
kb = subprocess.run([sys.executable, str(HERE / 'build_key.py')], capture_output=True, text=True, encoding='utf-8')
print(kb.stdout.strip())
rc2 = kb.returncode or ('CONFLICT' in kb.stdout) or ('FAIL' in kb.stdout)
sys.exit(1 if bad or rc1 or rc2 else 0)
