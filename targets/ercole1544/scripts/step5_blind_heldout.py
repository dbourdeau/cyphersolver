# Held-out score on an honest blind reading of c. 109r R01-R07 (validation/blind_0109_R01_R07.txt) against the clear c. 107.
# Letter table: validation/key_rebuilt_103_104.tsv (table-free rebuild from c. 103r/104r only), k set to z as in key_frozen because the rebuild has one
# vote on it. Code signs and nulls take the key_frozen values only. Measures: (1) share of decoded letters in matching runs of 3+ against c. 107,
# (2) letter signs agreeing under global DP. Controls: 200 shuffled tables for (1), 40 for (2).
import difflib
import random
import re
import sys
from lib import align, plain_text, is_letter
sys.stdout.reconfigure(encoding='utf8')
tab = {}
for l in open('validation/key_rebuilt_103_104.tsv', encoding='utf8'):
    if not l.startswith('#') and l.strip():
        f = l.rstrip('\n').split('\t')
        tab[f[0]] = f[1]
tab['k'] = 'z'
codes = {}
for l in open('key_frozen.tsv', encoding='utf8'):
    if not l.startswith('#') and l.strip():
        f = l.rstrip('\n').split('\t')
        if not (len(f[0]) == 1 and f[0].isalpha() and f[0] not in 'LS'):
            codes[f[0]] = f[1]
toks = []
for line in open('validation/blind_0109_R01_R07.txt', encoding='utf8'):
    if line.startswith('#') or not line.strip():
        continue
    toks += re.findall(r'L\^\w+|\d+|\?|[A-Za-z]', line.strip().partition(' ')[2])
clear_all = plain_text('transcription_0107.txt', skip_head=0)


def dec(t, ct):
    out = ''
    for x in t:
        if is_letter(x):
            out += ct.get(x, '?')
        else:
            v = codes.get(x, '')
            out += '' if v == 'null' else v.replace(' ', '') if x not in ('L',) else 'et'
    return out


def runs3(s, clear):
    sm = difflib.SequenceMatcher(None, s, clear, autojunk=False)
    return sum(m.size for m in sm.get_matching_blocks() if m.size >= 3) / max(1, len(s))


s0 = dec(toks, tab)
print(s0)
base = runs3(s0, clear_all)
rng = random.Random(1556)
letters = sorted(tab)
vals = [tab[k] for k in letters]
ctrl = []
for _ in range(200):
    v = vals[:]
    rng.shuffle(v)
    ctrl.append(runs3(dec(toks, dict(zip(letters, v))), clear_all))
print(f'decoded letters in runs of 3+: {base:.3f}; shuffled mean {sum(ctrl)/len(ctrl):.3f}, max {max(ctrl):.3f}')
# DP on the head of c. 107, where these lines sit, located by the best difflib window
sm = difflib.SequenceMatcher(None, s0, clear_all, autojunk=False)
m = max(sm.get_matching_blocks(), key=lambda b: b.size)
start = max(0, m.b - m.a - 40)
clear = clear_all[start:start + len(s0) + 120]


def score(ct):
    pairs, _ = align(toks, clear, ct)
    ok = n = 0
    for a, b in pairs:
        if a and is_letter(a):
            n += 1
            ok += b != '' and ct.get(a) == b
    return ok, n


ok, n = score(tab)
print(f'letter signs agreeing under DP: {ok}/{n} = {ok/n:.3f}')
c2 = []
for _ in range(40):
    v = vals[:]
    rng.shuffle(v)
    a, b = score(dict(zip(letters, v)))
    c2.append(a / b)
print(f'DP control, 40 shuffled tables: mean {sum(c2)/len(c2):.3f}, max {max(c2):.3f}')
