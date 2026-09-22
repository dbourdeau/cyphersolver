"""Decrypt R478 with every fetched G15 key transcription; rank by coverage and Hungarian LM."""
import re, sys, glob
sys.path.insert(0, r"C:/Users/dbour/cypher")
from lang import lm
M = lm.load('hu-modern', order=4, spaces=False)

def ct_tokens():
    t = open('DOC_R478_D2181_2181.txt', encoding='utf-8-sig').read()
    t = re.sub(r'<[^>]*>', ' ', t)
    t = '\n'.join(l for l in t.splitlines() if not l.startswith('#'))
    toks = []
    for g in re.split(r'[,.\n]', t):
        g = g.replace(' ', '').replace('i', '1').replace('I', '1').replace('l', '1')
        if re.fullmatch(r'\d+', g): toks.append(str(int(g)))
        elif g: toks.append('<' + g + '>')
    return toks

def parse_key(path):
    k = {}
    for line in open(path, encoding='utf-8-sig', errors='replace'):
        if line.startswith('#') or line.startswith('<'): continue
        m = re.match(r'\s*([\d|,\s/]+?)\s*[-=]\s*(.+?)\s*$', line)
        if not m: continue
        for n in re.findall(r'\d+', m.group(1)):
            k.setdefault(str(int(n)), m.group(2))
    return k

if __name__ == '__main__':
    ct = ct_tokens(); nums = [t for t in ct if not t.startswith('<')]
    print(len(ct), 'tokens', len(nums), 'numeric', file=sys.stderr)
    res = []
    for p in sorted(glob.glob('keys/DOC_*.txt')) + glob.glob('../papai1706/DOC_R58[01]*.txt') + glob.glob('../rakoczi1704/DOC_R639*.txt'):
        k = parse_key(p)
        if len(k) < 10: continue
        hit = [t for t in nums if t in k]
        cov = len(hit) / len(nums)
        txt = ''.join(k[t] for t in hit if len(k[t]) <= 3)
        s = M.per_char(lm.norm(txt, spaces=False)) if len(txt) > 20 else -9
        res.append((cov, s, p, ''.join(k.get(t, '?') if len(k.get(t, '?')) <= 4 else '[' + k[t] + ']' for t in nums[:60])))
    for r in sorted(res, key=lambda r: -r[1])[:15]:
        print(f'{r[0]:.2f} {r[1]:.2f} {r[2]}\n   {r[3]}')
