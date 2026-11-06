"""Give values to the signs the glossed sibling never pairs with a gloss, by language-model score over both bare letters.

    python refine.py       coordinate ascent over the free tokens; writes key_refined.tsv (key.tsv plus the new values)

Fixed: every token key.tsv values from three or more gloss pairs. Free: the rest (new signs of 252/142 such as {Hp},
{dbar}, {pbar}, and the rare ones). Each free token tries every letter, the doubled letters and the empty value; the value
that maximises the it-cinquecento 5-gram score of all cipher words of t252 + t142 (clear words kept as context) wins.
"""
import csv, os, string, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from build_key import merge

M = lm.load('it-cinquecento')
key, count = {}, {}
for r in csv.DictReader(open('key.tsv', encoding='utf-8'), delimiter='\t'):
    key[r['token']] = '' if r['value'] == '(null)' else r['value']
    count[r['token']] = int(r['count'])

lines = []
for f in ('t252.tsv', 't142.tsv'):
    cur, ln = [], None
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        if r['line'] != ln and cur:
            lines.append(cur); cur = []
        ln = r['line']
        if r['kind'] == 'C':
            cur.append(merge(r['text'].split()))
        elif r['kind'] == 'P':
            cur.append(r['text'])
    lines.append(cur)

toks = {t for L in lines for w in L if isinstance(w, list) for t in w}
free = sorted(t for t in toks if count.get(t, 0) < 3)
for t in free:
    key.setdefault(t, '')


def text():
    out = []
    for L in lines:
        out.append(' '.join(''.join(key.get(t, '') for t in w) if isinstance(w, list) else w for w in L))
    return lm.norm(' '.join(out), 'early')


def score():
    return M.per_char(text())


cands = list(string.ascii_lowercase) + ['tt', 'pp', 'll', 'ss', 'cc', 'ff', 'rr', 'mm', 'nn', 'ch', 'gl', 'gn', '']
best = score()
for rnd in range(3):
    changed = False
    for t in free:
        cur = key[t]
        for c in cands:
            key[t] = c
            s = score()
            if s > best + 1e-6:
                best, cur, changed = s, c, True
        key[t] = cur
    print(f'round {rnd}: score {best:.3f}', {t: key[t] for t in free})
    if not changed:
        break

with open('key_refined.tsv', 'w', encoding='utf-8') as f:
    f.write('token\tvalue\tsource\n')
    for t in sorted(key, key=lambda x: -count.get(x, 0)):
        src = f'gloss pairs ({count[t]})' if count.get(t, 0) >= 3 else 'LM fit over 252+142'
        f.write(f'{t}\t{key[t] or "(null)"}\t{src}\n')
print('-> key_refined.tsv')
