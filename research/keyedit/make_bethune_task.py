"""Béthune 1601: token map from key.tsv, tested on the known-plaintext blocks of corpus.txt (control) and the open letters."""
import os, re, json, collections, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(H, '..', '..', 'targets', 'bethune')

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s.replace('j', 'i').replace('v', 'u'))

def build_key():
    key = {}
    for line in open(os.path.join(B, 'key.tsv'), encoding='utf-8').read().splitlines()[1:]:
        c = line.split('\t')
        if len(c) < 3: continue
        sym, val, kind = c[0], c[1], c[2]
        base = re.sub(r'\s*\(.*?\)', '', sym).strip()
        if kind == 'code' or base.startswith('44,'):
            syms = [s.strip() for s in sym.split(',') if s.strip().isdigit()]; v = ''
        else:
            syms = [s.strip() for s in base.split(' / ')]
            first = val.split(' / ')[0].strip()
            if kind.startswith('sign'): v = '<d>'
            elif first in ('null', '?', 'null?', 'names / words'): v = ''
            elif kind.startswith('letter'): v = norm(first)[:1]
            else: v = norm(first)
        for s in syms:
            key.setdefault(s, v)
    return key

def tokens_of(line):
    return line.split()

key = build_key()
blocks = []
for line in open(os.path.join(B, 'corpus.txt'), encoding='utf-8'):
    if line.startswith('#') or '|' not in line: continue
    p = [x.strip() for x in line.split('|')]
    blocks.append((p[0], p[2].split(), norm(p[3])))
def decode(toks, k):
    out = ''
    for t in toks:
        v = k.get(t, '')
        if v == '<d>': out += out[-1:] if out else ''
        else: out += v
    return out
import difflib
tot = ok = 0
for _, toks, pt in blocks:
    d = decode(toks, key)
    tot += len(pt); ok += sum(b.size for b in difflib.SequenceMatcher(None, d, pt).get_matching_blocks())
cnt = collections.Counter(t for _, toks, _ in blocks for t in toks)
unk = [(n, t) for t, n in cnt.most_common() if t not in key]
print(len(blocks), 'blocks;', sum(cnt.values()), 'tokens;', len(cnt), 'distinct;', len(key), 'key entries')
print('plaintext letters matched by key decode: %d/%d = %.3f' % (ok, tot, ok / tot))
print('tokens with no key entry:', sum(n for n, _ in unk), unk[:25])
json.dump(key, open(os.path.join(H, 'bethune_key.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
