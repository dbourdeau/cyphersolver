# Doc 627 control: ONE decode of the blind transcription with the frozen Corsi key (w17).
# Run from anywhere: python3 -I /home/claude/corsi627_control/decode_once.py
# Refuses: a rerun (output exists), a key hash mismatch, a BLIND.tsv whose sha256 is not in FREEZE_blind.txt.
import json, csv, re, sys, os, hashlib
HERE = '/home/claude/corsi627_control'
KEY = '/home/claude/wt_cv/targets/corsi1513/key_corsi_w17_frozen.json'
KH = '5f56ad5879c6d53d9c865d52096fde97fbe831e6fcca924efe83a5247c732940'
MAP = HERE + '/private/LABELS_TO_KEY.tsv'
B = HERE + '/BLIND.tsv'            # copied here from the packet after freezing
FRZ = HERE + '/FREEZE_blind.txt'   # sha256 of BLIND.tsv, written before this script runs
OUT = HERE + '/decode_once.txt'

if os.path.exists(OUT): sys.exit('REFUSED: decode_once.txt exists; first pass is of record')
h = hashlib.sha256(open(KEY, 'rb').read()).hexdigest()
if h != KH: sys.exit('REFUSED: key hash mismatch ' + h)
if not os.path.exists(FRZ): sys.exit('REFUSED: no FREEZE_blind.txt')
bh = hashlib.sha256(open(B, 'rb').read()).hexdigest()
if bh not in open(FRZ).read(): sys.exit('REFUSED: BLIND.tsv hash not in FREEZE_blind.txt')
mh = hashlib.sha256(open(MAP, 'rb').read()).hexdigest()

lab = {r[0]: r[1] for r in csv.reader(open(MAP), delimiter='\t') if r and r[0] != 'label'}
k = json.load(open(KEY))
bare, base, vow, num = k['bare'], k['base'], k['vowel'], k['num']

def to_key(t):
    """neutral token -> key token (S07^3 -> b3); '#nn' and '.' pass through; unknown -> None"""
    if t in ('.', '') or t.startswith('#'): return t
    m = re.fullmatch(r'(S\d\d)(?:\^(\d))?', t)
    if not m or m.group(1) not in lab: return None
    return lab[m.group(1)] + (m.group(2) or '')

def dec(t):
    t = t.rstrip('?')
    kt = to_key(t)
    if kt is None: return '_', 'hole', t
    if kt in ('.', ''): return '', 'null', kt
    if kt.startswith('#'): return (num.get(kt, '[' + kt + ']'), 'num' if kt in num else 'hole', kt)
    if kt in num: return num[kt], 'num', kt
    if kt in bare: return bare[kt], 'val', kt
    m = re.match(r'^(.+?)(\d)$', kt)
    if m and m.group(1) in base and m.group(2) in vow: return base[m.group(1)] + vow[m.group(2)], 'val', kt
    return '_', 'hole', kt

rows = [r for r in csv.reader(open(B), delimiter='\t') if len(r) >= 2 and r[0] != 'line']
st = {'val': 0, 'num': 0, 'hole': 0, 'null': 0}; out = []; ktx = []
for r in rows:
    s = ''; kk = []
    for t in r[1].split():
        v, c, kt = dec(t); st[c] += 1; kk.append(kt); s += v if c != 'hole' else '_'
    out.append(f'{r[0]}\t{s}'); ktx.append(f'{r[0]}\t{" ".join(kk)}')
body = '\n'.join(out) + '\n\n# key tokens\n' + '\n'.join(ktx) + '\n'
body += f'\n# key sha256 {h}\n# blind sha256 {bh}\n# labels map sha256 {mh}\n# counts {st}\n'
open(OUT, 'w').write(body)
print(body)
