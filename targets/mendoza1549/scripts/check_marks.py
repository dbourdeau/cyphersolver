"""Mark check for 2161 (c. 44r). Rebuilds decryption_44r.txt from transcription_44r.txt + key.tsv and compares,
then runs reading.py check. Exit 1 on a stale decryption or an unmarked departure."""
import subprocess, sys, os, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
tmp = os.path.join(tempfile.gettempdir(), 'dec2161.txt')
subprocess.run([sys.executable, os.path.join(HERE, 'decrypt.py'), os.path.join(ROOT, 'key.tsv'), tmp], check=True)
if open(tmp, encoding='utf-8').read().strip() != open(os.path.join(ROOT, 'decryption_44r.txt'), encoding='utf-8').read().strip():
    print('FAIL decryption_44r.txt is not what decrypt.py gives'); sys.exit(1)
print('decryption_44r.txt: rebuilt, identical')
sys.exit(subprocess.run([sys.executable, os.path.join(HERE, 'reading.py'), 'check']).returncode)
