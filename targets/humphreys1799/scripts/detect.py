"""Code-page detector from two independent machine readings of every frame: our own macOS Vision OCR of the downloaded
image (../work/vocr.tsv, from vocr.swift) and the catalog's text layer (../work/ti_<roll>.tsv). A frame is flagged when
either reading has >= MIN numbers in 1-1700 (years 1780-1810 excluded) that sit in dot- or space-separated runs of >= 3.
Prints frame, vision count, catalog count, count of 994 / 240 / 565 / 1205 (frequent groups of the code), flag.
Usage: python3 -I detect.py [MIN]"""
import re, os, sys, glob, collections
W = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work')
MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 4
def runs(t):
    toks = re.split(r'[\s\.\,:;|]+', t)
    out, cur = [], []
    for x in toks:
        if re.fullmatch(r'\d{1,4}', x) and 1 <= int(x) <= 1700 and not 1780 <= int(x) <= 1810:
            cur.append(int(x))
        else:
            if len(cur) >= 3: out += cur
            cur = []
    if len(cur) >= 3: out += cur
    return out
vis = {}
for l in open(W + '/vocr.tsv'):
    p, _, t = l.rstrip('\n').partition('\t')
    vis[os.path.basename(p)[:-4]] = runs(t)
cat = {}
for f in glob.glob(W + '/ti_*.tsv'):
    for l in open(f):
        a = l.rstrip('\n').split('\t')
        cat[a[0]] = int(a[1]) if a[1].isdigit() else 0
for s in sorted(vis):
    v = vis[s]; c = cat.get(s, 0)
    marks = sum(v.count(k) for k in (994, 240, 565, 1205))
    flag = 'CODE' if len(v) >= MIN or c >= 8 else ''
    if flag: print(f'{s}\t{len(v)}\t{c}\t{marks}\t{flag}')
