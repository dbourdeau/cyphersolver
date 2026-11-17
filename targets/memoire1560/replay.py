"""Adapter for docs/_replay.py: key.txt applied to transcription/*.txt, against the two reading files.

Segmentation is decrypt.py's (longest unit first; bracketed doubtful transcriptions dropped, as decrypt.py drops them).
POLYPHONY is what key.txt declares in its third column, nothing more.
"""
import os, re
from decrypt import lines, load_key

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = True
SOURCES = {'key': 'key.txt', 'transcription': 'transcription/<fol>.txt',
           'reading': 'reading_152r-154r.txt + reading_154v-156v.txt'}

def _declared():
    """Other values key.txt declares for a sign (its third column)."""
    out = {}
    for line in open(os.path.join(HERE, 'key.txt'), encoding='utf8'):
        parts = line.split('#')[0].rstrip('\n').split('\t')
        if len(parts) >= 3 and parts[2].strip():
            out[parts[0].strip()] = parts[2].split()
    return out


POLYPHONY = _declared()


def mechanical():
    key = load_key()
    units = sorted((k for k in key if not k.startswith('=')), key=len, reverse=True)
    out = []
    for fol, n, ct in lines():
        words = []
        for w in re.sub(r'\[[^\]]*\]', ' ', ct).replace('=', '').split():
            if '=' + w in key:
                words.append([(w, key['=' + w])]); continue
            us, i = [], 0
            while i < len(w):
                for u in units:
                    if w.startswith(u, i):
                        v = key[u]; us.append((u, '' if v == '-' else v)); i += len(u); break
                else:
                    us.append((w[i], None)); i += 1
            words.append(us)
        out.append((f'{fol}.{n:02d}', words))
    return out


def reading():
    R = {}
    for fn in ('reading_152r-154r.txt', 'reading_154v-156v.txt'):
        for l in open(os.path.join(HERE, fn), encoding='utf8'):
            if l.startswith('#') or '\t' not in l:
                continue
            a, b = l.rstrip('\n').split('\t', 1)
            R[a] = b
    return R
