"""For each unread cipher word, try look-alike readings of its signs (one or two swaps) and keep the variant that
decodes to a word attested in the 15th-16th c. Italian corpora (lang/cache it-renaissance + it-nunziature).
Prints candidates only: a variant is a hypothesis about the transcription, to be checked on the image."""
import collections, csv, itertools, re, sys
from build_key import merge
from decode import key
from measure import UNREAD

LOOK = [('s', '5'), ('x', 'y'), ('b', '6'), ('q', '4', '9'), ('o', '{sg}'), ('H', '#', '{Hp}'), ('r', 'z'), ('+', 't', '{dbar}'),
        ('n', 'u'), ('m', 'n'), ('d', 'o'), ('g', 's'), ('f', '4')]
alt = collections.defaultdict(set)
for grp in LOOK:
    for a in grp:
        alt[a] |= set(grp) - {a}
W = collections.Counter()
for f in ('../../lang/corpora/it-renaissance.txt', '../../lang/corpora/it-nunziature.txt'):
    t = open(f, encoding='utf-8', errors='ignore').read().lower().replace('j', 'i').replace('v', 'u')
    W.update(re.findall(r'[a-z]+', t))


def dec(toks):
    return ''.join(key.get(t, '?') for t in merge(toks)).replace('v', 'u')


for f, u in UNREAD.items():
    u = set(u.split())
    for row in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        k = f"{row['line']}.{row['pos']}"
        if row['kind'] != 'C' or k not in u:
            continue
        T = row['text'].split()
        best = []
        for nswap in (1, 2):
            for idx in itertools.combinations(range(len(T)), nswap):
                for subs in itertools.product(*[sorted(alt[T[i]]) for i in idx]):
                    T2 = list(T)
                    for i, s in zip(idx, subs): T2[i] = s
                    d = dec(T2)
                    if W[d] >= 20:
                        best.append((nswap, -W[d], d, ' '.join(T2)))
            if best: break
        best.sort()
        print(f, k, dec(T).upper(), '->', ', '.join(f'{d} ({-c})' for _, c, d, _ in best[:4]) or '-')
