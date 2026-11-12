#!/usr/bin/env python3
"""Mechanical decryption, standard library only.
    python scripts/decrypt.py transcription_<doc>.txt key.tsv > decryption_<doc>.txt
Each line `label<TAB>text`. Clear text in double quotes is copied; every dot-separated number is replaced by its
key letter (N: adds a diaeresis, N^ doubles the letter, a trailing ? is ignored); a number not in the key becomes [N];
| (line end lost in the binding) becomes [...]; notes in square brackets are dropped. Word gaps are kept as written."""
import re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
def key(p):
    k = {}
    for l in open(p, encoding='utf-8').read().splitlines()[1:]:
        f = l.split('\t'); k[f[0]] = f[1]
    return k
TOK = re.compile(r'"[^"]*"|\[[^\]]*\]|\||[^\s"\[\]|]+(?:"[^"]*"[^\s"\[\]|]*)*')
def unit(u, k):
    tail = ''
    while u and u[-1] in ',;-/': tail = u[-1] + tail; u = u[:-1]
    if not u: return tail
    return unit1(u.rstrip('?'), k) + tail
def unit1(u, k):
    m = re.fullmatch(r'(\d+)([:^]?)', u)
    if not m: return f'[?{u}]'
    n, mk = m.groups()
    if n not in k: return f'[{n}]'
    c = k[n]
    if mk == ':': c = unicodedata.normalize('NFC', c + '̈')
    if mk == '^': c = c + c
    return c
def dec(text, k):
    out = []
    for t in TOK.findall(text):
        if t.startswith('"'): out.append(t.strip('"')); continue
        if t == '|': out.append('[...]'); continue
        if t.startswith('['): continue
        w = ''
        for piece in re.findall(r'"[^"]*"|[^.]+', t):
            w += piece.strip('"') if piece.startswith('"') else unit(piece, k)
        out.append(w)
    return ' '.join(x for x in out if x)
if __name__ == '__main__':
    k = key(sys.argv[2])
    for l in open(sys.argv[1], encoding='utf-8').read().splitlines():
        if not l.strip() or l.startswith('#'): continue
        lab, t = l.split('\t', 1)
        print(f'{lab}\t{dec(t, k)}')
