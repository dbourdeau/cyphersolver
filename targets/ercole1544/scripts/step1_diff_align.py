# Diff of the two passes on c. 103r, sign inventory, alignment with c. 104r, sign-by-sign counts.
import collections, difflib, re, sys
from lib import *
sys.stdout.reconfigure(encoding='utf8')


def rows(p):
    return {l.split()[0]: ' '.join(l.split()[1:]) for l in open(p, encoding='utf8') if re.match(r'L\d\d ', l)}


a, b, c = rows('validation/transcription_0103r_pass1.txt'), rows('validation/transcription_0103r_pass2.txt'), rows('transcription_0103r.txt')
tot = dif = 0
print('--- pass1 vs pass2 ---')
for k in c:
    ta, tb = [re.findall(r'L\^\w+|\d+|\?|[A-Za-z]', x[k]) for x in (a, b)]
    tot += max(len(ta), len(tb))
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op != 'equal':
            dif += max(i2 - i1, j2 - j1)
            print(k, ' '.join(ta[i1:i2]) or '-', '|', ' '.join(tb[j1:j2]) or '-')
print('signs', tot, 'differing', dif)
T = [t for _, t in tokens('transcription_0103r.txt')]
inv = collections.Counter(T)
print('inventory', len(inv), inv.most_common())
pl = plain_text('transcription_0104r.txt')
pairs, sc = align(T, pl, L2P)
cnt = collections.defaultdict(collections.Counter)
for s, p in pairs:
    cnt[s][p] += 1
print('plain letters', len(pl), 'signs', len(T), 'score', sc)
for s in sorted(cnt, key=lambda x: (len(x) > 1 or x.isdigit(), x)):
    print(repr(s), cnt[s].most_common(8))
with open('validation/align_0103_0104.txt', 'w', encoding='utf8') as o:
    for s, p in pairs:
        o.write(f'{s}\t{p}\n')
print('mismatches:')
for k, (s, p) in enumerate(pairs):
    if s and is_letter(s) and L2P.get(s) != p:
        print(s, repr(p), ''.join(q for _, q in pairs[max(0, k - 6):k + 7]))
