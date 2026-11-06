"""Collect the cipher tokens and the clear text of the letter from transcription/00*.txt (reading order 9r 9v 10r 10v 11r).

Writes solve/tokens.txt (one cipher run per line, prefixed '#leaf Lnn' comment lines), transcription/clear.txt
(the clear passages, for the language model and for context) and prints counts. A trailing '?' is dropped from a
token (kept in the transcription), '??' tokens are dropped. ALIAS="a=b ..." merges sign labels.
"""
import os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); TR = os.path.join(HERE, '..', 'transcription')
LEAVES = ['0009r', '0009v', '0010r', '0010v', '0011r']
G2 = set(os.environ.get('G2', '').split())   # two-letter tokens to treat as code groups
alias = dict(kv.split('=') for kv in os.environ.get('ALIAS', '').split())


def parse(line):
    """Split a transcription line into ('clear', text) and ('tok', token) items."""
    out = []; i = 0
    for m in re.finditer(r'\{[^}]*\}|[^\s{}]+', line):
        s = m.group(0)
        if s.startswith('{'): out.append(('clear', s[1:-1]))
        else: out.append(('tok', s))
    return out


runs = []; clear = []; cur = []; where = None
for leaf in LEAVES:
    p = os.path.join(TR, leaf + '.txt')
    if not os.path.exists(p): continue
    for line in open(p, encoding='utf-8'):
        m = re.match(r'^(L\d+):\s*(.*)$', line.strip())
        if not m: continue
        for kind, s in parse(m.group(2)):
            if kind == 'clear':
                if cur: runs.append((where, cur)); cur = []
                clear.append(s)
            else:
                if s == '??' or s.startswith('['): continue
                s = s.rstrip('?') or s
                s = alias.get(s, s)
                if not cur: where = f'{leaf} {m.group(1)}'
                cur.append(s)
if cur: runs.append((where, cur))
with open(os.path.join(HERE, 'tokens.txt'), 'w', encoding='utf-8') as f:
    for w, r in runs: f.write(f'#{w}\n' + ' '.join(r) + '\n')
open(os.path.join(TR, 'clear.txt'), 'w', encoding='utf-8').write('\n'.join(clear) + '\n')
toks = [t for _, r in runs for t in r]
isg = lambda t: len(t) == 3 and t.isalpha() and t.islower() or t in G2
sg = collections.Counter(t for t in toks if not isg(t)); gg = collections.Counter(t for t in toks if isg(t))
print(f'{len(runs)} cipher runs, {len(toks)} tokens: {sum(sg.values())} sign tokens of {len(sg)} types, '
      f'{sum(gg.values())} group tokens of {len(gg)} types')
print('signs:', ' '.join(f'{k}:{v}' for k, v in sg.most_common()))
print('groups:', ' '.join(f'{k}:{v}' for k, v in gg.most_common()))
