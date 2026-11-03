# Rebuild of the letter table from c. 103r / c. 104r ONLY, with no table as input.
# Method: take runs of plain letter signs between code signs on c. 103r. A run of 11+ signs is slid across the clear of c. 104r; a position is a hit
# if the run maps onto the clear one-to-one (same repeat pattern both ways). Unique hits vote for sign=letter. Majority gives the table.
# Writes validation/key_rebuilt_103_104.tsv and compares with key_frozen.tsv. Nothing from cc. 109, 107, 77-79 or 174-175 is read.
import collections
import re
import sys
from lib import plain_text
sys.stdout.reconfigure(encoding='utf8')


def runs(path):
    out = []
    cur = ''
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        body = line.strip().partition(' ')[2]
        for t in re.findall(r'L\^\w+|\d+|\?|[A-Za-z]', body):
            if len(t) == 1 and t.isalpha() and t not in 'LS':
                cur += t
            elif t in ('24', '25', '27'):   # nulls are not known to this script; they simply end a run
                out.append(cur)
                cur = ''
            else:
                out.append(cur)
                cur = ''
    out.append(cur)
    return [r for r in out if len(r) >= 11]


def iso(a, b):
    f = {}
    g = {}
    for x, y in zip(a, b):
        if f.setdefault(x, y) != y or g.setdefault(y, x) != x:
            return False
    return True


clear = plain_text('transcription_0104r.txt', skip_head=0)
R = runs('transcription_0103r.txt')
votes = collections.defaultdict(collections.Counter)
hits = letters = 0
for r in R:
    pos = [i for i in range(len(clear) - len(r) + 1) if iso(r, clear[i:i + len(r)])]
    if len(pos) == 1:
        hits += 1
        letters += len(r)
        for x, y in zip(r, clear[pos[0]:pos[0] + len(r)]):
            votes[x][y] += 1
print('runs of 11+:', len(R), 'unique hits:', hits, 'letters:', letters)
frozen = {}
for l in open('key_frozen.tsv', encoding='utf8'):
    if not l.startswith('#') and l.strip():
        f = l.rstrip('\n').split('\t')
        if len(f[0]) == 1 and f[0].isalpha():
            frozen[f[0]] = f[1]
agree = 0
with open('validation/key_rebuilt_103_104.tsv', 'w', encoding='utf8') as o:
    o.write('# sign\tplain\tvotes\tmixed\tfrozen\n')
    for s in sorted(votes):
        (p, n), = votes[s].most_common(1)
        rest = sum(votes[s].values()) - n
        o.write(f'{s}\t{p}\t{n}\t{rest}\t{frozen.get(s, "")}\n')
        print(s, p, n, rest, 'frozen', frozen.get(s), 'OK' if frozen.get(s) == p else 'DIFF')
        agree += frozen.get(s) == p
print('agree with key_frozen on', agree, 'of', len(votes), 'signs voted; not voted:', sorted(set(frozen) - set(votes)))
