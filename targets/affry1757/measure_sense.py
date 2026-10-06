# Sense measure for affry1757 (5 Oct 2026).
# The old measure (fraction 0.86) counted a group as read when it had ANY key or inferred value, including '?'
# values and values that make nonsense in place. This one counts a group as read only when
#   (1) it has a value from key_M.json or an H/M inferred value in read/*_new.tsv ('?' rows do not count), and
#   (2) the 9-group window centred on it decodes to French: lm per-char score above THR and at most one valueless
#       group in the window.
# THR is calibrated on the eight letters with Lyonet's decipherment, decoded through key_M (the same test applied
# to text known to be sense). Lyonet letters are reported both ways; the total counts them as read (contemporary
# decipherment), R1071 (code C) as unread.
import os, sys, json, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from view import load
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M = lm.load('fr-modern', spaces=False)
key = json.load(open('key_M.json', encoding='utf8'))
ext = json.load(open('key_X.json', encoding='utf8')) if os.path.exists('key_X.json') else {}
inf = {}
for f in glob.glob('read/*_new.tsv'):
    for line in open(f, encoding='utf8'):
        p = line.rstrip('\n').split('\t')
        if len(p) >= 3 and p[0].strip().isdigit() and p[2].strip()[:1] in 'HM' and p[2].strip():
            inf.setdefault(p[0].strip(), p[1].split('/')[0].strip())
LYONET = {'R1052', 'R1053', 'R1062', 'R1063', 'R1065', 'R1066', 'R1069', 'R1075'}
NULLS = {'105', '107'}
def val(g):
    g = str(g)
    if g in NULLS: return ''
    return ext.get(g) or key.get(g) or inf.get(g)
def sense(groups, thr, W=4):
    vals = [val(g) for g in groups]
    ok = []
    for i in range(len(groups)):
        if vals[i] is None: ok.append(False); continue
        win = vals[max(0, i - W): i + W + 1]
        if sum(v is None for v in win) > 1: ok.append(False); continue
        t = lm.norm(''.join(v for v in win if v), 'modern', spaces=False)
        ok.append(len(t) >= 6 and M.per_char(t) > thr)
    return ok
NAMES = {}
if os.path.exists('sense_names.tsv'):
    for line in open('sense_names.tsv', encoding='utf8').read().splitlines()[1:]:
        p = line.split('	'); NAMES.setdefault(p[0], []).append((int(p[1]), int(p[2])))
def sense_r(r, g, thr):
    ok = sense(g, thr)
    for a, b in NAMES.get(r, []):
        for i in range(a, min(b + 1, len(g))):
            if val(g[i]) is not None: ok[i] = True
    return ok
def run(thr, verbose=True):
    U = load('U'); C = load('C')
    for f in glob.glob('transcr/R*.txt'):   # image re-transcriptions replace the DECODE parse
        r = os.path.basename(f)[:-4]
        U[r] = [int(t.split('|')[0]) for line in open(f, encoding='utf8') if not line.startswith('#') for t in line.split()]
    rows = []
    for r, g in U.items():
        ok = sense_r(r, g, thr)
        rows.append((r, len(g), sum(ok)))
    extra = {}
    if os.path.exists('cipher_R2067.txt'):
        g = [int(x) for x in open('cipher_R2067.txt').read().split()]
        rows.append(('R2067', len(g), sum(sense(g, thr))))
    n = sum(x[1] for x in rows) + sum(len(g) for g in C.values())
    rd = sum(x[1] if x[0] in LYONET else x[2] for x in rows)
    if verbose:
        for r, t, s in rows:
            print(f'{r} {"lyonet" if r in LYONET else "      "} {s:4d}/{t:4d} = {s/t:.3f}')
        print('R1071 code C    0/%d' % sum(len(g) for g in C.values()))
        und = [x for x in rows if x[0] not in LYONET]
        print('undeciphered letters: %d/%d = %.3f' % (sum(x[2] for x in und), sum(x[1] for x in und),
              sum(x[2] for x in und) / sum(x[1] for x in und)))
        print('overall (Lyonet letters read, R1071 unread): %d/%d = %.3f' % (rd, n, rd / n))
        print('without R1071: %.3f' % (rd / (n - sum(len(g) for g in C.values()))))
    return rows
if __name__ == '__main__':
    thr = float(sys.argv[1]) if len(sys.argv) > 1 else -3.0
    run(thr)
