"""Decipher R1862 with the key rebuilt from R1874 (../r1874/key2.json) plus local overrides (key_over.json).

python decode.py            -> line-by-line plaintext, unknown groups in [brackets]
python decode.py --guess    -> for each unknown/weak group, rank candidate values by the Italian LM over all its occurrences
"""
import json, re, sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

HERE = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(HERE, '..', 'r1874', 'key2.json')))
KEY = {g: v[0] for g, v in base.items() if v[2] >= 2 or v[1] >= .8}
over_path = os.path.join(HERE, 'key_over.json')
OVER = json.load(open(over_path, encoding='utf8')) if os.path.exists(over_path) else {}
KEY.update({g: v for g, v in OVER.items() if not g.startswith('_')})
for g in OVER.get('_open', []):   # values the sibling alignment got from a mis-split stretch: treat as unread
    KEY.pop(g, None)


def lines():
    """Rows of tx/groups.txt. A group listed in key_over.json's _slips is the clerk's own miscoding:
    it keeps its written digits in the transcription and is read with the value he meant."""
    out = []
    for l in open(os.path.join(HERE, 'tx', 'groups.txt'), encoding='utf8'):
        m = re.match(r'(P\d L\d+[a-z]?):\s*(.*)', l)
        if not m:
            continue
        body = m.group(2)
        items = []
        for part in re.split(r'(\[CLEAR:[^\]]*\])', body):
            if part.startswith('[CLEAR'):
                items.append(('clear', part[7:-1].strip()))
            else:
                for g in part.split():
                    items.append(('g', re.sub(r'[?^]', '', g)))
        lab = m.group(1)
        gi = 0
        for k, (kind, v) in enumerate(items):
            if kind != 'g':
                continue
            s = SLIPS.get(f'{lab}:{gi}')
            if s:
                items[k] = ('g', s[0])
            gi += 1
        out.append((lab, items))
    return out


SLIPS = OVER.get('_slips', {})   # {"<line>:<index>": ["<group as the clerk should have written it>", "<value>"]}


def render(items, mark=True):
    s = []
    for kind, v in items:
        if kind == 'clear':
            s.append(' {' + v + '} ')
        elif v in KEY:
            s.append(KEY[v])
        else:
            s.append(f'[{v}]' if mark else '#')
    return ''.join(s)


if __name__ == '__main__':
    L = lines()
    if '--guess' not in sys.argv:
        for lab, items in L:
            print(lab, render(items))
        seq = [v for _, it in L for k, v in it if k == 'g']
        unk = collections.Counter(g for g in seq if g not in KEY)
        print(f'\n{len(seq)} groups, {len(set(seq))} types, {sum(unk.values())} unknown tokens in {len(unk)} types')
        print(unk.most_common())
    else:
        from lang import lm
        m = lm.load('it-cinquecento')
        seq = [(k, v) for _, it in L for k, v in it]
        unk = collections.Counter(v for k, v in seq if k == 'g' and v not in KEY)
        cons = ['', 'b', 'c', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'z', 'gn', 'gl', 'st', 'tr', 'pr', 'ss', 'nt']
        cands = sorted({c + v for c in cons for v in 'aeiou'} | set('bcdfglmnprstvz') |
                       {'che', 'con', 'per', 'non', 'il', 'et', 'del', 'nel', 'in', 'di', 'la', 'le', 'lo', 'sua', 'suo', 'se', 'si', 'ch', 'ss', 'nn', 'll'})
        for g, n in unk.most_common():
            ctxs = []
            for i, (k, v) in enumerate(seq):
                if k == 'g' and v == g:
                    left = ''.join(KEY.get(x, '#') for kk, x in seq[max(0, i - 8):i] if kk == 'g')
                    right = ''.join(KEY.get(x, '#') for kk, x in seq[i + 1:i + 9] if kk == 'g')
                    ctxs.append((left.split('#')[-1], right.split('#')[0]))
            sc = []
            for c in cands:
                tot = 0
                for a, b in ctxs:
                    t = lm.norm(a + c + b, 'early')
                    tot += m.per_char(t) * len(t) - m.per_char(lm.norm(a + b, 'early')) * len(lm.norm(a + b, 'early'))
                sc.append((tot / len(ctxs), c))
            sc.sort(reverse=True)
            print(g, n, ' '.join(f'{c}:{s:.1f}' for s, c in sc[:6]), '|', ctxs[0])
