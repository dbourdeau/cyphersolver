"""Estimate label -> value counts from aligned readings (words with '?' are skipped)."""
import sys, json, re, collections, os
os.environ.setdefault('KEY', 'key_strict.json')
import check
from decode import load
files = ['t1.txt', 't2.txt', 't3.txt']; L = dict(load(files))
cnt = collections.defaultdict(collections.Counter)
for rf in sys.argv[1:]:
    for line in open(rf, encoding='utf8'):
        if ':' not in line or line.startswith('#'): continue
        k, v = line.split(':', 1); k = k.strip()
        if k not in L: continue
        toks = [t for t in L[k] if t != '...']
        text = check.norm(v.replace('?', '').replace('[...]', ''))
        text = text.replace('[', '').replace(']', '')
        for t, ch in check.align(toks, text):
            if t is not None: cnt[t][ch or '0'] += 1
for t in sorted(cnt, key=lambda t: -sum(cnt[t].values())):
    print(t, sum(cnt[t].values()), dict(cnt[t].most_common(6)))
