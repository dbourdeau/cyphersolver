"""Shared parsing for the 44r files."""
import os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_align(path=os.path.join(HERE, 'align_44r.txt')):
    """Return {line: [words]}, each word a list of (token, value)."""
    out = {}
    for ln in open(path, encoding='utf-8'):
        if not ln.startswith('L'):
            continue
        lab, rest = ln.split(':', 1)
        words, cur = [], []
        for t in rest.split():
            if t == '#':
                if cur: words.append(cur)
                cur = []
            else:
                tok, val = t.rsplit('=', 1)
                cur.append((tok, val))
        if cur: words.append(cur)
        out[lab] = words
    return out

def read_transcription(path=os.path.join(HERE, 'transcription_44r.txt')):
    out = {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('L'):
            lab, rest = ln.split(':', 1)
            out[lab] = rest.split()
    return out

def read_key(path):
    key = {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('sign\t') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        key[f[0]] = f[1]
    return key
