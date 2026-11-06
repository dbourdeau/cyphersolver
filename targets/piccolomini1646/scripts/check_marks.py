"""Mark check for 2358. Standard library only.

    python scripts/check_marks.py

Checks that key.tsv equals key_frozen.tsv. For each letter (24874, 24876): rebuilds the decryption from
transcription_<doc>.txt and key.tsv, compares it with decryption_<doc>.txt, then runs reading.py check (every
departure of the reading from the signs must be marked) and prints the word counts. Also rebuilds the held-out
excerpt's decryption (heldout_24873_2_*.txt). Exit 1 on any failure.
"""
import pathlib, subprocess, sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
rc = 0
if (ROOT / 'key.tsv').read_text(encoding='utf-8') != (ROOT / 'key_frozen.tsv').read_text(encoding='utf-8'):
    print('FAIL key.tsv differs from key_frozen.tsv'); rc = 1


def rebuilt(tr, dec):
    out = subprocess.run([sys.executable, '-I', str(HERE / 'decrypt.py'), str(ROOT / tr), str(ROOT / 'key.tsv')],
                         capture_output=True, text=True, encoding='utf-8')
    have = (ROOT / dec).read_text(encoding='utf-8')
    ok = not out.returncode and out.stdout.replace('\r\n', '\n') == have.replace('\r\n', '\n')
    print(f'{dec}: rebuilt, identical' if ok else f'FAIL {dec} is not what decrypt.py gives', flush=True)
    return ok


for doc in ('24874', '24876'):
    if not rebuilt(f'transcription_{doc}.txt', f'decryption_{doc}.txt'):
        rc = 1; continue
    rc |= subprocess.run([sys.executable, '-I', str(HERE / 'reading.py'), 'check', doc]).returncode
if not rebuilt('heldout_24873_2_transcription.txt', 'heldout_24873_2_decryption.txt'):
    rc = 1
print('result:', 'FAIL' if rc else 'pass')
sys.exit(rc)
