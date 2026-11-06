"""Key-word-in-context for the code groups: each group with the decoded text around it (key.tsv)."""
import os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
key = {}
for l in open(os.path.join(HERE, '..', 'key.tsv'), encoding='utf-8'):
    l = l.split('#', 1)[0] if not l.startswith('#\t') else l
    if '\t' in l: k, v = l.rstrip('\n').split('\t')[:2]; key[k] = v
toks = [x for l in open(os.path.join(HERE, 'tokens.txt'), encoding='utf-8') if not l.startswith('#00') for x in l.split()]
isg = lambda t: len(t) == 3 and t.isalpha() and t.islower()
MARK = {'11', 'g#', '-o-'}
def show(t):
    if t in MARK: return '|'
    if isg(t): return f' {key[t].upper()} ' if t in key else f' [{t}] '
    return key.get(t, '{' + t + '}')
ctx = collections.defaultdict(list)
for i, t in enumerate(toks):
    if isg(t):
        L = ''.join(show(x) for x in toks[max(0, i - 10):i]); R = ''.join(show(x) for x in toks[i + 1:i + 11])
        ctx[t].append(f'{L[-40:]:>40} <{t}> {R[:40]}')
only = sys.argv[1:]
for g, c in sorted(ctx.items(), key=lambda kv: -len(kv[1])):
    if only and g not in only: continue
    print(f'== {g} ({len(c)})' + (f' = {key[g]}' if g in key else ''))
    for x in c[:int(os.environ.get('N', '12'))]: print('   ', re.sub(' +', ' ', x))
