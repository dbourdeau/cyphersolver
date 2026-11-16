"""Compare the ljs51 attack's transcription and values with the accepted transcription and key (qaysarani1350).

    python targets/qaysarani1350/ljs51_attack/compare_with_key.py      # prints, and writes compare_with_key.txt

Positions are aligned line by line (sign order); line 6 is aligned only for its first two words (the third word is
divided differently, 5 signs against 4). The attack's labels are arbitrary, so each label is matched to the accepted
sign it most often stands on (best fit): the 77 of 85 is a fitted figure, and labels used once agree trivially.
The attack's "firm" values are those its NOTES list under "Remaining gaps".
"""
import collections, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
KEY = json.load(open(os.path.join(PARENT, 'key.json'), encoding='utf-8'))['key']
FIRM = {'N': 'و', 'Y': 'م', 'K': 'ث', 'M': 'ل', 'A': 'ل', 'D': 'ه', 'P': 'ي', 'X': 'ض', 'F': 'ك', 'H': 'ا'}


def lines(path):
    return [m.group(2) for m in (re.match(r'L?(\d):\s*(.*)', l) for l in open(path, encoding='utf-8')) if m]


def toks(s):
    return re.findall(r'[A-Z8]', s.replace('[|]', ''))


acc = lines(os.path.join(PARENT, 'transcription.txt'))
att = lines(os.path.join(HERE, 'transcription.txt'))
out = []
pairs = []
for i, (x, y) in enumerate(zip(acc, att)):
    tq, ta = toks(x), toks(y)
    out.append(f'line {i + 1}: accepted {len(tq)} signs, attack {len(ta)}')
    if i == 5:
        tq, ta = tq[:8], ta[:8]
    pairs += list(zip(ta, tq))
fit = collections.defaultdict(collections.Counter)
for a, q in pairs:
    fit[a][q] += 1
agree = sum(c.most_common(1)[0][1] for c in fit.values())
once = sum(1 for c in fit.values() if sum(c.values()) == 1)
out.append(f'aligned positions {len(pairs)}; attack labels {len(fit)}; label -> best-fit accepted sign agrees at {agree} '
           f'({100 * agree / len(pairs):.0f}%), of which {once} are labels used once')
for a in sorted(fit):
    out.append(f'  {a} -> ' + ', '.join(f'{q} {KEY[q]} x{n}' for q, n in fit[a].most_common()))
firm = [(a, q) for a, q in pairs if a in FIRM]
ok = [(a, q) for a, q in firm if FIRM[a] == KEY[q]]
easy = [(a, q) for a, q in firm if a in 'HN']
easy_ok = [(a, q) for a, q in ok if a in 'HN']
out.append(f'attack firm values: {len(firm)} aligned positions carry one, {len(ok)} agree with key.json')
out.append(f'  alif and waw: {len(easy_ok)} of {len(easy)}; other firm signs: {len(ok) - len(easy_ok)} of {len(firm) - len(easy)}')
text = '\n'.join(out) + '\n'
print(text, end='')
open(os.path.join(HERE, 'compare_with_key.txt'), 'w', encoding='utf-8').write(text)
