"""Check every hash in key/FROZEN.sha256 and that the .json keys and key_T2.tsv regenerate byte for byte.
Usage (from dudout/):  python3 -I scripts/verify_hashes.py"""
import hashlib, os, re, subprocess, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ok = True
for l in open(os.path.join(HERE, 'key', 'FROZEN.sha256'), encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    h, spec = l.split()[:2]
    m = re.match(r'(.+?)(?:\[:(\d+)\])?$', spec)
    b = open(os.path.join(HERE, m.group(1)), 'rb').read()
    if m.group(2):
        b = b[:int(m.group(2))]
    good = hashlib.sha256(b).hexdigest() == h
    ok &= good
    print('OK ' if good else 'BAD', spec)
for script, target in (('key/table_T.py', 'key/table_T.json'), ('key/table_T2.py', 'key/table_T2.json'),
                       ('scripts/make_key_tsv.py', 'key/key_T2.tsv')):
    out = subprocess.run([sys.executable, '-I', os.path.join(HERE, script)], capture_output=True, check=True).stdout
    good = out == open(os.path.join(HERE, target), 'rb').read()
    ok &= good
    print('OK ' if good else 'BAD', script, '->', target, 'byte-identical')
sys.exit(0 if ok else 1)
