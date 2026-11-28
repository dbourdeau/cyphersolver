"""Measure the frozen 1577 key once on the held-out lines P2L01-P2L07 (PROTOCOL_v1.json).
Refuses to run if RESULT_v1.json exists, if any file in MANIFEST_v1.sha256 changed, or if the FreeTSA token
(MANIFEST_v1.sha256.tsr) does not verify against the manifest."""
import hashlib, json, os, subprocess, sys, datetime, platform
V = 'verification'
sys.path.insert(0, 'scripts')
if os.path.exists(f'{V}/RESULT_v1.json'): sys.exit('RESULT_v1.json exists: the passage is burnt')
for ln in open(f'{V}/MANIFEST_v1.sha256'):
    h, p = ln.split(None, 1); p = p.strip()
    if hashlib.sha256(open(p, 'rb').read()).hexdigest() != h: sys.exit('changed since freeze: ' + p)
v = subprocess.run(['openssl', 'ts', '-verify', '-data', f'{V}/MANIFEST_v1.sha256', '-in', f'{V}/MANIFEST_v1.sha256.tsr',
                    '-CAfile', f'{V}/freetsa_cacert.pem', '-untrusted', f'{V}/freetsa_tsa.crt'], capture_output=True, text=True)
if 'Verification: OK' not in v.stdout + v.stderr: sys.exit('timestamp does not verify: ' + v.stdout + v.stderr)
os.environ['TSPLIT'] = '1'
import build_key as B
import measure_lib as M
from kervyn_units import units
P = json.load(open(f'{V}/PROTOCOL_v1.json'))
TR = {'y': 'i', 'f': 's', 'e': 'c', 't': 'l'}
f = lambda x: ''.join(TR.get(c, c) for c in x)
key = {s: f(v) for s, v in json.load(open(f'{V}/key_1577_v1.json'))['key'].items()}
U = units(); j0, j1 = P['reference_units']; ref = [u if len(u) > 1 else f(u) for u in U[j0:j1]]
toks = [t for lab in sorted(B.L) if lab in B.HELDOUT for t in B.L[lab]]
r, s, holes = M.score(toks, key, ref); sc = r / s
ctrl = M.controls(toks, key, ref, n=200, seed=1577)
mean = sum(ctrl) / len(ctrl); sd = (sum((c - mean) ** 2 for c in ctrl) / len(ctrl)) ** 0.5
verdict = 'pass' if sc >= P['threshold'] and sc - max(ctrl) >= P['margin'] else 'fail'
res = {'measured_at': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'tokens': len(toks),
       'scored': s, 'right': r, 'unscored_or_no_value': holes, 'score': round(sc, 4), 'best_control': round(max(ctrl), 4),
       'control_mean': round(mean, 4), 'z': round((sc - mean) / sd, 2) if sd else None, 'verdict': verdict,
       'manifest_sha256': hashlib.sha256(open(f'{V}/MANIFEST_v1.sha256', 'rb').read()).hexdigest(),
       'python': platform.python_version()}
json.dump(res, open(f'{V}/RESULT_v1.json', 'w'), indent=1)
print(json.dumps(res, indent=1))
