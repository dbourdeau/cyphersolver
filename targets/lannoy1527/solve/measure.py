"""Measure the reading against the read bar: share of cipher tokens that are read as sense.

Aligns, run by run, the decode of solve/tokens.txt (key.tsv) with reading_aligned.txt (difflib, letters only).
A token is read when every letter it gives is matched in the reading inside a word that is not marked [?] and is not
an unvalued [group]. Frame marks (11, -o-, ny, and g# standing next to them or at a run's edge) are not counted.
Numbers written {/6/} count as read when the reading has them. A polyvalent sign (key value 'g/a') takes the
alternative that best fits the reading (greedy). Prints per-run and total counts and writes solve/measure_tokens.tsv.
"""
import os, re, difflib, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
key = {}
for l in open(os.path.join(ROOT, 'key.tsv'), encoding='utf-8'):
    if l.startswith('# ') or l.startswith('#S'): continue
    if '\t' in l: k, v = l.rstrip('\n').split('\t')[:2]; key[k] = v
MARK = {'11', '-o-', 'ny'}
norm = lambda s: s.lower().replace('v', 'u').replace('j', 'i').replace('_', '')


def runs(fn, comments=True):
    out = {}; cur = None
    for l in open(fn, encoding='utf-8'):
        if l.startswith('#00'): cur = l[1:].strip(); out[cur] = ''; continue
        if cur is None: continue
        if comments and l.startswith('# '): continue
        out[cur] += l.strip() + ' '
    return out


def vals(t):
    m = re.fullmatch(r'/(\d+)/', t)
    v = m.group(1) if m else key.get(t)
    return ['\x00'] if v is None else [norm(x) for x in v.rstrip('?').split('/')]


def reading_stream(text):
    R = []
    for w in re.findall(r'\{[^}]*\}|\[[^\]]*\]|[^\s|,.;:]+', text):
        if w.startswith('{'):
            m = re.fullmatch(r'\{/(\d+)/\}', w)
            R += [(c, True) for c in m.group(1)] if m else [('\x01', False)]
        elif w.startswith('['):
            R.append(('\x01', False))
        else:
            bad = '[' in w
            R += [(c, not bad) for c in norm(re.sub(r'\[\?\]|\{[^}]*\}', '', w))]
    return R


toks = {k: v.split() for k, v in runs(os.path.join(HERE, 'tokens.txt'), comments=False).items()}
read = runs(os.path.join(ROOT, 'reading_aligned.txt'))
rows = []; tot = collections.Counter()
for run, tk in toks.items():
    R = reading_stream(read.get(run, '')); Rs = ''.join(c for c, _ in R)
    counted = [not (t in MARK or (t == 'g#' and (i == 0 or i == len(tk) - 1 or tk[i - 1] in MARK or tk[i + 1] in MARK)))
               for i, t in enumerate(tk)]
    choice = {i: 0 for i, t in enumerate(tk) if counted[i] and len(vals(t)) > 1}

    def stream():
        return [(c, i) for i, t in enumerate(tk) if counted[i] for c in vals(t)[choice.get(i, 0)]]

    def align(D):
        return difflib.SequenceMatcher(None, ''.join(c for c, _ in D), Rs, autojunk=False)

    best = sum(n for *_, n in align(stream()).get_matching_blocks())
    for i in list(choice):
        for a in range(1, len(vals(tk[i]))):
            old = choice[i]; choice[i] = a
            s = sum(n for *_, n in align(stream()).get_matching_blocks())
            if s > best: best = s
            else: choice[i] = old
    D = stream(); ok = [False] * len(D)
    for a, b, n in align(D).get_matching_blocks():
        for j in range(n): ok[a + j] = R[b + j][1]
    per = collections.defaultdict(list)
    for (c, i), f in zip(D, ok): per[i].append(f)
    n_read = n_all = 0
    for i, t in enumerate(tk):
        if not counted[i]: continue
        r = bool(per.get(i)) and all(per[i])
        n_all += 1; n_read += r
        rows.append((t, vals(t)[choice.get(i, 0)] if t in key or re.fullmatch(r'/(\d+)/', t) else '', int(r), run))
    tot['read'] += n_read; tot['all'] += n_all
    print(f'{run:12s} {n_read:5d}/{n_all:5d} = {n_read / max(1, n_all):.3f}')
print(f'TOTAL        {tot["read"]:5d}/{tot["all"]:5d} = {tot["read"] / tot["all"]:.4f}')
with open(os.path.join(HERE, 'measure_tokens.tsv'), 'w', encoding='utf-8') as f:
    f.write('token\tvalue\tread\trun\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
with open(os.path.join(ROOT, 'validation.tsv'), 'w', encoding='utf-8') as f:
    f.write('# model: es-golden-age\n# source: solve/measure.py over solve/tokens.txt (frame marks dropped) with key.tsv, '
            'aligned to reading_aligned.txt\n# note: doubtful words [?], unvalued groups and signs and the numbers are '
            'unread (?); a polyvalent sign carries the value read here\n')
    for t, v, r, _ in rows:
        f.write(f'{t}\t{v if r and not re.fullmatch(r"/(\d+)/", t) else "?"}\n')
un =collections.Counter(t for t, v, r, _ in rows if not r)
print('unread tokens by type:', ' '.join(f'{k}:{v}' for k, v in un.most_common(40)))
