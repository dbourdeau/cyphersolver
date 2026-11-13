# -*- coding: utf-8 -*-
"""Mesure pré-enregistrée PREREG-2 — système à index Pentz 1644-45.
usage: python3 -I measure2.py KEY-v3.json HELDOUT.json
KEY = {"index": {"62": "T1", ...}, "T1": {"37": "a", ...}, "T2": {...}, "T3": {...}}
HELDOUT = {"docs": {"<id>": {"lines": [[groupes], ...]}}} ; groupe = entier, ou chaîne (mot clair, '?', 'code?')."""
import json, math, random, sys, hashlib, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
CORPUS = Path(__file__).resolve().parents[3] / 'lang' / 'corpora' / 'de-gutenberg.txt'
CORPUS_SHA = '4828ed84e7ddc33a3f74180cbe88804a7f8a5e29d3770f5ceb75499c546ea73c'
def fold(s):
    s = s.lower().replace('ß', 'ss').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    s = unicodedata.normalize('NFKD', s)
    return ''.join({'j': 'i', 'v': 'u'}.get(c, c) for c in s if 'a' <= c <= 'z')
def model():
    raw = CORPUS.read_bytes(); assert hashlib.sha256(raw).hexdigest() == CORPUS_SHA
    t = fold(raw.decode('utf-8', 'ignore')); V = len(set(t)); c4 = {}; c3 = {}
    for i in range(len(t) - 3):
        c4[t[i:i+4]] = c4.get(t[i:i+4], 0) + 1; c3[t[i:i+3]] = c3.get(t[i:i+3], 0) + 1
    return t, c4, c3, V
def ll(s, c4, c3, V):
    if len(s) < 4: return float('nan')
    return sum(math.log((c4.get(s[i:i+4], 0) + 0.1) / (c3.get(s[i:i+3], 0) + 0.1 * V)) for i in range(len(s) - 3)) / (len(s) - 3)
def decode(groups, key):
    tab = 'T1'; out = []; n_let = 0; n_ok = 0
    for g in groups:
        if not isinstance(g, int): continue
        if str(g) in key['index']: tab = key['index'][str(g)]; continue
        if g >= 100: continue
        n_let += 1
        v = key[tab].get(str(g))
        if v: out.append(v); n_ok += 1
    return ''.join(out), n_let, n_ok
if __name__ == '__main__':
    key = json.load(open(sys.argv[1])); H = json.load(open(sys.argv[2]))
    for T in ('T1', 'T2', 'T3'): key[T] = {k: fold(v) for k, v in key[T].items()}
    groups = [g for d in H['docs'].values() for line in d['lines'] for g in line]
    t, c4, c3, V = model()
    txt, n_let, n_ok = decode(groups, key); n = len(txt); L = ll(txt, c4, c3, V)
    rng = random.Random(20261114); W = []
    for _ in range(200):
        k2 = {'index': key['index']}
        for T in ('T1', 'T2', 'T3'):
            f = sorted(key[T]); v = [key[T][x] for x in f]; rng.shuffle(v); k2[T] = dict(zip(f, v))
        W.append(ll(decode(groups, k2)[0], c4, c3, V))
    rr = random.Random(7); R = [ll(t[i:i+n], c4, c3, V) for i in (rr.randrange(len(t) - n) for _ in range(50))]
    mw = sum(W) / 200; mr = sum(R) / 50; N = (L - mw) / (mr - mw); Nmax = (max(W) - mw) / (mr - mw); cov = n_ok / max(n_let, 1)
    ok = N >= 0.75 and N >= Nmax + 0.30 and cov >= 0.90
    print(f'groupes {len(groups)} ; figures lettres {n_let} ; résolues {n_ok} ({cov:.1%}) ; lettres décodées {n}')
    print(f'LL vrai {L:.4f} ; témoins moy {mw:.4f} max {max(W):.4f} ; allemand réf. moy {mr:.4f} (min {min(R):.4f})')
    print(f'N = {N:.4f} ; N témoin max = {Nmax:.4f} -> {"PASS" if ok else "ECHEC"}')
    print('décodé :', txt)
