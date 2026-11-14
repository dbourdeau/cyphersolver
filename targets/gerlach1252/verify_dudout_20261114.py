"""gerlach1252: independent decoder (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY key.tsv and transcription.txt, decodes every L-line (comma = word divider, '=' = word runs on, '?' after a
label = doubtful, kept as '?' after the letter), and compares line by line with decryption.txt.
Also lists the doubtful 4-shapes (4L l, 4R r, 4U u) per page.

    python3 verify_dudout_20261114.py [target_dir]
"""
import re, sys, pathlib, collections
T = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
key = {}
for line in (T / 'key.tsv').read_text(encoding='utf8').splitlines():
    if line.startswith('#') or line.startswith('letter\t') or not line.strip(): continue
    f = line.split('\t'); key[f[1]] = f[0]

def decode(body):
    out, words = [], body.split(',')
    for w in words:
        s = ''
        for tok in w.split():
            if tok in ('=', '.', ';'): continue
            if tok.startswith('[') or tok.startswith('@'): s += '[...]' if tok.startswith('@') else tok; continue
            q = tok.endswith('?'); lab = tok.rstrip('?')
            s += (key.get(lab, '#') + ('?' if q else ''))
        out.append(s)
    return out

def lines(p):
    page, res = None, collections.OrderedDict()
    for l in p.read_text(encoding='utf8').splitlines():
        m = re.match(r'### p\.(\S+)', l)
        if m: page = m.group(1); continue
        m = re.match(r'(L\d+):\s?(.*)', l)
        if m: res[(page, m.group(1))] = m.group(2)
    return res

tr, de = lines(T / 'transcription.txt'), lines(T / 'decryption.txt')
same = diff = 0
for k, body in tr.items():
    mine = ' '.join(x for x in decode(body) if x)
    pub = re.sub(r'\s+', ' ', de.get(k, '')).strip()
    norm = lambda x: re.sub(r'[\W#]', '', re.sub(r'\[[^\]]*\]', '', x))   # pictograms and damage marks dropped
    if norm(mine) == norm(pub): same += 1
    else:
        diff += 1
        if diff <= 15: print('differs', k, '| mine:', mine, '| published:', pub)
print(f'lines: {len(tr)} transcribed, {len(de)} in decryption; letters identical (spacing and punctuation ignored): {same}, differ: {diff}')
c = collections.Counter(k[0] for k, b in tr.items() for t in b.split() if re.fullmatch(r'4[LRU]\?', t))
print('doubtful 4-shapes per page:', dict(c))
