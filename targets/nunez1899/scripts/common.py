import pathlib, unicodedata
HERE = pathlib.Path(__file__).resolve().parent.parent

def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def read_lines(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln or ln.startswith('#'):
            continue
        lab, _, rest = ln.partition(' ')
        out.append((lab, rest.split()))
    return out

def read_key(path):
    key = {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip() or ln.startswith('code\t'):
            continue
        f = ln.rstrip('\n').split('\t')
        key[f[0].rstrip('?')] = f[1] if len(f) > 1 else ''
    return key

def decrypt_tokens(toks, key):
    """Longest match (two-word codes first). Returns list of (code, value) pairs; value None = clear word."""
    out, i = [], 0
    while i < len(toks):
        two = ' '.join(toks[i:i + 2])
        if i + 1 < len(toks) and two in key:
            out.append((two, key[two])); i += 2; continue
        t = toks[i]
        out.append((t, key[t] if t in key else None)); i += 1
    return out
