"""Decode transcription.txt with a sign->value key (key.txt: code=value per line or comma list)."""
import re, sys
def load_key(p='key.txt'):
    k = {}
    for part in re.split(r'[,\n]', open(p, encoding='utf-8').read()):
        part = part.strip()
        if '=' in part and not part.startswith('#'):
            a, b = part.split('=', 1); k[a.strip()] = b.strip()
    return k
def lines(p='transcription.txt'):
    page = None
    for ln in open(p, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('=='): page = ln.strip('= '); continue
        if not ln or ln.startswith('#') or ln.startswith('g:'): continue
        m = re.match(r'(\d+)\s+(.*)', ln)
        if m: yield page, m.group(1), m.group(2)
def tokens(s):
    out = []
    for m in re.finditer(r'\[[^\]]*\]|\S+', s):
        out.append(m.group(0))
    return out
def decode(s, k):
    r = []
    for t in tokens(s):
        if t.startswith('['): r.append(' ' + t.upper() + ' ')
        elif t == ':': r.append(' | ')
        else:
            v = k.get(t, '?')
            r.append('' if v == '_' else v)
    return ''.join(r)
if __name__ == '__main__':
    k = load_key(sys.argv[1] if len(sys.argv) > 1 else 'key.txt')
    for pg, n, s in lines():
        print(pg, n, decode(s, k))
