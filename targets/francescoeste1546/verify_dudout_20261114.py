#!/usr/bin/env python3
"""francescoeste1546: independent decode of c. 42r (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY key.tsv (all-pages key, pass A values; pass B as a second run), key_c42r.tsv (the c. 42r key) and
transcription_c42r.txt; does not use scripts/. Units: a two-sign unit of the key is taken when the next sign
completes it (greedy), else the single sign; the top value is used. The decoded letters of each line are aligned
with clear_c42r.txt (the interlinear decipherment) and the shared letters counted. Then the read share of
reading_c42r.md is measured on the cipher passages only (README rule, research/reading_audit/v10_relabel.share).

    python3 verify_dudout_20261114.py targets/francescoeste1546 [path/to/cyphersolver]
"""
import re, sys, pathlib, difflib, os
T = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')

def load(fn, cols):
    k = {}
    for l in (T / fn).read_text(encoding='utf8').split('\n'):
        if not l or l.startswith('#') or l.startswith('unit'): continue
        f = l.split('\t')
        if len(f) <= cols or not f[cols].strip(): continue
        unit = tuple(f[0].replace('_', ' ').split())
        top = f[cols].split()[0].split(':')[0]
        k[unit] = top
    return k
keys = {'key.tsv pass A': load('key.tsv', 2), 'key.tsv pass B': load('key.tsv', 4), 'key_c42r.tsv': load('key_c42r.tsv', 1)}

lines = {}
for l in (T / 'transcription_c42r.txt').read_text(encoding='utf8').split('\n'):
    if l.startswith('c0L'):
        lab, s = l.split('\t'); lines[lab] = [x.rstrip('?') for x in s.split()]
clear = {}
for l in (T / 'clear_c42r.txt').read_text(encoding='utf8').split('\n'):
    if l.startswith('c0L'):
        lab, _, s = l.partition('\t'); clear[lab] = re.sub(r'[^a-z]', '', s.lower())

def decode(toks, k):
    out, i = [], 0
    while i < len(toks):
        if i + 1 < len(toks) and (toks[i], toks[i+1]) in k: out.append(k[(toks[i], toks[i+1])]); i += 2
        elif (toks[i],) in k: out.append(k[(toks[i],)]); i += 1
        else: out.append('?'); i += 1
    return ''.join(out)

for name, k in keys.items():
    tot = hit = 0; per = []
    for lab, toks in lines.items():
        d = decode(toks, k); c = clear.get(lab, '')
        if not c: continue
        sm = difflib.SequenceMatcher(a=c, b=d, autojunk=False)
        h = sum(b.size for b in sm.get_matching_blocks()); tot += len(c); hit += h
        per.append(f'{lab} {h}/{len(c)}')
    print(f'{name}: {len(k)} units; clear letters matched by the decode {hit}/{tot} ({hit/tot:.3f})')
    print('   ', ', '.join(per))
d = decode(lines['c0L10'], keys['key_c42r.tsv']); print('    c0L10 decode (c42r key):', d, '| clear:', clear['c0L10'])

# read share on the cipher passages only
root = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else T.resolve().parents[1]
sys.path.insert(0, str(root / 'research' / 'reading_audit')); sys.path.insert(0, str(root / 'docs'))
cwd = os.getcwd(); os.chdir(root); import v10_relabel as v; os.chdir(cwd)
def rs(t):
    w, h, dd = v.share(t); return w, h, round(1 - (h + dd) / (w + h), 3)
t = (T / 'reading_c42r.md').read_text(encoding='utf8')
it = re.search(r'## Italian\n(.*?)(?=^## )', t, re.S | re.M).group(1)
bold = ' '.join(re.findall(r'\*\*(.*?)\*\*', it, re.S))
print('read share (words, holes, share): whole file', rs(t), '| ## Italian section', rs(it), '| cipher passages (bold) only', rs(bold))
print('[?] in the cipher passages:', bold.count('[?]'), '| words marked °:', bold.count('°'))
