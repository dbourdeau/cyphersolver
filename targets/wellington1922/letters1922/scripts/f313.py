"""Narvaez's key 313 (rule only) for the felicista letters, CEHM-Carso Fondo DCXXI.
Alphabet of 27 letters A-N, Ñ, O-Z; cipher = plain + 3, +1, +3, repeating; plain = cipher - 3, -1, -3, ...
Notation of the transcription: "/" line break inside a run (the cycle runs on); {X^Y} X typed over Y (X used);
[X|Y] doubtful sign (X used); N with a typed bar (U+0304) = Ñ; "?" an unreadable sign (holds its place, output "?").
Variant A: the cycle runs on through the whole run (for a hyphenated number-letter chain: through all its letters;
digits do not advance it). Variant B: the cycle restarts at each visible space (and, in a chain, at each letter group
between hyphens)."""
import re, unicodedata
from pathlib import Path
A = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
KEY = (3, 1, 3)

def clean(s):
    s = unicodedata.normalize('NFC', s).replace('N̄', 'Ñ').replace('V̄', 'V')
    s = re.sub(r'\{(.)\^[^}]*\}', r'\1', s)          # overtyping: top layer
    s = re.sub(r'\[([^|\]]*)\|[^\]]*\]', r'\1', s)    # doubt: first reading
    return s.replace('/', '').replace('+', '')

def is_chain(s):
    return bool(re.search(r'[0-9]', s))

def units(s, variant):
    """Split a cleaned run into restart units (lists of signs: letters and '?')."""
    if is_chain(s):
        groups = [g for g in re.split(r'[^A-ZÑ?]+', s) if g]
        return [''.join(groups)] if variant == 'A' else groups
    if variant == 'A':
        return [s.replace(' ', '')]
    return [g for g in s.split(' ') if g]

def dec_unit(u, key=KEY):
    out = []
    for j, ch in enumerate(u):
        out.append('?' if ch not in A else A[(A.index(ch) - key[j % len(key)]) % 27])
    return ''.join(out)

def decode(s, variant='A', key=KEY):
    return ' '.join(dec_unit(u, key) for u in units(clean(s), variant))

def load(path):
    R = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        f = l.rstrip('\n').split('\t')
        R.append({'id': f[0], 'image': f[1], 'para': f[2], 'before': f[3], 'run': f[4], 'note': f[5] if len(f) > 5 else ''})
    return R

def fold(t):
    o = []
    for ch in t.upper():
        if ch == 'Ñ':
            o.append(ch); continue
        d = unicodedata.normalize('NFD', ch)[0]
        o.append(d if d in A else ' ')
    return ''.join(o)

def repo_path(p):
    return Path(p).as_posix()
