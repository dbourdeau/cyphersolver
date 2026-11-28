"""Check the frozen manifest from the repository: each file listed in MANIFEST_v1.sha256 (paths of the local working
folder where it was frozen) is matched to its copy here, its SHA-256 compared, and the FreeTSA RFC 3161 token checked.
Run from targets/guaras1577 after scripts/fetch_kervyn.py. Needs openssl."""
import hashlib, subprocess
MAP = {'verification/': 'verification/', 'transcription_final_v2.txt': 'transcription/transcription_final_v2.txt',
       'work_D/class_t.tsv': 'transcription/class_t.tsv', 'scripts/': 'verification/frozen_scripts/',
       'verification_draft/': 'verification/', '../../sources/raw/sweep_calendar_2026-11-13/ocr/kervyn_relations/relationspolitiq09nethuoft.txt': 'kervyn9_djvu.txt'}
ok = True
for ln in open('verification/MANIFEST_v1.sha256'):
    h, p = ln.split(None, 1); p = p.strip()
    q = next((v + p[len(k):] if k.endswith('/') else v) for k, v in MAP.items() if p.startswith(k))
    got = hashlib.sha256(open(q, 'rb').read()).hexdigest()
    print('OK ' if got == h else 'BAD', q); ok &= got == h
r = subprocess.run(['openssl', 'ts', '-verify', '-data', 'verification/MANIFEST_v1.sha256', '-in', 'verification/MANIFEST_v1.sha256.tsr',
                    '-CAfile', 'verification/freetsa_cacert.pem', '-untrusted', 'verification/freetsa_tsa.crt'], capture_output=True, text=True)
print((r.stdout + r.stderr).strip()); print('all files match' if ok else 'MISMATCH')
