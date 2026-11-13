"""Rebuild KEY_HB_v1 / KEY_HB_v2 from the gloss-pair files (own code, standard library).
usage: python3 -I buildkey.py v1|v2 <gloss_pairs.tsv> <out.tsv>
Rule (both versions): each code takes the value most often written over it by the chancery glossator.
v1 (run b179): on a tie the first-seen value wins (Counter.most_common order).
v2 (run b180): on a tie the code is left UNVALUED (row type 'tie'), so the decoder ignores it.
Phrase rows ('phr') keep multi-token groups whose letters could not be split one-to-one; they are not used by the decoder."""
import sys, collections
mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
pairs = [l.rstrip('\n').split('\t') for l in open(src, encoding='utf-8') if l.strip() and not l.startswith('#')]
val = collections.defaultdict(collections.Counter); refs = collections.defaultdict(set); phr = {}
for img, toks, gl, seg in pairs:
    if seg != '-':
        for kv in seg.split(';'):
            k, v = kv.split('='); val[k][v] += 1; refs[k].add(img)
    if ',' in toks: phr[toks] = gl
out = open(dst, 'w', encoding='utf-8'); out.write('#type\tcode\tvalue\tattest\tconflict\trefs\n'); nt = 0
for k in sorted(val, key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x)):
    c = val[k]; mc = c.most_common(); v, n = mc[0]; tot = sum(c.values())
    tie = mode == 'v2' and len(mc) > 1 and mc[1][1] == n; nt += tie
    conf = ';'.join('%s:%d' % (a, b) for a, b in c.items() if a != v)
    out.write('%s\t%s\t%s\t%d/%d\t%s\t%s\n' % ('tie' if tie else 'tok', k, v, n, tot, conf or '-', ','.join(sorted(refs[k]))))
for t, g in sorted(phr.items()): out.write('phr\t%s\t%s\t1\t-\t-\n' % (t, g))
out.close()
print('%s: %d codes; %d valued; %d ties unvalued; %d attestations; %d phrase rows' % (mode, len(val), len(val) - nt, nt, sum(sum(c.values()) for c in val.values()), len(phr)))
