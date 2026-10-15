"""Build validation.tsv for one of the entries split from R1854 (14 Oct 2026), each with its own key:
  r1854          image 2 (Rome, 9 Aug 1428):  p2v3.txt + key7.txt              (Latin)
  mutiliana1428  image 3 (Forli, 6 Nov 1428): p3_signs.txt + key3_p3.txt       (Italian)
  cattanei1430   images 4-5 (Rome, Feb 1430): p4v2.txt, p5v2.txt + key4_v2.txt (Latin)
Image 1 (malatesta1428) has no reading. Usage: python targets/r1854/mk_validation.py <folder>   (default r1854)
'_' key values are nulls ('-'); '?' signs and unknown signs are '?'. Code ARW = cardinalis (reading_p2.md), ARO unread."""
import os, re, sys, collections
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

JOBS = {'r1854': ('la', [('P2', 'p2v3.txt', 'key7.txt')]),
        'mutiliana1428': ('it-cinquecento', [('P3', 'p3_signs.txt', 'key3_p3.txt')]),
        'cattanei1430': ('la', [('P45', 'p4v2.txt', 'key4_v2.txt'), ('P45', 'p5v2.txt', 'key4_v2.txt')])}


def key(fn):
    k = {}
    for l in open(fn, encoding='utf-8'):
        l = l.strip()
        if '=' in l and not l.startswith('//') and not l.startswith('#'):
            a, v = l.rsplit('=', 1); k[a.strip()] = v.strip()
    return k


def val(v):
    if v is None or v.startswith('[?') or v in ('?', '°'): return '?'
    if v == '_': return '-'
    return re.sub(r'[^a-zà-ÿ]', '', v.lower()) or '?'


folder = sys.argv[1] if len(sys.argv) > 1 else 'r1854'
model, jobs = JOBS[folder]
H = os.path.join(T, folder)
out = [f'# model: {model}', '# source: ' + ', '.join(f'{tf}+{kf}' for _, tf, kf in jobs) + ' (mk_validation.py in targets/r1854/)',
       f'# note: {folder}, split from R1854 on 14 Oct 2026; one key']
for pre, tf, kf in jobs:
    K = key(os.path.join(H, kf))
    if pre == 'P2': K['ARW'] = 'cardinalis'; K['ARO'] = '?'
    for l in open(os.path.join(H, tf), encoding='utf-8'):
        if not l.startswith('L') or ':' not in l: continue
        rest = l.split(':', 1)[1]
        rest = re.sub(r'\{[^}]*\}', ' ', rest)
        for t in rest.split():
            t = t.split('/')[0] if pre == 'P3' and '/' in t and len(t) > 1 else t
            if t == '_': continue          # separator point, not a sign
            if t == '?': out.append(f'{pre}:?\t?'); continue
            out.append(f'{pre}:{t}\t{val(K.get(t))}')
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(folder, len(out) - 3, collections.Counter(x.split(':')[0] for x in out[3:]))
