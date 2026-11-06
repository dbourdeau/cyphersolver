"""Mark check for catalogue 2258 (Rålamb 1657). Standard library only.

    python scripts/check_marks.py

For each bare document (114, 104):
1. rebuilds the decryption from transcription_<doc>.txt and key.tsv and compares it with decryption_<doc>.txt;
2. runs reading.py on reading_<doc>.md: every departure from the signs must be marked; counts words.
Exit 1 on a stale decryption file or any unmarked departure.
"""
import os, pathlib, subprocess, sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
rc = 0
for doc in ('114', '104'):
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / f'transcription_{doc}.txt'), str(ROOT / 'key.tsv')],
                         capture_output=True, text=True, encoding='utf-8', env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
    have = (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf-8')
    if out.returncode or out.stdout.replace('\r\n', '\n') != have.replace('\r\n', '\n'):
        print(f'FAIL decryption_{doc}.txt is not what decrypt.py gives from transcription_{doc}.txt and key.tsv')
        rc = 1
        continue
    print(f'decryption_{doc}.txt: rebuilt, identical', flush=True)
    sys.stdout.flush()
    rc |= subprocess.run([sys.executable, str(HERE / 'reading.py'), str(ROOT / f'reading_{doc}.md'),
                          str(ROOT / f'decryption_{doc}.txt')], env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}).returncode
sys.exit(rc)
