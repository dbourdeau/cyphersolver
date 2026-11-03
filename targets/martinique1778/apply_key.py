"""Build key_bouille.tsv (Bouillé code, 1778-79) from the interlinear pair files and apply it to the 1778 letter (transcription.txt).

Pair files: pairs1779_f123.txt (C8 A 78 f. 123), pairs1779_f3_f31.txt and pairs1779_f3_f31_more.txt (f. 3 and f. 31), pairs1779_f5_f144.txt (f. 5, f. 144; merged 3 Nov 2026). Provenance is kept per value
(source letter + count); values that differ between sources are kept as 'a/b' and listed as conflicts.
Tentative values (hypotheses from context, no interlinear) live in tentative.tsv and are applied only with --tentative.
"""
import re, collections, os, sys
H = os.path.dirname(os.path.abspath(__file__))
SRC = [('pairs1779_f123.txt', 'f123'), ('pairs1779_f3_f31.txt', None), ('pairs1779_f3_f31_more.txt', None), ('pairs1779_f5_f144.txt', None), ('pairs1779_f144_p2.txt', None), ('pairs1779_f144_p3.txt', None)]
vals = collections.defaultdict(lambda: collections.defaultdict(list))   # group -> value -> [source tags]
for fn, default in SRC:
    for l in open(os.path.join(H, fn), encoding='utf8'):
        m = re.match(r'(l\d+|f\d+[a-z]?-[\w-]+):(.*)', l)
        if not m: continue
        tag = default or m.group(1).split('-')[0]
        for g, v in re.findall(r'(\d+)=(\S+)', m.group(2)):
            v = v.replace('_', ' ').rstrip('?')
            if not v or not re.search('[A-Za-zÀ-ÿ]', v): continue   # '298=?' = label unreadable
            vals[g][v if v == 'M.' else v.lower()].append(tag)
key, conflicts = {}, {}
def fold(s): return re.sub("[éèe']", '', s)
with open(os.path.join(H, 'key_bouille.tsv'), 'w', encoding='utf8') as f:
    f.write('group\tvalue\tprovenance (letter x occurrences)\n')
    for g in sorted(vals, key=int):
        cands = vals[g]
        best = sorted(cands, key=lambda v: -len(cands[v]))
        key[g] = best[0]
        if len(best) > 1 and any(fold(b) != fold(best[0]) for b in best): conflicts[g] = best
        prov = '; '.join('%s: %s' % (v, ','.join('%s x%d' % (t, n) for t, n in collections.Counter(cands[v]).items())) for v in best)
        f.write('%s\t%s\t%s\n' % (g, '/'.join(best), prov))
tent = {}
if '--tentative' in sys.argv and os.path.exists(os.path.join(H, 'tentative.tsv')):
    for l in open(os.path.join(H, 'tentative.tsv'), encoding='utf8'):
        if l[:1].isdigit(): p = l.rstrip('\n').split('\t'); tent[p[0]] = p[1]
toks = [t for l in open(os.path.join(H, 'transcription.txt'), encoding='utf8') if l[0] != '#' for t in l.split()]
sure = sum(t in key for t in toks); allv = sum((t in key) or (t in tent) for t in toks)
print('key groups', len(key), '; conflicts', conflicts)
print('tokens valued (interlinear key)', sure, '/', len(toks), '= %.1f%%' % (100 * sure / len(toks)), '; distinct', len({t for t in toks if t in key}), '/', len(set(toks)))
if tent: print('with tentative values', allv, '/', len(toks), '= %.1f%%' % (100 * allv / len(toks)))
for l in open(os.path.join(H, 'transcription.txt'), encoding='utf8'):
    if l[0] != '#':
        print(' '.join((key[t].split('/')[0] if t in key else ('<%s>' % tent[t] if t in tent else '[%s]' % t)) for t in l.split()))
